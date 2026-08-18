# 107.147 -- Trace-norm square: a superlogarithmic dimension no-go

## 1. Result

`107_146` left one Euclidean tensorial replacement of the rank-one mass
functional open.  On a Euclidean projective tensor product

\[
 \mathbb R^2\otimes_\pi\mathbb R^2\simeq M_2(\mathbb R),
\]

the projective tensor norm is the trace (nuclear) norm.  This note computes
the resulting absolute dimension problem on the integral lattice
\(M_2(\mathbb Z)\).

The outcome is negative and stronger than a change from base 3 to base 2.

> **Theorem.**  Let \(d_*(n)\) be the minimum number of linear generators
> of the nuclear ball
> \[
>  B_*(n)=\{A\in M_2(\mathbb Z):\|A\|_*\le n\},
> \]
> with coefficients in \(\{0,\pm1\}\) and mass budget
> \(\sum\|\alpha(F)F\|_*\le n\).  If
> \[
>  n_k=\prod_{i=1}^k p_i,
>  \qquad p_i\equiv1\pmod4
> \]
> for distinct primes \(p_i\), then
> \[
>  d_*(n_k)\ge 2^{k+1}.
> \]
> In particular, for the product of the first \(k\) primes congruent to
> \(1\pmod4\),
> \[
>  \frac{d_*(n_k)}{\log n_k}\longrightarrow\infty.
> \]

Thus the Euclidean trace-norm candidate does not have Riemann--Roch-compatible
\(\Theta(\deg D)\) growth under \(n=\lfloor e^{\deg D}\rfloor\).  It is
not the mass functional sought for the square.

## 2. Exact integral model

For

\[
 A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]

the trace norm can be compared with an integer without numerical singular
value calculations:

\[
 \|A\|_*^2=\|A\|_F^2+2|\det A|
 =a^2+b^2+c^2+d^2+2|ad-bc|.
 \tag{2.1}
\]

Hence \(B_*(n)\) is a finite, exactly enumerable set.

A subset \(F\subset B_*(n)\) linearly generates when every
\(A\in B_*(n)\) admits coefficients \(\alpha(F)\in\{0,\pm1\}\) such that

\[
 A=\sum_{F}\alpha(F)F,
 \qquad
 \sum_F |\alpha(F)|\,\|F\|_*\le n.
 \tag{2.2}
\]

This is the direct trace-norm analogue of the definition used by
Connes--Consani and by `107_146`.

## 3. Primitive boundary rigidity

### Lemma 1

Let \(A\in M_2(\mathbb Z)\) have rank one, primitive entries
\(\gcd(A_{ij})=1\), and \(\|A\|_*=n\).  Every generating set for
\(B_*(n)\) contains either \(A\) or \(-A\).

### Proof

Write \(A=u v^t\) and put

\[
 Q=\frac{u}{\|u\|_2}\frac{v^t}{\|v\|_2}.
\]

Then \(\|Q\|_{\rm op}=1\) and
\(\langle Q,A\rangle=\|A\|_*=n\).  Suppose (2.2) represents \(A\), and
write \(W_F=\alpha(F)F\).  Nuclear/operator duality gives

\[
 n=\langle Q,A\rangle
 =\sum_F\langle Q,W_F\rangle
 \le\sum_F\|W_F\|_*
 \le n.
\]

Every inequality is therefore an equality.  For each nonzero \(W_F\),

\[
 \langle Q,W_F\rangle=\|W_F\|_*.
\]

But

\[
 \langle Q,W_F\rangle
 \le\|W_F\|_F\le\|W_F\|_*,
\]

so equality in Cauchy--Schwarz and equality of Frobenius and nuclear norms
force \(W_F=\lambda_F A\) with \(\lambda_F\ge0\).  Since both matrices
are integral and the entries of \(A\) are primitive,
\(\lambda_F\in\mathbb Z_{\ge0}\).  A nonzero summand already has norm at
least \(n\), so the budget permits exactly one, with \(\lambda_F=1\).
Thus \(A\) or \(-A\) belongs to the generating set.  \(\square\)

## 4. Arithmetic supply of mandatory rays

Let \(n_k=\prod_{i=1}^k p_i\), with distinct
\(p_i\equiv1\pmod4\).  The number of primitive signed ordered solutions
of

\[
 x^2+y^2=n_k^2
 \tag{4.1}
\]

is

\[
 r_{2,\mathrm{prim}}(n_k^2)=4\cdot2^k.
 \tag{4.2}
\]

Indeed, in \(\mathbb Z[i]\), each split prime
\(p_i=\pi_i\bar\pi_i\) contributes exponents
\((2,0),(1,1),(0,2)\) to a Gaussian integer of norm \(n_k^2\).
Primitivity excludes \((1,1)\), leaving two choices per prime and four
units.

For every solution \(u=(x,y)^t\), form

\[
 A_u=u(1,0).
\]

It is an integral primitive rank-one matrix with
\(\|A_u\|_*=\|u\|_2=n_k\).  Identifying \(A_u\) and \(-A_u\) leaves
\((4\cdot2^k)/2=2^{k+1}\) distinct mandatory generators by Lemma 1.
This proves the first assertion.

For the first \(k\) primes in the progression \(1\pmod4\), the prime
number theorem in arithmetic progressions gives
\(\log n_k=\Theta(k\log k)\).  Therefore

\[
 \frac{2^{k+1}}{\log n_k}\to\infty,
\]

which proves the superlogarithmic obstruction.

## 5. Small exact values

The verifier exhausts the first two balls:

\[
 |B_*(1)|=9,\qquad d_*(1)=4,
\]

\[
 |B_*(2)|=49,\qquad d_*(2)=12.
\]

At radius one the four matrix units are individually mandatory.  At
radius two, the mandatory set consists of those four units, their four
doubles, and the four primitive rank-one sign matrices of nuclear norm
two.  These twelve generators reach all 49 matrices, so the value is
exact.

The same program independently enumerates (4.1) for

\[
 n=5,65,1105,32045
\]

and recovers exactly \(4\cdot2^k\) primitive signed ordered solutions.

## 6. Consequence for row (a)

There are now two tested mass choices for the higher-rank absolute
dimension:

1. coordinate \(\ell^1\), treated in `107_146`, preserves linear growth
   but changes the rank-one base-3 mechanism; `107_150` proves that it is
   exactly the projective tensor norm inherited from \(\ell^1\) factors;
2. the Euclidean projective tensor norm, treated here, has a
   superlogarithmic mandatory-ray obstruction and fails linear
   Riemann--Roch growth.

This does not prove that no mass functional can work on the square.  It
closes the Euclidean trace-norm branch fixed in advance, but does not
close the CC-inherited projective tensor branch.  That branch is the
entrywise \(\ell^1\) model of `107_150`.

The 2026 Connes--Consani papers on the arithmetic Jacobian and the
absolute structure sheaf add divisor, Picard-monoid, Abel--Jacobi, and
local-point geometry, but do not define a Riemann--Roch mass functional
or the missing middle cohomology on the square.  They therefore do not
supersede this gate.

## 7. Verifier output

```text
TRACE_NORM_MODEL_EXACT: YES
EXACT_DIMENSION_N1: 4
EXACT_DIMENSION_N2: 12
PRIMITIVE_BOUNDARY_COUNTS: YES
BASE3_SURVIVES_ON_SQUARE: NO
LINEAR_RR_GROWTH_SURVIVES: NO
TRACE_NORM_BRANCH: CLOSED_NO_GO
VERDICT: YES
```

The proof is independent of the finite computation; the program certifies
the exact small balls and the arithmetic witness family.
