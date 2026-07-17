# E73.079 - History audit for pair divisibility

## 1. Purpose

This audit checks whether the current Phase 73 mechanism has already appeared in the earlier program,
and whether it is one of the routes that was falsified.

The current mechanism is:

```text
Pair_z^infty(w)=M_z^infty(w)+M_z^infty(-w)
=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w),
```

together with finite-tail absorption from E72.391--E72.392.

## 2. Search terms used

The audit searched the repository for:

```text
pair divisibility,
Pair_z,
H_0(w),
H0(w),
factor nodal,
CoeffBudget,
Mellin spectral divisibility,
Cauchy divisor,
divisor ideal,
finite Fourier tail nodal.
```

## 3. What already existed

### E72.320

E72.320 already proved the one-sided factor form:

```text
M_z(w)
= [ ((w+z)+e^(zL)(w-z))G_x(w) - 2wG_x(z) ]
   /(w^2-z^2).
```

Equivalently, in `H_0` notation, the one-sided packet contains:

```text
one term proportional to H_0(w),
one term proportional to H_0(z).
```

This means that the partial-fraction computation itself is not new in Phase 73.

### E72.391--E72.392

The finite Fourier tail was already collapsed to the nodal vector:

```text
Lcal(B_z^tail)
= -2i/L sum_w wG_x(w)R_M(z,w),
```

and was proved to be a lower-order perturbation of the maximal Cauchy block at polynomial active
cutoff.

Thus `TAIL-ABSORB` is not new in Phase 73; it is imported from Phase 72.

### E72.36--E72.37

Raw Mellin divisibility was falsified earlier.  Those falsifiers apply to unpaired or improperly
normalized scalar transforms, not to the endpoint-renormalized paired packet with finite-tail
absorption.

## 4. What is new in E73.075

The new step is the paired cancellation:

```text
Pair_z^infty(w)=M_z(w)+M_z(-w).
```

In the one-sided formula, the obstruction term is proportional to `G_x(z)` or `H_0(z)`.
Under `w -> -w`, that term is odd and cancels exactly.  What remains is:

```text
Pair_z^infty(w)
=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

Therefore the complete-mesh paired packet belongs to the nodal divisor ideal:

```text
(H_0(w),H_0(-w)).
```

This precise ideal membership was not found in the earlier documents.

## 5. Relation to old failures

The current mechanism avoids the earlier no-go cases because:

```text
1. it is paired under the functional equation;
2. it is endpoint-renormalized;
3. it uses the actual transformed packet from E72.319--E72.320;
4. it keeps the finite Fourier tail as a signed nodal operator;
5. it does not estimate the prime or zero sums by absolute values.
```

The remaining open theorem is not the old raw-Mellin divisibility.  It is:

```text
FACTOR-MAIN-5 + TAIL-NODAL-5
```

for the finite nodal divisor values.

## 6. Current status after audit

```text
not new: one-sided factor formula M_z(w)                         [E72.320]
not new: finite-tail nodal absorption                            [E72.391--E72.392]
new: paired cancellation removes the H_0(z) obstruction           [E73.075]
survives old falsifiers: yes, because the raw unpaired target is not being used
remaining: prove the uniform factor nodal budget                  [E73.078]
```

## 7. Instruction for next work

Any further progress must be checked against:

```text
E72.36--E72.37  raw Mellin divisibility falsifiers;
E72.320         one-sided packet factor formula;
E72.391--E72.392 tail absorption;
E72.393         nodal theorem endpoint;
E73.075         paired ideal membership.
```

This prevents redoing a previous route under a new name.
