# E73.214 - Bernoulli remainder lemma for the entry tail

Date: 2026-07-14.

## 1. Purpose

E73.210--E73.213 use a Bernoulli next-term style bound for the `psi/psi_1`
tail.  This note isolates the exact analytic lemma needed to make that step
fully proof-facing.

## 2. Required lemma

Let

```text
z=R+1/4-iomega/2,       R>=80,
```

where `omega` is one of the finite matrix frequencies `2pi m/L`.  For every
frequency in the Phase 73 finite windows, `Re z>=80`.

The proof-facing bound may include a fixed sector constant `C_sec`.  It is
sufficient to prove:

```text
|R_K^psi(z)| <= C_sec |B_{2K}|/(2K |z|^(2K)),

|R_K^psi1(z)| <= C_sec |B_{2K}|/|z|^(2K+1),
```

where

```text
psi(z)=log z -1/(2z)-sum_{k=1}^{K-1} B_{2k}/(2k z^(2k)) + R_K^psi(z),

psi_1(z)=1/z+1/(2z^2)+sum_{k=1}^{K-1} B_{2k}/z^(2k+1) + R_K^psi1(z).
```

In the numerical certificate E73.213 has about `10^7` slack in this component,
so any moderate absolute `C_sec` is harmless.

## 3. Proof route

Use the standard Binet/Stirling integral remainder for the logarithmic Gamma
expansion:

```text
log Gamma(z)
=(z-1/2)log z-z+1/2log(2pi)
 +sum_{k=1}^{K-1} B_{2k}/(2k(2k-1)z^(2k-1))
 +Rem_K(z),
```

with `|arg z|<=pi/2-epsilon` in our region.  More explicitly, for
`Re z>0` one may write the differentiated remainders using the periodic
Bernoulli polynomial:

```text
R_K^psi(z)
= - int_0^infty B_{2K}({t})/(t+z)^(2K+1) dt,

R_K^psi1(z)
= (2K+1) int_0^infty B_{2K}({t})/(t+z)^(2K+2) dt,
```

up to the conventional normalization matching the displayed Bernoulli
coefficients.  Since the whole ray `t+z` lies in the right half-plane and
`Re z>=80`,

```text
|t+z| >= (t+|z|)/sqrt(2)
```

for the present sector.  The periodic Bernoulli polynomial is bounded by a
constant multiple of `|B_{2K}|`.  Integrating the resulting majorant gives the
sectorial form above with an absolute `C_sec`.

Equivalently, cite the classical uniform asymptotic expansion of `psi` and its
derivative in sectors `|arg z|<=pi-delta`, specialized to the right half-plane.

## 4. Load-bearing use

With `R=80,K=16`, the proof-facing certificate uses this lemma only through:

```text
R_digamma
<= sum |c_omega| Rad(D_1(R,omega))
 + sum |l_omega| Rad(D_2(R,omega)).
```

E73.216 shows that `K=16` tolerates a sector constant of about `10^17` in the
tested windows.  Thus constant inflation in the formal Bernoulli remainder
bound does not threaten the certificate.

## 5. Status

```text
isolated: sectorial Bernoulli remainder lemma needed by BALL-ENTRY-CERT;
robust: certificate survives large fixed constants by increasing K if needed;
open: insert final citation/normalization convention in proof writeup.
```
