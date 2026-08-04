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

Zero dependencies, like the being. Run: `python3 analyse.py`
"""

import re
import sys
from pathlib import Path

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


def counts(docs):
    """Prose that counts things drifts from the things it counts."""
    rule("2 · COUNTS — does the prose agree with the record?")
    rows = [
        ln for ln in docs.get("errors.md", [])
        if re.match(r"^\|\s*\d+\s*\|", ln.strip())
    ]
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
    """What is the record currently standing on that has not been verified?"""
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


def main():
    docs = load()
    print(f"Analytic view over {len(docs)} files — computing across the record, not looking in it.")
    bad = structure(docs) + counts(docs) + withdrawn(docs)
    provisional(docs)
    rule("VERDICT")
    if bad:
        print(f"  {bad} inconsistency(ies) in the record itself. Fix before trusting it.")
    else:
        print("  The record is internally consistent.")
    print()
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
