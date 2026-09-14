# P121 -- multiplicative first character before scalar supertrace

## Status

This note constructs a source-defined multiplicative carrier for the
antisymmetric critical jet.  It is genuinely prior to `dlog` and to the
scalar supertrace of row (c).

The construction proves an exact equivalence:

```text
F2 at every simple critical point
<=> the relative K_2 class below is unramified there.
```

It does not prove that first contact makes the class unramified.  Two
tempting shortcuts are ruled out exactly: Adams-weight separation is not
available on a fixed localization window, and global reciprocity retains
an essential contribution at infinity.  No row-(d) or RH claim is made.

## 1. The relative symbol

Let

\[
 E(z)=\xi(1/2+z),\qquad
 K_F(z)=\int_{-T}^{T}F(t)e^{-zt}\,dt,
 \qquad R_\epsilon=\mathcal O(\mathbb C)[\epsilon]/(\epsilon^2).
\]

Since `1+epsilon K_F` is a unit in `R_epsilon`, define the relative Milnor
symbol

\[
 \boxed{\quad
 \kappa_F:=\{E,1+\epsilon K_F\}
 \in K_2^M(\mathcal M(\mathbb C)[\epsilon]/(\epsilon^2),
             (\epsilon)).\quad}                    \tag{1.1}
\]

Here `M(C)` denotes the meromorphic function field.  The class is linear
to first order in `F`, but it is constructed multiplicatively, before
applying a logarithmic derivative or a trace.

The relative `dlog`/Bloch coordinate is

\[
 \operatorname{bl}(\kappa_F)
   =K_F\,{dE\over E}.                               \tag{1.2}
\]

Thus the frozen-source current `(E'/E)K_F`, whose scalar Real sum loses its
critical residues, is the differential shadow of one relative `K_2`
class.

## 2. Exact tame-symbol calculation

Let `lambda` be a simple zero of `E`, let `O_lambda` be the local ring and
let `partial_lambda` be the tame symbol.  Since

\[
 v_\lambda(E)=1,
 \qquad v_\lambda(1+\epsilon K_F)=0,
\]

the tame-symbol formula gives

\[
 \begin{aligned}
 \partial_\lambda\kappa_F
 &=(-1)^{0}\left.
   {E^0\over(1+\epsilon K_F)^1}\right|_\lambda\\
 &=(1+\epsilon K_F(\lambda))^{-1}
  =1-\epsilon K_F(\lambda).                       \tag{2.1}
 \end{aligned}
\]

### Theorem 2.1 -- F2 is relative unramifiedness

On the simple critical divisor,

\[
 \boxed{
 \partial_\lambda\kappa_F=1
 \quad\Longleftrightarrow\quad
 K_F(\lambda)=0
 \quad\Longleftrightarrow\quad
 H_F=EK_F\in(E)^2_\lambda.}                       \tag{2.2}
\]

Consequently

\[
 \kappa_F\text{ is unramified at every }
 \lambda\in\Sigma_{\rm simp}
 \quad\Longleftrightarrow\quad \nu_T(F)=0.        \tag{2.3}
\]

By the already proved Cartwright faithfulness theorem, either side of
(2.3) implies `F=0`.

### Proof

Equation (2.1) proves the first equivalence.  The second is the local
conormal dictionary

\[
 [EK_F]=K_F(\lambda)[E]\quad\text{in }(E)/(E)^2.
\]

Taking all simple critical points proves (2.3), and phase 121 supplies the
last assertion.  QED.

## 3. Relation with the two oriented jets

Let the two causal orientations act by `epsilon -> +/- epsilon`.  Then

\[
 \partial_\lambda\{E,1+\epsilon K_F\}
    =1-\epsilon K_F(\lambda),
 \qquad
 \partial_\lambda\{E,1-\epsilon K_F\}
    =1+\epsilon K_F(\lambda).                     \tag{3.1}
\]

Their infinitesimal tame symbols are the two normal coefficients
`-nu_T(F)` and `+nu_T(F)` of F1.  Adding them after `dlog` gives zero for
every `F`; retaining the relative symbols keeps both orientations and
their ramification separately.

This is the minimal multiplicative refinement of row (c): the existing
scalar character is obtained only after applying `dlog`, taking the two
orientations and then supertracing.  The antisymmetric jet is already lost
at that last step.

## 4. Why Adams weights do not yet close the class

Formally, Milnor `K_2` has Adams weight two.  On symbols,

\[
 \psi^m\{f,g\}=\{f^m,g^m\}=m^2\{f,g\}             \tag{4.1}
\]

after rationalization and additive notation.  It is tempting to compare
this with the two polar/Tate lines and separate distinct weights.

That argument is not available for the localized first-contact equation.
On row-(b) correspondences, `psi^m` sends a displacement `log p` to
`m log p`.  At fixed `T` this changes the active contact set, does not
preserve `P_T`, and does not commute with the quarter-Gamma compression.
Therefore

\[
 P_T\mathscr A_TF=0
\]

has not been lifted to an Adams-equivariant equality containing
`kappa_F`.  Declaring such a lift would insert the missing source law.

## 5. Why global reciprocity does not localize F2

For an ordinary scalar parameter `a`, the symbol
`{E,1+aK_F}` has additional tame factors at the zeros of `1+aK_F`.
They cancel the factors at the Euler divisor in the global product formula.

Passing to dual numbers makes `1+epsilon aK_F` a unit at every finite
point, but `K_F` is an entire function of exponential type rather than a
rational function on the compactified line.  The analytic reciprocity law
then has a boundary symbol at infinity.  That symbol is the multiplicative
form of the exterior/annular defect already isolated in phase 121.  The two
Tate zeros cancel the polar points `s=0,1`; they do not make the infinity
symbol trivial.

Hence neither the product formula nor variation in `a` proves (2.3).

## 6. Exact remaining theorem in this carrier

The equality-state theorem would now read

\[
 \boxed{
 F\in\mathcal P_T,\quad P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 \kappa_F\text{ is unramified on }\Sigma_{\rm simp}.} \tag{6.1}
\]

By Theorem 2.1, (6.1) is F2 itself, not a weaker intermediate result.  Its
value is typing: it shows that the missing datum is multiplicative
ramification before `dlog`, not another additive trace, positive lift,
torsion anomaly or scalar boundary identity.

## 7. Ledger

```text
relative K_2 carrier kappa_F                         PROVED
tame symbol = 1 - epsilon K_F(lambda)               PROVED
F2 <=> unramifiedness on the simple critical divisor PROVED
compatibility with the two frozen causal jets        PROVED
Adams separation at fixed T                          UNAVAILABLE
reciprocity without an infinity symbol               FALSE
first contact => unramifiedness                       OPEN (F2)
global square and row (d)                             OPEN
```

No modification of paper 42 follows from this construction alone.

## 8. Exact boundary symbol and the off-line cancellation

Let `Omega` be a bounded domain with smooth boundary avoiding the zeros of
`E`.  The infinitesimal Contou--Carrere boundary symbol of (1.1) is

\[
 \boxed{
 \log\langle E,1+\epsilon K_F\rangle_{\partial\Omega}
 =-\epsilon {1\over2\pi i}
     \int_{\partial\Omega}K_F\,{dE\over E}
 =-\epsilon\sum_{\lambda\in\Omega}
       m_\lambda K_F(\lambda).}                    \tag{8.1}
\]

The sign agrees with the tame-symbol convention in (2.1).  Equation (8.1)
is just the residue theorem, but it identifies exactly what the previously
unnamed infinity symbol contains.

For a real source put

\[
 Q_F(z)=K_F(z)K_F(-z)
\]

and form the quadratic relative symbol
`{E,1+epsilon Q_F}`.  At an on-line zero `lambda=i gamma`,

\[
 Q_F(i\gamma)=K_F(i\gamma)K_F(-i\gamma)
              =|K_F(i\gamma)|^2.                  \tag{8.2}
\]

At an off-line reflected orbit, the residues instead pair the two distinct
values on that orbit and give the hyperbolic block of the spectral Weil
form.  Exhausting the completed divisor in (8.1), with the standard polar
regularization, therefore recovers the spectral quadratic form: critical
positive squares and off-line hyperbolic terms occur in the same boundary
symbol.

Consequently first contact makes the complete regularized quadratic
boundary symbol vanish, but does not make each tame symbol trivial.  The
implication

\[
 \text{zero total boundary symbol}
 \Longrightarrow
 \partial_\lambda\kappa_F=1\quad(\lambda\in\Sigma_{\rm simp})
                                                               \tag{8.3}
\]

is precisely the forbidden inference from a signed sum to its positive
critical summands.  It cannot be used as the source theorem for (6.1).

## 9. Rank-one provenance is not yet present in `kappa_F`

The construction (1.1) depends only on the completed meromorphic function
`E` and the compact transform `K_F`.  The same construction applies
verbatim to a shifted rank-two product

\[
 E_a(z)=\xi(1/2+z+a)\xi(1/2+z-a),
\]

whose localized Weil form has negative directions.  Hence no theorem based
only on the formal properties of the pair `(E,K_F)`, relative `K_2`, tame
symbols and global reciprocity can prove (6.1).

A surviving source law must lift `kappa_F` through the place-resolved row-(b)
package before multiplying the Euler factors.  At each prime that package
has one Frobenius conormal line for zeta and two for the shifted pair.  The
required construction is therefore not another global symbol: it is a
rank-one-provenance lift whose pushforward is (1.1) and whose equality-state
law becomes false when the local fibre has rank two.

This is a firewall, not a construction of that lift.

## 10. The finite place-resolved lift

Use the central coordinate `s=1/2+z` and put

\[
 e_p(z)=1-p^{-1/2-z},\qquad u_F(z)=1+\epsilon K_F(z).
                                                               \tag{10.1}
\]

For a finite prime set `S`, define

\[
 \boxed{
 \widetilde\kappa_{S,F}
 :=\bigl(\{e_p,u_F\}\bigr)_{p\in S}
 \in\bigoplus_{p\in S}
 K_2^M(\mathcal M(\mathbb C)[\epsilon]/(\epsilon^2),
       (\epsilon)).}                                  \tag{10.2}
\]

Let `Sigma_S` be addition of symbols.  Bilinearity in the first entry gives

\[
 \boxed{
 \Sigma_S(\widetilde\kappa_{S,F})
 =\left\{\prod_{p\in S}e_p,u_F\right\}.}           \tag{10.3}
\]

This is a genuine place-resolved object: the direct-sum label is retained
until `Sigma_S` is applied.  For a shifted degree-two Euler package there
are instead two summands at each prime,

\[
 e_{p,+a}(z)=1-p^{-1/2-z-a},\qquad
 e_{p,-a}(z)=1-p^{-1/2-z+a}.                       \tag{10.4}
\]

Thus (10.2), unlike the global class (1.1), distinguishes local rank one
from local rank two before pushforward.

## 11. Regulator compatibility with row (b)

The relative Bloch coordinate of the `p` component is

\[
 \operatorname{bl}(\widetilde\kappa_{p,F})
 =K_F(z){de_p(z)\over e_p(z)}.                    \tag{11.1}
\]

On `Re z>1/2`, absolute convergence gives

\[
 {de_p\over e_p}
 =\sum_{j\ge1}(\log p)p^{-j(1/2+z)}\,dz.          \tag{11.2}
\]

Therefore

\[
 \operatorname{bl}(\widetilde\kappa_{p,F})
 =K_F(z)\sum_{j\ge1}
   {\log p\over p^{j/2}}e^{-jz\log p}\,dz.        \tag{11.3}
\]

The coefficient and displacement in (11.3) are exactly the determinant
degree and central metric of the row-(b) contact at `(p,j)`.  Summing over
`p` gives the positive causal orientation of row (c), before Real reflection
and before scalar supertrace.

For finite `S`, (10.3) and (11.1) commute exactly with the Bloch map.  The
cofinal lift is consequently defined as the restricted product whose
regulator converges on `Re z>1/2`; its pushforward is the finite-place part
of `K_F dlog E` there.  Analytic continuation is taken only after this
pushforward, exactly as in row (c).  No termwise continuation of the
infinite prime direct sum is asserted.

## 12. Local tame coordinates

The zero set of `e_p` is

\[
 \lambda_{p,k}=-{1\over2}+{2\pi i k\over\log p},
 \qquad k\in\mathbb Z,                              \tag{12.1}
\]

and every zero is simple.  Hence

\[
 \boxed{
 \partial_{p,k}\widetilde\kappa_{p,F}
 =1-\epsilon K_F(\lambda_{p,k}).}                  \tag{12.2}
\]

The Tate condition is the resonant coordinate

\[
 K_F(-1/2)=0,
 \qquad\partial_{p,0}\widetilde\kappa_{p,F}=1     \tag{12.3}
\]

for every prime.  Thus primitivity trivializes the common `k=0` tame
symbol but says nothing by itself about `k!=0`.

### Theorem 12.1 -- cofinal first-harmonic rigidity

Let `P` be any infinite set of primes.  If

\[
 \partial_{p,1}\widetilde\kappa_{p,F}=1
 \qquad(p\in P),                                   \tag{12.4}
\]

then `F=0`.

### Proof

By (12.2),

\[
 K_F\left(-{1\over2}+{2\pi i\over\log p}\right)=0
 \qquad(p\in P).                                   \tag{12.5}
\]

The distinct points in (12.5) converge to `-1/2`.  Since `K_F` is entire,
the identity theorem gives `K_F=0`.  Fourier--Laplace injectivity gives
`F=0`.  QED.

This is the multiplicative `K_2` form of the first-harmonic accumulation
theorem in `P121_ALL_PRIME_SEAM_DIVERGENCE_THEOREM.md`; here the sampled
number is identified as a tame ramification coefficient.

## 13. The one remaining source implication

After Sections 10--12, the desired equality-state law has the concrete
place-resolved form

\[
 \boxed{
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 \partial_{p,1}\widetilde\kappa_{p,F}=1
 \quad\text{for infinitely many inactive primes }p.}  \tag{13.1}
\]

The conclusion of (13.1) closes first contact by Theorem 12.1 and hence
closes the global square by the proved nesting theorem.

Equation (13.1) is not supplied merely by inactivity.  If
`log p>2T`, the direct compressed translation vanishes, but the periodic
exterior seam has first coefficient

\[
 K_F\left(-{1\over2}+{2\pi i\over\log p}\right),  \tag{13.2}
\]

which need not vanish.  Therefore (13.1) is exactly an equality-state
boundary transport law, now expressed before the Euler factors are
multiplied.  The lift and its faithful terminal descent are constructed;
derivation of (13.1) from first contact remains the unresolved step.

## 14. Subsequent oriented localization refinement

`P121_ORIENTED_K2_LOCALIZATION_EXACTNESS.md` constructs the actual finite
relative localization sequence behind Sections 10--13 and corrects the
cofinal recipient.  Because the first-harmonic Euler divisors accumulate at
the Tate point, the cofinal target is not an ordinary Gersten direct sum.
It is the analytic-germ space obtained from the samples

\[
 K_F\left(-\frac12+\frac{2\pi i}{\log p}\right),\qquad p\to\infty.
\]

The two oriented tame symbols split exactly into the scalar character of
row (c) and a first oriented character `c^(1)`.  The latter is the complete
Taylor germ of `K_F` at `-1/2`, and its vanishing is equivalent to `F=0`.
Accordingly (13.1) can be weakened from exact vanishing at infinitely many
places to infinite-order cofinal flatness, but its derivation from first
contact remains the same source-compatibility problem.
