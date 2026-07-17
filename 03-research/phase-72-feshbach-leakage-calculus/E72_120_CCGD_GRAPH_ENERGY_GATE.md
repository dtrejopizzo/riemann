# E72.120 -- Graph-energy gate for CCGD

**Date:** 2026-07-09.
**Role:** reduce the Cauchy physical-tail condition `C-FIN` to a finite graph-energy bound.

## 0. Setup

Let:

```text
g_{x,s}:=B_xC_E^(-1)B_x^*r_s^even,
r_s^even(n)=s/(s^2-d_n^2),
D=diag(d_n).
```

The Cauchy physical tail is:

```text
CCGD_x(H,s)
 := ||1_{|d|>H}g_{x,s}||^2/||g_{x,s}||^2.
```

Define the normalized graph energy:

```text
Graph_x(s)
 := ||Dg_{x,s}||^2/||g_{x,s}||^2.                         (GE)
```

## 1. Spectral tail inequality

For every `H>0`:

```text
CCGD_x(H,s) <= H^(-2) Graph_x(s).                         (TAIL-GE)
```

### Proof

On the tail `|d_n|>H`,

```text
1 <= d_n^2/H^2.
```

Therefore:

```text
||1_{|d|>H}g||^2
 = sum_{|d_n|>H}|g_n|^2
 <= H^(-2)sum_n d_n^2|g_n|^2
 = H^(-2)||Dg||^2.
```

Divide by `||g||^2`. `QED`

## 2. Graph-energy criterion

### Theorem 72.120

Assume that for every compact Cauchy window `K`:

```text
(CGE)
limsup_{x->infty} sup_{s in K} Graph_x(s) < infinity.
```

Then:

```text
(C-FIN)
lim_{H->infty}limsup_{x->infty}sup_{s in K}CCGD_x(H,s)=0.
```

### Proof

By `(TAIL-GE)`:

```text
limsup_x sup_{s in K}CCGD_x(H,s)
 <= H^(-2) limsup_x sup_{s in K}Graph_x(s).
```

The right side tends to zero as `H->infty` by `(CGE)`. `QED`

## 3. Finite quadratic form

The graph energy is itself finite:

```text
Graph_x(s)
 = a_x(s)^*C_E^(-1)B_x^*D^2B_xC_E^(-1)a_x(s)
   / a_x(s)^*C_E^(-2)a_x(s),                              (GE-QR)
```

where:

```text
a_x(s)=B_x^*r_s^even.
```

Thus `C-FIN` is reduced to the finite rational inequality:

```text
sup_{s in K} Graph_x(s)=O_K(1).                            (CGE-QR)
```

## 4. Diagnostic

The companion script:

```text
E72_120_graph_energy_probe.py
```

prints `Graph_x(s)` and checks the inequality by reporting:

```text
H^2 CCGD_x(H,s)/Graph_x(s) <= 1.
```

Representative lines:

```text
E72.120 CCGD graph-energy probe
 lam   N      s   GraphE    Hcut   tail     H2tail/GraphE
  12  28    5.0 2.82e+01      8 5.53e-03      1.257e-02
  12  28   10.0 1.02e+02     12 1.02e-02      1.437e-02
  12  28   15.0 2.29e+02     18 7.46e-03      1.054e-02
  24  48    5.0 3.79e+01      8 1.00e-02      1.698e-02
  24  48   10.0 1.01e+02     18 3.30e-03      1.054e-02
  24  48   15.0 2.22e+02     24 2.47e-03      6.416e-03
```

The graph energy tracks the physical height of the Cauchy parameter and remains bounded in the tested
fixed `s` windows.

## 5. Updated final checklist

The `C-FIN` component of E72.119 can be replaced by:

```text
CGE:
Graph_x(s)=O_K(1).
```

Then:

```text
CGE + N-FIN + S-FIN
```

implies scalar WRL resonance annihilation.

## 6. Status

```text
proved: CGE implies C-FIN;
proved: CGE is a finite quadratic rational inequality;
observed: Graph_x(s) is bounded in tested fixed windows;
open:   prove CGE uniformly in x on compact Cauchy windows.
```
