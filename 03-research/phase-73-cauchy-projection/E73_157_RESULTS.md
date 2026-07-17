# E73.157 Results - Endpoint equivalence after RCE

Date: 2026-07-12.

Verification command:

```text
python3 03-research/phase-73-cauchy-projection/E73_003_critical_source_probe.py
```

Purpose:

Re-check the finite identity used in E73.157:

```text
C_OO^(-1)C_OKG_K
=
<xi_L,S_b>
=
sum_m xi_L(m)
   sum_{k=i gamma in K_L} Pi(b,k)DD_L(-gamma,d_m).
```

## Output

```text
E73.003 critical source probe
 lam     L    nO nK    |rat|       |src|       absErr     expWeighted
   8   4.159    3  5  4.004e-09  4.004e-09  1.382e-16    9.194e-09
  10   4.605    3  5  3.724e-09  3.724e-09  9.700e-17    9.349e-09
  12   4.970    3  5  4.735e-11  4.735e-11  2.133e-16    1.276e-10
  14   5.278    3  5  2.480e-09  2.480e-09  1.763e-15    7.123e-09
```

Here:

```text
rat = rational Cauchy projection C_OO^(-1)C_OKG_K,
src = finite divided-difference source <xi,S_b>.
```

The equality holds to numerical roundoff.

## Consequence

The endpoint after E73.153--E73.156 is not a new residual gate.  It is the
same explicit finite source identity:

```text
NAT-SRC / CC-PROJ.
```

The numerical check verifies equivalence of the two finite forms.  It does
not prove the required uniform natural-height bound.

## Active theorem

The current theorem to prove is:

```text
Strong-CC-PROJ:
max_{b in O_L} e^(Re b L)
 |sum_m xi_L(m)
    sum_{k=i gamma in K_L} Pi(b,k)DD_L(-gamma,d_m)|
<= L^B
```

with the exponent bookkeeping needed to feed the Phase 73 `CSV_17`/Ω7
route.
