# E67.5 — Modular/Woronowicz-character route for the prime current

**Date:** 2026-07-06.
**Role:** next modular vocabulary after the strict free-product Haar model was demoted by E67.4.
**Status update after E67.7:** Woronowicz characters alone do **not** escape the E67.4 no-go. They
identify the right modular data, but a Haar-weighted Cauchy-Schwarz estimate still gives an incoherent
`S_abs`-type ceiling unless an additional off-diagonal coherent state is supplied.

## Why a new channel is needed

The prime current needs two incompatible-looking features:

1. `P_lambda` is a coherent oscillatory linear sum over prime powers. It needs a Mellin/evaluation
   channel that preserves phases `n^{-it0}`.
2. `QSC-contract` needs a noncommutative Haar/Peter-Weyl mechanism, with quantum-dimension weights,
   strong enough to force a Schur bound.

Pure group-like/counit evaluation keeps 1 and loses 2.

Pure free-product Haar orthogonality keeps 2 and loses 1.

So a live candidate would have to be a **two-channel CQG object**:

```text
interference/evaluation channel  +  Haar/q-dimension control channel.
```

In compact quantum groups, the natural object with exactly this shape is the Woronowicz modular
character family.

## Woronowicz-character input

For a compact matrix quantum group with irreducible unitary corepresentation `u^alpha`, Woronowicz
theory supplies:

- a positive matrix `F_alpha`;
- quantum dimension `d_q(alpha)=Tr(F_alpha)=Tr(F_alpha^{-1})` after normalization;
- Haar orthogonality weighted by `F_alpha`;
- an analytic family of multiplicative functionals `f_z` whose values on matrix coefficients encode
  the modular data.

Schematic form:

```text
f_z(u^alpha_ij) = (F_alpha^z)_ij,
h((u^alpha_ij)^* u^beta_kl)
  = delta_alpha_beta * F_alpha-weighted constants / d_q(alpha).
```

The same matrix `F_alpha` controls both channels:

```text
f_z   -> Mellin/Euler phases and prime weights,
h     -> Haar/q-dimension orthogonality.
```

This is the right vocabulary for the missing bridge, but not yet the bridge itself. The matrix
`F_alpha` weights Haar orthogonality; it does not automatically create the off-diagonal arithmetic
coherence of `P_lambda`.

## Prime-local modular encoding

For each prime `p`, take a non-trivial compact matrix quantum group block with fundamental
corepresentation `u^(p)` and choose its modular matrix `F_p` so that one distinguished modular
eigenvalue is `p`:

```text
spec(F_p) contains p,
d_q(p) = Tr(F_p) = Tr(F_p^{-1}) after the CQG normalization.
```

Then Woronowicz evaluation gives the Mellin weight:

```text
f_{-s}(u^(p)_distinguished) ~ p^{-s}.
```

Prime powers are produced by convolution/tensor powers of the same modular character:

```text
f_{-s}((u^(p))^{tensor k}) ~ p^{-ks}.
```

The logarithmic Euler current is then:

```text
J_W(s)
  = -D_s sum_p log_cyc(1 - f_{-s}(u^(p)))
  = sum_{p,k>=1} (log p) p^{-ks} X_{p,k},
```

where `X_{p,k}` remains a noncommutative coefficient/trace in the Peter-Weyl block rather than a
group-like scalar.

The factor `Lambda(p^k)=log p` comes from differentiating the Woronowicz character evaluation, not from
fitting `P_lambda`.

## Candidate operator

At gauge `z0=t0-iy`, define

```text
B_lambda(z0,q)
  = sum_{p^k <= e^lambda}
      (log p) p^{-k/2}
      Phi_{t0,y,q}(X_{p,k})
      W_{k log p}
      arch_q(k log p; z0),
```

where:

- `Phi_{t0,y,q}` is the modular/Woronowicz evaluation channel, built from `f_z`;
- `W_{k log p}` is the Mellin shift on the Gamma_q archimedean module;
- `arch_q` is the already identified Gamma_q/Plancherel carrier;
- the Haar state `h` is **not** used to erase the phase sum, but to bound the coefficient norms through
  `F_p` and `d_q(p)`.

## Reformulated QSC gates, before the E67.7 correction

### QSC-exist-W

Show that the modular evaluation channel gives the exact prime Pick jet:

```text
P_lambda
 = lim_{q->1} PickGram(B_lambda)
```

without choosing coefficients from `P_lambda`.

This is plausible because the Woronowicz character evaluation already produces

```text
p^{-s}, p^{-2s}, ..., p^{-ks}
```

and the logarithmic derivative produces `Lambda(p^k)=log p`.

### QSC-contract-W

The original hope was: show that the same `F_p` matrices imply a Schur bound:

```text
B_lambda^* B_lambda <= I
```

by a modular Cauchy-Schwarz / Peter-Weyl inequality of the form

```text
|Phi_{t0,y,q}(X)|^2 <= C(t0,y,q) * h(X^* F_p X) / d_q(p),
```

with the Gamma_q archimedean normalization making `C <= 1` after whitening.

E67.7 shows that this is still too weak. Summed over prime powers, such a Haar Cauchy-Schwarz bound is
blind to phase cancellation and returns the incoherent ceiling unless the right-hand side retains
off-diagonal terms.

The required replacement is a coherent modular state `omega_{z0,q}` and a Haar-dominating density
`D_{z0,q}`:

```text
omega_{z0,q}(X_a^*X_b)  reproduces arithmetic off-diagonal phases,
|omega_{z0,q}(Y)|^2 <= h(Y^* D_{z0,q} Y),
```

with `D_{z0,q}` canonical and zeta-free.

## New kill-tests

### W1 — modular coefficient source

Does `f_{-s}` on the chosen prime block produce `p^{-s}` canonically from `F_p`, with no scalar
post-fit?

### W2 — Pick reproduction

Using `Phi_{t0,y,q}` rather than Haar expectation, does the current reproduce the linear oscillatory
`P_lambda` entries?

### W3 — Haar bound

Using the same `F_p`, does Haar/Peter-Weyl give a contractive bound that is not the group-like baseline
and not the incoherent `S_abs` ceiling?

### W4 — DH falsifier

Can DH be assigned compatible modular matrices `F_p` with an Euler logarithm and the same Haar bound?
Expected: no, because DH lacks the prime-local Euler factorization.

## Current status

This route is no longer sufficient by itself. The corrected live formulation is:

```text
Euler/Mellin data from Woronowicz characters;
off-diagonal interference from a coherent modular state omega_{z0,q};
contractivity from Haar domination of omega by a canonical density D_{z0,q}.
```

The remaining problem is sharply localized:

```text
construct omega_{z0,q} and D_{z0,q} without zeta/P_lambda,
then prove the modular domination inequality strong enough to imply Omega_7.
```

That is a real mathematical statement, not a rephrasing of `delta_N >= 0`.

## Source anchors

- Woronowicz compact matrix quantum group theory supplies the dense Hopf-* algebra of matrix
  coefficients, Haar state, Peter-Weyl orthogonality, and the canonical character family `f_z`.
- Banica's free unitary compact quantum group gives a concrete non-Kac compact matrix quantum group
  family where the fundamental corepresentation, fusion rules, Haar state, and Woronowicz characters
  are explicit enough for a finite-prime test.
- The general compact quantum group modular theory records that the Haar state is KMS in the non-Kac
  case; this is the analytic home of the `F_p` modular matrices used above.
