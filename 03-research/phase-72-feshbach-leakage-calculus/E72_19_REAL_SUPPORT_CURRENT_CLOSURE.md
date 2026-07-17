# E72.19 -- Real-support closure for divisor currents

**Date:** 2026-07-08.
**Role:** prove the functional theorem behind the finite residue cobordism: if finite CCM divisor
currents supported on the real axis converge as currents to the global `Xi` divisor current, then RH
follows.

## 0. The point

E72.18 shows that finite CCM real-zero divisors have no off-real residue. The only way an off-line zero
can appear in the limit is by failure of current convergence on off-real test contours.

This document proves the exact closure theorem.

## 1. Divisor currents

Let `S` be the centered critical strip

```text
S = { z in C : |Im z| < 1/2 }.
```

Let `F_x` be the finite CCM spectral functions from Phase 71, normalized so that their divisor currents
are

```text
[D_x] := (1/(2pi i)) d(d log F_x).
```

Equivalently, for a compactly supported smooth test function `phi`,

```text
<[D_x],phi> = sum_{F_x(r)=0} m_x(r) phi(r),
```

with all roots `r` real.

Let

```text
[D_Xi] := sum_{Xi(rho)=0} m(rho) delta_rho
```

be the divisor current of `Xi` in `S`.

## 2. The closure theorem

### Theorem 72.19

Assume:

1. every finite divisor `D_x` is supported on the real axis;
2. the divisor currents converge in distributions on `S`:

```text
[D_x] -> [D_Xi]  in  D'(S).                       (DCC)
```

Then every zero of `Xi` in `S` lies on the real axis. Hence RH follows.

### Proof

Let `rho` be a non-real point in `S`. Choose a disk

```text
U = D(rho,r) compactly contained in S
```

with `U cap R = empty`.

For every `x`, since `supp[D_x] subset R`,

```text
<[D_x],phi> = 0
```

for every `phi in C_c^\infty(U)`.

Passing to the distributional limit `(DCC)` gives

```text
<[D_Xi],phi> = 0
```

for every such `phi`. Therefore `[D_Xi]` has no support in `U`.

If `rho` were a zero of `Xi`, choose `phi>=0` supported in `U` with `phi(rho)>0` and with support small
enough to contain no other zero except the finite multiplicity cluster at `rho`. Then

```text
<[D_Xi],phi> = m(rho)phi(rho) > 0,
```

contradiction. Thus no non-real zero exists in `S`. `QED`

## 3. Equivalent contour form

The same theorem can be stated in residue language. If for every off-real contour `Omega`

```text
(1/(2pi i)) int_{partial Omega} Phi(s)d log F_x(s)
 ->
(1/(2pi i)) int_{partial Omega} Phi(s)d log Xi(s)
```

for every holomorphic test `Phi`, then the right-hand side must vanish because the left-hand side is
zero for all large `x`. Hence `Xi` has no off-real residues.

## 4. Why this is not circular

The theorem itself does not assume RH or positivity. It uses only:

```text
finite real-rootedness,
distributional divisor-current convergence.
```

The theorem is therefore a valid new closure principle:

```text
finite real-zero CCM divisors + current convergence => RH.
```

The unresolved mathematical work is now exactly `(DCC)`.

## 5. Relation to E72.18

E72.18 proves the test-current version needed for the resonance block:

```text
finite residue current zero off real
  + relative current convergence against R_x(s)/s
  => maximal resonance cancellation.
```

E72.19 proves the stronger global statement:

```text
finite divisor current convergence
  => no off-real Xi divisor.
```

Thus the route has a clean hierarchy:

```text
DCC  => RH directly;
RCCC => ACD resonance cancellation => reduced leakage => stable divisor convergence => RH.
```

The stronger theorem is easier to state; the weaker RCCC may be easier to prove because it tests only
the specific one-vector resonance family.
