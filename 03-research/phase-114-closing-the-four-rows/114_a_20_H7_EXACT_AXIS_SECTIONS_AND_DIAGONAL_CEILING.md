# 114.a.20 — H7 sections: exact prime-axis count and the diagonal ceiling

> **Refinement (`a_63`--`a_66`).** Section 1 and the abstract torsor grid are
> unconditional. Interpreting the square modules as completed lattices and
> speaking of their full bounded section sets requires H7-PB-REG.

```
+--------------------------------------------------------------------------+
| AXIS        H^0(X,L_p^m) = {k/p^m : |k|<=p^m}; size 2p^m+1.             |
| GRID        B_{m,n} contains (m+1)(n+1) distinct pure grid sections.     |
| CEILING     Any family distinguished only by diagonal restriction has   |
|             at most 2p^m q^n+1 elements, hence log-size O(m+n).          |
| CONSEQUENCE Quadratic growth must use a genuinely off-diagonal invariant.|
+--------------------------------------------------------------------------+
```

## 1. Exact sections on a prime axis

Let `L_p` be the effective inverse-uniformizer bundle of `114_a_18`.  In the
adelic description (11.17), its `m`-th power has local lattice
`p^{-m}Z_p` at `p`, the unit lattice at every other finite place, and the
one-dimensional real unit ball at infinity.  Therefore its scalar sections
are

\[
\begin{aligned}
 H^0(X,L_p^m)
 &=\mathbb Q\cap p^{-m}\mathbb Z_p
       \cap\!\prod_{\ell\ne p}\mathbb Z_\ell\cap[-1,1]\\
 &=p^{-m}\mathbb Z\cap[-1,1]\\
 &=\{k/p^m:k\in\mathbb Z,\ |k|\le p^m\}.                  \tag{1.1}
\end{aligned}
\]

### Theorem 1.1

For every `m>=0`,

\[
 \#H^0(X,L_p^m)=2p^m+1,
 \qquad
 \log\#H^0(X,L_p^m)=m\log p+O(1).                        \tag{1.2}
\]

### Proof

The finite local conditions say that the denominator of a rational section
divides `p^m`; the real condition says its absolute value is at most one.
This is exactly (1.1), which has the stated number of integer numerators. QED.

This also fixes the orientation issue: the idele with component `p`, rather
than `p^{-1}`, would impose `p^mZ_p` and leave only the zero scalar section for
`m>0` under the same real unit bound.

## 2. An unconditional abstract mixed grid on the literal square

Fix distinct primes `p!=q` and the bigraded bundles

\[
 \mathcal B_{m,n}=p_1^*L_p^m\otimes p_2^*L_q^n           \tag{2.1}
\]

from `114_a_19`.  For `0<=i<=m`, `0<=j<=n`, external section multiplication
gives

\[
 u_{i,j}=p_1^*(p^{-i})\,p_2^*(q^{-j})
       \in H^0(Y,\mathcal B_{m,n}).                       \tag{2.2}
\]

### Proposition 2.1

The `(m+1)(n+1)` sections in (2.2) are pairwise distinct.

### Proof

If `u_{i,j}=u_{i',j'}`, diagonal restriction gives

\[
 p^{-i}q^{-j}=p^{-i'}q^{-j'}\quad\text{in }\mathbb Q.    \tag{2.3}
\]

Unique factorization forces `i=i'` and `j=j'`. QED.

This is the first explicit noncolliding two-dimensional section grid on the
literal square.  Its cardinality is only polynomial, so it does not by itself
pass H7-K.

## 3. The exact diagonal ceiling

Diagonal restriction sends (2.1) to

\[
 \Delta^*\mathcal B_{m,n}=L_p^m\otimes L_q^n.             \tag{3.1}
\]

The same adelic calculation as (1.1) gives

\[
 H^0(X,L_p^m\otimes L_q^n)
 =\left\{\frac{k}{p^m q^n}:|k|\le p^m q^n\right\},       \tag{3.2}
\]

and hence

\[
 \#H^0(X,L_p^m\otimes L_q^n)=2p^m q^n+1.                \tag{3.3}
\]

### Theorem 3.1 (diagonal-detection no-go)

Assume either the completed realization supplied by H7-PB-REG, or explicitly
that the family below restricts into the bounded curve set (3.2).

Let `A_{m,n}` be any family of bounded sections of `B_{m,n}` such that
restriction

\[
 \Delta^*:A_{m,n}\longrightarrow
 H^0(X,L_p^m\otimes L_q^n)                               \tag{3.4}
\]

is injective. Then

\[
 |A_{m,n}|\le2p^m q^n+1,
 \qquad
 \log|A_{m,n}|\le m\log p+n\log q+O(1).                 \tag{3.5}
\]

In particular, for `m=n=r`, no family whose noncollision is detected only on
the diagonal can have `log |A_{r,r}|=Omega(r^2)`.

### Proof

An injection into the finite set (3.2) has cardinality at most (3.3). Taking
logarithms proves (3.5). QED.

## 4. Sharpened mixed-section gate

The H7-K lower bound now has an unavoidable structural requirement:

> an `exp(Omega(mn))` family must contain exponentially many distinct
> sections with repeated diagonal restrictions.  Their noncollision must be
> witnessed by genuinely off-diagonal operations or restrictions on `Y`.

Thus neither the diagonal nor ordinary rational denominators can certify the
needed entropy.  A successful next construction must provide:

1. an off-diagonal evaluation/normal form for mixed uses of Haran's two
   additions;
2. `Theta(mn)` independently switchable coefficients in that normal form;
3. preservation of the two real boundedness conditions;
4. an `exp(O(mn))` upper bound modulo Haran's relations.

This replaces the vague instruction “take mixed sums” by an exact target:
construct a large fiber of `Delta^*` and separate its members intrinsically on
the square.

## 5. Verification scope

`114_a_20_h7_axis_sections_verify.py` checks the local-to-global rational
lattice, exact counts, grid noncollision and diagonal ceiling over finite
ranges.  The off-diagonal normal form demanded in section 4 remains open.
