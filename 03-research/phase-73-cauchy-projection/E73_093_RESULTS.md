# E73.093 results - tail LC budget

## 1. Purpose

E73.092 leaves `TAIL-NODAL-5` as part of the global finite gate.
E72.391--E72.392 already prove that the finite Fourier tail is an explicit nodal operator with
coefficient scale:

```text
e^(sigma L)L^2/M^2.
```

E73.093 checks that the local nodal sum controlled by `LOCK-COMP-BUD` also controls the tail nodal
sum.

## 2. Tail local nodal sum

The tail uses:

```text
G_x(w)=(1-e^(wL))H_0(w)
```

and its local absolute nodal sum is:

```text
Gsum_loc(A,L)
:=
sum_{w in Z_loc(A,L)/+-}
|w| |1-e^(wL)| |H_0(w)|.
```

Since `|1-e^(wL)|<=2` on the critical line:

```text
Gsum_loc(A,L)
<= 2 Wloc(A,L) sum_{w in Z_loc/+-}|H_0(w)|,
```

where:

```text
Wloc(A,L):=max_{w in Z_loc(A,L)} |w|.
```

Thus `Gsum_loc` is bounded by the same `N_LC(A,L)` from E73.091:

```text
Gsum_loc(A,L) <= 2 Wloc(A,L) N_LC(A,L).
```

## 3. Output

```text
E73.093 tail LC budget probe
Compares local G-node tail budget with LOCK/COMP nodal budget.
Tail scale shown with unit kernel constant: e^(sigma L)L^2/M^2.
 lam     L tau    M    SFARB    GsumB     NLCB tailSuffB lcTailB ratio
  16   5.545   14.13   20    4.629  -12.023  -13.876    -8.245   -8.219   0.956
  16   5.545   21.02   20    4.581  -12.023  -13.876    -8.292   -8.266   0.956
  18   5.781   14.13   22    4.823  -12.686  -13.869    -8.728   -8.076   0.319
  18   5.781   21.02   22    4.816  -12.686  -13.869    -8.735   -8.083   0.319
  20   5.991   14.13   24    4.618  -16.186  -17.026   -12.449  -11.491   0.180
  20   5.991   21.02   24    4.582  -16.186  -17.026   -12.485  -11.527   0.180
  24   6.356   14.13   28    4.491  -15.779  -16.974   -12.204  -11.659   0.365
  24   6.356   21.02   28    4.378  -15.779  -16.974   -12.317  -11.771   0.365
```

## 4. Interpretation

With unit tail-kernel constant, the tested local tail budget lies between:

```text
L^-8.2 and L^-12.4.
```

This is below the `L^-5` target.  The column `lcTailB` confirms that the direct `Gsum` is bounded by
the `N_LC` budget after the expected factor `Wloc`.

## 5. Consequence

The local part of `TAIL-NODAL-5` follows from the same finite gate as LOCAL-HWIN:

```text
TAIL-LC-BUD:
C_K e^(sigma L)L^2/M^2 S_FAR(A,L) Wloc(A,L) N_LC(A,L)
<= C_tail L^-5.
```

The remaining tail work is only outside-window bookkeeping, already separated in E72.394 and
E73.092.

## 6. Status

```text
proved: local G-nodal tail sum is controlled by Wloc*N_LC;
verified: active-cutoff tail budget has slack in the finite harness;
open: uniform constants and outside-window tail contribution.
```
