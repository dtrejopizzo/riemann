# E74.19 - Truncation and compression audit

Date: 2026-07-16.

## Test

`E74_019_truncation_compression_probe.py` varies the Fourier cutoff at fixed
`L` and records

```text
reach=d_max/gamma,
spec(G^(-1/2)QHQ*G^(-1/2))/L.
```

It also separates the archimedean and prime-power matrices.

## Result

There is a sharp resolution transition near `reach=1`.  Below it the
compression can be small and the Gram matrix becomes ill-conditioned.  Once
the pole mesh extends beyond the critical height, the Gram condition number
settles near one and the full compression eigenvalues settle near `L`.

The limiting unit coefficient is coupled:

```text
archimedean contribution approximately 0.15L--0.28L,
prime-power contribution approximately 0.70L--0.85L.
```

Neither sector alone gives the observed normalization.  Any proof of
`CAUCHY-COMP` must preserve their signed coupling.

## Consequence

An admissible uniform theorem needs an explicit mesh condition such as

```text
d_max >= (1+delta) max(w)
```

before passing to the Phase 72/73 limit.  Small-window failures cannot be
used to infer a singular asymptotic transfer.

## Status

```text
identified: resolution threshold and stable Gram regime;
identified: coupled archimedean/prime origin of CAUCHY-COMP;
open: analytic error bound beyond the threshold without global Weil positivity.
```

