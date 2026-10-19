# R170_897 — Antidiagonal lift of the cutoff measure

## 0. Theorem, doubly reviewed

The degree-zero identity R170_896 admits a lift that produces
exactly the degree-one prime virial coefficient.

Let `delta` be the scale derivation at fixed cutoff,

\[
 \delta\tau_{\log a}
 =\log a\,\partial_t\tau_{\log a},                       \tag{0.1}
\]

with the Leibniz rule, and set `E=d_NZ_N`. Then

\[
\boxed{
 \mathfrak W_{\rm ad}(E)
 :=(\delta L)E-L(\delta E)
 =(\delta K)EM+KE(\delta M)-K(\delta E)M.}               \tag{0.2}
\]

On the atomic part,

\[
\boxed{
 \mathfrak W_{\rm ad}^{\rm at}(E)
 =\sum_{n,r}{\Lambda(r)\log(r/n)\over\sqrt{nr}}
 \partial_t\tau_{\log(nr)}\,\delta_n.}                 \tag{0.3}
\]

With the corpus's opposite convention for the scale point, the whole
formula picks up the corresponding overall sign.

## 1. Full Leibniz rule

Differentiating `KM=L` gives

\[
 \delta L=(\delta K)M+K(\delta M).                       \tag{1.1}
\]

Since the causal convolutions commute on the core before inserting
projections,

\[
 (\delta L)E-L\delta E
 =(\delta K)EM+KE\delta M-K\delta E M,                   \tag{1.2}
\]

which is (0.2). The term `KE delta M` is mandatory.

Equivalently,

\[
 \mathfrak W_{\rm ad}(E)
 =\delta(KEM)-2K(\delta E)M,                             \tag{1.3}
\]

the antidiagonal form of the derived identity
`delta(KEM)=delta(LE)`.

## 2. Extraction of the relative weight

One has

\[
 \delta K=\sum_d{(\log d)^2\over\sqrt d}
       \partial_t\tau_{\log d},
\]

\[
 \delta M=\sum_m{\mu(m)\log m\over\sqrt m}
       \partial_t\tau_{\log m}.                          \tag{2.1}
\]

On the fiber `r=dm`, the first two terms of (0.2) contribute

\[
\begin{aligned}
 &\sum_{dm=r}\mu(m)\big[(\log d)^2+\log d\log m\big]\\
 &\qquad=\log r\sum_{dm=r}\log d\,\mu(m)
 =\Lambda(r)\log r.                                     \tag{2.2}
\end{aligned}

The third term contributes `-Lambda(r)log n` at the birth atom
`n`. This proves (0.3).

## 3. The Möbius connection

From `SM=I`,

\[
 (\delta S)M+S\delta M=0,
 \qquad
 \delta M=-M(\delta S)M.                                \tag{3.1}
\]

Since `delta S=partial_t K`, the Möbius connection does not vanish: it completes
the term `(log d)^2 mu(m)` up to `Lambda(r)log r`. Omitting it would destroy
the exact virial coefficient.

## 4. Continuous part

For

\[
 E_{\rm cont}=-N^{-1/2}\tau_{\log N}dN,
\]

the derivation intrinsic to a fixed cutoff is

\[
 \delta E_{\rm cont}
 =-N^{-1/2}\log N\,
   \partial_t\tau_{\log N}dN.                            \tag{4.1}
\]

Then

\[
\boxed{
 \mathfrak W_{\rm ad}^{\rm cont}
 =\sum_r{\Lambda(r)\log(N/r)\over\sqrt{Nr}}
       \partial_t\tau_{\log(Nr)}dN.}                    \tag{4.2}
\]

Under `N=e^(2T)`, this becomes

\[
 2\sqrt N\sum_r{\Lambda(r)\log(N/r)\over\sqrt r}
       \partial_t\tau_{\log(Nr)}dT.                     \tag{4.3}
\]

This is, with the corresponding global orientation, the derivative fiber
of the collar `dot L C-L dot C`.

## 5. Separating the two derivations

The derivation `delta` is the opposite of the corpus's physical virial
derivation on the translation algebra. It is not the derivative of the curve
`N=e^(2T)`. R170_898 proves that `delta` commutes with `d_N` and that the
weight, moment, and face terms of `dot C_N` appear when integrating in
`N`, with a nonzero initial port `dot C_1`; they must not be added as a
second `Gamma_cut` to the frozen Wronskian.

If, in addition, a moving curve `T -> (P_T,N(T),h_T,F_T)` is chosen, its
derivative does contain `dot P_T`, `D_T h_T`, traces, and the Jacobian `dN/dT`. That is
the vector connection of R170_895 and is a different operation. Adding
both directions requires explicitly declaring the two-parameter
curve; otherwise the continuous face is duplicated.

The present lift closes the degree-one arithmetic coefficient. The rigorous
integrated law is formulated first with finite `L_M`, as in
R170_898; the full comb `L` has a domain obstruction at the port `N=1`.

```text
antidiagonal Leibniz rule (0.2)                              PROVED
contribution of delta M                                        NECESSARY AND PROVED
coefficient Lambda(r)log(r/n)                                   PROVED
continuous part log(N/r)                                        PROVED
degree-one prime virial channel                                 CLOSED ALGEBRAICALLY
finite integration and the port N=1                              R170_898
Gamma/adjoint/tail/Tate assembly                                 OPEN
VIR--LB / D                                                      OPEN
```
