# 104_62 — Unitary Fermi transform and microfrequency gate

**Result.** The Fermi partition of `104_61` admits an exact
representation in which the complete prime–pole block appears inside
unit-modulus phases. This removes the artificial blow-up produced by
separating the exponents of the unbounded partition.

The representation does not by itself give a new bound for zeta. The
obstacle is localized with an explicit constant: a negative excursion of
depth \(Y\) is detected at frequencies \(s=O(Y^{-1})\). In the
rational quadruple \(w=2i\), that window is \(s=O(2^{-n})\). Hence an
attack at a fixed frequency, or with only polynomial resolution in the
degree, misses the signal the partition was built to preserve.

The last audited coordinate does not eliminate \(s\downarrow0\): it uses
the diagonal change \(s=e^{-nv}\). This takes a rate \(Y_n\asymp e^{an}\) to
the fixed point \(v=a\), keeps unitary phases, and aligns its first
variation with the exact Laguerre generating function. But the generating
function only computes the geometric product of phases, while Fermi
requires their arithmetic mean. At the critical scale all Hadamard powers
survive. That is why the diagonal branch is closed as a stop-gate, not as
a successor nor as a proof of A1 or RH.

---

## 1. Notation and arithmetic regulator

Fix \(t>0\),

\[
 b_n=\log(n+1),\qquad x_n=\lambda_n+b_n,\qquad
 H_X=\sum_{n\le X}{1\over n}.                              \tag{1}
\]

The bounded partition is

\[
 \mathfrak F_t(X)={1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+e^{t x_n}}.                                      \tag{2}
\]

For \(\varepsilon>0\), use the convention of `104_61`:

\[
\begin{aligned}
 p_n(\varepsilon)
 &=n\sum_{k=1}^n{n-1\choose k-1}
   {(-1)^{k-1}\over k\varepsilon^k},\\
 \lambda_{n,\varepsilon}
 &=A_n+p_n(\varepsilon)
 -\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).
\end{aligned}                                               \tag{3}
\]

Then

\[
 \lambda_{n,\varepsilon}\longrightarrow\lambda_n
 \qquad(\varepsilon\downarrow0).                            \tag{4}
\]

For each \(\varepsilon>0\), the series of (3) converges absolutely. No
channel will be estimated separately when passing to the boundary.

---

## 2. Fourier formula for the logistic

Let \(\ell(y)=(1+e^y)^{-1}\).

**Lemma 2.1.** For all \(y\in\mathbb R\),

\[
 \boxed{\ell(y)={1\over2}-\int_0^\infty
 {\sin(sy)\over\sinh(\pi s)}\,ds.}                         \tag{5}
\]

The integral is absolutely convergent for each fixed \(y\).

**Proof.** Near zero,
\(\sin(sy)/\sinh(\pi s)\to y/\pi\); at infinity there is exponential
decay. Moreover,

\[
 {1\over\sinh(\pi s)}=2\sum_{j\ge0}e^{-(2j+1)\pi s}
 \qquad(s>0).
\]

Term-by-term integration and the Weierstrass product of
\(\cosh(y/2)\) give

\[
 \int_0^\infty{\sin(sy)\over\sinh(\pi s)}\,ds
 =2y\sum_{j\ge0}{1\over(2j+1)^2\pi^2+y^2}
 ={1\over2}\tanh{y\over2}.
\]

Since \(\ell(y)=(1-\tanh(y/2))/2\), (5) follows. \(\square\)

Define

\[
 \mathcal C_{t,X}(s):={1\over H_X}\sum_{n\le X}{e^{istx_n}\over n}.
                                                                    \tag{6}
\]

The outer sum is finite, so (5) implies exactly

\[
 \boxed{\mathfrak F_t(X)={1\over2}-\int_0^\infty
 {\mathrm{Im}\,\mathcal C_{t,X}(s)\over\sinh(\pi s)}\,ds.}
                                                                    \tag{7}
\]

This is not a linearization: \(\lambda_n\) remains inside the phase.

---

## 3. Exact unitary prime–Laguerre product

Before taking the boundary, set

\[
\boxed{
\begin{aligned}
 \mathcal C_{t,X,\varepsilon}(s)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 &e^{ist(A_n+b_n+p_n(\varepsilon))}\\[-2mm]
 &\times\prod_{m\ge2}
 \exp\!\left(-{ist\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right).
\end{aligned}}                                               \tag{8}
\]

Each factor of the product has modulus one. For \(\varepsilon>0\), its
logarithm is absolutely summable by `104_61`, (20b). By (3),

\[
 \mathcal C_{t,X,\varepsilon}(s)
 ={1\over H_X}\sum_{n\le X}{e^{ist(\lambda_{n,\varepsilon}+b_n)}\over n},
 \qquad |\mathcal C_{t,X,\varepsilon}(s)|\le1.              \tag{9}
\]

For fixed \(X\), (4) gives uniform convergence on compact sets of \(s\).
It also allows passing to the limit inside (7): for small \(\varepsilon\)
the finitely many \(\lambda_{n,\varepsilon}+b_n\), \(n\le X\), are
uniformly bounded, which dominates the integrand near zero; at infinity
\(|\mathcal C|\le1\) and the decay of \(1/\sinh(\pi s)\) are used. Thus,

\[
 \boxed{\mathfrak F_t(X)={1\over2}
 -\lim_{\varepsilon\downarrow0}\int_0^\infty
 {\mathrm{Im}\,\mathcal C_{t,X,\varepsilon}(s)
 \over\sinh(\pi s)}\,ds.}                                  \tag{10}
\]

The frequency tail is uniformly explicit:

\[
 \int_S^\infty{ds\over\sinh(\pi s)}
 ={1\over\pi}\log\coth{\pi S\over2}.                        \tag{11}
\]

Hence (8) solves a real conditioning problem of (20c): no
giant products appear that must then be canceled. It does not solve the
region \(s\downarrow0\).

To separate the baseline, let

\[
 \mathcal D_{t,X}(s)={1\over H_X}\sum_{n\le X}{e^{istb_n}\over n}
 \left(e^{ist\lambda_n}-1\right).                           \tag{12}
\]

Since

\[
 {1\over H_X}\sum_{n\le X}{1\over n(1+(n+1)^t)}\longrightarrow0,
\]

Theorem 3.2 of `104_61` and (7) give the exact equivalence

\[
 \boxed{\mathrm {RH}\iff
 \int_0^\infty{\mathrm{Im}\,\mathcal D_{t,X}(s)
 \over\sinh(\pi s)}\,ds\longrightarrow0.}                  \tag{13}
\]

Equation (13) is an equivalence, not the sought-after estimate.

---

## 4. Quantitative microfrequency theorem

**Theorem 4.1.** Let \(S\ge1\), \(Y\ge\pi S\), and

\[
 J(Y,S):=\int_0^{S/Y}{\sin(sY)\over\sinh(\pi s)}\,ds.
\]

Then

\[
 \boxed{\left|J(Y,S)-{1\over2}\right|
 \le {2\over\pi S}+{\pi S^2\over2Y^2}.}                    \tag{14}
\]

Moreover, for every \(\delta>0\),

\[
 \boxed{\left|\int_\delta^\infty
 {\sin(sY)\over\sinh(\pi s)}\,ds\right|
 \le {2\over Y\sinh(\pi\delta)}.}                          \tag{15}
\]

**Proof.** In (14), set \(u=sY\). For \(0\le u\le S\), put
\(z=\pi u/Y\le1\). The series for \(\sinh z\) gives

\[
 z\le\sinh z\le z(1+z^2),
\]

and hence

\[
 0\le {1\over\pi u}-{1\over Y\sinh(\pi u/Y)}
 \le {\pi u\over Y^2}.                                     \tag{16}
\]

Consequently,

\[
 \left|J(Y,S)-\int_0^S{\sin u\over\pi u}\,du\right|
 \le{\pi S^2\over2Y^2}.
\]

Integration by parts gives
\(\left|\int_S^\infty\sin u/u\,du\right|\le2/S\), and
\(\int_0^\infty\sin u/u\,du=\pi/2\). This proves (14).

For (15), apply integration by parts to
\(f(s)=1/\sinh(\pi s)\). The function is positive, decreasing, and tends
to zero; the boundary term and the total variation of \(f\) each cost at
most \(f(\delta)/Y\). \(\square\)

If \(x=-Y\), then

\[
 \ell(-Y)={1\over2}+\int_0^\infty
 {\sin(sY)\over\sinh(\pi s)}\,ds.
\]

Equation (14) says that, first letting \(Y\to\infty\) and then
\(S\to\infty\), all the saturation \(\ell(-Y)\to1\) is already encoded in
\(0<s<S/Y\). The relevant frequency is inverse to the depth, not to
the degree.

### 4.1 Rational falsifier

For the quadruple of `104_17`, \(w=2i\),

\[
 Q_n=4-2\mathrm{Re}(w^n+w^{-n}),
\]

and, if \(n\equiv0\pmod4\),

\[
 Q_n=4-2(2^n+2^{-n}).                                      \tag{17}
\]

With \(Y_n=-(Q_n+\log(n+1))\), the bound
\(\log(n+1)\le n\) gives, for \(n\equiv0\pmod4\), \(n\ge4\),

\[
 \boxed{Y_n\ge2^n.}                                        \tag{18}
\]

By (15), for every \(B>0\),

\[
 \left|\int_{n^{-B}}^\infty
 {\sin(sY_n)\over\sinh(\pi s)}\,ds\right|
 \le {2n^B\over\pi2^n}\longrightarrow0.                   \tag{19}
\]

However, \(\ell(Q_n+b_n)\to1\) on that class, of natural and
logarithmic density \(1/4\). Hence

\[
 \boxed{\text{a resolution }s\ge n^{-B}\text{ loses the Fermi detector
 on an exact off-line falsifier}.}                      \tag{20}
\]

This does not forbid estimating the full integral. It does forbid
asserting that the unitarity of (8), together with control away from
zero, closes (13): the omitted part contains exactly the exponential
excursion.

---

## 5. Two positive representations that also fail to close

### 5.1 There is no positive Laplace mixture of the logistic

There is no finite positive measure \(\mu\) on \([0,\infty)\) such that

\[
 \ell(x)=\int_0^\infty e^{-sx}\,d\mu(s)
 \qquad(x\in\mathbb R).                                    \tag{21}
\]

If \(\mu([a,\infty))>0\) for some \(a>0\), the right-hand side grows at
least like \(e^{a|x|}\mu([a,\infty))\) as \(x\to-\infty\), while
\(\ell(x)\to1\). So \(\mu\) would have to be supported at \(0\), which
produces a constant. The majorization \(\ell(x)\le e^{-x}\) does exist,
but it returns exactly the unbounded partition \(\mathcal Z_t\) and its
coefficient-by-coefficient control.

### 5.2 The variational form requires arbitrary degree selectors

Let

\[
 h(q)=-q\log q-(1-q)\log(1-q),\qquad0\le q\le1.
\]

The Fenchel identity

\[
 \log(1+e^{-y})=\sup_{0\le q\le1}\{h(q)-qy\}                \tag{22}
\]

corresponds to the distinct observable

\[
 \mathfrak V_t(X):={1\over H_X}\sum_{n\le X}{1\over n}
 \log(1+e^{-tx_n}).                                        \tag{22a}
\]

We have \(\ell(y)\le\log(1+e^{-y})\). Under RH, the numerator of
\(\mathfrak V_t\) is bounded by
\(\sum_n n^{-1}(n+1)^{-t}<\infty\). If RH is false, an excursion
\(\lambda_n\le-cR^n\) makes a single term grow like
\(R^n/n\). Hence \(\mathfrak V_t(X)\to0\) is also equivalent to RH, but it
is a quantitatively stronger target: it again amplifies individual
spikes and does not keep the Fermi density relaxation.

Formula (22) turns the numerator of (22a) exactly into

\[
\begin{aligned}
 \sup_{\boldsymbol q\in[0,1]^X}\lim_{\varepsilon\downarrow0}
 \Bigg\{&
 \sum_{n\le X}{h(q_n)\over n}
 -t\sum_{n\le X}{q_n(A_n+b_n+p_n(\varepsilon))\over n}\\
 &+t\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 K_{\boldsymbol q,X}(\log m)\Bigg\},                       \tag{23}\\
 K_{\boldsymbol q,X}(u)&:=
 \sum_{n\le X}{q_n\over n}L_{n-1}^{(1)}(u).
\end{aligned}
\]

The equality is exact for \(\mathfrak V_t\), not for \(\mathfrak F_t\):
the outer sum is finite and the supremum separates at each \(n\). Proving
that (23) is \(o(H_X)\) would prove RH via the stronger criterion (22a),
but the formula does not reduce the selectors to a positive radial
family.

Indeed, if \(0<z<1\) and \(y=z/(1-z)\), Laguerre gives

\[
 \boxed{\sum_{n\ge1}{z^n\over n}L_{n-1}^{(1)}(u)
 ={1-e^{-uy}\over u},}                                     \tag{24}
\]

with the value \(y\) at \(u=0\). Also

\[
\begin{aligned}
 \sum_{n\ge1}{z^n\over n}p_n(\varepsilon)
 &=\log\!\left(1+{y\over\varepsilon}\right),\\
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 {1-m^{-y}\over\log m}
 &=\log\zeta(1+\varepsilon)-\log\zeta(1+\varepsilon+y).
\end{aligned}                                               \tag{25}
\]

The first series of (25) initially converges for
\[
 |z|<\min\!\left(1,{\varepsilon\over|1-\varepsilon|}\right)
\]
(with radius \(1\) if \(\varepsilon=1\)); its right-hand side gives the
real continuation over \(0<z<1\). This distinction is mandatory when
\(\varepsilon\downarrow0\): that limit is not interchanged with the
infinite series. The geometric selectors have, within their safe domain,
a closed form. But for the quadruple
(17), `104_17` proves

\[
 \sum_{n\ge1}Q_nz^n>0\qquad(0<z<1/2),                      \tag{26}
\]

while its Fermi partition tends to \(1/4\). Every **positive** mixture of
the safe radial data of (26) keeps the wrong sign and does not control the
supremum of (23), whose optimal selector concentrates on a periodic
class. The generating function (24) is exact; restricting the selectors
to it is not.

---

## 6. Diagonal coordinate by exponential rate

In (5), set, for each term,

\[
 s=e^{-nv},\qquad-\infty<v<\infty.
\]

The Jacobian cancels the harmonic weight and gives

\[
 \boxed{\mathfrak F_t(X)={1\over2}-{1\over H_X}
 \int_{-\infty}^{\infty}\sum_{n\le X}
 {e^{-nv}\sin(t e^{-nv}x_n)\over\sinh(\pi e^{-nv})}\,dv.}  \tag{27}
\]

The integral is absolutely convergent for each \(X\): as
\(v\to-\infty\), the denominator doubly dominates; as
\(v\to\infty\), the sine contributes another factor \(e^{-nv}\).

The regulated arithmetic version uses

\[
\boxed{
\begin{aligned}
 U_{n,\varepsilon}(v)
 :=&\ e^{it e^{-nv}(A_n+b_n+p_n(\varepsilon))}\\
 &\times\prod_{m\ge2}\exp\!\left(
 -{it e^{-nv}\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right),
 \qquad |U_{n,\varepsilon}(v)|=1.
\end{aligned}}                                               \tag{28}
\]

In (27), \(\sin(t e^{-nv}x_n)\) is the limit of
\(\mathrm{Im}\,U_{n,\varepsilon}(v)\). Pole, archimedean block,
primes, and prime powers remain coupled until after applying the
nonlinearity.

If \(Y_n\asymp e^{an}\), its transition is no longer at an
exponentially small frequency:

\[
 e^{-nv}Y_n\asymp1\iff v\asymp a.                           \tag{29}
\]

For \(w=2i\), the boundary is \(v=\log2\).

The first variation in the safe region aligns with

\[
\begin{aligned}
 \sum_{n\ge1}z^nL_{n-1}^{(1)}(u)
 &={z\over(1-z)^2}e^{-uz/(1-z)},\\
 \sum_{n\ge1}{z^n\over n}L_{n-1}^{(1)}(u)
 &={1-e^{-uz/(1-z)}\over u},
 \qquad z=e^{-v}.                                           \tag{30}
\end{aligned}
\]

The higher orders of \(\sin(tz^n x_n)\) retain products among prime
towers and do not reduce to additive cumulants; (27)--(28) fall outside
the classifier of `104_53`.

### 6.1 The nonlinear strip has an explicit width

Use the certified fact that every nontrivial zero satisfies
\(|\mathrm{Im}\,\rho|>14\). If
\(z_\rho=1-1/\rho\), \(\rho=\beta+i\gamma\), then

\[
 |z_\rho|^2
 =1+{1-2\beta\over\beta^2+\gamma^2}
 \ge1-{1\over\gamma^2}>{195\over196}.                       \tag{31}
\]

Set

\[
 r_0=\sqrt{195\over196},\qquad
 v_0=-\log r_0={1\over2}\log{196\over195}<0.00257.           \tag{32}
\]

Li's generating function

\[
 \log\xi\!\left({1\over1-z}\right)-\log\xi(1)
 =\sum_{n\ge1}{\lambda_n\over n}z^n                         \tag{33}
\]

is holomorphic for \(|z|<r_0\). By Cauchy, for every \(r<r_0\)
there is \(M_r<\infty\) such that

\[
 |\lambda_n|\le nM_r r^{-n}.                                \tag{34}
\]

Fix \(\eta>0\), take \(r=r_0e^{-\eta/2}\), and suppose
\(v\ge v_0+\eta\). Then

\[
 e^{-nv}|\lambda_n|\le nM_r e^{-\eta n/2}.                  \tag{35}
\]

The same trivial conclusion holds for \(e^{-nv}b_n\). On every half-line
\(v\ge v_0+\eta\), the full expansion of the sine of (27) converges
uniformly and absolutely after summing in \(n\). The transition of an
off-line exponential mode is confined to

\[
 0\le v\le v_0.                                             \tag{36}
\]

This does not control the total integral: the limits \(v\downarrow0\) and
\(\eta\downarrow0\) are not uniform. It does turn
\(s\asymp e^{-an}\) into a strip of width less than \(0.00257\) without
assuming RH. A higher zero verification would narrow the figure but would
not remove the boundary \(v=0\), and it does not count as closure by a
finite range.

### 6.2 The diagonal generating function only sees the geometric product

The previous limitation can be made exact. For
\(z=e^{-v}\), \(\tau=z/(1-z)\), and

\[
 Q_{n,\varepsilon}:=
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),
\]

equations (24)--(25) give, initially within the common radius of
convergence,

\[
\begin{aligned}
 \sum_{n\ge1}{z^n\over n}Q_{n,\varepsilon}
 &=\log\zeta(1+\varepsilon)
   -\log\zeta(1+\varepsilon+\tau),\\
 \sum_{n\ge1}{z^n\over n}
 \{p_n(\varepsilon)-Q_{n,\varepsilon}\}
 &=\log\!\left(1+{\tau\over\varepsilon}\right)
   -\log\zeta(1+\varepsilon)
   +\log\zeta(1+\varepsilon+\tau).
\end{aligned}                                               \tag{36a}
\]

Call \(\mathscr G_\varepsilon^{\mathrm{cont}}(z)\) the real
continuation given by the right-hand side of the second line.
Consequently,

\[
 \lim_{\varepsilon\downarrow0}
 \mathscr G_\varepsilon^{\mathrm{cont}}(z)
 =\log\{\tau\zeta(1+\tau)\}.                                \tag{36b}
\]

For fixed \(z>0\), the radius of the polar series shrinks like
\(\varepsilon/(1-\varepsilon)\); hence (36b) is **not** an interchange
of the limit with the series written in (36a). It is a continuation
identity. In the domain where the Li series does converge, the linear
identity computes

\[
 \exp\!\left(iu\sum_{n\ge1}{z^n\lambda_n\over n}\right)
 =\prod_{n\ge1}\exp\!\left({iu z^n\lambda_n\over n}\right), \tag{36c}
\]

a **geometric product** of phases. Equation (27) needs, instead, the
**arithmetic mean**

\[
 \sum_{n\le X}
 {z^n\sin(tz^n x_n)\over\sinh(\pi z^n)}.                   \tag{36d}
\]

There is no algebraic step from (36c) to (36d).

The quadruple also shows there is no perturbative truncation at the
boundary. If a dominant mode has rate \(R>1\), then:

* for \(v>\log R\), \(z^n\lambda_n\to0\) and the expansion is safe;
* for \(v=\log R\), every Hadamard power
  \((z^n\lambda_n)^k\) is of order one; a truncation at any fixed
  order leaves a remainder that is not \(o(1)\) by the mere limit
  \(n\to\infty\);
* for \(v<\log R\), the radial series of \(\lambda_n\) does not
  converge. Evaluating (36b) there by analytic continuation is not
  summing the series.

In particular, permuting in that region the infinite sum in \(n\) with
\(\varepsilon\downarrow0\) would precisely assert the absence of the
interior pole \(z_\rho\), i.e. would introduce the RH-strength datum one
wanted to prove. The diagonal coordinate locates the wall, but does not
cross it.

The estimate that would need to be proved remains

\[
 \boxed{\int_{-\infty}^{\infty}\sum_{n\le X}
 {e^{-nv}\mathrm{Im}\,U_{n,0}(v)
  \over\sinh(\pi e^{-nv})}\,dv
 ={1\over2}H_X+o(H_X).}                                    \tag{37}
\]

Here \(U_{n,0}\) means the **paired** limit of (28), never the
factors separately. Equation (37) implies
\(\mathfrak F_t(X)\to0\), hence RH. It is not proved, and (36a)--(36d)
show that the linear generating function does not approximate it at the
critical scale. No successor opens from this branch: controlling all the
Hadamard powers at \(zR=1\) only renames the gap.

---

## 7. Verdict

**Proved.** The unitary formulas (8)--(10), the quantitative
localization (14)--(15), the polynomial-resolution no-go (17)--(20), the
positive-mixture gate (21)--(26), the diagonal representation (27)--(30),
the safe strip (31)--(36), and the product–mean collapse (36a)--(36d).

**Gain.** The blow-up of the exponential partition is not necessary: a
bounded, unitary, high-frequency-truncable prime–Laguerre lift exists.
The microfrequency and the diagonal variable identify exactly where the
obstruction lives.

**Not proved.** Estimate (37), the Fermi limit, A1, or RH. The
microfrequency layer shows why unitarity alone does not suffice; the
diagonal audit prevents presenting (27) as an already-simplified new
front.

---

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 unitary_fermi_microfrequency_check.py
```

The checker uses `Fraction` to verify (17)--(18), the density \(1/4\), and
the Laguerre and pole generating functions coefficient by coefficient. The
integral identity and its bounds are proved in the text; the Fourier
sampling the tool prints is only diagnostic.
