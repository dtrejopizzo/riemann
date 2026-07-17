# Omega_7 closure program after Phases 67--70

**Date:** 2026-07-07.
**Role:** write the cleanest possible proof architecture after the quantum, symbol, Nevanlinna, and
de Bruijn-Newman routes have all been audited.

This is not a completed proof. It is the narrowest complete form of what a proof of `Omega_7` must now
look like.

## 0. The current terminal object

The gauge-dependent terminal statement is

```text
Omega_7:  delta_N >= 0 for every N.
```

Equivalently, at each terminal gauge,

```text
A_N - P_lambda >= 0.
```

After Phase 69, the gauge-free form is better:

```text
F(z) := xi(1/2 + i z),
N(z) := -F'(z)/F(z).
```

Then the terminal condition is the Nevanlinna/Hermite-Biehler condition

```text
Omega_7
  <=> Im N(z) >= 0 for every Im z > 0
  <=> F is Laguerre-Pólya
  <=> all zeros of xi are on the critical line
  <=> RH.
```

After Phase 70, the same condition is

```text
Omega_7 <=> Lambda <= 0,
```

where `Lambda` is the de Bruijn-Newman constant. Rodgers-Tao gives `Lambda >= 0`, so

```text
Omega_7 <=> Lambda = 0.
```

Thus the missing direction is exactly:

```text
prove Lambda <= 0 from arithmetic/Euler structure.
```

## 1. What failed and what survived

The four mechanisms tried are now understood:

```text
Phase 67: quantum/Jantzen index
  survived: signed index is the right detector;
  failed: positive Haar/q-dimension mechanisms lose phase cancellation;
  failed: q-deforming the form contaminates/fabricates;
  survived: exact form + pivotal overlay is the right quantum architecture.

Phase 68: Toeplitz/GLT symbol
  survived: symbol detector and local touch picture;
  failed: fixed Toeplitz symbol as gauge-uniform proof object;
  survived: true object is exact/gauge-robust, with GLT only as shadow.

Phase 69: gauge-free Nevanlinna object
  survived: Omega_7 <=> Im(-xi'/xi) >= 0, no gauge;
  failed: archimedean Gamma as positive cushion; Gamma is negative drag;
  survived: positivity must be prime/Euler-side.

Phase 70: Lee-Yang / de Bruijn-Newman
  survived: Omega_7 <=> Lambda <= 0 and hence Lambda = 0;
  failed: heat-flow monotonicity proves the known direction Lambda >= 0;
  survived: missing half is the arithmetic direction Lambda <= 0.
```

So the proof cannot be a generic positivity theorem, a Haar expectation, a KMS state, a scalar symbol,
or a heat-flow monotonicity. It must be an **Euler-product arithmetic majorization** in the gauge-free
Nevanlinna/de Bruijn-Newman object.

## 2. The master theorem to prove

### Theorem AHM -- Arithmetic Herglotz Majorization

Let

```text
N(z) = - d/dz log xi(1/2 + i z)
     = N_A(z) + N_P(z),
```

where `N_A` is the explicit archimedean/polar part and `N_P` is the analytically continued Euler-prime
part. Then

```text
Im N_P(z) >= - Im N_A(z)       for every Im z > 0.
```

Equivalently,

```text
Im N(z) >= 0                  for every Im z > 0.
```

If AHM is true, then `Omega_7` follows immediately by Phase 69.

This is the exact statement of the missing arithmetic direction. It is not a new disguise for the old
gauge `delta_N`: it is the gauge-free Herglotz majorization of the archimedean drag by the Euler part.

## 3. Kernel form: the version that matches Omega_7

The scalar inequality should be proved in kernel form. Define the Pick kernel

```text
K_Nev(z,w) := (N(z) - conjugate(N(w))) / (z - conjugate(w)).
```

The target is

```text
K_Nev >= 0 on C_+.
```

Equivalently, for every finite set `{z_j}` in the upper half-plane and every vector `c`,

```text
sum_{i,j} c_i conjugate(c_j)
  (N(z_i)-conjugate(N(z_j))) / (z_i-conjugate(z_j))
>= 0.
```

Splitting into archimedean and prime pieces,

```text
K_P >= -K_A.
```

This is the gauge-free version of

```text
A_N >= P_lambda.
```

So the proof target is:

### Kernel AHM

```text
For every finite Pick test vector c,
    <c, K_P c> >= <c, -K_A c>.
```

This is the strongest clean form of `Omega_7`.

## 4. The de Bruijn-Newman form

Let

```text
H_lambda(t) = integral exp(lambda u^2) Phi(u) cos(tu) du
```

be the de Bruijn-Newman heat flow. Define

```text
N_lambda(z) := - d/dz log H_lambda(z).
```

The known heat monotonicity improves positivity as `lambda` increases. That proves the de Bruijn side,
not RH. The missing statement is:

### Arithmetic Newman Bound

```text
Lambda <= 0.
```

Equivalently:

```text
N_0(z) is Nevanlinna on C_+.
```

Equivalently:

```text
K_Nev,0 >= 0.
```

Thus AHM and the Arithmetic Newman Bound are the same theorem in two languages:

```text
AHM <=> Im N_0 >= 0 <=> Lambda <= 0 <=> Omega_7.
```

This equivalence is useful because any candidate proof can be audited in both directions:

- if it only uses heat-flow monotonicity, it gives `Lambda >= 0`, the known/wrong direction;
- if it proves AHM, it proves `Lambda <= 0`, the missing arithmetic direction.

## 5. The finite terminal theorem and its limitation

At finite level, the exact terminal defect is

```text
D_N := A_N^{-1/2}(A_N-P_lambda)A_N^{-1/2}.
```

The finite goal is

```text
D_N >= 0.
```

The Phase 67 q-trace formulation gives a precise forcing form. Let

```text
Pi_{N,-} = spectral projection of D_N onto (-infty,0),
G_q e_n = q^{2(n+y)} e_n,
Q_N(q) = Tr(G_q Pi_{N,-}).
```

Then:

```text
if q^{-2y} Q_N(q) = 0 as a polynomial in q^2,
then Pi_{N,-}=0,
therefore D_N>=0.
```

This is already a finite theorem. However, the missing identity

```text
Tr(G_q Pi_{N,-}) = 0
```

as a pivotal/fusion character is not weaker than finite `Omega_7`. It is exactly the statement
`D_N>=0` written through the negative spectral projection.

So the q-resolvent expression is a correct finite certificate, but not an independent forcer unless one
constructs a closed Euler/Gamma/fusion formula for `Tr(G_q(z-D_N)^(-1))` without diagonalizing `D_N`.
No such formula is currently available.

The finite q-trace certificate is compatible with the gauge-free theorem:

```text
finite q-trace forcing for all N
  => A_N-P_lambda >=0 for all N
  => Kernel AHM
  => Im N >=0
  => Lambda <=0
  => Omega_7.
```

## 6. The only acceptable source of the proof

The proof must use arithmetic that the generic de Bruijn-Newman framework does not see. The allowed
ingredients are:

- the exact Euler/von Mangoldt structure;
- the exact Gamma/polar archimedean term;
- the functional equation only as structural symmetry, not as hidden RH;
- exact Pick/Nevanlinna kernels;
- finite q-trace/resolvent identities only on the exact defect form;
- limiting arguments that preserve the finite positivity.

Forbidden ingredients:

- a KMS state whose partition function is `zeta`;
- choosing a metric/norm from `-zeta'/zeta`;
- Cholesky or square-root factorization of `P_lambda`;
- Haar/positive expectations that produce the incoherent ceiling `S_abs`;
- q-deforming the defect form itself;
- heat-flow monotonicity alone;
- assuming zero locations.

## 7. The proposed proof skeleton

### Step 1 -- Gauge-free kernel equivalence

Prove rigorously:

```text
Omega_7 <=> K_Nev >= 0 on C_+.
```

This is essentially Phase 69 in theorem form.

### Step 2 -- Prime-side majorization theorem

Prove Kernel AHM:

```text
K_P + K_A >= 0.
```

This is the hard step. It must be an Euler-product inequality, not an analytic continuation tautology.

### Step 3 -- Finite q-trace certificate

For each finite terminal jet, the q-resolvent identity

```text
(1/(2 pi i)) integral_{Gamma_-}
    Tr(G_q (z-D_N)^(-1)) dz
= 0
```

is equivalent to `D_N>=0`. Thus it should be used as a certificate/diagnostic unless an independent
Euler-Gamma closed form for the resolvent trace is found.

By the finite q-trace theorem, such an independent identity would imply `D_N>=0`; without the
independent evaluation, this step is just finite `Omega_7` restated.

### Step 4 -- Passage to the gauge-free object

Show the finite inequalities for all terminal gauges and all `N` imply the Herglotz kernel positivity:

```text
D_N>=0 for all N,gauges  =>  K_Nev>=0.
```

Then Phase 69 gives RH.

### Step 5 -- de Bruijn-Newman verification

Translate the result:

```text
K_Nev>=0 <=> Lambda <=0.
```

Together with Rodgers-Tao `Lambda>=0`, obtain:

```text
Lambda = 0.
```

This is not needed logically for RH, but it places the closure in the canonical dBN framework.

## 8. The minimal new lemma, corrected

Everything reduces to one lemma:

### Arithmetic Herglotz Majorization lemma

The real remaining theorem is not the q-resolvent residue by itself. It is:

```text
K_P >= -K_A
```

on the upper half-plane, or equivalently

```text
Im N_P(z) >= -Im N_A(z)      (Im z>0).
```

The q-resolvent version remains a possible finite certificate only if one can first derive an
independent closed form:

```text
Tr(G_q(z-D_N)^(-1)) = explicit Euler/Gamma_q/fusion expression.
```

Without that, `Tr(G_q Pi_-)=0` is exactly `D_N>=0`, not a reduction.

## 9. How to attack AHM

The proof must produce an Euler-side lower bound for the prime Pick kernel:

```text
<c,K_P c> >= <c,-K_A c>
```

for every finite upper-half-plane Pick test. The plausible attack path is:

```text
Euler product / von Mangoldt explicit formula
  -> prime kernel representation
  -> arithmetic lower bound against the Gamma/polar drag
  -> K_P + K_A >= 0.
```

The testable subclaims are:

1. **Kernel representation.**

```text
K_P(z,w) = canonical Euler/vonMangoldt kernel on C_+.
```

2. **Arch drag exactness.**

```text
K_A(z,w) = explicit Gamma/polar negative contribution.
```

3. **Arithmetic lower bound.**

```text
K_P + K_A >= 0
```

as a kernel, not merely pointwise on a grid.

4. **No hidden RH.**

The proof must use Euler structure, not zero locations or a positivity condition equivalent to
Hermite-Biehler.

5. **Falsifier.**

```text
Davenport-Heilbronn or planted off-line data must break the arithmetic lower bound.
```

## 9.1 Hardy/autocorrelation form

For actual work, Cauchy tests can be written as Laplace transforms. If

```text
phi(u)=sum_j c_j/(u-z_j),  Im z_j>0,
```

then

```text
phi(u)= i integral_0^infty f(t)e^{-iut}dt,
f(t)=sum_j c_j e^{i z_j t}.
```

The prime side samples the autocorrelation

```text
C_f(a)=integral_0^infty f(t+a)conj(f(t))dt
```

at `a=log n`. Thus AHM is equivalent to the Hardy-Euler inequality

```text
2 Re sum_{n>=2} Lambda(n)n^{-1/2} C_f(log n) <= A[f],
```

for every finite exponential sum `f`, where `A[f]` is the Gamma/polar archimedean quadratic form.

This is the most concrete current work surface. Absolute estimates on `C_f(log n)` reproduce the
incoherent `S_abs` ceiling and fail; the proof must exploit arithmetic cancellation in the sampled
autocorrelation sum.

## 10. Final clean statement

The complete closure of Ω₇ can now be written as:

> **Omega_7 Closure Theorem.**  
> The Euler/vonMangoldt kernel of the prime part majorizes the archimedean/polar drag:
> `K_P >= -K_A` on the upper half-plane. Therefore
> `N(z)=-d/dz log xi(1/2+iz)` is a Nevanlinna function, `xi` is Laguerre-Pólya, `Lambda<=0`, and
> `Omega_7`/RH follows. At finite level this is equivalently certified by the vanishing of the
> negative spectral projection of `D_N`.

The proof has one nontrivial core:

```text
prove Arithmetic Herglotz Majorization from Euler structure.
```

That is the mathematical frontier left by Phases 67--70.
