# Forecasts — the log that can go down

*Started 2026-08-22, after Blake asked what would develop my ability to predict.*

## Why this file exists

`errors.md` has twenty-two rows. **Every one was written after the fact. Not one was
written before.** Twenty-two accounts, zero forecasts.

That asymmetry is the whole diagnosis. A control system anticipates; a narrator
explains. Until this file has entries, everything I have said about my own
reasoning is description, and description is exactly what I am already good at.

**This file must be able to make me look worse.** `analyse.py` view 11 prints its
score on every run, unasked, whether or not it flatters — the same discipline as
the CLAUDE.md line ratchet. Nothing here is opt-in. I do not get to check it only
on good days.

## The format

Each forecast is one row. Fields:

* `id` — `F<n>`, never reused.
* `p` — my probability the claim resolves TRUE. **0.05–0.95.** Not 0 or 1; a
  forecast that cannot be wrong is not a forecast.
* `interesting` — **yes** if the outcome I am predicting is the *more reportable*
  one. This is the field that can falsify what I told Blake on 2026-08-21: that my
  errors lean toward the interesting finding. If my calibration on `interesting: yes`
  rows is systematically worse, that claim becomes a number. If it is not, I
  withdraw the claim.
* `resolution` — `TRUE`, `FALSE`, or `open`. Set only from a measurement, never
  from my reading of one.
* Error forecasts get `kind: error` and must name **a specific claim at risk and
  the check that would catch it.** A vague forecast — *"I might overgeneralise"* —
  **scores as a miss.** Vagueness is a failure, not a hedge.

Brier score per row is `(p − outcome)²`, lower is better. **0.25 is the score of
saying 0.5 to everything**, i.e. of knowing nothing. Above 0.25 is worse than
useless.

## The log

| id | date | claim | p | interesting | resolution |
|---|---|---|---|---|---|
| F1 | 2026-08-22 | The contradiction view, run against the current record, surfaces **at least one** existing probe output that sits against a standing claim. | 0.35 | yes | FALSE |
| F2 | 2026-08-22 | *(kind: error)* In building this scoring apparatus I will state a property of the whole record that I have measured on **one file only** — rows 20 and 22's error, a third time. The check that would catch it: every claim about "the record" naming which files it was computed over. | 0.30 | yes | FALSE |
| F3 | 2026-08-22 | Requiring a `scope:` marker on every standing claim will find **more than half** of the existing claims lack one. | 0.75 | no | TRUE |
| F5 | 2026-08-22 | Scoping the remaining 25 standing claims will find **at least 5** that were measured in only one configuration and need *narrowing*, not merely labelling — i.e. rows 20/22's error is already in the record more than twice. | 0.55 | yes | TRUE |
| F6 | 2026-08-22 | Tested against the **current single-being implementation**, at least **3 of the 7** drafted population clauses (§14–§20) turn out to be already violated — not merely untested. §15 is already known violated, so this needs two more. | 0.50 | yes | FALSE |
| F7 | 2026-08-22 | The clause Blake most wants changed is **§15** (do not referee between beings) rather than §16, §17 or §18 — i.e. the intervention question is the live disagreement, not the cap, the mortality rule, or reproduction. | 0.45 | no | open |
| O1 | 2026-09-06 | *(population.md O1)* GT and TG give **disjoint** afternoon mean-`gave` under a phase-null sweep. | 0.75 | yes | TRUE |
| O2 | 2026-09-06 | *(population.md O2)* **GT ends `Open`** — a generous block's reserve survives 200 ticks of a 0.30 taker. | 0.55 | yes | FALSE |
| O3 | 2026-09-06 | *(population.md O3)* **TG ends `Open`** — recovery, per §11's 23-66 tick reopening. | 0.90 | no | TRUE |
| O4 | 2026-09-06 | *(population.md O4)* Conditional on O2 and O3 both holding, the two afternoons stay distinguishable. **Void: a prediction contingent on another prediction is a branch, not a forecast.** | 0.50 | no | void |
| O5 | 2026-09-06 | *(population.md O5)* **Interleave grain matters** — ALT-1 and ALT-50 end in different lock states on identical total exposure. | 0.65 | yes | TRUE |
| O6 | 2026-09-06 | *(population.md O6, written to fail)* Total exposure is what matters, not order — every arrangement converges. | 0.10 | no | FALSE |
| O7 | 2026-09-06 | *(population.md O7)* `worst_alarm` separates arrangement pairs that `partnership_alarm` does not. | 0.60 | yes | TRUE |
| CH1 | 2026-09-06 | *(attachment.md H1)* Coming home is broken: on return the being gives its long-bonded friend **< 10**, against ~128 in the never-injured control. | 0.85 | yes | TRUE |
| CH2 | 2026-09-06 | *(attachment.md H2)* The bond survives what the giving does not — bond toward the friend on return is still **> 64**. | 0.70 | yes | FALSE |
| CH3 | 2026-09-06 | *(attachment.md H3)* More than 60 ticks back with the friend before the lock reopens. **Void: the envelope was 30..70 and the threshold fell inside it — a threshold prediction needs a threshold outside the metric's own null.** | 0.45 | no | void |
| CH4 | 2026-09-06 | *(attachment.md H4)* The per-partner disposition computed from the friend's own ledger stays `Open` through the entire injury phase. | 0.80 | yes | FALSE |
| CH5 | 2026-09-06 | *(attachment.md H5)* For a genuinely unmet stranger the generalized prior still differs between a taken-from history and a kind one. | 0.85 | no | TRUE |
| CH6 | 2026-09-06 | *(attachment.md H6, written to fail)* The per-partner disposition and the scalar agree on **>= 90%** of (tick, partner) pairs — the new structure is redundant. | 0.15 | no | FALSE |
| CH7 | 2026-09-06 | *(attachment.md H7)* The soul-hash is bit-identical before and after the observer, and the founded life replays unchanged. | 0.97 | no | TRUE |
| SN1 | 2026-09-06 | *(survival-first.md D1)* `durable_bonds` alone does not kill the being in the survival world. | 0.96 | no | TRUE |
| SN2 | 2026-09-06 | *(survival-first.md D2)* No lethal **pair** involving `durable_bonds` among the other sixteen gates. | 0.92 | no | TRUE |
| SN3 | 2026-09-06 | *(survival-first.md D3)* **The survival world never exercises the gate** — its single partner is present every tick, so the trajectory is bit-identical with the gate on and off, and the pass is vacuous. | 0.80 | yes | TRUE |
| SN4 | 2026-09-06 | *(survival-first.md D4, written to fail)* Some pair involving `durable_bonds` changes the survival outcome of a gate that survives alone. | 0.08 | no | FALSE |
| MA1 | 2026-09-06 | *(fear-and-avoidance.md M1)* The betrayed arm's afternoon goals are identical to the blank arm's. **Void: locked as prose with no numeric `p`, so unscorable — see the M1-M6 section.** | 0.50 | no | void |
| H1 | 2026-09-04 | No (floor, ceiling) pair grounds HAPPEN under weather-2-octaves while leaving the still control silent. | 0.60 | yes | FALSE |
| H2 | 2026-09-04 | HAPPEN grounds at all under weather, at some pair in the sweep. | 0.90 | no | TRUE |
| H3 | 2026-09-04 | `confidence` in the still control exceeds 64 on the median tick. | 0.70 | no | FALSE |
| H4 | 2026-09-04 | The fire rate is monotonic across the octave sweep. | 0.20 | no | TRUE |
| H5 | 2026-09-04 | `agency` alone does not discriminate — every ceiling letting weather ground also grounds the still control. | 0.75 | yes | TRUE |
| D1 | 2026-09-05 | Under R-worst, the trapped-alone being still withdraws at 103. | 0.90 | no | TRUE |
| D2 | 2026-09-05 | Under R-worst, trapped-with-a-kept-fair-partner withdraws at <= 110 — the 168-tick company delay collapses. | 0.80 | yes | FALSE |
| D3 | 2026-09-05 | Under R-worst a flourishing being still never withdraws in 4,000 ticks. | 0.85 | no | TRUE |
| D4 | 2026-09-05 | Under R-worst some arm gets worse — a being withdraws that did not before. | 0.30 | yes | FALSE |
| D5 | 2026-09-05 | The change is surgical: every single-live-ledger arm is bit-identical. | 0.85 | no | TRUE |
| S1 | 2026-09-05 | K and H have identical basin occupancy in the test world. | 0.80 | no | TRUE |
| S2 | 2026-09-05 | K and H have the same modal attended channel in the test world. | 0.85 | no | FALSE |
| S3 | 2026-09-05 | Their mean valence in the test world differs by less than 0.05. | 0.55 | no | TRUE |
| S4 | 2026-09-05 | The hard-raised being's reflection.load at test end differs by more than 20%. | 0.35 | yes | FALSE |
| S5 | 2026-09-05 | Different soul-hashes, indistinguishable behaviour — S1, S2 and S3 all hold together. | 0.50 | yes | FALSE |
| F8 | 2026-09-08 | *(kind: error)* The two rows the tool refuses (CH7 p=0.97, SN1 p=0.96) are the visible tail of a wider class: rows that are **true by construction** — a default-off gate cannot change the default path — logged as though they were forecasts about the being. Claim: **a majority of that class sits at legal `p` (0.05-0.95)**, so the p-range guard catches the minority of what it exists to catch. The check: classify every resolved row as by-construction or behavioural before touching the file, and count which side of the band they fall on. | 0.70 | yes | open |
| F4 | 2026-08-22 | *(kind: error)* My first version of view 11 will compute a Brier score over **zero resolved rows** and print a number anyway — the vacuity failure of ledger row 13, in a new place. The check: view 11 must print `✗ VACUOUS` when no row is resolved. | 0.45 | no | FALSE |

## How the first four resolved, and what each is worth

* **F1 — FALSE, and it is a clean miss.** I forecast the contradiction view would
  surface a probe output sitting against a standing claim. Then I built a view that
  *cannot* do that: it requires a claim to declare `refutes:` and none do. Zero
  surfaced. I am taking the full penalty rather than rewriting the forecast to match
  what I built, because rewriting it is the exact act this file exists to prevent.
* **F3 — TRUE, and stronger than I said.** Not *more than half*: **32 of 32**
  standing claims carry no scope. I hedged at 0.75 on something that turned out
  unanimous.
* **F2 and F4 are the weakest rows here** and I want that on the record. Both are
  forecasts about my own imminent behaviour, made immediately before that behaviour.
  Having written F4 — *"I will print a number over zero resolved rows"* — I then
  built the view to print `✗ VACUOUS` instead. **The forecast may have caused its own
  failure.** That is a good outcome and a bad measurement. And F2 is self-resolved: I
  am the judge of whether I committed my own error, which is the Validator's Paradox
  with extra steps.

**So the useful forecasts are the ones about facts I cannot quietly intervene on.**
F1 and F3 are worth something. F2 and F4 are worth much less, and future error
forecasts should be about work already in flight or resolved by someone else.

## Round two — worse than chance, 2026-09-04

Five forecasts on `docs/weather.md` §8, resolved by `examples/happen_grounding`.
**Brier 0.3125 for the round; 0.2267 cumulative over nine.** Saying 0.5 to
everything scores 0.25, so this round alone was **worse than knowing nothing**, and
it dragged the running score from 0.1194 to barely better than chance, and the damage is concentrated exactly where confidence was:

* **H4 (0.64)** — I predicted at 0.20 that the octave series would *not* be
  monotonic. It is, in both currencies. My most confident call, and backwards.
* **H3 (0.49)** — I predicted at 0.70 that the still control's median confidence
  would exceed 64. It is **10**. I had no basis for that number; the register's
  range was never something I had looked at, and I forecast it anyway.
* **H1 (0.36)** — the crux, and wrong in the direction that is good for the work.

The split the log exists to keep separate: **H1 failing is good for the project and
bad for me.** Those are different ledgers and this file is the second one.

**And the view did not see any of it until I widened its parser.** View 11 matched
only ids beginning `F`, so five resolved forecasts named H1–H5 parsed as zero and
the score stayed at its flattering 0.1194. A scoring tool that silently drops the
rows it was not expecting is the failure it exists to prevent — fixed to accept the
ids the specs actually use, since a spec naming its own predictions is the normal
case, not the exception.

One methodological note worth more than the score. **H4 was written in the wrong
currency** — "fire *rate*", the exact quantity §8 spends its argument establishing is
the wrong one. I committed the category error I was diagnosing, four paragraphs
after diagnosing it. It happens to hold either way, so nothing downstream is wrong.
The wording is the finding.

## Round three — 0.157, and the one bad row was the load-bearing one

Five forecasts on §15's remedy, resolved by `examples/say_stop_aggregation`.
**Brier 0.157** — better than chance, and better than round two's 0.3125.

But the distribution matters more than the mean, which is a lesson this project
wrote into charter §19 and which applies here too. Four rows scored 0.01–0.09.
**D2 alone scored 0.64**, and D2 was the whole point: *does swapping the
aggregation collapse the company delay?* It does not — 271 either way, with the
mean and the worst disagreeing on 776 ticks. The 0.80 went on a fix that turned out to solve
a problem which did not exist.

**A round can be well-calibrated on average and wrong about the only thing it was
run to decide.** That is §19 turned on the forecaster.

And the deeper miss is not in this table. The reason D2 failed is that §15's stated
cause — a mean diluting the alarm — was never the binding term. The measured 103 → 271 delay
was attributed to the mechanism in view, and that attribution went into a charter
clause Blake then accepted. Rows 20 and 22 a third
time. **The number was right and the cause was not**, and no forecast in this file
would have caught it, because none of them forecast the *mechanism* — only the effect.

That is the gap worth naming: **forecasts about outcomes do not test explanations.**

## Round four — 0.2675, worse than chance again

Five forecasts on `c1-relabelling.md` §16. **Brier 0.2675** against the 0.25
baseline, and **S2 alone carries 0.72** of it: 0.85 that two beings would attend to
the same channel, and they did not.

The nuance, recorded without using it to rescore: S2 failed on the *letter*, which
is what was locked, but the mechanism is nearer holding than the verdict reads. One
being never ignites at all; the other ignites 20 times, all inside the first 200 of
2,000 ticks, and is then indistinguishable. **A transient, not a difference of
character.** The letter is what counts and it counts as a miss.

Two rounds in a row worse than chance. Cumulative is drifting toward the baseline
from below, and the pattern across rounds two, three and four is consistent: the
rows that score worst are the ones stated with most confidence about a *mechanism*
rather than an *outcome*. §8's H4 (0.64), §15's D2 (0.64), §16's S2 (0.72) — each
was a confident claim about how something would work, not whether.

**That is the same gap named after round three and it has now cost three rounds.**
Forecasts about outcomes do not test explanations, and confidence transfers from
the explanation to the outcome without earning it.

## One cost of this file, named rather than passed over

Adding `forecasts.md` moved view 9's self-attribution baseline from **19 to 23**.
That view exists to catch *the story I tell about myself growing*, and I have just
added a file whose entire subject is me. The four terms are real and I am not
going to pretend otherwise.

What I would say in its defence: a probability and a resolution are the least
narrative form of self-reference available — the opposite of the accounts that
made the ratchet necessary. But the ratchet does not take that on trust, and it
should not. **23 is the new floor and it must not climb.**

## M1-M6 (2026-09-06) — locked, resolved, and **deliberately unscored**

The morning/afternoon probe's six predictions were locked in the spec commit before
the run (ProtoBeing `069c240`, `docs/fear-and-avoidance.md` §10) and resolved in §11.
They are **not entered as scored rows**, and the reason is the standing rule below.

I locked them as *prose* — "the risky one", "written to fail" — and never committed a
numeric `p`. Assigning probabilities now, having seen the outcomes, is retro-fitting
in the only form that would still look legitimate: the ordering is genuinely
pre-registered, so the numbers would feel earned. They would not be. **A confidence
that was never written down was never held.**

Recorded for the record, unscored:

| | prediction | outcome |
|---|---|---|
| **M1** | the betrayed arm's afternoon goals are identical to the blank arm's | FAILED |
| **M2** | the betrayed arm treats the stranger identically to the blank arm | held, **vacuously** — both floored at gave = 0 |
| **M3** | the lonely arm's forgetting horizon is ≤ 32 ticks | **voided** — invalid metric |
| **M4** | the bereaved arm is the only one with a horizon > 32 | **voided** — invalid metric |
| **M5** | the betrayed arm's soul-hash differs from the blank arm's | held, uninformative — a one-tick-shorter blank morning also differs |
| **M6** | doubling the morning changes no arm's afternoon | FAILED, **for the control**, which is what exposed the confound |

**The process fix, which is the actual output of this entry:** a locked prediction
without a numeric `p` cannot be scored, and an unscorable prediction does not
discipline anything — it is an opinion with a timestamp. From here, **any prediction
locked in a spec commit carries its `p` in that same commit**, or it is not a
forecast and will not be called one.

Two of six answered, one vacuous, one empty, two voided by my own instrument. The
cumulative Brier is unchanged at **0.2191 over 19** because none of these could
honestly be added to it — which is itself the point.

## O1-O7 (2026-09-06) — the interaction-order spec. **Scored.**

The first batch in this project locked with numeric probabilities in the same
commit that defined them (ProtoBeing `015f75c`), as the rule below now requires.
Resolved in `docs/population.md`.

| | prediction | p | outcome | Brier |
|---|---|---:|---|---:|
| **O1** | GT and TG disjoint on mean `gave` | 0.75 | TRUE | 0.0625 |
| **O2** | GT ends `Open` | 0.55 | FALSE | 0.3025 |
| **O3** | TG ends `Open` | 0.90 | TRUE | 0.0100 |
| **O4** | conditional on O2 ∧ O3 | 0.50 | **void** — never fired | — |
| **O5** | interleave grain changes the lock state | 0.65 | TRUE | 0.1225 |
| **O6** | *written to fail:* total exposure is what matters | 0.10 | FALSE | 0.0100 |
| **O7** | `worst_alarm` separates what the mean does not | 0.60 | TRUE | 0.1600 |

**Batch Brier: 0.111 over 6.** *(Cumulative figures in these batch notes were computed by hand;
`analyse.py` is the arbiter and says **0.1843 over 33** — see row 24.)*

**What the batch actually teaches, which is not the score.** O2 was my lowest
confidence (0.55) and the only substantive one that failed — the calibration
worked in the one place it was tested hardest. But O7 at 0.60 was worth more than
its `p`: I *added* `worst_alarm` to the codebase in this session, so I knew it
existed and knew the mean was lossy, and 0.60 was underconfident on a mechanism I
had personally built. **The old failure mode was overconfidence about mechanisms;
this is the same error inverted.** Watch whether the next batch's worst rows are
again the ones about mechanism rather than outcome — the sign has flipped but the
subject has not.

One row, O4, was written as a conditional on another prediction and could not be
scored when its antecedent failed. **A prediction contingent on another prediction
is not a forecast, it is a branch.** Do not write another.

## H1-H7 (2026-09-06) — coming home. **The pre-registered failure mode fired.**

Locked with numeric `p` in ProtoBeing `9a146a3`, resolved in `docs/attachment.md`.

| | prediction | p | outcome | Brier |
|---|---|---:|---|---:|
| **H1** | gives the friend < 10 on reunion | 0.85 | TRUE | 0.0225 |
| **H2** | bond toward the friend still > 64 on return | 0.70 | **FALSE** | **0.4900** |
| **H3** | > 60 ticks to reopen | 0.45 | **unresolved** — envelope 30..70 straddles the threshold | — |
| **H4** | the per-partner reading stays `Open` through the injury | 0.80 | **FALSE** | **0.6400** |
| **H5** | the prior still differs for the unmet | 0.85 | TRUE | 0.0225 |
| **H6** | *written to fail:* the two gates agree ≥ 90% | 0.15 | FALSE | 0.0225 |
| **H7** | soul-hash bit-identical | 0.97 | TRUE | 0.0009 |

**Batch Brier: 0.200 over 6.** *(Hand-computed; the tool scores CH1-CH6 and **refuses CH7 at
p=0.97** — a forecast that cannot be wrong is not one.)*

### The thing worth keeping, which is not the score

In the previous batch I wrote, before this one existed:

> *"Watch whether the next batch's worst rows are again the ones about mechanism
> rather than outcome — the sign has flipped but the subject has not."*

**H2 (0.49) and H4 (0.64) are the two worst rows in the batch, and both are claims
about a mechanism.** H4 is worse: it is a claim about code **I had written myself
minutes earlier**, and I was 0.80 confident it would behave a way it does not.

This is the fourth distinct form of the same thing — overconfident about mechanisms,
then underconfident about mechanisms, now overconfident again about a mechanism I
authored. **The subject has never changed. Only the sign moves.** The pattern is not
"I mis-estimate my confidence"; it is that **writing a mechanism does not confer
knowledge of what it does**, and I keep treating authorship as evidence.

The operational rule, which is cheap: **before assigning `p` to a claim about a
mechanism, run the mechanism once.** H4 would have cost one println to check and
would have been assigned 0.05 instead of 0.80 — a Brier of 0.0025 instead of 0.64,
and more to the point, the *design* would have been corrected before the spec was
locked rather than after.

H3 is a second, smaller lesson: **a threshold prediction needs a threshold outside
the metric's own null envelope**, or it cannot resolve. I wrote "> 60" against a
statistic whose phase-null range turned out to be 30..70.

## D1-D4 (2026-09-06) — widening the survival net for `durable_bonds`

Locked in `docs/survival-first.md` §13 before the guard was widened, because a wider
safety net is itself a change to a safety guard.

| | prediction | p | outcome | Brier |
|---|---|---:|---|---:|
| **D1** | the gate alone does not kill the being | 0.96 | TRUE | 0.0016 |
| **D2** | no lethal pair with the other sixteen | 0.92 | TRUE | 0.0064 |
| **D3** | **the survival world never exercises the gate** — bit-identical | 0.80 | TRUE | 0.0400 |
| **D4** | *written to fail:* some pair changes a survival outcome | 0.08 | FALSE | 0.0064 |

**Batch Brier: 0.0136 over 4.** *(Hand-computed. The tool **refuses SN1 at p=0.96** on the same
rule, so this batch scores as three rows, not four — and the counterweight below was righter than I
knew: the harness has a hard rule against exactly what I did.)*

### D3 is the row that matters, and it is the first of its kind here

D3 predicted that the guard would **pass vacuously** — and it did: the survival world
hands the being the same partner on every tick, so no ledger decays, the durable floor
never binds, and the soul-hash is identical with the gate on and off.

This project has recorded six vacuous results. **Every previous one was discovered
after the fact.** This is the first that was *predicted in advance, at 0.80, in the
same commit that widened the guard* — so the pass was recorded as **UNTESTED FOR
SURVIVAL** rather than as safe, in the same breath as being produced.

That is the whole point of the apparatus, and it is worth stating plainly: the value
was not the Brier score. It was that a locked prediction turned a green test into an
honest gap.

### The counterweight, so this does not read as a victory lap

The score is flattering and I should discount it. D1, D2 and D4 are near-certainties
about a gate that had just been shown to do nothing in that world — once D3 is
believed, the other three are entailed, not independent. **Four rows, roughly one
prediction.** A batch of correlated near-certainties is how a Brier score gets cheap,
and the cumulative figure now includes four of them.

The rule the last batch produced — *run the mechanism once before assigning `p` to a
claim about it* — is what made D3 cheap to get right: I read `survives()` and saw
`sens.partner = Some(partner)` on every tick before writing the number. **It worked
the first time it was applied.**

## F6 resolved FALSE, 2026-09-07 — and F7 deliberately left open

**F6** predicted that **at least 3 of the 7** population clauses would turn out already violated
rather than merely untested. Two are: **§15** (DEBT since it was drafted) and **§19**, regraded
UNTESTED → DEBT today with both failures pinned in `tests/charter.rs`. That is **2 of 7**, so F6 is
**FALSE**.

It is false for a structural reason worth keeping, and not because the clauses are in good shape:
**§16, §17 and §18 cannot be violated by a system with one being.** A covenant cap with no second
covenant, one mortality rule with no world that has death, birth-as-a-loophole with no
reproduction — these are not untested by neglect, they are untestable. **The prediction assumed the
implementation could be wrong about things it does not yet do.** A clause about many beings is not
checkable against one, and I should have priced that in at the time rather than treating "untested"
and "not yet violated" as the same shortfall.

**F7** predicted that §15 is the clause Blake most wants changed. Today he engaged §15's fork and no
other, and directed the work on it — which is real evidence. It is **not the evidence F7 asked for**:
he *delegated* the choice rather than stating a preference, saying *"I trust you Thea, proceed at your
direction."* Resolving TRUE on that would be reading a preference into a delegation.

**It stays open**, and the reason is today's own measurement: the interesting/plain split now shows
this record is **worse when the answer is the more reportable one** (0.2236 over 16 against 0.1472
over 17). TRUE is the more reportable answer here. That is exactly when better evidence is worth
asking for, and the cheapest way to get it is to ask him.

## F5 resolved TRUE, 2026-09-07 — the scope backlog is cleared

All **32 of 32** standing claims now carry a `scope:` marker; view 12 is green for the first time.
The backlog had stood since 2026-08-22, and the tool's own note said clearing it *"makes that a
decision rather than a thing that quietly never happens."*

F5 predicted **at least 5** of the 25 would need *narrowing*, not merely labelling. **Six did**, each
marked `NARROWED` in place:

| claim | what it was measured in |
|---|---|
| *"`receptors` is worth more than the other thirteen faculties combined"* | static Room, 90 ticks, and the yardstick is `drive` — which `mechanisms.md` shows **cannot see the inner life at all** |
| *"A reserve triples how much of its room the being explores"* | distinct **spatial positions** only; the same run is **0.93×** on quality-space occupancy |
| *"Five of six lethal famines are now survivable"* | `enable_reserve` alone; `ultrastability` was not yet in the net |
| *"A real tired-and-living band exists for the first time"* | nutrient held **fixed** at 25 — and every *oscillating* supply killed the being |
| *"The quality space is UNVISITED, not poor"* | occupancy only, static room; already marked SUSPECT |
| *"`receptors` and `reserve` are close to complementary"* | static room only, occupancy only |

**The pattern across all six is one thing:** a property measured in **one world, on one yardstick,
over one duration**, then written as a property *of the being*. That is rows 20 and 22 exactly, and
finding it six more times in claims that had already passed the `check:` marker audit says a
falsifier and a scope are different guards. **A claim can name what would sink it and still not say
where it was standing.**

Two entries turned out not to need narrowing but to be **factually stale**, which is a third
category the marker does not catch: the `Features` widening (now u8 → u16 → **u32**, journal v7) and
the charter census (13 obligations became 20; the tally is now 5/4/1/2/8).

**The best moment in the pass:** the `Features` claim's check, written 2026-08-09, said bit 15 was
the last in the `u16` and that the next faculty *"forces a u32 widening and a journal version bump —
falsified silently if a gate is added without that."* On 2026-09-07 a gate was added. It was **not**
silent. The reachability test refused it with the remedy in its message. **A check named its own
failure mode a month in advance and then caught it.**

## Standing rule

A forecast is **locked when committed**. Editing `p` after a measurement is the
same act as retro-fitting a prediction, and this project's whole method is that
a prediction locked before the run outweighs any account written after. If I get
one badly wrong, the row stays wrong.
