# E109 — finite-prime colligation: the scalar route fails at ω=0 (matrix colligation is essential)

**Date:** 2026-06-28 · mpmath dps=25 · Connes §7.2 (finite-prime + normal-convergence criterion).

## The criterion (Connes, Montel)

If the finite-prime approximants `Θ_{≤P,ω}` are Schur (passive) **and** converge locally uniformly on
`ℂ_+` to `Θ_ω`, the limit is Schur, hence at `ω=0` RH. We test the two regimes for the **scalar**
truncation `Θ_{≤P,ω}=Θ_∞·∏_{p≤P}Θ_p`.

## Result

**(1) Safe region `ω=1.0`, points in the convergence strip (`Im z<0.5`):**

| P | `max|trunc−full|` | Pick min eig |
|---|---|---|
| 20 | 3.0e-2 | +2.7e-2 (PSD) |
| 500 | 4.7e-3 | +2.4e-2 (PSD) |
| 2000 | 2.7e-3 | +2.2e-2 (PSD) |

The truncation **converges** and is **Pick-PSD** throughout. The safe-region colligation works as
expected.

**(2) Critical region `ω=0`, points near zero ordinates:**

| P | `max|trunc−full|` | Pick min eig |
|---|---|---|
| 20 | 1.21 | +0.11 |
| 500 | 1.00 | +0.11 |
| 2000 | 1.00 | +0.11 |
| 8000 | **9.8e8** | **−1.5e17** |

The scalar truncation **does not converge** (error stalls at ~1.0) and then **diverges
catastrophically** (P=8000). This is the Euler product `∏(1−p^{−s})^{−1}` diverging at `Re s=½`
(Connes audit 0.2: the Euler product is a boundary/strip object, and `ω=0` is deep outside it).

## Reading — the scalar finite-prime route is a non-starter at ω=0

The Montel criterion's hypothesis (`Θ_{≤P,0}` converges) **fails for the scalar product**: at the
critical value the Euler product does not converge, so `Θ_{≤P,0}` is not even an approximation of
`Θ_0`. This confirms Connes precisely:
- "naive Euler products will not give it in the critical half-plane";
- the Euler product must enter through the **global adelic restricted-tensor *matrix* Gram
  construction**, **not** scalar local factors or their scalar product.

So the genuine finite-prime object must be the **`J`-unitary matrix colligation** `T_{≤P,ω}` assembled
on the adelic Hilbert space, with a **renormalized** critical limit (the Critical Gram Realization).
The scalar product cannot be that object — it diverges at `ω=0`. This is an honest negative result
that correctly localizes the difficulty: the convergence/passivity must be proved at the
**matrix/Hilbert** level with renormalization, exactly the open `THEOREM-adelic-colligation.md` step.

## Status

- Safe region (`ω>½`, in strip): scalar truncation converges and is passive. ✓
- Critical (`ω=0`): scalar truncation **diverges** — the scalar finite-prime criterion is void. The
  matrix colligation + renormalization is essential (open).

## Reproduce
```
venv/bin/python E109_finite_prime_colligation.py
```
