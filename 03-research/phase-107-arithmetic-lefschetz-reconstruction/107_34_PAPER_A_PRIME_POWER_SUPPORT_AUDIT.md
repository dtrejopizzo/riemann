# 107.34 -- Paper A exact audit for prime-power support

## 1. Purpose

This note adds an exact audit artifact for the most arithmetic and most
falsifiable part of Paper A: the finite cyclotomic support law of
`107_04`.

The target under audit is Proposition 5.1 of `107_04`:

\[
 \frac{1}{\varphi(n)}
 \log\left|\operatorname{Res}(\Phi_m,\Phi_n)\right|
 =
 \begin{cases}
 \log p,&m/n=p^a,\\
 0,&\text{otherwise},
 \end{cases}
 \qquad (m>n>1).
 \tag{1.1}
\]

The same audit also checks the diagonal warning of Proposition 7.1:

\[
 \operatorname{Res}(\Phi_n,\Phi_n)=0,
 \tag{1.2}
\]

so the finite diagonal remains an excess-intersection object rather than
a scalar.

## 2. Verifier

The exact verifier is
`107_34_paper_a_prime_power_support_preflight.py`.

It is intentionally self-contained:

1. it reconstructs \(\Phi_n\) recursively from
   \(x^n-1=\prod_{d\mid n}\Phi_d(x)\);
2. it computes resultants exactly via the Sylvester determinant with the
   Bareiss fraction-free elimination algorithm;
3. it checks all pairs in a fixed finite audit window
   \(1\le n\le 24\).

No external CAS is used.

## 3. What is checked exactly

For every \(2\le n<m\le24\), the verifier checks:

1. if \(m/n\) is not an integral prime power, then
   \(|\operatorname{Res}(\Phi_m,\Phi_n)|=1\);
2. if \(m/n=p^a\), then
   \(|\operatorname{Res}(\Phi_m,\Phi_n)|=p^{\varphi(n)}\);
3. the prime support of the resultant is exactly \(\{p\}\) in the
   prime-power case and empty otherwise;
4. symmetry of the absolute norm:
   \(|\operatorname{Res}(\Phi_m,\Phi_n)|
    =|\operatorname{Res}(\Phi_n,\Phi_m)|\).

For every \(1\le n\le24\), it also checks:

5. \(\operatorname{Res}(\Phi_n,\Phi_n)=0\).

## 4. Audit outcome

Running the verifier on Friday, July 31, 2026 produced:

```text
All exact Paper A finite-support checks passed for 1 <= n <= 24.
Verified 253 off-diagonal pairs and 24 diagonal pairs.
```

This does **not** prove all of Paper A.  It proves something narrower
and useful:

1. the finite prime-power support law of `107_04` is pressure-tested by
   exact arithmetic rather than only cited from the source note;
2. the diagonal warning is also pressure-tested exactly in the same
   finite window;
3. Paper A still lacks exact audit artifacts for the archimedean
   Gamma--polar metric, diagonal Green coherence, and the full theorem
   synthesis of `107_06`.

## 5. Consequence for the ledger

After this audit, Paper A should still not be promoted wholesale to
`proved`.  The correct interpretation is:

\[
 \text{Paper A overall formalized},
 \qquad
 \text{finite prime-power support law exactly audited}.
 \tag{5.1}
\]

So the new verifier strengthens one foundational subclaim without
inflating the status of the entire package.
