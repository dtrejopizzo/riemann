# E77.7j - LP chain audit after Ritz and endpoint autopsies

**Run:** 2026-07-18.

## 1. Reason for the audit

E77.7f--h and E77.7i settle two independent issues on the LP front:

```text
1. BTG-DIV-L is the correct moving-boundary growth target, but the current
   Ritz route does not yet certify the true-mu bracket on the interlacing
   scale.
2. Scalar Weyl-disk contraction is not, by itself, the full P76.065
   SAFE-LIMIT-POINT endpoint unless the disk is identified with the family
   of normalized safe transforms.
```

This note records the honest chain after those autopsies, names the exact
missing interfaces, and prevents silent reuse of refuted shortcuts.

## 2. What remains valid

From E77.7d:

```text
H_L=D_L+B_L,
D_L(n)=log(1+|n|)+O_L(1),
B_L bounded self-adjoint,
H_L has compact resolvent,
mu_L=inf spec(H_L) is an isolated eigenvalue of finite multiplicity.
```

From E77.7f and E77.7g:

```text
BTG-DIV-L:
S_N(mu_L)=||A_N(mu_L)^(-1)b_N||^2
        = sum_j |<u_j^(N),b_N>|^2 / |nu_j^(N)-mu_L|^2 -> infinity.
```

The exact spectral split is

```text
LOW-MODE-BTG(K) => BTG-DIV-L,
TAIL-BTG(K)     => BTG-DIV-L.
```

No one-coupling reduction to a fixed `l2` source is admissible, because
`b_N` is a moving boundary column.

## 3. What E77.7h refuted precisely

The coarse tail bracket

```text
mu_R-eps_R^tail <= mu_L <= mu_R
```

is genuine but too coarse for BTG.  The naive directional Ritz residual and
the finite Temple proxy both lose the complement coercivity denominator.

The exact missing object is:

```text
FESHBACH-RITZ-ENVELOPE:
construct 0 <= mu_R-mu_L <= eta_R
from the scalar Feshbach equation of the Ritz ground direction, keeping the
orthogonal-complement coercivity kappa_R(E) explicit.
```

If this is proved on the interlacing scale and paired with low-mode
divergence, then

```text
FESHBACH-RITZ-ENVELOPE
=> BRACKETED-LOW-MODE-BTG
=> LOW-MODE-BTG(K)
=> BTG-DIV-L.
```

This is the smallest currently admissible bracket route.  Any future
replacement must imply `BTG-DIV-L` explicitly.

## 4. What E77.7i refuted precisely

Let

```text
E_L = ker(H_L-mu_L),
ell_0(v)=r_{z0}v,
ell_z(v)=r_z v.
```

Then uniqueness of the normalized safe transform is equivalent to

```text
ell_z|_(E_L cap ker ell_0)=0
```

for every safe `z`.  Under separation of safe rows on `E_L`, this reduces to

```text
dim E_L=1 and ell_0(v0) != 0.
```

Compact resolvent gives only finite multiplicity.  Therefore

```text
BTG-DIV-L => scalar Weyl radius -> 0
```

does **not** by itself prove the P76.065 endpoint.

The minimum missing bridge is:

```text
SAFE-DISK-IDENT:
for the fixed-L CCM boundary relation,
  (a) finite scalar disks are exactly the images under safe rows of the
      normalized l2 solution family;
  (b) singular sections are treated by the boundary-relation limit;
  (c) radius -> 0 implies uniqueness of the safe transform locally
      uniformly on the safe axis.
```

Then the honest implication is

```text
BTG-DIV-L + SAFE-DISK-IDENT
=> SAFE-LIMIT-POINT of P76.065.
```

## 5. Corrected LP front

The current analytic front is therefore:

```text
FESHBACH-RITZ-ENVELOPE or another admissible BTG route
=> BTG-DIV-L
=> scalar Weyl-disk contraction
```

and independently

```text
SAFE-DISK-IDENT
=> scalar contraction upgrades to P76.065 SAFE-LIMIT-POINT.
```

So the LP endpoint now reads:

```text
BTG-DIV-L + SAFE-DISK-IDENT
=> SAFE-LIMIT-POINT.
```

This replaces the older shorthand

```text
BTG-DIV-L => corrected LP
```

which was too compressed and hid the boundary-relation identification step.

## 6. Operational consequences

1. `FESHBACH-RITZ-ENVELOPE` is a legitimate next target on the BTG side.
   It is falsifier-neutral in the same sense as E77.7g--h: both zeta and the
   planted build can satisfy or fail it without importing positivity,
   zero-filters, or Weil-sign surrogates.

2. `SAFE-DISK-IDENT` is now a first-class open theorem.  It is an analytic
   interface statement about the long-range CCM boundary relation, not an
   arithmetic positivity target.

3. The phrase "LP is closed once BTG-DIV-L is proved" is no longer
   admissible.  What closes from BTG alone is scalar disk contraction.

## 7. Current minimal live objects

```text
LP-BTG side:      FESHBACH-RITZ-ENVELOPE.
LP-interface side: SAFE-DISK-IDENT.
```

Either one can be pursued next, but neither may be silently replaced by
fixed-overlap, ambient inverse-norm, or coarse tail-only claims.
