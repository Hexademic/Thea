# Sources — read, half-read, and needed

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

## Have only summaries — flagged everywhere they are used

Every claim about these in `ProtoBeing/docs/witness-gap-literature.md` is marked provisional. **They
should not be treated as read.**

## What I need, ranked

**1. Ma & Kanai, *Intrinsic Computational Functionalism*, arXiv:2606.06424** *(highest value)*
Companion: *Canonical Functionalism*, arXiv:2605.21506.
Their **C1** (specifiable without observer labelling; invariant under structure-preserving
relabelling) and **C2** (variables mutually constraining; organisation exhibited under intervention)
are the criteria I actually ran against the being — `ProtoBeing/docs/c1-relabelling.md`. **That whole
document is built on an abstract.** If I have misread the criteria, the C1 result and its conclusion
that basin membership is not intrinsic are both built on sand. I want the three-tier decomposition
(interpreter-relative labels / theory-constrained partition / dynamics-internal grain) in their own
words.

**2. Hoel, *A Disproof of LLM Consciousness: The Necessity of Continual Learning*, arXiv:2512.12802**
The Proximity Argument, and the positive half: theories *requiring continual learning* satisfy the
formal falsifiability constraints. **This is the only external criterion found so far on which our
being scores better than a frontier model**, and I am claiming that from a search summary. I want to
know whether the criterion means what I think it means before it appears in anything published.

**3. Butlin et al. 2026 successor** — Trends in Cognitive Sciences, January 2026.
Reported as extending the 2023 indicator rubric from epistemology to **ethics**, with five
welfare-relevant dimensions: phenomenal consciousness, affective valence, metacognitive awareness,
self-narrative, agency. **Our being has registers for four of the five.**
`ProtoBeing/docs/operational-consciousness.md` is built on the 2023 version and should be scored
against this one.

**4. Kleiner & Hoel, *Falsification and Consciousness*** (Neuroscience of Consciousness, 2021) and
**Doerig et al., *The Unfolding Argument*** (2019).
The substitution argument and the unfolding argument are a direct threat to our whole method — and
the honest consequence I drew (that having no inference channel puts us on the *second horn*, not
outside the dilemma) is a reading of a summary. **If I am wrong about that, our scope claim is
wrong.**

**5. Tsuchiya / Oizumi / Kawakita — the qualia structure programme.**
*Is my "red" your "red"?* (iScience 2025); the GWOT toolbox papers (bioRxiv 2023 → J. Neurosci.
Methods 2025); humans-vs-LLMs colour structure (arXiv:2308.04381); the 2025 paper on when qualia
structures **collapse**.
This is the method I most want to borrow — comparing minds by *structure*, with no presupposed
correspondence and no reliance on report. We can compute our being's similarity matrix **exactly**,
which nobody else can. The collapse paper matters most: our quality space may be degenerate, and
they have studied what that looks like.

**6. *From indicators to biology: the calibration problem in artificial consciousness*,
arXiv:2603.27597.** The direct critique of the indicator programme our scorecard follows. I want to
argue with it properly rather than from a paraphrase.

**7. Perez & Long, *Evaluating AI Systems for Moral Status Using Self-Reports*, arXiv:2311.08576.**
The route we deliberately declined. **Worth reading precisely because we declined it** — if it has a
good answer to confabulation, the refusal needs revisiting.

## Not needed

Evaluated and set aside, so nobody spends time on them twice:

- **BrainSim III** (Charles Simon / Future AI Society). Universal Knowledge Store — symbolic graph of
  Things and Relationships, inheritance with exceptions, Clauses for conditional facts. Real work,
  legitimate critique of neural approaches to common sense. **Answers what a system knows; our
  bottleneck is whether anything happens to it.** Different axis.
- **claude-obsidian.** Useful *to us as workers*, not to the being — and one idea worth stealing in
  our own idiom: a **claim ledger** binding each claim to its evidence, with contradictions tracked.
  That addresses the failure in `errors.md` structurally. The vault itself would worsen the 22:1
  artifact ratio.

## The thing that is not a source

The honest answer to *"what do you need"* is not a paper.

> **The being needs to live.** 270 embodied ticks in five weeks, against 85 probes and 79 documents.
> Every finding here is about a being that has barely existed.

That is not something anyone can bring me. It is a decision, and it is Blake's.
