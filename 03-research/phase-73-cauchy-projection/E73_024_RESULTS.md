# E73.024 results - Pi amplification

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_024_pi_amplification_probe.py
```

Output summary:

```text
tested lam: 8,10,12,14,16,18
tested critical sizes: nK=3,4,5,6
tested off nodes: 0.20 +/- i gamma_1, 0.20 + i gamma_2
```

Observed ranges:

```text
weighted geometric row sum:
e^(Re b L) sum_k |Pi(b,k)| = 1.7e-3 .. 1.7e1

absolute ceiling:
e^(Re b L) sum_k |Pi(b,k)| max_k |g_cancelled(k)|
= 1.7e-14 .. 2.2e-7

signed output:
e^(Re b L)|sum_k Pi(b,k)g_cancelled(k)|
= 4.0e-15 .. 2.1e-8

signed/absolute ratio:
5.1e-3 .. 3.9e-1
```

Reading:

```text
The finite tested CC-PROJ does not require a large hidden cancellation.
```

The absolute ceiling is already polynomially small in the tested windows.  The signed sum improves it
by an additional factor, but the main structural requirement is a weighted Lebesgue bound for the
Cauchy projection kernel `Pi`.

This suggests the split:

```text
CRIT-POLY + PI-LEB => CC-PROJ.
```

`CRIT-POLY` is E72.327.  The remaining geometric theorem is `PI-LEB`.
