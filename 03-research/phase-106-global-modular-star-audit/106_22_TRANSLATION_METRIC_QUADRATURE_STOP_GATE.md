# 106.22 — Translation-metric quadrature and the compact-support stop gate

## Purpose

The compensated identity of 106.19 contains the function

\[
 G_f(u):=\|f-\tau_u f\|_2^2.
\tag{1}
\]

This note asks whether the elementary geometry of \(G_f\)—negative type,
the triangle inequality for \(\sqrt{G_f}\), and the terminal value forced by
compact support—can transport the negative continuous PNT density onto the
literal prime-power atoms and prove the missing Weil inequality.

There are four conclusions.

1. The identity of 106.19 has an exact signed quadrature form on the cone of
   translation metrics.
2. That form gives a new unconditional short-support theorem.
3. Negative type, subadditivity, and even the single endpoint condition
   \(G(L)=2\|f\|^2\) do not imply the quadrature inequality.  An explicit
   one-frequency Hilbert translation metric violates it with the ordinary
   prime-power weights.
4. The full plateau \(G(u)=2\|f\|^2\) for every \(u\ge L\), equivalently the
   compactly supported positive-definite autocorrelation, is load-bearing.
   On that full cone the desired quadrature inequality is exactly the
   compressed Weil positivity theorem, not a generic metric consequence.

No statement below proves the global Weil inequality or RH.

## 1. Nonduplication audit

The following earlier constructions are the closest semantic matches.

| Earlier work | What is already proved there | Relation to this note |
|---|---|---|
| 103.61 | Exact von Mangoldt quantile cells and their first-moment/curvature decomposition | Already contains the canonical transport idea; it must not be reopened as new |
| 103.64 | Exact collapse of the cell tents to the Chebyshev sawtooth; Monge cross difference zero; convex-order signs fail | Kills a generic quantile, Monge, or convex-order closure |
| E72.285 and E72.294 | Exact arithmetic autocorrelation ceiling and signed subtraction of the continuous PNT main operator | In fact E72.294's \(\Delta_{\rm rem}=-\sum w_mQ_{a_m}+\int e^{u/2}Q_u\,du\), with \(Q_u=F_f(u)\), is exactly \(-\mathcal A_\Delta\).  Only the complement \(G=2M-F\), scalar bookkeeping, and the short-support corollary are new here |
| E72.379 and E72.386 | Prime terms are signed quadrature defects; absolute BV control is exponentially too large | Same structural rule: retain the full signed prime sum |
| E101.042 | Gaussian Weil quadrature for finite secular nodes | A different quadrature cone; it does not use translation distances |
| 103.69 | Completed Weil autocorrelation and the off-line quartet sign obstruction | Already proves that the word ``autocorrelation'' does not create unconditional positivity |
| Phase 102, 169 and 172 | Schoenberg negative type and increment Toeplitz positivity in the **Li index** \(n\) | Distinct variable and distinct kernel |
| Phase 102, 192 and 195 | Global positivity does not supply the missing signed comparative margin | Same logical warning, but not the identity below |
| Phase 60, `RH-PROOF-PAPER` | Gamma and prime jump/carre-du-champ forms; generic Markov and translation invariance do not force the desired spectral conclusion | The positive jump-square viewpoint is old in the project |
| 106.17 and 106.19 | The positive translation square and compensated prime--Gamma--pole identity | Starting point; the metric consequences were not developed |

Thus neither quantile transport, the arithmetic discrepancy,
autocorrelation, nor the positive jump square is new.  The genuinely new
residue is narrower: the complement coordinate \(G=2M-F\) with all scalar
terms retained, the resulting quantitative short-support refinement, and
the character stop-gate separating generic negative type from the
compact-support autocorrelation cone.  This is not a new global route.

## 2. Exact metric quadrature

Let \(f\in C_c^\infty(I_L)\), extended by zero to \(\mathbb R\), and put

\[
 M=\|f\|_2^2,
 \qquad
 H_f(u)=\langle f,\tau_u f\rangle,
 \qquad
 F_f(u)=H_f(u)+H_f(-u).
\tag{2}
\]

Then

\[
 G_f(u)=2M-F_f(u).
\tag{3}
\]

Write

\[
 a_m=\log m,
 \qquad
 w_m={\Lambda(m)\over\sqrt m},
 \qquad
 S_L=\sum_{a_m\le L}w_m,
\tag{4}
\]

and retain

\[
 \nu_*(du)={e^{-5u/2}\over1-e^{-2u}}\,du,
 \qquad
 c_*=\gamma+{\pi\over2}+3\log2+\log\pi-4.
\tag{5}
\]

### Theorem 1 — Translation-metric quadrature identity

The semilocal completed Weil form is

\[
\boxed{
\begin{aligned}
 QW_L(f,f)
 &=\int_0^\infty G_f(u)\,\nu_*(du)
   +\sum_{a_m\le L}w_mG_f(a_m)
   -\int_0^L e^{u/2}G_f(u)\,du\\
 &\quad-
 \left\{c_*+2S_L-4(e^{L/2}-1)\right\}M.
\end{aligned}}
\tag{6}
\]

#### Proof

By 106.19,

\[
 QW_L(f,f)=\int_0^\infty G_f\,d\nu_*-c_*M-\mathcal A_\Delta(f),
\tag{7}
\]

where

\[
 \mathcal A_\Delta(f)
 =\sum_{a_m\le L}w_mF_f(a_m)
  -\int_0^Le^{u/2}F_f(u)\,du.
\tag{8}
\]

Insert \(F_f=2M-G_f\) in (8) and use

\[
 \int_0^Le^{u/2}\,du=2(e^{L/2}-1).
\tag{9}
\]

Substitution in (7) gives (6).  If \(a_m=L\), compact support gives
\(G_f(L)=2M\), so its atom in the first line cancels its contribution to
\(2S_LM\), as it must.  \(\square\)

## 3. Exact geometry of \(G_f\)

### Theorem 2 — Negative type, metric subadditivity, and the terminal plateau

The function \(G_f\) has the following properties.

1. It is even, continuous, nonnegative, and \(G_f(0)=0\).
2. It is conditionally negative definite: for any \(t_1,\ldots,t_N\in
   \mathbb R\) and \(c_1,\ldots,c_N\in\mathbb C\) with
   \(\sum_jc_j=0\),

   \[
    \sum_{j,k}c_j\overline{c_k}G_f(t_j-t_k)
    =-2\left\|\sum_jc_j\tau_{t_j}f\right\|_2^2\le0.
   \tag{10}
   \]

3. The Hilbert distance \(d_f(u)=\sqrt{G_f(u)}\) is subadditive:

   \[
    d_f(u+v)\le d_f(u)+d_f(v).
   \tag{11}
   \]

4. If the support of \(f\) has length at most \(L\), then

   \[
    \boxed{G_f(u)=2M\qquad(|u|\ge L).}
   \tag{12}
   \]

#### Proof

The first assertions follow directly from (1).  For (10), expand the
squares; the constant term vanishes because \(\sum c_j=0\), while the
autocorrelation matrix is the Gram matrix of the translated vectors.
For (11), use unitarity of translation:

\[
 \|f-\tau_{u+v}f\|
 \le\|f-\tau_uf\|+\|\tau_uf-\tau_{u+v}f\|
 =d_f(u)+d_f(v).
\tag{13}
\]

For \(|u|\ge L\), the interiors of the supports of \(f\) and \(\tau_uf\)
are disjoint, so \(H_f(u)=0\).  Equations (1)--(3) give (12). \(\square\)

The plateau (12) is much stronger than one endpoint equality.  It is the
support theorem in the metric coordinate.

## 4. A short-support positivity theorem

Assume \(0<L<\log2\).  There are no prime-power atoms in the open support
range.  From (6) and (12), one obtains the exact decomposition

\[
\begin{aligned}
 QW_L(f,f)
 &=\int_0^L
   \left\{{e^{-5u/2}\over1-e^{-2u}}-e^{u/2}\right\}G_f(u)\,du\\
 &\quad+
 \left\{
  2\int_L^\infty {e^{-5u/2}\over1-e^{-2u}}\,du
  -c_*+4(e^{L/2}-1)
 \right\}M.
\end{aligned}
\tag{14}
\]

Let \(L_c\) be the unique positive solution of

\[
 e^{-3L_c}+e^{-2L_c}=1.
\tag{15}
\]

Thus \(L_c=0.2811995743\ldots\).  Define

\[
 B(L)=
 4\sum_{k=0}^\infty
 {e^{-(4k+5)L/2}\over4k+5}
 -c_*+4(e^{L/2}-1).
\tag{16}
\]

The series in (16) is exactly twice the tail integral in (14).

### Theorem 3 — Explicit prime-free support range

If

\[
 0<L\le L_c,
 \qquad
 B(L)\ge0,
\tag{17}
\]

then

\[
 \boxed{QW_L(f,f)\ge B(L)\|f\|_2^2\ge0}
\tag{18}
\]

for every test supported in an interval of length at most \(L\).

#### Proof

The first coefficient in (14) is nonnegative precisely when

\[
 {e^{-5u/2}\over1-e^{-2u}}\ge e^{u/2},
\tag{19}
\]

or equivalently \(e^{-3u}+e^{-2u}\ge1\).  This holds for
\(0<u\le L_c\).  Discard that nonnegative integral and use (16). \(\square\)

On \((0,L_c)\),

\[
 B'(L)=-2{e^{-5L/2}\over1-e^{-2L}}+2e^{L/2}\le0.
\tag{20}
\]

The positive-series formula in (16), with its geometric tail bound, gives
\(B(0.15)>0\) and \(B(0.16)<0\).  Hence there is a single short-support
threshold \(L_s\) in this interval, defined by \(B(L_s)=0\).  The
reproducible evaluation gives

\[
 L_s=0.15263091445\ldots.
\tag{21}
\]

The decimal is diagnostic; the exact theorem is (17).  In particular, any
explicit \(L\) for which a finite lower bound on the positive series in
(16) proves \(B(L)\ge0\) gives a fully elementary certified instance.

## 5. Negative type alone cannot prove the quadrature

The support plateau in Theorem 2 cannot be replaced by abstract negative
type.  Let \(\mathcal H=\mathbb C\), let

\[
 U_u z=e^{i\omega u}z,
 \qquad \|v\|^2=M,
\tag{22}
\]

and define the translation metric of this unitary orbit:

\[
 G_\omega(u)=\|v-U_uv\|^2
 =2M(1-\cos\omega u).
\tag{23}
\]

It satisfies (10)--(11).  Extend the right side of (6) to this abstract
metric and denote it by \(\mathfrak Q_L(M,G_\omega)\).  The Gamma term is

\[
 \int_0^\infty G_\omega\,d\nu_*
 =2M\sum_{k=0}^\infty
 {\omega^2\over
  \alpha_k(\alpha_k^2+\omega^2)},
 \qquad \alpha_k={5\over2}+2k,
\tag{24}
\]

and the continuous PNT term is

\[
 \int_0^Le^{u/2}G_\omega(u)\,du
 =4M(e^{L/2}-1)
 -2M\Re{e^{(1/2+i\omega)L}-1\over1/2+i\omega}.
\tag{25}
\]

Take

\[
 L=1.78,
 \qquad
 \omega={\pi\over2L}.
\tag{26}
\]

Then \(G_\omega(L)=2M\), so even the terminal value is correct.  The
literal atoms in (6) are exactly \(m=2,3,4,5\).  Substitution in
(6), using (24)--(25), gives

\[
 \boxed{
 {\mathfrak Q_{1.78}(M,G_\omega)\over M}
 =-0.02111091956\ldots<0.}
\tag{27}
\]

The tail after \(K\) terms in (24) is bounded by

\[
 0\le R_K
 \le {M\omega^2\over2(2K+1/2)^2},
\tag{28}
\]

so the sign in (27) is certified with a very short finite computation.

This is not a counterexample to Weil positivity: (23) does **not** satisfy
the plateau (12).  It is a counterexample to every proposed proof that uses
only conditional negative type, metric subadditivity, and the one endpoint
value.  The whole continuum of support constraints is essential.

## 6. Endpoint-mass and martingale transport stop gate

There is a second natural proposal: compare the continuous PNT measure

\[
 d\mu_0(u)=e^{u/2}{\bf1}_{(0,L)}(u)\,du
\tag{29}
\]

with the prime-power measure

\[
 \mu_p=\sum_{a_m<L}w_m\delta_{a_m},
\tag{30}
\]

and put the missing mass at or beyond the cutoff.  This is the
\(x^{-1/2}\)-weighted logarithmic version of the quantile constructions in
103.61--103.64, not a new transport mechanism.

Set

\[
 V_L=\mu_0((0,L))=2(e^{L/2}-1),
 \quad
 P_L=\int_0^Lu\,d\mu_0(u)
 =e^{L/2}(2L-4)+4,
\tag{31}
\]

and

\[
 S_L^-=\sum_{a_m<L}w_m,
 \qquad
 M_L^-=\sum_{a_m<L}w_ma_m.
\tag{32}
\]

If a nonnegative residual measure \(\eta\), supported in \([L,\infty)\),
is to match both total mass and first moment, then necessarily

\[
 r_L:=\eta([L,\infty))=V_L-S_L^-
\tag{33}
\]

and, when \(r_L>0\), its barycenter must be

\[
 b_L={P_L-M_L^-\over r_L}\ge L.
\tag{34}
\]

### Proposition 4 — Exterior barycenter failure before the first prime

For every \(0<L<\log2\), one has \(r_L=V_L>0\) and

\[
 \boxed{0<b_L={\int_0^Lu e^{u/2}\,du\over
                       \int_0^Le^{u/2}\,du}<L.}
\tag{35}
\]

Therefore no nonnegative residual measure supported at or beyond \(L\)
can match even the first two moments.  At the first atom, with the
right-continuous convention \(L=\log2\), the analogous one-atom formula
has positive residual mass but negative required barycenter.

#### Proof

Before \(\log2\), both sums in (32) vanish.  Formula (35) is the strict
weighted mean of points in the open interval \((0,L)\), so it lies strictly
inside that interval.  Any nonzero positive measure supported on
\([L,\infty)\) has barycenter at least \(L\), a contradiction.  The last
claim follows by direct substitution of the \(m=2\) weight in
(31)--(34). \(\square\)

This proposition only closes the exterior endpoint/martingale proposal.
It does not rule out a genuinely signed comparison retaining the Gamma
measure, and it does not replace the stronger sign obstructions already
proved in 103.64.

## 7. Verdict

The translation-metric coordinate is exact and gives a quantitative local
refinement of the earlier small-window positivity work: Theorem 3 proves
completed Weil positivity for an explicit short-support range.  It is not a
new mechanism, and it does not globalize through generic metric geometry.

The obstruction is now precise:

\[
 \text{CND + subadditivity + one endpoint}
 \quad\not\Longrightarrow\quad
 \text{prime--Gamma quadrature positivity}.
\tag{36}
\]

For an actual compactly supported translation orbit, the full plateau comes
together with positive definiteness of

\[
 H(u)=M-{1\over2}G(u)
\tag{37}
\]

and the fact that \(H\) is a compactly supported autocorrelation.  The inequality for all such
\(H\) is exactly positivity of the compressed completed Weil form.  Thus a
successful successor must exploit more than generic negative type: it must
use a specific collective property of the ordinary von Mangoldt atoms
inside the full compact autocorrelation cone.
