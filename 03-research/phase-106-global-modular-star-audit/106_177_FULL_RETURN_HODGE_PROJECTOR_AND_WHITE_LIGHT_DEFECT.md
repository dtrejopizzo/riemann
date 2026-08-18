# 106.177 — Full-return Hodge projector and the white-light defect

## 1. Purpose

The middle projector of 106.169 uses the first primitive Euler layer

\[
 \sum_p\frac{\log p}{p}.
\]

The local Green identity of 106.176 has a different scalar mass.  At a
finite prime it contains every nonzero valuation shell and therefore

\[
 c_p=\log p\sum_{k\ne0}p^{-|k|/2}
     =\frac{2\log p}{\sqrt p-1}.                         \tag{1}
\]

Consequently the first-layer projector cannot be inserted into the full
Green identity.  This note constructs the operator-valued Hodge projector
for all return shells at once.  Its range is positive and its norm admits
an exact formula.  The formula also isolates the remaining cofinal defect:
after the complete generic Hodge plane is removed, a full-rank
white-light term remains and must be cancelled jointly with the polar and
archimedean boundary pages.

No zero of zeta and no sign of the Weil form is used.

## 2. A finite weighted return system

Let \(H\) be a complex Hilbert space, viewed as a real Hilbert space with
complex structure \(J_Hf=if\).  Let \(I\) be finite, let \(w_i>0\), and
let \(U_i\) be unitary operators on \(H\).  Put

\[
 C_I=\sum_{i\in I}w_i,
 \qquad
 A_I=\sum_{i\in I}w_iU_i.                                \tag{2}
\]

On

\[
 \mathscr W_I=\bigoplus_{i\in I}(H\oplus H)               \tag{3}
\]

use the ordinary direct-sum metric and the complex structure

\[
 \mathcal J_I(x_i,y_i)_{i\in I}=(-y_i,x_i)_{i\in I}.      \tag{4}
\]

Define the complete generic Hodge plane by

\[
 \Gamma_I(z_0,z_1)
   =\bigl(\sqrt{w_i}z_0,\sqrt{w_i}z_1\bigr)_{i\in I}.      \tag{5}
\]

It is closed, invariant under \(\mathcal J_I\), and

\[
 \|\Gamma_I(z_0,z_1)\|^2
 =C_I(\|z_0\|^2+\|z_1\|^2).                              \tag{6}
\]

The full-return middle space is

\[
 \mathscr W_I^{\rm mid}
 =\mathrm{Ran}(\Gamma_I)^\perp
 =\left\{(x_i,y_i):
   \sum_i\sqrt{w_i}x_i=0,
   \ \sum_i\sqrt{w_i}y_i=0\right\}.                     \tag{7}
\]

### Theorem 2.1 — Exact operator-valued middle projector

The orthogonal projector \(P_I^{\rm mid}\) onto (7) is

\[
 \boxed{
 P_I^{\rm mid}(x_i,y_i)
 =\bigl(x_i-\sqrt{w_i}\bar x,
         y_i-\sqrt{w_i}\bar y\bigr)_{i\in I},}            \tag{8}
\]

where

\[
 \bar x=C_I^{-1}\sum_i\sqrt{w_i}x_i,
 \qquad
 \bar y=C_I^{-1}\sum_i\sqrt{w_i}y_i.                     \tag{9}
\]

Moreover \(P_I^{\rm mid}\mathcal J_I=\mathcal J_IP_I^{\rm mid}\).

#### Proof

The adjoint of (5) is

\[
 \Gamma_I^*(x_i,y_i)
 =\left(\sum_i\sqrt{w_i}x_i,
        \sum_i\sqrt{w_i}y_i\right),                       \tag{10}
\]

and \(\Gamma_I^*\Gamma_I=C_I I_{H\oplus H}\).  Hence

\[
 P_I^{\rm mid}
 =I-\Gamma_I(C_I I)^{-1}\Gamma_I^*,                       \tag{11}
\]

which is (8).  Equations (4)--(5) show that the generic plane is
\(\mathcal J_I\)-invariant; therefore its orthogonal projector commutes
with \(\mathcal J_I\). \(\square\)

## 3. The two-endpoint feature map

Define

\[
 \Psi_I f
 =\left(\sqrt{\frac{w_i}{2}}f,
         \sqrt{\frac{w_i}{2}}U_if\right)_{i\in I}.        \tag{12}
\]

The first coordinate is the common incoming endpoint and the second is
the transported endpoint.  Formula (12) retains their relative phases
before any square is taken.

### Theorem 3.1 — Full-return variance identity

For every \(f\in H\),

\[
 \boxed{
 \|P_I^{\rm mid}\Psi_If\|^2
 =\frac{C_I}{2}\|f\|^2
  -\frac{1}{2C_I}\|A_If\|^2.}                             \tag{13}
\]

If \(I\) is symmetric, in the sense that every \(U_i\) occurs with its
adjoint and the same weight, then \(A_I=A_I^*\).  For the associated
translation energy

\[
 \mathcal E_I(f)
 =C_I\|f\|^2-\langle f,A_If\rangle,                        \tag{14}
\]

one has the sharper exact identity

\[
 \boxed{
 \mathcal E_I(f)
 =\|P_I^{\rm mid}\Psi_If\|^2
  +\frac{1}{2C_I}\|(C_I I-A_I)f\|^2.}                    \tag{15}
\]

In particular,

\[
 \mathcal E_I(f)\ge
 \frac{1}{2C_I}\|(C_I I-A_I)f\|^2.                       \tag{16}
\]

#### Proof

Equations (9) and (12) give

\[
 \bar x=\frac{f}{\sqrt2},
 \qquad
 \bar y=\frac{A_If}{\sqrt2C_I}.                           \tag{17}
\]

The first coordinate of (8) therefore vanishes.  The second coordinate
is

\[
 \sqrt{\frac{w_i}{2}}
 \left(U_if-C_I^{-1}A_If\right).                           \tag{18}
\]

Expanding its squared norm and using \(U_i^*U_i=I\) proves (13).
When \(A_I=A_I^*\), expansion of the last square in (15) gives

\[
 \begin{aligned}
 &\frac{C_I}{2}\|f\|^2-rac{1}{2C_I}\|A_If\|^2
  +\frac{1}{2C_I}\|(C_II-A_I)f\|^2\\
 &=C_I\|f\|^2-\langle f,A_If\rangle,
 \end{aligned}                                             \tag{19}
\]

which is (14). \(\square\)

The two summands in (15) are respectively the Hodge-stable transverse
variance and the squared common-endpoint regression residual.  Thus the
complete local Dirichlet energy has now been factorized without throwing
away any return phase.

## 4. Specialization to the ordinary prime returns

For a finite prime set \(S\) and return cutoff \(K\), use

\[
 I_{S,K}=\{(p,k):p\in S,\ 0<|k|\le K\},
 \qquad
 w_{p,k}=(\log p)p^{-|k|/2},
 \qquad
 U_{p,k}=U_p^k.                                             \tag{20}
\]

Then

\[
 C_{S,K}
 =\sum_{p\in S}\log p\sum_{0<|k|\le K}p^{-|k|/2},        \tag{21}
\]

and

\[
 \mathcal E_{S,K}(f)
 =\frac12\sum_{p\in S}\log p
   \sum_{0<|k|\le K}p^{-|k|/2}
   \|(I-U_p^k)f\|^2.                                      \tag{22}
\]

Letting \(K\to\infty\) for fixed \(S\) is ordinary norm convergence,
because every shell series is geometric.  It gives

\[
 C_S=\sum_{p\in S}\frac{2\log p}{\sqrt p-1},             \tag{23}
\]

and (22) becomes exactly the finite-prime part of the local Green energy
in 106.176(14).  Thus (8) is the requested finite-cutoff
operator-valued projector with the correct complete scalar mass, not the
first primitive approximation.

The same construction applies to a finite quadrature of the positive
archimedean measure

\[
 4g_\Gamma(t)\,dt
 =\frac{4e^{-t/2}}{1-e^{-2t}}\,dt,                          \tag{24}
\]

and passes monotonically to its difference-form domain near \(t=0\).
The singular mass itself is not finite there; only the difference energy
is.  Therefore the archimedean endpoint belongs to the rigged boundary
space, not to the ordinary Hilbert direct sum.

## 5. Comparison with the compensated Green form

For a finite symmetric return system, write the Green form as

\[
 \mathfrak h_I(f)
 =\mathcal E_I(f)-C_I\|f\|^2+\mathcal P(f),                \tag{25}
\]

where \(\mathcal P\) denotes the two polar endpoint terms together with
the differential-idele normalization.  Combining (15) and (25) gives the
exact decomposition

\[
 \boxed{
 \mathfrak h_I(f)
 =\|P_I^{\rm mid}\Psi_If\|^2+\mathcal R_I(f),}             \tag{26}
\]

with

\[
 \boxed{
 \mathcal R_I(f)
 =\mathcal P(f)-C_I\|f\|^2
  +\frac{1}{2C_I}\|(C_II-A_I)f\|^2.}                      \tag{27}
\]

This is an equality, not an estimate.  It identifies precisely what the
full-return Hodge projector does and does not remove.

## 6. The white-light obstruction to an ordinary Hilbert limit

For ordinary primes, \(C_S\to\infty\) as \(S\) increases.  On a vector
whose correlations \(\langle f,U_p^kf\rangle\) decay along distinct
large translations, one has weakly

\[
 C_S^{-1}A_Sf\longrightarrow0.                              \tag{28}
\]

Equations (13) and (27) then contain opposite full-rank leading terms:

\[
 \|P_S^{\rm mid}\Psi_Sf\|^2
 =\frac{C_S}{2}\|f\|^2+o(C_S),
 \qquad
 \mathcal R_S(f)
 =-\frac{C_S}{2}\|f\|^2+\mathcal P(f)+o(C_S).             \tag{29}
\]

Their sum can have the finite CCM limit, but neither summand has an
ordinary positive Hilbert limit.  Thus the residual in (27) is not a
small endpoint error.  It is the second half of the generic white-light
sector.

This proves that equation 106.176(18), interpreted as convergence of the
raw norms \(\|P_S^{\rm mid}\Phi_Sf\|^2\), is too strong.  The correct
cofinal object must be a **relative superpolarization** in which the two
terms of (29) are paired before completion.  Subtracting the white-light
term after Hilbert completion is invalid, because its coefficient tends
to infinity and its finite tangent has no inherited sign.

## 7. Corrected global target

Let \(\mathscr W_S^{\rm odd}\) be the positive middle space of (7), and
let \(\mathscr G_S^{\rm even}\) be the generic/polar boundary module
carrying the form (27).  The finite compensated object is the graded pair

\[
 \mathbb H_S
 =\mathscr G_S^{\rm even}\ \widehat\oplus\
  \mathscr W_S^{\rm odd},                                  \tag{30}
\]

with supermetric

\[
 [\Phi_Sf,\Phi_Sg]_S
 =\langle P_S^{\rm mid}\Psi_Sf,
          P_S^{\rm mid}\Psi_Sg\rangle
  +\mathcal R_S(f,g).                                      \tag{31}
\]

By (26), (31) is exactly the finite compensated CCM Green form.  The
remaining polarization theorem is no longer the construction of the
prime-return projector: that projector is (8).  It is the following
single cofinal assertion:

\[
 \boxed{
 \mathrm{FP}_{S\nearrow\Sigma_{\mathbb Q}}[\Phi_Sf,\Phi_Sf]_S
 \ge0
 \quad\text{on the CCM relative cokernel}.}                \tag{32}
\]

Equivalently, one must construct a Hodge star on the relative graded
limit which turns the supermetric (31) into a positive metric.  The star
must mix the odd return variance with the even white-light boundary; a
block-diagonal star cannot do so because of (29).

## 8. Status

Proved without RH or zero input:

* the complete-return operator-valued generic Hodge plane;
* its exact orthogonal middle projector;
* the full operator variance identity (13);
* the exact factorization (15) of every finite local Green energy;
* exact recovery of the scalar masses (1) required by 106.176;
* the exact residual (27);
* identification of the opposite full-rank white-light divergences that
  prohibit an ordinary Hilbert-norm limit.

Still required:

* construction of the off-diagonal Hodge star on the relative graded
  cofinal object (30);
* proof that its positive metric equals the finite part (32) on the CCM
  cokernel.

The remaining step is therefore a super-Hodge gluing theorem, not a
missing prime-return projection and not a scalar finite-part assignment.

