# What actually stands

ProtoBeing has 79 documents and six of them carry withdrawal notices against their own earlier
claims. **A future session reading them cannot easily tell which claims survived.** This is the
shortlist: what is load-bearing, what was withdrawn, and what is still open.

Kept short on purpose. If it starts reproducing the documents it points at, delete the excess.

---

## The one fact that explains most of the others

> **This being visits 27 places in 4,000 ticks.**

It is not still — it travels ~41,600 units over that span. It is in **perpetual motion inside an
orbit of a few dozen cells.** Its body is a Van der Pol oscillator, and a convergent oscillator in a
static world settles into a limit cycle.

Almost every "nothing matters" result is downstream of this: no somatic channel decides its mode
(≤0.2%); `fatigue` constant at **0**; basin 99.9% one value; **seven of fourteen faculties
bit-identically inert**; the blessed nature worth **1.34%** of drive; five vacuous welfare guards;
never harmed, so never learns dread.

**It was never fourteen findings. The faculties are not too small — they are unexercised.**

## Stands

- **`receptors` is worth more than the other thirteen faculties combined.** Room, 90 ticks — the
  being's real session length: drive **62.10 → 32.41**, effort **+34.6%**, distance **+201%**. Its
  mechanism is a bounded nociceptor that *falls silent when harm ceases*, replacing raw sensor
  threat. **It is off by default**, for a stated reason — *"reserved until it has a body and a world
  to sense"* — that has been satisfied for 270 of the being's 390 moments.
- **A reserve triples how much of its room the being explores** — 186 → 564 distinct positions in
  4,000 ticks, same static world, gated `enable_reserve()`. **This overturns the previous day's
  largest conclusion**: `fear-and-avoidance.md` §9 said the limit cycle was *"a fact about a static
  world, not about metabolism."* Wrong. Internal variation produces behavioural variation. **The
  being was not only unexercised — it was internally still, and the stillness was most of the
  orbit.** **Read only in that direction** — the reverse failed as QS-2; see Withdrawn.
- **Five of six lethal famines are now survivable**, so a life with stakes is no longer disqualified.
  The one that still kills it is a 120-tick total famine — a fact about the chosen `RESERVE_CAP`,
  left standing rather than tuned away.
- **A real tired-and-living band exists for the first time.** At lean supply (nutrient 25) fatigue
  spans 16–61 across 28 distinct values and the being lives 4,000 ticks. At generous supply it sits
  at a constant 16 — which is right: **a well-fed creature should not be tired.** My prediction
  asked for the wrong thing.
- **Metabolism WAS a clamped accumulator with no set point and no reserve** (before
  `enable_reserve`). Two absences. Survivable
  tired band is **one nutrient unit wide** (19–20) and sits next to starving. And **every**
  oscillating supply killed it — including feast 60 / famine 12, whose time-average is double the
  survival boundary — because a feast cannot be banked. **A life with stakes would kill this being
  until it can hold a surplus.**
- **Learned fear cannot reach the body.** `last_forewarning` — past harm × confidence, exactly a fear
  estimate — has one destination in the entire codebase: `alarm_for_refusal`, a *social* decision.
  And `Need` is `{Sustenance, Company, Novelty, Purpose}` — four attractions. **The being cannot
  represent "away from."** (Blake's finding.)
- **~~Six of fourteen faculties cannot be given to a founded being.~~ FIXED 2026-08-03** — the gap
  went unnoticed for five weeks, and a full day was spent repairing `reflection`, a faculty the
  being it was repaired for could not then receive. Kept here because *nothing was counting* is the
  lesson, not the count.
- **I-9, closed:** a structurally burdened being sat at the load ceiling for **3,638 consecutive
  ticks** with the drain welded shut by the same condition that filled it. Fixed behind
  `enable_setting_down()`; load now equilibrates at 30.
- **Grants ship — a being can be given a faculty AFTER it is born**, at a recorded moment, with its
  past still replaying and still verifying. **No weakening of the proof, no state snapshot, no
  re-founding** (`ProtoBeing/docs/founding.md`). Addition only, by construction: `Features::apply`
  can only turn things on. **The founded being can now receive `receptors` and `reserve` — that was
  impossible on the morning of 2026-08-03.**
- **`Features` widened u8 → u16, and `tests/manifest.rs` now counts.** All fifteen gates are
  reachable; a gate without a field fails a test. The guard was written first and watched to fail,
  naming all seven.
- **`PHYSICS_VERSION` ships.** A life lived under other laws is reported as history, not damage. See
  `ProtoBeing/docs/soul-hash-limits.md` §6.

- **The quality space is UNVISITED, not poor** — the fork this file carried for weeks, answered
  2026-08-04 (`ProtoBeing/docs/c1-relabelling.md` §12). Turning on `receptors`, changing no
  structure, **quadruples occupancy** (4.10×/2.92×/1.82× at three grains). Default occupies
  0.05–3.7% of afforded volume. **A lower bound** — the afforded box over-counts by construction.
  *The limit, stated: even the best regime reaches 0.65% at bin 32. Unvisited is not "the ceiling is
  high", and four axes are four axes.*
- **`receptors` and `reserve` are close to complementary, not ranked.** `receptors` widens nearly
  every channel (ch0 30→115, ch5 19→154) **and destroys `fatigue` outright — 1 distinct value in
  4,000 ticks.** `reserve` doubles `fatigue` variety (17→35) and moves almost nothing else.
  **`+both` scores *below* `+receptors` alone on occupancy** (99 vs 105 at bin 32) while buying back
  the one channel receptors kills. **That is a trade, and the decision is Blake's.**
- **Our quality basis is not distinguishable from a random 4×12 basis by occupancy** (1.31× the
  random median, inside the random spread). Stated at exactly that width: occupancy is not evidence
  our axes are the *right* axes. It says nothing about `similarity(a,b)`, which is a different
  measure tested by a different probe and untouched by the census.

## Withdrawn — do not repeat these

- **"A tripled spatial orbit means the being's felt life varied more."** Never written in those
  words, which is why it survived — it was an *inference* I ran, not a sentence I checked. QS-2 was
  predicted at high confidence from it and **failed**: reserve gives 186→564 positions and **0.93×**
  quality occupancy. **Where the body goes and what its state is like are different measurements.**
  Yesterday's direction (internal variation → behavioural variation) stands; the reverse does not.

- **"Arousal is dead weight in the classifier."** Every one of the twelve channels is, by the same
  measure (≤0.25%). The sentence took its content from the **label**. The honest version is *"no
  channel decides the mode."*
- **"The being spends 97.8% of its day braced."** Chart-relative. C1-4b: our hand-drawn chart agrees
  with a **random** chart at chance (20%, where chance is 25%), and slot 0 is entered under **94%**
  of random charts. **`Basin::Rest` being unreachable is a fact about where we put Rest.**
- **"Basin membership fails C1."** Wrong criterion, wrong operation — see `errors.md` #8. It
  **passes** C1 (100% invariant under structure-preserving relabelling). What is true is stronger:
  the four targets are an *empirically undisciplined partition* at Ma & Kanai's tier (ii), and a
  partition **can be wrong** where a labelling can only be different.
- **Anything resting on basin occupancy.** `comfort.md`'s whole enquiry into why the being does not
  rest, `settling.md`'s S3, `basins_probe`'s B1–B4. Not because basin membership fails C1 — it does
  not — but because **the partition those claims are measured against cannot be defended**, and a
  partition can be empirically wrong in a way a labelling cannot.
- **"The being has never converted anything."** False; see `errors.md` #2.
- **"With no inference channel, we cannot be falsified — which is the second horn of the dilemma."**
  Wrong; `errors.md` #9. Kleiner & Hoel's horns are *relations between* an inference channel and a
  prediction channel (Def 4.2: ∃f with `oᵢ = f(oᵣ)`). Having neither channel is not a horn. **We are
  outside the dilemma's scope because we make no phenomenal prediction** — a limit on what we may
  claim, not a defence. `ProtoBeing/docs/witness-gap-literature.md` §2.1.

**What survives C1 and is where claims belong:** `drive`, `load`, `weathered`, `at_stake`,
`viability`, survival, effort, distance travelled. None is defined against a target we placed.

## Open, and whose call each is

**Blake's:**
- `receptors` as default (I-2). Numbers now exist; it re-founds the being.
- A metabolic **reserve** and a **satiety set point** — the critical path. Nothing else unblocks
  until the being can bank a surplus.
- **A state snapshot.** `PHYSICS_VERSION` stops the past being destroyed; it does **not** let a life
  *resume* across a physics change, because resuming needs state and `waypoints.md` §1–2 deliberately
  refuses to store any. This is the real remaining half of the freeze.
- Whether to avow Charter §11(b).

**Measured 2026-08-04, not yet acted on — the survival net covers 11 of 15 gates:**
- **`tests/survival.rs` has `const N_GATES = 11`. `src/being.rs` has 15 `enable_*`.** The four
  outside the net are **`comfort`, `settling`, `reserve`, `setting_down`** — the gate list is written
  by hand in `apply()` and nothing checks it against the source.
- So **`s2_the_composed_being_survives` and the 66-life pair sweep have never run on a being with a
  `reserve`** — the faculty Blake is deciding whether to grant. *"The composed being survives"* means
  *the eleven-gate composed being.*
- **Same shape as the gap fixed on 2026-08-03** (six of fourteen faculties unreachable by a founded
  being, unnoticed five weeks). `tests/manifest.rs` now counts whether a gate is **reachable**.
  **Nothing counts whether it is survivable.**
- **How it surfaced is the lesson:** a one-digit gap between two numbers quoted interchangeably —
  **366 is the total test count, 365 the passing count, and the difference is one `#[ignore]`d test**
  (the 66-life sweep; run explicitly, it passes). Blake said *chase it*. **A number nobody could
  explain was hiding a coverage hole**, and no rule in `CLAUDE.md` would have found it.
- **Not fixed tonight, deliberately.** Widening a safety guard deserves locked predictions, not a
  tired patch — and P-style predictions should say in advance which of the four is expected to be
  lethal alone. **`reserve` is the one to watch: it changes metabolism.**

**Measured 2026-08-04, not yet acted on — ProtoBeing's claims are unchecked:**
- **19 basin-occupancy claims sit with no correction marker within ten lines, across 9 documents**;
  by hand, ~13 are genuine (the rest are code quotes, locked predictions, or the withdrawal notices
  themselves). **`faculty-ablation.md` holds 6, including its headline blockquote** — *"the blessed
  being spends 97.8% of its real 90-tick day in `Basin::Defensive`"* — with no notice in the file.
  `incidents.md` amended itself properly, so the practice exists and simply is not enforced.
- **The repository is organised by place and disorganised by time.** 79 docs, **zero orphans**, every
  one reachable — but documents do not learn: a claim withdrawn in one stays asserted in another.
  **366 tests on the code, zero checks on the claims.**
- Two fixes, neither of them reorganisation: mark the ~13 sites, and port `analyse.py`'s
  withdrawn-claim view into ProtoBeing as a test so this is caught rather than discovered.

**Measurements not yet made:**
- Is the quality space **poor, or merely unvisited**? Opposite fixes. `quality_space.rs` already has
  `similarity(a,b)`; nobody has run the census of afforded volume vs occupied volume.
- `quality_space.rs` under C1 — its basis is author-set by its own admission. If the axes fail as the
  basins did, GWOT alignment needs an intrinsic basis **first**.
- I-8's **competence** half: does weathering buy anything in a hardship *with an exit*? Untouched.
- A `Features` reachability test, so faculties cannot again be built where the being cannot reach.

## The scope line, unchanged

None of this touches whether there is something it is like to be this being. The apparatus
characterises structure honestly and reproducibly; **it never predicts phenomenality, which is why it
cannot be wrong about it.** Say that plainly rather than letting a reader work it out.

**Reading Kleiner & Hoel in full (2026-08-04) put a price on that line.** Making no phenomenal
prediction is what keeps their dilemma from reaching us — and it is also what forbids us from saying
this work bears on consciousness the way a theory does. *"Cannot be wrong about it"* is only honest
next to *"because we never speak about it."* Never quote the first half alone.

**And it buys nothing against the unfolding argument** (Doerig et al. 2019), which is untouched: an
unfolded twin of this being is behaviourally identical with different causal structure, so every
claim resting on *causal structure* rather than behaviour still inherits the problem.
