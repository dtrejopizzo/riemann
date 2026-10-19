# R183.013 — The semilocal Weil form is a trace anomaly

> **Second audit R183.014:** the cancellation theorem only excludes
> separating the two original energies as finite traces. It does not exclude
> other sums of squares nor force the use of determinants. The general
> exclusion statements in §§3 and 6 are withdrawn. Trace class of the
> sandwich is a hypothesis to be verified in the concrete semilocal sector.

## 1. Cancellation theorem for every ordinary factorization

Let `\mathcal H=L^2(\widehat{C_{\mathbb Q,S}})`. Let `P` be an orthogonal
projection, `u=M_u` multiplication by a unimodular function, and
`M=M_\varphi` another multiplier. Then `uM=Mu`.

### Theorem 1. `PROVED`

If the two positive operators

\[
T_1=M^*u^*PuM,\qquad T_0=M^*PM                         \tag{1.1}
\]

are trace class, then

\[
\operatorname{Tr}(T_1-T_0)=0.                         \tag{1.2}
\]

**Proof.** By cyclicity of the trace and `uMM^*u^*=MM^*`,

\[
\begin{aligned}
\operatorname{Tr}(M^*u^*PuM)
 &=\operatorname{Tr}(P\,uMM^*u^*)\\
 &=\operatorname{Tr}(P\,MM^*)
  =\operatorname{Tr}(M^*PM).
\end{aligned}
\]

This proves (1.2). \(\square\)

### Consequence

The nonzero quantity

\[
\mathcal W_S(h)=
\operatorname{Tr}_{\rm loc}
\bigl(M^*(u^*Pu-P)M\bigr)                             \tag{1.3}
\]

is not the difference of two trace-class energies. It is a relative
trace: the separated summands diverge and the arithmetic lies in their
finite term. Every `RET` that writes (1.3) as
`\|PM\|_{HS}^2-\|PuM\|_{HS}^2` without fixing and transporting the same
counterterm is invalid. This is the defect of R183.002 and R183.003.

## 2. Localizing the anomaly on the diagonal

In the one-dimensional Hardy model, `P`'s distributional kernel has the
form

\[
P(s,t)=\tfrac12\delta(s-t)+c_P\,\operatorname{pv}{1\over s-t}, \tag{2.1}
\]

with a purely imaginary constant determined by the Fourier convention.
Hence

\[
(u^*Pu-P)(s,t)
=P(s,t)\bigl(\overline{u(s)}u(t)-1\bigr).             \tag{2.2}
\]

If `u=e^{i\vartheta}` is locally smooth,

\[
\overline{u(s)}u(t)-1
=i\vartheta'(s)(t-s)+O((t-s)^2).                      \tag{2.3}
\]

The zero of (2.3) cancels the singularity of (2.1), leaving on the
diagonal a real multiple of `\vartheta'(s)`. After localizing with
`M_\varphi`, (1.3) takes the form

\[
\mathcal W_S(h)
=c\int_{\widehat C}|\varphi(s)|^2\,d\vartheta_S(s),  \tag{2.4}
\]

in the distributional sense. This is precisely the sum of the phase
derivatives of Tate's local factors, i.e. the semilocal formula.
The constant and the orientation are fixed by
`\frac12u^{-1}[2P-1,u]=u^*Pu-P`; they need not be chosen for the
cancellation theorem.

## 3. What object can carry the sign

The sought object must jointly keep the pair

\[
(T_1,T_0)=(M^*u^*PuM,M^*PM)                           \tag{3.1}
\]

and its semilocal normalization. There are three operator possibilities
compatible with Theorem 1:

1. a relative determinant of the compressions of `P` and `u^*Pu`;
2. an index of a pair of projections localized by the Poisson–Tate
   ideal;
3. a closed quadratic form with a common counterterm, whose finite part
   is (1.3).

A representation via a different column is not excluded. The theorem
only treats the two original energies when they are trace class.

## 4. Well-defined relative object

Set

\[
B_1=M^*u^*PuM,\qquad B_0=M^*PM,
\qquad D=B_1-B_0.                                    \tag{4.1}
\]

For the Schwartz localizers of the semilocal formula, `D` is trace
class even though `B_0` and `B_1` are not. For `z\ge0` the operators
`I+zB_j` are invertible. Moreover

\[
(I+zB_1)(I+zB_0)^{-1}-I
=zD(I+zB_0)^{-1}                                    \tag{4.2}
\]

is trace class. Hence the following relative Fredholm determinant is
well defined without separating the two divergent energies:

\[
\Delta_{S,h}(z)
=\det\!\left[
 (I+zB_1)(I+zB_0)^{-1}\right].                       \tag{4.3}
\]

Its derivative at zero is

\[
{d\over dz}\log\Delta_{S,h}(0)
=\operatorname{Tr}(B_1-B_0)=\mathcal W_S(h).         \tag{4.4}
\]

Hence, a sufficient prespectral inequality is

\[
\boxed{
{d\over dz}\log\Delta_{S,h}(0)\le0}
\quad
(h\text{ with short support and the two Tate moments}).       \tag{4.5}
\]

(4.5) is not proved. Its logical advantage is that it no longer destroys
the anomaly via cyclicity and specifies what Poisson must produce: a
comparison of the **full relative pair**, not a comparison of separate
norms.

## 5. Mandatory tests for the next round

The next round must prove or refute:

* that Poisson induces an order, majorization, or spectral-flow
  comparison between `B_1` and `B_0` on the Tate cone;
* that such a comparison fails without the exact comb of `\mathbb Z`;
* that the invoked monotonicity is not simply a restatement of (4.5).

## 6. Status

* Cancellation under trace-class separability: **PROVED**.
* Relative/anomalous nature of the semilocal term: **PROVED** from the
  theorem and the cited trace formula.
* Diagonal kernel/phase derivative: **PROVED** on the smooth core;
  distributional extension: **CITED** via the semilocal formula.
* Relative determinant (4.3): **PROVED** whenever localization
  `D` is trace class, as in the semilocal formula.
* Identification of its derivative (4.4): **PROVED**.
* Sign (4.5): **OPEN**.
* Row D: **OPEN**.

The two original energies cannot be separated as finite traces to
obtain a nonzero value. This does not classify the possible positive
proofs nor prove that a determinant is necessary. The sign remains pending.

## 7. Determinant curvature test — PROVED, abstract scope

Suppose B_0,B_1 are positive bounded and D=B_1-B_0 is trace class. For
L(z)=log det((I+zB_1)(I+zB_0)^(-1)), real near z=0, one has

    L'(0)=Tr D,
    L''(0)=-Tr(B_1²-B_0²)=-Tr((B_1+B_0)D).

Proof: for |z|max(||B_0||,||B_1||)<1, the differences of the logarithm
series converge in trace norm. Indeed,
||B_1^n-B_0^n||_1 ≤ n max(||B_0||,||B_1||)^(n-1)||D||_1,
via telescopic expansion. Differentiating term by term gives the
formulas. For the second equality use B_1=B_0+D and cyclicity with the
trace-class factor D. No separate traces of B_j nor B_j² are taken.

Positivity of B_j does not fix the sign of the second derivative: in
R183.014's bilateral shift example, L(z)=log(1+z) for one orientation
and L(z)=-log(1+z) for the other. Their curvatures at zero are -1 and +1.
Both examples satisfy unitary equivalence and a rank-one difference.

Hence concavity of log det for individual positive matrices does not
automatically transport to the relative quotient. A curvature proof
needs an additional arithmetic inequality for the weighted trace
Tr((B_1+B_0)D). This proof does not show that inequality fails for the
real semilocal product: it only rules out deducing it from positivity,
unitary equivalence, and trace class. The semilocal sign remains OPEN.

## 8. Exact semilocal curvature — PROVED on R183.015's core

In the modulus sector, write u=e^{iθ}, φ=Fourier(h), w=|φ|²,
B_0=M_φ* P M_φ, B_1=M_φ* u* P u M_φ, D=B_1-B_0. Then

    L''(0) = (1/(2π)) ∫ θ'(s)|φ(s)|⁴ ds.

Proof. By §7 it suffices to compute Tr(D(B_1+B_0)). D's kernel is Schwartz
(R183.015), so it can be paired with the distributional kernel of the
bounded operator B_1+B_0 to obtain the trace. This is justified, for
example, by expanding the Schwartz kernel in the Hermite basis: the
series converges in the Schwartz space and the traces converge in trace
norm when composed with B_1+B_0.

The delta part of B_1+B_0 is w(s)δ(s-t), and contributes

    ∫ w(s)K_D(s,s)ds = -(1/(2π))∫w(s)²θ'(s)ds.

For the principal-value part, set r=conjugate(u(s))u(t).
Off the diagonal, the pairing's integrand is

    w(s)w(t)(r-r^(-1))/(4π²(s-t)²).

It is antisymmetric under exchanging s,t. For each ε>0, its integral over
|s-t|>ε is zero; the Schwartz decay makes the region away from the
diagonal integrable. Its principal value is zero. Hence the delta part is
the whole trace. Changing the sign, as §7 requires, proves the formula.

### Arithmetic interpretation and change of support

Let g=h*h, additive convolution. Its Fourier transform is φ², so the
above formula is exactly the primitive semilocal energy of g, with the
same set S of places. g's exponential moments are the squares of h's;
hence primitivity is preserved. But if h is supported on (-T,T), only g
supported on (-2T,2T) is guaranteed.

To identify this curvature with the GLOBAL energy of g, the support
argument requires including primes p<exp(4T). An S chosen only with
p<exp(2T) for the original test does not in general satisfy that
requirement. The exact global-minus-semilocal difference is

    -2 Σ_{p outside S} Σ_{k≥1} (log p)p^(-k/2) Re c_g(k log p),

a finite sum in this support. Its sign is not known from the support alone.

This computation proves neither convexity nor concavity. It makes
precise that the first attempt to control the slope via curvature again
requires a Weil energy over a convolution and, for the global
identification, a larger support. It provides neither an induction towards
smaller supports nor an independent inequality to close D.
