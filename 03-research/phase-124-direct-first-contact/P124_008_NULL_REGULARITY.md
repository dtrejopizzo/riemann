# P124.008 -- null-equation regularity does not cross the half gate

## Status

`OBSTRUCTION.`  The first-contact null equation gives no Sobolev power gain
beyond the phase-121 conclusion

\[
        E_TF \in H^s(\mathbb R)\qquad(0\le s<1/2).
\]

It may be read as an elliptic equation with logarithmic principal symbol,
and this does give harmless iterated logarithmic control inside every
strictly subcritical Sobolev scale.  It does not give any `H^(1/2)` endpoint
or any new `H^{1/2+epsilon}` input for window or virial differentiation.

## 1. Exact equation and domain

Let `I=(-T,T)`, `chi=1_I`, and extend the finite-window state by zero,

\[
        u=E_TF=\chi u .
\]

With the phase-121 notation

\[
        L=\log\langle D\rangle,
        \qquad
        \ell(\xi)={1\over2}\log(1+\xi^2),
\]

the first-contact Euler--Gamma equation has the whole-line form

\[
        (L+R_T)u=f_T .                                      \tag{1.1}
\]

Here

\[
\begin{split}
 R_T={}&[\chi,L]\chi+\chi(g_\Gamma(D)-L)\chi-m_0I \\
 &-\sum_{2\le n<e^{2T}}w_n\chi(\tau_{\log n}+\tau_{-\log n})\chi .
\end{split}                                                 \tag{1.2}
\]

The phase-121 commutator theorem proves

\[
        R_T:H^s(\mathbb R)\to H^s(\mathbb R)
        \quad\hbox{bounded for } |s|<1/2.                  \tag{1.3}
\]

The Tate term is smooth in the open window.  As a whole-line forcing after
sharp zero extension it is a finite linear combination of
`chi e^{t/2}` and `chi e^{-t/2}`.  Hence it lies in `H^s(R)` for every
`s<1/2`; at `s=1/2` a nonzero endpoint jump is forbidden exactly by the
P122.019/P122.029 Lions--Magenes gate.  Thus the natural equation domain is

\[
        u\in Dom(L)\cap H^s,\quad 0\le s<1/2,
\]

together with the two Tate moment equations.  No endpoint half-Sobolev
condition is part of the known first-contact data.

## 2. What the logarithmic equation proves

Fix `0<s<1/2`.  Since `R_T` is bounded on `H^s` and `f_T in H^s`, (1.1)
gives

\[
        Lu=f_T-R_Tu\in H^s                                  \tag{2.1}
\]

whenever `u in H^s`.  Equivalently,

\[
        \langle D\rangle^s\log\langle D\rangle\,u\in L^2.
\]

The same statement is available with any finite logarithmic weight below the
endpoint: if `s<s'<1/2`, then the already proved `u in H^{s'}` implies

\[
        \langle D\rangle^s(\log\langle D\rangle)^k u\in L^2
        \qquad(k<\infty).                                  \tag{2.2}
\]

Thus the null equation supports the expected conclusion: inside the
subcritical range the radical has arbitrary finite logarithmic room.  This
is still weaker than one additional Sobolev power.  Indeed, for every
`epsilon>0`,

\[
        \sup_{|\xi|\to\infty}
        {\langle\xi\rangle^\epsilon\over \log\langle\xi\rangle}
        =\infty,                                           \tag{2.3}
\]

so `L^{-1}` is not a bounded map `L^2 -> H^epsilon`.  A logarithmic
principal symbol is elliptic only in a logarithmic scale; it cannot turn an
`H^s` right side into an `H^{s+epsilon}` solution.

Applying the phase-121 bootstrap with (1.3) for each `s<1/2` therefore gives
precisely

\[
        u\in H^s\quad(s<1/2),
\]

plus finite log weights strictly below `1/2`.  The proof cannot be closed at
`s=1/2`, because the sharp cutoff and the commutator `[chi,L]chi` are only
known below the Lions--Magenes threshold, and because a nonzero Tate line has
exactly the critical jump obstruction.

## 3. Abstract counterexample to any power bootstrap from these hypotheses

The failure is not a technical gap in the dyadic proof.  It follows from the
mapping profile itself.

Choose a nonzero whole-line function with high-frequency density

\[
        |\widehat u(\xi)|^2 \asymp {1\over |\xi|^2\log |\xi|}
        \qquad(|\xi|\gg1),                                  \tag{3.1}
\]

realized by smooth dyadic packets.  Then

\[
        u\in H^s\quad(s<1/2),
        \qquad
        u\notin H^{1/2},                                    \tag{3.2}
\]

and also

\[
        Lu\in H^s\quad(s<1/2),                               \tag{3.3}
\]

because multiplying (3.1) by `log^2 |xi|` still leaves
`|xi|^{2s-2} log |xi|`, which is integrable exactly below `s=1/2`.

Define, on each `H^s`, `0<=s<1/2`, the rank-one bounded perturbation

\[
        Rv=-(Lu){\langle v,u\rangle_{L^2}\over \|u\|_{L^2}^2}.
                                                                    \tag{3.4}
\]

Since `Lu in H^s` for every `0<=s<1/2`, and the `L2` pairing is bounded on
each such `H^s`, this `R` is bounded `H^s -> H^s` throughout the same scale,
and

\[
        (L+R)u=0.                                             \tag{3.5}
\]

Thus an operator with the same abstract mapping profile, logarithmic
principal part plus subcritical bounded perturbation plus smooth zero forcing,
can have a nonzero null vector in all `H^s`, `0<=s<1/2`, and in no
`H^{1/2}`.  This `R` is not self-adjoint and is not claimed to model the
arithmetic `R_T`; it proves only that no argument using just the mapping
facts (1.1)--(1.3) can produce the missing half-Sobolev regularity.

## 4. Consequence for phase 124

The null equation does not legitimize the window derivative or a virial
identity at first contact.  It gives no derivative of the old Euler shift
correlations and no critical transmission trace.  If one assumes the
`H^(1/2)` Tate-collar regularity, then P122.019 kills the Tate coefficient;
using that assumption here would be circular.

The next viable arrow is therefore not an elliptic bootstrap from
`log<D>`.  It must be an additional arithmetic estimate at the critical
collar/window level, for example a bound on the D.240 support defect or an
endpoint transmission identity strong enough to place the completed Tate
current in the true `H^(1/2)` class.
