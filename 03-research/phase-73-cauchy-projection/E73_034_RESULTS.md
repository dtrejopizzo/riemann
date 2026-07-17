# E73.034 results - finite root alignment

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_034_finite_root_alignment_probe.py
```

Reading:

The smallness of `g_cancelled(i gamma)` sometimes coincides with a nearby finite Cauchy root:

```text
lam=16:
gamma_1 distance 1.8e-15, |g|=2.9e-15
gamma_2 distance 3.2e-14, |g|=8.1e-15

lam=24:
gamma_2 distance 0, |g|=1.3e-16
gamma_3 distance 0, |g|=2.3e-16
```

but not always.  Some small values occur without a nearby detected finite root in the current
finite section.

Conclusion:

```text
finite-root alignment is one source of CRIT-DIV, but not the whole mechanism.
```

This motivates the factor split in E73.035.
