# Phase 121 -- all-prime seam divergence theorem

## Status

The canonical periodic seam of each degree-one Euler factor is a useful
finite-place boundary coordinate.  This note proves that the unweighted
Hilbert direct sum of those seams over **all** primes contains no nonzero
compact source satisfying the resonant Tate zero.  Consequently an
all-prime finite seam-energy assertion is already a uniqueness theorem, not
an intermediate regularity estimate.  A valid global tail law must retain
signed/product cancellation before taking a norm.

## 1. Fourier coefficient of a prime seam

Let `F` be compactly supported and put

\[
 G_F(\omega)=\int_{\mathbb R}e^{t/2}F(t)e^{-i\omega t}\,dt. \tag{1.1}
\]

For `a_p=log p`, the stabilized periodic trace of the causal prime
resolvent has normalized Fourier coefficients (phase 120, seam formula)

\[
 \widehat{T_pF}(k)
 ={\sqrt{1-p^{-1}}\over\log p}
 G_F\!\left({2\pi k\over\log p}\right),
 \qquad k\in\mathbb Z.                                \tag{1.2}
\]

The Tate condition at the resonant character is `G_F(0)=0`, so the
constant coefficient vanishes.  The mean-zero seam is therefore measured
by the coefficients with `k ne 0`.

## 2. Divergence theorem

### Theorem 2.1

Let `F` be compactly supported, `F ne 0`, and suppose `G_F(0)=0`.  Then

\[
                         \sum_p\|T_pF\|_{L_0^2(\mathbb R/a_p\mathbb Z)}^2
                         =+\infty.                  \tag{2.1}
\]

In fact the subseries of the single Fourier coordinate `k=1` already
diverges.

#### Proof

`G_F` is entire and nonzero.  Let `m>=1` be its finite order of vanishing at
the origin.  Then, for real `omega ->0`,

\[
 G_F(\omega)=c\omega^m+O(\omega^{m+1}),\qquad c\ne0. \tag{2.2}
\]

Equations (1.2)--(2.2) give, for all sufficiently large primes,

\[
 |\widehat{T_pF}(1)|^2
 \ge {C_F\over(\log p)^{2m+2}}.                    \tag{2.3}
\]

For every fixed `A>0`, the prime number theorem gives

\[
 \sum_{p\le x}{1\over(\log p)^A}
 \asymp {x\over(\log x)^{A+1}}\longrightarrow\infty. \tag{2.4}
\]

Taking `A=2m+2`, Parseval and (2.3) prove (2.1).  QED.

### Corollary 2.2 -- trivial domain of the all-prime seam map

On compactly supported sources with the resonant Tate zero, the map

\[
 F\longmapsto (T_pF)_{p\ \mathrm{prime}}
 \quad\hbox{into}\quad
 \bigoplus_pL_0^2(\mathbb R/(\log p)\mathbb Z)       \tag{2.5}
\]

has domain `{0}`.

The conclusion is stronger than mere failure of boundedness.  No choice of
source Sobolev regularity repairs (2.5): the divergence comes from sampling
an entire transform arbitrarily close to its finite-order Tate zero, not
from large Fourier frequency.

### Corollary 2.3 -- one harmonic on cofinally many primes is enough

Let `P` be any infinite set of primes.  If

\[
 \widehat{T_pF}(1)=0\qquad(p\in P),                 \tag{2.6}
\]

then `F=0`.

#### Proof

By (1.2), `G_F(2 pi/log p)=0` for every `p in P`.  These distinct points
accumulate at zero.  The identity theorem gives `G_F identically 0`, and
Fourier--Laplace injectivity gives `F=0`.  QED.

Exact vanishing can be weakened to infinite-order decay.  If along an
unbounded prime sequence

\[
 G_F(2\pi/\log p)=O_N((\log p)^{-N})
 \quad\hbox{for every }N,                            \tag{2.7}
\]

then the first nonzero Taylor coefficient in (2.2) would contradict (2.7).
Thus (2.7) also forces `F=0`.

This is a substantial weakening of the backshift target.  One does not
need compact divisibility, the whole periodic trace, or square summability
over places.  It is sufficient to prove a **cofinal first-harmonic Tate-jet
law** for a first-contact state.

## 3. Consequence for the global-square search

If first contact independently implied finite all-prime seam energy, then
Theorem 2.1 would immediately give `F=0`.  But such a statement cannot be
obtained by embedding every local positive boundary into one Hilbert direct
sum: that direct sum has no nonzero physical compact source at all.

The Euler product avoids (2.1) through multiplicative, mixed-prime
cancellation before scalar observation.  Orthogonalizing the places first
deletes that cancellation and returns to the phase-120 locality--phase--sign
trilemma.  Therefore the remaining equality-state law must be formulated
as either

1. an exact signed/product identity before place orthogonalization, or
2. a distributional global seam identity whose individual Bohr
   coefficients can be extracted without asserting square summability.

By Corollary 2.3 the second option need only extract the `k=1` coefficient
on infinitely many primes, or prove its infinite-order decay.  This is the
weakest terminal seam statement currently isolated in the programme.

Finiteness of a positive all-prime boundary norm is forbidden as an
intermediate gate.  It is already first-contact exclusion in a stronger
topology.

## 4. Corpus audit

Phase 120 constructs the Bohr orthogonal assembly for every finite active
prime set.  It does not take the unweighted Hilbert direct sum over all
primes.  The phase-106 martingale audits explain why a positive all-prime
descent loses mixed Euler cancellation.  No phase-1--120 statement of
Theorem 2.1 or its `k=1` accumulation proof was found.

This theorem narrows the allowed topology of the missing global seam law;
it does not prove that law or the global square.
