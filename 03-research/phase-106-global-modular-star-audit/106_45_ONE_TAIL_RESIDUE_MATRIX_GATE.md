# 106.45 — The one-tail residue matrix gate

## Purpose

Document 106.44 isolates the proposed closing statement: a multiplier in
the mean-periodic complement should not be able to support a negative
arithmetic tail resonance. This note tests that statement before using it.

The one-tail incompatibility is not available. If an off-axis
mean-periodic frequency is provisionally admitted, the literal logarithmic
derivative of zeta produces a two-dimensional real residue matrix with
negative determinant. Hence it has one negative eigenchannel. The negative
resonance is not an accidental error term; it is the exact local signature
of an off-axis frequency.

The calculation uses no zero-location assumption. It is conditional only
in the falsifier sense: *if* a zero with nonzero transverse displacement is
inserted, the proposed one-tail contradiction fails algebraically.

## 1. The smoothed prime operator

For a rapidly decreasing function \(H\), define

\[
 (\mathcal P H)(x)=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}H(x-\log n),
 \qquad
 (\mathcal P_0H)(x)=\int_0^\infty e^{t/2}H(x-t)\,dt.   \tag{1}
\]

With the bilateral Laplace transform

\[
 \mathcal B H(s)=\int_{\mathbb R}H(x)e^{-sx}\,dx,     \tag{2}
\]

absolute convergence in \(\Re s>1/2\) gives

\[
\begin{aligned}
 \mathcal B(\mathcal P H)(s)
 &=-\frac{\zeta'}{\zeta}(s+1/2)\mathcal B H(s),\\
 \mathcal B(\mathcal P_0H)(s)
 &=\frac1{s-1/2}\mathcal B H(s).                      \tag{3}
\end{aligned}
\]

Consequently the backward discrepancy convolution

\[
 \mathcal D=\mathcal P-\mathcal P_0                  \tag{4}
\]

has multiplier

\[
 \boxed{
 d(s)=-\frac{\zeta'}{\zeta}(s+1/2)-\frac1{s-1/2}.}   \tag{5}
\]

The two poles at \(s=1/2\) cancel. If \(s_0\) corresponds to a zero of
\(\zeta(s+1/2)\) of multiplicity \(m\), then

\[
 \operatorname*{Res}_{s=s_0}d(s)=-m.                 \tag{6}
\]

The backward part of the operator in 106.44 is the commutator

\[
 (R_{\psi,-}q)(x)
 =\frac{c}{h(x)}
 \left[q(x)(\mathcal D K)(x)-(\mathcal D(Kq))(x)\right].
                                                               \tag{7}
\]

Formula (7) is 106.44(17) with the forward translate omitted; that forward
term is exponentially smaller at \(+\infty\).

## 2. Cancellation of the diagonal residue

Suppose that \(s_0\) is a mean-periodic frequency, so

\[
 \mathcal B K(s_0)=0.                                 \tag{8}
\]

Then the pole (6) is cancelled in

\[
 d(s)\mathcal B K(s).                                 \tag{9}
\]

Thus the first term in (7) has no \(e^{s_0x}\) residue. The second term
does, and inverse Laplace residue calculus gives

\[
 \boxed{
 R_{\psi,-}q(x)\big|_{s_0}
 =\frac{cm}{h(x)}\mathcal B(Kq)(s_0)e^{s_0x}.}        \tag{10}
\]

The sign in (10) is important. The multiplier has residue \(-m\), while
the convolution occurs with a minus sign in (7); the two signs cancel.

## 3. The real two-channel matrix

Let

\[
 s_0=a+i\gamma,
 \qquad 0<a<1/2,\quad \gamma\ne0,                     \tag{11}
\]

and set

\[
 C(x)=\cosh(s_0x)=A(x)+iB(x),                         \tag{12}
\]

where

\[
 A(x)=\cosh(ax)\cos(\gamma x),
 \qquad
 B(x)=\sinh(ax)\sin(\gamma x).                        \tag{13}
\]

Both \(A\) and \(B\) are real and even. Put

\[
 w(x)=\frac{K(x)}{h(x)}>0                             \tag{14}
\]

and consider a real even leading mode

\[
 F=uA+vB,
 \qquad q=F/h.                                        \tag{15}
\]

Since \(wF\) is even,

\[
\begin{aligned}
 \mathcal B(Kq)(s_0)
 &=\int_{\mathbb R}w(x)F(x)e^{-s_0x}\,dx\\
 &=\int_{\mathbb R}w(x)F(x)\cosh(s_0x)\,dx.           \tag{16}
\end{aligned}
\]

Define

\[
 \alpha=\int wA^2,\qquad
 \beta=\int wAB,\qquad
 \kappa=\int wB^2.                                   \tag{17}
\]

Then

\[
 \mathcal B(Kq)(s_0)
 =(\alpha u+\beta v)+i(\beta u+\kappa v).             \tag{18}
\]

At \(+\infty\),

\[
 A(x)=\frac12e^{ax}\cos(\gamma x)+O(e^{-ax}),
 \qquad
 B(x)=\frac12e^{ax}\sin(\gamma x)+O(e^{-ax}).         \tag{19}
\]

Combining (10), its conjugate, \(2c=1\), and
\(h(x)=\frac12e^{x/2}(1+o(1))\), the residue action on the real
cosine--sine coefficient vector is, up to a common positive multiplicity
and normalization factor, the matrix

\[
 \boxed{
 M_{s_0}=
 \begin{pmatrix}
  \alpha&\beta\\
  -\beta&-\kappa
 \end{pmatrix}.}                                     \tag{20}
\]

### Theorem 1 — Strict one-tail indefiniteness

For every \(a>0\) and \(\gamma\ne0\),

\[
 \boxed{\det M_{s_0}=\beta^2-\alpha\kappa<0.}         \tag{21}
\]

Consequently \(M_{s_0}\) has one strictly positive and one strictly
negative real eigenvalue.

#### Proof

The functions \(A\) and \(B\) are not proportional: \(A(0)=1\), whereas
\(B(0)=0\), and \(B\) is not identically zero because \(a\gamma\ne0\).
Strict Cauchy--Schwarz in \(L^2(w(x)dx)\) therefore gives

\[
 \beta^2<\alpha\kappa.                                \tag{22}
\]

This proves (21). A real two-by-two matrix with negative determinant has
two real eigenvalues of opposite signs. \(\square\)

When \(a=0\), \(B=0\) and the negative channel disappears. Thus the
transition in (21) occurs exactly at the critical axis.

## 4. Consequence for the proposed one-tail proof

The statement

\[
 (hq)*K=0\quad\Longrightarrow\quad
 R_\psi q\ne-\delta q+o(q)\quad(\delta>0)             \tag{23}
\]

cannot be proved from mean periodicity plus the one-tail residue sign. A
hypothetical off-axis frequency produces precisely a negative real residue
channel. Selecting its negative eigenvector gives the leading algebraic
relation required on the right of (23).

This does **not** construct an off-axis zero of zeta. It proves a logical
gate: once such a frequency is provisionally admitted, the one-tail
arithmetic equation and the mean-periodic equation are compatible rather
than contradictory.

For even \(q\), the two tails are reflections of one another, so asking for
failure in “at least one tail” supplies no additional independent equation.
The forward discrepancy translate and the full Gamma channel are lower
order by 106.44 and cannot change the determinant (21).

## 5. Correct surviving target

The tail calculation still gives useful information, but the closing
statement must be global. It must show that the negative eigenvector of
\(M_{s_0}\) cannot extend from its asymptotic residue channel to a vector in
the full ordinary-prime--Gamma form domain satisfying the complete
eigen-equation. Equivalently, one must prove a global matching obstruction
between

1. the negative tail polarization selected by (20), and
2. the central and opposite-tail matching conditions imposed by the full
   theta kernel, every prime power, Gamma and the polar centering.

No estimate confined to one tail can provide that obstruction. The
remaining candidate is therefore a **global Evans determinant** (or an
equivalent two-ended Wronskian) for the full nonlocal generator, normalized
so that (21) supplies its asymptotic stable channel. Its nonvanishing for
\(0<\lambda<1/2\), not one-tail incompatibility, is the precise next theorem.
