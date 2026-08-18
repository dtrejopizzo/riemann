# D.129 — Jordan ANOVA, two Real constants and Efron--Stein

## Verdict

The product Jordan model resolves the apparent infinity of local unit
channels at the algebraic level.  In a tensor product of prime probability
spaces there is one global constant, and the ANOVA decomposition places the
prime contacts in singleton first-chaos sectors.  Taking the Real double
gives exactly two global constants, matching the two Tate polar channels.

The product Efron--Stein inequality has sharp constant one.  However it does
not prove the desired landing estimate.  At first order in the Jordan
parameter, both variance and Efron--Stein energy coincide on singleton
chaos.  The physical Green landing on that same chaos is expansive:
\(\|A_p\|>1\).  Higher mixed chaoses start at order \(t^2\) and therefore
cannot repair the first derivative unless the landing coefficients blow up
as \(t\downarrow0\).

Thus the deficit already lies in the first chaos, not in uncontrolled mixed
prime terms.  A nonlocal martingale correction would have to mix singleton
prime sectors with Gamma before differentiation and remain uniformly
bounded; constructing it is again the global row-D problem.

## 1. Local centered Jordan variable

Let \(x=p^t>1\) and let \(X_p\) have distribution

\[
 x^{-1}\delta_0+(1-x^{-1})\delta_x.                    \tag{1.1}
\]

Then

\[
 \mathbb EX_p=x-1,\qquad
 \mathbb EX_p^2=x(x-1),\qquad
 \mathrm{Var}(X_p)=x-1.                          \tag{1.2}
\]

Hence

\[
 \mathrm{Var}(X_p)=t\log p+O(t^2).               \tag{1.3}
\]

The normalized centered variable spans the one-dimensional local
mean-zero space.

## 2. Product ANOVA decomposition

At a finite prime cutoff \(q\), the product space has the orthogonal
decomposition

\[
 L^2(\Omega_{q,t})
 =\bigoplus_{S\subseteq\{p\le q\}}\mathcal H_S,         \tag{2.1}
\]

where \(\mathcal H_\varnothing=\mathbb C1\) and
\(\mathcal H_S\) is the tensor product of centered local lines for
\(p\in S\).

There is therefore one global constant, not one independent constant for
each prime.  A chaos vector indexed by \(S\) has covariance scale

\[
 \prod_{p\in S}(p^t-1)
 =t^{|S|}\prod_{p\in S}\log p+O(t^{|S|+1}).             \tag{2.2}
\]

Consequently:

* singleton chaos survives in the first derivative and gives \(\log p\);
* two-prime chaos gives the \(\Lambda*\Lambda\) part of Selberg at order
  \(t^2\);
* all higher mixed contacts begin at their corresponding higher order.

This is the probabilistic version of D.126's Jordan expansion.

## 3. Two Real orientations and the Tate constants

Take the Real double

\[
 \mathcal H_{q,t}^{\rm R}
 =L^2(\Omega_{q,t})_+\oplus L^2(\Omega_{q,t})_-        \tag{3.1}
\]

with the involution exchanging the two summands and conjugating.  Its polar
constant sector is

\[
 \mathbb C1_+\oplus\mathbb C1_-.                       \tag{3.2}
\]

Under the two oriented Mellin landings, these constants correspond to the
two evaluations at \(s=0,1\), or \(\tau=\mp i/2\).  Thus the Real product
model has exactly the correct number of global unit channels to match
\(M_-,M_+\).

This is an identification of polar dimensions and orientations.  It is not
yet an isometric identification of the full physical landing.

## 4. Sharp Efron--Stein inequality

For \(f=\sum_Sf_S\) in (2.1),

\[
 \mathrm{Var}(f)=\sum_{S\ne\varnothing}\|f_S\|^2. \tag{4.1}
\]

Let \(\mathbb E_{-p}\) condition on all coordinates except \(p\).  The
Efron--Stein energy is

\[
 \mathcal E_{\rm ES}(f)
 =\sum_{p\le q}\|f-\mathbb E_{-p}f\|^2
 =\sum_{S\ne\varnothing}|S|\|f_S\|^2.                  \tag{4.2}
\]

Therefore

\[
 \boxed{\mathrm{Var}(f)\le\mathcal E_{\rm ES}(f)} \tag{4.3}
\]

with sharp constant one, and equality holds on the entire first chaos.
The beta Gamma coordinate may be included as one further product
coordinate; the same identity remains valid.

## 5. Why the physical landing fails in first chaos

For a prime \(p\), the desired preparation feature is

\[
 S_pF=\sqrt{\log p}\,A_pF,\qquad
 A_p=\sqrt{1-\rho_p^2}(I-\rho_pU_p)^{-1},              \tag{5.1}
\]

whereas the local boundary feature is

\[
 B_pF=\sqrt{\log p}\,F.                                \tag{5.2}
\]

The exact norm is

\[
 \|A_p\|^2={1+\rho_p\over1-\rho_p}>1.                  \tag{5.3}
\]

On singleton chaos, (4.3) is equality.  A coordinatewise conditional
expectation or Efron--Stein gradient cannot turn (5.2) into (5.1), because
that would expand a first-chaos vector by (5.3).

This obstruction occurs at order \(t\log p\), exactly the order retained in
the contact derivative.

## 6. Higher chaos cannot repair a bounded first derivative

For \(|S|\ge2\), the covariance scale is \(O(t^{|S|})\).  If a family of
landing maps \(C_t\) is uniformly bounded as \(t\downarrow0\), the
contribution of higher chaos to a quadratic form remains \(O(t^2)\) and
vanishes after division by \(t\).

To modify the first-order singleton deficit using second chaos, one would
need coefficients of size at least \(t^{-1/2}\).  Such a family is not
uniformly bounded, has no direct conditional-expectation interpretation,
and does not yield a cofinal Hilbert contraction.

Thus the first-order deficit cannot be hidden in Selberg's higher-order
positive terms.

## 7. Gamma and nonlocal martingale mixing

The beta coordinate gives a positive Gamma moment model, but the physical
Gamma derivative is the relative form

\[
 m_0\|F\|^2-\|\partial_\infty F\|^2.                   \tag{7.1}
\]

A product ANOVA decomposition keeps the Gamma coordinate orthogonal to the
prime singleton sectors.  It supplies no cross term capable of compensating
the expansive \(A_p\).

A possible continuation must therefore replace product conditioning by a
nonlocal martingale difference which mixes:

1. all prime singleton chaoses;
2. the Gamma first chaos;
3. the two Real constants; and
4. the Poisson relation.

The mixing must be uniformly bounded before taking \(t\downarrow0\).
Ordinary ANOVA/Efron--Stein does not construct it.

## 8. Conclusion

Jordan ANOVA gives a clean structural result:

\[
 \boxed{
 \text{one constant per orientation}
 \;+\;\text{singleton first chaos }(\log p)
 \;+\;\text{higher Selberg chaoses}.}
\]

The Real double matches the two Tate constants, and Efron--Stein has the
ideal constant one.  Nevertheless the physical orbit landing is already
expansive on singleton chaos, where Efron--Stein is equality.  Mixed chaos
is too high order to fix the derivative under any uniformly bounded map.

Hence the missing contraction must be a genuinely nonlocal prime--Gamma
martingale transform, not the product conditional expectation.

