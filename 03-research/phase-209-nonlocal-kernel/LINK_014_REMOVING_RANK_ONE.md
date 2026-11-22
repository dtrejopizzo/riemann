# LINK_014 — Removing the rank one does not repair map 011

2026-10-19. **PROVED, favourable review in AUDIT_014.md and its addendum**, with the same CITED input from Paper46 used and verified in LINK013. No new numerical computations.

**Result:** the Gaussian energy Π, by itself, is still too large on the explicit family F_T of Paper46 to admit a domination `Q_T≥c·Π(a(F))` with c>0 independent of T. Hence removing only the term κvv* from the kernel −R while keeping the same coefficient map a_d(F) does not work either.

This result is not inferred from the NO-GO of the full norm in LINK013: the Π component is computed again on the same tests and shown not to vanish. D and other maps remain open.

## 0. Corpus and written difference

Consulted: the project rules, the ROUTES-TRIED-INDEX index (LINK011–013, rank one, subkernels and margin family), grid and crossword, CONSTRUCTOR005 and LINK013. The test T=4/5 is not revisited, nor is the size of an infimum used as proof of the response of a map.

**Exact difference from 013:** its lower bound used κvv*. Removing that summand changes the form and the argument of 013 no longer applies. Here the explicit map 011 is kept and the remaining Gaussian summand Π is studied. The new step is a positive L¹ kernel and the local limit of the same family of tests, which give a lower bound of order T for Π.

## 1. Forms being compared, with no implicit projection

Fix α=1/4, s=1/2 and κ=−Z_(1/4)>0. Recall

`S=−R=κG_s+κvv*+Π`, `v(d)=d^(−1/2)−d^(−1)`.

The coefficients are exactly those of LINK011:

`a_d(F)=2∫F(x)e^(x/2)W_d(exp(2x))dx`,

`W_d(u)=τ(d²u)−τ(u)/d`, `q_d(y)=τ(d²y)/τ(y)`.

Define the two reduced energies

`E_Π(F)=Σ conjugate(a_d(F))a_e(F)Π(d,e)`,

`E_red(F)=Σ conjugate(a_d(F))a_e(F)[S(d,e)−κv(d)v(e)]`.

Both are PSD and `E_red≥E_Π`. A summand of the **kernel** is removed; it is not assumed that this is an orthogonal projection along a vector defined in the completion of S. The coefficients and their normalisation do not change.

Convergence is inherited from the absolutely convergent series of LINK011, since `Π≤S` and `S−κvv*≤S` as forms.

## 2. Positive kernel of the Gaussian component

For fixed y>0, put

`f_d(y)=q_d(y)−1/d<0`,

`K_y(x)=2e^(x/2)Σ_(d≥2)W_d(exp(2x))f_d(y)`.

Each summand is positive: W_d<0 and f_d(y)<0 by the already proved punctured concavity. On compact sets of x the sum converges uniformly, by W_d=O(1/d) and |f_d(y)|≤1/d.

**Lemma 1 (PROVED).** K_y is non-negative and integrable on all of R, with

`∫_R K_y(x)dx=C(y)`

`=κΣ_(d≥2)v(d)[1/d−q_d(y)]`,                       (1)

`0<C(y)≤κ[ζ(3/2)−ζ(2)]<∞`.

**Proof.** Change u=exp(2x) and use `W_d(u)=m(u)/d−m(d²u)` together with the Mellin transform of m:

`∫_R 2e^(x/2)W_d(exp(2x))dx`

`=∫_0^∞u^(−3/4)W_d(u)du=κ/d−κd^(−1/2)=−κv(d)`.

The integral converges absolutely because W_d keeps its sign and the two positive Mellin transforms of m are finite. Tonelli applies to the positive products with f_d(y) and gives (1). The sum is ≤κΣv(d)/d, which is the stated value. It is strictly positive because each difference 1/d−q_d(y) is. ∎

For a bounded compactly supported test F, interchanging sum and integral —dominated by ||F||∞K_y— gives

`B_F(y):=Σ_(d≥2)a_d(F)f_d(y)=∫_R F(x)K_y(x)dx`.     (2)

This function represents the Gaussian component of the vector U_TF and

`E_Π(F)=∫_0^∞y^(−3/4)τ(y)|B_F(y)|²dy`.              (3)

To link the pointwise and Hilbert identities, partial sums can be taken: they converge in the Gaussian factor by LINK011 and pointwise by (2); both limits coincide almost everywhere.

## 3. The same family F_T and its computed local limit

Use exactly the family of LINK013/Paper46 for T≥1 (in particular k≥8):

`k=ceil(21T/e)`, `a=21/e`,

`G_T(x)=ω_k(x/T)`, `ω̂_k(u)=sinc(u/k)^k`,

`F_T=G_T''''+(γ₁²−1/4)G_T''−(γ₁²/4)G_T`.

F_T is even, lies in the polar-free carrier and has support [−T,T].

**Lemma 2 (PROVED).** For each fixed x,

`G_T(x)/√T→g₀:=sqrt(3a/(2π))>0`,

while `sup_x|G_T(x)|/√T` remains bounded. Moreover

`||G_T''||∞=O(T^(−1/2))`, `||G_T''''||∞=O(T^(−3/2))`. (4)

**Proof of the local limit.** Fourier inversion, v=u/k and z=√k v give

`G_T(x)/√T=√(k/T)/(2π)`

` ·∫_R exp(i√k zx/T) sinc(z/√k)^k dz`.

For fixed z, the integrand tends to exp(−z²/6), and its phase tends to 1 because √k/T→0. On |z|≤√k the absolute value is dominated by exp(−z²/7), using the elementary sine bound of LINK013. The integral outside that range tends to 0: for 1≤|v|≤2 one uses |sinc v|≤sin1<1, and for |v|≥2 one uses |sinc v|≤1/|v|. Hence the limit is

`√a/(2π)∫exp(−z²/6)dz=sqrt(3a/(2π))`.

The same absolute estimate gives the uniform bound on the supremum. For derivatives,

`||G_T^(j)||∞≤(T^(−j)k^(j+1)/(2π))∫|v|^j|sinc v|^k dv`

`=O_j(T^(−j)k^((j+1)/2))=O_j(T^((1−j)/2))`.

The ranges are bounded in the same way; taking j=2,4 proves (4). ∎

Consequently, for each fixed x,

`F_T(x)/√T→−γ₁²g₀/4`,                              (5)

and there is a bound on `|F_T(x)|/√T` uniform in x and large T. These claims concern the functions extended by zero; for fixed x one is inside the support when T is large.

## 4. The Π component does not vanish: at least linear energy

For fixed y>0, apply (2), Lemma 1, (5) and dominated convergence:

`B_(F_T)(y)/√T→−(γ₁²g₀/4)C(y)≠0`.                  (6)

The measure in (3) is positive. Restricting it to y∈[1,2] and applying Fatou gives

`liminf_(T→∞) E_Π(F_T)/T`

`≥(γ₁⁴g₀²/16)∫_1² y^(−3/4)τ(y)C(y)²dy=:L₀>0`.    (7)

The integral is finite by the uniform bound on C(y) from Lemma 1 and positive because C(y)>0 for each y. The function C is measurable as a positive sum of continuous functions. To interpret the liminf with real T, apply Fatou to any sequence T_j→∞; the bound does not depend on the sequence.

Hence, for T sufficiently large,

`E_red(F_T)≥E_Π(F_T)≥(L₀/2)T`.                      (8)

The term κvv* was not used in any bound of this section.

## 5. Cross-check with Q and exclusion of all constant scales

**CITED, verified in LINK013 against the proof of Paper46.** For these same F_T,

`|Q_T(F_T)|/||F_T||²≤4·10⁹ T exp(−15.449T)`.

The bound on the L² derivatives of LINK013 gives `||F_T||²=O(T^(3/2))`. Then

`|Q_T(F_T)|=O(T^(5/2)exp(−15.449T))`.

Together with (8),

`|Q_T(F_T)|/E_Π(F_T)=O(T^(3/2)exp(−15.449T))→0`.     (9)

**Theorem 3 (PROVED, with the above CITED input).** For each c>0, for all T sufficiently large one has

`Q_T(F_T)<cE_Π(F_T)≤cE_red(F_T)`.

Hence, as uniform claims over all windows and tests, both

`Q_T(F)≥cE_Π(F)`

and

`Q_T(F)≥cE_red(F)`

are false.

The refutations transfer to a smooth C_c∞ core by the polar-corrected H¹ approximation of LINK013: Q is continuous in H¹ and the two reduced forms are bounded by the energy of U in each window, which is continuous in L².

A T-dependent scale is not excluded. If it were valid for either of these energies, this family imposes the necessary condition `c(T)=O(T^(3/2)exp(−15.449T))`; its existence is not proved.

## 6. Exact scope

The concrete repair «remove κvv*» was studied, with the same coefficients of map 011, and an independent obstruction was obtained in the Gaussian term Π. No obstruction was illegitimately transferred from a larger form to a smaller one.

Other maps, other changes of domain, sufficiently small window-dependent scales and a possible use of −R in a different identity are not excluded. The bound on Q, which uses zero information from the paper, serves here only to refute these dominations, not as new positivity for D. No paper is modified.

**Status:** NO-GO PROVED for the uniform constant dominations of this memo; favourable audit in AUDIT_014.md, including the extension §7. D remains OPEN and active.

## 7. Last piece: the arithmetic covariance G_s alone also fails

This extension uses the same family and the same coefficients of 011, with no other map. Let s=1/2 and

`L₂(F)=Σ_(d≥2)a_d(F)G_s(d,2)`.

Since

`G_s(d,2)=(1−1/√2)d^(−1/2)1_(2|d)`,

the sum converges absolutely by a_d=O(1/d). Cauchy–Schwarz in the covariance G_s gives

`E_G(F):=Σ conjugate(a_d)a_eG_s(d,e)≥|L₂(F)|²/G_s(2,2)`,

`G_s(2,2)=1/√2−1/2>0`.                              (10)

Define the profile

`h₂(x)=2e^(x/2)Σ_(d≥2)W_d(exp(2x))G_s(d,2)`,

`β=(1−1/√2)/2>0`.

Then h₂ is continuous and bounded, `h₂(+∞)=0`, and

`h₂(−∞)=−κβ`.                                      (11)

**Proof of (11).** It is the Riemann computation of LINK013 restricted to even indices. With N=y^(−1/2), g(r)=r^(−1/2)m(r²) and I=∫g=κ/2,

`N^(−1/2)Σ_(2|d)d^(−1/2)m((d/N)²)`

`=(1/N)Σ_(2|d)g(d/N)→I/2=κ/4`.

The controls at the origin and the tail are the same, with mesh 2/N. The term `N^(−1/2)m(N^(−2))Σ_(2|d)d^(−3/2)` tends to 0. Multiplying by `−2(1−1/√2)` gives (11). Continuity, boundedness and the right limit are obtained from the same bounds of LINK013. ∎

By absolutely convergent interchange, `L₂(F)=∫Fh₂`. Applying the escaping mass of G_T/T and the L¹ bounds of its derivatives, exactly as in LINK013, yields

`L₂(F_T)/T→γ₁²κβ/8>0`.                             (12)

From (10), `E_G(F_T)≥c₂T²` for T sufficiently large and some constant c₂>0. Consequently no window-independent c>0 allows `Q_T≥cE_G` on all tests.

### Corollary for combinations of the three existing summands

For constants A,B,C≥0 not all zero, keep exactly a_d(F) of 011 and define

`E_(A,B,C)(F)=AκE_G(F)+Bκ|M(F)|²+C E_Π(F)`.

LINK013 computes `|M(F_T)|²≳T²`; (10)–(12) compute `E_G(F_T)≳T²`; and (7)–(8) compute `E_Π(F_T)≳T`. Since the three summands are non-negative, any fixed nonzero combination satisfies `E_(A,B,C)(F_T)≳T`. The CITED bound on Q in §5 implies

`|Q_T(F_T)|/E_(A,B,C)(F_T)→0`.

Hence **no fixed non-negative nonzero combination of κG_s, κvv* and Π, applied with the same coefficient map 011, admits a positive uniform domination by Q_T**. This includes removing one or two of the summands; it allows no inferences about other coefficients, another map, combinations with signed cancellations or T-dependent factors.

The extension only completes the examination of the three pieces of the retained candidate. It opens no new route and does not modify the status of D.
