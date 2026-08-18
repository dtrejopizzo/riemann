# E77.7i - Safe limit-point endpoint audit

**Run:** 2026-07-18.

## 1. Reason for the audit

E77.7f--g use the implication

```text
BTG-DIV-L
=> bordered Weyl-disk radius tends to zero
=> CORRECTED-LP.
```

P76.065, however, defines the required endpoint as

```text
SAFE-LIMIT-POINT:
among l2 solutions of the infinite rectangular CCM equation,
r_{z0}v=1 selects a unique safe Cauchy transform.
```

Since E77.7d proves compact resolvent and makes `mu_L` an eigenvalue, the
last arrow needs a separate multiplicity/cyclicity audit.

## 2. Exact finite-dimensional obstruction

Let

```text
E_L = ker(H_L-mu_L),
ell_0(v)=r_{z0}v,
ell_z(v)=r_zv.
```

The normalized solution set is

```text
N_L={v in E_L : ell_0(v)=1}.
```

Assume `N_L` is nonempty.  Its safe transform at `z` is unique exactly when

```text
ell_z|_(E_L cap ker ell_0)=0.                    (I-1)
```

Indeed, any two normalized solutions differ by an element of
`E_L cap ker ell_0`, and the converse follows by adding such an element.
Uniqueness for every safe `z` is therefore equivalent to

```text
E_L cap ker ell_0 is contained in the common kernel of all safe ell_z.
                                                        (I-2)
```

If safe Cauchy rows separate vectors in `E_L`, `(I-2)` reduces to

```text
dim E_L=1 and ell_0(v_0) != 0.                  (I-3)
```

Thus compact resolvent alone is insufficient: it gives only finite
multiplicity, not simplicity or a nonzero normalizing functional.

## 3. What BTG-DIV-L proves directly

The spectral identity in E77.7f--g gives

```text
BTG-DIV-L
<=> ||A_N(mu_L)^(-1)b_N||^2 -> infinity
=> scalar bordered Weyl radius -> 0.            (I-4)
```

Statement `(I-4)` is an operational scalar contraction.  Without a theorem
identifying this scalar disk with the full family of safe transforms on
`E_L`, it does not by itself prove `(I-2)` or `(I-3)`.  In particular,
declaring that a singular finite block has "already collapsed" is valid
only after specifying the regularized disk and proving that its limiting
point is independent of the null direction.

## 4. Minimum admissible interface lemma

The missing bridge is:

```text
SAFE-DISK-IDENT:
for the CCM boundary triple at fixed L and mu_L,
  (a) the finite scalar disks are the images under all safe Cauchy rows of
      the normalized l2 solution family;
  (b) singular sections are interpreted by the boundary-relation limit;
  (c) radius -> 0 implies (I-2), locally uniformly on the safe axis.
```

Then the candid chain is

```text
BTG-DIV-L + SAFE-DISK-IDENT
=> SAFE-LIMIT-POINT of P76.065.
```

An alternative sufficient theorem is `(I-3)` together with separation and
finite-section convergence to the ground eigenspace, but that route must
not reuse the refuted fixed-overlap target of E77.7f.

## 5. Status

```text
proved:      normalized-transform uniqueness criterion (I-1)--(I-2);
proved:      under separation, simplicity/nonvanishing (I-3) is sufficient;
proved:      compact resolvent alone does not supply (I-2) or (I-3);
conditional: BTG-DIV-L => SAFE-LIMIT-POINT requires SAFE-DISK-IDENT;
open:        SAFE-DISK-IDENT for the long-range CCM boundary relation;
open:        treatment of singular finite sections in that relation.
```

This audit uses only linear algebra on the ground eigenspace and the exact
BTG identity.  It introduces no positivity, inverse-gap estimate, zero
filter, or arithmetic continuation.
