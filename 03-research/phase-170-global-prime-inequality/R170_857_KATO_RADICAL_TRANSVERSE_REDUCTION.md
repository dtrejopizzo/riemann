# R170_857 — Kato radical/transverse reduction of the Tate defect

## 0. Verdict

The minimality of first contact does orient a complete matrix, but it is
only the radical compression

\[
 B:=\mathsf Z\dot H\mathsf Z\preceq0,                       \tag{0.1}
\]

where \(\mathsf Z\) projects onto \(\ker H\). The dual scalar of
R170_856(8.7), on the other hand, contains the transverse response

\[
 R\,(I-\mathsf Z)\dot H\mathsf Z,
 \qquad
 R=\bigl(H|_{(\ker H)^\perp}\bigr)^{-1}.                   \tag{0.2}
\]

Block (0.2) receives no sign from (0.1). Below an exact identity is
obtained that separates both sectors and reduces the outer reciprocity
to a single scalar equality. The equality is not proved here. Hence the
outer Wronskian, VIR--LB and D remain open.

There is an essential analytic caveat. Claim (0.1) requires a
\(C^1\) family of forms on a fixed primitive space. That regularity is
not proved unconditionally in the corpus: R162_407 obtains the virial
law only under (REG), while without (REG) it gives only moduli of
continuity. Every use of \(\dot H\), of a differentiable branch, or of
the reduced resolvent in this memo is made under the precise hypothesis
of §1.

## 1. Legitimate perturbation framework

Let \(s=0\) be first contact and let \(s<0\) be the preceding windows.
Assume:

1. there is a fixed primitive space \(\mathfrak P\) and a \(C^1\)
   isometric transport, \(\iota_s:\mathfrak P\to\mathcal P_s\);
2. the transported forms
   \[
     H_s=\iota_s^*P A_s\iota_s                              \tag{1.1}
   \]
   form a self-adjoint \(C^1\) family of Kato type, with common form
   domain and compact resolvent;
3. \(H_0=:H\ge0\), zero is isolated, and
   \[
     H_s\ge0\qquad(-s_0<s\le0).                             \tag{1.2}
   \]
4. for \(u\in\ker H\), the form
   \(v\mapsto\dot h_0(u,v)\) is represented by a vector \(Vu\) of the
   Hilbert space, and \(q\in\operatorname{Dom}(\mathscr L_0^*)\). This is
   automatic for a \(C^1\) family of operators with common domain;
   it is made explicit because an abstract family of type-(B) forms does
   not guarantee it on its own.

Set

\[
 \mathsf Z=1_{\{0\}}(H),\quad
 \mathsf Q=I-\mathsf Z,\quad
 R=\mathsf Q(H|_{\mathsf Q\mathfrak P})^{-1}\mathsf Q,
 \quad V=\dot H.                                           \tag{1.3}
\]

The operator \(R\) is bounded and positive. Define the two velocity
blocks

\[
 B=\mathsf ZV\mathsf Z,\qquad
 C=\mathsf QV\mathsf Z.                                   \tag{1.4}
\]

The letters \(\mathsf Z,\mathsf Q\) are spectral projections. They
should not be confused with the renormalized operator \(Z_N\) nor with
the physical projection \(Q_T=I-P_T\).

## 2. The part that orients minimality

**Proposition 2.1.** Under §1,

\[
 \boxed{B\preceq0\text{ on }\ker H.}                    \tag{2.1}
\]

**Proof.** For \(u\in\ker H\) and \(t>0\), (1.2) gives

\[
 0\le \langle u,H_{-t}u\rangle
   =-t\langle u,Vu\rangle+o(t).
\]

Dividing by \(t\) and letting \(t\downarrow0\) proves
\(\langle u,Vu\rangle\le0\) for all \(u\in\ker H\). QED.

This is the important correction relative to a reading that would
orient only the minimal slope: if the fixed family is genuinely
\(C^1\), the whole compression \(B\) is oriented. What is not oriented
is \(C\).

Without the \(C^1\) hypothesis, the argument above cannot be written.
The unconditional continuity of R162_407 does not define \(V\); under
its (REG), the virial form is the candidate for \(-B\), provided the
expansion is uniform over all vectors of the radical.

## 3. Kato equation and the sector that remains free

Consider a normalized, differentiable spectral branch

\[
 H_s f_s=\lambda_s f_s,\qquad f_0=f\in\ker H,\qquad
 \lambda_0=0.                                              \tag{3.1}
\]

Write \(\nu=\dot\lambda_0\). Differentiating (3.1) and projecting gives

\[
 \boxed{Bf=\nu f,\qquad
        \mathsf Q\dot f=-RCf.}                             \tag{3.2}
\]

By (2.1), \(\nu\le0\). In normalized real gauge only the following is
known:

\[
 \alpha_f:=\mathsf Z\dot f\perp f;                         \tag{3.3}
\]

the first Kato equation does not determine \(\alpha_f\) inside a
multiple radical. In particular, it is not assumed that \(f_s\) remains
in the radical: typically \(\lambda_s=s\nu+o(s)\) and
\(\mathsf Q\dot f=-RCf\ne0\).

If only a correct first-order lift is needed, for an eigenvector
\(Bf=\nu f\) one may take the horizontal lift

\[
 f_s^{K}=f-sRCf+o(s).                                      \tag{3.4}
\]

Then

\[
 H_sf_s^{K}=s\nu f+o(s),                                  \tag{3.5}
\]

but (3.4) is a first-order quasimode, not a claim that an exact
radical branch exists.

## 4. The outer observable and the transport correction

Let \(Q_e=I-P_T\) be the outer physical projection and define the
port observation operator

\[
 \mathscr L_s:=Q_eA_s\iota_s:\mathfrak P\longrightarrow Q_eL^2,
 \qquad \ell=\mathscr L_0f=Q_eAF.                          \tag{4.1}
\]

The frozen jet from R170_856 is

\[
 \dot\ell^0=Q_e\dot AF.                                   \tag{4.2}
\]

The difference between differentiating the transported observable and
(4.2) is the explicit connection term

\[
 \chi_F:=\dot{\mathscr L}_0f-\dot\ell^0.                  \tag{4.3}
\]

For example, if \(P_T,Q_e\) are fixed and \(A_s\) does not absorb the
connection of \(\iota_s\), then

\[
 \chi_F=Q_eA\dot\iota_0f.                                 \tag{4.4}
\]

Thus (4.3) accounts precisely for the Tate/primitive correction of the
transport; it is not erased by a choice of gauge.

For branch (3.1),

\[
 \dot\ell^{\rm br}
 =\dot\ell^0+\chi_F+\mathscr L_0\dot f.                  \tag{4.5}
\]

Also define the dual primitive vector

\[
 \eta:=\mathscr L_0^*q\in\mathfrak P,                     \tag{4.6}
\]

where \(q=Q_eS^*Ph\) is the outer causal vector of R170_856(8.1).

## 5. Exact reduction of the Tate scalar

We work with real parts if the vectors are complex. From
R170_856(8.4), using
\(z=\ell-\rho q\) and
\(\dot z^0=\dot\ell^0-\rho\dot q^0\), the two terms
\(\rho(\dot q^0,q)\) cancel exactly. Hence R170_856(8.7) is equivalent
to

\[
 \boxed{
 g\Delta^{\rm Tate}
 =\rho(\dot b^0,b)+(\dot q^0,\ell)
  -(q,\dot\ell^0)-\rho g.}                                \tag{5.1}
\]

Introduce the total Wronskian of the branch

\[
 \mathfrak W_{\rm br}(f)
 :=\rho(\dot b^0,b)+(\dot q^0,\ell)
   -(q,\dot\ell^{\rm br})-\rho g.                         \tag{5.2}
\]

Substituting (4.5) into (5.1), using (4.6), and finally (3.2) gives the
main identity:

\[
\boxed{
\begin{aligned}
 g\Delta^{\rm Tate}
  ={}&\mathfrak W_{\rm br}(f)+(q,\chi_F)\\
    &+(\mathsf Z\eta,\alpha_f)
      -(\mathsf Q\eta,RCf).
\end{aligned}}                                             \tag{5.3}
\]

Every term in (5.3) has a fixed type:

* \(B\preceq0\) governs the slope \(\nu\);
* \(C=\mathsf Q\dot H\mathsf Z\) governs the leak out of the radical;
* \(R C f\) is the reduced response;
* \(\alpha_f\) is the rotation inside a multiple radical;
* \(\chi_F\) is the connection of the primitive/Tate submanifold;
* \(\mathfrak W_{\rm br}\) is the only total outer Wronskian that
  remains.

For the horizontal lift (3.4), set

\[
 \dot\ell^K=\dot\ell^0+\chi_F-\mathscr L_0RCf            \tag{5.4}
\]

and define \(\mathfrak W_K\) by (5.2) with
\(\dot\ell^{\rm br}\) replaced by \(\dot\ell^K\). Then

\[
 \boxed{
 g\Delta^{\rm Tate}
  =\mathfrak W_K(f)+(q,\chi_F)
    -(\mathsf Q\eta,RCf).}                                \tag{5.5}
\]

The signed slope \(\nu=(f,Bf)\) does not appear in the last term:
\(R\mathsf Z=0\) exactly removes the diagonal part \(Bf\). The Tate
defect observes the transverse block \(C\), not the quantity that
minimality signs.

## 6. Remaining operator condition

Equation (5.5) identifies the exact scalar condition

\[
\boxed{
 \mathfrak W_K(f)+(q,\chi_F)
 = (\mathsf Q\eta,RCf).}                                  \tag{6.1}
\]

For an exact branch, the radical term \(-(\mathsf Z\eta,\alpha_f)\)
must be added on the right according to (5.3).

Condition (6.1) is strictly weaker than a full outer vector
reciprocity: it only requires the coordinate against \(q\). Any
component of \(\dot\ell\) orthogonal to \(q\) is invisible in (6.1),
even though it changes the full outer law. In block language, only the
rank-one linear form intervenes

\[
 f\longmapsto
 (\mathsf Q\mathscr L_0^*q,
  R\mathsf Q\dot H\mathsf Z f).                            \tag{6.2}
\]

A proof of (6.1) would close \(\Delta^{\rm Tate}=0\) for the selected
vector without proving outer reciprocity in every direction. Here only
the equivalence has been shown, not (6.1).

## 7. Why (2.1) does not sign (6.2)

The failure already appears in dimension two. Take

\[
 H=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
 V=\begin{pmatrix}-1&c\\c&0\end{pmatrix}.                 \tag{7.1}
\]

For every \(c\in\mathbb R\), \(H_s=H+sV\ge0\) for \(s<0\)
sufficiently small, and \(B=-1\). However \(C=c\), so
\(RC=c\) can have any sign and magnitude. Thus left-hand positivity
orients \(B\) but not the pairing (6.2).

If \(Bf=0\), a \(C^2\) hypothesis produces at second order the
Feshbach operator

\[
 \mathsf Z_0\left({1\over2}\ddot H-VRV\right)\mathsf Z_0,
 \qquad \mathsf Z_0=1_{\{0\}}(B),                          \tag{7.2}
\]

but its orientation only bounds \(RCf\) quadratically. It does not
determine the linear pairing of (6.2). (7.2) is not used in (5.3).

## 8. Audit against the corpus

1. **Phases 80--91.** E90_002--003 already show that the level velocity
   vanishes from the line rotation and that a reduced resolvent kernel
   survives. In (5.5) exactly the same thing happens: \(B\) is signed,
   but the response uses \(RC\). E91_004 prevents erasing that leak
   through an Euler gauge.
2. **Phases 100--101.** The adjugate, projection, and commutator
   identities isolate off-diagonal blocks, but do not sign them.
   (6.2) is a coordinate of that same block, not a positive energy.
3. **R162_302/390.** Kato/Danskin orients diagonal compressions of the
   perturbed operator. R162_390 warns that a first-order condition does
   not control higher-order degenerate terms. No inequality on \(C\) is
   inferred here.
4. **R162_407.** Virial differentiability is conditional on (REG).
   Without it there is no proved \(C^1\) family, and §2 must be read as
   a conditional reduction, not as an unconditional theorem about
   Paper 46.
5. **R162_702.** There the spectral background is monotone but the
   angles and cross correlations are unsigned. Term (6.2) is precisely
   a cross correlation of that type.
6. **W12.** Passing through a Kato branch, a resolvent, or a cofactor
   preserves the exact information, but does not manufacture a sign.
   Formula (5.3) is a block reduction; declaring that the last term
   inherits the sign of \(B\) would repeat W12.

## 9. Status

```text
B = Z dotH Z <= 0 under fixed C1 family                PROVED
unconditional existence of that C1 family              OPEN (REG)
transverse equation Q dotf = -R Q dotH f                PROVED under Kato
persistence of the branch inside the radical            NOT ASSUMED / FALSE in general
exact reduction of Delta_Tate, (5.3) and (5.5)          PROVED
sign of the transverse block Q dotH Z                   UNDETERMINED
Kato--PC scalar condition, (6.1)                        IDENTIFIED / OPEN
complete outer reciprocity                              OPEN
VIR--LB and D                                           OPEN
```

The next piece must not diagonalize \(B\) again. It must prove the
scalar equality (6.1), or a direct vanishing of the rank-one coordinate
(6.2), using exact arithmetic. That is now the minimal remaining
operator residue of the Tate defect.
