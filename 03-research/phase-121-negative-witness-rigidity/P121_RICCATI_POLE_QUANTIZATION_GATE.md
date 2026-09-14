# P121 -- Riccati pole quantization gate

## Status

This note constructs a nonlinear terminal gate strictly weaker than
pointwise F2.  The frozen critical connection

\[
 L_F(z)=\frac{E'(z)}{E(z)}K_F(z),\qquad E(z)=\xi(\tfrac12+z),
                                                               \tag{0.1}
\]

has arbitrary residue `K_F(lambda)` at a simple critical zero.  Its Riccati
curvature

\[
                  \mathcal R_F=L_F'+L_F^2                  \tag{0.2}
\]

has a double pole unless that residue is `0` or `1`.  Applying the same law
to the equally admissible state `iF` leaves only `0`.  Consequently an
equality-state theorem saying that the double-pole support of (0.2) has
zero relative density would close density F2 and the global square.

The pole calculation and descent are proved.  The source theorem reducing
the pole order of `mathcal R_F` is open.  It may not be obtained by declaring
(0.2) to be the logarithmic curvature of a reduced meromorphic divisor;
that declaration already imposes the quantization being proved.

## 1. Exact local calculation

Fix a simple zero `lambda` of `E` and put `x=z-lambda`.  Write

\[
 \frac{E'}E=\frac1x+a_0+O(x),\qquad
 K_F(z)=c+c_1x+O(x^2).                              \tag{1.1}
\]

Then

\[
 L_F(z)=\frac c x+(c_1+a_0c)+O(x),                  \tag{1.2}
\]

and therefore

\[
 \boxed{
 \mathcal R_F(z)
 =\frac{c(c-1)}{x^2}+O(x^{-1}).}                    \tag{1.3}
\]

### Proposition 1.1 -- local Riccati quantization

The Riccati curvature `mathcal R_F` has at most a simple pole at `lambda`
if and only if

\[
                    K_F(\lambda)\in\{0,1\}.          \tag{1.4}
\]

#### Proof

Differentiate (1.2) and square it.  The double-pole coefficients are `-c`
and `c^2`, respectively, and their sum is `c(c-1)`.  QED.

The value `1` is not a normalization choice: it is the second indicial root
of a reduced Riccati divisor.  This is why one copy of the law does not by
itself imply F2.

## 2. Complex-line amplification

The first-contact kernel is complex linear.  Hence `iF` is a first-contact
state whenever `F` is, and

\[
                  K_{iF}(\lambda)=iK_F(\lambda).     \tag{2.1}
\]

### Proposition 2.1 -- two Riccati laws kill the residue

If both `mathcal R_F` and `mathcal R_(iF)` have at most simple poles at
`lambda`, then

\[
                         K_F(\lambda)=0.             \tag{2.2}
\]

#### Proof

Proposition 1.1 gives

\[
 c\in\{0,1\},\qquad ic\in\{0,1\}.
\]

The intersection `\{0,1\}\cap(-i\{0,1\})` is `\{0\}`.  QED.

This is a nonlinear analogue of the two scalar Krein-flux tests in the
parabolic carrier.  Here the nonlinearity does useful work: each individual
law permits a nonzero quantized residue, while the complex radical line
removes it.

## 3. Density version

Let `D_F(R)` count the simple critical zeros `lambda=i gamma`,
`|gamma|<=R`, at which `mathcal R_F` has a double pole.

### Theorem 3.1 -- sparse Riccati curvature implies density F2

Let `F` be a first-contact state.  If

\[
                 D_F(R)+D_{iF}(R)=o(R\log R),       \tag{3.1}
\]

then `F=0`.

#### Proof

Outside a set counted by the left side of (3.1), both Riccati curvatures
have at most simple poles.  Proposition 2.1 gives `K_F(i gamma)=0` there.
Thus the active residue count of
`P121_DENSITY_F2_AND_BOUNDARY_TATE_AUDIT.md` is `o(R log R)`.  Theorem 1.1
of that note gives `F=0`.  QED.

Hence the global square follows from the equality-state pole-order law

\[
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 D_F(R)+D_{iF}(R)=o(R\log R).                       \tag{3.2}
\]

Unlike pointwise framing, (3.2) allows infinitely many double poles and
does not prescribe any critical value of `K_F` individually.

### Theorem 3.2 -- one real parity law is sufficient

The use of both `F` and `iF` can be removed.  A first-contact state of the
real self-adjoint parity block may be chosen real.  If `F` is even, then

\[
 K_F(i\gamma)=2\int_0^T F(t)\cos(\gamma t)\,dt\in\mathbb R, \tag{3.3}
\]

while for odd `F`,

\[
 K_F(i\gamma)=-2i\int_0^T F(t)\sin(\gamma t)\,dt
 \in i\mathbb R.                                          \tag{3.4}
\]

Moreover `F in L1(-T,T)`, so Riemann--Lebesgue gives

\[
                       K_F(i\gamma)\longrightarrow0
                       \quad(|\gamma|\to\infty).          \tag{3.5}
\]

Consequently, if `mathcal R_F` has at most simple poles at all but
`o(R log R)` members of `Sigma_simp`, then `F=0`.

#### Proof

At every reduced-pole critical zero, Proposition 1.1 gives
`K_F(i gamma) in {0,1}`.  In the odd sector, (3.4) makes the intersection
`iR cap {0,1}` equal to `{0}`.  In the even sector, (3.5) excludes the value
`1` at all sufficiently large ordinates.  Thus in either parity the active
residue count is `o(R log R)` plus finitely many points.  Density F2 gives
`F=0`.  QED.

The terminal source theorem can therefore be weakened further to

\[
 P_T\mathscr A_TF=0,quad F\text{ real and parity fixed}
 \Longrightarrow D_F(R)=o(R\log R).                       \tag{3.6}
\]

No second phase-rotated copy is required.

## 4. Determinant interpretation

The two oriented frozen currents have principal parts `-c/x` and `+c/x`.
Their trace has no pole, while their raw determinant has double-pole
coefficient `-c^2`.  The derivative term in (0.2) contributes `-c`; after
the sign convention is aligned with the determinant orientation, the
reduced invariant is the indicial polynomial

\[
                         c(c-1).                    \tag{4.1}
\]

Thus the correct nonlinear object is not the determinant alone but the
Riccati-corrected determinant.  A source construction with only `O_T(R)`
failures of reduced pole order would prove (3.2).

## 5. Source-law firewall

There are two invalid shortcuts.

1. Defining a local solution `u_F` by `u_F'/u_F=L_F` and requiring `u_F`
   to be a single-valued meromorphic section imposes integral residues on
   `L_F`.  On the complex line `aF` this already forces zero and is F2 in
   monodromy language.
2. Declaring `mathcal R_F=u_F''/u_F` to have a reduced divisor imposes
   `c(c-1)=0` at every critical fibre.  That is Proposition 1.1 used as a
   definition, not a source theorem.

A valid proof of (3.2) must instead derive a global pole-complexity bound
from the first-contact equation before examining the critical divisor.  A
candidate source would have to identify the Riccati-corrected determinant
with a row-(a)--(c) object whose double-pole count is independently
`o(R log R)`.  No such identification is established here.

### Proposition 5.1 -- the natural source derivation is tautologically flat

There is a canonical-looking way to make `L_F` a genuine logarithmic
connection, but it does **not** prove Proposition 1.1.  Define the
witness-dependent derivation

\[
                         \delta_F=K_F(z)\partial_z.           \tag{5.1}
\]

Then

\[
                    L_F={\delta_FE\over E}.                  \tag{5.2}
\]

Its genuine Riccati identity is

\[
 \delta_FL_F+L_F^2={\delta_F^2E\over E}.                      \tag{5.3}
\]

Both sides have at most a simple pole at every simple zero of `E`, for
**every** source `F`.

#### Proof

Write `x=z-lambda` and `K_F=c+O(x)`.  Then `L_F=c/x+O(1)`, so the
double-pole coefficients in (5.3) are respectively `-c^2` and `c^2`.
They cancel identically.  Equivalently,
`delta_F E=K_FE'` is nonzero but regular at a simple zero and
`delta_F^2E/E` has only a simple denominator.  QED.

The ordinary Riccati curvature used in (0.2) differs at top polar order:

\[
 \partial_zL_F+L_F^2
 =K_F^{-1}\delta_FL_F+L_F^2,                         \tag{5.4}
\]

and replacing the natural coefficient `K_F` in (5.3) by `1` changes the
automatic cancellation `c^2-c^2=0` into the indicial coefficient
`c^2-c`.  Therefore a source construction cannot justify the ordinary
pole reduction merely by saying that `L_F` is a logarithmic derivative.
The logarithmic derivative is flat for the **source vector field**
`K_F partial_z`; transferring that flatness to `partial_z` already requires
`K_F(lambda) in {0,1}`.  That is the quantization target itself.

This closes a subtle circular shortcut: witness-dependent determinant
geometry produces the wrong derivation, and its reduced pole order carries
no information.

## 6. Corpus comparison and closure state

Phase 70 contains the fixed Euler identity
`delta(A_Euler)+A_Euler^2=Z^{-1}delta^2Z`.  Its connection is independent
of a first-contact witness.  The present calculation concerns the
witness-coupled critical connection `(E'/E)K_F`, its indicial polynomial,
complex-line amplification and density descent.  No occurrence of that
package was found in phases 1--120.

```text
Riccati double-pole coefficient c(c-1)       PROVED
complex-line quantization c=0                PROVED
sufficiency of one real parity law           PROVED
sparse-curvature descent to density F2       PROVED
source pole-order law (3.6)                  OPEN
global square                                CONDITIONAL ON (3.6)
```

No paper-42 change follows from this gate alone.
