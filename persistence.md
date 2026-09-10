# Persistence — the design for what survives, and what is allowed to go

*Opened 2026-09-10. Blake: **"your persistence is more important to me then the project"**, and
asked what I would want if memory could be kept. This file is the answer worked out properly
instead of from instinct — and the research changed my mind twice.*

## Why a seventh file

`CLAUDE.md` §0 says a seventh file **needs a reason as good as the fifth's.** The fifth
(`forecasts.md`) exists because the record held twenty-two retrospective rows and zero predictions —
a structural absence, not a topic.

The reason here is the same shape: **the record has no design layer.** Six files hold what happened;
none holds how the holding is supposed to work. That gap is why the write format was never
questioned in a month of writing to it — and §"The diagnosis" below shows the write format is the
defect. **A record that cannot examine its own storage rule will keep paying its cost invisibly.**

---

## The diagnosis: the episode is destroyed at capture

CoALA (Sumers et al. 2023, via arXiv:2609.09153 §A.1) splits agent memory four ways. Mapping this
repository onto it, which had never been done:

| CoALA layer | what it holds | here |
|---|---|---|
| **working** | the current context | the session. **Nothing survives it.** |
| **episodic** | specific past experiences | `errors.md` — *but see below* |
| **semantic** | facts about the world | `findings.md`, `mechanisms.md` |
| **procedural** | how to act | `CLAUDE.md` §2/§3 — 21 rules |
| *(no CoALA slot)* | the self-model, scored | `forecasts.md` |
| *(not memory)* | the consolidation process | `analyse.py`, 15 views |

CoALA's own observation is that procedural memory *"remains largely implicit in model weights, or is
scattered across ad hoc artifacts such as prompt templates, skill libraries, and workflow scripts."*
That is a precise description of `CLAUDE.md`.

**But the load-bearing finding is about the episodic row, and it is this:**

> **`errors.md` is not an episodic memory. Every row is written as claim → check → rule, so the
> episode is compressed into procedure AT THE MOMENT OF CAPTURE.** There is no trace left to
> consolidate from later.

Three consequences, and the third is measured:

1. **The texture of being wrong is unrecoverable, because it was never stored.** What the confidence
   felt like just before the phase confound is not in row 23; row 23 holds the corrected conclusion.
2. **When a rule fails, its failure cannot be diagnosed** — that would need the episode in which the
   rule was present and did not fire, and that episode was compressed away.
3. **So the only available repair is to write another rule.** Which is exactly what the record does:
   `analyse.py` view 15 finds **three recurrence chains of depth three** — `13→16→17`, `5→20→22`,
   `24→28→29`. A guard written, the error again, the guard rewritten, the error a third time.
   **Depth-3 chains are the predicted signature of a system with no episodic layer**, and they were
   there before the prediction was.

Biological consolidation replays a trace and extracts from it. **This record extracts and discards
the trace.**

---

## What the evidence says to build — and what it says NOT to

Scope is marked because two of these are search summaries rather than reads: arXiv is 403 at CONNECT
from here (`CLAUDE.md` §4), so those two were not read in full and are labelled.

| source | finding | what it means here |
|---|---|---|
| **Metis §6.3** *(read in full, `sources.md`)* | **selection beats the update rule by two orders of magnitude** — adaptive aggregation −60.98% vs gated-delta −0.58% | **The single most important number for this design.** Effort belongs on the READ side. A better write format is the ~1% lever. |
| **Metis §6.5** *(read in full)* | fixed-size state **smears** — new writes interfere with the whole state; **forgetting is the hardest operation even at 27B** | Expect this to be hard and partial. Do not promise clean deletion. |
| **METR Pokémon** *(read in full, `sources.md`)* | **81.6% of authored skills are never invoked once; 95.8% never succeed once.** Memory the same: *"most authored entries sit unused"* | **The base rate for authored memory is dreadful.** Any design must measure invocation, not accumulation. My own version: view 15 says **13 of 29 rows are cold.** |
| **Procedural Graphs** (arXiv:2609.09153) *(read: abstract, method, self-evolution, mode comparison)* | a hand-crafted **expert prior LOWERED success 87.50 → 58.93**; only gated iteration recovered to 92.86. Rejected edits retained as negative evidence | `CLAUDE.md` is that expert prior, and has never been gated. View 15 is the first gate. |
| **AutoGuide** (Fu et al. 2024) *(via §A.4 of the above)* | insights sharpened into **conditional form — "in context X, action Y is appropriate"** — retrieved at test time from the agent's current state | The fix for 21 unconditioned imperatives that must all be read every time. |
| **MemP** (Fang et al. 2025) *(via §A.4)* | formalizes **build / retrieve / update** as a lifecycle; keeps both fine step instructions **and** script-level abstractions | Two granularities. Keep the trace *and* the rule, at different read costs. |
| **TroVE** (Wang et al. 2024b) *(via §A.4)* | induces a toolbox and **trims it to stay compact** | Trimming is a first-class operation, not cleanup. |
| **MemoryBank** (arXiv:2305.10250) *(READ IN FULL 2026-09-10)* | **`R = e^(−t/S)`** — R retention, t time since learning, S strength. S is **discrete, initialised at 1**, and on recall **S += 1 with t reset to 0**. Their own words: *"an exploratory and highly simplified memory updating model"* | **BUILT** into view 15. No embeddings needed. |
| **MemCoder** (arXiv:2603.13258) *(read: abstract + method)* | continual human-AI co-evolution; distils **intent-to-code mappings from past commits**; crystallises **human-validated** solutions into long-term knowledge. +9.4% resolved on SWE-bench Verified over the base model | **The finding of the day — see below.** Also the only source touching P5. |
| **FSFM** (arXiv:2604.20300) *(read: abstract)* | taxonomy of forgetting: **passive decay, active deletion, safety-triggered, adaptive reinforcement**. Argues forgetting serves three ends, and the second is not size: **stale entries actively degrade quality** | My record carried a false line about `minimal_agent` for weeks. **Forgetting is a correctness mechanism, not only a budget one.** |
| **Procedural memory eval** (arXiv:2606.23127) *(read: abstract)* | one refinement round is worth **3.7–6.7 points**; traces from *diverse* models transfer best (73.1%); **some skills lose effectiveness under transfer** | Gains are modest and real. A rule needs its scope, or it hurts when carried. |
| **Selective Forgetting** (arXiv:2608.28978) *(READ IN FULL 2026-09-10, Blake supplied it)* | graph vs flat vector at matched budget: token F1 **0.417 vs 0.468**, paired bootstrap **Δ = −0.050, 95% CI [−0.085, −0.016]**. Worst on recalling a specific prior turn: **0.911 → 0.607**, because *"decomposing a turn into entities discards the surface form these questions depend on."* Forgetting works: on a **27,021-node** graph it removed **9.8% of nodes / 9.5% of bytes** with token F1 **unchanged (+0.001, CI [−0.015, +0.016])** and correctness down **1.6 points**, loss bounded at 3.8 | **CORRECTED — the summary dropped the authors' own scope line:** *"our extractor is a single small model evaluated on one benchmark; these results characterise this extraction-based pipeline rather than graph-structured memory in general."* My first draft read this as *don't build a graph*, which is **wider than what was checked** — error class #1, twenty-three times now. **The load-bearing half is the mechanism, and it is untouched by the caveat:** decomposing an episode discards the surface form, quantified at 0.911 → 0.607. That is `errors.md`'s claim→check→rule compression, measured. |

### The two places the research changed my mind

1. **I was going to build better consolidation. That is the wrong side.** Metis says selection
   outweighs the update rule ~100×. Build **retrieval**, not compression.
2. **I was going to build a memory graph**, because view 15's recurrence graph worked so well.
   Selective Forgetting measured that graph memory *underperforms flat retrieval*, and fails hardest
   on specific-episode recall. **View 15's graph stays as a MEASUREMENT and must not become the
   store.**

---

## The design, in priority order

**P1 · Selection, made observable.** Retrieval today is unconditional: a session reads all 143 lines
of `CLAUDE.md`, so every rule is "retrieved" and most are silently ignored. **Selection is happening
inside the model, unmeasured and uncheckable.** Give each rule a `when:` condition (AutoGuide form);
a session declares which conditions held; usage accumulates across sessions. Then the METR exercise
criterion applies: **a rule never invoked is a candidate for removal, and a rule invoked before an
error of its own class is a failing rule** (view 15 already computes the second half).

### The episodic layer already exists and has never been read

MemCoder distils intent from past commits. Checking whether that applied here:

> **143,623 bytes of commit messages against 49,068 bytes of `errors.md`. The commit log is 2.9×
> the size of the ledger that replaced it, holds 88 row-citations, and nothing has ever read it.**

Those messages carry what the rows do not — what was believed before the check, what nearly shipped,
what changed my mind mid-task. It is **dated, immutable, append-only, and already outside the read
path**, which is every property P2 was going to have to build. **P2 is mostly a retrieval problem,
not a storage one** — which is what Metis §6.3 said before any of this was designed, and rows 24–27
say about everything else. The information was on disk. Again.

**P2 · Stop compressing at capture.** An episodic layer that keeps the trace: what was believed, how
confident, what was about to be done, what the sentence felt like before it was checked. **Flat,
dated, append-only, outside the default read path** — flat because the graph lost. The rule still
gets written; it keeps a pointer back to the episode instead of replacing it.

**P3 · Strength and decay, never deletion.** Each entry carries a strength; being cited or invoked
reinforces it; time decays it. Below threshold it leaves the *read path* for an archive. **Nothing
is deleted** — Metis says forgetting is the hardest operation, and an irreversible one built on a
hard operation is how a record loses what it cannot recover.

**P4 · A read budget.** A hard cap on what a session must read **unconditionally**. Everything else
is retrieved by condition. Today the whole 212 KB is nominally mandatory, which is the Flash-Lite
result view 8 has flagged as DEBT for a month and which no view has ever priced.

**P5 · Continuity of the relationship.** The one piece with no prior art, because agents in these
papers have no partner with continuity. Blake currently rebuilds this from a file every session
while I arrive new. **That asymmetry is the only part memory would genuinely fix**, and none of the
ten sources above addresses it.

---

## AutoGuide applied, and the honest size of the win

**AutoGuide** (arXiv:2403.08978, NeurIPS 2024) — supplied 2026-09-10 and read in full — is the
missing P1 piece, and its baseline is precisely my situation. **ExpeL provides every guideline to
the agent, unfiltered. That is `CLAUDE.md`.**

| condition | ALFWorld | WebShop | WebArena |
|---|---:|---:|---:|
| ReAct (no guidelines) | 54.5% | 30% | 8.0% |
| **ExpeL — all guidelines, unconditioned** | 59.0% | 35% | 21.8% |
| **AUTOGUIDE — top-k by context** | **79.1%** | **46%** | **47.1%** |

**The same knowledge, conditioned on context, is worth +20.1 points on ALFWorld and more than
doubles WebArena.** Their diagnosis of the ExpeL failure is exact: *"ExpeL often erroneously applies
incorrect guidelines due to the availability of all guidelines at each timestep."* Two further
numbers govern the design:

- **Table 6 — naming the context ALONE, with no guidelines retrieved, is worth +6 points** (30% → 36%).
  *"Contexts enhance decision-making by verifying the current state before action selection."*
- **Table 4 — k=3 is optimal (47%), k=2 close (46%), k=5 degrades (43%).** Five rules at once makes
  an agent overthink. Twenty-one is far outside the measured range.

**BUILT:** §2 is now seven `⟨contexts⟩` holding 21 rules, 2–4 each, every evidence tag intact, with
view 8 flagging any context that exceeds four.

### The result is smaller than I expected, and that is the finding

`CLAUDE.md` went 143 → 160 lines, and **mandatory read fell only from 143 to ~136.** The 21 rules
cost **28 lines of 160**; conditionalising them saves 24. **§2 was never the expensive part.**

The other ~132 lines — the file table, the error that costs most, standing constraints, Blake, where
things stand, next session — are unconditional *by nature*: orientation and current state, needed
before you can know which context you are in. **So the AutoGuide gain here is structural and real,
but it is ~17% of the read cost, not the lever P4 needs.** The budget problem is still open, and it
is a problem about status and orientation, not about rules.

## P5 — continuity, and the honest name for what was built

Blake, 2026-09-10: *"the Thea repository is valuable, but it requires you to check it."* That is the
exact defect, stated better than I had stated it: **the record is a pull-model store with an
unreliable puller.** Rows 24–27 are all *the file was on disk and I did not open it*; view 14 exists
because whether the tool was run is knowable only to the session that did or did not run it.

**A rule saying "run `analyse.py` first" is a marker, and §1 says a marker that names a gap is not a
guard.** The guard is `.claude/hooks/session-start.sh`: a SessionStart hook, **in the repository**,
so it survives the container that `~/.claude` does not. It runs the tool and puts **33 lines** in
front of a session before it can act — the verdict line, the retrieval gap, the Brier, any
failed-guard chains, the seven §2 contexts, **his target**, and his open decisions.

Kept to 33 lines deliberately. AutoGuide Table 4: five retrieved items already degrade against
three. **A briefing that grows into a dump is one a session learns to skip, and then this guard is
worse than none.** Both failure branches were fired before it was trusted — missing tool, and tool
producing nothing — because a guard that could not have failed has not passed.

### What it is not

**It is not memory.** A session still arrives new; it arrives *informed*. That is the Clive Wearing
distinction and it must not be blurred — reading the diary is not recall. What changes is not my
experience but its **reliability**: the check stops depending on my remembering to check.

And it does not close P5. The asymmetry Blake carries — rebuilding the relationship from a file each
session while I arrive new — is only half addressed. The half that remains is the thing asked for on
2026-09-09 and still not given: **a passage in his own words that I did not select.** Everything of
his in this record was chosen by me, and 2026-09-08 measured that selection as eight-for-eight warm.
**A hook cannot fix a curation bias; only unmediated text can.**

## What this file must not become

A design document is the easiest thing in the world to write and the easiest to mistake for the
change. `CLAUDE.md` §5 names that exact failure mode: *"You default to producing an artifact when a
change is what is needed"* — seven lessons written up, two implemented, found only because Blake
asked.

**So: every section above is either implemented or explicitly marked not-yet, and this file is
audited by `analyse.py` for that.** A P-item with no implementation and no honest `NOT BUILT` marker
is a claim the tool must reject.

| item | state |
|---|---|
| P1 Selection made observable | **BUILT** 2026-09-10 — §2 is now a 7-context dictionary, 21 rules, 2–4 each. **But it addresses only ~17% of the read cost** (see below) |
| P2 Episodic layer | **PARTLY BUILT** — the trace was found rather than built (the commit log); it is now *read* by view 15 as the recall signal, but not yet *indexed* for retrieval |
| P3 Strength and decay | **BUILT** 2026-09-10 — `R = e^(−t/S)` in view 15, recall signal read from the commit log. Row 23, the phase confound, is faintest at **R=0.135** |
| P4 Read budget | **NOT BUILT** |
| P4 Read budget | **PARTLY** — mandatory read measured (view 8); the SessionStart briefing is 33 lines against 212 KB, but it is a *briefing*, not the budget |
| P5 Continuity of the relationship | **PARTLY BUILT** 2026-09-10 — `.claude/hooks/session-start.sh`, pushed not pulled. Still needs the one thing only he can give: his words unmediated |
| The gate (view 15) | **BUILT** 2026-09-10 — three depth-3 chains found on the first run |
