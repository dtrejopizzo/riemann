# D.202 — Exact A–B–C jet/moment pullback of the nuclear form

## Scope

This note closes the comparison statement, not the Hodge-sign statement.
It identifies the two boundary jets with the two primitive Mellin moments
used in A–B–C and proves, by a direct change of variables and
polarization, that the pulled-back row-C Lefschetz form is exactly
\(B_{\rm nuc}\).  The equality contains every prime power and the complete
archimedean Gamma contribution.  It neither assumes nor proves a sign.

Throughout, \(f,g\in C_c^\infty(\mathbb R_+^\times)\), Haar measure is
\(d^\times x=dx/x\), and

\[
  F(t)=({\cal U}f)(t):=e^{t/2}f(e^t),\qquad
  G(t)=({\cal U}g)(t):=e^{t/2}g(e^t).
                                                               \tag{1.1}
\]

The map \({\cal U}\) is the central logarithmic conjugation.  It is unitary
from \(L^2(\mathbb R_+,dx)\) to \(L^2(\mathbb R,dt)\); it is not unitary
for Haar measure \(d^\times x\).  Haar measure is used below only in the
Mellin transform and multiplicative convolution.  Since the test functions
are compactly supported, both operations and the conjugation are defined on
the common test space.

## 1. The two jets are exactly the two primitive moments

With

\[
 \widehat f(s)=\int_0^\infty f(x)x^s\,d^\times x,
                                                               \tag{1.2}
\]

the substitution \(x=e^t\) gives

\[
 \widehat f(s)
 =\int_{\mathbb R}F(t)e^{(s-1/2)t}\,dt.              \tag{1.3}
\]

Consequently

\[
 \boxed{\widehat f(0)=J_-(F),\qquad
        \widehat f(1)=J_+(F)},                        \tag{1.4}
\]

where

\[
 J_-(F)=\int_{\mathbb R}e^{-t/2}F(t)\,dt,\qquad
 J_+(F)=\int_{\mathbb R}e^{t/2}F(t)\,dt.              \tag{1.5}
\]

For the Fourier–Laplace transform

\[
 {\cal F}_{\mathbb C}F(z)=\int_{\mathbb R}F(t)e^{-izt}\,dt,
                                                               \tag{1.6}
\]

(1.4) becomes

\[
 J_-(F)={\cal F}_{\mathbb C}F(-i/2),\qquad
 J_+(F)={\cal F}_{\mathbb C}F(i/2).                  \tag{1.7}
\]

Thus the following three definitions give the same primitive subspace:

\[
 \begin{aligned}
 {\cal P}
 &=\{f:\widehat f(0)=\widehat f(1)=0\}\\
 &\xrightarrow[\cal U]{\;\simeq\;}
 \{F:J_-(F)=J_+(F)=0\}\\
 &=\{F:{\cal F}_{\mathbb C}F(-i/2)
          ={\cal F}_{\mathbb C}F(i/2)=0\}.            \tag{1.8}
 \end{aligned}
\]

No coordinate choice is present in (1.8): the two functionals are the
two Tate characters \(s=0,1\), equivalently the two primitive ruling
degrees of A.

## 2. Multiplicative correlation becomes additive translation correlation

Let

\[
 g^\vee(x)=x^{-1}\overline{g(x^{-1})},\qquad
 h=f*g^\vee,                                         \tag{2.1}
\]

where convolution is multiplicative.  Define

\[
 C_{F,G}(a)=\int_{\mathbb R}F(t)\overline{G(t-a)}\,dt
           =\langle F,S_aG\rangle,\qquad
 (S_aG)(t)=G(t-a).                                   \tag{2.2}
\]

A direct calculation gives the exact identity

\[
 \boxed{e^{a/2}h(e^a)=C_{F,G}(a).}                   \tag{2.3}
\]

Indeed,

\[
 \begin{aligned}
 h(e^a)
 &=\int_0^\infty
       f(y)g^\vee(e^a/y)\,d^\times y\\
 &=e^{-a}\int_0^\infty
       y f(y)\overline{g(ye^{-a})}\,d^\times y\\
 &=e^{-a/2}\int_{\mathbb R}
       F(t)\overline{G(t-a)}\,dt .
 \end{aligned}                                      \tag{2.4}
\]

This proves (2.3), including its central factor and its orientation.

## 3. Every finite contact, including every \(p^k\)

The finite part of the row-C Lefschetz functional evaluated on \(h\) is

\[
 I_{\rm fin}(h)
 =\sum_{p}\sum_{k\ge1}\log p\,
       \bigl(h(p^k)+p^{-k}h(p^{-k})\bigr).             \tag{3.1}
\]

Apply (2.3) with \(a=\pm k\log p\).  Since
\(\Lambda(p^k)=\log p\),

\[
 \boxed{
 I_{\rm fin}(f*g^\vee)
 =
 \sum_p\sum_{k\ge1}
 \frac{\Lambda(p^k)}{p^{k/2}}
 \bigl(C_{F,G}(k\log p)+C_{F,G}(-k\log p)\bigr).
 }                                                    \tag{3.2}
\]

For compactly supported \(F,G\), the correlation \(C_{F,G}\) is compactly
supported.  Therefore (3.2) is literally a finite sum: no rearrangement
or convergence convention is needed.  It contains every \(k\ge1\);
replacing it by the square-free or prime-only term would change the
form.

The coefficient in (3.2) is precisely the A–B local datum:

\[
 \deg_{\det}{\mathbb L}_{p^k}\,
     p^{-k/2}
 =\log p\,p^{-k/2}
 =\Lambda(p^k)p^{-k/2}.                              \tag{3.3}
\]

Here \(\deg_{\det}{\mathbb L}_{p^k}=\log p\) comes from the reduced
derived prime contact, while \(p^{-k/2}\) is the central metric character
of the \(k\)-fold Witt orbit.  If \(n\) has at least two distinct prime
factors, the reduced dynamic contact and \(\Lambda(n)\) both vanish.
Thus (3.3) identifies the whole finite row-C orbit with the A–B contact
orbit, not merely their total masses.

## 4. The complete Gamma contribution

Use the unitary Fourier convention

\[
 \widehat F(\tau)=\int_{\mathbb R}F(t)e^{-i\tau t}\,dt,
 \qquad
 \langle F,G\rangle
 ={1\over2\pi}\int_{\mathbb R}
       \widehat F(\tau)\overline{\widehat G(\tau)}\,d\tau .
                                                               \tag{4.1}
\]

Put

\[
 \gamma_\infty(\tau)
 =\log\pi-\Re\psi\!\left({1\over4}+{i\tau\over2}\right).
                                                               \tag{4.2}
\]

The archimedean term in row C, after the same central logarithmic
transform, is

\[
 \boxed{
 I_\infty(f*g^\vee)
 =G_\infty(F,G)
 ={1\over2\pi}\int_{\mathbb R}
       \gamma_\infty(\tau)
       \widehat F(\tau)\overline{\widehat G(\tau)}\,d\tau .
 }                                                    \tag{4.3}
\]

This is the complete real Gamma factor: both the nonlocal digamma part
and its finite-part constant are present.  Equivalently, with

\[
 m_0=\log\pi-\psi(1/4)
 \quad\hbox{and}\quad
 d\mu(r)={e^{-r/2}\over1-e^{-2r}}\,dr,
                                                               \tag{4.4}
\]

the digamma difference formula and Plancherel give

\[
 G_\infty(F,G)
 =m_0\langle F,G\rangle
  -\int_0^\infty
     \langle F-S_rF,G-S_rG\rangle\,d\mu(r).           \tag{4.5}
\]

Formula (4.5) is the Gamma boundary energy used in the A–C realization.
It is identical to (4.3), not an asymptotic or a selected collection of
archimedean modes.

## 5. Exact pullback theorem

Define the polarized nuclear form on logarithmic test functions by

\[
 \begin{aligned}
 B_{\rm nuc}(F,G)
 :={}&G_\infty(F,G)\\
 &+\sum_p\sum_{k\ge1}
 \frac{\Lambda(p^k)}{p^{k/2}}
 \bigl(C_{F,G}(k\log p)+C_{F,G}(-k\log p)\bigr).
                                                               \tag{5.1}
 \end{aligned}
\]

Let \(I_\Delta^{\rm nuc}=I_{\rm fin}+I_\infty\) be the row-C nuclear
Lefschetz functional.  Equations (2.3), (3.2), and (4.3) prove:

\[
 \boxed{
 I_\Delta^{\rm nuc}(f*g^\vee)
   =B_{\rm nuc}({\cal U}f,{\cal U}g).
 }                                                    \tag{5.2}
\]

This is an equality of polarized sesquilinear forms.  Hence it also holds
on every finite Gram matrix and, by polarization, is not merely a
diagonal equality.

Under (1.8), its primitive restriction is exactly

\[
 I_\Delta^{\rm nuc}(f*g^\vee)
   =B_{\rm nuc}(F,G),
 \qquad F,G\in\ker J_-\cap\ker J_+.                  \tag{5.3}
\]

Consequently the desired row-D inequality is precisely

\[
 B_{\rm nuc}(F,F)\le0
 \quad\text{for}\quad J_-(F)=J_+(F)=0.               \tag{5.4}
\]

The comparison (5.2) is already complete and independent of (5.4).
In particular it does not define a quotient using the sign of
\(B_{\rm nuc}\), invoke zeros of zeta, or remove a positive spectral
subspace.

## 6. Operator form on a compact support chart

If \(\operatorname{supp}F\subset[-T,T]\), only integers
\(2\le n<e^{2T}\) occur in (5.1).  Let

\[
 G_{\Gamma,T}
 ={\cal F}^{-1}\gamma_\infty{\cal F}
 \quad\hbox{on the zero-extension chart},             \tag{6.1}
\]

and let \(S_a\) denote the corresponding truncated translation.  Then

\[
 B_{\rm nuc}(F,G)=\langle F,L_TG\rangle,              \tag{6.2}
\]

where

\[
 L_T
 =G_{\Gamma,T}
  +\sum_{2\le n<e^{2T}}
      {\Lambda(n)\over\sqrt n}
      \bigl(S_{\log n}+S_{-\log n}\bigr).             \tag{6.3}
\]

Equivalently the row-D positive candidate is

\[
 A_T=-L_T.                                            \tag{6.4}
\]

The two primitive constraints are the exact rank-two jet map
\(J_T=(J_-,J_+)\).  Thus the chart problem is the non-circular operator
statement

\[
 P_{\ker J_T}A_TP_{\ker J_T}\ge0.                    \tag{6.5}
\]

Equations (6.3)–(6.5) are the bridge to the three-block Feshbach
criterion: all prime powers and the entire Gamma operator are already
inside \(A_T\); only the independent positivity estimate remains.

## Conclusion

The two jets, the primitive A ruling moments, and the Tate points are one
and the same pair of functionals.  The row-C finite orbit pulls back to
the full von-Mangoldt translation orbit, including every \(p^k\), and its
archimedean term pulls back to the complete digamma/Gamma boundary
operator.  Therefore the pullback is exactly \(B_{\rm nuc}\), with no
missing local term and no normalization ambiguity.

This establishes the decisive A–B–C comparison.  It deliberately leaves
the separate Hodge inequality (6.5) to the source-defined positivity
argument.
