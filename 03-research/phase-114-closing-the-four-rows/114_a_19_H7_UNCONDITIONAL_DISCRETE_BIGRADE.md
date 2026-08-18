# 114.a.19 — H7: unconditional abstract two-prime bigrade; completed realization conditional

> **Refinement (`a_63`--`a_66`).** The diagonal/degree proof is unconditional
> for abstract unit torsors in `Pic_tor(Y)`. H7-PB-REG is needed only
> to promote them to completed Section-11 lattices with independent gauges.

```
+--------------------------------------------------------------------------+
| INPUT       Distinct primes p and q and their unit torsors T_p,T_q.      |
| FAMILY      B_{m,n}=p_1^*T_p^m tensor p_2^*T_q^n, (m,n) in Z^2.          |
| THEOREM     (m,n) -> B_{m,n} is injective.                               |
| MECHANISM   Diagonal pullback plus unique factorization p^a q^b=1.       |
| GAIN        A genuine discrete rank-two bigrade without H7-U3 or H7-LD.  |
+--------------------------------------------------------------------------+
```

## 1. Construction

Let `X=overline{Spec Z}`, `S=Spec F{+-1}`, and `Y=X x_S X`. Fix two distinct
rational primes `p != q`. With the abstract prime torsors of `a_18`/`a_66`, put

\[
 \mathcal B_{m,n}=p_1^*T_p^{\otimes m}\otimes
                   p_2^*T_q^{\otimes n},\qquad (m,n)\in\mathbb Z^2.        \tag{1.1}
\]

The positive sector is the subfamily with `(m,n) in N^2`.  Its two real degree
coordinates are

\[
 (a,b)=(m\log p,n\log q).                                                   \tag{1.2}
\]

## 2. Exact bigrade theorem

### Theorem 2.1 (unconditional abstract bigrade)

The homomorphism

\[
 \beta_{p,q}:\mathbb Z^2\longrightarrow\operatorname{Pic}_{\rm ext}(Y),
 \qquad (m,n)\longmapsto[\mathcal B_{m,n}]                                 \tag{2.1}
\]

is injective.  In particular its restriction to `N^2` is a genuine
two-parameter positive bigrade.

### Proof

Suppose `B_{m,n}` and `B_{m',n'}` are isomorphic. Pull back by the diagonal.
Since `Delta^*p_i^*=id`, one obtains on `X`

\[
 T_p^{\otimes(m-m')}\otimes T_q^{\otimes(n-n')}\simeq 1.                   \tag{2.2}
\]

By `a_66`, triviality of this torsor trivializes the corresponding completed
curve bundle. Apply the additive idelic degree of `114_a_18`:

\[
 (m-m')\log p+(n-n')\log q=0.                                             \tag{2.3}
\]

Exponentiating gives `p^(m-m')q^(n-n')=1`. Unique factorization in `Q^*`
forces both integer exponents to vanish. Hence `(m,n)=(m',n')`. QED.

### Corollary 2.2 (anti-diagonal bypass)

Theorem 2.1 does not assume the unit-detection or effective-descent statements
of `114_a_16`.  Even if the full external Picard map has an anti-diagonal
kernel, that kernel cannot meet the two-prime lattice except at the origin.

More generally, any two multiplicatively independent positive Picard degrees
give the same conclusion.

## 3. Meaning for row A

This closes the abstract algebraic part of Step 1:

> the literal square now contains a verified injective rank-two lattice of
> unit-torsor classes detected by independent curve degrees.

Their realization as completed square lattices with two bounded gauges
remains conditional on H7-PB-REG.

It does not yet close the full continuous bidegree:

1. `Pic(X)^2 -> Pic(Y)` may still have an anti-diagonal kernel outside this
   lattice;
2. the choice of two primes is not canonical under all arithmetic symmetries;
3. `114_a_20` computes the prime-axis sections and an explicit mixed grid,
   but not all sections of `B_{m,n}`;
4. pure external section products cannot yield quadratic logarithmic growth
   by `114_a_14`;
5. the proper gauge, mixed sections, intersection and Riemann--Roch remain
   open.

The next load-bearing problem is therefore Step 2, not the existence of a
rank-two parameter lattice: construct mixed sections for (1.1) whose count is
`exp(Theta(mn))` or `exp(Theta((m+n)^2))` under a proper gauge.

## 4. Verification scope

`114_a_19_h7_discrete_bigrade_verify.py` checks source/Picard anchors and the
unique-factorization argument over a finite exponent box.  The proof itself is
the exact argument above and is not numerical; it does not prove the
fraction-pullback hypothesis exposed in `a_63`.
