# 106.160 — The archimedean spin page and the Lefschetz grading

## 1. Purpose

Document 106.159 derives the ordinary-prime factors from harmonic transfer
on the Tate prime fibres.  The remaining local term in the completed
explicit formula is the Gamma density

\[
 g_\Gamma(u)=\frac{e^{-u/2}}{1-e^{-2u}},
 \qquad u>0.                                      \tag{1}
\]

This note gives an exact positive operator realization of (1) and separates
it from the two polar characters.  The result completes the local graded
dictionary: prime fibres, the archimedean spin page, and the \(H^0/H^2\)
plane are all explicit.  What remains is a global Lefschetz complex whose
fixed-point formula has these local terms and whose degree-one
polarization descends faithfully.

## 2. Positive spin realization of the Gamma density

Let

\[
 \mathcal H_\Gamma=\ell^2(\mathbb N_0),
 \qquad
 N_\Gamma e_m=\left(2m+\frac12\right)e_m.          \tag{2}
\]

### Theorem 2.1 — Exact archimedean trace

For every \(u>0\), \(e^{-uN_\Gamma}\) is positive and trace class, and

\[
 \boxed{
 \operatorname {Tr}_{\mathcal H_\Gamma}(e^{-uN_\Gamma})
 =\frac{e^{-u/2}}{1-e^{-2u}}.}                    \tag{3}
\]

#### Proof

The spectrum in (2) is positive and discrete.  Therefore

\[
 \operatorname {Tr}(e^{-uN_\Gamma})
 =\sum_{m\ge0}e^{-(2m+1/2)u}
 =e^{-u/2}\sum_{m\ge0}e^{-2mu},
\]

which is (3). □

The half-integer offset is the archimedean spin shift; the spacing (2)
is the parity selected by the real Gamma factor.  Thus the Gamma density is
not merely positive as a scalar function.  It is an ordinary trace of a
positive semigroup on a source-defined Hilbert page.

## 3. The polar plane

Let

\[
 \mathcal H^{\rm triv}=\mathbb C e_0\oplus\mathbb C e_2,
 \qquad
 N_{\rm triv}e_0=-\frac12e_0,
 \qquad
 N_{\rm triv}e_2=\frac12e_2.                      \tag{4}
\]

Then

\[
 \boxed{
 \operatorname {Tr}_{\mathcal H^{\rm triv}}(e^{-uN_{\rm triv}})
 =2\cosh(u/2).}                                   \tag{5}
\]

This is exactly the threshold density occurring in the compensated Weil
measure.  The negative eigenvalue in (4) is not a defect of the desired
degree-one polarization.  It is the cohomological \(H^0/H^2\) Tate pair
before the weight-one normalization.

Combining (3), (5), and the Tate-prime atoms gives the exact signed source

\[
\boxed{
 d\sigma(u)=
 \sum_{p,k\ge1}\log p\,p^{-k/2}\delta_{k\log p}(du)
 +\operatorname {Tr}(e^{-uN_\Gamma})\,du
 -\operatorname {Tr}(e^{-uN_{\rm triv}})\,du.}     \tag{6}
\]

Equation (6) is the operator-graded version of the compensated source in
106.66 and 106.102.

## 4. Why (6) is local data, not yet the polarization

The prime and Gamma terms in (6) are geometric fixed-point terms.  They are
not eigenstates of the desired global \(H^1\).  A Lefschetz formula has the
direction

\[
 \operatorname {Tr}(H^0)-\operatorname {Tr}(H^1)
 +\operatorname {Tr}(H^2)
 =\sum_{\text{fixed fibres}}\text{local index}.    \tag{7}
\]

Consequently one cannot obtain \(H^1\) by declaring the positive local
pages in (6) to be an orthogonal direct sum.  Doing so reverses the
geometric direction and reproduces the relative-trace obstruction of
106.152.

The required construction is instead a global chain complex

\[
 \mathcal C^0\xrightarrow d\mathcal C^1
 \xrightarrow d\mathcal C^2                         \tag{8}
\]

with the following simultaneously verified properties:

1. the local Lefschetz indices of its scaling flow are the Tate midpoint
   terms of 106.159 and the spin trace (3);
2. its trivial cohomology is the polar plane (4);
3. its distributional degree one is the CCM cyclic cokernel;
4. its Hodge star is positive on \(H^1\) and has the exact weight-one
   covariance.

Items 1 and 2 are now explicit.  CCM supplies item 3 as a cyclic cokernel.
The relative Fourier--Weyl cone of 106.156 supplies the chain-level star
for item 4.  The unresolved theorem is that the geometric localization
map from (8) to the Tate and spin pages is a quasi-isomorphism in the
nuclear resonant category and that its star is nondegenerate there.

## 5. The exact remaining comparison map

Let \(\mathfrak C_{\rm CCM}\) be the relative cyclic cone of 106.158 and
let

\[
 \mathfrak C_{\rm loc}
 =\mathfrak C_\Gamma
  \widehat\oplus
  \bigwidehat\oplus_p\mathfrak C_{E_p}             \tag{9}
\]

denote the nuclear restricted sum of the spin and Tate local complexes.
This raw sum is **not** the desired polarized target.  The local terms are
Lefschetz indices and their signs are fixed by cohomological degree; taking
the positive local norms in direct sum would reverse the trace formula.

The common rooted-divisor phase boundary must first be imposed by a gluing
map

\[
 \partial_{\rm gl}:\mathfrak C_{\rm loc}\longrightarrow
 \mathfrak C_{\rm bd},                              \tag{10}
\]

and the actual target is the mapping fibre

\[
 \mathfrak C_{\rm glue}
 :=\operatorname {Fib}(\partial_{\rm gl}).          \tag{11}
\]

Restriction to the fixed fibres is expected to define, only after this
boundary map is constructed, a localization morphism

\[
 \operatorname {Loc}:\mathfrak C_{\rm CCM}
 \longrightarrow\mathfrak C_{\rm glue}.             \tag{12}
\]

The sought polarization theorem has now the concrete form

\[
 \boxed{
 \begin{aligned}
 &H^1(\operatorname {Loc})\text{ is injective},\\
 &\Omega_{\rm CCM}(c,\star_{\rm ar}c)
   =\|H^1(\operatorname {Loc})[c]\|^2_{\rm glue}.
 \end{aligned}}                                    \tag{13}
\]

The first line is faithful localization; the second is the arithmetic
Hodge-index identity.  Both must be proved before completion.  Their local
coefficients are no longer unknown: Theorems 2.1 and 3.1 of 106.159 give
them exactly.  What is not yet defined is the boundary differential
\(\partial_{\rm gl}\); writing a direct-sum norm in its place would simply
assume the missing sign.

## 6. Status

Proved without zero input:

* a positive trace-class realization of the complete Gamma density;
* the exact \(H^0/H^2\) polar plane;
* the fully graded operator identity (6);
* separation of local fixed-point data from global degree-one states;
* the precise glued localization/Hodge comparison (13) still required.

Not proved:

* construction of \(\partial_{\rm gl}\) and the two assertions in (13).
