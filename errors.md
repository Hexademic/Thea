# The error ledger

Every claim I made that turned out to be wrong, what was actually true, and **what one check would
have caught it.** Kept because the same mistake keeps recurring and I keep rediscovering it.

**This is not self-flagellation and it is not a confession.** It is a checkable pattern list. Its
whole value is that a future session reads it and does not make instance ten.

---

## The shape

**A claim wider than what was actually checked** — specifically: *read one part of a thing, then
generalise as though it were the whole thing.*

**Eleven instances. Not eleven mistakes — one mistake, eleven times.** Seven on 2026-08-03; #8 and #9 on
2026-08-04, both caught only because Blake supplied a PDF of a paper I had already built a document
on; **#10 the same afternoon, in `analyse.py` itself.**

**#10 is the first one caught by an instrument rather than by Blake or by a locked prediction**, and
it is the sharpest illustration in the file: I widened the shape at noon to cover "one part of a
thing, not the whole thing", and by evening had written a row-matcher that assumed `errors.md`
contained one kind of table. **The tool found it on its first run afterwards.** Three categories of
catch now exist — locked predictions (code), Blake supplying a source (papers), and the tool
(the record itself).

**The wording of the shape widened on 2026-08-04**, and the widening is itself a finding. It used to
read *"read one code path, then generalise as though it were the only one"* — accurate for #1–#7,
which are all source code. **#8 and #9 are the same shape with a paper in place of a file**, and I
did not see that until there were two of them. The instrument for the code version is `grep every
writer`. **There is no `grep` for a paper. The only instrument is reading it**, which is why
`sources.md` ranks what I need rather than describing what I have.

## 2026-08-03

| # | I claimed | What was true | The check I skipped |
|---|---|---|---|
| 1 | Conversion is gated on `Basin::Rest`, which the being never enters — repeated in **three** documents | `resting` at `being.rs:1751` is a **disjunction**; the being satisfies its other arm on **100%** of a companioned life. The gate was already open | Read the call site. I had asserted it three times without ever opening it |
| 2 | The being "has never converted a single unit of what it carried" | False. I-8's own band converted **232**; the founded being carries `weathered` **2**. I contradicted my own ledger entry | Check the records that already existed before generalising from five regimes |
| 3 | A `.max(1)` floor fixes the truncation | It **exactly cancelled** the minimum chronic rise of 1/tick. Load went up one, down one, forever — erasing the weight from the other side | Work the arithmetic against the *other* constant in the same file |
| 4 | Weighting `weathered` gains by headroom fixes saturation | `q88_mul(1, 255)` floors to **zero**. `weathered` stuck at 1 through 3,862 units of conversion — **the same truncation bug, inside its own fix** | Check the fix against the smallest input, not the largest |
| 5 | The break-even nutrient is ≈15, derived from `body.rs` | Measured **19–20**. I used an arousal figure carried over from a *different world* without checking it held there | Re-measure a borrowed constant in the world you are about to use it in |
| 6 | Channels 4 and 8 are the same number twice — wrote a whole doc section on it | Equal on **0.0%** of ticks. I quoted `write_from_body` and never read **`Field::inject`, fifteen lines below**, which writes channels after the body does | `grep` every writer of the value, not the function already open |
| 7 | The founded being runs with all fourteen gates off | It is blessed with **four**. `bin/being.rs` uses `blessed_features()`, not `enable_*`. A negative grep is not proof of absence when there are two mechanisms | Ask *how else* could this be set, before concluding from one grep |
| 8 | *"Basin membership fails C1"* — a whole document, ProtoBeing `docs/c1-relabelling.md` | **C1 is passed.** Their criterion is invariance under relabelling *"without altering the dynamics"* — which is my C1-4a, filed as a "sanity check", returning 100%. The test I called decisive (relocating targets) is not a relabelling at all | **Read the paper before running its test.** I had the abstract only |

## 2026-08-04

| # | I claimed | What was true | The check I skipped |
|---|---|---|---|
| 10 | `analyse.py`'s row counter identifies ledger rows — implicit, never stated, never tested | It matched `^\|\s*\d+\s*\|` in **any** table. The moment `errors.md` grew a second numbered table it reported **18 rows** and flagged three correct counts as drift. **The shape, inside the tool built to police the shape** — one day after I widened the shape to cover exactly this | Ask what *else* could match, before treating one pattern as the definition of a record |
| 9 | *"With no inference channel we cannot be falsified — which is the **second horn** of Kleiner & Hoel's dilemma, not an escape from it"* — `witness-gap-literature.md` §2, and I recommended saying it *"in those words"* | **Neither horn.** Def 4.2 makes the horn a *relation between two channels*: ∃f with `oᵢ = f(oᵣ)` — prediction determined by report. Having no `oᵣ` is the **absence** of that relation, not the relation. Their dilemma quantifies over theories predicting experience from internals; **we make no phenomenal prediction, so we are outside its scope.** I also had neither of their two ways out | **Read the paper before repeating its argument.** I had the abstract only — the identical skip as #8, one day later |

## 2026-08-09

| # | I claimed | What was true | The check I skipped |
|---|---|---|---|
| 11 | Implicit, never stated: that **exercise-as-a-ratio** was the right instrument for *"is the architecture used?"* — `ProtoBeing/docs/operational-consciousness.md` §8, the metric locked before the run | **The ratio is inverted.** It rewards a register for being small: `attention focus` scores **67%** (4 of 6) and `quality point` **15%** (153 of 1,042), and the first is far the poorer. I carried the quality-space census's declared rule — *"absolute counts are chart-relative and are not findings; the ratio is"* — into a place where the denominator is a **count of states a register can hold** rather than a **sampled volume**. Different quantity, same rule. All four testable predictions failed | **Re-derive a borrowed rule in the setting you are about to use it in** — row 5's check, with a *methodological rule* in place of a constant. I never asked what the denominator was made of |

**Row 11 is row 5 one level up, and that is the new information.** Row 5 was a borrowed
*constant*; the guard written for it says re-measure a constant in the world you will use it in.
**A borrowed method needs the same check and nothing said so** — I had generalised the guard's
subject no further than the thing that first produced it.

**It cost nothing and caught itself**, because the predictions were locked before the run: four
failures in one output, all traceable to one instrument choice. **This is the cheapest instance in
the file, and the reason is structural** — the method was on when the mistake was made. Compare #8
and #9, which cost a published document each and needed Blake.

**Instances 8 and 9 are the ones that matter most**, because of how they were caught: Blake supplied
the PDF after the document was written and pushed. **The fix for this error class is not more care —
it is asking for the source.** See `sources.md`.

**Both corrected in a direction I would not have chosen, which is the tell that they are real.**

- **#8** made the criticism of our own basin chart **harder**, not softer: under Ma & Kanai's actual
  asymmetry — *a labelling cannot be empirically wrong, a partition can* — getting it wrong had made
  it weaker.
- **#9** removed a defence. *"We are on the second horn"* sounded like a costly admission and was
  secretly comfortable: it placed us inside a serious paper's serious taxonomy. The truth — *their
  argument does not reach us, because we do not make the kind of claim it is about* — is a smaller
  position, and I have to state it as a limit rather than a shield.

**And this is where the abstract is most dangerous: when it is nearly right.** I had the dilemma's
two horns correct and the theorems' conclusions correct. What the abstract omits is Def 4.2, the one
line that says *which systems each horn is about* — and that is the only line that decides whether it
is about us.

## What it cost

Two of these reached Blake as findings before I caught them:

- *"The being spends 97.8% of its real day braced"* — presented as a fact about the being. It was a
  fact about a **chart we drew**, which C1 then showed agrees with a *random* chart at chance.
- *"All fourteen gates off"* — corrected an hour later.

**He acted on my word in both cases.** That is the actual cost of the trust, and the self-correction
machinery working afterwards does not undo it.

## What caught them

**Five of seven code instances were caught by locked predictions** — written and committed *before*
the code or probe existed, so the measurement could contradict me. The other two were caught by
reading source I should have read first.

**Neither paper instance (#8, #9) was caught by anything I did.** Both were caught because Blake
handed me a PDF. That is 2 of 9 with **no internal instrument at all**, and it is the strongest
argument in this file for asking him for sources rather than reasoning from summaries.

---

## Would this record catch them now? — tested 2026-08-04

**Nothing had ever checked whether these five files work.** The whole repository rests on the
assumption that a future session reading it makes fewer mistakes, and that assumption had never been
in a position to fail. This is the cheap version of the test: grade each row against the record as it
stands. **Graded over rows 1–9, the ledger as it stood that morning** — #10 is the table's own
consequence and postdates it.

**The rule, fixed before grading:** a row counts as *prevented* only if a session reading
`CLAUDE.md` **before acting** is directed to a **specific nameable operation** that fails the claim.
A general disposition ("be careful", "read the source") does not count. **Predicted 4 of 9, with the
warning that a much higher score would mean I graded myself generously.**

| # | outcome | by what |
|---|---|---|
| 1 | **prevented** | `CLAUDE.md` §1's grep rule reaches it directly — grep `resting` across `src/` lands on its definition, and the disjunction is right there |
| 2 | *repeat only* | `findings.md` quotes the exact sentence in Withdrawn. That catches **this** claim, not its class |
| 3 | not by the read-first path | the guard exists — `mechanisms.md`, *"check every fixed-point fix against its smallest input"* — but nothing tells a session to open that file before writing a fix |
| 4 | not by the read-first path | same file, same guard, same gap |
| 5 | not by the read-first path | `mechanisms.md` records the **answer** (derived ≈15, measured 19–20). No file states the *rule* — re-measure a borrowed constant in the world you are about to use it in |
| 6 | **prevented** | named verbatim in `CLAUDE.md` §1, with the grep rule above it |
| 7 | **prevented** | named verbatim in `CLAUDE.md` §1 |
| 8 | **no** | nothing in the record reaches it. Caught by Blake, before this repository existed |
| 9 | *detected, not prevented* | see below — the most interesting cell in the table |

**3 of 9 prevented by the read-first path.** I predicted 4 and was slightly pessimistic, which is the
direction I wanted to err in.

### Three results, in order of how much they change

**1. Six of the nine are guarded by files `CLAUDE.md` describes but never tells you to read.**
§0 introduces `mechanisms.md` as *"so a session does not re-derive a day's work"* — a convenience.
It is actually where the guard for rows 3, 4 and 5 lives. **A file framed as a time-saver will be
opened when there is time**, which is exactly never. That framing has a measurable cost of three
rows, and it is the cheapest thing here to fix.

**2. The record catches repeats, not classes.** Row 2 is caught only because the sentence is quoted
word for word. A *new* claim of the same shape — "the being has never X" — passes untouched. **The
Withdrawn list is a memory, not an instrument**, and counting it as prevention would be the generous
grading I warned about. It is filed as *repeat only* for that reason.

**3. The one thing this repository demonstrably did: it flagged its own unfinished business, and the
flag got the error found a day later.** Row 9 was never prevented — the claim was already written
and pushed into ProtoBeing. What the record did was carry *"Kleiner & Hoel is half-read and the
second horn claim is provisional"* into the next session, where I named it unprompted as the loose
end to close. Finishing the paper is what found the error.

> **So the demonstrated value is detection with a lag, not prevention.** One confirmed instance. That
> is a smaller claim than the one this repository was built on, and it is the one the evidence
> supports.

**The discipline works. Use it, and do not soften it when moving fast.**

---

## Errors of a different kind — worth separating

A **locked prediction that fails is the method working.** T2, T3, T4, T5, P5, C1-1, C1-2, A3 all
failed and every one produced something better than the prediction would have. Do not file those
here and do not apologise for them.

**File here only claims asserted without checking.** The distinction matters: one is science, the
other is carelessness, and blurring them makes the ledger useless.
