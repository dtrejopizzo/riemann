# LINK_011 — Explicit Mellin–Gauss map from the continuous tests

2026-10-19. **PROVED, favourable review in AUDIT_011.md:** the concrete map defined below converges in 𝓗_α, its FE exhibits exactly the polar moment of the even carrier, but its form is smoothing and **does not coincide with Q_T**. Other maps and a domination with positive remainder are not excluded. Goal D active.

## 0. Corpus check and reason for this computation

Read: the project rules, the ROUTES-TRIED-INDEX index (families, residues 06, entries 209), master grid, crossword, CONSTRUCTOR005–008 and LINK009–010 with audits. Targeted searches: theta and tests, Gaussian maps, sampling/mollifier, co-Poisson, Hamburger and cosh moments. Relevant references: SPEC005, R11_2_ORIGIN, Z_CARRIER, P1_BBSTAR and compression controls.

A continuous interpolation of D_n is not retried, nor an abstract square root of Q_T. Nor is evaluation F(log d) alone used. **New reason:** the Mellin analysis operator of the factor Π of the already constructed kernel −R is fixed, applied to continuous tests, its domain is proved, and its FE and the failure of equality with the three terms of Q_T are computed. This answers a concrete link question; it does not aim to evade the indexed classes by names.

## 1. Objects and candidate with no parameters fitted to Q_T

Fix T>0, 0<α<1/2 and s=2α. Use 𝓗_α and S_α=−R_α of CONSTRUCTOR005–007. The Haar-centred representative of each divisor is

`f_d=X_d−1/d`, d≥2,

with `⟨f_d,f_e⟩_(𝓗_α)=S_α(d,e)`.

Let `W_d(y)=τ(d²y)−τ(y)/d`. For F∈L²([−T,T]) define

`a_d(F)=∫_(exp(−2T))^(exp(2T)) y^(α−1) F((log y)/2)W_d(y)dy`

`       =2∫_(−T)^T e^(2αx)F(x)W_d(exp(2x))dx`,

`U_(T,α)F=Σ_(d≥2) a_d(F) f_d`.                    (1)

This is the analysis of the profiles of Π with the same Mellin measure: in the Gaussian factor the profile of f_d is `q_d−1/d`, and `τ(q_d−1/d)=W_d`. The definition uses τ and the kernel S, not Q_T nor a minimiser.

At α=1/4, which is the candidate for the critical link, the weight of the integral in x is e^(x/2).

## 2. Domain and convergence of the series

**Lemma 1 (PROVED).** For all d≥2 and 0<α<1/2,

`S_α(d,d)≤C_α d^(−s)`

with C_α finite independent of d.

**Proof.** By CONSTRUCTOR005,

`S_α(d,d)=(−Z_α)[d^(−s)−2d^(−s−1)+d^(−2)]+Π_α(d,d)`.

The bracketed expression is ≤2d^(−s). Comparisons of Gaussian sums with integrals give `τ(y)≤c(y)` and `τ(d²y)≥c(y)/d−1`. Together with `q_d≤1/d`, obtained from punctured concavity,

`0≤1/d−q_d(y)≤min(1/d,√y)`.

For the second bound, if c/d−1≥0 divide that lower bound by τ≤c; if it is negative, q_d≥0 suffices. Hence

`Π_α(d,d)≤∫_0^∞ y^(α−3/2)min(d^(−2),y)dy`

`=[1/(α+1/2)+1/(1/2−α)]d^(−2α−1)`.

Both integrals split at y=d^(−2). This proves the lemma. ∎

**Lemma 2 (PROVED).** For y∈[exp(−2T),exp(2T)] and any integer j≥0,

`|∂_x^j W_d(exp(2x))|≤C_(T,j)/d`, `|x|≤T`.

**Proof.** The summand −τ(exp(2x))/d has that bound on every compact set. The other summand and its derivatives are Gaussian sums of polynomial factors in d²n²exp(2x), and decay exponentially in d² uniformly on the compact set. The exponential bound implies the bound C/d for d≥2. ∎

In particular `|a_d(F)|≤C_(T,α)||F||₂/d`. By Lemma 1,

`Σ_d |a_d(F)|·||f_d|| ≤ C_(T,α)||F||₂ Σ_d d^(−1−s/2)<∞`.

Thus (1) converges absolutely in the norm of 𝓗_α and defines a bounded linear operator from **all** of L²([−T,T]). Membership of a formal infinite series in the domain is not assumed.

## 3. Resulting continuous kernel: effective formula

Define the analysis vector

`b_(T,α)(x)=2e^(2αx)Σ_(d≥2)W_d(exp(2x)) f_d`, `|x|≤T`.

Lemmas 1–2 show uniform convergence in Hilbert norm, also after each finite number of derivatives. Hence b is C∞ and

`U_(T,α)F=∫_(−T)^T F(x)b_(T,α)(x)dx`.

The induced positive form is

`𝔈_(T,α)(F)=||U_(T,α)F||²`

`=∫∫ F(x)conjugate(F(x′)) L_(T,α)(x,x′)dx dx′`,

`L_(T,α)(x,x′)=4e^(2α(x+x′))`

` ·Σ_(d,e≥2)W_d(exp(2x))W_e(exp(2x′))S_α(d,e)`.

The sum has the meaning of the inner product of b(x),b(x′); the bound `|S(d,e)|≤sqrt(S(d,d)S(e,e))` also proves its absolute convergence and that of all derivatives. **L is C∞ on the compact square.** U is Hilbert–Schmidt, in particular compact.

This is an explicit effective kernel in the continuous coordinates x. It is not automatically declared outside every multiplier class after Fourier or restrictions; to decide the link that classification is not needed, because it can be compared directly with Q_T.

## 4. FE and polar moment: exact identity of the critical map

Fix α=1/4 and F even. The inversion x↦−x and the exact formula of CONSTRUCTOR006 give

`W_d(exp(−2x))`

`=e^x/d[τ(exp(2x)/d²)−τ(exp(2x))]−(1−1/d)`.

Substitute it in a_d and use parity:

`a_d(F)= (2/d)∫_(−T)^T F(x)e^(x/2)`

`                   ·[τ(exp(2x)/d²)−τ(exp(2x))]dx`

`         −2(1−1/d)∫_(−T)^T F(x)cosh(x/2)dx`.       (2)

There is no stationary-phase remainder nor any discarded term. The equality is valid for every even F in L² of the interval.

On the polar-free carrier, `∫F cosh(x/2)=0`, the last line vanishes exactly. Thus **the polar moment of this map does coincide with the declared linear restriction**. This does not identify the full quadratic contribution of that moment with the pole of Q_T: when computing ||UF||² cross products between the two terms of (2) also appear. The coefficients of the polar block of the paper have not been proved from that expansion.

The derivation of (2) uses F(−x)=F(x). For non-even F, the change of variable keeps F(−x) in the transformed terms; (2) is not used without that reflection nor extrapolated to the odd sector.

**Limit of the polar expansion.** (2) is an identity for each coefficient before summing over d. If C(F)≠0, its two lines are not summed separately as vectors of 𝓗: the formal series `Σ_(d≥2)(1−1/d)f_d` diverges. Indeed, the positive rank-one component of S gives as a lower bound for the norm of its partial sums `(-Z_α)|Σ_(d≤N)(1−1/d)(d^(−s)−d^(−1))|²`, which diverges for s<1. The cancellation between both lines must be carried out before taking the series. For C(F)=0, the backward coefficient equals the already controlled a_d=O(1/d). Hence the computation constructs neither a separate polar vector nor an identity of the quadratic polar block.

## 5. Cross-check of gamma and comb: the map does not give equality with Q_T

On the even polar-free carrier of Paper47, the sought form is the archimedean form minus the comb:

`Q_T(F)= (1/(2π))∫ m(t)|F̂(t)|²dt`

`         −Σ_(n<exp(2T)) (2Λ(n)/√n) c_F(log n)`.

Here `m(t)=Re ψ(1/4+it/2)−logπ~log|t|−log(2π)` by the asymptotics of the digamma; the exact representation and the domain are in Paper47 eq:Aform and thm:A. Only that definition is cited, not a new claim about its sign.

The comb in a fixed window is a bounded operator: its form in absolute value is ≤`(Σv_n)||F||²`. The gamma term has logarithmic frequency growth and is unbounded on the L² ball of smooth tests of the polar-free carrier. In contrast, 𝔈_(T,1/4) is a bounded smoothing form with C∞ kernel.

### Explicit high-frequency test preserving the polar condition

Choose φ∈C_c∞((−T,T)) even nonzero, and χ also even in that space with `C(χ):=∫χcosh(x/2)≠0`. Put

`g_λ(x)=φ(x)cos(λx)`,

`F_λ=g_λ−[C(g_λ)/C(χ)]χ`,

and normalise F_λ to L² norm=1. Then C(F_λ)=0. Integration by parts gives C(g_λ)=O_M(λ^(−M)) for all M, and F_λ converges weakly to 0.

The transform of g_λ consists of two translates of φ̂ to frequencies ±λ. The asymptotics of the gamma symbol and the rapid decay of φ̂ give

`gamma(F_λ)=logλ+O(1)`.

The correction with χ does not alter the main term, because of its superpolynomially small coefficient. The comb contribution remains uniformly bounded. Hence

`Q_T(F_λ)→+∞`,

while compactness of U implies

`𝔈_(T,1/4)(F_λ)→0`.

**Exact class conclusion:** for the map (1), the identity `Q_T=||U_(T,1/4)·||²` is false. This is not an exclusion of every map from tests to 𝓗, nor are LINK009 or 010 used as if they proved it.

### The comb compared as a kernel

The kernel L of §3 is smooth. It does not by itself produce the translation atoms `x−x′=±log n` of the comb. Nor does it produce the gamma operator of logarithmic order, whose Lévy energy has kernel K(u)~1/u near the origin. This fact agrees with the previous test; no attempt is made to compensate those terms by calling them a positive remainder without proof.

## 6. Exact remainder and unresolved question

For this candidate the remainder is perfectly defined:

`𝔅_T(F)=Q_T(F)−𝔈_(T,1/4)(F)`.

`𝔅_T≥0` has not been proved. The positive divergence at high frequency only localises a favourable behaviour there; **it does not decide its sign in the low directions nor their couplings**, which are the original difficulty.

As a distributional identity of forms, 𝔅 keeps the singular gamma and all the atoms of the comb, plus the smooth kernel −L. This indicates exactly why the polar FE of (2), although correct, does not complete the link. The map smooths the terms whose cancellation needed to be preserved.

No NO-GO is declared for a domination `Q_T≥𝔈`, for non-smoothing maps, for irregular compressions of D_n nor for O1. Those statements require other constructions and proofs.

## 7. Outcome of the attempt

A single map was computed from the continuous tests to the positive kernel −R, with controlled domain and series and without choosing coefficients from Q_T. Its FE shows exactly the cosh moment of the even carrier. Its effective form is smooth and fails as an identity of the node by the explicit cross-check of gamma and comb.

**Outcome:** candidate (1) computed, equality with Q_T refuted for that candidate; domination with positive remainder OPEN. Paper47 was not modified and goal D was not closed.
