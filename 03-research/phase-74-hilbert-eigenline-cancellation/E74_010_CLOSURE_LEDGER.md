# E74.10 - Residual-slot closure ledger for Omega7

Date: 2026-07-16.

## Purpose

E74.1--E74.9 closed the Hilbert product-rule bookkeeping and rejected the
direct primitive-span closure.  This note records the exact theorem that would
close the current Omega7 route, and the rules under which it must be proved.

## Objects

Use the Phase 73/74 endpoint notation:

```text
H_L xi_L = mu_L xi_L,
Q=Q_w,
P_w=Q^*(QQ^*)^(-1)Q,
R_w=I-P_w,
q=q_a,
rho_{a,w}=qH_LR_w.
```

The scalar endpoint is

```text
S_{a,w,L}=rho_{a,w}xi_L.
```

E73.295, E73.304, and E73.305 prove the equivalences:

```text
S_{a,w,L}=F_L[y -> qQ_yR_wxi_L]
          =<T^diag_{a,w,L}+T^off_{a,w,L},W_L>
          =HPR-DIV total
          =FINAL-ETA-ADJ normalized scalar.
```

## RSLOT-O7

The residual-slot theorem needed to close the route is:

```text
RSLOT-O7.
For every admissible natural-height row/window and every M, construct

rho_{a,w}=Y_{a,w,L}(H_L-mu_LI)+R_{a,w,L}

where Y_{a,w,L} is built from a fixed finite cell/Loewner/Hilbert algebra and
R_{a,w,L} belongs to a named residual slot, such that

R_{a,w,L}xi_L=O_M(L^(-M)).
```

Then, because `(H_L-mu_LI)xi_L=0`,

```text
rho_{a,w}xi_L=R_{a,w,L}xi_L=O_M(L^(-M)).
```

## Consequence chain

The full conditional chain is:

```text
RSLOT-O7
=> HPR-DIV / FINAL-ETA-ADJ / Directional Cell Eigenline Cancellation
=> NAT-PROJ                                      [E72.396]
=> off-line nodal suppression                    [E72.396]
=> PW-Cauchy                                     [E72.326]
=> SQB => CB => RNS => MC-NZ => NZ-MSD
=> scalar WRL
=> Omega7.
```

This is the exact current meaning of "close Omega7" in Phase 74.

## Forbidden proof moves

The proof of `RSLOT-O7` may not use:

```text
1. Q_wxi_L or Q_weta being small as input;
2. a pseudoinverse or adjugate row chosen to solve rho xi_L directly;
3. absolute row sums or a separated archimedean/prime ceiling;
4. a zero-filter whose divisor contains the off-critical zeta divisor;
5. a reduction back to generic Weil positivity or heat-flow monotonicity;
6. a new primitive module whose only effect is a left-coborder projection.
```

The only allowed smallness source is a signed finite identity from the
cell/Gamma-prime/eigenline algebra.

## Current implementation path

E73.277 says the next meaningful move is:

```text
N1. Prove symbolically that the APR principal residual maps to the same
    three-dimensional cauchy0 quotient as QUOT-CRIT-DIV.
```

Therefore E74.11 tests the bridge:

```text
APR principal residual -> C_L/(C_L cap M_L).
```

If the bridge closes with an explicit quotient lift, the named residual slot
is the quotient-lifted cauchy0 residual.  If it fails, `RSLOT-O7` needs a new
finite residual slot.

## Status

```text
proved: all endpoint forms above are equivalent;
proved: left-coborder projection alone cannot change the scalar;
open:   construct a named residual slot and prove its eigenline pairing is
        super-polynomially small.
```

