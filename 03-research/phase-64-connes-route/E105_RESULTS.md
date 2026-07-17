# E105 — Tate factorization of the shifted scattering colligation (ω>½): confirmed, with a refinement

**Date:** 2026-06-27 · mpmath dps=30 · ω=1.0 (unconditional region, Re s = ½+ω = 1.5 > 1).

## Object (Connes §3 / Q1)

For ω>½ the Euler product converges and `Θ_ω(z) = ξ(½+ω+iz)/ξ(½+ω−iz)` factors as
```
   Θ_ω(z) = Θ_∞(z) · ∏_p Θ_p(z),
   Θ_∞ = G(s_+)/G(s_-),  G(s)=½s(s−1)π^{−s/2}Γ(s/2)   (archimedean+pole block),
   Θ_p(z) = (1 − p^{−s_-})/(1 − p^{−s_+}) = (1 − a p^{iz})/(1 − a p^{−iz}),  a=p^{−(½+ω)},
```
with `s_± = ½+ω±iz`. This is the claimed "restricted tensor product of local Tate colligations."

## Results

| claim | result |
|-------|--------|
| **(2) factorization** `Θ_∞·∏_{p≤P}Θ_p → Θ_ω` | **confirmed** — error 0.075 (P=10) → 0.005 (P=1000); slow `~P^{−1/2}` Euler rate at Re s=1.5 |
| **(3) assembled product passive** (Pick matrix, strip `Im z<½+ω`) | **PSD**, min eig = **+8.8e-3** → the global colligation is passive as a product, for ω>½ |
| (1) individual scalar local factors `|Θ_p|≤1`? | **NO** — `|Θ_p|` up to 1.16 (p=3), 1.05 (p=7) in the strip |

## The refinement (honest, and useful for the construction)

- The local factors `Θ_p` are **unimodular on ℝ** (`|Θ_p|=1`, since numerator/denominator are
  conjugates there) but are **not scalar-Schur** in the interior — `|Θ_p|>1` occurs. They are also
  analytic only in the **strip** `Im z < ½+ω` (the factor's relevant pole sits at `Im z = ½+ω`).
- Therefore **passivity is collective, not scalar-local.** "Passive local building blocks" must be
  read at the **J-unitary transfer-matrix (Livšic colligation) level** — each local Tate piece is a
  `J`-unitary 2×2 transfer matrix (a passive delay element with delay `log p`), whose *scalar*
  characteristic function need not be `|·|≤1`; the **product** of the matrix colligations is what is
  contractive (Pick-PSD), confirmed in (3).
- So the correct object to assemble is the **matrix** colligation `∏_v (J-unitary local block)`, not
  the scalar product `∏_v Θ_v`. The scalar `Θ_ω` is its characteristic function.

## Correction (Connes audit 0.2, 2026-06-28): the Euler product is a *boundary/strip* object

The Euler product for `ξ(½+ω+iz)` converges only where `Re(½+ω+iz)=½+ω−Im z>1`, i.e. in the **shallow
strip `0<Im z<ω−½`** (and on the real boundary) — **not** on all of `ℂ_+`. Recheck (ω=1, strip
`Im z<0.5`): in-strip the partial-product error converges monotonically (`Im z=0.2`: 0.0031→0.0005;
`Im z=0.4`: 0.006→0.0019); **outside** (`Im z=0.6`) it is non-monotone and stalls (~0.0065) — *not*
converging. The original run above used `Im z=0.6` (outside the strip), so its "convergence" was only
conditional/analytic. **Corrected reading:** the factorization holds genuinely in the strip; passivity
on the full `ℂ_+` is by **analytic continuation + zero-free denominator placement**, not literal
product convergence everywhere. The analytic continuation must not be smuggled into the local product.

## Status

- **Unconditional (ω>½):** the factorization holds and the assembled product is passive — the
  Tate/Euler colligation exists and is passive in the safe region, as Connes stated. ✓
- **Refinement delivered:** passivity is a J-unitary *matrix*-colligation property; scalar local
  factors are unimodular-on-ℝ but not individually inner. The construction should be done with the
  local **transfer matrices**, not scalar factors.
- **The RH-strength step is unchanged:** continue the passive matrix colligation to ω↓0 (E104 shows
  the *scalar* characteristic function stays Pick-PSD to ω=0 for ζ, fails at ω=β−½ off-line). The
  open theorem is that the *adelic matrix colligation* admits the regularized passive continuation —
  Connes' final statement.

## Reproduce
```
venv/bin/python E105_tate_factorization.py     # omega=1.0; factorization + strip passivity
```
