# E92.003 - Exact parity polynomial

## 1. Two scalar parity sectors

For the endpoint cluster of E88.004,

```text
F_t=diag(f_(E,t),f_(O,t)).                            (1.1)
```

Write the corresponding effective rows and sources as

```text
h_(t,z)^eff=(h_(E,t,z),h_(O,t,z)),
b_t^eff=(b_(E,t),b_(O,t))^T.                         (1.2)
```

E92.001 becomes

```text
N_t(z)
 =G_(t,z)^reg f_(E,t)f_(O,t)
  -h_(E,t,z)b_(E,t)f_(O,t)
  -h_(O,t,z)b_(O,t)f_(E,t).                          (1.3)
```

This is an exact identity, including at `f_E=0` or `f_O=0`.

## 2. No matched-width requirement

The nested scales of E88.004 describe which term of (1.3) is largest in a
chosen coordinate.  They are not required to define the projective endpoint
object.  All three coefficients can be retained until the endpoint and outer
limits are taken.

More precisely, let

```text
c_t=(f_(E,t)f_(O,t),-b_(E,t)f_(O,t),-b_(O,t)f_(E,t)) (2.1)
```

and

```text
V_(t,z)=(G_(t,z)^reg,h_(E,t,z),h_(O,t,z)).            (2.2)
```

Then

```text
N_t(z)=c_t dot V_(t,z).                               (2.3)
```

Only the projective class `[c_t]` matters in normalized safe ratios.  A
single common scaling of all three entries cancels.  Distinct parity scales
are therefore coordinates on the same finite projective coefficient space,
not separate singular layers that must be multiplied.

## 3. Cofinal compactness and its limit

Finite-dimensional projective space is compact.  Every cofinal sequence with
`c_t` nonzero has a subsequence for which `[c_t]` converges.  If the regular
profiles in (2.2) also converge, (2.3) gives a subsequential projective
endpoint numerator.

This proves existence of projective cluster subsequences.  It does not prove
uniqueness or identify their limit with the Euler--Gamma profile.  Those are
the convergence and arithmetic clauses of RDI.

## 4. Status

```text
proved:
  exact parity polynomial;
  elimination of a matched-width hypothesis from projective definition;
  subsequential compactness of the finite coefficient class;

open:
  uniqueness of the coefficient-profile limit;
  Euler--Gamma identification.
```

