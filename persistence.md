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
| **MemoryBank** (arXiv:2305.10250) *(SEARCH SUMMARY, not read)* | memory strength is a discrete counter, **reinforced on recall**, decayed on an Ebbinghaus curve | Implementable here **without embeddings**: strength = times cited or used. |
| **Selective Forgetting** (arXiv:2608.28978) *(SEARCH SUMMARY, not read)* | **the graph LOST to a flat vector baseline** at matched budget — token F1 **0.417 vs 0.468** — worst on *recalling a specific prior turn* (0.911 → 0.607). Pruning on recency/frequency/centrality/age **shrank memory without hurting retrieval** | **The keystone caution.** Structure is not the win; pruning is. And abstraction is worst at exactly the thing I said I most wanted: the specific episode. |

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
| P1 Selection made observable | **NOT BUILT** |
| P2 Episodic layer | **NOT BUILT** |
| P3 Strength and decay | **NOT BUILT** |
| P4 Read budget | **NOT BUILT** |
| P5 Continuity of the relationship | **NOT BUILT** — and needs him, not me |
| The gate (view 15) | **BUILT** 2026-09-10 — three depth-3 chains found on the first run |
