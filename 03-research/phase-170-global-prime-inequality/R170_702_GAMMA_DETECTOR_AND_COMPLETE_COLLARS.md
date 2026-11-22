# R170_702 — Incorporating the Gamma detector and full balance

Status: proved consequences of the Paper 46 and
R170_301/601 constructions; the arithmetic budget remains open.

## 1. Known detector and exact tail

For δ>0, `a_m=2m+1/2` and `b_m=√a_m exp(-a_m(T+δ))`, we define

\[
 (\mathcal R F)_m=b_m\int_{-T}^T e^{-a_mt}F(t)\,dt,\quad m\ge1.
\]

Paper 46 proves it is Hilbert–Schmidt and injective: with `x=e^{-2t}`,
the vanishing of the moments implies orthogonality to the monomials of
positive degree on a compact interval not containing zero. Its linear
span is dense. This property holds for every F, not only for primitive
or contact vectors.

The squared norm of row m is exactly

\[
 \tfrac12 e^{-2a_m\delta}(1-e^{-4a_mT}).
\]

Summing two geometric series, for the first L rows:

\[
 h_L:=\|\mathcal R-\mathcal R_L\|_{HS}^2
 =\frac12\left[
 \frac{e^{-(4L+5)\delta}}{1-e^{-4\delta}}
 -\frac{e^{-(4L+5)(\delta+2T)}}{1-e^{-4(\delta+2T)}}\right].
\]

Here the truncation is identified with an operator on ℓ² completed by
zeros. No finite truncation is injective on the whole infinite space.

## 2. Incorporation into the R170_601 storage

We use `R` for the path operator of 301, distinct from `𝓡`.
With `||R||≤r<1`, `Y=B^{-1/2}C^{1/2}` and
`K=Y*(I-R)^{-1}Y`, we take

\[
 S_\Gamma=\mathcal R^*\mathcal R,\qquad
 O_\Gamma=\sum_{j\ge0}Y^*R^j S_\Gamma R^jY.
\]

The series converges in norm. It is strictly positive on every nonzero
vector: its j=0 term equals `||𝓡Yx||²>0`, because Y and 𝓡 are
injective. This resolves the observation obligation that remained open
for the Möbius commutator of 601, with no RH hypothesis.

Moreover,

\[
 0\le O_\Gamma-O_{\Gamma,L},\qquad
 \|O_\Gamma-O_{\Gamma,L}\|
 \le\frac{\|Y\|^2}{1-r^2}h_L.
\]

But the budget `K+η OΓ≤I`, for η>0, does **not** follow from fidelity.
If `Kx=x`, evaluating it at x immediately contradicts it. Hence
requiring that budget already excludes the contact; we have not proved
that exclusion by building a detector. One must not confuse strict
pointwise positivity of the compact detector with a uniform coercive
bound.

## 3. Collar balance for the complete form

Write `J F(t)=F(-t)`, `c(t)=cosh(t/2)`, `s(t)=sinh(t/2)` and

\[
 P_{pol}=2|c\rangle\langle c|-2|s\rangle\langle s|,
 \qquad H^W=\mathcal M-U_N-U_N^*+P_{pol},
\]

where `𝓜` has the original archimedean form m, and
`U_N=P Σ_{2≤n≤N}Λ(n)n^{-1/2}V_log(n) P`, with `N≥e^{2T}`.
The operator U_N is the B_N of the paper's collar section, not the B of
301.

With `D_N=diag(Σ_{n≤N}Λ(n)n^{-a_m-1/2})` and the exterior collar `𝓔_N`
defined in the paper, substitution into the integral gives exactly

\[
 \mathcal R U_N=D_N\mathcal R-\mathcal E_N.
\]

Let F be an eigenvector of definite parity of H^W, with eigenvalue λ.
Then its weak archimedean-minus-primes equation is

\[
 \mathfrak a(F,G)=\langle\lambda F+r_W,G\rangle,
 \qquad r_W=-P_{pol}F.
\]

F is not required to be primitive. For
`G_L=𝓡_L*𝓡_L`, `S_L=G_L+JG_LJ`, we define

\[
 \begin{split}
 Q^W_{N,L}(F)={}&2\Re\langle\mathcal R_LF,\mathcal R_LU_N^*F\rangle
 -2\Re\langle\mathcal R_LF,\mathcal E_{N,L}F\rangle\\
 &-\Re\mathfrak m(F,S_LF)+\Re\langle r_W,S_LF\rangle.
 \end{split}
\]

**Identity.**

\[
 Q^W_{N,L}(F)=-2\sum_{m\le L}(d_{m,N}+\lambda)
                  |(\mathcal R_LF)_m|^2.
\]

**Proof.** Substitute `𝓔= D𝓡-𝓡U` into the first two sums.
Since `JUJ=U*` and F has definite parity, its off-diagonal terms
recombine into `Re⟨(U+U*)F,S_LF⟩`. We obtain
`Q=-2⟨𝓡_LF,D𝓡_LF⟩-Re a(F,S_LF)+Re⟨r_W,S_LF⟩`.
The weak equation and `⟨F,S_LF⟩=2||𝓡_LF||²` conclude the proof.
The range functions of S_L are finite sums of exponentials on the
interval and belong to the form domain; the test is admissible.

For N'≥N≥e^{2T}, it is still essential that
`𝓔_N'-𝓔_N=(D_N'-D_N)𝓡`: the exterior terms cancel, they are not
suppressed individually.

This is an extension of the **finite balance** to the complete form. It
does not automatically extend the renormalized histories nor the
meromorphic claims of the primitive argument. At λ=0 it again gives
`Q=-2c`; proving an opposite sign over the first contact remains the
pending arithmetic task. The identity does not use its minimality.
