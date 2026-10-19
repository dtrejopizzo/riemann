# R161_024 — Gamma-pole removability is enough; global scattering is unnecessary

## 0. Verdict

The Gamma-pole rigidity of `R161_019` needs much less than physical scattering. It is enough to prove that the
corrected functional-equation defect

```
W_epsilon^0(s)
 =d_Gamma(s)K_F(s-1/2)-Q_+(s-1/2)-Q_-(s-1/2)
  -Theta_+(s)-Theta_-(s)                                       (0.1)
```

has removable singularities at

```
s=3,5,7,... .                                                    (0.2)
```

No vanishing of `W_epsilon^0`, no cosine eigenrelation on the critical line, and no global causality theorem is
needed. Removability alone forces the complete exponential-moment lattice and hence `F=0`.

This is a genuine weakening of L161.4--L161.6. The terminal source problem may now be attacked entirely in the
zero-free safe half-plane `Re s>1`.

## 1. Removable-pole rigidity

Recall

```
d_Gamma(s)
 =-log pi+(1/2)psi((1-s)/2)+(1/2)psi(s/2).                       (1.1)
```

At `s_m=2m+1`, `m>=1`, it has a simple pole with nonzero residue. The functions `Q_+` and `Q_-` are entire in
`s-1/2`, while the canonical Hardy corrections have possible finite poles only at `s=0,1`. Thus every term in
(0.1), except `d_Gamma K_F`, is holomorphic at `s_m`.

**Theorem 1.1 (removability criterion; PROVED).** If `W_epsilon^0` is holomorphic at every `s_m=2m+1`, `m>=1`, then
`F=0` almost everywhere.

*Proof.* Taking the residue of (0.1) at `s_m` gives

```
0=Res_(s=s_m)d_Gamma(s) K_F(s_m-1/2).
```

The residue of `d_Gamma` is nonzero, so

```
K_F(2m+1/2)=0,       m=1,2,3,... .                              (1.2)
```

Theorem 3.1 of `R161_019` proves that these moments are complete on every finite window: after `x=e^(-2t)`, they
are the moments of a weighted copy of `F` against `x^m`, `m>=1`, on a compact interval separated from zero.
Therefore `F=0`. ∎

Only removability at the discrete set (0.2) was used.

## 2. Equivalent product-port formulations

The exact defect identity is

```
G_+^0(s)+chi(s)G_-^0(s)=zeta(s)W_epsilon^0(s).                  (2.1)
```

Since `zeta(2m+1)` is finite and nonzero, removability of `W_epsilon^0` at `s_m` is equivalent to removability of the
left side of (2.1) there. The right port `G_+^0` is already holomorphic at every `s_m`. Hence the condition is also
equivalent to removability of

```
chi(s)G_-^0(s)                                                    (2.2)
```

at those points.

The factor `chi` has a simple pole at `s_m`. The reflected port is holomorphic there, so (2.2) is removable exactly
when

```
G_-^0(2m+1)=0.                                                   (2.3)
```

At `1-s_m=-2m`, the zeta function has a simple trivial zero and its derivative is nonzero. The correction terms are
multiplied by that zero. Consequently (2.3) again reduces to (1.2).

Thus the terminal statement has three exactly equivalent safe-half-plane forms:

```
W_epsilon^0 removable at every positive odd Gamma pole;
chi G_-^0 removable there;
the reflected product port vanishes at the corresponding trivial zeros.
```

## 3. Why boundary unitarity does not prove removability

The support commutator suggested after `R161_023` is the Hankel block

```
(I-P_+)M_chi P_+=[P_+,M_chi]P_+.                                (3.1)
```

Phase 114 (`114_d_234_CAUSAL_SCATTERING_AUDIT.md`) proves that its vanishing is causality/innerness of the completed
scattering multiplier. Boundary unitarity follows from the functional equation, but innerness is the missing
zero-free information and cannot be assumed. The phase-120 signed Green identity likewise supplies a first-order
indefinite conservation law, not removability of one oriented polar datum.

Therefore Theorem 1.1 does not license a formal Hardy continuation from the critical line. Its gain is different:
the finite `(PC)` construction only needs to control a discrete family of germs in the already zero-free half-plane,
not a global Hardy block.

## 4. The new finite target

For each `m>=1`, let `s_m=2m+1`. Every finite Dirichlet polynomial and hyperbola remainder in `(PC)` is holomorphic
near `s_m`; all possible poles come from the Fourier/Gamma and polar-continuum pieces. This suggests the exact
finite acceptance target:

> **L161.7 (safe-half-plane pole annihilation; OPEN, superseded in its linear form by L161.8).** For a primitive
> first-contact state, expand the two oriented finite `(PC-ren)` germs near `s=s_m` before recombining them. Prove
> that the coefficient of the Gamma pole vanishes for every `m>=1`.

Equivalently, prove directly from the finite identity that the limiting germ `zeta W_epsilon^0` is holomorphic at
every `s_m`.

This target has strict noncircularity tests:

1. the calculation occurs in `Re s>1`, so no division across a critical zero is involved;
2. it must display and annihilate the residue coefficient before taking a critical-line boundary value;
3. it may use the exact first-contact equation and the crossed Tate coefficients, but not global scattering,
   causality, or `X_T=0`;
4. local uniform/graph convergence near each `s_m` must be proved; pointwise convergence away from the pole is not
   enough to infer removability.

## 5. Collision with the old large-moment route

Testing the first-contact equation directly against `exp(-(2m+1/2)t)` does not prove L161.7. The phase-121
large-Gamma-moment audit shows that translated collar cells cancel the apparent contracting factor and leave the
depth-zero transport block unchanged. L161.7 must therefore use the simultaneous Poisson/Fourier residue in `(PC)`,
not merely the scalar first-contact equation paired with high exponentials.

## 6. Closure chain

If L161.7 is proved, then

```
finite PC residue cancellation
 -> W_epsilon^0 removable at s=3,5,7,...
 -> K_F(5/2)=K_F(9/2)=...=0
 -> F=0
 -> no first contact
 -> row D.
```

The compressed scattering and extremal-correlation results remain valid sufficient routes, but are no longer
necessary for closure.

## 7. Status

- removability at the positive odd Gamma poles implies `F=0`: **PROVED**;
- equivalence with reflected-port vanishing at the trivial-zero lattice: **PROVED**;
- support-commutator/innerness shortcut: **REJECTED AS CIRCULAR by the existing audit**;
- direct high-exponential testing: **REJECTED by the phase-121 moment audit**;
- safe-half-plane residue cancellation from finite `(PC-ren)` L161.7: **OPEN**;
- row D: **OPEN**.

**Successor audit.** `R161_025` computes the exact residue and proves that mere finite holomorphy or a linear graph
limit cannot yield removability. The surviving version is the quadratic Gamma-residue energy L161.8.

**Correction.** Since every non-Gamma term of `W_epsilon^0` is holomorphic at the positive odd poles, there is no
second Laurent residue available to cancel the Gamma residue. “Cancellation by the continuum/Tate residue” was an
incorrect description. The required statement is annihilation of its coefficient `K_F(2m+1/2)` by an independent
equality-state law.
