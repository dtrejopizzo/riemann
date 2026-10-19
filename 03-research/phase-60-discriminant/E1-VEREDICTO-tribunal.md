# E1 — Consolidated verdict of the panel (· ·) The three worked E1 in parallel and **converged unanimously**. Honest result: **E1
does NOT close elementarily — it is a mandatory citation of CCM Thm 1.1(iii)** — but the panel
**proved it with an obstruction theorem** (it is not opinion: it is mathematics). That IS a result. ## 1. Decisive fact (, verbatim from the code)
The secular of the validated engine (`E4hp_convergence.py:66`) is **LINEAR**:
``` f(s) = Σ_k ξ_k/(s − d_k) ← residues ξ_k of VARIABLE sign (boundary carrier ω*≈0.966π)
```
It is **NOT** the quadratic `Σξ_k²/(s−d_k)`. The hope of an easy win is ruled out from the start. ## 2. The quadratic rescue: elementarily REFUTED (§1.3)
The quadratic `m(s)=Σξ_k²/(s−d_k)` **is** indeed Herglotz (real-rooted), but it is **a different object**:
in the counterexample `ξ=(−1,2,−1)`, `d=(−1,0,1)`:
- linear `f = −2/(s³−s)` → **0 roots**;
- quadratic `m = (6s²−4)/(s³−s)` → roots `±√(2/3)`, **real**.
The zeros of `m` (±0.816) **are not** those of `ξ̂` (none). Squaring the residues **breaks the
Weil identity** `⟨ξ,QWξ⟩=Σ_ρ ξ̂(γ_ρ)conj(ξ̂(conj γ_ρ))` that defines `ξ̂`. It is not a typo nor a gauge.
*The square that would help* (`Σ_ρ|ξ̂(γ_ρ)|²≥0`) is baked in with RH (kernel IV.2); *the free
square* (`m`) is the wrong object. ## 3. OBSTRUCTION THEOREM () — the result of the day
> **There is no universal construction** that realizes the roots of `f(s)=Σξ_k/(s−d_k)` as
> the **spectrum of a self-adjoint operator** from the isolated data `(ξ_k, d_k)`. *Proof.* The counterexample `ξ=(−1,2,−1)` **is the ground state of the discrete
Dirichlet Laplacian** `tridiag(−1,2,−1)` (up to sign) — a legitimate real eigenvector of a
symmetric matrix — and its secular `f=−2/(s³−s)` **has no real roots**. The canonical arrow-matrix
`B=[[D,ξ],[e^T,0]]` (whose spectrum = roots of `f` via Schur) is **not symmetric** and has
**non-real** spectrum for this input. A self-adjoint operator cannot have that spectrum. ∎ **Consequence:** real-rootedness, when it holds, **must** use SPECIFIC information from the
ground state of the Weil form that `(−1,2,−1)` (= top mode of the Laplacian) **does not possess**. And
it is not: sign of `ξ` (DH has signs and it holds), nor total positivity (refuted,
Gantmacher–Krein), nor Perron–Frobenius alone. ## 4. The de Branges route: it exists but is NOT a shortcut (§2)
The structure function `E=A−iB` (with `B=ξ̂`) exists in the abstract, but the Hermite–Biehler
inequality `|E(s̄)|<|E(s)|` is **logically equivalent to E1** (de Branges Thm 12–13).
Verifying it requires the **Wronskian `A'B−AB'` of constant sign** = the self-adjoint spectral
interlacing. The only proved positivity (PF: envelope `u_k>0` in the function basis) **does not
translate** into positivity of the raw residues `ξ_k` because of the phase mismatch `ω*≈0.966π≠π`.
Exhibiting `E` with HB **is** re-proving the self-adjoint realization = **CCM Thm 1.1(iii)**. ## 5. Precise obstruction (unanimous one-liner)
> *The real-rootedness of `ξ̂` is the claim that the linear secular `f(s)=Σξ_k/(s−d_k)` is
> a self-adjoint Nevanlinna m-function. The only proved positivity (PF, envelope
> `u_k>0`) lives in the function basis and, via the boundary carrier `ω*≈0.966π≠π`, does NOT translate into
> positivity of the raw residues `ξ_k` nor into a Wronskian of constant sign. Therefore E1
> admits no proof at the elementary Herglotz/HB level; it is a mandatory citation of CCM 1.1(iii).* ## 6. What IS settled
- **Lemma M1 [SOLID]:** sub-case `ξ_k>0` ⟹ Herglotz ⟹ real-rooted. The only self-contained piece. The real ground state **does not** fall here.
- **Obstruction theorem [SOLID]:** E1 is not constructible from isolated `(ξ_k,d_k)` (counterexample = ground state of the Dirichlet Laplacian). **This turns "🔧 pending repair" into "mandatory citation PROVED"** — no more time should be spent trying to close it elementarily.
- **E1 is RH-neutral** (it holds for DH) ⟹ citing CCM 1.1(iii) and using it **is not circular** (the RH burden is in the convergence, not in E1). ## Unanimous verdict
E1 **was not a closing win** — but the panel delivered a **clarity win**: it proved that the
mandatory citation of CCM 1.1(iii) is **necessary**, not laziness, with an obstruction theorem and the
finding that the counterexample is the mode of the Dirichlet Laplacian. The label of the
master document stands **confirmed and reinforced**: real-rootedness certain (CCM), own proof
impossible at the elementary level, sub-case `ξ_k>0` closed (M1).
