# R170_898 — Finite integrated law of the cutoff Wronskian

## 0. Theorem

The corpus's virial derivation commutes with the Stieltjes differential
of the cutoff. This integrates the antidiagonal lift of R170_897 without
introducing an artificial diagonal connection between scale and window.

Fix

\[
 L_M=\sum_{r\le M}{\Lambda(r)\over\sqrt r}\tau_{\log r},
 \qquad Z_N=S_N-C_N,                                    \tag{0.1}
\]

and use the physical convention

\[
 \dot B={d\over ds}(U_s^{-1}BU_s)|_{s=1},
 \qquad \dot\tau_{\log a}=-(\log a)\partial_t\tau_{\log a}. \tag{0.2}
\]

Then

\[
 \mathcal W_{M,N}:=\dot L_MZ_N-L_M\dot Z_N              \tag{0.3}
\]

satisfies, as an identity of operator measures,

\[
 \boxed{d_N\mathcal W_{M,N}=\mathcal I_{M,N},}           \tag{0.4}
\]

where

\[
\boxed{
\begin{aligned}
 \mathcal I_{M,N}^{\rm at}
 &=\sum_{n\ge1}\sum_{r\le M}
 {\Lambda(r)\log(n/r)\over\sqrt{nr}}
 \partial_t\tau_{\log(nr)}\,\delta_n,\\
 \mathcal I_{M,N}^{\rm cont}
 &=\sum_{r\le M}{\Lambda(r)\log(r/N)\over\sqrt{Nr}}
 \partial_t\tau_{\log(Nr)}\,dN .
\end{aligned}}                                           \tag{0.5}
\]

With \(S_1=I\), the rigorous integrated law is

\[
\boxed{
 \mathcal W_{M,N}=\mathcal W_{M,1}
 +\int_{(1,N]}\mathcal I_{M,x},
 \quad
 \mathcal W_{M,1}=\dot L_M(I-C_1)+L_M\dot C_1.}         \tag{0.6}
\]

Equivalently, for the left limit
\(Z_{1^-}=-C_1\),

\[
\boxed{
 \mathcal W_{M,N}=-(\dot L_MC_1-L_M\dot C_1)
 +\int_{[1,N]}\mathcal I_{M,x}.}                         \tag{0.7}
\]

The atom \(n=1\) is included in (0.7) and excluded in (0.6).

## 1. Proof

Conjugation by \(U_s\) does not depend on \(N\). Hence

\[
 d_N\dot Z_N=\dot{(d_NZ_N)}                              \tag{1.1}
\]

in the sense of operator distributions. Since \(L_M\) is finite and
independent of \(N\),

\[
 d_N\mathcal W_{M,N}
 =\dot L_Md_NZ_N-L_M\dot{(d_NZ_N)}.                      \tag{1.2}
\]

On the atom
\(n^{-1/2}\tau_{\log n}\delta_n\), the coefficient of the fiber
\((n,r)\) is

\[
 {-\Lambda(r)\log r+\Lambda(r)\log n\over\sqrt{nr}}
 = {\Lambda(r)\log(n/r)\over\sqrt{nr}}.                 \tag{1.3}
\]

On the continuous part
\(-N^{-1/2}\tau_{\log N}dN\), the same rule gives

\[
 {\Lambda(r)\log(r/N)\over\sqrt{Nr}},                   \tag{1.4}
\]

which proves (0.4)--(0.5). Integrating the measure proves
(0.6)--(0.7). In particular,

\[
 \mathcal W_{M,1}-\mathcal W_{M,1^-}=\dot L_M,           \tag{1.5}
\]

and this is exactly the atom \(n=1\) of (0.5).

The positive form of R170_897 uses
\(\delta\tau_{\log a}=+(\log a)\partial_t\tau_{\log a}\).
Hence (0.5) is its global opposite, as required by
\(\dot{}=-\delta\) in the translation algebra.

## 2. Initial port and polar face

The initial causal port is

\[
 C_1f(t)=e^{-t/2}\int_{-\infty}^{t}e^{u/2}f(u)\,du,      \tag{2.1}
\]

and

\[
\boxed{
 \dot C_1f(t)=(1-t/2)C_1f(t)
 +{e^{-t/2}\over2}\int_{-\infty}^{t}u e^{u/2}f(u)\,du.} \tag{2.2}
\]

Moreover,

\[
 d_N\dot C_N
 =-{\log N\over\sqrt N}\partial_t\tau_{\log N}\,dN,   \tag{2.3}
\]

so that

\[
 \dot C_N=\dot C_1-
 \int_1^N{\log x\over\sqrt x}
 \partial_t\tau_{\log x}\,dx.                           \tag{2.4}
\]

Integrating by parts reproduces

\[
\begin{aligned}
 \dot C_Nf(t)={}&(1-t/2)C_Nf(t)
 +e^{-t/2}\int_{-\infty}^{t+\log N}{u\over2}e^{u/2}f(u)\,du\\
 &-(\log N)\sqrt N f(t+\log N).                          \tag{2.5}
\end{aligned}
\]

Thus the weight terms and the face of \(\dot C_N\) are the
integrated form of (2.3), with initial condition (2.2); they do not
constitute a second cutoff connection.

## 3. Domain and uniformity

The finiteness of \(L_M\) makes all the products of (0.3)--(0.7) well
defined on the core used in Paper 46. The naive limit
\(M\to\infty\) is not claimed here: \(C_Nf\) has an exponential tail and
terms such as \(LC_Nf\) may contain the divergent series
\(\sum_r\Lambda(r)/r\) and \(\sum_r\Lambda(r)\log r/r\).

For each \(M\), (0.6) holds simultaneously for all \(N\ge1\). The uniformity
is algebraic: it does not depend on a margin estimate.

## 4. Exact port towards R170_894

For an exterior vector \(v\), the two coordinates of R170_894 satisfy

\[
 \mathsf X_N(v)=(h,PC_1v)
 +\int_1^Nx^{-1/2}(h,P\tau_{\log x}v)\,dx,                \tag{4.1}
\]

\[
 \mathsf D_N(v)=(h,P\dot C_1v)
 -\int_1^N{\log x\over\sqrt x}
 (h,P\partial_t\tau_{\log x}v)\,dx.                     \tag{4.2}
\]

These formulas exactly replace the two truncated exterior data
by ports at \(N=1\) and integrals over the same cutoff of (0.5).

They do not by themselves identify all of \(\mathfrak R_{\rm pol}\) with
\(\mathcal W_{M,N}\). For
\(A_M=\mathcal M-L_M-L_M^*\), the Gamma channel, the adjoint
orientation, the Tate normalization, and the exterior routes must still be
assembled. If \(T\) is also moved, the connections of
\(P_T,h_T,F_T\) appear separately; they do not belong to the frozen jet of (0.3).

## 5. Double neutral audit

The first audit reconstructed (0.4) from the commutation (1.1) and
verified the conventions \((1,N]\) and \([1,N]\). The second reconstructed
the arithmetic fibers, the adjoint, and the continuum; it confirmed the
finite law and detected the domain obstruction preventing replacement of
\(L_M\) by the infinite comb without renormalization. Neither audit
presupposed a defect.

```text
commutation of d_N with the virial derivation                PROVED
finite integrated law (0.6)/(0.7)                              PROVED
coefficients Lambda(r) log(n/r)                                PROVED
initial port C_1, dot C_1                                       EXPLICIT
moving face counted exactly once                                PROVED
exact substitution of X_N and D_N                                PROVED
naive passage to the infinite prime comb                         NOT JUSTIFIED
Gamma/adjoint/tail/Tate assembly                                  OPEN
sign via minimality / VIR--LB / D                                 OPEN
```
