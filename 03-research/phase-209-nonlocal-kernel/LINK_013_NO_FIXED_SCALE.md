# LINK_013 — No fixed positive scale repairs map 011 in all windows

2026-10-19. **PROVED, favourable review in AUDIT_013.md**, using as CITED input the bound for the explicit family of Paper47 lem:testfam and the proof of thm:margin/cor:margin1. No new numerical computation.

**Statement:** for each constant c>0 there exist arbitrarily large windows —in fact all sufficiently large ones— and even polar-free tests F_T such that

`Q_T(F_T)<c ||U_TF_T||²`.

U_T is exactly the Mellin–Gauss map of LINK011, without changing its normalisation. A repair by a small universal constant is discarded. A T-dependent scale or another map is not excluded. D remains OPEN and active.

## 0. Corpus and difference from 012

Consulted: the project rules, the ROUTES-TRIED-INDEX index (LINK011/012, margin and family 42/e, residues 06), master grid and crossword. Direct verification in Paper47: lem:testfam, thm:margin **and its proof**, cor:margin1. A small infimum is not confused with a test that does not annihilate U.

**New written reason:** LINK012 only falsified scale 1 at T=4/5. Here T→∞ is used and the response of the **same** U is computed on the explicit family of the paper that has small Q quotient. The new fact to be proved is that U does not share its vanishing: its rank-one component grows linearly in T. Only then is the bound of the paper applied.

The CITED upper bound of the paper uses certified zero information and the explicit formula. It is used here exclusively to refute a proposed domination, not as a new source of positive sign for D nor via external equivalences.

## 1. Rank-one component of the map U

Use κ=−Z_(1/4)>0 and v(d)=d^(−1/2)−d^(−1). By CONSTRUCTOR005 and LINK012,

`||U_TF||²≥κ|M(F)|²`,

`M(F)=Σ_(d≥2)a_d(F)v(d)=∫_(−T)^T F(x)h(x)dx`,

`h(x)=2e^(x/2)Σ_(d≥2)v(d)W_d(exp(2x))`.

The profile h does not depend on T: the windows only restrict the integral. Define

`m(y)=y^(−1/2)−τ(y)`, `z_c=ζ(3/2)−ζ(2)`.

Since W_d(y)=m(y)/d−m(d²y), the same series is

`h(x)=2y^(1/4)[z_c m(y)−Σ_(d≥2)(d^(−1/2)−d^(−1))m(d²y)]`, `y=exp(2x)`.  (1)

Both expressions converge absolutely for each x; no divergent polar vector is split off.

## 2. Asymptotics of the profile: h(−∞)=−κ and h(+∞)=0

**Lemma 1 (PROVED).** h is continuous and bounded on R and

`lim_(x→−∞)h(x)=−κ`, `lim_(x→+∞)h(x)=0`.

**Proof.** From Poisson and the Gaussian comparison,

`0<m(y)<min(1,y^(−1/2))`.

Put N=y^(−1/2) and

`g(r)=r^(−1/2)m(r²)`.

The function g is continuous on (0,∞), with integrable bound `g(r)≤min(r^(−1/2),r^(−3/2))`. The Riemann sum satisfies

`N^(−1/2)Σ_(d≥2)d^(−1/2)m((d/N)²)`

`=(1/N)Σ_(d≥2)g(d/N)→∫_0^∞g(r)dr`.

To justify the singularity and the tail uniformly, the range d≤εN is ≤2√ε+o(1); the range d≥RN is ≤2/√R+o(1); between both ends the usual Riemann sum applies. Omitting d=1 costs O(N^(−1/2)).

The integral is

`I=∫_0^∞r^(−1/2)m(r²)dr=(1/2)∫_0^∞y^(−3/4)m(y)dy=κ/2`.

Meanwhile,

`Σ_(d≥2)d^(−1)m((d/N)²)=O(1+logN)`

by splitting into d≤N and d>N and using the two bounds of m. Multiplied by N^(−1/2), that term tends to 0, as does `N^(−1/2)z_c m(N^(−2))`. Formula (1) gives h(−∞)=−2I=−κ.

At +∞ the representation with τ is used: all terms decay in a Gaussian way in exp(2x), and their sum, multiplied by exp(x/2), tends to 0. Local uniform convergence follows from the bounds of LINK011. The Riemann sums above are also uniformly bounded, and give global boundedness of h. ∎

For the even profile `h_ev(x)=[h(x)+h(−x)]/2` one concludes

`h_ev(x)→−κ/2` as |x|→∞.                         (2)

## 3. The precise family of the paper, not an abstract minimiser

From now on work with T≥1, so that k≥8. Let γ₁ be the first ordinate used in Paper47 lem:testfam and fix

`k=k(T)=ceil(21T/e)`,

`b_k=(k/2)1_[-1/k,1/k]`, `ω_k=b_k^{*k}`,

`G_T(x)=ω_k(x/T)`,

`P(D)=D⁴+(γ₁²−1/4)D²−γ₁²/4`,

`F_T=P(D)G_T`.

By the cited lemma, F_T is real, even, supported in [−T,T], of finite energy, and its two exponential moments ±1/2 are zero. Hence it belongs to the polar-free carrier, with `Q_T(F_T)=𝔞_T(F_T)`.

Moreover G_T≥0 and `∫G_T=T`. F_T is not normalised yet: the comparison of the two forms is homogeneous.

## 4. Spline estimates needed to compute M(F_T)

**Lemma 2 (PROVED).** For each fixed integer j≥0,

`||ω_k^(j)||₂²=O_j(k^(j+1/2))`, `||ω_k||∞=O(√k)`.

**Proof.** By Plancherel and `ω̂_k(u)=sinc(u/k)^k`,

`||ω_k^(j)||₂²=(k^(2j+1)/(2π))∫v^(2j)|sinc(v)|^(2k)dv`.

For |v|≤1, the alternating series of the sine gives `|sinc v|≤1−v²/7≤exp(−v²/7)`, and the integral with the weight v^(2j) is O_j(k^(−j−1/2)). For 1≤|v|≤2, `|sinc v|≤sin1<1`; for |v|≥2 one uses `|sinc v|≤1/|v|`. The last two contributions decrease exponentially and are absorbed in the stated bound for large k. The argument with `∫|ω̂_k|` and exponent k, without the weight, gives `||ω_k||∞=O(√k)`. ∎

Since k~T, the change of scale gives

`||G_T^(j)||₂=O_j(T^(3/4−j/2))`.

In particular,

`||G_T''||₁=O(T^(1/4))`,

`||G_T''''||₁=O(T^(−3/4))`,

`||F_T||₂²=O(T^(3/2))`.                             (3)

The two L¹ bounds use the support of length 2T and Cauchy–Schwarz; h is not differentiated to obtain them.

### The mass of G_T/T escapes every compact set

It is an even probability. For fixed R,

`(1/T)∫_|x|≤R G_T(x)dx≤(2R/T)||ω_k||∞=O_R(T^(−1/2))→0`.

By (2), boundedness of h and parity of G_T,

`(1/T)∫G_T(x)h(x)dx→−κ/2`.                         (4)

The proof separates a compact set where its mass tends to 0 and its complement where h_ev is uniformly close to −κ/2.

## 5. U does not share the vanishing of the family: M grows like T

By definition of F_T,

`M(F_T)=−(γ₁²/4)∫G_T h`

`       +(γ₁²−1/4)∫G_T''h+∫G_T''''h`.

The profile h is bounded. The two L¹ bounds of (3) make the derivative terms o(T). With (4), one obtains the exact asymptotics

`M(F_T)/T→γ₁²κ/8>0`.                               (5)

Consequently,

`||U_TF_T||²≥κ|M(F_T)|²`,

`liminf_(T→∞) ||U_TF_T||²/T² ≥γ₁⁴κ³/64>0`.          (6)

This is the step that does not follow from a small margin: the response of the map was computed on the same tests that will be used to bound Q.

## 6. Bound on Q for THIS family and comparison

**CITED and verified against the proof of Paper47.** The proof of thm:margin takes precisely F_T from lem:testfam; its step (6) bounds `𝔞_T(F_T)` by a sum of absolute values, and its step (7) divides by a lower bound for `||F_T||²`. The optimisation k=ceil(21T/e) of cor:margin1 gives, for T≥1,

`|Q_T(F_T)|/||F_T||²≤4·10⁹ T exp(−15.449T)`.            (7)

(7) is not inferred from `inf Q/||F||²` by an illegitimate logical switch: the concrete family of the proof is used. The zero input of the paper is limited to this CITED upper bound.

By (3),

`|Q_T(F_T)|≤O(T^(5/2)exp(−15.449T))`.

By (6), the denominator `||U_TF_T||²` is ≥c₀T² for some constant c₀>0 and T sufficiently large. Thus

`|Q_T(F_T)|/||U_TF_T||²=O(T^(1/2)exp(−15.449T))→0`     (8)

without presupposing Q_T≥0. If some Q were negative, the positive domination would already fail there. The absolute value in (7) comes from the absolute sum of step (6) of the proof of the paper, although the statement of the corollary only needs its upper bound without absolute value.

## 7. Universal-scale exclusion theorem

**Theorem 3 (PROVED, with CITED input (7)).** For each c>0 there exists T_c such that for all T≥T_c,

`Q_T(F_T)<c||U_TF_T||²`.

Hence there is no positive constant c independent of T with

`Q_T(F)≥c||U_TF||²`

for all windows and all even polar-free tests of the carrier.

The same refutation reaches a C_c∞ core: for each window giving a strict inequality, approximate F_T in H¹ by smooth even tests and correct the cosh moment. Q_T is continuous in H¹ and U_T in L²; the strict margin is preserved.

### T-dependent scales

The result does not exclude c(T)>0. If a domination of that type were valid, the computed family would force

`c(T)≤O(T^(1/2)exp(−15.449T))`

for large T. This is only a necessary condition; it does not prove that such a scale exists nor that its choice produces a useful sign.

## 8. Scope

LINK012 refuted scale 1 in one window. This note excludes **every positive universal constant** for the same map, because its rank-one component does not vanish on the explicit family of small Q energy.

The kernel −R is not changed, and neither another map nor a generic norm is presented as a proof of D. Different maps, general compressions and a possible exact link that changes class are not excluded. Goal D remains open and active.
