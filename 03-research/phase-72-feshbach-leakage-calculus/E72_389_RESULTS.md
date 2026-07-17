# E72.389 results - D2BV packet bound

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_389_d2bv_packet_probe.py
```

## Output

```text
E72.389 D2BV packet probe
 lam    L    dim     M      D0        D1        D2        D2BV      scaled4   scaled5
   6  3.584    21    10 1.859e+01 2.220e+01 3.871e+01 7.950e+01 1.916e-02 5.348e-03
   8  4.159    25    12 1.804e+01 4.290e+01 2.150e+02 2.759e+02 2.184e-02 5.253e-03
  10  4.605    29    14 1.165e+01 6.517e+01 5.337e+02 6.105e+02 2.151e-02 4.672e-03
  12  4.970    33    16 2.171e+01 1.026e+02 5.527e+02 6.770e+02 1.267e-02 2.549e-03
  14  5.278    37    18 1.433e+01 1.314e+02 1.406e+03 1.552e+03 1.730e-02 3.277e-03
```

## Interpretation

The tested quantity is

```text
D2BV = int_0^L e^(ct)(|B_z^M|+|(B_z^M)'|+|(B_z^M)''|)dt.
```

The second derivative dominates, as predicted by the proof: differentiating the Dirichlet-Cauchy
packet creates the `D_M'` term, whose Parseval size is `M^(3/2)L^(-1/2)`.

The normalized column

```text
D2BV / (e^((c+sigma)L)L^4)
```

stays between `1.267e-2` and `2.184e-2` in this range.  Thus the computation supports the
analytic theorem with a polynomial loss no worse than `L^4` for this active bandwidth.

## Status

```text
verified numerically: D2BV-K scale for the actual finite packet;
proved analytically: D2BV-K from Volterra + Parseval under polynomial active bandwidth;
feeds: SV-K, hence SFREQ at natural height.
```

