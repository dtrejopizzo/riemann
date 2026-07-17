# E73.102 results - FAR3 tradeoff

## 1. Purpose

`FAR3-MAIN-RAT` is the limiting gate in E73.100.  Earlier attempts split:

```text
T_k = prefactor_k * |C_x(-gamma_k)|
```

and tried to prove `PREF + CMAIN`.  E73.063 showed that absolute denominator-gap bounds are the
wrong route.

E73.102 tests the finer decomposition:

```text
T_k
= prefactor_k * |C_x(-gamma_k)|
= [prefactor_k * dist(-gamma_k,Div(P_x))]
  * [|C_x(-gamma_k)|/dist(-gamma_k,Div(P_x))].
```

The first bracket is exactly the FAR score used to select `D_3`.

## 2. Representative output

```text
E73.102 FAR3 tradeoff probe
Decomposes each selected main row into prefactor, Cauchy, divisor distance, and quotient.
 lam     L tau  gamma   geomB  meshB  prefB     cB  distB     qB  termB
  16   5.545   14.13  37.59   3.555  0.015   4.217 -10.595   1.639 -12.234  -6.378
  18   5.781   14.13  30.42   3.320 -1.699   2.280  -9.085   1.277 -10.363  -6.805
  20   5.991   14.13  37.59   3.401 -0.024   4.046 -10.618   1.414 -12.032  -6.572
  24   6.356   21.02  37.59   3.339 -1.061   2.966  -8.902   1.369 -10.271  -5.937
  28   6.664   14.13  37.59   3.210 -0.109   3.804  -9.892   1.264 -11.155  -6.087
```

Here:

```text
qB = log_L(|C_x(-gamma)|/dist(-gamma,Div(P_x))).
```

## 3. Diagnosis

The correct factorization is:

```text
T_k = FAR_k * Q_k,
```

where:

```text
FAR_k := prefactor_k dist(-gamma_k,Div(P_x)),
Q_k   := |C_x(-gamma_k)|/dist(-gamma_k,Div(P_x)).
```

In the tested FAR3 rows:

```text
FAR_k can be as large as about L^5.9,
Q_k is about L^-10.3 to L^-16.5.
```

Thus the main budget is not explained by `dist` being small.  These nodes are deliberately far from
finite Cauchy roots.  The smallness comes from the quotient:

```text
|C_x| per unit divisor distance.
```

This is exactly why the FAR selector works: it identifies rows where root-covering does not protect
the term, and then the remaining theorem is a slope/quotient theorem.

## 4. New target

The sharp main theorem should be:

```text
FAR-SLOPE:
sum_{gamma_k in D_3(A,L)}
FAR_k(A,L) Q_k
<= C_main L^-5.
```

A sufficient split is:

```text
FAR_k <= C_F L^6,
Q_k   <= C_Q L^-11.
```

This is weaker and better aligned than:

```text
prefactor <= L^5,
|C_x| <= L^-10.
```

because it allows the measured tradeoff between divisor distance and Cauchy value.

## 5. Status

```text
observed: FAR3 main smallness is a FAR-score times slope-quotient phenomenon;
old split: PREF+CMAIN too rigid;
new target: FAR-SLOPE.
```
