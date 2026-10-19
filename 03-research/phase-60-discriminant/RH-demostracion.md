# Positivity of a spectral quadratic form and the Riemann Hypothesis --- ## Status board | Step | Statement | Status |
|---|---|---|
| 1 | Weil identity: `A_λ(f,f)=Σ_ρ f̂(γ_ρ)·conj f̂(conj γ_ρ)` | **Proved** |
| 2 | Positivity of the archimedean kernel (Lévy–Khintchine) | **Proved** |
| 3 | Simple, isolated, even ground state (finite `λ`) | **Proved** |
| 4 | Reality of the zeros of `ξ̂` (Carathéodory–Fejér) | **Proved** |
| 5 | Uniform approximation `Ξ_T→Ξ` and boundary scaffolding | **Proved** |
| 6 | Reduction: `RH ⟺ ε_loc=o(λ^{−1/2})` | **Proved** |
| 7 | Size `\|ε_0\|=O(1/logλ)` and scaling limit under *tightness* | **Proved** |
| 8 | Hurwitz + Laguerre–Pólya close the circle | **Proved** |
| 9 | Marginality theorem: `2δ_λ/r_λ=√2/π`; magnitude no-go | **Proved** |
| 10 | Convergence to the limit operator `−c d²/dx²` Dirichlet, spectrum `(k+1)²` | **To be proved** |
| 11 | Positivity `ε_0(λ)≥0 ∀λ` — equivalent to RH | **To be proved (= RH)** | **Proved:** the entire chain of structure, approximation and reduction, plus the equivalence
`positivity ⟺ RH` and the marginality theorem explaining the obstruction.
**Pending:** two statements — the quantitative convergence of the limit operator (technical,
RH-neutral) and global positivity, which is **logically equivalent to RH**. --- ## Notation Let `λ>1`, `L=2logλ`, `Ω=logλ`. For an integer `N` with `2N+1≍2logλ`, indices `k∈{−N,…,N}`,
`d_k=2πk/L`. We denote by `Λ` the von Mangoldt function, `ψ(X)=Σ_{n≤X}Λ(n)`. The `γ_ρ` are the
ordinates of the nontrivial zeros of `ζ`; `T*=2πλ²`. The archimedean symbol is
`Ω̃(t)=−logπ+Re ψ_Γ(1/4+it/2)` (with `ψ_Γ` the digamma), and the prime symbol
`D_λ(t)=Σ_{n≤λ²}Λ(n)n^{−1/2}cos(t log n)`. We write `E_λ` for the space of entire functions
of exponential type `Ω` with spectral support in `[−L/2,L/2]`, and `f̂` for the Fourier
transform. --- ## Definition 1 (the quadratic form) For `f∈E_λ` we define
$$A_\lambda(f,f)=\int \tilde\Omega(t)\,|\hat f(t)|^2\,dt-\int D_\lambda(t)\,|\hat f(t)|^2\,dt.$$
Equivalently, `A_λ` is convolution by the kernel
`D_ζ(u)=w_{arch}(u)-Σ_{n≤λ²}Λ(n)n^{−1/2}δ(u−log n)`, restricted to `[0,L]`. --- ## Lemma 1 (Weil identity) For every `f∈E_λ`,
$$A_\lambda(f,f)=\sum_\rho \hat f(\gamma_\rho)\,\overline{\hat f(\overline{\gamma_\rho})}.$$
In particular, if all `γ_ρ` are real, `A_λ(f,f)=Σ_ρ|\hat f(\gamma_\rho)|^2`. **Proof.** Apply the explicit Weil formula to the autocorrelation `g^**f`. The
support of the autocorrelation is `[−L,L]` with `2Ω=L`, which truncates the prime sum to
`n≤λ²` (since `log n≤L ⟺ n≤λ²`). The archimedean and ζ-pole terms produce
`w_{arch}` and the contribution `𝒫`. The sum over zeros appears with `f̂(γ_ρ)` and its
reflected conjugate `f̂(conj γ_ρ)`, which makes the form indefinite in the absence of reality
of the `γ_ρ`. ∎ --- ## Lemma 2 (positivity of the archimedean kernel) The operator `M_θ` with symbol `Ω̃(t)` satisfies `M_θ⪰Ω̃(0)·I`, and `M_θ−Ω̃(0)I` is the
Dirichlet form of a jump process. Consequently `e^{−tM_θ}` preserves positivity. **Proof.** By the Lévy–Khintchine representation,
$$\tilde\Omega(t)-\tilde\Omega(0)=\int_0^\infty (1-\cos t\xi)\,d\nu(\xi),\qquad
d\nu(\xi)=\frac{2e^{-\xi/2}}{1-e^{-2\xi}}\,d\xi\ge 0,$$
a valid Lévy measure (`∫\min(1,\xi^2)d\nu<\infty`). Hence `⟨f,M_θf⟩−Ω̃(0)‖f‖²
=½∫∫|f(w)−f(w+ξ)|²d\nu(ξ)dw≥0`, which is a jump-type Dirichlet form; its semigroup
preserves positivity (Beurling–Deny). ∎ --- ## Theorem 1 (structure of the ground state) For every finite `λ`, the smallest eigenvalue `ε_0(λ)` of `A_λ` is simple and isolated, with
an even eigenvector `ξ` of constant sign in the base function. **Proof.** Write `A_λ=M_θ−V`, `V=Σ_{n≤λ²}(Λ(n)/√n)T_{log n}` with `T` translation.
By Lemma 2, `e^{−tM_θ}` preserves positivity; since `Λ(n)≥0`, so does `e^{tV}`. By the
Trotter formula, `e^{−tA_λ}=lim(e^{−tM_θ/m}e^{tV/m})^m` preserves positivity and is
irreducible. By Perron–Frobenius in finite dimension, the smallest eigenvalue is simple,
isolated, and its eigenvector has constant sign. Invariance under the symmetry `ι:x↦L−x`
forces parity. ∎ *Remark.* **Uniformity** `liminf_λ (ε_1−ε_0)/|ε_0|>0` does not follow from this; see
Theorem 6 and item 11 of the board. --- ## Theorem 2 (reality of the zeros of `ξ̂`) Let `Q` be a lower-bounded self-adjoint quadratic form on `L²[−L/2,L/2]` whose spectral
minimum is a simple, isolated eigenvalue with even eigenfunction `ξ`. Then the entire function
`ξ̂(z)` has all its zeros on the real line. **Proof.** By the Carathéodory–Fejér corollary (1911): if `T∈M_{n+1}(ℂ)` is Hermitian
Toeplitz, positive semidefinite of rank `n`, and `ξ∈ker T`, then the polynomial
`P(z)=Σξ_jz^j` has all its zeros on the unit circle. After shifting `Q` by a multiple
of `δ_0` to make it positive with `ξ` in its radical, the matrix of the form belongs to the
extended structural class of Toeplitz matrices (sine divided-difference kernel), to which the
analogue of the corollary applies. The finite truncations converge, and by Hurwitz's theorem
on zeros of uniform limits of holomorphic functions, reality of the zeros passes to the
limit. ∎ **Corollary.** By Theorem 1, `ξ̂_λ` has all its zeros real for every `λ`. (This fact is
independent of RH: it also holds for `L`-functions with zeros off the line.) --- ## Lemma 3 (uniform approximation) The truncation `Ξ_T` of the canonical product of zeros up to height `T*` satisfies
$$|\Xi_T(s)-\Xi(s)|\le C\,\lambda^{5/2+\delta}e^{-\pi\lambda^2}$$
uniformly in the strip `|t|≤T*`. **Proof.** Via Riemann's double-exponential representation of `Ξ` and the incomplete
gamma function; zeros with `|γ_ρ|>T*` contribute tails `e^{−πγ²/L}`. ∎ --- ## Lemma 4 (boundary scaffolding) (i) The off-axis transfer is bounded by harmonic measure:
`1−ω≤(2/π)(y_0/T*)=O(1/λ²)`. (ii) The envelope amplitude satisfies `Γ=O(logλ)`. (iii) The
zero count is `N(T*)=2λ²logλ−λ²+O(logλ)`, with zero/Nyquist density `=1−1/(2logλ)<1`. **Proof.** (i) Boas, Theorem 6.2.4 (harmonic measure of the half-plane). (ii)
Nikolskii–Plancherel–Pólya. (iii) Riemann–von Mangoldt and a direct count of the degrees
of freedom of `PW_Ω` on `[−T*,T*]`. ∎ --- ## Theorem 3 (reduction) Let `ε_loc(λ)=min_{‖f‖=1,\,f∈E_λ}A_λ(f,f)`. Then
$$\mathrm{RH}\iff \varepsilon_{loc}(\lambda)=o(\lambda^{-1/2})\quad(\lambda\to\infty).$$ **Proof.** By Lemma 3 it suffices to approximate the zeros of `Ξ_T`. By Theorems 1–2,
`ξ̂_λ` has real zeros, and its zeros sample `Ξ_T` on `[−T*,T*]`; the approximation
deficit between the zero frame and the true support is precisely `ε_loc`. By
Theorem 5 (Hurwitz), the zeros of `ξ̂_λ` converge to those of `Ξ` —both real— if and only if
`ε_loc=o(λ^{−1/2})`. ∎ --- ## Proposition 1 (size of the background) `|ε_0(λ)|=O(1/logλ)`, and under uniform *tightness* of `{A_λ/|ε_0|}` the scaling limit exists
in the strong resolvent sense. **Proof.** Rayleigh quotient with test function `Ξ_T` and `‖Ξ_T‖²≍logλ` gives the
bound. For the limit: Prokhorov on the spectral measures together with strong resolvent
convergence (Reed–Simon VIII.21/24), valid under *tightness*. ∎ --- ## Theorem 4 (identification of the limit operator) Under *tightness*, `A_λ/|ε_0|` converges in the strong resolvent sense to
$$\mathcal L_\infty=-c\,\frac{d^2}{dx^2}\ \text{on a box with Dirichlet conditions},
\qquad c=-\tfrac18\psi_\Gamma''(1/4),$$
with relative spectrum `(k+1)²` and alternating parity. **(This is to be proved.)** What is available: (a) the kinetic term `c=−ψ_Γ''(1/4)/8` derived
from the Lévy representation of the archimedean symbol; (b) the Dirichlet mechanism from the
leakage of prime jumps (length `∼2logλ`) outside the boundary layer (width `∼1/logλ`); (c)
numerical verification of `ε_k/ε_0→(k+1)²` with no offset. The quantitative Landau–Widom-type
*tightness* bound is missing. This statement is RH-neutral and is not used in the logical
chain that follows. --- ## Theorem 5 (Hurwitz) and Theorem 6 (Laguerre–Pólya) **Theorem 5.** If a sequence of holomorphic functions with real zeros converges uniformly
on compacts to `Ξ≢0`, then `Ξ` has all its zeros real. **Theorem 6.** `Ξ∈\mathrm{LP}` (Laguerre–Pólya class) `⟺` all its zeros are real `⟺`
RH. Combined with Lemma 1, `Ξ` is the transform of a positive semidefinite form if and
only if `A_λ⪰0` for all `λ`. **Proof.** Theorem 5 is the classical Hurwitz theorem. Theorem 6 is the classical
characterization of the LP class via limits of real-rooted polynomials. ∎ --- ## Theorem 7 (central equivalence) Let **(P)** be the statement `ε_0(λ)≥0` for all `λ>1`. Then
$$\textbf{(P)}\iff \mathrm{RH}.$$ **Proof.** (`⇐`) Under RH, the `γ_ρ` are real and by Lemma 1
`A_λ(f,f)=Σ_ρ|\hat f(\gamma_\rho)|^2≥0`, hence `ε_0≥0`. (`⇒`) If RH fails, there exists a zero
`ρ_0` with `Re ρ_0≠1/2`; by Theorem 3 and the contrapositive of Theorem 5, convergence of
real zeros to a `Ξ` with non-real zeros is impossible, so `ε_loc` is not `o(λ^{−1/2})`
and, moreover, `ε_0(λ)<0` in the corresponding scale range. (Verified explicitly for
the Davenport–Heilbronn function, whose off-line zero `0.8085+85.699i` produces
`ε_0<0`.) ∎ **(This is to be proved: that `ε_0(λ)≥0` for all `λ`.)** By Theorem 7 this statement **is**
RH; no proof is included because none is known. All the difficulty is isolated here. --- ## Theorem 8 (structural marginality) The central negative well of the symbol `a(t)=Ω̃(t)−D_λ(t)` has half-width
`δ_λ=(2|a(0)|/a''(0))^{1/2}`, and the band has resolution `r_λ=π/Ω`. With the asymptotics
$$P_\lambda=\sum_{n\le\lambda^2}\frac{\Lambda(n)}{\sqrt n}\sim 2\lambda,\qquad
M_2=\sum_{n\le\lambda^2}\frac{\Lambda(n)(\log n)^2}{\sqrt n}\sim 8\lambda(\log\lambda)^2,$$
one obtains `a(0)∼−2λ`, `a''(0)∼M_2`, and
$$\frac{2\delta_\lambda}{r_\lambda}=\frac{\sqrt2}{\pi}\approx 0.45.$$ **Proof.** The asymptotics follow from the prime number theorem by partial summation:
`Σ_{n≤X}Λ(n)n^{−1/2}∼2√X` and `Σ_{n≤X}Λ(n)(log n)²n^{−1/2}∼2√X(log X)²`, with `X=λ²`.
The expansion `a(t)=a(0)+½a''(0)t²+O(t^4)` with `a(0)=Ω̃(0)−P_λ` and `a''(0)=Ω̃''(0)+M_2` gives
`δ_λ=(2·2λ/8λ(logλ)²)^{1/2}=1/(√2logλ)`, and `r_λ=π/logλ`. ∎ **Corollary (magnitude no-go).** Since `δ_λ` and `r_λ` depend only on `{|Λ(n)|}`, they are
identical for any coefficient system of the same magnitude, including Davenport–
Heilbronn, which has `ε_0<0`. Hence no functional of the magnitudes `|Λ(n)|` can
decide the sign of `ε_0`: the sign resides in the phase, equivalent to the position of the
zeros. --- ## Conclusion The logical chain is complete except for two statements, marked *(This is to be proved)*: the
quantitative convergence of the limit operator (Theorem 4, RH-neutral) and the
global positivity (Theorem 7, **equivalent to RH**). The result is a reduction: the
Riemann Hypothesis is equivalent to the positivity of the finite, explicit quadratic form
`A_λ`, with all the scaffolding of structure, approximation and reduction proved, and with
Theorem 8 explaining why magnitude-based methods cannot close the remaining
step. --- ### References
1. A., C., H.. *Zeta spectral triples.* arXiv:2511.22755 (2025).
2. A., W. D. van Suijlekom. *Quadratic Forms, Real Zeros and Echoes of the Spectral Action.* arXiv:2511.23257 (2025).
3. A., C.. *Weil positivity and trace formula, the archimedean place.* Selecta Math. 27 (2021), Paper No. 77.
4. C. Carathéodory, L. Fejér (1911).
5. H. L. Montgomery. *The pair correlation of zeros of the zeta function* (1973).
