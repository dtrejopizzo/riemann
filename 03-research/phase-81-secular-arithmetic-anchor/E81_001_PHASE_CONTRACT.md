# E81.001 - Secular-anchor contract

## 1. Target

Let `C_{L,N}` be the bilateral core characteristic of Phase 80 and let `E_L`
be the independent Euler--Gamma product.  First assume the fixed-`L`
projective limit `C_L` exists.  The target is

```text
RDI-ANCHOR:
for every safe simply connected V and s_* in V,

  [C_L(s)/C_L(s_*)]/[E_L(s)/E_L(s_*)] -> 1

locally uniformly on V as L->infinity.                 (1.1)
```

Equivalently,

```text
d/ds log C_L(s)-H_L(s) -> 0                            (1.2)
```

locally uniformly, where `H_L=E_L'/E_L`.

## 2. Admissibility

Every reduction must preserve the complete bilateral and mesh-renormalized
object.  The following moves are excluded:

```text
- replacing the coupled Schur quotient by a hard prime trace;
- identifying a limit from fixed-L convergence alone;
- taking absolute values before the reflected transfer factors are combined;
- using a zero of xi or a zero-location statement as input;
- replacing a directional rank-one determinant by an ambient inverse norm;
- assuming C_L'/C_L=H_L at each finite L.
```

## 3. Proof obligation

The bordered determinant formula is finite algebra and holds for comparison
builds as well.  Therefore it is infrastructure.  Arithmetic content enters
only when its secular residues are identified with the independent
Euler--Gamma current in the outer limit.  The representation must remain valid
when `c_{L,N}=0`; division by this scalar is not admissible.

## 4. Status

```text
fixed input:
  exact finite bordered determinant representation;
  independent product E_L and current H_L;

open:
  the outer relative determinant identity (1.1);

next:
  remove every determinant and inverse from the target in favor of one
  explicit rank-one secular transform.
```
