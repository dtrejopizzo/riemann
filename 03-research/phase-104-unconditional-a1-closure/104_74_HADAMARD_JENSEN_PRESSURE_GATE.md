# 104_74 — Hadamard semigroup, Jensen–logistic formula, and interior-residue gate

**Result.** The pressure ratio of `104_72` does admit an exact complex
representation. It is not, however, an ordinary functional of Li's
generating function: it appears after applying a **Hadamard exponential**
to its coefficients.

Let

\[
 \mathcal G(z)
 :=z{d\over dz}\log {\xi(1/(1-z))\over\xi(1)}
 =\sum_{n\geq1}\lambda_nz^n.                              \tag{1}
\]

If \(\odot\) denotes the coefficient-wise product, then, formally,

\[
 \mathcal U_t(z)
 :=\mathrm{Exp}_{\odot}(-t\mathcal G)(z)
 =\sum_{k\geq0}{(-t)^k\over k!}\mathcal G^{\odot k}(z)
 =\sum_{n\geq1}e^{-t\lambda_n}z^n.                       \tag{2}
\]

This series has a dichotomy with no intermediate zone:

\[
 \boxed{
 \mathrm {RH}\Longrightarrow \mathcal U_t\text{ is entire of order }2/t,
 \qquad
 \neg\mathrm {RH}\Longrightarrow
 R(\mathcal U_t)=0.}                                      \tag{3}
\]

In particular, for any \(t>0\), (2) having positive radius is already
equivalent to RH.

For the real activities

\[
 z_n={e^{-\lambda_n}\over n+1},\qquad
 D_L(\omega)=\prod_{n\in I_L}(1+\omega z_n),\qquad
 I_L=\{L^2,\ldots,L^2+L-1\},                              \tag{4}
\]

the bounded pressure simultaneously satisfies

\[
 e^{\tau G_L}={D_L(1)\over D_L(e^{-\tau})}                \tag{5}
\]

and an exact Jensen–logistic formula. If

\[
 J_L(R)={1\over2\pi}\int_0^{2\pi}
          \log|D_L(Re^{i\theta})|\,d\theta,
 \qquad
 \kappa(v)={e^v\over(1+e^v)^2},                           \tag{6}
\]

then

\[
 \boxed{
 G_L={1\over\tau}\int_{-\infty}^{\infty}\kappa(v)
 \{J_L(e^{-v})-J_L(e^{-v-\tau})\}\,dv.}                 \tag{7}
\]

The \(\log X\) form has an analogous subharmonic representation via
the radial derivative of a weighted Jensen potential.

The gain is conceptual and exact: the pressure counts, with a logistic
smoothing, zeros of \(D_L\) crossing concentric rings. But (3) locates
the gate. Analytically constructing those determinants from
\(\mathcal G\) requires the Hadamard semigroup to exist on some disk;
that mere existence already excludes all interior poles of Li's
generating function.

A quantitative no-go is also proved. On the rational quadruple
\(w=2i\), any truncation of (2) to \(K_n=o(2^n)\) Hadamard powers loses
a proportion \(1-o(1)\) of the activity in the bad class. If the
truncation is even it also creates a spurious activity in the positive
class; if odd it loses the positivity Jensen requires. To approximate
the activities in both classes one must reach \(K_n\asymp2^n\).

Finally, an unconditional safe contour separates

\[
 \lambda_n=C_{n,N}-
 \sum_{|w_\rho|<r_N}m_\rho w_\rho^{-n},\qquad
 C_{n,N}\ll N^5\log^2N\quad(N\le n\le2N).                \tag{8}
\]

So every exponential rate sits inside the finite sum of interior
residues. Jensen, Poisson, and growth bounds control the contour part;
they do not eliminate that sum. The document obtains an exact
representation and a new gate, not a proof that \(G_L\to0\), A1, or RH.

---

## 1. No-duplication audit

The closest internal background is:

* `104_33`, which proves a boundary–residue formula for the first
  prime–pole moment;
* `104_62`, which observes that at the critical scale all Hadamard
  powers are of order one, but does not build the coefficient-wise
  semigroup;
* `104_63`, which studies the linear \(H^2\) energy of \(\mathcal G\);
* `104_68`--`104_73`, which build the activities, the pressure ratio, and
  their probabilistic or Bernstein representations.

What is new here is the combination of four facts:

1. the zero-radius/entire-function dichotomy for
   \(\mathrm{Exp}_\odot(-t\mathcal G)\);
2. the exact representation of the pressure as a mixture of Jensen
   increments;
3. a safe contour common to a dyadic block, with polynomial exterior
   part;
4. the exact exponential cost of truncating the Hadamard exponential on
   the falsifier.

No novelty is claimed for Jensen's formula, for the Hadamard product,
or for residue computation separately. The contribution is their joint
application to Phase 104's bounded detector.

---

## 2. The Hadamard semigroup of Li's generating function

For two formal series with no constant term,

\[
 f(z)=\sum_{n\ge1}f_nz^n,\qquad
 g(z)=\sum_{n\ge1}g_nz^n,
\]

write

\[
 (f\odot g)(z)=\sum_{n\ge1}f_ng_nz^n.                    \tag{9}
\]

The unit element of this algebra is

\[
 \mathbf1_\odot(z)={z\over1-z}=\sum_{n\ge1}z^n.         \tag{10}
\]

Adopt \(\mathcal G^{\odot0}=\mathbf1_\odot\). Then equality
(2) is rigorous as a formal identity: for each fixed coefficient, the
sum over \(k\) is the ordinary exponential series

\[
 \sum_{k\ge0}{(-t)^k\lambda_n^k\over k!}=e^{-t\lambda_n}.
\]

Moreover

\[
 \mathcal U_t\odot\mathcal U_s=\mathcal U_{t+s},
 \qquad
 \partial_t\mathcal U_t=-\mathcal G\odot\mathcal U_t,
 \qquad
 \mathcal U_0=\mathbf1_\odot.                            \tag{11}
\]

It is a formal diagonal semigroup. The analytic question is whether
\(\mathcal U_t\) even defines a nontrivial holomorphic germ.

### Theorem 2.1 (instantaneous dichotomy)

For each \(t>0\), the following are equivalent:

1. RH;
2. \(\mathcal U_t\) has positive radius of convergence;
3. \(\mathcal U_t\) is entire.

Under these conditions its order as an entire function is exactly
\(2/t\).

**Proof.** Under RH, Lagarias's theorem used in `104_02` gives

\[
 \lambda_n={1\over2}n\log n+O(n).                         \tag{12}
\]

Hence

\[
 \log {1\over e^{-t\lambda_n}}
 ={t\over2}n\log n+O_t(n).                               \tag{13}
\]

The Cauchy–Hadamard criterion shows the radius is infinite. The
classical formula for the order of an entire function
\(F(z)=\sum a_nz^n\),

\[
 \mathrm{ord}\,F
 =\limsup_{n\to\infty}{n\log n\over\log(1/|a_n|)},       \tag{14}
\]

applied to (13), gives \(2/t\).

If RH is false, `104_56` produces \(c>0\), \(R>1\), and an infinite
syndetic set \(D\) such that

\[
 \lambda_n\le-cR^n\qquad(n\in D).                        \tag{15}
\]

On that subsequence,

\[
 \left(e^{-t\lambda_n}\right)^{1/n}
 \ge\exp\!\left({tcR^n\over n}\right)\longrightarrow\infty.
 \tag{16}
\]

So the radius of (2) is zero. This proves the equivalences. \(\square\)

The activity used by the pressure is the coefficient of

\[
 \mathcal Z_t(z)
 :=\sum_{n\ge1}{e^{-t\lambda_n}\over(n+1)^t}z^n.          \tag{17}
\]

The polynomial factor \((n+1)^{-t}\) does not change the dichotomy or
the order. In particular,

\[
 \boxed{\mathrm {RH}\Longleftrightarrow
 R\!\left(\sum_{n\ge1}{e^{-\lambda_n}\over n+1}z^n\right)>0.}
 \tag{18}
\]

The non-RH direction of (18) is much stronger than a singularity
inside the disk: no disk of convergence remains at all.

---

## 3. Finite determinant and Jensen–logistic representation

Set

\[
 x_n=\lambda_n+\log(n+1),\qquad z_n=e^{-x_n}>0.           \tag{19}
\]

The polynomial \(D_L\) of (4) is the determinant of the diagonal
compression

\[
 D_L(\omega)
 =\det_{\ell^2(I_L)}
 \left(I+\omega\mathrm{diag}(z_n)_{n\in I_L}\right).
 \tag{20}
\]

Identity (5) is immediate from `104_72`:

\[
 \tau G_L
 =\sum_{n\in I_L}\log{1+z_n\over1+e^{-\tau}z_n}.
 \tag{21}
\]

All zeros of \(D_L\) are negative real, at
\(-z_n^{-1}\). Jensen gives, for every \(R>0\),

\[
 \boxed{
 J_L(R)=\sum_{n\in I_L}\log^+(Rz_n).}                    \tag{22}
\]

Define the hard detector

\[
 h_\tau(x)
 :={1\over\tau}\int_0^\tau\mathbf1_{\{x+s<0\}}\,ds
 =\begin{cases}
 0,&x\ge0,\\
 -x/\tau,&-\tau<x<0,\\
 1,&x\le-\tau.
 \end{cases}                                              \tag{23}
\]

Equations (19) and (22) give exactly

\[
 {J_L(R)-J_L(e^{-\tau}R)\over\tau}
 =\sum_{n\in I_L}h_\tau(x_n-\log R).                     \tag{24}
\]

Let \(V\) be a standard logistic variable, with density

\[
 \kappa(v)={e^v\over(1+e^v)^2},
 \qquad
 \mathbb P(V<-y)={1\over1+e^y}.                          \tag{25}
\]

Then, by Tonelli,

\[
\begin{aligned}
 \mathbb E h_\tau(x+V)
 &={1\over\tau}\int_0^\tau
   \mathbb P(V<-x-s)\,ds\\
 &={1\over\tau}\int_0^\tau{ds\over1+e^{x+s}}
 =g_\tau(x).                                             \tag{26}
\end{aligned}
\]

Substituting \(R=e^{-v}\) in (24) and averaging with (25) proves (7).
There is no approximation or limit in this identity.

### 3.1 The hard ring criterion

Set

\[
 H_L={J_L(1)-J_L(e^{-\tau})\over\tau}
 =\sum_{n\in I_L}h_\tau(x_n).                            \tag{27}
\]

Under RH, \(x_n\ge\log(n+1)>0\), so \(H_L=0\) for all
\(L\). Under non-RH, the syndetic set of (15) contributes
\(h_\tau(x_n)=1\) in a positive proportion of every large block. Hence,

\[
 \boxed{
 \mathrm {RH}\Longleftrightarrow H_L\longrightarrow0,}
 \qquad
 \neg\mathrm {RH}\Longrightarrow
 \liminf_{L\to\infty}{H_L\over L}>0.                   \tag{28}
\]

Geometrically, \(H_L\) measures the zeros of \(D_L\) that are inside
the unit disk or cross the ring
\(e^{-\tau}<|\omega|<1\), weighted linearly in the logarithm of the
radius.

### 3.2 The \(\log X\) form as a subharmonic potential

For \(X\ge1\), define

\[
 J_X^{\log}(R)
 :=\sum_{n\le X}{1\over n}\log^+(Rz_n).                  \tag{29}
\]

It is the circular average of the finite subharmonic potential

\[
 \omega\longmapsto
 \sum_{n\le X}{1\over n}\log|1+\omega z_n|.
\]

For almost every \(R>0\),

\[
 {d\over d\log R}J_X^{\log}(R)
 =\sum_{\substack{n\le X\\Rz_n>1}}{1\over n}
 =:\mathcal N_X^{\log}(R).                              \tag{30}
\]

Using (25) directly,

\[
\boxed{
 \mathfrak F(X)
 ={1\over H_X}\int_{-\infty}^{\infty}
 \kappa(v)\,\mathcal N_X^{\log}(e^{-v})\,dv.}           \tag{31}
\]

So the finite form of `104_69` is exactly a smoothed radial Riesz
mass. Proving that (31) tends to zero is equivalent to proving that the
weighted mass of zeros of the activity determinants escapes every
fixed logistic ring.

---

## 4. Safe contour and exact residue separation

The function

\[
 \Phi(z)={\xi(1/(1-z))\over\xi(1)}                        \tag{32}
\]

is holomorphic on \(\mathbb D\), but can have zeros there. Its weighted
logarithmic derivative is \(\mathcal G\) of (1). For a nontrivial zero
\(\rho\), set

\[
 w_\rho=1-{1\over\rho}.                                  \tag{33}
\]

At \(w_\rho\), \(\mathcal G\) has residue \(m_\rho w_\rho\).
For a radius \(r<1\) not passing through a zero, define

\[
 C_n(r)={1\over2\pi i}\int_{|z|=r}
 {\mathcal G(z)\over z^{n+1}}\,dz.                       \tag{34}
\]

The residue theorem gives the exact sign

\[
 \boxed{
 \lambda_n=C_n(r)-
 \sum_{|w_\rho|<r}m_\rho w_\rho^{-n}.}                  \tag{35}
\]

Only zeros with \(\Re\rho>1/2\) appear, because

\[
 |w_\rho|^2
 =1+{1-2\Re\rho\over|\rho|^2}.                          \tag{36}
\]

### Theorem 4.1 (safe radius common to a block)

For every sufficiently large \(N\) there is

\[
 r_N\in[1-2/N,1-1/N]                                     \tag{37}
\]

such that, uniformly for \(N\le n\le2N\),

\[
 \boxed{|C_n(r_N)|\ll N^5\log^2N.}                       \tag{38}
\]

The implicit constant is absolute.

**Proof.** Use the standard unconditional bounds

\[
 N_\zeta(T)\ll T\log(T+2),\qquad
 \sum_{|\Im\rho|>T}{m_\rho\over|\rho|^2}
 \ll{\log(T+2)\over T}.                                 \tag{39}
\]

Let \(K_N\) be the number of zeros with \(|\Im\rho|\le2N\), counted
with multiplicity, and set

\[
 \delta_N={1\over4N(K_N+1)}\gg{1\over N^2\log N}.       \tag{40}
\]

Removing from (37) the radius-\(\delta_N\) intervals centered at the
corresponding \(|w_\rho|\) eliminates length less than
\(1/(2N)\). What remains is an \(r_N\) whose circle is at distance at
least \(\delta_N\) from all those poles.

If \(|\Im\rho|>2N\) and \(|w_\rho|<1\), (36) gives

\[
 1-|w_\rho|\le {1\over|\Im\rho|^2}<{1\over4N^2};        \tag{41}
\]

its distance to (37) is \(\gg1/N\). The critical or left zeros
have \(|w_\rho|\ge1\) and satisfy the same conclusion. Hence

\[
 \mathrm{dist}(|z|=r_N,\{w_\rho\})\ge\delta_N.   \tag{42}
\]

On the circle, \(s=(1-z)^{-1}\) satisfies \(|s|\le N\). Moreover

\[
 |s-\rho|
 ={|z-w_\rho|\,|\rho|\over|1-z|}
 \gg\delta_N.                                            \tag{43}
\]

The canonical product of \(\xi\) gives

\[
 {\xi'\over\xi}(s)
 =B+\sum_\rho m_\rho
 \left({1\over s-\rho}+{1\over\rho}\right).           \tag{44}
\]

The zeros with \(|\Im\rho|\le2N\) contribute
\(O(K_N/\delta_N)=O(N^3\log^2N)\). In the tail,
\(|s-\rho|\ge |\Im\rho|-|\Im s|\ge|\Im\rho|/2\); writing the term as
\(s/[\rho(s-\rho)]\) and using (39) gives \(O(\log N)\). Hence

\[
 \sup_{|z|=r_N}\left|{\xi'\over\xi}(s(z))\right|
 \ll N^3\log^2N.                                        \tag{45}
\]

Since

\[
 \mathcal G(z)={z\over(1-z)^2}{\xi'\over\xi}(s(z)),
\]

the supremum of \(|\mathcal G|\) is \(O(N^5\log^2N)\).
Finally, \(r_N^{-n}=O(1)\) for \(n\le2N\), and (34) proves
(38). \(\square\)

Combining (35) and (38) gives (8). The exterior contour is always
subexponential in the degree of the block. Every fixed-rate excursion
comes from the finite sum

\[
 Z_{n,N}:=\sum_{|w_\rho|<r_N}m_\rho w_\rho^{-n}.          \tag{46}
\]

A modulus bound for the contour does not determine the sign of (46).

---

## 5. What Jensen sees of \(\xi\), and what it does not

Applied directly to (32), Jensen gives

\[
 \boxed{
 {1\over2\pi}\int_0^{2\pi}\log|\Phi(re^{i\theta})|\,d\theta
 =\sum_{|w_\rho|<r}m_\rho\log{r\over|w_\rho|}\ge0.}     \tag{47}
\]

Hence RH is equivalent to the left-hand side being zero for every
\(r<1\). Subharmonicity automatically delivers the opposite sign to
what would be needed to conclude that vanishing: it produces (47), not
an upper bound of zero. Growth bounds for \(\xi\) control the size of
the left-hand side, but a positive bound does not exclude a finite
interior mass.

The radial average also does not contain the phases needed to
quantify the pressure. This is seen within the class of divisors
preserving the functional equation and conjugation. Fix \(0<r<1\),
\(a=re^{i\vartheta}\), and set

\[
 \rho_a={1\over1-a},\qquad
 X_a(s)=\prod_{\eta\in
 \{\rho_a,\bar\rho_a,1-\rho_a,1-\bar\rho_a\}}(s-\eta).
 \tag{48}
\]

The polynomial is real and satisfies \(X_a(1-s)=X_a(s)\). Inside the
disk, \(X_a(1/(1-z))/X_a(1)\) has exactly the zeros \(a,\bar a\). So
all its Jensen averages are

\[
 \boxed{J_a(R)=2\log^+(R/r)\qquad(0<R<1),}               \tag{49}
\]

independent of \(\vartheta\). Its Li coefficients, instead, are

\[
 Q_n^{(a)}=4-2(r^n+r^{-n})\cos(n\vartheta).               \tag{50}
\]

With \(r=3/4\), the choices \(\vartheta=\pi/2\) and
\(\vartheta=\pi/3\) have exactly the same datum (49), but

\[
 {G_L^{(\pi/2)}\over L}\longrightarrow{1\over4},
 \qquad
 {G_L^{(\pi/3)}\over L}\longrightarrow{1\over2}.        \tag{51}
\]

In the first case \(\cos(n\vartheta)>0\) on one class out of four; in
the second, on three classes out of six. On those classes (50) tends
exponentially to \(-\infty\), and on the remaining ones it does not
contribute to the pressure.

Equation (51) does not say Jensen is unable to detect an interior zero:
(47) detects it. It says a radial estimate does not control the
density or phase appearing in (7). To prove RH via (47) one would have
to prove directly that its nonnegative mass is zero; that is already
the absence of all interior \(w_\rho\).

---

## 6. Quantitative Hadamard-truncation gate

Define the formal truncation

\[
 \mathcal U_{t,K}(z)
 :=\sum_{k=0}^K{(-t)^k\over k!}\mathcal G^{\odot k}(z).
 \tag{52}
\]

Its degree-\(n\) coefficient is the Taylor polynomial

\[
 [z^n]\mathcal U_{t,K}
 =\sum_{k=0}^K{(-t\lambda_n)^k\over k!}.                  \tag{53}
\]

Use the rational quadruple

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\}.          \tag{54}
\]

For \(4\mid n\), write

\[
 Y_n=-Q_n=2(2^n+2^{-n})-4\ge2^n.                         \tag{55}
\]

If \(K\le tY_n/2\), then

\[
\begin{aligned}
 {\sum_{k=0}^K(tY_n)^k/k!\over e^{tY_n}}
 &=\mathbb P\{\mathrm{Pois}(tY_n)\le K\}\\
 &\le e^{-tY_n/8}.                                       \tag{56}
\end{aligned}
\]

The last inequality is the Chernoff bound with deviation \(1/2\).
So a truncation with \(K_n=o(2^n)\) loses a fraction
\(1-o(1)\) of the true activity \(e^{-Q_n}=e^{Y_n}\) across the whole
bad class.

On the class \(n\equiv2\pmod4\), set
\(Y_n^+=Q_n=4+2(2^n+2^{-n})\). If \(K=o(Y_n^+)\), the last term of
(53) dominates:

\[
 \sum_{k=0}^K{(-tY_n^+)^k\over k!}
 =(-1)^K{(tY_n^+)^K\over K!}\{1+o(1)\}.                  \tag{57}
\]

Indeed, the sum of the absolute ratios of all preceding terms to the
last one is bounded by

\[
 \sum_{j\ge1}\left({K\over tY_n^+}\right)^j=o(1).       \tag{58}
\]

So:

* if \(K\) is even, truncation creates a huge spurious positive
  activity relative to the true one, even on the class where it tends
  to zero (and, if \(K\to\infty\), huge in absolute value too);
* if \(K\) is odd, that activity becomes negative and the determinant
  polynomial loses the negative-real-zero geometry Jensen relies on.

To approximate the true activities with relative error less than a
fixed constant on both classes it is necessary to reach

\[
 \boxed{K_n\gg2^n.}                                      \tag{59}
\]

This scale is also sufficient, up to a constant depending on
\(t\). On the bad class, truncating \(e^x\) after \(K\ge2x\)
terms leaves an exponentially small relative Poisson tail. On
the positive class, the Taylor remainder and

\[
 {e^x x^{K+1}\over(K+1)!}
 \le e^x\left({ex\over K+1}\right)^{K+1}
\]

show, for example, that \(K+1\ge4x\) gives exponentially small
relative error. Since in both classes \(x\asymp_t2^n\), the cost of
a direct Taylor approximation is \(\Theta_t(2^n)\).

In a window \(n\asymp L^2\), the number of Hadamard powers required
is \(\exp(\Theta(L^2))\). This closes fixed, polynomial, and, in
general, \(e^{o(n)}\) truncations. It does not rule out a
non-perturbative identity for the complete semigroup.

---

## 7. Verdict

**Proved.** The radius dichotomy (3), determinant (5), the
Jensen–logistic formula (7), the \(\log X\) potential (31), the safe
contour (35)--(38), the radial Jensen formula (47), the phase falsifier
(49)--(51), and the exponential truncation gate (56)--(59).

**Gain.** The bounded observable has a precise complex interpretation:
it is a logistic average of Jensen masses of finite determinants. All
the exponential rate of the coefficients is moreover separated into
the interior residues, while the contour can be made polynomial over
complete blocks.

**No-go.** Building the determinants from Li's generating function
requires the complete Hadamard exponential. The analytic existence of
that semigroup is already equivalent to RH, and no subexponential-order
truncation passes the quadruple. Jensen applied directly to \(\xi\)
turns the problem into canceling its nonnegative interior mass, without
supplying that cancellation.

**Surviving front.** A non-perturbative identity, specific to the real
weights \(\Lambda(m)\), directly controlling the finite determinant
(20) or the complete prime–pole difference before forming its
activities. It cannot come from a subexponential number of Hadamard
powers nor from a radial modulus bound.

**Not proved.** \(G_L\to0\), \(\mathfrak F(X)\to0\), A1, or RH.

---

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 hadamard_jensen_pressure_check.py
```

The checker verifies the semigroup identity at finite degrees, Jensen
for determinants with positive activities, the logistic mixture (7),
the \(1/4\) and \(1/2\) densities of (51), and the truncation scales of
the quadruple. Theorem 4.1 and the asymptotic equivalences are proved
in the text; they are not certified by sampling.
