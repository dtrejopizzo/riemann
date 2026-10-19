# R170_896 — Exact Möbius extraction of the cutoff measure

## 0. Identity, doubly reviewed

Let

\[
 K=\sum_{d\ge1}{\log d\over\sqrt d}\tau_{\log d},
 \quad
 M=\sum_{m\ge1}{\mu(m)\over\sqrt m}\tau_{\log m},
 \quad
 L=\sum_{r\ge1}{\Lambda(r)\over\sqrt r}\tau_{\log r}.
\]

In the local causal algebra,

\[
\boxed{K(d_NZ_N)M=L(d_NZ_N).}                            \tag{0.1}
\]

The identity extracts exactly `Lambda`; it corrects the composition
`L(dZ)M` of R170_895, which unnecessarily left `Lambda*mu`.

## 1. Proof fiber by fiber

The Dirichlet identity

\[
 \sum_{dm=r}\log d\,\mu(m)=\Lambda(r)                    \tag{1.1}
\]

gives `KM=MK=L`. All the factors of (0.1) are convolutions of
translations with the same orientation, so they may be associated before
inserting projections.

Using R170_895(1.2), the left-hand side is

\[
\begin{aligned}
 &\sum_{n,d,m}{\log d\,\mu(m)\over\sqrt{ndm}}
       \tau_{\log(ndm)}\delta_n\\
 &\qquad-
 \sum_{d,m}{\log d\,\mu(m)\over\sqrt{Ndm}}
       \tau_{\log(Ndm)}dN.
\end{aligned}                                             \tag{1.2}
\]

Grouping `r=dm` proves

\[
\boxed{
 \sum_{n,r}{\Lambda(r)\over\sqrt{nr}}
       \tau_{\log(nr)}\delta_n
 -\sum_r{\Lambda(r)\over\sqrt{Nr}}
       \tau_{\log(Nr)}dN.}                               \tag{1.3}
\]

This is exactly the expansion of `L(d_NZ_N)`.

For adjoints, the correct order is

\[
 [K(d_NZ_N)M]^*=M^*(d_NZ_N)^*K^*
 =(d_NZ_N)^*L^*.                                         \tag{1.4}
\]

## 2. Domain and projections

The proof holds on a compact/distributional core where the causal sums
are locally finite. It does not claim that the combs are globally bounded
operators. It also does not authorize inserting `P` or `Q` between `K`, `dZ`, and `M`; that
insertion would break the convolution producing (1.1).

## 3. Comparison with the virial

Identity (0.1) has logarithmic degree zero. On the fiber composed of
the birth `n` and the prime factor `r`, it carries weight

\[
 \Lambda(r)\tau_{\log(nr)}.                              \tag{3.1}
\]

The corresponding dilation Wronskian carries, by orientation,

\[
 -\Lambda(r)\log(r/n)\,
       \partial_t\tau_{\log(nr)}.                        \tag{3.2}
\]

Hence the relative factor `log(r/n)` and the spatial derivative are
missing. They are not a normalization constant.

Under `N=e^(2T)`, the continuous part of (1.3) is

\[
 -2\sqrt N\sum_r{\Lambda(r)\over\sqrt r}
       \tau_{\log(Nr)}dT.                                \tag{3.3}

The degree-one polar collar instead contains
`log(N/r) partial_t tau_(log(Nr))`, together with amplitude and the moving
face.

## 4. Consequence

The degree-zero arithmetic is closed exactly. The next operation
must not repeat Möbius nor Selberg: it must apply the antidiagonal
derivation to (0.1), with the full Leibniz rule for `K`, `dZ`, and `M`. Only that
lift can produce the relative weight of (3.2).

```text
K(dZ)M=L(dZ)                                                PROVED
exact extraction of Lambda                                   PROVED
order of adjoints                                              PROVED
Lambda*mu reading of R895                                       CORRECTED
match with the degree-one virial channel                        FALSE
antidiagonal lift of the measure                                 OPEN
VIR--LB / D                                                      OPEN
```
