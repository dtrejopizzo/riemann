# 107.35 -- Paper A exact audit for connected extraction

## 1. Purpose

This note adds an exact audit artifact for the connected-extraction
layer of `107_03`.

The target is Proposition 4.1 of `107_03`:

\[
 \mathfrak e_1=\log^\star(I),
 \qquad
 \mathfrak e_1(X_a)=X_a,
 \qquad
 \mathfrak e_1(X_{a_1}\cdots X_{a_r})=0 \ (r\ge2).
 \tag{1.1}
\]

This is the structural point behind the separation

\[
 \text{Euler union}
 \neq
 \text{connected extraction}
 \neq
 \text{categorical composition}.
 \tag{1.2}
\]

The same audit also checks the function-field specialization stated in
`107_03` §7: the Euler-product logarithm built from primitive closed
points recovers the exact point-count sequence of the fixed control
curve \(E/\mathbb F_5\).

## 2. Verifier

The exact verifier is
`107_35_paper_a_connected_extraction_preflight.py`.

It performs two finite exact checks.

### 2.1. Hopf-algebra primitive extraction

The script works in the symmetric Hopf algebra on three primitive
generators, truncated to total degree at most four.  It computes the
coproduct exactly, forms the convolution logarithm
\(\log^\star(I)\), and checks:

1. every degree-one generator is fixed by \(\mathfrak e_1\);
2. every monomial of degree at least two is annihilated.

So the verifier directly pressure-tests the connected/disconnected
separation in a nontrivial exact finite window.

### 2.2. Function-field specialization

Using the fixed control curve

\[
 E/\mathbb F_5:\quad y^2=x^3+x+1,
 \tag{2.1}
\]

the script reuses the exact point-count recurrence from the Paper 0
control, reconstructs the primitive closed-point counts \(B_d\), forms
the truncated Euler product

\[
 Z_E(u)=\prod_{d\le16}(1-u^d)^{-B_d},
 \tag{2.2}
\]

and checks exactly that

\[
 \log Z_E(u)=\sum_{n\le16}\frac{N_n}{n}u^n.
 \tag{2.3}
\]

This is the arithmetic specialization of the statement in `107_03` §7
that the Eulerian extractor turns the Euler product into primitive
closed-point data.

## 3. Audit outcome

Running the verifier on Friday, July 31, 2026 produced:

```text
Primitive extraction passed on 3 degree-1 monomials and 31 decomposable monomials.
Euler-product logarithm audit passed through n=16.
```

So `107_03` now has an exact audit layer for two of its sharpest claims:

1. the first Eulerian idempotent does isolate primitive generators and
   kill decomposable Euler unions;
2. the positive-control specialization to \(E/\mathbb F_5\) recovers
   the exact Euler/logarithm identity in a finite audited window.

## 4. What this does not yet prove

This audit still does **not** promote all of Paper A to `proved`.

In particular, it does not by itself prove:

1. the full local determinant package of `107_04`;
2. the Gamma--polar metric package of `107_05`;
3. the full theorem synthesis of `107_06`;
4. the Davenport--Heilbronn failure statement for any specific external
   non-Eulerian \(L\)-series.

What it does prove is narrower and useful: the connected-extraction
mechanism is no longer supported only by formal prose.
