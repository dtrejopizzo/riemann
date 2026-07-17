# E72.270 -- Pole-even XNEG/mixed probe

**Purpose.** Recheck the mixed-block sign (`XNEG`) in the corrected pole-relative even geometry.

The old mixed probes used the accidental `setup_pair` complement. E72.270 recomputes:

```text
cross = 2 Tr(G_0 G_1)
```

where `G_j` are the signed Chebyshev approximants on the two prime-position blocks, but now using:

```text
C_model = B_even^T(H_model-e_pole I)B_even.
```

## Output

```text
E72.270 pole-even XNEG/mixed probe
Corrected geometry; reports cross=2Tr(G0G1). Negative supports XNEG.
prepared lambda=16
prepared lambda=20
prepared lambda=24
-- cut=0.55
lam op0 op1 D8 D16 D32 Dauto
 16 4.168e-01 5.245e-01 +5.271198e-04 -3.179925e-02 -3.816543e-02 -4.025151e-02
 20 3.564e-01 5.163e-01 +1.271958e-02 -2.090874e-02 -3.058383e-02 -3.379623e-02
 24 3.356e-01 5.144e-01 +2.351813e-02 -1.163373e-02 -2.542255e-02 -2.847195e-02
maxCross D8:+2.351813e-02 D16:-1.163373e-02 D32:-2.542255e-02 Dauto:-2.847195e-02
-- cut=0.60
lam op0 op1 D8 D16 D32 Dauto
 16 4.609e-01 5.310e-01 -2.521960e-02 -5.725244e-02 -6.532145e-02 -6.771291e-02
 20 4.048e-01 5.235e-01 +1.298052e-05 -3.488454e-02 -4.478123e-02 -4.834210e-02
 24 3.736e-01 5.176e-01 +1.253310e-02 -2.199674e-02 -3.489370e-02 -3.832364e-02
maxCross D8:+1.253310e-02 D16:-2.199674e-02 D32:-3.489370e-02 Dauto:-3.832364e-02
-- cut=0.65
lam op0 op1 D8 D16 D32 Dauto
 16 5.016e-01 5.358e-01 -3.847236e-02 -6.784789e-02 -7.873471e-02 -8.253188e-02
 20 4.569e-01 5.250e-01 -3.465615e-02 -6.654136e-02 -7.522908e-02 -7.814083e-02
 24 4.136e-01 5.181e-01 -1.431357e-02 -5.081628e-02 -6.219693e-02 -6.777803e-02
maxCross D8:-1.431357e-02 D16:-5.081628e-02 D32:-6.219693e-02 Dauto:-6.777803e-02
```

## Reading

The mixed sign survives the pole-even correction, but only after the signed approximant is sufficiently
sharp:

* `D8` is too crude for cuts `0.55` and `0.60`;
* `D16`, `D32`, and adaptive degree are negative in all tested corrected windows and cuts;
* the robust cut `0.65` is negative even at `D8`.

Thus the corrected XNEG statement should not be formulated as a degree-8 fact. A proof-facing target is:

```text
XNEG-pole-even-D16:
2 Tr(G_0^{(16)}G_1^{(16)}) <= 0
```

for the corrected pole-even blocks and for cuts in the stable range.

## Status

Positive diagnostic. Together with E72.269, the HOC3/K1/mixed mechanisms all survive the correction of
the model complement geometry. The remaining work is to replace these floating traces with explicit
cycle/trace inequalities in the corrected pole-even setting.
