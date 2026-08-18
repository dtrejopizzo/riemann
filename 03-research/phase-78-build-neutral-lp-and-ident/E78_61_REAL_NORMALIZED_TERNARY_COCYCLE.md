# E78.61 - The real denominator core is still a genuinely ternary normalized cocycle

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.60 proved that the denominator core factors through the normalized ternary
cocycle

```text
w_N = -(A_N+B_N+C_N)/(1-theta_N).                         (RNT-1)
```

But the scalar that actually enters the E78.50 fixed point is

```text
Re(w_N),                                                  (RNT-2)
```

since the exact denominator core is

```text
2 Re(w_N) + |w_N|^2 < 0.                                  (RNT-3)
```

So the candid next question is whether passing from the full complex cocycle to
its real part removes the ternary obstruction.

## 2. Exact real-part reduction

From E78.60 we have

```text
w_N = A_N^* + B_N^* + C_N^*,
```

with

```text
A_N^* := -A_N/(1-theta_N),
B_N^* := -B_N/(1-theta_N),
C_N^* := -C_N/(1-theta_N).                               (RNT-4)
```

Taking real parts gives the exact scalar decomposition

```text
Re(w_N)
 = Re(A_N^*) + Re(B_N^*) + Re(C_N^*).                    (RNT-5)
```

Thus the live denominator sign is already a **real normalized ternary cocycle**.

## 3. Audit on the common certified ladder

The common certified ladder from E78.60 was reused:

```text
sigma in {1.0, 3.0},   N in {8,10,12,14,16,18,20}.       (RNT-6)
```

using

```text
E77_5i_schur_cocycle_cell_results.json
E77_5ac_theta_logderiv_coupling_{zeta,plant}.json.       (RNT-7)
```

The reconstruction

```text
A_N^* + B_N^* + C_N^* = w_N                               (RNT-8)
```

holds to roundoff:

```text
zeta:   max reconstruction error = 1.58e-12,
plant:  max reconstruction error = 4.45e-16.             (RNT-9)
```

### Zeta

Representative rows:

```text
N= 8, sigma=1.0:
  Re(w_N)   = 1.9766245e-1
  Re(A_N^*) = 1.8358731e2
  Re(B_N^*) = -1.7030785e2
  Re(C_N^*) = -1.3081805e1
  max real part / |Re(w_N)| = 9.288e2
  best real pair / |Re(w_N)| = 6.718e1

N=10, sigma=1.0:
  Re(w_N)   = 1.9410103e-1
  Re(A_N^*) = -1.8288817e2
  Re(B_N^*) = 3.1139166e4
  Re(C_N^*) = -3.0956083e4
  max real part / |Re(w_N)| = 1.604e5
  best real pair / |Re(w_N)| = 9.432e2.                 (RNT-10)
```

Across the audited zeta ladder:

```text
median max real part / |Re(w_N)| = 5.992e3
max                               = 1.629e5

min best real pair / |Re(w_N)|    = 4.910e1
median                            = 9.498e2
max                               = 6.338e3.             (RNT-11)
```

So taking real parts does **not** collapse the ternary burden on zeta. Even the
best real pair remains far larger than the final scalar `Re(w_N)`.

### Planted build

Representative rows:

```text
N= 8, sigma=1.0:
  Re(w_N) = -1.2668001
  max real part / |Re(w_N)| = 1.281
  best real pair / |Re(w_N)| = 2.805e-1

N=10, sigma=1.0:
  Re(w_N) = -3.2805007e-1
  max real part / |Re(w_N)| = 1.447e1
  best real pair / |Re(w_N)| = 5.791.                  (RNT-12)
```

Across the audited planted ladder:

```text
median max real part / |Re(w_N)| = 8.939e-1
max                               = 1.611e1

median best real pair / |Re(w_N)| = 4.911e-1
max                                = 6.476.             (RNT-13)
```

Again the plant does not reproduce the giant zeta-style ternary cancellation
profile.

## 4. Consequence

This is an candid autopsy of the hoped-for simplification:

```text
complex normalized ternary cocycle
  --take Re-->
real normalized ternary cocycle
```

does **not** produce a smaller pairwise target on zeta.

The legitimate live object therefore sharpens to

```text
REAL-NORMALIZED-TERNARY-CANCEL:
  prove the sign/cancellation law for
  Re(-(A_N+B_N+C_N)/(1-theta_N)).                        (RNT-14)
```

The denominator front is now localized all the way down to the exact scalar
entering the E78.50 core, and that scalar is still genuinely ternary.

## 5. Candid reading

This note is not a new proof of the denominator core. It is a theorem-grade
localization of the remaining burden.

Passing to the real part does not unlock a hidden one-term or two-term
mechanism. The sign relevant for denominator descent still comes from a large
three-way cancellation inside the normalized cocycle itself.

So the next admissible step is not another projection or polarization. It must
derive a coupled finite cell/Loewner law directly for

```text
Re(-(A_N+B_N+C_N)/(1-theta_N)).                          (RNT-15)
```

## 6. Status

```text
proved:
  the E78.50 denominator scalar Re(w_N) is exactly the real part of the
  normalized ternary cocycle;

observed:
  on the common audited zeta ladder, both the individual real normalized parts
  and the best real normalized pairs remain huge compared with |Re(w_N)|;

autopsied:
  taking real parts does not dissolve the ternary obstruction from E78.60;

reduced:
  further denominator/IDENT progress to REAL-NORMALIZED-TERNARY-CANCEL.
```
