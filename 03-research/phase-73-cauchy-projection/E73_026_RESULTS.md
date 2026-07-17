# E73.026 results - confluent Pi probe

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_026_confluent_pi_probe.py
```

Output summary:

```text
Separated-node Lebesgue rows blow up like inverse powers of the cluster spacing.
Hermite/confluent coordinates remain independent of the artificial spacing.
```

Representative values:

```text
L=20, m=3:
sepScale=0.0   separated=1.138e4   confluent=8.207e3
sepScale=0.5   separated=5.655e12  confluent=8.207e3
sepScale=1.0   separated=2.702e27  confluent=8.207e3
sepScale=1.5   separated=3.407e44  confluent=8.207e3

L=20, m=4:
sepScale=0.0   separated=5.784e4   confluent=3.322e4
sepScale=1.5   separated=1.165e73  confluent=3.322e4
```

Conclusion:

```text
CONFL-PI passes the cluster falsifier.
```

The enormous `Pi` growth in E73.025 is a separated-node coordinate singularity.  In Hermite
coordinates the local projection operator stays finite as the off-line nodes coalesce.

This does not yet prove natural-height `NAT-PROJ`, because the final norm must be expressed in the
same Hermite coordinates used by the nodal system.  It does prove that cluster blow-up alone is not a
fundamental obstruction.
