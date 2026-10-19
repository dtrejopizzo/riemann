# 104_104 — Real jets, tangent discs, and the Li-block gate

**Status.** This document directly attacks the proposal of obtaining
consecutive blocks with \(\lambda_n\ge-1\) from the real generating function

\[
 \mathcal F(z):=\log\!\left(2\xi\!\left({1\over1-z}\right)\right)
 =\sum_{n\ge1}{\lambda_n\over n}z^n.                 \tag{1}
\]

The result does not prove RH. It produces three exact conclusions.

1. RH is equivalent to a growth bound on **jets along the real axis** of
   \(\mathcal F\). Hence the real axis loses no information.
2. The Euler series with the ordinary weights \(\Lambda(m)\) proves that
   bound only on the horodisc \(|z-\tfrac12|<\tfrac12\), corresponding to
   \(\Re s>1\). The missing part of the tangent discs is exactly the
   continuation through the critical strip, not an error of one constant.
3. Functional equation, reality, positivity on \(s>1\), order one, and any
   **perturbatively stable** argument that inspects a finite amount of
   real differential data are not enough: there is an explicit factor,
   arbitrarily invisible in that data, that introduces an off-line
   quartet and syndetic negative excursions. The factor does not preserve
   the exact \(\Lambda(m)\); preserving them is impossible by uniqueness
   of the logarithmic derivative.

This rules out a precise family of local attacks. Any input that could
still close the block criterion must use the real \(\Lambda(m)\) globally
and not in a perturbatively stable way.

---

## 1. Non-duplication audit

`104_17` proves that radial Abel positivity of a quartet is compatible
with exponentially negative coefficients. `104_62`, `104_64`, `104_69`,
and `104_75` show that Fejér, Abel, and Fermi do not recover the nonlinear
mean from a fixed radial resolution. `104_56` and `104_61` prove that it
suffices to obtain good blocks of unbounded length.

`104_84` already identifies the Euler horodisc, uniqueness from exact
values, and a symmetric polynomial factor with an off-line quartet.
Neither the horodisc nor the factor of §4 is claimed as new here. They
are reused for a narrower audit: the factor is made quantitatively
invisible in \(C^J\) norm and connected to the syndetic excursions of the
block criterion. The new ingredients relative to that document are the
tangent-radius criterion in real jets, the exact recurrence (12)–(13) with
\(\Lambda(m)\), and the precise localization of which real centers are
already controlled by the horodisc.

Here (1) is not averaged again. The Taylor radius of its **germ at each
real point** is studied, and it is determined exactly which part of that
radius is certified by the ordinary Euler series.

---

## 2. An RH criterion using only real jets

For \(0<r<1\), let \(\mathcal F_r\) be the germ of the real branch of (1) at
\(r\), and define

\[
 \mathscr R(r)^{-1}:=
 \limsup_{k\to\infty}
 \left({|\mathcal F_r^{(k)}(r)|\over k!}\right)^{1/k}. \tag{2}
\]

By Cauchy–Hadamard, \(\mathscr R(r)\) is the radius of convergence of that
germ. Derivatives of positive order do not depend on adding a constant
\(2\pi i\) to the logarithm branch.

**Theorem 2.1 (tangent-disc criterion).** The following are equivalent:

1. RH;
2. for every \(r\in(0,1)\),

   \[
    \boxed{\quad
    \limsup_{k\to\infty}
    \left({|\mathcal F_r^{(k)}(r)|\over k!}\right)^{1/k}
    \le {1\over1-r};\quad}                          \tag{3}
   \]

3. (3) holds for all rationals \(r\in(0,\tfrac12)\).

**Proof.** A zero \(\rho\) of \(\xi\) is transported to

\[
 z_\rho=1-{1\over\rho}.                              \tag{4}
\]

Moreover

\[
 |z_\rho|^2-1={1-2\Re\rho\over|\rho|^2}.            \tag{5}
\]

Under RH all the points (4) lie on \(|z|=1\). Hence
\(\mathcal F\) is holomorphic in the unit disc and the Taylor series at
\(r\) is holomorphic at least in \(D(r,1-r)\). Cauchy–Hadamard gives (3).

Conversely, if RH fails, the symmetry \(\rho\mapsto1-\rho\) provides
a zero with \(\Re\rho>\tfrac12\), and (5) gives a \(z_\rho\) inside the
unit disc. For any

\[
 0<r<{1-|z_\rho|^2\over2(1-\Re z_\rho)}              \tag{6}
\]

one has \(|z_\rho-r|<1-r\). The logarithm has a singularity at
\(z_\rho\), so
\(\mathscr R(r)\le|z_\rho-r|<1-r\), contradicting (3). One can choose
a rational \(r\) smaller than the right-hand side of (6), which also
proves 3 \(\Rightarrow\) 1. \(\square\)

The geometric union used in the proof is

\[
 \boxed{\quad\mathbb D=\bigcup_{0<r<1}D(r,1-r).\quad} \tag{7}
\]

Indeed,

\[
 |z-r|<1-r
 \iff
 r<{1-|z|^2\over2(1-\Re z)},                        \tag{8}
\]

and the right-hand side is positive for every \(|z|<1\).

**Relation to the blocks.** `104_61` proves

\[
 \mathrm {RH}
 \iff
 \lambda_n\ge-1\ \hbox{on consecutive blocks of unbounded length}.
                                                               \tag{9}
\]

Theorem 2.1 is another formulation of the same obstacle: (9) excludes the
syndetic excursions of the coefficients; (3) excludes the interior
singularity that generates them. The theorem does not turn a known local
bound into one on those blocks.

---

## 3. What the weights \(\Lambda(m)\) exactly deliver

Set

\[
 s={1\over1-z},\qquad
 \mathcal A(s)=\log(s(s-1))-{s\over2}\log\pi
                 +\log\Gamma(s/2).                 \tag{10}
\]

For \(\Re s>1\), the absolutely convergent Euler identity is

\[
 \boxed{
 \mathcal F(z)=\mathcal A(s)+
   \sum_{m\ge2}{\Lambda(m)\over\log m}\,m^{-s}.}    \tag{11}
\]

Let \(\mathscr D=s^2\,d/ds=d/dz\). If

\[
 P_0(s,L)=1,\qquad
 P_{k+1}(s,L)=s^2(\partial_s-L)P_k(s,L),             \tag{12}
\]

then, for each \(r\in(0,1)\), \(s_r=(1-r)^{-1}\), and each fixed
\(k\),

\[
 \boxed{
 \mathcal F^{(k)}(r)=
 \mathscr D^k\mathcal A(s_r)+
 \sum_{m\ge2}{\Lambda(m)\over\log m}\,
 m^{-s_r}P_k(s_r,\log m).}                          \tag{13}
\]

The sum converges absolutely. This is an identity with the real ordinary
weights, not a model.

However, its natural domain in the \(z\)-plane is

\[
 \begin{aligned}
 \Omega_E
  &:=\left\{z:\Re{1\over1-z}>1\right\}\\
  &=\boxed{\left\{z:\left|z-{1\over2}\right|<{1\over2}\right\}}.
                                                               \tag{14}
 \end{aligned}
\]

For \(r\ge\tfrac12\), the tangent disc required by (3) satisfies

\[
 D(r,1-r)\subset\Omega_E,                            \tag{15}
\]

because the distance between their centers plus its radius equals
\((r-\tfrac12)+(1-r)=\tfrac12\). Thus, (11) unconditionally proves (3)
for every \(r\ge\tfrac12\).

For \(0<r<\tfrac12\), the Euler series directly guarantees only the
disc \(D(r,r)\subset\Omega_E\), while Theorem 2.1 needs
\(D(r,1-r)\). In terms of (2), the available geometric estimate is

\[
 \mathscr R(r)^{-1}\le {1\over r},                  \tag{16}
\]

against the needed

\[
 \mathscr R(r)^{-1}\le {1\over1-r}.                 \tag{17}
\]

Cancellation of the pole at \(s=1\) extends \(\mathcal F\) across
\(z=0\), but extending all the discs (17) is equivalent, by Theorem 2.1,
to RH. Estimating \(\mathcal A\) and the sum in (11) separately destroys
precisely that cancellation.

### 3.1 Exact translation back to \(\lambda_n\)

When the Taylor series at \(r>0\) contains \(0\) in its disc of
convergence, the exact translation gives

\[
 \boxed{
 \lambda_n={1\over(n-1)!}
 \sum_{j\ge0}{(-r)^j\over j!}\,
 \mathcal F^{(n+j)}(r).}                            \tag{18}
\]

Indeed, the right-hand side is
\(\mathcal F^{(n)}(0)/(n-1)!\). For \(r\) sufficiently small the
hypothesis holds unconditionally, because \(\xi(1)\ne0\).

The alternation in (18) is binding. Neither \(\Lambda(m)\ge0\) in (13),
nor a bound on a finite number of jets, produces a one-sided remainder
for (18). Using (18) without controlling that tail just rewrites
\(\lambda_n\); it does not prove the blocks (9).

---

## 4. Quantitative refinement of the `104_84` falsifier

Fix \(\tfrac12<\beta<1\), \(\gamma>0\), and define

\[
 P_{\beta,\gamma}(s):=
 {\big((s-\beta)^2+\gamma^2\big)
  \big((s-(1-\beta))^2+\gamma^2\big)
  \over
  (\beta^2+\gamma^2)((1-\beta)^2+\gamma^2)}.        \tag{19}
\]

This factor satisfies exactly

\[
 \begin{gathered}
 P_{\beta,\gamma}(1-s)=P_{\beta,\gamma}(s),\qquad
 P_{\beta,\gamma}(\bar s)=\overline{P_{\beta,\gamma}(s)},\\
 P_{\beta,\gamma}(0)=P_{\beta,\gamma}(1)=1,\qquad
 P_{\beta,\gamma}(s)>0\quad(s\in\mathbb R),        \tag{20}
 \end{gathered}
\]

and it has the four zeros

\[
 \beta\pm i\gamma,\qquad1-\beta\pm i\gamma.        \tag{21}
\]

Hence

\[
 \widetilde\xi_{\beta,\gamma}(s)
 :=\xi(s)P_{\beta,\gamma}(s)                       \tag{22}
\]

preserves the functional equation, reality, positivity on the real axis,
the normalization at \(0,1\), and the order-one property of \(\xi\), but
violates RH.

**Theorem 4.1 (invisibility of finite jets).** For every compact
\(K\subset\mathbb R\), every \(J\ge0\), and every \(\varepsilon>0\), one
can choose \(\gamma\) so that

\[
 \max_{0\le j\le J}\sup_{s\in K}
 \left|{d^j\over ds^j}\log P_{\beta,\gamma}(s)\right|
 <\varepsilon.                                      \tag{23}
\]

**Proof.** On a fixed compact set,

\[
 \log\big((s-a)^2+\gamma^2\big)
 =2\log\gamma+\log\left(1+{(s-a)^2\over\gamma^2}\right).
                                                               \tag{24}
\]

After canceling the normalization constants in (19), (24) and each
of its first \(J\) derivatives are \(O_{K,J}(\gamma^{-2})\). \(\square\)

This is not merely adding abstract zeros. Set, for each zero \(\eta\)
of (19),

\[
 u_\eta={\eta\over\eta-1}.
\]

If \(u_{\beta+i\gamma}=Re^{i\theta}\), then \(R>1\) and the contribution
of factor (19) to the Li coefficients is

\[
 \boxed{
 Q_n=4-2(R^n+R^{-n})\cos(n\theta).}                 \tag{25}
\]

The returns of \(n\theta\) to a neighborhood of \(0\) are syndetic
(periodic if \(\theta/2\pi\in\mathbb Q\), and syndetic by minimality
of the rotation otherwise). At those returns, \(Q_n\) is negative
and exponential. In particular, the symmetries and all the local data
listed in (20), even perturbed by less than any finite \(\varepsilon\)
in (23), are compatible with the exact obstruction that prevents the
blocks of `104_61`.

The full sequence of (22) also has syndetic negative excursions: if the
original \(\xi\) already has an exterior mode, the dominant-mode theorem
of `104_56` applies; if it does not, (25) dominates its subexponential
part. This property is not being attributed to the original \(\xi\), but
to the perturbed completion (22).

A rational witness is \(u=2i\), corresponding to
\(\rho=u/(u-1)=(4-2i)/5\). Then

\[
 Q_n=4-2(2^n+2^{-n})\cos{\pi n\over2},              \tag{26}
\]

and \(Q_{4k}<0\) for every \(k\ge1\): every block of four indices contains
a negative excursion.

### 4.1 Exact interpolation of any finite family of jets

The closeness of (23) can be strengthened to exact equality if only the
qualitative axioms of the real axis are kept. Let

\[
 \mathcal S=\{s_1,\ldots,s_J\}\subset(1,\infty),
 \qquad K_1,\ldots,K_J\ge0.                          \tag{27}
\]

Set \(a_j=s_j-\tfrac12\), choose \(M_0\ge2\) and integers \(M_j\) with
\(2M_j>K_j\), and define

\[
 \begin{aligned}
 \mathcal R(s)
  &:=[s(s-1)]^{2M_0}
    \prod_{j=1}^J
    \left((s-\tfrac12)^2-a_j^2\right)^{2M_j},\\
 \mathcal Q_c(s)&:=1+c\mathcal R(s),\qquad c>0.      \tag{28}
 \end{aligned}
\]

**Theorem 4.2 (exact finite-jet falsifier).** Factor (28)
satisfies

\[
 \begin{gathered}
 \mathcal Q_c(1-s)=\mathcal Q_c(s),\qquad
 \mathcal Q_c(\bar s)=\overline{\mathcal Q_c(s)},\\
 \mathcal Q_c(s)\ge1\quad(s\in\mathbb R),\qquad
 \mathcal Q_c(\tfrac12+iy)>1\quad(y\in\mathbb R),  \tag{29}\\
 {d^k\over ds^k}\log\mathcal Q_c(s_j)=0
 \quad(0\le k\le K_j),                              \tag{30}\\
 \mathcal Q_c(0)=\mathcal Q_c(1)=1.
 \end{gathered}
\]

For \(c\) sufficiently large, \(\mathcal Q_c\) has a zero
\(\rho_c\) with

\[
 {1\over2}<\Re\rho_c<1,
 \qquad \Im\rho_c\ne0.                              \tag{31}
\]

Consequently,
\(\xi(s)\mathcal Q_c(s)\) coincides **exactly** with \(\xi(s)\) on the
logarithmic jets prescribed by (27), preserves the functional equation,
reality, real positivity, normalization, and order one, but has zeros
off the line.

**Proof.** Writing \(t=s-\tfrac12\), each factor of
\(\mathcal R\) is an even power of \(t^2-a^2\). This proves the symmetry
and \(\mathcal R(s)\ge0\) on the real axis. On the critical line,
\(t=iy\), every \(t^2-a^2\) is a negative real number and its even
powers are positive; hence (29). At \(s_j\), \(\mathcal R\) has a zero
of order at least \(2M_j\). Since
\(\log(1+c\mathcal R)=c\mathcal R+O(\mathcal R^2)\), (30) follows. The
factor \([s(s-1)]^{2M_0}\) proves the normalization.

Near \(s=1\), write
\(\mathcal R(s)=(s-1)^{2M_0}C(s)\), with \(C(1)>0\). The roots of
\(1+c\mathcal R(s)=0\) have the expansions

\[
 s=1+c^{-1/(2M_0)}C(1)^{-1/(2M_0)}
 e^{(2\ell+1)\pi i/(2M_0)}
 +o\!\left(c^{-1/(2M_0)}\right).                    \tag{32}
\]

Choose a phase with negative cosine and nonzero sine. For \(c\) large,
the corresponding root satisfies (31). Expansion (32) is obtained by
Rouché after the rescaling
\(s-1=c^{-1/(2M_0)}w\). \(\square\)

The composition \(s=(1-z)^{-1}\) does not alter (30): by the chain
rule, the jets at \(z_j=1-1/s_j\) also coincide up to order \(K_j\).

There is an essential caveat. Although (28) has no zeros on the real
axis nor on the critical line, it may have other zeros with \(\Re s>1\).
Hence Theorem 4.2 falsifies deductions made from **finitely many real
jets plus qualitative axioms**, but not a deduction using the full
Euler identity over all of \(\Re s>1\). Factor (19) does keep its zeros
within the strip, but there we obtain arbitrary closeness, not exact
equality.

### 4.2 Why these falsifiers do not supplant the ordinary primes

Factor (19) changes the logarithmic derivative and does not preserve the
weights \(\Lambda(m)\). This is not a limitation that another factor with
the same weights could repair. If, for \(\Re s>1\), two normalized
functions satisfy

\[
 -{Z_1'(s)\over Z_1(s)}
 =\sum_{m\ge2}{\Lambda(m)\over m^s}
 =-{Z_2'(s)\over Z_2(s)},                           \tag{33}
\]

then \((\log Z_1-\log Z_2)'=0\). Normalization as
\(\sigma\to+\infty\) gives \(Z_1=Z_2\) in \(\Re s>1\), and uniqueness of
analytic continuation gives the same global function.

Likewise, exact equality of \(\mathcal F\) and
\(\widetilde{\mathcal F}\) on any open real interval forces global
equality of their germs by the identity theorem. Equation (23) asserts
arbitrary closeness, not equality. **Infinite and exact** values or jets
do contain all the information; the falsifier only rules out the finite,
stable local inference.

Therefore there is no "zero not corresponding to a prime" that
**exactly** preserves the ordinary \(\Lambda(m)\): those weights
determine \(\zeta\), and with the standard archimedean factor fixed they
determine \(\xi\). What remains to be proved is a global property of that
single continuation, not ruling out a second product with the same
coefficients.

---

## 5. Reproducible verification

`tools/real_jet_tangent_disk_gate_check.py` checks:

1. the geometric identities (8), (14), and (15) on a rational grid;
2. symmetry, normalization, and positivity of (19);
3. the \(O(\gamma^{-2})\) decay of the order-\(0,1,2\) jets on a real
   compact set;
4. the rational formula (26) and the presence of an excursion in every
   block of four indices;
5. for a case of (28), equality of jets at the prescribed nodes and
   explicit zeros off the line.

The checker verifies finite algebra and scale diagnostics. The
Cauchy–Hadamard criterion and the uniqueness (33) are proved in the text.

---

## 6. Verdict

\[
 \boxed{
 \begin{gathered}
 \mathrm {RH}
 \iff
 \mathscr R(r)\ge1-r\quad(0<r<1),\\
 \text{Euler--}\Lambda\text{ proves that inequality directly only in }
 |z-\tfrac12|<\tfrac12,\\
 \text{no argument stable under a finite number of real jets can
 complete the missing step.}
 \end{gathered}}                                    \tag{34}
\]

**Proved:** (3), (13), the horodisc geometry, (18), the stable symmetric
and exact finite-jet falsifiers, and uniqueness with exact weights.

**Not proved:** (3) for \(r<\tfrac12\) from the ordinary
\(\Lambda(m)\), existence of the blocks (9), the Deep limit,
A1, or RH.
</content>
