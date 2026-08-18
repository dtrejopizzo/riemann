# E77.5h - Schur Factor Regularizer Autopsy

## Objective

E77.5g reduced `SHELL-REG` to

```text
THETA-REG:
  theta_N(i sigma)=tau_N(i sigma) Sigma_N^{-1}kappa_N/t0_N(i sigma)
  is Cauchy with a summable envelope on sigma-compacts.
```

E77.5h tests the simplest possible proof strategy: control the factors of
`theta_N` separately.

Write

```text
v_N = Sigma_N^{-1} kappa_N,
c_N = 1/t0_N,
theta_N = tau_N v_N c_N.
```

For `M=N+2`, the exact telescoping identity is

```text
theta_N-theta_M
=(tau_N-tau_M)v_N c_N
 +tau_M(v_N-v_M)c_N
 +tau_M v_M(c_N-c_M).
```

If factorwise regularity were the right route, each term on the right would
be comparable to `theta_N-theta_M`, or at least separately small.

## Probe

Artifacts:

```text
E77_5h_schur_factor_regularizer_probe.py
E77_5h_schur_factor_regularizer_results.json
E77_5h_smoke_results.json
```

Main command:

```bash
python3 E77_5h_schur_factor_regularizer_probe.py --lambda 6 --max-modes 22 --dps 100 --output E77_5h_schur_factor_regularizer_results.json
```

Falsifier:

```text
gamma=14.134725141734693790, beta=0.30, strength=5.0
```

The probe uses only the finite Schur objects already certified in E77.5f.
No pseudoinverse, ambient inverse norm, zero-location input, or positivity
principle appears.

## Certification Table

Max over `sigma in {0.55,0.6,0.75,1,1.5,2,3}`.

| build | step | max abs Delta theta | tau-part | v-part | c-part | max part / Delta |
|---|---:|---:|---:|---:|---:|---:|
| zeta | 8 -> 10 | 0.068445728 | 63.309535 | 58.738369 | 4.5027428 | 924.96 |
| zeta | 10 -> 12 | 0.053619596 | 50.462139 | 8590.6906 | 8540.1749 | 160215.5 |
| zeta | 12 -> 14 | 0.023515542 | 78.766112 | 79.920552 | 1.1779646 | 3398.63 |
| zeta | 14 -> 16 | 0.022835206 | 44.639520 | 30.793944 | 13.822742 | 1954.86 |
| zeta | 16 -> 18 | 0.017264103 | 107.72357 | 278.96859 | 171.22776 | 16158.88 |
| zeta | 18 -> 20 | 0.015438585 | 74.676457 | 92.090406 | 17.398511 | 5964.95 |
| zeta | 20 -> 22 | 0.0067492443 | 14.871492 | 97.710681 | 82.832441 | 14477.28 |
| planted | 8 -> 10 | 2.8023251 | 2.7728739 | 2.1179988 | 3.6041042 | 1.286 |
| planted | 10 -> 12 | 1.8421061 | 11.053542 | 14.208246 | 23.723546 | 12.878 |
| planted | 12 -> 14 | 3.6679515 | 7.4223641 | 6.7734608 | 10.532662 | 2.872 |
| planted | 14 -> 16 | 7.2624973 | 1.1486496 | 6.2342360 | 0.10227615 | 0.858 |
| planted | 16 -> 18 | 1.8386094 | 0.93598803 | 0.72349188 | 0.17944218 | 0.509 |
| planted | 18 -> 20 | 1.9241482 | 0.41995125 | 0.84977037 | 0.65581233 | 0.442 |
| planted | 20 -> 22 | 1.9757430 | 1.7662958 | 0.15280255 | 0.056970206 | 0.894 |

Telescoping errors:

```text
zeta:    <= 1.82e-97
planted: <= 1.88e-100
```

## Autopsy

The factorwise strategy fails.  In the zeta build, `Delta theta` is small
only after a large signed cancellation among the three telescoping pieces.
The worst observed cancellation index is

```text
max part / |Delta theta| = 1.60e5       (zeta, 10 -> 12).
```

This rules out a proof that first bounds

```text
|Delta tau|, |Delta v|, |Delta c|
```

separately and then adds the estimates absolutely.  That would reproduce
the forbidden ambient-norm pattern in miniature: it would destroy the
signed structure before the selected Cauchy response is assembled.

The planted build behaves differently.  Its `Delta theta` remains O(1), and
the factor pieces are generally comparable to the final delta rather than
canceling down by many orders.  Thus the zeta property is not simple
factor-smallness; it is a special three-term cancellation law.

## Reduced Target

`THETA-REG` is reduced to the smaller finite object:

```text
SCHUR-COCYCLE:
  the signed three-term cocycle

    (Delta tau) v_N c_N
    + tau_M (Delta v) c_N
    + tau_M v_M (Delta c)

  has a summable envelope on sigma-compacts.
```

The proof must keep these three terms coupled until after cancellation.
Any route that estimates them separately is now autopsied.

## Status

```text
proved:    exact telescoping identity for Delta theta to roundoff;
refuted:   separate factor-regularity as a viable proof route;
observed:  zeta has huge internal cancellation and small Delta theta;
observed:  planted has O(1) Delta theta and lacks the same cancellation
           anatomy;
reduced:   THETA-REG -> SCHUR-COCYCLE;
next:      E77.5i should derive the three-term cocycle symbolically from
           the shell Loewner/cell identity and look for the signed
           cancellation source.
```
