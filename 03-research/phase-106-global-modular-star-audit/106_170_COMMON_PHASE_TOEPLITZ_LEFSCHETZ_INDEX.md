# 106.170 — The common phase Toeplitz class and the exact prime Lefschetz index

## 1. Purpose

Document 106.153 obtained the negative prime channel by placing a positive
local coefficient module formally in degree one. Document 106.169 supplied
the missing geometric phase circle, common to every complex Tate curve.
This note turns the formal degree into an actual Fredholm index.

There is one Hardy--Toeplitz class on the prime-independent phase circle.
Its cokernel is one-dimensional and odd. Tensoring it with the global
Cauchy coefficient algebra of 106.154 gives, at the \(k\)-th return of the
\(p\)-orbit, the exact equivariant index

\[
 -p^{-k/2}.
\]

Multiplication by the orbit length \(\log p\) therefore gives the complete
ordinary-prime channel of the Weil explicit formula. The sign is now a
geometric parity index, not an assigned convention and not a signed norm.

## 2. The odd phase class

Let \(H^2(\mathbb S^1)\) be the Hardy space with orthonormal basis
\(e_n(z)=z^n\), \(n\geq0\). Let

\[
 T_z=P_+M_zP_+,\qquad T_ze_n=e_{n+1}.                        \tag{1}
\]

### Lemma 2.1 — The phase index

\[
 \boxed{
 \ker T_z=0,\qquad
 \mathrm{coker}\,T_z=\mathbb C e_0,\qquad
 \mathrm{Ind}\,T_z=-1.}                                \tag{2}
\]

#### Proof

The unilateral shift is an isometry, so its kernel is zero. Its range is
the closed span of \(e_n\), \(n\geq1\), whose orthogonal complement is
\(\mathbb C e_0\). Hence the Fredholm index is \(0-1=-1\).
\(\square\)

This is the \(K^1\)-orientation of the phase circle. It is independent of
the prime and of the return number: return number belongs to the orbit
holonomy, whereas (2) is the transverse odd orientation.

## 3. Tensoring with the common arithmetic coefficient algebra

Let

\[
 \mathscr M=L^\infty(\Omega_{\rm path},\mathbf P)
             \,\bar\otimes\,M_2(\mathbb C)                   \tag{3}
\]

with normalized trace

\[
 \tau(A)=\frac12\mathbf E\,\mathrm{Tr}_2A             \tag{4}
\]

be the finite algebra of 106.154. Its common return holonomies are

\[
 U_t(\omega)=R_{c_t(\omega)},\qquad
 \tau(U_t^k)=e^{-|k|t/2}.                                   \tag{5}
\]

On the standard Hilbert \(\mathscr M\)-module
\[
 \mathscr E=H^2(\mathbb S^1)\bar\otimes L^2(\mathscr M,\tau),
                                                                    \tag{6}
\]
put
\[
 \mathcal T=T_z\otimes I.                                   \tag{7}
\]

It is Breuer--Fredholm. Its kernel is zero and its cokernel is the copy
\[
 e_0\otimes L^2(\mathscr M,\tau).                            \tag{8}
\]

For \(A\in\mathscr M\), define the equivariant \(\tau\)-index character
\[
 \mathrm{Ind}_\tau(\mathcal T;A)
 =\mathrm{Tr}_\tau(A\mid\ker\mathcal T)
  -\mathrm{Tr}_\tau(A\mid\mathrm{coker}\,\mathcal T).
                                                                    \tag{9}
\]

### Theorem 3.1 — Exact return character

For every \(t>0\) and \(k\geq1\),

\[
 \boxed{
 \mathrm{Ind}_\tau(\mathcal T;U_t^k)
 =-\tau(U_t^k)
 =-e^{-kt/2}.}                                               \tag{10}
\]

#### Proof

The kernel term in (9) vanishes. On (8), \(U_t^k\) acts only on the
\(\mathscr M\)-coefficient, so its module trace is \(\tau(U_t^k)\).
Equation (5) gives the last equality. \(\square\)

The metric on \(\mathscr E\) is positive throughout. The minus sign in
(10) comes solely from the odd cokernel in (2).

## 4. The complete prime orbit distribution

Let \(\widehat h\) be compactly supported on \((0,\infty)\). Define

\[
 \mathcal L_{\rm pr}(\widehat h)
 =\sum_p\sum_{k\geq1}(\log p)\,
   \mathrm{Ind}_\tau
      (\mathcal T;U_{\log p}^{\,k})\,
   \widehat h(k\log p).                                      \tag{11}
\]

The sum is finite for compactly supported \(\widehat h\).

### Theorem 4.1 — Prime Lefschetz identity

\[
 \boxed{
 \mathcal L_{\rm pr}(\widehat h)
 =-\sum_p\sum_{k\geq1}
   \frac{\log p}{p^{k/2}}\,
   \widehat h(k\log p).}                                     \tag{12}
\]

Thus (11) is exactly the finite-place term of the completed Weil explicit
formula.

#### Proof

Apply Theorem 3.1 with \(t=\log p\):
\[
 \mathrm{Ind}_\tau
   (\mathcal T;U_{\log p}^{\,k})
 =-e^{-k\log p/2}=-p^{-k/2}.
\]
Substitution in (11) proves (12). \(\square\)

By continuity, (12) extends to every Weil test class for which the
prime-orbit distribution is defined.

## 5. Why the same Toeplitz class is used at every iterate

The two factors in (10) have different geometric roles:

* \(U_{\log p}^{\,k}\) is the \(k\)-fold return holonomy along the
  arithmetic orbit \(C_p\);
* \(T_z\) is the transverse \(K^1\)-orientation of the common phase
  circle.

The return changes the first factor and leaves the transverse orientation
fixed. Replacing \(T_z\) by \(T_{z^k}\) would incorrectly iterate the
normal orientation and introduce an extraneous factor \(k\). The external
index product (9) keeps orbit iteration and transverse parity in their
proper factors.

## 6. Compatibility with the middle Tate polarization

The phase circle in (1) of 106.169 now has two simultaneous, compatible
functions:

1. its harmonic class \(b_p\) is the Hodge partner of the arithmetic
   class \(a_p\);
2. its Toeplitz class \([T_z]\) supplies the odd Thom orientation whose
   index gives the minus sign.

Both are prime-independent. The generic Hodge plane removed in
Theorem 6.1 of 106.169 is therefore not an artificial doubling: it is the
harmonic realization of the same common phase object whose \(K\)-homology
class produces (12).

The finite-prime localization package is now source-defined:

\[
 \boxed{
 (E_p,\star_p)
 \quad+\quad
 (\mathscr M,U_{\log p})
 \quad+\quad
 [T_z]
 \quad\Longrightarrow\quad
 -\,{\log p\over p^{k/2}}.}                                  \tag{13}
\]

No zero of zeta is used in any arrow of (13).

## 7. What remains for faithful CCM descent

Theorem 4.1 proves the complete finite-place Lefschetz distribution, not
the global cohomological comparison. The missing chain map must still:

1. identify the phase Toeplitz boundary class with the odd part of the
   CCM relative cyclic cone;
2. glue the identity sector to the Gamma spin and \(H^0/H^2\) polar pages;
3. prove that the resulting localization is a quasi-isomorphism on the
   nonreduced resonant degree one.

The first item is now a precise Bott/Toeplitz comparison rather than a
choice of sign. Items 2--3 are the remaining analytic descent.

## 8. Prior-route distinction

Earlier Toeplitz constructions in this project used a symbol whose winding
counted off-line zeros; their Fredholm property already encoded the
spectral conclusion. The operator \(T_z\) here is different:

* its symbol is the geometric coordinate of the phase circle;
* it is Fredholm unconditionally;
* its index is always \(-1\);
* all arithmetic information enters only through the positive coefficient
  character \(\tau(U_{\log p}^k)\).

Thus no RH-equivalent symbol has been inserted into the index.

## 9. Status

Proved without RH or zero input:

* one common odd phase class for all primes;
* its exact Breuer equivariant index with the Cauchy coefficient algebra;
* the full ordinary von Mangoldt prime channel as an actual Lefschetz
  index distribution;
* compatibility of this parity class with the Tate middle polarization.

Still required:

* the Bott/cyclic localization map from the CCM cone;
* the Gamma/polar identity-sector gluing;
* a degree-one quasi-isomorphism in the nuclear resonant category.
