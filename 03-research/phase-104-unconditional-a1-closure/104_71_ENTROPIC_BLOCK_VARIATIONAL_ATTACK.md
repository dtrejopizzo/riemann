# 104_71 — Entropic variational attack on deterministic blocks

**Result.** The non-interacting partition function of `104_68` admits an
exact probabilistic representation and a finite Gibbs–Donsker–Varadhan
duality. For

\[
 I_L=\{L^2,L^2+1,\ldots,L^2+L-1\},\qquad
 \pi_n:={1\over n+2},                                    \tag{1}
\]

let \(\nu_L=\bigotimes_{n\in I_L}\mathrm{Bern}(\pi_n)\), write
\(B=(B_n)_{n\in I_L}\), and set

\[
 Y_L(B)=\sum_{n\in I_L}B_n\lambda_n,\qquad
 Z_L=\mathbb E_{\nu_L}e^{-Y_L}.                           \tag{2}
\]

Then

\[
 \boxed{
 P_L^{-1}=C_LZ_L,\qquad
 C_L={L^2+L+1\over L^2+1}.}                               \tag{3}
\]

In particular,

\[
 \boxed{
 \mathrm{RH}\Longrightarrow Z_L\longrightarrow1,
 \qquad
 \neg\mathrm{RH}\Longrightarrow Z_L\longrightarrow\infty.} \tag{4}
\]

The entropic duality translates (4) into a uniform bound over
profiles \(q=(q_n)\), and the prime–Laguerre lift keeps all the degrees
together inside the combined polynomial

\[
 G_{L,q}(x)=\sum_{n\in I_L}q_nL_{n-1}^{(1)}(x).            \tag{5}
\]

However, the audit is negative: entropy creates no interaction between
degrees. Every correlated measure pays exactly its total information
(multi-information), the maximizer is again a product, and the
partition function refactors site by site. This document obtains an
exact variational form of the target; it proves neither its bound, A1,
nor RH.

> **Notation.** The Bernoulli probability \(\pi_n\) is the
> \(p_n=1/(n+2)\) of the attack's statement. We use
> \(\mathfrak p_n(\varepsilon)\) for the polar term of the
> prime–Laguerre identity, avoiding a symbol clash.

---

## 1. Bernoulli identity and exact telescoping

Recall from `104_68` that

\[
 a_n={1\over1+(n+1)e^{\lambda_n}},\qquad
 P_L=\prod_{n\in I_L}(1-a_n).                             \tag{6}
\]

Since

\[
 (1-a_n)^{-1}=1+{e^{-\lambda_n}\over n+1},                \tag{7}
\]

and \(B_n\sim\mathrm{Bern}(\pi_n)\),

\[
\begin{aligned}
 \mathbb E e^{-B_n\lambda_n}
 &=1-\pi_n+\pi_ne^{-\lambda_n}\\
 &={n+1\over n+2}
   \left(1+{e^{-\lambda_n}\over n+1}\right).
\end{aligned}                                             \tag{8}
\]

Independence gives

\[
 Z_L=\prod_{n\in I_L}{n+1\over n+2}\,P_L^{-1}.           \tag{9}
\]

If \(N=L^2\) and \(M=L^2+L-1\), the telescoping prefactor is

\[
 \prod_{n=N}^{M}{n+1\over n+2}
 ={N+1\over M+2}
 ={L^2+1\over L^2+L+1}=C_L^{-1}.                         \tag{10}
\]

This proves (3) with no limit or approximation.

### 1.1 Dichotomy

Under RH, `104_68` proves \(P_L\to1\); also \(C_L\to1\). By (3),
\(Z_L\to1\). If RH is false, the same document proves \(P_L\to0\),
while \(1<C_L<2\), and hence \(Z_L=P_L^{-1}/C_L\to\infty\).
So (4) strengthens to the equivalence

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad Z_L\longrightarrow1.}    \tag{11}
\]

The expectation does not linearly average the coefficients: a single
excursion \(\lambda_d\ll0\) produces the factor \(\pi_de^{-\lambda_d}\)
and dominates the whole block.

---

## 2. Finite Gibbs–Donsker–Varadhan duality

For probabilities \(\mu,\nu\) on \(\{0,1\}^{I_L}\), use

\[
 D(\mu\Vert\nu)=\sum_b\mu(b)\log{\mu(b)\over\nu(b)},      \tag{12}
\]

with the convention \(0\log0=0\). Since \(\nu_L\) has full support,
the finite variational identity is

\[
 \boxed{
 \log Z_L
 =\sup_{\mu}
 \{-\mathbb E_\mu Y_L-D(\mu\Vert\nu_L)\}.}               \tag{13}
\]

Indeed, for

\[
 {d\mu_L^*\over d\nu_L}(b)={e^{-Y_L(b)}\over Z_L},        \tag{14}
\]

one has exactly

\[
 -\mathbb E_\mu Y_L-D(\mu\Vert\nu_L)
 =\log Z_L-D(\mu\Vert\mu_L^*)\leq\log Z_L.              \tag{15}
\]

### 2.1 Reduction to single-coordinate profiles

Let \(q_n=\mathbb E_\mu B_n\) and
\(\nu_q=\bigotimes_{n\in I_L}\mathrm{Bern}(q_n)\). The chain rule for
entropy gives

\[
 D(\mu\Vert\nu_L)
 =D(\mu\Vert\nu_q)
  +\sum_{n\in I_L}d(q_n\Vert\pi_n),                       \tag{16}
\]

where

\[
 d(q\Vert p)=q\log{q\over p}+(1-q)\log{1-q\over1-p}.     \tag{17}
\]

Since \(\mathbb E_\mu Y_L=\sum_nq_n\lambda_n\), correlations only
subtract the nonnegative term \(D(\mu\Vert\nu_q)\). Hence (13) is
exactly

\[
 \boxed{
 \log Z_L
 =\sup_{q\in[0,1]^{I_L}}
 \left\{-\sum_{n\in I_L}q_n\lambda_n
 -\sum_{n\in I_L}d(q_n\Vert\pi_n)\right\}.}              \tag{18}
\]

The functional is strictly concave in the interior and its maximizer
is

\[
 q_n^*={\pi_ne^{-\lambda_n}
       \over1-\pi_n+\pi_ne^{-\lambda_n}}
 ={1\over1+(n+1)e^{\lambda_n}}=a_n.                      \tag{19}
\]

So \(\mu_L^*=\bigotimes_n\mathrm{Bern}(a_n)\), and (18) again
factors:

\[
 \log Z_L
 =\sum_{n\in I_L}\log(1-\pi_n+\pi_ne^{-\lambda_n}).     \tag{20}
\]

The apparent interaction of the supremum over measures disappears
exactly.

---

## 3. Combined prime–Laguerre form

Write the regulated identity with separated notation

\[
\begin{aligned}
 \lambda_{n,\varepsilon}
 &=A_n+\mathfrak p_n(\varepsilon)-Q_{n,\varepsilon},\\
 Q_{n,\varepsilon}
 &=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
   L_{n-1}^{(1)}(\log m).
\end{aligned}                                             \tag{21}
\]

Define

\[
 Y_{L,\varepsilon}=\sum_{n\in I_L}B_n\lambda_{n,\varepsilon},
 \qquad Z_{L,\varepsilon}=\mathbb E_{\nu_L}e^{-Y_{L,\varepsilon}}.
                                                                    \tag{22}
\]

For \(\varepsilon>0\), the Euler sum is absolutely convergent.
Substituting (21) into (18) and first collecting all the degrees
gives

\[
 \boxed{
 \log Z_{L,\varepsilon}
 =\sup_{q\in[0,1]^{I_L}}\mathcal V_{L,\varepsilon}(q),}   \tag{23}
\]

with

\[
\begin{aligned}
 \mathcal V_{L,\varepsilon}(q)
 ={}&\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
       G_{L,q}(\log m)\\
 &-\sum_{n\in I_L}q_n
       \{A_n+\mathfrak p_n(\varepsilon)\}
 -\sum_{n\in I_L}d(q_n\Vert\pi_n).
\end{aligned}
\tag{24}
\]

\[
 G_{L,q}(x)=\sum_{n\in I_L}q_nL_{n-1}^{(1)}(x).          \tag{25}
\]

This is the requested combined form: profile \(q\) is applied before
estimating the Mangoldt sum, and primes and prime powers appear
together against a single polynomial \(G_{L,q}\).

### 3.1 A single diagonal

Use exactly the diagonal of `104_68`:

\[
 N_L=L^2+L-1,\qquad
 \varepsilon_L=e^{-N_L/100},\qquad
 \eta={1\over100}-\log{200\over199}>0.                   \tag{26}
\]

There is \(M<\infty\), independent of \(L\), such that, for
sufficiently large \(L\),

\[
 \sup_{n\in I_L}|\lambda_{n,\varepsilon_L}-\lambda_n|
 \leq2MN_Le^{-\eta N_L}=: \delta_L.                      \tag{27}
\]

For any configuration \(b\),

\[
 |Y_{L,\varepsilon_L}(b)-Y_L(b)|\leq L\delta_L.           \tag{28}
\]

Comparing the two exponential sums term by term, or using (13), gives

\[
 \boxed{
 |\log Z_{L,\varepsilon_L}-\log Z_L|
 \leq L\delta_L\longrightarrow0.}                        \tag{29}
\]

Consequently,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \sup_{q\in[0,1]^{I_L}}
 \mathcal V_{L,\varepsilon_L}(q)\longrightarrow0.}       \tag{30}
\]

Profile \(q=0\) gives the automatic lower bound

\[
 \mathcal V_{L,\varepsilon_L}(0)
 =\sum_{n\in I_L}\log(1-\pi_n)
 =-\log C_L\longrightarrow0.                             \tag{31}
\]

### 3.2 The genuinely weak target

The zero limit of (30) is exact, but much stronger than needed to
exclude an exterior zero. Under non-RH, the syndetic set of negative
excursions of `104_56` cuts every \(I_L\), for large \(L\), at some
\(d_L\) such that

\[
 \lambda_{d_L}\leq-cR^{d_L},\qquad R>1.
\]

All Bernoulli factors other than \(d_L\) are at least
\(1-\pi_n\). Using (10),

\[
 Z_L\geq {e^{-\lambda_{d_L}}\over(d_L+1)C_L},
 \qquad
 \log Z_L\geq cR^{L^2}-O(\log L).                        \tag{32}
\]

The same bound holds for \(Z_{L,\varepsilon_L}\), up to \(o(1)\), by
(29). Consequently one obtains the strictly weaker criterion

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \liminf_{L\to\infty}\log Z_{L,\varepsilon_L}<\infty.}  \tag{33}
\]

Equivalently, an upper bound on an unbounded subsequence suffices. More
generally, let \(B_L\geq0\) be any prefixed slack with

\[
 \log(1+B_L)=o(L^2).                                     \tag{34}
\]

If for a sequence \(L_j\to\infty\)

\[
 \boxed{
 \sum_{n\in I_{L_j}}q_n\lambda_{n,\varepsilon_{L_j}}
 \geq-\sum_{n\in I_{L_j}}d(q_n\Vert\pi_n)-B_{L_j}
 \quad\text{for all }q\in[0,1]^{I_{L_j}},}             \tag{35}
\]

then RH is true. The admissible hierarchy includes \(B_L=O(1)\), any
polynomial slack, and in general \(B_L=\exp(o(L^2))\). Proving
convergence to zero is not necessary.

In arithmetic coordinates, (35) is precisely

\[
\boxed{
 \begin{aligned}
 &\sum_{n\in I_{L_j}}q_n
       \{A_n+\mathfrak p_n(\varepsilon_{L_j})\}
 -\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon_{L_j}}}
       G_{L_j,q}(\log m)\\
 &\hspace{22mm}\geq
 -\sum_{n\in I_{L_j}}d(q_n\Vert\pi_n)-B_{L_j}
 \quad\text{uniformly in }q.
 \end{aligned}}                                          \tag{36}
\]

The condition with \(B_L=O(1)\) is the cleanest entropic-coercivity
form; (34)--(36) record that even it can be relaxed up to scale
\(\exp(o(L^2))\). None of these bounds is proved here.

---

## 4. Interaction audit

The entropic duality seems to introduce a collective competition
between degrees. Identity (16) settles the point exactly:

\[
 \underbrace{-\mathbb E_\mu Y_L
 -D(\mu\Vert\nu_L)}_{\text{correlated functional}}
 =\underbrace{-\sum_nq_n\lambda_n
 -\sum_nd(q_n\Vert\pi_n)}_{\text{product functional}}
 -\underbrace{D(\mu\Vert\nu_q)}_{\text{correlation cost}}. \tag{37}
\]

Every probabilistic interaction decreases the functional.
Equivalently, the Hessian of (18) is diagonal,

\[
 {\partial^2\over\partial q_n\partial q_k}
 \left[-\sum_jq_j\lambda_j-\sum_jd(q_j\Vert\pi_j)\right]
 =-{\mathbf1_{n=k}\over q_n(1-q_n)}.                     \tag{38}
\]

The polynomial \(G_{L,q}\) of (25) is useful for keeping degrees
together when applying a hypothetical arithmetic bound, but it does
not change this fact: the Euler sum of (24) is linear in \(G_{L,q}\),
hence linear in \(q\). Solving the supremum recovers the independent
activities of `104_68`.

**Gate verdict.** Entropy produces a convex penalty and a legitimate
uniform formulation, but no connected reserve across degrees. It does
not avoid the pole–prime cancellation within each
\(\lambda_{n,\varepsilon_L}\), whose conditioning was already
quantified in `104_66`--`104_69`.

---

## 5. Off-line falsifier

Consider again the rational quadruple

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\}.           \tag{39}
\]

Every \(I_L\), for \(L\geq4\), contains an index
\(d_L\equiv0\pmod4\), and

\[
 -Q_{d_L}\geq2^{d_L}.                                    \tag{40}
\]

The Bernoulli factor of that site, together with the bound
\(1-\pi_n\) for all the others, gives

\[
 Z_L^Q\geq {e^{-Q_{d_L}}\over(d_L+1)C_L}
 \geq{e^{2^{d_L}}\over(d_L+1)C_L}\longrightarrow\infty. \tag{41}
\]

The same obstruction appears within the duality. Take
\(q_{d_L}=1\) and \(q_n=0\) for \(n\neq d_L\). Then

\[
 -\sum_nq_nQ_n-\sum_nd(q_n\Vert\pi_n)
 =-Q_{d_L}-\log(d_L+1)-\log C_L
 \geq2^{d_L}-\log(d_L+1)-\log C_L.                       \tag{42}
\]

Hence the supremum diverges and the criterion rejects the off-line
model in every large window. The falsifier passes; it does not supply
bound (32) for the real weights \(\Lambda(m)\).

---

## 6. Balance

**Proved.** The telescoping identity (3), the dichotomy (4), the
finite duality (13), its exact reduction to profiles (18), the
maximizer (19), the combined prime–Laguerre form (23)--(25), the
transport via the diagonal (29), and the falsifier (39)--(42).

**Gain.** The block target is converted into a single one-sided
uniform bound over Laguerre polynomials \(G_{L,q}\), with an Euler sum
absolutely convergent for each \(L\). That bound suffices on a
subsequence and with slack as large as \(\exp(o(L^2))\).

**No-go.** Relative entropy creates no interaction: mutual information
penalizes all correlations and the optimizer is a product. The
partition function refactors exactly to the same sites of `104_68`.

**Not proved.** The uniform bound (36), the limit (30), a new block of
real coefficients, A1, or RH.

---

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 entropic_block_variational_check.py
```

The checker uses `Fraction` for (3), (8)--(10) and a finite Bernoulli
enumeration. In floating point it verifies (13), (16), (18)--(20), the
combined prime–Laguerre identity on a finite test Euler sum, the decay
of the diagonal envelope, and the off-line witness. It does not check
(36).
