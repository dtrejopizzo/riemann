# E101.076 - Jet, Wronskian, literature and parity gate

## 1. Decision

E101.075 derives the exact source-jet response but leaves open whether a
Wronskian or a family of derivative inequalities can remove the critical-line
background.  The answer divides sharply into three classes.

```text
linear jet channels:
  classical confluent evaluation and parity-sensitive, but they retain the
  complete zero background;

holomorphic Wronskians and derivative inequalities:
  classical Laguerre--Polya or Jensen criteria, and therefore RH-equivalent
  when imposed with the strength needed here;

sesquilinear full-jet quantities:
  capable of vanishing pointwise on the real axis without vanishing
  identically, and not covered by the scalar-radical no-go.              (1.1)
```

The first two classes are imported and frozen.  They do not provide a new
route to Omega7.  The only unabsorbed possibility is a source-first,
sesquilinear jet current which uses conjugation to distinguish real from
nonreal points, is positive on every off-line quartet, and is then realized
without spectral input in the finite arithmetic model.

This document proves the parity and factorization gates and records the exact
primary-literature boundary before that nonlinear construction is attempted.

## 2. Coordinate convention

Let

```text
Xi(z)=integral_R k(t)exp(-izt)dt.                  (2.1)
```

The variable `t` is the additive logarithmic coordinate.  In the original
multiplicative coordinate `u`, it is `t=log u`.  Consequently,

```text
F[t^r k](z)=i^r Xi^((r))(z),                       (2.2)
```

whereas powers of the translation generator satisfy

```text
F[(-i partial_t)^r k](z)=z^rXi(z).                 (2.3)
```

Thus `(log u)^r k(u)`, not `u^r k(u)`, is the multiplicative form of the
position jet.  Equation (2.2) is the jet channel; equation (2.3) is a
reversible radical channel.

## 3. Exact parity of a linear quartet jet

The Riemann function is real entire and even:

```text
Xi(-z)=Xi(z),
Xi(conj z)=conj Xi(z).                             (3.1)
```

Hence

```text
Xi^((r))(-z)=(-1)^rXi^((r))(z),
Xi^((r))(conj z)=conj Xi^((r))(z).                 (3.2)
```

Let `Phi` be a real entire test of parity `epsilon in {+1,-1}`:

```text
Phi(-z)=epsilon Phi(z),
Phi(conj z)=conj Phi(z).                           (3.3)
```

For a nonreal point `zeta`, define its symmetric quartet

```text
P_zeta={zeta,-zeta,conj zeta,-conj zeta}           (3.4)
```

and the order-`r` linear jet response

```text
J_(r,epsilon)(zeta;Phi)
=sum_(p in P_zeta)Xi^((r))(p)Phi(p).               (3.5)
```

### Theorem 3.1 - Parity reduction

One has

```text
J_(r,epsilon)(zeta;Phi)
=2[1+epsilon(-1)^r]
 Re{Xi^((r))(zeta)Phi(zeta)}.                      (3.6)
```

### Proof

Pair `zeta` with `-zeta`.  Equations (3.2)--(3.3) give

```text
Xi^((r))(-zeta)Phi(-zeta)
=epsilon(-1)^rXi^((r))(zeta)Phi(zeta).             (3.7)
```

The conjugate pair is the complex conjugate of (3.7) together with the
unshifted term.  Adding both pairs gives (3.6). `QED`

### Corollary 3.2

```text
even tests annihilate every odd jet quartet;
odd tests annihilate every even jet quartet.        (3.8)
```

At a simple zero the first nonzero jet has order one.  Therefore the
canonical even channel is blind to it.  Passing to an odd test repairs that
parity cancellation but does not remove the contributions of the critical
zeros.  At a zero of unknown multiplicity `nu`, the first nonzero order is
`nu`, so a single fixed parity cannot cover all multiplicities.

Keeping both parities is legitimate infrastructure.  It is not a
critical-line discriminator.

## 4. Two holomorphic atomwise no-go statements

### Proposition 4.1 - Node-blind real-axis filter

If an entire function `H` satisfies

```text
H(x)=0 for every real x,                            (4.1)
```

then `H` is identically zero.

### Proof

The real axis contains accumulation points in the domain of `H`; the
identity theorem applies. `QED`

Therefore a holomorphic weight fixed independently of the real zero
locations cannot annihilate every possible on-line atom and retain a
nonreal atom.  Exact real-axis discrimination must use conjugation,
nonholomorphic dependence, or a global relation tied to the actual divisor.

### Proposition 4.2 - Complete-divisor radical factorization

Let `F` be entire.  If `F` vanishes at every zero of `Xi` with at least the
same multiplicity, then

```text
F=Xi G                                               (4.2)
```

for an entire function `G`.

### Proof

The quotient `F/Xi` is holomorphic off the divisor.  The multiplicity
hypothesis makes every apparent pole removable. `QED`

On a test module stable under multiplication by `G`, equation (4.2) is the
original radical with a transformed test.  This eliminates a second
holomorphic radical but does not eliminate a sesquilinear quantity involving
both a jet and its conjugate.

The two propositions expose the relevant dichotomy:

```text
holomorphic and node-blind  => identically zero;
holomorphic on the full divisor => divisible by Xi;
real-axis selective and nontrivial => necessarily nonholomorphic or
                                      globally spectral.               (4.3)
```

## 5. Confluent evaluators are classical

Burnol constructs derivative evaluators

```text
Y_(rho,k), 0<=k<m_rho,                              (5.1)
```

which recover the `k`-th Mellin derivative at a zeta zero of multiplicity
`m_rho`.  The dual system is generated, up to triangular changes inside each
confluent block, by

```text
zeta(Z)/(Z-rho)^ell,
1<=ell<=m_rho.                                      (5.2)
```

For a simple zero, the residue interpolation coefficient contains

```text
G(rho)/zeta'(rho).                                  (5.3)
```

This has two consequences for the present program.

```text
the algebra of multiplicity jets and confluent Cauchy blocks is not new;

the dual system (5.2)--(5.3) is not source-first, because it requires rho,
m_rho and derivative data at the zero.                              (5.4)
```

The internal counterparts are E72.324--E72.325 and E72.357.  Their block
invertibility separates prescribed Hermite slots, but does not produce a
nonzero value on the actual terminal row and does not control its tail.

## 6. The first Wronskian is a known Laguerre quantity

For a real entire function `F`, define

```text
L_1(F;x)=F'(x)^2-F(x)F''(x), x real.                (6.1)
```

It is the negative Wronskian

```text
L_1(F;x)=-W(F,F')(x).                               (6.2)
```

At a simple zero `rho`,

```text
L_1(F;rho)=F'(rho)^2.                               (6.3)
```

Thus the first derivative Wronskian responds at real and nonreal simple
zeros alike.  It contains no mechanism which cancels the critical-line
background.

The real-axis inequalities

```text
[F^((j))(x)]^2-F^((j-1))(x)F^((j+1))(x)>=0         (6.4)
```

are necessary for the Laguerre--Polya class but the elementary family (6.4)
alone is not the missing sufficient theorem.

The complex Jensen quantity is

```text
J_F(z)=|F'(z)|^2-Re{F(z)conj(F''(z))}.              (6.5)
```

For the standard real-entire genus class containing `Xi`, the Jensen
criterion states

```text
J_F(z)>=0 for every complex z
  <=> F belongs to the Laguerre--Polya class.        (6.6)
```

For `F=Xi`, (6.6) is equivalent to RH.  Therefore proving the global sign of
the obvious radical--jet Wronskian is not an intermediate estimate; it is
the entire force-bearing step.

## 7. The root-free two-channel correlation is also known

Dimitrov--Xu express derivative Wronskians of a Fourier transform as Fourier
transforms of correlation kernels.  For the Riemann kernel `Phi`, their
order-two kernel is

```text
Phi_(2,y)(t)
=cosh(ty) integral_R (t-2s)^2 Phi(t-s)Phi(s)ds.     (7.1)
```

They prove the equivalence

```text
RH
<=> for every fixed 0<|y|<1/2, the translates of Phi_(2,y)
    are dense in L^1(R).                             (7.2)
```

They also show that including `y=0` in the density statement detects real
and simple zeros, which is stronger than RH.

Equation (7.1) is already a root-free, quadratic, two-channel expression
built entirely from the Riemann Fourier kernel.  Consequently, merely
introducing a correlation, a Wronskian, or translation density cannot count
as a new discriminant.  The new content would have to prove the density or
an equivalent noncancellation from the finite Gamma--Euler/CCM structure.

The internal hyperbolic-pair Wronskian of E72.372 has the same logical
boundary: the divided difference removes a denominator exactly, while the
weighted sampling theorem `HPAIR` remains open.

## 8. Jensen, Turan and higher Laguerre hierarchies

Write the centered Taylor series as

```text
psi(z)=xi(1/2+z)=sum_(n>=0)gamma(n)z^(2n)/n!       (8.1)
```

and define

```text
J^((d,n))(X)
=sum_(j=0)^d binom(d,j)gamma(n+j)X^j.              (8.2)
```

The Polya--Jensen criterion gives

```text
RH <=> J^((d,n)) is hyperbolic for every d,n.       (8.3)
```

For every fixed degree `d`, hyperbolicity is already known for all
sufficiently large shifts `n`; effective results cover very large finite
regions.  These theorems arise from universal Hermite asymptotics of high
derivatives.  They do not control all pairs `(d,n)`, and no converse from the
eventual fixed-degree regime to the original zero set is available.

Similarly, higher Turan and generalized Laguerre inequalities are known in
large-shift regimes.  Requiring every order at every shift characterizes the
Laguerre--Polya class and returns to (8.3).  Proving any fixed order, or every
fixed order only eventually, is compatible with off-line zeros and cannot
imply Omega7.

Therefore the following moves are frozen:

```text
another fixed-degree Jensen polynomial;
another finite Turan determinant;
large-shift Hermite asymptotics;
finite or eventual Laguerre inequalities;
an all-order hierarchy assumed without a new propagation theorem.     (8.4)
```

## 9. Weil, Pick and screw-function positivity

The ordinary Weil spectral form weights a zero by its multiplicity; it does
not provide higher Hermite slots.  A positive Weil or Pick kernel at every
depth, or zero negative squares for the associated Nevanlinna kernel, is
already equivalent to all zeros lying on the line.

Suzuki's screw-function model gives an unconditional continuous realization
of finite Weil forms and finite selfadjoint operators.  It does not supply a
source-first cancellation of all real zeros together with a retained
off-line quartet signal.  The proposed global normalized limits and the
spectral identifications are precisely the force-bearing statements.

Thus selfadjointness of each finite model is infrastructure; global
positivity, zero negative index, Hermite--Biehler structure, or convergence
to the logarithmic derivative cannot be imported as lemmas for RDC-4.

## 10. Surviving nonlinear possibility

A linear jet statistic cannot pass all gates above.  A sesquilinear statistic
can vanish on real points for an elementary reason: every derivative of a
real entire function is real there.  For example,

```text
Im{Xi^((r))(x)conj(Xi^((s))(x))}=0,
x real.                                             (10.1)
```

At a nonreal point the same determinant need not vanish.  A single pair
`(r,s)` is not safe: it may vanish accidentally and a fixed finite jet depth
does not cover arbitrary multiplicity.  The only formulation which survives
the gate must use the complete predetermined jet and a positive Gram sum,
not a selected derivative order.

The next target is therefore

```text
FULL-JET-PHASE-DISCRIMINANT:

1. construct an absolutely convergent Gram functional from
   {Xi^((r))(z)/r! : r>=0};
2. prove that it vanishes exactly for real z, using only unconditional
   structure of Xi;
3. prove that a symmetric off-line quartet contributes with one sign and
   cannot cancel;
4. realize the functional from the predetermined arithmetic source jets,
   retaining every finite-section collar;
5. connect the resulting scalar to the actual terminal row rather than to
   an arbitrarily chosen test.                                     (10.2)
```

Items 1--3 would close the abstract point-discrimination problem.  Items
4--5 are the source-first and DIRECTIONAL-IDENT bridge; without them the
construction remains another spectral reformulation.

## 11. Primary sources imported by this gate

```text
J.-F. Burnol,
Two complete and minimal systems associated with the zeros of the Riemann
zeta function,
arXiv:math/0203120;

D. K. Dimitrov, Y. Xu,
Wronskians of Fourier and Laplace Transforms,
arXiv:1606.05011;

M. Griffin, K. Ono, L. Rolen, J. Thorner, Z. Tripp, I. Wagner,
Jensen Polynomials for the Riemann Xi Function,
arXiv:1910.01227;

D. W. Farmer,
Jensen polynomials are not a plausible route to proving the Riemann
Hypothesis,
arXiv:2008.07206;

I. Wagner,
On a new class of Laguerre--Polya type functions with applications in number
theory,
arXiv:2108.01827;

L. X. W. Wang, N. N. Y. Yang,
Laguerre inequalities and complete monotonicity for the Riemann Xi-function
and the partition function,
DOI 10.1090/tran/9081;

M. Suzuki,
Weil's quadratic form via the screw function,
arXiv:2606.09096.                                    (11.1)
```

## 12. Status

```text
proved here:
  exact quartet parity formula for every linear jet;
  node-blind holomorphic real-axis no-go;
  complete-divisor factorization no-go;
  separation of linear, holomorphic and sesquilinear mechanisms;

imported and frozen:
  confluent derivative evaluators and their zero-adapted duals;
  Wronskian and Jensen criteria;
  correlation-kernel translation-density criteria;
  fixed-degree Jensen, Turan and Laguerre asymptotics;
  finite screw-function and Weil realizations;

rejected as new routes:
  Xi' alone,
  a fixed jet order,
  a scalar radical--jet Wronskian,
  finite or eventual derivative inequalities,
  another translation-density reformulation;

promoted for exact audit:
  FULL-JET-PHASE-DISCRIMINANT;

still open:
  its arithmetic finite realization,
  terminal-row noncancellation,
  DIRECTIONAL-IDENT and Omega7.
```
