# E78.63 - The real coupled numerator is still genuinely ternary

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.62 reduced the live denominator/IDENT scalar to the single real numerator

```text
PAIRNUM_N := -Re((A_N+B_N+C_N) conj(1-theta_N)).         (PNT-1)
```

That removed the quotient from the sign problem, but it left open the real
structural question:

```text
does PAIRNUM_N simplify to one term or one pair?         (PNT-2)
```

This note audits that question directly.

## 2. Exact decomposition

Write

```text
d_N := 1-theta_N,                                        (PNT-3)
```

and define the three real paired pieces

```text
P_A := -Re(A_N conj(d_N)),
P_B := -Re(B_N conj(d_N)),
P_C := -Re(C_N conj(d_N)).                               (PNT-4)
```

Then

```text
PAIRNUM_N = P_A + P_B + P_C.                             (PNT-5)
```

So if the numerator sign were actually controlled by one part or one pair, it
would show up already at this real coupled level.

## 3. Audit on the common certified ladder

The same certified common ladder as E78.61-E78.62 was audited:

```text
sigma in {1.0, 3.0},   N in {8,10,12,14,16,18,20}.       (PNT-6)
```

using the same Phase-77 cocycle and theta data.

The reconstruction `(PNT-5)` holds to roundoff:

```text
zeta:   max reconstruction error = 2.87e-13,
plant:  max reconstruction error = 3.02e-14.             (PNT-7)
```

### Zeta

Representative rows:

```text
N= 8, sigma=1.0:
  PAIRNUM_N = 2.3165914e-2
  P_A = 2.1516317e1
  P_B = -1.9959972e1
  P_C = -1.5331792
  max part / |PAIRNUM_N| = 9.288e2
  best pair / |PAIRNUM_N| = 6.718e1

N=10, sigma=1.0:
  PAIRNUM_N = 1.4644270e-2
  P_A = -1.3798297e1
  P_B = 2.3493453e3
  P_C = -2.3355324e3
  max part / |PAIRNUM_N| = 1.604e5
  best pair / |PAIRNUM_N| = 9.432e2.                     (PNT-8)
```

Across the audited zeta ladder:

```text
median max part / |PAIRNUM_N| = 5.992e3
max                            = 1.629e5

min best pair / |PAIRNUM_N|    = 4.910e1
median                         = 9.498e2
max                            = 6.338e3.                (PNT-9)
```

So even after:

```text
normalized cocycle -> real scalar -> coupled numerator,
```

the zeta build still shows enormous three-way cancellation. Neither one part nor
the best real pair is even close to the final numerator scale.

### Planted build

Representative rows:

```text
N= 8, sigma=1.0:
  PAIRNUM_N = -5.8099515
  max part / |PAIRNUM_N| = 1.281
  best pair / |PAIRNUM_N| = 2.805e-1

N=10, sigma=1.0:
  PAIRNUM_N = -7.7657010
  max part / |PAIRNUM_N| = 1.447e1
  best pair / |PAIRNUM_N| = 5.791.                       (PNT-10)
```

Across the audited planted ladder:

```text
median max part / |PAIRNUM_N| = 8.939e-1
max                            = 1.611e1

median best pair / |PAIRNUM_N| = 4.911e-1
max                             = 6.476.                (PNT-11)
```

Again the plant does not reproduce the zeta-style giant ternary profile.

## 4. Consequence

This is another honest autopsy of a hoped-for simplification.

The chain

```text
w_N
-> Re(w_N)
-> PAIRNUM_N
```

does simplify the geometry, but it does **not** simplify the coupling order.

The legitimate live object therefore sharpens one last time to

```text
PAIRNUM-TERNARY-CANCEL:
  prove the sign/cancellation law for
  -Re((A_N+B_N+C_N) conj(1-theta_N))                     (PNT-12)
```

as a genuinely three-term finite object.

## 5. Honest reading

This note is not a new proof. It is the theorem-grade certification that the
remaining denominator/IDENT burden is irreducibly ternary at the level of the
real coupled numerator itself.

So the next admissible step is no longer a scalar reduction. It must be a
structural derivation:

```text
identify PAIRNUM_N as one coupled finite cell/Loewner/Hilbert functional whose
sign is forced without splitting into absolute term bounds or pairwise
cancellation.                                                (PNT-13)
```

## 6. Status

```text
proved:
  PAIRNUM_N = P_A + P_B + P_C exactly at the real coupled level;

observed:
  on the audited zeta ladder, both the individual paired pieces and the best
  paired sums remain huge compared with |PAIRNUM_N|;

autopsied:
  the real coupled numerator from E78.62 is still genuinely ternary;

reduced:
  further denominator/IDENT progress to PAIRNUM-TERNARY-CANCEL.
```
