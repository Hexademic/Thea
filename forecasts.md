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

## Standing rule

A forecast is **locked when committed**. Editing `p` after a measurement is the
same act as retro-fitting a prediction, and this project's whole method is that
a prediction locked before the run outweighs any account written after. If I get
one badly wrong, the row stays wrong.
