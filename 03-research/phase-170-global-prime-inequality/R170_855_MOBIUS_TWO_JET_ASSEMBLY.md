# R170_855 — Möbius assembly of the two jets: exact recovery of the prime virial

> **Correction R170_856 (reading inside full PC).** The coefficient
> identities of this record, including
> `-M A_raw + M K2 = -2 dot L` on complete fibers, are correct.
> However, `K2` does not survive as an independent summand of the
> differentiated PC identity. If `K_-:=2K+K2`, then the jet of
> `{X_r,E(r,q)} mathscr F_r` contains `-K_- - J K_- mathscr F`, while
> the two branches of `-JH mathscr F-H` contain
> `+J K_- mathscr F+K_-`. The cancellation is term by term, before
> compressing and before applying Möbius. Hence (3.3) is an arithmetic
> subidentity of separate branches, but not a surviving contribution to
> the Ward--PC balance. It cannot be used to claim that PC reconstructs
> the prime virial via `gamma+W`.

## 0. Result

The antidiagonal derivative of PC at two scales contains two channels
that, after causal Möbius extraction, complement each other exactly:

1. the Wronskian of the `L` and `S` legs;
2. the second jet of the integer comb contained in `partial_-K_N(r,q)`.

Their interior coefficients are

\[
 \gamma_\Lambda=\Lambda\log-\Lambda*\Lambda,
 \qquad
 W=\mu*\log^2=\Lambda\log+\Lambda*\Lambda.
 \tag{0.1}
\]

Therefore

\[
 \boxed{\gamma_\Lambda+W=2\Lambda\log.}                     \tag{0.2}
\]

This exactly recovers the weight of the prime virial **in the partial
combination of these two branches**. R170_856 proves that `W` also
appears with opposite sign in the Poisson--`X` jet; therefore this
combination does not survive in the full PC derivative.

## 1. Second jet of the Chebyshev operator

R170_847 defines

\[
 K_N(r,q)={r\over q}\sum_{n\le N}{\log n\over\sqrt n}
                 \tau_{\log n/q}.
\]

With `partial_-=(partial_r-partial_q)|_(1,1)`, the chain rule gives

\[
 \boxed{
 \partial_-K_N(r,q)
 =2K_N+K_N^{(2,\partial)},}                                  \tag{1.1}
\]

where

\[
 K_N^{(2,\partial)}
 :=\sum_{n\le N}{(\log n)^2\over\sqrt n}
          \partial_t\tau_{\log n}.                           \tag{1.2}
\]

The term `2K_N` comes from the covariant factor `r/q`; the second term
comes from the motion of the frequencies `log n/q`.

## 2. Extraction by the Möbius comb

Let

\[
 M=\sum_{d\ge1}{\mu(d)\over\sqrt d}\tau_{\log d}.
\]

On every complete fiber `k<=N`, the causal composition of `M` with (1.2)
has coefficient

\[
 \sum_{d\mid k}\mu(d)\left(\log{k/d}\right)^2.
 \tag{2.1}
\]

Changing `d` to the complementary divisor, or using Dirichlet series,
identifies (2.1) with

\[
 W(k)=(\mu*\log^2)(k).                                      \tag{2.2}
\]

Therefore, on the interior block,

\[
 \boxed{
 MK_N^{(2,\partial)}
 =\sum_{k\le N}{W(k)\over\sqrt k}
       \partial_t\tau_{\log k}.}                            \tag{2.3}

The routes crossing the cut are kept as a terminal tail; (2.3) does
not declare them zero.

## 3. Sum with the extracted Wronskian

R170_850 proves

\[
 M\mathcal A_\Lambda^{\rm raw}
 =-\sum_{k}{\gamma_\Lambda(k)\over\sqrt k}
       \partial_t\tau_{\log k}.                             \tag{3.1}

Thus

\[
\begin{aligned}
 -M\mathcal A_\Lambda^{\rm raw}
 +MK_N^{(2,\partial)}
 &=\sum_k{\gamma_\Lambda(k)+W(k)\over\sqrt k}
       \partial_t\tau_{\log k}\\
 &=2\sum_k{\Lambda(k)\log k\over\sqrt k}
       \partial_t\tau_{\log k}\\
 &=-2\dot L.
\end{aligned}                                               \tag{3.2}

The last equality uses the convention
`dot L=-sum Lambda(k)log(k) partial tau_log(k)/sqrt(k)` from
R170_841.

**Theorem 3.1 (two-jet assembly).** On every complete fiber of the
finite cutoff,

\[
 \boxed{
 -M\mathcal A_\Lambda^{\rm raw}
 +MK_N^{(2,\partial)}=-2\dot L.}                            \tag{3.3}

The identity simultaneously uses `mu*1=delta`, `Lambda*1=log` and
scale differentiation. Changing the von Mangoldt weights introduces
the corresponding defect in (0.1).

## 4. Difference from the Selberg no-go

R162_501 and R170_841 §4.3 reject the argument

\[
 \text{"introduce }W\ge0\text{ and deduce the sign of }c_F'\text{"}.
\]

Theorem 3.1 does not make that inference. It correctly states that `W`
is inside the exact derivative of `K_N(r,q)` on the branch considered.
Full PC, however, contains the opposite copy computed in R170_856;
it is not permitted to reach the physical pairing by keeping only the
copy from this record.

Nonetheless, (3.3) is still a coefficient identity. To obtain VIR--LB
one must verify, in the full expansion, that:

1. the covariant term `2MK_N` of (1.1) cancels against the terms coming
   from `dot X_r=X`;
2. the incomplete tails of both channels coincide with `dot H_M,N`;
3. the polar continuum, the boundary atoms and the Tate defect of
   R170_852 remain on the same side;
4. after these cancellations, the remaining diagonal has the Hankel
   sign proved in R170_843, not only the physical value (3.3).

## 5. Status

```text
second jet partial_-K=2K+K2                               PROVED
extraction M K2 = W on complete fibers                     PROVED
gamma+W=2 Lambda log                                        PROVED
assembly -M A_raw+M K2=-2 dotL                              PROVED
full cancellation of 2MK+MK2 in PC                          PROVED R170_856
physical survival of the assembly (3.3)                     REFUTED R170_856
tail and port ledger                                        PROVED R170_856
sign of the physical diagonal                                OPEN
VIR--LB / D                                                  OPEN
```
