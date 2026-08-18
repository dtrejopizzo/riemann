# 106.107 — Theta residue Poisson duality and the amplitude gate

## 1. Purpose

The zero residue of the theta--divisor current is the already known
Möbius connection.  The only arithmetic information not used by that
current is carried by the nonzero residue classes of the rational theta
lattice.  This note computes those classes exactly before any square is
taken.

There is an exact finite Fourier--Poisson identity.  It sends an additive
character on the rational lattice (n^{-1}\mathbb Z) to one congruence
class on the reflected integer lattice.  In particular, it gives a second
exact formula for the complete fractional theta remainder.  The formula
retains phases and is specific to the actual Gaussian theta kernel.

The calculation also identifies the next obstruction.  Poisson duality is
linear in the theta masses (k_y), whereas the physical source norm is
quadratic in amplitudes and therefore uses their positive square roots.
The reflected character masses are signed.  Consequently finite Fourier
Parseval cannot be applied to the physical norm without introducing a new
signed amplitude operator.  Its contractivity is exactly the canonical
transfer norm computed in 106.105.

No zero location is used below.

## 2. The primitive Gaussian and the differentiated theta atom

For (y\geq0) and (x\in\mathbb R), put

\[
 f_y(x)=e^{x/2}e^{-\pi y^2e^{2x}}.
 \tag{1}
\]

Let (D=d/dx).  Direct differentiation gives

\[
 \boxed{
 k_y(x)=\frac12(D^2-\tfrac14)f_y(x)
 =\pi y^2e^{5x/2}(2\pi y^2e^{2x}-3)
   e^{-\pi y^2e^{2x}}.}
 \tag{2}
\]

Thus (k_0=0), and for (y>0) formula (2) is the continuous theta atom
used throughout 106.38--106.65.  All Gaussian series below converge
normally on compact subsets of (x\), and the same remains true after two
derivatives.  Poisson summation and application of (D^2-1/4) may
therefore be interchanged.

## 3. Exact finite-character Poisson formula

Fix (n\geq2) and (a\in\{0,\ldots,n-1\}).  Define the character sum

\[
 \mathcal K_{n,a}(x)
 :=\sum_{j\in\mathbb Z}k_{|j|/n}(x)
       e^{2\pi iaj/n}.
 \tag{3}
\]

It is real, because the terms (j) and (-j) are conjugate.

### Theorem 1 — Residue-character modular duality

For every real (x),

\[
 \boxed{
 \mathcal K_{n,a}(x)
 =n\!\sum_{\substack{\ell\in\mathbb Z\\
                 \ell\equiv-a\ ({\rm mod}\ n)}}
       k_{|\ell|}(-x).}
 \tag{4}
\]

#### Proof

Poisson summation for the shifted Gaussian gives

\[
\begin{aligned}
 \sum_{j\in\mathbb Z}f_{|j|/n}(x)e^{2\pi iaj/n}
 &=e^{x/2}\sum_{j\in\mathbb Z}
   e^{-\pi e^{2x}j^2/n^2}e^{2\pi iaj/n}\\
 &=ne^{-x/2}\sum_{m\in\mathbb Z}
   e^{-\pi(nm-a)^2e^{-2x}}\\
 &=n\!\sum_{\substack{\ell\in\mathbb Z\\
                 \ell\equiv-a\ ({\rm mod}\ n)}}f_{|\ell|}(-x).
\end{aligned}
\tag{5}
\]

The operator (D^2-1/4) commutes with reflection (x\mapsto-x).
Apply one half of this operator to (5) and use (2).  This proves (4).
\(\square\)

The zero character gives

\[
 \boxed{
 \sum_{j\geq1}k_{j/n}(x)
 =n\sum_{m\geq1}k_{nm}(-x).}
 \tag{6}
\]

This is the modular form of the scaling identity

\[
 K(x-\log n)=n^{-1/2}\sum_{j\geq1}k_{j/n}(x).
\]

Indeed, (k_m(\log n-x)=\sqrt n\,k_{nm}(-x)) and (K) is even.

## 4. Exact formula for the fractional remainder

Recall

\[
 R_n(x)=n^{-1/2}
 \sum_{\substack{j\geq1\\n\nmid j}}k_{j/n}(x),
 \qquad x\geq\log n.
 \tag{7}
\]

Subtracting the divisible sublattice from (6) gives the new exact form

\[
 \boxed{
 R_n(x)=\sqrt n\sum_{m\geq1}k_{nm}(-x)
          -n^{-1/2}K(x).}
 \tag{8}
\]

Although the individual reflected atoms in (8) can have either sign,
their completed difference is strictly positive on the domain in (7).
Equivalently,

\[
 n\sum_{m\geq1}k_{nm}(-x)>K(x)
 \qquad(x\geq\log n).
 \tag{9}
\]

Formula (4), followed by inverse finite Fourier transform in (a), gives
each individual residue class (j\bmod n).  Hence (8) does not merely
reproduce the total mass: it supplies the complete signed phase resolution
of every nondivisible theta index.

## 5. Why linear Poisson duality is not yet the source contraction

At fixed (n,x), every theta mark (j) in the latent lift of 106.65
carries the same spatial increment

\[
 \Delta_nr(x)=r(x)-r(x-\log n),
 \tag{10}
\]

and its contribution to the physical norm is

\[
 \sum_j k_{j/n}(x)|\Delta_nr(x)|^2.
 \tag{11}
\]

Thus the Hilbert-space amplitude attached to the mark is

\[
 \sqrt{k_{j/n}(x)}\,\Delta_nr(x),
 \tag{12}
\]

on the positive domain (x\geq\log n).  In contrast, Theorem 1 transforms
the masses (k_{j/n}(x)), not the amplitudes in (12).  There is no identity

\[
 \mathcal F_n\bigl(\sqrt{k_{j/n}(x)}\bigr)
 =\sqrt{n\,k_{|\ell|}(-x)}
 \tag{13}
\]

because the quantities on the right are not even nonnegative in general.
Consequently Parseval for the finite Fourier transform cannot convert
(4) into an equality or lower bound between the physical source norm and
the polar norm.

This obstruction is exact rather than terminological.  Any amplitude lift
of (4) must choose a complex factorization of the signed reflected masses.
After all theta, Gamma and polar fibers are assembled, such a factorization
is an exact signed operator (C) satisfying

\[
 D_\mu=C\mathcal G
 \tag{14}
\]

on the shorted complement.  By 106.105, the interpolation equation has the
unique minimal realization

\[
 C_0=2^{-1/2}U_DA^{-1/2}U_A^*,
 \qquad
 \|C_0\|=(2\inf\sigma A)^{-1/2}.
 \tag{15}
\]

Therefore selecting phases in (4) is not enough: one must prove, from the
literal residue geometry, that the resulting amplitude realization obeys

\[
 \|C_0\|\leq1.
 \tag{16}
\]

Equation (16) is precisely the physical surplus.

## 6. Reflected total variation is exponentially ill-conditioned

The failure of the termwise square root is not a small loss.  Write

\[
 \phi(y)=\pi y^2(2\pi y^2-3)e^{-\pi y^2},
 \qquad k_m(-x)=e^{-x/2}\phi(me^{-x}).
 \tag{17}
\]

The two Gaussian moment evaluations give

\[
 \int_0^\infty\phi(y)\,dy=0,
 \qquad
 c_\phi:=\int_0^\infty|\phi(y)|\,dy>0.
 \tag{18}
\]

### Theorem 2 — Exponential total-variation blowup

For every fixed residue (r\bmod n),

\[
 \boxed{
 \sum_{\substack{m\geq1\\m\equiv r\ ({\rm mod}\ n)}}
 |k_m(-x)|
 =\frac{c_\phi}{n}e^{x/2}+o(e^{x/2})
 \qquad(x\to+\infty).}
 \tag{19}
\]

On the other hand, every signed character sum in (4) satisfies, for
(x\geq\log n),

\[
 |\mathcal K_{n,a}(x)|
 \leq2\sum_{j\geq1}k_{j/n}(x)
 =2\sqrt n\,K(x-\log n),
 \tag{20}
\]

which decreases double exponentially.

#### Proof

The first formula in (18) follows from

\[
 \int_0^\infty y^2e^{-\pi y^2}dy=\frac1{4\pi},
 \qquad
 \int_0^\infty y^4e^{-\pi y^2}dy=\frac3{8\pi^2}.
\]

The function (|\phi|) is continuous and integrable.  Formula (19) is
the ordinary shifted Riemann-sum limit with mesh (ne^{-x}), after using
(17):

\[
 e^{-x/2}\sum_{m\equiv r\,(n)}|\phi(me^{-x})|
 =\frac{e^{x/2}}n
   \left[ne^{-x}\sum_{m\equiv r\,(n)}
                 |\phi(me^{-x})|\right].
\]

The bracket tends to (c_\phi).  For (20), pair (j) with (-j) in
(3), use the triangle inequality, and note that every (k_{j/n}(x)) is
positive when (x\geq\log n).  Formula (6) and the theta decay of (K)
finish the proof. \(\square\)

Thus the reflected Poisson formula is maintained by cancellation of
signed masses of order (e^{x/2}) down to a double-exponentially small
answer.  Factoring the reflected atoms separately and replacing each mass
by its absolute value destroys precisely this cancellation.  Any viable
amplitude construction must group the complete reflected lattice before
taking a norm, together with the central and Gamma--pole terms.

## 7. Radical and subthreshold tests

For every exact radical multiplier (r_j=K^{(2j)}/K), equality holds in
the source--polar norm comparison.  Hence any valid amplitude use of (4)
must be isometric on the complete radical signature; no nonzero residue
class can be discarded.  This agrees with the strict (p^2)-dispersion
test of 106.104.

Conversely, a hypothetical subthreshold eigenvector (q), (Aq=\alpha q)
with (0<\alpha<1/2), is amplified by the forced transfer by

\[
 \frac{\|D_\mu q\|}{\|\mathcal Gq\|}
 =\frac1{\sqrt{2\alpha}}>1.
 \tag{21}
\]

The linear modular identities (4)--(9) remain valid for that vector.
Thus they pass the required falsifier: they do not silently assign a false
positive sign under the off-line counterfactual.

## 8. Result and remaining theorem

The nonzero residue characters are now completely evaluated, and the
fractional theta channel has the reflected integer-lattice formula (8).
This is a new exact source identity beyond the zero-character Möbius
current.

It does not yet prove the heat/hybrid surplus.  The remaining theorem has
not changed its quantitative content, but its only possible new input is
now explicit: construct the signed square-root amplitude of the character
identity jointly with the central, Gamma and polar fibers and prove (16).
The mass-level Poisson formula alone cannot imply that norm bound.
