# E73.206 results - high-precision matrix entries

Command:

```text
python3 E73_206_hp_matrix_entry_probe.py
```

Output:

```text
E73.206 high-precision closed matrix entries
Compares closed mp entries to the legacy quadrature matrix.
 lam     L    N  dim include   maxEntryB   diffB   relDiff
   8   4.159    6   13   False       1.48  -23.75  2.43e-16
   8   4.159    6   13    True      -2.12  -23.58  5.22e-14
  10   4.605    8   17   False       1.53  -21.79  3.42e-16
  10   4.605    8   17    True      -1.53  -21.64  4.65e-14
  12   4.970   10   21   False       1.57  -20.61  3.55e-16
  12   4.970   10   21    True      -1.29  -20.23  6.39e-14
```


Reading:

```text
The closed finite-frequency/digamma entry engine matches the legacy quadrature
matrix at the expected double floor.  This validates the entry-mode
normalization and gives the center engine needed for the bordered Krawczyk
route.

The arithmetic matrix (`include=True`) has slightly larger relative discrepancy
because the legacy prime side is double-evaluated and the entries themselves
are smaller, but the agreement is still at the same absolute floor.
```
