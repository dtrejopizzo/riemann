# 107.36 -- Paper B exact audit for the function-field return/Lefschetz shadow

## 1. Purpose

This note adds an exact audit artifact for the function-field control
shadow of Paper B.

The target is not the whole flow construction of `107_07`--`107_09`.
What is audited here is narrower:

\[
 \Gamma_m\circ\Gamma_n=\Gamma_{m+n},
 \qquad
 \Gamma_n\cdot\Delta=N_n,
 \qquad
 \Gamma_m\cdot\Gamma_n=q^nN_{m-n},
 \tag{1.1}
\]

in the fixed positive control

\[
 E/\mathbf F_5:\quad y^2=x^3+x+1.
 \tag{1.2}
\]

These are exactly the function-field arithmetic shadows of the
same-tower return law, diagonal Lefschetz trace, and cross-check package
that Part II intends to encode source-geometrically.

## 2. Verifier

The exact verifier is
`107_36_paper_b_return_lefschetz_preflight.py`.

It reuses the exact point-count recurrence of the fixed elliptic
control and checks, in a finite window \(n\le12\):

1. same-tower additive composition of return labels:
   \(k\log 5+\ell\log 5=(k+\ell)\log 5\);
2. multiplicative degree compatibility:
   \(5^k\cdot 5^\ell=5^{k+\ell}\);
3. diagonal Lefschetz trace:
   \(N_n=5^n+1-a_n\);
4. graph-vs-graph arithmetic cross-check:
   \(\Gamma_m\cdot\Gamma_n=5^nN_{m-n}\) for \(m>n\);
5. the balanced half-density descriptor attached to bidegree
   \((1,5^n)\), namely \(5^{-n/2}\).

The last item is recorded symbolically because the critical weight is a
half-power normalization rather than an integer count.

## 3. Audit outcome

Running the verifier on Friday, July 31, 2026 produced:

```text
All Paper B function-field return/Lefschetz checks passed through n=12.
Verified 66 same-tower compositions and 66 graph-vs-graph cross-checks.
```

So Paper B now has an exact arithmetic anchor for the same-tower
function-field specialization of its return/composition/Lefschetz
package.

## 4. What this does and does not prove

This audit is useful but deliberately limited.

It does prove that:

1. the arithmetic shadow of the same-tower return semigroup is exact in
   the fixed control window;
2. the diagonal Lefschetz count and graph-vs-graph cross-check agree
   with the control recurrence;
3. the bidegree-to-balance normalization is aligned with the Paper 0
   control.

It does **not** yet prove:

1. the mixed-tower refinement geometry of `107_07`;
2. the common-phase suspension geometry of `107_08`;
3. the joint prime--Gamma--polar fixed-point derivation of `107_09`;
4. the full Davenport--Heilbronn falsifier as an independently audited
   external counterexample.

So the correct status consequence is conservative:

\[
 \text{Paper B overall formalized},
 \qquad
 \text{same-tower function-field shadow exactly audited}.
 \tag{4.1}
\]
