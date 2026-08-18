# 107.178 -- The equivariant boundary class recovers the local explicit term

## 1. Derived fixed-point determinant

Let \(F\) be a local field and let

\[
 m_u(x)=ux,qquad u\in F^\times,quad u\neq1,
\]

act on the transverse line at a monoidal boundary fixed point.  The
linearized graph--diagonal equation is

\[
 (1-u)x=0.
\]

The corresponding one-term Koszul differential on the normal line is
multiplication by \(1-u\).  Its determinant, or equivariant Euler class,
is therefore

\[
 e_u=\det(1-dm_u)=1-u.
 \tag{1.1}
\]

Equivariant fixed-point localization inverts this Euler class.  Define
the local boundary class

\[
 \mathscr L_u=e_u^{-1}=(1-u)^{-1}.
 \tag{1.2}
\]

Applying the normalized absolute value gives

\[
 |\mathscr L_u|_v={1\over|1-u|_v},
 \tag{1.3}
\]

which is exactly the local factor in the published distributional trace
formula.

This is a derivation, not a definition chosen to fit the answer:
\(1-u\) is forced by the differential of the actual graph--diagonal
Koszul complex, and inversion is the standard localization operation for
a fixed stratum.

## 2. Resolution of the excess fibre

For \(F=\mathbb Q_p\) and \(u=1+p^k\), the ordinary integral
intersection in `107_177` has a vertical excess component.  Its normal
Euler class is

\[
 e_u=-p^k,
\]

and hence

\[
 |e_u^{-1}|_p=p^k.
\]

Thus equivariant localization records exactly the information lost when
ordinary proper intersection fails.  It does not assign length \(p^k\)
to the excess scheme; it replaces the noninvertible normal Euler class
by its inverse in the localized coefficient theory.

## 3. Invariance and products

The class is invariant under every change of transverse coordinate
\(x'=ax\), because conjugating the one-dimensional derivative leaves
\(u\) unchanged.

For a direct sum of transverse characters \(u_1,\ldots,u_r\), the
Koszul complex is the tensor product of the one-dimensional complexes,
so

\[
 e_{\boldsymbol u}=\prod_{j=1}^r(1-u_j),
 \qquad
 |e_{\boldsymbol u}^{-1}|_v
 =\prod_{j=1}^r{1\over|1-u_j|_v}.
 \tag{3.1}
\]

This is the exact multiplicativity required of a normal localization
class.

## 4. Result and strict scope

The local gap exposed in `107_176`--`107_177` is closed:

\[
 \boxed{
 \text{monoid boundary + transverse Koszul determinant + localization}
 \Longrightarrow {1\over|1-u|_v}.}
\]

This supplies the correct local realization of the geometric side of
the explicit formula.  It does **not** yet supply:

1. a global compactified boundary object over
   \(\mathrm{Spec}\,\mathbb Z\);
2. a global bilinear intersection pairing on localized classes;
3. the archimedean Green-current completion;
4. an arithmetic Hodge-index theorem for this equivariant theory.

Accordingly row (c) is not promoted.  The next exact question is whether
the local classes (1.2) glue over the Abel--Jacobi image and admit a
global trace/pairing compatible with the semilocal sheaf of crossed
product algebras.

## 5. Falsifier

The verifier evaluates the forced determinant and its normalized
absolute value for the same 20 p-adic samples used by `107_177`, for
archimedean rational samples, and for multi-character products.  It also
checks invariance under nontrivial coordinate conjugations.  Any
mismatch with (1.3) returns `VERDICT: NO`.
