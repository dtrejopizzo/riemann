# R170_900 — PC--Tate collision audit

## 0. Verdict

The identity

\[
\boxed{
 \mathcal G_{\mathcal M}(C_N)-\mathcal G_{L_M^*}(C_N)
 =\mathcal C_{\rm PC}+\mathcal A^{\rm raw}
  -\mathcal G_{A_M+L_M}(Z_N)}                              \tag{0.1}
\]

is correct. Here

\[
 \mathcal G_B(Y)=\dot BY-B\dot Y,\qquad
 Z_N=S_N-C_N,\qquad
 \mathcal C_{\rm PC}=S_N\dot A_M-\dot S_NA_M.
\]

It was checked two ways: by expanding
\(\mathcal M-L_M^*=A_M+L_M\), and by substituting
\(C_N=S_N-Z_N\). However, (0.1) is an exact recombination of the
R170_853 and R170_856 ledgers; it does not reduce the remaining logical
obligation.

## 1. Full PC form

Set

\[
 \mathcal D_{\rm PC}:=\mathcal C_{\rm PC}+\mathcal A^{\rm raw}.
\]

R170_856 gives

\[
\begin{aligned}
 \mathcal D_{\rm PC}={}&S_N\dot{\mathcal M}-\dot S_N\mathcal M\\
 &-\dot L_M^*E_N\mathscr F-L_M^*E_{N,-}\mathscr F
   -L_M^*E_N\dot{\mathscr F}\\
 &-J\mathcal A^{\rm raw}\mathscr F
   -JK_N\dot{\mathscr F}-JH_{M,N}\dot{\mathscr F}.       \tag{1.1}
\end{aligned}
\]

Hence the residual of R170_899(7.2) is exactly

\[
\boxed{
\begin{aligned}
 \mathfrak R_{\rm rem}={}&
 \operatorname{Re}(h,P[
   \mathcal D_{\rm PC}-\mathcal G_{A_M+L_M}(Z_N)]F)\\
 &-\rho\operatorname{Re}[(P\dot S_N^*Ph,b)-g].           \tag{1.2}
\end{aligned}}
\]

This is the remaining object. The formula literally keeps

\[
 H_{M,N}=\sum_{N<k\le MN}{h_{M,N}(k)\over\sqrt k}
             \tau_{\log k},                               \tag{1.3}
\]

the parts \(k>N\) of \(\mathcal A^{\rm raw}\), the Poisson defect,
the Fourier jet, and, after compression, every exterior route of
R170_856(5.4), including \(-PJH_{M,N}Q\dot{\mathscr F}P\).

## 2. Collision with the Tate coordinate

Use

\[
 S_N^*Ph=b+q,\qquad A_MF=\rho b+\ell,\qquad
 \dot b^0=P\dot S_N^*Ph,\quad
 \dot q^0=Q\dot S_N^*Ph.
\]

Then

\[
\begin{aligned}
 \operatorname{Re}(h,P\mathcal C_{\rm PC}F)
 ={}&\operatorname{Re}(b,P\dot A_MF)
    +\operatorname{Re}(q,Q\dot A_MF)\\
 &-\rho\operatorname{Re}(\dot b^0,b)
  -\operatorname{Re}(\dot q^0,\ell).                     \tag{2.1}
\end{aligned}
\]

Adding the Tate normalization of (1.2) gives

\[
\boxed{
\begin{aligned}
 \mathfrak R_{\rm rem}={}&
 \operatorname{Re}(b,P\dot A_MF)
 +\operatorname{Re}(q,Q\dot A_MF)\\
 &-2\rho\operatorname{Re}(\dot b^0,b)
 -\operatorname{Re}(\dot q^0,\ell)\\
 &+\operatorname{Re}(h,P[
   \mathcal A^{\rm raw}-\mathcal G_{A_M+L_M}(Z_N)]F)
 +\rho g.                                                 \tag{2.2}
\end{aligned}}
\]

The factor \(2\) is mandatory: one copy comes from
\(\mathcal C_{\rm PC}\) and the other from the Tate normalization. Removing one
copy would require a tangency law relating the variation of the
contact vector to \(\dot b^0\). No such tangency has been proved.
Hence it remains forbidden to cancel it by invoking minimality, by differentiating
a branch of vectors that has not been constructed, or by identifying the
frozen jet with a total derivative.

## 3. Scope

Forms (1.2) and (2.2) are equivalent. The first exhibits PC, tails, and
exterior ports; the second exhibits the exact collision with Tate. Neither
produces a new sign or cancellation. The pending step remains an
additional law orienting the full object of (1.2), preserving
\(H_{M,N}\), both orientations, Gamma, Fourier, and the support
crossings.

```text
operator identity (0.1)                                      PROVED
equivalence with R170_853/R170_856                             PROVED
new logical reduction                                           NO
tails and exterior ports                                        PRESERVED
Tate factor 2                                                    MANDATORY
tangency that would cancel it                                     NOT PROVED
sign or vanishing of (1.2)                                        OPEN
```
