# Phase 121 -- exact isodivisor deformation no-go

## Status

This note tests the only scalar determinant deformation which uses the
compact first-contact source without separating prime labels:

\[
 E_\varepsilon(z)=E(z)+\varepsilon E(z)K_F(z)
                  =E(z)(1+\varepsilon K_F(z)),      \tag{0.1}
\]

where `E(z)=xi(1/2+z)` and `K_F` is the compact Laplace transform of the
witness.  In fact it is enough that `1+epsilon K_F` be zero-free for one
nonzero parameter: Paley--Wiener and Hadamard then annihilate the witness.
First contact does not imply that preservation: it fixes every old zero
automatically but does not prohibit the additional zeros of
`1+epsilon K_F`.  Leading zero density cannot see those additional zeros
either.

The result closes the isodivisor shortcut.  It does not prove the global
square.

## 1. Old zeros are preserved for every source

For every entire `K` and every complex `epsilon`,

\[
                         E_\varepsilon=E(1+\varepsilon K). \tag{1.1}
\]

Hence

\[
                         \operatorname {div}(E)
                         \leq\operatorname {div}(E_\varepsilon) \tag{1.2}
\]

as effective divisors, except at the isolated parameters for which
`1+epsilon K` also vanishes at an old zero and increases its multiplicity.
In particular no zero of `E` moves.  This statement is independent of the
first-contact equation.

At a simple zero `lambda` of `E`,

\[
 E_\varepsilon'(\lambda)
 =E'(\lambda)(1+\varepsilon K(\lambda)).            \tag{1.3}
\]

Thus the frozen conormal coefficient `K(lambda)` changes the framing of the
old zero; it does not move that zero.  This is why ordinary infinitesimal
divisor preservation erases precisely the coefficient needed by F2.

## 2. Complete isodivisor rigidity

### Theorem 2.1 -- an affine entire deformation cannot be isodivisor on a complex line

Let `E` be a nonzero entire function and `K` an entire function.  Suppose

\[
             \operatorname {div}(E(1+\varepsilon K))
             =\operatorname {div}(E)                \tag{2.1}
\]

for every `epsilon in C`.  Then `K=0`.

#### Proof

If `K(z_0) != 0`, choose

\[
                         \varepsilon_0=-1/K(z_0).   \tag{2.2}
\]

Then `1+epsilon_0 K` vanishes at `z_0`.  If `E(z_0) != 0`, this creates a
new zero of the left side of (2.1).  If `E(z_0)=0`, it increases the
multiplicity there.  Both contradict equality of effective divisors.
Therefore `K(z)=0` at every point and `K=0`.
QED.

The all-parameter hypothesis of Theorem 2.1 is much stronger than necessary
for a compact source.

### Theorem 2.2 -- one zero-free Paley--Wiener unit is already trivial

Let `K` be an entire function of finite exponential type whose restriction
to the imaginary axis belongs to `L2`, namely

\[
                         x\longmapsto K(ix)\in L^2(\mathbb R). \tag{2.3}
\]

If, for one `epsilon != 0`,

\[
                         1+\varepsilon K             \tag{2.4}
\]

is zero-free on `C`, then `K=0`.

#### Proof

The zero-free entire function (2.4) has order at most one.  Hadamard
factorization therefore gives

\[
                         1+\varepsilon K(z)=e^{az+b} \tag{2.5}
\]

for constants `a,b in C`.  Hence

\[
                         e^{iax+b}-1\in L^2(\mathbb R). \tag{2.6}
\]

If `Im(a)<0`, the first term grows exponentially as `x->+infinity`; if
`Im(a)>0`, it grows as `x->-infinity`.  If `Im(a)=0` and `a!=0`, the
continuous periodic function `|e^(iax+b)-1|^2` has strictly positive mean,
so its integral over `R` diverges.  Thus `a=0`.  A constant belongs to
`L2(R)` only if it is zero, so `e^b=1`.  Equation (2.5) now gives `K=0`.
QED.

### Corollary 2.3 -- one no-new-zero parameter would close F2

For a first-contact radical line `C F`, put

\[
 E_{\varepsilon,F}=E(1+\varepsilon K_F).           \tag{2.7}
\]

If the equality-state source law prohibited additional zeros of (2.7) for
even one fixed `epsilon != 0`, then Theorem 2.2 would give `K_F=0`, hence
`F=0` by injectivity of the compact Laplace transform.  Exact equality of
the complete divisor for the whole parameter line, as in Theorem 2.1, is
therefore unnecessary.  No critical-zero sampling or Cartwright descent
would be needed.

This corollary is a terminal exclusion theorem, not a derivation of its
premise.

## 3. Leading divisor density is blind to the new zeros

Let `F` be supported in `[-T,T]`.  Paley--Wiener gives that `K_F` is entire
of exponential type at most `T` and belongs to the Cartwright class under
the phase-121 graph regularity already proved.  Therefore, for each fixed
`epsilon != 0`,

\[
 N_{1+\varepsilon K_F}(R)=O_F(R).                  \tag{3.1}
\]

On the other hand the Riemann--von Mangoldt formula gives

\[
 N_E(R)={R\over\pi}\log R+O(R).                   \tag{3.2}
\]

Consequently

\[
 N_{E(1+\varepsilon K_F)}(R)
 =N_E(R)+O_F(R)                                    \tag{3.3}

\]

with the same `R log R` principal term for every compact source, including
every nonzero one.  Thus preservation of order, exponential type, the
functional-equation main count, or the leading zero density does not imply
complete isodivisor preservation.

The lower-order `O(R)` term is not negligible for the desired conclusion:
it is exactly the maximal zero density available to a nonzero compact
Laplace transform.  Controlling it pointwise enough to rule out every new
zero is the zero-free assertion of Theorem 2.2, not a consequence of
Riemann--von Mangoldt.

## 4. Why first contact does not supply complete isodivisor transport

First contact is the linear equality

\[
                         P_T\mathscr A_TF=0.        \tag{4.1}
\]

It implies the full polarized family `q_T(F,G)=0` for primitive tests `G`.
Neither statement refers to the zero set of `1+epsilon K_F`.  The local
universal model

\[
                         E(z)=z,\qquad K(z)=c       \tag{4.2}
\]

already preserves the old divisor at `z=0` for every `c`, while
`E(1+epsilon c)` has the same old zero and the conormal framing coefficient
remains arbitrary.  For nonconstant `K`, additional zeros occur away from
the old divisor and are invisible to this local package.

The genuine determinant variation confirms the typing.  Its logarithmic
connection varies by

\[
 \left.\partial_\varepsilon{E_\varepsilon'\over E_\varepsilon}
 \right|_{\varepsilon=0}=K_F',                     \tag{4.3}
\]

because the two copies of `(E'/E)K_F` cancel.  Therefore ordinary
single-valuedness and flatness of the determinant deformation see the
derivative of the unit, not its value on the critical fibres.

Asserting that (4.1) forbids the new zeros of `1+epsilon K_F` for one
nonzero parameter would add an equality-state law with F2 force.  Theorem
2.2 shows why that assertion closes the problem; it does not make it
available.

## 5. Corpus audit and verdict

Phase 121's source-framing audit already proves (4.3) and distinguishes the
frozen current from a genuine determinant variation.  The one-parameter
zero-free Paley--Wiener theorem and the density comparison (3.1)--(3.3) were
not found in phases 1--120.  They sharpen the rejection but do not derive
the terminal equality-state law.

```text
preservation of every old E-zero                   AUTOMATIC
one zero-free factor 1+epsilon K_F, epsilon!=0      IMPLIES K_F=0
leading R log R density preservation               AUTOMATIC, INSUFFICIENT
first contact implies one zero-free deformation     NOT PROVED (F2 FORCE)
global square                                       OPEN
```

No modification of paper 42 follows from this no-go.
