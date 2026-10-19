# R162_201 — Global Euler stripping as a finite Hardy criterion for the Sonin range


Status: **NEW SUFFICIENT CRITERION / GATE 1 STILL OPEN.** This note replaces the abstract phrase
"physical co-Poisson range" by a concrete uniform estimate for finite Euler products. The estimate
is not proved from first contact. If it can be obtained from the oriented finite `(PC-ren)` identity,
it annihilates the Gamma moments and closes Gate 1.

The construction is global: every prime enters before a limit is taken. It is therefore not
refuted by R162_103's first-chamber models, whose local `2,3,4` data cannot see the infinite divisor
defect.

## 1. Finite Euler stripping on the causal Hardy space

Let `G=G_(+,T)^0` be the corrected right product port of R161_008–R161_012 and put

    ghat(z)=exp(Tz)G(z),              Re z>0.

For a first-contact source, `ghat` belongs to `H2(C_+)`. For `Y>=2` define the finite inverse Euler
multiplier

    A_Y(z)=product_(p<=Y) (1-p^(-1/2-z)),
    h_Y(z)=A_Y(z) ghat(z).                                      (1.1)

Each `A_Y` is a bounded analytic multiplier of `H2(C_+)`; no infinite Euler product has yet been
used. In physical coordinates on `L2(0,infinity)`, multiplication by one new factor is

    h_(Y union {p})=(I-r_p S_(log p))h_Y,
    r_p=p^(-1/2),                                               (1.2)

where `S_a` is the unilateral delay, `(S_ah)(t)=1_(t>=a)h(t-a)`.

## 2. Uniform stripping forces all critical jets to vanish

**Theorem 2.1 (Euler-stripping Hardy criterion; PROVED).** Assume

    sup_(Y>=2) ||A_Y ghat||_(H2(C_+)) < infinity.                (2.1)

Then `G(i gamma)=0` at every critical-line zero `rho=1/2+i gamma` of zeta. At every simple such
zero,

    K_F(i gamma)=0.                                             (2.2)

Consequently, for a first-contact source in the phase-121 regularity class, `F=0`.

*Proof.* Exhaust the primes in increasing order. The bounded sequence `h_Y` has a weakly
convergent subsequence in `H2(C_+)`, say with limit `h`.
Point evaluation is a continuous functional on this Hardy space. For `Re z>1/2`, hence
`Re(1/2+z)>1`, the ordinary Euler product converges and gives

    A_Y(z) -> 1/zeta(1/2+z).

Therefore

    h(z)=ghat(z)/zeta(1/2+z)       for Re z>1/2.                 (2.3)

Analytic continuation makes (2.3) valid throughout `C_+` away from the zeros of zeta there; in
particular the quotient has an `H2(C_+)` extension.

Let `z_0=i gamma` be a boundary zero of zeta of order `m>=1`. The corrected numerator `ghat` is
holomorphic across `z_0` (the pole at `s=1` was removed separately). If `ghat` vanished there to
order `k<m`, then along `z=z_0+x`, `x>0`, equation (2.3) would give

    |h(z_0+x)| asymp x^(k-m).

But every `H2(C_+)` function satisfies the point-evaluation bound

    |h(x+iy)| <= C x^(-1/2)||h||_H2.

Since `m-k>=1`, the two estimates are incompatible as `x->0+`. Hence `ghat`, and therefore `G`,
vanishes to order at least `m` at `z_0`. For a simple critical zero, R161_007 gives

    G(i gamma)=-zeta'(rho)K_F(i gamma),

so (2.2) follows. The unconditional superlinear family of simple critical zeros, together with the
phase-121 Cartwright uniqueness theorem for the compactly supported source transform `K_F`, forces
`K_F` and then `F` to vanish. ∎

**Remark 2.2.** The theorem needs no claim that the divergent Euler product converges on the critical
line. It uses only finite products, weak compactness in `H2`, and ordinary Euler convergence in
`Re s>1`, followed by Hardy boundary growth. This is why the order of limits is legitimate.

## 3. Exact prime increment and the missing estimate

For `h in L2(0,infinity)` and `a=log p`, equation (1.2) gives

    ||(I-r_pS_a)h||^2
      =(1+r_p^2)||h||^2-2r_p Re<h,S_ah>.                        (3.1)

There is no sign in (3.1). The local oriented defect is nevertheless exactly positive:

    ||(I-r_pS_a)h||^2-||(I-r_pS_a^*)h||^2
      =r_p^2||1_[0,a)h||^2.                                    (3.2)

Indeed `S_a^*S_a=I` and `S_aS_a^*=I-P_[0,a)`. Formula (3.2) is the elementary version of the
Brown–Halmos Euler-factor square audited in R161_045. Its right side is the literal first collar.

The new finite target is therefore:

> **ESB (Euler stripping bound; OPEN).** For the corrected product port of a primitive first-contact
> state, prove (2.1), uniformly over the directed family of finite prime sets, from the two oriented
> finite `(PC-ren)` histories with the continuum polar and crossed Tate terms retained.

Unlike the former "return inequality", ESB is a genuine finite exhaustion statement: for a general
nonzero Hardy function the norms in (2.1) need not be uniformly bounded. Theorem 2.1 proves that ESB
has the required arithmetic consequence, but does not derive ESB.

## 4. Relation with the Sonin range-intersection gate

The typed scattering equation places `G` in the parity Sonin space after logarithmic reflection.
Theorem 2.1 shows

    Sonin membership + ESB  =>  G(i gamma)=0 on the critical simple family  =>  F=0.  (4.1)

In fact Sonin membership is not used in the analytic proof of Theorem 2.1; it is expected to be
load-bearing only in deriving ESB from the two oriented physical histories. Thus the open
intersection lemma R161_011 (4.2) has been sharpened to a concrete question: does its product-port
range satisfy the uniform finite-prime estimate (2.1)?

This is one-sided and stronger than formal meromorphic divisibility. It is also compatible with
R161_012: an `H2` quotient by zeta is precisely a physical range certificate, while a formal
quotient with poles at critical zeros is not.

## 5. Falsifier audit

- **F1 (spectral).** Theorem 2.1 is source-independent, but ESB is asserted only as an open
  equality-state consequence. No estimate has been claimed for positive eigenvectors. A derivation
  must still use the first-contact oriented equation non-perturbatively.
- **F2 (orientation).** Squaring `(PC)` does not imply ESB. Formula (3.2) shows exactly which
  same-history adjoint comparison is required; R161_045 proves that the known undifferentiated
  transport has the wrong tangent. This obstruction is retained, not hidden.
- **F3 (arithmetic).** The implication in Theorem 2.1 uses the full Euler product in `Re s>1`.
  Davenport–Heilbronn has no corresponding prime exhaustion. For a finite modification of Lambda,
  the finite PC identity acquires an interior divisor defect supported on infinitely many multiples;
  a derivation of ESB from the defect-free oriented histories must fail there. Merely applying the
  zeta factors `A_Y` to an arbitrary model port proves nothing: the missing statement is the uniform
  bound.
- **F4 (linear limit).** ESB is a uniform quadratic bound before the prime limit, not the linear
  graph limit excluded by R161_018.

## 6. Exact status

- finite Euler stripping operators and prime increment (3.1): **PROVED**;
- positive adjoint defect (3.2): **PROVED**;
- uniform bound (2.1) implies critical-jet and Gamma-moment annihilation: **PROVED**;
- ESB from first contact + oriented `(PC-ren)`: **OPEN**;
- Sonin range-intersection and Gate 1: **OPEN**;
- row D: **OPEN**.

The next calculation is no longer to prove an abstract sign for `Q`. It is to expand the finite
prime exhaustion of the two actual Sonin histories and decide whether their crossed polar/Tate
Green identity gives a telescoping upper bound for `||A_Y ghat||_H2`.
