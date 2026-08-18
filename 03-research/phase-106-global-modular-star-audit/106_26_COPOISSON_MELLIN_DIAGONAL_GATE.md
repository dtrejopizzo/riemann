# 106.26 — The parity-corrected co-Poisson Mellin diagonal gate

## Purpose

Document 106.23 reduces the moving-vector Rayleigh estimate to

\[
 \frac{|QW(R^+,R^+)|}{\|V^+\|^2}
 \ll \lambda^{p_R}d_4,
 \qquad p_R<8.
 \tag{1}
\]

Using Slepian IV's independently stated fixed-order endpoint asymptotic,
106.24 derives unconditionally the additive exterior estimate

\[
 \|(1-P_\lambda)\widehat f_\lambda^{(0)}\|_{H^1}^2
 \ll \lambda^4d_4.
 \tag{2}
\]

The purpose of this note is to identify the exact analytic transfer between
(2) and (1).  There are three results.

1. The inversion-even leakage has an exact scalar coordinate on the complete
   zeta divisor.
2. A Fuchs--Mellin carrier estimate with any fixed polynomial loss makes
   the normalized diagonal tend to zero.  The stronger exponent \(a<4\)
   recovers the quantitative budget (1).
3. The additive \(H^1\) estimate (2) does not imply that carrier estimate.
   A concrete bounded-\(H^1\) family makes the co-Poisson Mellin functional
   unbounded.

Thus the diagonal problem is no longer an unspecified continuity question.
For the direct RH gate of 106.25 it is enough to prove the qualitative
carrier estimate (31) below; the sharper estimate with \(a<4\) is needed
only for the weighted-curvature budget of 106.23.  Neither estimate is
proved in this note.

## 1. Exact Mellin coordinate of the even leakage

Use the notation of 106.12 and 106.23.  Put

\[
 \ell_\lambda=(1-P_\lambda)\widehat f_\lambda^{(0)},
 \qquad
 H_\lambda(v)=\mathcal E(\ell_\lambda)(v),
 \qquad v>\lambda.
 \tag{3}
\]

The two exact moment conditions are

\[
 f_\lambda^{(0)}(0)=0,
 \qquad
 \int_{\mathbb R}f_\lambda^{(0)}(t)\,dt=0.
 \tag{4}
\]

Poisson summation and 106.12(23) give

\[
 R(u)=H_\lambda(u^{-1}),
 \quad 0<u<\lambda^{-1},
 \qquad
 R(u)=0,
 \quad u>\lambda.
 \tag{5}
\]

By Poisson summation and (4),

\[
 H_\lambda(v)=\mathcal E(f_\lambda^{(0)})(v^{-1}).
 \tag{5a}
\]

The BV estimate of 106.12, now applied to \(f_\lambda^{(0)}\) before
multiplicative inversion, gives

\[
 |H_\lambda(v)|\ll v^{-1/2}\operatorname {Var}(f_\lambda^{(0)}).
 \tag{6}
\]

Consequently the Mellin tail

\[
 A_\lambda(w)
 :=\int_\lambda^\infty H_\lambda(v)v^{-w}\,d^*v
 \tag{7}
\]

is holomorphic for \(\Re w>-1/2\).  Define, on the common strip
\(|\Re w|<1/2\),

\[
 \boxed{
 b_\lambda(w)
 :=\frac{A_\lambda(w)+A_\lambda(-w)}{\sqrt2}.}
 \tag{8}
\]

The function \(b_\lambda\) is even and has Schwarz symmetry.

### Theorem 1 — Exact parity coordinate on the divisor

Write a nontrivial zero as

\[
 \rho=\frac12+iz_\rho,
 \qquad
 x_\rho:=\rho-\frac12=iz_\rho.
 \tag{9}
\]

Then

\[
 \boxed{\widehat {R^+}(z_\rho)=b_\lambda(x_\rho)}
 \tag{10}
\]

and, with multiplicities and the complete divisor convention of 106.12,

\[
 \boxed{
 QW(R^+,R^+)=\sum_\rho b_\lambda(x_\rho)^2.}
 \tag{11}
\]

The terms in (11) are not asserted to be nonnegative.  Whenever the right
side is absolutely convergent,

\[
 \boxed{
 |QW(R^+,R^+)|
 \leq\sum_\rho|b_\lambda(x_\rho)|^2.}
 \tag{12}
\]

#### Proof

With the logarithmic Fourier convention of 106.12,

\[
\begin{aligned}
 \widehat R(z)
 &=\int_0^{\lambda^{-1}}
     H_\lambda(u^{-1})u^{-iz}\,d^*u \\
 &=\int_\lambda^\infty H_\lambda(v)v^{iz}\,d^*v
 =A_\lambda(-iz).
\end{aligned}
\tag{13}
\]

Since \(\widehat{JR}(z)=\widehat R(-z)\), equations 106.23(7), (9)
and (13) give

\[
 \widehat {R^+}(z)
 =\frac{A_\lambda(-iz)+A_\lambda(iz)}{\sqrt2}
 =b_\lambda(iz),
 \tag{14}
\]

which proves (10).  The zero-side form is

\[
 QW(G,G)=\sum_{1/2+iz\in Z}
   \overline{\widehat G(\bar z)}\widehat G(z).
 \tag{15}
\]

Because \(b_\lambda\) is even and has Schwarz symmetry,

\[
 \overline{b_\lambda(i\bar z)}
 =b_\lambda(-iz)=b_\lambda(iz).
 \tag{16}
\]

Substitution of (14) into (15) proves (11), and the triangle inequality
gives (12) after absolute convergence has been established. \(\square\)

## 2. The sufficient Fuchs--Mellin carrier estimate

For an integer \(m\geq0\) and a real number \(q>1/2\), introduce the
carrier seminorm

\[
 \|\ell_\lambda\|_{\mathrm{FM},m,q}
 :=\sup_{\substack{|\sigma|<1/2\\ \tau\in\mathbb R}}
 (1+|\tau|)^q(1-2|\sigma|)^m
 |A_\lambda(\sigma+i\tau)+A_\lambda(-\sigma-i\tau)|.
 \tag{17}
\]

The desired source-side theorem is

\[
 \boxed{
 \|\ell_\lambda\|_{\mathrm{FM},m,q}
 \leq C_{m,q}\lambda^a\sqrt{d_4},
 \qquad a<4.}
 \tag{FM}
\]

This estimate retains the two Mellin orientations before taking an absolute
value.  That feature is essential: at a zero, the two full Mellin factors
are respectively divisible by \(\zeta(\rho)\) and \(\zeta(1-\rho)\).

### Theorem 2 — Carrier summability theorem

Let \(m\geq0\), \(q>1/2\), and suppose

\[
 \|\ell_\lambda\|_{\mathrm{FM},m,q}\leq B_\lambda.
 \tag{17a}
\]

Then

\[
 \boxed{
 |QW(R^+,R^+)|\ll_{m,q}B_\lambda^2.}
 \tag{18}
\]

Moreover the normalized vector of 106.23 satisfies

\[
 \boxed{
 \frac{|QW(R^+,R^+)|}{\|V^+\|^2}
 \ll_{m,q}B_\lambda^2.}
 \tag{19}
\]

#### Proof

For \(\rho=\beta+i\gamma\), put

\[
 \delta_\rho
 :=1-2\left|\beta-\frac12\right|
 =2\min(\beta,1-\beta).
 \tag{20}
\]

The Vinogradov--Korobov zero-free region, applied at both sides by the
functional equation, gives, for all sufficiently large \(|\gamma|\),

\[
 \delta_\rho
 \gg
 (\log(3+|\gamma|))^{-2/3}
 (\log\log(e^e+|\gamma|))^{-1/3}.
 \tag{21}
\]

At \(x_\rho=(\beta-1/2)+i\gamma\), (17a), (8), and (21) imply

\[
 |b_\lambda(x_\rho)|
 \ll_m
 B_\lambda\,
 \frac{
   (\log(3+|\gamma|))^{2m/3}
   (\log\log(e^e+|\gamma|))^{m/3}}
 {(1+|\gamma|)^q}.
 \tag{22}
\]

The finitely many remaining zeros are absorbed into the constant.  The
local Riemann--von Mangoldt estimate, including multiplicities, is

\[
 N(T+1)-N(T)=O(\log(3+T)).
 \tag{23}
\]

Consequently

\[
 \sum_\rho
 \frac{
  (\log(3+|\gamma|))^{4m/3}
  (\log\log(e^e+|\gamma|))^{2m/3}}
 {(1+|\gamma|)^{2q}}<\infty.
 \tag{24}
\]

The last series converges precisely because \(q>1/2\).  Equations (12),
(22), and (24) prove (18), as well as absolute convergence of (11).

It remains only to record that the normalization in (19) costs no power of
\(\lambda\).  The normalized constrained coefficients of 106.12 satisfy

\[
 a_j^{\infty}:=h_j(0)\neq0,
 \tag{24a}
\]

and

\[
 (c_0,c_4,c_8)\longrightarrow
 C\left(-(a_0^{\infty})^{-1},
          (a_4^{\infty})^{-1},0\right),
 \qquad C\neq0,
 \tag{25}
\]

because \(q_0/q_4,q_4/q_8=O(\lambda^{-8})\).  Fixed-order
prolate-to-Hermite localization therefore gives

\[
 f_\lambda^{(0)}\longrightarrow
 f_\infty=C\left(-(a_0^{\infty})^{-1}h_0
                  +(a_4^{\infty})^{-1}h_4\right)
 \tag{26}
\]

in the normalization used in 106.10.  The proof of 106.10, Theorem 2,
applies unchanged to this fixed three-mode combination and yields

\[
 V\longrightarrow K_\infty:=\mathcal E(f_\infty)
 \quad\hbox{in }L^2(\mathbb R_+^*,d^*u).
 \tag{27}
\]

The function \(f_\infty\) is nonzero and Fourier invariant.  Hence
\(K_\infty\neq0\) and \(JK_\infty=K_\infty\).  Since

\[
 V^+=\frac{V+JV}{\sqrt2},
 \tag{28}
\]

unitarity of \(J\) gives

\[
 V^+\longrightarrow\sqrt2K_\infty,
 \qquad
 \|V^+\|\geq c_0>0
 \tag{29}
\]

for all sufficiently large \(\lambda\).  Combining (18) and (29) proves
(19). \(\square\)

### Corollary 3 — Quantitative 106.23 budget

If (FM) holds for some fixed \(m\), \(q>1/2\), and \(a<4\), then

\[
 \frac{|QW(R^+,R^+)|}{\|V^+\|^2}
 \ll_{m,q}\lambda^{2a}d_4.
 \tag{30}
\]

Thus \(p_R=2a<8\), exactly the range required by 106.23(17).

### Corollary 4 — Qualitative 106.25 budget

For the direct branch contradiction of 106.25 it is enough that

\[
 \boxed{
 \|\ell_\lambda\|_{\mathrm{FM},m,q}\longrightarrow0
 \quad\text{for some fixed }m\geq0,
 \ q>\frac12.}
 \tag{31}
\]

Indeed, (19) then gives

\[
 \frac{|QW(R^+,R^+)|}{\|V^+\|^2}\longrightarrow0.
 \tag{32}
\]

In particular, (FM) with **any fixed polynomial exponent** \(a\) implies
(31), because

\[
 \lambda^a\sqrt{d_4}
 \asymp
 \lambda^{a+9/2}e^{-2\pi\lambda^2}\longrightarrow0.
 \tag{33}
\]

More generally, a bound

\[
 \|\ell_\lambda\|_{\mathrm{FM},m,q}
 \leq M_\lambda\sqrt{d_4}
 \tag{34}
\]

is sufficient whenever \(M_\lambda^2d_4\to0\).  Thus every subexponential
loss \(\log M_\lambda=o(\lambda^2)\) is harmless for the direct RH gate.
The restriction \(a<4\) belongs only to the stronger weighted-curvature
comparison.

## 3. Why the additive \(H^1\) theorem does not prove (FM)

The unconditional estimate in 106.24(35) is

\[
 \|\ell_\lambda\|_{H^1}^2\ll\lambda^4d_4.
 \tag{35}
\]

There is no bounded map

\[
 H^1(\mathbb R)\ni\ell
 \longmapsto
 \int_\lambda^\infty\mathcal E(\ell)(v)\,d^*v.
 \tag{36}
\]

Here is an explicit obstruction.  Choose a fixed smooth cutoff which is one
on \([2T,T^2/2]\) and supported in \([T,T^2]\), and put, on the positive
half-line,

\[
 \ell_T(t)=c_Tt^{-1/2}\eta_T(t),
 \qquad
 c_T\asymp(\log T)^{-1/2},
 \tag{37}
\]

then extend evenly.  The cutoffs may be chosen with transition widths
comparable to their adjacent endpoints.  Direct integration gives

\[
 \|\ell_T\|_{H^1}\asymp1.
 \tag{38}
\]

For \(2T\leq v\leq3T\), all integers
\(1\leq n\leq T^2/(3v)\) sample the plateau, and positivity gives

\[
\begin{aligned}
 \mathcal E(\ell_T)(v)
 &=v^{1/2}\sum_{n\geq1}\ell_T(nv)\\
 &\gg c_T\sum_{n\leq T^2/(3v)}n^{-1/2}
 \gg\sqrt{\frac{T}{\log T}}.
\end{aligned}
\tag{39}
\]

Therefore

\[
 \int_{2T}^{3T}\mathcal E(\ell_T)(v)\,d^*v
 \gg\sqrt{\frac{T}{\log T}}\longrightarrow\infty.
 \tag{40}
\]

Thus no argument using only (35) can prove (FM), even at the center of the
strip.  The example is not a prolate leakage; its role is to prove that the
missing input must use the special exterior PSWF phase and the joint Mellin
cancellation, not merely the additive Sobolev size.

The exact endpoint identities and Slepian IV's independent endpoint
asymptotic give the unconditional leakage-scale bounds
106.24(20)--(22).  Integration by parts gives, for \(t>\lambda\),

\[
\begin{aligned}
 \ell_\lambda(t)
 ={}&\frac{f_\lambda(\lambda)\sin(2\pi\lambda t)}{\pi t}
 +\frac{f_\lambda'(\lambda)\cos(2\pi\lambda t)}{2\pi^2t^2}\\
 &-\frac1{2\pi^2t^2}
   \int_0^\lambda f_\lambda''(x)\cos(2\pi tx)\,dx.
\end{aligned}
\tag{41}
\]

Equations 106.24(22) and 106.24(35), together with the constrained
coefficient hierarchy, imply

\[
 |f_\lambda(\lambda)|\ll\lambda^{1/2}\sqrt{d_4},
 \qquad
 |f_\lambda'(\lambda)|\ll\lambda^{7/2}\sqrt{d_4}.
 \tag{42}
\]

Both boundary carriers fit even the stronger admissible exponent \(a<4\).
For the qualitative gate, any fixed polynomial loss would suffice.  What
the additive \(H^1\) bound does not control is the last term of (41) after
co-Poisson summation and
the two-orientation Mellin evaluation.  Estimating that term absolutely
loses the exponential leakage scale; estimating the two orientations
separately discards the factors \(\zeta(\rho)=\zeta(1-\rho)=0\).

This is the precise remaining regularity statement:

> **Co-Poisson Fuchs--Mellin diagonal gate.**  Use the exterior prolate
> differential equation, the unconditional endpoint bounds (42), and the two
> zeta-zero
> cancellations jointly to prove (31).  The stronger objective is (FM)
> with some fixed \(a<4\).

It is narrower than Weil positivity on arbitrary tests and narrower than
Gate SPG, but it is not a consequence of the scalar angle defect or of the
additive \(H^1\) identity.

## 4. Status

\[
\begin{array}{c|c}
\text{statement}&\text{status}\\ \hline
\widehat{R^+}(z_\rho)=b_\lambda(\rho-1/2)
  &\text{proved exactly}\\
QW(R^+,R^+)=\sum_\rho b_\lambda(\rho-1/2)^2
  &\text{proved exactly}\\
\|\ell_\lambda\|_{\mathrm{FM},m,q}\le B_\lambda
 \Longrightarrow |QW|\ll B_\lambda^2
  &\text{proved unconditionally}\\
\text{(FM) with any fixed }a\Longrightarrow\mathscr R_L^+\to0
  &\text{proved unconditionally}\\
\text{(FM) with }a<4\Longrightarrow p_R=2a<8
  &\text{proved unconditionally}\\
\|\ell_\lambda\|_{H^1}^2\ll\lambda^4d_4
  &\text{proved unconditionally in 106.24 from Slepian IV}\\
\text{(FM) for the constrained PSWF leakage}
  &\text{open}.
\end{array}
\tag{43}
\]

No statement in this note proves (31), (FM), the vanishing cross residual,
the complementary inertia estimate, or RH.
