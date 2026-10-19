# 104_34 — Flag prefix curvature and the adjacent Schur gate

**Role.** Directly attack the remaining proportional bound

\[
 B_n:=A_n-\lambda_n\le {1501\over2002}A_n\qquad(n\ge150)
 \tag{1}
\]

from the flag form of `104_30`, with no operator norm or absolute values
of the prime–pole form. First the most direct domination of its Toeplitz
coefficients is proved and then refuted with outward arithmetic.
Afterward, a strictly more flexible coercive inequality is extracted: the
positivity of a single adjacent Schur compression for each prefix.

The Schur inequality passes the off-line falsifier and has a large margin
in the diagnostic range, but it is not proved uniformly. Hence this
document proves neither A1 nor RH.

## 1. Non-duplication audit

`103_52` obtained the difference recurrences for the earlier margin
\(2\lambda_n-A_n\). `103_55` certified that its positive-curvature ansatz
fails at \(n=147\). `104_30` built the positive reference
\(\mathsf A_{\rm flag}\), the prime–pole form \(\mathsf Q_0\), and its
coefficients

\[
 q_0=B_1=-\gamma,
 \qquad
 q_d={B_{d+1}-2B_d+B_{d-1}\over2}\quad(d\ge1).               \tag{2}
\]

What is new here is:

1. auditing curvature with the final constant \(501/2002\), not
   \(1/2\), and doing so beyond the threshold \(150\);
2. proving the exact formula for the adjacent compression in the flag
   metric;
3. isolating a single quadratic determinant whose uniform positivity
   suffices to close (1), without requiring the sign of every second
   difference.

No external literature or web search is used in this attack.

## 2. Proportional defect in the correct gauge

Set

\[
 c={501\over2002},\qquad
 \kappa=1-c={1501\over2002},\qquad
 H_n:=\kappa A_n-B_n=\lambda_n-cA_n.                           \tag{3}
\]

Then (1) is exactly \(H_n\ge0\). The flag construction of `104_30` works
unchanged with base \(M=149\): the finite certificate gives
\(A_{149}>0\), and \(\Delta A_k>0\) for \(k\ge149\). We adopt that
one-position extension so that the induction can start at the last
certified index. On that space, define the algebraic form

\[
 \mathsf M:=\kappa\mathsf A_{\rm flag}-\mathsf Q_0.           \tag{4}
\]

For every \(n\ge149\),

\[
 \boxed{\mathsf M[g_n]=H_n.}                                  \tag{5}
\]

So (5) keeps the fixed ray. Neither a supremum of \(\mathsf M\) nor
positivity on the whole space is required.

## 3. First attack: coefficient-by-coefficient domination

Let \(H_0=0\) and write the centered second difference

\[
 \nabla_c^2H_d=H_{d+1}-2H_d+H_{d-1}.                          \tag{6}
\]

Two discrete summations give

\[
 H_n=nH_1+\sum_{d=1}^{n-1}(n-d)\nabla_c^2H_d.                \tag{7}
\]

Hence

\[
 H_1\ge0,\qquad \nabla_c^2H_d\ge0\ (d\ge1)                  \tag{8}
\]

would be a sufficient condition for (1). In the coordinate of `104_30`,
(8) is precisely domination of the Toeplitz coefficients

\[
 q_d(B)\le\kappa q_d(A)\qquad(d\ge1),                         \tag{9}
\]

because

\[
 \kappa q_d(A)-q_d(B)={1\over2}\nabla_c^2H_d.                \tag{10}
\]

This candidate proof takes no absolute values and would be weaker than
requiring positivity of the entire matrix. However, it is false for the
real zeta data, even with the final constant.

### 3.1 Outward counter-certificate past 150

`tools/flag_prefix_curvature_gate.py` reconstructs, with the certified
Hasse–eta generator of `103_51`, the intervals

\[
 H_n=\lambda_n^{\rm prime}+{1501\over2002}A_n.                \tag{11}
\]

With \(K=850\), logarithmic depth \(820\), and scale \(10^{500}\), it
proves

\[
 \boxed{
 -{1058\over10^5}
 <H_{221}-2H_{220}+H_{219}
 <-{10577\over10^6}<0.}                                      \tag{12}
\]

Equivalently,

\[
 \nabla_c^2H_{220}<0,
 \qquad q_{220}(B)>\kappa q_{220}(A).                         \tag{13}
\]

The index lies within the infinite range A1 must control. So lowering the
ratio from \(1/2\) to \(501/2002\) does not rescue curvature induction nor
coefficient-by-coefficient domination. This is a new exact stop-gate; it
does not depend on the FFT diagnostic.

## 4. Exact adjacent compression

Failure of (8) does not prevent the accumulated energy \(H_n\) from being
positive. To preserve that accumulation, consider only the plane

\[
 \mathcal P_n=\mathrm{span}\,\{g_n,\phi_n\},\qquad n\ge149. \tag{14}
\]

The two vectors are orthogonal for \(\mathsf A_{\rm flag}\), and

\[
 \mathsf A_{\rm flag}[\phi_n]=\Delta A_n.                    \tag{15}
\]

The Toeplitz identity (2) gives, with no estimate at all,

\[
 \begin{aligned}
 \mathsf Q_0(g_n,g_n)&=B_n,\\
 \mathsf Q_0(\phi_n,\phi_n)&=B_1=-\gamma,\\
 \mathsf Q_0(g_n,\phi_n)
 &=\sum_{d=1}^{n}q_d
 ={1\over2}(\Delta B_n-B_1).
 \end{aligned}                                                \tag{16}
\]

Define

\[
 d_n:=\kappa\Delta A_n+\gamma>0.                              \tag{17}
\]

Since \(B_n=\kappa A_n-H_n\), equations (4), (16)–(17) produce the exact
matrix

\[
 \boxed{
 \mathsf M|_{\mathcal P_n}=
 \begin{pmatrix}
 H_n&-\frac12(H_n+d_n-H_{n+1})\\
 -\frac12(H_n+d_n-H_{n+1})&d_n
 \end{pmatrix}.}                                              \tag{18}
\]

No operator tail appears: (18) uses only two adjacent rays and the exact
scalar values.

## 5. Sufficient adjacent-Schur theorem

Set

\[
 \boxed{
 \mathcal T_n
 :=4H_nd_n-(H_n+d_n-H_{n+1})^2
 =4(\kappa A_n-B_n)(\kappa\Delta A_n+\gamma)
   -(\Delta B_n+\gamma)^2.}                                  \tag{19}
\]

**Proposition.** If

\[
 \mathcal T_n\ge0\qquad(n\ge149),                            \tag{20}
\]

then \(H_n\ge0\) for every \(n\ge149\), and hence (1) is obtained for
every \(n\ge150\).

**Proof.** The finite certificate of `103_51` gives
\(\lambda_{149}-A_{149}/2>0\), and \(A_{149}>0\). Since

\[
 H_{149}=\lambda_{149}-{501\over2002}A_{149}
 =\left(\lambda_{149}-{A_{149}\over2}\right)
   +{250\over1001}A_{149},                                    \tag{21}
\]

one has \(H_{149}>0\). Assume inductively \(H_n\ge0\). By
(17), \(d_n>0\), and (20) says the determinant of (18) is non-negative.
Matrix (18) is then positive semidefinite. Since
\(g_{n+1}=g_n+\phi_n\),

\[
 H_{n+1}=\mathsf M[g_n+\phi_n]\ge0.                           \tag{22}
\]

The induction proves the claim. \(\square\)

In scalar form, (20) is the coercive bound

\[
 \boxed{
 |\Delta B_n+\gamma|
 \le2\sqrt{(\kappa A_n-B_n)(\kappa\Delta A_n+\gamma)}.}     \tag{23}
\]

It is a **slope bound from accumulated energy**, not a curvature sign, a
term-by-term positivity, or an operator norm. Identity (12) does not
refute it.

There is a useful reformulation for the next attack. For \(t\in\mathbb R\),

\[
 g_n+t\phi_n
 =e^{-x/2}\bigl(L_{n-1}^{(1)}(x)+tL_n(x)\bigr),               \tag{24}
\]

and (18) gives

\[
 \mathsf M[g_n+t\phi_n]
 =H_n-t(H_n+d_n-H_{n+1})+t^2d_n.                              \tag{25}
\]

So \(\mathcal T_n\ge0\) is equivalent to non-negativity of (25) for every
\(t\), and it suffices to check it at the optimal taper

\[
 t_n^*={H_n+d_n-H_{n+1}\over2d_n},\qquad
 \mathsf M[g_n+t_n^*\phi_n]={\mathcal T_n\over4d_n}.          \tag{26}
\]

So the front can be attacked as a **tapered** Laguerre family of two
consecutive degrees. It remains a renormalized prime–pole form, but it no
longer requires controlling any vector outside the prefix path.

## 6. Off-line falsifier

Condition (20) is not blind to an off-line zero. Add a functional
quartet with

\[
 w=e^{\alpha+i\theta},\qquad
 \rho=(1-w)^{-1},\qquad
 0<\alpha<\theta^2/4,\qquad \theta={2\pi\over q},              \tag{27}
\]

where \(q>149\) is prime. For \(\alpha\) sufficiently small the quartet
lies in \(0<\Re\rho<1/2\), and its contribution is

\[
 L_n^{\rm off}=4-4\cosh(n\alpha)\cos(n\theta).                \tag{28}
\]

For the finite set \(n\le149\), (28) converges as
\(\alpha\downarrow0\) to \(4-4\cos(n\theta)>0\); it does not destroy the
base datum. But along the subsequence \(n=kq\),

\[
 L_{kq}^{\rm off}=4-4\cosh(kq\alpha)\longrightarrow-\infty   \tag{29}
\]

exponentially, and dominates \(A_n=O(n\log n)\). Hence the perturbed
margin \(H_n\) crosses from positive to negative. At the first crossing,
\(H_n\ge0\), \(H_{n+1}<0\), and \(d_n>0\); if \(\mathcal T_n\ge0\), (18)
would be positive and (22) would prevent the crossing. Necessarily
\(\mathcal T_n<0\).

So (20) detects the required off-line falsifier: it cannot be deduced
solely from functional symmetry and the archimedean block using a finite
basis. It is not claimed that the artificial quartet preserves an Euler
product with positive von Mangoldt coefficients; that special arithmetic
structure remains precisely the possible input for a proof of (20).

## 7. Verification and observed scale

The same outward certificate that proves (12) gives, at the index where
curvature dies,

\[
 2220.98<\mathcal T_{219}<2220.99.                             \tag{30}
\]

So the Schur successor is not another way of writing the refuted sign.

The uncertified diagnostic
`tools/flag_prefix_adjacent_schur_diagnostic.py`, with two Cauchy radii,
gives for \(149\le n\le500\):

* blocks of negative centered curvature
  \([199,241]\), \([293,336]\), \([383,417]\), \([464,499]\);
* \(\min\mathcal T_n\approx1224.944748587\), at \(n=149\);
* maximum discrepancy between radii of \(5.1\cdot10^{-9}\) in the Li
  coefficients.

These figures only select the successor; they do not prove its uniform
sign.

Reproduced with

```bash
cd 03-research/phase-104-unconditional-a1-closure
python3 tools/flag_prefix_curvature_gate.py --index 219 --K 850 --terms 820
python3 tools/flag_prefix_adjacent_schur_diagnostic.py \
  --nmax 500 --first 149 --fft-power 18
```

## Status

* **Proved:** the exact compression (18), the sufficient criterion
  (19)–(22), and its off-line sensitivity.
* **Certified with intervals:** final-curvature domination fails at
  \(\nabla_c^2H_{220}<0\), past the threshold; simultaneously
  \(\mathcal T_{219}>2220\).
* **Ruled out:** proving (1) via
  \(q_d(B)\le(1501/2002)q_d(A)\) coefficient by coefficient.
* **Live front:** proving (23) for every \(n\ge149\) while keeping the
  prime–pole collision. It is strictly local to the family of prefixes
  and avoids the gapless operator supremum, but it remains an unproved
  RH-strength theorem.
* **Not proved:** (20), A1, and RH.
</content>
