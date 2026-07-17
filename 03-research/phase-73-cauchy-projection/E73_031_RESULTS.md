# E73.031 results - absolute geometry route falsifier

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_031_geom_absolute_route_falsifier.py
```

Output:

```text
E73.031 absolute geometry route falsifier
Fixed off-line node: e^(sigma L) times confluent geometry grows exponentially.
 sigma      t   gamma    m      localNorm       L      weighted
  0.05   14.0    21.0    3    19.80906775     5.0  25.4353464765
  0.05   14.0    21.0    3    19.80906775    10.0  32.6596313581
  0.05   14.0    21.0    3    19.80906775    20.0  53.8466289133
  0.05   14.0    21.0    3    19.80906775    40.0  146.370312899
  0.05   14.0    21.0    3    19.80906775    80.0  1081.53845323
  0.10   14.0    21.0    3    19.81227113     5.0  32.6649128363
  0.10   14.0    21.0    3    19.81227113    10.0  53.8553365987
  0.10   14.0    21.0    3    19.81227113    20.0  146.393982842
  0.10   14.0    21.0    3    19.81227113    40.0  1081.71335176
  0.10   14.0    21.0    3    19.81227113    80.0  59059.5478725
  0.20   14.0    21.0    3    19.82508641     5.0  53.8901721395
  0.20   14.0    21.0    3    19.82508641    10.0  146.488675659
  0.20   14.0    21.0    3    19.82508641    20.0   1082.4130423
  0.20   14.0    21.0    3    19.82508641    40.0  59097.7496816
  0.20   14.0    21.0    3    19.82508641    80.0  176167908.929
```

Conclusion:

```text
CONFL-PI fixes cluster coordinates, but absolute geometry cannot prove NAT-PROJ.
```

For fixed off-line `sigma>0`, the Hermite projection geometry is essentially independent of `L`, so
the weighted quantity still carries the factor `e^(sigma L)`.  Therefore

```text
CRIT-POLY + CONFL-PI-NH
```

is insufficient unless the critical data themselves have exponential cancellation in the projected
directions.

The route must switch to `DATA`.
