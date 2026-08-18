# D.148 — Directed certificate for the finite primitive block at `T=log(5)/2`

## Exact scope

Let `L_170` be the span of the first 170 normalized Legendre modes on
`[-T,T]`, and let `P_T` denote the two Tate moment conditions.  This
certificate proves strict positivity of the completed quadratic form on

\[
       V_{170}=L_{170}\cap P_T.
\]

It does **not** assert positivity on the full infinite-dimensional primitive
space.  In particular, the `P/Q` splitting is not reducing for the completed
multiplier.  A full endpoint certificate still has to control the Feshbach
cross term and the rank-two primitive defect between the truncated and full
moment representers.

## Directed inputs

1. `114_d_147_hurwitz_gamma_arb.py` evaluates the complete, untruncated
   Gamma block by the finite Hurwitz--Lerch formula of D.146.  The target run
   uses 1300 decimal digits.
2. `114_d_100_log5_contacts_arb.py` constructs a degree-exact Gauss--Legendre
   rule with certified root intervals and encloses the three active contacts
   `n=2,3,4`.  Conversion of Arb midpoints and radii to binary64 is enlarged
   outward by half an ulp and `nextafter(+infinity)`.
3. `114_d_148_log5_directed_congruence.py` evaluates both Tate moments with
   the exact modified-Bessel formula, eliminates them by an interval
   two-column graph, and forms the resulting 168 by 168 symmetric Arb matrix.

No Fourier quadrature, Gamma truncation, tail atom, or floating-point sign
decision enters the certificate.

## Positivity congruence

If `B` is the interval matrix after exact graph elimination, its midpoint is
used only to choose a numerical Cholesky preconditioner.  The stored decimal
upper-triangular matrix is exactly invertible because its diagonal entries
are nonzero.  Thus

\[
                 C=P^tBP
\]

is a genuine congruence.  Arb then proves, row by row,

\[
 C_{ii}-\sum_{j\ne i}|C_{ij}|>0.
\]

Gershgorin and Sylvester inertia therefore imply `B>0` without relying on
the midpoint eigenvalue computation.

## Reproduction

From the repository root used by the phase:

```sh
PYTHONPATH=/tmp/d61-flint D100_N=170 D100_PREC=2048 \
  python3 114_d_100_log5_contacts_arb.py

PYTHONPATH=/tmp/d61-flint D148_N=170 D148_DPS=1300 \
  python3 114_d_148_log5_directed_congruence.py
```

The certified output is:

```text
Gauss mass enclosure error= [+/- 1.42e-173]
max native contact radius= 3.454827379733383e-173
PASS directed polynomial-exact contact matrix enclosure

directed-block centre eigenvalues first =
[3.12096329e-12 6.26221520e-10 3.12351855e-07 3.12491856e-05 ...]
minimum directed Gershgorin margin = [0.9999 +/- 5.96e-5]
D148 T=log(5)/2 constrained low block: DIRECTED POSITIVITY PASS
```

## Verdict

The finite primitive block obligation is closed.  This result must be used
with its stated finite scope; it is one input to, not a substitute for, the
remaining infinite-dimensional Feshbach certificate.
