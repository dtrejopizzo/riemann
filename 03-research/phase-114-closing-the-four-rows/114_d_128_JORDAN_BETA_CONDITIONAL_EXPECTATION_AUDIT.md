# D.128 — Conditional expectation for Jordan--Green--beta measures

## Verdict

At every finite prime cutoff there is a canonical probability product and a
contractive martingale of conditional expectations.  It realizes the
positive Jordan covariances, the Green depth processes and the beta Gamma
factor.

This martingale is place-diagonal.  It does not realize the required global
landing \(S=CB\).  Already at one prime the Green preparation operator has
norm

\[
 \|A_p\|^2={1+p^{-1/2}\over1-p^{-1/2}}>1,               \tag{0.1}
\]

so no placewise conditional expectation can map the boundary channel
\(B_p=\sqrt{\log p}\,I\) to
\(S_p=\sqrt{\log p}\,A_p\).

The semilocal Poisson operator supplies the missing cross-place coupling,
but it is a unitary Fourier transform, not a positivity-preserving Markov
operator.  Its logarithmic derivative is signed.  The two Tate constraints
are an orthogonal linear shorting, not a sigma-algebra.  Hence they cannot
turn Poisson summation into a conditional expectation.

Thus a genuine finite-cutoff martingale exists for the separate positive
moment models, but no correctly typed conditional expectation has been
constructed for the signed annulus landing.  Existence of such an
expectation with \(S=EB\) would itself imply the desired contraction and is
equivalent to D.

## 1. Finite Jordan probability space

For \(t>0\) and a prime \(p\), put \(x_p=p^t\) and

\[
 \nu_{p,t}=x_p^{-1}\delta_0+(1-x_p^{-1})\delta_{x_p}.   \tag{1.1}
\]

Its moments are \(J_t(p^k)\).  At cutoff \(q\), take

\[
 (\Omega_{q,t}^{\rm ar},\mathbb P_{q,t}^{\rm ar})
 =\prod_{p\le q}(\{0,x_p\},\nu_{p,t}).                  \tag{1.2}
\]

The monomial \(X_n=\prod_pp^{tv_p(n)}\) with the convention that a zero
coordinate kills a positive exponent satisfies

\[
 \mathbb E(X_m\overline{X_n})=J_t(mn).                  \tag{1.3}
\]

Centering by the constant gives the Jordan covariance of D.126.

Tensor (1.2) with the stationary Green/AR path at each prime and with the
positive beta measure from D.127.  The resulting space
\(\Omega_{q,t}\) realizes all separate positive factors in a single product
probability space.

## 2. The cutoff martingale

For \(q<q'\), let

\[
 \mathcal E_{q',q}:L^2(\Omega_{q',t})\to L^2(\Omega_{q,t}) \tag{2.1}
\]

be conditional expectation onto the coordinates with \(p\le q\), retaining
the beta coordinate.  Then

\[
 \|\mathcal E_{q',q}\|=1,\qquad
 \mathcal E_{q'',q}=\mathcal E_{q',q}\mathcal E_{q'',q'}.
                                                                  \tag{2.2}
\]

Thus the positive coefficient models form a genuine reverse martingale as
primes are added.  Differentiating their centered covariance at \(t=0\)
recovers the reduced contacts.

This proves compatibility of the positive **source moments**.  It says
nothing yet about the Toeplitz/annulus boundary map.

## 3. Local norm obstruction

For \(\rho=p^{-1/2}\), the prime landing is

\[
 A_p=\sqrt{1-\rho^2}(I-\rho U_p)^{-1}.                 \tag{3.1}
\]

Since \(U_p\) is unitary, its multiplier norm is

\[
 \|A_p\|
 ={\sqrt{1-\rho^2}\over1-\rho}
 =\sqrt{{1+\rho\over1-\rho}}>1.                        \tag{3.2}
\]

If a placewise conditional expectation \(E_p\) satisfied
\(S_p=E_pB_p\), contractivity would give
\(\|A_p\|\le1\), contradicting (3.2).  Therefore the required \(C\) must
mix primes with Gamma before the norm is taken.

The product conditional expectations (2.1) preserve place labels and cannot
provide this mixing.

## 4. Poisson coupling is not Markov coupling

Semilocal Poisson summation does couple finite places and infinity.  On
Hilbert realizations its basic operation is Fourier transformation.  Fourier
transformation is unitary, but not positivity preserving: already on
\(\mathbb Z/2\), the normalized Fourier matrix sends the positive point mass
\((0,1)\) to a vector with one negative coordinate.

Therefore the Poisson operator is not a conditional expectation between
commutative probability algebras.  Applying the logarithmic derivation
produces the signed contact character, not a Markov kernel.

This is exactly the distinction corrected in D.127: the positive Hankel
moment model and the Toeplitz/annulus landing are not related by one fixed
positive pullback.

## 5. The Tate shorting is not a sigma-algebra

The primitive space is

\[
 \mathcal P=\ker M_-\cap\ker M_+.                       \tag{5.1}
\]

It is a closed linear subspace, but it is not closed under pointwise
multiplication and does not contain the unit.  Hence it is not
\(L^2(\mathcal G)\) for a sub-sigma-algebra \(\mathcal G\).

The projection onto \(\mathcal P\) is an orthogonal rank-two shorting.  It is
not a positive unital conditional expectation.  Consequently polar removal
does not supply a probabilistic conditioning theorem capable of changing
the Fourier Poisson map into a Markov map.

## 6. Cofinal failure of uniform \(L^2\) landing

The probability products themselves exist cofinally.  But the relevant
central feature map does not have uniformly bounded \(L^2\) norm.  At the
arithmetic level this is already visible in the divergent contact mass and
in the Möbius inverse estimate of D.125.

Martingale convergence applies to a family bounded in \(L^2\).  It therefore
applies to fixed cylinder observables, but not automatically to the
cutoff-dependent landed vectors whose squared norms accumulate all
\((\log p)p^{-k/2}\) contacts.

Thus (2.2) has a cofinal probability meaning without giving the cofinal
Hilbert contraction required by D.

## 7. Exact conditional-expectation criterion

Suppose there were a common Hilbert probability realization and a
conditional expectation \(E\) such that on the primitive source

\[
 S=EB.                                                   \tag{7.1}
\]

Then Jensen gives

\[
 \|SF\|=\|E(BF)\|\le\|BF\|,                              \tag{7.2}
\]

which is row D.  Conversely, if row D holds, Douglas factorization produces
a Hilbert contraction \(C\) with \(S=CB\), though not necessarily a
commutative conditional expectation.

Hence constructing (7.1) is stronger than, and cannot be assumed
independently of, the desired inequality.

## 8. Conclusion

The Jordan--Green--beta factors possess a canonical finite-cutoff martingale
of positive conditional expectations.  It proves consistency and
contractivity of the source moment system.

It does not land on the A--B--C boundary differential:

* local Green landing is expansive;
* product expectation is place-diagonal;
* Poisson coupling is unitary but non-Markov;
* polar shorting is not sigma-algebra conditioning; and
* the cutoff-dependent feature vectors are not uniformly \(L^2\)-bounded.

The desired global expectation \(S=EB\) is therefore not obtained.  Its
contractivity would prove D directly.

## 9. Local-unit amalgamation versus the two global jets

The Jordan shorting at a prime removes the local unit before taking the
infinitesimal covariance.  After Green landing this reappears as

\[
 S_p^*S_p-(\log p)I.                                    \tag{9.1}
\]

Thus a finite set \(P\) of primes carries the unit-channel map

\[
 U_PF=(\sqrt{\log p}\,F)_{p\in P}.                      \tag{9.2}
\]

Together with Gamma, the negative boundary map is

\[
 B_PF=(U_PF,\partial_\infty F).                         \tag{9.3}
\]

By contrast, the global polar shorting has only

\[
 MF=(M_-(F),M_+(F))\in\mathbb C^2.                     \tag{9.4}
\]

An amalgamation theorem would need a Poisson-defined map

\[
 \mathfrak A_P:
 \left(\bigoplus_{p\in P}H\right)\oplus H_\infty
 \longrightarrow\mathbb C^2                            \tag{9.5}
\]

compatible with (9.3)--(9.4), while retaining in its kernel enough positive
boundary energy to dominate all Green preparations.

This cannot be a lossless finite-rank shorting.  On any \(d\)-dimensional
test subspace \(V\subset H\), the range of \(U_P|_V\) has dimension \(d\),
whereas \(\mathfrak A_PU_P|_V\) has rank at most two.  Hence

\[
 \dim\ker(\mathfrak A_PU_P|_V)\ge d-2.                  \tag{9.6}
\]

No identity through the two jets can recover the unit-channel norm on those
directions.  The required assertion is instead that Gamma and the
nonlocal Poisson coupling control this entire kernel.  That is an
infinite-rank estimate, not a rank-two product-formula identity.

At the scalar-character level Poisson does amalgamate all local degrees into
the two polar residues.  But equality of scalar traces does not provide a
bounded map (9.5) on the Hilbert feature spaces.  Proving the necessary
kernel domination is another exact formulation of D.
