# R161_045 — Brown--Halmos supplies the local square, not the global Gamma--Tate trivialization

## 0. Verdict

The Toeplitz--Hankel identity is exactly the right local mechanism: each degree-one Euler factor has a positive
rank-one self-commutator. However, phase 122 already proves that assembling those local squares on the physical
carrier requires a global metrized Euler--Gamma determinant trivialization. No such trivialization is present in
the corpus.

The phase-161 Poisson identity improves the situation by identifying the two undifferentiated exterior histories
modulo `E_N^ren`. But `R161_041` proves that differentiating this difference gives the orientation mean rather than
the critical jet. Thus the local Brown--Halmos square does not supply the missing global exterior reciprocity.

## 1. Exact local result

For a prime `p`, put `r=p^(-1/2)` and

```
A_r=rS(1-rS)^(-1).                                      (1.1)
```

`P122_013_LOCAL_EULER_DETERMINANT_LINE` proves

```
A_r* A_r-A_r A_r*
 =H_(bar phi_r)*H_(bar phi_r)
 =(1-r^2)^(-1) ell_r*ell_r >=0.                        (1.2)
```

This is an exact rank-one root observation and has the correct orientation under port reversal.

## 2. Why it does not close first contact

The physical first-contact equations supply two histories `h_(p,+)` and `h_(p,-)`, not one vector in both entries
of (1.2). They give a cross-port norm relation, not

```
||A_rh||=||A_r*h||.                                     (2.1)
```

Phase 121 identifies (2.1) as the missing annular transport. Phase 161 proves the finite undifferentiated
transport

```
H_N^+f-epsilon H_N^-f=(I-P)E_N^renf,                  (2.2)
```

but the logarithmic derivative required for (1.2) changes the orientation according to

```
derivative of difference E_N -> K_NFcal+JK_N,
derivative of sum C_N       -> K_NFcal-JK_N.            (2.3)
```

Therefore (2.2) cannot be differentiated into the same-history hypothesis (2.1).

## 3. Global determinant obstruction

`P122_015_EULER_CONTOU_CARRERE_DETERMINANT_BRIDGE` derives the exact local analytic determinant cocycle

```
<1-rz,1-rz^(-1)>_Hdet=1-r^2.                           (3.1)
```

Its grading derivative is the connection (1.1), and its curvature is (1.2). But the same note proves that
multiplying these local lines does not construct:

1. the archimedean quarter-Gamma line;
2. the two Tate boundary factors;
3. a convergent critical-boundary determinant extension;
4. a metric anomaly/trivialization identifying the two physical histories;
5. first-contact flatness.

Asserting any of these is the missing global theorem, not a consequence of Brown--Halmos.

## 4. Relation to the phase-161 mixed Green route

`R161_042` produces the correct exterior first moments, `R161_043` kills the `Xf` Tate term by opposite parity,
and `R161_044` reduces the primitive term to horizontal radicality plus an exterior commutator. The remaining
commutator is exactly the global version of the local Hankel curvature.

To close D one still needs an independent equality-state law trivializing that curvature on the actual
Euler--Gamma carrier. No identity in phases 1--161 or the phase-122 determinant audit supplies it.

## 5. Status

- local Euler Toeplitz--Hankel square: **PROVED**;
- local analytic determinant cocycle and normalization: **PROVED**;
- Poisson identification of undifferentiated physical histories: **PROVED**;
- differentiation into the required critical orientation: **FALSE / WRONG ORIENTATION**;
- global Gamma--Tate determinant anomaly/trivialization: **MISSING**;
- antisymmetric exterior reciprocity: **OPEN / TERMINAL**;
- row D: **OPEN**.
