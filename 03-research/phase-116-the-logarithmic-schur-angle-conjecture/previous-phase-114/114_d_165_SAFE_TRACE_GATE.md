# D.165 — Safe trace gate for the rank-60 graph

## Statement

After the rank-60 graph shorting, split the finite primitive frame into the
five frozen endpoint-flat columns and 163 safe columns.  On the safe block
write

\[
 K=\mathcal S_{Y,ss}>0,
 \qquad G=\mathcal R_s^*\mathcal R_s\ge0,
 \qquad L_{ss}=K-\delta^{-1}G.
\]

Put

\[
 \theta=\delta^{-1}\mathrm{tr}(K^{-1}G)
 =\delta^{-1}\|\mathcal R_sK^{-1/2}\|_{HS}^2.
\]

If `theta<1`, then

\[
 \boxed{L_{ss}\ge(1-\theta)K>0.}
\]

Indeed, `X=K^{-1/2}GK^{-1/2}` is positive and
`X <= ||X|| I <= tr(X) I`.  This replaces a directed 163 by 163 residual
Gram by one directed Hilbert--Schmidt scalar.

## Final five-dimensional Schur bound

The same estimate gives

\[
 L_{ss}^{-1}\le(1-\theta)^{-1}K^{-1}.
\]

Consequently the endpoint follows from the directed five-dimensional test

\[
 \boxed{
 L_{dd}-{1\over1-\theta}L_{ds}K^{-1}L_{sd}>0.
 }
\]

Thus no 163-dimensional inverse is required in the delicate final step.

## Selection audit (not evidence)

For the frozen rank-60 centre and the five endpoint-flat columns selected
against that centre:

```text
lambda_min(K)              = 5.7577e-2
trace(K^-1 G) / 0.218      = 4.6531e-1
||K^-1/2 G K^-1/2||/0.218 = 5.1661e-2
```

The trace gate therefore has a factor larger than two of numerical room.
These figures only set interval budgets.

## Exact directed data still required

The five-column moment matrices alone do not determine this gate.  A proof
needs the following contractions from the frozen rank-60 graph:

1. a directed congruence proving `K>0`;
2. the scalar `||R_s K^-1/2||_HS^2`;
3. the directed `5x5` block `L_dd`;
4. the directed `5x5` cross-short Gram `L_ds K^-1 L_sd`.

Items 2 and 4 can be accumulated as scalar and five-column norms after a
frozen safe preconditioner; they do not require storing a dense residual
Gram.  Item 1 still requires a directed Loewner enclosure of the safe graph
short, obtained from `B`, `D_Y`, and `C_Y` (or an operator-norm enclosure of
their preconditioned error).  The selector-only binary64 file is not proof.

The rank-two Tate defect is independent and already satisfies the directed
absorption estimate of D.152.
