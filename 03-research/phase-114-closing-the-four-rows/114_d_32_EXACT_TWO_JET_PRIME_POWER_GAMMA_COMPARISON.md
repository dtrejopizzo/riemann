# D.32 — Exact two-jet, prime-power and Gamma comparison

## Status

This note proves the exact local and global comparison which can be obtained
before the Hodge sign.  It includes every prime power and the complete Gamma
term.  It also proves that the scalar one-column-per-prime space of D.31 is
not the target of this comparison: the full prime-power orbit forces a
vector-valued enlargement, and that enlargement has positive local
directions which can only be controlled after coupling all finite places to
the Gamma boundary.

No zero of zeta and no sign of the Weil form is used below.

## 1. The two primitive jets

Put

\[
 M_-(F)=\int_{\mathbb R}e^{-t/2}F(t)\,dt,\qquad
 M_+(F)=\int_{\mathbb R}e^{t/2}F(t)\,dt                 \tag{1.1}
\]

for `F in C_c^infinity(R)`.  If `S_aF(t)=F(t-a)`, then a change of
variables gives

\[
 M_\pm(S_aF)=e^{\pm a/2}M_\pm(F).                     \tag{1.2}
\]

Thus `(M_-,M_+)` is the pair of central Tate characters of the translation
representation.  Under the central logarithmic change

\[
 F(t)=e^{t/2}f(e^t),                                  \tag{1.3}
\]

they are exactly the two ruling degrees

\[
 M_-(F)=\widehat f(0),\qquad M_+(F)=\widehat f(1).     \tag{1.4}
\]

Consequently the primitive space is intrinsically

\[
 \mathcal P=\ker M_-\cap\ker M_+.                     \tag{1.5}
\]

With the Fourier--Laplace convention

\[
 \widehat F(\zeta)=\int_{\mathbb R}F(t)e^{-i\zeta t}\,dt,             \tag{1.6}
\]

Paley--Wiener gives the exact two-jet identification

\[
 M_+(F)=\widehat F(i/2),\qquad
 M_-(F)=\widehat F(-i/2).                              \tag{1.7}
\]

Thus primitivity means that the Fourier--Laplace section vanishes at the
two Tate points `+i/2` and `-i/2`.

Equations (1.2)--(1.4), rather than a choice of Hardy coordinates, identify
the two jets carried by A--B--C.

## 2. Every prime power from one central Szego vector

For a prime `p`, set `r_p=p^(-1/2)` and

\[
 h_p(z)=\frac{\sqrt{1-r_p^2}}{1-r_pz}\in H^2(\mathbb D).             \tag{2.1}
\]

Let `Z` be the unilateral shift.  Direct summation of the Taylor
coefficients proves, for every `k>=0`,

\[
 \langle h_p,Z^kh_p\rangle=r_p^k=p^{-k/2}.             \tag{2.2}
\]

The reduced A--B contact of `Gamma_(p^k)` has determinant degree `log p`.
Multiplying (2.2) by that degree gives

\[
 \log p\,\langle h_p,Z^kh_p\rangle
   =\frac{\Lambda(p^k)}{\sqrt{p^k}}.                  \tag{2.3}
\]

If `n` has two distinct prime factors, the reduced dynamic contact is zero,
as is `Lambda(n)`.  Hence (2.3), together with the reduced tensor law of B,
recovers the coefficient `Lambda(n)/sqrt(n)` for every `n>=2`.

This is an equality of source-defined matrix coefficients: the contact
degree comes from the derived prime incidence, while the central decay is
the orbit coefficient of the normalized Szego vector.

## 3. The exact vector-valued finite-place pullback

Let

\[
 U_p=S_{\log p},\qquad
 A_p=\sqrt{1-p^{-1}}\,(I-p^{-1/2}U_p)^{-1}.            \tag{3.1}
\]

The inverse exists in operator norm.  Functional calculus gives

\[
 A_p^*A_p=P_{p^{-1/2}}(U_p)
 =\sum_{k\in\mathbb Z}p^{-|k|/2}U_p^k.                \tag{3.2}
\]

Therefore, for `F,G in L^2(R)`, polarization of the norm-convergent series
gives

\[
 \begin{aligned}
 K_p(F,G)
  &: =\log p\bigl(\langle A_pF,A_pG\rangle-\langle F,G\rangle\bigr)\\
  &=\log p\sum_{k\ne0}p^{-|k|/2}\langle F,U_p^kG\rangle .           \tag{3.3}
 \end{aligned}
\]

For `F=G`, the `k` and `-k` terms combine into the complete prime-power
tower

\[
 K_p(F,F)=2\sum_{k\ge1}\frac{\Lambda(p^k)}{\sqrt{p^k}}
                    \mathrm{Re}\,\langle F,S_{k\log p}F\rangle.
                                                                    \tag{3.4}
\]

For a finite set `P` of primes define

\[
 \mathcal S_PF=(\sqrt{\log p}\,A_pF)_{p\in P},\qquad
 \mathcal T_PF=(\sqrt{\log p}\,F)_{p\in P}.          \tag{3.5}
\]

Then

\[
 \sum_{p\in P}K_p(F,G)
 =\langle\mathcal S_PF,\mathcal S_PG\rangle
  -\langle\mathcal T_PF,\mathcal T_PG\rangle .        \tag{3.6}
\]

For compactly supported `F,G`, only finitely many correlations in (3.4)
are nonzero after the paired subtraction.  Thus the cofinal value of (3.6)
is well defined as a renormalized difference even though its two positive
norms diverge separately.

## 4. The complete Gamma pullback

Let `partial_infinity` be the oscillator boundary derivation

\[
 (\partial_\infty F)(x,j,t)
  =2^{-1/2}e^{-x(j+1/4)/2}\bigl(F(t)-F(t-x/2)\bigr).   \tag{4.1}
\]

Tonelli and the heat trace of `j+1/4` give

\[
 \langle\partial_\infty F,\partial_\infty G\rangle
 =\int_0^\infty\frac{e^{-r/2}}{1-e^{-2r}}
   \langle F-S_rF,G-S_rG\rangle\,dr.                 \tag{4.2}
\]

With

\[
 m_0=\log\pi-\psi(1/4),                              \tag{4.3}
\]

the digamma difference formula and Plancherel yield the exact
archimedean finite part

\[
 G_\infty(F,G)=m_0\langle F,G\rangle
   -\langle\partial_\infty F,\partial_\infty G\rangle.               \tag{4.4}
\]

The density in (4.2) is also the centrally normalized character of the two
even Hardy dilation modules of A--C.  Thus (4.4) includes the full Gamma
factor, including its finite-part constant.

## 5. Exact global pullback identity

For a cofinal prime cutoff `P`, put

\[
 \mathbf S_PF=(\mathcal S_PF,\sqrt{m_0}F),\qquad
 \mathbf B_PF=(\mathcal T_PF,\partial_\infty F).       \tag{5.1}
\]

Combining (3.6) and (4.4) proves, by polarization,

\[
 \boxed{
 B_{\rm nuc}(F,G)
 =\langle\mathbf S_PF,\mathbf S_PG\rangle
  -\langle\mathbf B_PF,\mathbf B_PG\rangle .}         \tag{5.2}
\]

The right side is understood as the stabilized paired difference.  Formula
(5.2) is term-by-term exact for all powers `p^k` and for Gamma.  Moreover

\[
 F\text{ is primitive}\quad\Longleftrightarrow\quad
 (M_-(F),M_+(F))=(0,0).                               \tag{5.3}
\]

This completes the comparison of the A--B--C moments and local contacts
with the signed mixed-section form.  It does **not** prove its Hodge sign.

## 6. Why D.31 is not yet the target of (5.2)

The space in D.31 has one scalar coordinate per prime.  A single local
tower already has infinite translation rank: the distribution

\[
 W_p=\log p\sum_{k\ne0}p^{-|k|/2}\delta_{k\log p}     \tag{6.1}
\]

has infinitely many point masses, and the convolution map
`F -> W_p*F` has infinite algebraic rank.  Hence the local form (3.3) cannot
factor through one scalar coordinate.

There is also a direct sign obstruction to the most natural orbit
enlargement.  If multiplication by `h_p` is used on `H^2` and

\[
 V_N(z)=z^2(1+z+\cdots+z^{N-1}),\qquad N\ge2,          \tag{6.2}
\]

then the constant and linear jets of `h_pV_N` vanish, but

\[
 \begin{aligned}
 \|h_pV_N\|^2-\|V_N\|^2
 &=2\sum_{d=1}^{N-1}(N-d)r_p^d>0.                    \tag{6.3}
 \end{aligned}
\]

Thus the scalar two-jet Hodge theorem does not extend prime by prime to the
full orbit.  The Gamma term and the other primes must enter before taking
the primitive sign.  This proves that the required target is a genuinely
global, vector-valued two-jet quotient, not the direct sum of local D.31
spaces.

## 7. Remaining comparison theorem

The unresolved statement is now sharply typed.  One must construct from
periodic Yoneda multiplication and Tate--Gamma duality a cofinal quotient
`H_mix` and a contraction

\[
 \mathfrak C:\mathbf B(\mathcal P)\longrightarrow\mathbf S(\mathcal P),
 \qquad \mathfrak C\mathbf BF=\mathbf SF,
 \qquad\|\mathfrak C\|\le1,                          \tag{7.1}
\]

before using (5.2).  Then (5.2) would be the pullback comparison and (7.1)
would supply the independent Hodge theorem.  Defining `mathfrak C` by polar
decomposition of (5.2), or quotienting by its positive spectral subspace,
would be circular.
