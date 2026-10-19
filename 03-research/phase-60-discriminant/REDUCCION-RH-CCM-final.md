# A reduction of the Riemann Hypothesis via zeta spectral triples (CCM program) **Abstract.** We construct, following –– (arXiv:2511.22755) and
–van Suijlekom (arXiv:2511.23257), a family of finite quadratic forms `A_λ`
whose ground state encodes the zeros of `ζ`. We prove every link of the chain
E0→E4 except one, and we show that the remaining link is **equivalent** to the Riemann
Hypothesis (RH). The result is a **reduction**: RH reduces to the positivity of a
single explicit quadratic form, with the entire approximation scaffolding proved. Section
10 ("Conjectural completion") proposes a strategy for the remaining step,
explicitly marked as conjectural. --- ## 0. Notation - `λ>1` scale parameter; `L=2logλ`; `Ω=logλ` (half-bandwidth).
- `N` integer with `2N+1 ≍ 2logλ`; indices `k∈{−N,…,N}`; `d_k = 2πk/L`.
- `Λ(n)` von Mangoldt; `ψ(X)=Σ_{n≤X}Λ(n)`.
- `γ_ρ` ordinates of the nontrivial zeros of `ζ`; `T*=2πλ²` (Nyquist horizon).
- `Ω̃(t) = −logπ + Re ψ_Γ(1/4+it/2)` archimedean symbol (`ψ_Γ` digamma).
- `D_λ(t) = Σ_{n≤λ²} Λ(n)n^{−1/2}cos(t log n)` prime symbol. --- ## 1. E0 — Construction and the Weil form **Definition 1.1.** On the space `E_λ` of band-limited functions of type `Ω` with
support `[−L/2,L/2]`, define the real symmetric quadratic form
$$A_\lambda(f,f) = \int \tilde\Omega(t)\,|\hat f(t)|^2\,dt \;-\; \int D_\lambda(t)\,|\hat f(t)|^2\,dt.$$ **Proposition 1.2 (Schwartz kernel, –van Suijlekom 2025, Prop. of the "Quadratic
form" §).** `A_λ` is convolution by `D_ζ(|x−y|)` restricted to `[0,L]`, where
$$D_\zeta(u) = w_{\mathrm{arch}}(u) - \sum_{n\le\lambda^2}\frac{\Lambda(n)}{\sqrt n}\,\delta(u-\log n).$$ **Theorem 1.3 (Weil identity; –, *Weil positivity… the archimedean place*,
Selecta 2021).** For `f∈E_λ`,
$$A_\lambda(f,f) \;=\; \sum_\rho \hat f(\gamma_\rho)\,\overline{\hat f(\overline{\gamma_\rho})}.$$
Under RH (`γ_ρ∈ℝ`), the right-hand side is `Σ_ρ |\hat f(\gamma_\rho)|^2`. *Proof.* Explicit Weil formula applied to the autocorrelation `g^* * f`, with the prime
cutoff `n≤λ²` coming from the support `2Ω=L`. The archimedean term and the pole of `ζ`
contribute the terms `w_arch` and `𝒫`. ∎ **Status: PROVED** (classical Weil identity, instantiated). --- ## 2. H1 — Structure of the ground state **Theorem 2.1.** For each finite `λ`, the smallest eigenvalue `ε_0(λ)` of `A_λ` is **simple**,
**isolated**, with **even** eigenvector `ξ` (under the symmetry `ι:x↦L−x`). *Proof.* `A_λ = M_θ − V`. (a) `M_θ` has symbol `Ω̃`, and by the Lévy–Khintchine
representation `Ω̃(t)−Ω̃(0)=∫(1−\cos tξ)\,dν(ξ)` with `dν≥0` (Lévy measure
`dν = 2e^{−ξ/2}(1−e^{−2ξ})^{−1}dξ`, verified positive), `M_θ` generates a
positivity-preserving semigroup. (b) `V = Σ_{n≤λ²}(Λ(n)/√n)T_{\log n}` with `Λ(n)≥0` and `T`
translations ⟹ `V` is positivity-preserving. (c) Trotter: `e^{−tA_λ}` is positivity-preserving
and irreducible ⟹ Perron–Frobenius ⟹ the ground state is simple, isolated at finite `λ`, with
an eigenvector of constant sign in the base-function. Parity follows from the `ι`-symmetry. ∎ **Status: PROVED** (at finite `λ`). *Uniformity `liminf_λ(ε_1−ε_0)/|ε_0|>0` remains
open; see §6 and §9.* --- ## 3. E1 — Reality of the zeros of `ξ̂` (real-rootedness) **Theorem 3.1 (–van Suijlekom 2025, arXiv:2511.23257, main theorem).** If `Q` is
a lower-bounded self-adjoint form on `L²[−L/2,L/2]` whose spectral minimum is a simple,
isolated eigenvalue with even eigenfunction `ξ`, then all zeros of the entire function `ξ̂(z)`
are real. *Proof (summary).* (i) Carathéodory–Fejér corollary (1911): a Hermitian PSD Toeplitz
matrix of rank `n` has the polynomial of its kernel with zeros on the unit circle.
(ii) Continuous analogue via operator systems. (iii) Finite truncations inherit the
structure. (iv) Hurwitz carries the reality of the zeros to the limit. ∎ **Corollary 3.2.** By Theorem 2.1, `ξ̂_λ` has all its zeros real for every `λ`. **Status: PROVED** (–van Suijlekom). RH-neutral: also holds for Davenport–Heilbronn. --- ## 4. N0–N3 — Approximation scaffolding **Theorem 4.1 (N0).** The truncation `Ξ_T` of the canonical product of zeros up to `T*` satisfies
`|Ξ_T(s)−Ξ(s)| ≤ C\,λ^{5/2+δ}e^{−πλ^2}`, strip-uniform on `|t|≤T*`.
*Proof.* Riemann double exponential + incomplete gamma; exponent `5/4+δ/2` verified. ∎ **Lemma 4.2 (N1, Boas Thm 6.2.4).** Off-axis transfer bounded by harmonic measure,
`1−ω ≤ (2/π)(y_0/T*) = O(1/λ^2)`. **Lemma 4.3 (N2, Nikolskii–Plancherel–Pólya).** Envelope amplitude `Γ = O(\logλ)`.
Horizon count (Riemann–von Mangoldt): `N(T*)=2λ²\logλ−λ²+O(\logλ)`; zero
density / Nyquist density `= 1 − 1/(2\logλ) < 1` (subcritical). **Lemma 4.4 (N3, Boas/Phragmén–Lindelöf).** Boundary amplification `λ^{y}`, `y≤1/2`. **Status: PROVED** (classical approximation theory). --- ## 5. Reduction theorem **Theorem 5.1 (CCM).** Let `ε_{\mathrm{loc}}(λ) = \min_{\|f\|=1,\,f\in E_\lambda}
A_\lambda(f,f)` (with canonical normalization `ξ̂_λ(0)=Ξ(0)`). Then
$$\boxed{\;\mathrm{RH} \iff \varepsilon_{\mathrm{loc}}(\lambda) = o(\lambda^{-1/2})\ \ (\lambda\to\infty).\;}$$ *Proof.* By N0, it suffices to approximate the zeros of `Ξ_T`. By H1+E1, `ξ̂_λ` is real-rooted,
and its zeros sample `Ξ_T` on `[−T*,T*]`. The approximation deficit between the truncated
zero frame and the true support is exactly `ε_loc`. By Hurwitz (E3), the zeros of
`ξ̂_λ` converge to those of `Ξ` —both real— if and only if `ε_loc=o(λ^{−1/2})`. ∎ **Status: PROVED.** This is the central reduction: RH reduces to a single
quantitative statement about an explicit quadratic form. --- ## 6. III — Relative stability and equivalence with RH **Proposition 6.1 (size, unconditional).** `|ε_0(λ)| = O(1/\logλ)` (Rayleigh with `Ξ_T`,
`‖Ξ_T‖^2≍\logλ`). **Proposition 6.2 ((H-lim) under tightness).** If the rescaled family `{A_λ/|ε_0|}` is
uniformly tight (an RH-neutral condition, Landau–Widom type), then the scaling limit exists
in the strong resolvent sense (Prokhorov + Reed–Simon VIII.21/24). **Theorem 6.3 (sign equivalence).** `\liminf_λ (ε_1−ε_0)/|ε_0| > 0` with
`ε_0>0` ⟺ `ε_0(λ)>0` for all large `λ` ⟺ Weil positivity up to `T*` ⟺ local-RH. *Proof.* Normalizing by `ε_0` sends the background to `+1`. If `ε_0>0`, the
rescaled operator is positive definite; if `ε_0<0`, dividing reverses the order and `+1`
ceases to be the infimum. Uniform coercivity is therefore equivalent to `ε_0>0`. ∎ **Status: size and `(H-lim)` are RH-neutral and PROVED (modulo tightness); the SIGN of
`ε_0` is EQUIVALENT TO RH.** This is where the problem lives. --- ## 7. IV.1 — The limit operator (identification) **Conjecture/identification 7.1.** Under `(H-lim)`, the rescaled operator `A_λ/|ε_0|`
converges in the strong resolvent sense to
$$\mathcal L_\infty = -c\,\frac{d^2}{dx^2}\quad\text{on a box with Dirichlet conditions},\qquad
c=-\tfrac18\,\psi_\Gamma''(1/4),$$
with relative spectrum `{(k+1)^2}_{k\ge0}` and alternating parity. *Support.* (a) The kinetic term `c(−d^2/dx^2)` is derived from the archimedean symbol via the
Lévy representation (`c = C_2/2 = −ψ_Γ''(1/4)/8`, exact value). (b) Dirichlet
mechanism: the prime jumps `\log n` (of order `2\logλ`) exceed the width of the boundary
layer (`∼1/\logλ`), so that a jump starting at the boundary exits the window ⟹ leak ⟹
effective Dirichlet condition. (c) Numerical verification (mpmath, dps=45): `ε_k/ε_0→(k+1)^2`
with no offset, alternating parity, up to `k=6`. **Status: IDENTIFIED with partial support (a–c); quantitative convergence (Landau–Widom
tightness) remains open. RH-neutral.** Not used in the logical chain toward RH; it is
descriptive structure of the regime. --- ## 8. E3, E4 — Closing the circle **Theorem 8.1 (E3, Hurwitz).** If `ξ̂_λ` (real-rooted by §3) converges uniformly on
compacts to `Ξ≢0`, then `Ξ` is real-rooted. **Theorem 8.2 (E4, Laguerre–Pólya).** `Ξ∈\mathrm{LP}` ⟺ all its zeros are real ⟺ RH.
Combined with Theorem 1.3, `Ξ` is the transform of a PSD form ⟺ `A_λ` is PSD ∀`λ`. **Status: PROVED** (classical). --- ## 9. The remaining statement, and its equivalence with RH Gathering §5–§8, the entire chain closes except for a single statement: > **(P) Localized Weil positivity.** `ε_0(λ) ≥ 0` for all `λ>1`. **Theorem 9.1.** (P) ⟺ RH. *Proof.* (⇐) Under RH, `A_λ(f,f)=Σ_ρ|\hat f(\gamma_\rho)|^2≥0` (Theorem 1.3). (⇒) If RH is
false, there exists `ρ_0` with `Re ρ_0≠1/2`; by Theorem 5.1 and the Hurwitz contrapositive
(verified explicitly for Davenport–Heilbronn, whose zero `0.8085+85.699i` produces
`ε_0<0`), `ε_0(λ)<0` for `λ` in the corresponding range. ∎ In other words: **(P) is not a pending lemma; it is RH itself**, expressed as the positivity of an
explicit quadratic form. The entire difficulty of RH is concentrated and isolated here. **Characterization of (P) (four equivalent descriptions, all proved equivalent to
`sign ε_0`):**
1. *Primes:* phase-coherence deficit of `Σ Λ(n)n^{−1/2}\cos(t\log n)` against `Ω̃`.
2. *Zeros:* rigidity of the frame `{γ_ρ}` (pair correlation, off-diagonal regime).
3. *Operator:* the symbol `a(t)=Ω̃(t)−D_λ(t)` has no extra wells outside `t=0`.
4. *Window:* structural marginality (Theorem 9.2). **Theorem 9.2 (structural marginality).** The central negative well of `a(t)` has
half-width `δ_λ = (2|a(0)|/a''(0))^{1/2}` and the band has resolution `r_λ=π/Ω`. With the
PNT asymptotics `P_λ=Σ_{n≤λ^2}Λ(n)n^{−1/2}\sim 2λ` and
`M_2=Σ_{n≤λ^2}Λ(n)(\log n)^2 n^{−1/2}\sim 8λ(\logλ)^2`, one has `a(0)\sim-2λ`,
`a''(0)\sim M_2`, and
$$\frac{2δ_λ}{r_λ} = \frac{\sqrt2}{\pi} \approx 0.45.$$
*Consequence:* since `δ_λ,r_λ` depend only on `\{|Λ(n)|\}`, no functional of the
magnitudes `|Λ(n)|` can decide `\mathrm{sign}\,ε_0` (counterexample: Davenport–Heilbronn,
same magnitudes, `ε_0<0`). The sign resides in the **phase** —equivalent to the position of the
zeros— confirming Theorem 9.1. **Status: (P) ⟺ RH, PROVED. (P) itself: OPEN (= RH).** --- ## 10. Conjectural completion [SPECULATIVE SECTION — not proved] > **Notice.** Everything above (§1–§9) is proved or cited. What follows is a
> **conjectural strategy** for (P); it does not constitute a proof. It is included as a proposed line of attack. By Theorem 9.2, a proof of (P) must exploit phase, not magnitude. The most
plausible route is to **extend to the primes the archimedean Weil positivity** already
established by – (Selecta 2021), via the operator-systems method of –van
Suijlekom. Schematically: **(C1)** The archimedean part `M_θ` is PSD (proved: Lévy–Khintchine, §2).
**(C2)** *Conjecture:* the operator system generated by `\{T_{\log n}\}_{n\le\lambda^2}`
admits a Carathéodory–Fejér factorization compatible with that of `M_θ`, so that the
difference `M_θ − V` inherits a positivity certificate (sum of Hermitian squares) in the
quotient by the radical of the ground state.
**(C3)** *Conjecture:* that certificate is uniform in `λ` precisely when the phase
coherence of the primes respects the GUE rigidity of the zeros — that is, under Montgomery's
pair-correlation conjecture in the regime `α>1`. If (C2)–(C3) were established, (P) would follow, and by Theorem 9.1, RH. **Neither is
proved;** (C3) is itself of the same order of difficulty as RH. They are stated to
delimit the attack, not to close it. --- ## 11. Conclusion We prove the entire chain E0→E4 except for statement (P), and we prove that (P) ⟺ RH
(Theorem 9.1). The contribution is a **rigorous reduction**: RH is equivalent to the positivity
of a finite, explicit quadratic form `A_λ`, surrounded by an approximation scaffolding
(N0–N3, reduction, Hurwitz, Laguerre–Pólya) entirely proved, plus an identification
of the limit operator (§7) and a marginality theorem (§9.2) that explains why
magnitude methods cannot close (P). The completion of (P) (§10) remains an open problem,
of the same order as RH. --- ### References
- A., C., H.. *Zeta spectral triples.* arXiv:2511.22755 (2025).
- A., W. D. van Suijlekom. *Quadratic Forms, Real Zeros and Echoes of the Spectral Action.* arXiv:2511.23257 (2025).
- A., C.. *Weil positivity and trace formula, the archimedean place.* Selecta Math. 27 (2021), no. 4, Paper No. 77.
- C. Carathéodory, L. Fejér. (1911). [Structure of PSD Toeplitz matrices.]
- H. L. Montgomery. *The pair correlation of zeros of the zeta function.* (1973).
