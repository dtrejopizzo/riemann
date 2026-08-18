# E101.060 - Bilateral Abel duality for the complete exterior current

## 1. Lattice and normalization

Put

```text
h=2pi/L,
a=2/L,
d_n=hn.                                              (1.1)
```

Let the row mesh be `-N<=n<=N`, let `p_z` be the dual row and let
`b_(N,z)` be a nonzero normalization.  Write

```text
p_tilde_z=p_z/b_(N,z).                              (1.2)
```

For `j>=1`, denote the two exterior columns by

```text
m_j^+=m(d_(N+j)),
m_j^-=m(-d_(N+j)).                                  (1.3)
```

The external displacement formula E101.051 reads

```text
m(d)=-a(D_r-dI)^(-1)[s_r-s(d)1_r].                 (1.4)
```

The goal is to sum both exterior half-lattices before inserting an artificial
collar boundary.

## 2. Four finite Abel polynomials

Define

```text
A_z^+(t)=sum_(r=0)^(2N)
          (p_tilde_z)_(N-r)s_(N-r)t^r,

B_z^+(t)=sum_(r=0)^(2N)
          (p_tilde_z)_(N-r)t^r,

A_z^-(t)=sum_(r=0)^(2N)
          (p_tilde_z)_(r-N)s_(r-N)t^r,

B_z^-(t)=sum_(r=0)^(2N)
          (p_tilde_z)_(r-N)t^r.                    (2.1)
```

Let `c_j^+,c_j^-` be finitely supported exterior source coefficients and put

```text
C^+(t)=sum_(j>=1)c_j^+t^j,
C^-(t)=sum_(j>=1)c_j^-t^j,

D^+(t)=sum_(j>=1)c_j^+s(d_(N+j))t^j,
D^-(t)=sum_(j>=1)c_j^-s(-d_(N+j))t^j.              (2.2)
```

Each function in (2.2) vanishes at zero.

## 3. Exact bilateral identity

### Theorem 3.1

The complete normalized exterior pairing is

```text
sum_(j>=1)[
 c_j^+ p_zm_j^+/b_(N,z)
+c_j^- p_zm_j^-/b_(N,z)]

=1/pi integral_0^1 {
   A_z^+(t)C^+(t)-B_z^+(t)D^+(t)
  -A_z^-(t)C^-(t)+B_z^-(t)D^-(t)
  } dt/t.                                           (3.1)
```

### Proof

For a positive exterior node and a row index `n=N-r`,

```text
d_(N-r)-d_(N+j)=-h(r+j).                            (3.2)
```

Equations (1.4) and `a/h=1/pi` give

```text
p_zm_j^+/b_(N,z)
=1/pi sum_(r=0)^(2N)
 [(p_tilde_z)_(N-r)s_(N-r)
  -s(d_(N+j))(p_tilde_z)_(N-r)]/(r+j).             (3.3)
```

For a negative exterior node and `n=r-N`,

```text
d_(r-N)+d_(N+j)=h(r+j),                             (3.4)
```

and hence

```text
p_zm_j^-/b_(N,z)
=-1/pi sum_(r=0)^(2N)
 [(p_tilde_z)_(r-N)s_(r-N)
  -s(-d_(N+j))(p_tilde_z)_(r-N)]/(r+j).            (3.5)
```

Use the moment identity

```text
1/(r+j)=integral_0^1 t^(r+j-1)dt.                  (3.6)
```

Multiply (3.3)--(3.5) by the corresponding source coefficients, sum, and
apply the definitions (2.1)--(2.2).  All sums are finite, so the interchange
with the integral is immediate. `QED`

Formula (3.1) is exact.  It contains the near collar and the far exterior in
one integral and preserves cancellation between them.

## 4. Parity reduction

Assume the symbol is odd.

### 4.1 Even source

If

```text
c_j^-=c_j^+=c_j,                                    (4.1)
```

put

```text
C(t)=sum_(j>=1)c_jt^j,
D(t)=sum_(j>=1)c_js(d_(N+j))t^j.                   (4.2)
```

Then `C^-=C^+=C` and `D^-=-D^+=-D`.  Equation (3.1) becomes

```text
PAIR_even
=1/pi integral_0^1 [
  (A_z^+-A_z^-)C-(B_z^++B_z^-)D
  ]dt/t.                                            (4.3)
```

The endpoint polynomial identities are

```text
A_z^+(1)-A_z^-(1)=0,
B_z^+(1)+B_z^-(1)=2 p_tilde_z1_r.                   (4.4)
```

Thus bilateral parity cancels the complete leading `A_0/d` mode and retains
the constant-generator `B_0` mode, exactly as predicted by E101.051(4.3).

### 4.2 Odd source

If `c_j^-=-c_j^+`, the complementary formula is

```text
PAIR_odd
=1/pi integral_0^1 [
  (A_z^++A_z^-)C-(B_z^+-B_z^-)D
  ]dt/t.                                            (4.5)
```

Now

```text
A_z^+(1)+A_z^-(1)=2 p_tilde_zs_r,
B_z^+(1)-B_z^-(1)=0.                                (4.6)
```

The two parity sectors therefore exchange the surviving generator.

## 5. A finite H1 sufficient estimate

Use the normalized Hardy norm

```text
||F||_(H1)
=1/(2pi) integral_0^(2pi)|F(e^(itheta))|dtheta.     (5.1)
```

The Fejer--Riesz inequality gives, for every analytic `F` with `F(0)=0`,

```text
integral_0^1 |F(t)|dt/t<=pi||F||_(H1).              (5.2)
```

Indeed, apply the line-segment inequality to the analytic function `F(w)/w`;
its boundary `H1` norm equals that of `F`.

Applying (5.2) to (4.3) proves

```text
|PAIR_even|
<=||A_z^+-A_z^-||_(Linf(0,1)) ||C||_(H1)
 +||B_z^++B_z^-||_(Linf(0,1)) ||D||_(H1).          (5.3)
```

The constant `1/pi` in (4.3) cancels the constant `pi` in (5.2).  There is
no residual power of `L`.

The same argument applied after differentiating the normalized polynomials
in `z` gives the corresponding one-safe-derivative bound.  If the source
coefficients are independent of `z`, no derivative of `C,D` occurs.

## 6. Natural BMOA form

For a finite polynomial `A`, define its Abel--Cauchy transform

```text
Kcal A(w)
=w/pi integral_0^1 A(t)/(1-tw)dt.                  (6.1)
```

Its `j`-th Taylor coefficient is

```text
1/pi integral_0^1 A(t)t^(j-1)dt.                   (6.2)
```

Consequently (4.3) is the coefficient pairing of the source pair `(C,D)`
with

```text
(Kcal(A_z^+-A_z^-),-Kcal(B_z^++B_z^-)).             (6.3)
```

The natural dual of `H1` is BMOA.  Therefore a uniform BMOA bound for (6.3)
is the intrinsic bounded-functional version of (5.3).  The polynomial
`Linf(0,1)` bounds in (5.3) are explicit sufficient conditions; they are not
asserted to be necessary.

The logarithmic mode found in E101.057 is compatible with this formulation:
`-log(1-w)` belongs to BMOA although it does not belong to `H^infinity`.

## 7. Why the dual bound is stronger than the scalar target

The identity (4.3) does not imply a uniform norm bound for its dual
polynomials.  Consider

```text
q_N(t)
=N[1-t^4-(16/5)(t-t^3)].                            (7.1)
```

It is anti-palindromic,

```text
q_N(t)=-t^4q_N(1/t),                                (7.2)
```

so it has the same reversal symmetry as `A^+-A^-`.  For the fixed source
`C(t)=t`,

```text
integral_0^1 q_N(t)C(t)dt/t
=integral_0^1q_N(t)dt=0,                            (7.3)
```

because

```text
integral_0^1(1-t^4)dt=4/5,
integral_0^1(t-t^3)dt=1/4.                          (7.4)
```

Nevertheless `||q_N||_(Linf(0,1))` grows linearly.  Hence the scalar pairing
may vanish while the sufficient dual norm diverges.  Proving a BMOA or
polynomial bound is genuine additional mathematics, not a consequence of
the desired scalar limit.

## 8. Cofinal criterion

The symmetric convention in Sections 1--7 treats `N+j` and `-N-j` as
external for every `j>=1`.  In the actual right-bordered block, the selected
columns are `-N,...,N+1`.  Therefore the positive exterior begins at `j=2`
and the negative exterior begins at `j=1`.  E101.065 proves the exact
correction for the selected column `N+1`; it must be applied before using the
following criterion on the terminal source.

For an even complete exterior source define

```text
P_(A,N,z)=A_z^+-A_z^-,
P_(B,N,z)=B_z^++B_z^-.                              (8.1)
```

A concrete sufficient theorem would be

```text
ABEL-POLYNOMIAL-EXTERIOR:

sup_(z in K){
 ||P_(A,N,z)||_infinity+||partial_zP_(A,N,z)||_infinity
+||P_(B,N,z)||_infinity+||partial_zP_(B,N,z)||_infinity
}=O(1),                                             (8.2)

||C_N||_(H1)+||D_N||_(H1)->0.                       (8.3)
```

Here every polynomial norm is taken on `[0,1]`, and `C_N,D_N` must describe
the complete recombined exterior source, not separate collar and far pieces.
Equations (5.3) and its derivative then give

```text
PAIR_even->0                                        (8.4)
```

locally uniformly with one safe derivative.

E101.061 constructs an exact symmetric family for which the source-adapted
scalar tends to zero while all four uniform dual bounds in (8.2) diverge.
Thus (8.2) is rejected as a main target.  The weaker product version, in
which the complete source-adapted products tend to zero without separate
boundedness and convergence, remains sufficient but unproved.

## 9. No-go audit

The Abel variable in this document is the exterior Fourier index.  It is not
the prime-shift variable `log n` of the Hardy--Euler inequality, and no sign
inequality occurs.  Thus the identity is not the Abel-prime route.

It also does not produce the Paley--Wiener factor `e^(-sigma L)` required in
E72.316.  That scale must appear either in the actual source convergence
(8.3), in a sharper coupled estimate, or in the exact nodal cancellation of
E72.391.

Finally, (8.2) does not force detection of an inserted quartet.  A bounded
limiting test may annihilate its four evaluation functionals.  The
discriminating clause of E101.056 remains separate.

## 10. Status

```text
proved:
  exact bilateral Abel representation of the whole exterior current;
  parity reduction and exact leading-mode cancellation;
  finite H1 estimate with no residual lattice scale;
  BMOA dual coordinate;
  strictness of the uniform dual bound over one scalar pairing;

reduced:
  the complete exterior pairing to one exact coupled Abel integral;

sufficient but too strong:
  ABEL-POLYNOMIAL-EXTERIOR;

rejected in E101.061:
  uniform ABEL-POLYNOMIAL-EXTERIOR as a proof mechanism;

not claimed:
  derivation of (8.2) from the dual equation;
  H1 convergence of the complete recombined source;
  Paley--Wiener suppression or quartet detection;

open:
  a coupled source-adapted estimate, DIRECTIONAL-IDENT and Omega7.
```
