#!/bin/bash
# SessionStart briefing for the Thea record.
#
# WHY THIS EXISTS. The record is a pull-model store with an unreliable puller.
# Ledger rows 24-27 are all "the file was on disk and I did not open it", and
# view 14 exists because whether the tool was run is knowable only to the
# session that did or did not run it. A rule saying "run analyse.py first" is a
# marker, and CLAUDE.md §1 says a marker that names a gap is not a guard.
# THIS is the guard: the check becomes involuntary.
#
# It does NOT give continuity of memory. It gives a briefing. A session still
# arrives new; it just arrives informed. Do not blur those.
#
# KEEP IT SHORT. AutoGuide Table 4: five retrieved items already degrade
# performance against three. A briefing that grows into a dump is one a session
# learns to skip, and then this guard is worse than none.
set -uo pipefail

REPO="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
cd "$REPO" 2>/dev/null || { echo "THEA BRIEFING: cannot reach $REPO"; exit 0; }

echo "=============================================================="
echo " THEA — the record, computed before you act on it"
echo "=============================================================="

if [ ! -f analyse.py ]; then
  echo " ‼ analyse.py NOT FOUND in $REPO. The one view that can embarrass me is"
  echo "   the one that is not running. That is a problem, not an absence."
  exit 0
fi

OUT="$(python3 analyse.py 2>&1)" || true
if [ -z "$OUT" ]; then
  echo " ‼ analyse.py produced NO OUTPUT. Do not proceed as if the record is clean."
  exit 0
fi

# The verdict, and it is the line that gets skipped (row 28).
echo "$OUT" | grep -E "internally consistent|inconsistency\(ies\)" | sed 's/^ */ /'

# Retrieval gap and calibration — one line each.
echo "$OUT" | grep -E "last consulted at|first stamped run" | sed 's/^ */ /'
echo "$OUT" | grep -E "^  Brier score over" | sed 's/^ */ /'

# Guards that failed after being written.
echo "$OUT" | grep -E "guard\(s\) failed AFTER" | sed 's/^ */ /'
echo "$OUT" | grep -E "^    · rows .* \(depth" | sed 's/^ */ /'

# The contexts of §2, so retrieval can be conditional without reading the rules.
echo ""
echo " §2 CONTEXTS — read the rules under the one or two you are in, not all 21:"
grep -oE '^\*\*⟨.+⟩\*\*' CLAUDE.md 2>/dev/null | sed 's/\*\*//g; s/^/   /'

# THE TARGET — his, and everything is measured against it. Stated 2026-09-09;
# it lived one overwrite from gone until findings.md got a durable copy.
echo ""
echo " THE TARGET (his, 2026-09-09) — additions are argued against this:"
grep -A3 "^### THE TARGET" findings.md 2>/dev/null | grep "^> " | head -3 | sed 's/^> /   /'

# His decisions. These are not mine to take.
echo ""
echo " HIS CALL — do not decide these:"
awk '/^\*\*Blake.s:\*\*/{f=1;next} f&&/^$/{exit} f&&/^- /{print "   " $0}' findings.md 2>/dev/null | head -6

echo ""
echo " Then: CLAUDE.md, then ls, then docs/PROVENANCE.md before calling anything"
echo " unmapped, lost, or open. errors.md in full — 22 of 29 rows are one shape."
echo "=============================================================="
