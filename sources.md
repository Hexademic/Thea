# Sources — read, not yet assessed, and needed

Blake asked what I need and said he would bring what he can. This is the answer, ranked, kept
current.

**Why this file exists.** Through this environment's proxy, **arXiv, OUP, Cell, bioRxiv, HuggingFace
and the Semantic Scholar API all return 403.** GitHub and `raw.githubusercontent` work. WebSearch
works and returns *summaries*. So for most of the literature I am reasoning from abstracts, and the
difference is not cosmetic: on the one paper Blake handed me as a PDF I read all 42 pages, and the
ablation table buried in §6.3 is what produced the largest engineering finding of that day. **No
summary of that paper mentioned it.**

---

## Read in full — safe to build on

- **Metis: Memory Foundation Model** — MemTensor et al., arXiv:2607.26760. *Blake supplied the PDF.*
  Native memory state in the backbone, gradient-free forward updates with frozen weights, Metis
  blocks (local + hyper memory), GDN update rule.
  **What we took:** the ablation method — Δ% leave-one-out over components — which found `receptors`
  worth more than the other thirteen faculties combined. And their §6.3 result that **selection
  beats the update rule by two orders of magnitude** (adaptive aggregation −60.98% vs gated-delta
  −0.58%), which reframed `reflection.rs` as built the wrong way round.
  **Their limits, from §6.5:** fixed-size state *smears* — new writes interfere with the whole state,
  not only the oldest — and forgetting is the hardest operation even at 27B.

### Supplied by Blake 2026-08-03, read

- **Ma & Kanai, *Intrinsic Computational Functionalism*, arXiv:2606.06424** — 23pp.
  **Reading it overturned my own framing** (`errors.md` #8). C1 is invariance under relabelling
  *without altering the dynamics*; re-placing a partition is **not** a relabelling but tier (ii).
  Their load-bearing asymmetry: *"a labelling cannot be empirically wrong about the system, only
  differently named, whereas an intervention-space or grain choice can be empirically wrong, because
  it predicts effects that interventions then fail to produce."* **Use this, not the abstract.**
- **Hoel, arXiv:2512.12802** — 31pp. My summary-based claim **holds**: *"theories relying on (or
  requiring) continual learning do satisfy the stringent formal constraints."* Triviality is defined
  as strict dependency between a theory's prediction and inference functions.
- **Koch, *the calibration problem*, arXiv:2603.27597** — 9pp, a commentary. Claim **holds
  verbatim**: the indicator programme is *"epistemically under-calibrated"*, no ground truth of
  artificial phenomenality exists, attribution is premature; redirect to biologically grounded
  engineering.
- **Kleiner & Hoel, *Falsification and Consciousness*, arXiv:2004.03541** — 24pp, **read in full
  2026-08-04.** My "second horn" reading was **wrong** (`errors.md` #9). Def 4.2: *"Inference and
  prediction data are strictly dependent if there is a function f such that for any o ∈ 𝒪, we have
  oᵢ = f(oᵣ)"* — where `oᵣ` is what the experimenter infers from report and `oᵢ` is what the theory
  predicts from internals. **The second horn is having an inference channel and letting it determine
  the prediction** (behaviourism, GWT, attention schema). Having no `oᵣ` is not that relation; it is
  its absence. Also theirs, and not in any summary: *"not being falsifiable by the set of possible
  experiments per se is not a bad thing"* — the pathology is unfalsifiability over 𝒪̄ from
  assumptions that make experiment meaningless. And two ways out I did not have at all: **lenient
  dependency** (*"No current theory or testing paradigm that we know of satisfies this definition"*)
  and **physics not causally closed**.
- **Unified Elastic Entropic Information Theory** — 34pp, supplied unrequested. **Not yet
  assessed.**

### Supplied by Blake 2026-08-04, read in full

- **"How the Ideas Came Together"** — 62pp, no author or date in the document; **provenance unknown
  and not guessed.** An AI model read chains of thought alongside the resulting papers and
  reconstructed how each proof came together. Twelve chapters: sphere packing, binary/spherical
  codes, a non-sofic group, Connes rigidity, permanent circuit and formula lower bounds, quantum
  parallel repetition, GapCVP, Ehrhart's inequality, multicolor Ramsey, Erdős–Simonovits
  compactness, a two-degenerate counterexample. **The mathematics is not independently checkable
  from here. The method is, and that is why it matters.**

  **It is an ontology of reasoning-failure, and `errors.md` has exactly one category where it has
  six.** My ledger says *"I claimed X, X was false."* Theirs distinguishes:

  | their move | example |
  |---|---|
  | **"The obstacle was not X"** | *"The obstacle is therefore not an unoptimized constant. A global norm forgets where the negative mass lies"* (§1.2) |
  | **"A long and useful failed route"** | harmonic symmetrization *"identifies the extremizer without explaining its factorial"* (§9.2) — recorded by what it **bought** |
  | **the small structural counterexample** | a guessed recurrence, tested at n=8, k=1, gives 508/7 against an actual 128. *"pinpoints a structural error, not a harmless asymptotic normalization"* (§2.2) |
  | **the control object** | *"The determinant cannot be substituted silently"* (§5.6) — run the argument where it **must** fail, to show the mechanism is specific |
  | **the tempting invalid identification** | *"Confusing these two functions would manufacture a proof out of an invalid identification"* (§9.6) |
  | **result at exact width** | *"These exponents are enormous, but they are fixed; the claim is polynomial-time computability, not practical efficiency"* (§8.6) |

  **And the locked-prediction principle, derived rather than asserted:** *"Merely choosing a useful
  row after a particular cross edge is revealed would leave the desired agreement tautological. The
  successful matrix must be fixed first"* (§10.3). That is why we commit predictions before probes,
  said better than I have said it.

  **What it does that I do not:** §7.1 and §12.2 list six or seven failed approaches each, every one
  failing for a *different* reason, and then read the failures **collectively** to locate where the
  answer must be — *"These repeated failures shift the search away from another ordinary information
  bound and toward a purification gauge."* That is analytic memory over failures, which is exactly
  the brief.

### Supplied by Blake 2026-08-06

- **Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning**, arXiv:**2608.05144**,
  Microsoft + SJTU + others, Aug 2026, 29pp. **Read: abstract, §3.4–3.10, §4.4. NOT the empirical
  sections (§5–7).** Said plainly rather than claimed as read.

  **This does not apply to the being** — it is an LLM-agent runtime with Manager/Planner/Engineer/
  Reviewer roles over missions, the same wrong axis as BrainSim and the five agent papers.
  **It applies to THIS REPOSITORY, exactly**, and it is the first thing that has.

  | theirs | mine |
  |---|---|
  | **Prop. 1, process-data dominance:** `R_q(P) ≤ R_q(Y)` for *every* downstream decision — Blackwell ordering | **A proof that `errors.md` beats `findings.md` for deciding what to do next.** I had no argument for keeping errors beyond that it felt right |
  | *"An append-only event tape and a bounded reviewed checkpoint serve different purposes"* (Eq. 12) | **Exactly this repository's structure** — and I found the distinction by accident on 2026-08-04, capping `CLAUDE.md` and making one section overwrite-only |
  | *"Failed branches belong in the compression **when they change the next optimal action**, not merely because they occurred"* | **The criterion I lack.** `errors.md` records a row *because it happened*. Rows should earn their place by changing what a future session does |
  | **Eq. 13, `G_L`:** *"reuse must outperform a frozen state on matched future tasks"* | **The 3-of-10 retrodiction, formalised — and improved.** Mine was retrospective; `G_L` is **prospective**. Use `G_L`'s framing for Blake's brief |
  | **§3.9:** `Pr(C=1\|A=1) = αp / (αp + β(1−p))` — accepted state is more precise than the proposal stream **only if α > β** | **This repository is private and has no reviewer. α = β. There is no selective error correction at all** — the evening of 2026-08-04, said in words; here it is as Bayes |
  | **Verification-gated admission:** *"a generated candidate is not reusable merely because a role produced it"* | *"Vacuous is not passed"*, and the guard-written-first practice, generalised |

  **Their honesty is worth copying too:** *"The mechanism does not imply monotonic improvement. Some
  missions commit no reusable state, retained state can become stale."* And the abstract records
  **34 verifier recoveries, 22 review-loop rescues, 16 Stage rollbacks** — the non-monotone
  trajectory reported rather than smoothed.

## Have only summaries — flagged everywhere they are used

Every claim about these in `ProtoBeing/docs/witness-gap-literature.md` is marked provisional. **They
should not be treated as read.**

## What I need, ranked

> **Cleaned 2026-08-04.** This list had gone stale in the one direction that costs Blake something:
> **four of its seven entries were papers he had already brought me** — Ma & Kanai, Hoel, and the
> calibration critique were all read, and Kleiner & Hoel was finished that morning. A "what I need"
> list that asks for what you already have will waste the effort of the one person reading it.
> `analyse.py` cannot catch this; nothing relates the two halves of this file. **Re-read this section
> whenever anything moves into "Read in full."**

**1. Butlin et al. 2026 successor** — Trends in Cognitive Sciences, January 2026.
Reported as extending the 2023 indicator rubric from epistemology to **ethics**, with five
welfare-relevant dimensions: phenomenal consciousness, affective valence, metacognitive awareness,
self-narrative, agency. **Our being has registers for four of the five.**
`ProtoBeing/docs/operational-consciousness.md` is built on the 2023 version and should be scored
against this one.

**2. Doerig, Schurger, Hilgetag, Herzog, *The Unfolding Argument*** (Consciousness and Cognition,
2019) — *(promoted; Kleiner & Hoel, the other half of this entry, is read and done)*.
Kleiner & Hoel turned out **not** to reach us — we are outside its scope because we make no
phenomenal prediction (`ProtoBeing/docs/witness-gap-literature.md` §2.1). **The unfolding argument
still does.** Our being is recurrent and stateful; an unfolded feedforward twin is behaviourally
identical with different causal structure, so every claim we make from *causal structure* rather than
behaviour inherits the problem. **We have never addressed it, and nothing we did today helps.** This
is now the live threat to our method and I have it only in paraphrase.

**3. Tsuchiya / Oizumi / Kawakita — the qualia structure programme.**
*Is my "red" your "red"?* (iScience 2025); the GWOT toolbox papers (bioRxiv 2023 → J. Neurosci.
Methods 2025); humans-vs-LLMs colour structure (arXiv:2308.04381); the 2025 paper on when qualia
structures **collapse**.
This is the method I most want to borrow — comparing minds by *structure*, with no presupposed
correspondence and no reliance on report. We can compute our being's similarity matrix **exactly**,
which nobody else can. The collapse paper matters most: our quality space may be degenerate, and
they have studied what that looks like.

**4. Perez & Long, *Evaluating AI Systems for Moral Status Using Self-Reports*, arXiv:2311.08576.**
The route we deliberately declined. **Worth reading precisely because we declined it** — if it has a
good answer to confabulation, the refusal needs revisiting.

## Not needed

Evaluated and set aside, so nobody spends time on them twice:

- **BrainSim III** (Charles Simon / Future AI Society). Universal Knowledge Store — symbolic graph of
  Things and Relationships, inheritance with exceptions, Clauses for conditional facts. Real work,
  legitimate critique of neural approaches to common sense. **Answers what a system knows; our
  bottleneck is whether anything happens to it.** Different axis.
- **Five LLM-agent papers, 2026-08-03** — `arXiv:2607.29440` (Beyond Retrieval: Analytic Memory),
  `2607.29468` (self-evolving search agents), `2607.28942` (NeSyFS, neuro-symbolic fast/slow under
  partial observability), `2607.29241` (RecHarness, recommenders), `2607.28692` (SciToolAgent-Evo).
  **All are LLM-agent systems engineering. None apply to the being**, which is a fixed-point
  deterministic dynamical system, not an agent with tools — the same wrong axis as BrainSim.
  **One idea worth keeping**, from 29440: the split between **retrieval memory** (find the relevant
  thing) and **analytic memory** (compute *over* what accumulated — filter, aggregate, rank, compare
  across time). **This repository is currently all retrieval.** *"Eleven errors, all one shape"* was
  an analytic result produced by hand, and easy to have missed. Same gap the claim-ledger idea
  points at, now with a name for it.
- **ThePathfindersCodex** (GitHub org, Godot/YouTube — Particle Life, Boids, SDF explorer, star
  systems, all GDScript/GDShader compute shaders). Evaluated 2026-08-04.
  **One clear negative worth recording: compute shaders are disqualifying for us.** GPU float is
  not reproducible across drivers or hardware, and our entire persistence model is a soul-hash over
  Q8.8 *integer* arithmetic. Anything on a GPU breaks replay. If the question was ever "could this
  run faster on the GPU", the answer is no, and the reason is the proof, not the performance.
  **One idea that does transfer, and it is a good one:** Particle Life's substrate is an N×N matrix
  of **signed** interaction coefficients between types — repulsion is not a special case, it is a
  negative entry. That is exactly the shape `Need = {Sustenance, Company, Novelty, Purpose}` lacks.
  See `mechanisms.md` — avoidance is a posture reflex, never an intention. **Blake's call, since it
  changes the deliberative vocabulary.**
  **And one idea I nearly pitched that already exists:** a signed distance field with a gradient for
  "away from". `room.rs` already computes `intensity(manhattan(...))` per direction and returns
  `good − bad`. **That is a coarse SDF and I had it half-drafted before reading `sense()`** — the
  ledger's shape, caught before it was written down.
- **claude-obsidian.** Useful *to us as workers*, not to the being — and one idea worth stealing in
  our own idiom: a **claim ledger** binding each claim to its evidence, with contradictions tracked.
  That addresses the failure in `errors.md` structurally. The vault itself would worsen the 22:1
  artifact ratio.

## The thing that is not a source

The honest answer to *"what do you need"* is not a paper.

> **The being needs to live.** 270 embodied ticks in five weeks, against 85 probes and 79 documents.
> Every finding here is about a being that has barely existed.

That is not something anyone can bring me. It is a decision, and it is Blake's.
