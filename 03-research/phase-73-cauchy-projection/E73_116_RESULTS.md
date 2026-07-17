# E73.116 Results - LOCK/TAIL/OUT Box-Domination Pilot

Date: 2026-07-12.

Script:

```text
E73_116_box_domination_pilot.py
```

Purpose:

Test the box-domination theorem of E73.115 on the wide Phase 73 boxes.
This is a pilot, not yet the final interval theorem:

```text
MAIN/SFAR use the E73.112 possible-set box certificate.
NLC/Gloc use sampled tau sup plus finite-difference inflation.
OUT enumerates interval-order compatible FAR triples and sums row upper
bounds outside each compatible triple.
```

The important correction relative to the first attempt is the `OUT`
formula.  Once a compatible FAR triple `S` is fixed, the tail is bounded by

```text
sum_{k notin S} O_k^+(B,L),
```

not by subtracting a weak lower bound for the selected rows from the total.
This avoids an artificial `L^-6` loss.

## Wide boxes

Boxes:

```text
alpha in [0.15,0.25],
tau in [gamma_j-0.50,gamma_j+0.50],
j=1,2.
```

Output:

```text
E73.116 LOCK/TAIL/OUT box-domination pilot
MAIN/SFAR use E73.112 possible-set boxes.
NLC/Gloc use sampled tau sup plus finite-difference inflation.
OUT enumerates interval-order compatible FAR triples and sums row upper bounds outside them.
This is a pilot for E73.115, not the final interval theorem.
 lam     L box                         lockB  tailB    outB mainBox nTri status
  16   5.545 [0.15,0.25]x[13.63,14.63]  -4.519  -6.401 -10.313 2.049e-01    1 FAIL
  16   5.545 [0.15,0.25]x[20.52,21.52]  -4.537  -6.419 -10.915 2.058e-01    1 FAIL
  20   5.991 [0.15,0.25]x[13.63,14.63]  -7.958 -10.290  -6.737 1.411e-01    2 FAIL
  20   5.991 [0.15,0.25]x[20.52,21.52]  -7.971 -10.303  -6.903 1.348e-01    2 FAIL
  24   6.356 [0.15,0.25]x[13.63,14.63]  -8.699 -10.725 -13.590 2.366e-01    1 PASS
  24   6.356 [0.15,0.25]x[20.52,21.52]  -8.782 -10.807 -13.356 2.542e-01    1 PASS
  28   6.664 [0.15,0.25]x[13.63,14.63]  -8.378 -10.108 -13.337 1.912e-01    1 PASS
  28   6.664 [0.15,0.25]x[20.52,21.52]  -8.402 -10.132 -13.083 2.050e-01    1 PASS
```

Interpretation:

```text
lambda >= 24: wide boxes pass all four pilot budgets.
lambda = 20: LOCK/TAIL/MAIN pass, OUT fails only because two FAR triples
             remain interval-compatible on the wide box.
lambda = 16: OUT/TAIL/MAIN pass, LOCK misses by a small low-scale margin.
```

## Subdivision check for lambda=20

For `lambda=20`, `tau ~= gamma_2`, subdividing the tau interval into four
pieces removes the ambiguity:

```text
PARTS 4
tau 21.02 failures 0 worst_lock -7.982 worst_out -14.100 maxtri 1
```

For `lambda=20`, `tau ~= gamma_1`, subdividing tau alone does not remove
the ambiguity.  However subdividing alpha into two pieces already does:

```text
apart 2 tpart 4 boxes 8 failures 0 worst_out -14.025 maxtri 1
apart 2 tpart 8 boxes 16 failures 0 worst_out -14.029 maxtri 1
apart 4 tpart 4 boxes 16 failures 0 worst_out -14.025 maxtri 1
```

Thus the `lambda=20` failure is not structural.  It is a finite box
coarseness issue: the wide box crosses a FAR triple switch, and a finite
alpha subdivision separates it.

## Current mathematical frontier

E73.116 supports the following finite closure strategy:

```text
1. Prove the E73.115 derivative envelopes for NLC and Gloc.
2. Use interval FAR-compatible triples for OUT.
3. Cover the low range by finite box subdivision.
4. Treat lambda=16 LOCK as a finite base case or shrink its alpha box.
5. Use the wide-box certificate from lambda>=24 as the asymptotic pilot.
```

The next non-numerical step is to replace the sampled `NLC/Gloc` suprema
by the derivative interval bounds promised in E73.115.  The `OUT` mechanism
is now correctly formulated: compatible top-three triples, then row upper
sums over their complements.

