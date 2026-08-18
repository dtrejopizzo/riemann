# 106.144 — Full-chord fiber rigidity and the Möbius-incidence gate

## 1. Purpose and result

Document 106.143 leaves open only a source-specific multiplier constructed
after the complete radical anti-short.  The first candidate is to combine
three exact ordinary-integer operations before taking a norm:

1. the finite residue Fourier--Poisson transform of 106.107--106.108;
2. the divisor-current/cross-divisor decomposition of 106.104;
3. the same-side and central-crossing parts of every theta chord.

This note proves that their complete combination is still rigid.  The
same-side and central pieces are the two halves of one symmetric chord.
Residue Fourier transformation and divisor ANOVA are orthogonal changes of
coordinates on that chord source.  Their direct sum therefore has the form

\[
 \mathcal G'=W\mathcal G,
 \qquad W^*W=I,
 \tag{1}
\]

and the complete radical anti-short intertwines with (W).  Hence this
ordinary-integer compression leaves the post-short transfer gain exactly
unchanged.

There is a stronger fiber theorem.  Every decomposable contraction which
preserves equality on one nonconstant exact radical is forced to be
isometric on the entire one-dimensional physical chord fiber almost
everywhere.  Thus no multiplier acting separately on residue, divisor, or
chord fibers can create the missing surplus.

The first genuinely cross-chord arithmetic map is Möbius incidence.  Its
raw critical-line multiplier has diverging mean-square norm.  It cannot be
used as a Hilbert contraction before Gamma, the pole, and the complete
theta metric are assembled.  The surviving class is consequently a
nondecomposable signed operator mixing distinct chords globally, with all
three completed sources retained before its norm is estimated.

No zero-location statement is used below.

## 2. Same-side and central crossing are one chord

For (a,c\geq0), define

\[
 \mathcal F_q(c,a)
 =K(c+a)K(c-a)
  |q(c+a)-q(c-a)|^2,
 \tag{2}
\]

where (K) and (q) are even.  Evenness gives the two symmetries

\[
 \boxed{\mathcal F_q(-c,a)=\mathcal F_q(c,a),
 \qquad \mathcal F_q(c,a)=\mathcal F_q(a,c).}
 \tag{3}
\]

### Theorem 1 — Exact full-chord formula

For every (a>0),

\[
 \boxed{
 J_{2a}(q)=2\int_0^\infty \mathcal F_q(c,a)\,dc.}
 \tag{4}
\]

Under the fold used in 106.38, the same-side channel is the part

\[
 2\int_a^\infty\mathcal F_q(c,a)\,dc,
 \tag{5}
\]

and the central-crossing channel is

\[
 2\int_0^a\mathcal F_q(c,a)\,dc.
 \tag{6}
\]

#### Proof

In the definition of (J_{2a}), put (x=c+a).  Its two endpoints become
(c+a) and (c-a), and (dx=dc).  The resulting integrand is (2).
The first identity in (3) makes the integral over the full real (c)-axis
twice its positive half, proving (4).  The endpoint pair lies on one side
of the origin precisely when (c\geq a); it crosses the origin precisely
when (0\leq c\leq a).  This proves (5)--(6).  The second identity in (3)
is immediate after interchanging (a) and (c) and using evenness at the
second endpoint. \(\square\)

Thus the central channel is not an independent reserve which can be spent
after the tail has been estimated.  It is the missing interval of the same
physical chord.

## 3. The two exact orthogonal changes of coordinates

Retain

\[
 \phi(t)=\pi t^2(2\pi t^2-3)e^{-\pi t^2}.
 \tag{7}
\]

With the Fourier convention

\[
 \widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt,
\]

Gaussian differentiation gives

\[
 \boxed{\widehat\phi=\phi.}
 \tag{8}
\]

Indeed,

\[
 \mathcal F(t^2e^{-\pi t^2})
 =\left({1\over2\pi}-\xi^2\right)e^{-\pi\xi^2},
\]

and

\[
 \mathcal F(t^4e^{-\pi t^2})
 =\left(\xi^4-{3\over\pi}\xi^2
              +{3\over4\pi^2}\right)e^{-\pi\xi^2};
\]

substitution in (7) gives (8).

Consequently the exact residue identity of 106.107 is

\[
 \sum_{j\in\mathbb Z}k_{|j|/n}(x)e^{2\pi iaj/n}
 =n\!\sum_{\ell\equiv-a\ ({\rm mod}\ n)}k_{|\ell|}(-x).
 \tag{9}
\]

For (x\geq\log n), the bilateral residue masses

\[
 M_{n,r}(x)=
 \sum_{j\equiv r\ ({\rm mod}\ n)}k_{|j|/n}(x)
 \tag{10}
\]

are nonnegative.  If (U_n) denotes the unitary finite Fourier matrix,
then

\[
 C_n(x)=U_n\mathrm{diag}(M_{n,r}(x))U_n^*\succeq0
 \tag{11}
\]

and its entries are the signed reflected congruence sums in (9).  Its
grouped square root is merely the unitary image of the positive residue
amplitude.  It preserves the physical norm exactly.

At a farther theta endpoint (b), let

\[
 e_d={\sqrt{\Lambda(d)}\over\sqrt{\log b}},
 \qquad
 v_d=\sqrt{\Lambda(d)}\,Delta_dq,
 \qquad d\mid b,
 \tag{12}
\]

where entries with \(\Lambda(d)=0\) are omitted.  The ordinary-integer
identity

\[
 \sum_{d\mid b}\Lambda(d)=\log b
 \tag{13}
\]

makes (e) a unit vector and gives

\[
 \boxed{
 \|v\|^2=|\langle e,v\rangle|^2
          +\|(I-ee^*)v\|^2.}
 \tag{14}
\]

The first term in (14) is the divisor current and the second is exactly the
cross-divisor dispersion of 106.104.  Retaining both is another orthogonal
change of coordinates, not a lower estimate.

## 4. Intertwining with the complete anti-short

Let \(\mathcal G\) be the direct sum of the literal ordinary-prime, Gamma,
fractional, and complete chord amplitudes.  Apply the residue rotation
(11), the ANOVA rotation (14), and the identity on Gamma.  By Theorem 1 no
central interval is omitted.  Their direct sum is an isometry (W), and

\[
 \mathcal G'=W\mathcal G,
 \qquad
 (\mathcal G')^*\mathcal G'=\mathcal G^*\mathcal G.
 \tag{15}
\]

Let \(\mathcal R\) be the complete radical and
\(\mathscr M=\overline{\mathcal G\mathcal R}\).  Then

\[
 \mathscr M'=\overline{\mathcal G'\mathcal R}=W\mathscr M.
 \tag{16}
\]

### Theorem 2 — Arithmetic fiber rotations do not change the shorted gain

One has

\[
 \boxed{
 P_{(\mathscr M')^\perp}\mathcal G'
 =W P_{\mathscr M^\perp}\mathcal G.}
 \tag{17}
\]

In particular the two shorted generators and every source-to-polar
singular value coincide.

#### Proof

An isometry maps \(\mathscr M\) unitarily onto \(W\mathscr M\) inside its
range, so

\[
 P_{(W\mathscr M)^\perp}W=WP_{\mathscr M^\perp}.
\]

Apply this identity to \(\mathcal G\) and use (15)--(16). \(\square\)

This proves the exact post-short rigidity, not merely source-level norm
preservation.

## 5. Fiberwise non-isometry is also impossible

The previous theorem concerns the canonical DFT and ANOVA rotations.  The
same obstruction holds for every decomposable contraction which is sharp
on the radical.

On each marked chord fiber (e), every physical source vector has the
form

\[
 a(e)\,\Delta_eq,
 \tag{18}
\]

where (a(e)) is the fixed theta/arithmetic amplitude vector.  Let
(T=\int^\oplus T_e\) be a measurable decomposable contraction on these
fibers.

### Theorem 3 — One nonconstant radical forces fiberwise isometry

Let (r_1=K''/K).  If

\[
 \|T\mathcal G r_1\|=\|\mathcal G r_1\|,
 \tag{19}
\]

then

\[
 \boxed{\|T_ea(e)\|=\|a(e)\|}
 \tag{20}
\]

for almost every physical chord fiber.  Consequently

\[
 \|T\mathcal Gq\|=\|\mathcal Gq\|
 \tag{21}
\]

for every physical (q) in the form domain.

#### Proof

Contractivity and (18) give the nonnegative identity

\[
\begin{aligned}
 0={}&\|\mathcal Gr_1\|^2-\|T\mathcal Gr_1\|^2\\
 ={}&\int |\Delta_er_1|^2
 \{\|a(e)\|^2-\|T_ea(e)\|^2\}\,d\eta(e).
\end{aligned}
 \tag{22}
\]

For every nonzero chord, analyticity makes \(\Delta_er_1\) either
identically zero or zero only on a discrete set.  The first alternative
would make (r_1) periodic.  The theta asymptotics make the nonconstant
(r_1) unbounded at the positive end, so it is not periodic.  Hence the
first factor in (22) is positive almost everywhere on each nonzero chord.
The second factor is nonnegative by contractivity; it must vanish almost
everywhere.  This proves (20).  Formula (18) then proves (21). \(\square\)

Therefore a useful non-isometric multiplier cannot be decomposable over
the marked chord variables.  It must mix distinct chord lengths and
centers after the global short.

## 6. The raw Möbius incidence is not a bounded successor

The canonical cross-endpoint operation generated by (13) is Möbius
incidence.  At a finite cutoff its critical-line translation multiplier is

\[
 M_N(t)=\sum_{d\leq N}{\mu(d)\over\sqrt d}
 e^{it\log d}.
 \tag{23}
\]

### Theorem 4 — Mean-square divergence of raw Möbius incidence

For every finite (N),

\[
 \boxed{
 \lim_{T\to\infty}{1\over2T}
 \int_{-T}^T|M_N(t)|^2\,dt
 =\sum_{d\leq N}{\mu(d)^2\over d}.}
 \tag{24}
\]

The right side diverges as (N\to\infty).

#### Proof

Expanding the square in (23), every off-diagonal average contains

\[
 {1\over2T}\int_{-T}^T
 e^{it\log(d/e)}\,dt\longrightarrow0
 \qquad(d\ne e),
\]

while the diagonal terms remain.  This proves (24).  The diagonal sum is
at least \(\sum_{p\leq N}p^{-1}\), which diverges. \(\square\)

Thus (Z^{-1}\delta Z=\Lambda) cannot be split into a bounded Möbius
inverse and a positive divisor derivative at the critical metric.  Its
cancellation is bounded only when the product is retained jointly, which
returns the literal prime source.

## 7. Surviving construction class

The following operations are now excluded as sources of new gain:

* finite residue Fourier/Poisson changes of basis;
* divisor current plus its complete dispersion;
* separate treatment of the central chord;
* every fiberwise source-dependent contraction sharp on the radical;
* the raw cofinal Möbius-incidence inverse.

The next admissible object must be a globally nondecomposable signed
operator which mixes distinct chord centers and lengths, is defined only
after the complete radical anti-short, and combines ordinary
\(\Lambda(n)\), Gamma, and the pole before any Hilbert norm is taken.  Its
compressed remainder must be a genuine source-specific null IQC of the
kind isolated in 106.143.  Constructing such an operator and proving its
two compressed signs remains the active arithmetic task.

