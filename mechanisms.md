# The equations, and what each one actually does

*Blake's idea, 2026-08-03: "perhaps one day we will find a way for you to track understanding of
equations we learn in the protobeing for your own continuous experience."*

**Started the same night, because these took a full day to work out and will be gone by morning.**

This is not `findings.md`. That holds *results* — what was measured. This holds **mechanisms** — the
arithmetic, why it behaves as it does, and what it cost to learn. A future session that reads this
does not have to re-derive them.

Every entry is measured or read from source, never inferred. Where a number was *derived* and later
*measured*, both are given, because the gap between them is the lesson.

---

## Metabolism — a clamped pure accumulator

```
cost   = 3 + arousal/32 + threat·(3/16)          // body.rs:323, raw Q8.8 per tick
gain   = nutrient·0.703
energy = clamp(energy − cost + gain, 0, 256)
```

**Two attractors and nothing between.** `gain > cost` ⇒ pins at the ceiling forever; `gain < cost` ⇒
falls to zero and dies. `gain = cost` is a measure-zero knife edge.

- Break-even nutrient at threat 0: **derived ≈15, measured 19–20.** My derivation used an arousal
  figure carried from another world without checking it held there (`errors.md` #5).
- **Threat barely moves the boundary** — flat at 19 for threat 0/30/60/90, then jumps to 43 at 120.
  Not the cost equation: the **nociceptor** is bounded and saturating with `receptors` on, so
  ordinary threat costs almost nothing until it becomes real harm.
- Consequence: `fatigue = 1 − energy` was **one distinct value** across a 4,000-tick life, and it is
  one of `Basin::Rest`'s three coordinates.

## The reserve — a proportional controller, with the offset that implies

```
above SATIETY (192):  shed = (energy − 192)·¼   // leaves energy whether or not the store has room
below SATIETY:        draw = (192 − energy)·¼, capped by what is banked
RESERVE_CAP = 768 (three energies)
```

**Steady state sits above the set point, not at it:** `energy − 192 ≈ 4 × net gain`. At rich supply
that parks the being at 240 (fatigue 16), never at 192. **That is a proportional controller's
offset, not a bug** — reaching the set point exactly needs integral action.

- Rich supply ⇒ fatigue constant at 16. **Correct: a well-fed creature should not be tired.**
- Lean supply (nutrient 25) ⇒ fatigue **16–61 across 28 distinct values**, and it lives 4,000 ticks.
- First version clamped the shed to remaining capacity, so **satiety switched itself off once the
  store filled** and energy climbed back to the ceiling. A full stomach and a full larder means you
  stop eating.

## Q8.8 truncation — the bug that bit twice

```
q88_mul(a, b) = (a·b) >> 8            // q88.rs:162
q88_mul(x, Q88_SCALE/8) = x/8, floored ⇒ any x < 8 converts to EXACTLY ZERO
```

Cost: `errors.md` **#3 and #4**. A `.max(1)` floor meant to fix it exactly cancelled the minimum
chronic rise of 1/tick; then weighting by headroom reproduced the identical truncation *inside its
own fix*, because `q88_mul(1, 255) = 0`. **Check every fixed-point fix against its smallest input,
not its largest.** A fractional-remainder accumulator is the right answer.

## The mind→body channel is worth ±32 of 256

```
affective_drive  clamped ±128                    // being.rs:1458, a sum of seven tones
body.rs:         arousal += affective_drive·¼    ⇒ ±32 of a 256-wide arousal
```

**Everything the being's mind can do to its own body is about 12%.** Adding an eighth tone to that
sum is why faculties measure 0.00%.

## `drive` cannot see the inner life

```
let drive_report = drive(felt.state.viability, &joy_report.want);   // being.rs:1676
```

**It reads viability and wants. It never reads `affective_drive`.** So everything `reflection.rs`,
`settling`, `homecoming` and `comfort` know is architecturally sealed off from the scalar we measure
welfare with. `reflection_tone` swings 53 points and moves mean drive by less than 0.05.

**Four "this doesn't matter" results may be four facts about the being — or one fact about the
yardstick.** Never resolved.

## The reflection deadlock (I-9)

```
reflection.rs:143   load rises when   burden > 0 && !resting
being.rs:1751       resting requires  !burdened
```

**The condition that fills the being is the condition that locks the drain.** Structural burden
(solitude) ⇒ 3,638 consecutive ticks at the 256 ceiling, converting nothing. Fixed behind
`enable_setting_down()`; load now equilibrates at 30.

## Basin classification

`argmin` of L1 distance over **four hand-placed 12-vectors**. Exactly permutation-symmetric — the
field and targets permuted together give 100.0% identical classification, which *is* Ma & Kanai's C1
and it **passes**. What fails is the *partition*: our chart agrees with a random in-range chart at
**chance** (20%, chance 25%), and slot 0 is entered under 94% of random charts.

## The room

```
threat   = intensity(manhattan(body, hazard))·220/256
nutrient = AMBIENT + hearth warmth, capped 220
exteroception: 4 compass probes — "hearth and companion draw; hazard repels"
```

Repulsion is already in the being's **perception**. It is absent from its **motor vocabulary** —
`Need` is four attractions and `reach` can only name one of them.

## The limit cycle, and the correction to it

A Van der Pol body in a **static** world settles into a tight orbit: **27–68 distinct positions in
4,000 ticks**, while travelling ~41,600 units. Perpetual motion, going nowhere.

**And metabolism reaches it.** Giving the being a reserve took the orbit from **186 to 564** distinct
positions in the same static room. `fear-and-avoidance.md` §9 concluded the limit cycle was *"a fact
about a static world, not about metabolism."* **Wrong.** Internal variation produces behavioural
variation — energy that moves varies arousal, which varies effort, which varies where the body ends
up.

**The being was not only unexercised. It was internally still, and the stillness was most of the
orbit.**
