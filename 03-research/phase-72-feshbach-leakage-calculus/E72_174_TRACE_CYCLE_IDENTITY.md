# E72.174 -- Trace cycle identity for PTC

**Date:** 2026-07-09.
**Role:** express the polynomial trace certificate as a finite prime-power cycle identity.

## 0. Relative cell operators

Let:

```text
S_j(x)={n=p^m<=x : log n in I_j},
I_0=[0,0.60L],
I_1=(0.60L,L],
L=log x.
```

For each prime power `n=p^m`, define:

```text
y_n=log n,
beta_n=Lambda(n)n^{-1/2},
Q_n=Q_x(y_n),
```

and let `W_x` denote the fixed relative whitening/compression used in Phase 72:

```text
A_n := -beta_n W_x Q_n W_x^*.
```

Then the two relative prime blocks are:

```text
K_j = sum_{n in S_j(x)} A_n.
```

## 1. Cycle identity

For every integer `r>=1`:

```text
Tr(K_j^r)
 =
sum_{n_1,...,n_r in S_j(x)}
Tr(A_{n_1}A_{n_2}...A_{n_r}).                  (TCI)
```

This follows by multilinearity of matrix multiplication and trace. No spectral projection, zero, or
positivity input is used.

Therefore, for the certified degree-10 polynomials:

```text
p_j(t)=sum_{r=0}^{10} c_{j,r}t^r,
```

the PTC trace gate is exactly:

```text
Tr p_0(K_0)+Tr p_1(K_1)
= c_{0,0}dim(K_0)+c_{1,0}dim(K_1)
  + sum_{j=0}^1 sum_{r=1}^{10} c_{j,r}
    sum_{n_1,...,n_r in S_j(x)}
    Tr(A_{n_1}...A_{n_r}).                     (PTC-cycle)
```

This is the desired finite explicit identity behind the stable arithmetic certificate.

## 2. Verification

The companion script:

```text
E72_174_trace_cycle_identity_probe.py
```

checks the cycle expansion by brute force for moments `r=2,3` in small windows:

```text
E72.174 trace cycle identity probe
verifies Tr((sum_a A_a)^r)=sum_{a1..ar}Tr(A_a1...A_ar)
lambda=6 block=0 cells=6
  r=2 direct=+1.894811817068e+00 cycle=+1.894811817068e+00 relErr=0.000e+00
  r=3 direct=+7.412135474707e-01 cycle=+7.412135474707e-01 relErr=5.551e-16
lambda=6 block=1 cells=12
  r=2 direct=+7.233123129588e-01 cycle=+7.233123129588e-01 relErr=2.220e-16
  r=3 direct=-1.902974194625e-01 cycle=-1.902974194625e-01 relErr=8.327e-17
lambda=8 block=0 cells=8
  r=2 direct=+1.461278418408e+00 cycle=+1.461278418408e+00 relErr=1.520e-16
  r=3 direct=+2.083292041401e-01 cycle=+2.083292041401e-01 relErr=1.110e-16
lambda=8 block=1 cells=19
  r=2 direct=+5.957447848709e-01 cycle=+5.957447848709e-01 relErr=1.110e-16
  r=3 direct=-3.593871007226e-02 cycle=-3.593871007226e-02 relErr=6.939e-18
```

The identity is algebraic, so the brute-force check is only an implementation audit.

## 3. Current exact reduction

The stable arithmetic gate is now:

```text
Norm:
||K_0||<=0.90, ||K_1||<=0.60.

Cycle-trace:
PTC-cycle <= 0.92.

Cross:
cross_+<=0.04.
```

Together these imply:

```text
F2B-PSD.
```

E72.175/E72.176 supersede the `cross_+` line by polynomializing the signed residual itself. The
cycle-trace identity here remains useful as the trace half of that stronger residual-polynomial gate.
