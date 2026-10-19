# 104_109 — Low residue, block barrier, and the transport-average gate

**Question.** Combining the block relaxation of `104_67` with the
boundary–residue formula of `104_33`–`104_41`: does averaging the
transport defect over consecutive degrees and using the bound

\[
 |\mathcal B_{n,a}|\leq3n\qquad(a\geq4)                    \tag{1}
\]

suffice to obtain the upper barrier
\(\lambda_n\leq e^{\sqrt n}\) on arbitrarily long blocks?

**Result.** The combination does reduce the criterion, with exponential
margin, to a **finite** sum of exterior residues of height
\(\gamma\leq(2N)^{1/4}\). This is the correct scale for the barrier
\(e^{\sqrt n}\); the scale \(\sqrt n\) corresponds only to the onset of
the radial amplification \(na_\rho\asymp1\), not to this deep threshold.

The linear average over the block, however, does not preserve the
degree-by-degree barrier. A rational quartet with

\[
 w={4i\over5},\qquad
 \rho={1\over1-w}={25+20i\over41}                         \tag{2}
\]

has exponential positive excursions in every class
\(n\equiv2\pmod4\), yet has linearly averaged blocks of arbitrary length
whose average is negative. Moreover, the negative binomial transform of
(1) turns its two dangerous modes into strictly contractive modes and
satisfies \(|T_4b_n|\leq3n\) for every \(n\geq2\). So neither the ordinary
average of the defect nor (1), even though the transform identity
converges absolutely, proves the barrier of `104_67`.

The minimal remaining target is nonlinear: controlling the maximum, or
the positive part, of the full prime–Laguerre form on a block. This
document does not prove that control, nor A1, nor RH.

---

## 1. Internal audit and scope

This attack does not reopen routes already closed:

* `104_65` proves that every fixed linear filter preserves an exterior
  mode or artificially cancels it;
* `104_67` proves that an **upper** barrier on blocks of unbounded length
  is equivalent to RH;
* `104_74` separates, on a block, a polynomial contour from the finite
  sum of interior poles;
* `104_76` absolutely bounds the high-height tail at the deep scale;
* `104_33` and `104_41` identify the transport defect with the
  meromorphic Fejér kernel;
* `104_106` already proves the identity for an arbitrary finite filter,
  the duality with all selectors, and the signed-average gate;
* `104_107` already obtains the Fejér triangular average and its phase
  bound \(O(N/L+1)\), and shows that the exterior residue survives.

What is new here relative to `104_106`–`104_107` is the uniform
localization of the selector in the **low residue** of height
\(O(N^{1/4})\), with the complementary tail separated by an exponential
margin, and the additional gate of the negative binomial transform that
connects directly to the bound at \(a=4\). The averaging example of §5 is
recorded again only because the same quartet also satisfies, absolutely
convergently, the \(a=4\) gate of §6. No bibliographic novelty is claimed
for Li's formula nor for that transform.

---

## 2. Exact identity of the low exterior residue

For a zero \(\rho=\beta+i\gamma\), \(\beta>1/2\), \(\gamma>0\), set

\[
 w_\rho=1-{1\over\rho},
 \qquad
 \mathcal F_n(w)=n+\sum_{d=1}^{n-1}(n-d)(w^d+w^{-d}).     \tag{3}
\]

The algebraic identity of `104_33` is

\[
 {\mathcal F_n(w_\rho)\over\rho(\rho-1)}
 =w_\rho^n+w_\rho^{-n}-2.                                \tag{4}
\]

Let \(\mathscr Z_+(Y)\) be the multiset of zeros with
\(\beta>1/2\), \(0<\gamma\leq Y\), one per right-hand member of positive
ordinate. Define the truncated transport defect

\[
 \boxed{
 D_n(Y):=2\Re\sum_{\rho\in\mathscr Z_+(Y)}
 {m_\rho\mathcal F_n(w_\rho)\over\rho(\rho-1)}.}         \tag{5}
\]

By (4), the summand corresponding to the full functional orbit is

\[
 2m_\rho\Re(w_\rho^n+w_\rho^{-n}-2),                     \tag{6}
\]

which is the negative of that quartet's contribution to the Li
coefficient. If

\[
 C_n(Y)=\sum_{\substack{\rho=1/2+i\gamma\\0<\gamma\leq Y}}
 2m_\rho\{1-\cos(n\theta_\rho)\},
 \qquad w_\rho=e^{i\theta_\rho},                         \tag{7}
\]

and \(H_n(Y)\) is the sum, by complete orbits, over all zeros with
\(\gamma>Y\), Li's formula grouped functionally gives exactly

\[
 \boxed{\lambda_n=-D_n(Y)+C_n(Y)+H_n(Y).}                \tag{8}
\]

RH has not been assumed. Moreover,

\[
 0\leq C_n(Y)\leq4N_\zeta(Y).                            \tag{9}
\]

By Lemma 2.1 of `104_76`, uniformly for \(1\leq n\leq X\) and
\(2\leq Y\leq2X\),

\[
 |H_n(Y)|\ll X\log(X+2)
 \left\{1+\exp\left({X\over2Y^2}\right)\right\}.       \tag{10}
\]

Together with \(N_\zeta(Y)\ll Y\log(Y+2)\), (8)–(10) prove

\[
 \boxed{
 \sup_{n\leq X}|\lambda_n+D_n(Y)|
 \ll Y\log(Y+2)+X\log(X+2)
 \left\{1+e^{X/(2Y^2)}\right\}.}                         \tag{11}
\]

The critical part was kept with its sign in (8); only its modulus was
used for the uniform bound (11).

---

## 3. The minimal block criterion

Take

\[
 X=2N,\qquad Y_N=(2N)^{1/4}.                             \tag{12}
\]

The right-hand side of (11) is

\[
 O\!\left(N\log(N+2)e^{\sqrt{2N}/2}\right)
 =o(e^{\sqrt N}).                                        \tag{13}
\]

Hence there is an absolute \(N_0\) such that, for \(N\geq N_0\),

\[
 \sup_{N\leq n\leq2N}|\lambda_n+D_n(Y_N)|
 \leq{1\over2}e^{\sqrt N}.                              \tag{14}
\]

The constant \(1/2\) is not intrinsic: any fixed constant between
\(0\) and \(1\) works after increasing \(N_0\).

**Theorem 3.1 (low-residue block criterion).** The following are
equivalent:

1. RH;
2. there exist \(N_j\to\infty\) and consecutive intervals
   \(I_j\subset[N_j,2N_j]\), with \(|I_j|\to\infty\), such that

   \[
   \boxed{
   D_n((2N_j)^{1/4})\geq-{1\over2}e^{\sqrt{N_j}}
   \quad(n\in I_j).}                                    \tag{15}
   \]

*Proof.* Under RH, \(\mathscr Z_+(Y)\) is empty for every \(Y\), so
\(D_n(Y)=0\) and (15) holds on any interval.

Conversely, (14)–(15) imply, for \(n\in I_j\),

\[
 \lambda_n\leq-D_n(Y_{N_j})+{1\over2}e^{\sqrt{N_j}}
 \leq e^{\sqrt{N_j}}\leq e^{\sqrt n}.                   \tag{16}
\]

So there are blocks of unbounded length satisfying the upper barrier of
`104_67`, Corollary 2.1, and by that corollary RH holds. \(\square\)

Reduction (15) does not require controlling all the zeros. For level
\(e^{\sqrt n}\), every contribution that could still cross the threshold
has been concentrated in \(\gamma\ll n^{1/4}\). The two other scales that
could be confused with this one are:

* \(\gamma\asymp\sqrt n\), where \(na_\rho\asymp1\) begins;
* \(\gamma\asymp\sqrt{n/\log n}\), where an absolute radial bound drops to
  polynomial size.

For the deep barrier used in `104_67`, the relevant scale is
\(n^{1/4}\), as shown by (10)–(13).

---

## 4. The arithmetic form that would actually need to be bounded

Use exactly the regularization of `104_61` and `104_67`:

\[
\begin{aligned}
 Q_{n,\varepsilon}
 &=\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
      L_{n-1}^{(1)}(\log m),\\
 \lambda_{n,\varepsilon}
 &=A_n+p_n(\varepsilon)-Q_{n,\varepsilon},
 \qquad \lambda_{n,\varepsilon}\longrightarrow\lambda_n.
                                                               \tag{17}
\end{aligned}
\]

For a finite interval \(I\), continuity of the positive part gives

\[
\boxed{
 \sum_{n\in I}(\lambda_n-e^{\sqrt n})_+
 =\lim_{\varepsilon\downarrow0}
 \sum_{n\in I}
 \left(
 A_n+p_n(\varepsilon)
 -\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
       L_{n-1}^{(1)}(\log m)-e^{\sqrt n}
 \right)_+.}                                             \tag{18}
\]

The barrier over the whole block is equivalent to (18) being zero. The
expression preserves the pole, the archimedean block, the primes, the
prime powers, and the Laguerre phase right up until the positive part is
taken. Proving that the right-hand side vanishes on blocks of unbounded
length would close RH via `104_67`.

A linear average does not substitute for (18). The reason is not a lost
inequality, but the following exact falsifier.

---

## 5. Rational falsifier of the block average

Consider (2). One has

\[
 \Re\rho={25\over41}>{1\over2},
 \qquad |w|^2={16\over25}<1.                              \tag{19}
\]

Its quartet's contribution to Li is

\[
 q_n=4-2\Re(w^n+w^{-n}).                                  \tag{20}
\]

Writing \(r=5/4\),

\[
 q_n=
 \begin{cases}
 4-2(r^n+r^{-n}),&n\equiv0\pmod4,\\
 4+2(r^n+r^{-n}),&n\equiv2\pmod4,\\
 4,&n\text{ odd}.
 \end{cases}                                             \tag{21}
\]

In particular, every four consecutive integers contain an index at which

\[
 q_n>2(5/4)^n.                                            \tag{22}
\]

There are no pointwise blocks for the upper barrier. However, for
\(K\geq0\), \(M\geq1\), the exact linear sum is

\[
\begin{aligned}
 \sum_{n=4K+1}^{4K+4M}q_n
 ={}&16M-{2\over1+r^2}
 \left\{
 r^2(r^{4(K+M)}-r^{4K})
 +r^{-4(K+M)}-r^{-4K}
 \right\}.                                               \tag{23}
\end{aligned}
\]

For each \(M\), (23) tends to \(-\infty\) as \(K\to\infty\).
Consequently there are intervals as long and as far away as desired on
which the **average** of \(q_n\) is negative, even though (22) violates
the barrier in every subinterval of length four.

Thus, a bound on

\[
 {1\over|I|}\sum_{n\in I}D_n(Y)                           \tag{24}
\]

does not imply the minimal bound (15). The negative part must be
controlled degree by degree, equivalently the maximum or the positive
part of (18).

---

## 6. Why the bound at \(a=4\) does not repair the average

When the expansion converges, (4a) of `104_41` can be written as the
negative binomial average

\[
 T_aB(n):=\sum_{k\geq n}\pi_{n,k}^{(a)}B_k,
 \qquad
 \pi_{n,k}^{(a)}=a^{-n}{k-1\choose n-1}
 \left(1-{1\over a}\right)^{k-n},                        \tag{25}
\]

with \(\sum_{k\geq n}\pi_{n,k}^{(a)}=1\), and

\[
 \mathcal B_{n,a}=T_aB(n).                               \tag{26}
\]

For a geometric mode \(v^k\),

\[
 \boxed{
 T_a(v^k)(n)=\tau_a(v)^n,
 \qquad
 \tau_a(v)={v\over a-(a-1)v},}                           \tag{27}
\]

if \(|(1-1/a)v|<1\).

In quartet (2), the defect of \(B=A-\lambda\) is

\[
 b_n=-q_n=-4+2\Re(w^n+w^{-n}).                            \tag{28}
\]

For \(a=4\), even the dominant mode lies within the domain of
convergence, since

\[
 {3\over4}|w^{-1}|={15\over16}<1.                         \tag{29}
\]

Nevertheless,

\[
\begin{aligned}
 |4w-3|^2&={481\over25}>1,\\
 |\tau_4(w)|^2&={1\over34},\\
 |\tau_4(w^{-1})|^2&={25\over481},
 \qquad \tau_4(w^{-1})=(4w-3)^{-1}.                      \tag{30}
\end{aligned}
\]

By (27)–(28),

\[
 T_4b(n)=-4+2\Re\{\tau_4(w)^n+\tau_4(w^{-1})^n\}.       \tag{31}
\]

Both modes of (31) are contractive. In particular,

\[
\begin{aligned}
 |T_4b(n)|
 &\leq4+2\left(34^{-n/2}+(25/481)^{n/2}\right)\\
 &\leq4+2\left({1\over34}+{25\over481}\right)<6\leq3n
 \qquad(n\geq2),
\end{aligned}                                             \tag{31a}
\]

that is,

\[
 \boxed{|T_4b(n)|\leq3n\qquad(n\geq2),}                 \tag{32}
\]

while (22) keeps positive excursions of size \((5/4)^n\) with gaps of
four. Transporting down to \(a=4\) has precisely damped the mode that the
barrier was supposed to detect. Inverting it is unstable and crosses the
interior pole of `104_41` again.

Quartet (2) does not have the Euler weights of the ordinary primes.
Hence (19)–(32) do not refute (18) for the real zeta. They do refute the
inference

\[
 |\mathcal B_{n,4}|\leq3n
 \quad+\quad\text{linear average in }n
 \quad\Longrightarrow\quad\text{block barrier}.      \tag{33}
\]

A proof for the real \(\Lambda(m)\) must use arithmetic information not
contained in (1), (25), or the average (24).

---

## 7. Verdict

**Proved.** The low-residue identity (8), the uniform bound (11), the
equivalent block criterion (15), the \(n^{1/4}\) scale, the minimal
prime–Laguerre form (18), the misleading average (23), and the exact
contraction under \(T_4\) (30)–(32).

**Gain.** Returning from the Cramér energy to the Li–Laguerre scaffolding,
the upper barrier is localized to a finite sum of residues of height
\(O(n^{1/4})\), while the entire high block has margin
\(e^{-(1-1/\sqrt2)\sqrt n+O(\log n)}\).

**Exact gate.** `104_67` requires an inequality for every degree of the
block. A linear average can have the correct sign over arbitrarily long
blocks while simultaneously failing every four degrees. The phase bound
at \(a=4\) can also coexist with that failure because transform (27)
makes the exterior mode contractive.

**Remains.** Proving that (18) vanishes on blocks of unbounded length, or
directly (15), using a nonlinear identity specific to the ordinary
weights \(\Lambda(m)\).

**Not proved.** (15) for the ordinary zeta without assuming RH,
vanishing of (18), A1, or RH.

---

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 low_residue_block_transport_gate_check.py
```

The checker uses only `Fraction`. It verifies (2), (19), (21)–(23), the
two contractive factors of (30), (31)–(32), the positive excursion in
every class \(2\pmod4\), and the existence of negative averages over
blocks of increasing lengths.
</content>
