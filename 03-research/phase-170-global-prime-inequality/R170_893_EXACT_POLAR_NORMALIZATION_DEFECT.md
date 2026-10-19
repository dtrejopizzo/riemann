# R170_893 — Exact polar normalization defect

## 0. Doubly audited identity

The pending identification between the Euler--Maclaurin anchor and the
total Tate defect reduces, for the frozen jet, to a single scalar polar
law.

Use exactly the conventions of R170_856:

\[
 \dot b^0=P\dot S_N^*Ph,\qquad
 \dot q^0=Q\dot S_N^*Ph,\qquad
 \dot z^0=Q\dot A_MF-\rho\dot q^0,                       \tag{0.1}
\]

\[
 \mathfrak W_{\rm ext}=(\dot q^0,z)-(q,\dot z^0),
 \qquad g=\|b\|^2.                                      \tag{0.2}
\]

Define

\[
 \Omega_{\rm EM}:=\mathfrak W_{\rm ext}
 +(h,P\mathcal P_{C,A_M}F).                              \tag{0.3}
\]

Then

\[
\boxed{
 g\Delta^{\rm Tate}-\Omega_{\rm EM}
 =\rho[(\dot b^0,b)-g]-(h,P\mathcal P_{C,A_M}F).}         \tag{0.4}
\]

Consequently,

\[
\boxed{
 \Omega_{\rm EM}=g\Delta^{\rm Tate}
 \Longleftrightarrow
 (h,P\mathcal P_{C,A_M}F)
 =\rho[(\dot b^0,b)-g].}                                 \tag{0.5}
\]

The right-hand equation is the remaining **polar normalization law**.

## 1. Proof

R170_856(8.4) gives

\[
 g\omega^{\rm comb}=\rho(\dot b^0,b)+\mathfrak W_{\rm ext}.
                                                                    \tag{1.1}
\]

Since `Delta^Tate=omega^comb-rho`,

\[
 g\Delta^{\rm Tate}
 =\mathfrak W_{\rm ext}+\rho[(\dot b^0,b)-g].             \tag{1.2}
\]

Subtracting (0.3) proves (0.4), and (0.5) is immediate. No
minimality, sign, or exterior reciprocity is used.

## 2. Literal expansion of the polar scalar

By R170_856(9.2), with `ell=QA_MF` and `PA_MF=rho b`,

\[
\boxed{
\begin{aligned}
 (h,P\mathcal P_{C,A_M}F)={}&
 (h,PC_NP\dot A_MF)+(h,PC_NQ\dot A_MF)\\
 &-\rho(h,P\dot C_Nb)-(h,P\dot C_N\ell).
\end{aligned}}                                           \tag{2.1}
\]

This formula keeps the exterior route `PC_NQ dot A_MF` and the coupling
`P dot C_N ell`; discarding them would turn (0.5) into a false identity.

The signs also agree with R170_885:

\[
 \Omega_{\rm EM}
 =W(QZ_N^*h,\ell)-W(PC_N^*h,\rho b).                     \tag{2.2}
\]

## 3. Covariant scope

Equations (0.4)--(2.2) use the frozen jets `^0`. If the branch, `h`, or
`rho` are differentiated, the connections of R170_887 must be added. The
total covariant law is obtained by adding those same terms to both
sides; reinterpreting the dots of (0.1) as total derivatives is not authorized.

In the complex case, real parts are taken. If `rho` is not zero, (0.5)
can be divided by `rho`; the undivided form remains valid and
keeps the case `rho=0`.

## 4. Consequence for the KKT

R170_892 showed that the physical residue is `sigma Delta`. Using (0.4),

\[
\boxed{
 \sigma\Delta^{\rm Tate}
 ={\sigma\over g}\left[
 \Omega_{\rm EM}
 +\rho((\dot b^0,b)-g)
 -(h,P\mathcal P_{C,A_M}F)\right].}                      \tag{4.1}
\]

This is the correctly typed version of the Tate virtual work. KKT
does not sign the three summands separately. To reduce it to
`sigma Omega_EM/g` one must prove exactly (0.5).

## 5. Status

```text
difference g Delta - Omega_EM                                PROVED
full expansion of the polar scalar                             PROVED
identification Omega_EM=g Delta                                EQUIVALENT TO (0.5)
polar normalization law (0.5)                                   OPEN
total version with connections                                   FORMULATED, NOT SHOWN TO VANISH
correctly typed virtual work, (4.1)                               PROVED
VIR--LB / D                                                       OPEN
```
