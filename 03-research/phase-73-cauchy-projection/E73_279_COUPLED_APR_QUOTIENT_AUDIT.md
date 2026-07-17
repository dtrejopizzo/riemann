# E73.279 - Coupled APR quotient audit

Date: 2026-07-14.

## 1. Purpose

E73.278 rejected the pure `cauchy0` reduction of APR-U4.  The next possible
residual slot was the full canonical source quotient

```text
S_L/M_L,
```

where `S_L` is the canonical source space of E73.163 and `M_L` is the image of
the finite local action `(H_L-mu_LI)` in those source coordinates.

The candidate theorem was:

```text
COUPLED-APR-QUOT:
[rho_j(w)] in S_L/M_L pairs with xi_L by O_M(L^(-M)).
```

E73.279 tests this candidate.

## 2. Test

For each scale and critical Cauchy plane:

```text
rho_j(w)=q_jH_L(I-P_w).
```

Fit `rho_j(w)` in the canonical source basis:

```text
S_L=span{
  cauchy0_gamma,
  DD_L(-gamma,d)/(d^2+beta^2)^r,
  d^(2q)DD_L(-gamma,d)
}.
```

Build `M_L` by applying `(H_L-mu_LI)` to the canonical primitive module and
expressing the result in `S_L`.  Then decompose the coefficient vector:

```text
coeff(rho)=Proj_{M_L}coeff(rho)+(I-Proj_{M_L})coeff(rho).
```

Pair both parts with `xi_L` after reconstruction in mesh space:

```text
center      = rho xi_L,
class_pair  = S_L(I-Proj_M)coeff(rho) xi_L,
gen_pair    = S_LProj_M coeff(rho) xi_L.
```

## 3. Result

The full quotient also fails as a residual slot.

In trusted rows the quotient and generated parts are individually much larger
than the true APR center:

```text
class/center often ranges from 1e2 to 1e7,
gen/center often ranges from 1e3 to 1e9.
```

The true center is small because of cancellation between the quotient class
and the generated component.  Passing to the quotient destroys that
interference.

The computed quotient dimensions are modest:

```text
rank(S_L) about 15--17,
rank(M_L) about 5--6,
quotient dimension about 10--12
```

in these windows, but the quotient class is not the small object.

## 4. Meaning

E73.278 and E73.279 together rule out the current quotient strategy:

```text
pure cauchy0 quotient: fails;
full canonical source quotient S_L/M_L: fails.
```

This is not merely numerical disappointment.  It identifies the mechanism:

```text
APR-U4 is an interference theorem between generated and residual sectors.
```

Any proof that kills the generated sector by quotienting loses the cancellation
that makes

```text
rho_j(w)xi_L
```

small.

## 5. Correct next form

The next theorem cannot be a quotient theorem.  It must be a coupled pairing
identity:

```text
COUPLED-PAIR:
rho_j(w)=S_L c_{j,w},
c_{j,w}=m_{j,w}+u_{j,w},   m_{j,w} in M_L,
```

with a direct identity or estimate for the paired sum

```text
<xi_L,S_Lm_{j,w}> + <xi_L,S_Lu_{j,w}> = O_M(L^(-M)).
```

The finite algebraic object is therefore the pair

```text
(M_L, ell_L),
ell_L(c)=<xi_L,S_Lc>,
```

not the quotient `S_L/M_L`.  The target is to prove that the APR coefficient
vector lies near the kernel of the induced functional:

```text
ell_L(c_{j,w})=O_M(L^(-M)).
```

## 6. Non-tautology condition

This is not allowed to be solved by defining `c_{j,w}` from the final scalar.
The coefficient vector must be obtained from the fixed canonical source
expansion of `rho_j(w)`, and the proof must use:

```text
1. the explicit action matrix of (H_L-mu_LI) in canonical coordinates;
2. the finite Cauchy/Loewner cell identities;
3. the eigenline relation only through fixed generated coordinates.
```

The new proof target is therefore a finite left-null or near-left-null
identity for the functional `ell_L` on the coupled canonical source graph.

## 7. Status

```text
tested: full canonical quotient S_L/M_L;
rejected: quotient class as small residual;
identified: APR-U4 is generated/residual interference;
open: build the coupled pairing graph and prove a finite left-null identity
      for ell_L on APR coefficient vectors.
```
