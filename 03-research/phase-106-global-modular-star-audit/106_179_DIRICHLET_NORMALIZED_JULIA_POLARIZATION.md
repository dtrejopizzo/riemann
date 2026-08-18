# 106.179 — Dirichlet-normalized Julia polarization

## 1. Purpose

The Julia involution of 106.178 supplies the correct off-diagonal Hodge
operator, but its unweighted positive metric is not the local Green
metric. On an invariant Julia graph it produces the inverse defect

\[
 2C_I(I\mp T_I)^{-1},
\]

whereas the finite-place Green identity contains the first-order defect

\[
 C_I(I-T_I)=C_I I-A_I.
\]

This note determines the unique commuting weight which changes the
ambient Julia metric into the exact Dirichlet metric on the physical
invariant graph. The weight vanishes quadratically at the unitary
endpoint, while the graph is singular there; their product leaves the
required first-order radical. Thus the correction is compatible with
the nonreduced/torsion-sensitive nature of CCM degree one.

No zero of zeta and no sign of the global Weil form is used.

## 2. Weighted Julia Hodge structures

Let \(H\), \(C>0\), \(T=T^*\), \(\|T\|\le1\), and

\[
 D=(I-T^2)^{1/2},\qquad
 S=\begin{pmatrix}T&D\\D&-T\end{pmatrix}
\tag{1}
\]

be the complete-return data of 106.178. Thus \(S=S^*=S^{-1}\). Let
\(q:[-1,1]\to[0,\infty)\) be Borel and put

\[
 Q_q=\begin{pmatrix}q(T)&0\\0&q(T)\end{pmatrix}.
\tag{2}
\]

Functional calculus gives

\[
 [Q_q,S]=0.
\tag{3}
\]

On the form domain of \(Q_q^{1/2}\), define

\[
 \mathfrak k_q(v,w)=-\langle Q_qSv,w\rangle,
 \qquad
 \Omega_q(v,w)=-\operatorname {Im}\mathfrak k_q(v,w),
 \qquad
 \mathcal J=-iS.
\tag{4}
\]

### Theorem 2.1 — Weighted positive polarization

The form \(\Omega_q\) is real alternating, \(\mathcal J^2=-I\), and

\[
 \Omega_q(\mathcal Jv,\mathcal Jw)=\Omega_q(v,w).
\tag{5}
\]

Its compatible symmetric form is

\[
 \boxed{
 g_q(v,w)=\Omega_q(v,\mathcal Jw)
          =\operatorname {Re}\langle Q_qv,w\rangle.}
\tag{6}
\]

It is nonnegative and its radical is \(\ker Q_q\). After quotienting by
that radical and completing, (4)--(6) give a positive Hodge structure.
Every symmetry commuting with the return operators commutes with
\(Q_q\), \(S\), and \(\mathcal J\).

#### Proof

Self-adjointness of \(Q_qS\) follows from (3), so the imaginary part in
(4) is alternating on the underlying real space. Equations
\(S^2=I\) and (3) give \(\mathcal J^2=-I\) and invariance (5). With the
inner product linear in the first variable,

\[
 \mathfrak k_q(v,\mathcal Jw)
 =-\langle Q_qSv,-iSw\rangle
 =-i\langle Q_qv,w\rangle.
\tag{7}
\]

Taking minus the imaginary part proves (6). The remaining assertions
follow from \(Q_q\ge0\) and functional calculus. \(\square\)

## 3. The two invariant Julia graphs

On the defect domains define

\[
 K_+=(I-T)D^\dagger,
 \qquad
 K_-=-(I+T)D^\dagger.
\tag{8}
\]

Their graphs are respectively the \(+1\) and \(-1\) eigenspaces of
\(S\). Let \(\iota_\pm f=(f,K_\pm f)\). On the open spectral interval
\((-1,1)\), scalar functional calculus gives

\[
 I+K_+^*K_+=2(I+T)^{-1},
 \qquad
 I+K_-^*K_-=2(I-T)^{-1}.
\tag{9}
\]

Consequently

\[
 \boxed{
 \begin{aligned}
 g_q(\iota_+f,\iota_+g)
  &=\operatorname {Re}\langle
      2q(T)(I+T)^{-1}f,g\rangle,\\
 g_q(\iota_-f,\iota_-g)
  &=\operatorname {Re}\langle
      2q(T)(I-T)^{-1}f,g\rangle.
 \end{aligned}}
\tag{10}
\]

These identities extend as closed-form identities at the endpoints.

## 4. Exact and unique Dirichlet normalization

The physical complete-return energy is

\[
 \mathcal E_T(f,g)
 =C\operatorname {Re}\langle(I-T)f,g\rangle.
\tag{11}
\]

Define

\[
 \boxed{q_D(t)=\frac C2(1-t)^2,\qquad
 Q_D=\frac C2
 \begin{pmatrix}(I-T)^2&0\\0&(I-T)^2\end{pmatrix}.}
\tag{12}
\]

### Theorem 4.1 — Exact local Green metric on the negative graph

For every \(f,g\) in the closed graph-form domain,

\[
 \boxed{
 g_D(\iota_-f,\iota_-g)
 =C\operatorname {Re}\langle(I-T)f,g\rangle
 =\mathcal E_T(f,g).}
\tag{13}
\]

Among all scalar weights \(q(T)\) commuting with \(T\), equation (13)
determines \(q\) uniquely on the spectral support in \((-1,1)\).

#### Proof

Substitution of (12) in the second line of (10) gives

\[
 2q_D(T)(I-T)^{-1}=C(I-T),
\tag{14}
\]

which is (13). Conversely, equality with (11) for every vector in every
spectral subspace implies

\[
 {2q(t)\over1-t}=C(1-t)
\tag{15}
\]

for the spectral measure of \(T\), hence
\(q(t)=C(1-t)^2/2\) on \((-1,1)\). \(\square\)

For the return system of 106.177,

\[
 T_I=C_I^{-1}A_I,
\tag{16}
\]

and (13) becomes the literal full local energy

\[
 \boxed{
 g_{D,I}(\iota_-f,\iota_-g)
 =\operatorname {Re}\langle(C_I I-A_I)f,g\rangle
 =\frac12\operatorname {Re}\sum_iw_i
   \langle(I-U_i)f,(I-U_i)g\rangle.}
\tag{17}
\]

For the oriented ordinary-prime shells
\(w_{p,k}=(\log p)p^{-|k|/2}\), this is exactly the finite-place
Dirichlet term in the CCM local Green identity of 106.176.

## 5. Endpoint order and the torsion signal

The unweighted Julia metric used in 106.178 corresponds to constant
\(q=C\). Its pullback to the negative graph is

\[
 2C(I-T)^{-1},
\tag{18}
\]

so it polarizes the inverse defect, not the Green energy. This is why a
direct unweighted graph descent cannot prove the CCM metric identity.

Near the unitary endpoint \(t=1\), the negative graph has

\[
 |K_-(t)|^2={1+t\over1-t},
\tag{19}
\]

while \(q_D(t)\) vanishes as \((1-t)^2\). Their product in (10) is
exactly first order:

\[
 q_D(t)(1+|K_-(t)|^2)=C(1-t).
\tag{20}
\]

Thus the singular graph is not discarded. It converts a quadratic
ambient radical into the first-order Dirichlet radical required by the
Green form. Completing the ambient space before pulling back to the
graph would lose this endpoint information; the order in (20) is a
concrete reason the descent must remain torsion-sensitive.

## 6. What is now reduced to the global boundary

At a finite return cutoff, the compensated Green form is

\[
 \mathfrak h_I(f,g)
 =\mathcal E_I(f,g)-C_I\langle f,g\rangle+\mathcal P_I(f,g).
\tag{21}
\]

By (17), this is now the exact identity

\[
 \boxed{
 \mathfrak h_I(f,g)
 =g_{D,I}(\iota_-f,\iota_-g)
  +\mathcal B_I(f,g),
 \qquad
 \mathcal B_I=\mathcal P_I-C_I\langle\cdot,\cdot\rangle.}
\tag{22}
\]

Unlike the variance decomposition of 106.177, no regression-square
remainder is left in (22): every complete return shell is already inside
the polarized graph metric. The sole remaining discrepancy is the
joined Gamma--polar/generic boundary form \(\mathcal B_I\).

Equation (22) does not assign a sign to that boundary. Its cofinal finite
part must be taken jointly with the graph metric, because both contain
the opposite white-light terms identified in 106.177. The remaining
comparison is therefore narrower:

1. extend the weighted negative graph through the nuclear CCM
   restriction cone without Hilbert-closing its endpoint;
2. prove that the Gamma--polar boundary is precisely the boundary term
   in the torsion graph Green formula;
3. identify the resulting finite-part alternating form with the CCM
   Rosati residue pairing.

The local prime-return metric and the choice of Julia weight are no
longer open.

## 7. Status

Proved without RH or zero input:

* a family of weighted Julia Hodge structures;
* exact pullback formulas on both invariant graphs;
* the unique Dirichlet-normalizing weight;
* equality of the induced negative-graph metric with every finite local
  CCM return energy;
* the precise quadratic-to-linear endpoint mechanism retaining the
  radical;
* reduction of the finite metric discrepancy to the single
  Gamma--polar/generic boundary form.

Still required:

* torsion-sensitive nuclear extension of the weighted graph;
* the global Gamma--polar boundary Green identity on that graph;
* equality of the descended alternating form with the CCM Rosati pairing.
