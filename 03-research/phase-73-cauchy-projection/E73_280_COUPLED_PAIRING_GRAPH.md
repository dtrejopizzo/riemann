# E73.280 - Coupled pairing graph

Date: 2026-07-14.

## 1. Purpose

E73.278 and E73.279 show that APR-U4 is not explained by a quotient:

```text
pure cauchy0 quotient: fails,
full canonical quotient S_L/M_L: fails.
```

The reason is structural: the true APR scalar is small because generated and
residual sectors cancel.  E73.280 tests the correct object:

```text
ell_L(c)=<xi_L,S_Lc>,
```

where `S_L` is the canonical source-coordinate reconstruction map.  The
question is whether APR coefficient vectors lie near the kernel of this
functional.

## 2. Objects

Let

```text
S_L=span{
  cauchy0_gamma,
  DD_L(-gamma,d)/(d^2+beta^2)^r,
  d^(2q)DD_L(-gamma,d)
}.
```

Let `M_L` be the coefficient image of `(H_L-mu_LI)` from the canonical
primitive module.  For each Cauchy plane row:

```text
rho_j(w)=q_jH_L(I-P_w)=S_Lc_{j,w}.
```

Let

```text
ell_L(c)=<xi_L,S_Lc>.
```

The scalar APR theorem is exactly:

```text
ell_L(c_{j,w})=O_M(L^(-M)).
```

## 3. Test

Decompose the coefficient vector orthogonally:

```text
c_{j,w}=m_{j,w}+u_{j,w},
m_{j,w} in M_L,
u_{j,w} perpendicular to M_L.
```

Then compare:

```text
ell_L(c_{j,w}),
ell_L(m_{j,w}),
ell_L(u_{j,w}),
dist(c_{j,w},ker ell_L)
= |ell_L(c_{j,w})|/(||ell_L|| ||c_{j,w}||).
```

## 4. Result

The APR coefficient vectors are extremely close to the kernel of `ell_L`:

```text
kerDist ~ 1e-8 to 1e-10
```

in the tested windows.

At the same time, the two components are not small:

```text
ell_L(m_{j,w}) and ell_L(u_{j,w})
```

are often many powers of `L` larger than `ell_L(c_{j,w})`, with nearly equal
opposite phase.  This is exactly the interference pattern predicted by
E73.279.

The graph identity

```text
ell_L(m_{j,w})+ell_L(u_{j,w})=ell_L(c_{j,w})
```

holds at numerical floor; the point is not that this identity is deep, but
that the near-kernel property of the specific APR vector is the correct
finite theorem to prove.

## 5. Correct theorem target

The current endpoint is now:

```text
APR-NEARKER:
For every admissible critical Cauchy plane row,
if c_{j,w} is the canonical coefficient vector of rho_j(w)=q_jH_L(I-P_w),
then

|ell_L(c_{j,w})| <= A_M L^(-M)

for every M.
```

The proof must not quotient out `M_L`.  It must prove that the generated and
orthogonal canonical sectors have paired values cancelling to all powers.

Equivalently:

```text
ell_L(m_{j,w}) = -ell_L(u_{j,w}) + O_M(L^(-M)).
```

## 6. Why this is progress

This identifies the exact algebraic place where the scalar cancellation lives:

```text
not in a small residual norm,
not in a quotient class,
not in a positive estimate,
but in a finite near-kernel relation for ell_L on the APR coefficient graph.
```

Thus the next proof-facing object is a symbolic relation between:

```text
1. the canonical action matrix of (H_L-mu_LI);
2. the APR coefficient vector c_{j,w};
3. the pairing row ell_L.
```

## 7. Next step

Build the finite matrix identity:

```text
ell_L c_{j,w}
= ell_L A_L y_{j,w} + ell_L u_{j,w},
ell_L A_L y_{j,w} + ell_L u_{j,w}=O_M(L^(-M)),
```

with `A_L` the canonical action matrix.  The target is a symbolic cancellation
formula for the scalar

```text
ell_L A_L y + ell_L u.
```

Because `ell_L A_L` is not zero as a row, this is not a left-coborder
tautology.  It is the first formulation that keeps the interference required
by the data.

## 8. Status

```text
tested: ell_L near-kernel property of APR coefficient vectors;
observed: kerDist ~ 1e-8 to 1e-10;
identified: cancellation between generated and orthogonal sectors;
open: derive symbolic finite near-kernel identity APR-NEARKER.
```
