# P122 -- the Bohr determinant cocycle splits by prime

## Status

`IMPORTED COCYCLE + PROVED SPECIALIZATION/NO-GO`.  The flow cocycle and
semifinite index framework are standard; the primewise splitting and zero
Euler-index calculation for this carrier are proved here.  The semifinite Bohr
carrier of P122.016 retains all cross-prime products in its algebra, but its
canonical determinant two-cocycle is diagonal in torus characters.  On the
Euler logarithms it is the sum of the local analytic Hardy determinant cocycles and
creates no nondecomposable Gamma--prime or cross-prime equality law.

Thus the crossed-product topology is correct finite-place infrastructure,
not the missing global theorem.

## 1. The canonical flow cocycle

For a finite active set `S`, retain

\[
 X_S=\mathbb T^S,qquad
 \delta_S(z^n)=i\omega_nz^n,qquad
 \omega_n=\sum_{p\in S}n_p\log p.                 \tag{1.1}
\]

On smooth zero-mean functions define

\[
 \Omega_S(f,g)={1\over i}
   \int_{X_S} f\,\delta_Sg\,dm_S.                 \tag{1.2}
\]

Haar invariance gives integration by parts

\[
 \Omega_S(f,g)=-\Omega_S(g,f),                    \tag{1.3}
\]

up to the usual bilinear rather than sesquilinear convention.  This is the
Lie-algebra cocycle obtained from the semifinite Hardy polarization; its
Fourier expression is

\[
 \boxed{
 \Omega_S(f,g)=
   \sum_{n\in\mathbb Z^S}\omega_n f_{-n}g_n.}      \tag{1.4}
\]

The convergence is absolute for the analytic Euler logarithms below.

## 2. Exact cross-prime vanishing

### Theorem 2.1

Suppose `f_p` is a zero-mean function of coordinate `z_p` alone and `g_q`
is a zero-mean function of `z_q` alone.  If `p ne q`, then

\[
                         \Omega_S(f_p,g_q)=0.       \tag{2.1}
\]

#### Proof

The derivative `delta_S g_q` still depends only on `z_q` and has zero Haar
mean.  Product Haar measure gives

\[
 \int_{X_S}f_p(z_p)\delta_Sg_q(z_q)dm_S
 =\left(\int_{\mathbb T}f_pdm_p\right)
  \left(\int_{\mathbb T}\delta_Sg_qdm_q\right)=0.
\]

Equivalently, the Fourier supports lie on two distinct coordinate axes and
no nonzero indices in (1.4) can sum to zero.  QED.

The result is not a statement that the algebra has no mixed products.
Products such as `f_p g_q` are present.  It states that the **canonical
central-extension trace** annihilates their off-diagonal bilinear pairing.

## 3. Evaluation on the Euler loop pair

Put

\[
 F^+=\sum_{p\in S}\log(1-r_pz_p),
 \qquad
 F^-=\sum_{p\in S}\log(1-r_pz_p^{-1}),
 \qquad r_p=p^{-1/2}.                              \tag{3.1}
\]

Theorem 2.1 gives

\[
 \Omega_S(F^+,F^-)
 =\sum_{p\in S}(\log p)
   \operatorname {Res}_{z_p=0}
   \bigl(\log(1-r_pz_p)d\log(1-r_pz_p^{-1})\bigr). \tag{3.2}
\]

Using the analytic determinant calculation of P122.015,

\[
 \boxed{
 \Omega_S(F^+,F^-)
 =\sum_{p\in S}(\log p)\log(1-p^{-1}).}           \tag{3.3}
\]

If coordinate grading rather than physical flow grading is used, the
factors `log p` are absent.  In either normalization, exponentiation
factorizes over primes.  There is no mixed `p,q` central commutator.

## 4. Consequence for a determinant trivialization

The algebra `C^infinity(X_S)` remembers a mixed monomial
`product p^(n_p)` before trace, but the standard determinant cocycle is
quadratic and character-diagonal.  Therefore its central line is, on the
Euler subgroup, canonically the tensor product of the local central lines.

This puts it under the exact warning of P122.014: its virtual curvature can
package the known sum of local forms, but its positivity or equality-state
flatness is not created by the central extension.

### 4.1 The primary semifinite index is zero

The standard odd index pairing for an invariant real flow is the
semifinite spectral flow of `D` to `u^*Du`; in the one-dimensional smooth
case its local formula is proportional to

\[
                         \tau_S(u^*\delta_Su).      \tag{4.1}
\]

This is the setting of Carey--Phillips--Rennie--Sukochev,
[The local index formula in semifinite von Neumann algebras I](https://arxiv.org/abs/math/0411019).
For one relative Euler scattering factor,

\[
 {1\over i}c_p^{-1}\delta_Sc_p
 = (\log p)(P_p-1).                                \tag{4.2}
\]

The Poisson kernel has Haar mean one.  Hence

\[
 \tau_S(c_p^{-1}\delta_Sc_p)=0,                    \tag{4.3}
\]

and additivity gives zero for the finite product `c_S`.  Equivalently, each
relative factor has winding number zero.  Therefore the primary K-theory
index/spectral flow of the Euler unitary is trivial.

The nonzero analytic determinant pairing of P122.015 is a secondary
polarization invariant, not this primary index.  A proof of row (d) cannot
come from merely computing the K1 pairing of `c_S`: that computation is
identically zero before any first-contact condition is imposed.

The Gamma multiplier cannot secretly supply the missing cross term inside
(1.2), because

\[
 b_\infty(\tau)=\pi^{-i\tau}
 {\Gamma(1/4+i\tau/2)\over\Gamma(1/4-i\tau/2)}
\]

is not an element of the Bohr algebra.  The mixed expression
`Omega_S(log b_infty,F^+)` is simply undefined in this cocycle domain.
Assigning it a regularized value without first constructing an enlarged
cycle and proving its trace property would insert the desired anomaly by
hand.

## 5. Exact surviving construction problem

P122.016 supplies the finite Euler determinant class, and P122.017 proves
that its native central extension remains placewise additive.  The missing
object is consequently not a different cocycle on the same Bohr algebra.
It must be a correspondence

\[
 \mathcal E_{\infty,S}:
 (C^\infty(X_S)\rtimes\mathbb R,\tau_S)
 \longrightarrow \mathcal C_{\Gamma,T}             \tag{5.1}
\]

with a **relative** cyclic cocycle whose domain contains both the Bohr Euler
logarithms and the quarter-Gamma scattering.  It must prove:

1. trace/cocycle identities before scalar evaluation;
2. exact cancellation of every regulator-dependent boundary term;
3. compatibility with the two Tate constraints;
4. an equality-state anomaly formula whose positive local term is the
   P122.013 rank-one curvature.

The common causal half-line/slit-disk carrier of phase 120 is the only
existing object containing both families of traces.  Endowing it with the
relative cocycle in (5.1), rather than altering the Bohr cocycle, is the
next live construction task.
