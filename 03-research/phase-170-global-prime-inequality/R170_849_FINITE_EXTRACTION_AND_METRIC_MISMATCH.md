# R170_849 — Finite causal extraction and clash between the physical metric and the Hankel metric

> **Update R170_850.** The physical metric `B_N,T` does not remain
> abstract: for `N>=e^(2T)` it is exactly the compression of the
> Möbius comb. When composed with the Wronskian, its coefficients are
> `gamma=mu*beta_Lambda`, which R170_850 computes completely. The metric
> defect thus reduces to an explicit channel supported on integers with
> one or two distinct prime bases.

## 0. Result

The extraction gate isolated in R170_848 can be solved exactly in the
physical window. The compressed operator `P_T S_N P_T` is
unitriangular and has a finite inverse. This allows solving for the
physical jet `P_T dot A_M F` from the curvature

\[
 \mathcal C_{M,N}:=S_N\dot A_M-\dot S_NA_M.
\]

However, the extraction changes the test vector. The Wronskian sign
from R170_843 holds in the Hankel metric, while the exact extraction
requires the dual metric of `(P S P)^{-1}`. There is no identity in the
corpus identifying the two. This is the new precise defect.

## 1. Finite causal inverse

Let `P=P_T` and write

\[
 P S_NP=P+R_{N,T},
 \qquad
 R_{N,T}=\sum_{2\le n\le N}n^{-1/2}P\tau_{\log n}P.
 \tag{1.1}
\]

Each non-identity factor shifts by at least `log 2`. A composition of
`j` factors shifts by at least `j log 2`; hence

\[
 R_{N,T}^{J_T}=0,
 \qquad
 J_T:=\left\lfloor{2T\over\log2}\right\rfloor+1.
 \tag{1.2}
\]

Consequently,

\[
 \boxed{
 B_{N,T}:=(PS_NP)^{-1}ig|_{PL^2}
 =\sum_{j=0}^{J_T-1}(-R_{N,T})^j.}
 \tag{1.3}
\]

No convergent series is used, nor PNT, nor an inverse of the Weil
operator. The formula is finite for each `T` and valid simultaneously for
every `N`; when `N>=e^(2T)`, the compressed operator has already
stabilized.

## 2. Exact extraction formula

For `F` supported in the window, decompose before applying `S_N`:

\[
\begin{aligned}
 P\mathcal C_{M,N}F
 ={}&PS_NP\dot A_MF+PS_NQ\dot A_MF\\
   &-P\dot S_NP A_MF-P\dot S_NQ A_MF,
 \qquad Q=I-P.
\end{aligned}
 \tag{2.1}
\]

Applying (1.3) gives

\[
\boxed{
\begin{aligned}
 P\dot A_MF={}&B_{N,T}P\mathcal C_{M,N}F
 +B_{N,T}P\dot S_NP A_MF\\
 &+B_{N,T}P\dot S_NQ A_MF
 -B_{N,T}PS_NQ\dot A_MF.
\end{aligned}}
 \tag{2.2}
\]

At first contact `PA_MF=r_F` for `M>=e^(2T)`, with the regularity and
truncation convention of Paper 47. Thus the second term of (2.2) is
an explicit Tate port; the last two are the outer concomitants
that could not be omitted in R161_057--065.

Pairing with `F` gives

\[
\begin{aligned}
 \langle F,P\dot A_MF\rangle
={}&\langle B_{N,T}^*F,P\mathcal C_{M,N}F\rangle\\
 &+\langle B_{N,T}^*F,P\dot S_Nr_F\rangle\\
 &+\langle B_{N,T}^*F,P\dot S_NQ A_MF\rangle\\
 &-\langle B_{N,T}^*F,PS_NQ\dot A_MF\rangle.
\end{aligned}
 \tag{2.3}
\]

The left-hand side, together with the `dot Pi_T` connection from
R170_845, is the negative of the full virial. Hence (2.3) algebraically
resolves the extraction left open by R170_848.

## 3. Why (2.3) still does not carry the Wronskian sign

The arithmetic block of `mathcal C` contains `-mathcal A_raw`. In (2.3)
there then appears

\[
 -\operatorname{Re}
  \langle B_{N,T}^*F,P\mathcal A_{M,N}^{\rm raw}F\rangle.
 \tag{3.1}
\]

R170_843 does not prove a sign for (3.1). It proves the sign of

\[
 -\operatorname{Re}
  \langle G_\delta F,\mathcal A_{M,N}^{\rm raw}F\rangle
 =\mathscr E_{N;T,\delta}^{\beta}(F)>0.                       \tag{3.2}
\]

Substituting `B^*F` for `G_delta F` in (3.1) would be a new identity, not
an estimate. The exact defect that must be controlled is

\[
 \boxed{
 \mathfrak D_{N,T,\delta}^{\rm met}(F)
 :=\operatorname{Re}\langle
   (B_{N,T}^*-G_\delta)F,
   P\mathcal A_{M,N}^{\rm raw}F\rangle.}
 \tag{3.3}
\]

The operator equality
`P_N(B^*-G_delta)P_N=0` would be a much stronger sufficient condition,
not a necessary one. What is required is a cancellation or a sign
for (3.3), together with the three ports of (2.3). This is not proved.

## 4. Diagonal cancellation in Laplace coordinates and its limit

The cause of the clash can be seen exactly. For `a>0`, the Laplace
functional satisfies

\[
 K_{S_Nh}(a)=\sigma_N(a)K_h(a),
 \qquad
 \sigma_N(a)=\sum_{n\le N}n^{a-1/2}>0.                       \tag{4.1}
\]

Hence the modified observer

\[
 G_{N,\delta}^{\rm ext}
 :=\mathscr R_\delta^*
   \operatorname{diag}(\sigma_N(a_m)^{-1})
   \mathscr R_\delta                                  \tag{4.2}
\]

extracts `S_N` exactly within the Gamma coordinates:

\[
 \langle F,G_{N,\delta}^{\rm ext}S_Nh\rangle
 =\langle\mathscr R_\delta F,\mathscr R_\delta h\rangle.
 \tag{4.3}

All the weights in (4.2) are positive, so the Wronskian sign over the
Gamma lattice is preserved. But the right-hand side of
(4.3) is still a compact Hankel form; it is not the physical product
`<F,h>`. No discrete choice of Gamma weights turns
`R_delta^* D R_delta` into the identity on `L^2(-T,T)`: it is a compact
operator, while the identity is not.

So there are two different extractions:

* `B_N,T` extracts `S_N` in the physical metric and loses the proved
  sign;
* `G_N,delta^ext` extracts `S_N` in the Gamma metric and preserves the
  sign, but produces a filtered virial, not the physical virial.

## 5. Consequence for the Ward--PC route

The two-scale PC identity and the causal extraction are correct. The
step still missing can now be stated as a metric compatibility
law on the radical:

> **MET--WARD.** Prove, using minimality of first contact and the
> polar/Tate/outer ports of (2.3), that the difference between the
> physical extraction `B_N,T^*` and the positive Hankel extraction
> `G_N,delta^ext` has non-positive diagonal (or cancels exactly)
> over `ker H_T`.

Positing MET--WARD is equivalent to positing the sign bridge; it is not
declared proved. Its usefulness is to separate the algebraic problem,
already solved by (2.2), from the remaining geometric problem.

## 6. Status

```text
nilpotency of the compressed causal part                     PROVED
finite inverse of P S_N P                                    PROVED
exact extraction of P dot A, equation (2.2)                  PROVED
explicit identification of Tate and two outer ports          PROVED
positive Laplace extraction, equations (4.1)--(4.3)          PROVED
equality between physical metric and Hankel metric           FALSE IN GENERAL
MET--WARD on the radical                                     OPEN
VIR--LB / D                                                  OPEN
```
