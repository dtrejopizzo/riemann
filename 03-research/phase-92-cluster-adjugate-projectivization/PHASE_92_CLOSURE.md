# Phase 92 closure - Exact projectivization before the endpoint limit

## 1. Closed mathematics

The full Feshbach numerator is

```text
N_t(z)
 =det[[F_t,             b_t^eff],
      [h_(t,z)^eff, G_(t,z)^reg]].                    (1.1)
```

and

```text
G_t(z)=N_t(z)/det F_t                                (1.2)
```

away from the cluster singularity.  The determinant in (1.2) cancels exactly
from every normalized safe ratio, while `N_t` continues polynomially through
the singularity.

For the two parity sectors,

```text
N_t(z)
 =G_(t,z)^reg f_Ef_O-h_Eb_Ef_O-h_Ob_Of_E.            (1.3)
```

All parity scales remain in one projective coefficient vector.  No
matched-width construction or dominant eigenline is needed.

## 2. Consequences

```text
removed from the minimal route:
  DOM-E;
  DOM-M;
  matched-width existence;
  simple-line tracking through the endpoint;

retained as optional coordinates:
  Feshbach layer scales;
  Kato line current;
  prime-response kernel.                              (2.1)
```

## 3. New minimal endpoint front

The analytic front is `CA-1` of E92.005.  Complementary invertibility
is removed by the global bordered fallback, and safe base points are handled
by a projective atlas.  Cofinal compatibility is supplied by E92.007.  The
arithmetic front is

```text
CLUSTER-RDI-ANCHOR,                                   (3.1)
```

the identification of the normalized bordered determinant with the
independent Euler--Gamma product.

## 4. Closure grade

```text
closed:
  exact cluster projectivization;
  continuation through cluster singularities;
  parity polynomial;
  inverse-free cluster tangent;
  removal of dominance and matching obligations;
  removal of complementary invertibility as a logical obligation;
  removal of fixed base-point nonvanishing as a separate obligation;
  cofinal projective diagonal without a uniform rate;

open and transferred:
  CA-1 fixed-L projective convergence;
  CLUSTER-RDI-ANCHOR;
  RDI-ANCHOR and Omega7.
```
