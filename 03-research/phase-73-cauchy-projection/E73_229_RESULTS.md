# E73.229 results - sector constant probe

Command:

```text
python3 E73_229_sector_constant_probe.py
```

Output:

```text
E73.229 sector constant probe
Computes S=max |z|/Re z for z=80+1/4-i omega/2 and C=S^(2K+1).
 lam     L    N  dim   S        C_K16       log10C
   8   4.159    6   13 1.001594     1.053952   0.022821
  10   4.605    8   17 1.002310     1.079107   0.033065
  12   4.970   10   21 1.003098     1.107454   0.044326
```

Interpretation:

The sector constant actually required by Lemma 229.1 in the tested windows is
about `1.11` at `K=16`.  The audits using `C_sec=10^6` are therefore vastly
more conservative than the formal sector proof requires.
