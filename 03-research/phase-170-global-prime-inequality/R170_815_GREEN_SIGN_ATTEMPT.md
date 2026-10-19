# R170_815 — Attempt at a Green sign for the interior contraction

Constructive audit of obligation (ii) of
R170_814. The Tate port with \(S_N^*\), the domain
\(Q_{\log}\), and the two collars of the PC identity are kept.

## 1. Verdict

The corrected contraction of R170_814 produces an exact interior
variation of fixed sign, but it does not produce the flux \(\Phi\). The
proved identity is

\[
 \frac{\mathfrak a_T(F,F)-
        \mathfrak a_{\rho T}(G_\rho F,G_\rho F)}{h}
       =-E_\rho(F)\le0.                                  \tag{1}
\]

By contrast,

\[
 \Phi(F)=\Re\,e_{M,F}(S_N\mathscr F S_LF),\qquad
 e_{M,F}(v)=a_M(F,v)-\langle r_F,v\rangle,               \tag{2}
\]

evaluates the local residual on a different, nonlocal test. No Green
identity has been found that turns (2) into the left-hand side of (1),
nor an inequality that dominates it. Hence

\[
 \Phi(F)+E_\rho(F)\le0                                  \tag{G-}
\]

remains unproved. The following analysis further shows that (G-)
cannot be deduced solely from semidefiniteness of the compression,
radicality, and the existence of an interior competitor: the exterior
coupling remains an independent datum. This is not a counterexample to
the specific zeta arithmetic law, because no first contact of zeta is
exhibited. It IS an exact counterexample to the local inference based
only on the semidefinite compression and an interior competitor; the
complete bridge would need a new arithmetic identity.

## 2. The real interior variation

Let \(F\ne0\), \(H_TF=0\), \(H_T\ge0\), and let \(F\) be primitive. For
the parameters of R170_814,

\[
 G_\rho F=D_\rho F-C(D_\rho F)p-S(D_\rho F)q
\]

is primitive, has the same parity as \(F\), and is supported on
\(I_{\rho T}\). By extension by zero, the form on the smaller window
coincides with the form on the window \(T\) for this datum:

\[
 \mathfrak a_{\rho T}(G_\rho F,G_\rho F)
 =\mathfrak a_T(G_\rho F,G_\rho F).                     \tag{3}
\]

The radical equation on the primitive subspace gives

\[
 \mathfrak a_T(F,G_\rho F)=0,
 \qquad \mathfrak a_T(F,F)=0.                           \tag{4}
\]

Hence

\[
 \mathfrak a_T(G_\rho F-F,G_\rho F-F)
 =\mathfrak a_T(G_\rho F,G_\rho F)=hE_\rho(F)\ge0.     \tag{5}
\]

Equations (3)–(5) prove (1) without taking a derivative with respect to
the window and without additional regularity. This is the entire sign
the contraction yields. In particular, the first contact is used here
only through the nonnegativity of the form on the current window (and,
equivalently, on the smaller one). The fact that larger windows are
negative is compatible with an exterior flux of either sign; it does
not impose stationarity under an enlargement.

## 3. Exact separation of the exterior flux

Set

\[
 z=S_N\mathscr F S_LF.
\]

By the corrected formulation of R170_813, \(z\in Q_{\log}\) and (2) is
well defined as a form. The weak equation implies

\[
 e_{M,F}(v)=0\quad\hbox{for every }v\in Q_{\log}
 \hbox{ supported on }I_T.                              \tag{6}
\]

We do not use here the decomposition \(z=P_Tz+(I-P_T)z\): belonging to
\(Q_{\log}\) does not by itself prove that multiplying by the indicator
of \(I_T\) preserves that domain. What (6) proves, with no additional
multiplier hypothesis, is that \(\Phi\) observes a direction that
cannot be replaced by an admissible interior test.

Thus (G-) is exactly equivalent to the new comparison

\[
 \Re\,e_{M,F}(S_N\mathscr F S_LF)
 \le -\frac1h\mathfrak a_T(G_\rho F-F,G_\rho F-F).     \tag{7}
\]

The two sides of (7) live in different directions: the first evaluates
the residual on a nonlocal Poisson test; the second is the energy of an
interior primitive difference. The weak equation only gives (6) and
contains no mixed term connecting them.

The finite PC identity preserves exactly this conclusion. On the
regular kernel it rewrites the first side of (7) as

\[
\begin{split}
 \Phi(F)={}&\Re\langle
 \{X,E_N\}F-L_M^*E_NF-JH_{M,N}F-H_{M,N}\mathscr F F,
 S_LF\rangle\\
 &-\Re\langle S_N^*r_F,\mathscr F S_LF\rangle.          \tag{9}
\end{split}
\]

For general data, (9) is understood only as the joint extension of (2).
The presence of \(S_N^*\) is indispensable. None of the four PC terms
is the difference \(G_\rho F-F\), and (9) does not by itself contain
the energy of the right-hand side of (8). The cancellation
\(\sum_{d\mid k}\Lambda(d)=\log k\) removes the interior coefficients of
the hyperbola, but it neither creates that mixed term nor fixes the
sign of the collars. There is an exact simplification that isolates the
obstacle. Since \(\log N\ge2T\), and both \(F\) and \(S_LF\) are
supported on \(I_T\), the support geometry gives

\[
 \langle JH_{M,N}F,S_LF\rangle=0.                       \tag{9a}
\]

However the following survives:

\[
 -\Re\langle H_{M,N}\mathscr F F,S_LF\rangle,           \tag{9b}
\]

because \(\mathscr F F\) is not supported on the window. The
coefficients \(h_{M,N}(k)\ge0\) do not fix the sign of this oscillating
pairing. This is the PC term that realizes, in the real problem, the
exterior-coupling freedom exhibited by the following model.

## 4. Exact counterexample to the purely variational bridge

The decoupling above already appears in dimension three. Let the
interior space be \(H_{\rm in}=\mathbb R^2\), the exterior
\(H_{\rm out}=\mathbb R e_3\), and for \(c\in\mathbb R\) define the
symmetric full-line form by

\[
 A_c=\begin{pmatrix}
       0&0&c\\
       0&1&0\\
       c&0&0
     \end{pmatrix}.                                    \tag{10}
\]

Its interior compression is \(\operatorname{diag}(0,1)\), independent
of \(c\), and is positive semidefinite. With

\[
 F=e_1,\qquad r=0,
\]

we have a nonzero radical vector and the interior weak equation
\(\langle A_cF,v\rangle=0\) for every \(v\in H_{\rm in}\). Choose as the
interior competitor \(G=e_2\). For any \(h>0\),

\[
 E=\frac1h\langle A_c(G-F),G-F\rangle=\frac1h>0.        \tag{11}
\]

Taking the exterior test \(z=e_3\), the flux is

\[
 \Phi=\langle A_cF,z\rangle=c.                         \tag{12}
\]

All interior data, the radical, and the energy (11) remain fixed as
\(c\) varies, while \(\Phi+E=c+1/h\) ranges over the whole line. In
particular, \(c=0\) violates (G-) and \(c=-2/h\) satisfies it strictly.

This model does not define a continuous family of windows, does not
realize the specific contraction \(G_\rho\), and does not attempt to
reproduce the von Mangoldt coefficients or PC. Its precise conclusion is
local: no proof of (G-) can use only semidefiniteness of the interior
form, radicality, and the energy of an interior competitor. It does not
rule out a deduction that essentially uses the whole first-contact
family and the concrete formula for \(G_\rho\). That deduction would
need to prove an additional restriction on the real exterior coupling.
Writing PC as an operator equality is not enough; the new step would
have to use the divisor structure to bound (2) by the concrete energy
of (5).

## 5. The remaining arithmetic obligation

Using the exact expansion already fixed in R170_814,

\[
 \Phi=\Omega-\sum_{2\le d\le M}\frac{\Lambda(d)}{\sqrt d}\,\xi_d,
\]

(G-) is exactly

\[
 \sum_{2\le d\le M}\frac{\Lambda(d)}{\sqrt d}\,\xi_d
 \ge \Omega+E_\rho(F).                                 \tag{13}
\]

The inversion \(\Lambda=\mu*\log\) transforms the left side into

\[
 \sum_{km\le M}\frac{\mu(k)\log m}{\sqrt{km}}\,\xi_{km},\tag{14}
\]

but this does not prove (13): both \(\mu(k)\) and the correlations
\(\xi_{km}\) change sign. The interior variation does not control those
correlations either, since it only knows the compressed form.
Consequently (13), with both collars and the crossed Tate term
included, is the new arithmetic inequality still missing.

(13) cannot be replaced by the argument that a positive exterior flux
contradicts the first contact. By definition, after the first contact,
the larger windows are precisely the ones that can acquire negative
values. Nor can the interior quotient (1) be identified with an
exterior derivative: the tests differ, and differentiability of the
family of forms at the contact vector has not been proved.

## 6. Decision on the proposal

The primitive construction of \(G_\rho\), the sign \(E_\rho\ge0\),
identity (1), the definition of \(\Phi\) on \(Q_{\log}\), the adjoint
\(S_N^*\) at Tate, and the joint PC expansion are validated.

The obligation \(\Phi+E_\rho\le0\) is not validated and must not be
presented as a consequence of minimality. The route can only continue
if (13) is proved via a one-sided property of the divisor incidences
that controls the correlations with the real exterior test. Without
that inequality, the R170_814 proposal does not complete the
annihilation of Gamma moments nor the global proof.
