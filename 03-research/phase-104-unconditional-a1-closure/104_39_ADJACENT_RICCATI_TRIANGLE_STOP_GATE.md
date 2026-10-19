# 104_39 — Adjacent Riccati, discrete triangle, and necessity stop-gate

**Role.** Audit the adjacent sufficient criterion of `104_34`

\[
 \mathcal T_n=4H_nd_n-(H_n+d_n-H_{n+1})^2\ge0,
 \qquad
 H_n=\lambda_n-{501\over2002}A_n,
 \quad
 d_n={1501\over2002}\Delta A_n+\gamma,                 \tag{1}
\]

as a Riccati recurrence, and decide whether its positivity can be the
final goal instead of the scalar inequality \(H_n\ge0\).

The result is precise:

1. (1) is exactly a triangle inequality for
   \(\sqrt{H_n},\sqrt{d_n},\sqrt{H_{n+1}}\), not a recurrence with a new
   sign;
2. it is **strictly stronger** than \(H_n\ge0\): a quartet contribution
   lying entirely on the critical line keeps every margin positive and
   exactly breaks (1);
3. under RH, for the Riemann zeta function, (1) does hold for every
   sufficiently large \(n\), so there is no asymptotic obstruction;
4. consequently, (1) remains a valid sufficient criterion for the real
   zeta function, but it must not be confused with A1 nor treated as a
   necessary condition. Proving it requires additional arithmetic
   regularity that mere critical support and Li positivity do not
   contain.

This document proves neither (1) for zeta, nor A1, nor RH. It does close
the attempt to obtain (1) solely via Riccati algebra, positivity of the Li
coefficients, or term-by-term critical localization.

## 1. Exact factorization: the recurrence is a triangle

Suppose \(H_n\ge0\), \(d_n>0\), and \(H_{n+1}\ge0\), and write

\[
 x_n=\sqrt{H_n},\qquad a_n=\sqrt{d_n},\qquad x_{n+1}=\sqrt{H_{n+1}}.
\]

The algebraic identity

\[
\boxed{
 \mathcal T_n=
 \bigl((x_n+a_n)^2-x_{n+1}^2\bigr)
 \bigl(x_{n+1}^2-(x_n-a_n)^2\bigr)}                         \tag{2}
\]

proves the equivalences

\[
\boxed{
 \mathcal T_n\ge0
 \iff |x_n-a_n|\le x_{n+1}\le x_n+a_n}                     \tag{3}
\]

and

\[
\boxed{
 (\sqrt{H_n}-\sqrt{d_n})^2
 \le H_{n+1}\le
 (\sqrt{H_n}+\sqrt{d_n})^2.}                               \tag{4}
\]

When \(H_nd_n>0\), there is therefore a parameter

\[
 u_n={H_n+d_n-H_{n+1}\over2\sqrt{H_nd_n}}
\]

such that

\[
\boxed{
 H_{n+1}=H_n+d_n-2\sqrt{H_nd_n}\,u_n,\qquad |u_n|\le1.}   \tag{5}
\]

This is the complete Riccati form. The parameter \(u_n\) receives no
sign from the identity: bounding it by one is exactly the
Cauchy–Schwarz inequality for the compression of `104_34`, not a new
consequence of rewriting it.

In relative variables \(r_n=H_{n+1}/H_n\) and
\(\delta_n=d_n/H_n\), (3) says

\[
 (1-\sqrt{\delta_n})^2\le r_n\le
 (1+\sqrt{\delta_n})^2.                                    \tag{6}
\]

For the expected scale \(H_n\asymp n\log n\), \(d_n\asymp\log n\),
one has \(\delta_n\asymp n^{-1}\). So (1) demands a local
square-root regularity of the margin, in addition to its positivity.

## 2. It is not a necessary condition for the margin

The difference between positivity and adjacent regularity can be
exhibited with an exact critical quartet. Let

\[
 L_n^{\rm crit}=4-4\cos(n\pi/2)\in\{0,4,8,4\}.              \tag{7}
\]

This is the Li contribution of a quartet with \(|w|=1\), and in
particular

\[
 L_n^{\rm crit}\ge0\qquad(n\ge1).                           \tag{8}
\]

Consider first the normalized model

\[
 \widehat H_n=1+L_n^{\rm crit},\qquad \widehat d_n=1.       \tag{9}
\]

Every margin is at least one. However, at \(n=4\),

\[
 \widehat H_4=1,\qquad \widehat H_5=5,\qquad
 \widehat{\mathcal T}_4
 =4-(1+1-5)^2=-5<0.                                         \tag{10}
\]

The same obstruction does not depend on the normalization. Let a base
sequence have \(H_n\ge0\) and let \(d_q>0\) be fixed. Choose
\(q\equiv0\pmod4\). Adding \(M L_n^{\rm crit}\), with integer multiplicity
\(M\ge1\), gives \(L_q^{\rm crit}=0\), \(L_{q+1}^{\rm crit}=4\), and
\(H_n\ge0\) is preserved for every \(n\), but

\[
 \mathcal T_q(M)=4H_qd_q-
   (H_q+d_q-H_{q+1}-4M)^2\longrightarrow-\infty              \tag{11}
\]

as \(M\to\infty\) through the integers.

Hence:

\[
\boxed{
 H_n\ge0\ \hbox{for every }n
 \quad\not\Longrightarrow\quad
 \mathcal T_n\ge0\ \hbox{for every }n.}                   \tag{12}
\]

The example does not claim to be another Euler product: it proves exactly
that the adjacent criterion does not follow from Li positivity, functional
symmetry, and critical support. A proof for zeta must use the special
distribution and weights of its primes; summing positive critical-zero
contributions is not enough.

## 3. The off-line falsifier in rational form

The off-line witness of `104_34` can be made rational. Take

\[
 w={5i\over4},\qquad
 \rho={1\over1-w}={16\over41}+{20\over41}i,                  \tag{13}
\]

so that \(0<\Re\rho<1/2\). The reciprocal functional orbit contributes

\[
 L_n^{\rm off}
 =4-\left(w^n+\bar w^n+w^{-n}+\bar w^{-n}\right).           \tag{14}
\]

For \(n=4k\),

\[
 L_{4k}^{\rm off}
 =4-2\left((5/4)^{4k}+(4/5)^{4k}\right),                    \tag{15}
\]

which is negative and exponential in modulus. Against any polynomial
base, there is then a first crossing \(H_{N-1}\ge0>H_N\). If
\(\mathcal T_{N-1}\ge0\), (4) would force \(H_N\ge0\), a contradiction.
Hence \(\mathcal T_{N-1}<0\).

The attached rational verifier uses base \(n^2\), finds the first
crossing exactly at \(N=28\), and checks the negative determinant with no
floating point.

## 4. Under RH the gate is asymptotically automatic

This section only classifies the logical strength of (1); it is not used
as an unconditional input.

Assume RH. For each zero \(1/2+i\gamma\), \(\gamma>0\), let

\[
 \vartheta_\gamma=2\arctan {1\over2\gamma},
 \qquad 0<\vartheta_\gamma\le {1\over\gamma}.
\]

The positive representation of Li is

\[
 \lambda_n=2\sum_{\gamma>0}
       \bigl(1-\cos(n\vartheta_\gamma)\bigr).                \tag{16}
\]

The difference series converges absolutely and

\[
\begin{aligned}
 |\Delta\lambda_n|
 &\le2\sum_{\gamma>0}
   \min\left\{\vartheta_\gamma,
        {2n+1\over2}\vartheta_\gamma^2\right\}\\
 &\le2\sum_{0<\gamma\le n}{1\over\gamma}
 +(2n+1)\sum_{\gamma>n}{1\over\gamma^2}.                   \tag{17}
\end{aligned}
\]

The classical bound \(N(T)=O(T\log T)\), integrated by parts in (17),
gives

\[
 \boxed{\Delta\lambda_n=O(\log^2 n)\qquad({\rm RH}).}       \tag{18}
\]

On the other hand,

\[
 A_n={n\over2}(\log n+\gamma-1-\log2\pi)+O(\log n),
 \qquad
 \Delta A_n={1\over2}\log n+O(1),                          \tag{19}
\]

and Lagarias's conditional theorem gives

\[
 \lambda_n=A_n+O(\sqrt n\log n).                            \tag{20}
\]

With \(c=501/2002\), \(\kappa=1-c\), it follows that

\[
 H_n={\kappa\over2}n\log n+O(n),\qquad
 d_n={\kappa\over2}\log n+O(1),                            \tag{21}
\]

while

\[
 H_n+d_n-H_{n+1}
 =\Delta A_n+\gamma-\Delta\lambda_n
 =O(\log^2 n).                                               \tag{22}
\]

Finally,

\[
\boxed{
 \mathcal T_n
 =\kappa^2 n\log^2 n
  +O(n\log n+\sqrt n\log^2 n+\log^4 n)>0}                  \tag{23}
\]

for every sufficiently large \(n\) under RH.

The correct conclusion is twofold. The gate is not too strong at the real
asymptotic scale of zeta, but it does add a finite local condition that
RH/positivity alone do not supply. \(\mathcal T_n\ge0\) cannot be declared
equivalent to RH without also certifying all its finite indices.

## 5. Freedom of the reference: formal optimum and circularity

The diagonal flag reference of `104_34` is not the only positive form
interpolating \(A_n\) over the prefixes. This freedom seems to allow
improving the determinant, but its exact optimization shows that it
creates no inequality.

Let \(\mathsf A\) be any positive form with
\(\mathsf A[g_n]=A_n\), and set

\[
 a_n=\mathsf A[\phi_n],\qquad D_n=\kappa a_n+\gamma.
\]

Since \(g_{n+1}=g_n+\phi_n\), one has

\[
 \mathsf A(g_n,\phi_n)={\Delta A_n-a_n\over2}.
\]

For \(\mathsf M=\kappa\mathsf A-\mathsf Q_0\), the compression onto
\(\mathrm{span}\,\{g_n,\phi_n\}\) has diagonal \(H_n,D_n\) and
determinant, multiplied by four,

\[
 F_n(D)=4H_nD-(H_n+D-H_{n+1})^2.                             \tag{24}
\]

As a function of \(D\), this is a concave parabola, and

\[
 \boxed{D_n^{\rm opt}=H_n+H_{n+1},\qquad
        \max_DF_n(D)=4H_nH_{n+1}.}                           \tag{25}
\]

The formal optimum reduces the determinant exactly to the positivity one
wants to propagate. But realizing it requires choosing

\[
 a_n^{\rm opt}={H_n+H_{n+1}-\gamma\over\kappa},              \tag{26}
\]

which already contains \(H_{n+1}\). It is a circular encoding of the
goal, in addition to the global constraints that building a single
positive form with all those diagonals would impose.

There is a fixed extreme reference useful for checking that changing the
gauge likewise supplies no sign. Declare the prefixes \(g_k\) orthogonal
and give them squared norms \(A_k\). This form is positive, and

\[
 a_n=A_n+A_{n+1}.
\]

In the basis \(\{g_n,g_{n+1}\}\), its compression is

\[
 \begin{pmatrix}
 H_n&-\frac12(B_n+B_{n+1}+\gamma)\\
 -\frac12(B_n+B_{n+1}+\gamma)&H_{n+1}
 \end{pmatrix},                                             \tag{27}
\]

because

\[
 \mathsf Q_0(g_n,g_{n+1})
 =B_n+{\Delta B_n+\gamma\over2}
 ={B_n+B_{n+1}+\gamma\over2}.
\]

This produces another sufficient criterion,

\[
 \boxed{
 \mathcal U_n:=4H_nH_{n+1}-(B_n+B_{n+1}+\gamma)^2\ge0.}     \tag{28}
\]

It is not a new theorem about zeta: the critical contribution of Section 2
breaks it for large multiplicity, since the quadratic term in \(M\)
dominates the linear one. Nor does (28) generally order against (1): it
controls the value \(B_n+B_{n+1}\), while (1) controls the slope
\(\Delta B_n\). The choice of reference only moves the difficulty between
those two coordinates.

Hence optimizing the reference metric produces no coercive mechanism. The
optimum is tautological, and fixed references again require an unproved
signed arithmetic inequality.

## 6. Consequence for the Phase 104 front

The minimal induction one wants is only

\[
 H_{n+1}=H_n+d_n-(H_n+d_n-H_{n+1})\ge0.                      \tag{29}
\]

The Schur bound replaces the one-sided requirement of (29) with

\[
 |H_n+d_n-H_{n+1}|\le2\sqrt{H_nd_n},                         \tag{30}
\]

which also controls the unneeded sign and is strictly stronger, as (10)
shows. The Riccati form does not remove that loss.

Hence `104_34` stands as a legitimate sufficient criterion, but not as
the only front. After the Hankel stop-gate of `104_37`, continuing to
seek an abstract proof of (30) via PSD, sum of squares, or positivity of
critical quartets would repeat an already-refuted category. It would only
make sense to return to it if a specific inequality for the weights
\(\log p\) appears that controls the signed slope

\[
 \Delta B_n+\gamma.
\]

In the absence of that input, the mathematically narrower goal remains
the scalar margin \(H_n\ge0\), equivalent to the adopted proportional
ceiling, not the adjacent determinant.

## Verification

```bash
cd 03-research/phase-104-unconditional-a1-closure
python3 tools/adjacent_riccati_gate_check.py
```

The script uses only `Fraction` and verifies (2), the critical witness
(10), the rational point (13), and the first off-line crossing of
Section 3.

## Status

* **Proved:** the triangular equivalences (2)–(6).
* **Proved exactly:** positive margin does not imply the adjacent gate.
* **Proved conditionally:** RH implies the gate for every sufficiently
  large index.
* **Ruled out:** obtaining the gate solely from the Riccati form, Li
  positivity, or term-by-term critical support.
* **Not proved:** the gate for zeta at every \(n\ge149\), A1, and RH.
</content>
