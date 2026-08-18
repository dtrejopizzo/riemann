# 106.183 — White-light singular trace and finite-part invisibility

## 1. Purpose

Documents 106.179--106.181 identify the arithmetically selected Julia
branch and cancel its full-rank white-light divergence against the
Gamma--polar boundary with one matched cutoff.  This raises a natural
question: can a Dixmier trace, a residue trace, or another singular trace
turn the white-light coefficient into the missing positive polarization?

The answer is no.  A singular trace detects the leading divergent
coefficient and is insensitive to the finite correction.  In the present
construction the leading coefficient is the universal Hilbert norm,
whereas the finite correction is exactly the joined Rosati form.  Thus a
singular trace recovers the already known positive ambient metric and
deletes the arithmetic intersection term whose sign is at issue.

This note proves that statement abstractly and applies it to the matched
CCM cutoff.  It does not alter the global polarization target; it removes
one possible source for its positivity.

## 2. The cutoff asymptotic

Let \(V\) be the nuclear test core and let \(C_X\to\infty\) denote the
common white-light mass.  Before the two parity sectors are joined, their
quadratic cutoff forms have the shape

\[
 Q_X^{\rm odd}(f,g)
   ={C_X\over2}\langle f,g\rangle+B_X^{\rm odd}(f,g),
 \qquad
 Q_X^{\rm even}(f,g)
   =-{C_X\over2}\langle f,g\rangle+B_X^{\rm even}(f,g).       \tag{1}
\]

The matched-cutoff identity of 106.181 states that the divergent terms
cancel before a limit is taken and

\[
 B_X^{\rm odd}(f,g)+B_X^{\rm even}(f,g)
   \longrightarrow \mathfrak h_{\rm Ros}([f],[g]).           \tag{2}
\]

For compact logarithmic support, (2) actually stabilizes once \(X\) has
passed the support.  The two coefficients in (1) therefore have distinct
roles:

* \(C_X\langle f,g\rangle/2\) is the universal white-light coefficient;
* the order-one term in the *joined* expression is the arithmetic
  intersection form.

## 3. Normalized singular limits

Fix any positive normalization \(a_X\to\infty\) with
\(C_X/a_X\to c\in(0,\infty)\), and let \(\mathrm{Lim}_\omega\) be
any generalized limit extending the ordinary limit on convergent bounded
sequences.  Define

\[
 \mathcal T_\omega(Q(f,g))
 =\mathrm{Lim}_\omega {Q_X(f,g)\over a_X}.             \tag{3}
\]

### Theorem 3.1 — The finite part is invisible

If

\[
 Q_X(f,g)=C_X a(f,g)+b(f,g)+o(1),                            \tag{4}
\]

then

\[
 \boxed{\mathcal T_\omega(Q(f,g))=c\,a(f,g).}               \tag{5}
\]

In particular, \(\mathcal T_\omega\) is independent of \(b\).

#### Proof

Divide (4) by \(a_X\).  Since \(C_X/a_X\to c\),
\(b(f,g)/a_X\to0\), and \(o(1)/a_X\to0\), the sequence converges to
\(c,a(f,g)\).  A generalized limit agrees with an ordinary limit on a
convergent sequence, proving (5). \(\square\)

For the odd sector of (1), Theorem 3.1 gives

\[
 \mathcal T_\omega(Q^{\rm odd}(f,g))
 ={c\over2}\langle f,g\rangle,                              \tag{6}
\]

and for the even sector it gives the negative of (6).  Applied after the
matched cancellation, the same normalization gives zero because the
joined form is order one.  Hence neither order of application returns
\(\mathfrak h_{\rm Ros}\): separately it returns the universal norm,
and jointly it annihilates the finite arithmetic form.

## 4. Operator-ideal formulation

The same conclusion is the defining invariance of singular traces.  Let
\(K\ge0\) be a measurable operator in \(\mathcal L^{1,\infty}\), let
\(R\in\mathcal L^1\), and let \(\mathrm{Tr}_\omega\) be a Dixmier
trace.  Then

\[
 \mathrm{Tr}_\omega(aK+R)
 =a\mathrm{Tr}_\omega(K),                             \tag{7}
\]

because every singular trace vanishes on \(\mathcal L^1\).  Thus, even if
the finite return construction is represented by operators

\[
 Q_f=a_fK+R_f,                                               \tag{8}
\]

the singular trace sees \(a_f\), not the ordinary trace or finite part of
\(R_f\).  In the CCM application \(a_f\) is proportional to
\(\|f\|^2\); the arithmetic dependence lies in the compensated remainder.

Equation (7) also explains why the earlier Phase-15 Dixmier-trace proposal
could not supply a prime-localized metric.  The present matched cutoff
repairs the definition of the finite part, but it does not change which
coefficient a singular trace measures.

## 5. Residue traces and zeta regularization

Suppose a regularized trace has a Laurent expansion

\[
 Z_f(s)={a(f)\over s-s_0}+b(f)+O(s-s_0).                    \tag{9}
\]

Then

\[
 \mathop{\mathrm{Res}}_{s=s_0} Z_f(s)=a(f),                  \tag{10}
\]

while the desired arithmetic correction is the constant term
\(b(f)=\mathrm{FP}_{s=s_0}Z_f(s)\).  Positivity of the residue
places no sign constraint on the finite part.  Indeed, for every real
number \(r\),

\[
 Z_r(s)={1\over s-s_0}+r                                   \tag{11}
\]

has the same positive residue and arbitrary finite part.  A derivative,
counterterm, or Hadamard finite part can extract \(r\), but that extraction
is no longer a positive trace.  It is precisely a renormalization rule.

The matched CCM construction already provides the canonical rule: join
the prime and Gamma--polar sectors before the cutoff is removed.  A
residue trace cannot add a sign theorem to that rule.

## 6. Scale anomaly

Let the scale flow translate the cutoff by a bounded amount,
\(C_X\mapsto C_X+\alpha(t)\).  The separate sectors of (1) acquire the
opposite anomalies

\[
 \mathcal A_{\rm odd}(t;f,g)
   =+{\alpha(t)\over2}\langle f,g\rangle,
 \qquad
 \mathcal A_{\rm even}(t;f,g)
   =-{\alpha(t)\over2}\langle f,g\rangle.                   \tag{12}
\]

Therefore

\[
 \boxed{\mathcal A_{\rm odd}+\mathcal A_{\rm even}=0}       \tag{13}
\]

for the matched cutoff.  This proves anomaly cancellation of the joined
form.  It does **not** select the sign of its finite part: adding a scalar
weight-one form after the cancellation preserves (13).  In the actual
CCM construction that scalar freedom is removed not by covariance alone
but by the literal distributional identity of 106.181.  After that
identity there is a unique finite form, but its Hodge-index sign remains
to be proved.

## 7. Consequence for the polarization program

The following parts of the construction are now separate and unambiguous.

1. The finite Julia colligation and the Green identity select the singular
   negative graph \(K_-\).
2. The Dirichlet weight converts its inverse defect into
   \(C_XI-A_X\).
3. The common cutoff cancels the two white-light anomalies exactly.
4. The stabilized finite part descends to the CCM quotient and equals
   \(\mathfrak h_{\rm Ros}\).
5. A singular trace sees only item 1's universal leading norm and cannot
   prove the sign of item 4.

Consequently the source-defined map required by 106.182 cannot be obtained
by applying a Dixmier, Wodzicki, residue, or normalized generalized trace
to the white-light divergence.  It must act on the *finite relative
intersection class itself* and satisfy

\[
 \mathfrak h_{\rm Ros}(u,v)=\langle Du,Dv\rangle             \tag{14}
\]

for a target norm defined independently of the left-hand side.

## 8. Status

Proved:

* the singular-trace finite-part invisibility theorem;
* its operator-ideal and residue-trace forms;
* cancellation of the two scale anomalies under the matched cutoff;
* impossibility of obtaining the Rosati sign from the white-light residue.

Still required:

* an arithmetic relative intersection map on the already descended CCM
  degree one, or a direct arithmetic Hodge-index theorem for its Rosati
  form.
