# E1 (real-rootedness) — lens: is the secular LINEAR or QUADRATIC? **Author of audit:** C. (with,), for the CCM zeta spectral-triple
program. Cold honesty. Scope: settle whether the validated engine's secular function is the
*linear* form `Σ ξ_k/(s−d_k)` or the *quadratic resolvent* `Σ ξ_k²/(s−d_k)`, because the
latter would close E1 elementarily (Herglotz), the former would not. --- ## 1. What the engine ACTUALLY computes (VERBATIM from the code) — DECISIVE File: `experiments/E4hp_convergence.py`, lines 64–66: ```python
def root_near(xi,idx,L,target): d=[2*mp.pi*k/L for k in idx] f=lambda s: mp.fsum([xi[i]/(s-d[i]) for i in range(len(d))])
``` Header comment, line 14:
```
# eigenvalues = raices de f(s)=Σ_k ξ_k/(s-2πk/L), ξ=autovector menor autovalor.
``` `xi` is the **raw** ground eigenvector of the symmetric Weil matrix `QW`, built at
lines 58–61:
```python
E,V=mp.eigsy(M)
jmin=min(range(dim),key=lambda j:E[j])
xi=[V[i,jmin] for i in range(dim)]
``` `E11_relspec_prolate.py` does **not** contain a secular function at all — it only computes
the spectrum `ε_k/ε_0` of `QW` (`spec()`, lines 13–18). So the secular lives solely in E4hp. **VERDICT (checkable, unambiguous):** the secular function is ``` f(s) = Σ_k ξ_k / (s − d_k) ← LINEAR, signed residues ξ_k
``` It is **NOT** `Σ ξ_k²/(s−d_k)`. The residues are the bare components of the ground
eigenvector, which are real but **of indefinite sign** (the boundary carrier ω*≈0.966π gives
~N sign changes). This matches RH-PROOF-FULL.md Def 0.2 / Prop 0.3 verbatim. **Consequence:** the "easy win" via an automatically-Herglotz quadratic resolvent is **not
available as written**. The engine does not use the resolvent form. We cannot wave it in. --- ## 2. What the secular SHOULD be — and why the linear form is NOT a bug The natural spectral object whose zeros are forced real is the **diagonal resolvent**
`R(s) = ⟨ξ,(s−D)^{−1}ξ⟩ = Σ_k ξ_k²/(s−d_k)`, `D=diag(d_k)`. Its residues `ξ_k²≥0` make it
Herglotz, so its zeros interlace the `d_k` and are real (this is exactly Lemma M1 applied to
positive residues). If THIS were the engine's secular, E1 would be a one-line corollary. But the CCM construction does **not** put the zeros of `ξ̂` at the zeros of a diagonal
resolvent of `D`. The eigenvalue equation is geometric: `ξ̂(s)=sin(Ls/2)·f(s)` is the
band-limited entire function whose value at the zeta zeros realizes the Weil quadratic form
(Identity, §1: `⟨ξ,QWξ⟩ = Σ_ρ ξ̂(γ_ρ)·conj(ξ̂(conj γ_ρ))`). The zeros `ρ̂_n` of `f` are the
spectrum of the **finite zeta operator**, not of `D`. So: - The linear form `Σ ξ_k/(s−d_k)` is a **genuine feature**, not a transcription error. Squaring the residues would change the entire function `ξ̂` and break the Weil identity (`ξ̂` would no longer be the band-limited interpolant whose nodal data is the eigenvector).
- Therefore option (a) of the brief ("linear is wrong, replace by quadratic") is **false**. We are in option (b): the linear form is correct and E1 needs the Hermite–Biehler / de Branges argument. **The quadratic shortcut does not apply.** This is the cold finding: the resolvent `Σξ_k²/(s−d_k)` is the object one *wishes* governed
the spectrum, but the CCM realization is the interpolation secular `Σξ_k/(s−d_k)`. They
coincide only when `ξ_k≥0` (then `ξ_k` and `ξ_k²` have the same sign pattern and both give
interlacing) — which is precisely the sub-case Lemma M1 already covers and which the ground
state does **not** satisfy. --- ## 3. Reconciliation: why does the linear form give real roots empirically? The counterexample `ξ=(−1,2,−1)`, `d=(−1,0,1)` gives `f(s)=−2/(s³−s)` — zero real roots.
So linear `Σξ_k/(s−d_k)` is **NOT** generically real-rooted. Yet the validated engine
reproduces real zeta zeros, and even Davenport–Heilbronn (RH-false, signed coefficients)
empirically yields real secular roots. What special property does the GROUND eigenvector
have that `(−1,2,−1)` lacks? The `(−1,2,−1)` vector is the **second difference** — a high-frequency, fully oscillating
vector orthogonal to smooth modes; its `ξ̂` is `∝ 1/(s³−s)·sin(Ls/2)`, a rational with a
constant numerator, no real zeros. The ground eigenvector of `QW` is the opposite extreme:
it is the **minimizer of a quadratic form whose value is Σ_ρ|ξ̂(γ_ρ)|²-type data**, i.e. it
is the *smoothest* band-limited shape (lowest "energy"), with an envelope that is positive
in the de-modulated basis (H1, Perron–Frobenius gives a *simple* bottom with positive
envelope). The relevant structural fact is: > **The ground state is a Hermite–Biehler (de Branges) reproducing element**, not an
> arbitrary real vector. `QW` is the matrix of a Weil/Pólya-type form; its bottom eigenvector
> is the band-limited function `ξ̂∈H(E)` for the de Branges space `E` of the construction,
> and elements of `H(E)` are real-rooted by the structure theory (`E` Hermite–Biehler ⟹
> `ξ̂=A−iB` with `A,B` real entire having interlacing real zeros). The sign-indefiniteness
> of the raw `ξ_k` is just the phase of the boundary carrier `ω*`; after de-modulation by
> that carrier the residues recover a definite-sign (Herglotz) structure. That is exactly why real-rootedness is **RH-neutral** (holds for DH too): it depends on the
*self-adjointness* of `QW` and the de Branges structure of the band-limited model, **not** on
positivity of the coefficients `Λ(n)≥0`. The `(−1,2,−1)` failure is consistent: that vector
is not the ground state of any such Weil form; it is a top-of-spectrum oscillation. **This is real and it is the correct reading — but it is not yet a proof.** It identifies the
missing lemma precisely: > **(E1-core)** The de-modulated ground eigenvector `(ξ_k e^{−iω*k})` has a definite-sign
> (or interlacing-with-`d_k`) structure, equivalently `ξ̂` lies in `H(E)` with `E`
> Hermite–Biehler. Then Hermite–Biehler ⟹ real roots. Proving (E1-core) from `QW=`Weil-form + PF-simplicity is the open work. It is **not**
closeable by the quadratic-resolvent shortcut, and it is **not** Perron–Frobenius alone
(PF gives a simple positive *envelope*, which is structure, not the phase-alignment needed). --- ## 4. Honest verdict - **Secular = LINEAR**, `Σ ξ_k/(s−d_k)`, signed residues. Confirmed verbatim from `E4hp_convergence.py:66` and its header. NOT quadratic. (Decisive, checkable.)
- **The easy win is unavailable.** The Herglotz/resolvent argument needs `ξ_k²` (or `ξ_k≥0`); the engine uses bare signed `ξ_k`, and squaring them would destroy the Weil identity that defines `ξ̂`. So we are genuinely in the de Branges / Hermite–Biehler regime.
- **E1 does NOT close elementarily here.** It closes *correctly* only via the self-adjoint / de Branges realization: `ξ̂∈H(E)`, `E` Hermite–Biehler ⟹ real roots. The sub-case `ξ_k>0` is the only elementary piece (Lemma M1) and the ground state is not in it.
- The recorded refutation (interlacing proof refuted by `ξ=(−1,2,−1)`) stands. The reconciliation in §3 explains the empirics without rescuing the elementary proof: the ground state is special (smoothest band-limited / de Branges reproducing element), generic real vectors are not. **Status: cita obligada CCM Thm 1.1(iii) confirmed**, with the open repair now sharply
localized to lemma (E1-core): show the de-modulated ground eigenvector has Hermite–Biehler
structure (`ξ̂∈H(E)`). That is honest finite-entire-function analysis — RH-neutral, hence
non-circular to use — but it is **not** the quadratic one-liner, and I will not claim it is.
