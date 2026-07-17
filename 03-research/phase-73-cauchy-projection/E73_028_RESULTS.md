# E73.028 results - multiplicity growth, double precision

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_028_confluent_multiplicity_growth_probe.py
```

Reading:

Double precision suggested artificial explosive growth for high multiplicity, especially after
`m>=12`.  E73.029 reruns the same cases at high precision and shows the growth is numerical
ill-conditioning, not mathematical growth of the Hermite operator.

Therefore E73.028 should be read only as a warning:

```text
do not use double precision linear solves for high-order confluent Cauchy blocks.
```
