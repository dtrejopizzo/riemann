# D.245 — The first-order Euler score is the even tangent–dual pairing

## Verdict

D.244 constructs a Lorentzian signed Gram from the squares of the local
Fourier-parity tangents.  The A--B--C operator, however, is first order in
\(\log p\).  The missing normalization is exact: the complete prime score
is the pairing of the Fourier-even tangent with the **dual central Euler
state**, not the square of the tangent.

This proves a first-order port containing every \(p^k\).  It removes the
homogeneity objection to the tangent route.  The remaining work is to prove
that after tensoring the places, adjoining Gamma, support compression and
old-core shorting, the source Lorentzian contraction of D.244 transports to
the D.190 contraction.

## 1. Central and tangent multipliers

Fix a prime \(p\), and put

\[
 r=p^{-1/2},\qquad L=\log p,\qquad
 U=M_{p^{i\tau}},\qquad h=I-rU.                    \tag{1.1}
\]

The local central inverse-Euler vector has multiplier \(h\).  The
multiplicative image of the derivative
\(d_p=(L/p)\epsilon_1\) from D.244 is

\[
 d=LrU^*.                                           \tag{1.2}
\]

D.242(2.13) says that the multiplier of
\(\mathcal F_pd_p-d_p=-2d_{p,-}\) is

\[
 Lr\,{U-U^*\over1-rU}.
\]

Consequently

\[
 \boxed{
 d_-={Lr\over2}(I-rU)^{-1}(U^*-U),
 }                                                   \tag{1.3}
\]

and \(d_+=d-d_-\) gives

\[
 \boxed{
 d_+={Lr\over2}(I-rU)^{-1}(U+U^*-2r).
 }                                                   \tag{1.4}
\]

These are bounded rational multipliers because \(0<r<1\).

## 2. Exact score identity

The normalized Poisson operator is

\[
 P_r=(1-r^2)(I-rU^*)^{-1}(I-rU)^{-1}.
\]

A direct common-denominator calculation gives

\[
 P_r-I
 =r\,{U+U^*-2r\over
          (I-rU)(I-rU^*)}.                         \tag{2.1}
\]

Comparing (1.4) and (2.1) proves

\[
 \boxed{
 L(P_r-I)=2d_+(h^*)^{-1}.
 }                                                   \tag{2.2}
\]

The right side is self-adjoint, although neither factor is separately
self-adjoint.  Expanding the resolvent gives

\[
 \begin{aligned}
 2d_+(h^*)^{-1}
 &=L\sum_{k\ge1}r^k(U^k+U^{*k}).                  \tag{2.3}
 \end{aligned}
\]

Thus (2.2) contains every prime power with its exact coefficient
\[
 Lr^k={\log p\over p^{k/2}}.
\]

This is precisely the prime score in D.236--D.240.

## 3. Dual-pair interpretation

The Euler state is \(\eta=(h^*)^{-1}\), while the inverse-Euler state is
\(\theta=h\); they obey \(\theta^*\eta=I\).  Formula (2.2) is therefore

\[
 \boxed{
 \text{prime logarithmic score}
 =2\,(\text{Fourier-even tangent of }\theta)
    \cdot(\text{dual central state }\eta).
 }                                                   \tag{3.1}
\]

The Fourier-odd tangent \(d_-\) is the anomaly/defect channel.  The
Fourier-even tangent \(d_+\), paired with the dual state, is the score
channel.  Their equality of norms before quotient, proved in D.244, is the
local conservative balance behind this first-order formula.

This explains why the raw anomaly Gram had the wrong \((\log p)^2\)
homogeneity: the correct score is a cross term and has only one tangent
factor.

## 4. Compression and all active powers

Let \(J_T\) extend by zero from \(I_T\).  Compression of (2.3) gives

\[
 J_T^*L(P_r-I)J_T
 =\sum_{\substack{k\ge1\\k\log p<2T}}
 {\log p\over p^{k/2}}\,
 J_T^*(U^k+U^{*k})J_T.                             \tag{4.1}
\]

Terms beyond the support diameter vanish exactly.  Applying the two-Tate
projection on both source variables preserves the identity.  Therefore the
first-order tangent–dual port is compatible with the actual finite-window
prime tower, without a limiting interchange.

## 5. Remaining global comparison

For several primes, the central vector is a tensor product and its
derivative is a sum of one-prime tangents.  The dual pairing cancels the
spectator central factors and reproduces the sum of the local scores.
To turn that formal tensor statement into the D.190 factorization one must
still:

1. carry the tensor pairing through the semilocal quotient;
2. add the archimedean Gamma tangent and its dual state;
3. compress by support and the two Tate equations;
4. identify the old/born shorted tangent contraction with the source
   contraction \(\Theta_S\) of D.244;
5. prove the supported-range statement on the closed form domain.

Items 1--3 are comparison/type work; item 4 is the carrying sign theorem.
None may be replaced by the already desired Schur inequality.

## 6. Classification

* Tangent multiplier formulas (1.3)--(1.4): **PROVED IDENTITIES**.
* First-order score identity (2.2): **PROVED**.
* Recovery of every \(p^k\) and exact central coefficient (2.3)--(4.1):
  **PROVED**.
* Compatibility with finite support and Tate compression: **PROVED**.
* Multi-place semilocal tensor port including Gamma: **OPEN**.
* Identification with the D.190 sharp contraction: **OPEN**.
* Row D: **OPEN**.
