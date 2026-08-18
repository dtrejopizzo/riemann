# E80.009 - Minimal LP boundary-trace cut

## 1. Exact boundary-trace quantity

At fixed `L`, let

```text
A_N(mu_L)=H_L[I_N,I_N]-mu_L I,
b_N=H_L[I_N,N].                                       (1.1)
```

When `A_N(mu_L)` is invertible, define

```text
S_N(mu_L)=||A_N(mu_L)^(-1)b_N||^2.                     (1.2)
```

If `(nu_j^(N),u_j^(N))` are the eigenpairs of the inner block, the finite
spectral theorem gives

```text
S_N(mu_L)
 = sum_j |<u_j^(N),b_N>|^2/|nu_j^(N)-mu_L|^2.          (1.3)
```

Thus `BTG-DIV` is exactly `S_N(mu_L)->infinity`.  No approximation enters
(1.3).

## 2. A Ritz bracket does not imply boundary-trace divergence

The Feshbach program estimates the low spectral denominator.  It cannot by
itself control the moving boundary numerator.

### Proposition 2.1

There are positive matrices `A_N`, spectral points `mu=0`, and sources `b_N`
such that

```text
min spec(A_N)=delta_N -> 0,                             (2.1)
```

while `||A_N^(-1)b_N||->0`.

### Proof

Take

```text
A_N=diag(delta_N,1),
b_N=delta_N^2 e_1,
delta_N=1/N.                                           (2.2)
```

Then the lowest denominator tends to zero, but

```text
||A_N^(-1)b_N||=delta_N->0.                            (2.3)
```

`QED`

This example is not a CCM counterexample.  It proves the logical point that a
Ritz or Feshbach envelope must be accompanied by a directional lower estimate
for the actual source.  That additional estimate is precisely the divergent
low-mode sum already present in the inherited implication.

## 3. Exact status of the Feshbach route

Compact resolvent already gives qualitative Ritz convergence

```text
mu_R decreases to mu_L.                                (3.1)
```

The weighted Feshbach equation provides an exact method for certifying the
size of `mu_R-mu_L`.  It is useful if one proves, on the same scale,

```text
sum_{j<K}|<u_j^(N),b_N>|^2
 /( |nu_j^(N)-mu_R|+eta_R )^2 -> infinity.              (3.2)
```

But (3.2), not the bracket alone, carries the boundary-trace conclusion.
Therefore

```text
WFE-CYCLIC-TAIL + (3.2) => BTG-DIV,                    (3.3)
```

whereas `WFE-CYCLIC-TAIL => BTG-DIV` is false as a formal implication.

The Feshbach envelope is one possible proof route to the denominator control
inside BTG-DIV.  It is not an additional mandatory link in the final chain.

## 4. Minimal LP cut

Combining this note with E80.007 gives the smallest currently valid LP cut:

```text
LP-1  BTG-DIV:
      S_N(mu_L)->infinity for the true fixed-L spectral point;

LP-2  MU-FREE-COMPLETENESS:
      clauses MF-1--MF-6, identifying the disk intersection with the full
      normalized square-summable solution family.                      (4.1)
```

Then

```text
LP-1 + LP-2
 => scalar disk contraction plus full-family identification
 => the corrected LP endpoint.                         (4.2)
```

Every Feshbach, low-mode or cyclic-tail lemma is admissible only as a route to
`LP-1`.  It does not replace `LP-2`.

## 5. Status

```text
proved:
  the exact BTG spectral identity (1.3);
  a vanishing Ritz denominator alone does not imply BTG divergence;

closed:
  classification of FESHBACH-RITZ-ENVELOPE as an optional denominator route,
  not a separate final-chain obligation;

reduced:
  the complete LP front to LP-1 plus LP-2;

open:
  BTG-DIV for the CCM moving boundary source;
  MU-FREE-COMPLETENESS, clauses MF-1--MF-6;

optional route:
  WFE-CYCLIC-TAIL together with the directional low-mode estimate (3.2).
```

