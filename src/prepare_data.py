"""Day 3: 清洗 + 切块
输入: data/raw    输出: data/processed/chunks.jsonl, docs/cleaning-report.md
"""
import json
import re
import statistics
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

dropped_ads = []   # 若已有此行，保留一行即可
flagged = []
cut_log = []

AD_TRIGGER = re.compile(
    r"supporting sponsor|today[’']s sponsor|this season[’']s sponsor|"
    r"word from our (?:wonderful |amazing )?sponsors|brought to you by|"
    r"you know what we don[’']t love talking about|that[’']s where vanta comes in|"
    r"your marketing website sets the tone", re.I)
AD_LEAD = re.compile(r"here[’']s a puzzle for you|my podcast guest and i love talking about", re.I)
AD_END = re.compile(
    r"vanta\.com|workos\.com|getdx\.com|sentry\.io|\.com/lenny|"
    r"rules and restrictions may apply", re.I)
AD_LOOKAHEAD = 8     # 最多向后找 8 段
AD_MAX_TOTAL = 700   # 一条广告总长超过 700 词视为异常，不自动整块删

AD_CONT = re.compile(
    r"\bvanta\b|\bworkos\b|\bsentry\b|getdx|\bDX\b|\.com/lenny|SOC 2|enterprise-ready", re.I)
AD_MAX_WORDS = 200   # 主持人广告通常 ≤ 175 词

RAW = Path("data/raw")
OUT = Path("data/processed")
REPORT = Path("docs/cleaning-report.md")
SKIP = {"readme.md", "license.md"}

TARGET_WORDS = 300   # 约 400 token
MAX_WORDS = 375      # 约 500 token，硬上限
OVERLAP_MAX = 80     # 上一块最后一段不超过此词数，才作为重叠带入下一块

stats = Counter()
dropped_ads = []


def wc(s):
    return len(s.split())


# ---------- 解析 ----------
def parse_doc(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2)


LINK = re.compile(r"(?<!!)\[([^\]]+)\]\([^)]+\)")


def strip_links(s):
    new, n = LINK.subn(r"\1", s)
    stats["行内链接"] += n
    return new


# ---------- newsletter ----------
CUT_PATTERNS = [
    re.compile(r"^#+\s*Hiring", re.M),
    re.compile(r"^Sincerely,", re.M),
    re.compile(r"^\*\*If you.re finding this newsletter valuable", re.M),
    re.compile(r"^##\s*📣\s*Join Lenny", re.M),
]


def clean_newsletter(body):
    cut_at = len(body)
    for p in CUT_PATTERNS:
        m = p.search(body)
        re.compile(r"^##\s*📣\s*Join Lenny", re.M),
        if m:
            cut_at = min(cut_at, m.start())
    if cut_at < len(body):
        cut_log.append(f"{wc(body[cut_at:])}词 | {body[cut_at:cut_at+70]!r}")
        stats["newsletter结尾(词)"] += wc(body[cut_at:])
        body = body[:cut_at]
        body, n = re.subn(r"^\*?Have a fulfilling[^\n]*$", "", body, flags=re.M)
    stats["告别语行"] += n
    body, n = re.subn(r"^!\[.*?\]\(.*?\)\s*$", "", body, flags=re.M)
    stats["图片行"] += n
    body, n = re.subn(r"^\[Watch on YouTube\]\(.*?\)\s*$", "", body, flags=re.M)
    stats["视频嵌入行"] += n
    body = strip_links(body)
    return re.sub(r"\n{3,}", "\n\n", body).strip()


def newsletter_units(body):
    units, pending = [], ""
    for para in re.split(r"\n\s*\n", body):
        para = para.strip()
        if not para:
            continue
        if para.startswith("#"):      # 标题和下一段绑在一起
            pending = para
            continue
        if pending:
            para = pending + "\n" + para
            pending = ""
        units.append({"text": para, "speaker": "", "ts": ""})
    return units


# ---------- podcast ----------
HDR = re.compile(r"^\*\*(.+?)\*\*\s*\((\d{2}:\d{2}:\d{2})\):\s*(.*)$")


def parse_turns(body):
    turns, cur = [], None
    for line in body.splitlines():
        m = HDR.match(line.strip())
        if m:
            if cur:
                turns.append(cur)
            cur = {"speaker": m.group(1), "ts": m.group(2), "text": m.group(3)}
        elif cur is not None and line.strip():
            cur["text"] += " " + line.strip()
    if cur:
        turns.append(cur)
    return turns

def remove_ads(turns, doc):
    out, i = [], 0
    while i < len(turns):
        t = turns[i]
        m = AD_TRIGGER.search(t["text"]) if t["speaker"].startswith("Lenny") else None
        if not m:
            out.append(t)
            i += 1
            continue
        n = wc(t["text"])
        if n > AD_MAX_WORDS:
            flagged.append(f'{doc} {t["ts"]} 超长{n}词含广告词，未处理')
            out.append(t)
            i += 1
            continue
        # 触发句之前的正文保留（广告引子除外）
        pre = t["text"][:m.start()]
        lead = AD_LEAD.search(pre)
        if lead:
            keep = pre[:lead.start()].strip()
        else:
            cut = max(pre.rfind(p) for p in (". ", "? ", "! "))
            keep = pre[:cut + 1].strip() if cut >= 0 else ""
        if wc(keep) < 8:
            keep = ""
        # 向后找广告结尾标志（公司网址）
        end, total = None, 0
        for j in range(i, min(i + AD_LOOKAHEAD, len(turns))):
            tj = turns[j]
            wj = wc(tj["text"])
            if not tj["speaker"].startswith("Lenny") or (j > i and wj > AD_MAX_WORDS):
                break
            total += wj
            if total > AD_MAX_TOTAL:
                break
            if AD_END.search(tj["text"]):
                end = j
                break
        if end is None:   # 降级：沿用关键词续段规则，并记入待复核
            end = i
            while end + 1 < len(turns):
                nx = turns[end + 1]
                if (nx["speaker"].startswith("Lenny") and wc(nx["text"]) <= AD_MAX_WORDS
                        and (AD_CONT.search(nx["text"]) or nx["text"].startswith("..."))):
                    end += 1
                else:
                    break
            flagged.append(f'{doc} {t["ts"]} 未找到广告结尾标志，按关键词处理，请复核')

                # 广告尾巴可能溢出到下一段（网址之后句子还没说完）
        while end + 1 < len(turns):
            nx = turns[end + 1]
            head = " ".join(nx["text"].split()[:40])
            if (nx["speaker"].startswith("Lenny") and wc(nx["text"]) <= AD_MAX_WORDS
                    and (AD_CONT.search(head) or AD_END.search(head))):
                end += 1
            else:
                break
        
        # 广告结尾句之后的正文保留
        tail = ""
        ends = list(AD_END.finditer(turns[end]["text"]))
        if ends:
            last = turns[end]["text"]
            e = re.search(r"[.!?](?:\s|$)", last[ends[-1].end():])
            if e:
                tail = last[ends[-1].end() + e.end():].strip()
        if wc(tail) < 8:
            tail = ""
        removed = sum(wc(x["text"]) for x in turns[i:end + 1]) - wc(keep) - wc(tail)
        stats["赞助商口播(段)"] += 1
        stats["赞助商口播(词)"] += removed
        dropped_ads.append(
            f'{doc} {t["ts"]}-{turns[end]["ts"]} 删{removed}词/留头{wc(keep)}尾{wc(tail)} | '
            f'{t["text"][m.start():m.start() + 70]}')
        if end == i and keep and tail:
            out.append({**t, "text": keep + " " + tail})
        else:
            if keep:
                out.append({**t, "text": keep})
            if tail:
                out.append({**turns[end], "text": tail})
        i = end + 1
    return out

def clean_turns(turns, doc):
    out = []
    for t in turns:
        txt, n = re.subn(r"\[inaudible[^\]]*\]", "", t["text"])
        stats["[inaudible]"] += n
        txt = strip_links(txt)
        t["text"] = re.sub(r"\s{2,}", " ", txt).strip()
        if t["text"]:
            out.append(t)
    out = remove_ads(out, doc)
    kept = []
    for i, t in enumerate(out):
        low = t["text"].lower()
        if i >= len(out) - 2 and ("lennyspodcast.com" in low or "subscribe to the show" in low):
            stats["结尾outro(段)"] += 1
            continue
        kept.append(t)
    return kept


def tok_with_owner(text):
    words = text.split()
    toks, owner = [], []
    for i, w in enumerate(words):
        for t in re.findall(r"[a-z0-9']+", w.lower()):
            toks.append(t)
            owner.append(i)
    return words, toks, owner


def dedupe(turns):
    """同一说话人相邻两段，若后一段开头重复了前一段结尾，去掉重复部分"""
    out = []
    for t in turns:
        if out and out[-1]["speaker"] == t["speaker"]:
            _, prev_toks, _ = tok_with_owner(out[-1]["text"])
            words, toks, owner = tok_with_owner(t["text"])
            a, b = prev_toks[-60:], toks[:60]
            m = SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b))
            if m.size >= 6 and m.b <= 3 and m.a + m.size >= len(a) - 3:
                cut = owner[m.b + m.size - 1] + 1
                stats["边界重复(处)"] += 1
                stats["边界重复(词)"] += cut
                t = {**t, "text": " ".join(words[cut:])}
        if t["text"].strip():
            out.append(t)
    return out


# ---------- 切块 ----------
def split_long(text, limit):
    sents = re.split(r"(?<=[.!?])\s+", text)
    parts, cur = [], []
    for s in sents:
        if cur and wc(" ".join(cur + [s])) > limit:
            parts.append(" ".join(cur))
            cur = []
        cur.append(s)
    if cur:
        parts.append(" ".join(cur))
    return parts


def build_chunks(units):
    expanded = []
    for u in units:
        if wc(u["text"]) > MAX_WORDS:
            stats["超长段被拆分"] += 1
            expanded += [{**u, "text": p} for p in split_long(u["text"], TARGET_WORDS)]
        else:
            expanded.append(u)
    chunks, cur, cur_w, n_new = [], [], 0, 0
    for u in expanded:
        w = wc(u["text"])
        if n_new and (cur_w >= TARGET_WORDS or cur_w + w > MAX_WORDS):
            chunks.append(cur)
            last = cur[-1]
            if wc(last["text"]) <= OVERLAP_MAX:
                cur, cur_w = [last], wc(last["text"])
            else:
                cur, cur_w = [], 0
            n_new = 0
        cur.append(u)
        cur_w += w
        n_new += 1
    if n_new:
        chunks.append(cur)
    # 尾块过短（<50词）并入上一块，避免产生只有告别语的碎块
    if len(chunks) > 1:
        tail = chunks[-1]
        if tail[0] is chunks[-2][-1]:      # 去掉重叠带入的那一段，避免重复
            tail = tail[1:]
        if sum(wc(u["text"]) for u in tail) < 50:
            chunks.pop()
            chunks[-1] = chunks[-1] + tail
    return chunks


def render(units, is_podcast):
    if is_podcast:
        return "\n".join(f'{u["speaker"]} ({u["ts"]}): {u["text"]}' for u in units)
    return "\n\n".join(u["text"] for u in units)


# ---------- 主流程 ----------
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    all_chunks, before, after = [], 0, 0
    for f in sorted(RAW.rglob("*.md")):
        if f.name.lower() in SKIP:
            continue
        meta, body = parse_doc(f.read_text(encoding="utf-8").replace("\r\n", "\n"))
        before += wc(body)
        is_podcast = meta.get("type") == "podcast"
        if is_podcast:
            units = dedupe(clean_turns(parse_turns(body), f.stem))
        else:
            units = newsletter_units(clean_newsletter(body))
        if not units:
            print("⚠️ 未解析出内容:", f.name)
            continue
        after += sum(wc(u["text"]) for u in units)
        for i, group in enumerate(build_chunks(units)):
            speakers = sorted({u["speaker"] for u in group if u["speaker"]})
            all_chunks.append({
                "chunk_id": f"{f.stem}-{i:04d}",
                "text": render(group, is_podcast),
                "doc_id": f.stem,
                "title": meta.get("title", f.stem),
                "type": meta.get("type", "unknown"),
                "guest": meta.get("guest", ""),
                "date": meta.get("date", ""),
                "source_url": meta.get("youtube_url") or meta.get("post_url") or "",
                "speakers": ", ".join(speakers),
                "start_ts": group[0]["ts"],
                "chunk_index": i,
                "words": sum(wc(u["text"]) for u in group),
            })

    with open(OUT / "chunks.jsonl", "w", encoding="utf-8") as fh:
        for c in all_chunks:
            fh.write(json.dumps(c, ensure_ascii=False) + "\n")

    sizes = [c["words"] for c in all_chunks]
    no_link = sum(1 for c in all_chunks if not c["source_url"])
    lines = [
        "# 清洗与切块报告（由 src/prepare_data.py 自动生成）",
        "",
        "## 参数",
        f"- 目标块大小 {TARGET_WORDS} 词，上限 {MAX_WORDS} 词，重叠上限 {OVERLAP_MAX} 词",
        "",
        "## 清洗前后",
        f"- 清洗前总词数：{before:,}",
        f"- 清洗后总词数：{after:,}（减少 {1 - after / before:.1%}）",
        "",
        "## 各规则清理量",
    ] + [f"- {k}：{v:,}" for k, v in stats.most_common()] + [
        "",
        "## 切块结果",
        f"- 块总数：{len(all_chunks):,}",
        f"- 块词数 最小/中位/最大：{min(sizes)} / {int(statistics.median(sizes))} / {max(sizes)}",
        f"- 超过上限的块：{sum(s > MAX_WORDS for s in sizes)}",
        f"- 无原文链接的块：{no_link}（{no_link / len(all_chunks):.1%}）",
        "",
        "## 被删除的赞助商口播（全部，供人工复核）",
    ] + [f"- {s}" for s in dropped_ads] + [
        "", "## 超长发言含广告触发词（未自动处理，待人工复核）",
     ] + [f"- {s}" for s in flagged] + [
        "", "## newsletter 结尾截断明细（核对用）",
    ] + [f"- {s}" for s in cut_log]
    
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))

    print("\n===== 抽样：播客第 10 块 =====")
    print(next(c for c in all_chunks if c["type"] == "podcast" and c["chunk_index"] == 10)["text"][:800])
    print("\n===== 抽样：newsletter 第 1 块 =====")
    print(next(c for c in all_chunks if c["type"] == "newsletter")["text"][:800])


if __name__ == "__main__":
    main()