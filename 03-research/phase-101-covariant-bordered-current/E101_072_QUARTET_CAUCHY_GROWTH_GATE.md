# E101.072 - Quartet Cauchy growth gate for the rational exterior current

## 1. Result

E101.071 reduces the complete controlled-build response to the rational
exterior current

```text
RQEC_(N,eta)(x,phi)
=sum_(sigma=+,-)sum_m eta_m
  phi delta L_m^sigma P_N^sigma x.                 (1.1)
```

The Cauchy factorization of `delta L` yields an exact growth gate.  For the
arithmetic source, whose fixed-`L` Fourier coefficients satisfy
`kappa_j=O_L(j^(-2))`, one has

```text
|RQEC_(N,eta)(kappa,phi)|
<=C_(L,zeta,chi) ||eta||_1 T_N(phi)/N^2,            (1.2)
```

where `T_N` is a pole-adapted Cauchy size of the test.  Consequently,

```text
||eta||_1 T_N(phi)=o(N^2)
  => RQEC_(N,eta)(kappa,phi)->0.                    (1.3)
```

This is a stop rule, not a proof of noncancellation.  A nonzero controlled
limit requires the normalized terminal tests or the shift coefficients to
reach at least the quadratic threshold in (1.3).  Thus a uniformly bounded
test-module argument cannot carry the discriminant in this coordinate.

## 2. Exact face contraction

Retain the notation of E101.071.  For

```text
Delta=sigma m h,
R_p(n)=1/(d_n-p),                                   (2.1)
```

the pole component of the shifted exterior kernel is

```text
delta L_(m,p)^sigma(n,j)
=K_p [(d_n-d_j)/(d_n-d_j-Delta)]R_p(n)R_p(j).      (2.2)
```

### Lemma 2.1 - Right-bordered contraction

For `n in I_N` and `j in T_N^sigma`,

```text
abs[(d_n-d_j)/(d_n-d_j-sigma m h)]<=1.             (2.3)
```

### Proof

On the positive face, `d_n-d_j<0` and subtraction of `mh` increases its
absolute value.  On the negative face, `d_n-d_j>0` and subtraction of
`-mh` again increases its absolute value.  This proves (2.3). `QED`

The asymmetric right border is compatible with the same inequality: the
negative face begins at `-N-1`, while the positive face begins at `N+2`.
No denominator collision occurs.

## 3. Pole-adapted test and source sizes

For a row test supported on `I_N`, define

```text
Phi_(p,N)(phi)
=sum_(n in I_N)|phi_n|/|d_n-p|.                    (3.1)
```

For a source `x`, define the two exterior Cauchy tails

```text
X_(p,N)^sigma(x)
=sum_(j in T_N^sigma)|x_j|/|d_j-p|.                (3.2)
```

The quartet pole set and its coefficients are

```text
P_zeta={zeta,-zeta,conj(zeta),-conj(zeta)},

K_zeta=K_(-zeta)=a chi[1-cos(zeta L)]/2,

K_(conj(zeta))=K_(-conj(zeta))=conj(K_zeta).        (3.3)
```

Put

```text
T_N(phi)=sum_(p in P_zeta)|K_p|Phi_(p,N)(phi).      (3.4)
```

### Theorem 3.1 - Exact absolute gate

For every finite shift family `eta`, source and row test,

```text
|RQEC_(N,eta)(x,phi)|
<=||eta||_1 sum_(p in P_zeta)|K_p|Phi_(p,N)(phi)
   [X_(p,N)^+(x)+X_(p,N)^-(x)],                    (3.5)

||eta||_1=sum_m|eta_m|.                            (3.6)
```

### Proof

Insert (2.2) in (1.1), use Lemma 2.1, and take the absolute value only after
the complete kernel has been reduced to its four pole channels.  The sums in
`n` and `j` then factor as (3.1)--(3.2).  Summing in the two faces, shifts and
poles gives (3.5). `QED`

No smallness has been assigned to an individual prime or CCM cell.  The
bound is applied to the already recombined controlled quartet response.
Nevertheless it destroys signed cancellation and is therefore suitable only
as a vanishing criterion and search gate.

## 4. Arithmetic source tail

For fixed `L`, E101.070(6.5)--(6.6) gives

```text
|kappa_j|<=C_L/j^2                                 (4.1)
```

for all sufficiently large `|j|`.  Fix `beta>0`, so every pole in `P_zeta`
is separated from the real lattice.

### Lemma 4.1 - Weighted Cauchy tail

There exists `N_0=N_0(L,zeta)` such that, for `N>=N_0`,

```text
X_(p,N)^+(kappa)+X_(p,N)^-(kappa)
<=2C_L/(hN^2)                                      (4.2)
```

for every `p in P_zeta`.

### Proof

Choose `N_0` so that `h|j|>=2|p|` on both exterior faces.  Then

```text
1/|d_j-p|<=2/(h|j|).                               (4.3)
```

Using (4.1) on both tails,

```text
X^++X^-
<=4C_L/h sum_(j>=N+1)j^(-3)
<=2C_L/(hN^2).                                     (4.4)
```

This proves (4.2). `QED`

### Theorem 4.2 - Quadratic test-growth barrier

For `N>=N_0`,

```text
|RQEC_(N,eta)(kappa,phi)|
<=[2C_L/(hN^2)]||eta||_1 T_N(phi).                 (4.5)
```

In particular,

```text
||eta^(N)||_1 T_N(phi_N)=o(N^2)
  =>RQEC_(N,eta^(N))(kappa,phi_N)->0.               (4.6)
```

### Proof

Combine Theorem 3.1 with Lemma 4.1. `QED`

## 5. Consequences for fixed and growing shifts

For a fixed finite shift family, (4.6) becomes

```text
T_N(phi_N)=o(N^2)
  =>RQEC_N->0.                                      (5.1)
```

In particular, every test family uniformly bounded in the pole-adapted norm
`T_N` makes the controlled exterior response vanish at least as `N^(-2)`.

For the binomial coefficients of E101.067,

```text
eta_m=(-1)^(m+1)binom(K,m),
||eta||_1=2^K-1.                                   (5.2)
```

Thus the corresponding gate is

```text
(2^(K_N)-1)T_N(phi_N)=o(N^2)
  =>RQEC_(N,K_N)->0.                                (5.3)
```

Growing order can evade the sufficient vanishing condition only by paying
the same exponential coefficient cost already found in E101.067--E101.070.
Equation (5.3) does not show that such growth creates a nonzero signed
limit; it only removes the easy vanishing proof.

## 6. Necessary condition for a discriminating limit

Assume along a subsequence that

```text
liminf |RQEC_(N,eta^(N))(kappa,phi_N)|>0.           (6.1)
```

Then Theorem 4.2 forces

```text
limsup [||eta^(N)||_1T_N(phi_N)/N^2]>0.             (6.2)
```

Therefore the actual discriminant, if it exists in this coordinate, cannot
live in a test topology which makes every quartet Cauchy evaluation
uniformly bounded.  The amplification must be visible in at least one of

```text
the terminal dual row;
the source normalization absorbed into that row;
the growing shift polynomial.                       (6.3)
```

The first two are the same projective amplification already isolated in
E101.056--E101.059.  The third is accompanied by the exponential wall
(5.2).  Hence (6.2) is not a new closure route.  It is a quantitative audit
of where any surviving route must carry its force.

## 7. Why this does not prove noncancellation

The converse of (4.6) is false.  Even if

```text
||eta^(N)||_1T_N(phi_N)>=cN^2,                     (7.1)
```

the four poles, the two faces and the shifted rows may cancel in the signed
sum.  The absolute gate cannot distinguish

```text
a genuinely nonzero terminal residue;
a large quartet term cancelled by the boundary;
a large pole channel cancelled by its conjugate;
opposite-face cancellation;
growth caused only by normalization.                (7.2)
```

Consequently (6.2) is necessary but very far from sufficient.  Promoting it
to a lower bound would repeat the absolute-ceiling error.

## 8. Relation to existing no-go results

E101.057 rejects uniform Hardy and separate-generator bounds.  E101.059
rejects a source norm containing the terminal Cauchy functions.  E101.061
shows that fixed Abel shifts retain the singular dual mode.  E101.068 shows
that formal transfer conserves the target in the boundary.  E101.071 shows
that the controlled quartet has a forced full-source cancellation.

The new content here is the pole-specific inequality (4.5) and the exact
quadratic threshold (6.2).  The conceptual conclusion agrees with those
earlier walls:

```text
bounded test control makes the discriminating current disappear;
uncontrolled test growth merely relocates the original projective burden.
                                                            (8.1)
```

This does not yet reject the rational exterior current.  It rejects only
the hope that rank four plus ordinary boundedness makes it easy.

## 9. Revised live calculation

The next admissible calculation is not another norm bound.  It is the signed
leading coefficient at the quadratic threshold:

```text
SIGNED-RQEC-LEADING-TERM:

determine the asymptotic direction of the normalized terminal row in the
four Cauchy coordinates Phi_(p,N), retain both faces, and compute whether the
N^2-scaled signed sum in (1.1) has a nonzero transverse limit.         (9.1)
```

If the required row asymptotic is equivalent to `RDC-4` or to the terminal
secant, the route closes as another no-go.  If it follows independently from
the horizontal dual equation and the safe-half-plane arithmetic data, it is
new input capable of feeding the discriminant.

## 10. Status

```text
proved:
  exact right-bordered contraction of every shifted quartet kernel;
  pole-adapted factorized bound for the complete rational current;
  N^(-2) weighted source-tail bound for the arithmetic radical;
  quadratic necessary growth condition for any nonzero controlled limit;

rejected:
  uniformly Cauchy-bounded tests as a discriminating mechanism;
  rank-four factorization plus ordinary boundedness as a closure route;
  the converse inference from large test norm to nonzero signed response;

open:
  SIGNED-RQEC-LEADING-TERM,
  RATIONAL-EXTERIOR-NONCANCELLATION,
  the phase-79 bridge, DIRECTIONAL-IDENT and Omega7.

subsequent refinement:
  E101.073 evaluates the complete signed binomial shift sum before taking
  absolute values.  Its Hilbert correction is O(1/(K+1)), so the exponential
  coefficient norm in Section 5 is only a crude pre-cancellation gate, not
  the final binomial behavior.
```
