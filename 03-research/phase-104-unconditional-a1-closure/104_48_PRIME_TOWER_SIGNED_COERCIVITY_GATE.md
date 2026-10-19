# 104_48 — Prime-tower closed phase and the unit-multiplicity gate

**Objective of the attack.** A direct attempt is made to prove

\[
 B_n=A_n-\lambda_n\le \kappa A_n,
 \qquad \kappa={1501\over2002},\qquad n\ge150,              \tag{1}
\]

using the rigidity

\[
 \Lambda(p^k)=\log p\qquad(k\ge1)                           \tag{2}
\]

before estimating. A closed per-tower sum is obtained that preserves the
entire Laguerre phase, along with an exact one-sided inequality. However,
the inequality points the wrong direction for (1), and it survives with no
essential change under the shifted falsifier

\[
 \omega_c(m)=2\Lambda(m)\cosh(c\log m),\qquad 0<c<1/2.      \tag{3}
\]

A narrower quantitative no-go is also obtained: positivity, support on
the prime powers, PNT, and **exact constancy along each tower** are not
enough. Raising the multiplicity of a single complete tower breaks any
proportional bound already at \(n=151\), while preserving all those
properties. Hence any future input must use the exact unit multiplicity
of each prime, equivalently the global renewal identity

\[
 \sum_{d\mid m}\Lambda(d)=\log m.                           \tag{4}
\]

But (4) uniquely determines \(\Lambda\); incorporating it via the divisor
selector returns exactly to `104_43`–`104_47`. This attack proves neither
(1), A1, nor RH.

## 0. Non-duplication audit

Document 103_66 telescopes a tower across multiplicative annuli and,
after summing over every prime, obtains the normalized germ. It does not
compute the closed phase (12) of a single tower. Document 104_20
factorizes local tower differences inside an operational square and
proves both signs; it does not use the Poisson summation formula.
Document 104_47 already introduces falsifier (3), but does not check
whether a signed inequality derived from tower constancy accepts or
rejects it.

The singleton fiber (33) and asymptotic tower-coherence falsifiers
already appear in E101_089, §§9–10. They are not claimed again. The
narrow additions of this document are: the closed phase (12), the proof
that its automatic sign accepts (3), and the finite witness (24)–(31),
which breaks the margin directly at \(n=151\) by altering a single
complete tower.

## 1. Closed sum of a complete tower

Write

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad
 \Phi_n(x)=\sum_{k\ge1}e^{-kx}P_n(kx),\qquad x>0.           \tag{5}
\]

For \(a>2\), the complete Euler–pole form of `104_41` groups absolutely
by primes as

\[
 \boxed{
 \mathcal B_{n,a}
 =a\sum_p(\log p)\Phi_n(a\log p)-Q_{n,a},}
 \qquad
 Q_{n,a}=a\int_0^\infty e^{-(a-1)u}P_n(au)\,du.            \tag{6}
\]

The Laplace transform of \(P_n\) is

\[
 \int_0^\infty e^{-su}P_n(u)\,du
 =1-\left(1-{1\over s}\right)^n,
 \qquad \Re s>0.                                           \tag{7}
\]

In particular,

\[
 \boxed{Q_{n,a}=1-\left({-1\over a-1}\right)^n.}          \tag{8}
\]

Tower (5) has two further closed forms. The Laguerre generating function
gives

\[
 \boxed{
 \sum_{n\ge1}\Phi_n(x)z^{n-1}
 ={1\over(1-z)^2\{e^{x/(1-z)}-1\}}.}                       \tag{9}
\]

If \(A_j(q)\) is the Eulerian polynomial, normalized by

\[
 \sum_{k\ge1}k^j q^k={qA_j(q)\over(1-q)^{j+1}},            \tag{10}
\]

then, with \(q=e^{-x}\),

\[
 \boxed{
 \Phi_n(x)=
 \sum_{j=0}^{n-1}{n\choose j+1}{(-x)^j\over j!}
 {qA_j(q)\over(1-q)^{j+1}}.}                               \tag{11}
\]

Formulas (6), (9), and (11) separate neither the higher powers nor take
absolute values. Unlike the annulus telescoping of `103_66`, (9)
explicitly retains the phase of a single tower. Summing over primes,
it naturally recomposes the same normalized germ of `103_66`; no second
reduction of A1 is claimed.

## 2. Poisson's formula and the only automatic direction

The function \(t\mapsto e^{-xt}P_n(xt){\bf1}_{t\ge0}\) has bounded
variation and exponential decay. The one-sided Poisson formula, with half
weight at zero, together with (7), gives

\[
 \boxed{
 \Phi_n(x)
 ={1\over x}-{n\over2}
 +{2\over x}\sum_{\ell\ge1}
 \Re\left\{1-w_{\ell}(x)^n\right\},}
 \qquad
 w_\ell(x)={2\pi i\ell\over x+2\pi i\ell}.                \tag{12}
\]

The series in (12) converges absolutely: its real summand is
\(O_n(x^2/\ell^2)\). Moreover

\[
 |w_\ell(x)|<1,
 \qquad
 \Re\{1-w_\ell(x)^n\}\ge1-|w_\ell(x)|^n>0.               \tag{13}
\]

Consequently the rigidity of a tower does produce a sign, but it is

\[
 \boxed{\Phi_n(x)>{1\over x}-{n\over2}.}                   \tag{14}
\]

Requirement (1) needs an **upper** bound for the prime sum minus the
pole. Inequality (14) is a lower one. It cannot be inverted by a
pointwise sign nor summed in (6) either: its right-hand side tends to
\(-n/2\) as \(x\to\infty\), so the sum of these lower bounds over the
primes diverges to \(-\infty\). It is an exact single-tower inequality,
not a finite global lower bound. Moreover, since

\[
 P_n(x)={(-1)^{n-1}x^{n-1}\over(n-1)!}+O_n(x^{n-2}),       \tag{15}
\]

one has

\[
 \Phi_n(x)=e^{-x}P_n(x)+O_n(e^{-2x}x^{n-1}),               \tag{16}
\]

and hence \(\Phi_n(x)\) has sign \((-1)^{n-1}\) for sufficiently large
\(x\).

## 3. The phase sign also accepts the shifted weights

To see exactly what distinguishes (12), define, for \(r>0\),

\[
 \Phi_{n,r}(x)=\sum_{k\ge1}e^{-rkx}P_n(kx).                \tag{17}
\]

The same proof gives

\[
\begin{aligned}
 \Phi_{n,r}(x)
 ={}&{1\over x}\left\{1-\left(1-{1\over r}\right)^n\right\}
      -{n\over2}\\
 &+{2\over x}\sum_{\ell\ge1}
 \Re\{1-w_{\ell,r}(x)^n\},                               \tag{18}\\
 w_{\ell,r}(x)
 ={}&{r-1+2\pi i\ell/x\over r+2\pi i\ell/x}.
\end{aligned}
\]

The elementary identity

\[
 1-|w_{\ell,r}(x)|^2
 ={2r-1\over r^2+(2\pi\ell/x)^2}                           \tag{19}
\]

shows that every phase summand of (18) remains positive for \(r>1/2\).

Now, tower by tower,

\[
\begin{aligned}
 &\sum_{k\ge1}{\omega_c(p^k)\over p^{ka}}
       P_n(ak\log p)\\
 &\qquad=(\log p)
 \left\{\Phi_{n,1-c/a}(a\log p)
          +\Phi_{n,1+c/a}(a\log p)\right\}.                \tag{20}
\end{aligned}
\]

Since \(a>1\) and \(0<c<1/2\), the two rates in (20) exceed
\(1/2\). So phase positivity (13) survives entirely under the shifted
system. It cannot be the input that proves (1).

This conclusion is not merely diagnostic. Set

\[
 \Xi_c(s)=\xi(s+c)\xi(s-c).                                \tag{21}
\]

Its Euler logarithmic derivative has exactly the weights (3), and
\(\Xi_c(1-s)=\Xi_c(s)\). If
\(\rho=1/2+i\gamma\) is a critical zero of \(\xi\), (21) has the
quartet

\[
 \rho-c,\quad\bar\rho-c,\quad\rho+c,\quad\bar\rho+c,      \tag{22}
\]

off the line of symmetry. For
\(w=1-(\rho-c)^{-1}=e^{\alpha+i\theta}\), \(\alpha>0\), that quartet's
response in the Li coefficient is

\[
 4-4\cosh(n\alpha)\cos(n\theta).                           \tag{23}
\]

The failure occurs at arbitrarily large degrees, not only at an initial
coefficient. Indeed, for the zeros \(\eta\) of (21) set
\(w_\eta=1-\eta^{-1}\). Since \(|w_\eta|\to1\) as
\(|\Im\eta|\to\infty\), the number

\[
 R=\max_\eta |w_\eta|>1                                   \tag{23a}
\]

is attained on a finite multiset. After removing that set, there exists
\(R_2<R\) dominating the remaining \(w_\eta\) outside the unit disc. If
the dominant ones are \(R e^{i\theta_1},\ldots,
R e^{i\theta_M}\), the Darboux expansion of Li's generating function
(equivalently, separating those finitely many singularities in the
Hadamard product) gives

\[
 \lambda_n[\Xi_c]
 =-R^n\sum_{j=1}^{M}e^{in\theta_j}
   +O(R_2^n)+O_c(n\log n).                                \tag{23b}
\]

The right-hand side is real because the multiset is stable under
conjugation. Simultaneous Dirichlet approximation provides infinitely
many \(n\) for which every
\(e^{in\theta_j}\) lies arbitrarily close to \(1\). Along that
subsequence,

\[
 \lambda_n[\Xi_c]\le-{M\over2}R^n                          \tag{23c}
\]

for sufficiently large \(n\). This is also the standard proof of the
obstructive direction of the Bombieri–Lagarias criterion in this case. In
particular, no uniform positive proportional inequality holds for (3) at
large degrees. Equations (18)–(20) show that the automatic sign obtained
via Poisson does not detect that falsehood.

## 4. Minimal no-go preserving complete towers

The following witness preserves more structure than the simple prime
atom of `104_35`. Fix a prime \(p_0\) and an integer \(t\ge1\), and
replace only its local factor by multiplicity \(1+t\):

\[
 \zeta_t(s)=\zeta(s)(1-p_0^{-s})^{-t}.                     \tag{24}
\]

The weights of its logarithmic derivative are

\[
 \Lambda_t(p^k)=
 \begin{cases}
  (1+t)\log p_0,&p=p_0,\\
  \log p,&p\ne p_0,
 \end{cases}
 \qquad k\ge1.                                             \tag{25}
\]

So (25) preserves positivity, the exact support on prime powers, and the
constancy in \(k\) of **every complete tower**. It also preserves PNT with
the same leading term, since

\[
 \psi_t(x)-\psi(x)
 =t(\log p_0)\left\lfloor{\log x\over\log p_0}\right\rfloor
 =O_{t,p_0}(\log x).                                      \tag{26}
\]

However, its change at the critical limit of (6) is ordinarily
convergent and equals exactly

\[
 \boxed{B_n[\Lambda_t]-B_n[\Lambda]
 =t(\log p_0)\Phi_n(\log p_0).}                            \tag{27}
\]

Positivity of (27) can be certified with no root computation. Let
\(n=151\), \(N=n-1=150\), and write

\[
 P_{151}(x)=\sum_{j=0}^{N}(-1)^j a_j(x),
 \qquad
 a_j(x)={151\choose j+1}{x^j\over j!}.                    \tag{28}
\]

For \(0\le j<N\),

\[
 {a_{j+1}(x)\over a_j(x)}
 ={x(N-j)\over(j+1)(j+2)}
 \ge {x\over N(N+1)}.                                     \tag{29}
\]

If \(x>N(N+1)=22650\), the magnitudes of (28) grow strictly. Since
\(N\) is even, pairing from the leading term gives

\[
 P_{151}(x)>0\qquad(x>22650).                               \tag{30}
\]

By Bertrand's postulate there is a prime

\[
 2^{33977}<p_0<2^{33978}.
\]

The elementary bound \(\log2>2/3\) implies
\(\log p_0>22651\). By (30),
\(P_{151}(k\log p_0)>0\) for every \(k\ge1\), and so

\[
 \boxed{\Phi_{151}(\log p_0)>0.}                           \tag{31}
\]

Making \(t\) arbitrarily large in (27) violates any bound
\(B_{151}\le C A_{151}\) with fixed \(C\). Hence

```text
positivity + p^k support + complete tower constancy + PNT
    does not imply a proportional bound for B_n.
```

The falsifier does not satisfy the exact unit value of (2) on tower
\(p_0\). That is precisely the logical boundary it identifies.

## 5. Unit multiplicity leaves no intermediate family

The global property fixing those multiplicities simultaneously is (4),
or in Dirichlet convolution,

\[
 \Lambda*{\bf1}=\log.                                      \tag{32}
\]

Since \({\bf1}^{-1}=\mu\), (32) has the unique solution

\[
 \boxed{\Lambda=\mu*\log.}                                \tag{33}
\]

This was already isolated as the "singleton fiber" in `E101_089`, §9. In
particular:

* using only tower constancy lets in witness (24)–(31);
* imposing (32) eliminates the witness, but selects exactly
  \(\Lambda\), with no auxiliary cone or homotopy;
* disintegrating (32) produces the exact divisor selector of `104_43`,
  and its signed flux is the functional equivalent to the margin of
  `104_47`.

Hence the closed sum (9)–(12) supplies no new coercive inequality. The
still-missing theorem must be a **global, nonlocal** comparison using
(32) together with the Laguerre test, keeping the pole to the end, and
directly proving (1). That is exactly the still-open RH-strength piece.

## 6. Verdict

Proved unconditionally:

1. the exact per-tower closure (6), (9), and (11);
2. the Poisson phase representation (12) and its one-sided bound (14);
3. that this sign also holds for the two shifted towers of (3);
4. the local-multiplicity no-go (24)–(31), already at \(n=151\);
5. that exact renewal (32) has the singleton fiber (33).

Ruled out:

```text
one-sided per-tower phase
+ positivity
+ constancy of the weights along p^k
+ PNT
    => B_n <= (1501/2002) A_n.
```

Not ruled out is a global inequality using exact renewal (32) in a
nonlocal way. Neither (1), A1, nor RH has been proved.

## 7. Reproducible verification

`tools/prime_tower_signed_coercivity_gate_check.py` uses only integers,
`Fraction`, and rational Gaussian arithmetic. It checks:

* the Laguerre coefficients and transform (7);
* the closed Eulerian sum (11) for several rational degrees;
* algebraic identity (19) and positivity of the phase atoms;
* the shifted split (20) at finite truncation;
* the alternating growth (29)–(30) for \(n=151\);
* the quartet identity (23) on the rational test of `104_41`.

The checker does not claim to certify an infinite sum by truncation.
Poisson's formula (12) is proved analytically from (7), and (31) follows
term by term from (30); the program checks the finite algebraic identities
entering those two proofs.

Reproduced with

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 prime_tower_signed_coercivity_gate_check.py
```
</content>
