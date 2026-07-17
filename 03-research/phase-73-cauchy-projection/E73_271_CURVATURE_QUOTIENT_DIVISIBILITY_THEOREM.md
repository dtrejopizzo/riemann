# E73.271 - Curvature quotient divisibility theorem

Date: 2026-07-14.

## 1. Purpose

E73.270 identifies the admissible Loewner form of the remaining scalar WRL
gate.  E73.239--E73.245 show that endpoint moments and the first DD-local
coborder module do not by themselves prove the center: after removing the
obvious left-coborders, the scalar obstruction survives in a finite quotient.

This note states the proof-facing theorem in that quotient.  It is the next
analytic target after `CLMD`.

## 2. Fixed objects

Let

```text
H_L=H_L^A-H_L^P,
H_Lxi_L=mu_Lxi_L,
E_L=H_L-mu_LI,
Q=Q_w,
P=Q^*(QQ^*)^(-1)Q,
R=I-P,
eta=Rxi_L.
```

For each Cauchy row `q_a`, the master scalar is

```text
S_a=q_aH_Leta=q_aH_LRxi_L.                       (1)
```

Because `q_aeta=0`,

```text
S_a=q_aE_Leta.                                  (2)
```

Equation (2) is not a proof: using `E_Leta=-E_LPxi_L` reintroduces the
Cauchy-plane data `Qxi_L`, which is circular by E73.240.  The valid direction
is a left-coborder identity for the row `q_aH_LR`, so that `E_L` falls on
`xi_L`, not on `eta`.

## 3. The admissible row quotient

Choose a fixed symbolic primitive module `P_L^{sym}` before looking at `xi_L`.
It may contain the DD-local rational blocks already audited in E73.245, plus
endpoint slots forced by the balanced second-Abel normalization.  Define the
left-coborder rowspace

```text
M_L^{sym}={Y^*E_L : Y in P_L^{sym}}.              (3)
```

Let

```text
rho_a=q_aH_LR,                                  (4)
```

and let `Pi_L` denote the exact projection to `M_L^{sym}` in the finite row
space.  Define the quotient row

```text
Delta_a=rho_a-Pi_Lrho_a.                        (5)
```

Then

```text
S_a=rho_axi_L=Delta_axi_L + (Pi_Lrho_a)xi_L.
```

Since `(Pi_Lrho_a)=Y_a^*E_L` for some primitive `Y_a`,

```text
(Pi_Lrho_a)xi_L=Y_a^*E_Lxi_L=0.                 (6)
```

Therefore the master scalar is exactly the quotient pairing

```text
S_a=Delta_axi_L.                                (7)
```

This is the non-circular replacement for the forbidden branch
`S_a=(mu I-A(w))Qxi_L`.

## 4. Relation to CLMD and second-Abel curvature

E73.238 identifies the same scalar as the curvature quotient pairing

```text
S_a=<x(eta),G_curv>,
```

where `x(eta)=(c_omega,l_omega)` is the coefficient vector of

```text
B_a(y)=q_aQ_yeta,
```

and `G_curv=(U^bal_omega,Z^bal_omega)` is the balanced second-Abel curvature
weight.  E73.241 proves that this source row is exactly `q_aH_L` modulo the
Cauchy constraints.  Hence projecting `rho_a=q_aH_LR` modulo `M_L^{sym}` is
the row-space form of projecting the curvature quotient source modulo
structured coefficient coborders.

Thus the following statements are equivalent:

```text
CLMD:
  F_L[q_aQ_yRxi_L]=O_M(L^-M);

BSA-DIV:
  int_0^L K_L(t)(B_a^bal)''(t)dt=O_M(L^-M);

CURV-QUOT-DIV:
  Delta_axi_L=O_M(L^-M).
```

The first two equalities are E73.268--E73.270.  The third is (7).

## 5. The theorem that remains

### Curvature Quotient Divisibility

For every admissible Cauchy window and row, there exists a fixed symbolic
primitive module `P_L^{sym}` and explicit endpoint residual class
`R_L^{end}` such that

```text
rho_a = Y_a^*E_L + Delta_a + r_a^{end},          (8)
```

with:

```text
Y_a in P_L^{sym},
Delta_a in finite quotient coordinates independent of xi_L,
r_a^{end} in R_L^{end},
```

and

```text
Delta_axi_L = O_M(L^-M),
r_a^{end}xi_L = O_M(L^-M).                      (9)
```

Then

```text
S_a=q_aH_LRxi_L=O_M(L^-M),
```

hence `UNIF-ETA`, hence the scalar WRL gate.

## 6. What counts as a proof

The theorem is non-circular only if:

```text
1. P_L^{sym} is specified symbolically from the CCM/Loewner cell formula;
2. Pi_L and Delta_a are obtained from exact row relations, not from a
   pseudoinverse tuned against xi_L;
3. the estimate Delta_axi_L=O_M(L^-M) uses the finite eigenline equation
   and explicit quotient coordinates, not smallness of Qxi_L;
4. endpoint residual slots are fixed before the final scalar is evaluated.
```

The theorem is invalid if it uses:

```text
1. the exact branch Eeta=-EPxi_L;
2. h=Qxi_L as a small input;
3. row-level arch-prime convergence;
4. absolute bounds on separated cosine and Loewner pieces.
```

## 7. Analytic reduction of the remaining estimate

The new analytic work is to compute the quotient coordinates of `Delta_a`
from the coupled Loewner identity

```text
Q_y=2cos(yD)-(2/L)D(sin(yD))[J],
```

after balanced ramp subtraction.  In concrete terms:

```text
(B_a^bal)''(t)
=q_aQ_t''Rxi_L - B_a'(0)r_*''(t),
```

where

```text
Q_t''
=-2D^2cos(tD)+(2/L)D(D^2sin(tD))[J].            (10)
```

Formula (10) is the coupled curvature form: it is not legitimate to estimate
the two displayed terms separately.  After the E73.299 sign audit, the
balanced representative must include the rank-one ramp correction.  The
quotient theorem asks for an exact finite reduction of the corrected row

```text
q_a int_0^L K_L(t)[Q_t''+alpha_L(t)J]dt R
```

modulo `M_L^{sym}` and endpoint slots, followed by the quotient pairing
estimate (9).

The sign comes from

```text
Q_0'=-(2/L)J,
r_*''(t)=-2/L+c_L(2-6t/L),
alpha_L(t)=(2/L)r_*''(t),
```

so `(B_a^bal)''=q_a[Q_t''+alpha_L(t)J]Rxi_L`.  The simplified constant
correction `-(4/L^2)J` is only the `c_L=0` ramp; the neutral ramp of E73.193
requires the full `alpha_L(t)`.

## 8. Immediate finite checks

The next verification should not enlarge the module ad hoc.  It should test
the theorem's proof-facing ingredients:

```text
CQD-1  exact symbolic rank of M_L^{sym};
CQD-2  closed quotient coordinates of rho_a;
CQD-3  equality S_a=Delta_axi_L after exact projection;
CQD-4  scaling of Delta_axi_L against L without using Qxi_L;
CQD-5  endpoint residual pairing after balanced ramp subtraction.
```

The prior E73.245 probe established only a floating diagnostic version of
CQD-1--CQD-3 for the DD-local module.  It did not prove (9), and it showed
that naive module enlargement is not the missing argument.

## 9. Status

```text
proved: master scalar equals quotient pairing after any valid left-coborder
        projection;
proved: this quotient theorem is equivalent to CLMD/BSA-DIV/UNIF-ETA;
audited: forbidden circular branches and separated Loewner estimates;
open: exact symbolic quotient coordinates and the analytic estimate
      Delta_axi_L=O_M(L^-M).
```

## 10. Correction by E73.256 / E73.272

E73.256 applies to the rowspace used here:

```text
M_L^{sym}={Y^*E_L},        E_Lxi_L=0.
```

Hence every exact generated row pairs to zero with `xi_L`, and

```text
Delta_axi_L=(rho_a-Pi_Lrho_a)xi_L=rho_axi_L.
```

Therefore the quotient presentation is not a new scalar cancellation
mechanism.  It is a coordinate/nondegeneracy framework.  The scalar theorem
remains the principal residual:

```text
APR-U4:
rho_axi_L=q_aH_LR_wxi_L=O_M(L^-M).
```

See E73.272 for the corrected route, and E73.300--E73.301 for the corrected
neutral-ramp curvature quotient normal form.
