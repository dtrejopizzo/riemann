# E73.277 - Residual slot theorem and program audit

Date: 2026-07-14.

## 1. Purpose

E73.274--E73.276 tested the last apparent freedom in the APR-U4 scalar
residual:

```text
S_{a,w,L}=q_aH_LR_w xi_L.
```

The tests show that changing coordinates does not create a new cancellation
mechanism.  This note records the exact obstruction and compares it with the
older Phase 73 canonical `cauchy0` obstruction and the earlier program-wide
Sonin/prolate/Feshbach audits.

## 2. Current exact scalar form

Let

```text
E_L=H_L-mu_L I,
E_L xi_L=0,
R_w=I-Q_w^*(Q_wQ_w^*)^(-1)Q_w,
rho_{a,w}=q_aH_LR_w.
```

The endpoint scalar theorem is

```text
APR-U4:
rho_{a,w} xi_L = O_M(L^(-M)).
```

E73.269 gives equivalent exact forms:

```text
rho_{a,w}xi_L
= A_L[B_{a,w}]-P_L[B_{a,w}]
= sum_omega c_omega W_omega + sum_omega l_omega V_omega
= int_0^L K_L(t)(B_{a,w}^{bal})''(t)dt
= q_a[H_L^A,R_w]xi_L-q_a[H_L^P,R_w]xi_L.
```

E73.270 imports the exact Loewner displacement identity:

```text
Q_y=2cos(yD)-(2/L)D(sin(yD))[J],
```

so the Loewner form is

```text
F_L[2q_acos(yD)R_wxi_L
    -(2/L)q_aD(sin(yD))[J]R_wxi_L].
```

The cosine and Loewner pieces cannot be bounded separately: E72.55 already
showed that the cancellation is coupled.

## 3. Coborder invariance

Let `M_L` be any left coborder module:

```text
M_L={Y^*E_L : Y in P_L}.
```

Then every row in `M_L` annihilates the ground line:

```text
(Y^*E_L)xi_L=Y^*(E_Lxi_L)=0.
```

Therefore, for every orthogonal projection `Proj_M` onto a left coborder
module,

```text
(rho_{a,w}-Proj_M rho_{a,w})xi_L=rho_{a,w}xi_L.
```

This is the formal reason behind:

```text
E73.256: quotient pairing invariance,
E73.272: curvature quotient correction,
E73.275: CL-action row projection cannot prove APR-U4,
E73.276: curvature source coordinates collapse back to q_aH_L.
```

## 4. Residual slot theorem

Any non-tautological proof of APR-U4 by eigenline algebra must produce a
decomposition

```text
rho_{a,w}=Y_{a,w}^*E_L+r_{a,w}
```

with all three properties below.

### R1. Fixed symbolic primitive

`Y_{a,w}` must be built from a fixed symbolic primitive module.  It cannot be
the ambient least-squares primitive or an adjugate row chosen to solve the
scalar equation.

### R2. Named residual class

`r_{a,w}` must lie in a named residual slot not equal to:

```text
left coborders,
coordinate quotients,
source-coordinate rewrites,
endpoint normal forms,
generic kernel constraints,
full rowspace certificates.
```

### R3. Direct scalar estimate

The proof must estimate

```text
r_{a,w}xi_L=O_M(L^(-M))
```

directly from the finite CCM/Feshbach equation, the exact Loewner identity, or
an explicit finite critical Cauchy divisor.  If the estimate is merely
`rho_{a,w}xi_L=O_M(L^(-M))` in different notation, it is APR-U4 restated.

## 5. Relation with the canonical cauchy0 obstruction

E73.163--E73.167 already identified a genuine residual slot in a different
coordinate system.

After eliminating generated rational and endpoint slots, the remaining
canonical source has the form

```text
D_A(d)=sum_{gamma in K_L} delta_A(gamma)DD_L(-gamma,d).
```

The exact obstruction is the quotient

```text
C_L/(C_L cap M_L),
dim C_L=5,
dim(C_L cap M_L)=2,
dim quotient=3
```

in the trusted windows.  The surviving theorem was

```text
QUOT-CRIT-DIV:
e^(alpha L)|<P_{Q,L}Pi_A,G_K>| <= L^B.
```

E73.274--E73.276 do not supersede this.  They show that the APR source row
does not create an additional residual slot by curvature or Loewner
coordinate changes.  Thus the honest fork is:

```text
either APR-U4 is reduced to the old three-dimensional cauchy0 quotient,
or a genuinely new residual slot must be exhibited.
```

At present no new slot has been exhibited.

## 6. Program audit

A quick text audit against the earlier program shows that the following
themes are not new closing mechanisms here:

```text
Sonin / Connes compression:
  already audited in the proof log and Phase 39 as a zero-independent
  positive archimedean square.  It identifies the local positive side but does
  not supply the finite-place residual sign.

Prolate / Slepian bridge:
  previously classified as superficial for the global P8 route and useful
  only for localized diagnostics.  It does not close the master arithmetic
  quantifier.

Feshbach shorting:
  Phase 65 already made the correct move: remove the pole by Schur/Feshbach
  shorting, not subtraction.  The wall remained the cross-term/Feshbach
  inverse continuation, not the algebra of shorting itself.

Loewner/Nevanlinna:
  Phase 39 and Phase 72 show that Loewner is an excellent inertia language,
  but the exact Loewner identity alone does not prove the coupled cancellation.
```

Therefore the current work is not allowed to claim novelty from these words
alone.  The only possible new content is a finite residual estimate that sees
the signed CCM/Feshbach eigenline data without converting it into a positive
incoherent ceiling.

## 7. Current map after E73.277

The route to Omega7 now has this shape:

```text
Omega7
<= scalar WRL
<= UNIF-ETA
<=> CELL-CTM
<=> COEFF-ETA
<=> SECOND-ABEL
<=> COMM-TRANSPORT
<=> APR-U4
```

The load-bearing analytic theorem is still:

```text
APR-U4:
q_aH_LR_wxi_L=O_M(L^(-M)).
```

The strongest non-tautological finite residual already available is:

```text
QUOT-CRIT-DIV:
e^(alpha L)|<P_{Q,L}Pi_A,G_K>| <= L^B
```

on the three-dimensional canonical `cauchy0` quotient.

## 8. Next mathematically meaningful move

Do not add another projection module.  The next step must be one of:

```text
N1. Prove symbolically that the APR principal residual maps to the same
    three-dimensional cauchy0 quotient as QUOT-CRIT-DIV.

N2. Write an explicit basis for C_L cap M_L by partial fractions, so
    P_{Q,L} is algebraic rather than numerical.

N3. Prove a finite signed Cauchy divisor estimate on the quotient:

    e^(alpha L)|<P_{Q,L}Pi_A,G_K>| <= L^B.
```

`N1` is the immediate bridge.  If it succeeds, the current APR-U4 formulation
and the older canonical `cauchy0` endpoint are the same theorem in two
languages.  If it fails, APR-U4 still lacks a named residual slot and the route
is not yet mathematically closed.

## 9. Status

```text
proved: left-coborder quotienting cannot change the scalar pairing;
proved: curvature source adjoint equals q_aH_L;
audited: Sonin/prolate/Feshbach/Loewner mechanisms were already explored and
         cannot be reused as standalone closure;
identified: only surviving non-tautological residual slot is the canonical
            three-dimensional cauchy0 quotient, unless a new slot is explicitly
            constructed;
open: prove the APR-to-cauchy0 bridge, then prove the signed quotient estimate.
```
