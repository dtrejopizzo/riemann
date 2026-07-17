# E74.9 - Harmonic left-coborder audit

Date: 2026-07-16.

## 1. Purpose

E74.2--E74.4 introduced the exact finite harmonic coordinate

```text
A r_beta = H_beta r_beta,
```

where `A` is the closed mesh Hilbert matrix.  E74.8 then showed that the
Gamma-prime cancellation is not a cell-functional identity on all of `ker Q_w`;
it is specific to the eigenline.

This note tests whether the new harmonic coordinate supplies the missing
structured left-coborder:

```text
rho_a = q_a H_L(I-P_w)
      = Y_{a,w,L}(H_L-mu_L I) + residual.
```

The primitive `Y` is restricted to fixed symbolic modules built before seeing
the final scalar.  No full pseudoinverse, no vector depending on `xi_L`, and
no residual-selected atom is allowed.

## 2. Modules Tested

Baseline controls from Phase 73:

```text
poly:
  span{D^k q_j : 0<=k<=2, j=1,2}.

rat:
  poly plus D^k q_j/(D^2+beta^2),
  beta in {gamma, 2pi/L, 1}.
```

New harmonic modules:

```text
harm:
  span{D^k q_j,
       D^k(q_j H_beta_j),
       D^k(q_j A) : 0<=k<=2, j=1,2}.

harmRat:
  harmonic atoms plus the same fixed geometric denominators.

harmHi:
  harmRat with one extra polynomial power.
```

Here

```text
H_beta_j(n)= -i/(2 pi) sum_{m != n}
             [1/(m-n)-1/(m-beta_j)].
```

For each module `P`, fit:

```text
rho_a approx Y(H_L-mu_LI),       Y in P.
```

## 3. Algebraic Constraint

The audit exposes the invariant obstruction:

```text
(H_L-mu_LI)xi_L=0.
```

Therefore every exact primitive term is scalar-invisible:

```text
Y(H_L-mu_LI)xi_L=0.
```

So for any fitted primitive,

```text
(rho_a-Y(H_L-mu_LI))xi_L = rho_a xi_L
```

up to numerical error.  This is not a bug of the fit.  It is left-coborder
invariance.

Consequently, row-norm approximation cannot by itself prove the Gamma-prime
cancellation.  A successful theorem must identify a named residual slot
`R_{a,w,L}` and prove directly that

```text
R_{a,w,L}xi_L=O_M(L^(-M)).
```

## 4. Computed Result

The script:

```text
python3 E74_009_harmonic_coborder_probe.py
```

reports:

```text
centerB  = exponent of |rho_a xi_L|
resPairB = exponent of |(rho_a-Proj_M rho_a)xi_L|
resRel   = row-norm residual / row-norm rho_a
projRel  = row-norm projection / row-norm rho_a
```

Representative values:

```text
L=5.545, gamma=14.13, row=0:
  poly    centerB=-19.21, resPairB=-19.37, resRel=3.1e-01
  rat     centerB=-19.21, resPairB=-16.48, resRel=3.4e-07
  harm    centerB=-19.21, resPairB=-19.19, resRel=3.8e-04
  harmRat centerB=-19.21, resPairB=-19.26, resRel=1.4e-09

L=5.991, gamma=21.02, row=1:
  poly    centerB=-17.79, resPairB=-17.88, resRel=9.2e-01
  rat     centerB=-17.79, resPairB=-13.77, resRel=4.5e-06
  harm    centerB=-17.79, resPairB=-17.49, resRel=6.8e-03
  harmRat centerB=-17.79, resPairB=-19.31, resRel=1.5e-08
```

The row residual can be tiny after adding rational/harmonic atoms, but the
scalar residual does not acquire a stable improvement over the original
center.  This is exactly what the invariant predicts.

## 5. Verdict

```text
tested:  harmonic-symbol primitive modules built from q_j, q_jH_beta_j,
         q_jA, polynomial powers, and fixed geometric denominators;
failed:  direct left-coborder fitting as a scalar closure mechanism;
proved:  every direct Y(H_L-mu_LI) primitive is scalar-invisible on xi_L;
kept:    harmonic coordinates as exact row normal form, not as a scalar
         cancellation theorem by themselves.
```

The surviving theorem must be a residual-slot theorem:

```text
rho_a = Y_{a,w,L}(H_L-mu_LI) + R_{a,w,L},
R_{a,w,L}xi_L=O_M(L^(-M)),
```

where `R_{a,w,L}` is not the arbitrary least-squares remainder.  It must be an
explicit finite cell/Loewner/harmonic residual whose eigenline pairing is
proved directly.

