# E78.148 - Residue sign autopsy: the Herglotz route to the zero-side is dead

**Run:** 2026-07-21.
**Scope:** IDENT, fixed-L; companion to E78.147.
**Class:** AUTOPSIA (refutes one rigorization route; sharpens the open lemma).

## 1. Purpose

E78.147 reduced fixed-L convergence to `ZERO-SIDE-BOUNDEDNESS`: the zeta
zero-side is a bounded, sigma-independent correction (`~0.83`) to the rigorous
build-independent pole-pair term `P_N = O(sigma/N^2)`. The natural rigorization
is Herglotz/interlacing: if

```text
F_{L,N}(z) = 1 + sum_n r_n^{(N)}/(z - d_n),   r_n = a_N u_n + b_N v_n,
```

has sign-definite residues `r_n`, then `F_{L,N}` is (up to sign) Nevanlinna, its
zeros strictly interlace the symmetric mesh `{d_n}`, the interlaced zeros pair
up `+-`, and the zero-side gets its own `O(sigma/N^2)` just like the pole side.
This note tests the hypothesis and refutes it.

## 2. Result (probe E78_148_residue_sign_probe.py, lambda=6, dps=50)

```text
zeta   N= 8  total=15  pos= 8 neg= 7   sign-mixed    max|Im r|=0
zeta   N=10  total=19  pos=11 neg= 8   sign-mixed    max|Im r|=0
zeta   N=12  total=23  pos=10 neg=13   sign-mixed    max|Im r|=0
zeta   N=14  total=27  pos=12 neg=15   sign-mixed    max|Im r|=0
zeta   N=16  total=31  pos=19 neg=12   sign-mixed    max|Im r|=0
plant  N= 8  total=15  pos=15 neg= 0   SIGN-DEFINITE max|Im r|=0
plant  N=10  total=19  pos=15 neg= 4   sign-mixed    max|Im r|=0
plant  N=12  total=23  pos=15 neg= 8   sign-mixed    max|Im r|=0
plant  N=14  total=27  pos=15 neg=12   sign-mixed    max|Im r|=0
plant  N=16  total=31  pos=15 neg=16   sign-mixed    max|Im r|=0
```

The residues are exactly real (`max|Im r| = 0`, as required by self-adjointness),
but for the zeta build they are **sign-mixed at every N**. So `F_{L,N}` is NOT a
Herglotz/Nevanlinna function, its zeros do not simply interlace the mesh, and the
`+-` zero-pairing argument does not apply.

## 3. Reading

1. The clean zeta zero-side correction (`~0.83`, sigma-independent, E78.147 Sec 5)
   is therefore NOT a consequence of interlacing. It holds for a non-obvious
   reason -- a genuine open structural fact, not a formality.
2. Curiosity: the plant residues start sign-definite (all 15 positive at N=8,
   which equals the 2*8-1 inner size) and acquire exactly the new modes as
   negatives (pos frozen at 15, neg = 0,4,8,12,16). The zeta residues have no
   such frozen-positive core. This is a structural fingerprint separating the
   builds at the residue level, but it is a regularity/anatomy difference, not
   used as a forcing detector (E77.7az).

## 4. Consequence

`ZERO-SIDE-BOUNDEDNESS` (E78.147 Sec 6) must be proved by a mechanism other than
Herglotz interlacing. The indicated route is the **residue-evolution law**: bound
the convergence rate of the fixed-mesh residues `r_n^{(N)} -> r_n^{(inf)}` as
`N -> inf` (for fixed n), and show the tail/readjustment contributes a bounded
sigma-independent multiple of the pole-pair term. That is the next analytic
target; the interlacing shortcut is closed.

## 5. Status

```text
refuted:
  Herglotz/interlacing rigorization of the E78.147 zero-side -- zeta residues
  r_n^{(N)} are real but sign-mixed at every tested N, so F_{L,N} is not
  Nevanlinna;

observed:
  plant residues have a frozen positive core of size 2N0-1 (N0=8) with new modes
  entering negative -- a residue-level build fingerprint (regularity, not a
  forcing detector);

open (unchanged, sharpened):
  ZERO-SIDE-BOUNDEDNESS via the residue-evolution law r_n^{(N)} -> r_n^{(inf)},
  NOT via interlacing;

next:
  measure the residue-evolution rate and test whether its tail reproduces the
  ~0.83 zero-side correction.
```
