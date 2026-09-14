# P122 -- singular commutators hit the residue-domain wall

## Status

`PROVED-IN-REPOSITORY` as a no-go theorem.  A logarithmic-derivative
observable can see the critical residue, but its unregularized vector is an
admissible equality-state variation exactly after that residue has already
vanished.  Regularization exposes the positive residue square, but
first-contact positivity supplies only its correct nonnegative sign, not an
upper bound forcing it to be zero.

This closes the last apparent loophole in the commutator-moment route.  It
does **not** prove row (d).

## 1. The singular observable

Write

\[
 E(z)=\xi(\tfrac12+z)
\]

and let `K_F` be the entire Fourier--Laplace transform attached to a compact
window vector `F`.  Near a critical-line zero

\[
 \rho=\tfrac12+i\gamma
\]

of multiplicity `m_rho`, the logarithmic derivative has expansion

\[
 {E'(z)\over E(z)}={m_\rho\over z-i\gamma}+a_\rho(z),       \tag{1.1}
\]

with `a_rho` holomorphic.  Thus every localized logarithmic-derivative
observable has the same singular part, up to sign, as the completed incoming
current audited in phase 121:

\[
 \chi(\tau-gamma){E'\over E}(\sigma+i\tau)
                  K_F(\sigma+i\tau)
 ={m_\rho K_F(i\gamma)\chi(\tau-gamma)
       \over \sigma+i(\tau-gamma)}+R_\sigma(\tau).         \tag{1.2}
\]

Here `chi` is supported in a zero-free punctured neighbourhood of `gamma`
and equals one near `gamma`; the localized remainder is uniformly bounded
in every fixed noncritical Sobolev norm.

The sign in (1.2) is immaterial below.  Using `-zeta'/zeta` instead of
`E'/E` changes the holomorphic Gamma and elementary corrections, not the
critical principal part.

## 2. Exact domain criterion

### Theorem 2.1 -- the residue-domain equivalence

For the observable in (1.2),

\[
 \lim_{\sigma\downarrow0}{
 \left\|\chi {E'\over E}(\sigma+i\,\cdot)
                  K_F(\sigma+i\,\cdot)\right\|_{H^{-1/2}}^2
 \over\log(1/\sigma)}
 =2\pi m_\rho^2|K_F(i\gamma)|^2.                  \tag{2.1}
\]

Consequently the unregularized boundary observable is locally in
`H^(-1/2)` only if

\[
                         K_F(i\gamma)=0.            \tag{2.2}
\]

Conversely, if (2.2) holds, the pole in (1.2) is removable and the localized
observable is in every Sobolev space allowed by its smooth cutoff and
holomorphic remainder.

#### Proof

Equation (1.2) has precisely the Cauchy principal part used in Theorem 2.1
of `P121_CRITICAL_NEGATIVE_HALF_RESIDUE_GATE.md`.  That theorem gives (2.1)
with residue `m_rho K_F(i gamma)`.  A nonzero Cauchy boundary value fails at
the endpoint `H^(-1/2)`, so membership implies (2.2).  If (2.2) holds, write

\[
 K_F(z)=(z-i\gamma)\widetilde K_F(z).
\]

The singular factor in (1.1) then cancels and the localized product is
smooth.  This proves the converse.  QED.

### Corollary 2.2 -- no singular equality-state variation before F2

Let `X_E F` denote any proposed physical variation whose transformed local
component is the boundary value of `(E'/E)K_F`.  If the equality-state form
domain embeds in `L^2` (as does the fixed common form domain in P122.002),
then

\[
 X_EF\in\mathcal Q_T
 \quad\Longrightarrow\quad K_F(i\gamma)=0          \tag{2.3}
\]

at every critical zero tested by `X_E`.

Indeed, a nonzero Cauchy principal part is not even locally `L^2`, and
Theorem 2.1 gives the sharper endpoint obstruction.  Therefore an argument
which substitutes `X_EF` into the first-contact quadratic form has already
assumed the desired critical residue cancellation through its domain
hypothesis.

## 3. Regularization does not force equality

For `sigma>0`, localize (1.2) and call the corresponding admissible smooth
variation `G_sigma`.  At first contact let `H>=0`, `HF=0`, and suppose the
regularized multiplier preserves the required operator domains.  The exact
double-commutator identity is

\[
 \langle F,[X_\sigma^*,[H,X_\sigma]]F\rangle
       =q_H(X_\sigma F)+q_H(X_\sigma^*F)\ge0.       \tag{3.1}
\]

For a symmetric regularization this is `2q_H(X_sigma F)`.  First-contact
positivity proves only the last inequality.

By (2.1), the singular part of the regularized observation has leading
mass

\[
 2\pi m_\rho^2|K_F(i\gamma)|^2\log(1/\sigma).       \tag{3.2}
\]

This is compatible with (3.1) for every value of `K_F(i gamma)`.  To infer
that the coefficient in (3.2) vanishes one would additionally need one of:

1. an independently proved `o(log(1/sigma))` upper bound for the relevant
   form energy;
2. an equality or conservation law making (3.1) zero; or
3. a signed renormalized identity in which all other leading coefficients
   are known and cancel.

None follows from `H>=0` and `HF=0`.  The first is the endpoint regularity
form of F2; the second is equality-state transport; and the third is exactly
the missing nonflat curvature/anomaly theorem required of `D_candidate`.

An abstract model already proves the logical point.  Take
`H=diag(0,1)` on `C^2`, `F=(1,0)`, and choose regularized maps with
`X_sigma F=(0,sqrt(log(1/sigma)))`.  Then `HF=0` and (3.1) equals
`2 log(1/sigma)>0`; positivity places no restriction on its leading
coefficient.

## 4. Relation to the previous commutator audits

`P121_COMMUTATOR_MOMENT_TOMOGRAPHY_NO_GO.md` shows that regular position
commutators produce uncontrolled Gram moments rather than zero moments.
The present theorem handles the complementary idea: choose a singular
multiplier tailored to the zeta divisor so that the commutator directly
sees critical residues.

The two possibilities exhaust this family:

* regular multipliers are admissible but do not force their positive Gram
  terms to vanish;
* divisor-singular multipliers detect the desired residue, but are
  admissible at the boundary only after that residue vanishes.

Thus changing the commutator test function cannot by itself construct row
`D`.  A successful construction must supply new pre-supertrace geometry
that proves an equality or a curvature identity; it cannot obtain that
identity merely by inserting `E'/E` into the already known positive form.

## 5. Verdict for the construction programme

The singular-commutator route is `RETIRED` as an independent proof of F2.
Its useful output is a precise design constraint:

\[
 \boxed{\text{D must control the logarithmic divergence from above, not
 merely recognize its positive coefficient.}}       \tag{5.1}
\]

Equivalently, the next live object must contain a source-defined nonflat
Hermitian metric or an oriented equality law whose anomaly has local
coefficient `2 pi m_rho^2 |K_F(i gamma)|^2`.  Defining that metric by this
coefficient after the fact would be circular; its construction and global
flatness/equality theorem must precede comparison with `B_nuc`.
