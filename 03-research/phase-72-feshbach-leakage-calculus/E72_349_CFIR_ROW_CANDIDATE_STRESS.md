# E72.349 -- CFIR row-candidate stress test

**Purpose.** Move from abstract row-ideal algebra to the actual Phase 72 finite harness.  This test
uses the full singular operator

```text
E=H_actual-lambda_0 I,
```

whose null vector is the pole-even ground vector `xi`.  This is the correct object for row-ideal
membership; the shorted complement matrix `C_E` is invertible and would give a false row-ideal test.

## 1. Rows tested

Let

```text
k_z(m)=(1-e^(zL))/(iz-d_m).
```

For finite Cauchy roots `tau`, use shifted representatives

```text
a=i tau.
```

Three candidate rows are tested:

```text
base:
  mu k_a.

self:
  (mu-K_L(a,a))k_a.

window:
  mu k_a - sum_{w in W_T} K_L(a,w)k_w.
```

These are not the full `R_T`; they omit the collapsed tail and several normalization terms.  They are
stress tests for the row-ideal detector and for the finite interpolation layer.

## 2. Control nodes

Two node types are used:

```text
root:
  a=i tau, where tau is a finite Cauchy root.

shift:
  a=0.5+i tau.
```

At `root` nodes, `k_a xi=G(a)=0` by construction, so base rows should be nearly in the row ideal.  At
`shift` nodes this root cancellation is absent; row-ideal defects should be visible.

## 3. Distance used

Since `E` is Hermitian with one-dimensional nullspace spanned by normalized `xi`,

```text
dist(row,Row(E)) = |row xi|.
```

The relative defect is

```text
relNull = |row xi|/||row||.
```

This is better conditioned than raw replacement determinants in the current finite harness, where
determinants can underflow.

## 4. Status

```text
proved: the correct finite operator for row-ideal testing is H_actual-lambda_0 I;
proved: rowspace distance is the null component |row xi|;
tested: base/self/window candidate rows at root and shifted control nodes.
```
