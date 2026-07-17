# The adelic passive-colligation theorem for RH — statement and proof architecture

*A precise formulation of the RH-strength step of Connes' route. Honest throughout: the final
positivity is **not proven** — it is RH — and is flagged as the single open crux. What is rigorous
(the equivalences and the unconditional `ω>½` colligation) is separated from what is open.*

---

## 0. Notation

- `ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s)` — the completed zeta; entire, order 1, `ξ(s)=ξ(1−s)`,
  real on `ℝ` and on the critical line `Re s=½`.
- `Ξ(z) := ξ(½+iz)` — entire, even, real for `z∈ℝ`; **RH ⟺ all zeros of `Ξ` are real**.
- For `κ>0`: `E_κ(z) := Ξ'(z) − iκ Ξ(z)`, and `E_κ^#(z) := \overline{E_κ(\bar z)} = Ξ'(z) + iκ Ξ(z)`.
- de Branges kernel `K_κ(z,w) := [E_κ(z)\overline{E_κ(w)} − E_κ^#(z)\overline{E_κ^#(w)}] / [2πi(\bar w − z)]`.
- Shifted scattering family, `ω>0`: `Θ_ω(z) := ξ(½+ω+iz) / ξ(½+ω−iz)`.
- Herglotz field `φ(z) := Ξ'(z)/Ξ(z)`, `m(z):=−φ(z)`.

---

## 1. The equivalence theorem (classical / established)

**Caveat (Connes, audit 0.1): use the non-strict form.** *Strict* Hermite–Biehler excludes common
real zeros of `E_κ` and `E_κ^#`, hence would force **simple** zeros of `Ξ` — which RH does not
include. So the safe equivalence is with **`m=−Ξ'/Ξ` Herglotz** ⟺ **`K_{S_κ}⪰0`**, allowing
degeneracy at multiple real zeros. Statement (2) below is the *non-strict / degenerate-allowed* HB.

**Theorem 1 (de Branges; verified numerically in E103/E104/E106/E107/E108).**
The following are equivalent:
1. **RH** (all zeros of `Ξ` real).
2. `E_κ` is **Hermite–Biehler (non-strict)** (`|E_κ^#(z)| ≤ |E_κ(z)|` for `Im z>0`), for some/any `κ>0`.
3. The de Branges kernel `K_κ` is a **positive kernel** (`[K_κ(z_i,z_j)] ⪰ 0` for all finite
   `{z_i}⊂ℂ_+`).
4. `m=−Ξ'/Ξ` is a **Herglotz** function (`Im m ≥ 0` on `ℂ_+`), i.e. admits the representation
   `m(z)=az+b+∫(\frac{1}{t−z}−\frac{t}{1+t^2})dμ(t)` with `μ≥0` (and then `μ=∑_{Ξ(γ)=0} m_γ δ_γ`).
5. The Schur function `S_κ = E_κ^#/E_κ` is **inner** on `ℂ_+` (analytic, `|S_κ|≤1`).
6. (continuation form) For the shifted family, `Θ_ω` is Schur/inner on `ℂ_+` for **every** `ω>0`,
   i.e. the **regularized margin `R(\{z_i\}) = \lim_{ω↓0} \min\mathrm{spec\,Pick}_ω/\max(...) ≥ 0`**
   for all finite configurations `{z_i}⊂ℂ_+`.

*Status:* (1)⟺(2)⟺(3)⟺(4)⟺(5) is classical de Branges/Herglotz theory. (1)⟺(6) is the
shift-continuation reformulation (Θ_ω pole at `−γ+i(β−½−ω)` enters `ℂ_+` iff `β>½` and `ω<β−½`),
verified sharply in E104/E107 (threshold `ω*=β−½`). **All RH-equivalent; none is a proof.**

---

## 2. The unconditional building block (rigorous, `ω>½`)

**Theorem 2 (Tate/Euler colligation in the safe region; numerics E105).**
For `ω>½`, `Re(½+ω±iz)=½+ω>1`, the Euler product converges and
```
   Θ_ω(z) = Θ_∞(z) · ∏_p Θ_p(z),   Θ_p(z)=\frac{1−p^{−(½+ω−iz)}}{1−p^{−(½+ω+iz)}},
   Θ_∞(z)=G(½+ω+iz)/G(½+ω−iz),  G(s)=½s(s−1)π^{−s/2}Γ(s/2).
```
Each place `v` carries a **`J`-unitary local transfer matrix** `T_v(z)` (a Tate local colligation:
the finite primes are passive delay elements of delay `log p`; the archimedean place is the
Γ-cascade), and `Θ_ω` is the characteristic function of the **restricted product**
`T_ω = ∏_v T_v` (Sz.-Nagy–Foiaş/Livšic product of colligations).

*Status:* the **factorization** and the **passivity of the assembled product** are verified for `ω>½`
(E105). **Two caveats:**
- **(E105)** the scalar local factors are unimodular on `ℝ` but **not individually inner** — passivity
  is a property of the `J`-unitary *matrix* product, not the scalar factors. `T_ω` is assembled at the
  matrix-colligation level.
- **(Connes audit 0.2) the Euler product is a *boundary* object.** The product for `ξ(½+ω+iz)`
  converges only where `Re(½+ω+iz)=½+ω−Im z>1`, i.e. in the **shallow strip** `0<Im z<ω−½`, and on
  the real boundary — **not** on all of `ℂ_+`. So the `ω>½` colligation must be read as: (i) boundary
  scattering data from the Euler/Tate product; (ii) **analytic continuation** into `ℂ_+`; (iii)
  Schur/passivity in `ℂ_+` from the **zero-free placement of the denominator**, not from literal
  Euler-product convergence everywhere. The analytic continuation must **not** be smuggled into the
  local product. (Our E105 "convergence" at `Im z=0.6` for `ω=1` was *outside* the strip `Im z<0.5`,
  hence only conditionally/analytically continued — see the E105 strip recheck.)

**Adelic realization (Connes §3, to be made rigorous).** The state space is
`ℋ = L²(𝔸_ℚ^×/ℚ^×, d^×x)`; with `u=log|x|`, the dilation `U_t f(x)=f(e^t x)` is diagonalized by
Mellin. The Lax–Phillips incoming/outgoing subspaces are
`𝒟_− = \{f: f(x)=0,\ |x|>1\}`, `𝒟_+ = ℱ𝒟_−` (`\widehat f(x)=0,\ |x|>1`).
For `ω>½` the pair `(𝒟_−,𝒟_+)` defines a **conservative unitary colligation** with characteristic
function `Θ_ω`, the restricted tensor product of the local Tate colligations.

---

## 3. The target theorem (the RH-strength crux — OPEN)

> **Theorem 3 (Adelic passive-colligation continuation = RH).**
> The conservative unitary colligation `T_ω` of Theorem 2, defined unconditionally for `ω>½`, admits
> a **regularized continuation** to `ω=0` that remains **passive** (`J`-contractive on `ℂ_+`).
> Equivalently: the critical de Branges kernel `K_κ` (`E_κ=Ξ'−iκΞ`) is **positive**.
> Equivalently: `R(\{z_i\}) ≥ 0` for all finite configurations.

**Theorem 3 ⟺ RH** (by Theorem 1). It is therefore the entire content; proving it *is* proving RH.
Numerically (E104/E106/E107): the continuation **exists and the regularized margin is `>0` for ζ**
on every configuration tested, and **fails at `ω=β−½`** for any off-line zero. What is missing is an
**unconditional** proof that the matrix colligation stays passive through `ω↓0`.

### 3a. What a proof must supply (the two ingredients, Connes §5)

Passivity of a `J`-unitary characteristic function decomposes into two statements, **both needed**:

- **(U) Boundary unitarity:** `S_κ^* S_κ = 1` on `ℝ` (equiv. `|Θ_ω|=1` on `ℝ`). This is the
  **functional equation** `ξ(s)=ξ(1−s)` and holds unconditionally. ✔ (It is *not* enough alone — a
  wrong-orientation Blaschke factor is unimodular on `ℝ` yet has poles in `ℂ_+`.)
- **(P) Interior passivity / causality:** `K_{S_κ}(z,w)=\frac{1−S_κ(z)\overline{S_κ(w)}}{2πi(\bar w−z)} ⪰ 0`
  on `ℂ_+`. This forbids poles of `S_κ` in `ℂ_+`, i.e. forbids off-line zeros. **This is the open
  half, and it is RH.**

(U) comes from Riemann–Roch / scattering symmetry; (P) must come from **Hilbert-space positivity of
the colligation** — the adelic Gram structure. The theorem is: *the critical de Branges kernel is the
Gram kernel of the adelic passive colligation*, so (P) holds by construction.

### 3b. The precise gap

We have, unconditionally:
- the colligation for `ω>½` (Theorem 2),
- boundary unitarity (U) for all `ω` (functional equation),
- the equivalences (Theorem 1).

The gap is a single **continuation-of-positivity** statement: the positive Gram structure that
exists for `ω>½` (where there are no `ℂ_+` poles) is **preserved** through `ω↓0`. In de Branges
language: the chain of spaces `ℋ(E_{κ,ω})` extends to a **limit de Branges space `ℋ(E_κ)` that is
still a Hilbert space (positive kernel)** at the critical value. The obstruction to extension is
exactly a zero of `Ξ` leaving the real axis (a sign change of `K_κ`), i.e. an off-line zero.

### 3c. Candidate mechanisms (for the open step)

1. **Index positivity — the Kreĭn–Langer negative-square count (Connes round 3, E108).** The correct
   index is **not** `μ_max=1` (boundary norm-one / Euler-characteristic balance — invisible to interior
   off-line spectrum) but `ind₋(K_{S_κ}) = #{UHP poles of S_κ} = #{off-line zeros}`. By Kreĭn–Langer,
   a function unimodular on `ℝ` is a *generalized* Schur function whose kernel has exactly that many
   negative squares. **`RH ⟺ ind₋(K_{S_κ})=0`.** Verified exactly (E108): ζ has `ind₋=0`; `k` planted
   off-line zeros give `ind₋=2k`. So the arithmetic Riemann–Roch / Hodge-index theorem one must prove
   is **`ind₋=0` (absence of negative squares)** — *not* merely boundary balance `μ_max=1`. This is
   where the program's MW-5 wall reappears in its sharpest form: a Hodge-index/Castelnuovo positivity
   over Spec ℤ that forbids negative squares.
2. **Monotone continuation.** Show `ω ↦ (\text{Gram of } T_ω)` is **operator-monotone / has no
   eigenvalue crossing 0** on `(0,∞)` for the arithmetic colligation, using that an eigenvalue can
   cross 0 only at an off-line-zero pole, and that the **passive (causal) structure** forbids such a
   crossing from the safe region. (E107's stable positive `R` is the numerical signature of exactly
   this no-crossing.)
3. **Restricted-tensor passivity.** Prove each local `J`-unitary `T_v` is passive **as a colligation**
   (not scalar) on the adelic Hilbert space, and that the **restricted product preserves passivity**
   in the `ω↓0` limit (a tensor-product/Szegő-type theorem). DH fails because it is **not** a
   restricted tensor product of local Tate colligations (no Euler product).

### 3d. Where DH (the falsifier) must fail

DH satisfies (U) (it has a functional equation) but **not** (P): it is not a restricted tensor
product of passive local Tate colligations (no Euler product), so its regularized continuation breaks
at `ω=β−½` for its off-line zero `β` (E104/E107, exactly). Any proof of Theorem 3 must use an
ingredient DH lacks — **the Euler product / adelic multiplicativity** — not merely the functional
equation and symmetry. This is the invariant lesson of the whole program: soft (functional-equation +
symmetry) structure is DH-symmetric and cannot prove RH.

---

## 4. Summary

| ingredient | status |
|---|---|
| Equivalences RH ⟺ `K_κ⪰0` ⟺ `Θ_ω` passive ⟺ `m` Herglotz ⟺ `R≥0` | **rigorous** (de Branges) + numerically validated |
| Unconditional colligation for `ω>½` (Tate/Euler product) | **rigorous/verified** (matrix level) |
| Boundary unitarity (U) for all `ω` | **rigorous** (functional equation) |
| **Interior passivity (P) / continuation to `ω=0` (Theorem 3)** | **OPEN = RH** |

**Theorem 3 is the proof of RH.** Everything else is in place. The single missing statement is that
the **adelic passive colligation's positivity continues to the critical value `ω=0`** — equivalently
that the critical de Branges kernel `K_κ` is positive — equivalently that interior passivity (P)
holds. It must be powered by the **Euler product / an arithmetic index positivity** (the
Connes–Consani arithmetic-site Hodge-index analogue), the one input the Davenport–Heilbronn falsifier
provably lacks.

*This document states the theorem and its architecture; it does not prove Theorem 3. Per the
program's standing rule, a false victory is worse than failure: Theorem 3 is RH and remains open.*
