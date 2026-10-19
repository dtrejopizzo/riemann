# Design note: a candidate Hilbert–Pólya operator

**Goal.** A self-adjoint operator `H` whose eigenvalues are the ordinates `γ`
with `ζ(1/2+iγ)=0`, compatible with Weil's explicit formula (checked
numerically in `selector_weil.py`).

**Caveat.** This is a candidate, not a solution. Designing such an operator is
not the hard part (it has been done several times). The hard and unsolved part
is **proving that its spectrum is real**. What follows is the best available
reverse engineering, with the gap marked.

---

## 1. Properties forced by the explicit formula

Matching the explicit formula with the Gutzwiller trace formula gives:

- Space: `L²(ℝ⁺, dx)` (half-line).
- Weyl term: `N(T) = (T/2π)(log(T/2π) − 1) + 7/8`.
- Dynamical core: the dilation generator `H₀ = ½(xp + px) = −i(x d/dx + ½)`.
- Periodic orbits of length `log p^k`, Lyapunov exponent 1.
- **Broken** time-reversal symmetry (GUE statistics, not GOE).

## 2. Explicit candidate (Bender–Brody–Müller, 2017)

    H  =  1/(1 − e^{−ip}) · (x p + p x) · (1 − e^{−ip})

on `L²(ℝ⁺)` with boundary condition `ψ(0) = 0`, where `p = −i d/dx`.

Properties shown by Bender, Brody and Müller:
- `H` is symmetric with respect to a modified inner product (PT-symmetric).
- Formally, `(1 − e^{−ip})` acts as a comb introducing the integers `n`
  (and hence the primes through `Λ(n)`): this is where the orbits `log p` enter.
- The eigenvalues `E_n` formally satisfy `ζ(1/2 + i E_n) = 0`.

## 3. The gap

**Open lemma.** The spectrum of `H` is **real**.

Equivalently, the PT symmetry of `H` is unbroken (real eigenvalues, not complex
conjugate pairs). Bender, Brody and Müller reduced this to showing that a certain
similarity operator that makes `H` Hermitian is well defined and bounded. This
has **not** been proved.

Routes to the same lemma:
- **(a) Genuine self-adjointness:** exhibit the inner product for which `H` is
  self-adjoint (not only symmetric) and prove it is positive definite (a domain /
  self-adjoint extension problem).
- **(b) Weil positivity:** prove `Σ_γ h(γ) ≥ 0` for all `h = φ⋆φ̃`; by the explicit
  formula this gives reality of the spectrum.
- **(c) Connes's orbits:** realize the `log p` as lengths of closed orbits on the
  adele class space and prove positivity of the trace.

## 4. Why a design does not reduce the difficulty

The three routes (a), (b), (c) carry the same difficulty in different form; it
has resisted Weil, Selberg, Berry, Keating, Connes, and Bender–Brody–Müller. The
design exists; the obstruction is a positivity/reality theorem that nobody knows
how to prove. Any "proved operator" offered without that lemma is a candidate
with §3 assumed, not demonstrated.
