# E73.223 results - packet coefficient ball budget

Command:

```text
python3 E73_223_coefficient_ball_budget.py
```

Output:

```text
E73.223 packet coefficient ball budget
For c_omega=u_omega eta and l_omega=v_omega eta, radius is ||u|| rho_eta.
 lam     L    N Csec gamma row kind modes maxCoeffB maxRadB sumCoeffB sumRadB maxRatio worstOmega
   8   4.159    6    1   14.13   0    c    13     -2.69   -56.74     -1.44   -55.23  2.0e-32     0.000
   8   4.159    6    1   14.13   0    l    13     -4.10   -57.79     -2.73   -56.26  2.0e-32     0.000
   8   4.159    6  1e6   14.13   0    c    13     -2.69   -47.05     -1.44   -45.54  1.9e-26     0.000
   8   4.159    6  1e6   14.13   0    l    13     -4.10   -48.10     -2.73   -46.57  1.9e-26     0.000
  10   4.605    8    1   14.13   0    c    17     -1.52   -52.88     -0.42   -51.46  3.5e-33   -10.915
  10   4.605    8    1   14.13   0    l    17     -2.52   -53.92     -1.46   -52.50  3.3e-33   -10.915
  10   4.605    8  1e6   14.13   0    c    17     -1.52   -43.83     -0.42   -42.41  3.5e-27   -10.915
  10   4.605    8  1e6   14.13   0    l    17     -2.52   -44.87     -1.46   -43.45  3.3e-27   -10.915
  12   4.970   10    1   14.13   0    c    21     -1.83   -50.10     -0.70   -48.88  7.7e-32     0.000
  12   4.970   10    1   14.13   0    l    21     -3.14   -51.12     -1.96   -49.92  7.7e-32     0.000
  12   4.970   10  1e6   14.13   0    c    21     -1.83   -41.49     -0.70   -40.27  7.6e-26     0.000
  12   4.970   10  1e6   14.13   0    l    21     -3.14   -42.51     -1.96   -41.31  7.6e-26     0.000
```

Only representative rows are shown here; the command checks both rows and both
Cauchy heights for all listed windows.  The full output was written during the
run and shows the same pattern throughout.

Interpretation:

Coefficient uncertainty is inherited linearly from the Krawczyk/Cauchy vector
radius and remains far below the coefficient centers.  The center interval
problem now moves to the weight side.
