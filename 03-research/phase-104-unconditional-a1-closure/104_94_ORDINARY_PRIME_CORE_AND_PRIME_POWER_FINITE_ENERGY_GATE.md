# 104_94 — Core of ordinary primes and finite energy of the powers

## Result

Put

\[
 S_m=\sum_{n=2}^m{1\over\log n},\qquad
 P_m=\pi(m)-S_m,
 \tag{1}
\]

and

\[
 Q_m=\sum_{2\le k\le \log_2m}{1\over k}\,
       \pi\!\left(m^{1/k}\right).
 \tag{2}
\]

The roots and the upper limit of (2) are understood in the exact
sense: \(\pi(m^{1/k})\) counts the primes \(p\) such that \(p^k\le m\).
Then the vector of `104_93` decomposes exactly as

\[
 \boxed{B_m=P_m+Q_m.}
 \tag{3}
\]

The whole block of proper powers has finite energy
unconditionally:

\[
 \boxed{
 \mathcal Q:=\sum_{m=2}^{\infty}{Q_m^2\over m(m+1)}<\infty.}
 \tag{4}
\]

Consequently, if

\[
 \mathcal E_B(N)=\sum_{m\le N}{B_m^2\over m(m+1)},
 \qquad
 \mathcal E_P(N)=\sum_{m\le N}{P_m^2\over m(m+1)},
 \tag{5}
\]

then

\[
 \boxed{
 \sup_N\mathcal E_B(N)<\infty
 \Longleftrightarrow
 \sup_N\mathcal E_P(N)<\infty,}
 \tag{6}
\]

and

\[
 \boxed{
 \mathcal E_B(N)=N^{o(1)}
 \Longleftrightarrow
 \mathcal E_P(N)=N^{o(1)}.}
 \tag{7}
\]

If \(L_2(x)=\int_2^xdt/\log t\), replacing \(S_m\) by
\(L_2(m)\) is also a finite-energy perturbation. Therefore

\[
 \boxed{
 \mathcal E_B(N)=N^{o(1)}
 \Longleftrightarrow
 \sum_{m\le N}{\{\pi(m)-L_2(m)\}^2\over m(m+1)}=N^{o(1)}.}
 \tag{8}
\]

Together with `104_93`, (8) remains equivalent to RH. It is not a proof
of (8). Its new content is locating exactly the obstacle:
**all powers \(p^k\), \(k\ge2\), form a finite-energy
perturbation; the possible exponent already lives in the primes \(p\)**.

The lcm/factorial identity does not evade this reduction. Indeed,

\[
 \psi(x)=\log\mathrm{lcm}(1,\ldots,\lfloor x\rfloor),
 \qquad
 \vartheta(x)=\log\mathrm{rad}(\lfloor x\rfloor!),
 \tag{9}
\]

and

\[
 J(x)-\pi(x)
 =\int_{2^-}^x{d(\psi-\vartheta)(t)\over\log t}
 =Q(x).
 \tag{10}
\]

Thus, passing from the radical of the factorial to the lcm adds precisely
the finite-energy block (2), and nothing more.

**Status.** An exact reduction and a coordinate no-go are obtained for
the \(J\), lcm and factorial identities. It is not proved that
\(\mathcal E_B(N)=N^{o(1)}\), Deep-\(\Lambda\), A1, or RH.

---

## 1. Exact combinatorial decomposition

At a prime power \(n=p^k\),

\[
 {\Lambda(n)\over\log n}={\log p\over k\log p}={1\over k},
 \tag{11}
\]

and the quotient is zero outside the prime powers. Therefore

\[
 \begin{aligned}
 J(m)
 &:=\sum_{2\le n\le m}{\Lambda(n)\over\log n}\\
 &=\sum_{k\ge1}{1\over k}\#\{p:p^k\le m\}\\
 &=\pi(m)+\sum_{2\le k\le\log_2m}{1\over k}\pi(m^{1/k}).
 \end{aligned}
 \tag{12}
\]

Since \(B_m=J(m)-S_m\), (12) proves (3).

The tower transformation loses no information. Möbius inversion gives,
also with finite sums,

\[
 \boxed{
 \pi(x)=\sum_{k\le\log_2x}{\mu(k)\over k}J(x^{1/k}).}
 \tag{13}
\]

Indeed, the coefficient of \(\pi(x^{1/r})\) when substituting (12) into the
right-hand side is

\[
 {1\over r}\sum_{k\mid r}\mu(k)
 =\begin{cases}1,&r=1,\\0,&r>1.\end{cases}
 \tag{14}
\]

Hence (12) cannot by itself create a gain: it is a finite, invertible
change of coordinates.

## 2. The proper powers have finite energy

We will only use the elementary Chebyshev bound

\[
 \pi(y)\le C_\pi {y\over\log y}\qquad(y\ge2),
 \tag{15}
\]

with an absolute constant. For instance, one can take a large explicit
constant: the fact that every prime \(n<p\le2n\) divides
\({2n\choose n}<4^n\), followed by a dyadic sum, gives
\(\vartheta(y)\ll y\); separating the primes \(p\le\sqrt y\) from the
remaining ones gives (15). Neither PNT nor zero localization is used.

For each term of (2), (15) gives

\[
 {1\over k}\pi(m^{1/k})
 \le {C_\pi\over\log m}m^{1/k}.
 \tag{16}
\]

If \(K=\lfloor\log_2m\rfloor\), then

\[
 \sum_{k=2}^{K}m^{1/k}
 \le \sqrt m+(K-2)m^{1/3}
 \le \sqrt m+{\log m\over\log2}m^{1/3}.
 \tag{17}
\]

From (16)--(17),

\[
 0\le Q_m\le
 C_\pi{\sqrt m\over\log m}
 +{C_\pi\over\log2}m^{1/3}.
 \tag{18}
\]

Finally,

\[
 {Q_m^2\over m(m+1)}
 \le
 2C_\pi^2{1\over m\log^2m}
 +{2C_\pi^2\over\log^22}m^{-4/3}.
 \tag{19}
\]

Both series converge. This proves (4).

## 3. Equivalence of the energies

For a real sequence \(U=(U_m)\), write

\[
 \|U\|_N^2=\sum_{m=2}^{N}{U_m^2\over m(m+1)}.
 \tag{20}
\]

This is a finite Euclidean norm with positive weights. From (3), the
triangle inequality and (4),

\[
 \big|\|B\|_N-\|P\|_N\big|
 \le\|Q\|_N\le\sqrt{\mathcal Q}.
 \tag{21}
\]

Equivalence (6) is immediate. If one of the two energies is
\(N^{o(1)}\), then for every \(\varepsilon>0\)

\[
 \|P\|_N^2
 \le(\|B\|_N+\sqrt{\mathcal Q})^2
 \ll_\varepsilon N^\varepsilon,
 \tag{22}
\]

and conversely. This proves (7).

To compare the sum and the integral of the comparator, the monotonicity
of \(1/\log x\) gives exactly

\[
 0\le
 D_m:=S_m-L_2(m)
 \le {1\over\log2}.
 \tag{23}
\]

Hence

\[
 \sum_{m=2}^{\infty}{D_m^2\over m(m+1)}
 \le {1\over2\log^22}<\infty.
 \tag{24}
\]

Applying (21) once more with \(D\) gives (8).

## 4. Lcm, radical of the factorial, and the same block

The prime factorization identities give (9): the maximum exponent of
\(p\) dividing \(1,\ldots,m\) produces \(\psi(m)\), while the radical of
\(m!\) contains a single copy of each prime \(p\le m\) and
produces \(\vartheta(m)\).

Since the jumps of \(\psi\) at \(p^k\) weigh \(\log p\), and those of
\(\vartheta\) only at \(p\),

\[
 \int_{2^-}^x{d\psi(t)\over\log t}=J(x),
 \qquad
 \int_{2^-}^x{d\vartheta(t)\over\log t}=\pi(x).
 \tag{25}
\]

Their difference is (10), and Section 2 proves that this difference has
finite energy. In particular:

* the lcm retains all the prime powers, but the proper powers
  cannot be the origin of a positive exponent for \(\mathcal E\);
* the radical of the factorial retains exactly the channel \(k=1\), which
  does contain the whole obstacle;
* inverting (12) via (13) recovers that same channel and does not
  contribute a sign inequality.

This is the exact reason why the lcm/factorial combinatorial identities
do not close (8): after removing a finite-energy perturbation, the
quadratic error of the ordinary primes remains.

## 5. What a successor would need to contribute

The sought bound can already be written without proper powers:

\[
 \sum_{m\le N}{\{\pi(m)-L_2(m)\}^2\over m(m+1)}=N^{o(1)}.
 \tag{26}
\]

A PNT-magnitude bound is not enough. For instance, an error
\(O(xe^{-c(\log x)^{3/5}(\log\log x)^{-1/5}}/\log x)\) still produces,
by direct substitution in (26), a bound with logarithmic exponent
superior equal to \(1\), not \(0\). The successor must use real
quadratic cancellation of the placement of the primes, not merely PNT nor
the accounting of its powers.

## 6. Duplication audit

* `103_66` already proves the telescoping of towers to
  \(\psi=\log\mathrm{lcm}\,\), but does not eliminate the block
  \(k\ge2\) in the Cramér norm.
* `E101_090` isolates the multiplicative ratio covariance for
  \(\Lambda-1\), with another cutoff and another norm.
* `104_89` and `104_93` identify the Cramér energy and its equivalence
  with RH.

What is additional here is (3)--(8): the exact separation of the
\(p\) channel and the unconditional proof that **every**
\(p^k\), \(k\ge2\), is a finite-energy perturbation in the exact discrete
norm.

## 7. Reproduction

From `tools`:

```bash
python3 ordinary_prime_core_energy_check.py
```

The checker verifies with rational arithmetic the finite identities
(12)--(14), checks (3) for each prefix and shows separately the
energies of \(B\), \(P\), \(Q\) and the Minkowski edge. The numerical
table is diagnostic; the proofs of (4)--(8) are the ones above.
