# E72.190 -- D-ASRP and BSE identification

**Date:** 2026-07-09.
**Role:** identify the diagonal adaptive SRP energy with the earlier block sign energy.

## 0. Question

E72.167 introduced:

```text
BSE=||(1-a_0)K_0^+||_HS^2+||K_0^-||_HS^2
   +||(1-a_1)K_1^+||_HS^2+||K_1^-||_HS^2.
```

E72.188 recommends the diagonal adaptive polynomial target:

```text
D-ASRP-0.03:
Tr(G_0^2)+Tr(G_1^2)<0.9409.
```

This diagnostic checks whether `D-ASRP` is genuinely new energy, or a polynomial/cycle presentation of
`BSE`.

## 1. Output

The comparison gives:

```text
lam D Gsum BSE diff
12  60 0.898098 0.898090 +7.716e-06
16  66 0.793895 0.793782 +1.128e-04
20  72 0.734996 0.734853 +1.423e-04
24  78 0.740588 0.740377 +2.115e-04
28  84 0.636168 0.635941 +2.274e-04
32  90 0.492249 0.492143 +1.066e-04
36  94 0.647731 0.647642 +8.897e-05
```

where:

```text
Gsum=Tr(G_0^2)+Tr(G_1^2).
```

## 2. Reading

`D-ASRP` is effectively `BSE` expressed through explicit adaptive polynomials:

```text
Tr(G_0^2)+Tr(G_1^2) = BSE + tiny approximation error.
```

The mathematical gain of E72.175--E72.188 is therefore not a new energy functional. The gain is:

```text
spectral sign projections K_j^+, K_j^-
```

have been replaced by:

```text
finite polynomial/cycle identities.
```

Thus the final arithmetic theorem can be interpreted as:

```text
prove BSE<0.9409
```

but in the admissible proof language:

```text
prove the adaptive cycle inequality D-ASRP-0.03.
```

## 3. Consequence

The Phase 72 endpoint is now conceptually clean:

```text
BSE is the right energy.
ASRP is the cycle-realization of BSE.
XNEG is a small structural mixed-sign correction.
```

The next proof attempt should attack `BSE` intuition, but write every step in the cycle language of
`D-ASRP-0.03`.
