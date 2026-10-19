# 104_107 — Fejér blocks and the exact phase-transport gate

**Question.** Does the block relaxation of `104_67`, applied before
transporting the phase bound of `104_41` from \(a\geq4\) down to
\(a=1\), reduce the cost enough to control the residue defect of
`104_33`?

**Result.** The correct smoothing does produce a strong, uniform gain in
the Euler half-plane. Over \(2L-1\) consecutive degrees, a triangular
average centered at \(N\) satisfies

\[
 \boxed{
 |\mathcal B^{\triangle}_{N,L,a}|
 \le {3\pi\over2}{N\over L}
       +2\left(1-{1\over L^2}\right),\qquad a\geq4.}       \tag{1}
\]

In particular, for \(N\asymp L\), the right-hand side is a constant,
instead of the degree-by-degree bound \(3n\). No boundary term is lost
in (1).

However, the filter evaluated at an interior residue is exactly

\[
 T_{N,L}(w)+T_{N,L}(w^{-1})-2,
 \qquad
 T_{N,L}(w)=w^{N-L+1}
 \left({1-w^L\over L(1-w)}\right)^2.                       \tag{2}
\]

For \(|w|<1\), the second summand of (2) has size

\[
 { |1-w^L|^2\over L^2|1-w|^2}\,|w|^{-N-L+1},              \tag{3}
\]

and it never vanishes: the only zeros of \(1-w^L\) lie on
\(|w|=1\). So the averaging that reduces the boundary variation to
\(O(N/L+1)\) preserves — and even localizes at the high end — the
exponential load of every zero with real part \(>1/2\).

The rational quartet \(w=i/2\) gives both signs of size
\(\asymp2^{N+L}/L^2\), while leaving the phase on the critical line
unchanged. Hence the one-sided transport of the block average, using
only the phase bound and the homotopy, is refuted. The corresponding
inequality for the literal weights \(\Lambda(m)\) remains a new
arithmetic theorem of RH strength; this document does not prove it, nor
does it prove A1 or RH.

---

## 1. Two consecutive averages and why the triangular one is used

As in `104_41`, let

\[
 W_n(t)=2-2\cos(n\theta(t)),\qquad
 {-1/2+it\over1/2+it}=e^{i\theta(t)},\qquad t>0,           \tag{4}
\]

where \(\theta\) decreases from \(\pi\) to \(0\). For the uniform average
of \(L\) degrees \(N,\ldots,N+L-1\),

\[
 W^{\rm unif}_{N,L}(\theta)
 =2-{2\over L}{\sin(L\theta/2)\over\sin(\theta/2)}
 \cos\left({(2N+L-1)\theta\over2}\right).                 \tag{5}
\]

Its exact variation is

\[
 \mathrm{TV}_{\mathbb R}(W^{\rm unif}_{N,L})
 ={4\over L}\int_0^\pi
 \left|\sum_{n=N}^{N+L-1}n\sin(n\theta)\right|d\theta.   \tag{6}
\]

Orthogonality and Cauchy–Schwarz give

\[
 \mathrm{TV}_{\mathbb R}(W^{\rm unif}_{N,L})
 \le {2\sqrt2\pi\over L}
       \left(\sum_{n=N}^{N+L-1}n^2\right)^{1/2}.           \tag{7}
\]

This improves \(O(N)\) to \(O(N/\sqrt L)\), but it is not the optimal
scale for a long block.

To get the optimal scale, suppose \(N\geq L\geq1\) and set

\[
 \alpha_{L,k}:={L-|k|\over L^2},\qquad |k|<L,
 \qquad \sum_{|k|<L}\alpha_{L,k}=1.                       \tag{8}
\]

Define

\[
 \begin{aligned}
 W^\triangle_{N,L}(t)
   &:=\sum_{|k|<L}\alpha_{L,k}W_{N+k}(t),\\
 \mathcal B^\triangle_{N,L,a}
   &:=\sum_{|k|<L}\alpha_{L,k}\mathcal B_{N+k,a}.
 \end{aligned}                                             \tag{9}
\]

These are genuine averages of the consecutive degrees
\(N-L+1,\ldots,N+L-1\); no coefficient of negative sign appears. The
exact transform of (8) is

\[
 H_L(\theta):=\sum_{|k|<L}\alpha_{L,k}e^{ik\theta}
 =\left({\sin(L\theta/2)\over L\sin(\theta/2)}\right)^2.
                                                               \tag{10}
\]

Hence

\[
 \boxed{
 W^\triangle_{N,L}(\theta)
 =2-2H_L(\theta)\cos(N\theta).}                           \tag{11}
\]

In particular \(W^\triangle_{N,L}\geq0\), being an average of the
\(W_n\), and \(W^\triangle_{N,L}(t)\to0\) as
\(|t|\to\infty\). At the other end,

\[
 W^\triangle_{N,L}(0)
 =\begin{cases}
 2,&L\text{ even},\\
 2-2(-1)^N/L^2,&L\text{ odd}.
 \end{cases}                                               \tag{12}
\]

Equation (12) is recorded so as not to discard the boundary \(t=0\) when
splitting the integral into two half-lines. In the integral over all of
\(\mathbb R\) it is not a boundary; the only boundaries of the
integration by parts are at \(\pm\infty\), where (11) vanishes.

---

## 2. Total variation of the Fejér block

From (11) and the monotonicity of \(\theta(t)\) on each half-line one
obtains the exact identity

\[
 \boxed{
 \mathrm{TV}_{\mathbb R}(W^\triangle_{N,L})
 =4\int_0^\pi
   \left|{d\over d\theta}\{H_L(\theta)\cos(N\theta)\}
   \right|d\theta.}                                      \tag{13}
\]

Moreover,

\[
 \int_0^\pi H_L(\theta)d\theta={\pi\over L}.             \tag{14}
\]

We also need a uniform bound, with an explicit constant, for the
variation of \(H_L\):

\[
 \boxed{
 \mathrm{TV}_{[0,\pi]}(H_L)
 \le {4\over3}\left(1-{1\over L^2}\right).}              \tag{15}
\]

This accounts for all the lobes. To prove (15), write
\(x=\theta/2\). Between two consecutive zeros of
\(\sin(Lx)/\sin x=U_{L-1}(\cos x)\) there is exactly one critical point:
Rolle's theorem gives one, and the degree of \(U'_{L-1}\) prevents there
being more. The lobe starting at \(x=j\pi/L\), \(j\geq1\), has height at
most

\[
 {1\over L^2\sin^2(j\pi/L)}.                              \tag{16}
\]

For \(L\) even, the identity

\[
 \sum_{j=1}^{L/2-1}\csc^2(j\pi/L)={L^2-4\over6}           \tag{17}
\]

gives (15), counting the drop of the main lobe once and each interior
lobe twice. For \(L\) odd one uses

\[
 \sum_{j=1}^{(L-1)/2}\csc^2(j\pi/L)={L^2-1\over6},        \tag{18}
\]

the last summand, which is at least \(1\), is removed, and the boundary
\(H_L(\pi)=1/L^2\) is added. The same right-hand side of (15) results.
For \(L=1\), both sides equal zero.

Applying the product rule in (13), and then (14)–(15),

\[
 \boxed{
 \mathrm{TV}_{\mathbb R}(W^\triangle_{N,L})
 \le4\left\{{\pi N\over L}
       +{4\over3}\left(1-{1\over L^2}\right)\right\}.}  \tag{19}
\]

---

## 3. One-sided bound in the Euler half-plane

The phase identity of `104_41` is linear in \(W_n\). By (9),

\[
 \mathcal B^\triangle_{N,L,a}
 =-{1\over2\pi}\int_{\mathbb R}
 W^\triangle_{N,L}(t)d\vartheta_a(t).                     \tag{20}
\]

For \(a\geq4\), `104_41` proves
\(|\vartheta_a(t)|<3\pi/4\). Integrating (20) by parts over the whole
line, the boundaries at \(\pm\infty\) vanish by (11). The possible
variations at \(t=0\) from the two half-lines cancel because both
\(W^\triangle_{N,L}\) and the conjugate branch of the phase are
continuous there. From (19),

\[
 \begin{aligned}
 |\mathcal B^\triangle_{N,L,a}|
 &\le {1\over2\pi}{3\pi\over4}
       \mathrm{TV}_{\mathbb R}(W^\triangle_{N,L})\\
 &\le {3\pi\over2}{N\over L}
       +2\left(1-{1\over L^2}\right),
 \end{aligned}                                             \tag{21}
\]

which proves (1). In particular, for \(N=2L+O(1)\), the entire block is
bounded by \(3\pi+2+o(1)\). This is a two-sided inequality and therefore
contains both one-sided versions. We did not use

\[
 \left|\int gh\right|\leq\int|g||h|;
\]

only the full prime–pole phase and the variation of the combined test
function.

There is a binding logical distinction. Bound (21) controls the
**signed average** of the \(2L-1\) degrees; it does not claim that these
degrees form a good block in the coefficient-by-coefficient sense of
`104_67`. Large positive and negative values can cancel within the
average. To use the `104_67` criterion directly one would need to
control the maximum, the positive part, or every single degree of the
block. None of those operations is linear in \(W_n\), and (21) does not
estimate them.

---

## 4. Exact transport of the block residues

For a zero \(\rho\) with \(\Re\rho>1/2\), set

\[
 w=1-{1\over\rho},\qquad |w|<1.                            \tag{22}
\]

The identity of `104_33`, with no factors omitted, is

\[
 {\mathcal F_n(w)\over\rho(\rho-1)}=w^n+w^{-n}-2.          \tag{23}
\]

The algebraic transform of the weights (8) holds for every \(w\ne0,1\):

\[
 \begin{aligned}
 T_{N,L}(w)
 &:=\sum_{|k|<L}\alpha_{L,k}w^{N+k}\\
 &=w^{N-L+1}\left({1-w^L\over L(1-w)}\right)^2.           \tag{24}
 \end{aligned}
\]

Averaging (23) gives exactly (2). Consequently, the block version of
(22) from `104_41` is

\[
 \boxed{
 B^\triangle_{N,L}=\mathcal P^\triangle_{N,L}
 +\sum_{\Re\rho>1/2}m_\rho
 \{T_{N,L}(w_\rho)+T_{N,L}(w_\rho^{-1})-2\}.}             \tag{25}
\]

The sum is understood with the same functional orbits and the same
symmetric limit as in `104_33`; the average is finite, so it can be
interchanged with each partial sum. No new boundary term appears.

Using (24) twice,

\[
 \begin{aligned}
 T_{N,L}(w)+T_{N,L}(w^{-1})
  =\left({1-w^L\over L(1-w)}\right)^2
   \{w^{N-L+1}+w^{-N-L+1}\}.                              \tag{26}
\end{aligned}
\]

If \(|w|<1\), the coefficient of \(w^{-N-L+1}\) in (26) is not zero,
since \(w^L\ne1\). Its modulus is exactly (3). So the variation
reduction of (21) produces no exponential reduction in the residues: the
upper endpoint \(N+L-1\), whose weight is only \(L^{-2}\), dominates an
evaluation outside the circle.

---

## 5. Rational falsifier of both signs

Take

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5}.         \tag{27}
\]

Complete the functional quartet as in `104_41`. Its polynomial is
strictly positive on \(\Re s=1/2\), so multiplying the completion by any
power of the quartet does not change the phase on the critical line.

Let \(4\mid L\) and define

\[
 c_L:={(1-2^{-L})^2\over L^2},\qquad
 \left({1-w^L\over L(1-w)}\right)^2
 =c_L\,{12+16i\over25}.                                  \tag{28}
\]

For \(N_+=2L+1\), the exponents in (26) are \(L+2\) and \(-3L\), and

\[
 \Re\{T_{N_+,L}(w)+T_{N_+,L}(w^{-1})\}
 ={12c_L\over25}\{2^{3L}-2^{-L-2}\}.                    \tag{29}
\]

For \(N_-=2L+3\), they are \(L+4\) and \(-(3L+2)\), and

\[
 \Re\{T_{N_-,L}(w)+T_{N_-,L}(w^{-1})\}
 =-{12c_L\over25}\{2^{3L+2}-2^{-L-4}\}.                 \tag{30}
\]

The Li contribution of the quartet to the average is

\[
 Q^\triangle_{N,L}
 =4-2\Re\{T_{N,L}(w)+T_{N,L}(w^{-1})\},                  \tag{31}
\]

and the corresponding change in \(B^\triangle_{N,L}\) is
\(-M Q^\triangle_{N,L}\) for multiplicity \(M\). From (29), the change
is positive and of size \(\asymp M2^{3L}/L^2\); from (30), it is negative
and of the same size. In contrast, (21), with \(N_\pm/L=2+O(1/L)\), has
a right-hand side smaller than an absolute constant.

Hence **both** candidate transports fail,

\[
 B^\triangle_{N,L}\leq C,
 \qquad B^\triangle_{N,L}\geq-C,                         \tag{32}
\]

if only the critical phase, functional symmetries, and the homotopy are
used without the term (25). The quartet does not carry the Euler
weights of the ordinary primes; that is why (29)–(30) do not refute a
specific inequality for \(\Lambda(m)\). What they do prove is that the
block average does not allow transporting (21) by a scaling argument or
by automatic cancellation of the filter.

---

## 6. Decision

```text
proved:
  closed formula for the uniform average and its exact TV;
  positive triangular filter over 2L-1 consecutive degrees;
  exact TV as an integral and explicit bound O(N/L+1);
  phase bound |B^triangle_{N,L,a}|=O(N/L+1), a>=4;
  exact transport of the filter to each interior residue;
  absence of zeros of the multiplier inside the disc;
  rational quartet with defects of both signs ~2^(N+L)/L^2.

real gain:
  the block average completely removes the linear boundary cost when
  L is comparable to N.

ruled out:
  that this boundary gain attenuates or cancels the off-line defect;
  transporting either of the two one-sided inequalities of (21) using
  only phase, symmetry, and homotopy.

remains:
  proving directly, for the ordinary weights Lambda(m), a one-sided
  block bound that couples P^triangle with the sum in (25).

not proved:
  that arithmetic bound, the block criterion, A1, or RH.
```

The result is not another energy coordinate: it preserves exactly the
\(a\geq4\) scaffolding, the full phase, the residue sum, and the
falsifier of the Li–Laguerre route.

## 7. Reproducible verification

The file `tools/fejer_block_phase_transport_check.py` uses only
`Fraction` and Gaussian rationals. It checks the normalization and
centering of the weights, (24), (23), (26), and the signed formulas
(28)–(31) for multiple values of \(L\). The analytic variation bound is
proved in §2 and is not replaced by sampling.

Reproduce with

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 fejer_block_phase_transport_check.py
```
</content>
