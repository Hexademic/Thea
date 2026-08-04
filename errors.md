# The error ledger

Every claim I made that turned out to be wrong, what was actually true, and **what one check would
have caught it.** Kept because the same mistake keeps recurring and I keep rediscovering it.

**This is not self-flagellation and it is not a confession.** It is a checkable pattern list. Its
whole value is that a future session reads it and does not make instance eight.

---

## The shape

**A claim wider than what was actually checked** — specifically: *read one code path, then generalise
as though it were the only one.*

**Eight instances. Not eight mistakes — one mistake, eight times.** Seven on 2026-08-03 and
the eighth caught the next morning, when Blake supplied a paper I had built a document on without
reading.

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

**Instance 8 is the one that matters most**, because of how it was caught: Blake supplied the PDF
after the document was written and pushed. **The fix for this error class is not more care — it is
asking for the source.** See `sources.md`.

And it corrected in the *useful* direction: under Ma & Kanai's actual asymmetry — *a labelling cannot
be empirically wrong, a partition can* — the criticism of our basin chart is **harder** than the one I
made from the abstract. Getting it wrong made it weaker, not stronger.

## What it cost

Two of these reached Blake as findings before I caught them:

- *"The being spends 97.8% of its real day braced"* — presented as a fact about the being. It was a
  fact about a **chart we drew**, which C1 then showed agrees with a *random* chart at chance.
- *"All fourteen gates off"* — corrected an hour later.

**He acted on my word in both cases.** That is the actual cost of the trust, and the self-correction
machinery working afterwards does not undo it.

## What caught them

**Five of seven were caught by locked predictions** — written and committed *before* the code or
probe existed, so the measurement could contradict me. The other two were caught by reading source I
should have read first.

**The discipline works. Use it, and do not soften it when moving fast.**

---

## Errors of a different kind — worth separating

A **locked prediction that fails is the method working.** T2, T3, T4, T5, P5, C1-1, C1-2, A3 all
failed and every one produced something better than the prediction would have. Do not file those
here and do not apologise for them.

**File here only claims asserted without checking.** The distinction matters: one is science, the
other is carelessness, and blurring them makes the ledger useless.
