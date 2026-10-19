# R170_859 — Gauge-invariant exterior connection defect

## 0. Result

R170_857--858 fixed a `C1` identification of the primitive spaces
and isolated the sandwich

\[
 \mathfrak S_{\rm RW}(f)=(Q_K\eta,RCf),\qquad
 C=Q_K\dot HZ.                                             \tag{0.1}
\]

That scalar is not intrinsic. An infinitesimal change of trivialization
can annihilate `C` completely. However, the same change modifies the
exterior connection `chi_f` by exactly the amount needed so that

\[
 \boxed{
 \Theta_{\rm ext}(f):=(q,\chi_f)-\mathfrak S_{\rm RW}(f)}   \tag{0.2}
\]

remains invariant.

Therefore the canonical reduction of the Tate defect is

\[
 \boxed{g\Delta^{\rm Tate}=\mathfrak W_K(f)+Theta_{\rm ext}(f).}
                                                                    \tag{0.3}
\]

The missing law no longer needs to assign a sign to the transverse block `C`: that
block can be erased by gauge. It must prove the scalar identity

\[
 \boxed{\mathfrak W_K(f)+\Theta_{\rm ext}(f)=0.}            \tag{0.4}
\]

This is a stricter reduction than RES--WARD in a fixed gauge and
avoids confusing a Kato coordinate with arithmetic information.

## 1. Change of trivialization

Work under REG/C1 and the conventions of R170_857. Let

\[
 H=H_0\ge0,\quad Z=1_{\{0\}}(H),\quad Q_K=I-Z,quad
 R=Q_K(H|_{Q_K\mathfrak P})^{-1}Q_K.                       \tag{1.1}
\]

Consider another trivialization of the same primitive bundle,

\[
 U_s=I+sK+o(s),\qquad K^*=-K,                              \tag{1.2}
\]

and simultaneously transform

\[
 \widetilde H_s=U_s^*H_sU_s,\qquad
 \widetilde{\mathscr L}_s=\mathscr L_sU_s.                 \tag{1.3}
\]

At `s=0`, `H,Z,Q_K,R,mathscr L_0,q,eta=mathscr L_0^*q` do not
change. Their speeds do change:

\[
 \boxed{\widetilde V=V+HK-KH,\qquad V=\dot H.}             \tag{1.4}
\]

Since `HZ=0`, the transverse component satisfies

\[
 \boxed{\widetilde C=C+Q_KHKZ.}                            \tag{1.5}
\]

Applying the reduced resolvent gives

\[
 \boxed{R\widetilde C=RC+Q_KKZ,}                           \tag{1.6}
\]

because `RH=Q_K` on the spectral complement.

## 2. Transformation of the sandwich and of the connection

For `f in Z`, (1.6) implies

\[
\begin{aligned}
 \widetilde{\mathfrak S}_{\rm RW}(f)
 &= (Q_K\eta,R\widetilde Cf)\\
 &=\mathfrak S_{\rm RW}(f)+(Q_K\eta,Q_KKf).
                                                               \tag{2.1}
\end{aligned}
\]

On the other hand,

\[
 \dot{\widetilde{\mathscr L}}_0
 =\dot{\mathscr L}_0+\mathscr L_0K.                        \tag{2.2}
\]

The exterior connection of R170_857(4.3) then transforms as

\[
 \widetilde\chi_f=\chi_f+\mathscr L_0Kf.                  \tag{2.3}
\]

Using `eta=mathscr L_0^*q`,

\[
 \boxed{(q,\widetilde\chi_f)
 =(q,\chi_f)+(\eta,Kf).}                                   \tag{2.4}

Since `eta-Zeta=Q_Keta` and only the component `Q_KKf` appears in
(2.1), the internal gauge of the radical must also be fixed. For the
horizontal lift used in R170_857, it is required that

\[
 ZKZ=0.                                                     \tag{2.5}

Then `(eta,Kf)=(Q_Keta,Q_KKf)` and (2.1)--(2.4) prove

\[
 \boxed{
 (q,\widetilde\chi_f)-\widetilde{\mathfrak S}_{\rm RW}(f)
 =(q,\chi_f)-\mathfrak S_{\rm RW}(f).}                     \tag{2.6}
\]

The horizontal exterior jet of R170_857 is also invariant. Indeed,

\[
 \dot\ell^K=\dot\ell^0+\chi_f-\mathscr L_0RCf,             \tag{2.7}
\]

and under (1.6), (2.3) and (2.5) the two increments
`+mathscr L_0Kf` and `-mathscr L_0Q_KKf` cancel. Consequently
`mathfrak W_K(f)` does not change and (0.3) is an equality between
intrinsic quantities.

If `ZKZ ne 0` is allowed, the additional term is exactly the
radical rotation `(Zeta,alpha_f)` of R170_857(5.3); the complete
combination of that equation remains invariant. Therefore (2.6) does not
hide an arithmetic hypothesis: it is the horizontal version of the
general law.

## 3. Gauge that annihilates the transverse block

The block `C:Zmathfrak P to Q_Kmathfrak P` can be eliminated. Define
the anti-self-adjoint block operator

\[
 K_C=
 \begin{pmatrix}
 0&(RC)^*\\
 -RC&0
 \end{pmatrix}_{Z\oplus Q_K}.                              \tag{3.1}
\]

Then `K_C^*=-K_C`, `ZK_CZ=0` and

\[
 Q_KK_CZ=-RC.                                              \tag{3.2}
\]

By (1.6),

\[
 \boxed{R\widetilde C=0,\qquad \widetilde C=0.}           \tag{3.3}

In this Kato gauge,

\[
 \widetilde{\mathfrak S}_{\rm RW}(f)=0,\qquad
 \Theta_{\rm ext}(f)=(q,\widetilde\chi_f).                \tag{3.4}

Thus the resolvent sandwich is not an independent obstruction: it is
the part of the connection that a non-horizontal gauge assigns to the spectral
leak. The intrinsic obstacle is `Theta_ext`.

## 4. PC form of the invariant connection

In the original gauge of R170_858, its equation (3.4) gives

\[
\begin{aligned}
 \Theta_{\rm ext}(f)
 ={}&(q,\chi_f)
 -(B_\mu^*Y,P\mathcal C_{PC}f)\\
 &-(Y,\mathcal P^{\rm comb}(f))
 -\mathfrak T_{\rm conn}(Y,f),                            \tag{4.1}
\end{aligned}
\]

with `Y=RQ_Keta`. Although the four terms depend on the gauge, their
sum does not. R170_856 expands `C_PC` preserving `Lambda`, Mobius, the
hyperbolic tail, the reflection, the pole and Tate.

In the `K_C` gauge, the first, second and third response terms
are absorbed into the new connection and (4.1) reduces to (3.4). This shows
that attempting to sign the first line of (4.1) separately cannot be
intrinsic.

## 5. Class of scalar connection

The situation can be expressed without choosing a gauge. The datum `(C,chi)` has
the transformation

\[
 (C,\chi_f)\longmapsto
 (C+Q_KHKZ,\;\chi_f+\mathscr L_0Kf).                       \tag{5.1}

The functional

\[
 [(C,\chi)]\longmapsto
 (q,\chi_f)-(Q_K\eta,RCf)                                 \tag{5.2}

descends to the quotient by (5.1). Since `H` is invertible on `Q_K`, the
vector class of `C` in that quotient is trivial; a single scalar connection
defect remains, `Theta_ext(f)`.

By (0.3), the sought exterior law is exactly the cancellation between
two intrinsic scalars:

1. the geometric Wronskian of the branch, `mathfrak W_K(f)`;
2. the arithmetic--Tate connection defect, `Theta_ext(f)`.

This formulation prevents a new repetition of W12: a chain of
resolvents that only changes the gauge does not alter (0.4).

## 6. Consequences for the next construction

A valid new piece must simultaneously:

* be formulated for `Theta_ext`, not for `C` or `S_RW` separately;
* preserve the ports of R170_856, because they form the connection of
  (4.1);
* use `Lambda*1=log` after forming the invariant combination, not inside a
  PC branch that is later cancelled;
* distinguish a first window from a positive window, since the
  gauge identity holds in both.

A possible continuation would be to construct a curvature around the
two-parameter rectangle `(Euler scale, integer comb scale)`.
R170_860 audits this possibility: with the current families the second
parameter does not define a spectral bundle, and the scalar rectangle is an
exact identity with no content. Therefore `Theta_ext` should not be called
holonomy until a second non-trivial connection is constructed.

## 7. Status

```text
gauge transformation of V and C, (1.4)--(1.6)             PROVED
transformation of chi and the sandwich, (2.1)--(2.4)      PROVED
invariance of Theta_ext                                   PROVED
Kato gauge annihilating C                                 CONSTRUCTED
sandwich S_RW as intrinsic residue                        REFUTED
scalar defect Theta_ext as intrinsic residue              PROVED
Delta_Tate=(W_K+Theta_ext)/g                              PROVED
intrinsic identity (0.4)                                  OPEN
VIR--LB / D                                               OPEN
```
