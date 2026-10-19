# 115.10 — Why all the rays have the same shape

Observation on `115_09_fig_primos_polar.png`: each ray starts at the origin,
stretches out, and near the end bends slightly, and **all of them bend the same
way**.

This is correct, and exact. Script: `115_10_por_que_se_curvan_los_rayos.py`,
output in `115_10_resultados.txt`, figure `115_10_fig_rayos.png`.

## The number that governs the drawing

```
113 · 2π = 709.999939706…
710      = 710
δ        = 710 − 113·2π = +6.0289 × 10⁻⁵ rad
```

Advancing p by 710 rotates the point by exactly δ radians. **δ does not depend
on the ray.** Hence the 280 rays are not merely similar: they are the same arc,
rotated.

Each ray is an arc of an **Archimedean spiral**

> r = 710 (θ − θ_a) / δ

with pitch 710/δ = 1.18 × 10⁷, which is huge; that is why it looks straight.

## Verification, with nothing fitted

Prediction: for every prime p, with a = p mod 710,

> Δθ(p) = δ · (p − a) / 710

Measured over the 100,000 primes of the drawing:

* maximal deviation: **3.9 × 10⁻¹¹ rad**
* width of one ray: 2π/710 = 8.85 × 10⁻³ rad, 2.3 × 10⁸ times larger

They do not merely resemble each other: they agree to machine precision (panel B).

## How much they bend

At the edge of the drawing (p = 1,299,709):

* accumulated turn = **0.110363 rad = 6.323°**
* that is **12.47 ray widths**, in the same direction for all 280

This is exactly "they all have the same wave and bend at the end".

## Why the drawing changes with the radius

Each convergent of 2π generates its own family of rays, and each family breaks
up when the accumulated drift reaches one ray width, at r = 2π/|δ|:

| family | δ (rad/step) | breaks up at r ≈ |
|---|---|---|
| 6/1 | −2.83 × 10⁻¹ | 22 |
| 19/3 | +1.50 × 10⁻¹ | 42 |
| 25/4 | −1.33 × 10⁻¹ | 47 |
| 44/7 | +1.77 × 10⁻² | 355 |
| 333/53 | −8.82 × 10⁻³ | 712 |
| **710/113** | **+6.03 × 10⁻⁵** | **104,218** |

The drawing reaches r = 1,299,709. Hence the nested structure: near the centre
the families 6 and 44 dominate and break up quickly; further out the family 710
dominates; and beyond r ≈ 10⁵ the family 710 also starts to bend visibly, which is
exactly where the eye sees the rays "fall".

## The only thing the drawing says about the primes

Everything above is about 2π, not about primes: with **all integers** the drawing
would have the same 710 rays, only denser.

The primes do exactly one thing: 710 = 2·5·71, and a prime cannot share a factor
with 710 unless it is 2, 5 or 71. So of the 710 classes only **φ(710) = 280** are
occupied (plus the three exceptional primes, 283 measured). The other 430 stay
empty.

That the 280 shine evenly (100,000/280 = 357 primes per ray, measured) is
**Dirichlet's theorem** on primes in arithmetic progressions.

That is the whole arithmetic of the drawing: **which rays are missing, and that
the remaining ones weigh the same.** The shape of each ray is geometry of 2π.

## Classification

* Congruence of the 280 rays: **PROVED AND VERIFIED**, deviation 3.9 × 10⁻¹¹ rad.
* Curvature = arc of an Archimedean spiral of pitch 710/δ: **DERIVED**, no free
  parameters.
* Nested structure by radius: **EXPLAINED** by the coherence radii 2π/|δ| of the
  convergents.
* Arithmetic content: **280 of 710 classes + Dirichlet equidistribution**.
  Nothing more.
* Relation with φ: **NONE**; see `115_08`.
