# R171 FINAL — Discrete Beurling frontier


## 0. Verdict

**(A) COUNTEREXAMPLE — PROVED.** There exists a discrete system of
generalized Beurling primes whose prime and integer multiplicities are
nonnegative integers, such that

\[
 N_{\mathcal P}(x)=c x+O(x^{2/5}),\qquad c>0,             \tag{0.1}
\]

and whose zeta has infinitely many zeros at

\[
 \Re s={11\over16}>{1\over2}.                            \tag{0.2}
\]

The construction selects, via a deterministic algorithm, a total
computable function of prime multiplicities. It uses no numerical
evidence nor a random seed. In fact, the selected system satisfies the
slightly stronger bound

\[
 N_{\mathcal P}(x)=c x+O(x^{83/208}),\qquad
 {83\over208}={2\over5}-{1\over1040}.                  \tag{0.3}
\]

The product measure of roundings is used only as a device to define
conditional expectations and effectively choose a branch.

This result is the specialization \(\lambda=3/8\), with the loss absorbed
into \(2/5\), of the discrete theorem `BFdisc` of R163_803, audited in
R163_891. The specialization removes any ambiguity between
\(O_\varepsilon(x^{\lambda+\varepsilon})\) and a fixed exponent less than
\(1/2\).

## 1. Prior corpus audit

The requested reference `R163_401 §L2` does not literally exist. Line L2
is in R164_000 §2 and is proved in R164_201; R163_401 §4.11(f) only
records its consequence.

| Source | Result | Label | Scope that must not be repeated |
|---|---|---|---|
| R163_103; final version R163_803; audit R163_891 | For \(1/3<\lambda<1/2\), random rounding of the Witt multiplicities produces a discrete system with \(N=cx+O_\varepsilon(x^{\lambda+\varepsilon})\) and zeros \(s=\lambda+(1-\lambda)\rho\) | **PROVED** after the corrections of R163_891 | Do not round the prime measure directly; the Witt exponents must be rounded. At \(\lambda=1/3\) only \(+\varepsilon\) is obtained. |
| R163_401 §4.11(f) / R164_000 L2 | Formulates the discrete frontier remaining below \(1/3\) | **PROVED** as a record; "every example must be off-lattice" is **ARGUED** | Do not confuse the summary with a proof of general rigidity. |
| R164_201, Theorem L; R164_291 | Every bounded rounding on the Witt lattice, for \(\lambda<1/3\), loses a positive exponent above \(\lambda\) | **PROVED**; Theorem \(L^*\) is **ARGUED** | Do not relaunch independent, correlated, greedy, or deterministic rounding within that same class to reach the natural exponent. Theorem L does not locate zeros. |
| R167_103, Theorem S | Selberg, Brun--Titchmarsh, Vaughan, large sieve, and mean values transfer to the discrete Beurling class with \(N=Ax+O(x^\theta)\) | **PROVED / PROVED-CITED** | These tools alone do not single out \(\mathbb Z\). |
| R169_101 §6 | The exact Eratosthenes induction "integers = \(\mathbb N\)" identifies \(\zeta\); the relaxation \(N=Ax+O(x^\theta)\) returns to the Beurling frontier | **PROVED** for the identification; its phrase "every \(\theta<1/2\) open" became obsolete through BFdisc | The currently open range is \(\theta\le1/3\), not every \(\theta<1/2\). |
| Paper 48, Problem 6 and Theorem BFdisc | The class-level answer is already negative for every fixed exponent in \((1/3,1/2)\) | **PROVED** in the record | The frontier \(\theta\le1/3\) remains open. |

The audit found no reason to downgrade BFdisc. Two independent reviews
verified the Witt identity, integrality, the moment product, the
Borel--Cantelli step, and the zero-free continuation of the rounding factor.

## 2. Required literature

In the table, "integer-valued" means that the final system is a discrete
multiset of primes and that the multiplicities of its generalized
integers are nonnegative integers.

| Source | Error of \(N(x)\) | Multiplicities | Zeros | Label and consequence |
|---|---|---|---|---|
| Diamond--Montgomery--Vorhauer, *Beurling primes with large oscillation*, Math. Ann. 334 (2006), [primary text](https://deepblue.lib.umich.edu/bitstream/handle/2027.42/46253/208_2005_Article_638.pdf) | \(N=\kappa x+O(x^\theta)\), only \(1/2<\theta<1\) | Integer-valued, discrete system | Infinitely many zeros at \(\sigma=1-a/\log |t|\), none to the right | **CITED.** Counterexample above \(1/2\); the article explicitly leaves open the possibility \(\theta<1/2\Rightarrow\mathrm{RH}\). |
| W.-B. Zhang, *Beurling primes with RH and Beurling primes with large oscillation*, Math. Ann. 337 (2007), [DOI](https://doi.org/10.1007/s00208-006-0051-5) | \(N=kx+O(x^{1/2}e^{c(\log x)^{2/3}})\), hence \(O(x^{1/2+\varepsilon})\), not \(O(x^{1/2})\) | Integer-valued, discrete systems | One system satisfies RH; another has zeros at \(\sigma=1-1/\log |t|\) | **CITED** from the author's abstract/bibliographic record. Does not go below \(1/2\). |
| T. Hilberdink, *Generalised prime systems with periodic integer counting function*, Acta Arith. 152 (2012), [primary text](https://www.impan.pl/shop/en/publication/transaction/download/product/83080) | Much stronger hypothesis: \(N(x)-cx\) periodic | In the discrete case, integer-valued | Classifies the system as the ordinary one with a finite modification; does not prove RH | **CITED.** Uses integer jumps essentially, but reduces the zeros to those of \(\zeta\) and finite factors. |
| Broucke--Debruyne--Vindas, *Beurling integers with RH and large oscillation*, [arXiv:2004.11501](https://arxiv.org/abs/2004.11501) | \(N=\rho x+\Omega_\pm(xe^{-c\sqrt{\log x\log\log x}})\); not \(O(x^\theta)\) for \(\theta<1\) | Integer-valued after random discretization | Satisfies RH | **CITED.** Shows that large oscillation of \(N\) is compatible with RH; does not provide the sought counterexample. |
| F. Broucke, *On zero-density estimates for Beurling zeta functions*, [arXiv:2409.10051](https://arxiv.org/abs/2409.10051) | General part: \(N=Ax+O(x^\theta)\). The extended model \(\zeta_\theta\) achieves \(O(x^\theta)\); its total-variation discretization requires \(\theta\ge1/2\) | The model \(\zeta_\theta\) has real multiplicities; the discretization theorem produces integer-valued systems only in the indicated range | The extended model has zeros at \((1+\theta)/2\); the main theorems are density theorems, not zero-free regions | **CITED.** Proves the analytic NO-GO: without integrality, theorem (B) cannot exist. |
| Sz. Gy. Révész, Pintz's method in the Beurling context, [arXiv:2207.00665](https://arxiv.org/abs/2207.00665) | Axiom A: \(N=\kappa(x-1)+O(x^\theta)\) | Discrete semigroup; the integrality input used in Rem. 7 comes from Hilberdink's theorem on discrete systems | For \(\theta<1/2\), forces \(\sup\Re\rho\ge1/2\); does not force \(\Re\rho=1/2\) nor give a zero-free region to its right | **CITED.** It is an obstruction in the direction opposite to (B), not a partial proof of RH. |

As an additional check, Broucke--Debruyne--Révész,
[*Some examples of well-behaved Beurling number systems*](https://arxiv.org/abs/2309.01567),
builds certain systems with an integer exponent below \(1/2\) only under RH
and in a different parameter region. It does not contain the Witt
construction used here.

## 3. Construction of the counterexample

Fix

\[
 \lambda={3\over8},\qquad
 \Theta={2\over5},\qquad
 a={\lambda\over1-\lambda}={3\over5},\qquad
 w={s-\lambda\over1-\lambda}.                            \tag{3.1}
\]

For each rational prime \(p\) and each \(k\ge1\), let

\[
 c_{p,k}={1\over k}\sum_{d\mid k}\mu(k/d)p^{3d/5},
 \qquad c^+_{p,k}=\max(c_{p,k},0).                       \tag{3.2}
\]

Take independent variables

\[
 b_{p,k}\in\{\lfloor c^+_{p,k}\rfloor,
                    \lceil c^+_{p,k}\rceil\},
 \qquad \mathbb E b_{p,k}=c^+_{p,k},                    \tag{3.3}
\]

and place \(b_{p,k}\) copies of the generalized prime

\[
 v_{p,k}=p^{8k/5}.                                      \tag{3.4}
\]

Each \(b_{p,k}\) is a nonnegative integer and only finitely many
\((p,k)\) have \(v_{p,k}\le x\). Thus (3.4) defines a discrete system.
Its integers are finite products of those primes; their multiplicities,
which count formal factorizations, are also nonnegative integers.
This is the essential use of hypothesis (ii).

## 4. Factorization and zeros

For

\[
 c_k(q)={1\over k}\sum_{d\mid k}\mu(k/d)q^d,
\]

Möbius inversion gives

\[
 (1-qz)^{-1}=\prod_{k\ge1}(1-z^k)^{-c_k(q)}.             \tag{4.1}
\]

If \(q\ge2\), all \(c_k(q)\) are nonnegative; for
\(1<q<2\), only finitely many can be negative. With
\(q=p^{3/5}\) and \(z=p^{-(w+3/5)}\), (4.1) produces

\[
 \zeta_{\mathcal P}(s)=\zeta(w)F(w)G(w),                 \tag{4.2}
\]

initially for \(\Re w>1\), where \(F\) is the finite product that
replaces the negative exponents and

\[
 G(w)=\prod_{p,k}
 (1-p^{-k(w+3/5)})^{-\varepsilon_{p,k}},
 \qquad \varepsilon_{p,k}=b_{p,k}-c^+_{p,k}.             \tag{4.3}
\]

Write \(\log G=L+R\), with

\[
 L(w)=\sum_p\varepsilon_{p,1}p^{-3/5-w}.                 \tag{4.4}
\]

For almost every random realization, the variables of (4.4) are
independent, bounded, and of mean zero. If
\(\Re w>-1/10\),

\[
 \sum_p\operatorname{Var}(\varepsilon_{p,1})
          p^{-6/5-2\Re w}<\infty,                        \tag{4.5}
\]

and the remainder \(R\) converges absolutely on the same half-plane. The
Kolmogorov criterion, applied over a countable family of lines,
and the Jensen--Cahen theorem give almost-sure locally uniform convergence.
Hence \(F G\) is holomorphic and nonzero for \(\Re w>-1/10\).

The corresponding region in the variable \(s\) is

\[
 \Re s>{3\over8}+{5\over8}\left(-{1\over10}\right)
 ={5\over16}.                                            \tag{4.6}
\]

Within it, the zeros of \(\zeta_{\mathcal P}\) are exactly

\[
 s={3\over8}+{5\over8}\rho,                             \tag{4.7}
\]

with \(\rho\) a nontrivial zero of \(\zeta\), preserving multiplicity.
Hardy's theorem gives infinitely many \(\rho=1/2+i\gamma\), without using RH. Their
images satisfy

\[
 \Re s={3\over8}+{5\over16}={11\over16}>{1\over2}.       \tag{4.8}
\]

## 5. Counting integers

Expand

\[
 F(w)G(w)=\sum_{m\ge1}\gamma_m m^{-w}.                  \tag{5.1}
\]

The random function \(\gamma\) is multiplicative; the families
\((\gamma_{p^j})_{j\ge0}\) are independent for distinct primes,

\[
 \mathbb E\gamma_p=0,
 \qquad
 |\gamma_{p^j}|\le C_\eta(1+\eta)^jp^{-3j/5}.            \tag{5.2}
\]

For every integer \(q\ge1\) and every finite family
\(|u_m|\le1\), expanding the \(2q\)-th moment, any prime of
total exponent one has mean zero. The remaining terms have
total exponent at least two, so that

\[
 \mathbb E\left|\sum_m u_m\gamma_m\right|^{2q}
 \le
 \prod_p\left(1+C_q\sum_{E\ge2}
 {E+2q-1\choose2q-1}((1+\eta)p^{-3/5})^E\right)<\infty, \tag{5.3}
\]

because \(\sum_pp^{-6/5}<\infty\). This is the only analytic input
that forces \(\lambda>1/3\).

Set \(X=x^{5/8}\). Euler--Maclaurin for
\(S_{3/5}(Y)=\sum_{d\le Y}d^{3/5}\) gives a function
\(|\Phi(Y)|\le1\) and the exact identity

\[
\begin{aligned}
 N_{\mathcal P}(x)={}&{5\over8}x
       \sum_{m\le X}{\gamma_m\over m}
 +\zeta(-3/5)\sum_{m\le X}\gamma_m m^{3/5}\\
 &+x^{3/8}\sum_{m\le X}\gamma_m\Phi(X/m).              \tag{5.4}
\end{aligned}
\]

Applying (5.3), Chebyshev, and Borel--Cantelli, for every \(\delta>0\),
almost surely

\[
 \sum_{m\le Y}\gamma_m=O_\delta(Y^\delta),
 \qquad
 \sum_{m\le X}\gamma_m\Phi(X/m)=O_\delta(X^\delta).   \tag{5.5}
\]

Partial summation in the first two terms of (5.4) proves

\[
 N_{\mathcal P}(x)=cx+
 O_\delta\left(x^{3/8+(5/8)\delta}\right),
 \qquad
 c={5\over8}F(1)G(1)>0.                                 \tag{5.6}
\]

The positivity of \(c\) follows from the absolute convergence of
\(\log G(1)\), not merely from the formal positivity of its factors.
Taking \(\delta=1/25\), the exponent of (5.6) is

\[
 {3\over8}+{5\over8}{1\over25}={2\over5}.               \tag{5.7}
\]

This proves (0.1) probabilistically. The next section singles out
one choice via an algorithm and obtains a better bound.

## 6. Effective derandomization

This section uses only the moment lemma (5.3) and the exact identity
(5.4). The auxiliary probability of (3.3) is not part of the final system.

Fix \(q=26\). For a choice \(\omega=(b_{p,k})\), define on the
positive integers

\[
 \Gamma_\omega(n)=\sum_{m\le n}\gamma_m(\omega),\qquad
 T_\omega(n)=\sum_{m\le n}\gamma_m(\omega)\Phi(n/m)
\]

and the nonnegative potential

\[
 Z(\omega)=\sum_{n\ge1}{|\Gamma_\omega(n)|^{52}
                    +|T_\omega(n)|^{52}\over n^2}.     \tag{6.1}
\]

By (5.3), applied to each of the two sums,

\[
 \mathbb E Z\le 2K_{26}\zeta(2)<\infty.                \tag{6.2}
\]

Effectively enumerate the non-degenerate coordinates \((p,k)\), i.e.
those for which the two options of (3.3) are distinct and have
positive probability. For a finite prefix \(\tau\) of decisions,
let

\[
 H(\tau)=\mathbb E(Z\mid\tau).                          \tag{6.3}
\]

Since \(c_{p,k}\in\mathbb Q(p^{1/5})\) is given effectively, its sign,
its floor, and the condition \(c^+_{p,k}\in\mathbb Z\) are decidable via
exact arithmetic of algebraic numbers. The non-degenerate coordinates thus
form a decidable set and their two probabilities are algebraic,
computable, and strictly positive.

**Effectiveness lemma.** The real number \(H(\tau)\) is computable uniformly
in \(\tau\).

Indeed, for \(m\le M\), the coefficient \(\gamma_m\) only uses
\(\varepsilon_{p,k}\) with \(k\le v_p(m)\). The first \(M\) summands
of (6.1) depend only on the finitely many coordinates with \(p^k\le M\), and their
conditional expectation is a finite combination of computable reals.
The function \(\Phi\) is computable by (2.2), using the finite sum
\(S_{3/5}\) and the computable value \(\zeta(-3/5)\).

When conditioning on \(\tau\), only finitely many primes lose the
cancellation \(\mathbb E\gamma_p=0\). In the Euler-product proof of (5.3), the
degree-one terms are allowed for those finitely many factors, while
total degree at least two is kept for all the others. This effectively
provides a constant \(C_\tau\) such that, uniformly in \(n\),

\[
 \mathbb E\bigl(|\Gamma(n)|^{52}+|T(n)|^{52}\mid\tau\bigr)
 \le C_\tau.                                             \tag{6.4}
\]

To make effectiveness explicit, fix a rational \(\eta>0\) such that
\(r_p=(1+\eta)p^{-3/5}\) satisfies \(r_2<1\), and set
\(B=C_\eta^{52}\), with the effective majorant of (5.2). If \(S_\tau\) is
the finite set of primes touched by \(\tau\), both moments are
bounded, up to a fixed effective factor, by

\[
 \prod_{p\in S_\tau}\left(1+B\sum_{E\ge1}{E+51\choose51}r_p^E\right)
 \prod_{p\notin S_\tau}\left(1+B\sum_{E\ge2}{E+51\choose51}r_p^E\right).
                                                               \tag{6.5}
\]

The inner sums are \((1-r)^{-52}-1\) and
\((1-r)^{-52}-1-52r\). The second product has an effective tail because its
logarithm is \(O(\sum_{p>P}p^{-6/5})\), a sum bounded by
\(5(P-1)^{-1/5}\). Consequently, the tail of (6.1) beyond \(M\)
is at most \(C_\tau\sum_{n>M}n^{-2}\). This proves the lemma.

Suppose \(\tau_{j-1}\) has been constructed. Compute
\(H(\tau_{j-1}0)\) and \(H(\tau_{j-1}1)\) to within error less than
\(2^{-j-3}\), and choose the branch whose approximation is smaller; in case of a tie,
branch 0. Since

\[
 H(\tau)=q_0H(\tau0)+q_1H(\tau1),\qquad q_0,q_1>0,
\]

the chosen branch satisfies

\[
 H(\tau_j)\le H(\tau_{j-1})+2^{-j-1}.
\]

Hence \(H(\tau_j)\le H(\varnothing)+1\) for every \(j\). For each \(M\),
all the coordinates occurring in the partial sum \(Z_M\) become
fixed at some stage \(j(M)\). Then

\[
 Z_M(\omega_*)
 =\mathbb E(Z_M\mid\tau_{j(M)})
 \le\mathbb E(Z\mid\tau_{j(M)})
 =H(\tau_{j(M)})
 \le H(\varnothing)+1.
\]

Since \(Z_M\uparrow Z\), it follows that \(Z(\omega_*)\le H(\varnothing)+1<\infty\).
Moreover \(|\Gamma(n)|^{52}/n^2\le Z\) and \(|T(n)|^{52}/n^2\le Z\), hence

\[
 \Gamma_{\omega_*}(n)=O(n^{1/26}),\qquad
 T_{\omega_*}(n)=O(n^{1/26}).                            \tag{6.6}
\]

The procedure computes each coordinate after finitely many operations with
certified approximations; hence \((p,k)\mapsto b_{p,k}\) is a
total computable function. Inserting (6.6) into (5.4) and repeating the
partial summation of §5 gives

\[
 N_{\mathcal P}(x)=cx+
 O\left(x^{3/8+(5/8)(1/26)}\right)
 =cx+O(x^{83/208}).                                     \tag{6.7}
\]

For the zeros, there is no need to impose on the selected branch the
almost-sure continuation of §4. For every choice with \(|\varepsilon_{p,k}|<1\), the
series defining \(\log G\) converges absolutely and locally uniformly
when \(\Re(w+3/5)>1\), i.e. for \(\Re w>2/5\); one uses
\(|\log(1-z)|\ll|z|\) on compacta and
\(\sum_{p,k}p^{-k\sigma}<\infty\) for \(\sigma>1\). Hence
\(G=\exp(\log G)\), and also the finite product \(F\), are holomorphic and
nonzero there. The right-hand side of (4.2), equal to \(\zeta_{\mathcal P}\)
initially for \(\Re w>1\), defines its meromorphic continuation to
\(\Re w>2/5\). That region contains \(\Re w=1/2\), so the Hardy
zeros cannot cancel and they transport to (4.8). This completes a
deterministic, computable construction with no elementary closed formula.

## 7. Separating the two hypotheses

| Step | Uses \(N(x)=cx+O(x^\Theta)\) | Uses integer multiplicities |
|---|---:|---:|
| Definition of \(b_{p,k}\) and of the multiset \(\mathcal P\) | No | **Yes:** rounding of the Witt exponents |
| Multiplicities of the generalized integers | No | **Yes:** counting of formal monomials/factorizations |
| Factorization \(\zeta_{\mathcal P}=\zeta(w)FG\) | No | **Yes:** the Euler factors have exponents \(b_{p,k}\in\mathbb Z_{\ge0}\) |
| Control of moments and of \(N\) | Produces (i) | Uses the multiplicative structure created by integer rounding and the exact mean |
| Transport of zeros | Does not use (i) alone | Uses the already-built discrete product |

If integrality is removed, the extended model
\(\zeta((s-\lambda)/(1-\lambda))\) already gives zeros off the line for
any \(\lambda>0\). The novelty needed to answer the discrete question is
that (3.2)--(3.4) turn that model into a multiset of
primes with integer exponents without losing either the fixed error \(2/5\) or
the zeros.

## 8. Neutral audit

Two independent checks of the construction were carried out.

1. The Witt inversion, the finite correction of negative exponents, the
   moment product, and the exact identity (5.4) were verified coefficient by
   coefficient.
2. The convergence of \(FG\), the absence of zero cancellation, the change
   of variables, and the arithmetic of the exponents \(2/5\), \(5/16\), and
   \(11/16\) were verified separately.

No mathematical defect was found. A second review separated the
probabilistic existence from the effective selection and verified the
potential (6.1), the uniform computability of (6.3), the conditional tail
(6.4), and the exponent of (6.7). The algorithm is finite for each
coordinate, although it is not claimed to be efficient nor to admit an
elementary closed formula.

No theorem (B) was obtained for \(\theta_0\le1/3\). DMV and BFdisc refute
every \(\theta_0>1/3\); Hilberdink--Révész only forces
\(\sup\Re\rho\ge1/2\) when \(\theta<1/2\), and gives no zero-free
region \(\Re s>\sigma(\theta)\).

## 9. Implication for row D

**Since (A) is PROVED, every route based solely on properties of the
class \(N(x)=cx+O(x^\theta)\), even with integer multiplicities and
\(\theta<1/2\), is closed. Row D depends on the individual datum of
\(\zeta\), not on that class-level regularity.**
