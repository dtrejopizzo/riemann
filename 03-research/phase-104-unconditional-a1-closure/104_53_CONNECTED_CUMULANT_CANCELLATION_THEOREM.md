# 104_53 — Connected cumulant cancellation theorem between prime towers

**Result.** Every natural polynomial identity in the moments that is
additive with respect to independent sums is necessarily a linear
combination of cumulants. For the zeta law, each cumulant is a sum over a
single prime tower. Consequently, any exact polynomial lift that
additively recomposes

\[
 B_n=A_n-\lambda_n
\]

into joint moments may introduce pairs or tuples of distinct towers, but
all those disconnected terms cancel when the logarithmic functional is
recomposed. The phenomenon observed at second order in `104_50`--`104_52`
is not accidental: it holds at every cumulant order of this additive
hierarchy.

This does not prove

\[
 B_n\le {1501\over2002}A_n,\qquad n\ge150,                 \tag{1}
\]

nor A1 nor RH. It does rule out, as an autonomous mechanism, every
*additive polynomial identity* of multi-tower moments that would expect,
after recomposition, to retain a positive reserve built from correlations
between distinct primes. A viable successor would have to apply a
non-additive inequality **before** the connected projection and prove that
the disconnected reserve being discarded pays a margin proportional to the
fixed Laguerre test.

## 1. Universal algebra of moments

Let

\[
 \mathcal H=\mathbb Q[m_1,m_2,\ldots],\qquad m_0=1,
\]

with coproduct

\[
 \boxed{
 \Delta m_r=\sum_{j=0}^r {r\choose j}m_j\otimes m_{r-j}.}  \tag{2}
\]

Equation (2) encodes exactly the moments of a sum of independent
variables. Introduce the exponential series

\[
 M(t)=1+\sum_{r\ge1}m_r{t^r\over r!},\qquad
 K(t)=\log M(t)=\sum_{r\ge1}\kappa_r{t^r\over r!}.          \tag{3}
\]

From (2),

\[
 \Delta M(t)=M(t)\otimes M(t),
\]

and therefore

\[
 \boxed{
 \Delta K(t)=K(t)\otimes1+1\otimes K(t),\qquad
 \Delta\kappa_r=\kappa_r\otimes1+1\otimes\kappa_r.}       \tag{4}
\]

The \(\kappa_r\) are the universal cumulants.

## 2. Classification of additive polynomial observables

**Theorem 2.1.** Let \(P\in\mathcal H\) be a polynomial satisfying

\[
 \Delta P=P\otimes1+1\otimes P.                            \tag{5}
\]

Then there exist only finitely many scalars \(c_r\in\mathbb Q\) such that

\[
 \boxed{P=\sum_r c_r\kappa_r.}                             \tag{6}
\]

If moreover \(P\) is homogeneous of weight \(r\), with
\(\deg m_j=j\), then \(P=c\kappa_r\).

**Proof.** The triangular change of variables (3) is an automorphism

\[
 \mathbb Q[m_1,m_2,\ldots]
 =\mathbb Q[\kappa_1,\kappa_2,\ldots].                     \tag{7}
\]

Write \(P=Q(\kappa_1,\ldots,\kappa_R)\). By (4), condition
(5) is the polynomial identity

\[
 Q(x_1+y_1,\ldots,x_R+y_R)=Q(x_1,\ldots,x_R)+Q(y_1,\ldots,y_R). \tag{8}
\]

Over a field of characteristic zero, an additive polynomial is linear:
indeed, substituting \(y=x\) shows that each homogeneous component of
ordinary degree \(d\) satisfies \(2^dQ_d=2Q_d\), and hence vanishes unless
\(d=1\). This proves (6). The last statement follows from the weights.
\(\square\)

The same proof holds over any field of characteristic zero. In the
application below one may fix \(s>1\), or extend scalars from
\(\mathbb Q\) to \(\mathbb Q(s)\); hence the rational coefficients in
\(s\) of (15) are not outside the scope of the theorem.

## 3. Exact application to the zeta law

Fix \(s=1+\varepsilon>1\) and

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad X=\log N.   \tag{9}
\]

Its moment generating function is

\[
 \mathbb E_se^{tX}={\zeta(s-t)\over\zeta(s)}.              \tag{10}
\]

Since the prime exponents are independent geometric variables, (3) and the
Euler product give, for each \(r\ge1\),

\[
\boxed{
 \kappa_r(s)
 =\sum_p(\log p)^r\sum_{k\ge1}k^{r-1}p^{-ks}
 =\sum_{m\ge2}{\Lambda(m)(\log m)^{r-1}\over m^s}.}        \tag{11}
\]

No tuple of distinct primes remains in (11). By contrast the moments
\(m_r(s)=\mathbb E_sX^r\) contain all products of cumulants. Theorem 2.1
proves that those products must cancel in any exact additive observable.

The polar comparator \(X_0\sim\mathrm{Exp}(\varepsilon)\) has

\[
 \kappa_r^{(0)}=(r-1)!\varepsilon^{-r}.                    \tag{12}
\]

With

\[
 R(q)=-{\zeta'\over\zeta}(1+q)-{1\over q},                 \tag{13}
\]

one obtains

\[
 \boxed{
 \kappa_r(1+\varepsilon)-\kappa_r^{(0)}
 =(-1)^{r-1}R^{(r-1)}(\varepsilon).}                       \tag{14}
\]

Finally, for

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad
 c_{n,r}(s)=(-1)^{r-1}{n\choose r}{s^{r-1}\over(r-1)!},   \tag{15}
\]

the Laguerre recomposition is

\[
 \boxed{
 {\mathcal B_{n,s}\over s}
 =\sum_{r=1}^n c_{n,r}(s)
 \{\kappa_r(s)-(r-1)!\varepsilon^{-r}\},
 \qquad \mathcal B_{n,s}\longrightarrow B_n.}            \tag{16}
\]

Thus every exact polynomial lift that preserves additivity and represents
this same functional returns to the cumulant combination (16). A
non-additive quadratic form may retain multi-tower terms and falls outside
Theorem 2.1. In the concrete PSD construction of `104_50`, its disconnected
part is an energy or variance that loses the orientation of the margin;
it is not claimed that every conceivable quadratic form has that
structure or lacks a useful sign.

## 4. Scope of the no-go

The theorem rules out the scheme

```text
introduce joint moments of several towers
+ exactly recompose an additive observable
=> retain a positive cross reserve.
```

It does not rule out a genuine inequality that uses, before recomposing:

1. the uniform unit mark of `104_49`;
2. a non-additive reserve between several towers;
3. a specific sign of the Laguerre vector;
4. an estimate that fails for the shifted selector (39) of `104_49`.

But that inequality cannot be a disguised cumulant identity. It must prove
that a specific part of the disconnected moments dominates, with the
correct sign, the connected observable (16). That is new RH-strength
arithmetic content, not a formal consequence of the renewal.

The same warning applies to the falsifier
\(Z_c(s)=\zeta(s+c)\zeta(s-c)\): it is also a product of independent
geometric fields in its Euler half-plane, and every universal cumulant
identity again linearizes its factors. Hence a mechanism that only uses
(2)--(6) does not distinguish the critical line.

## 5. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 connected_cumulant_cancellation_check.py
```

The checker uses `Fraction`. It exactly verifies the moment convolution,
the additivity of the cumulants up to order twelve, and the cancellation
of all cross terms at low orders. It is a verification of the identities,
not a substitute for the algebraic proof of Theorem 2.1.
