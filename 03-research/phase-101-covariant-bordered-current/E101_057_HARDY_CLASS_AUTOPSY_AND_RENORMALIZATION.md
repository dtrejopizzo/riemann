# E101.057 - Hardy-class autopsy and moment renormalization

## 1. Exterior lattice

Fix `L` and put

```text
h=2pi/L,
d_n=hn.                                               (1.1)
```

Let the row mesh be contained in `|n|<=N`.  For a dual row `p_z`, retain the
two rational functions of E101.051,

```text
U_z(d)=p_z(D_r-dI)^(-1)s_r,
V_z(d)=p_z(D_r-dI)^(-1)1_r.                          (1.2)
```

Their first moments are

```text
A_0(z)=p_zs_r,
B_0(z)=p_z1_r.                                       (1.3)
```

On the positive exterior lattice define

```text
mathcal U_(N,z)(w)=sum_(j>=1)U_z(d_(N+j))w^j,
mathcal V_(N,z)(w)=sum_(j>=1)V_z(d_(N+j))w^j.        (1.4)
```

E101.056 proposed an `H^infinity` bound for these two functions.  The first
task is to check whether they even belong to that class section by section.

## 2. Logarithmic boundary obstruction

### Theorem 2.1

For fixed `N` and `z`,

```text
U_z(d)=-A_0(z)/d+O_(N,z)(d^(-2)),
V_z(d)=-B_0(z)/d+O_(N,z)(d^(-2)).                   (2.1)
```

Consequently,

```text
mathcal U_(N,z)(w)
=-(A_0(z)/h)w Phi(w,1,N+1)+H_(N,z)^U(w),

mathcal V_(N,z)(w)
=-(B_0(z)/h)w Phi(w,1,N+1)+H_(N,z)^V(w),            (2.2)
```

where `Phi` is the Lerch series and `H_(N,z)^U,H_(N,z)^V` belong to the
Wiener algebra.  In particular,

```text
A_0(z)!=0 => mathcal U_(N,z) notin H^infinity,
B_0(z)!=0 => mathcal V_(N,z) notin H^infinity.       (2.3)
```

### Proof

The finite diagonal resolvent expansion gives

```text
(D_r-dI)^(-1)=-d^(-1)I-d^(-2)D_r+O_(N)(d^(-3)).     (2.4)
```

Pairing with `p_zs_r` and `p_z1_r` proves (2.1).  Since

```text
sum_(j>=1) w^j/(N+j)=w Phi(w,1,N+1),                (2.5)
```

and the remainders in (2.1) are absolutely summable in `j`, equation (2.2)
follows.  Radially as `w->1`,

```text
w Phi(w,1,N+1)=-log(1-w)+O_N(1).                    (2.6)
```

The Wiener remainders are bounded on the closed disk.  A nonzero logarithmic
coefficient therefore proves (2.3). `QED`

Thus the unrenormalized `H^infinity` proposal in E101.056 is false in
general.  This is an algebraic obstruction, not a missing estimate.

## 3. Exact moment subtraction

Define

```text
U_z^sharp(d)=U_z(d)+A_0(z)/d,
V_z^sharp(d)=V_z(d)+B_0(z)/d.                       (3.1)
```

The resolvent identity gives the exact formulas

```text
U_z^sharp(d)
=p_z D_r[d(D_r-dI)]^(-1)s_r,

V_z^sharp(d)
=p_z D_r[d(D_r-dI)]^(-1)1_r.                       (3.2)
```

Hence their exterior coefficients are `O_(N,z)(j^(-2))`, and

```text
sum_(j>=1)U_z^sharp(d_(N+j))w^j,
sum_(j>=1)V_z^sharp(d_(N+j))w^j                    (3.3)
```

belong to the Wiener algebra for every fixed section.

The external response itself is

```text
p_zm(d)
=a[A_0(z)-s(d)B_0(z)]/d
R_z^sharp(d),                                       (3.4)

R_z^sharp(d)
=-a[U_z^sharp(d)-s(d)V_z^sharp(d)].                 (3.5)
```

Equation (3.4) is the required renormalization.  The leading two-generator
current is not discarded; it remains explicit and coupled to the matched
current of E101.052.

For a symmetric even source, the `A_0/d` contribution cancels between `d`
and `-d`, while the `s(d)B_0/d` contribution generally survives.  Therefore
parity alone does not remove the logarithmic obstruction.

## 4. Fixed-section Wiener bound

Let `R_N=hN` and suppose `|d_i|<=R_N` on the row mesh.  From (3.2), for
`d=d_(N+j)` and `j>=1`,

```text
|U_z^sharp(d)|
<=sum_i |(p_z)_i s_i d_i|/[h^2 j(N+j)],

|V_z^sharp(d)|
<=sum_i |(p_z)_i d_i|/[h^2 j(N+j)].                 (4.1)
```

The exact sum

```text
sum_(j>=1)1/[j(N+j)]=H_N/N                          (4.2)
```

therefore gives

```text
||U_z^sharp||_W
<=H_N/(h^2N) sum_i |(p_z)_i s_i d_i|,

||V_z^sharp||_W
<=H_N/(h^2N) sum_i |(p_z)_i d_i|.                  (4.3)
```

Here `||.||_W` is the sum of the absolute Taylor coefficients.  For fixed
`L`, the real odd Weil symbol is bounded on the lattice:

```text
sup_n |s(d_n)|<=C_L.                                 (4.4)
```

Indeed its archimedean part is a finite sum of Fourier sine transforms of
integrable kernels plus a bounded sine-integral term, and its arithmetic
part is a finite signed sine sum.  Combining (3.5), (4.3), and (4.4) yields

```text
||R_z^sharp||_W
<=a H_N/(h^2N)
  {sum_i |(p_z)_i s_i d_i|
   +C_L sum_i |(p_z)_i d_i|}.                       (4.5)
```

This proves fixed-section membership.  It does not prove a cofinal bound:
the right side may grow through the dual row.

## 5. Corrected cofinal target

Let `b_(N,z)` be the matched normalization used in DIRECTIONAL-IDENT.  A
sufficient renormalized target is

```text
WIENER-EDGE-MOMENT:

sup_(z in K)
 H_N/[h^2N|b_(N,z)|]
 {sum_i |(p_z)_i s_i d_i|
  +C_L sum_i |(p_z)_i d_i|}
is locally bounded,                                     (5.1)
```

together with convergence to zero of the recombined anti-analytic source
collar in the corresponding `H^1` norm.  The explicit leading current in
(3.4) must be combined with `J_z` before this estimate is applied.

Condition (5.1) is not known.  It is also visibly close to an ambient
absolute dual-row bound and may be much too strong in the ill-conditioned
regime.  It is a sufficient theorem, not the preferred one.

## 6. The natural Hilbert-space alternative

The logarithmic singularity is compatible with `H^2`, because the sequence
`1/j` is square summable.  Reindex the positive exterior Cauchy matrix as

```text
U_j=-(1/h)sum_(r>=0) alpha_r/(j+r),                  (6.1)
```

where `alpha_r` is the finite reversed row `p_zs_r`, extended by zero.  The
Hilbert matrix bound gives

```text
||mathcal U_(N,z)||_(H^2)
<=pi h^(-1)||p_z s_r||_2,

||mathcal V_(N,z)||_(H^2)
<=pi h^(-1)||p_z||_2.                               (6.2)
```

If `|s(d_n)|<=C_L`, then the complete external response satisfies

```text
||p_zm(.)||_(ell^2 exterior)
<=a pi h^(-1)
  [||p_zs_r||_2+C_L||p_z||_2].                     (6.3)
```

Pairing (6.3) with a recombined source collar in `ell^2` is an
`H^2`--`H^2` estimate.  It takes one norm only after forming each full
exterior sequence and does not sum prime-cell magnitudes.

The crude right side in (6.3) may still inherit the ambient dual explosion.
The proof-facing target must therefore be stated directly on the normalized
external response:

```text
H2-DUAL-BOUND:

sup_(z in K)
 ||{p_(N,z)m(d)}_(d external)||_2/|b_(N,z)|
is locally bounded.                                  (6.4)
```

This is weaker than (5.1) and does not require subtracting the logarithmic
mode.  If the recombined source collar tends to zero in `ell^2`, (6.4)
closes its paired contribution by Cauchy--Schwarz.

## 7. Relation to the novelty gate

Both corrected targets are build-neutral.  Their role is transport, not
discrimination.  The discriminating input remains the radical identity of
E101.056.

```text
unrenormalized H^infinity bound for U_z,V_z:       false generically;
moment-subtracted Wiener bound:                   exact reduction, open;
normalized H2-DUAL-BOUND:                         preferred, open;
radical model separation:                         unchanged.             (7.1)
```

No claim of progress on `Omega7` follows merely from membership in a Hardy
class.

## 8. Revised RDC-1

```text
RDC-1a  compute the normalized exterior response directly and test (6.4);

RDC-1b  if (6.4) fails, determine whether its divergence is confined to the
        explicit two-generator term (3.4);

RDC-1c  if so, absorb that term into the invariant matched current and prove
        an H2 bound for R_z^sharp;

RDC-1d  reject the Hardy route if the remaining response still has unbounded
        normalized H2 mass.                             (8.1)
```

This is a falsifiable sequence.  It does not permit indefinite sharpening of
the same norm.

## 9. Status

```text
proved:
  logarithmic obstruction to individual H^infinity bounds;
  exact first-moment subtraction;
  fixed-section Wiener bounds;
  Hilbert-matrix H2 bounds;

rejected:
  the original HARDY-DUAL-BOUND of E101.056 as stated;

open:
  normalized H2-DUAL-BOUND;
  matched-current absorption of the two-generator mode;
  RDC-1a--RDC-1d;
  RADICAL-DUAL-COMPLETION and Omega7.
```
