# 104_67 — Two-sided excursions and upper-barrier gate

**Question.** The block criterion of `104_61` uses negative excursions.
Does the zero-Haar-mean of the dominant characters also produce positive
excursions, allowing RH to be attacked via a more accessible **upper**
bound?

**Result.** Yes to the first question, not with current tools to the
second. If RH is false, \(\lambda_n\) has positive and negative
excursions of the same maximal exponential rate, each on a syndetic set
of positive density. Hence any of the conditions

\[
 \lambda_n\geq-e^{\sqrt n},\qquad
 \lambda_n\leq e^{\sqrt n},\qquad
 |\lambda_n|\leq e^{\sqrt n}                                \tag{1}
\]

on consecutive blocks of unbounded length is, by itself, equivalent to
RH.

The upper barrier translates into a very weak lower bound for the
prime–pole functional \(B_n=A_n-\lambda_n\). In the Euler half-plane
that bound is already available: `104_41` proves \(|\mathcal B_{n,a}|\leq3n\)
for \(a\geq4\). But transporting it to \(a=1\) crosses exactly the
residues of the zeros to the right; those residues generate the positive
excursions just proved. So the upper route reaches the same homotopy
gate with a different sign. It proves neither A1 nor RH.

---

## 1. Two-sided dominant-mode theorem

Suppose RH is false. In the notation of `104_56`, there exist

\[
 R>1,\qquad1<R_1<R,\qquad
 S(n)=\sum_{j=1}^Km_j\cos(n\phi_j),                         \tag{2}
\]

with \(m_j>0\), such that

\[
 \lambda_n=C_0-R^nS(n)+O(n^2R_1^n+n^2).                   \tag{3}
\]

Equal and opposite angles have been grouped. Let

\[
 H=\overline{\{n\phi:n\in\mathbb Z\}}\subset\mathbb T^K,
 \qquad F(x)=\sum_{j=1}^Km_j\cos x_j.                       \tag{4}
\]

Each character of (4) is nontrivial: a nontrivial zero has nonzero
ordinate. By character orthogonality,

\[
 \int_HF\,d\mu_H=0.                                        \tag{5}
\]

Also \(F(0)=\sum_jm_j>0\), so \(F\) is not identically zero. Continuity
and (5) force \(F\) to also take negative values. Choose \(\eta>0\)
such that the open sets

\[
 U_-:=\{F>2\eta\},\qquad U_+:=\{F<-2\eta\}                 \tag{6}
\]

are nonempty and have boundaries of zero Haar measure. Rotation by
\(\phi\) is minimal and uniquely ergodic on \(H\). Hence its return sets

\[
 D_-:=\{n:n\phi\in U_-\},\qquad
 D_+:=\{n:n\phi\in U_+\}                                   \tag{7}
\]

have positive natural density. Both are syndetic: the translations of
each open set cover \(H\), and a finite subcover bounds the return
times.

The gap \(R_1<R\) in (3) gives the following strengthening of `104_56`.

**Theorem 1.1 (two-sided excursions).** If RH is false, there exist
\(c>0\), \(n_0\), \(R>1\) and two syndetic sets \(D_+,D_-\), each of
positive natural density, such that

\[
 \boxed{
 \lambda_n\geq cR^n\quad(n\in D_+),\qquad
 \lambda_n\leq-cR^n\quad(n\in D_-),}                       \tag{8}
\]

for \(n\geq n_0\). The two sets may have different densities and
different gaps; no universal constant is claimed.

The second inequality is `104_56`. The first is the new content: it
comes from the returns to \(U_+\) instead of the returns to a
neighborhood of the origin.

---

## 2. Upper and two-sided block criteria

Under RH, Lagarias's theorem gives

\[
 \lambda_n=A_n+O(\sqrt n\log n)=O(n\log n).                 \tag{9}
\]

In particular, all three inequalities of (1) eventually hold. If RH is
false, (8) beats \(e^{\sqrt n}\) on \(D_+\) and \(D_-\). Since both sets
are syndetic, none of the three inequalities can hold on blocks of
unbounded length.

**Corollary 2.1.** The following are equivalent:

1. RH;
2. there exist consecutive blocks of unbounded length on which
   \(\lambda_n\leq e^{\sqrt n}\) at every index;
3. there exist such blocks with \(|\lambda_n|\leq e^{\sqrt n}\);
4. there exist such blocks with \(\lambda_n\geq-e^{\sqrt n}\).

Version 4 is weaker than the \(-1\) barrier of `104_61`; it is
included to display the symmetry of rates. Version 2 is logically
independent of Li's sign: it does not require positivity, but the
local absence of exponential positive growth.

The same argument allows exceptions. Each of the barriers of (1),
outside a set of zero upper logarithmic density, is equivalent to RH.
It does not suffice for the exception to have a small fixed density: the
return densities depend on the dominant phases.

---

## 3. Positive, negative, and two-sided rate detectors

For \(V>0\), define

\[
\begin{aligned}
 \Psi^+_{V,n}(x)
   &=\min\!\left\{V,{1\over n}\log\max(1,x)\right\},\\
 \Psi^-_{V,n}(x)
   &=\min\!\left\{V,{1\over n}\log\max(1,-x)\right\},\\
 \Psi^{\pm}_{V,n}(x)
   &=\min\!\left\{V,{1\over n}\log\max(1,|x|)\right\}.
                                                               \tag{10}
\end{aligned}
\]

Their layer identities are

\[
\begin{aligned}
 \Psi^+_{V,n}(x)&=\int_0^V{\bf1}_{\{x>e^{nv}\}}\,dv,\\
 \Psi^-_{V,n}(x)&=\int_0^V{\bf1}_{\{x<-e^{nv}\}}\,dv,\\
 \Psi^{\pm}_{V,n}(x)&=\int_0^V{\bf1}_{\{|x|>e^{nv}\}}\,dv.
                                                               \tag{11}
\end{aligned}
\]

With \(H_X=\sum_{n\leq X}1/n\), set

\[
 \mathfrak R_V^\sigma(X)={1\over H_X}
 \sum_{n\leq X}{\Psi^\sigma_{V,n}(\lambda_n)\over n},
 \qquad\sigma\in\{+,-,\pm\}.                               \tag{12}
\]

**Theorem 3.1 (bounded two-sided criterion).** For each \(V>0\) and each
\(\sigma\in\{+,-,\pm\}\),

\[
 \boxed{
 \mathrm {RH}\quad\Longleftrightarrow\quad
 \liminf_{X\to\infty}\mathfrak R_V^\sigma(X)=0.}           \tag{13}
\]

**Proof.** Under RH, (9) implies

\[
 \Psi^+_{V,n}(\lambda_n),\qquad
 \Psi^{\pm}_{V,n}(\lambda_n)\ll{\log n\over n},
 \qquad \Psi^-_{V,n}(\lambda_n)=0.                         \tag{14}
\]

Since \(\sum_{n\geq2}(\log n)/n^2<\infty\), the averages (12) tend to
zero. Under non-RH, (8) and the positive logarithmic density of \(D_+\)
and \(D_-\) give

\[
\begin{aligned}
 \liminf_X\mathfrak R_V^+(X)
   &\geq d_+\min(V,\tfrac12\log R)>0,\\
 \liminf_X\mathfrak R_V^-(X)
   &\geq d_-\min(V,\tfrac12\log R)>0,
                                                               \tag{15}
\end{aligned}
\]

and the two-sided version dominates both. \(\square\)

For the quadruple \(w=2i\) of `104_17`,

\[
 Q_{4k}=-2^{4k+1}+O(1),\qquad
 Q_{4k+2}=2^{4k+3}+O(1),\qquad
 Q_{2k+1}=4.                                                  \tag{16}
\]

Hence

\[
\boxed{
\begin{aligned}
 \mathfrak R_V^+(X)&\longrightarrow{1\over4}\min(V,\log2),\\
 \mathfrak R_V^-(X)&\longrightarrow{1\over4}\min(V,\log2),\\
 \mathfrak R_V^{\pm}(X)&\longrightarrow{1\over2}\min(V,\log2).
                                                               \tag{17}
\end{aligned}}
\]

So the upper detector passes the falsifier with the same margin as the
lower one; the two-sided one sees both exponential classes.

---

## 4. Prime–Laguerre translation of the upper barrier

Set, as in `104_60`,

\[
 B_n:=A_n-\lambda_n.                                        \tag{18}
\]

The upper barrier of (1) is exactly equivalent to

\[
 \boxed{B_n\geq A_n-e^{\sqrt n}.}                           \tag{19}
\]

Since \(A_n=O(n\log n)\), the right-hand side is
\(-e^{\sqrt n}(1+o(1))\). This looks much weaker than A1: it only
requires that the complete prime functional not have a negative tail of
fixed exponential rate.

With the regulator of `104_61`,

\[
 B_n=\lim_{\varepsilon\downarrow0}
 \left\{
 \sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)-p_n(\varepsilon)
 \right\}.                                                  \tag{20}
\]

The positivity of \(\Lambda(m)\) does not give (19), because
\(L_{n-1}^{(1)}\) changes sign and the two terms of (20) are of order
\(\varepsilon^{-n}\). Separating them by absolute value again loses the
finite part, exactly as in `104_61`, `104_63` and `104_65`.

---

## 5. Why the strong Euler half-plane bound does not transport

The upper orientation does fit an already-proved estimate. For the
complete prime–pole deformation of `104_41`,

\[
 |\mathcal B_{n,a}|\leq3n\qquad(a\geq4).                    \tag{21}
\]

In particular, \(\mathcal B_{n,a}\geq-3n\), much stronger than (19).
The whole problem concentrates when moving \(a\downarrow1\). The exact
formula is

\[
 B_n=\mathcal P_n+
 \sum_{\Re\rho>1/2}
 {m_\rho\mathcal F_n(w_\rho)\over\rho(\rho-1)},
 \qquad w_\rho=1-{1\over\rho}.                             \tag{22}
\]

The critical phase \(\mathcal P_n\) does not see a reciprocal off-line
quadruple; the residue sum does. On the classes where that quadruple
contributes \(\lambda_n\gg R^n\), it changes \(B_n\) by \(-\lambda_n\ll-R^n\)
and violates (19). By Theorem 1.1, those classes generally form a
syndetic set, not a scattered exception a block criterion can ignore.

Hence transporting only the lower bound
\(\mathcal B_{n,a}\geq-3n\) to the boundary would already prove the
upper barrier equivalent to RH. The homotopy does not simplify by
flipping the sign of the target: the residue that formerly produced a
negative excursion now produces a positive one.

---

## 6. Verdict

**Proved.** Syndetic two-sided excursions (8), upper and two-sided block
criteria, bounded detectors (10)--(17), and the exact translation of the
upper barrier to the prime–pole channel.

**Gain.** It is no longer necessary to attack Li's positivity: a
subexponential upper bound on blocks would also close RH. The two-sided
formulation identifies the exterior rate without choosing a sign.

**Distinct no-go.** The lower bound needed for \(B_n\) is proved on the
Euler half-plane with a huge margin, but its transport to \(a=1\) fails
exactly because of the positive excursions of the new Theorem 1.1. It is
not a loss of constant or modulus; it is the same signed residue sum.

**Not proved.** A new block for the upper barrier, the zero limit of any
of (12), (19), A1, or RH.

---

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 two_sided_excursion_check.py
```

The checker uses `Fraction`. It verifies the two exponential classes of
(16), the absence of one-sided blocks of length four in the quadruple,
and the harmonic densities \(1/4,1/4,1/2\) of (17). The proof of
syndetic returns is in §1 and does not depend on sampling.
