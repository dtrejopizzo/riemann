# P121 -- density F2 and the boundary--Tate audit

## Status

Pointwise critical framing is stronger than the global-square argument
needs.  It is enough to prove that the nonzero oriented residues of a
first-contact state have zero relative density inside an unconditional
superlinear family of simple critical zeros.  The density descent is proved
below; the equality-state sparsity law is not yet proved.

The second part audits the tempting boundary--Tate closure.  Packaging the
two logarithmic endpoint coefficients and the two Tate multipliers into a
four-dimensional matrix does not produce an independent determinant: its
injectivity is first-contact exclusion in boundary coordinates.

## 1. The sparse-residue terminal theorem

Let `Sigma_simp` be a family of simple critical-line zeros satisfying

\[
 N_{\rm simp}(R)
 :=\#\{\tfrac12+i\gamma\in\Sigma_{\rm simp}:|\gamma|\le R\}
 \gg R\log R .                                           \tag{1.1}
\]

For a compact-window source put

\[
 K_F(z)=\int_{-T}^{T}F(t)e^{-zt}\,dt
\]

and define

\[
 N_F^{\rm act}(R)
 :=\#\{\tfrac12+i\gamma\in\Sigma_{\rm simp}:|\gamma|\le R,
                     K_F(i\gamma)\ne0\}.                 \tag{1.2}
\]

### Theorem 1.1 -- density F2 is sufficient

If

\[
             N_F^{\rm act}(R)=o(R\log R),                 \tag{1.3}
\]

then `F=0`.

#### Proof

The number of members of `Sigma_simp` at which `K_F` vanishes is

\[
 N_{\rm simp}(R)-N_F^{\rm act}(R)\gg R\log R.             \tag{1.4}
\]

If `F` were nonzero, `K_F` would be a nonzero Cartwright entire function of
exponential type at most `T`.  Its zero counting function in `|z|<=R` is
`O_T(R)`, contradicting (1.4).  Hence `K_F` is identically zero.  Injectivity
of the compact-support Laplace transform gives `F=0`.  QED.

### Corollary 1.2 -- pointwise framing is stronger than needed

To exclude a first-contact state it suffices to prove

\[
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 N_F^{\rm act}(R)=o(R\log R).                           \tag{1.5}
\]

No particular residue must be identified or annihilated.  Finitely many,
`O_T(R)`, or any zero-relative-density family of surviving critical
monodromies is harmless.  F2 makes the active count identically zero, so
(1.5) is a strict logical weakening.

## 2. Pole-support formulation

The oriented current

\[
 \mathcal H_{+,T}F(z)
 =-\frac{\zeta'}{\zeta}(\tfrac12+z)K_F(z)-Q_{+,T}(z)       \tag{2.1}
\]

has residue `-K_F(i gamma)` at a simple critical zero.  Since `Q_(+,T)` is
entire, (1.5) is equivalently

\[
 \#\{i\gamma\in\Sigma_{\rm simp}:|\gamma|\le R,
       \operatorname {Res}_{i\gamma}\mathcal H_{+,T}F\ne0\}
 =o(R\log R).                                           \tag{2.2}
\]

Thus the missing source law need not fix the unit framing fibre by fibre.
It may instead prove a global complexity bound on the antisymmetric port.
Any independently sourced theorem putting its critical pole support in a
class with `O_T(R)` counting closes the square through Theorem 1.1.  Defining
such a class by deleting the poles of (2.1) would be circular.

## 3. Finite critical energy is not enough

The negative-half residue theorem assigns the positive mass

\[
 8\pi\sum |K_F(i\gamma)|^2.                            \tag{3.1}
\]

Even finiteness of (3.1) would not imply (1.3): a square-summable sequence
may be nonzero at every index.  The revised target is a support or
finite-complexity theorem, not another norm bound.

## 4. Boundary--Tate closure does not supply sparsity

The logarithmic Dirichlet model suggests two endpoint coefficients
`c_-`, `c_+` multiplying the sharp germ

\[
             (\log(1/d))^{-1/2}.                         \tag{4.1}
\]

A first-contact equation also has two Tate multipliers `alpha`, `beta`.
It is tempting to assert that the equation and the two primitive moments
give an invertible four-by-four system in

\[
                 (c_-,c_+,\alpha,\beta).                 \tag{4.2}
\]

This is not an external closure mechanism.  Forming the matrix requires
solving the compressed Gamma--Euler boundary problem, whose homogeneous
kernel is precisely the first-contact space.  If the boundary solution map
uses the inverse compressed operator, its existence already excludes first
contact.  If it is defined modulo the homogeneous kernel, (4.2) does not
determine that component.  Proving injectivity of the homogeneous boundary
matrix is therefore first-contact exclusion in new coordinates.

The moment-corrected endpoint counterexample in
`P121_F2_SOURCE_FLUX_AND_FRAMING_AUDIT.md` also proves that the two moments
alone do not kill `c_-` and `c_+`.  The equation could still supply an
Euler-specific boundary law, but the dimension match `2+2` is not one.

## 5. Revised terminal target

```text
first contact
 -> equality-state pole-support law (2.2)       OPEN
 -> density F2, Theorem 1.1                     PROVED
 -> F = 0                                       PROVED
 -> no first contact / global square             CONDITIONAL
 -> cofinal limit / row (d)                      CONDITIONAL
```

No change to paper 42 follows until (2.2) is proved.
