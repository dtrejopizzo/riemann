# 106.133 — Physical connection adjoint and the KYP--Gamma gate

## 1. Purpose and conclusion

The exact Abel delay realization of 106.131 leaves the connection port

\[
 \mathcal C_{K,h}F
 =\{(K/h)F\}*(K'+\tfrac12K).
 \tag{1}
\]

This note computes its adjoint in the physical Hilbert space and asks
whether a cross-storage/KYP completion can absorb it into the positive
completed Gamma remainder.

The calculation gives a sharp answer.

1. In the physical metric, the \(K'\) part of (1) is exactly
   skew-adjoint.  It is a lossless storage current and contributes no
   Hermitian power.
2. The complete Hermitian part is

   \[
    \mathcal C_{\rm s}=\tfrac12T_KM_{K/h}.
    \tag{2}
   \]

3. On the mean-periodic kernel \(F*K=0\), its quadratic form is the exact
   signed connection coboundary

   \[
    \operatorname {Re}\langle F,\mathcal C_{K,h}F\rangle_{\omega_K}
    =-\frac1{4c_K}\iint K(x-y)\{a(x)-a(y)\}^2
       \operatorname {Re}\{\overline{F(x)}F(y)\}\,dx,dy,
    \quad a=K/h.
    \tag{3}
   \]

4. Therefore every KYP completion has the same non-removable real
   remainder.  A storage operator may reorganize the skew \(K'\) current,
   but it cannot change (3).
5. The exact Gamma Schur gate is a relative form inequality between (3)
   and the positive Gamma-remainder gradient.  It is not automatic from
   mean periodicity or heat smoothing.  The literal one-prime transfer
   also fails the local (J)-passivity test, so no product of passive
   prime cells can prove this gate.

The note does not prove the physical surplus.  It removes the derivative
part from the missing sign and reduces the connection contribution to one
explicit, symmetric, nonlocal kernel which can now be tested against the
Gamma remainder without a hidden phase loss.

## 2. Physical Hilbert space and common core

Put

\[
 h(x)=\cosh(x/2),\qquad
 a(x)=\frac{K(x)}{h(x)},\qquad
 d\omega_K(x)=\frac{a(x)}{c_K}\,dx,
 \qquad c_K=\frac12.
 \tag{4}
\]

Let

\[
 \mathscr H_\omega=L^2_{\rm even}(\omega_K),
 \qquad
 \mathcal M=\{F:(F*K)=0\}
 \tag{5}
\]

in the closed realization fixed in 106.43 and 106.98.  All calculations
are first made on the common real-even Schwartz multiplier core and then
extended whenever the displayed forms are finite.

For an integrable kernel (b), write

\[
 T_bF=b*F,
 \qquad
 b^\vee(x)=\overline{b(-x)}.
 \tag{6}
\]

Since \(K\) is real and even,

\[
 b_+:=K'+\tfrac12K,
 \qquad
 b_+^\vee=-K'+\tfrac12K=:b_-.
 \tag{7}
\]

Thus (1) is

\[
 \mathcal C=T_{b_+}M_a.
 \tag{8}
\]

## 3. Exact physical adjoint

### Theorem 1 — Adjoint and Hermitian/skew splitting

On the common core, the adjoint of \(\mathcal C\) in
\(\mathscr H_\omega\) is

\[
 \boxed{\mathcal C^{\sharp}=T_{b_-}M_a.}
 \tag{9}
\]

Consequently

\[
 \boxed{
 \mathcal C_{\rm s}:=\frac{\mathcal C+\mathcal C^{\sharp}}2
 =\frac12T_KM_a,}
 \tag{10}
\]

and

\[
 \boxed{
 \mathcal C_{\rm a}:=\frac{\mathcal C-\mathcal C^{\sharp}}2
 =T_{K'}M_a,
 \qquad \mathcal C_{\rm a}^{\sharp}=-\mathcal C_{\rm a}.}
 \tag{11}
\]

#### Proof

For core vectors \(F,G\), set \(f=aF\), \(g=aG\).  Then

\[
\begin{aligned}
 \langle G,\mathcal CF\rangle_{\omega_K}
 &=\frac1{c_K}\langle g,T_{b_+}f\rangle_{L^2(dx)}\\
 &=\frac1{c_K}\langle T_{b_-}g,f\rangle_{L^2(dx)}\\
 &=\langle T_{b_-}M_aG,F\rangle_{\omega_K}.
\end{aligned}
 \tag{12}
\]

This proves (9).  Equations (10)--(11) follow from

\[
 \frac{b_++b_-}{2}=\frac K2,
 \qquad
 \frac{b_+-b_-}{2}=K'.
 \tag{13}
\]

The last assertion in (11) follows again from (9).  □

Thus the derivative in the Abel drive is not a hidden dissipative term.
It is precisely the skew current of the physical connection.

## 4. Exact Hermitian connection power

### Corollary 2 — Fourier and spatial formulas

Let \(f=aF\).  Then

\[
 \boxed{
 \operatorname {Re}\langle F,\mathcal CF\rangle_{\omega_K}
 =\frac1{2c_K}\langle f,T_Kf\rangle_{L^2(dx)}.}
 \tag{14}
\]

With the Fourier convention of Phase 106,

\[
 \boxed{
 \operatorname {Re}\langle F,\mathcal CF\rangle_{\omega_K}
 =\frac1{4\pi c_K}
   \int_{\mathbb R}\Xi(\xi)|\widehat f(\xi)|^2\,d\xi.}
 \tag{15}
\]

#### Proof

Equation (14) is (10) evaluated on \(F\).  Since
\(\widehat K=\Xi\), Plancherel gives (15).  □

Formula (15) is signed: \(\Xi\) changes sign between consecutive real
zeros.  The restriction \(F*K=0\) acts on \(F\), not on \(f=aF\), so it
does not annihilate (15).

### Theorem 3 — Mean-periodic connection coboundary

If \(F\in\mathcal M\) is in the common core, then

\[
 \boxed{
 T_K(aF)(x)
 =[T_K,M_a]F(x)
 =\int_{\mathbb R}K(x-y)\{a(y)-a(x)\}F(y)\,dy.}
 \tag{16}
\]

Moreover,

\[
 \boxed{
 \operatorname {Re}\langle F,\mathcal CF\rangle_{\omega_K}
 =-\frac1{4c_K}
 \iint_{\mathbb R^2}
 K(x-y)\{a(x)-a(y)\}^2
 \operatorname {Re}\{\overline{F(x)}F(y)\}\,dx,dy.}
 \tag{17}
\]

In the normalization \(c_K=1/2\), this is exactly (3).

#### Proof

Mean periodicity gives (T_KF=0).  Hence

\[
 T_K(aF)=T_KM_aF-M_aT_KF=[T_K,M_a]F,
\]

which is (16).  Put (I=\langle aF,T_K(aF)\rangle_2).  Subtracting
(a(x)T_KF(x)=0) and symmetrizing (I+\overline I) under
(x\leftrightarrow y) gives

\[
 2\operatorname {Re}I
 =-\iint K(x-y)\{a(x)-a(y)\}^2
       \operatorname {Re}\{\overline{F(x)}F(y)\}\,dx,dy.
 \tag{18}
\]

Combine (14) and (18).  □

The diagonal terms have canceled exactly.  What remains is not a Dirichlet
square: its sign is the phase correlation
\(\operatorname {Re}\{\overline{F(x)}F(y)\}\).

## 5. The exact KYP--Gamma Schur gate

Let the positive completed Gamma-remainder gradient be

\[
 (D_{\Gamma,*}q)(u,x)
 =\left\{
 r_\Gamma(u)K(x)K(x-u)
 \right\}^{1/2}
 \{q(x)-q(x-u)\},
 \tag{19}
\]

where

\[
 r_\Gamma(u)=\frac{e^{-5u/2}}{1-e^{-2u}},
 \qquad u>0.
 \tag{20}
\]

Thus

\[
 \mathfrak b_{\Gamma,*}(q)
 =\|D_{\Gamma,*}q\|^2.
 \tag{21}
\]

For a real coupling parameter \(\eta\), define the connection-corrected
Gamma form on \(F=hq\in\mathcal M\) by

\[
 \mathfrak q_\eta(F)
 :=\mathfrak b_{\Gamma,*}(F/h)
 +2\eta\operatorname {Re}
     \langle F,\mathcal CF\rangle_{\omega_K}.
 \tag{22}
\]

Theorems 1 and 3 give the exact formula

\[
\boxed{
\begin{aligned}
 \mathfrak q_\eta(F)
 ={}&\mathfrak b_{\Gamma,*}(F/h)\\
 &-\frac{\eta}{2c_K}
 \iint K(x-y)\{a(x)-a(y)\}^2
 \operatorname {Re}\{\overline{F(x)}F(y)\}\,dx,dy.
\end{aligned}}
 \tag{23}
\]

This is the real finite part which every cross-storage must pay.

Let
\(\mathcal R_{\Gamma,*}=D_{\Gamma,*}^*D_{\Gamma,*}\) be the closed
Gamma-remainder operator and let \(\mathcal C_{\rm s}\) be understood as
its closed relative form whenever this is possible.  Assume first that
\(X\) is boundedly invertible.  The block form

\[
 \mathbb K_X=
 \begin{pmatrix}
  \mathcal R_{\Gamma,*}&\mathcal C^{\sharp}\\
  \mathcal C&X
 \end{pmatrix},
 \qquad X>0,
 \tag{24}
\]

is nonnegative if and only if

\[
 \boxed{
 \mathcal R_{\Gamma,*}
 \succeq\mathcal C^{\sharp}X^{-1}\mathcal C}
 \tag{25}
\]

as closed forms.  If \(X\) is merely nonnegative, the same statement uses
the Moore--Penrose inverse on \(\overline{\operatorname {Ran}X}\) and also
requires

\[
 \operatorname {Ran}\mathcal C
 \subseteq\operatorname {Ran}X^{1/2}.
 \tag{26}
\]

This is the exact Schur-complement version of a Gamma KYP certificate.
It is stronger than (23): it controls the full connection amplitude, not
only its Hermitian power.

There is also a necessary condition which no choice of storage changes.
Taking the real part of the KYP supply and using (11), every certificate
must imply (23) with the physical coupling \(\eta\).  The skew part can be
moved into storage; the symmetric kernel (17) cannot.

## 6. Heat rows do not alter the real connection kernel

Let \(A=L|_{\mathscr C}\), \(S=A+\frac12I\), and let

\[
 F_t=h e^{-tS}q
 \tag{27}
\]

be a smooth heat row.  Since \(\mathscr C\) reduces \(S\), one has
\(F_t\in\mathcal M\).  Equations (16)--(23) apply at every \(t>0\).
Heat regularization improves the domains of the factors, but it does not
change \(a\), \(K\), or the phase kernel in (17).

In particular, the KYP inequality on all heat rows is equivalent, by
form-core exhaustion, to its closed-form version on the complete radical
complement.  Heat smoothing provides no additional sign for (17).

## 7. Literal ordinary-prime falsifier for local passive cells

The connection gate cannot be replaced by a product of independently
passive prime cells.  For one literal prime \(p\), set

\[
 a_p=p^{-1/2},
 \qquad
 \theta_p(z)=\frac{1-a_pp^{iz}}{1-a_pp^{-iz}}.
 \tag{28}
\]

The exact (2\times2) transfer cell tested in Phase 64 satisfies, for
\(y=\operatorname {Im}z>0\),

\[
 \boxed{
 \det\{J-T_p(z)^*JT_p(z)\}
 =-\frac{a_p^2(p^y-p^{-y})^2}{1-a_p^2}<0.}
 \tag{29}
\]

Thus the local cell is not (J)-contractive for any prime.  Equation
(29) uses the literal prime displacement and weight; it is not an abstract
countermodel.  There is therefore no proof by multiplying independently
passive local prime cells: the required local premise already fails.  A
different global metric may still couple several primes, but its transport
is then exactly the globally signed connection (16), which must be
estimated as a whole.

Therefore a successful KYP proof must be global in all ordinary-prime
delays and must retain the common Gamma remainder.  It cannot be assembled
prime by prime.

## 8. Result and surviving inequality

The exact connection decomposition is

\[
 \boxed{
 \mathcal C_{K,h}
 =\underbrace{T_{K'}M_{K/h}}_{\text{lossless/skew}}
 +\underbrace{\frac12T_KM_{K/h}}_{\text{signed Hermitian}}.}
 \tag{30}
\]

On the mean-periodic kernel, the second term is the nonlocal coboundary
(17).  Consequently the strongest noncircular continuation of this route
is to prove, with the physical coupling and with the outgoing and incoming
ordinary-prime ports still paired,

\[
 \boxed{
 \mathfrak b_{\Gamma,*}(F/h)
 +2\eta_{\rm phys}\operatorname {Re}
   \langle F,\mathcal C_{K,h}F\rangle_{\omega_K}
 +\mathfrak P_{\rm PNT}(F)
 \ge0,}
 \tag{31}
\]

where \(\mathfrak P_{\rm PNT}\) denotes the single common-cutoff outgoing
plus Abel-incoming ordinary-prime power of 106.127--106.131.  Formula
(31) is now free of an artificial derivative sign: every derivative
contribution belonging to \(K'\) is storage, and the only connection cost
is (17).

What remains unproved is domination of that symmetric connection cost
together with the literal PNT power.  The adjoint calculation does not
prove the physical surplus, but it reduces the proposed KYP closure to its
minimal real kernel and rules out local prime-cell passivity.
