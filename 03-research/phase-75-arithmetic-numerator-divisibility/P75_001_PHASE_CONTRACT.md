# P75.001 - Phase contract and closure ledger

Date: 2026-07-16.

## Target

Phase 75 attacks the exact finite numerator obstruction:

```text
EG_LOCK_L(gamma)
= T_W02(i gamma)[xi_L]
- T_WR(i gamma)[xi_L]
- T_Prime(i gamma)[xi_L].
```

The desired theorem is:

```text
ARITH-LOCK:
For every natural resolved window W and every M,
|C_L(gamma_j)| <= A_{W,M} L^-M
```

for the critical ordinates `gamma_j` in the window, with constants uniform in
the window after fixing its height range and multiplicity pattern.

The logical closure ledger is:

```text
ARITH-LOCK
=> CRIT-NUM-DIV
=> CCM-ROOT-LOCK
=> CAUCHY-EIG-LOC
=> HPR-DIV
=> E72.396 NAT-PROJ
=> E72.326 PW-Cauchy
=> SQB => CB => RNS => MC-NZ => NZ-MSD
=> scalar WRL
=> Omega7.
```

## Finite regime

`L` is the CCM length parameter.  The symmetric index set is

```text
I_L={-N_L,...,-1,1,...,N_L}
```

or the locally established equivalent from the Phase 71/72 builder.  The
mesh is

```text
d_n=2 pi n/L.
```

Resolved windows satisfy

```text
d_max >= (1+delta) max_{gamma in W} |gamma|
```

with fixed `delta>0`.  The cutoff size `M_L` is allowed to grow
polynomially or subexponentially only when the Hilbert/CCM identities,
self-adjointness, and the Phase 72-74 chain remain intact.

## Normalizations

For a normalized ground eigenline `xi_L` of `H_L` with eigenvalue `mu_L`,

```text
D_L(z)=prod_{n in I_L}(z-d_n),
P_L(z)=sum_n xi_L(n) prod_{m != n}(z-d_m),
C_L(z)=P_L(z)/D_L(z)=sum_n xi_L(n)/(z-d_n).
```

The two-row Cauchy detector is

```text
Q_gamma xi_L=(C_L(gamma), C_L(-gamma))
```

up to the fixed row normalization used in Phase 72/74.  Multiplicities are
handled by Hermite jets:

```text
P_L^(r)(gamma), 0 <= r < m.
```

## Prohibitions

The phase excludes:

```text
no numerical root matching as proof;
no Xi divisor inserted into the construction;
no global Weil positivity;
no termwise absolute prime bounds;
no quotient or ambient projection;
no pseudoinverse closure theorem;
no claim inferred from roundoff.
```

## Acceptance gate

Phase 75 closes Omega7 only if it proves, without numerical premises:

```text
ARITH-LOCK + derivative separation + Schur transfer
```

with all constants and limits explicit.  If that fails, the phase must end
with one of the P75.015 autopsy outcomes A-F, naming the exact finite object
that blocks closure.

