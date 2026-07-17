# E73.207 results - high-precision bordered eigen audit

Command:

```text
python3 E73_207_hp_bordered_eigen_probe.py
```

Output:

```text
E73.207 high-precision bordered eigen audit
Uses closed mp matrix entries and mp.eigsy.
 lam     L    N  dim    muB    gapB     resB    stepB
   8   4.159    6   13  -25.00  -25.82  -164.30  -140.78
  10   4.605    8   17  -22.76  -23.67  -152.56  -131.24
  12   4.970   10   21  -21.27  -22.24  -146.19  -125.40
```


Reading:

```text
The high-precision closed-entry matrix removes the double-residual obstruction.
The bordered residual is now more than 100 powers of L below the gap, and the
bordered correction step is correspondingly tiny.  This is the positive
counterpart to E73.205: the eigenline can plausibly be certified by a Krawczyk
argument once the same closed entries are given outward-rounded intervals.

Thus the active bottleneck is no longer eigenline conditioning in principle;
it is implementing rigorous ball/interval enclosures for the closed matrix
entries and the bordered Krawczyk map.
```
