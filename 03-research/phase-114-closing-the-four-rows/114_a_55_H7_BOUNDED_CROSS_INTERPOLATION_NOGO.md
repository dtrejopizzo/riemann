# 114.a.55 — H7 no-go: bounded cross interpolation saturates a moment block

```
+--------------------------------------------------------------------------+
| BLOCK       m odd moments modulo p, with p>2^(2m).                      |
| INTERPOLATE A Vandermonde system lifts every y in F_p^m to m integers.  |
| BOUNDED     One first-row/second-column contraction realizes the lift.  |
| DEGREES     d_1=log(m(p-1)) and d_2=m log 2 are both linear in m.       |
| SURJECT     The bounded sections map onto the complete block F_p^m.     |
| NO-GO       Their entropy exceeds the a_53 code coefficient by          |
|             (1-log(2)/(2log(3)))m log p+o(m log p).                    |
| RESULT      The current complete-bounded h_FM cannot satisfy sharp RR.  |
+--------------------------------------------------------------------------+
```

## 1. The block and its interpolation matrix

Use an actual block of `a_51`--`a_52`. Write

\[
 m=2r,\qquad s_j=2j+1\quad(0\le j<m),                                  \tag{1.1}
\]

and let `p` be its controlled prime. The strengthened harmless lower bound
in `a_51` is

\[
 p>2^{4r}=2^{2m}.                                                        \tag{1.2}
\]

Consequently the integers

\[
 b_j=2^{s_j}\pmod p                                                     \tag{1.3}
\]

are pairwise distinct. Hence the Vandermonde matrix

\[
 V=(b_j^k)_{0\le j,k<m}                                                 \tag{1.4}
\]

is invertible over `F_p`.

Put

\[
 A=m(p-1).                                                               \tag{1.5}
\]

Since `p>m`, the denominators `A` and `2^m` are invertible modulo `p`.
Given any `y=(y_j) in F_p^m`, solve

\[
 V(a_0,\ldots,a_{m-1})^t
 =\bigl(A2^{ms_j}y_j\bigr)_{j=0}^{m-1}\pmod p                          \tag{1.6}
\]

and choose the centered representatives

\[
 |a_k|\le(p-1)/2.                                                       \tag{1.7}
\]

## 2. A genuinely bounded lift

In the first and second rulings respectively define

\[
 \alpha_y=(a_0/A,\ldots,a_{m-1}/A),\qquad
 \beta=(1/2^m,2/2^m,\ldots,2^{m-1}/2^m).                               \tag{2.1}
\]

Their exact Euclidean bounds are

\[
 \|\alpha_y\|_2^2
 \le {m(p-1)^2\over4m^2(p-1)^2}={1\over4m}<1,
 \qquad
 \|\beta\|_2^2={4^m-1\over3\,4^m}< {1\over3}.                       \tag{2.2}
\]

Form the typed cross-contraction

\[
 C_y=p_1^*\alpha_y\circ(p_2^*\beta)^t.                                 \tag{2.3}
\]

Let

\[
 D_1=\sum_\ell v_\ell(A)L_\ell,\qquad D_2=mL_2.                       \tag{2.4}
\]

### Theorem 2.1 (bounded cross interpolation)

Every `C_y` is a genuine scalar pro-section of

\[
 p_1^*\mathcal O(D_1)\otimes p_2^*\mathcal O(D_2).                     \tag{2.5}
\]

Moreover its projection to the selected moment block is exactly `y`.

### Proof

At a finite prime, (2.4) clears the denominator `A` in the first row and
`2^m` in the second column. At every real or mixed boundary chart, (2.2)
puts both vectors in Haran's Euclidean operator ball. The same rational
vectors occur at every finite refinement, so the pro-section condition is
automatic, exactly as in `a_28` Theorem 3.1.

Under the `s_j`-th homogeneous-endobio evaluation of `a_49`--`a_51`, the
first row is ordinary linear and every entry of the second column is raised
to the `s_j`-th power. Therefore

\[
 \begin{aligned}
 \varepsilon_{p,s_j}(C_y)
 &=\sum_{k=0}^{m-1}{a_k\over A}
       \left({2^k\over2^m}\right)^{s_j}\\
 &=A^{-1}2^{-ms_j}\sum_{k=0}^{m-1}a_k(2^{s_j})^k
 =y_j\pmod p,
 \end{aligned}                                                         \tag{2.6}
\]

where the last equality is (1.6). QED.

### Corollary 2.2 (bounded saturation)

The image of the complete bounded scalar section set in (2.5), projected
to this block, is all of `F_p^m`. In particular it contains `p^m` distinct
classes and

\[
 h_{\rm FM}(D_1,D_2)\ge m\log p.                                       \tag{2.7}
\]

This is stronger than `a_54`: saturation no longer uses the unfiltered
Laurent algebra, but a single explicitly bounded cross-contraction for each
target vector.

## 3. Quadratic mismatch with the proposed RR coefficient

The degrees of (2.4) are

\[
 d_1=\log A=\log p+O(\log m),\qquad d_2=m\log2.                         \tag{3.1}
\]

The controlled-prime construction has `log p=Theta(m)`: (1.2) gives the
lower bound and Linnik gives the linear upper bound. Thus both degrees tend
to infinity on a compact cone of positive rays.

The code coefficient asserted in `a_35` and extended in `a_53`, evaluated
on these degrees, is

\[
 {d_1d_2\over2\log3}
 ={\log2\over2\log3}\,m\log p+o(m\log p).                              \tag{3.2}
\]

But (2.7) gives `m log p`. Hence the excess is at least

\[
 \boxed{
 \left(1-{\log2\over2\log3}\right)m\log p+o(m\log p)
 =\Theta(m^2).
 }                                                                      \tag{3.3}
\]

The coefficient in parentheses is positive.

This also yields a fixed-ray obstruction. The ratios `log(A)/m` lie in a
compact positive interval, so take a convergent subsequence with limit `c`.
For any sufficiently small `eta>0`, the sections (2.3) embed, by the
residual positive metric used in `a_53`, into the fixed ray with degrees
`((c+eta)m,m log2)`. Choose `eta` so that

\[
 c>{ (c+\eta)\log2\over2\log3}.                                        \tag{3.4}
\]

Using a fresh block at every member of the subsequence, (2.7) and (3.4)
contradict any per-degree complete-bounded moment candidate with the sharp
comparison (4.1) of `a_53` by a positive quadratic amount. This does not
require retaining old blocks; `a_57` later retracts that retention.

### Theorem 3.1 (failure of the present RR candidate)

The normalized dimension defined as the moment image of the **complete
bounded scalar section set** cannot have the universal sharp coefficient
`d_1d_2/(2log3)`. Therefore the former H7-RR-FILT gate is not merely an
unproved estimate for the existing `h_FM`: that estimate is false.

Any surviving replacement must change the measured object. It must exclude
the genuine bounded cross-interpolation family (2.3), or quotient it further,
and then prove that this exclusion is canonical, multiplicative, principal
invariant and compatible with sheaf restriction/exactness. Ordinary divisor
boundedness alone cannot do this.

We call this strictly stronger replacement gate **H7-SEL-RR/EXACT**.

`a_56` later classifies its quotient-based finite part: every multiplicative
quotient of a block is a coordinate projection, and the least possible size
is `p^kappa`, where `kappa` is the exact difference-support hitting number.
The first surviving asymptotic is H7-SEL-MOM.

`a_57` adds a separate global obstruction: positive-characteristic blocks
cannot persist across the full denominator cone. Thus even a successful
per-block H7-SEL-MOM would still require H7-DEN-TRANS.

## 4. Verification scope

`114_a_55_h7_bounded_cross_interpolation_verify.py` checks exact
Vandermonde inversion, centered coefficient lifts, both rational norm
bounds, every target over the full `m=2,p=17` block, deterministic targets
for the `m=4,p=257` block, and the positive asymptotic gap. The categorical
typing and pro-section membership use the same source definitions and proof
as `a_28`; the script does not replace that source-level argument.
