# 104_40 — Canonical Euler variational resolvent and the critical-modulus gate

**Status.** The fixed ray \(g_n\) was attacked, not the norm of the flag
operator, with the canonical prime–pole factorization of 104_36. For every
safe regularization \(a>2\), the simple-prime functional is a signed
spectral average of

\[
 M(s)={1\over s-1}-\sum_p{\log p\over p^s}.
\]

The most general positive resolvent commuting with translations was
allowed, that is, an arbitrary positive Fourier multiplier. The
variational optimization can be done exactly. Its best lower bound
replaces \(\Re M\) with \(-|M|\). Approaching \(a=1\), that bound diverges
like \(-\log(1/(a-1))\) at any non-resonant critical zero, even though the
renormalized prime–pole moment has a finite limit. Off-line zeros instead
cause a pole crossing and the exponential residue of 104_36 first.

Hence every proof of the proportional margin via a **positive, quadratic,
translation-invariant** resolvent applied to the Euler discrepancy vector
is ruled out. This is broader than using the unweighted norm of 104_36.
Neither a non-commutative resolvent adapted to the degree, nor a signed
identity preserving the phase of \(M\), is ruled out. This document proves
neither A1 nor RH.

## 1. Pre-registration and falsifier

The target remains

\[
 \lambda_n\ge {501\over2002}A_n,
 \qquad n\ge150,                                      \tag{1}
\]

or, after 104_32, the corresponding lower bound for
\(B_{n}^{(p+\mathrm{pole})}\), leaving the correction
\(P_{n-1}^{(\ge2)}(1)\) explicit.

The only ansatz of this attack is the following: start from

\[
 B_{n,a}^{(p+\mathrm{pole})}=\langle V_{n,a},g_n\rangle,
                                                               \tag{2}
\]

with all the simple primes and the pole already coupled inside
\(V_{n,a}\), and insert between the two factors a positive operator
\(R_a\) commuting with the translation semigroup. No prime-by-prime
absolute value is taken.

The mandatory falsifier is

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5}.             \tag{3}
\]

It has \(\Re\rho=4/5\). As \(a\) decreases, the Laplace transform's pole
crosses the Hardy boundary at \(a=2\Re\rho=8/5\), and at \(a=1\) it sits
at \(\Re z=3/10>0\). For \(n=152\), its residual multiplier is

\[
 1-\left(1-{1\over\rho}\right)^{152}=1-2^{-152}>0.           \tag{4}
\]

So the ansatz does not certify the off-line divisor: the required
deformation hits a pole and must add its residue. The checker reproduces
(3)–(4) with Gaussian rationals.

## 2. Exact scalar identity in the Euler half-plane

We use the normalization of 104_36:

\[
 g_n(x)=e^{-x/2}L_{n-1}^{(1)}(x),
 \qquad
 \widehat g_n(t)
 =1-\left({-1/2+it\over1/2+it}\right)^n.                    \tag{5}
\]

Let

\[
 Q(s)=\sum_p{\log p\over p^s},
 \qquad M(s)={1\over s-1}-Q(s).                              \tag{6}
\]

For \(a>2\), the Euler integrations converge absolutely, and
104_36, (13), gives

\[
 \widehat V_{n,a}(t)
 =a\widehat g_n(t)M\!\left(a(1/2+it)\right).                 \tag{7}
\]

Plancherel preserves the complete phase of the prime–pole difference:

\[
 \boxed{
 B_{n,a}^{(p+\mathrm{pole})}
 ={a\over2\pi}\int_{\mathbb R}|\widehat g_n(t)|^2
 \Re M\!\left(a(1/2+it)\right)\,dt.}                         \tag{8}
\]

Convergence of (8) is absolute for \(a>2\). In particular, (8) is already
an estimate on the **fixed vector** \(g_n\); the spectral supremum of
104_30 does not appear.

## 3. Optimization over all positive commutative resolvents

A positive translation-invariant operator is, in the Fourier
representation, multiplication by a measurable function \(r(t)>0\). The
pointwise Young inequality, applied to \(z=aM(a(1/2+it))\), is

\[
 2\Re z\ge-r|z|^2-r^{-1}.                                  \tag{9}
\]

By (8),

\[
 B_{n,a}^{(p+\mathrm{pole})}\ge-\mathcal C_{n,a}[r],         \tag{10}
\]

\[
 \mathcal C_{n,a}[r]
 ={1\over4\pi}\int_{\mathbb R}|\widehat g_n(t)|^2
 \left\{a^2r(t)|M(a(1/2+it))|^2+r(t)^{-1}\right\}\,dt.       \tag{11}
\]

No interaction was lost before (11): the modulus contains the complete
difference \(1/(s-1)-Q(s)\), and squaring it brings in every prime–prime
and prime–pole cross term.

The variation in \(r\) is pointwise and exact. For \(M\ne0\), the minimum
is attained at \(r=(a|M|)^{-1}\); at a zero it is obtained by limit.
Hence

\[
 \boxed{
 \inf_{r>0}\mathcal C_{n,a}[r]
 =\mathcal J_{n,a}
 :={a\over2\pi}\int_{\mathbb R}|\widehat g_n(t)|^2
 |M(a(1/2+it))|\,dt.}                                      \tag{12}
\]

Equation (12) is an optimality theorem for this entire class of
resolvents. A more elaborate positive multiplier does not recover the
phase: its best result is exactly

\[
 B_{n,a}^{(p+\mathrm{pole})}\ge-\mathcal J_{n,a}.             \tag{13}
\]

## 4. The best cost already diverges from the critical zeros

The meromorphic continuation used in 104_36 is

\[
 Q(s)=\sum_{k\ge1}\mu(k)\left(-{\zeta'\over\zeta}(ks)\right).
                                                               \tag{14}
\]

If \(\rho=1/2+i\gamma\) is a critical zero of multiplicity \(m_\rho\),
then, in a disc with no other singularities,

\[
 M(s)={m_\rho\over s-\rho}+H_\rho(s),                        \tag{15}
\]

with \(H_\rho\) holomorphic. On \(s=a(1/2+it)\), setting

\[
 \delta={a-1\over2},\qquad t_\rho(a)={\gamma\over a},        \tag{16}
\]

one has

\[
 s-\rho=\delta+ia\{t-t_\rho(a)\}.                           \tag{17}
\]

For each \(n\) there is a critical zero with
\(\widehat g_n(\gamma)\ne0\). Indeed, by Hardy's unconditional theorem
there are infinitely many distinct zeros on the critical line, while

\[
 \widehat g_n(t)=0
 \iff
 \left({-1/2+it\over1/2+it}\right)^n=1                     \tag{18}
\]

admits only a finite set of real ordinates.

Fix one such zero. By continuity of \(\widehat g_n\), and making the
interval in (15) sufficiently small, there exist constants
\(c_{n,\rho}>0\), \(r_\rho>0\), and \(a_0>1\) such that

\[
 \mathcal J_{n,a}
 \ge c_{n,\rho}
 \int_{-r_\rho}^{r_\rho}
 {du\over\sqrt{\delta^2+a^2u^2}}
 \ge c_{n,\rho}\log{1\over a-1}                    \tag{19}
\]

for \(1<a<a_0\), avoiding the isolated values where the line passes
through another singularity. In particular,

\[
 \boxed{\mathcal J_{n,a}\longrightarrow+\infty
 \quad(a\downarrow1).}                                      \tag{20}
\]

This result is unconditional: it uses only the existence of infinitely
many critical zeros, not RH. The divergence is logarithmic, against the
\((a-1)^{-1}\) divergence of the squared norm of 104_36; optimizing the
resolvent improves the exponent, but leaves no finite limit.

By contrast, the scalar Abel prime–pole combination has the finite limit
defined in 104_32. So the divergence of (20) is created exactly by
replacing the phase of \(M\) with its modulus. The higher-power
correction, bounded by \(14n+1\), cannot cancel a divergence in \(a\) for
fixed \(n\), and \(A_n\) does not depend on \(a\) either.

## 5. What happens with an off-line zero

If \(\Re\rho>1/2\), the pole of (15) crosses the line
\(\Re s=a/2\) at \(a=2\Re\rho\). The Euler identity (8), initially proved
for \(a>2\), cannot be deformed down to \(a=1\) without picking up that
residue. In the Laplace coordinate of 104_36, the pole is at

\[
 z_{\rho,a}={\rho\over a}-{1\over2},                           \tag{21}
\]

and its multiplier is

\[
 m_\rho\left[1-\left(1-{a\over\rho}\right)^n\right].         \tag{22}
\]

Equations (21)–(22) are precisely the datum that makes falsifier (3)
fail. So the stop-gate has both correct branches:

* an off-line zero prevents the deformation from proceeding with no
  residues;
* even absent that crossing, critical zeros make the best quadratic
  modulus bound diverge.

## 6. Decision

The following no-go is proved, with full quantifiers:

> **Theorem (commutative variational gate).** Among every Young
> factorization obtained by inserting a positive operator commuting with
> translations in the prime–pole identity (2), the optimal lower bound is
> (13). Its cost diverges upon removing the regulator, by (20). If an
> attempt is made to deform across an off-line zero, residue (22) appears
> first. Hence no proof of (1) can emerge from this class of resolvents.

The result does not rule out:

1. a non-translation-invariant resolvent essentially using the degree
   \(n\) and preserving a signed phase;
2. an arithmetic identity that cancels the residues with another channel
   before applying a positive form;
3. the adjacent Schur criterion \(\mathcal T_n\ge0\) of 104_34.

It does rule out replacing the norm of 104_36 with a positive spectral
weight or with a Fourier preconditioner: after optimizing all of them, the
same phase loss reappears as \(|M|\).

## 7. Reproducible verification

Run

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 canonical_euler_resolvent_gate_check.py

The program uses Fraction for (3)–(4), the Young minimization identity on
a rational grid, and a rational model critical pole
\(\rho=1/2+i\), for which
\(1-1/\rho=(3+4i)/5\) is not a root of unity. The table of
\(2\mathrm{arsinh}(1/\delta)\) only illustrates the logarithmic law of
(19); the mathematical decision is the proof above, not the decimal table.
</content>
