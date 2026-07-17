# E73.103 - FAR-slope certificate for the main gate

## 1. Purpose

E73.102 shows that the limiting gate `FAR3-MAIN-RAT` should not be attacked by the old split:

```text
prefactor * Cauchy.
```

The correct split is:

```text
T_k = FAR_k * Q_k,
```

where `FAR_k` is the selector score and `Q_k` is a slope quotient.

## 2. Definitions

For a critical row `gamma_k`, define:

```text
W_k(A,L)
:= e^(alpha L)G_theta,m(a,i gamma_k)|1-e^(i gamma_k L)|.
```

Let:

```text
R_k := dist(-gamma_k,Div(P_x)).
```

The FAR selector score is:

```text
FAR_k := W_k(A,L)R_k.
```

Define the Cauchy divisor slope quotient:

```text
Q_k := |C_x(i gamma_k)|/R_k
     = |P_x(-gamma_k)|/(|D_x(-gamma_k)|R_k).
```

Then the WCS term is exactly:

```text
T_k(A,L)=W_k(A,L)|C_x(i gamma_k)|=FAR_k Q_k.          (1)
```

## 3. FAR-SLOPE certificate

Define `FAR-SLOPE(A,L)` by:

```text
sum_{gamma_k in D_3(A,L)} FAR_k Q_k <= C_main L^-5.
```

Equivalently, in finite rational form:

```text
sum_{gamma_k in D_3(A,L)}
W_k(A,L)R_k
|P_x(-gamma_k)|/(|D_x(-gamma_k)|R_k)
<= C_main L^-5.
```

The `R_k` cancels algebraically, but it must remain in the proof structure because `D_3(A,L)` is
selected by `FAR_k`.

## 4. Crude sufficient split

A useful sufficient version is:

```text
FAR-CEIL:
sum_{gamma_k in D_3(A,L)} FAR_k <= C_F L^6,
```

and:

```text
SLOPE-11:
max_{gamma_k in D_3(A,L)} Q_k <= C_Q L^-11.
```

Then:

```text
sum_{D_3} FAR_k Q_k
<= C_F C_Q L^-5.
```

E73.104 shows that this split is too crude in low finite windows: the direct weighted sum passes, but
`sum FAR_k * max Q_k` can fail.  Thus the load-bearing theorem should be the weighted certificate
itself, or a per-node budget, not a global max bound for `Q_k`.

## 5. Theorem

**Theorem 103.1.**  `FAR-SLOPE(A,L)` implies `FAR3-MAIN-RAT(A,L)`.

*Proof.*  Equation (1) gives:

```text
sum_{gamma_k in D_3(A,L)} T_k(A,L)
=
sum_{gamma_k in D_3(A,L)} FAR_k Q_k.
```

The right side is at most `C_main L^-5` by `FAR-SLOPE`.  This is exactly `FAR3-MAIN-RAT`. `□`

**Corollary 103.2.**  `FAR-CEIL + SLOPE-11` implies `FAR3-MAIN-RAT`, but it is not the sharp target.

*Proof.*  This is the estimate in §4. `□`

## 6. Why this avoids the old dead end

The older `CMAIN-10` demanded:

```text
|C_x(i gamma_k)| <= C L^-10
```

uniformly on FAR3 nodes.  E73.102 shows this is not the natural invariant.  The invariant that
stays small is:

```text
Q_k=|C_x(i gamma_k)|/dist(-gamma_k,Div(P_x)).
```

This is a finite derivative/slope statement about the rational Cauchy transform away from its roots,
not a root-covering statement.

## 7. Current endpoint

The final uniform theorem can now be phrased as:

```text
Uniform WEIGHTED-FAR-SLOPE
+ LOCK-COMP-BUD
+ TAIL-LC-BUD
+ OUT-FAR
=> Uniform GATE-73
=> scalar WRL.
```

The remaining hard part is the weighted three-row inequality:

```text
sum_{gamma_k in D_3(A,L)} FAR_k Q_k <= C_main L^-5.
```

The max-slope split is only a fallback if later one can prove stronger constants.
