# E73.025 - Pi Lebesgue audit

## 1. Why this audit is necessary

E73.024 observed that

```text
CRIT-POLY + PI-LEB-NH => CC-PROJ.
```

But E72.396 already warned that the natural-height projection is the remaining hard finite
assertion.  Therefore `PI-LEB-NH` cannot be treated as automatic Cauchy geometry.

## 2. Cluster falsifier

Take three off-line nodes with fixed positive real part and nearly equal imaginary parts:

```text
b_j = sigma + i(t+j epsilon),     j=0,1,2.
```

For `epsilon=exp(-cL)`, the Cauchy interpolation kernel develops inverse powers of `epsilon` through
the factors

```text
prod_{c!=a}(a-c)^(-1)
```

inside the Lagrange weights.  E73.025 confirms the resulting blow-up numerically.

Therefore the estimate

```text
e^(sigma L)sum_k|Pi(b,k)| <= L^B
```

is false without further hypotheses.

## 3. Corrected status of PI-LEB

The right statement is conditional:

```text
PI-LEB-NH holds if the natural-height off-line Cauchy block has polynomially controlled
confluent condition after Hermite normalization.
```

Equivalently, the dangerous quantity is not just `Pi`, but the normalized Cauchy inverse:

```text
Leb_O,K(L)
= max_{b in O_L} e^(Re b L)sum_{k in K_L}|Pi(b,k)|.
```

The finite theorem must prove:

```text
Leb_O,K(L) <= L^B
```

or prove that the bad singular directions of `Pi` annihilate the critical vector `G_K`.

## 4. Three possible closures

The remaining finite projection can close by one of three mechanisms:

```text
GEOM:
natural-height off-line clusters have polynomial Hermite-normalized Cauchy condition;

CONFL:
after confluent/Hermite coordinates, the exponential cluster blow-up is exactly removed;

DATA:
the critical cancelled-Cauchy vector lies in the null directions of the large Pi modes.
```

`GEOM` alone is unlikely to be available without arithmetic information about zeros.  `CONFL` is
structural and should be tested next because Phase 72 already has a confluent Cauchy determinant
mechanism.  `DATA` is closest to the original NAT-PROJ identity.

## 5. Corrected chain

The honest chain is:

```text
E72.327 CRIT-POLY
+ (GEOM or CONFL or DATA)
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL
=> Omega_7.
```

E73.024 gives a sufficient route.  E73.025 prevents overclaiming it as a solved route.

## 6. Next target

The next natural finite task is:

```text
CONFL-PI:
rewrite Pi in Hermite/confluent coordinates for clustered off-line nodes and test whether the
weighted Lebesgue blow-up is an artifact of using separated-node coordinates.
```

If `CONFL-PI` fails, the remaining gate is genuinely `DATA`: cancellation of the critical vector in
the bad Cauchy inverse modes.

## 7. Update from E73.026

`CONFL-PI` passes the local cluster falsifier.  In normalized Hermite coordinates the Cauchy
projection remains finite as separated nodes coalesce.  Therefore the E73.025 blow-up is a coordinate
singularity, not by itself a fatal obstruction.

The remaining theorem is now the global natural-height version:

```text
CONFL-PI-NH:
Hermite-normalized confluent Cauchy projection has polynomial weighted Lebesgue size over all
natural-height off-line clusters.
```

If this global Hermite bound fails, then the only remaining closure mechanism is `DATA`.
