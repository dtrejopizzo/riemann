# D.82 — Unitary Hankel lifting and the unavoidable Toeplitz channel

## Status

D.81 isolates a nonzero cutoff-annulus cocycle and proposes a non-diagonal
Hankel lifting.  This note constructs the canonical Hankel operator of the
semilocal Fourier--Poisson scattering symbol and checks the three required
types: shift commutator, primitive landing, and preservation of the full
local character.

The symbol is unitary on the boundary, so its Hankel compression is indeed
a contraction.  It is not the required contraction.  A genuine Hankel
operator satisfies a homogeneous shift relation; after window truncation
its inhomogeneous commutator contains an additional Toeplitz edge channel.
More importantly, a unitary multiplier has two opposite Hankel blocks.  The
row-C character is their signed difference (together with the established
Meyer chart defects), whereas the norm estimate applies to each block
separately.  The semilocal symbol is neither Hardy analytic nor coanalytic:
already the single-prime factor `b_r/z` has nonzero positive and negative
Fourier coefficients.

Multiplying by the missing winding makes the prime factor inner, but deletes
exactly the torsor term `-1` in the logarithmic derivative and therefore
changes `B_nuc`.  Keeping both blocks preserves every `p^k` and Gamma but
returns a Krein/Euler difference, not an ordered Hilbert landing.  Hence the
Toeplitz term is not removable without either changing the character or
proving the same block domination as row D.

No RH or spectral-sign choice is used.  The paper is not modified.

## 1. Boundary-unitary semilocal symbol

For a finite set of primes `P`, D.33 constructs

\[
 \Theta_P(\tau)=u_\infty(\tau)\prod_{p\in P}v_p(\tau),     \tag{1.1}
\]

where

\[
 v_p(\tau)
 ={b_{p^{-1/2}}(e^{i\tau\log p})\over e^{i\tau\log p}},
 \qquad
 u_\infty(\tau)
 =\pi^{i\tau}{\Gamma(1/4-i\tau/2)\over
                    \Gamma(1/4+i\tau/2)}.                 \tag{1.2}
\]

For real `tau`,

\[
 |\Theta_P(\tau)|=1.                                      \tag{1.3}
\]

Its phase derivative is exactly

\[
 {1\over i}{d\over d\tau}\log\Theta_P(\tau)
 =m_\infty(\tau)+\sum_{p\in P}\log p
  \left(P_{p^{-1/2}}(e^{i\tau\log p})-1\right).            \tag{1.4}
\]

Thus integration of (1.4) against the squared central transform of a test
contains every `p^k`, the trivial Tate winding, and the complete Gamma
finite part.  This is the unique character which the lifting must preserve.

## 2. Two Hankel blocks of a unitary multiplier

Let

\[
 L^2(\mathbb T)=H^2_+\oplus H^2_-,
 \qquad P=P_+,
 \qquad Q=P_-.                                             \tag{2.1}
\]

For any boundary-unitary symbol `Theta`, multiplication `U=M_Theta` is
unitary.  Relative to (2.1), write

\[
 U=\begin{pmatrix}T&G\\H&R\end{pmatrix},                  \tag{2.2}
\]

where

\[
 T=PUP,
 \quad H=QUP=H_\Theta,
 \quad G=PUQ=H_{\overline\Theta}^{,*}.                    \tag{2.3}
\]

Unitarity gives

\[
 \begin{aligned}
 T^*T+H^*H&=I_P,\\
 G^*G+R^*R&=I_Q,\\
 T^*G+H^*R&=0.                                             \tag{2.4}
 \end{aligned}
\]

In particular,

\[
 \|H_\Theta\|\le1,
 \qquad \|H_{\overline\Theta}\|\le1.                    \tag{2.5}
\]

This is the valid unitary-Hankel estimate.  It does not compare the two
blocks.

The Fourier--Poisson projection is

\[
 \widehat P=U^*PU
 =\begin{pmatrix}
 T^*T&T^*G\\G^*T&G^*G
 \end{pmatrix}.                                            \tag{2.6}
\]

Hence

\[
 C=P\widehat PP=T^*T=I-H^*H,
 \qquad \beta=P\widehat PQ=T^*G.                           \tag{2.7}
\]

The Schur tower of D.80 is therefore the defect-observability tower of the
Toeplitz contraction `T`, while its cross landing contains the **other**
Hankel block through `T*G`.  Contractivity of `H` alone cannot determine
that cross landing.

## 3. Exact shift identity

Let `S_+` be multiplication by `z` on `H^2_+`.  On the basis
`(z^(-m-1))_(m>=0)` of `H^2_-`, let `S_-` be the unilateral shift

\[
 S_-z^{-m-1}=z^{-m-2}.                                    \tag{3.1}
\]

The Hankel matrix is

\[
 (H_\Theta)_{m,n}=\widehat\Theta(-m-n-1).                  \tag{3.2}
\]

Consequently

\[
 \boxed{H_\Theta S_+=S_-^*H_\Theta.}                      \tag{3.3}
\]

Thus the canonical Hankel has a **homogeneous** shift intertwining.  The
landing cocycle of D.81 is nonzero, so it cannot be (3.3).

The inhomogeneous term appears only after compressing a two-sided shift to
a window.  Let `W` commute with `U`, and put

\[
 W_+=PWP,
 \qquad W_-=QWQ.                                           \tag{3.4}
\]

A direct insertion of `I=P+Q` gives

\[
 \boxed{
 HW_+-W_-H
 =-QUQWP+QWPUP.}                                          \tag{3.5}
\]

The first term in (3.5) is a Fourier--Poisson transport of the boundary
annulus `QWP`.  The second is the exact Toeplitz edge term

\[
 \boxed{\mathfrak t_{\Theta,W}=QWP\,T.}                    \tag{3.6}
\]

For the logarithmic scale `W=theta(e^R)`, `QWP` is the difference of the
two nested position cutoffs in D.81(4.4).  Thus (3.5) has the correct
annulus type, but not the requested bare cocycle: it contains (3.6).

The term (3.6) vanishes under either of the strong triangularity conditions

\[
 QWP=0
 \quad\text{or}\quad T=PUP=0.                             \tag{3.7}
\]

Neither holds for the two-sided scaling window and the Fourier--Poisson
unitary.

## 4. The single-prime test

The failure is present before Gamma or stabilization.  For `0<r<1`,

\[
 v_r(z)={b_r(z)\over z}={1-rz^{-1}\over1-rz}.               \tag{4.1}
\]

Its Laurent expansion is

\[
 \boxed{
 v_r(z)=-rz^{-1}+(1-r^2)\sum_{n\ge0}r^nz^n.}               \tag{4.2}
\]

Therefore both Hardy orientations are nonzero:

\[
 H_{v_r}\ne0,
 \qquad H_{\overline{v_r}}\ne0.                            \tag{4.3}
\]

In fact both are rank one and

\[
 \|H_{v_r}\|_{\rm HS}^2
 =\|H_{\overline{v_r}}\|_{\rm HS}^2=r^2.                  \tag{4.4}
\]

The local phase derivative also has both signs:

\[
 \begin{aligned}
 P_r(1)-1&={2r\over1-r}>0,\\
 P_r(-1)-1&=-{2r\over1+r}<0.                               \tag{4.5}
 \end{aligned}
\]

Thus boundary unitarity is compatible with a signed local phase and two
nonzero Hankel blocks.

Multiplication by `z` changes `v_r` into the analytic inner function
`b_r`.  But

\[
 {1\over i}{d\over d\theta}\log b_r(e^{i\theta})=P_r,
 \qquad
 {1\over i}{d\over d\theta}\log v_r(e^{i\theta})=P_r-1.   \tag{4.6}
\]

The deleted `-1` is exactly the trivial Tate/torsor channel in (1.4).
Hence triangularizing the symbol this way changes the A--B--C pullback.

## 5. Character identity is a signed Hankel identity

For a projection `P` and an operator `A` with Hilbert--Schmidt off-diagonal
blocks, the exact Toeplitz commutator formula is

\[
 \mathrm{Tr}\,\bigl(A[P,A^*]\bigr)
 =\|QAP\|_{\rm HS}^2-\|PAQ\|_{\rm HS}^2.                  \tag{5.1}
\]

Applied to the semilocal Fourier--Poisson construction and then stabilized,
the two terms in (5.1), together with Meyer's positive-chart and zeta
nonunitarity corrections, recombine into

\[
 \boxed{
 B_{\rm nuc}(F,F)=\|\mathbf SF\|^2-\|\mathbf BF\|^2,}     \tag{5.2}
\]

whose local expansion is exactly (1.4).  Keeping only `H_Theta` replaces
the signed difference (5.1) by one of its summands.  It therefore loses the
opposite Hardy block and changes (5.2).

For the finite semilocal symbol, all `p^k` and Gamma are still present if
**both** Hankel orientations and the Toeplitz/chart terms are retained.
The resulting coefficient space is graded or Krein:

\[
 \mathscr H_{\rm Hankel}
 =\mathscr H(H_\Theta)\ominus
  \mathscr H(H_{\overline\Theta}).                         \tag{5.3}
\]

Unitary multiplication supplies no order on (5.3).

## 6. Landing audit

The desired D.81 equation is

\[
 \mathcal K_+(F)=\mathcal T\mathcal J_-(F),
 \qquad \|\mathcal T\|\le1,                              \tag{6.1}
\]

where `K_+` is the Schur observability tower and `J_-` the primitive defect
frame.  The canonical Hankel block `H_Theta` has the correct norm bound but
fails both typing requirements:

1. its exact shift law is (3.3), while the primitive/window landing has the
   nonzero annulus cocycle (3.5)--(3.6);
2. `K_+` depends on `C=T*T` and on the cross block `T*G`, whereas `H_Theta`
   sees only `I-T*T=H*H`.

In particular, (2.7) shows that the missing datum is not a norm estimate
for `H`; it is a comparison between the two Hankel orientations through
the Toeplitz block `T`.

One may enlarge `H_Theta` to the full unitary colligation (2.2).  Then the
landing and the character are exact, but its metric is the signed metric
of (5.3).  Converting it into (6.1) requires the block domination

\[
 \|\mathcal K_+(F)\|^2\le\|\mathcal J_-(F)\|^2,           \tag{6.2}
\]

which, by D.80, is precisely `B_nuc(F,F)<=0` on the primitive source.

## 7. Can the Toeplitz term be repaired?

There are three formal repairs, and each has an exact cost.

### 7.1 Delete the opposite Hankel block

Impose that `Theta` be analytic or coanalytic inner.  This makes one
off-diagonal block vanish and turns (5.1) into a single signed square.
For `Theta_P` this is false by (4.2), and multiplying away the denominators
deletes the torsor and Gamma denominator contributions in (1.4).

### 7.2 Retain a two-sided unitary colligation

This preserves the character, but gives the virtual difference (5.3).  Its
effectivity is exactly (6.2).

### 7.3 Solve a Nehari problem for the corrected cocycle

One may absorb (3.6) into a new Hankel symbol `Psi` only if the complete
edge operator belongs to the Hankel commutant class.  Even then, Nehari's
theorem gives

\[
 \|H_\Psi\|
 =\mathrm{dist}_{L^\infty}(\Psi,H^\infty).          \tag{7.1}
\]

The fact that `Theta` itself is unitary bounds `H_Theta`; it does not bound
the corrected symbol containing `QWP T`.  Proving the bound in (7.1) for
that corrected symbol is another form of the landing inequality, unless a
new Poisson factorization of the Toeplitz edge is constructed.

Thus the Toeplitz term is algebraically explicit and potentially the input
to a corrected lifting, but it is not removable by the unit modulus of the
scattering phase.

## 8. Exact surviving candidate

The calculation replaces the bare Hankel proposal by a more precise one.
Construct a **two-symbol Redheffer/Hankel lifting**

\[
 \mathcal T_{\rm corr}
 =H_{\Theta_P}+H_{\Psi_P}                                  \tag{8.1}
\]

such that

\[
 H_{\Psi_P}W_+-W_-H_{\Psi_P}
 =-\mathfrak t_{\Theta_P,W}                                \tag{8.2}
\]

and whose second symbol simultaneously carries the opposite Hankel block
needed in (5.1).  Equations (3.5), (5.1) and (1.4) fix the required symbol
up to an analytic summand.  A source-side proof that a representative can
be chosen with norm at most one would solve (6.1) without selecting the
sign of `B_nuc`.

The remaining difficulty is now concrete: (8.2) is a constrained Nehari
problem with a prescribed Toeplitz edge and with prime--Gamma trace
normalization.  It is not the unconstrained statement that a unitary symbol
has a contractive Hankel compression.

## 9. Conclusion

The canonical Hankel operator of the Fourier--Poisson symbol exists and is
contractive.  It does not have the required inhomogeneous shift cocycle and
does not land the complete Schur tower from the negative primitive frame.
The exact failures are the Toeplitz edge (3.6) and the second Hankel block
in (5.1).

Keeping those terms preserves the exact pullback with all prime powers and
Gamma, but leaves a signed colligation.  Deleting them yields a contraction
but changes `B_nuc`.  The next viable construction is the constrained
two-symbol lifting (8.1)--(8.2), whose norm must be obtained from a new
Poisson factorization rather than assumed from row D.
