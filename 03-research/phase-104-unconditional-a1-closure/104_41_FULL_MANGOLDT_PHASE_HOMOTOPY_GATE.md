# 104_41 — Full Euler phase and the residue homotopy gate

**Status.** The complete combination was attacked directly,

\[
 M_\Lambda(s):={1\over s-1}+{\zeta'(s)\over\zeta(s)}
 ={d\over ds}\log\{(s-1)\zeta(s)\},                         \tag{1}
\]

without separating simple primes, prime powers, or the pole. In the Euler
half-plane an identity is obtained that preserves the whole phase, along
with a genuine one-sided bound, uniform in the degree:

\[
 \boxed{|\mathcal B_{n,a}|\le3n\qquad(a\ge4).}               \tag{2}
\]

The bound uses no moduli inside \(M_\Lambda\): it integrates the exact
phase of \((s-1)\zeta(s)\). The attempt fails when transporting (2) down
to \(a=1\). The homotopy from the Euler circle to the critical line
crosses exactly the zeros with real part \(>1/2\), and the defect is
exactly the signed residue sum of `104_33`, not an error term estimable
from the boundary phase. A rational reciprocal quartet leaves the
**complete phase identical** on the critical line and changes the moment
by an exponential amount.

Hence the following mechanism is ruled out: "bound the complete phase in
an Euler half-plane of convergence and transfer the bound to \(a=1\) via a
homotopy, with no separate theorem about the residues." Not ruled out is a
new arithmetic inequality that specifically uses the real weights
\(\Lambda(m)\) to jointly control those residues. This document proves
neither A1 nor RH.

## 1. Non-duplication and sign audit

Set

\[
 F(s)=(s-1)\zeta(s),\qquad B_n=A_n-\lambda_n.                \tag{3}
\]

The identities of `phase-102/140–141`, `103_66`, and `104_03` already
imply

\[
 B_n=-{1\over2\pi i}\oint M_\Lambda(s)
              \left({s\over s-1}\right)^n ds,              \tag{4}
\]

on a canonical small circle around \(s=1\). The mere contour identity is
not new. Nor is replacing it with the Cayley symbol: `104_33` proves that
the boundary alone omits the interior residues.

What is new in this attack is quantitative: (2) proves that the phase
estimator is indeed strong before moving the contour, and it localizes its
entire failure in the residue crossing. The sign of (4) is binding. Since

\[
 \lambda_n=A_n+\lambda_n^{\rm prime},
\]

one has \(B_n=-\lambda_n^{\rm prime}\); hence \(M_\Lambda\) appears with a
negative sign in the form of \(B_n\).

There is a second identity that will not be counted as independent
progress. Let \(G(z)=\log F((1-z)^{-1})\) and \(q=1-a^{-1}\). Whenever
\(q\) belongs to the Taylor disc of \(G\), the composition
\(G_a(z)=G(q+z/a)\) gives

\[
 \mathcal B_{n,a}=a^{-n}\sum_{k\ge n}
 {k-1\choose n-1}q^{k-n}B_k.                              \tag{4a}
\]

This is a positive Abel tail, not a one-sided inversion. Using it to
recover \(B_n\) would exactly repeat the Tauberian stop-gate of
`104_17`; moreover a transformed zero within \(|z|\le q\) invalidates the
expansion before it could be hidden as an error term. (4a) is not used in
the proof of (2).

## 2. Complete regularization in an Euler half-plane

Let

\[
 g_n(x)=e^{-x/2}L_{n-1}^{(1)}(x){\bf1}_{x\ge0},
 \qquad
 \widehat g_n(t)=1-
 \left({-1/2+it\over1/2+it}\right)^n,                      \tag{5}
\]

and write

\[
 W_n(t)=|\widehat g_n(t)|^2.                                \tag{6}
\]

For \(a>1\), the following prime series and integral converge
absolutely. We define the complete prime–pole form, with the sign of
\(B_n\), by

\[
\begin{aligned}
 \mathcal B_{n,a}:={}&a\sum_{m\ge2}{\Lambda(m)\over m^a}
       L_{n-1}^{(1)}(a\log m)\\
 &-a\int_1^\infty y^{-a}L_{n-1}^{(1)}(a\log y)\,dy .        \tag{7}
\end{aligned}
\]

Euler's formula and the Laguerre generating function simultaneously give

\[
 \boxed{
 \mathcal B_{n,a}
 =-n[z^n]\log F\!\left({a\over1-z}\right).}                \tag{8}
\]

Coefficient formula (8) continues \(\mathcal B_{n,a}\) from the Euler
domain to a neighborhood of \(a=1\). Removing the regulator in that joint
continuation,

\[
 \boxed{B_n=\lim_{a\downarrow1}\mathcal B_{n,a}.}           \tag{9}
\]

The series in (7) converges directly for every \(a>1\). The semigroup
realization that follows requires \(a>2\); (9) does not claim that its
separate channels have a limit as \(a\) decreases to \(1\).

The realization via the contractive semigroup of `104_36`, now with
\(d\psi\) instead of \(d\theta\), gives the Plancherel identity

\[
 \boxed{
 \mathcal B_{n,a}
 =-{a\over2\pi}\int_{\mathbb R}W_n(t)
 \Re M_\Lambda\!\left(a(1/2+it)\right)dt .}                \tag{10}
\]

In (10), the pole and every \(p^k\) are combined **before** taking the
real part. \(|M_\Lambda|\) does not appear.

## 3. Exact phase identity

For \(a>2\), \(F\) does not vanish on the line
\(s=a(1/2+it)\). Let

\[
 \vartheta_a(t)=\arg F\!\left(a(1/2+it)\right)              \tag{11}
\]

be the continuous branch fixed by \(\vartheta_a(0)=0\). Since

\[
 {d\over dt}\vartheta_a(t)
 =a\Re M_\Lambda\!\left(a(1/2+it)\right),                 \tag{12}
\]

(10) becomes

\[
 \mathcal B_{n,a}
 =-{1\over2\pi}\int_{\mathbb R}W_n(t)\,d\vartheta_a(t).
                                                                    \tag{13}
\]

For \(a\ge4\), the phase is bounded. Indeed,
\(\Re(s-1)\ge1\), so \(|\arg(s-1)|<\pi/2\). Moreover

\[
 |\zeta(s)-1|
 \le\zeta(2)-1
 <{2\over3}<\sin{\pi\over4}.                              \tag{14}
\]

The second inequality can be proved without evaluating \(\pi\):

\[
 \sum_{m=2}^\infty {1\over m^2}
 <{1\over4}+{1\over9}+{1\over16}+{1\over25}
   +\int_5^\infty{x^{-2}}dx
 ={2389\over3600}<{2\over3}.                              \tag{15}
\]

The disc \(|z-1|<2/3\) viewed from the origin has aperture less than
\(\pi/4\). Hence

\[
 \boxed{|\vartheta_a(t)|<{3\pi\over4}\qquad(a\ge4).}      \tag{16}
\]

It remains to compute exactly the variation of the test function. For
\(t>0\), write

\[
 {-1/2+it\over1/2+it}=e^{i\theta(t)},\qquad
 \theta(0)=\pi,\qquad\theta(\infty)=0.
\]

Then

\[
 W_n(t)=2-2\cos(n\theta(t)).                                \tag{17}
\]

Since \(W_n\) is even,

\[
\begin{aligned}
 \mathrm{TV}_{\mathbb R}(W_n)
 &=2\int_0^\pi 2n|\sin(n\theta)|\,d\theta\\
 &=8n.                                                       \tag{18}
\end{aligned}
\]

The boundary terms in the integration by parts of (13) vanish, because
\(W_n(t)=O_n(t^{-2})\). From (13), (16), and (18),

\[
 |\mathcal B_{n,a}|
 \le {1\over2\pi}{3\pi\over4}\,8n
 =3n,                                                        \tag{19}
\]

which proves (2). This is a phase bound, not a modulus bound.

## 4. Where the homotopy breaks

In the coordinate of (8), a nontrivial zero \(\rho=\beta+i\gamma\)
appears at

\[
 z_{\rho,a}=1-{a\over\rho}.                                \tag{20}
\]

The distance to the Hardy circle satisfies the exact identity

\[
 \boxed{
 |z_{\rho,a}|^2-1
 ={a(a-2\beta)\over|\rho|^2}.}                             \tag{21}
\]

As \(a\) decreases from \(4\) to \(1\):

* a zero with \(\beta>1/2\) crosses \(|z|=1\) at \(a=2\beta>1\);
* a critical zero only reaches the boundary at \(a=1\);
* a zero with \(\beta<1/2\) never enters before the endpoint.

Germ (8) remains a well-defined quantity throughout; what stops being
valid is its representation by a defect-free holomorphic boundary.
Applying the correct meromorphic deformation of `104_33` gives

\[
 \boxed{
 B_n=\mathcal P_n+
 \sum_{\Re\rho>1/2}
 {m_\rho\,\mathcal F_n(w_\rho)\over\rho(\rho-1)},
 \qquad w_\rho=1-{1\over\rho}.}                            \tag{22}
\]

Here
\(\mathcal P_n:=\mathcal I_n^\partial(-M_\Lambda\circ s)\) is the radial
boundary moment of `104_33`; via (12)–(13) it is the moment of the
distributional derivative of the phase, including critical zeros, and

\[
 \mathcal F_n(w)
 =n+\sum_{d=1}^{n-1}(n-d)(w^d+w^{-d}).                      \tag{23}
\]

The residue series of (22) converges absolutely for fixed \(n\). Equation
(22) shows that transporting (19) does not cost a contour constant: it
costs exactly the sum that detects right-hand zeros. An estimate of that
sum strong enough for

\[
 B_n\le {1501\over2002}A_n                                  \tag{24}
\]

is the RH-strength theorem that was being sought, not a consequence of
(19).

## 5. Falsifier: same critical phase, exponential residue

Let

\[
 w={i\over2},\qquad
 \rho={1\over1-w}={4+2i\over5},                             \tag{25}
\]

and complete the orbit

\[
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\},
 \qquad Q_\rho(s)=\prod_{\eta\in\mathcal O(\rho)}(s-\eta).
                                                                    \tag{26}
\]

If \(s=1/2+it\), \(\delta=\Re\rho-1/2\), and
\(\gamma=\Im\rho\), then

\[
 \boxed{
 Q_\rho(1/2+it)
 =\{(t-\gamma)^2+\delta^2\}
  \{(t+\gamma)^2+\delta^2\}>0.}                            \tag{27}
\]

Consequently, multiplying \(F\) by \(Q_\rho^M\) does not change the phase
on the critical line (it does multiply the modulus by a positive factor):

\[
 \arg\{F(1/2+it)Q_\rho(1/2+it)^M\}
 =\arg F(1/2+it).                                           \tag{28}
\]

However, the two right-hand residues change \(B_n\) by

\[
 -M Q_n,\qquad
 Q_n=4-2\Re(w^n+w^{-n}).                                    \tag{29}
\]

For \(n=152\),

\[
 \boxed{
 -Q_{152}=2(2^{152}+2^{-152})-4>0,}                         \tag{30}
\]

and multiplicity \(M\) defeats any fixed proportional ceiling without
altering (28). The quartet does not preserve the positive Euler product
of \(\zeta\), so (30) does not refute a specific inequality for the real
weights \(\Lambda(m)\). It does prove that the critical phase and the
analytic homotopy, by themselves, do not supply that inequality.

The same witness passes the crossing gate: \(2\Re\rho=8/5\), so its poles
enter strictly during the path \(4\downarrow1\).

## 6. Decision

```text
proved:
  the complete Mangoldt+pole identity with the sign of B_n;
  the exact representation via the phase of (s-1)zeta(s);
  TV(W_n)=8n;
  the phase-preserving bound |B_{n,a}|<=3n for a>=4;
  the exact crossing law |1-a/rho|^2-1=a(a-2Re rho)/|rho|^2;
  the final defect equal to the signed residue sum of 104_33;
  a rational quartet with identical critical phase and exponential
  residue.

ruled out:
  transferring the strong Euler half-plane bound down to a=1 without
  explicitly controlling the interior residues;
  any argument using only the phase or the boundary symbol, even keeping
  them complex rather than taking moduli.

remains:
  a specific arithmetic inequality for the exact weights Lambda(m) that
  couples the boundary moment with the residue sum and proves (24).

not proved:
  (24), A1, or RH.
```

## 7. Reproducible verification

The file `tools/full_mangoldt_phase_homotopy_gate_check.py` uses only
`Fraction` and Gaussian rationals to check:

1. the rational bound of (15);
2. the exact count giving \(\mathrm{TV}(W_n)=8n\);
3. the crossing identity (21) for quartet (25);
4. the exact positivity of (27) on a rational grid;
5. the exponential residue (30).

Reproduced with

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 full_mangoldt_phase_homotopy_gate_check.py
</content>
