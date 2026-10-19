# R183.006 — Laurent bridge between the semilocal interference and D.247

> **Correction by R183.007--008.** The fiber computation and the agreement
> of the coordinate \(\log p/(p+1)\) are valid. The positivity of the finite
> part proposed in §5 is not inherited from the raw Gram matrix: its
> residue is infinite-rank white light. §5 remains a target only after
> cancelling that residue within a relative contraction.

## 0. Result

R183.005's greatest-common-divisor fiber has a closed generating function.
Its pole is a positive multiplicative Gram matrix. Its finite part contains
exactly the coordinate

\[
                 \ell(a)=\sum_{p\mid a}{\log p\over p+1},       \tag{0.1}
\]

which appears, with opposite sign, in D.247's conservative prime-tangent
coligation. Hence D.247's scalar ports are not auxiliary add-ons: they are
the finite part forced by renormalizing the interference between two
co-Poisson paths sharing the same greatest common divisor.

The computation is exact under Dirichlet regularization. What remains to be
proved is that the semilocal trace's cutoff regularization transports this
decomposition to the same Tate short with no residue.

## 1. Fiber reduction

Let \(a,b\in M_S\), \((a,b)=1\), and define, for \(\Re s>0\),

\[
 \Phi_{S;a,b}(s)
 =\sum_{\substack{d\in M_S\\(d,ab)=1}}
        {\mu(da)\mu(db)\over d^{1+s}}.              \tag{1.1}
\]

### Theorem 1. `PROVED`

If \(a\) or \(b\) is not squarefree, \(\Phi_{S;a,b}=0\). If both are squarefree, then

\[
 \boxed{
 \Phi_{S;a,b}(s)
 =\mu(a)\mu(b)
  \prod_{\substack{p\notin S_f\\p\nmid ab}}
       (1+p^{-1-s}).}                               \tag{1.2}
\]

**Proof.** For \(\mu(da)\mu(db)\ne0\), the three integers \(a,b,d\) must be squarefree and \((d,ab)=1\). Under those conditions,

\[
 \mu(da)\mu(db)=\mu(d)^2\mu(a)\mu(b).
\]

The sum over \(d\) is multiplicative and each allowed prime contributes \(1+p^{-1-s}\). \(\square\)

Hence the entire oscillation of each fiber lies in \(\mu(a)\mu(b)\); the remaining factor has nonnegative coefficients.

## 2. Laurent expansion at the central point

Set

\[
 C_S={1\over\zeta(2)}
       \prod_{p\in S_f}(1+p^{-1})^{-1},
 \qquad
 \rho(a)=\prod_{p\mid a}{p\over p+1}.              \tag{2.1}
\]

Let

\[
 F_S(s)=\prod_{p\notin S_f}(1+p^{-1-s}).             \tag{2.2}
\]

Since

\[
 \prod_p(1+p^{-1-s})={\zeta(1+s)\over\zeta(2+2s)}, \tag{2.3}
\]

there is a real constant \(\kappa_S\) such that

\[
 F_S(s)=C_S\left({1\over s}+\kappa_S+O(s)\right).   \tag{2.4}
\]

For \((a,b)=1\), removing the factors dividing \(ab\) gives

\[
 \prod_{\substack{p\notin S_f\\p\nmid ab}}
 (1+p^{-1-s})
 =F_S(s)\prod_{p\mid ab}(1+p^{-1-s})^{-1}.          \tag{2.5}
\]

Now

\[
 (1+p^{-1-s})^{-1}
 ={p\over p+1}
  \left(1+s{\log p\over p+1}+O(s^2)\right).        \tag{2.6}
\]

Multiplying (2.4)--(2.6) proves:

### Theorem 2. `PROVED`

For \(a,b\) squarefree and coprime,

\[
 \boxed{
 \Phi_{S;a,b}(s)
 ={C_S\mu(a)\rho(a)\mu(b)\rho(b)\over s}
 +C_S\mu(a)\rho(a)\mu(b)\rho(b)
   \bigl(\kappa_S+\ell(a)+\ell(b)\bigr)
 +O(s).}                                             \tag{2.7}
\]

The separation \(\ell(ab)=\ell(a)+\ell(b)\) uses \((a,b)=1\).

## 3. Matrix form of the three ports

Define, over the squarefree indices of \(M_S\),

\[
 r_a={\mu(a)\rho(a)\over\sqrt a},
 \qquad L_{aa}=\ell(a).                              \tag{3.1}
\]

Before inserting the autocorrelation Gram matrix, the fiber's Laurent coefficient has the form

\[
 {C_S\over s}\,rr^*
 +C_S\bigl(\kappa_S rr^*+(Lr)r^*+r(Lr)^*\bigr).     \tag{3.2}
\]

Hence exactly three ports appear:

1. \(rr^*\): the degree/pole channel;
2. \((Lr)r^*+r(Lr)^*\): the oriented first-moment channel;
3. the remainder after short-circuiting the above: the contact channel.

When restoring

\[
 G_h(a,b)=c_h(\log(b/a)),                            \tag{3.3}
\]

(3.2) must be understood as a Schur product with the positive Gram matrix \(G_h\). By Schur's theorem, the product of the polar term \(rr^*\) with \(G_h\) remains positive. The first-moment term keeps the orientation and has no separate sign.

## 4. Agreement with D.247

D.247 uses the local coordinates

\[
 x_p=-{\log p\over p+1}.                            \tag{4.1}
\]

For a squarefree index \(a\),

\[
             \ell(a)=-\sum_{p\mid a}x_p.            \tag{4.2}
\]

Hence the Laurent first moment (2.7) is the multiplicative lift of D.247's degree coordinate. D.247's conservative identity

\[
 \|\widetilde{\mathcal E}_-z\|^2
 +\left|\sum_p\sqrt{\log p}\,z_p\right|^2
 =\|\widetilde{\mathcal E}_+z\|^2
 +\sum_p(\log p)|z_p|^2                            \tag{4.3}
\]

can now be read as the local, prime-by-prime polarization of the finite
part in (3.2). The coligation and the semilocal interference thus share the
same arithmetic coordinate; they are not independent mechanisms.

This agreement does not yet prove that their Hilbertian completions are
identical. For that, (2.7) must be transported through:

1. the autocorrelation Gram matrix (3.3);
2. the Poisson reflection \(a/b\leftrightarrow b/a\);
3. the two Tate shorts;
4. the semilocal trace's cutoff limit.

## 5. Pending compatibility theorem

**Relative Laurent--Tate bridge (OPEN; the raw-Gram version is
NO-GO by R183.008).** After cancelling the white light within a
source contraction, the semilocal cutoff's finite part must agree
with D.247's conservative elimination of the degree/contact ports,
with D.246's Gamma channel attached. In symbols, on the kernel of the
two moments,

\[
 \operatorname{FP}_{s=0}\,\mathcal G_{S,h}(s)
 =Z_{S,h}^*Z_{S,h},                                 \tag{5.1}
\]

with \(Z_{S,h}\) built via the source coligation and not via the square
root of the left-hand side.

If (5.1) is proved with the exact identification of normalizations, it
delivers R183.005's (4.2) and, by R183.003, closes D.

## 6. Logical status

* Eulerian fiber formula (1.2): **PROVED**.
* Laurent expansion and additive separation (2.7): **PROVED**.
* Positivity of the polar residue after the Schur product: **PROVED**.
* Agreement of the coordinate \(\log p/(p+1)\) with D.247: **PROVED**.
* Full identification of spaces and normalizations with D.247: **OPEN**.
* Laurent--Tate bridge (5.1): **OPEN**.
* Row D: **OPEN**.
