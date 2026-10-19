# R170_899 — Finite assembly of the polar port

## 0. Result

Fix \(M<\infty\) and use the physical derivation

\[
 \dot\tau_{\log a}=-(\log a)\partial_t\tau_{\log a}.
\]

For a convolution operator \(B\), define

\[
 \mathcal G_B(N):=\dot B C_N-B\dot C_N.                 \tag{0.1}
\]

With

\[
 A_M=\mathcal M-L_M-L_M^*,
 \qquad
 \mathcal P_{C,A_M}=C_N\dot A_M-\dot C_NA_M,
\]

one has, on the common core,

\[
\boxed{
 \mathcal P_{C,A_M}(N)
 =\mathcal G_{\mathcal M}(N)
  -\mathcal G_{L_M}(N)-\mathcal G_{L_M^*}(N).}           \tag{0.2}
\]

Each block is a port at \(N=1\) plus an explicit integral. R170_893's
polar normalization law is thus equivalent to the vanishing of a
finite, fully typed sum; that vanishing is not proved here.

In the complex case, all scalars in this note are understood via their
real part.

## 1. Order and signs

The operators \(C_N,\dot C_N,\mathcal M,L_M,L_M^*\) are convolution
operators on the line and commute on the core. Hence

\[
 C_N\dot B-\dot C_NB=\dot BC_N-B\dot C_N=\mathcal G_B(N).
\]

Expanding \(A_M\) proves (0.2). No projection \(P_T\) has been commuted
through these operators.

## 2. Fundamental theorem on the cutoff

One has

\[
 d_NC_N=N^{-1/2}\tau_{\log N}\,dN,
\]

and \(d_N\dot C_N=\dot{(d_NC_N)}\). Hence, for any \(B\) independent
of \(N\),

\[
\boxed{
 \mathcal G_B(N)=\mathcal G_B(1)
 +\int_1^N\big[(\dot B)dC_x-B\,d\dot C_x\big].}         \tag{2.1}
\]

There is no atom at \(x=1\) in this integral: \(C_N\) is continuous in \(N\).
The base port is

\[
 \mathcal G_B(1)=\dot BC_1-B\dot C_1,                    \tag{2.2}
\]

with

\[
 C_1f(t)=e^{-t/2}\int_{-\infty}^{t}e^{u/2}f(u)du,
\]

\[
 \dot C_1f(t)=(1-t/2)C_1f(t)
 +e^{-t/2}\int_{-\infty}^{t}{u\over2}e^{u/2}f(u)du.     \tag{2.3}
\]

## 3. Gamma block

The physical conjugation gives

\[
 \dot{\mathcal M}=-D m'(D).
\]

By (2.1),

\[
 {d\over dx}\mathcal G_{\mathcal M}(x)
 =\mathcal J_\Gamma(x),                                  \tag{3.1}
\]

where

\[
\boxed{
 \mathcal J_\Gamma(x)
 =x^{-1/2}\tau_{\log x}
   [\dot{\mathcal M}+(\log x)\mathcal M\partial_t].}    \tag{3.2}
\]

This is the full Gamma block. It receives no sign from being a
real multiplier.

## 4. The two prime orientations

For

\[
 L_M=\sum_{r\le M}{\Lambda(r)\over\sqrt r}\tau_{\log r},
\]

the causal orientation is

\[
\boxed{
 \mathcal J_+(x):={d\over dx}\mathcal G_{L_M}(x)
 =\sum_{r\le M}{\Lambda(r)\log(x/r)\over\sqrt{rx}}
  \partial_t\tau_{\log(rx)}.}                            \tag{4.1}
\]

For the adjoint,

\[
 L_M^*=\sum_{r\le M}{\Lambda(r)\over\sqrt r}\tau_{-\log r},
 \qquad
 \dot\tau_{-\log r}=+(\log r)\partial_t\tau_{-\log r},
\]

and hence

\[
\boxed{
 \mathcal J_-(x):={d\over dx}\mathcal G_{L_M^*}(x)
 =\sum_{r\le M}{\Lambda(r)\log(xr)\over\sqrt{rx}}
  \partial_t\tau_{\log(x/r)}.}                            \tag{4.2}
\]

The adjoint orientation's factor is \(\log(xr)\), not
\(\log(x/r)\). Changing it would lose the sign of the jet of the
negative translation.

Combining (2.1)--(4.2),

\[
\boxed{
\begin{aligned}
 \mathcal P_{C,A_M}(N)={}&\mathcal P_{C,A_M}(1)\\
 &+\int_1^N
 [\mathcal J_\Gamma(x)-\mathcal J_+(x)-\mathcal J_-(x)]dx.
\end{aligned}}                                             \tag{4.3}
\]

It is convenient to name the combined port

\[
 \mathcal B_1:=\mathcal P_{C,A_M}(1)
 =\mathcal G_{\mathcal M}(1)
  -\mathcal G_{L_M}(1)-\mathcal G_{L_M^*}(1).             \tag{4.4}
\]

Although \(L_M^*\) is the adjoint of \(L_M\), in general
\(\mathcal G_{L_M^*}\ne\mathcal G_{L_M}^*\): the causal continuum
\(C_N\) is not self-adjoint. The two orientations of (4.1)--(4.2) must
remain separate.

## 5. Tate normalization

At a fixed parity, use the notation of R170_893--894:

\[
 g=\|b\|^2,\qquad h=(PS_N^*P)^{-1}b,\qquad PA_MF=\rho b.
\]

The adjoint jet of the comb is

\[
 \dot S_N^*=\sum_{2\le n\le N}{\log n\over\sqrt n}
                  \partial_t\tau_{-\log n}.              \tag{5.1}
\]

Define the normalization residue

\[
 \mathfrak R_{\rm pol}^{M,N}(F)
 :=\operatorname{Re}(h,P\mathcal P_{C,A_M}(N)F)
 -\rho\operatorname{Re}[(P\dot S_N^*Ph,b)-g].            \tag{5.2}
\]

R170_893(0.5) is exactly
\(\mathfrak R_{\rm pol}^{M,N}(F)=0\). Inserting (4.3) and (5.1) gives

\[
\boxed{
\begin{aligned}
 \mathfrak R_{\rm pol}^{M,N}(F)={}&
 \operatorname{Re}(h,P\mathcal B_1F)+\rho g\\
 &+\int_1^N
 \operatorname{Re}(h,P[\mathcal J_\Gamma(x)-\mathcal J_+(x)
                         -\mathcal J_-(x)]F)dx\\
 &-\rho\sum_{2\le n\le N}{\log n\over\sqrt n}
 \operatorname{Re}(P\partial_t\tau_{-\log n}Ph,b).
\end{aligned}}                                             \tag{5.3}
\]

This is the requested decomposition into a port at \(N=1\), a finite
integral, and discrete Tate normalization.

## 6. Comparison with the moments of R170_894

The literal identity

\[
 (h,P\mathcal P_{C,A_M}F)
 =(C_N^*h,\dot A_MF)-(\dot C_N^*h,A_MF)                   \tag{6.1}
\]

is the adjoint form of (0.2). Inserting
\(PA_MF=\rho b\), \(QA_MF=\ell\),
\(P\dot A_MF=u\), and \(Q\dot A_MF=v\), (6.1) reproduces

\[
 H_0\alpha(u)+\mathsf X_N(v)
 -\rho[(H_0-H_1/2)\alpha(b)+(H_0/2)\beta(b)]
 -\mathsf D_N(\ell),                                     \tag{6.2}
\]

which is the polar block of R170_894(3.2). Thus (5.3) introduces no new
hypothesis: it reorganizes exactly the same scalar before separating its
interior and exterior moments.

## 7. Tail and minimal residue

Identity (4.3) uses finite \(L_M\) and does not by itself create a
hyperbolic tail. If the integral is rewritten via the finite PC
identity, the products crossing the cutoffs produce the corresponding
tail and must be kept; no term-by-term limit with the
full prime comb is authorized.

The minimal residue is the right-hand side of (5.3). Its four types are:

1. base port at \(N=1\);
2. Gamma integral;
3. the two finite prime orientations;
4. discrete Tate normalization.

No identity used here annihilates these blocks individually. In
particular, PC can recombine them and exhibit \(\Lambda*1=\log\), but it does not
prove

\[
 \mathfrak R_{\rm pol}^{M,N}(F)=0.                       \tag{7.1}
\]

If the causal channel already present in the virial is isolated, what remains is
the typed residual

\[
\boxed{
 \mathfrak R_{\rm rem}^{M,N}(F)
 :=\operatorname{Re}(h,P[
      \mathcal G_{\mathcal M}(N)-\mathcal G_{L_M^*}(N)]F)
 -\rho\operatorname{Re}[(P\dot S_N^*Ph,b)-g].}           \tag{7.2}
\]

Indeed, with the notation of R170_843,

\[
 \mathcal A_{M,N}^{\rm ren}
 =\mathcal A_{M,N}^{\rm raw}-\mathcal G_{L_M}(N).         \tag{7.3}
\]

Hence \(\mathcal G_{L_M}\) is exactly the causal collar that
turns the raw Wronskian into the renormalized one. Equation (7.2)
contains what remains after isolating that channel: Gamma, the adjoint
orientation, and Tate normalization. It remains open; it is not an implicit
cancellation of (5.3).

Nor has exterior reciprocity, a differentiable branch of first contact,
or a sign for the moments of R170_894 been assumed.

```text
Gamma-primes-adjoint decomposition                           PROVED
fundamental theorem from N=1                                  PROVED
causal orientation log(x/r)                                    PROVED
adjoint orientation log(xr)                                     PROVED
equivalence with the moments of R170_894                        PROVED
finite residue (5.3)                                             EXPLICIT
vanishing or sign of the residue                                 OPEN
```
