# P121 -- exact compressed Euler-divisor collar formula

## Status

This note computes the Mellin--Laplace transform of a compressed prime
tower at the zeros of its own local Euler factor.  The calculation is
exact and separates the interior coefficient `K_F(lambda_(p,k))` from the
two lost boundary collars.

It also proves a strict typing fact: an inactive prime is absent not merely
from the interior operator but from the complete transformed compressed
tower, by termwise cancellation against the full collar.  Therefore the
cofinal inactive-prime oriented boundary cannot be deduced from the
localized first-contact equation alone.  It must enter through the global
pre-supertrace row-(b)--row-(c) source comparison.

## 1. Transform of one compressed translation

Let `I_T=(-T,T)`, extend `F in L^2(I_T)` by zero, and put

\[
 K_F(w)=\int_{-T}^{T}e^{-wt}F(t)\,dt.              \tag{1.1}
\]

For `a>=0` define the `w`-weighted right and left collars

\[
 \begin{aligned}
 R_w(a)&=\int_{\max(T-a,-T)}^{T}e^{-wt}F(t)\,dt,\\
 L_w(a)&=\int_{-T}^{\min(-T+a,T)}e^{-wt}F(t)\,dt.
 \end{aligned}                                    \tag{1.2}
\]

Thus `R_w(a)=L_w(a)=K_F(w)` for `a>=2T`.  With

\[
 (S_aF)(t)=F(t-a),\qquad(S_{-a}F)(t)=F(t+a),       \tag{1.3}
\]

one has

### Lemma 1.1 -- exact collar loss

\[
 \boxed{
 \begin{aligned}
 \int_{-T}^{T}e^{-wt}S_aF(t)\,dt
   &=e^{-wa}\bigl(K_F(w)-R_w(a)\bigr),\\
 \int_{-T}^{T}e^{-wt}S_{-a}F(t)\,dt
   &=e^{ wa}\bigl(K_F(w)-L_w(a)\bigr).
 \end{aligned}}                                    \tag{1.4}
\]

#### Proof

In the first integral set `u=t-a`; the surviving range is
`-T<u<T-a`.  In the second set `u=t+a`; the surviving range is
`-T+a<u<T`.  Completing each integral to `(-T,T)` gives (1.4), including
the case `a>=2T`, where both sides are zero.  QED.

## 2. One complete prime tower

For a prime `p`, let `ell_p=log p` and define the symmetric compressed
tower

\[
 B_{p,T}F=(\log p)\sum_{j\ge1}p^{-j/2}
       (S_{j\ell_p}+S_{-j\ell_p})F.                \tag{2.1}
\]

The sum in (2.1) is locally finite after compression: every term with
`j ell_p>=2T` is zero.  Lemma 1.1 gives, for every `w in C`,

\[
 \begin{aligned}
 \mathcal L_w(B_{p,T}F)
  =(\log p)\sum_{j\ge1}p^{-j/2}\{&
  e^{-wj\ell_p}[K_F(w)-R_w(j\ell_p)]\\
  &+e^{wj\ell_p}[K_F(w)-L_w(j\ell_p)]\}.
                                                               \tag{2.2}
 \end{aligned}
\]

Although written as an infinite sum, (2.2) is exactly finite because both
brackets vanish once `j ell_p>=2T`.

## 3. Evaluation on the local Euler divisor

The zeros of

\[
 e_p(w)=1-p^{-1/2-w}
\]

are

\[
 \lambda_{p,k}=-\frac12+\frac{2\pi i k}{\log p},
 \qquad k\in\mathbb Z.                             \tag{3.1}
\]

At `w=lambda_(p,k)`,

\[
 p^{-j/2}e^{-wj\ell_p}=1,
 \qquad
 p^{-j/2}e^{wj\ell_p}=p^{-j}.                     \tag{3.2}
\]

### Theorem 3.1 -- Euler-divisor collar formula

For every prime `p` and integer `k`,

\[
 \boxed{
 \mathcal L_{\lambda_{p,k}}(B_{p,T}F)
  =(\log p)\sum_{j\ge1}\left\{
     K_F(\lambda_{p,k})-R_{\lambda_{p,k}}(j\ell_p)
   +p^{-j}[K_F(\lambda_{p,k})-L_{\lambda_{p,k}}(j\ell_p)]
  \right\}.}                                      \tag{3.3}
\]

Again every summand with `j ell_p>=2T` is individually zero.  In
particular the coefficient singled out by oriented `K_2` localization,

\[
 c^{(1)}_{p,k}(F)=K_F(\lambda_{p,k}),               \tag{3.4}
\]

occurs before compression, while compression replaces it by the exact
interior-minus-collar combination in (3.3).

#### Proof

Substitute (3.2) into (2.2).  The last assertion follows from
`R_w(a)=L_w(a)=K_F(w)` for `a>=2T`.  QED.

### Corollary 3.2 -- inactive-prime invisibility is termwise

If `log p>=2T`, then

\[
 B_{p,T}=0,
 \qquad
 \mathcal L_{\lambda_{p,k}}(B_{p,T}F)=0            \tag{3.5}
\]

for every `k` and every `F`, while `c^(1)_(p,k)(F)` may be nonzero.

#### Proof

For every `j>=1`, `j log p>=2T`; hence both collars in (3.3) equal the
complete transform and each displayed bracket is zero.  Nothing in this
argument constrains (3.4).  QED.

This distinguishes two statements which must not be conflated:

\[
 P_TS_{\pm j\log p}P_T=0
 \quad\not\Longrightarrow\quad
 K_F(\lambda_{p,k})=0.                             \tag{3.6}
\]

## 4. Consequence for the Rees lift

The first-contact equation at window `T` contains exactly the compressed
towers (2.1).  Corollary 3.2 proves that its inactive-prime components are
identically zero for every source, whereas the cofinal Rees normal is

\[
 (\eta-\eta^{-1})K_F(\lambda_{p,1}).               \tag{4.1}
\]

Therefore no manipulation of the localized operator equation by itself can
produce the cofinal first-harmonic law.  An admissible proof of the
orientation-Rees lift must use a global operation which is present before
compression and before scalar supertrace.  The candidates already
constructed with the correct type are:

1. the global Poisson equalizer `B_+=B_-`;
2. its fixed-source Rees normal `Zf`;
3. the place-resolved Euler connection `Z_p partial Z_p^(-1)`;
4. the oriented relative `K_2` localization of that normal.

The still missing compatibility is not an estimate.  It is the assertion
that the first-contact inclusion is horizontal for this global normal
complex.  Formula (3.3) prevents replacing that assertion by inactive
compression.

## 5. Ledger

```text
compressed translation transform                         PROVED
prime-tower transform at its local Euler divisor          PROVED
interior c^(1) versus collar loss                         SEPARATED EXACTLY
inactive-prime cancellation term by term                  PROVED
localized first contact determines inactive c^(1)         FALSE
global pre-supertrace first-contact lift                   OPEN
global square and row (d)                                 OPEN
```
