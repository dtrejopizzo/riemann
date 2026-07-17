# E73.048 results - arithmetic DNS proxy

## 1. Purpose

E73.046 showed that selecting dominant nodes only by geometry and mesh fails.  E73.048 tests
structural arithmetic selectors built from the finite Cauchy divisor of

```text
C_x=P_x/D_x.
```

The selectors do not use the final values `|C_x(i gamma)|`.

## 2. Tested proxies

For each critical height `gamma`, let

```text
distRoot(gamma)=dist(-gamma, Div(P_x)),
sepPole(gamma)=dist(-gamma, Div(D_x)).
```

The tested scores multiply the geometric-mesh weight by one of:

```text
near          = 1/distRoot;
far           = distRoot;
slope         = distRoot/sepPole;
divisor_small = distRoot/(sepPole+distRoot);
divisor_large = (sepPole+distRoot)/distRoot.
```

The strongest and most stable proxy is:

```text
far = distRoot.
```

## 3. Representative output

```text
E73.048 arithmetic DNS proxy probe
Selectors use finite divisor/pole geometry but not C_x(gamma) values.
 lam     L sigma     tau  m   WCS  geom3 near3 far3 slope3 small3 large3 post3 best bestCap
   8   4.159  0.20   21.02  3 4.78e-06  0.70  0.70  1.00   1.00   1.00   0.70  1.00          far    1.00
  10   4.605  0.20   14.13  3 1.20e-05  0.45  0.45  1.00   0.45   0.45   0.45  1.00          far    1.00
  16   5.545  0.20   21.02  3 2.86e-05  0.69  0.69  1.00   1.00   1.00   0.69  1.00          far    1.00
  18   5.781  0.20   14.13  3 9.02e-06  0.28  0.07  1.00   0.28   0.28   0.20  1.00          far    1.00
  24   6.356  0.20   14.13  3 1.59e-05  0.02  0.00  1.00   1.00   1.00   0.00  1.00          far    1.00
```

The `far` selector fixes the severe E73.046 failure:

```text
geometry-only top3 at L=6.356 captured about 0.02;
far-divisor top3 captures about 1.00.
```

## 4. Diagnosis

The dangerous WCS nodes are those where the critical height is far from the finite Cauchy numerator
divisor.  This matches the exact identity

```text
C_x(t)=P_x(t)/D_x(t).
```

Near a root of `P_x`, the Cauchy defect is suppressed.  Far from the numerator divisor, there is no
root cancellation, so the WCS term can dominate.

## 5. Status

```text
rejected: geometry-only DNS;
supported: FAR-DNS, using distance from critical heights to Div(P_x);
next: formulate FAR-DNS as the finite non-tautological selector theorem.
```
