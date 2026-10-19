# 104_92 — Euler tightness gate under Abel--Cesàro smoothings

**Result.** There are two natural smoothings of the global product of
`104_85` that literally preserve the ordinary weights
\(\Lambda(m)\), the normalization at \(s=1\), the zero-freeness of each
approximant, and the zero Poisson logarithmic mean:

1. Riesz--Cesàro means of the prime cutoff;
2. exponential Abel \(e^{-\varepsilon m}\) in the arithmetic size.

Neither one by itself converts the one-sided gate of `104_89` into an
unconditional estimate. For any finite smoothing \(w\), if

\[
 u_w(t)=\log|F_w(1/2+it)|,
 \qquad u(t)=\log|(s-1)\zeta(s)|_{s=1/2+it},
\]

then the exact identity

\[
 \boxed{
 \int (u-u_w)_+\,d\nu
 =D_B+\int(u_w-u)_+\,d\nu,}
 \qquad
 d\nu(t)={dt\over2\pi(t^2+1/4)}.                    \tag{1}
\]

holds. Here \(D_B\ge0\) is the Blaschke defect of `104_89`, and
\(D_B=0\Longleftrightarrow\mathrm{RH}\). Therefore proving that the
left-hand side of (1) tends to zero for either of these families
**would prove RH**, but the smoothing does not lower the content of
the step.

Two exact no-go results are proved.

* The Abel in the logarithmic cutoff is computed in closed form and is
  only a horizontal translation:

  \[
   \eta\int_0^\infty e^{-\eta R}L_R(s)\,dR
   =\log{H(s+\eta)\over H(1+\eta)},
   \qquad H(s)=(s-1)\zeta(s).                         \tag{2}
  \]

  Its unconditional zero-free range reaches \(\eta=1/2\), but it does
  not produce a family \(\eta\downarrow0\): crossing that threshold is
  equivalent to excluding zeros in the shifted half-planes.

* Every regular positive mean, including Cesàro or Abel, can preserve
  intact a Poisson mass leak even though the approximants are
  zero-free and normalized. A continuous Euler model is further
  constructed with positive Mangoldt measure, PNT with error
  \(O(x^\beta)\), a simple pole, and symmetric zeros \(\beta,1-\beta\),
  \(1/2<\beta<1\), for which the one-sided Abel and Cesàro defects
  diverge at least like

  \[
   {\varepsilon^{1/2-\beta}\over\log^2(1/\varepsilon)},
   \qquad
   {X^{\beta-1/2}\over\log^2X},                       \tag{3}
  \]

  respectively.

The model does not live on ordinary prime powers and does not preserve
the exact values \(\Lambda(p^k)=\log p\). It does not refute the real
target. It proves that PNT, positivity, and positive smoothing cannot
prove it. By the uniqueness theorem of `104_88`, a falsifier that
literally preserved all the \(\Lambda(m)\) would be zeta itself and
hence a counterexample to RH.

This document does not prove Deep-\(\Lambda\), A1, or RH. It only
closes the possibility of obtaining the missing step from an
Abel--Cesàro regularization plus a general tightness principle.

---

## 1. All smoothed truncations have zero mean

In the coordinate \(y=\log x\), introduce the signed measure

\[
 d\mathcal M(y)
 =\sum_{m\ge2}{\Lambda(m)\over\log m}\,
       \delta_{\log m}(dy)-{e^y\over y}\,dy.           \tag{4}
\]

The singularity at \(y=0\) always appears multiplied by a function
that vanishes there. For a real weight \(w\) of compact support, or of
sufficient decay, set

\[
 L_w(s)=\int_0^\infty
 w(y)(e^{-sy}-e^{-y})\,d\mathcal M(y),
 \qquad F_w(s)=e^{L_w(s)}.                              \tag{5}
\]

Then \(F_w\) is entire and zero-free in the finite cases considered
below, and \(F_w(1)=1\). On \(s=1/2+it\),

\[
 \Re(e^{-sy}-e^{-y})=e^{-y/2}\cos(ty)-e^{-y}.          \tag{6}
\]

The characteristic function of the Cauchy probability \(\nu\) is

\[
 \int_{\mathbb R}e^{ity}\,d\nu(t)=e^{-|y|/2}.         \tag{7}
\]

By (6)--(7), every mode of (5) has zero mean. Fubini is legitimate for
every finite or exponential weight used here, and gives

\[
 \boxed{\int_{\mathbb R}\log|F_w(1/2+it)|\,d\nu(t)=0.} \tag{8}
\]

Three concrete choices are:

\[
\begin{array}{c|c}
\text{hard cutoff at }R & w_R(y)={\bf1}_{[0,R]}(y),\\[2mm]
\text{Riesz--Cesàro of order }k
  & w_{R,k}(y)=(1-y/R)_+^k,\\[2mm]
\text{Abel at }X=e^R & w_\varepsilon(y)=e^{-\varepsilon e^y}.
\end{array}                                             \tag{9}
\]

The last family is particularly clean:

\[
\begin{aligned}
 L_\varepsilon^{\rm ar}(s)
={}&\sum_{m\ge2}{\Lambda(m)\over\log m}e^{-\varepsilon m}
       (m^{-s}-m^{-1})\\
 &+\int_1^\infty e^{-\varepsilon x}
       {x^{-1}-x^{-s}\over\log x}\,dx.                \tag{10}
\end{aligned}
\]

For each \(\varepsilon>0\), (10) is entire, its exponential never
vanishes, equals one at \(s=1\), uses the literal \(\Lambda(m)\), and
satisfies (8). It is also exactly the Abel average of the hard cutoffs
in the arithmetic variable:

\[
 L_\varepsilon^{\rm ar}(s)
 =\varepsilon\int_1^\infty e^{-\varepsilon X}
       L_{\log X}(s)\,dX.                              \tag{11}
\]

For \(\Re s>1\), dominated convergence gives

\[
 L_\varepsilon^{\rm ar}(s)
 \longrightarrow\log H(s)\qquad(\varepsilon\downarrow0), \tag{12}
\]

with the branch fixed by \(H(1)=1\). VK allows the germ to be
transported up to \(\Re s=1\), but not to a half-plane fixed to its
left, exactly as in `104_85`.

## 2. The one-sided requirement is invariant under smoothing

Let \(u_w(t)=\Re L_w(1/2+it)\), and let \(u\) be the log-modulus of
\(H\). By `104_89`,

\[
 \int u\,d\nu=D_B,
 \qquad \int u_w\,d\nu=0.                              \tag{13}
\]

Defining

\[
 I_w=\int(u-u_w)_+d\nu,
 \qquad J_w=\int(u_w-u)_+d\nu,                         \tag{14}
\]

the identity \(f=f_+-(-f)_+\) proves (1):

\[
 \boxed{I_w=D_B+J_w.}                                  \tag{15}
\]

There is no loss of constants or estimation. In particular:

\[
 I_{w_j}\to0
 \quad\Longrightarrow\quad D_B=0
 \quad\Longleftrightarrow\quad\mathrm{RH}.            \tag{16}
\]

The additional part \(J_{w_j}\to0\) is boundary tightness. It is not a
formal consequence of \(w_j\to1\), of interior convergence, or of the
zero mean.

## 3. The logarithmic Abel is a translation, not an escape

For the hard cutoff \(L_R=L_{w_R}\), set

\[
 \mathcal A_\eta L(s)
 =\eta\int_0^\infty e^{-\eta R}L_R(s)\,dR.             \tag{17}
\]

When \(\Re s+\eta>1\), the integral is absolutely interchangeable and

\[
 \mathcal A_\eta L(s)
 =\int_0^\infty e^{-\eta y}
      (e^{-sy}-e^{-y})\,d\mathcal M(y).                \tag{18}
\]

The discrete part is

\[
 \log\zeta(s+\eta)-\log\zeta(1+\eta),                 \tag{19}
\]

and Frullani's formula gives for the continuous part

\[
 \int_0^\infty
 {e^{-\eta y}-e^{-(s+\eta-1)y}\over y}\,dy
 =\log{s+\eta-1\over\eta}.                            \tag{20}
\]

This proves (2). On the Poisson half-plane \(\Re s>1/2\), the
unconditional derivation covers \(\eta>1/2\); the boundary
\(\eta=1/2\) is obtained by the PNT and a limit from the right. For
\(0<\eta<1/2\), the continuation of (2) has a zero in that half-plane
exactly when there exists \(\rho\) with
\(\Re\rho>1/2+\eta\). Therefore asserting simultaneously

\[
 \mathcal A_\eta L=\log{H(s+\eta)\over H(1+\eta)}
 \quad\text{as a zero-free holomorphic logarithm on }\Re s>1/2          \tag{21}
\]

for a sequence \(\eta\downarrow0\) already excludes all right-hand
zeros. The logarithmic Abel reaches the same RH boundary from another
coordinate; it does not cross it.

## 4. No-go for every regular positive mean

On the disk, set

\[
 C_r(z)={1+rz\over1-rz},
 \qquad
 G_r(z)=\exp\{D[C_r(z)-C_{-r}(z)]\},
 \quad0<r<1.                                            \tag{22}
\]

Each \(G_r\) is zero-free and \(G_r(0)=1\). On the boundary,

\[
 g_r(\theta):=\log|G_r(e^{i\theta})|
 =D\{P_r(\theta)-P_{-r}(\theta)\},                    \tag{23}
\]

where \(P_r\) is the Poisson kernel. All the \(g_r\) have zero mean
and, crucially,

\[
 \mathrm{sgn}\,g_r(\theta)=\mathrm{sgn}\,\cos\theta
 \quad\text{for every }r.                              \tag{24}
\]

Moreover,

\[
 \int(g_r)_+{d\theta\over2\pi}
 =D\left\{{4\over\pi}
   \arctan{1+r\over1-r}-1\right\}\longrightarrow D.  \tag{25}
\]

Let \((a_{N,j})\) be any regular positive summation matrix:
\(a_{N,j}\ge0\), \(\sum_j a_{N,j}=1\), and its mass leaves every fixed
initial segment. If \(r_j\uparrow1\), (24) gives equality, not just a
bound,

\[
 \left(\sum_j a_{N,j}g_{r_j}\right)_+
 =\sum_j a_{N,j}(g_{r_j})_+.                            \tag{26}
\]

By (25), both one-sided mean costs tend to \(D\). This includes Cesàro
\(a_{N,j}=N^{-1}{\bf1}_{j\le N}\) and Abel
\(a_{q,j}=(1-q)q^{j-1}\), \(q\uparrow1\). The geometric means

\[
 \exp\left\{\sum_j a_{N,j}\log G_{r_j}(z)\right\}     \tag{27}
\]

remain holomorphic, normalized, and zero-free. Thus a regular positive
mean does not automatically destroy a signed leak: if the peaks share
the same geometric sign, it preserves it exactly.

The falsifier includes even interior convergence. On every compact
subset of the disk,

\[
 G_r(z)\longrightarrow
 G_*(z):=\exp\{D[C_1(z)-C_{-1}(z)]\}.                  \tag{27a}
\]

The regularity of the matrix transports that limit to (27). The
function \(G_*\) is holomorphic, normalized, and zero-free; except at
the two boundary singular points, \(C_1-C_{-1}\) has zero real part,
so \(\log|G_*|=0\) almost everywhere. Nevertheless, by (25)--(26), the
positive and negative parts of the boundary defect still tend to
\(D\). Not even "zero-free interior limit + regular positive
summation" implies tightness.

## 5. Positive Euler countermodel with PNT

The above no-go is functional. The next one further preserves a
positive continuous Euler channel and a strong PNT.

Fix \(1/2<\beta<1\) and choose \(X_0>1\) large enough that

\[
 X_0^{\beta-1}+X_0^{-\beta}<1.                          \tag{28}
\]

Define the continuous Mangoldt measure

\[
 d\Psi_\beta(x)=
 \begin{cases}
 dx,&1\le x<X_0,\\
 \{1-x^{\beta-1}-x^{-\beta}\}\,dx,&x\ge X_0.
 \end{cases}                                           \tag{29}
\]

It is positive by (28), and

\[
 \Psi_\beta(x)=x+O(x^\beta).                           \tag{30}
\]

In particular, (30) is stronger than a VK-type majorant for large
\(x\). Its centered Mellin transform is

\[
 \int_1^\infty x^{-s}\{d\Psi_\beta(x)-dx\}
 =-{X_0^{\beta-s}\over s-\beta}
  -{X_0^{1-\beta-s}\over s-(1-\beta)}.                \tag{31}
\]

The residues at \(\beta\) and \(1-\beta\) are \(-1\). Define the
normalized

\[
\begin{aligned}
 P_\beta(s)
 =-\int_{X_0}^\infty &(x^{-s}-x^{-1})\\
 &\times {x^{\beta-1}+x^{-\beta}\over\log x}\,dx,
 \qquad H_\beta(s)=e^{P_\beta(s)}                     \tag{32}
\end{aligned}
\]

first for \(\Re s>\beta\), and then by continuation. Since

\[
 P_\beta'(s)
 ={X_0^{\beta-s}\over s-\beta}
 +{X_0^{1-\beta-s}\over s-(1-\beta)},                 \tag{33}
\]

the continuation of \(H_\beta\) has simple zeros at
\(\beta,1-\beta\). The function

\[
 Z_\beta(s)={H_\beta(s)\over s-1}                     \tag{34}
\]

has a simple pole at one and

\[
 -{Z_\beta'\over Z_\beta}(s)
 =\int_1^\infty x^{-s}\,d\Psi_\beta(x).               \tag{35}
\]

Thus the Mangoldt channel is positive, satisfies PNT, and yet has a
symmetric pair off the line.

### 5.1 Quantitative failure of Cesàro

The Cesàro mean of the hard cutoffs at \(X\) inserts the weight
\((1-x/X)_+\). Let \(P_{\beta,X}^{C}\) be the version of (32) with
that weight. At \(s=1/2\),

\[
 -P_{\beta,X}^{C}(1/2)
 \gg {X^{\beta-1/2}\over\log X}.                       \tag{36}
\]

The same bound, with a smaller constant, holds for
\(|t|\le c/\log X\): for \(x\le X\), the phase
\(\cos(t\log x)\) stays positive if \(c\) is small. Since
\(\nu([-c/\log X,c/\log X])\asymp1/\log X\),

\[
 \boxed{
 \int(-\Re P_{\beta,X}^{C}(1/2+it))_+d\nu(t)
 \gg {X^{\beta-1/2}\over\log^2X}\longrightarrow\infty.} \tag{37}
\]

### 5.2 Quantitative failure of Abel

Now insert \(e^{-\varepsilon x}\) into (32) and call the result
\(P_{\beta,\varepsilon}^{A}\). On the window
\(x\asymp\varepsilon^{-1}\),

\[
 -\Re P_{\beta,\varepsilon}^{A}(1/2+it)
 \gg {\varepsilon^{1/2-\beta}\over
          \log(1/\varepsilon)}                         \tag{38}
\]

uniformly for \(|t|\le c/\log(1/\varepsilon)\).
The tail \(x>\varepsilon^{-2}\) is exponentially negligible and the
fixed interval \([X_0,4]\) costs \(O(1)\), so they cannot cancel the
main window. Integrating again against \(\nu\),

\[
 \boxed{
 \int(-\Re P_{\beta,\varepsilon}^{A}(1/2+it))_+d\nu(t)
 \gg {\varepsilon^{1/2-\beta}\over
          \log^2(1/\varepsilon)}\longrightarrow\infty.} \tag{39}
\]

The limit \(H_\beta\) is finite on the critical line. Hence replacing
\(-\Re P_{\beta,\varepsilon}^{A,C}\) by the positive defect between the
limiting log-modulus and the approximant only changes (37)--(39) by a
bounded term. The one-sided gate fails divergently.

Model (29) has no discrete support nor the full functional equation of
zeta. Its role is to falsify the inference

\[
 \text{PNT/VK + positive Mangoldt measure + Abel/Cesàro}
 \Longrightarrow\text{one-sided tightness}.          \tag{40}
\]

`104_90` preserves, in a different construction, support on ordinary
prime powers and a broad functional equation, at the cost of altering
one tower and admitting additional Euler poles. The two falsifiers are
complementary.

## 6. Internal duplication audit

* `104_64` and `104_66` apply Abel to the Li **degree** and the
  prime--Laguerre regulator, not to the Euler cutoff of `104_85`.
* `104_75` poissonizes the degree and obtains the Bessel transform of
  the first moment; it likewise does not smooth the prime cutoff.
* `104_79` works with the zeta law before the logarithm and proves a
  different diagonal uniformity failure.
* `104_85` constructs the global hard cutoff; `104_89` obtains the
  one-sided gate and the individual spikes. Formulas (10)--(11), the
  translation barrier (17)--(21), and the stability of the spikes
  under every regular positive matrix do not appear there.
* E101.060--E101.068 use Abel on the exterior index of another
  current. E101.086--E101.087 study a log-Gaussian energy of the prime
  error. They are precedents of the same tightness wall, but do not
  contain the normalized Euler truncations of (9)--(11).

Therefore this gate does not repeat the Hurwitz/Nyman attack: it does
not use Hurwitz to attempt closure nor introduce a Möbius residual.
Its conclusion is negative and specific to the smoothing of the Euler
cutoff.

## 7. Exact status

It has been proved:

\[
\begin{gathered}
 \text{Riesz--Cesàro and arithmetic Abel preserve zero Poisson mean},\\
 \text{one-sided tightness for the real }\Lambda(m)
   \Longrightarrow\mathrm{RH},\\
 \text{logarithmic Abel}=\text{horizontal translation},\\
 \text{regular positive summation does not eliminate aligned spikes},\\
 \text{PNT + positivity do not imply tightness, even with smoothing}.
\end{gathered}                                           \tag{41}
\]

It has not been proved:

\[
 \int(u-u_{w_j})_+d\nu\longrightarrow0
 \quad\text{for the ordinary weights }\Lambda(m).     \tag{42}
\]

Equation (42) remains an RH-equivalent criterion (with the
corresponding tightness), not an unconditional consequence of the
regularizations.

## 8. Reproduction

From `tools/`:

```bash
python3 abel_cesaro_euler_tightness_check.py
```

The checker verifies the closed one-sided mass of (25), its
preservation under Cesàro/Abel means, the positivity and residues of
model (29)--(31), and the numerical growth of the scales of
(36)/(38). It is a diagnostic check of identities proved above; it
does not certify (42).
