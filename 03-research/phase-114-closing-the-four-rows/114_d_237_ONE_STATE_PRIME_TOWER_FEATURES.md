# D.237 — One-state rational features for the balanced prime tower

## Verdict

The two positive feature Grams of D.137 belonging to all powers of a fixed
prime can each be represented by one rational filter.  This is stronger
than the difference identity of D.236 and removes the countable
prime-power feature multiplicity without changing either Gram.

Let

\[
 U=S_{\log p},\qquad r=p^{-1/2},\qquad
 a={r\over1-r},\qquad L=\log p.
\]

On the full line define

\[
 \begin{aligned}
 R_{p,-}&=\sum_{k\ge1}Lr^kJ_{p^k,-}^*J_{p^k,-},\\
 R_{p,+}&=\sum_{k\ge1}Lr^kJ_{p^k,+}^*J_{p^k,+},
 \end{aligned}                                      \tag{0.1}
\]

where (J_{p^k,\pm}=(U^k\pm I)/\sqrt2).  Then

\[
 \boxed{
 R_{p,-}=W_{p,-}^*W_{p,-},\qquad
 W_{p,-}=c_{p,-}(I-rU)^{-1}(I-U),
 }                                                     \tag{0.2}
\]

with

\[
 c_{p,-}^2={Lr(1+r)\over2(1-r)}.                    \tag{0.3}
\]

For the symmetric feature put

\[
 A=1-r+2r^2,\qquad B=1-3r,
 \qquad t={B\over A},                               \tag{0.4}
\]

and define

\[
 s=
 \begin{cases}
 -t/(1+\sqrt{1-t^2}),&t\ne0,\\
 0,&t=0,
 \end{cases}
 \qquad
 c_{p,+}^2={Lr\over1-r}{A\over1+s^2}.              \tag{0.5}
\]

Then (|t|\le1), (|s|\le1), and

\[
 \boxed{
 R_{p,+}=W_{p,+}^*W_{p,+},\qquad
 W_{p,+}=c_{p,+}(I-rU)^{-1}(I-sU).
 }                                                     \tag{0.6}
\]

Equations (0.2) and (0.6) are exact operator identities obtained before
support localization, Tate compression, or a sign assumption.  Compression
to (I_T) automatically removes the inactive powers.  Thus the finite
place portion of the balanced A--B--C feature map may be realized with one
state channel per prime rather than one channel per prime power.

This does not yet give the D.190 contraction.  The antisymmetric filter in
(0.2) vanishes at the constant mode (U=1), while the symmetric filter
does not.  The continuous Gamma reference and the two Tate conditions are
therefore essential to control the quotient near that mode.  The missing
global theorem has become a coupling problem for these explicit rational
prime filters and the Gamma channel.

## 1. Resummation of the two Grams

D.236 proves, in norm-convergent functional calculus,

\[
 P_r(U):=I+\sum_{k\ge1}r^k(U^k+U^{*k})
 =(1-r^2)(I-rU^*)^{-1}(I-rU)^{-1}.                 \tag{1.1}
\]

Since

\[
 J_{p^k,\pm}^*J_{p^k,\pm}
 =I\pm{U^k+U^{*k}\over2},                           \tag{1.2}
\]

we have

\[
 \begin{aligned}
 R_{p,-}&=L\left((a+\tfrac12)I-\tfrac12P_r(U)\right),\\
 R_{p,+}&=L\left((a-\tfrac12)I+\tfrac12P_r(U)\right).
 \end{aligned}                                      \tag{1.3}
\]

Their difference is the complete prime tower from D.236:

\[
 R_{p,+}-R_{p,-}=L(P_r(U)-I)
 =\sum_{k\ge1}Lr^k(U^k+U^{*k}).                    \tag{1.4}
\]

## 2. Antisymmetric spectral factor

On the unit circle write (z=e^{i\theta}) and

\[
 D_r(z)=|1-rz|^2=1-2r\cos\theta+r^2.               \tag{2.1}
\]

The symbol of the first line of (1.3) is

\[
 L\sum_{k\ge1}r^k(1-\cos k\theta)
 ={Lr(1+r)\over2(1-r)}
   {|1-z|^2\over|1-rz|^2}.                          \tag{2.2}
\]

Functional calculus now proves (0.2)--(0.3).  In particular the complete
prime reference is a rational difference filter, not merely a formal sum
of positive channels.

## 3. Symmetric spectral factor

The symbol of the second line of (1.3) simplifies to

\[
 L\sum_{k\ge1}r^k(1+\cos k\theta)
 ={Lr\over1-r}
 {A+B\cos\theta\over D_r(e^{i\theta})},             \tag{3.1}
\]

with (A,B) from (0.4).  Direct calculation gives

\[
 A-B=2r(1+r)>0,\qquad A+B=2(1-r)^2\ge0,             \tag{3.2}
\]

so (A\ge|B|) and (|t|\le1).  The choice (0.5) is the root of

\[
 {-2s\over1+s^2}=t                                  \tag{3.3}
\]

having modulus at most one.  Therefore

\[
 A+B\cos\theta
 ={A\over1+s^2}|1-se^{i\theta}|^2.                 \tag{3.4}
\]

Substitution of (3.4) into (3.1) proves (0.6).

## 4. Support compression

Let (J_T) denote extension by zero from (I_T).  Although the rational
filters in (0.2) and (0.6) contain all powers, their compressed Grams obey

\[
 J_T^*U^kJ_T=0\qquad(k\log p\ge2T)                  \tag{4.1}
\]

as quadratic-form cross terms, apart from the null endpoint convention.
Consequently the compressed identities reproduce exactly the active
finite sums in D.137.  No convergence or interchange problem remains:
the full-line series is norm convergent because (r<1), and the localized
cross series is finite.

The exact two-Tate projection (Pi_T) may be applied on the source of
both (W_{p,-}) and (W_{p,+}).  It does not commute with the individual
translations, but no such commutation is required for the Gram identities:

\[
 \Pi_TJ_T^*R_{p,\pm}J_T\Pi_T
 =(W_{p,\pm}J_T\Pi_T)^*(W_{p,\pm}J_T\Pi_T).         \tag{4.2}
\]

## 5. The new colligation target

Let

\[
 \mathcal W_-F=(W_{p,-}J_T\Pi_TF)_p,
 \qquad
 \mathcal W_+F=(W_{p,+}J_T\Pi_TF)_p.               \tag{5.1}
\]

Then the prime part of the complete balanced factorization is exactly

\[
 \mathcal W_+^*\mathcal W_+-\mathcal W_-^*\mathcal W_-.
                                                               \tag{5.2}
\]

The remaining source-defined continuous features are (D_\infty) on the
reference side and ((\sqrt\beta I,Q_{1/2})) on the load side.  Hence the
global D.190 problem can be restated without separate prime-power feature
coordinates:

\[
 \left\|
 \begin{pmatrix}\sqrt\beta I\\Q_{1/2}\\\mathcal W_+\end{pmatrix}F
 \right\|^2
 \le
 \left\|
 \begin{pmatrix}D_\infty\\\mathcal W_-\end{pmatrix}F
 \right\|^2,
 \qquad F\in\mathcal P_T.                           \tag{5.3}
\]

Equation (5.3) is still row D, not its proof.  The gain is structural: a
candidate arithmetic colligation now needs one rational state per prime
and one Gamma state continuum, while all Frobenius depths are already
encoded by the resolvents ((I-p^{-1/2}S_{\log p})^{-1}).

## 6. Epistemic classification

* Resummed prime Grams (1.3): **PROVED OPERATOR IDENTITIES**.
* Rational spectral factors (0.2), (0.6): **PROVED**.
* Exact preservation under support/Tate compression: **PROVED**.
* Reduction from prime-power channels to one state per prime: **PROVED**.
* Completed prime--Gamma contraction (5.3): **OPEN and equivalent to row
  D on the localized primitive space**.
* Uniform birth propagation and row D: **OPEN**.
