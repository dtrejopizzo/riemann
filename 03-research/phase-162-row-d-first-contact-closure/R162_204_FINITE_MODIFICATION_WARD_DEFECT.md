# R162_204 — Finite-modification Ward defect and where arithmetic must enter


Status: **PROVED CALIBRATION / GATE 1 OPEN.** The critical value of the product-regularised port does
not itself distinguish `Lambda` from a finite modification. The distinction occurs one step earlier,
in the divisor defect of the finite Poisson--Chebyshev identity. Consequently, a valid Gate-1 proof
must annihilate the critical value through a defect-free finite identity; it cannot infer arithmetic
specificity from the final evaluation at a zero.

## 1. General coefficient system

Let

    a=Lambda+eta,

where `eta` has finite support, and put

    A_a(s)=sum_(n>=1)a(n)n^(-s),
    E_eta(s)=sum_(n>=1)eta(n)n^(-s).                             (1.1)

In `Re s>1`,

    A_a(s)=-zeta'(s)/zeta(s)+E_eta(s).                           (1.2)

The failure of the convolution law `Lambda*1=log` is

    b_a:=a*1-log=eta*1.                                         (1.3)

Its Dirichlet series is

    B_a(s):=sum_(n>=1)b_a(n)n^(-s)
           =zeta(s)E_eta(s)
           =zeta(s)A_a(s)+zeta'(s).                             (1.4)

Formula (1.4) is an exact Ward-defect identity. For `a=Lambda`, `B_a=0`; for a nonzero finite
modification, `b_a` is supported on infinitely many multiples even though `eta` itself is finite.

## 2. Product port under finite modification

For the same compact source `F`, let the oriented current associated with `a` have the form

    H_a(z)=A_a(s)K_F(z)-Q_a(z),          s=1/2+z,                (2.1)

where `Q_a` is entire. Its product regularisation is

    G_a(z)=zeta(s)H_a(z)
          =-zeta'(s)K_F(z)+B_a(s)K_F(z)-zeta(s)Q_a(z).           (2.2)

This is just (1.4), with no limiting Euler product on the critical line.

**Theorem 2.1 (finite-modification invariance of the critical jet; PROVED).** If
`rho=1/2+i gamma` is a simple zero of zeta, then for every finite modification `a=Lambda+eta`,

    G_a(i gamma)=-zeta'(rho)K_F(i gamma).                        (2.3)

*Proof.* The Dirichlet polynomial `E_eta` is entire, hence (1.4) gives
`B_a(rho)=zeta(rho)E_eta(rho)=0`. Also `zeta(rho)Q_a(i gamma)=0`. Evaluating (2.2) proves (2.3). ∎

For a zero of order `m`, the coefficient of order `m-1` is likewise unchanged: both modification
terms in (2.2) contain `zeta` and vanish to order at least `m`.

## 3. Consequence for the falsifier test

The final implication

    G_a(i gamma)=0  =>  K_F(i gamma)=0                           (3.1)

cannot distinguish `Lambda` from a finite modification: its left side has the same critical jet in
both systems. Therefore the requirement that the proof fail for a finite modification must be
enforced **before** critical evaluation.

The only new arithmetic datum visible there is `B_a`, equivalently the coefficient defect `b_a` in
(1.3). In a finite `(PC-ren)` calculation, it is the interior divisor error left after replacing
`a*1` by `log`. It vanishes identically for `Lambda` and is nonzero on infinitely many multiples for
every nontrivial finite modification.

This rules out a broad class of candidates: no argument depending only on

- the functional equation;
- Sonin membership of the completed port;
- the final value `G_a(i gamma)`;
- or a local estimate made only after multiplication by zeta

can pass the finite-modification falsifier. Such an argument sees (2.3), which is modification
invariant.

## 4. Required form of a closing identity

Let `J(F)` denote the critical-jet vector

    J(F)=(zeta'(rho)K_F(rho-1/2))_(rho simple, Re rho=1/2),      (4.1)

in any fixed summable normalization. A noncircular finite identity capable of closing Gate 1 must
have the schematic, but falsifiable, form

    ||J(F)||^2 + E_phys(F)
      = R_first-contact(F) + D_a(F),                             (4.2)

where all four terms are obtained before the critical-line limit and:

1. `E_phys(F)>=0` is a genuine exterior/polar--Tate square;
2. `R_first-contact(F)=0` follows from the radical equation, not from residue removability;
3. `D_a(F)` is built from the divisor defect `b_a=a*1-log` and therefore `D_Lambda(F)=0`;
4. for a finite modification, `D_a` is retained and has no forced sign or vanishing;
5. for Davenport--Heilbronn data, (1.4) has no prime-Euler realization, so (4.2) is not available.

For `a=Lambda`, (4.2) would give `J(F)=0` and close Gate 1. For a modified system it would not do so,
because the infinite-multiple defect survives on the right. This is the first location at which both
falsifiers can be separated while the terminal jet remains the correct one.

Equation (4.2) is **not proved here**. Its purpose is to fix the algebraic type of the missing identity
more tightly than “prove residue zero.” Any proposed Green identity that has no explicit `b_a` slot
cannot be the missing argument, even if all its formulas are correct for zeta.

## 5. The next calculation

Start with the finite rectangle identity before imposing `a*1=log`. Write every occurrence of the
hyperbola coefficient as

    (a*1)(k)=log k+b_a(k).                                      (5.1)

Then perform the two-orientation mixed Green pairing, retaining:

- the `log k` contribution as the covariant critical jet of R161_036;
- the `b_a(k)` contribution as `D_a(F)`;
- the continuum polar layer and both crossed Tate endpoints;
- the right/left exterior compression before any scalar trace.

The decisive question is whether the remaining `log k` Green term is exactly `||J(F)||^2` plus a
nonnegative exterior square. If it is, (4.2) is proved. If it is merely the symmetric completed
commutator, the calculation has returned to the known cancellation `(-c,+c)` and must be rejected.

## 6. Exact status

- Ward-defect identity (1.4): **PROVED**;
- invariance of the critical jet under finite modifications (2.3): **PROVED**;
- location at which the finite-modification falsifier must act: **PROVED**;
- closing Green identity (4.2): **OPEN**;
- Gate 1 and row D: **OPEN**.
