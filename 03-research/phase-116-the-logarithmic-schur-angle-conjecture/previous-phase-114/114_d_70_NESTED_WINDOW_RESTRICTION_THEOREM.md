# D.70 — Nested-window restriction theorem

## 1. Statement

Let \(a=\log 2\), let \(0<T\leq T_*=2/5\), and write

\[
\mathcal H_T=L^2([-T,T]).
\]

The directed certificate D.63 proves, at \(T_*=2/5\),

\[
 B_{T_*}(F,F):=
 (q_{19,T_*}+10H_{T_*})(F,F)
 >0.0044\,\|F\|_2^2                         \tag{1.1}
\]

for every nonzero \(F\in\mathcal H_{T_*}\).  Then the same inequality holds
with the same constant on every nested window:

\[
 \boxed{
 B_T(F,F)>0.0044\,\|F\|_2^2
 \quad(0<T\leq2/5,\;0\neq F\in\mathcal H_T).}          \tag{1.2}
\]

Consequently, on the two-Tate-moment primitive subspace of every such
window,

\[
 \boxed{QW_T(F,F)>0.0044\,\|F\|_2^2.}                  \tag{1.3}
\]

Thus no interval continuation is needed between the endpoint/near-endpoint
certificates and \(T=2/5\).  D.65 and D.66 remain useful independent directed
cross-checks, but D.63 plus the theorem below already supplies the complete
nested-window implication.

More generally, a future certificate on a larger window need only be proved
on its primitive subspace.  Zero extension preserves both Tate moments, so a
primitive gap at `T_*` restricts with the same constant to every `T<=T_*`.

## 2. The form is the restriction of one global form

For compactly supported \(F\in L^2(\mathbb R)\), define

\[
\begin{aligned}
 B(F,F)={}&C_{19}\|F\|_2^2
 -c\langle(S_a+S_{-a})F,F\rangle\\
 &-\sum_{j=0}^{19}\iint_{\mathbb R^2}
 e^{-b_j|x-y|}F(y)\overline{F(x)}\,dy\,dx\\
 &+10\left(
 \left|\int_{\mathbb R}F(x)e^{x/2}\,dx\right|^2+
 \left|\int_{\mathbb R}F(x)e^{-x/2}\,dx\right|^2
 \right),                                               \tag{2.1}
\end{aligned}
\]

where \(b_j=2j+1/2\), \(c=\log2/\sqrt2\), and
\((S_aF)(x)=F(x-a)\).  Every term is finite for compactly supported
\(L^2\)-functions.  The form denoted by \(B_T=q_{19,T}+10H_T\) in D.63 is
exactly the restriction of (2.1) to functions supported in \([-T,T]\): the
subscript \(T\) records the support window, not a coefficient depending on
\(T\).

This observation includes the translation contact.  Compressing the global
translation to a window and then evaluating on a function supported in a
smaller window gives the same scalar product as first extending that
function by zero and evaluating the larger compression.  No boundary term
is created.

## 3. Proof by zero extension

For \(T\leq T_*\), let

\[
 E_{T,T_*}:\mathcal H_T\longrightarrow\mathcal H_{T_*}
\]

be extension by zero.  It is an isometry.  From (2.1), term by term,

\[
 B_T(F,F)=B_{T_*}(E_{T,T_*}F,E_{T,T_*}F).              \tag{3.1}
\]

Indeed:

1. the norm term is preserved by the isometry;
2. both translation scalar products are integrals over the support of the
   zero extension and hence are identical;
3. the double kernel integral is unchanged because the extension vanishes
   outside \([-T,T]\);
4. both Tate moments are unchanged for the same reason.

Applying the complete-space estimate (1.1) to \(E_{T,T_*}F\) gives

\[
 B_T(F,F)>0.0044\,\|E_{T,T_*}F\|_2^2
 =0.0044\,\|F\|_2^2,
\]

which proves (1.2).  Notice that the extension is applied to the penalized
form on the complete space; it does not need to preserve an approximate
finite-element constraint.

If instead the estimate at `T_*` is available only for vectors satisfying
the two exact moment equations, the same proof still applies to primitive
`F`: extension by zero leaves both integrals unchanged.  Hence

\[
 B_{T_*}|_{\ker M_{T_*}}\ge\gamma I
 \quad\Longrightarrow\quad
 B_T|_{\ker M_T}\ge\gamma I\qquad(0<T\le T_*).          \tag{3.2}
\]

This primitive nesting form is the version needed for later prime-power
threshold certificates; no full-space penalty is logically required there.

## 4. Removal of the moment penalty

The primitive subspace is defined by the two exact equations

\[
 \int_{-T}^{T}F(x)e^{x/2}\,dx=0,
 \qquad
 \int_{-T}^{T}F(x)e^{-x/2}\,dx=0.                      \tag{4.1}
\]

Therefore \(H_T(F,F)=0\) exactly on that subspace, so (1.2) becomes

\[
 q_{19,T}(F,F)>0.0044\|F\|_2^2.                        \tag{4.2}
\]

D.63 retains the first twenty nonnegative exponential energies of the
complete Gamma factor and discards only a favorable tail.  Hence

\[
 QW_T(F,F)\geq q_{19,T}(F,F),                           \tag{4.3}
\]

and (1.3) follows.

## 5. Endpoint and directed status

D.63 is an Arb certificate on the full ball
\(|T-2/5|\leq10^{-12}\), so in particular it contains the exact value
\(T_*=2/5\).  Its complete-space lower bound is obtained before imposing
the primitive equations:

\[
 \lambda_{\min}(P B_{T_*}P)>0.15530,
 \qquad
 \|B_{T_*}-PB_{T_*}P\|<0.15090.
\]

Their strict difference is \(0.00440\).  The restriction theorem is exact
functional analysis and introduces no additional numerical rounding.

## 6. Scope

The conclusion covers every compact support window \(0<T\leq2/5\).  It does
not assert positivity for \(T>2/5\), where a separate larger-window argument
is required.
