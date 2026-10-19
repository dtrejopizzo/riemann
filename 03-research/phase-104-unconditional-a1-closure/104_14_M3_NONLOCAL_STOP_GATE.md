# 104_14 — Nonlocal M3: completed form and stationary stop-gate

## Verdict

M3 produces no new inequality. The canonical nonlocal completion of the Laguerre
test is already the Weil autocorrelation of `103_69`. For the goal **A1**, not for the
stronger margin \(D_n\), one obtains the exact identity

\[
 \boxed{
  C_n^\theta(T)
  ={1\over2}\mathcal W_\zeta(f_n*f_n^\#)-\theta A_n-R_n(T).}
 \tag{1}
\]

Hence A1 is exactly the positivity of the right-hand side of (1). On the critical
line, the spectral symbol of the autocorrelation is a squared modulus; off the line
it is a reciprocal product of indefinite sign. The stationary map

\[
 \gamma\longmapsto u_\gamma={n\over\gamma^2}
 \tag{2}
\]

retains the height but loses the zero's radial coordinate. That coordinate is
precisely the one generating the sign defect.

An exact falsifier within the **bulk**, not at an edge, is given below: for every
\(n\ge300\) divisible by \(100\), a quartet satisfying the functional symmetry falls
at a single stationary point with

\[
 {9\over2500}n<u_\gamma<{1\over225}n,
 \tag{3}
\]

but contributes a strictly negative amount to the completed autocorrelation. A
critical divisor with the same height multiconfiguration contributes a non-negative
amount. Hence no Gram matrix whose sign comes solely from the zero–lobe pairing, the
Laguerre geometry, and the divisor symmetries can prove A1.

This stop-gate **does not refute** a special inequality for the real weights
\(\Lambda(m)\). It proves that M3, as specified, does not contain that inequality:
the stationary map organizes the terms but does not supply the missing arithmetic
sign. Neither A1 nor RH is proved.

---

## 1. Exact nonlocal form of A1

Set, as in `103_69`,

\[
 f_n(x)={\bf1}_{[0,\infty)}(x)L_{n-1}^{(1)}(x),
 \qquad f^\#(x)=e^x\overline{f(-x)},
 \qquad h_n=f_n*f_n^\# .
 \tag{4}
\]

Its Laplace transform is, with \(w=(s-1)/s\),

\[
 \mathcal Lh_n(s)
 =\left(1-w^n\right)\left(1-w^{-n}\right)
 =2-w^n-w^{-n}.
 \tag{5}
\]

The completed explicit formula, with pole, Gamma, primes, conjugation, and boundary
terms kept before evaluation, gives

\[
 \boxed{\mathcal W_\zeta(h_n)=2\lambda_n.}
 \tag{6}
\]

On the other hand, `104_01`, Theorem 1, proves with no hypothesis on zeros that

\[
 C_n^\theta(T)=\lambda_n-\theta A_n-R_n(T).
 \tag{7}
\]

Equations (6)–(7) prove (1), and `104_01`, Theorem 2, gives

\[
 \boxed{
 \mathrm{A1}_\theta(T)
 \iff
 {1\over2}\mathcal W_\zeta(h_n)-\theta A_n-R_n(T)\ge0.}
 \tag{8}
\]

This is already a nonlocal factorization: \(h_n\) is an autocorrelation over the
whole additive line. The prime side has not been separated from the archimedean
side.

On \(s=\frac12+it\) one has \(1-s=\bar s\), and by (5)

\[
 \mathcal Lh_n(s)=|1-w^n|^2\ge0.
 \tag{9}
\]

Off that line, \(w^{-1}\ne\bar w\) and (5) is not a squared modulus. The word
"autocorrelation" makes the symbol positive only after identifying the functional
involution \(s\mapsto1-s\) with conjugation, an identification equivalent to being
on the critical line.

Thus, (8) keeps exactly every term called for by M3, but gives no bound: the
missing bound is the very right-hand side of (8).

---

## 2. What the stationary map keeps and what it loses

In the regime where the Laguerre phase is \(2\sqrt{nu}\), the term for a zero of
positive height \(\gamma\) has phase

\[
 \gamma u-2\sqrt{nu},
 \qquad
 {d\over du}\left(\gamma u-2\sqrt{nu}\right)
 =\gamma-\sqrt{n/u}.
 \tag{10}
\]

This produces (2). The abscissa \(\beta\) does not enter the critical point's
location, but it does enter the amplitude \(e^{(\beta-1/2)u}\). In the Cayley
coordinate it enters as the modulus of

\[
 w_\rho=1-{1\over\rho}=e^{-a+i\vartheta}.
 \tag{11}
\]

A non-critical quartet contributes to (6)

\[
 \boxed{
 8-8\cosh(na)\cos(n\vartheta).}
 \tag{12}
\]

Hence (2) discards exactly \(a\), the parameter that can make (12) exponential and
of both signs. Moreover, the zero count is
\(N(\sqrt n)\sim(\sqrt n/4\pi)\log n\), while there are
\(\asymp n\) Laguerre lobes: (2) is not a bijection, and several zeros can fall in
the same lobe.

None of this invalidates the stationary-phase method as an estimate. It does
prevent using its critical point as a source of exact positivity.

The uniform Plancherel–Rotach phase across the whole bulk is not literally
\(2\sqrt{nu}\); (10) is the small-ratio approximation \(u/n\) used to propose
(2). The falsifier below grants (2) on its own terms. If it is replaced by the
exact bulk phase, the sign conclusion does not change: the stationary equation
still depends on \(n\) and on the frequency \(\gamma\), not on \(\beta\). The two
divisors of §3.5 have the same \(\gamma\)-multiconfiguration and therefore also the
same critical points for the correct uniform phase.

---

## 3. Off-line falsifier within the bulk

### 3.1 Construction

Let \(n\ge300\) be divisible by \(100\), and define

\[
 \vartheta={\pi\over50},
 \qquad
 r={1+\cos\vartheta\over2},
 \qquad
 w=re^{i\vartheta},
 \qquad
 \rho={1\over1-w}.
 \tag{13}
\]

Since \(\cos\vartheta<r<1\), the point \(\rho=\beta+i\gamma\) lies strictly in
the right half of the critical strip. Indeed, with

\[
 D=|1-w|^2=1-2r\cos\vartheta+r^2,
 \tag{14}
\]

one has

\[
 \beta={1-r\cos\vartheta\over D},
 \qquad
 \gamma={r\sin\vartheta\over D},
 \tag{15}
\]

and the identities

\[
 \beta-{1\over2}={1-r^2\over2D}>0,
 \qquad
 1-\beta={r(r-\cos\vartheta)\over D}>0
 \tag{16}
\]

prove \(1/2<\beta<1\). The quartet is completed with

\[
 \rho,\quad\bar\rho,\quad1-\rho,\quad1-\bar\rho.
 \tag{17}
\]

It satisfies conjugation and the functional symmetry. Its two members of positive
height have exactly the same height \(\gamma\), so (2) assigns them the same
\(u_\gamma\).

### 3.2 The height lies in the block \(<\sqrt n\)

For \(0<r<1\), the function in (15) is strictly increasing:

\[
 {d\gamma\over dr}
 ={\sin\vartheta(1-r^2)\over D^2}>0.
 \tag{18}
\]

Evaluating at the endpoints \(r=\cos\vartheta\) and \(r\uparrow1\) gives

\[
 \cot\vartheta<\gamma<{1\over2}\cot{\vartheta\over2}.
 \tag{19}
\]

The elementary inequalities
\(\sin x<x\), \(\cos x>1-x^2/2\), \(\tan x>x\),
\(3<\pi<22/7\) give

\[
 \cot\vartheta>{1\over\vartheta}-{\vartheta\over2}
 >{175\over11}-{11\over350}>15,
 \tag{20}
\]

and

\[
 {1\over2}\cot{\vartheta\over2}
 <{1\over\vartheta}={50\over\pi}<{50\over3}<\sqrt{300}\le\sqrt n.
 \tag{21}
\]

So the quartet belongs to the incomplete block of `104_02`.

### 3.3 The stationary point is uniformly within the bulk

From (20)–(21),

\[
 {9\over2500}n<{n\over\gamma^2}<{1\over225}n.
 \tag{22}
\]

For \(n\ge300\), the left end is greater than \(1>\log2\), and the right end is
less than \(4n\). Moreover, \(u_\gamma/n\) lies in the fixed compact interval
\((9/2500,1/225)\subset(0,4)\): the example uses neither the hard edge nor the
soft edge of Plancherel–Rotach.

If, for a particular index, \(u_\gamma\) coincided with a Laguerre zero, \(r\)
is replaced by a sufficiently close point within
\((\cos\vartheta,1)\). There are only finitely many forbidden values, while (16),
(20)–(22), and the sign below are open conditions and are preserved.

### 3.4 Exact adverse sign

Set \(a=-\log r>0\). Since \(100\mid n\),

\[
 n\vartheta={n\pi\over50}=2\pi{n\over100},
 \qquad \cos(n\vartheta)=1.
 \tag{23}
\]

The quartet's contribution (12) to the completed form is therefore

\[
 \boxed{8-8\cosh(na)<0.}
 \tag{24}
\]

The quartet can be repeated with multiplicity \(M\), multiplying (24) by \(M\),
without altering its heights or the symmetries used by the map.

### 3.5 Same zero–lobe information, opposite sign

Now consider the critical pair \(1/2\pm i\gamma\) with multiplicity two. It has the
same height multiconfiguration as (17), so (2) produces exactly the same
stationary points with the same multiplicity. If

\[
 1-{1\over1/2+i\gamma}=e^{i\phi},
 \tag{25}
\]

its contribution to (6) is

\[
 8\{1-\cos(n\phi)\}\ge0.
 \tag{26}
\]

The inputs seen by map (2) coincide; the signs of (24) and (26) do not. Hence no
sign rule depending only on heights, lobe occupancy, conjugation, and functional
symmetry can represent the completed form.

Divisor (17) does not claim to have the Euler product of \(\zeta\). That is
precisely the logical boundary of the falsifier: it rules out any argument that does
not use additional information from the real von Mangoldt weights. It does not rule
out a new arithmetic theorem that does use it.

---

## 4. Algebraic obstruction to a Gram matrix of lobe charges

There is an independent stop-gate on the prime side. In a finite cutoff, write the
signed lobe charges as \(c=(c_1,\ldots,c_m)\). A1 is affine in those charges:

\[
 \mathcal A(c)=q_{n,\theta}-\sum_{j=1}^m c_j.
 \tag{27}
\]

Suppose that, in an open family of perturbations of the charges, there existed a
nonlocal Gram representation

\[
 \mathcal A(c)=
 \begin{pmatrix}1&c^T\end{pmatrix}
 G
 \begin{pmatrix}1\\c\end{pmatrix},
 \qquad G\succeq0.
 \tag{28}
\]

The Hessian of the left-hand side is zero. Hence the block \(G_{cc}\) is zero. Since
\(G\succeq0\), every \(2\times2\) principal minor containing the first coordinate
also forces \(G_{1c}=0\). The right-hand side of (28) would then be constant,
contradicting (27).

So a PSD form in the charge vector cannot by identity turn the linear A1
functional into a square. If signed terms are added to cancel the Hessian, what
remains is a difference of Gram matrices, and controlling its negative part is
again (27). If nonlinear variables such as \(\sqrt{\Lambda(m)}\) are used, cross
terms appear; for independent weights they must vanish, leaving the oscillatory
diagonal weights already refuted in `103_60` and `103_64`.

This argument does not forbid a special identity satisfied only by the real
sequence \(\Lambda\). It says that such an identity would have to be the new
arithmetic input; it cannot come from lobe geometry or a formal polarization.

---

## 5. Relation to earlier no-gos

* `103_64` proves that the tent matrix collapses exactly to the sawtooth
  \(t-1-\psi(t)\), and kills local PSD, total positivity, Monge, and convex order.
* `103_69` builds the completed autocorrelation (4)–(6) and shows that the
  reciprocal product is not a squared modulus off the line.
* The present document connects those two facts **directly to A1** via
  (1) and adds the bulk falsifier (13)–(26). The stationary map repairs neither of
  the earlier defects because it forgets \(a\).

No candidate matrix, additional arithmetic identity, or intermediate inequality
weaker than A1 remains within M3. The surviving claim is literally

\[
 {1\over2}\mathcal W_\zeta(h_n)\ge
 \theta A_n+R_n(T_n),
 \tag{29}
\]

which, by (8), is A1.

---

## 6. Decision

```text
proved:
  the exact nonlocal completed form (1);
  A1 is exactly equivalent to (8), without replacing it with the margin D_n;
  the stationary map loses the radial parameter that determines the defect;
  an off-line quartet falls uniformly in the bulk and gives a negative sign;
  the same height multiconfiguration on the line gives a non-negative sign;
  a PSD Gram matrix of the charge vector cannot represent a non-constant affine
  functional.

ruled out:
  M3 as a sign derived from the zero–lobe pairing;
  a nonlocal PSD obtained only from geometry, functional symmetry, and conjugation;
  presenting the Weil autocorrelation as unconditional positivity.

not proved:
  a new special inequality for the real von Mangoldt weights;
  (29), A1, or RH.

decision:
  M3 is closed as a stop-gate in its current specification.
  It is reopened only if a concrete arithmetic identity appears that uses the
  real sequence Lambda and that is not, after simplification, equivalent to (29).
```
</content>
