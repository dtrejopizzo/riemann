# 107.179 -- The localized boundary class has no ordinary Arakelov forgetful map

## 1. Coefficient rings

Let \(T=\mathbb G_m\) act on the one-dimensional normal direction.  Its
representation ring is

\[
 R(T)=\mathbb Z[t,t^{-1}],
\]

where \(t\) is the normal character.  The local class constructed in
`107_178` lives in

\[
 R(T)[(1-t)^{-1}].
 \tag{1.1}
\]

Forgetting the equivariant structure on an candid \(T\)-equivariant
bundle sends every one-dimensional character to its rank.  On
coefficients this is the augmentation

\[
 \epsilon:R(T)\longrightarrow\mathbb Z,
 \qquad \epsilon(t)=1.
 \tag{1.2}
\]

## 2. Nonextension theorem

There is no unital ring homomorphism

\[
 \widetilde\epsilon:R(T)[(1-t)^{-1}]\longrightarrow A
 \tag{2.1}
\]

to any nonzero ring \(A\) that extends (1.2).  Indeed, in the localized
ring,

\[
 (1-t)(1-t)^{-1}=1.
\]

Applying a hypothetical extension gives

\[
 (1-1)\widetilde\epsilon((1-t)^{-1})=1_A,
\]

hence \(0=1_A\), a contradiction.

This is the universal property of localization: a map extends only when
the image of every inverted element is a unit.  Here the inverted Euler
class maps to zero.

## 3. Consequence for rows (c) and (d)

The local factor \((1-t)^{-1}\) cannot be forgotten term-by-term into
ordinary Chow groups, ordinary adelic line bundles, or arithmetic
intersection theory.  In particular it does not directly define an
object in the published domains of Faltings--Hriljac, Yuan--Zhang, or
ordinary numerical cohomology for arithmetic surfaces.

This establishes a hard fork:

1. **global cancellation:** after assembling all local terms, prove that
   the localization denominators cancel and the resulting class lies in
   the unlocalized arithmetic theory; or
2. **equivariant Hodge theory:** construct and prove an index theorem
   directly in the localized equivariant theory.

Neither option follows from the distributional trace formula alone.
The pole at \(t=1\) and the semilocal white-light term show that any
global cancellation must include the generic-point subtraction; it
cannot occur independently at each place.

Thus `107_178` closes the local numerical factor but does not by itself
join row (c) to the existing row-(d) theorems.

## 4. Scope

This is not a no-go for every equivariant arithmetic Hodge theorem, nor
does it prove that global denominators cannot cancel.  It proves the
specific and unavoidable statement that the standard forgetful map does
not extend across the localization required by the local explicit
formula.

## 5. Falsifier

The verifier constructs the Laurent coefficient ring, confirms that
\(1-t\) is not a unit before localization, imposes its inverse, and
checks the augmentation relation.  It repeats the contradiction for
finite character products and verifies that no nonzero target ring can
satisfy the required equation.  If an ordinary augmentation extension
exists, it returns `VERDICT: NO`.
