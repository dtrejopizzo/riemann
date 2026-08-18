# Phase 77 - Omega7 Closure Plan V2

**Updated:** 2026-07-18 after E77.7e.

## 1. Exact Conditional Chain

The proved assembly is

```text
LP + IDENT + RDP-SHELL + RADICAL-PAIRING
=> SAFE-LIMIT-POINT
=> SAFE-PROLATE-BRIDGE
=> SR-SAFE
=> Omega7
=> RH.
```

Here

```text
RADICAL-PAIRING = PROLATE + WEIL-TAIL
```

in the normalized selected Cauchy pairing.  LP and IDENT alone do not close
Omega7.

## 2. Mandatory E77.7f Audit

E77.7d proves

```text
H_L=D_L+B_L,
D_L(n)=log(1+|n|)+O_L(1),
B_L bounded self-adjoint.
```

Therefore `(D_L-z)^(-1)` is compact and the resolvent identity should imply
compact resolvent for `H_L`.  If so, `mu_L=inf spec(H_L)` is an isolated
eigenvalue with an `l2` eigenvector.

This conflicts literally with the Phase-76 wording

```text
ker_l2(H_L-mu_L)=0.
```

E77.7f must resolve the conflict before any LP claim.  It must identify which
of the following is the actual SAFE-LIMIT-POINT input:

```text
uniqueness of a normalized inhomogeneous Weyl response;
contraction of bordered Weyl disks;
divergence of canonical energy at an isolated eigenvalue;
or triviality of a different rectangular homogeneous kernel.
```

No equivalence among these statements may be imported from scalar Jacobi
Weyl theory without matching the actual rectangular CCM variables.

## 3. Front A - Operational LP

### A1. Compact-Resolvent Theorem

Prove the resolvent identity at one `z<inf spec(H_L)`:

```text
(H_L-z)^(-1)
=(D_L-z)^(-1)
 [I+B_L(D_L-z)^(-1)]^(-1).
```

Conclude compact resolvent and discrete spectrum.  Repeat for the planted
build; this layer must be falsifier-neutral.

### A2. Correct Weyl-Disk Criterion

Restate LP in the exact bordered/rectangular topology used by P76.065.  Prove
the implication needed upstream:

```text
canonical energy divergence
=> Weyl-disk radius tends to zero
=> uniqueness of the selected safe Cauchy transform.
```

Only this direction is required.  Record and retract any false converse or
false homogeneous-kernel statement.

### A3. Fundamental Coupling Audit

Test the candidate reduction

```text
S_N(mu_L)->infinity
from nonzero coupling to the isolated ground mode.
```

The source is section-dependent.  E77.7f must determine whether there exists
an actual infinite `b in l2`, a convergent transported source, or only a
boundary functional.  The admissible target is named only after this audit.

If a stable coupling exists, prove its nonvanishing for both zeta and plant.
If it does not, reduce to the correct boundary-trace residue.  A numerical
overlap alone is a detector.

### A4. Shell Interface

After operational LP, prove

```text
SHELL-CAUCHY-GROWTH
=> RDP-SHELL.
```

Sources are paired with the selected Cauchy response before inversion or
absolute values.  No P76.061 ambient norm may enter.

## 4. Front B - IDENT

### B1. FIXED-L-WEYL

Use operational LP to prove finite Weyl-response convergence at each fixed
`L`.  Include the identification clause:

```text
finite sections -> intrinsic fixed-L m-function,
```

including the RFL-2 Fourier endpoint.  Convergence to an unidentified limit
does not count.

### B2. SAFE-GAMMA-IDENT

At `s=1/2+sigma>1`, identify the intrinsic derivative by the coupled
Gamma-prime/cell formula:

```text
G_L(sigma)
=lim_N [L coth(sigma L/2)
        +2 Re(i T'_{L,N}/T_{L,N})
        -B_ext,L,N].
```

Keep archimedean and prime pieces coupled until after the logarithmic
derivative is formed.

### B3. OUTER-LIMIT

Prove locally uniformly on safe compacta

```text
G_L(sigma)->2 Xi'(1/2+sigma)/Xi(1/2+sigma).
```

Use only absolute Euler convergence in `Re(s)>1`.  Integrate from the safe
normalization point after proving the derivative identity.

### B4. Cofinal Assembly

Apply the proved E77.6 diagonal lemma:

```text
fixed-L convergence + outer-L convergence
=> exists N(L)/L->infinity with SR-LOG-2SCALE
=> IDENT.
```

The plant must pass the finite algebra and fail SAFE-GAMMA-IDENT or
OUTER-LIMIT.  A break in generic diagonal glue is a ledger error.

## 5. Front C - Radical Pairings

Prove on the same compact exhaustion and in the selected pairing:

```text
PROLATE:    P_rows Q_W(k_lambda-k) -> 0,
WEIL-TAIL: P_rows(Q_{W,L}-Q_W)k -> 0,
FOURIER:   shell term -> 0 through RDP-SHELL.
```

At stage `m`, choose `L_m,N_m` large enough to satisfy IDENT and all three
paired errors simultaneously.  This uses the finite-additional-errors clause
of E77.6 and requires no joint rate formula.

## 6. Audits

### E77.8 - Falsifier Location

Run the assembled chain on zeta, the standard planted divisor, additional
plant depths, and the available DH-type control.

Expected location:

```text
plant passes operator realization and operational LP;
plant passes abstract diagonal selection;
plant fails SAFE-GAMMA-IDENT / OUTER-LIMIT.
```

If operational LP itself fails persistently for the plant, apply the E72.16
zero-filter gate before using that fact.

### E77.9 - Non-Circularity

Audit K1--K5, zero-filter, P76.061, MW-1--MW-6, no pseudoinverse, no ambient
inverse norm, no prime-by-prime positivity, and no absolute estimate before
the signed pairing.

## 7. Final Checklist

```text
[x] E77.7f compact resolvent and corrected LP ledger
[x] E77.7az attribution gate: shell-mismatch cascade = detector (Outcome A);
    BTG-DIV-L is falsifier-neutral; discriminant quarantined to IDENT
[ ] BTG-DIV-L => operational fixed-mu Weyl-disk contraction  (BUILD-NEUTRAL only)
[ ] operational fixed-mu Weyl-disk contraction
[ ] SHELL-CAUCHY-GROWTH => RDP-SHELL   (audit under E77.7az gate)
[ ] FIXED-L-WEYL with intrinsic identification
[ ] SAFE-GAMMA-IDENT
[ ] OUTER-LIMIT => IDENT through E77.6 diagonal
[ ] PROLATE + WEIL-TAIL in normalized pairing
[ ] E77.8 falsifier location
[ ] E77.9 non-circularity
[ ] E77.10 assembly => Omega7
```

**Phase status (2026-07-18):** Phase 77 CLOSED at 111 documents; see
`PHASE_77_CLOSURE.md`. All open items above handed to
`phase-78-build-neutral-lp-and-ident/`. The E77.7az gate archives the
E77.5d-5ah and E77.7aa-ay shell-mismatch branches as detectors: any LP step
that separates the zeta build from the plant by order one is inadmissible as
forcing (E72.16). The arithmetic discriminant lives in IDENT (front B).

## 8. Stop Rule

Every failed mechanism receives a theorem-grade autopsy naming the exact
coefficient, denominator, source, or topology that fails.  A replacement
target is admissible only with a proved implication to its predecessor.
Detector-only quantities are archived and not pursued as forcing mechanisms.
