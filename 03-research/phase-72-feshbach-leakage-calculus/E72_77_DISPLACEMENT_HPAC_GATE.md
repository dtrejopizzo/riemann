# E72.77 -- Displacement HPAC gate

**Date:** 2026-07-08.
**Role:** identify the displacement term as HPAC applied to `h_x=k_x-xi_x`, and prevent a circular
closure by assuming full model/actual convergence.

## 0. HPAC functional for an even vector

For any even vector `a`, define:

```text
HPAC_x(s;tau)[a]
 := alpha(tau){
      i<v_even,S_tau a>
      -(E_tau-1)/L <v_even,S_tau1><r_-(tau),a> }.
```

Then:

```text
HPAC_x(s;tau)[a]=<v,A_x(tau)a>,
```

where `A_x(tau)` is the half-power Abel concomitant of E72.68.

Thus:

```text
HPAC_x(s;tau)[k_x]
 = HPAC_x(s;tau)[xi_x]+HPAC_x(s;tau)[h_x],
h_x=k_x-xi_x.                                                     (LIN)
```

## 1. Finite-root specialization

At a finite root `P_x(tau_j)=0`:

```text
<r_-(tau_j),xi_x>=0.
```

Therefore:

```text
HPAC_x(s;tau_j)[xi_x]
 = alpha_j i<v_even,S_jxi_x>,                                    (CORE)
```

and:

```text
HPAC_x(s;tau_j)[h_x]
 = alpha_j <v_even,
     S_j(ih_x-(E_j-1)L^(-1)<r_j,h_x>1)>.
```

This is exactly the displacement term `DISP-C` of E72.76.

## 2. Non-circularity gate

The tempting proof would be:

```text
h_x=k_x-xi_x -> 0, therefore DISP-C.
```

But `k_x -> xi_x` is essentially the stable-divisor convergence conclusion that Phase 72 is trying to
prove. Therefore this route is circular.

The admissible target is strictly weaker:

```text
HPAC-displacement invisibility:
max_j sup_s |HPAC_x(s;tau_j)[h_x]| -> 0,                         (HDI)
```

proved directly in the shorted even Weyl-Feshbach norm:

```text
HPAC_x(s;tau_j)[h_x]/alpha_j
 = <Q r_s^even,
     C_even^(-1)Q S_j(ih_x-(E_j-1)L^(-1)<r_j,h_x>1)>.
```

This statement does not require full `||h_x|| -> 0`; it asks only that one rank-one-corrected transform
of `h_x` be invisible to the two current-generating Weyl tests after Feshbach shorting.

## 3. Current decomposition of the proof target

HPAC divisibility is now reduced to:

```text
CORE-C: max_j sup_s |HPAC_x(s;tau_j)[xi_x]| -> 0,
HDI:    max_j sup_s |HPAC_x(s;tau_j)[h_x]|  -> 0.
```

`CORE-C` is an actual finite-divisor identity. `HDI` is the remaining displacement gate.

## 4. Diagnostic warning

In the finite windows currently tested, `k_x` and `xi_x` are not close in ambient norm. Consequently
ambient convergence is not the right finite diagnostic. The meaningful quantity is the shorted Weyl
pairing in `(HDI)`, as measured in E72.75--E72.76.

## 5. Status

```text
proved: DISP-C equals HPAC_x[h_x] at finite roots;
proved: closing DISP-C by assuming k_x->xi_x would be circular;
open:   prove HPAC-displacement invisibility directly in the even shorted Weyl-Feshbach norm.
```
