# 104_42 — Degree-adapted noncommutative preconditioner: exact optimum and stop-gate

**Status.** Attacked directly:

\[
 B_n:=A_n-\lambda_n\le \kappa A_n,\qquad
 \kappa={1501\over2002},\qquad n\ge150.                     \tag{1}
\]

Positive, \(n\)-dependent preconditioners were allowed, with no
commutation condition whatsoever. The arithmetic operator simultaneously
contains every prime power, the continuous pole, and the phase. The
pre-compression onto the space of the first \(n\) Laguerre states was also
studied.

The result is exact:

1. the best quadratic completion among **all** noncommutative positive
   preconditioners equals the modulus of the moment one wants to bound;
   when \(B_n>0\), its optimal value is \(B_n\) itself;
2. the canonical degree compression preserves the phase and removes the
   Hardy tail, but its gain over the new datum is
   \(\sqrt{n/2}>1\), so it does not propagate an upper bound.

This rules out **autonomous algebraic optimization** of positive quadratic
completions, not a signed linear identity. Nor does it preclude an
explicit choice of \(R\) receiving a new arithmetic bound; such a bound
would itself have to supply the margin of (1). Neither (1), A1, nor RH is
proved.

## 1. Complete Euler–pole operator

Let

\[
 g_n(x)=e^{-x/2}L_{n-1}^{(1)}(x),\qquad
 (T_tf)(x)=e^{-t/2}f(x-t){\bf1}_{x\ge t}.                    \tag{2}
\]

Then

\[
 \|g_n\|_2^2=n,\qquad
 \langle T_tg_n,g_n\rangle=e^{-t}L_{n-1}^{(1)}(t).          \tag{3}
\]

Write the complete von Mangoldt measure as

\[
 d\Psi(y)=\sum_{m\ge2}\Lambda(m)\,\delta_m(dy).             \tag{4}
\]

For \(a>2\), the Bochner integral

\[
 \boxed{\mathcal D_a
 =a\int_1^\infty T_{a\log y}\{d\Psi(y)-dy\}}                \tag{5}
\]

defines a bounded operator on \(L^2(0,\infty)\), since the norm of each
translation is \(y^{-a/2}\). Set

\[
 v_{n,a}=\mathcal D_ag_n,\qquad
 b_{n,a}=\langle v_{n,a},g_n\rangle\in\mathbb R.             \tag{6}
\]

With no channel separated, (3) gives

\[
\boxed{
\begin{aligned}
 b_{n,a}
={}&a\sum_{m\ge2}{\Lambda(m)\over m^a}
       L_{n-1}^{(1)}(a\log m)\\
 &-a\int_1^\infty y^{-a}L_{n-1}^{(1)}(a\log y)\,dy .
\end{aligned}}                                               \tag{7}
\]

If \(s_a(z)=a/(1-z)\), the coefficient identity of 104_32 proves

\[
 \boxed{
 b_{n,a}=-n[z^n]\log\bigl((s_a(z)-1)\zeta(s_a(z))\bigr).}    \tag{8}
\]

Since \((s-1)\zeta(s)\) is analytic and nonzero at \(s=1\), coefficient
formula (8) continues \(b_{n,a}\) to a neighborhood of \(a=1\), and

\[
 \boxed{\lim_{a\downarrow1}b_{n,a}=A_n-\lambda_n=B_n.}       \tag{9}
\]

In (9) the limit is that of this continuation. The Bochner integral (5)
and the separated series (7) only converge directly in the safe domain
\(a>2\).

So (5)–(9) preserve primes, prime powers, the pole, and the phase. In the
half-plane of absolute convergence,

\[
 \widehat v_{n,a}(t)
 =a\widehat g_n(t)\,\mathcal M\!\left(a(1/2+it)\right),
 \qquad
 \mathcal M(s)=-{\zeta'\over\zeta}(s)-{1\over s-1}.          \tag{10}
\]

The subtraction cancels the pole at \(s=1\), but not the poles of the
zeros.

## 2. Noncommutative optimum

> **Lemma 2.1.** Let \(v,g\) be vectors of a real Hilbert space and
> \(b=\langle v,g\rangle\). For every bounded, self-adjoint, strictly
> positive, invertible operator \(R\), define
>
> \[
> \mathcal C_R(v,g)
> ={1\over2}\{\langle Rv,v\rangle+\langle R^{-1}g,g\rangle\}.
> \]
>
> Then
>
> \[
> b\le\mathcal C_R(v,g),\qquad
> \boxed{\inf_{R>0}\mathcal C_R(v,g)=|b|.}                  \tag{11}
> \]

**Proof.** One has

\[
 2\{\mathcal C_R-b\}
 =\|R^{1/2}v-R^{-1/2}g\|^2\ge0,                             \tag{12}
\]

and Cauchy–Schwarz in the \(R\) metric gives

\[
 \mathcal C_R\ge
 \sqrt{\langle Rv,v\rangle\langle R^{-1}g,g\rangle}
 \ge|\langle v,g\rangle|.                                  \tag{13}
\]

If \(b\ne0\), let \(\sigma=\mathrm{sgn}\,b\). There exists \(R>0\) such
that

\[
 Rv=\sigma g.                                               \tag{14}
\]

Indeed, for \(u=v/\|v\|\), decompose
\(\sigma g/\|v\|=\alpha u+\beta e\), where \(e\perp u\) is unit and
\(\alpha=|b|/\|v\|^2>0\). On
\(\mathrm{span}\,\{u,e\}\), take

\[
 R=\begin{pmatrix}\alpha&\beta\\ \beta&d\end{pmatrix},
 \qquad d>{\beta^2\over\alpha},                             \tag{15}
\]

and extend it by the identity. Then
\(R^{-1}g=\sigma v\), and both terms of (11) equal \(|b|\).
If \(b=0\), \(v\perp g\); weights \(\tau\) on \(v\) and
\(\tau^{-1}\) on \(g\), followed by \(\tau\downarrow0\), give infimum
zero. \(\square\)

Applied to (6),

\[
 b_{n,a}\le\mathcal C_{n,a}[R],\qquad
 \boxed{\inf_{R>0}\mathcal C_{n,a}[R]=|b_{n,a}|.}            \tag{16}
\]

If \(b_{n,a}\le0\), the target with positive right-hand side is automatic
and the completion loses the sign. If \(b_{n,a}>0\), the only regime that
can violate (1), the optimum of (16) is \(b_{n,a}\) itself.
Consequently,

\[
 \mathcal C_{n,a}[R]\le\kappa A_n                           \tag{17}
\]

already contains \(b_{n,a}\le\kappa A_n\). Operator (15) attains the
optimum using the complete arithmetic vector and the sign of
\(b_{n,a}\), so it is not an independent estimate.

Every factorization
\(\|Cv-C^{-*}g\|^2\ge0\) belongs to this class by taking \(R=C^*C\). This
includes triangular factors, dense degree matrices, and non-normal
factors before squaring.

The scope of this conclusion is precise: (16) shows that choosing or
optimizing \(R\) using only Hilbert-space algebra creates no slack. If an
explicit arithmetic construction proved (17) for some \(R\), it would
indeed close (1), but (17) would then contain the new one-sided theorem
and would not be a consequence of Lemma 2.1.

## 3. Conditioning cost at the boundary

Let \(\rho=1/2+i\gamma\) be a critical zero of multiplicity \(m_\rho\).
Locally,

\[
 \mathcal M(s)=-{m_\rho\over s-\rho}+H_\rho(s).              \tag{18}
\]

For each \(n\), such a zero with
\(\widehat g_n(\gamma)\ne0\) can be chosen: Hardy gives infinitely many
critical zeros, while the real zeros of \(\widehat g_n\) form a finite
set. Integrating (18) over a fixed interval around \(\gamma/a\), one
obtains, whenever the continuation of \(v_{n,a}\) belongs to \(L^2\),

\[
 \boxed{\|v_{n,a}\|_2^2\ge {c_{n,\rho}\over a-1}}
 \qquad(1<a<a_{n,\rho}),                                   \tag{19}
\]

with \(c_{n,\rho}>0\).

Define

\[
 m(R)=\|R^{-1}\|^{-1},\qquad
 \mathrm{cond}(R)={\|R\|\over m(R)}.
\]

If \(\mathcal C_{n,a}[R_{n,a}]\le C_0\), then

\[
 m(R_{n,a})\|v_{n,a}\|^2\le2C_0,\qquad
 {n\over\|R_{n,a}\|}\le2C_0.                               \tag{20}
\]

By (19),

\[
 \boxed{\mathrm{cond}(R_{n,a})
 \ge {n c_{n,\rho}\over4C_0^2(a-1)}.}                       \tag{21}
\]

So any finite-cost preconditioner must degenerate at least like
\((a-1)^{-1}\). Noncommutative freedom shifts the divergence onto the
preconditioner's condition number; to reach the optimum it must
singularly align the arithmetic vector with \(g_n\).

## 4. Canonical degree compression

To correctly compress the form, set

\[
 \mathcal X_a={\mathcal D_a+\mathcal D_a^*\over2}.           \tag{22}
\]

Then \(b_{n,a}=\langle\mathcal X_ag_n,g_n\rangle\).
Let \(P_n\) be the orthogonal projection onto

\[
 \mathcal V_n=\mathrm{span}\,\{\phi_0,\ldots,\phi_{n-1}\},
 \qquad \phi_j=e^{-x/2}L_j(x).                              \tag{23}
\]

Since \(g_n=\sum_{j<n}\phi_j\in\mathcal V_n\),

\[
 b_{n,a}=\langle P_n\mathcal X_ag_n,g_n\rangle
 \le\sqrt n\,\|P_n\mathcal X_ag_n\|.                        \tag{24}
\]

Projection \(P_n\) commutes with no nontrivial translation, and (24)
contains no Hardy-tail norm.

In the Abel limit, the symmetric form is the Toeplitz matrix
\(\mathsf Q_0=[q_{|j-k|}]\) of 104_30. With \(B_0=0\),

\[
 q_0=B_1,\qquad
 q_d={B_{d+1}-2B_d+B_{d-1}\over2}\quad(d\ge1).              \tag{25}
\]

Set \(\Delta B_j=B_{j+1}-B_j\), including
\(\Delta B_0=B_1\). For \(0\le j<n\),

\[
\begin{aligned}
 (P_n\mathsf Q_0g_n)_j
 &=q_0+\sum_{d=1}^{j}q_d+\sum_{d=1}^{n-1-j}q_d\\
 &=\boxed{{\Delta B_j+\Delta B_{n-1-j}\over2}}.             \tag{26}
\end{aligned}
\]

Hence (24) has the finite, fully signed limit

\[
 \boxed{
 B_n\le{\sqrt n\over2}
 \left\{\sum_{j=0}^{n-1}
  (\Delta B_j+\Delta B_{n-1-j})^2\right\}^{1/2}.}            \tag{27}
\]

This inequality keeps the joint cancellation of the weights
\(\Lambda(m)\), but it closes no induction. Keep
\(B_0,\ldots,B_{n-1}\) fixed and write \(x=B_n\to+\infty\). The value \(x\)
enters only at \(j=0,n-1\), via

\[
 \Delta B_{n-1}+\Delta B_0=x-B_{n-1}+B_1.                  \tag{28}
\]

The right-hand side of (27) is then

\[
 {\sqrt n\over2}\{2x^2+O_n(x)+O_n(1)\}^{1/2}
 =\boxed{\sqrt{n\over2}\,x+O_n(1).}                         \tag{29}
\]

For \(n\ge3\), \(\sqrt{n/2}>1\). So (27) is compatible with arbitrarily
large values of the new datum \(B_n\), even if all earlier data are
known. The non-uniform diagonal weights, upon optimization, return to
Lemma 2.1 and to the value \(|B_n|\).

## 5. Off-line falsifier

Take

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5}.           \tag{30}
\]

For \(n\equiv0\pmod4\), its quartet contributes

\[
 \lambda_n^{\rm off}=4-2(2^n+2^{-n}),\qquad
 B_n^{\rm off}=2(2^n+2^{-n})-4.                             \tag{31}
\]

At \(n=152\),

\[
 B_{152}^{\rm off}>{1501\over2002}\,152^2.                 \tag{32}
\]

Optimum (16) returns the same excessive value and does not certify the
false divisor. When deforming from \(a>2\), the pole of (10) crosses the
boundary at \(a=8/5\), as in 104_36. The compression does not erase it
either: the growth reappears at the two extreme coordinates of (28).

## 6. Decision

    proved unconditionally:
      the Euler--pole operator with every Lambda(m), (5)--(10);
      the optimum over every positive noncommutative R, (11)--(16);
      cond(R) >= c/(a-1) for every bounded cost whose
        vector continuation belongs to L2, (21);
      degree compression and the signed formula (26)--(27);
      defective gain sqrt(n/2)>1, (29);
      failure against the off-line quartet, (30)--(32).

    ruled out:
      closing (1) by pure algebraic optimization of a positive quadratic
        completion;
      obtaining the margin solely by singularizing the preconditioner;
      using the degree projection as an inductive recurrence.

    remains open:
      a one-sided linear inequality preserving the canonical sign of
      Lambda(m) without turning the correlation into a positive energy;
      (1), A1, and RH.

## 7. Verification

Run:

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 degree_adapted_noncommutative_gate_check.py

The program uses Fraction. It checks non-diagonal positive matrices that
attain (11) for inner products of both signs, the Toeplitz inversion
(25), the coordinates (26), the \(n/2\)-squared coefficient of
(29), and the falsifier (32). No floating point is used.
</content>
