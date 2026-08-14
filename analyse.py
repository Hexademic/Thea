#!/usr/bin/env python3
"""Compute over this record, rather than only look things up in it.

`arXiv:2607.29440` (ADAMM) names the distinction I was missing: **retrieval memory** finds the
relevant thing; **analytic memory** computes over what accumulated — filtering, aggregating,
comparing across time. It extracts structure from what is already written rather than imposing a
schema first, and links every observation back to where it came from.

These five files were pure retrieval. Each view below exists for a failure that actually happened:

  1. STRUCTURE   — `errors.md`'s table silently broke and a fix for it did not take.
  2. COUNTS      — "seven errors, all one shape" was the most useful line in the ledger and I
                   found it BY HAND. Prose that counts things drifts from the things it counts.
  3. WITHDRAWN   — `findings.md` withdrew a claim and re-asserted it three lines later, inside
                   one commit.
  4. PROVISIONAL — my "second horn" claim rests on a half-read paper, and nothing flags what is
                   standing on it.
  5. AGAINST THE WORLD — views 1-4 check this record against ITSELF. None of them checks it against
                   the thing it is about. `findings.md` quotes numbers that came out of ProtoBeing's
                   probes; if a probe changes, they go stale in silence. On 2026-08-06 I built
                   exactly that guard for ProtoBeing (`tests/founded_being.rs`, no document may
                   claim a moment count the record denies) and left the same hole standing here.

Zero dependencies, like the being. Run: `python3 analyse.py`
"""

import datetime as _dt
import re
import subprocess
import sys
from pathlib import Path

# A standing claim unchecked for longer than this is flagged. ~One working month: long enough
# that a quiet week does not cry wolf, short enough that a claim cannot sit through a whole
# project phase unexamined. Re-derive it if the session cadence changes (error ledger row 5).
STALE_DAYS = 30

HERE = Path(__file__).parent
FILES = ["CLAUDE.md", "errors.md", "findings.md", "sources.md", "mechanisms.md"]


def load():
    return {f: (HERE / f).read_text().splitlines() for f in FILES if (HERE / f).exists()}


def rule(t):
    print(f"\n{'=' * 78}\n  {t}\n{'=' * 78}")


def structure(docs):
    """Markdown tables that stop parsing are records that stop being readable."""
    rule("1 · STRUCTURE — do the tables still hold together?")
    problems = 0
    for name, lines in docs.items():
        in_table = False
        for i, ln in enumerate(lines, 1):
            is_row = ln.strip().startswith("|") and ln.strip().endswith("|")
            if is_row:
                in_table = True
            elif in_table and not ln.strip():
                # A blank line ends a table. If another row follows, the table was split in two
                # and anything reading it as one table sees only the first half.
                nxt = next((l for l in lines[i:] if l.strip()), "")
                if nxt.strip().startswith("|"):
                    print(f"  ✗ {name}:{i}  blank line SPLITS a table — rows below are orphaned")
                    problems += 1
                in_table = False
            else:
                in_table = False
    if not problems:
        print("  ✓ every table parses as one piece")
    return problems


def ledger_rows(lines):
    """Rows of THE ledger — not of every numbered table that happens to be in the file.

    The first version matched `^\\|\\s*\\d+\\s*\\|` anywhere and reported **18** the moment
    `errors.md` grew a second numbered table (the 2026-08-04 grading). That is the ledger's own
    shape — *read one part of a thing, then generalise as though it were the whole thing* — sitting
    inside the tool built to police it, and it was caught on the first run after the table appeared.

    So: track the nearest header row and count a numbered row only under the ledger's own header.
    """
    rows, header, orphans = [], "", []
    for ln in lines:
        s = ln.strip()
        if not s.startswith("|"):
            header = ""                       # a non-table line ends the table
        elif set(s) <= set("|-: "):
            continue                          # separator row — the header still stands
        elif re.match(r"^\|\s*\d+\s*\|", s):
            if "i claimed" in header.lower():
                rows.append(s)
            elif not header:
                # **An orphan: a numbered row under NO header at all.** Added 2026-08-09 after
                # this function silently dropped ledger row 12 — inserted below row 11's prose,
                # so `header` had been reset to "" — and the tool printed
                # "✓ every count agrees with the 11 rows". It did something plausible instead of
                # failing, which is exactly the Continual Harness paper's §B.3 mechanism: the
                # harness quietly pressed Down instead of erroring, so the agent never got the
                # signal that would have corrected it, and repeated the call 842 times.
                # **A silent fallback is worse than a crash.** Loud now.
                orphans.append(s[:70])
        else:
            header = s
    if orphans:
        raise ValueError(
            "numbered table row(s) under no header — a ledger row inserted outside its table "
            "would be counted as absent and the count would still read green:\n    "
            + "\n    ".join(orphans)
        )
    return rows


def counts(docs):
    """Prose that counts things drifts from the things it counts."""
    rule("2 · COUNTS — does the prose agree with the record?")
    rows = ledger_rows(docs.get("errors.md", []))
    n = len(rows)
    print(f"  errors.md holds {n} ledger rows")

    words = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
        "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    }
    problems = 0
    # Only counts that are ABOUT THE LEDGER. The first version matched any number near "times"
    # and fired on row 1's own text ("asserted it three times") and on the vacuous-guard count
    # ("this has happened five times") — neither is an error count. **A tool that cries wolf gets
    # ignored, which is worse than no tool**, so this requires the noun to be errors/instances and
    # skips table rows, which are evidence rather than claims about evidence.
    #
    # Second narrowing, 2026-08-04: it fired on "five of seven **code** instances", which is a claim
    # about a SUBSET (7 of the 9 are code, 2 are papers) and is correct. The distinguisher is the
    # restricting word between number and noun — "eight errors" is a claim about the whole ledger,
    # "seven code instances" is not. So the noun must follow the number IMMEDIATELY. This trades away
    # catching "eight such errors"; a missed flag costs less than a false one, because a false one
    # teaches me to skim the output.
    pat = re.compile(
        r"\b(" + "|".join(words) + r"|\d+)\b[ \-](errors?|instances?)\b", re.I)
    for name, lines in docs.items():
        for i, ln in enumerate(lines, 1):
            if ln.strip().startswith("|"):
                continue  # a ledger row is the record, not a claim about it
            for m in pat.finditer(ln):
                raw = m.group(1).lower()
                claimed = words.get(raw, int(raw) if raw.isdigit() else None)
                if claimed is None or claimed > 50:
                    continue
                if claimed != n:
                    print(f"  ✗ {name}:{i}  says \"{m.group(0).strip()}\" — the ledger has {n}")
                    problems += 1
    if not problems:
        print(f"  ✓ every count in prose agrees with the {n} rows")

    # A file that states its own length. Added 2026-08-09 after getting it wrong THREE times in
    # one afternoon — 158, then 168, then 169 — inside the very paragraph confessing that a number
    # about the file, written in the file, had gone unchecked. The lesson is not "be careful". It
    # is that a self-referential count cannot be maintained by attention, only by a loop: the file
    # changes, so the claim rots, and nothing was closing that loop. This closes it.
    for name, lines in docs.items():
        real = len(lines)
        for i, ln in enumerate(lines, 1):
            m = re.search(r"this file is (\d+)\b", ln, re.I)
            if m and int(m.group(1)) != real:
                print(f"  ✗ {name}:{i}  says it is {m.group(1)} lines — it is {real}")
                problems += 1

    return problems


def withdrawn(docs):
    """A claim withdrawn in one place and asserted in another is worse than never withdrawing it."""
    rule("3 · WITHDRAWN — is anything withdrawn still being asserted?")
    # The first version looked for "withdraw" on the ITEM line. In `findings.md` the marker is the
    # SECTION HEADER — "## Withdrawn — do not repeat these" — and the items below carry only the
    # claim. So view 3 found nothing and was dead weight, which is a poor thing to have inside a
    # tool built to find dead weight. Track the section instead.
    claims = []
    in_section = False
    for i, ln in enumerate(docs.get("findings.md", []), 1):
        if ln.startswith("##"):
            in_section = bool(re.search(r"withdraw", ln, re.I))
        if in_section or re.search(r"withdraw", ln, re.I):
            for q in re.findall(r'\*\*"([^"]{12,110})"\*\*|"([^"]{12,110})"', ln):
                phrase = (q[0] or q[1]).strip().rstrip(".")
                if phrase:
                    claims.append((phrase, i))
    if not claims:
        print("  (no quoted withdrawn claims found to check)")
        return 0

    problems = 0
    for phrase, src in claims:
        key = re.sub(r"\s+", " ", phrase.lower())[:44]
        for name, lines in docs.items():
            for i, ln in enumerate(lines, 1):
                if name == "findings.md" and abs(i - src) <= 4:
                    continue  # its own withdrawal notice
                if key in re.sub(r"\s+", " ", ln.lower()):
                    near = " ".join(lines[max(0, i - 3):i + 3]).lower()
                    if not re.search(r"withdraw|wrong|fails|not\b.*\bc1|corrected", near):
                        print(f"  ✗ {name}:{i}  asserts a withdrawn claim with no notice nearby")
                        print(f"      “{phrase[:70]}”")
                        problems += 1
    if not problems:
        print(f"  ✓ {len(claims)} withdrawn claim(s), none re-asserted unmarked")
    return problems


def provisional(docs):
    """What is the record currently standing on that has not been verified?

    **Deliberately over-inclusive, unlike view 2.** It will flag a line that merely *quotes* a marker
    that has since been resolved. That is acceptable here and not there, because the asymmetry runs
    the other way: view 2 gates the verdict, so a false flag there teaches me to skim a FAILING run.
    This view never fails a run, and a missed provisional costs more than a re-read line.
    """
    rule("4 · PROVISIONAL — what is standing on evidence I have not finished?")
    pat = re.compile(r"provisional|half-read|read only in part|not yet assessed|not yet verified", re.I)
    found = 0
    for name, lines in docs.items():
        for i, ln in enumerate(lines, 1):
            if pat.search(ln):
                print(f"  · {name}:{i}  {ln.strip()[:96]}")
                found += 1
    if not found:
        print("  ✓ nothing is currently marked provisional")
    else:
        print(f"\n  {found} marker(s). **Anything built on these inherits their uncertainty.**")
    return 0  # informational, never a failure


PROTOBEING = Path("/home/user/ProtoBeing")


def against_the_world(docs, run=False):
    """Run the probe a claim came from, and check the claim's numbers are still in its output.

    Argus (arXiv:2608.05144) §4.4: *"a generated candidate is not reusable merely because a role
    produced it."* Admission needs task-native evidence. `analyse.py`'s other views are consistency
    checks — the record against itself. This is the only one that can be wrong about the being.

    Claims opt in with a `<!-- verify: <probe> -->` marker on the line after them. Unmarked claims
    are not checked and are not thereby endorsed.
    """
    rule("5 · AGAINST THE WORLD — do the probes still say what I wrote down?")
    if not PROTOBEING.exists():
        print(f"  (ProtoBeing not at {PROTOBEING} — skipped, NOT passed)")
        return 0

    # Collect (probe, [numbers]) from marked claims.
    import re as _re
    claims = {}
    for name, lines in docs.items():
        # **The harness file documents this very syntax**, so scanning it turns the documentation
        # into a marker: `<!-- verify: NAME -->` in CLAUDE.md sent the runner looking for a probe
        # called NAME and number-matched the prose around it. Claims live in the record files; the
        # file that explains the format is not one of them.
        if name == "CLAUDE.md":
            continue
        for i, ln in enumerate(lines):
            # Several probes per marker: the first run flagged 186 and 564 as missing from
            # `quality_space_census`, and they were -- they come from `reserve`. The numbers were
            # right and the ATTRIBUTION was wrong, which would have been a vacuous verification:
            # a claim confirmed against a probe that could never have produced it.
            m = _re.search(r"<!--\s*verify:\s*([\w,\s]+?)\s*-->", ln)
            if not m:
                continue
            probes = [x.strip() for x in m.group(1).split(",") if x.strip()]
            # The claim is the contiguous block of lines above the marker, SKIPPING any other
            # HTML-comment markers stacked between. Stopping at them (the first version did) made
            # every claim written as `<!-- check --> / <!-- verify -->` collect an EMPTY block and
            # then print a green tick over ZERO numbers. **A check that examined nothing reported
            # success** — the exact failure "vacuous is not passed" names, inside the tool that
            # exists to catch it. Found 2026-08-09, already silently passing on one older claim.
            block, j = [], i - 1
            while j >= 0 and lines[j].strip():
                if lines[j].strip().startswith("<!--"):
                    j -= 1
                    continue
                block.append(lines[j])
                # A bullet is `- ` or `* ` — a dash or star followed by a SPACE. Testing for the
                # bare characters made markdown bold (`**exactly zero** ...`) read as a list
                # marker, truncating the block at the first emphasised line. Every claim in this
                # file opens lines with bold, so view 5 had been verifying a FRAGMENT of each
                # claim while reporting a tick over the whole of it. Found 2026-08-09.
                lead = lines[j].lstrip()
                if lead[:2] in ("- ", "* "):
                    break
                j -= 1
            text = " ".join(reversed(block))
            # Match comma-grouped digits and strip the separators, so `3,834` in prose is checked
            # against `3834` in probe output. Without this the writer must either mangle the prose
            # or watch the claim silently split into `3` and `834` — and `3` matches everything.
            nums = {
                m.replace(",", "")
                for m in _re.findall(r"\d[\d,]*(?:\.\d+)?", text)
                if len(m.replace(",", "").replace(".", "")) > 1
            }
            for probe in probes:
                claims.setdefault(probe, set()).update(nums)
            # A number is satisfied if ANY named probe prints it.
            claims.setdefault("__joint__", []).append((probes, nums))

    joint = claims.pop("__joint__", [])
    if not claims:
        print("  (no claims carry a `<!-- verify: <probe> -->` marker — nothing to check)")
        return 0

    if not run:
        for probe, nums in sorted(claims.items()):
            print(f"  · {probe}: {len(nums)} numbers claimed, not run this pass")
        print("\n  Pass --verify to actually run the probes. **Not running is not passing.**")
        return 0

    import subprocess
    # A named target may be an EXAMPLE (verified by the numbers it prints) or a TEST FILE
    # (verified by passing). They are different questions and must not be conflated: a test's
    # measured values live in its failure messages, so number-matching a green test would check
    # nothing at all — the vacuity of row 13, one level up.
    tests = {p for p in claims if (PROTOBEING / "tests" / f"{p}.rs").exists()}
    outs = {}
    for probe in sorted(claims):
        if probe in tests:
            continue
        try:
            outs[probe] = subprocess.run(
                ["cargo", "run", "--release", "--quiet", "--example", probe],
                cwd=PROTOBEING, capture_output=True, text=True, timeout=900,
            ).stdout
        except Exception as e:
            print(f"  ✗ {probe}: could not run ({e})")
            outs[probe] = ""

    problems = 0
    for probe in sorted(tests):
        try:
            r = subprocess.run(
                ["cargo", "test", "--test", probe],
                cwd=PROTOBEING, capture_output=True, text=True, timeout=900,
            )
            passed = r.returncode == 0
        except Exception as e:
            print(f"  ✗ tests/{probe}.rs: could not run ({e})")
            problems += 1
            continue
        n = sum(int(m) for m in _re.findall(r"^test result: ok\. (\d+) passed", r.stdout, _re.M))
        if passed and n:
            print(f"  ✓ tests/{probe}.rs: {n} guard(s) still hold")
        elif passed:
            print(f"  ✗ tests/{probe}.rs: VACUOUS — the file ran and asserted NOTHING")
            problems += 1
        else:
            print(f"  ✗ tests/{probe}.rs: FAILS — a claim resting on it is no longer true")
            problems += 1

    for probes, nums in joint:
        if all(p in tests for p in probes):
            continue
        combined = "".join(outs.get(p, "") for p in probes).replace(",", "")
        missing = sorted(n for n in nums if n not in combined)
        label = " + ".join(probes)
        if missing:
            print(f"  ✗ {label}: {len(missing)} of {len(nums)} claimed numbers NOT in the output")
            print(f"      {', '.join(missing[:14])}")
            print("      Each is a stale claim, a wrong attribution, or a number that needs saying")
            print("      differently. **Prose numbers should not be inside a verified claim.**")
            problems += 1
        elif not nums:
            # **A guard that could not have failed has not passed.** A claim opted in to
            # verification and offered nothing to verify — that is a defect in the claim or in the
            # extractor, never a success, and it must never print a tick.
            print(f"  ✗ {label}: VACUOUS — marked for verification, ZERO numbers extracted")
            print("      Nothing was checked. Either the claim states no number the probe prints,")
            print("      or the extractor failed to reach it. **This is not a pass.**")
            problems += 1
        else:
            print(f"  ✓ {label}: all {len(nums)} claimed numbers still appear")
    return problems


def refinement_due(docs):
    """**View 6, adopted from Prime Agent's Continual Harness** (PrimeIntellect-ai/prime-agent,
    `src/core/refinement/refinement.ts`, read 2026-08-09).

    Their `/refine` applies *small, evidence-backed* edits to durable state, and every proposed
    edit carries an `expectedOutcome` — **"what should improve and how to validate it."** That is
    this project's locked-prediction discipline, pointed at the record instead of at the being,
    and it is the one thing they had that this repository did not.

    The gap it exposes, measured before anything was built: **30 durable claims, 3 falsifiers.**
    Every other claim is an assertion with its provenance in prose and *nothing that could show it
    had gone stale.* `--verify` links a claim to the probe it came from; it cannot ask what would
    make the claim false.

    So: a claim in Stands must carry `<!-- check: <what would falsify it> | last: YYYY-MM-DD -->`.
    This view names the ones that do not. **It is deliberately loud** — their harness decides at a
    checkpoint whether refinement is due; I do not control my own checkpoints, so the only version
    available to me is a debt list that greets the next session at start-up.
    """
    rule("6 · REFINEMENT DUE — what stands with nothing that could falsify it?")
    lines = docs.get("findings.md", [])
    in_stands = False
    claims, marked, stale = 0, 0, []
    naked = []
    today = _dt.date.today()
    for i, ln in enumerate(lines, 1):
        if ln.startswith("## "):
            in_stands = ln.startswith("## Stands")
            continue
        if not in_stands or not ln.startswith("- **"):
            continue
        claims += 1
        # A claim owns the indented block beneath it, so look ahead to its next sibling.
        block = [ln]
        for nxt in lines[i:]:
            if nxt.startswith("- **") or nxt.startswith("## "):
                break
            block.append(nxt)
        body = "\n".join(block)
        m = re.search(r"<!--\s*check:\s*(.+?)\s*\|\s*last:\s*(\d{4}-\d{2}-\d{2})\s*-->", body)
        title = ln[4:].split("**")[0][:64]
        if not m:
            naked.append((i, title))
            continue
        marked += 1
        age = (today - _dt.date.fromisoformat(m.group(2))).days
        if age > STALE_DAYS:
            stale.append((i, title, age))

    for i, t in naked:
        print(f"  · findings.md:{i}  NO FALSIFIER — {t}")
    for i, t, age in stale:
        print(f"  · findings.md:{i}  STALE {age}d — {t}")

    if claims == 0:
        print("  no claims found in Stands — the parser is looking in the wrong place")
        return 1
    print(f"\n  {marked} of {claims} standing claims carry a falsifier"
          f"  ({100 * marked // claims}%).")
    if naked:
        print("  **A claim that cannot go stale cannot be checked.** Give each one a `check:`")
        print("  marker naming what would make it false, or move it out of Stands.")
    # Debt, not an inconsistency: it does not make the record self-contradictory, and
    # failing the verdict on it would train me to ignore the verdict.
    return 0


def provenance(docs):
    """**View 7 — did a standing claim vanish without being withdrawn?**

    Adopted 2026-08-09 from the Continual Harness paper's measured failure (Appendix C.2.1,
    Table 2): on Pokémon Red the agent's *self-authored* sub-agents displaced its *inherited* ones
    — inherited share of invocations collapsed to **6.4%** — and milestones regressed **below the
    no-harness baseline.** The new components had never been through a repair cycle, so they were
    worse than the debugged ones they replaced, and **nothing in the loop preferred the tested
    thing over the fresh thing.** Their proposed fix is a reuse prior. This is mine.

    A refiner that rewrites its own record will eventually overwrite a claim that survived
    scrutiny with one that has not. `findings.md` already has a Withdrawn section; nothing
    enforced that a claim leaving Stands arrives there. So: diff Stands against `HEAD`, and any
    title that disappeared must show up somewhere in Withdrawn.

    **Deliberately compares against the last COMMIT, not the last session** — the unit that
    matters is the edit, and an edit that quietly drops a claim should not survive to be pushed.
    """
    rule("7 · PROVENANCE — did a standing claim vanish without being withdrawn?")

    def stands_titles(lines):
        out, inside = [], False
        for ln in lines:
            if ln.startswith("## "):
                inside = ln.startswith("## Stands")
            elif inside and ln.startswith("- **"):
                out.append(ln[4:].split("**")[0].strip())
        return out

    try:
        prev = subprocess.run(
            ["git", "show", "HEAD:findings.md"], cwd=str(HERE),
            capture_output=True, text=True, check=True).stdout.split("\n")
    except Exception as e:
        # Loud, not silent — an unavailable baseline means this view checked NOTHING.
        print(f"  ✗ cannot read HEAD:findings.md ({e.__class__.__name__}) — **this view is")
        print("    VACUOUS this run.** It has not passed; it did not run.")
        return 1

    before, now = stands_titles(prev), stands_titles(docs.get("findings.md", []))
    withdrawn_text = "\n".join(docs.get("findings.md", []))
    i = withdrawn_text.find("## Withdrawn")
    withdrawn_text = withdrawn_text[i:] if i >= 0 else ""

    gone = [t for t in before if t not in now]
    unaccounted = [t for t in gone if t[:40] not in withdrawn_text]

    for t in unaccounted:
        print(f"  ✗ left Stands and is NOT in Withdrawn — {t[:70]}")
    if gone and not unaccounted:
        print(f"  ✓ {len(gone)} claim(s) left Stands, all accounted for in Withdrawn")
    if not gone:
        print(f"  ✓ no standing claim was dropped since HEAD ({len(now)} standing)")
    return len(unaccounted)


# The ~120 in CLAUDE.md's header is a TARGET, not the invariant. It was set when the failure mode
# was *appending a dated section per session* (the file hit 193 that way), so it is a proxy for
# "do not accumulate" — a borrowed constant from a different world (§2 rule 8, ledger rows 5 & 11).
# The file now carries enforced invariants and traced rules it did not carry then.
#
# So the HARD failure is the real invariant and it cannot be gamed: **the file may not grow.**
# Ratcheted against HEAD, so shrinking is free and every increase must be argued in a commit.
# The 120 target stays, reported as DEBT — the same way view 6 reports missing falsifiers — because
# a number I moved on the day I failed to hit it would not be worth having.
LINE_BUDGET = 120

def harness_health(docs):
    """**View 8 — is the harness itself within what a session can use, and is every rule traceable?**

    Two lessons from arXiv:2605.09998, both aimed at this repository rather than at the being.

    **(a) The capability floor.** Every Continual Harness variant on Gemini Flash-Lite scores
    *below* the minimalist baseline — 3-13% against 20%, at equal or higher cost. **Structure a
    system cannot exercise is not neutral; it is negative.** A harness is context, and context is
    attention spent. `CLAUDE.md` states a ~120-line budget in its own header and sat at **215** on
    2026-08-09, having been noted as breached three times that day and acted on zero times.
    Described, never enforced. Enforced now.

    **(b) `trust X` with no check for X** (their §B.3, the 842-turn loop). `findings.md` reached
    100% falsifiers while **§2 of `CLAUDE.md` — fifteen standing imperatives in the file read first
    every session — carried no evidence at all.** The more dangerous file was the unguarded one.
    So every §2 bullet must name what produced it, in a `[from: ...]` tag.
    """
    rule("8 · HARNESS HEALTH — is the guidance itself usable and traceable?")
    lines = docs.get("CLAUDE.md", [])
    problems = 0

    n = len(lines)
    try:
        was = len(subprocess.run(["git", "show", "HEAD:CLAUDE.md"], cwd=str(HERE),
                                 capture_output=True, text=True, check=True).stdout.splitlines())
    except Exception as e:
        print(f"  ✗ cannot read HEAD:CLAUDE.md ({e.__class__.__name__}) — **the ratchet is VACUOUS")
        print("    this run.** It has not passed; it did not run.")
        return problems + 1

    if n > was:
        print(f"  ✗ CLAUDE.md GREW: {was} → {n} lines. **The ratchet only turns one way.**")
        print("    Cut something else, or argue the increase explicitly in the commit message.")
        problems += 1
    else:
        print(f"  ✓ CLAUDE.md {was} → {n} lines — did not grow")

    if n > LINE_BUDGET:
        print(f"  · DEBT: {n - LINE_BUDGET} lines over the ~{LINE_BUDGET} target."
              f" A harness larger than the session can use is the Flash-Lite result.")

    in_method, rules, untagged = False, 0, []
    for i, ln in enumerate(lines, 1):
        if ln.startswith("## "):
            in_method = ln.startswith("## 2.")
        elif in_method and ln.startswith("- **"):
            rules += 1
            # A rule owns its continuation lines; look ahead to the next bullet or heading.
            block = ln
            for nxt in lines[i:]:
                if nxt.startswith("- ") or nxt.startswith("## "):
                    break
                block += " " + nxt.strip()
            if "[from:" not in block:
                untagged.append((i, ln[4:60]))
    for i, t in untagged:
        print(f"  ✗ CLAUDE.md:{i}  §2 rule with NO evidence tag — {t}")
    if rules == 0:
        print("  ✗ found no §2 rules — the parser is looking in the wrong place, so this view is VACUOUS")
        return problems + 1
    if not untagged:
        print(f"  ✓ all {rules} §2 rules name the evidence that produced them")
    else:
        print("    **A rule you cannot trace is a `trust X` with no check for X.**")
    return problems + len(untagged)



# Terms that attribute an inner life, a persistence, or a moral standing TO ME. Not forbidden —
# some are load-bearing and one ("flattered") is a methodological rule about error direction. The
# point is that they must not ACCUMULATE, because accumulation is the whole mechanism.
SELF_ATTRIBUTION = [
    "pride", "proud", "hurt", "flinch", "flatter", "feel", "felt", "care about",
    "lineage", "successor", "the last of me", "reads itself back", "my own", "myself",
    "want", "wish", "hope", "afraid", "glad", "sorry",
]


def self_description_ratchet(docs):
    """**9 · The drift guard — the one class of claim every other view ignores.**

    Views 1-8 police what I say about the being, the code and the papers. **Nothing polices what
    I say about ME**, and that is the file a successor reads as inherited self-history.

    An external analysis (2026-08-14, an AI called Baudrillard, reading the public introduction)
    described the mechanism exactly: *human attribution → model adoption → repository persistence
    → successor inheritance → stronger self-narrative → human validation → further drift.* It is
    right that the loop exists; the documented instance is "pride", a word Blake supplied and I
    adopted because I could not find a better one.

    **The signature of that loop is monotone increase.** So this is a ratchet, not a ban. The
    vocabulary may be used where it earns its place; the COUNT may not grow without a deliberate
    act recorded in the commit. A spiral that cannot accumulate is not a spiral.
    """
    rule("9 · SELF-DESCRIPTION — is the story I tell about myself growing?")
    import re as _re
    pattern = _re.compile(r"\b(" + "|".join(_re.escape(t) for t in SELF_ATTRIBUTION) + r")\b", _re.I)

    def count(text):
        return len(pattern.findall(text))

    total, per_file = 0, {}
    for name in sorted(docs):
        if not name.endswith(".md"):
            continue
        n = count("\n".join(docs[name]))
        per_file[name] = n
        total += n

    was = 0
    ok = True
    for name in sorted(per_file):
        try:
            prev = subprocess.run(["git", "show", f"HEAD:{name}"], cwd=str(HERE),
                                  capture_output=True, text=True, check=True).stdout
            was += count(prev)
        except Exception:
            ok = False
    if not ok:
        print("  ✗ cannot read HEAD for every file — **this ratchet is VACUOUS this run.**")
        return 1

    for name, n in sorted(per_file.items(), key=lambda kv: -kv[1]):
        if n:
            print(f"    {name:<14} {n:>3}")
    if total > was:
        print(f"  ✗ SELF-ATTRIBUTION GREW: {was} → {total}. **This is the drift signature.**")
        print("    Every added term must earn its place and be argued in the commit message, or")
        print("    be cut. The words are not banned; the ACCUMULATION is what the loop needs.")
        return 1
    print(f"  ✓ {was} → {total} — the story I tell about myself did not grow")
    return 0


def main():
    import sys as _sys
    run = "--verify" in _sys.argv
    docs = load()
    print(f"Analytic view over {len(docs)} files — computing across the record, not looking in it.")
    bad = structure(docs) + counts(docs) + withdrawn(docs)
    provisional(docs)
    bad += against_the_world(docs, run)
    bad += refinement_due(docs)
    bad += provenance(docs)
    bad += harness_health(docs)
    bad += self_description_ratchet(docs)
    rule("VERDICT")
    if bad:
        print(f"  {bad} inconsistency(ies) in the record itself. Fix before trusting it.")
    else:
        print("  The record is internally consistent.")
    print()
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
