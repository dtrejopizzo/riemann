# D.135 — The centred Birman--Schwinger operator is compact but not finite-channel

## Verdict

The Tate--Chebyshev identity of D.133 admits an exact Birman--Schwinger
formulation on every fixed support window.  The positive reference
\(\mathcal H_{5/4}\) has compact resolvent, and the centred Chebyshev
contact is bounded.  Hence

\[
 K_T=H_{5/4,T}^{-1/2}V_{E,T}H_{5/4,T}^{-1/2}             \tag{0.1}
\]

is compact and self-adjoint on the two-jet primitive space, and

\[
 \boxed{
 -B_{\rm nuc,T}^{\rm prim}\geq0
 \quad\Longleftrightarrow\quad
 \lambda_{\max}(K_T)\leq1.}                            \tag{0.2}

\]

This is a genuine non-perturbative capacity criterion.  It does not,
however, reduce to one or finitely many coherent directions.  For every
fixed \(T\), the centred contact has positive index infinity on the
primitive smooth core.  Consequently \(K_T\) has infinitely many positive
eigenvalues tending to zero.  The two Tate conditions remove only two
directions and do not change this conclusion.

Thus a proof of D may approximate the *top* of the spectrum by finite rank,
but it cannot prove that all but finitely many contact channels vanish.
Moreover the available comparison proves no Schatten-class membership: it
gives singular-value control no better than \(1/\log j\).  An ordinary
Fredholm determinant is therefore not justified without an additional
smoothing or relative-determinant argument.

## 1. Lévy form of the shifted Gamma energy

The digamma integral gives, for real \(\tau\),

\[
 h_{5/4}(\tau)
 =\mathrm{Re}\,\psi(5/4+i\tau/2)-\psi(5/4)
 =\int_0^\infty \nu(a)(1-\cos(a\tau))\,da,              \tag{1.1}
\]

where

\[
 \nu(a)={2e^{-5a/2}\over1-e^{-2a}}>0.                  \tag{1.2}

\]

Therefore

\[
 \mathcal H_{5/4}(F)
 =\int_0^\infty\nu(a)
   \left(\|F\|_2^2-\mathrm{Re}\,C_F(a)\right)da.  \tag{1.3}

\]

The integral is understood in quadratic-form sense; the cancellation in
the parentheses removes the \(a^{-1}\) singularity at zero.  Its Fourier
symbol satisfies

\[
 h_{5/4}(\tau)=\log(2+|\tau|)+O(1)\qquad(|\tau|\to\infty)               \tag{1.4}

\]

and vanishes only at \(\tau=0\).

## 2. The centred contact as a bounded Toeplitz form

On a support window \([-T,T]\), set

\[
 d\eta_T(a)
 =\sum_{p^k\leq e^{2T}}{\log p\over p^{k/2}}\delta_{k\log p}(a)
  -e^{a/2}{\bf1}_{[0,2T]}(a)\,da
  +{\beta\over2}\delta_0(a),                           \tag{2.1}

\]

where \(\beta=\log\pi-\psi(5/4)\).  This is just the logarithmic
pushforward of \(x^{-1/2}dE_\beta(x)\).  The contact in D.133 is

\[
 V_{E,T}(F,G)
 =2\mathrm{Re}\,\int_{[0,2T]}C_{F,G}(a)\,d\eta_T(a),              \tag{2.2}

\]

with the Hermitian polarization understood.  Since \(\eta_T\) is a finite
signed measure for fixed \(T\) and every truncated translation has norm at
most one,

\[
 |V_{E,T}(F,G)|
 \leq2\|\eta_T\|_{\rm TV}\|F\|_2\|G\|_2.              \tag{2.3}

\]

Thus \(V_{E,T}\) is represented by a bounded self-adjoint operator on
\(L^2([-T,T])\), and also after compression by the primitive projection
\(P_T\).

## 3. Compact resolvent of the positive reference

Let \(H_{5/4,T}\) be the Friedrichs operator associated with (1.3),
compressed to

\[
 \mathcal P_T=\ker M_+\cap\ker M_-.                    \tag{3.1}

\]

The form-domain unit ball with norm

\[
 \|F\|_2^2+\mathcal H_{5/4}(F)                          \tag{3.2}

\]

is relatively compact in \(L^2([-T,T])\).  Indeed, (1.4) makes the Fourier
tail uniformly smaller than \(O(1/\log R)\), and common compact support
gives tightness.  The Kolmogorov--Riesz criterion then gives compactness.

The kernel is trivial.  If \(\mathcal H_{5/4}(F)=0\), (1.1) implies that
\(|\widehat F|^2\) is supported at \(\tau=0\); an \(L^2\) function with
compact support cannot have this Fourier support unless it is zero.  By
compactness, the bottom eigenvalue of \(H_{5/4,T}\) is therefore strictly
positive.  Its inverse square root is compact.

It follows that (0.1) is compact and self-adjoint.  Congruence by
\(H_{5/4,T}^{1/2}\) gives

\[
 H_{5/4,T}-V_{E,T}geq0
 \quad\Longleftrightarrow\quad I-K_T\geq0,              \tag{3.3}

\]

which proves (0.2).

## 4. Infinitely many positive centred-contact channels

Choose a nonzero \(\phi\in C_c^\infty((-T,T))\) and put

\[
 F_\xi(t)=e^{i\xi t}\phi(t).                            \tag{4.1}

\]

For every fixed \(a\),

\[
 C_{F_\xi}(a)=e^{i\xi a}C_\phi(a).                     \tag{4.2}

\]

Hence \(V_{E,T}(F_\xi,F_\xi)\) is the Fourier transform of the finite
measure

\[
 2C_\phi(a)\,d\eta_T(a).                               \tag{4.3}

\]

Its atom at zero has mass

\[
 \beta C_\phi(0)=\beta\|\phi\|_2^2>0.                 \tag{4.4}

\]

All other atoms lie at nonzero \(a\), and the continuous part has an
\(L^1\) density.  Cesàro averaging in \(\xi\) and the
Riemann--Lebesgue lemma therefore give

\[
 \lim_{R\to\infty}{1\over R}\int_0^R
 V_{E,T}(F_\xi,F_\xi)\,d\xi
 =\beta\|\phi\|_2^2>0.                                 \tag{4.5}

\]

There are consequently arbitrarily large frequencies at which this
quadratic value is positive.

The primitive correction is negligible.  Since \(\phi\) is smooth and
interior-supported,

\[
 M_\pm(F_\xi)=O_N(|\xi|^{-N})\qquad\text{for every }N,  \tag{4.6}

\]

so \(P_TF_\xi-F_\xi\to0\) rapidly in both the \(L^2\) and logarithmic
form norms.  Thus (4.5) remains true after replacing \(F_\xi\) by
\(P_TF_\xi\).

Choose the frequencies inductively far apart.  The mixed matrix
coefficients of \(V_{E,T}\) between two such modulations tend to zero by
the same Fourier-decay argument.  For every \(N\) one can therefore obtain
\(N\) primitive modulations whose \(V_{E,T}\)-Gram matrix is positive
definite.  The positive index of \(V_{E,T}|_{\mathcal P_T}\) is infinite.

Congruence with the positive operator \(H_{5/4,T}^{1/2}\) preserves finite
inertia.  By the min--max principle, \(K_T\) consequently has infinitely
many positive eigenvalues.  Compactness forces them to converge to zero.

## 5. Why an ordinary determinant does not follow from this estimate

The eigenvalues of a logarithmic-order operator on a bounded interval have
the natural scale

\[
 \lambda_j(H_{5/4,T})\asymp\log j.                     \tag{5.1}

\]

The bounded-contact comparison alone consequently yields only

\[
 s_j(K_T)=O_T((\log j)^{-1}).                           \tag{5.2}

\]

This tends to zero, proving compactness, but

\[
 \sum_{j\geq2}(\log j)^{-p}=\infty
 \qquad\text{for every finite }p.                      \tag{5.3}

\]

Thus neither trace class nor any finite Schatten class follows from this
comparison.  This does not prove that a sharper relative cancellation is
impossible.  It says that a Fredholm determinant proof would first have to
establish such an extra cancellation beyond D.133; inserting a determinant
at this point would be unjustified.

## 6. Consequence for the next step

The exact remaining statement is still the sharp top-eigenvalue bound

\[
 \boxed{\lambda_{\max}(K_T)\leq1\quad\text{for every }T>0.}            \tag{6.1}

\]

The compact formulation makes certified finite-rank approximation valid at
each fixed \(T\), but Section 4 rules out a proof based on a globally
finite number of contact modes.  The next viable mechanism must control
the spectral top uniformly while allowing infinitely many small positive
channels--for example a relative screw-kernel factorization or a directed
shorted-capacity estimate.  No such uniform bound is asserted here.
