# E80.001 - Phase contract and dependency cut

## 1. Mathematical endpoint

For each physical cutoff `L`, let `T_{L,N}` be the finite CCM transfer of the
safe-ratio construction.  Put

```text
u = s - 1/2,
z_+(s) = i u,
z_-(s) = -i u.
```

The raw finite bilateral characteristic is

```text
C^raw_{L,N}(s)
  = sinh(Lu/2)^2 T_{L,N}(z_+(s)) T_{L,N}(z_-(s)).       (1.1)
```

For real `s>1`, the transfer has real coefficients, hence

```text
C^raw_{L,N}(s)
  = sinh(Lu/2)^2 |T_{L,N}(iu)|^2 > 0.                  (1.2)
```

Let `Z^ext_{L,N}(z)` be the explicit external-mesh canonical product of
P76.037 and set

```text
C_{L,N}(s)
 = C^raw_{L,N}(s)/Z^ext_{L,N}(-iu).                    (1.3)
```

This is the core characteristic used below.  The external product is
holomorphic and zero-free after restriction to `Re s>1`.  Its removal is
compulsory at the natural horizon `N/L->infinity`; otherwise the known mesh
background remains in the logarithmic derivative.  One could keep the raw
object only under the stronger condition `N/L^2->infinity`.

The arithmetic comparison object is the finite Euler--Gamma product

```text
E_L(s)
  = s^2(s-1)^2 pi^{-s} Gamma(s/2)^2
    exp(2 sum_{2<=n<=exp(L)} Lambda(n)n^{-s}/log n).    (1.4)
```

The principal theorem sought in this phase has two quantified layers.

```text
RDI-CONV:
for every fixed L, every simply connected V compactly contained in
{Re s>1}, and one base point s_* in V, the normalized ratios

  C_{L,N}(s)/C_{L,N}(s_*)

converge locally uniformly on V as N->infinity to a zero-free ratio
C_L(s)/C_L(s_*).                                       (1.5)

RDI-ANCHOR:
for every such V and s_*,

  [C_L(s)/C_L(s_*)]/[E_L(s)/E_L(s_*)] -> 1

locally uniformly on V as L->infinity.                 (1.6)
```

Equivalently, one may choose a cofinal diagonal `N=N(L)` and require the same
relative ratio to tend to one.  The scalar is unavoidable and harmless: safe
ratios and logarithmic derivatives do not see it.

Requiring `C_{L,N}/E_L` to become projectively constant as `N->infinity` for
each fixed `L` would assert the stronger identity `C_L'/C_L=E_L'/E_L` at every
finite `L`.  That is not the inherited endpoint.  Only the outer defect in
(1.6) must vanish.

## 2. Why the bilateral factor is compulsory

Differentiating the raw object (1.1) gives

```text
d/ds log C^raw_{L,N}(s)
 = L coth(Lu/2)
   + i T'_{L,N}(iu)/T_{L,N}(iu)
   - i T'_{L,N}(-iu)/T_{L,N}(-iu).                    (2.1)
```

On the real safe axis this becomes

```text
d/ds log C^raw_{L,N}(s)
 = L coth(Lu/2)
   + 2 Re(i T'_{L,N}(iu)/T_{L,N}(iu)).                (2.2)
```

For the core object, subtract

```text
B^ext_{L,N}(s)=d/ds log Z^ext_{L,N}(-iu).               (2.3)
```

On the real safe axis this is the explicit `B_ext` term of P76.037.  The
resulting expression is exactly the finite core derivative package inherited
from the safe-ratio chain.  Comparing only the bordered determinant
`F_{L,N}` would omit the hyperbolic term, one reflected transfer and the mesh
renormalization.  Such a comparison cannot imply `SR-SAFE` without restoring
all three factors.

## 3. Dependency cut

The route separates into four logical modules.

```text
Module A: fixed-L convergence
  GAP-Z plus the proved MESH and BND estimates.

Module B: arithmetic identification
  RDI-ANCHOR, equivalently outer vanishing of the intrinsic
  Euler--Gamma logarithmic-derivative defect.

Module C: LP interface and radical tails
  mu-free disk intersection, RDP-SHELL, PROLATE, WEIL-TAIL.

Module D: normal-family closure
  SR-SAFE => Omega7, already proved in P76.034.
```

No statement in Module A selects the limit in Module B.  No statement in
Module B by itself proves the tail estimates in Module C.  Consequently the
claim that one named finite signature carries the complete difficulty is not a
theorem until Modules A and C are independently closed.

## 4. Conservation statement

Since `Omega7` is equivalent to RH, every complete proof of the chain contains
at least one assertion not obtainable from the presently closed inputs.  The
stronger phrase "exactly one assertion" does not follow formally: two distinct
open lemmas may both imply RH after different closed reductions.

The phase therefore uses the following precise rule:

```text
Difficulty localization means finding a minimal sufficient cut of open
statements, not assuming in advance that the cut has cardinality one.  (4.1)
```

## 5. Exit conditions

The phase closes only under one of the following outcomes.

```text
A. RDI and every remaining module are proved.
B. RDI is reduced to one new exact identity and every other module is either
   proved or moved to a separately stated phase with no hidden dependency.
C. RDI or a downstream implication is refuted, with the exact failed assertion
   and a corrected replacement theorem.
```

## 6. Status

```text
proved:
  the correct bilateral core comparison object is (1.3), by direct
  differentiation and the external-mesh renormalization;
  the dependency cut into Modules A--D;

corrected:
  a relative determinant containing only F_{L,N}, or the unrenormalized raw
  characteristic at the natural horizon, is incomplete for SR-SAFE;
  conservation gives at least one hard assertion, not automatically exactly one;

open:
  RDI-CONV and RDI-ANCHOR;
  Modules A and C;

next:
  construct E_L independently and prove its exact derivative and outer limit.
```
