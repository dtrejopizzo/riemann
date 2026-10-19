# R170_858 — Möbius--resolvent coordinate and Ward wall

## 0. Verdict

The transverse coordinate isolated in R170_857,

\[
 \mathfrak r_T(f):=
 \operatorname{Re}(\mathsf Q\eta,
                    R\mathsf Q\dot H\mathsf Zf),           \tag{0.1}
\]

admits a complete finite arithmetic expansion. The observer
\(\eta\) and the source \(\mathsf Q\dot H\mathsf Zf\) contain the comb of
all integers, the Möbius inverse, the exact values of
\(\Lambda\), both orientations, the hyperbolic tail, and the combined
ports. No residue of \(K^{(2,\partial)}\) remains.

The expansion does not produce a Ward cancellation. Setting

\[
 Y=R\mathsf Q\eta,                                        \tag{0.2}
\]

the coordinate is the mixed pairing

\[
 \mathfrak r_T(f)=\operatorname{Re}(Y,\dot Hf).             \tag{0.3}
\]

Möbius extracts the physical source, but changes the test to
\(B_{N,T}^*Y\). This is the same metric clash from MET--WARD, now in a
single resolvent coordinate. The linear Ward identity of R162_305
cancels algebraically for any test before \(R\) appears; inserting it
into (0.3) gives \(0=0\). In a spectral basis,

\[
 \mathfrak r_T(f)
 =\operatorname{Re}\sum_{\lambda_j>0}
 { (\eta,\phi_j)(\phi_j,\dot Hf)\over\lambda_j},            \tag{0.4}
\]

and neither of the two cross numerators has a sign.

So the operation does not evade W12. It does leave a smaller, exact
residue: a single Ward--resolvent bilinear identity, formulated in
§7. That identity is not proved. VIR--LB and D remain open.

## 1. Three distinct projections

Fix \(M\ge N\ge e^{2T}\) and work in the finite core of R170_856. Use:

\[
 P=P_T,\qquad Q_e=I-P,\qquad
 \Pi:\ PL^2\longrightarrow\mathcal P_T,                   \tag{1.1}
\]

where \(\Pi\) is the primitive projection. In the transported
primitive space of R170_857, set

\[
 \mathsf Z=1_{\{0\}}(H),\qquad
 \mathsf Q=I-\mathsf Z,\qquad
 R=\mathsf Q(H|_{\mathsf Q\mathcal P_T})^{-1}\mathsf Q.   \tag{1.2}
\]

Thus \(Q_e\) is the physical outer projection, \(I-\Pi\) is Tate, and
\(\mathsf Q\) is the spectral complement of the radical. They are not
interchanged in any formula.

Abbreviate

\[
 S=S_N,\quad L=L_M,\quad A=A_M=\mathcal M-L-L^*,\quad
 \mathscr B=(PSP)^{-1}=PM_\mu P.                           \tag{1.3}
\]

The last equality is R170_850(1.5). Although \(M_\mu\) is an infinite
comb, its compression in a window is finite.

## 2. The dual observer is an explicit arithmetic block

At fixed parity, let

\[
 h=\mathscr B^*b=PM_\mu^*Pb,\quad
 q=Q_eS^*Ph.                                                \tag{2.1}
\]

The outer observation operator of R170_857 is
\(\mathscr L=Q_eA\iota\). For every primitive vector \(u\), using the
symmetry of the finite operator \(A\),

\[
 (\mathscr L^*q,u)=(q,Q_eAu)=(Aq,u).
\]

Consequently,

\[
 \boxed{
 \eta=\mathscr L^*q
 =\Pi PAQ_eS^*PM_\mu^*Pb.}                                \tag{2.2}
\]

This is already a closed arithmetic formula. Expanding only the combs,
without moving the outer projection between factors,

\[
\boxed{
\begin{aligned}
 \eta={}&\Pi P\mathcal M Q_e
   \sum_{n\le N}{\tau_{-\log n}\over\sqrt n}
       PM_\mu^*Pb\\
 &-\sum_{d\le M}\sum_{n\le N}
   {\Lambda(d)\over\sqrt{dn}}\,
   \Pi P(\tau_{\log d}+\tau_{-\log d})Q_e
          \tau_{-\log n}PM_\mu^*Pb .
\end{aligned}}                                             \tag{2.3}
\]

The intermediate \(Q_e\) is indispensable: erasing it would turn the
routes that leave and return into a full convolution and would repeat
the error of R161_043/R170_851. Formula (2.3) shows exactly where each
piece enters:

* all integers, through \(S^*\);
* unique factorization, through \(M_\mu^*\);
* the exact values of \(\Lambda(d)\), through \(L+L^*\);
* the archimedean term, through \(\mathcal M\);
* the outer port, through \(Q_e\).

## 3. The transverse source with the Tate connection retained

Let \(f\in\ker H\), \(F=\iota f\), and let \(y\in\mathsf Q\mathcal P_T\),
\(Y=\iota y\). Differentiating
\(H_s=\iota_s^*PA_s\iota_s\) gives

\[
 (y,\dot Hf)
 =(Y,P\dot AF)+\mathfrak t_T(Y,F),                         \tag{3.1}
\]

where the connection term is exactly

\[
 \boxed{
 \mathfrak t_T(Y,F)
 :=(\dot\iota,y,PAF)+(PAY,\dot\iota,f).}                \tag{3.2}
\]

In the normal transport of the primitive fiber,

\[
 \dot\iota,u=\dot\Pi,U
 =-\Phi G^{-1}\dot\Phi^*U                                 \tag{3.3}
\]

by R170_845(1.5). If \(r_U=(I-\Pi)PAU\) is the Tate port of
\(U\), then

\[
 \mathfrak t_T(Y,F)
 =(-\Phi G^{-1}\dot\Phi^*Y,r_F)
  +(r_Y,-\Phi G^{-1}\dot\Phi^*F).                         \tag{3.4}
\]

Thus (3.2) is not a free scalar. It is a finite rank-two term, or
rank-one once parity is fixed. Nor can it be omitted when projecting
onto \(\mathsf Q\).

R170_856(7.2)--(7.3) gives the physical extraction

\[
 P\dot AF=\mathscr B P\mathcal C_{PC}F
              +\mathcal P^{\rm comb}_{N,T}(F),             \tag{3.5}
\]

with

\[
 \mathcal P^{\rm comb}_{N,T}(F)
 =\mathscr BP\dot S AF-\mathscr BPSQ_e\dot AF.             \tag{3.6}
\]

The two terms of (3.6) remain combined; their boundary atoms cancel
only in that order.

From (3.1)--(3.6), the transverse source
\(\mathsf C:=\mathsf Q\dot H\mathsf Z\) is characterized by

\[
\boxed{
 (y,\mathsf C f)
 =(\mathscr B^*Y,P\mathcal C_{PC}F)
  +(Y,\mathcal P^{\rm comb}_{N,T}(F))
  +\mathfrak t_T(Y,F).}                                   \tag{3.7}
\]

## 4. Complete PC expansion of the coordinate

Set

\[
 Y=\iota R\mathsf Q\eta,\quad
 \widetilde Y=\mathscr B^*Y=PM_\mu^*PY.                   \tag{4.1}
\]

Since \(R\) is self-adjoint,

\[
 (\mathsf Q\eta,R\mathsf C f)=(Y,\dot Hf).                \tag{4.2}
\]

The reduced PC curvature of R170_856(3.5) is

\[
\begin{aligned}
 \mathcal C_{PC}={}&S\dot{\mathcal M}-\dot S\mathcal M\\
 &-\dot L^*E\mathscr F-L^*E_-\mathscr F
   -L^*E\dot{\mathscr F}\\
 &-J\mathcal A^{\rm raw}\mathscr F
   -JK\dot{\mathscr F}-JH_{M,N}\dot{\mathscr F}
   -\mathcal A^{\rm raw}.                                \tag{4.3}
\end{aligned}
\]

Here

\[
 \mathcal A^{\rm raw}=\dot LS-L\dot S,\quad
 H_{M,N}=LS-K,                                             \tag{4.4}
\]

with the finite tails and coefficients of R170_856(3.6). In
particular, the full jet \(2K+K^{(2,\partial)}\) has already cancelled
between the Poisson--\(X\) block and the two hyperbolic branches. It is
not reintroduced via Selberg.

Substituting (4.3) into (3.7) gives the requested representation:

\[
\boxed{
\begin{aligned}
 \mathfrak r_T(f)={}&\operatorname{Re}(\widetilde Y,
 P[,S\dot{\mathcal M}-\dot S\mathcal M\\
 &\quad-\dot L^*E\mathscr F-L^*E_-\mathscr F
       -L^*E\dot{\mathscr F}\\
 &\quad-J\mathcal A^{\rm raw}\mathscr F
       -JK\dot{\mathscr F}-JH_{M,N}\dot{\mathscr F}
       -\mathcal A^{\rm raw},]F)\\
 &+\operatorname{Re}(Y,\mathcal P^{\rm comb}_{N,T}(F))
   +\mathfrak t_T(Y,F).
\end{aligned}}                                             \tag{4.5}
\]

Formula (4.5) is finite, preserves both orientations and all ports. It
is uniform as a law in \(T\): the number of active routes changes, not
the identity.

## 5. Spectral form and absence of sign

Let \((\phi_j)\) be an orthonormal basis of the complement of the
radical with

\[
 H\phi_j=\lambda_j\phi_j,\quad \lambda_j>0.
\]

Then (4.2) is equivalent to

\[
 \boxed{
 \mathfrak r_T(f)
 =\operatorname{Re}\sum_j
 { (\eta,\phi_j)(\phi_j,\dot Hf)\over\lambda_j}.}          \tag{5.1}
\]

The denominators are positive. This does not sign the sum because
\((\eta,\phi_j)\) is the return port (2.3), while
\((\phi_j,\dot Hf)\) is the virial source (4.5). They are two
independent cross correlations. Minimality only signs
\(\mathsf Z\dot H\mathsf Z\), which was eliminated by \(R\mathsf Z=0\).

The Cauchy--Schwarz version,

\[
 |\mathfrak r_T(f)|
 \le \|R^{1/2}\mathsf Q\eta\|
      \|R^{1/2}\mathsf Q\dot Hf\|,                        \tag{5.2}
\]

is correct but useless for an equality or a sign without slack. It is
not used as a closing step.

## 6. Ward audit: why no cancellation appears

For a finite perturbation of coefficients \(\xi\), R162_305 proves the
exact identity

\[
 -S(L^\xi+(L^\xi)^*)\mathscr F
 =-(L^\xi)^*E-JL^\xi S-L^\xi S\mathscr F.                 \tag{6.1}
\]

Expanding \(E=S\mathscr F-JS\), the terms of (6.1) cancel in pairs.
This holds for every source vector and every test vector. In
particular, pairing (6.1) with \(\widetilde Y\) produces zero before
using (4.1):

\[
 (\widetilde Y,\text{left side}-\text{right side})=0.\tag{6.2}
\]

That is why the linear Ward identity does not cancel (4.5). It only
asserts that two expansions of the same \(\mathcal C_{PC}\) coincide.
If \(H,R,\mathsf Z,\eta,Y\) are also varied, the chain rule
differentiates the identity \(0=0\); \(\dot R\), \(\dot{\mathsf Z}\),
and \(\dot\eta\) appear, but no additional law.

This route is exactly:

* **MET--WARD:** \(\mathscr B^*\) extracts in the physical metric,
  while the available sign lives in the Hankel metric. In (4.5) the
  vector to which that metric is applied is \(Y\), not \(F\), but the
  clash is the same;
* **W12:** the chain PC \(\to\) Möbius \(\to\) resolvent preserves all
  the information and creates no sign;
* **R162_305:** an outer Ward direction is an algebraic zero even with
  polar, Tate, and both orientations;
* **E90--E91:** the reduced response retains a leak that no Euler gauge
  eliminates.

## 7. The missing exact scalar law

Combine R170_857(6.1) with (4.5). Closing the Tate coordinate for the
horizontal Kato lift is equivalent to the following single equality:

\[
\boxed{
\begin{aligned}
 &\operatorname{Re}(\widetilde Y,P\mathcal C_{PC}F)
 +\operatorname{Re}(Y,\mathcal P^{\rm comb}_{N,T}(F))
 +\mathfrak t_T(Y,F)\\
 &\hspace{25mm}=\mathfrak W_K(f)
       +\operatorname{Re}(q,\chi_F),\\
 &Y=\iota R\mathsf Q\Pi PAQ_eS^*PM_\mu^*Pb.
\end{aligned}}                                             \tag{7.1}
\]

Call (7.1) **RES--WARD**. It is weaker than MET--WARD over the whole
radical and weaker than full outer vector reciprocity: it is a single
bilinear equality for the canonical pair \((Y,F)\). But it is not a
consequence of (6.1); positing it is equivalent to positing the scalar
still missing for \(\Delta^{\rm Tate}=0\).

A valid arithmetic derivation of RES--WARD would have to use
simultaneously:

1. the null defect \(\Lambda*1-\log=0\) before the cancellation of
   (6.1);
2. the nonlinear response \(R\mathsf Q\), before reducing it to a
   spectral identity;
3. the ports \(\mathcal P^{\rm comb}\) and \(\mathfrak t_T\), on the
   same side of the balance;
4. a second physical orientation. An isolated linear Ward identity is
   not enough.

This identifies the minimal type of new mathematics needed: a
**mixed Ward--resolvent** identity, not another coefficient
convolution.

## 8. Finite causal falsifier

The following model shows that minimality, exact causal inversion, and
a rank-one outer observation do not imply RES--WARD.

In the primitive space \(\mathbb R^2\), take

\[
 H=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad
 V_c=\begin{pmatrix}-1&c\\c&0\end{pmatrix},\qquad
 f=e_1.                                                     \tag{8.1}
\]

Then \(\mathsf Z=e_1e_1^*\), \(R=e_2e_2^*\),
\(\mathsf ZV_c\mathsf Z=-1\), and
\(H+sV_c\ge0\) for all sufficiently small \(s<0\). Add an outer space
\(\mathbb Re_3\) and the symmetric operator

\[
 A_0=\begin{pmatrix}
 0&0&0\\0&1&1\\0&1&0
 \end{pmatrix}.                                            \tag{8.2}
\]

With \(P\) on the first two coordinates and \(q=e_3\),

\[
 Q_eA_0P(x_1,x_2)=x_2e_3,\quad
 \eta=(Q_eA_0P)^*q=e_2.                                   \tag{8.3}
\]

Hence

\[
 (\mathsf Q\eta,R\mathsf QV_c\mathsf Zf)=c.              \tag{8.4}
\]

Now incorporate a causal cell of the integer comb. Let

\[
 N_0=\begin{pmatrix}0&1\\0&0\end{pmatrix},\quad N_0^2=0,
 \quad S_2=I+2^{-1/2}N_0,\quad
 M_2=I-2^{-1/2}N_0.                                       \tag{8.5}
\]

Thus \(M_2S_2=S_2M_2=I\), exactly like the local pair
\(1(2)=1,\mu(2)=-1\). Define

\[
 \mathcal C_{PC,c}=S_2V_c,\quad
 \mathcal P^{\rm comb}=0.                                 \tag{8.6}
\]

The Möbius extraction is exact:

\[
 M_2\mathcal C_{PC,c}=V_c,                                \tag{8.7}
\]

but coordinate (8.4) is still the arbitrary number \(c\). The model
does not claim to replace the comb of \(\mathbb Z\); it falsifies the
claim that the formal structures already proved --minimality, Kato,
nilpotent causality, Möbius inversion and rank-one outer observation--
force the cancellation. A proof must use an additional relation
between the exact cells of \(\Lambda\) and the global resolvent.

## 9. Calibration by finite modification

The additional relation also cannot be an identity that survives a
finite modification of \(\Lambda\). For the model \(a_\kappa\) of the
first chamber, R163_133 proves

\[
\begin{aligned}
 D_{a_\kappa,2}
  &=(\kappa-1)\log2\,(\delta_0-\nu_4),\\
 D_{a_\kappa,3}
  &=(\kappa-1)\log3\,(\delta_0-\nu_3).                    \tag{9.1}
\end{aligned}
\]

Those terms are the exact finite edges of the defect
\(a*1-\log\). The full linear Ward identity cancels them again with
their PC counterparts, as in §6. Hence a valid RES--WARD must pass the
following adversarial test:

* for \(a=\Lambda\), its defective side must vanish;
* for \(a=a_\kappa\), the derivation prior to cancellation must retain
  the edges \(4\to1\) and \(3\to1\) of (9.1), coupled to the variation
  of the resolvent/observer;
* if the same equality (7.1) holds for every \(\kappa\), the supposed
  law is just (6.1) rewritten and fails the finite-modification
  falsifier.

The mixed coupling between (9.1) and the reduced response does not
exist in the corpus. That is the exact law still missing.

## 10. Status

```text
observer eta as block A--Q--S*--Möbius, (2.2)--(2.3)        PROVED
transverse source with Tate connection, (3.7)               PROVED
full PC/Möbius expansion of the coordinate, (4.5)            PROVED
preservation of tail, reflection, and combined port          PROVED
separate cancellation of 2K + K2                             RETAINED
cancellation of the coordinate by linear Ward                REFUTED
identification with MET--WARD/W12                            PROVED
finite causal falsifier                                      PROVED
mixed scalar law RES--WARD, (7.1)                            FORMULATED / OPEN
coupling of the Ward edges with the resolvent                ABSENT
Delta_Tate / VIR--LB / D                                     OPEN
```

The next admissible piece is not another PC expansion: (4.5) already
contains all of them. It must construct the mixed coupling between the
divisor defect and the resolvent variation that RES--WARD requires, and
it must reproduce (9.1) in the \(a_\kappa\) falsifier.
