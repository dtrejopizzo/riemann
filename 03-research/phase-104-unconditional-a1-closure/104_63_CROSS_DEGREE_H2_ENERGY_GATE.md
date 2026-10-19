# 104_63 — Cross-degree energy, Parseval (H^2), and Christoffel–Darboux gate

**Question.** Can degree-by-degree control of A1 be avoided by summing a
positive energy of the *complete* coefficient, for example

\[
 \mathcal E_N:=\sum_{N<n\le 2N}{\lambda_n^2\over n},             \tag{1}
\]

and using Parseval or Christoffel–Darboux before separating the pole, the
archimedean block, the primes, and the prime powers?

**Verdict.** Energy (1) gives an exact, quantitative criterion, but not a
new bound. Its Hardy series has an interior pole exactly when RH
fails. The Christoffel–Darboux identity exists and keeps the whole prime
sum together, but its three regulated pieces diverge like
\(\varepsilon^{-4N}\), and only their complete cancellation has a limit.
Hence the positivity of the kernel produces no upper bound: using it
would require estimating the same prime–pole defect that determines
\(\lambda_n\).

This document closes the **bare Parseval/CD** attack. It proves neither
A1 nor RH, and presents no other equivalence as progress toward its proof.

---

## 1. No-duplication audit

The internal search found adjacent background, not this argument:

* `phase-33-dbn/78-transform-between-li-s-criterion.md`, §5.3, raises an individual
  coefficient to \(\lambda_n^2\), with a constant depending on the
  off-line zeros; it neither sums degrees nor obtains an arithmetic
  Parseval;
* `phase-55-two-arrows/173-structural-representation-of-sum-rules.md`, §5.2, studies
  quadratic norms of holomorphic functionals for the zeros' transverse
  energy, not the energy of the Li coefficients;
* `104_28`--`104_30` build the regulated prime–pole form and already prove
  that its two channels cannot be estimated separately. Here that
  collapse is made exact in the direction of the degrees.

In the primary literature cited by the phase, Lagarias gives the growth of
the coefficients under RH and Suzuki represents individual coefficients as
conditional norms. A directed search did not find the dyadic energy
(1). No novelty is claimed: the criterion of the next section is an
elementary consequence of Cauchy–Hadamard and Parseval.

---

## 2. Exact radius and dyadic-energy theorem

Set

\[
 G(z):=z{d\over dz}\log\xi\!\left({1\over1-z}\right)
      ={z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
      =\sum_{n\ge1}\lambda_nz^n.                            \tag{2}
\]

For a nontrivial zero \(\rho\), write

\[
 w_\rho=1-{1\over\rho}.
\]

We have

\[
 |w_\rho|<1\quad\Longleftrightarrow\quad\Re\rho>{1\over2}. \tag{3}
\]

If a zero exists to the right of the line, define

\[
 r_0:=\min_{\Re\rho>1/2}|w_\rho|<1;                          \tag{4}
\]

the minimum exists because \(|w_\rho|\to1\) as
\(|\Im\rho|\to\infty\). Under RH set \(r_0=1\).

**Theorem 2.1 (exact cross-degree growth law).** With (1) and (4),

\[
 \boxed{\displaystyle
  \limsup_{N\to\infty}\mathcal E_N^{1/(4N)}={1\over r_0}.}  \tag{5}
\]

In particular, the following are equivalent:

\[
 \mathrm{RH},\qquad
 \log(1+\mathcal E_N)=o(N),\qquad
 \limsup_N\mathcal E_N^{1/(4N)}=1.                          \tag{6}
\]

Under RH, Lagarias's effective theorem used in `104_02` gives more:

\[
 \mathcal E_N\ll N^2\log^2N.                               \tag{7}
\]

**Proof.** The transformation \(s=1/(1-z)\) sends the unit disk to the
half-plane \(\Re s>1/2\). If \(\rho\) has multiplicity \(m_\rho\), (2)
has at \(w_\rho\) a simple pole of residue

\[
 \mathop{\rm Res}_{z=w_\rho}G(z)=m_\rho w_\rho\ne0.         \tag{8}
\]

Hence the radius of convergence of (2) is exactly \(r_0\). Cauchy–
Hadamard gives

\[
 \limsup_n|\lambda_n|^{1/n}=r_0^{-1}.                       \tag{9}
\]

For the upper bound in (5), fix \(r<r_0\). Cauchy gives
\(|\lambda_n|\le M_r r^{-n}\), whence
\(\limsup_N\mathcal E_N^{1/(4N)}\le r^{-1}\); let
\(r\uparrow r_0\). For the lower bound, take a subsequence attaining (9)
and \(N=\lceil n/2\rceil\). Then \(N<n\le2N\) and
\(\mathcal E_N\ge\lambda_n^2/n\), giving the opposite direction. Under RH,
\(r_0=1\); estimate (7) follows from
\(\lambda_n=\frac12n\log n+O(n)\). \(\square\)

The Abel/Hardy version is equally exact. For \(0<r<r_0\),

\[
 {1\over2\pi}\int_0^{2\pi}|G(re^{it})|^2dt
   =\sum_{n\ge1}\lambda_n^2r^{2n}.                          \tag{10}
\]

If \(W_0=\{w_\rho:|w_\rho|=r_0\}\), the principal expansion (8) gives

\[
 {1\over2\pi}\int_0^{2\pi}|G(re^{it})|^2dt
 ={\sum_{w\in W_0}m_w^2\over1-(r/r_0)^2}+O(1)
 \qquad(r\uparrow r_0<1).                                  \tag{11}
\]

So the hoped-for "Hardy bound" collides literally with the first interior
pole, not with a loss of constants.

---

## 3. Exact arithmetic representation before squaring

Use the convention of `104_61`. For \(\varepsilon>0\), define

\[
\begin{aligned}
 p_n(\varepsilon)
 &=n\sum_{j=1}^n{n-1\choose j-1}{(-1)^{j-1}\over j\varepsilon^j},\\
 Q_{n,\varepsilon}
 &=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
        L_{n-1}^{(1)}(\log m),\\
 \lambda_{n,\varepsilon}
 &=A_n+p_n(\varepsilon)-Q_{n,\varepsilon}.
\end{aligned}                                                \tag{12}
\]

Then \(\lambda_{n,\varepsilon}\to\lambda_n\). Since the outer block
is finite, Parseval gives the rigorous identity

\[
\boxed{
 \mathcal E_N=
 \lim_{\varepsilon\downarrow0}{1\over2\pi}
 \int_0^{2\pi}\left|
 \sum_{N<n\le2N}{\lambda_{n,\varepsilon}\over\sqrt n}e^{int}
 \right|^2dt.}                                               \tag{13}
\]

Formula (13) keeps the archimedean block, the pole, all the
primes, and all the prime powers together until after forming the
square.

There is also a signed-measure form. Let

\[
 d\nu_\varepsilon(x)=e^{-\varepsilon x}\,dx-
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       \delta_{\log m}(dx).                                  \tag{14}
\]

Then

\[
 p_n(\varepsilon)-Q_{n,\varepsilon}
 =\int_0^\infty L_{n-1}^{(1)}(x)\,d\nu_\varepsilon(x).       \tag{15}
\]

This is the exact form of the pole–prime coupling; \(\nu_\varepsilon\)
is signed, not positive.

---

## 4. Christoffel–Darboux exists, but does not bound the limit

Laguerre orthogonality of parameter one is

\[
 \int_0^\infty xe^{-x}L_j^{(1)}(x)L_k^{(1)}(x)dx
 =(k+1)\delta_{jk}.                                          \tag{16}
\]

Hence the weight \(1/n\) of (1) produces exactly the kernel

\[
\begin{aligned}
 \mathcal K_N(x,y)
 &:=\sum_{n=N+1}^{2N}{L_{n-1}^{(1)}(x)L_{n-1}^{(1)}(y)\over n}\\
 &=K_{2N-1}^{(1)}(x,y)-K_{N-1}^{(1)}(x,y),                   \tag{17}
\end{aligned}
\]

where

\[
 K_M^{(1)}(x,y)
 =\sum_{k=0}^M{L_k^{(1)}(x)L_k^{(1)}(y)\over k+1}
 ={L_M^{(1)}(x)L_{M+1}^{(1)}(y)
       -L_{M+1}^{(1)}(x)L_M^{(1)}(y)\over x-y}.              \tag{18}
\]

The last fraction is understood by continuity when \(x=y\).

In particular,

\[
 \sum_{n=N+1}^{2N}{Q_{n,\varepsilon}^2\over n}
 =\sum_{m,\ell\ge2}{\Lambda(m)\Lambda(\ell)\over
 (m\ell)^{1+\varepsilon}}
 \mathcal K_N(\log m,\log\ell).                            \tag{19}
\]

More precisely, if
\[
 a_{m,\varepsilon}={\Lambda(m)\over m^{1+\varepsilon}},
 \qquad
 c_{n,\varepsilon}=A_n+p_n(\varepsilon),
 \qquad
 \mathcal S_{N,\varepsilon}(x)
 =\sum_{n=N+1}^{2N}{c_{n,\varepsilon}\over n}
 L_{n-1}^{(1)}(x),
\]
then the complete regulated energy of (13) is
\[
\boxed{
\begin{aligned}
 \mathcal E_{N,\varepsilon}
 ={}&\sum_{n=N+1}^{2N}{c_{n,\varepsilon}^2\over n}
 -2\sum_{m\ge2}a_{m,\varepsilon}
       \mathcal S_{N,\varepsilon}(\log m)\\
 &+\sum_{m,\ell\ge2}a_{m,\varepsilon}a_{\ell,\varepsilon}
       \mathcal K_N(\log m,\log\ell),
 \qquad
 \mathcal E_N=\lim_{\varepsilon\downarrow0}
       \mathcal E_{N,\varepsilon}.
\end{aligned}}                                               \tag{19a}
\]
So (19a), not only (19), explicitly keeps \(A_n\), the pole, and all the
weights \(\Lambda(m)\) before any estimation.

The series are absolutely convergent for \(\varepsilon>0\). The Gram
positivity of \(\mathcal K_N\) makes (19) nonnegative, but it gives
no upper bound for the signed combination (13).

The failure is quantitative. From (12), for each fixed \(n\),

\[
 p_n(\varepsilon)=(-1)^{n-1}\varepsilon^{-n}
 \bigl(1+O_n(\varepsilon)\bigr),
 \qquad
 Q_{n,\varepsilon}=p_n(\varepsilon)+A_n-\lambda_n+o(1).      \tag{20}
\]

Hence, with the \(c_{n,\varepsilon}\) of (19a),

\[
\begin{aligned}
 \sum_{N<n\le2N}{c_{n,\varepsilon}^2\over n}
   &={\varepsilon^{-4N}\over2N}(1+O_N(\varepsilon)),\\
 \sum_{N<n\le2N}{Q_{n,\varepsilon}^2\over n}
   &={\varepsilon^{-4N}\over2N}(1+O_N(\varepsilon)),\\
 \sum_{N<n\le2N}{c_{n,\varepsilon}Q_{n,\varepsilon}\over n}
   &={\varepsilon^{-4N}\over2N}(1+O_N(\varepsilon)).        \tag{21}
\end{aligned}
\]

However,

\[
 \sum_{N<n\le2N}{(c_{n,\varepsilon}-Q_{n,\varepsilon})^2\over n}
 \longrightarrow\mathcal E_N<\infty.                       \tag{22}
\]

The two positive terms and the cross term of (22) cancel all the
negative powers up to order \(\varepsilon^{-4N}\). A separate estimate
would need relative precision \(O_N(\varepsilon^{4N})\) to recover even
a bound \(O_N(1)\). The triangle inequality, Bessel, or discarding the
cross term instead gives a quantity that diverges like
\(\varepsilon^{-4N}\).

Equivalently, (15)--(18) write the prime–pole square as

\[
 \iint\mathcal K_N(x,y)\,d\nu_\varepsilon(x)d\nu_\varepsilon(y), \tag{23}
\]

but no total-variation bound survives the limit. Controlling (23)
with sign and uniformly in \(N\) would be a new arithmetic theorem; by
Theorem 2.1, a subexponential bound for the **complete** energy already
implies RH.

---

## 5. Closure of the attack

Two useful identities are obtained: complete Parseval (13) and the
cross-degree kernel (17)--(19). The sought-after bound is not obtained.

* The analytic side returns to the interior pole \(w_\rho\), with exact
  rate \(r_0^{-1}\) in (5) and blow-up (11).
* The arithmetic side returns to the prime–pole cancellation: CD only
  controls one of three pieces of size \(\varepsilon^{-4N}\).
* The positivity of the energy eliminates the sign of A1 and hence
  requires an RH-strength upper bound, not an automatic inequality.

**Status:** quantitative no-go for the cross-degree attack based solely
on Parseval, Laguerre orthogonality, or Christoffel–Darboux positivity.
A successor would have to supply a signed estimate of (23) that
preserves the compensation of \(\nu_\varepsilon\); those identities by
themselves do not contain it.
