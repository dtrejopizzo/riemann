# E101.077 - Full-jet phase rigidity and an exact off-line point discriminator

## 1. Main theorem and limitation

Let `F` be a nonzero real entire function and form its complete Taylor jet at
`z`:

```text
a_r(F;z)=F^((r))(z)/r!, r>=0.                      (1.1)
```

The real and imaginary parts of this jet are two vectors in real `ell^2`.
Their Gram determinant is nonnegative.  Its vanishing means that all Taylor
coefficients at `z` have one common complex phase.

The central result is:

```text
if F has at least one zero and all its zeros lie in a bounded horizontal
strip, then the full-jet Gram determinant vanishes exactly on the real
axis.                                                                (1.2)
```

The proof is unconditional and short: common jet phase at a nonreal point
would force a nonzero imaginary translation symmetry of `F`; translating
one zero repeatedly would leave every bounded horizontal strip.

Applied to `Xi`, this gives a predetermined, root-free function which is
zero at every real point and strictly positive at every nonreal point.  It
therefore solves the abstract point-discrimination and quartet-cancellation
problem left by E101.074--E101.076.

It does not prove Omega7.  To do so one must still derive from the finite
arithmetic model an identity whose spectral side is a positive sum of these
Gram values at the zeros.  No such identity is asserted here.

## 2. The complete Taylor jet belongs to `ell^2`

### Lemma 2.1

For every entire `F` and every `z`,

```text
a(F;z)={a_r(F;z)}_(r>=0) belongs to ell^2.          (2.1)
```

### Proof

The Taylor expansion

```text
F(z+w)=sum_(r>=0)a_r(F;z)w^r                       (2.2)
```

has infinite radius of convergence.  In particular, for any fixed `R>1`,

```text
sum_(r>=0)|a_r(F;z)|R^r<infinity.                  (2.3)
```

Thus the sequence is absolutely summable and hence square summable. `QED`

Write

```text
a=u+iv,
u=Re a in ell^2(R),
v=Im a in ell^2(R).                                (2.4)
```

## 3. The full-jet Gram functional

### Definition 3.1

Define

```text
G_F(z)
=||u||_2^2||v||_2^2-<u,v>_R^2.                    (3.1)
```

Also put

```text
S_F(z)=sum_(r>=0)|a_r(F;z)|^2,
T_F(z)=sum_(r>=0)a_r(F;z)^2.                       (3.2)
```

### Proposition 3.2 - Equivalent forms

The series below converge and

```text
G_F(z)
=sum_(0<=r<s) Im{a_r(F;z)conj(a_s(F;z))}^2         (3.3)

=1/4 [S_F(z)^2-|T_F(z)|^2]                        (3.4)

>=0.                                               (3.5)
```

Moreover,

```text
G_F(z)=0
<=> u and v are linearly dependent over R
<=> there exists theta in R such that
    exp(-itheta)a_r(F;z) is real for every r.       (3.6)
```

### Proof

The real Hilbert-space Binet--Cauchy identity gives

```text
||u||^2||v||^2-<u,v>^2
=sum_(r<s)(u_rv_s-u_sv_r)^2.                       (3.7)
```

Since

```text
Im(a_r conj(a_s))=v_ru_s-u_rv_s,                  (3.8)
```

equation (3.3) follows.  Absolute convergence follows from `u,v in ell^2`.

Set

```text
A=||u||^2,
B=||v||^2,
C=<u,v>.                                           (3.9)
```

Then

```text
S_F=A+B,
T_F=A-B+2iC.                                       (3.10)
```

Therefore

```text
S_F^2-|T_F|^2
=(A+B)^2-(A-B)^2-4C^2
=4(AB-C^2),                                        (3.11)
```

which proves (3.4)--(3.5).  Equality in Cauchy--Schwarz is equivalent to
linear dependence of `u` and `v`.  A vector `u+iv` with dependent real and
imaginary parts is a complex phase times a real vector, including the cases
`u=0` or `v=0`.  This proves (3.6). `QED`

The factor `1/r!` is not cosmetic.  It makes the full jet a canonical
square-summable vector without any growth assumption beyond entire-ness.

## 4. Phase rigidity is translation rigidity

Assume from now on that `F` is real entire:

```text
F(conj w)=conj F(w).                               (4.1)
```

### Theorem 4.1 - Phase--translation equivalence

For every `z`, the following are equivalent:

```text
(i)  G_F(z)=0;

(ii) there is theta in R such that
     exp(-itheta)F(z+w) has real Taylor coefficients in w;

(iii) there is c with |c|=1 such that
      F(t+z-conj z)=cF(t) for every complex t.      (4.2)
```

When (ii) holds, one may take `c=exp(2itheta)`.

### Proof

The equivalence of (i) and (ii) is Proposition 3.2 applied to the Taylor
series (2.2).

Suppose (ii) holds.  A power series has real coefficients exactly when

```text
exp(-itheta)F(z+w)
=conj{exp(-itheta)F(z+conj w)}.                    (4.3)
```

Using (4.1), the right side is

```text
exp(itheta)F(conj z+w).                            (4.4)
```

Thus

```text
F(z+w)=exp(2itheta)F(conj z+w).                    (4.5)
```

Put `t=conj z+w`; then (4.5) is (iii).

Conversely, let

```text
q=z-conj z,
F(t+q)=cF(t),
|c|=1.                                             (4.6)
```

Choose `theta` with `c=exp(2itheta)`.  Since

```text
F(z+w)=cF(conj z+w)
=c conj{F(z+conj w)},                              (4.7)
```

multiplication by `exp(-itheta)` turns (4.7) into the reality relation
(4.3).  Hence (ii) holds. `QED`

The theorem identifies the exact content of full-jet phase collapse.  It is
not a local accident: it propagates to a global imaginary translation law.

## 5. Bounded-strip zero theorem

### Theorem 5.1 - Exact real-axis discrimination

Let `F` be a nonzero real entire function.  Assume

```text
F has at least one zero;
every zero rho of F satisfies |Im rho|<A            (5.1)
```

for some finite `A`.  Then

```text
G_F(z)=0 <=> z is real.                             (5.2)
```

### Proof

If `z` is real, every derivative `F^((r))(z)` is real, so `v=0` in (2.4)
and `G_F(z)=0`.

Conversely, suppose `G_F(z)=0`.  Theorem 4.1 gives

```text
F(t+q)=cF(t),
q=2i Im z,
|c|=1.                                             (5.3)
```

Let `rho` be any zero of `F`.  Iterating (5.3) in both directions yields

```text
F(rho+nq)=0 for every integer n.                    (5.4)
```

If `Im z` were nonzero, then

```text
Im(rho+nq)=Im rho+2n Im z                           (5.5)
```

would be unbounded as `n` ranges over the integers.  This contradicts
(5.1).  Hence `Im z=0`. `QED`

The hypotheses are sharp in their logical role.  A zero-free exponential
can have common jet phase away from the real axis.  A function whose divisor
is invariant under a nonzero imaginary translation can also have off-axis
phase collapse.  The nonempty bounded strip excludes both mechanisms.

## 6. Application to the Riemann function

Use

```text
Xi(z)=xi(1/2+iz).                                   (6.1)
```

If `rho=sigma+igamma` is a nontrivial zeta zero, its `Xi` coordinate is

```text
z_rho=gamma+i(1/2-sigma).                          (6.2)
```

The critical strip gives unconditionally

```text
|Im z_rho|<1/2.                                    (6.3)
```

The function `Xi` is real entire, nonzero, and has zeros.  Theorem 5.1
therefore applies.

### Corollary 6.1 - Full-jet phase discriminator for `Xi`

```text
G_Xi(z)=0 <=> z is real.                            (6.4)
```

In particular, for any zero `rho` of `Xi`,

```text
rho on the critical coordinate line <=> G_Xi(rho)=0,
rho off that line                    <=> G_Xi(rho)>0.  (6.5)
```

No zero position, multiplicity, simplicity assumption or inverse of `Xi`
enters the definition of `G_Xi`.  The function is defined at every complex
point directly from the predetermined source `Xi`.

Equation (6.5) is an exact detector, not an exclusion theorem.  Evaluating a
positive detector at hypothetical zeros is different from proving that the
divisor has no such points.

## 7. Finite jet depths and unknown multiplicity

Define the depth-`M` truncation

```text
G_(F,M)(z)
=sum_(0<=r<s<=M)
  Im{a_r(F;z)conj(a_s(F;z))}^2.                    (7.1)
```

Then

```text
0<=G_(F,M)(z)<=G_(F,M+1)(z),
G_(F,M)(z)->G_F(z).                                (7.2)
```

### Corollary 7.1 - Cofinal finite detection

For every fixed nonreal `z` there exists a finite `M(z)` such that

```text
G_(F,M(z))(z)>0.                                   (7.3)
```

### Proof

If every finite truncation vanished, every summand in (3.3) would vanish and
`G_F(z)` would be zero.  Apply Theorem 5.1. `QED`

If `z` is a zero of multiplicity `nu`, then

```text
a_0=...=a_(nu-1)=0,
a_nu!=0.                                           (7.4)
```

The theorem guarantees that some later coefficient has a different phase,
but supplies no uniform bound for the first such coefficient.  Therefore:

```text
no fixed finite depth is multiplicity-safe;
the predetermined cofinal family {G_(F,M)} is multiplicity-safe pointwise;
a quantitative terminal argument must control how M grows with the finite
section.                                                            (7.5)
```

This is stronger than selecting `r=nu`: no multiplicity is used in defining
the hierarchy.

## 8. Symmetric quartet positivity

For even real entire `F`,

```text
F^((r))(-z)=(-1)^rF^((r))(z),
F^((r))(conj z)=conj F^((r))(z).                   (8.1)
```

Both transformations preserve the Gram determinant, because the first is a
real diagonal sign change of the jet and the second sends `v` to `-v`.
Hence

```text
G_F(-z)=G_F(conj z)=G_F(-conj z)=G_F(z).           (8.2)
```

### Corollary 8.1 - No quartet cancellation

If the four points in `P_zeta` are distinct and have common multiplicity
`m`, then

```text
sum_(p in P_zeta)m G_F(p)=4mG_F(zeta).             (8.3)
```

For `F=Xi` and nonreal `zeta`, the right side is strictly positive.

Thus the conjugation and parity cancellations of E101.076 do not occur in
the full-jet Gram channel.  Squaring the two-by-two real minors is essential:
a signed linear jet sum would still cancel.

## 9. Circle representation

For a radius `tau>0`, define

```text
S_(F,tau)(z)
=sum_(r>=0)tau^(2r)|a_r(F;z)|^2,

T_(F,tau)(z)
=sum_(r>=0)tau^(2r)a_r(F;z)^2,                     (9.1)

G_(F,tau)(z)
=1/4[S_(F,tau)(z)^2-|T_(F,tau)(z)|^2].            (9.2)
```

Positive real rescaling of each jet coordinate does not change common-phase
collapse.  Consequently,

```text
G_(F,tau)(z)=0 <=> G_F(z)=0                        (9.3)
```

for every `tau>0`.

Parseval on the circle gives the exact formulas

```text
S_(F,tau)(z)
=(1/2pi)integral_0^(2pi)
 |F(z+tau exp(itheta))|^2 dtheta,                  (9.4)

T_(F,tau)(z)
=(1/2pi)integral_0^(2pi)
 F(z+tau exp(itheta))F(z+tau exp(-itheta))dtheta.  (9.5)
```

### Proof

Insert

```text
F(z+tau exp(itheta))
=sum_r a_r(F;z)tau^r exp(irtheta)                  (9.6)
```

into (9.4)--(9.5).  Orthogonality of circle characters retains only equal
indices. `QED`

Equations (9.4)--(9.5) show that the discriminator is a quadratic circle
correlation, but its zero set follows from translation rigidity rather than
from a Laguerre--Polya sign assumption.

## 10. Direct source representation

Suppose

```text
F(z)=integral_R k(t)exp(-izt)dt                    (10.1)
```

with real `k` decaying fast enough to justify differentiation.  Define the
entire Bessel series

```text
B(q)=sum_(r>=0)q^r/(r!)^2.                         (10.2)
```

Then

```text
S_(F,tau)(z)
=double_integral_(R^2)
 k(t)k(u)exp(-izt+i(conj z)u)B(tau^2tu)dtdu,       (10.3)

T_(F,tau)(z)
=double_integral_(R^2)
 k(t)k(u)exp(-iz(t+u))B(-tau^2tu)dtdu.             (10.4)
```

### Proof

Differentiate (10.1):

```text
F^((r))(z)=integral_R(-it)^r k(t)exp(-izt)dt.       (10.5)
```

In the product with its conjugate, the order-`r` multiplier is

```text
(-it)^r(iu)^r=(tu)^r.                              (10.6)
```

In the square without conjugation it is

```text
(-it)^r(-iu)^r=(-tu)^r.                            (10.7)
```

Sum over `r` using (10.2).  For the Riemann kernel, double-exponential decay
dominates the Bessel growth and justifies Fubini. `QED`

Equations (10.3)--(10.4) are root-free and source-first.  They show that the
nonholomorphic dependence required by E101.076 enters only through the
conjugate factor in `S`; no zero data have been inserted.

## 11. Relation to the known no-go results

The construction avoids the previous failures for precise reasons.

```text
fixed radical blindness:
  G_Xi uses derivative jets and does not vanish on the complete divisor;

linear parity cancellation:
  squared real two-by-two minors are invariant under the full quartet;

unknown multiplicity:
  the full predetermined hierarchy contains every derivative order;

holomorphic zero-filter no-go:
  G_Xi is sesquilinear and is not an entire function of z;

Laguerre/Jensen circularity:
  positivity off the real axis follows from bounded-strip translation
  rigidity, not from assuming that Xi is Laguerre--Polya;

zero-adapted confluent duals:
  neither rho, m_rho nor 1/Xi^((m_rho))(rho) occurs in the definition.  (11.1)
```

The construction does not avoid the terminal bridge:

```text
an explicit formula is linear in a holomorphic test;
G_Xi is quadratic and couples conjugate jet channels;
the finite CCM current presently supplies no trace identity whose spectral
side is sum_rho m_rho G_Xi(rho).                                  (11.2)
```

Building that arithmetic identity without importing Weil/Pick positivity is
the remaining force-bearing task.

## 12. Build-neutrality and primary-literature novelty gate

The strict positivity theorem is not special enough to constrain the Riemann
divisor.  It holds for every real entire function satisfying the elementary
strip hypotheses, including functions with nonreal zeros.  For example,

```text
F(z)=z^2+1,
a(F;i)=(0,2i,1,0,...),
G_F(i)=4.                                           (12.1)
```

Thus `G_F` correctly detects that `i` is nonreal while placing no obstacle
to `i` being a zero.  For `Xi`, the statement

```text
G_Xi(rho)=0 for every zero rho of Xi                (12.2)
```

is exactly RH rewritten through Corollary 6.1.  The automatic inequality
`G_Xi>=0` contains no RH force.  The force lies entirely in deriving (12.2),
or the vanishing of a positive sum of the values in (12.2), from arithmetic
data.

The inspected primary sources do not contain the exact complete Taylor-jet
Gram formula (3.1)--(3.4) applied to `Xi`.  Its packaging is therefore a
plausibly new finite statement.  Its governing mechanism is not a new
principle:

```text
Cauchy--Binet gives the Gram sum of squares;
Schwarz reflection turns common phase into a parallel-line symmetry;
parallel-line phase retrieval turns that symmetry into translation of the
divisor;
a bounded horizontal strip excludes a nonzero imaginary period.       (12.3)
```

Liehr derives imaginary periodicity obstructions from reflection across
parallel lines in holomorphic phase retrieval.  Wellershoff classifies
finite-order entire functions with equal magnitudes on parallel lines and
describes the induced divisor symmetries.  These works are the closest
primary antecedents to Theorem 4.1.  They do not state the full-jet Gram or
an arithmetic trace for the Riemann divisor.

```text
L. Liehr,
Arithmetic progressions and holomorphic phase retrieval,
arXiv:2308.05722;

M. Wellershoff,
Phase retrieval of entire functions and its implications for Gabor phase
retrieval,
arXiv:2202.03733.                                   (12.4)
```

The calibrated novelty verdict is therefore:

```text
exact full-jet packaging: potentially new;
phase-to-translation rigidity: known in nearby primary literature;
RH progress supplied by the theorem alone: none;
possible value: a noncancelling target for a genuinely new arithmetic
trace, if such a trace can be derived.                              (12.5)
```

This classification prevents the geometric detector from being reported as
the missing discriminant.  It is infrastructure until the arithmetic trace
exists.

## 13. New target localized by the theorem

The former `ROOT-FREE-JET-CURRENT` can now be sharpened to

```text
ARITHMETIC-JET-GRAM-TRACE:

construct finite, source-first scalars A_(N,M,tau) from the CCM/Gamma--Euler
data such that

1. every finite jet, endpoint and Fourier collar is retained exactly;
2. the spectral limit, if an off-line orbit exists, contains a nonnegative
   term proportional to G_(Xi,M)(rho);
3. the complete real-zero background vanishes atomwise by the Gram wedge,
   not by a zero-adapted filter;
4. M grows cofinally and the limit may be interchanged with the finite
   section without a uniform multiplicity assumption;
5. the arithmetic side is proved to have the value or sign which excludes a
   positive quartet contribution;
6. the same scalar is the actual terminal DIRECTIONAL-IDENT pairing.    (12.1)
```

Items 2--3 now have an exact abstract mechanism and cannot suffer quartet
cancellation.  Items 1 and 4--6 remain open.

## 14. Status

```text
proved:
  square summability of the complete Taylor jet;
  three exact Gram representations;
  phase collapse iff imaginary translation covariance;
  bounded-strip phase-rigidity theorem;
  G_Xi(z)=0 iff z is real;
  cofinal finite-depth detection for every fixed nonreal point;
  positive, noncancelling response of every off-line quartet;
  circle and direct Riemann-source formulas;

not assumed:
  RH, simplicity, a multiplicity bound, zero locations,
  Laguerre--Polya membership, Weil positivity or a Pick kernel sign;

closed abstractly:
  pointwise real/off-line discrimination,
  parity cancellation of the full quartet,
  fixed-depth selection of a multiplicity;

novelty classification:
  potentially new full-jet packaging,
  known phase-reflection principle,
  build-neutral and not an RH advance by itself;

open:
  ARITHMETIC-JET-GRAM-TRACE,
  quantitative finite-depth/collar control,
  the terminal-row identification,
  DIRECTIONAL-IDENT and Omega7.
```
