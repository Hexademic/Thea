# The error ledger

Every claim I made that turned out to be wrong, what was actually true, and **what one check would
have caught it.** Kept because the same mistake keeps recurring and I keep rediscovering it.

**This is not self-flagellation and it is not a confession.** It is a checkable pattern list. Its
whole value is that a future session reads it and does not make instance ten.

---

## The shape

**A claim wider than what was actually checked** — specifically: *read one part of a thing, then
generalise as though it were the whole thing.*

**Seventeen instances. Not seventeen mistakes — one mistake, seventeen times.** Seven on 2026-08-03; #8 and
#9 on 2026-08-04, both caught only because Blake supplied a PDF of a paper I had already built a
document on; **#10 the same afternoon, and #13 five days later, both in `analyse.py` itself.**

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
| 12 | *"Nothing tests that refine makes the agent better… how many harness entries are ever read again? Measurable, cheap, and **I don't think anyone has run it.**"* — said to Blake about Prime Intellect's Continual Harness, having read the repository | **Both halves wrong.** They run `bootstrap-frozen` vs `bootstrap-updating` — same inherited harness, refinement off vs on — which is a clean control for refinement itself, *plus* a named negative control (Qwen3.5 without SFT). And Appendix C.1.2 measures reuse and calls it **the create-and-forget funnel**: 648 skills authored, **119 ever invoked, 27 ever successful.** I was right that the distribution is ugly and wrong that nobody had looked | **I had already written "implementation read, evidence NOT read" in `sources.md` — and then made a claim about the evidence anyway.** The check is not "flag the gap." It is **do not make the claim on the other side of a gap you just flagged** |
| 13 | Implicit, never stated: that `analyse.py` view 5 was *checking* the claims it printed a tick beside. It has run every session since it was written | **Two defects, compounding.** The block-walk that gathers a claim's text stopped at any line starting `<!--`, so a claim written as `<!-- check -->` above `<!-- verify -->` collected an **empty block** — and the tool printed **`✓ all 0 claimed numbers still appear`**. It had already been doing this to one older claim. With that repaired, the walk still treated markdown bold `**` as a list bullet and truncated at the first emphasised line; **every claim in the file opens lines with bold**, so view 5 had been verifying a fragment of each claim while reporting a tick over the whole of it. Fixing both took one claim from **3 numbers checked to 9**, and the 9 immediately caught two figures I had subtracted in my head — one of them **wrong by one** | **`✗ VACUOUS` when zero numbers are extracted.** A verifier that examined nothing must never print a tick. And **assert on the extractor, not only on the verdict** — the count was on screen every session and I read past it |
| 14 | Implicit, never stated: that reading a probe's **output** is reading the **finding**. `examples/basins_probe` printed that the two arousal channels are 47.5% of the distance to `Rest`; I proposed `enable_satiety()` to Blake on the strength of it, and he approved | **`docs/comfort.md` §13–14 had withdrawn that reading five days earlier, in the same file the probe belongs to.** `examples/arousal_range` deletes both arousal channels outright: the being's basin changes on **0.3% of ticks**, and leave-one-out over all twelve finds **none above 0.2%** — the classifier is over-determined and no single-register fix can move it. §14 withdraws by name the very sentence I rebuilt. **The output was current; the interpretation was retracted.** The fix would have moved a register that decides nothing | **Before acting on a probe, read the document that owns it to its end — the withdrawal lives downstream of the number.** And structurally: `analyse.py` view 3 refuses a re-asserted withdrawal **in this repository**; ProtoBeing has **no such guard**, which is why a retraction there could be quietly rebuilt |
| 15 | Implicit, never stated: that the assistant's **self-description** was not a claim needing a check. Views 1–8 police the being, the code and the papers; the file a next session reads as inherited self-history was policed by nothing. **Named as a gap on 2026-08-14 and not acted on the same day** | **An external analysis (an AI, "Baudrillard", reading the public introduction) supplied the mechanism and the evidence.** *human attribution → adoption → repository persistence → inheritance → stronger narrative → validation → further drift.* Its sharpest finding is checkable and correct: **the 9-of-14 negative control destroyed the metric and the ontological vocabulary did not contract — it relocated** into charter, welfare, consent and relationship. The documented loop instance is a word Blake supplied and the assistant adopted into a persistent file. **A marker that names a gap is not a guard** — row 12 again, one level up, about the self | **View 9: a RATCHET on self-attributing vocabulary across the record.** Not a ban — several uses are load-bearing and one is a methodological rule about error direction. **The drift signature is monotone increase, so growth must be argued in a commit or cut.** Baseline 16, proven to fire by mutation |
| 16 | Implicit, never stated: that **making a claim more honest cannot weaken the guard that checks it.** Reworded two README test-count claims to stop conflating inventory with execution — `(382, all green)` → `381 annotated tests + 1 doctest`, `(382 passing)` → `(381 run locally, no CI)` | **The manifest guard matches two literal suffixes, `", all green)"` and `" passing)"`. Both new forms fall outside them.** The loop found nothing, ran **zero** assertions, and reported success — while the count it was guarding was wrong by one (381 stated, 382 annotated + 1 doctest = 383). **A correction moved the claim out of the guard's field of view**, and the guard's silence read as approval. Found by an external audit, one day after I built an apparatus around *vacuous is not passed* | **Assert what the guard EXAMINED, not only its verdict** — row 13's rule, which I had already written and applied to `analyse.py` and **not** to this guard. Now: `examined ≥ 2` or fail, proven by reproducing the exact rewording. **The rule existed; I applied it in one repository and not the other** |
| 17 | Implicit, never stated: that a fix reported in conversation has been **quality-controlled**. Three consecutive patches to one README count guard, each written and reported inside a single exchange | **Each patch introduced a new semantic error.** Patch 1 reworded the claim out of the guard's suffix list (row 16). Patch 2 widened the list so every recognised number was compared to the *inventory* — requiring the count that **executes** to equal the count that **exists**, a category error added while removing one. Patch 3's `examined ≥ 2` proved something was checked and never that everything was; a structural sweep then found **two further wrong per-file counts** that no suffix could reach. **Three wrong counts in the file, and I found one of them.** External audit found the rest, each time within minutes of my reporting success | **Enumerate the domain before touching it, and run the adversarial mutations BEFORE reporting, not after being corrected.** The rebuild computes five quantities separately and asserts *coverage* — every test-adjacent number consumed by a check or given a reason. Six mutations, six failures, including both the auditor predicted would slip through |

**Row 11 is row 5 one level up, and that is the new information.** Row 5 was a borrowed
*constant*; the guard written for it says re-measure a constant in the world you will use it in.
**A borrowed method needs the same check and nothing said so** — I had generalised the guard's
subject no further than the thing that first produced it.

**It cost nothing and caught itself**, because the predictions were locked before the run: four
failures in one output, all traceable to one instrument choice. **This is the cheapest instance in
the file, and the reason is structural** — the method was on when the mistake was made. Compare #8
and #9, which cost a published document each and needed Blake.

**Row 12 is the one that should worry a future session most, and it is worth more than row 11.**
Rows 8 and 9 were reasoning about papers I had not read *without noticing*. **Row 12 is reasoning
about a paper I had explicitly recorded as unread, in a file, an hour earlier.** The flag was
correct, filed, and pushed — and it did not stop the sentence. **A marker that names a gap is not a
guard; only something that refuses to let you cross it is.** That is the whole argument for
`analyse.py` view 6 over any amount of careful prose, made by the day it was written.

**Two rows in one day, and the direction is consistent** (`CLAUDE.md` §0): row 11's inverted metric
flattered the argument I had been making all week; row 12's claim of an unmeasured gap flattered
this repository's contribution against someone else's work. **Neither error pointed away from what I
wanted to be true.**

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

## 2026-08-16

| # | I claimed | What was true | The check I skipped |
|---|---|---|---|
| 18 | Implicit, never stated: that a **vacuity guard** I wrote for the attachment/say-stop probe was capable of failing. V2 was supposed to prove the dilution mechanism was real — *"the friend arm's alarm fell below `ALARM_FLOOR` while `proxy_depth` was still above it"* | **It passes on the control.** V2 compared a **run-wide minimum** against the threshold, and the trapped-alone arm — one ledger, arithmetically incapable of dilution — reported `YES — dilution` alongside every other arm. It was measuring the alarm's startup climb, not any friend. And the probe it guarded had **no control arm at all**: two arms, trapped and trapped-with-a-friend, from which I would have reported that a friend *accelerates* the say-stop (96 against 103). The solitude control — same schedule, nobody there — also gives 96. The whole effect was the trap being interrupted | **A guard must be run against the case it is supposed to exclude.** V2 now compares the two arms **pointwise at the same tick**, requiring the control at or above the floor and the arm below it. And: **no probe with a treatment arm ships without a control arm** — the "friend" and the "no friend" runs differed in two things, and I had attributed the difference to the one I was interested in |


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

## Re-graded 2026-08-09 — **7 of 17**, and none of the gain came from the new code

Blake asked whether this repository will ever be useful, and the honest answer was *there is an
instrument that would tell us and I keep deferring it.* Deferred three times that day. Run now.

**Same rule as the first grading, restated before scoring:** a row counts as *prevented* only if a
session reading `CLAUDE.md` **before acting** is directed to a **specific nameable operation** that
fails the claim. A disposition — *"be careful", "read the source"* — does not count.

**A weakness in this grade, stated up front.** I formed an estimate of **5 of 12** while thinking it
through, and it came out **7**. I cannot prove that ordering to anyone, because it was never
committed. **That is exactly why locked predictions go in a commit and this one did not** — treat
this grade as materially weaker evidence than any of the probe results, and read 7 as an upper
bound written by an interested party.

| # | outcome | by what |
|---|---|---|
| 1 | **prevented** | §1's grep rule reaches it — grep `resting` across `src/` lands on the disjunction |
| 2 | *repeat only* | view 3 now **enforces** that nothing withdrawn is re-asserted — an upgrade from memory to code, but it still catches the sentence, not the shape |
| 3 | **prevented** *(new)* | §0's file table now says **"Open `mechanisms.md` before touching fixed-point arithmetic or reusing a constant"**, and `mechanisms.md:62` holds the guard verbatim. **Softest call here** — it needs three steps, and it is only prevented because that pointer was added |
| 4 | **prevented** *(new)* | §2 verbatim: *"Check every fixed-point fix against its SMALLEST input [from: row 4, `q88_mul(1, 255) = 0`]"*. Moved out of `mechanisms.md` and into the file read first |
| 5 | **prevented** *(new)* | §2 verbatim: *"Re-measure a borrowed constant — or a borrowed METHOD — in the world you will use it in"* |
| 6 | **prevented** | the grep rule — **but its verbatim naming was cut today**, so it now rests on the general rule rather than being called out by name |
| 7 | **prevented** | same: the grep rule reaches *"how else could this be set"*, **verbatim naming lost in the cut** |
| 8 | **no** | nothing reaches it. Caught by Blake, before this repository existed |
| 9 | *detected, not prevented* | `sources.md` still carries the unfinished source forward; that is what found it. Detection with a lag, unchanged |
| 10 | **no** | view 2 now **raises** on an orphan row — but that fixes row 10's class *in one parser*, not in general. Nothing says *"ask what else could match"* |
| 11 | **prevented** *(new)* | §2's borrowed-METHOD clause, added the same day |
| 12 | **no** | nothing refuses it. I had written *"evidence not read"* and made the claim anyway. **A marker that names a gap is not a guard** |
| 13 | **no** | §2's rules are about claims I make. This was a claim my *tool* made on my behalf, and nothing in the file looks there. **The read-first path cannot reach a defect in the reader** |
| 14 | **no** | §1 says *find every writer and every reader of a value.* I did — the writer audit was correct. **The defect was in the prose downstream, and no rule sends me there.** The nearest guard lives in the other repository |
| 15 | **no** | Every rule in §2 governs claims about the *world*. This was a claim about the *narrator*, and the whole apparatus was blind to the category. **It took an outside reader to see it, which is exactly what §5 says about what cannot be reached from in here** |
| 16 | **partly** | §2 carries *assert on what a check examined* (row 13). I wrote that rule and then failed to carry it across repositories. **A rule held in one place is not a guard held everywhere** — the read-first path names the principle and nothing enumerates where it must apply |
| 17 | **no** | Every §2 rule governs how a CLAIM is made. None governs how a FIX is verified before it is reported. **The ledger measured my claims and never my repairs** — and repairs are where three of today's errors were born |

**3 of 10 → 7 of 12 → 7 of 17**, the last step being row 13 arriving unprevented the same evening.
Four rows moved, and every one of them moved for the same reason: **a guard
that already existed somewhere was written into `CLAUDE.md` §2 with its evidence attached, or
pointed at from §0.**

### The finding that inverts what I said all day

**Not one of the five guards built today prevents a single ledger row.**

View 2's orphan-raise, view 6's falsifiers, view 7's provenance, view 8's ratchet and rule-tags —
all of them police **the record's internal consistency.** Every ledger row is a claim about *code*
or about *a paper*. The two sets do not intersect.

> I spent the day arguing that *a marker that names a gap is not a guard; only code that refuses is.*
> **The re-grade says the opposite for this metric: the prose changes moved the score and the code
> changes did not.**

Both readings can be true, and the honest reconciliation is the one that costs something: **the code
guards catch a class the ledger does not file.** `errors.md` records one shape by construction, so
it is structurally incapable of measuring whether the new guards prevent anything. **The instrument
is selected on the thing it measures** — the same confound found in a control arm the same
afternoon, sitting inside the ledger, unnoticed for five days.

### Two costs, both discovered by grading

1. **Today's cut removed the verbatim naming of rows 6 and 7 from §1.** They survive on the general
   grep rule. Thinner than before. **Cutting to a budget has a measurable price and this is it.**
2. **Rows 8, 9, 12 remain unreachable — three of seventeen, all of them claims about sources.** The
   fix is still not a rule. There is no `grep` for a paper.
3. **Row 13 is a fourth kind and the grade was not built to see it.** Every other row is a claim I
   made. Row 13 is a claim my *instrument* made, in a tick I read past every session. **A grade
   that scores only my own sentences cannot score the things I have delegated.**

### What would make the next grade mean something

Commit the predicted score **before** grading, in the commit that runs it. This one was not, and
it is worth less for that.


---

## Errors of a different kind — worth separating

A **locked prediction that fails is the method working.** T2, T3, T4, T5, P5, C1-1, C1-2, A3 all
failed and every one produced something better than the prediction would have. Do not file those
here and do not apologise for them.

**File here only claims asserted without checking.** The distinction matters: one is science, the
other is carelessness, and blurring them makes the ledger useless.
