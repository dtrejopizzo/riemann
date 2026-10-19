# R170_879 — Möbius divisor law at the exterior boundary

> **Correction R170_884.** The physical predictor uses `S_N`. All sums
> must include `n<=N`; besides the window defect there is also the
> cutoff defect `n>N`. The corrected formulas use `mathfrak m_N;T,t`.

## 0. Result

The representation of R170_878 admits a pointwise expansion. Let
`b` be extended by zero outside `I_T=[-T,T]`. For `t>T`, the causal
predictor

\[
 q_N=QS_N^*P(PS_N^*P)^{-1}b                              \tag{0.1}
\]

is

\[
\boxed{
 q_N(t)=\sum_{k\ge1}{b(t-\log k)\over\sqrt k}
       \mathfrak m_{N;T,t}(k),}                           \tag{0.2}
\]

where

\[
\boxed{
 \mathfrak m_{N;T,t}(k)
 :=\sum_{\substack{n\mid k\\
          n\le N\\
          -T\le t-\log n\le T}}
       \mu(k/n).}                                         \tag{0.3}
\]

The sum in (0.2) is locally finite because `b(t-log k)` requires
`e^(t-T)<=k<=e^(t+T)`.

Since

\[
 \sum_{n\mid k}\mu(k/n)=0\qquad(k>1),                    \tag{0.4}
\]

the difference from `m_N;T,t(k)` counts exactly the routes whose
intermediate point crosses the boundary or whose first factor exceeds `N`. It is not
an estimated error: it is an exact arithmetic law.

## 1. Derivation

R170_850 and adjunction give

\[
 h=(PS^*P)^{-1}b=PM^*Pb.                                  \tag{1.1}
\]

With the convention `tau_a f(t)=f(t+a)`, the adjoint satisfies
`tau_a^*f(t)=f(t-a)`. Hence, inside the window,

\[
 h(u)=\sum_{m\ge1}{\mu(m)\over\sqrt m}\,b(u-\log m).      \tag{1.2}
\]

For `t>T`, applying `S_N^*` to `Ph` produces

\[
 q_N(t)=\sum_{1\le n\le N}{1\over\sqrt n}
       1_{I_T}(t-\log n)\,h(t-\log n).                   \tag{1.3}
\]

Inserting (1.2), setting `k=nm`, and grouping all factorizations
of `k`, gives (0.2)--(0.3). Both support conditions are
preserved: `t-log n` is the intermediate point and `t-log k` the starting point
observed by `b`.

## 2. Form of the excluded routes

For `t>T`, the divisors admitted in (0.3) satisfy

\[
 e^{t-T}\le n\le e^{t+T}.                                 \tag{2.1}
\]

On the effective support of (0.2), `k>1`. Using (0.4),

\[
\boxed{
 \mathfrak m_{N;T,t}(k)
 =-\sum_{\substack{n\mid k\\
          n>N\ \text{or}\ t-\log n\notin[-T,T]}}
       \mu(k/n).}                                         \tag{2.2}
\]

This coincides with the exterior loop

\[
 q_N=-QS_N^*QM^*Pb-QU_N^*M^*Pb                           \tag{2.3}
\]

of R170_878: (0.3) counts the routes admitted by the window and cutoff;
(2.2) counts the excluded ones with the opposite sign, before
`S^*M^*=I` can cancel them.

## 3. Structural consequences

The formula has four properties necessary for a law of D:

1. **it uses the exact integers:** every divisor of each
   `k` appears, with the exact values of `mu`;
2. **it is uniform in `T`:** changing the window only moves the
   divisor interval of (2.1);
3. **it preserves the exterior:** the cut is at the intermediate point, before
   recombining `nm=k`;
4. **it distinguishes the unit route:** total cancellation depends on
   `mu*1=delta_1`, while the Mangoldt comb has no `n=1`.

Moreover, `m_N;T,t(k)` has no fixed sign. For `N>=6`, `k=6`, a divisor
window that contains only `n=6` gives `m=mu(1)=1`, while one that
contains `n=2,3,6` but not `n=1` gives
`m=mu(3)+mu(2)+mu(1)=-1`. Both patterns are realized by multiplicative
intervals of the form (2.1), the second when `2T>=log 3` and the lower
endpoint is chosen between `1` and `2`. Thus unique factorization
locates the residue, but it does not yet sign the Wronskian.

## 4. Insertion into the exterior law

Define the boundary operator

\[
 (\mathfrak B_{N,T}b)(t)
 :=1_{(T,\infty)}(t)
   \sum_k{k^{-1/2}}b(t-\log k)\mathfrak m_{N;T,t}(k).      \tag{4.1}
\]

Then `q_N=mathfrak B_N,Tb` on the right boundary; the left boundary is
obtained by reflection. The open law of R170_853 takes the form

\[
 \mathfrak W_{\rm ext}
 =(\dot{\mathfrak B}_{N,T}b,z_F)
  -(\mathfrak B_{N,T}b,\dot z_F^{\,0}),                    \tag{4.2}
\]

where `dot B_T` means the frozen derivative of the `S` leg, not a
derivative of the divisor interval.

A term-by-term vanishing of (4.2) would be false in general because
`m_N;T,t(k)` changes sign. The piece that could still produce a law is a
summation-by-parts identity over the divisor poset combining (4.2)
with the tail `R_M` and the polar continuum, before taking the
real part. That identity is not claimed here.

## 5. Status

```text
pointwise expansion of the predictor q                     PROVED
coefficient as a partial Möbius sum                         PROVED
equivalence of interior/excluded routes                     PROVED
local finiteness and uniformity in T                         PROVED
individual sign of m_T,t(k)                                  FALSE IN GENERAL
summation-by-parts law with tail and polar term              OPEN
VIR--LB / D                                                  OPEN
```
