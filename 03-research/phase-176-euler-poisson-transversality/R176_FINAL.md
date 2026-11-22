# R176 — Quick audit of Euler–Poisson transversality

## Verdict

**NO-GO for the formulation proposed via two projections.** The proof
stops before any estimate: the proposal provides no canonical Poisson
discretization on `Z/NZ` associated with the multiplicative cutoff
`k <= N`, and the natural reduction mod `N` is incompatible with
the shifts `log k`. In the
discretization most favorable for `N=4`, the exact vector imposed by
`Lambda*1=log` is fixed by the DFT, and hence the proposed intersection is not
zero. If the two directions that model identifies as polar are removed,
the vector disappears entirely. The continuous alternative has a nontrivial exterior
intersection (Sonine spaces). None of these variants forces the
coherent defect of R161 to vanish.

This result rules out the concrete idea; it does not affect R161.035 nor Paper 46.

## 1. Typing test

In R161.035, the integer `N` appears in

\[
 K_N=\sum_{k\leq N}(\log k)k^{-1/2}\tau_{\log k}.
\]

It is a cutoff of the multiplicative hyperbola. Poisson–Tate, by contrast, acts on
the additive lattice `Z` (or adelically over `Q`). There is no canonical morphism

\[
 \{k:k\leq N\}\longrightarrow \mathbb Z/N\mathbb Z
\]

simultaneously compatible with the product, divisibility, the translation
`log k`, and additive Fourier. Reducing `k mod N` is an additional choice: it identifies
`N` with `0`, does not preserve `log k`, and changes if the cutoff `N` is replaced by another
cutoff containing the same physical contacts. Hence an order-`N` DFT
is not the finite compression of the Poisson term appearing in `(PC)`.

**Result 1 (PROVED, for the proposed construction).** Reduction modulo
`N` does not interlace the physical translations `tau_(log k)` with the additive structure
of `Z/NZ`. Hence it does not define the required Poisson compression. No
nonexistence theorem is claimed about every conceivable discretization.

## 2. The most favorable exact test at N=4

Although not canonical, we test the suggested model. On the fiber `b=4`, the
only divisors with nonzero von Mangoldt are `2` and `4`, and

\[
 {\Lambda(2)\over\log4}={\Lambda(4)\over\log4}={1\over2}.
\]

Taking `4` to the class `0 mod 4`, the normalized amplitude is

\[
 e_4=2^{-1/2}(\delta_0+\delta_2).
\]

For the unitary DFT

\[
 (\mathcal F_4f)(j)={1\over2}\sum_{k=0}^3
 e^{-2\pi ijk/4}f(k)
\]

one computes exactly

\[
 \mathcal F_4e_4=e_4.
\]

Hence, if `P_mult` projects onto the divisor amplitude and `P_add` onto its
Fourier image,

\[
 \operatorname{Ran}P_{4}^{mult}\cap
 \operatorname{Ran}P_{4}^{add}=\mathbb C e_4\ne\{0\}.
\]

There is also a revealing degeneracy. Let

\[
 c={1\over2}(1,1,1,1),\qquad
 \chi_2={1\over2}(1,-1,1,-1).
\]

Then `e_4=(c+chi_2)/sqrt(2)`. If, within this artificial discretization,
the two polar directions are modeled by
declaring `span{c,chi_2}`, the primitive projection of `e_4` is zero. We thus
obtain either a nontrivial intersection, or a vacuous statement; never the
nontrivial TU lemma proposed.

**Result 2 (PROVED).** The finite TU lemma fails already in the first laboratory
`N=4` under the natural DFT discretization.

## 3. The continuous realization does not give vanishing either

The correct realization of Poisson uses support projections `P_Lambda` on
`L2(R)` and its Fourier conjugate

\[
 \widehat P_\Lambda=\mathcal F P_\Lambda\mathcal F^{-1}.
\]

The interior intersection is zero by Paley–Wiener: a function and its transform
cannot both have compact support unless the function is zero. But this
statement contains no `Lambda`, no unique factorization, nor `Lambda*1=log`; it holds for
any comb and cannot produce D's sign.

The opposite happens on the exterior side. Sonine spaces contain
nonzero functions that vanish in a neighborhood of the origin and whose Fourier
transform also vanishes there. Hence

\[
 \operatorname{Ran}(I-P_\Lambda)\cap
 \operatorname{Ran}(I-\widehat P_\Lambda)\ne\{0\}
\]

for admissible scales. This is precisely the geometry described by Burnol and
by Connes–Consani; there is no automatic exterior transversality.

**Result 3 (PROVED/CITED).** The continuous projections offer a
trivial but arithmetically blind interior intersection, and a nontrivial
exterior intersection. Neither claims the vanishing of `z_(N,F)`.

## 4. Comparison with the real coherent defect

The physical object already built is

\[
 z_{N,F}=(K_N^{ren}\mathcal F-JK_N^{ren})F,
\]

and R161.035 proves

\[
 D_N^{coh}(F)={1\over4}\|z_{N,F}\|^2.
\]

The identity `Lambda*1=log` builds `K_N`; it does not claim that `z_{N,F}` belongs
to a proper subspace. Poisson builds the two orientations; it also does not claim
that their difference belongs to a proper Fourier subspace. Defining those
subspaces as the ranges containing `z_{N,F}` would be circular. Defining the
additive subspace as `ker(K_N^{ren}F-JK_N^{ren})` makes membership exactly
`z_{N,F}=0`, the open saturation of R161.035.

**Result 4 (PROVED).** After replacing the artificial DFT by the physical
operators, the proposed second membership is equivalent to the sought
vanishing; it is not an independent consequence of KKT or of Poisson.

## 5. Exact stopping point

The intended chain was

\[
 \text{first contact}
 \Longrightarrow z\in\operatorname{Ran}P^{mult}\cap
 \operatorname{Ran}P^{add}
 \Longrightarrow z=0.
\]

It fails in two places:

1. the proposal does not build the two canonical projections with the
   required types, and its choice mod `N` is mistyped;
2. in the natural finite model the intersection is not zero;
3. in the continuous model, the only trivial intersection is sign-blind;
4. forcing the physical membership merely recodes the open saturation.

Investing another round in the two-projection route is not recommended. The useful
negative datum is: the future law cannot come from support incompatibility or
from separate ranges. It must act on the mixed operator
`K_N^ren F-JK_N^ren` before separating its two orientations, exactly as
the R161–R170 map requires.
