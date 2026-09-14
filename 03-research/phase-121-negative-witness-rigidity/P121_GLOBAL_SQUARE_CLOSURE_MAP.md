# P121 -- exact closure map for the global square

## Status

This note freezes the logical boundary after the corpus-wide `A_T` audit.
It contains no new positivity assertion. Its purpose is to prevent the
remaining theorem from being renamed, split into artificial gates, or hidden
inside a factorization.

Write

\[
 \mathscr A_T=G_{\Gamma,T}-m_0I-
 \sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
       (S_{\log n}+S_{-\log n}),
 \qquad
 \Delta_T=P_T\mathscr A_TP_T .                       \tag{1.1}
\]

Then row (d) is `Delta_T >= 0` for every `T>0`.

## 1. The contradiction branch already available

If global positivity fails, exact nesting and the certified initial interval
give a first parameter `T_*` and a nonzero parity vector
`F_* in P_(T_*)` such that

\[
 P_{T_*}\mathscr A_{T_*}F_*=0,                       \tag{1.2}
\]

equivalently

\[
 \mathscr A_{T_*}F_*
 =\alpha e^{-t/2}+\beta e^{t/2}.                    \tag{1.3}
\]

This first-contact reduction is proved. No uniform lower spectral gap is
used or needed.

## 2. The canonical local observation

For zero extension outside `I_T=(-T,T)`, put

\[
 Z_{T,+}=I+K_{T,+},\qquad
 K_{T,+}F(t)=\sum_{2\le n<e^{2T}}n^{-1/2}
             F(t-\log n),                           \tag{2.1}
\]

and set

\[
 h=Z_{T,+}F.                                        \tag{2.2}
\]

Every application of `K_(T,+)` moves at least `log 2` to the right. Hence

\[
 K_{T,+}^{N}=0\quad(N\log2>2T),
 \qquad
 Z_{T,+}^{-1}=\sum_{j=0}^{N-1}(-K_{T,+})^j.         \tag{2.3}
\]

Therefore

\[
 h=0\quad\Longrightarrow\quad F=0                 \tag{2.4}
\]

is already an exact finite algebraic theorem.

## 3. What first contact says in the observed coordinate

The local Euler commutator and Mobius inversion give, for parity
`RF=epsilon F`, the exact equation

\[
 \left[(G_{\Gamma,T}-m_0I)Z_{T,+}^{-1}
       -Z_{T,+}^{-1}Q
       -\varepsilon RZ_{T,+}^{-1}Q\right]h
 =r_\varepsilon,                                    \tag{3.1}
\]

where `r_epsilon` is the corresponding two-Tate forcing. This is v94
(445), now justified on the maximal graph domain by the phase-121 dyadic
bootstrap.

The following are the same open statement:

\[
\begin{aligned}
 &P_T\mathscr A_TF=0\Longrightarrow F=0,             \tag{3.2a}\\
 &(3.1),\ h\in Z_{T,+}\mathcal P_T
       \Longrightarrow h=0,                         \tag{3.2b}\\
 &\mathfrak S_T^{\rm loc}F=0
       \quad\hbox{on }(e^{-T},e^T),                 \tag{3.2c}\\
 &\text{the incoming oriented annular current vanishes.}   \tag{3.2d}
\end{aligned}
\]

Equations (3.2a)--(3.2d) are not four gates. They are four coordinates for
one theorem.

## 4. What the Abel theorem has already closed

For a first-contact vector phase 121 proves

\[
 \mathscr W_\eta(F)
 =2\eta\,
   \|\zeta(1/2+i\,\cdot)\widehat F\|_2^2+o(\eta),
 \qquad \eta\downarrow0.                            \tag{4.1}
\]

Moreover, since the global co-Poisson observation restricts to `h` on the
physical annulus,

\[
 \lim_{\eta\downarrow0}{\mathscr W_\eta(F)\over\eta}
 \ge 4\pi\|h\|_{L^2(I_T)}^2.                       \tag{4.2}
\]

Consequently

\[
 \mathscr W_\eta(F)=o(\eta)
 \quad\Longleftrightarrow\quad h=0
 \quad\Longleftrightarrow\quad F=0.                \tag{4.3}
\]

Thus regularity, finiteness of the Abel slope and identification of its
coefficient are closed. The unproved implication is exactly

\[
 \boxed{
 (3.1)\quad\Longrightarrow\quad
 \mathscr W_\eta(F)=o(\eta).}                       \tag{4.4}
\]

Writing (4.4) as an independent `Abel estimate' does not make it weaker:
by (4.3) it is precisely the oriented annular uniqueness theorem (3.2).

## 5. The one missing mathematical object

The source construction still lacks an identity which distinguishes the two
causal Euler orientations after the symmetric scalar trace. In meromorphic
coordinates the required statement is physical divisibility of the oriented
commutator:

\[
 [Q,Z_+]F=Z_+U_F                                    \tag{5.1}
\]

with `U_F` belonging to the actual causal graph domain across the critical
line, not merely as a meromorphic quotient. Equivalently,

\[
 -{\zeta'\over\zeta}(s)K_F(s-1/2)                  \tag{5.2}
\]

must be holomorphic at every critical zero. This forces
`K_F(rho-1/2)=0`; Cartwright uniqueness then gives `F=0`.

The missing object is therefore not another realization of `mathscr A_T`.
It is a **source-defined oriented range certificate** for (5.1), valid only
on the particular equality state (1.2). It must retain radial divisor data;
boundary modulus, a positive Bohr measure, Real symmetry and the two Tate
moments are provably insufficient.

The critical negative-half analysis now supplies a canonical quantitative
coordinate for this one missing object.  On compact ordinate windows,

\[
 \lim_{\sigma\downarrow0}{
  \|\chi_J(\mathscr A_+-\mathscr A_-)
        (\sigma+i\,\cdot)\|_{H^{-1/2}}^2
 \over\log(1/\sigma)}
 =8\pi\sum_{\substack{\rho=1/2+i\gamma\\\gamma\in J}}
 m_\rho^2|K_F(i\gamma)|^2.                           \tag{5.3}
\]

The symmetric port has zero normalized mass.  Taking the supremum over
compact windows and restricting to the unconditional simple critical family
gives a faithful extended square: it vanishes if and only if `F=0`.
Consequently the terminal theorem can now be stated without a Hardy-space
surrogate:

\[
 \boxed{
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 \mathfrak D_T^{\rm crit}(F)=0.}                    \tag{5.4}
\]

Equation (5.4) is still open.  It is not an additional gate after (5.1): it
is the exact positive defect coordinate of the same oriented divisibility
statement.  Its value is that any proposed source law must annihilate a
specified extensive square, rather than an unnamed boundary leakage.

## 6. Closure after the missing lemma

Once (3.2), (4.4), or (5.1) is proved non-circularly, no further new
mathematics is missing:

```text
oriented equality-state transport
 -> h=0                                  by (4.2)--(4.3)
 -> F=0                                  by the finite inverse (2.3)
 -> no first contact                     by (1.2)
 -> Delta_T >= 0 for every T             by exact nesting
 -> global square on every finite window by the proved form identity
 -> cofinal row (d)                       by the existing core/limit theorem.
```

In particular, `cofinal limit` is not a second research obstruction after
the global sign: it is an already available passage whose hypothesis is the
uniform finite-window sign.

## 7. Binding acceptance test

A proposed terminal lemma is admissible only if it supplies (5.1), or an
equivalent annihilation of `h`, from source data not obtained by solving
`Delta_T>=0`. It is rejected immediately if it is:

1. a square root, Douglas contraction, Schur complement or Sylvester
   solution of `Delta_T`;
2. a boundary-modulus or positive-measure statement blind to inner divisors;
3. a symmetric conservation identity which fixes only the sum of the two
   causal ports;
4. a labelwise prime assertion which does not survive the scalar row-(c)
   trace;
5. a finite-endpoint estimate or a uniform inequality in new notation.

This freezes the barrier. There is one open theorem, not a moving list of
successive residuals.
