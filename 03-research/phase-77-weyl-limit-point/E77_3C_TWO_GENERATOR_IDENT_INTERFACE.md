# E77.3c - Two-generator IDENT interface

**Run:** 2026-07-18.

## 1. Statement

P76.041 rewrote the safe transfer function using only two generator
solutions:

```text
T_b(z)=F_b(z)/(z-d_b),
F_b(z)=1+a_b(U(z)+U_b)+b_b(V(z)+V_b).
```

E77.3c tests whether the `MOM-RATIO` object from E77.3b is already enough
to close IDENT, or whether IDENT remains the next live arithmetic
insertion.

## 2. Probe

Probe:

```text
E77_3c_two_generator_ident_probe.py
```

Command:

```bash
python3 E77_3c_two_generator_ident_probe.py \
  --lambdas 6,7,8 \
  --max-modes 18 \
  --dps 60
```

Output:

```text
E77_3c_two_generator_ident_results.json
```

The probe measures:

```text
two-generator identity error:
    generated T_b and T_b'/T_b versus direct transfer;

safe zeta-target error:
    L coth(sigma L/2) + 2 Re(i T_b'/T_b) - B_ext
    versus 2 Xi'(1/2+sigma)/Xi(1/2+sigma),
    sigma in {0.6,0.75,1.0,1.5,2.0}.
```

The planted falsifier uses its own planted sine symbol for the exact
two-generator algebra, but is compared against the zeta target.  Therefore
passing the exact identity is not counted as arithmetic success.

## 3. N=18 Table

| case | two-gen id. error | max zeta-target rel. error | |a_b| | |b_b| |
|---|---:|---:|---:|---:|
| zeta L6 | 3.59e-17 | 0.3716 | 2.01e-10 | 1.90e-9 |
| plant L6 | 4.08e-60 | 48.41 | 3.91 | 4.69 |
| zeta L7 | 1.32e-14 | 0.3739 | 2.32e-12 | 2.58e-11 |
| plant L7 | 9.97e-60 | 58.96 | 14.4 | 1.33 |
| zeta L8 | 2.66e-13 | 0.3777 | 6.12e-14 | 6.12e-13 |
| plant L8 | 1.94e-59 | 87.11 | 0.581 | 34.8 |

The full table contains N=8,10,12,14,16,18 for all six cases.

## 4. Reading

The two-generator identity is exact for both zeta and planted builds.  The
identity therefore belongs to the finite algebra layer, not to the
arithmetic discriminator.

The arithmetic discriminator appears at the safe zeta target.  At N=18,
zeta has target-relative error about `0.37` for lambdas 6,7,8.  The planted
build fails by factors `48`, `59`, and `87`.  This is the first place in
the E77.1b-E77.3c chain where the planted falsifier clearly breaks while
the zeta build remains plausibly convergent.

However, zeta is not yet close enough to claim IDENT.  The finite range
shows slow improvement, not convergence proof.  Thus E77.3c is a reduction,
not a closure.

## 5. Reduced Target

E77.3c reduces `MOM-RATIO` and the IDENT interface to:

```text
SR-LOG-ERR:
prove that the two-generator safe log derivative error

    E_{L,N}(sigma)
    = L coth(sigma L/2)
      + 2 Re(i F_b'(i sigma)/F_b(i sigma) - i/(i sigma-d_b))
      - B_ext(sigma)
      - 2 Xi'(1/2+sigma)/Xi(1/2+sigma)

goes to 0 locally uniformly for sigma>1/2, using only the coupled
Gamma-prime/cell formula and absolute prime-power convergence in Re(s)>1.
```

This is exactly IDENT in its current smallest finite form.  The falsifier
does not pass it.

## 6. Next Step

Proceed to E77.5 proper:

```text
E77.5a:
split SR-LOG-ERR into the finite two-generator term plus the
Euler-safe prime-power tail, keeping archimedean and prime pieces coupled
until after F_b'/F_b is formed.

Forbidden:
no hard prime trace alone, no per-prime positivity, no ambient inverse
norm, no zero-location input.
```

If this fails, the autopsy must identify the exact finite error term in
`SR-LOG-ERR` that is not controlled by absolute convergence.

## 7. Status

```text
proved:    exact two-generator transfer identity in the tested sections;
observed:  zeta safe-target error is ~0.37 at N=18;
observed:  planted safe-target error is 48--87 at N=18;
refuted:   two-generator identity alone as arithmetic discriminator;
open:      SR-LOG-ERR -> 0 locally uniformly;
next:      E77.5a Gamma-prime insertion for SR-LOG-ERR.
```
