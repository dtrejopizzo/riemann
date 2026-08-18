# E78.76 - The `safe_u` geometric ratio does not by itself control the radial tail budget

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.28-E78.29 isolated a strong one-dimensional sign-side target:

```text
SAFE-U-GEOMETRIC-ENVELOPE
=> SAFE-U-GEOMETRIC-TAIL                               (STA-1)
```

for

```text
A_N := N Delta safe_u_N.                               (STA-2)
```

After E78.74-E78.75, the live shell front is instead governed by the normalized
radial budget

```text
TAIL_N(sigma_0,sigma) / BASE_N(sigma_0).               (STA-3)
```

This note audits a tempting shortcut:

```text
can the safe_u geometric ratio rho_N = A_{N+2}/A_N
by itself control the radial tail ratio TAIL/BASE?      (STA-4)
```

The answer is no.

## 2. Why the shortcut is tempting

At first sight the two fronts look morally similar:

```text
SAFE-U side:      A_{N+2} <= rho_* A_N
radial side:      TAIL_N / BASE_N small.               (STA-5)
```

If the same one-dimensional contraction parameter explained both, one might try
to transfer E78.28-E78.29 directly into the shell budget.

That would be a very efficient bridge if true.

## 3. Sample-common audit

The available common ladder between the two fronts is

```text
sigma in {1.0, 3.0},
N = 8,10,12,14,16,18.                                  (STA-6)
```

Companion:

```text
E78_76_safeu_tail_autopsy_probe.py
E78_76_safeu_tail_autopsy_results.json
```

The probe compares the normalized radial tail ratio

```text
tau_N(sigma) := TAIL_N(sigma_0,sigma)/BASE_N(sigma_0)  (STA-7)
```

from E78.75 against the safe-u data from E78.28.

## 4. Observed mismatch

On the common zeta rows, the safe-u geometric ratios stay in a very narrow band:

```text
rho_N in [0.80898, 0.91223],                           (STA-8)
```

yet the normalized radial tail varies by more than an order of magnitude:

```text
tau_N(1.0) in [0.00129, 0.00804],
tau_N(3.0) in [0.01599, 0.09616].                      (STA-9)
```

The direct correlation audit gives

```text
corr( rho_N, tau_N )  ≈ -0.319,                        (STA-10)
```

which is weak and of the wrong sign for a clean transfer law.

By contrast, the raw amplitude `A_N` itself shows a strong positive correlation:

```text
corr( A_N, tau_N ) ≈ 0.945.                            (STA-11)
```

Representative rows make the mismatch concrete:

```text
sigma=1.0, N=8:   rho=0.80898, tau=0.00804,  A_N=0.25473
sigma=3.0, N=8:   rho=0.82015, tau=0.09616,  A_N=0.73409

sigma=1.0, N=18:  rho=0.91068, tau=0.00129,  A_N=0.10807
sigma=3.0, N=18:  rho=0.91223, tau=0.01599,  A_N=0.32129. (STA-12)
```

So rows with very similar `rho_N` can carry radically different tail budgets,
depending on the ambient scale.

## 5. Autopsy

This kills the shortcut

```text
SAFE-U-GEOMETRIC-ENVELOPE
=> small TAIL/BASE
```

when the only transferred datum is the contraction ratio `rho_N`. The ratio
controls how the safe-u updates decay along `N`; it does **not** normalize them
against the shell basepoint reserve `BASE_N(sigma_0)`.

In other words:

```text
rho_N is a shape parameter,
TAIL/BASE needs a scale coupling.                      (STA-13)
```

That is the exact missing ingredient.

## 6. Consequence: the next candid object

The correct reduced target is therefore not a ratio-only transfer, but a
coupling statement between the safe-u amplitude and the shell reserve scale.

Name:

```text
SAFEU-BASE-COUPLING:
  control TAIL_N(sigma_0,sigma) / BASE_N(sigma_0)
  through a normalized amplitude law involving A_N and BASE_N. (STA-14)
```

For example, any theorem-grade implication of the form

```text
TAIL_N(sigma_0,sigma)
 <= C(sigma) A_N                                        (STA-15)
```

together with a lower comparison

```text
A_N <= C' BASE_N(sigma_0)                               (STA-16)
```

would feed directly into E78.75:

```text
TAIL/BASE <= C(sigma) C'.                               (STA-17)
```

So the next live target is a **scale-coupled** law, not a ratio-only one.

## 7. Candid reading

This note does not prove the coupling law `(STA-14)`. It proves that we need
one.

That is genuine progress because it prevents a false reduction:

```text
geometric decay of safe_u updates alone is not enough.  (STA-18)
```

The live shell front now points to a strictly sharper object than before.

## 8. Status

```text
refuted:
  the safe_u geometric contraction ratio rho_N, by itself, does not explain or
  control the normalized radial tail ratio TAIL/BASE;

observed:
  on the common zeta ladder corr(rho_N, TAIL/BASE) ≈ -0.319, while
  corr(A_N, TAIL/BASE) ≈ 0.945;

clarified:
  the missing ingredient is a scale coupling between safe_u amplitude and the
  shell basepoint reserve;

reduced:
  the next candid object to SAFEU-BASE-COUPLING.
```
