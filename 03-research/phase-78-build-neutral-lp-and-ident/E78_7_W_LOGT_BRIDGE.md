# E78.7 - The W/LOGT bridge

**Run:** 2026-07-18.
**Scope:** IDENT, finite/fixed-L side.

## 0. ERRATUM (2026-07-21)

The claim in Sec. 3 that the boundary-pole term `-1/(z-d_b)` cancels across
sections "because `d_b` depends only on `L`, not on the section depth `N`" is
FALSE. The boundary index is `idx[-1] = n_modes = N`, so `d_{b,N} = 2 pi N/L`
DOES depend on `N`. Therefore the exact identity `(WL-7) LOGT-CELL =
W-QUOTIENT-DELTA` does NOT hold; the correct relation is

```text
LOGT-CELL = Delta[T'/T]
          = W-QUOTIENT-DELTA - [ 1/(z-d_{b,N+2}) - 1/(z-d_{b,N}) ].
```

The correction term is the moving-boundary increment. It is not zero, but it is
explicit and summable: on any bounded safe collar `|1/(z-d_{b,N})| = O(N^{-1})`
and its consecutive difference is `O(N^{-2})`. Hence W-QUOTIENT-DELTA summable
<=> LOGT-CELL summable, and the WL-10 chain's *conclusion* (summability =>
fixed-L convergence) survives, but WL-7 must be read as "equal up to a summable
explicit boundary increment", not as an exact identity. See E78.149 (true object
recomputed) and E78.147 Sec 0.5.

## 1. Purpose

E78.6 reduced the fixed-L IDENT object to the coupled holomorphic package

```text
W_{L,N}(z)=a_b(U+U_b)+b_b(V+V_b),
W'_{L,N}(z)=a_b U'(z)+b_b V'(z),
```

while the Phase-77 section-lag front was already reduced to the partition-
invariant moving-section quantity

```text
LOGT-CELL:
  Delta 2 Re(i T_N'/T_N).
```

This note proves that these are the same object in different coordinates.  So
the new Phase-78 package does not open a third arithmetic front; it is exactly
the invariant content already isolated in E77.5l.

## 2. Exact algebra

From P76.041:

```text
T_{L,N}(z)=F_{L,N}(z)/(z-d_b),                               (WL-1)

F_{L,N}(z)=1+W_{L,N}(z),                                     (WL-2)

F'_{L,N}(z)=W'_{L,N}(z).                                     (WL-3)
```

Therefore

```text
T'_{L,N}(z)/T_{L,N}(z)
=F'_{L,N}(z)/F_{L,N}(z)-1/(z-d_b)
=W'_{L,N}(z)/(1+W_{L,N}(z)) - 1/(z-d_b).                    (WL-4)
```

Taking the safe-axis invariant used in E77.5l gives

```text
2 Re(i T'_{L,N}(i sigma)/T_{L,N}(i sigma))
=2 Re( i W'_{L,N}(i sigma)/(1+W_{L,N}(i sigma))
      -i/(i sigma-d_b) ).                                    (WL-5)
```

This is exactly the nontrivial part of the cell-smoothed symbol `J_{L,N}` from
E78.6.

## 3. Consecutive-section bridge

For one fixed `L` and one consecutive step `N -> N+2`, subtract `(WL-5)`:

```text
Delta_N logT(sigma)
:=2 Re i[ T'_{L,N}(i sigma)/T_{L,N}(i sigma)
         -T'_{L,N+2}(i sigma)/T_{L,N+2}(i sigma) ]

=2 Re i[
   W'_{L,N}(i sigma)/(1+W_{L,N}(i sigma))
  -W'_{L,N+2}(i sigma)/(1+W_{L,N+2}(i sigma))
  ].                                                         (WL-6)
```

The boundary pole term `-1/(z-d_b)` cancels because `d_b` depends only on `L`,
not on the section depth `N`.

Thus:

```text
LOGT-CELL = W-QUOTIENT-DELTA.                                (WL-7)
```

This identity is exact.

## 4. Consequence for the fixed-L front

E77.5l already proved that the section-lag reconstruction is partition-
invariant and exact:

```text
E_{L,N} - E_{L,N+2}
= Delta 2 Re(i T'/T) - Delta B_ext,L,N.                      (WL-8)
```

Using `(WL-6)`, the finite/fixed-L convergence of the E78.6 package is therefore
equivalent to controlling the consecutive differences of the quotient

```text
W'_{L,N}/(1+W_{L,N})                                         (WL-9)
```

rather than the raw coordinates `W_{L,N}` or `W'_{L,N}` separately.

This is better aligned with the Phase-77 autopsies:

```text
- coordinate-dependent theta objects are dead (E77.5k);
- the invariant quantity is the safe log-transfer update (E77.5l);
- E78.6's W-package is exactly the numerator/denominator package behind that
  invariant.
```

## 5. Reduced target

The fixed-L side of IDENT now reduces to:

```text
W-QUOTIENT-DELTA:
prove that the consecutive differences of

  W'_{L,N}(i sigma)/(1+W_{L,N}(i sigma))

have a summable cofinal envelope on safe compacta, together with a zero-free
bound for 1+W_{L,N}.
```

Indeed:

```text
W-QUOTIENT-DELTA + zero-free denominator
=> LOGT-CELL summability
=> SECTION-LAG control
=> fixed-L convergence of J_{L,N}.                           (WL-10)
```

The implication `(WL-10)` uses only the exact identities `(WL-6)` and
E77.5l `(WL-8)`.

## 6. Reading

This is a genuine simplification of the live arithmetic front.

Before E78.7, the package `W_{L,N},W'_{L,N}` from E78.6 and the section-lag
package from E77.5l looked like two neighboring but separate fronts.

After E78.7:

```text
they are one front.
```

The candid open object is not the raw holomorphic pair and not the full
cell-smoothed symbol, but the invariant quotient-delta `(WL-9)`.

## 7. Status

```text
proved:
  the E78.6 coupled-generator package and the E77.5l LOGT-CELL invariant are
  exactly the same finite object after the change of variables F=1+W;

proved:
  consecutive section lag is the exact quotient-delta of W'/(1+W);

reduced:
  COUPLED-GENERATOR-LIMIT to the smaller invariant target W-QUOTIENT-DELTA
  plus a zero-free denominator bound;

clarified:
  no new arithmetic front was created by E78.6; it merges with the existing
  Phase-77 section-lag machinery;

live:
  derive a summable envelope or an exact shell-update law for
  Delta[W'/(1+W)] on safe compacta.
```
