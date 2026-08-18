# 107.175 -- Universal arithmetic linking has no source-only component selector

## 1. The new channel

Connes--Consani's 2026 arithmetic Jacobian equips the universal
Abel--Jacobi cover with the arithmetic linking homomorphism.  For a
rational prime \(p\), its image in every finite abelian quotient is the
Artin symbol \(\operatorname{Frob}_p\).  Morishita's bridge preserves
this Galois action and the corresponding closed prime orbit.

This channel is strictly richer than the valuative package rejected in
`107_133`: it contains the values of every abelian character unramified
at \(p\).  The question is whether it canonically selects the character
needed by a local intersection target.

## 2. The forcing pair at 2

Retain the real curves

\[
 20\mathrm{a}1@2,\qquad 36\mathrm{a}4@2.
\]

Both have type \(IV^*\), and the geometric component group is
\(\Phi_{\overline{\mathbb F}_2}\simeq\mathbb Z/3\mathbb Z\).  Their
rational Tamagawa numbers are

\[
 c_2(20\mathrm{a}1)=3,\qquad c_2(36\mathrm{a}4)=1.
\]

An automorphism of \(\mathbb Z/3\mathbb Z\) is either the identity,
with three fixed points, or inversion, with one fixed point.  Hence the
two targets require opposite Frobenius actions:

\[
 \rho_{20\mathrm{a}1}(F_2)=+1,qquad
 \rho_{36\mathrm{a}4}(F_2)=-1.
 \tag{2.1}
\]

## 3. Capacity is not a selector

The universal linking datum at \(p=2\) contains both signs.  For
example, the quadratic characters of fundamental discriminants \(-7\)
and \(5\) are unramified at 2 and satisfy

\[
 \left({-7\over2}\right)=+1,
 \qquad
 \left({5\over2}\right)=-1.
 \tag{3.1}
\]

Thus universal linking has enough **capacity** to represent either
component action.  But its complete source value \(\operatorname{lk}_2\)
is the same for both curves: it is attached to the rational prime 2,
not to a chosen elliptic curve.  A target-independent rule applied to
that same input can select only one quotient character, whereas (2.1)
requires two different outputs.

Selecting \(\chi_{-7}\) for one curve and \(\chi_5\) for the other is
not a source construction.  It imports a target-dependent quotient of
\(\operatorname{Gal}(\mathbb Q^{\rm ab}/\mathbb Q)\), exactly the
component datum that the realization was required to produce.

## 4. No-go and remaining route

Therefore adjoining the **universal** rooted/linking datum to the
prime/Gamma source does not by itself reopen the old \(S3\) target:

\[
 \boxed{
 (p,\operatorname{lk}_p)\ \text{has Galois capacity but no
 target-independent component selector}.}
\]

This is not a no-go for arithmetic linking in the correct Riemann-zeta
target.  It proves only that the 20a1/36a4 component collision cannot be
solved by citing the universal cover without also deriving a canonical
quotient from the zeta source.  Row (c) can be reopened by this channel
only after either:

1. the required divisors are proved component-trivial, so no selector is
   needed; or
2. a quotient character is derived canonically from the source test
   function and is shown to enter the actual local pairing.

## 5. Falsifier

The Sage verifier loads both Cremona curves, checks their real local
data at 2, infers the two actions on the geometric component group, and
computes the two unramified quadratic character values in (3.1).  It
returns `VERDICT: NO` if the targets do not differ or if the same
source-only selector could realize both.
