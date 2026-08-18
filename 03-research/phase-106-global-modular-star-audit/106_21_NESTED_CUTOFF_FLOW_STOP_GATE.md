# 106.21 — Nested-cutoff flow and the prime-event stop gate

## Purpose

The compensated inequality of 106.19 is numerically saturated by
low-frequency vectors concentrated near the moving endpoints. This suggests
varying the support length \(L\), following the ground branch through the
prime-power events \(L=\log m\), and applying a Schur/Feshbach argument at
each event.

That proposal must first pass the repository nonduplication gate. It does
not. Feshbach shorting, endpoint traces, prime-cell Kato currents and
moving-cutoff rank-one von Mangoldt events were already developed in Phases
72, 73, 77, 88--90, 95 and 101. The present normalization nevertheless
reveals a short exact reason that this flow cannot by itself prove the
missing inequality:

\[
 \boxed{J_{L,M}^{*}Q_MJ_{L,M}=Q_L\qquad(M\ge L).}
\tag{1}
\]

Thus a new prime-power event has **zero compressed jump** on the old
Hilbert space. The family is a nested-domain compression of one form, not
an arithmetic monotone perturbation. Its ground Rayleigh value can only
move downward as \(L\) grows.

No statement in this note proves positivity of the Weil form or RH.

## 1. Nonduplication audit

The closest previous constructions are the following.

| Earlier item | Content already established | Consequence here |
|---|---|---|
| Phases 22--23; P75.007--009 | Paley--Wiener support barriers and cutoff transport | No Paley--Wiener continuation claim is reopened here |
| Phase 72 | Exact Feshbach/Schur shorting, endpoint corrections and prime-power cells | A Feshbach identity is a coordinate system, not a sign theorem |
| E73.175, E73.190--192 | Boundary-trace reduction, rank-one endpoint derivative and ramp subtraction | A generic endpoint-trace attack is duplicated |
| E77.7d | Fixed-\(L\) CCM matrices are nested compressions of a lower-semibounded operator | Nested finite-section min--max is already available |
| E88.001--004 | Exact layer Feshbach pencil; common-scale closure fails | A layer denominator does not select the arithmetic branch |
| E90.002--004 | Kato rotation current expanded exactly into von Mangoldt prime cells | Prime-driven spectral flow has already been written explicitly |
| Phase 95 | Moving scalar level absorbed into determinant identities | Moving the level is not an independent sign source |
| E101.081, E101.083 | Moving-cutoff rank-one von Mangoldt events and finite graph no-go | Event labels do not transport to spectral-zero labels |
| Phase 104 closure | Cofinal cutoff freedom in the A1 normalization | Enlarging a cutoff redistributes the same RH-strength content |

The theorem below is not a new Feshbach mechanism. It is a stop gate for
reopening that mechanism in the compensated form of 106.19.

## 2. The semilocal forms

Let

\[
 I_L=[-L/2,L/2],\qquad \mathcal H_L=L^2(I_L),
\tag{2}
\]

and let \(J_{L,M}:\mathcal H_L\to\mathcal H_M\) be extension by zero,
\(M\ge L\). Every function below is identified with its zero extension to
\(L^2(\mathbb R)\). Put

\[
 w_m=\frac{\Lambda(m)}{\sqrt m},\qquad a_m=\log m.
\tag{3}
\]

On the common smooth core, the semilocal completed Weil form has the
structure

\[
\begin{aligned}
 Q_L(f,g)
 &=Q_{\infty,\Gamma,\mathrm{pol}}(f,g)\\
 &\quad-\sum_{2\le m\le e^L}w_m
 \bigl(\langle f,\tau_{a_m}g\rangle
       +\langle f,\tau_{-a_m}g\rangle\bigr),
\end{aligned}
\tag{4}
\]

where the first line contains the full Gamma and polar terms and is
independent of the cutoff once \(f,g\) are fixed. Formula (4) is the
polarization of 106.17(5).

### Lemma 1 — Support orthogonality

If \(f,g\in\mathcal H_L\) and \(|a|\ge L\), then

\[
 \langle f,\tau_ag\rangle=0.
\tag{5}
\]

#### Proof

The supports of \(f\) and \(\tau_ag\) are contained in intervals of length
\(L\) whose interiors are disjoint. At \(|a|=L\) they meet in at most one
endpoint, a null set. Hence their \(L^2\) inner product is zero. \(\square\)

### Theorem 2 — Exact nested-compression consistency

For every \(M\ge L\),

\[
 \boxed{
 Q_M(J_{L,M}f,J_{L,M}g)=Q_L(f,g)
 }
\tag{6}
\]

for all vectors in the common form core, and hence on the closed form
domains by continuity.

#### Proof

The Gamma and polar terms in (4) are unchanged by zero extension. The terms
with \(a_m\le L\) are the same in both forms. Every additional term in
\(Q_M\) has

\[
 L<a_m\le M,
\tag{7}
\]

and both of its correlations vanish by Lemma 1. The event \(a_m=L\) also
vanishes because equality in (5) is allowed. This proves (6). \(\square\)

## 3. The cancellation inside the centered square

The absence of an event jump is less obvious in the centered decomposition
of 106.17,

\[
 Q_L=\mathcal D_{e^L}-\kappa_{e^L}I+P_L,
\tag{8}
\]

where \(P_L\) is the polar rank-two form. Suppose \(L<a_m\le M\). By
Lemma 1 and unitarity of translation on the full line,

\[
\begin{aligned}
 w_m\langle f-\tau_{a_m}f,g-\tau_{a_m}g\rangle
 &=2w_m\langle f,g\rangle.
\end{aligned}
\tag{9}
\]

On the other hand this atom changes the centering constant by exactly

\[
 \Delta\kappa=2w_m.
\tag{10}
\]

Therefore its contribution to
\(\mathcal D_{e^M}-\kappa_{e^M}I\), compressed to \(\mathcal H_L\), is
identically zero. Equations (9)--(10) give an independent term-by-term
check of (6). In particular, treating the positive term (9) without the
centering jump (10) creates a false monotone flow.

## 4. Variational and Feshbach consequences

Define the bottom Rayleigh value

\[
 \mu_L=\inf_{0\ne f\in\operatorname{Dom}Q_L}
 \frac{Q_L(f,f)}{\|f\|^2}.
\tag{11}
\]

### Corollary 3 — The domain flow has the wrong monotonicity

For \(M\ge L\),

\[
 \boxed{\mu_M\le\mu_L.}
\tag{12}
\]

#### Proof

The zero-extended copy of \(\operatorname{Dom}Q_L\) is a trial subspace for
\(Q_M\), and its Rayleigh quotients are unchanged by (6). \(\square\)

Consequently a negative branch, once present, cannot be lifted by increasing
the cutoff. Conversely, positivity at one finite cutoff does not propagate
to larger cutoffs.

For completeness, decompose

\[
 \mathcal H_M=J_{L,M}\mathcal H_L\oplus\mathcal S_{L,M}
\tag{13}
\]

and write the form matrix as

\[
 Q_M=\begin{pmatrix}Q_L&B_{L,M}\\B_{L,M}^*&C_{L,M}\end{pmatrix}.
\tag{14}
\]

If \(C_{L,M}>0\) is invertible, exact shorting gives

\[
 \operatorname{Short}_{\mathcal H_L}(Q_M)
 =Q_L-B_{L,M}C_{L,M}^{-1}B_{L,M}^*
 \le Q_L.
\tag{15}
\]

Thus even under the favorable assumption that the new shell is positive,
its Feshbach correction is negative semidefinite. At a fresh prime-power
threshold the old--old event block is zero; all new information enters
through the shell and its coupling \(B_{L,M}\). Proving that this coupling
cannot create a negative direction is the original branch inequality, not a
consequence of event monotonicity.

## 5. Fixed-radical endpoint flow is necessarily nonmonotone

The moving co-Poisson construction suggests a second version of the same
idea: start with a complete radical vector and vary only its truncation.
The following abstract identity shows why monotonicity again cannot be the
missing theorem.

Let \(Q\) be a continuous Hermitian form on a space stable under the
cutoffs \(P_a=\mathbf1_{[-a,a]}\). Let \(F\) lie in its polarized radical,

\[
 Q(F,h)=0\qquad\text{for every admissible }h.
\tag{16}
\]

Put \(q_a=P_aF\) and \(r_a=(1-P_a)F\).

### Lemma 4 — Radical truncation conservation

For every admissible \(a\),

\[
 \boxed{Q(q_a,q_a)=Q(r_a,r_a).}
\tag{17}
\]

#### Proof

From \(F=q_a+r_a\) and (16),

\[
 0=Q(F,q_a)=Q(q_a,q_a)+Q(r_a,q_a).
\tag{18}
\]

Using (18) and its conjugate in \(Q(F,F)=0\) gives (17). \(\square\)

Assume additionally that \(q_a\to0\) in form topology as \(a\downarrow0\)
and \(r_a\to0\) in form topology as \(a\to\infty\). Then

\[
 \lim_{a\downarrow0}Q(q_a,q_a)
 =\lim_{a\to\infty}Q(q_a,q_a)=0.
\tag{19}
\]

Hence any one-sided monotonicity in \(a\) forces
\(Q(q_a,q_a)\equiv0\). A nontrivial truncated radical must rise and fall.
This conclusion does not depend on zero locations.

The obstruction is not peculiar to the Weil form. For example, on
\(L^2(\mathbb R)\) let

\[
 Q_h(f,f)=|\langle f,h\rangle|^2,
 \qquad h(x)=e^{-x^2},
\tag{20}
\]

and choose

\[
 F(x)=(x^2-\tfrac14)e^{-x^2}.
\tag{21}
\]

Then \(\langle F,h\rangle=0\), so \(F\) is in the radical of the rank-one
form, while

\[
 Q_h(P_aF,P_aF)>0
\tag{22}
\]

for generic finite \(a\), and the value tends to zero at both endpoints.
Thus radicality plus positivity does not imply endpoint monotonicity even in
the simplest exact model.

For the actual moving co-Poisson tests, allowing the complete radical vector
\(F_L\) itself to depend on \(L\) adds the uncontrolled derivative
\(\partial_LF_L\). No sign follows from (17); this is precisely the leakage
and frame-conditioning gate already isolated in 106.12--106.14.

### Proposition 5 — Exact endpoint trace and the moving-shape term

The preceding obstruction can also be read directly on the divisor side.
Let \(Q_T\) denote any finite symmetry-complete truncation of the divisor
sum. With

\[
 \widehat q_a(z)=\int_{-a}^{a}F(x)e^{-izx}\,dx,
 \qquad
 b_a(z)=F(a)e^{-iaz}+F(-a)e^{iaz},
\tag{23}
\]

one has the finite identity

\[
 \boxed{
 \frac d{da}Q_T(q_a,q_a)
 =
 2\operatorname{Re}\sum_{z\in\mathcal Z_T}
 \overline{\widehat q_a(\bar z)}\,b_a(z).
 }
\tag{24}
\]

Here \(\mathcal Z_T\) is the finite symmetry-complete spectral divisor in the
normalization of 106.12. If the differentiated full divisor series converges
in a specified ordinary or Abel sense, (24) passes to that limit in the same
sense. No such passage is needed for the sign obstruction: already every
finite current is a signed correlation between the accumulated transform and
the two boundary values.

If the complete radical vector also moves, \(F=F_a\), then

\[
 \boxed{
 \partial_a\widehat{P_aF_a}(z)
 =
 F_a(a)e^{-iaz}+F_a(-a)e^{iaz}
 +\widehat{P_a(\partial_aF_a)}(z).
 }
\tag{25}
\]

Thus a boundary estimate controls only the first two terms. The in-window
shape derivative is an independent term, and for the prolate/co-Poisson
family it contains the same moving-frame conditioning already exposed in
106.14.

#### Proof

Leibniz' rule gives (23) and (25). Differentiate the finite polarized
divisor sum term by term. The two differentiated factors are conjugates
after the divisor symmetries are combined, giving twice the real part in
(24). The final limiting statement is immediate whenever the declared
summation method permits differentiation. \(\square\)

## 6. Verdict

The proposed prime-event/Feshbach flow is closed as a duplicate and as an
independent sign mechanism:

\[
\boxed{
 \text{new atom on the old block}=0,
 \qquad
 \text{domain expansion can only lower the ground infimum}.}
\tag{26}
\]

The vector-specific endpoint variant is also not a new route: Phases 72--73
already reduce it to boundary packets, while Lemma 4 shows that a monotone
fixed-radical flow is impossible unless it is trivial.

What survives is narrower. Any proof of

\[
 \mathcal A_\Delta(f)
 \le\mathcal E_*(f)-c_*\|f\|^2
\tag{27}
\]

must estimate the **old--shell coupling on the moving near-radical family**
while retaining the complete signed prime--Gamma compensation. Neither
prime-event jumps nor a scalar monotone endpoint flow supplies that estimate.
