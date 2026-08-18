# 106.47 — The essential threshold and local Gamma compactness

## Purpose

The Evans boundary channel of 106.46 is infinite-dimensional. A Fredholm
matching theory therefore requires compactness after the asymptotic
channels have been removed. This note proves the two estimates responsible
for that compactness:

1. the Gamma small-jump form is locally compact because it controls a
   logarithmic Fourier weight; and
2. the literal prime measure gives a Dirichlet tail floor tending to
   \(1/2\), directly by PNT.

Consequently spectrum below \(1/2\) is discrete with finite multiplicity.
The global problem is reduced from arbitrary subthreshold spectrum to
isolated bound states.

## 1. Local logarithmic coercivity from Gamma

Fix bounded intervals \(I\Subset I'\). Choose \(u_0>0\) so that
\(x,x-u\in I'\) whenever \(x\in I\) and \(0<u<u_0\). Since \(K>0\) is
smooth, there is \(k_{I'}>0\) such that \(K\ge k_{I'}\) on \(I'\).
Moreover,

\[
 g(u)=\frac{e^{-u/2}}{1-e^{-2u}}\ge\frac{c_0}{u}
 \qquad(0<u<u_0).                                    \tag{1}
\]

For \(f\in C_c^\infty(I)\), the Gamma form therefore satisfies

\[
 \mathscr E_\Gamma(f)
 \ge c_I\int_0^{u_0}\frac{\|f-\tau_uf\|_2^2}{u}\,du. \tag{2}
\]

Plancherel gives

\[
\begin{aligned}
 \int_0^{u_0}\frac{\|f-\tau_uf\|_2^2}{u}\,du
 &=2\int_{\mathbb R}|\widehat f(\xi)|^2
 \left(\int_0^{u_0}\frac{1-\cos(u\xi)}u\,du\right)
 \frac{d\xi}{2\pi}.                                  \tag{3}
\end{aligned}
\]

The elementary bound

\[
 \int_0^{u_0}\frac{1-\cos(u\xi)}u\,du
 \ge c_1\log(2+|\xi|)-C_{u_0}                         \tag{4}
\]

follows by integrating over the disjoint subintervals on which
\(1-\cos(u\xi)\ge1/2\). Hence

\[
\boxed{
 \mathscr E_\Gamma(f)+C_I\|f\|_2^2
 \ge c_I'\int_{\mathbb R}
 \log(2+|\xi|)|\widehat f(\xi)|^2\,d\xi.}             \tag{5}
\]

### Lemma 1 — Local compact embedding

On every bounded interval \(I\), a set bounded in the full form norm

\[
 \|f\|_{L^2(\mu_K)}^2+\mathscr E_K(f)                 \tag{6}
\]

is relatively compact in \(L^2(I)\).

#### Proof

On \(I\), Lebesgue measure and \(\mu_K\) are equivalent with bounded
positive densities. Let \(\chi\in C_c^\infty(I')\) equal one on \(I\).
The commutator produced by replacing \(f\) with \(\chi f\) in the Gamma
form is bounded by the form norm, because
\(|\chi(x)-\chi(x-u)|\ll\min(u,1)\), which is integrable against
\(g(u)\,du\) after squaring. Thus (5) applies uniformly to \(\chi f\).

For \(R>1\),

\[
 \int_{|\xi|>R}|\widehat{\chi f}(\xi)|^2\,d\xi
 \le\frac{C}{\log(2+R)}.                              \tag{7}
\]

The low-frequency restrictions \(\mathbf1_{[-R,R]}\widehat{\chi f}\)
form a bounded set in a fixed band-limited space and are equicontinuous on
\(I\). A finite Fourier mesh followed by (7) proves total boundedness in
\(L^2(I)\). \(\square\)

## 2. The literal PNT tail floor

For \(\varphi\in C_c(\mathbb R)\), define

\[
 S_x(\varphi)
 =e^{-x/2}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   \varphi(x-\log n).                                 \tag{8}
\]

### Lemma 2 — Moving PNT quadrature

For every compactly supported continuous \(\varphi\),

\[
 \boxed{
 S_x(\varphi)\longrightarrow
 \int_{\mathbb R}\varphi(y)e^{-y/2}\,dy
 \qquad(x\to+\infty).}                                \tag{9}
\]

The convergence is uniform on compact subsets of \(C_c\) with common
support and common modulus of continuity.

#### Proof

Write the sum as a Stieltjes integral and put \(y=x-\log t\):

\[
 S_x(\varphi)
 =e^{-x/2}\int t^{-1/2}\varphi(x-\log t)\,d\psi(t).   \tag{10}
\]

On the support of \(\varphi\), \(t\asymp e^x\). The prime number theorem
\(\psi(t)=t+o(t)\), uniformly on every fixed multiplicative interval,
and Stieltjes partial summation replace \(d\psi(t)\) by \(dt\) with
relative error \(o(1)\). The main term is

\[
\begin{aligned}
 e^{-x/2}\int t^{-1/2}\varphi(x-\log t)\,dt
 &=\int\varphi(y)e^{-y/2}\,dy.                        \tag{11}
\end{aligned}
\]

Approximation by a finite piecewise-linear net gives the asserted uniform
version. \(\square\)

Choose \(A>0\) and a continuous cutoff \(0\le\chi_A\le1\), supported in
\([-A-1,A+1]\) and equal to one on \([-A,A]\). Lemma 2 with
\(\varphi=\chi_AK\) gives

\[
 \frac{c_K}{h(x)}
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \chi_A(x-\log n)K(x-\log n)
 \longrightarrow
 2c_K\int\chi_A(y)K(y)e^{-y/2}\,dy.                  \tag{12}
\]

Letting \(A\to\infty\), the right side tends to

\[
 2c_K\int K(y)e^{-y/2}\,dy=2c_K^2=\frac12.           \tag{13}
\]

### Theorem 3 — Dirichlet tail floor

For every \(\varepsilon>0\), there is \(R_\varepsilon\) such that every
smooth even \(f\) supported in
\((-\infty,-R_\varepsilon]\cup[R_\varepsilon,\infty)\) satisfies

\[
 \boxed{
 \mathscr E_K(f)\ge
 \left(\frac12-\varepsilon\right)
 \|f\|_{L^2(\mu_K)}^2.}                              \tag{14}
\]

#### Proof

Take \(A\) so large that the right side of (12) is at least
\(1/2-\varepsilon/2\) for all sufficiently large \(x\). Increase \(R\)
so that the support of \(f\) is disjoint from \([-A-1,A+1]\).

Retain only the nonnegative prime edges for which
\(y=x-\log n\in[-A-1,A+1]\). On those edges \(f(y)=0\), so their squared
difference is \(|f(x)|^2\). Equations (12)--(13), first on the positive
tail and then by reflection on the negative tail, give

\[
 \mathscr E_p(f)
 \ge\left(\frac12-\varepsilon\right)
 \int|f|^2\,d\mu_K.                                  \tag{15}
\]

The omitted prime edges and the whole Gamma form are nonnegative. This
proves (14). \(\square\)

## 3. Essential spectral threshold

Let \(L\) be the self-adjoint generator of 106.41 and let constants be
removed. The local compactness lemma and the tail floor imply:

### Theorem 4 — No essential spectrum below \(1/2\)

\[
 \boxed{\sigma_{\mathrm{ess}}(L|_{\mathbf1^\perp})
 \subset[1/2,\infty).}                               \tag{16}
\]

Hence, after shorting the exact threshold radical,

\[
 \boxed{
 \sigma\!\left(L|_{(1\oplus\mathcal R)^\perp}\right)
 \cap(0,1/2)}
                                                               \tag{17}
\]

consists only of isolated eigenvalues of finite multiplicity, with possible
accumulation only at \(1/2\).

#### Proof

Suppose a spectral interval \(J\Subset(0,1/2)\) had an infinite-dimensional
spectral subspace. Choose an orthonormal sequence \(f_j\) in that subspace.
Its form norms are uniformly bounded. By Lemma 1, after passing to a
subsequence, \(f_j\to0\) in \(L^2([-R,R])\) for every fixed \(R\).

Choose smooth cutoffs \(\eta_R,\chi_R\) with
\(\eta_R^2+\chi_R^2=1\), where \(\eta_R\) vanishes on \([-R,R]\) and
equals one outside \([-R-1,R+1]\). The exact nonlocal IMS identity is

\[
\begin{aligned}
 &\mathscr E_K(\eta_Rf_j)+\mathscr E_K(\chi_Rf_j)
 -\mathscr E_K(f_j)\\
 &\quad=2\mathrm{Re}\,\iint
 \overline{f_j(x)}f_j(y)
 \{1-\eta_R(x)\eta_R(y)-\chi_R(x)\chi_R(y)\}
 \,d\mathfrak j(x,y).                                \tag{18}
\end{aligned}
\]

The factor in braces vanishes unless the cutoff values at the two
endpoints differ. At least one endpoint then lies in a fixed bounded
region (for fixed \(R\)). Cauchy--Schwarz in the edge measure, the uniform
form bound, and local \(L^2\)-convergence show that the right side is
\(o_j(1)\). The Gamma singularity is controlled by
\(|\eta_R(x)-\eta_R(y)|=O(|x-y|)\), and the large prime-power edges are
summable by the double-exponential theta factor. Since the
\(\chi_R\)-energy is nonnegative,

\[
 \mathscr E_K(\eta_Rf_j)
 \le\mathscr E_K(f_j)+o_j(1),                         \tag{18a}
\]

while \(\|\eta_Rf_j\|\to1\).

Apply Theorem 3 to \(\eta_Rf_j\), let \(j\to\infty\), and then
\(R\to\infty\). This gives

\[
 \liminf_j\mathscr E_K(f_j)\ge\frac12,                \tag{19}
\]

contradicting \(\sup J<1/2\). Therefore every spectral projection on
\(J\Subset(0,1/2)\) has finite rank, which is (16). Removing the
\(1/2\)-eigenspace \(\mathcal R\) does not change this conclusion.
\(\square\)

## 4. Consequence for the Evans construction

Theorem 4 supplies the missing discreteness condition. On each compact
\(J\Subset(0,1/2)\), the subthreshold spectral projection has finite rank.
Therefore a local characteristic determinant can be defined by a finite
Riesz projection around \(J\), independently of any finite Euler product.

What remains is not essential-spectrum control. It is the exclusion of the
isolated eigenvalues in (17). Equivalently, the half-line Cauchy-data pair
of 106.46 can fail to be transverse only at a discrete set of real
parameters in \((0,1/2)\).
