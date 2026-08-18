# 106.168 — The primitive determinant connection and its interior residues

## 1. Purpose

Document 106.167 shows that every repeated prime winding belongs to a
nonvanishing Hilbert--Schmidt determinant on
\(\operatorname {Re}s>1/2\).  Only the primitive trace
\(P(s)=\sum_p p^{-s}\) remains.  A scalar finite part of \(P\) has branch
ambiguities, so it is not the correct invariant.  Its derivative is a
canonical meromorphic connection one-form.

This note constructs that connection from the prime operator and proves
an exact residue theorem.  The pole at \(s=1\) is removed by the generic
orbit.  Every remaining interior residue is a nontrivial zeta zero, with
its multiplicity.  Thus the missing relative polarization is precisely a
source-side theorem which pushes the curvature/residue current of this
connection to the critical boundary.

## 2. The regular determinant channel

Retain the notation

\[
 H(s)=\sum_p\sum_{k\ge2}\frac{p^{-ks}}k,
 \qquad \operatorname {Re}s>\frac12.                         \tag{1}
\]

By 106.167, \(H\) is holomorphic in this half-plane and

\[
 \det{}_2(I-D_s)=e^{-H(s)}.                                  \tag{2}
\]

In \(\operatorname {Re}s>1\),

\[
 \log\zeta(s)=P(s)+H(s).                                     \tag{3}
\]

Differentiating removes every logarithmic branch:

\[
 P'(s)=\frac{\zeta'(s)}{\zeta(s)}-H'(s).                     \tag{4}
\]

Equation (4), initially obtained in the Euler half-plane, defines the
unique meromorphic continuation of the primitive derivative wherever
\(\zeta\) is meromorphic.

## 3. Generic-orbit renormalization

The pole of \(\zeta\) at \(s=1\) has residue one, so

\[
 \frac{\zeta'(s)}{\zeta(s)}
 =-\frac1{s-1}+O(1).                                         \tag{5}
\]

Define the primitive relative connection

\[
 \boxed{
 \nabla_{\rm pr}
 =d+\omega_{\rm pr},
 \qquad
 \omega_{\rm pr}(s)
 =\left(
 \frac{\zeta'(s)}{\zeta(s)}
 +\frac1{s-1}
 -H'(s)
 \right)ds.}                                                 \tag{6}
\]

The term \(ds/(s-1)\) is the differential form of the generic-orbit
subtraction.  Unlike a choice of \(\log(s-1)\), it is single valued.
The higher-winding correction \(-H'(s)ds\) is the logarithmic derivative
of the nonvanishing determinant (2).

### Theorem 3.1 — Exact interior residue law

The form \(\omega_{\rm pr}\) is regular at \(s=1\).  At every nontrivial
zero \(\rho\) of multiplicity \(m_\rho\),

\[
 \boxed{\operatorname {Res}_{s=\rho}\omega_{\rm pr}=m_\rho.} \tag{7}
\]

There are no other singularities of \(\omega_{\rm pr}\) in
\(\operatorname {Re}s>1/2\).

#### Proof

Regularity at \(s=1\) follows from (5) and the holomorphy of \(H\) there.
If

\[
 \zeta(s)=(s-\rho)^{m_\rho}a(s),
 \qquad a(\rho)\ne0,
\]

then

\[
 \frac{\zeta'(s)}{\zeta(s)}
 =\frac{m_\rho}{s-\rho}+\frac{a'(s)}{a(s)}.
\]

Both \(ds/(s-1)\) and \(H'(s)ds\) are holomorphic at a nontrivial zero,
which proves (7).  In the indicated half-plane the only singularities of
\(\zeta'/\zeta\), apart from \(s=1\), are its nontrivial zeros. \(\square\)

Thus the primitive connection is constructed without choosing a branch
of the prime logarithm and without naming any zero.

## 4. A contour formulation independent of zero labels

Let \(\Gamma\) be a positively oriented rectifiable Jordan curve contained
in \(\operatorname {Re}s>1/2\), avoiding \(s=1\) and the zero divisor.
Then

\[
 \boxed{
 \frac1{2\pi i}\int_\Gamma\omega_{\rm pr}
 =N_\zeta(\operatorname {int}\Gamma),}                       \tag{8}
\]

where the right side is the number of nontrivial zeros inside \(\Gamma\),
counted with multiplicity.

#### Proof

The term \(H'(s)ds\) has zero integral because \(H\) is single-valued and
holomorphic.  If \(\Gamma\) encloses \(s=1\), the residue \(-1\) of
\((\zeta'/\zeta)ds\) is cancelled exactly by the residue \(+1\) of
\(ds/(s-1)\); if it does not, neither contributes.  The remaining
residues are precisely the zero multiplicities. \(\square\)

Equation (8) is the intersection number of the primitive determinant line
with the analytic divisor in the right critical half-strip.  It is
defined entirely by the connection; no spectral enumeration is involved.

## 5. Exact equivalence of the missing descent

Let

\[
 \mathbb H_{1/2}=\{s\in\mathbb C:\operatorname {Re}s>1/2\}.
\]

### Theorem 5.1 — Flat interior connection criterion

The following are equivalent:

1. \(\omega_{\rm pr}\) is holomorphic on \(\mathbb H_{1/2}\);
2. every contour integral in (8) vanishes;
3. \(\zeta\) has no nontrivial zero in \(\mathbb H_{1/2}\);
4. every nontrivial zero of \(\zeta\) lies on
   \(\operatorname {Re}s=1/2\).

#### Proof

The equivalence of (1)--(3) follows from Theorem 3.1 and the residue
theorem.  If (3) holds, functional-equation symmetry sends every zero
\(\rho\) to \(1-\bar\rho\).  A zero with real part less than \(1/2\)
would therefore produce one with real part greater than \(1/2\).
Hence all zeros lie on the line.  The reverse implication is immediate.
\(\square\)

This theorem is a completion audit, not a proof of item 1.  It prevents a
finite-part prescription from silently assuming the desired zero-free
domain.

## 6. Polarization interpretation

The data constructed so far now have a precise geometric arrangement:

* \(\det_2(I-D_s)\) is the nonvanishing determinant of the polarized
  repeated-winding sector;
* \(ds/(s-1)\) is the generic-orbit counterconnection;
* the archimedean Gamma and polar pages provide the real structure and
  functional-equation gluing;
* \(\omega_{\rm pr}\) is the remaining primitive determinant connection;
* its interior residue current is the obstruction to faithful positive
  descent.

On a complex curve, a Hermitian determinant line has a Chern connection,
and a section contributes its zero divisor through the
Poincaré--Lelong formula.  In the present relative problem, the desired
arithmetic Hodge theorem must do more than provide a positive metric: it
must prove that the divisor current of \(\nabla_{\rm pr}\) is supported on
the real fixed boundary \(\operatorname {Re}s=1/2\).  A positive metric
on an arbitrary determinant line would not imply this support theorem.

Equivalently, the missing map from the rooted prime module to the CCM
Rosati degree one must identify the interior current in (8) with the
zero class of the relative pair.  Theorem 5.1 shows that this
identification is exactly the faithful-descent clause; it cannot be
replaced by a branch choice for \(P(s)\).

## 7. Status

Proved:

* the canonical single-valued primitive determinant connection;
* exact cancellation of the generic pole;
* the residue and contour laws;
* identification of every possible interior obstruction;
* the precise support theorem required of the global polarization.

Still required:

* a source-side arithmetic intersection identity forcing the residue
  current (8) to have no support in
  \(\operatorname {Re}s>1/2\).
