# R170_856 — Full PC jet: total cancellation of Chebyshev and boundary ledger

## 0. Result and scope correction

The two-scale PC is derived here at finite cutoff, without recombining
its branches before checking the signs. The central result corrects
the provisional reading of R170_855:

\[
 K_-:=\partial_-K_N(r,q)|_{1,1}
 =2K_N+K_N^{(2,\partial)}                                    \tag{0.1}
\]

cancels **entirely** between the Poisson--`X` jet and the two branches
of the hyperbola. It is not only `2K_N` that cancels, leaving the
second jet free. Literally,

\[
 \boxed{
 (-K_- -JK_-\mathscr F)
 +(K_-+JK_-\mathscr F)=0.}                                  \tag{0.2}
\]

Cancellation (0.2) holds as an operator identity on the core, both
before and after applying `P_T` and the causal Möbius inverse. It also
cancels the atoms that would appear if the derivatives were cut before
summing the branches.

Therefore

\[
 -M_\mu\mathcal A_\Lambda^{\rm raw}
 +M_\mu K_N^{(2,\partial)}=-2\dot L_N                       \tag{0.3}
\]

from R170_855 remains a correct identity **inside branch
`-H_-`**, but it is not a surviving summand of the differentiated PC.
Its companion term in the Poisson--`X` jet contains

\[
 -M_\mu K_-=-2L_N-M_\mu K_N^{(2,\partial)},                 \tag{0.4}
\]

which again cancels the Selberg term of (0.3). R170_855 cannot be
used, by itself, as the physical assembly of the prime virial.

After this cancellation an exact ledger remains, with:

1. the archimedean curvature `S dot M-dot S M`;
2. the raw Wronskian, including its incomplete hyperbola;
3. the reflected orientation and the tail `H dot Fcal`;
4. the explicit blocks crossing `P_T`;
5. the combined port of R170_851;
6. the polar continuum and the full Tate coordinate.

No new sign appears. Gates 1--2 of R170_854 §7 are now **computed**,
but their result is a tautological cancellation of the full jet, not
the expected positive energy. VIR--LB and D remain open.

## 1. Finite conventions

Fix cutoffs `M>=N` and use the definitions of R170_847:

\[
 \begin{aligned}
 S(q)&=\sum_{n\le N}n^{-1/2}\tau_{\log n/q},\\
 L(r)&=\sum_{d\le M}{\Lambda(d)\over\sqrt d}
                    \tau_{\log d/r},\\
 K(r,q)&={r\over q}\sum_{n\le N}{\log n\over\sqrt n}
                    \tau_{\log n/q},\\
 A(r)&=\mathcal M_r-L(r)-L(r)^*,\\
 E(r,q)&=S(q)\mathscr F_r-JS(q),\\
 H(r,q)&=L(r)S(q)-K(r,q).
 \end{aligned}                                               \tag{1.1}
\]

The derivation is

\[
 \partial_-=(\partial_r-\partial_q)|_{r=q=1}.                \tag{1.2}
\]

Without an argument, evaluation at `(1,1)` is understood. Set

\[
 \begin{aligned}
 K_-&:=2K+K^{(2,\partial)},\\
 K^{(2,\partial)}
   &:=\sum_{n\le N}{(\log n)^2\over\sqrt n}
          \partial_t\tau_{\log n},\\
 \mathcal A^{\rm raw}&:=\dot L S-L\dot S,\\
 E_-&:=S\dot{\mathscr F}-\dot S\mathscr F+J\dot S.
 \end{aligned}                                               \tag{1.3}
\]

Then

\[
 \boxed{H_-=\mathcal A^{\rm raw}-K_-.}                      \tag{1.4}
\]

All the identities that follow hold on the Schwartz core. No limit is
taken in `M,N`.

## 2. The exact Poisson--`X` jet

The identity prior to the hyperbolic substitution is

\[
 \boxed{
 \{X_r,E(r,q)\}\mathscr F_r
 =S(q)\mathcal M_r-K(r,q)-JK(r,q)\mathscr F_r.}              \tag{2.1}
\]

### Proof

Expand \(E=S\mathscr F-JS\), use
\(\mathscr F_rX_r\mathscr F_r=\mathcal M_r-X_r\),
`X_rJ=-JX_r` and `[X_r,S(q)]=-K(r,q)`. The four terms regroup exactly
into the right-hand side of (2.1). QED.

Differentiating (2.1) gives the complete ledger of the Poisson block:

\[
\boxed{
\begin{aligned}
 \mathcal X_-:={}&
   \{X,E\}\mathscr F
  +\{X,E_-\}\mathscr F
  +\{X,E\}\dot{\mathscr F}\\
 ={}&S\dot{\mathcal M}-\dot S\mathcal M
    -K_- -JK_-\mathscr F-JK\dot{\mathscr F}.
\end{aligned}}                                               \tag{2.2}
\]

The first line shows where the literal jet `dot X=X` is: it is the
first summand \(\{X,E\}\mathscr F\). The second line shows that the
derivative of the full Poisson block contains `-K_-`, not only `-2K`.
Separating only the summand `dot X` is not stable under the Poisson
identity and does not authorize keeping `K2`.

## 3. Differentiated PC and total cancellation

The PC without right Fourier is

\[
 SA=\{X,E\}\mathscr F-L^*E\mathscr F-JH\mathscr F-H.        \tag{3.1}
\]

Its antidiagonal derivative is

\[
\boxed{
\begin{aligned}
 \mathcal C:=S\dot A-\dot S A
 ={}&\mathcal X_-\\
 &-\dot L^*E\mathscr F-L^*E_-\mathscr F
   -L^*E\dot{\mathscr F}\\
 &-JH_-\mathscr F-JH\dot{\mathscr F}-H_-.
\end{aligned}}                                               \tag{3.2}
\]

Insert (1.4) and (2.2). On the causal branch,

\[
 -K_- -H_-=-\mathcal A^{\rm raw},                            \tag{3.3}
\]

and on the reflected branch,

\[
 -JK_-\mathscr F-JH_-\mathscr F
 =-J\mathcal A^{\rm raw}\mathscr F.                         \tag{3.4}
\]

This proves (0.2) and leaves the reduced identity

\[
\boxed{
\begin{aligned}
 \mathcal C={}&S\dot{\mathcal M}-\dot S\mathcal M\\
 &-\dot L^*E\mathscr F-L^*E_-\mathscr F
   -L^*E\dot{\mathscr F}\\
 &-J\mathcal A^{\rm raw}\mathscr F
   -JK\dot{\mathscr F}-JH\dot{\mathscr F}
   -\mathcal A^{\rm raw}.
\end{aligned}}                                               \tag{3.5}
\]

The tail has not been dropped. For `M>=N`,

\[
 \begin{aligned}
 H&=\sum_{N<k\le MN}{h_{M,N}(k)\over\sqrt k}
              \tau_{\log k},\\
 \mathcal A^{\rm raw}
  &=-\sum_{k\le MN}{\beta_{M,N}(k)\over\sqrt k}
              \partial_t\tau_{\log k}.
 \end{aligned}                                               \tag{3.6}
\]

Thus `-JH dot Fcal` literally keeps the incomplete positive tail, and
the `k>N` parts of both Wronskians in (3.5) keep the signed tail.
Formula (3.5) does not replace any of them with a full convolution.

## 4. Möbius audit of R170_855

Let

\[
 M_\mu=\sum_{d\ge1}{\mu(d)\over\sqrt d}\tau_{\log d}.       \tag{4.1}
\]

On complete fibers,

\[
 M_\mu K=L,\qquad
 M_\mu K^{(2,\partial)}=W^{(\partial)},\qquad
 W=\mu*\log^2.                                               \tag{4.2}
\]

Branch `-H_-` of (3.2) produces

\[
 \begin{aligned}
 M_\mu(-H_-)
 &=-M_\mu\mathcal A^{\rm raw}+2L+W^{(\partial)}\\
 &=-2\dot L+2L,                                             \tag{4.3}
 \end{aligned}
\]

where the second line is exactly R170_855. But the causal branch of
`mathcal X_-` simultaneously produces

\[
 M_\mu(-K_-)=-2L-W^{(\partial)}.                             \tag{4.4}
\]

Adding (4.3)--(4.4),

\[
 \boxed{
 M_\mu(-K_--H_-)=-M_\mu\mathcal A^{\rm raw}.}               \tag{4.5}
\]

Consequently, `gamma+W=2 Lambda log` is a correct coefficient identity
on one branch, but **not** a surviving contribution of the full PC.
The `W` that completes `gamma` cancels against the `-W` of (4.4).
Using only (4.3) would repeat a branch separation that the exact
identity (2.1) forbids.

This diagnosis is independent of sign, of first contact and of the
physical cutoff.

## 5. Physical compression: ledger of all return routes

Set `P=P_T`, `Q=I-P`. For any product `UV`,

\[
 PUVP=PUPVP+PUQVP.                                           \tag{5.1}
\]

Applying (5.1) to each product as ordered in (3.5), one obtains

\[
 P\mathcal C P=\mathcal R_{\rm int}+\mathcal R_{\rm cross}, \tag{5.2}
\]

where

\[
\begin{aligned}
\mathcal R_{\rm int}={}&
 PSP\dot{\mathcal M}P-P\dot SP\mathcal MP\\
&-P\dot L^*PE\mathscr FP-PL^*PE_-\mathscr FP
 -PL^*PE\dot{\mathscr F}P\\
&-PJ\mathcal A^{\rm raw}P\mathscr FP
 -PJKP\dot{\mathscr F}P-PJHP\dot{\mathscr F}P\\
&-P\mathcal A^{\rm raw}P,                                  \tag{5.3}
\end{aligned}
\]

and the ledger of routes that leave and return is

\[
\boxed{
\begin{aligned}
\mathcal R_{\rm cross}={}&
 PSQ\dot{\mathcal M}P-P\dot SQ\mathcal MP\\
&-P\dot L^*QE\mathscr FP-PL^*QE_-\mathscr FP
 -PL^*QE\dot{\mathscr F}P\\
&-PJ\mathcal A^{\rm raw}Q\mathscr FP
 -PJKQ\dot{\mathscr F}P-PJHQ\dot{\mathscr F}P.
                                                               \tag{5.4}
\end{aligned}}
\]

Formulas (5.3)--(5.4) are identities at finite cutoff. It is not
claimed that their separate summands have a sign or a domain beyond
the core. Since `JP=PJ`, reflection does not hide another block: all
its crossings are visible in the third line of (5.4). In particular,

\[
 -PJHQ\dot{\mathscr F}P                                    \tag{5.5}
\]

is the reflected route of the hyperbolic tail, and

\[
 -PJ\mathcal A^{\rm raw}_{>N}Q\mathscr FP,\qquad
 -P\mathcal A^{\rm raw}_{>N}P                              \tag{5.6}
\]

are the two explicit appearances of the Wronskian tail, where

\[
 \mathcal A^{\rm raw}_{>N}
 =-\sum_{N<k\le MN}{\beta_{M,N}(k)\over\sqrt k}
              \partial_t\tau_{\log k}.                      \tag{5.7}
\]

The `K_-` terms do not appear in (5.3)--(5.4), because they canceled as
operators before inserting `P+Q`. Inserting projections between the
two identical sides of (0.2) only produces two opposite copies of the
same block; it does not create a new tail.

## 6. Boundary atoms

For a smooth vector with traces,

\[
 \partial_t(Pg)=P g'
 +g(-T+)\delta_{-T}-g(T-)\delta_T,                            \tag{6.1}
\]

while

\[
 \partial_t(Qg)=Q g'
 -g(-T+)\delta_{-T}+g(T-)\delta_T.                            \tag{6.2}
\]

With `tau_a g(t)=g(t+a)`, the translated atoms are

\[
 \partial_t\tau_a(Pg)
 =\tau_a(Pg')+g(-T+)\delta_{-T-a}-g(T-)\delta_{T-a},          \tag{6.3}
\]

and have opposite signs for `Q`. Therefore

\[
 P\dot S(P+Q)AF=P\dot SAF                                  \tag{6.4}
\]

is the only admissible split of the derived port. The atoms of
R170_851 cancel inside (6.4).

The cancellation of `K_-` is even more rigid: the terms of (0.2) are
the same distribution with opposite sign. In particular, the atoms of
`K^{(2,partial)}` cancel before applying the causal inverse. No
Selberg atom is left at the endpoints.

## 7. Causal extraction and combined port

Let

\[
 B=(PSP)^{-1}=PM_\mu P.                                     \tag{7.1}
\]

The exact physical extraction of R170_851 is

\[
\boxed{
 P\dot AF
 =BP\mathcal C F+\mathcal P^{\rm comb}_{N,T}(F),}           \tag{7.2}
\]

with

\[
 \boxed{
 \mathcal P^{\rm comb}_{N,T}(F)
 :=BP\dot S AF-BPSQ\dot AF.}                                \tag{7.3}
\]

Equations (3.5), (5.3)--(5.4) give a full development of the first
term of (7.2). Equations (6.1)--(6.4) fix the distributional order of
the second. Thus every route crossing the window is in one of two
disjoint places:

* internal returns of PC: `R_cross` of (5.4);
* the defect from extracting `S`: the combined port (7.3).

There is no third `K2` residue.

## 8. Full Tate coordinate

Fix a parity and write

\[
 b=b_\epsilon,\qquad g_\epsilon=\|b\|^2,\qquad
 h=(PS^*P)^{-1}b,\qquad q=QS^*Ph.                            \tag{8.1}
\]

At first contact,

\[
 PAF=\rho b,\qquad \ell=QAF,\qquad z=\ell-\rho q.            \tag{8.2}
\]

Set

\[
 \dot b^0=P\dot S^*Ph,\qquad
 \dot q^0=Q\dot S^*Ph,\qquad
 \dot z^0=Q\dot AF-\rho\dot q^0.                            \tag{8.3}
\]

R170_852 simplifies, in the real product, to

\[
\boxed{
 g_\epsilon\,\omega^{\rm comb}
 =\rho(\dot b^0,b)
  +(\dot q^0,z)-(q,\dot z^0).}                              \tag{8.4}
\]

The graded Green law R170_854 gives

\[
 (h,P\mathcal C F)
 +(\dot q^0,z)-(q,\dot z^0)
 =(b,P\dot AF)-\rho(\dot b^0,b).                            \tag{8.5}
\]

Adding (8.4)--(8.5) gives a formula with no hidden ports:

\[
 \boxed{
 g_\epsilon\,\omega^{\rm comb}
 =(b,P\dot AF)-(h,P\mathcal C F).}                          \tag{8.6}
\]

Therefore the exact Tate defect is

\[
 \boxed{
 g_\epsilon\,\Delta^{\rm Tate}
 =(b,P\dot AF)-(h,P\mathcal C F)-\rho g_\epsilon.}         \tag{8.7}
\]

Formula (8.6) jointly accounts for the atoms, the causal exterior and
the Tate term. It does not prove that `Delta_Tate=0`: doing so would
require the open dual equality R170_854 (0.5), or an equivalent
minimality law.

## 9. Polar continuum

For `Z=S-C_N`, the renormalized curvature is exactly

\[
 \boxed{
 Z\dot A-\dot Z A
 =\mathcal C-\mathcal P_{C,A},\qquad
 \mathcal P_{C,A}:=C_N\dot A-\dot C_N A.}                   \tag{9.1}
\]

On a first-contact vector,

\[
\boxed{
\begin{aligned}
 P\mathcal P_{C,A}F={}&
 PC_NP\dot AF+PC_NQ\dot AF\\
 &-\rho P\dot C_N b-P\dot C_N\ell.
\end{aligned}}                                               \tag{9.2}
\]

Neither the exterior route `PC_NQ dot A F` nor the coupling
`P dot C_N ell` has been removed. The polar velocity is the explicit
formula of R170_844:

\[
\begin{aligned}
 \dot C_Nf(t)={}&(1-t/2)C_Nf(t)
 +e^{-t/2}\int_{-\infty}^{t+\log N}
       {v\over2}e^{v/2}f(v)\,dv\\
 &-(\log N)\sqrt N\,f(t+\log N).                            \tag{9.3}
\end{aligned}

The last line is the moving face of the continuum. Together with the
integer atoms of §6 it forms the complete polar boundary; neither has
a sign on its own.

The renormalized version of (7.2) is obtained without a new inversion:

\[
 \boxed{
 P\dot AF
 =BP(Z\dot A-\dot Z A)F
  +BP\mathcal P_{C,A}F
  +\mathcal P^{\rm comb}_{N,T}(F).}                          \tag{9.4}
\]

Thus (5.4), (7.3), (8.6) and (9.2) are the requested ledger of
support, tail, reflected orientation, Tate and polar terms.

## 10. Collisions with the corpus

1. **Mixed `E--C`.** The right-hand side of (8.5) is the same,
   correctly typed, concomitant of R161_057--064. The expansion does
   not cancel it; it only shows that no `K2` port is missing.
2. **Selberg.** R170_855 correctly uses
   `gamma+W=2 Lambda log`, but (4.4) supplies the mandatory `-W` from
   the same PC. Keeping one and omitting the other would repeat the
   partial deconvolution rejected in R170_851.
3. **Ratio-comb.** No operator has been squared, so the ratio-comb of
   R166_502 is not manufactured. Squaring (3.2) would return to that
   wall or to the indefinite metric of R170_854 (3.4).
4. **Positive tail.** `H` remains in (3.6), (5.3) and (5.5). Its
   positive coefficient does not sign `H dot Fcal`, because the
   Fourier jet and the compression have both signs.
5. **Minimality.** The only appearance used is `PAF=rho b`. Dynamical
   minimality does not prove (8.7)=0 nor orient the seven blocks of
   (5.4).

## 11. Verdict for gates 1--2 of R170_854

Gate 1 has a complete answer:

\[
 \boxed{
 \text{the term }2M_\mu K\text{ cancels, but only as part of the
 larger cancellation }M_\mu K_-=0.}                         \tag{11.1}
\]

In particular, no `M_mu K2=W` remains to combine as an independent
energy with `gamma`.

Gate 2 is also fully accounted for, but not signed:

\[
 \boxed{
 \text{full boundary}
 =\mathcal R_{\rm cross}
  +\mathcal P^{\rm comb}_{N,T}
  +BP\mathcal P_{C,A},}                                     \tag{11.2}
\]

with its Tate coordinate given by (8.6) and its tails by (3.6),
(5.5)--(5.7). None of these three summands can be erased or signed
separately.

The remaining problem is not completing the algebraic cancellation:
it is already complete. It is a new law orienting the dual scalar

\[
 (b,P\dot AF)-(h,P\mathcal C F)-\rho\|b\|^2                 \tag{11.3}
\]

or, equivalently, the exterior Wronskian of R170_853. That law remains
unproved.

## 12. Status

```text
exact jet of the Poisson--X block, equation (2.2)              PROVED
full antidiagonal PC, equation (3.2)                           PROVED
cancellation of 2K + K2 on both orientations                   PROVED
persistence of K2 as an independent physical contribution      REFUTED
R170_855 as a one-branch identity                               VALID
R170_855 as a surviving assembly of the full PC                INVALID
tails H and A_raw at finite cutoff                            PRESERVED
explicit ledger of P/Q routes                                   PROVED
cancellation of atoms in the combined port                      PROVED
simplified Tate coordinate, equation (8.6)                      PROVED
full polar ledger, equations (9.2)--(9.4)                       PROVED
sign of the boundary ledger                                      OPEN
exterior law / VIR--LB / D                                       OPEN
```
