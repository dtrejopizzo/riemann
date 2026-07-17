# E72.167 -- Block sign-energy gate

**Date:** 2026-07-09.
**Role:** replace asymptotic `F2B-PSD` by a diagonal sign-energy estimate.

## 0. Definition

For the fixed split:

```text
I_0=[0,0.60L],
I_1=(0.60L,L],
```

write:

```text
K_rel=K_0+K_1,
K_j=K_j^+ + K_j^-.
```

With fixed weights:

```text
a_0=0.70,
a_1=0.60,
```

define the block sign energy:

```text
BSE(x)=||(1-a_0)K_0^+||_HS^2+||K_0^-||_HS^2
      +||(1-a_1)K_1^+||_HS^2+||K_1^-||_HS^2.
```

Equivalently:

```text
BSE(x)=E_0(x)+E_1(x),
E_j(x)=(1-a_j)^2||K_j^+||_HS^2+||K_j^-||_HS^2.
```

## 1. Exact identity and sufficient lemma

The fixed residual is:

```text
R=K_rel-a_0K_0^+-a_1K_1^+
 =(1-a_0)K_0^+ + K_0^- + (1-a_1)K_1^+ + K_1^-.
```

Thus:

```text
||R||_HS^2 = BSE(x)+cross(x),
```

where `cross(x)` is the sum of the Hilbert-Schmidt inner products between distinct signed pieces,
with the factor `2`.

Therefore, if:

```text
BSE(x)+cross_+(x) <= eta^2 < 1,
cross_+(x)=max(0,cross(x)),
```

then:

```text
||K_rel-a_0K_0^+-a_1K_1^+||_HS <= eta < 1.
```

Hence:

```text
{BSE+cross_+ < 1} => F2B-PSD => PSD-DIST.
```

In particular, the diagonal version:

```text
DBSE(x): BSE(x) <= eta^2 < 1 and cross(x) <= 0
```

is sufficient. A fully absolute sufficient condition is:

```text
SBSE(x): sum of the four pairwise absolute positive cross contributions
         <= eta^2 - BSE(x).
```

In the tested asymptotic range the measured cross contribution is not needed for scale; `BSE` itself
is already below `1`.

## 2. Diagnostic output

The companion script:

```text
E72_167_block_energy_probe.py
```

reports:

```text
E72.167 block sign-energy probe
cut=0.60, a=0.70, b=0.60
 lam    L     E0      E1    E0+E1   dist^2  crossE
   6  3.58   0.659   0.545    1.204    0.926  -0.278
   8  4.16   0.641   0.384    1.024    0.935  -0.089
  10  4.61   0.515   0.461    0.975    0.790  -0.186
  12  4.97   0.565   0.333    0.898    0.846  -0.052
  14  5.28   0.511   0.332    0.843    0.783  -0.061
  16  5.55   0.457   0.337    0.794    0.745  -0.049
  18  5.78   0.447   0.213    0.660    0.693   0.034
  20  5.99   0.403   0.332    0.735    0.710  -0.025
  22  6.18   0.381   0.377    0.759    0.739  -0.020
  24  6.36   0.372   0.368    0.740    0.714  -0.026
worst_E0plusE1_after_lambda12=0.898 at lambda=12
```

## 3. New theorem target

The arithmetic gate can be stated as the following two-part theorem:

```text
BSE-eventual:
There exist L_0 and eta<1 such that for all L>=L_0,
BSE(x)<=eta^2.

BSE-finite:
For L<L_0 the finitely many terminal windows satisfy F2B-PSD directly.
```

Then:

```text
BSE-eventual + BSE-finite => F2B-PSD => PSD-DIST.
```

The numerical evidence supports `L_0` near the `lambda=12` window and `eta^2=0.90`.

## 4. Correction to the proof target

The raw lemma `BSE<1 => F2B-PSD` is true only if the cross contribution is non-positive or separately
bounded. The tested rows have small cross terms, with one positive row at `lambda=18`. Therefore the
fully safe sufficient condition is:

```text
BSE(x)+cross_+(x) <= eta^2 < 1,
```

where:

```text
cross_+(x)=max(0, ||R||_HS^2-BSE(x)).
```

The asymptotic theorem to prove is thus:

```text
BSE(x)+cross_+(x) <= 1-epsilon.
```

The point of E72.167 is that `cross_+` is no longer the main object; the main scale is the diagonal
sign energy.
