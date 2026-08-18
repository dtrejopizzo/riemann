# E101.071 - Exact rank-four quartet response and exterior-current reduction

## 1. Result

The controlled off-line insertion used in the finite CCM builds admits a
complete closed-form calculation.  Three facts emerge.

First, the full CCM kernel needs both its sine and cosine symbols.  The
off-diagonal Loewner formula alone is not the operator on which the radical
identity holds.

Second, after the diagonal cosine term is restored, a controlled quartet is
an exact real perturbation of rank at most four:

```text
delta M_(n,j)
=a chi Re{A[1/((d_n-zeta)(d_j-zeta))
             +1/((d_n+zeta)(d_j+zeta))]},          (1.1)

A=1-cos(zeta L),
zeta=gamma-i beta,
a=2/L.                                             (1.2)
```

Formula (1.1) includes the diagonal.

Third, the quartet term in E101.068 cancels an exact full-source component
of the controlled-build boundary difference.  The cancellation is not
total.  What remains is precisely one explicit rational exterior current:

```text
Response_(N,eta)(x,phi)
=sum_(sigma=+,-)sum_m eta_m
  phi delta L_m^sigma P_N^sigma x.                 (1.3)
```

Thus `quartet plus boundary` is not the primitive discriminant.  Its exact
irreducible form is (1.3).  The kernel in (1.3) is nonzero for every genuine
off-line insertion, but its pairing with the actual arithmetic source and
terminal tests is not yet controlled.  That paired noncancellation remains
the force-bearing problem.

## 2. Controlled insertion and the two CCM symbols

Fix `L>0` and put

```text
d_n=2pi n/L,
h=2pi/L,
a=2/L.                                             (2.1)
```

The controlled insertion acts on a real test `f` by

```text
delta W_(beta,gamma)(f)
=2chi Re integral_0^L f(y)cos(zeta y)dy,
zeta=gamma-i beta,                                  (2.2)
```

where `chi` is the prescribed strength.  Since

```text
Re cos((gamma-i beta)y)=cos(gamma y)cosh(beta y),   (2.3)
```

the perturbation is real and even in `beta`.

Define its sine and cosine symbols by

```text
delta S(t)
=2chi Re integral_0^L sin(ty)cos(zeta y)dy,

delta C(t)
=2chi Re integral_0^L cos(ty)cos(zeta y)dy.         (2.4)
```

For the CCM cells

```text
q_(n,j)(y)
 =[sin(d_n y)-sin(d_j y)]/[pi(j-n)], n!=j,

q_(n,n)(y)=2(1-y/L)cos(d_n y),                     (2.5)
```

one obtains

```text
delta M_(n,j)
=-a[delta S(d_n)-delta S(d_j)]/[d_n-d_j], n!=j,

delta M_(n,n)
=2delta C(d_n)-a delta S'(d_n).                    (2.6)
```

Equation (2.6) is the fixed-level perturbation.  If the comparison level is
also moved by `delta mu`, the additional term is

```text
-delta mu I.                                       (2.7)
```

That moving-level direction must be recombined through the horizontal
projection of E101.001--E101.003.  It is not included in the fixed-level
quartet calculation below.

## 3. Exact lattice symbols

Product-to-sum in (2.4) gives, for every complex `t` away from the removable
singularities,

```text
delta S(t)
=chi Re{
 [1-cos((t+zeta)L)]/(t+zeta)
 +[1-cos((t-zeta)L)]/(t-zeta)},                    (3.1)

delta C(t)
=chi Re{
 sin((t+zeta)L)/(t+zeta)
 +sin((t-zeta)L)/(t-zeta)}.                        (3.2)
```

Put

```text
A=1-cos(zeta L).                                   (3.3)
```

On the Fourier lattice, periodicity reduces (3.1) to

```text
delta S_n:=delta S(d_n)
=chi Re{A[1/(d_n-zeta)+1/(d_n+zeta)]}
=2chi d_n Re[A/(d_n^2-zeta^2)].                   (3.4)
```

Writing

```text
u=1-cos(gamma L)cosh(beta L),
v=sin(gamma L)sinh(beta L),
X_n=d_n^2-gamma^2+beta^2,
Y=2gamma beta,                                     (3.5)
```

the real form of (3.4) is

```text
delta S_n
=2chi d_n [uX_n-vY]/[X_n^2+Y^2].                  (3.6)
```

This is a real odd rational function on the lattice.  Its meromorphic
continuation has poles

```text
zeta,-zeta,conj(zeta),-conj(zeta).                 (3.7)
```

The residues at `zeta,-zeta` are `chi A/2`; those at the conjugate poles are
`chi conj(A)/2`.

## 4. The diagonal identity and rank-four factorization

It is not valid to differentiate the lattice-restricted expression (3.4)
as though `A` were the off-lattice numerator.  Differentiating (3.1) first
and only then setting `t=d_n` gives

```text
delta S'(d_n)
=L delta C(d_n)
 -chi Re{A[(d_n-zeta)^(-2)+(d_n+zeta)^(-2)]}.      (4.1)
```

Consequently the two diagonal channels in (2.6) combine as

```text
2delta C(d_n)-a delta S'(d_n)
=a chi Re{A[(d_n-zeta)^(-2)+(d_n+zeta)^(-2)]}.     (4.2)
```

For `n!=j`, the elementary divided-difference identity

```text
[1/(x-p)-1/(y-p)]/(x-y)
=-1/[(x-p)(y-p)]                                   (4.3)
```

applied to (3.4) gives

```text
delta M_(n,j)
=a chi Re{A[
 1/((d_n-zeta)(d_j-zeta))
 +1/((d_n+zeta)(d_j+zeta))]}.                      (4.4)
```

By (4.2), the same formula holds when `n=j`.

### Theorem 4.1 - Exact quartet factorization

Let

```text
P_zeta={zeta,-zeta,conj(zeta),-conj(zeta)},
R_p(n)=1/(d_n-p),                                   (4.5)
```

and set

```text
K_zeta=K_(-zeta)=a chi A/2,
K_(conj(zeta))=K_(-conj(zeta))=a chi conj(A)/2.     (4.6)
```

Then, on every finite section and entrywise on the bilateral lattice,

```text
delta M=sum_(p in P_zeta)K_p R_p R_p^T.            (4.7)
```

In particular, `delta M` is real symmetric and has real rank at most four.

### Proof

Expanding the real part in (4.4) as half the sum of a complex expression and
its conjugate yields (4.7) off the diagonal.  Equation (4.2) supplies the
same identity on the diagonal. `QED`

The diagonal cosine channel is therefore not a harmless detail.  It is what
makes the complete perturbation factorize with exactly the same Cauchy
vectors on and off the diagonal.

For `beta>0`, one has

```text
A!=0.                                               (4.8)
```

Indeed, `cos((gamma-i beta)L)=1` would force both
`sin(gamma L)sinh(beta L)=0` and
`cos(gamma L)cosh(beta L)=1`, which is impossible when `beta>0`.

## 5. Shifted exterior kernels

Let `sigma` be `+1` or `-1`, let `m>=0`, and write

```text
Delta=sigma m h,
x_n=d_n,
y_j=d_j.                                           (5.1)
```

The controlled variation of the shifted-test correction in E101.068 is

```text
delta D_m^sigma(n,j)
=-a[delta S(d_n)-delta S(d_(n-sigma m))]
   /[d_n-d_(j+sigma m)].                            (5.2)
```

The controlled variation of the raw radial kernel is

```text
delta L_m^sigma(n,j)
=-a[delta S(d_n)-delta S(d_j)]
   /[d_n-d_(j+sigma m)].                            (5.3)
```

### Theorem 5.1 - Residual shifted response

For each pole `p` in (4.5),

```text
delta D_(m,p)^sigma(n,j)
=K_p Delta R_p(n)R_p(n-sigma m)
  /[x_n-y_j-Delta],                                 (5.4)

delta L_(m,p)^sigma(n,j)
=K_p (x_n-y_j)R_p(n)R_p(j)
  /[x_n-y_j-Delta].                                 (5.5)
```

The full real kernels are the sums of (5.4)--(5.5) over `P_zeta`.

### Proof

For the symbol component associated with `p`,

```text
delta S_p(d_n)=(K_p/a)R_p(n).                      (5.6)
```

Since

```text
R_p(n)-R_p(n-sigma m)
=-Delta R_p(n)R_p(n-sigma m),                      (5.7)
```

substitution into (5.2) gives (5.4).  Likewise,

```text
R_p(n)-R_p(j)
=-(x_n-y_j)R_p(n)R_p(j),                           (5.8)
```

which gives (5.5). `QED`

The actual faces

```text
T_N^+={j:j>=N+2},
T_N^-={j:j<=-N-1}                                  (5.9)
```

prevent the real denominator in (5.4)--(5.5) from vanishing.  The complex
Cauchy denominators are also nonzero when `beta>0`.

## 6. Exact response of the boundary vector

For a finite source `x`, define

```text
Ccal_p(v)=sum_j R_p(j)v_j,                          (6.1)

V_(m,p)^sigma(n;x)
=sum_(j in T_N^sigma)
  x_j/[d_n-d_j-sigma m h].                         (6.2)
```

For a single shift, the boundary vector of E101.068 is

```text
H_(B,m)^sigma(x)
=D_(B,m)^sigma P_N^sigma x
 -U^(sigma m)M_B(I-P_N^sigma)x.                    (6.3)
```

### Theorem 6.1 - Exact controlled boundary response

For every row index `n`,

```text
delta H_m^sigma(x)_n
=sum_(p in P_zeta)K_p R_p(n-sigma m){
   sigma m h R_p(n)V_(m,p)^sigma(n;x)
  -Ccal_p((I-P_N^sigma)x)}.                         (6.4)
```

Equivalently, as a vector identity,

```text
delta H_m^sigma(x)
=delta L_m^sigma P_N^sigma x
 -U^(sigma m)delta Mx.                              (6.5)
```

### Proof

Insert (5.4) in the first term of (6.3) and (4.7) in the second.  This gives
(6.4).  Alternatively, subtract the two controlled-build versions of the
shift factorization

```text
L_m^sigma=U^(sigma m)M+D_m^sigma                   (6.6)
```

and substitute it in (6.3), which gives (6.5). `QED`

Formula (6.4) is a Cauchy-residual expression for the complete boundary
difference.  It does not take absolute values and retains both faces.

## 7. Quartet-boundary cancellation theorem

For one shift, the explicit quartet functional on the translated test is

```text
Qcal_m^sigma(x,phi)
=phi U^(sigma m)delta Mx.                           (7.1)
```

### Theorem 7.1 - Exact irreducible response

For every finite source and test,

```text
Qcal_m^sigma(x,phi)+phi delta H_m^sigma(x)
=phi delta L_m^sigma P_N^sigma x.                  (7.2)
```

For arbitrary finite coefficients `eta_m`, summing both faces gives

```text
Quartet_eta(x,A_eta phi)
 +phi[H_(P,N,eta)(x)-H_(Z,N,eta)(x)]

=sum_(sigma=+,-)sum_m eta_m
  phi delta L_m^sigma P_N^sigma x.                 (7.3)
```

### Proof

Equation (7.2) is immediate from (6.5).  Summation in `m` and `sigma` gives
(7.3). `QED`

This theorem decides the cancellation question left in E101.068(7.2).

```text
the full-source quartet term cancels identically against the
-U^(sigma m)delta Mx component of the boundary;

the complete response does not vanish algebraically;

the survivor is exactly the shifted exterior current on the right side of
(7.3).                                               (7.4)
```

Consequently, separately estimating the quartet and boundary terms would
fight a forced cancellation.  Future work must begin from the already
recombined right side of (7.3).

## 8. Nonzero kernel versus nonzero actual pairing

The rank-four kernel `delta M` is not identically zero for a genuine
off-line insertion.  The same holds for the family of exterior kernels
`delta L_m^sigma`: if all their lattice entries vanished, (5.3) would force
`delta S` to be constant on an infinite lattice tail; its odd rational form
(3.4) would then be identically zero, contradicting the nonzero residues in
Section 3.

This proves only

```text
there exist finite sources and tests for which the response (7.3) is
nonzero.                                             (8.1)
```

It does not prove the required statement

```text
the response is nonzero, with a controlled cofinal size, for
x=kappa_Z and for the terminal tests selected by the arithmetic chain.
                                                            (8.2)
```

The distinction is essential.  The Cauchy factors in (5.5) can annihilate a
particular source or test, and the two faces and four poles can cancel after
pairing.  Rank, rationality and nonzero residues alone do not exclude those
cancellations.

## 9. Transverse order at the critical line

By (2.3), every controlled matrix entry is an even analytic function of
`beta`.  Therefore

```text
partial_beta delta M|_(beta=0)=0,                  (9.1)
```

and the same holds for `delta L`, `delta H` and the response (7.3).

More precisely, from (2.2),

```text
[delta W_(beta,gamma)(f)-delta W_(0,gamma)(f)]/beta^2
 ->chi integral_0^L y^2 f(y)cos(gamma y)dy.         (9.2)
```

Thus the first local transverse detector is quadratic in `beta`.  Any
linear derivative test is blind by symmetry.

For two tests `phi_1,phi_2` fixed before the build, let

```text
Q_i(beta)=Qcal_eta(kappa_Z,phi_i;beta)
          -Qcal_eta(kappa_Z,phi_i;0),

B_i(beta)=phi_i{
 [delta H_eta(beta)](kappa_Z)
 -[delta H_eta(0)](kappa_Z)}.                       (9.3)
```

The wedge

```text
Wedge_(N,eta)(phi_1,phi_2;beta)
=Q_1(beta)B_2(beta)-Q_2(beta)B_1(beta)              (9.4)
```

is of order at least `beta^4`.  If its normalized limit is nonzero, the
quartet and boundary changes are not proportional functionals on the
declared two-test space.  This is a useful falsifier for universal
cancellation, but it is not a closure theorem for the selected terminal
test.  The direct exterior response (7.3) remains the minimal scalar there.

## 10. Relation to the earlier discriminant

The phase-79 `DISCRIMINANT` asks for a global fixed-`L` identification:
finite residue-cloud coherence must be connected to
`SAFE-GAMMA-IDENT`, while an off-line build must fail.  The finite coherence
signature was later shown not to be sufficient: a controlled off-line row
can be nearly coherent without arithmetic closure.

The present response has the same logical role of separating the arithmetic
build from an off-line perturbation, but it is not yet equivalent to the
phase-79 statement.  It is a local variation of the complete right-bordered
current.  No theorem currently identifies (7.3) with the fixed-`L`
arithmetic limit.

There is also an exact earlier analogue inside this phase.  E101.056(3.2)
and E101.059(4.4) show that, after completion, the controlled-build defect
has the spectral form

```text
sum_(rho in Q)Xi(rho)Phi_phi(rho).                  (10.1)
```

They already isolate nonvanishing on the actual limiting test as the open
condition `RDC-4`.  Therefore the force-bearing problem in (7.3) is not a
new logical burden.  The advance here is the exact finite rank-four and
right-bordered realization of that burden, together with the cancellation
of its artificial full-source component.  Any argument that merely relabels
(7.3) as nonzero would circle back to `RDC-4`.

To replace the earlier discriminant rather than merely supply a falsifier,
four bridges are required:

```text
Q1  construct the paired response from finite CCM and absolutely convergent
    Euler data on a safe half-plane, without using a zeta-zero location;

Q2  prove that the arithmetic response identity is equivalent to, or
    explicitly bypasses, SAFE-GAMMA-IDENT;

Q3  prove the required noncancellation for every admissible off-line quartet
    on the actual test module, not only for one controlled example;

Q4  connect the fixed-level current to the horizontal moving-level direction
    and then to the declared cofinal limit.                           (10.2)
```

The known controlled location may be used to test Q3.  It may not be
transported into the zeta-side forcing step.

## 11. No-go cross-check

The reduction (7.3) respects the existing walls only in its complete form.

```text
E101.068:
  exact transfer conserves the radical scalar in the boundary;

E101.056 and E101.059:
  nonvanishing on the actual limiting test is already the open RDC-4
  condition; a new coordinate must add an independent estimate;

E72.311 and E73.023:
  a rational Cauchy representation does not control its rotated evaluation
  and can be another form of the same endpoint;

E72.323--E72.324:
  a nondegenerate quartet Cauchy block does not estimate the exterior error;

E72.355:
  a universal node-blind compatibility identity is false;

E79.87:
  finite coherence alone does not discriminate every off-line control;

E79.116:
  build separation is admissible only inside the identification step and
  may not insert a zeta-zero location into the forcing argument.       (11.1)
```

In particular, no conclusion may be drawn from the rank-four norm, from the
absolute values of the four residual channels, or from positivity of the
finite perturbation.  The full signed current (7.3) is the object.

## 12. Independent identity check

The signs and constants were checked directly against the defining CCM
integrals at high precision with

```text
L=2log 6,
gamma=14.134725141734693790,
beta=0.30,
chi=5,
-3<=n,j<=3.                                        (12.1)
```

The maximum entrywise discrepancies were

```text
complete CCM integral versus (4.4):    1.48e-71;
delta D direct versus (5.4):           2.13e-73;
delta L direct versus (5.5):           3.41e-72;
boundary vector (6.5):                 2.27e-72.    (12.2)
```

This check is not used in the proofs.  It independently detects the two
most likely implementation errors: omission of the diagonal cosine channel
and reversal of the shifted denominator.

## 13. Revised target

Define the rational exterior quartet current

```text
RQEC_(N,eta)(beta,gamma;x,phi)
=sum_(sigma=+,-)sum_m eta_m
  phi delta L_(beta,gamma,m)^sigma P_N^sigma x.     (13.1)
```

The force-bearing target is now

```text
RATIONAL-EXTERIOR-NONCANCELLATION:

derive a source-first normalization and a declared terminal test module for
which RQEC with x=kappa_Z has a controlled nonzero transverse response for
every beta>0, while the arithmetic identity needed for DIRECTIONAL-IDENT is
obtained without inserting any zero location.                         (13.2)
```

Near the critical line the correct normalization begins with

```text
[RQEC(beta,gamma)-RQEC(0,gamma)]/beta^2.            (13.3)
```

The exact factorization in this document closes the algebraic quartet
response and removes the artificial `quartet versus boundary` split.  It
does not prove (13.2).

## 14. Status

```text
proved:
  exact sine and cosine symbols of the controlled insertion;
  exact diagonal identity restoring the complete CCM kernel;
  real rank-at-most-four factorization of the quartet perturbation;
  exact Cauchy formulas for delta D and delta L;
  exact response of the complete Loewner boundary vector;
  forced cancellation of the full-source quartet channel;
  reduction of the surviving response to one rational exterior current;
  quadratic transverse order at beta=0;

corrected:
  the full radical pairing in E101.068 must use both CCM symbols;

rejected:
  separate quartet and boundary estimates;
  rank-four nondegeneracy as proof of actual terminal noncancellation;
  a first-order transverse detector;
  finite residue-cloud coherence as the discriminant;

open:
  RATIONAL-EXTERIOR-NONCANCELLATION,
  the four bridges in (10.2),
  ARITHMETIC-LOEWNER-DISCRIMINANT,
  UNIFORM-BETA-ENDPOINT, DIRECTIONAL-IDENT and Omega7.
```
