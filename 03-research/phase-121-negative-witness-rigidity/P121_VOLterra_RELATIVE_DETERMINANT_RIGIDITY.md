# Phase 121 -- Volterra relative-determinant rigidity

## Status

This note constructs a literal causal determinant for the compact transform
of a hypothetical first-contact source. It also classifies completely the
zero-free case. Unlike an ordinary self-adjoint perturbation determinant,
the carrier has empty nonzero spectrum before perturbation, so no Euler
divisor is inserted as spectral input.

The classification has one exceptional family: constant step sources. A
single Tate moment excludes that family. Consequently a primitive source
whose rank-one Volterra perturbation remains quasinilpotent must vanish.

What is not proved here is that the first-contact equation makes that
perturbation quasinilpotent. The note identifies a nonlinear causal source
law which would close first contact; it does not infer the law from the Weil
sign.

## 1. A causal realization of the compact transform

Translate the physical window `(-T,T)` to `(0,L)`, where `L=2T`, and write
the translated source as `f`. On `H=L2(0,L)` let

\[
 (Vg)(x)=\int_0^x g(t)\,dt,\qquad u(x)=1,           \tag{1.1}
\]

and use the complex-linear functional

\[
 \ell_f(g)=\int_0^L f(x)g(x)\,dx.                  \tag{1.2}
\]

For `eta in C` put

\[
 A_{\eta,f}=V+\eta\,u\otimes\ell_f .              \tag{1.3}
\]

The Volterra operator is compact and quasinilpotent, and

\[
 (I-zV)^{-1}u=e^{zx}.                              \tag{1.4}
\]

Define the relative determinant

\[
 D_{\eta,f}(z)
 :=\det\!\left((I-zA_{\eta,f})(I-zV)^{-1}\right).
                                                               \tag{1.5}
\]

The operator inside the determinant differs from the identity by rank one,
so (1.5) is defined although `V` itself is only Hilbert--Schmidt.

### Proposition 1.1 -- exact determinant formula

If

\[
 K_f(z)=\int_0^L f(x)e^{zx}\,dx,                   \tag{1.6}
\]

then

\[
 \boxed{D_{\eta,f}(z)=1-\eta zK_f(z).}             \tag{1.7}
\]

Moreover

\[
 A_{\eta,f}\text{ is quasinilpotent}
 \quad\Longleftrightarrow\quad
 D_{\eta,f}\text{ is zero-free on }\mathbb C.     \tag{1.8}
\]

#### Proof

Factor

\[
 I-zA_{\eta,f}
 =(I-zV)\left[I-\eta z (I-zV)^{-1}u\otimes\ell_f\right].
\]

The rank-one determinant lemma and (1.4) give (1.7). Since `I-zV` is
invertible for every `z`, a zero of (1.7) is equivalent to noninvertibility
of `I-zA_(eta,f)`. The compact operator `A_(eta,f)` has no nonzero spectrum
exactly when this never occurs. QED.

## 2. Classification of the zero-free case

### Theorem 2.1 -- zero-free causal perturbations are interval steps

Let `0 != eta in C` and `f in L2(0,L)`. If `D_(eta,f)` is zero-free on
`C`, then there is an `a in [0,L]` such that, almost everywhere,

\[
 f(x)=-\eta^{-1}{\bf1}_{(0,a)}(x).                 \tag{2.1}
\]

Conversely every source (2.1) gives

\[
 D_{\eta,f}(z)=e^{az}                              \tag{2.2}
\]

and hence a quasinilpotent `A_(eta,f)`.

#### Proof

The function `D_(eta,f)` is entire of exponential type and has order at
most one. If it is zero-free, Hadamard factorization and `D_(eta,f)(0)=1`
give

\[
 D_{\eta,f}(z)=e^{az}                              \tag{2.3}
\]

for some `a in C`. Formula (1.7) yields

\[
 K_f(z)={1-e^{az}\over\eta z}.                    \tag{2.4}
\]

Because `f in L1(0,L)`, `K_f(iy)` is bounded and tends to zero as
`|y|->infinity`. If `Im(a) != 0`, the right side of (2.4) grows
exponentially in one imaginary direction, a contradiction. Hence `a` is
real.

For real `a`,

\[
 {1-e^{az}\over\eta z}
 =-\eta^{-1}\int_0^a e^{zx}\,dx                  \tag{2.5}
\]

with the oriented convention when `a<0`. Uniqueness of the Fourier
transform of compactly supported distributions shows first that the support
of the right side must lie in `[0,L]`; hence `a in [0,L]`. The same
uniqueness then gives (2.1). Substitution proves the converse. QED.

The exceptional steps are not a technical artifact: a rank-one feedback can
change the length of a Volterra interval while preserving empty nonzero
spectrum. Thus zero-free determinant rigidity without the Tate conditions
would be false.

## 3. Tate primitivity removes every exception

Return to the original coordinate `t=x-T`. The two Tate conditions are

\[
 \int_0^L e^{\pm(x-T)/2}f(x)\,dx=0.                \tag{3.1}
\]

### Corollary 3.1 -- primitive Volterra rigidity

Let `f` satisfy either one of the two conditions in (3.1). For one
`eta != 0`, suppose `A_(eta,f)` is quasinilpotent. Then `f=0`.

#### Proof

By Proposition 1.1 and Theorem 2.1, `f` has the form (2.1). If `a>0`,
then

\[
 \int_0^L e^{\pm(x-T)/2}f(x)\,dx
 =-\eta^{-1}\int_0^a e^{\pm(x-T)/2}\,dx\ne0.      \tag{3.2}
\]

Thus `a=0`, and (2.1) gives `f=0`. QED.

### Corollary 3.2 -- exact nonlinear causal closure target

Let `F` be a primitive first-contact source and let `f(x)=F(x-T)`. If the
uncompressed equality-state law implies, for one fixed `eta != 0`,

\[
 \sigma(A_{\eta,f})=\{0\},                         \tag{3.3}
\]

then `F=0`. Therefore (3.3), derived independently of primitive
positivity, excludes first contact and closes the global square by the
already proved nesting argument.

This target is nonlinear in the source: equivalently, all nonzero roots of
`1-eta zK_f(z)` are forbidden. It is not a Hilbert square, a Douglas
contraction, or a self-adjoint realization of the Euler divisor.

### Proposition 3.3 -- moment form of the causal law

Put

\[
 m_k(f)=\int_0^L x^k f(x)\,dx.                    \tag{3.4}
\]

For `eta != 0`, the following are equivalent:

1. `A_(eta,f)` is quasinilpotent;
2. `D_(eta,f)(z)=exp(-eta m_0 z)`;
3. for every `k>=0`,

\[
 \boxed{
 m_k={(-1)^{k+2}\over k+1}\eta^k m_0^{k+1}.}      \tag{3.5}
\]

In particular the first nonlinear trace obstruction is

\[
                         2m_1+\eta m_0^2=0.        \tag{3.6}
\]

#### Proof

Theorem 2.1 gives `f=-eta^(-1)1_(0,a)` and comparison of the coefficient of
`z` in (1.7) and (2.2) gives `a=-eta m_0`. Direct integration then gives

\[
 m_k=-\eta^{-1}{a^{k+1}\over k+1}
 ={(-1)^{k+2}\over k+1}\eta^k m_0^{k+1},
\]

proving `1 => 2 => 3`. Conversely (3.5) reconstructs

\[
 K_f(z)=\sum_{k\ge0}{m_kz^k\over k!}
 ={1-e^{-\eta m_0z}\over\eta z},
\]

so (1.7) is `exp(-eta m_0 z)`, proving `3 => 2 => 1`. QED.

Thus the equality-state attack can be made coefficientwise without any
spectral terminology. It must derive (3.6) and its higher analogues from the
uncompressed Euler--Gamma equation. The Tate conditions then force the
classified moment sequence to be zero. Merely defining these identities as
relative trace cancellations would, of course, assume the desired causal
law.

### Corollary 3.4 -- two-scale rigidity on the radical line

Let `c in C` with `c != 0,1`. If, for the same `eta != 0`, both

\[
 A_{\eta,f}\quad\hbox{and}\quad A_{\eta,cf}        \tag{3.7}
\]

are quasinilpotent, then `f=0`.

#### Proof

If `f != 0`, Theorem 2.1 says

\[
 f=-\eta^{-1}{\bf1}_{(0,a)},\qquad
 cf=-\eta^{-1}{\bf1}_{(0,b)}                       \tag{3.8}
\]

for positive `a,b`. Equality of the two functions forces their supports to
coincide and then forces `c=1`, a contradiction. QED.

A first-contact radical is a complex line. Therefore any sourced
quasinilpotence law which is functorial on that line and uses a fixed
normalization `eta` annihilates it already by applying the law to `F` and
`iF`; the Tate moments are then not needed. This is stronger than scalar
zero-free rigidity, but functorial quasinilpotence still has to come from
the uncompressed source equation rather than from the determinant formula.

### Proposition 3.5 -- homogeneity audit

There is no nontrivial implication from the homogeneous first-contact line
alone to fixed-`eta` quasinilpotence of `A_(eta,f)`.

More precisely, suppose a rule depending only on membership in a complex
linear subspace `N` asserts

\[
 f\in N\quad\Longrightarrow\quad
 A_{\eta,f}\text{ is quasinilpotent}               \tag{3.9}
\]

for one fixed `eta != 0`. Then `N={0}`.

#### Proof

For every `f in N`, complex linearity also puts `if in N`. Applying (3.9)
to both vectors and using Corollary 3.4 with `c=i` gives `f=0`. QED.

The first-contact equation and all of its ordinary polarizations specify
exactly such a complex linear radical. Consequently (3.9) cannot be
obtained merely by retesting, differentiating or changing coordinates in
that equation: as a line-functorial assertion it already is first-contact
exclusion. A viable use of Theorem 2.1 would require an additional
nonhomogeneous source normalization constructed before the Weil comparison.
Rows (a)--(c), as presently proved, supply the scalar nuclear character but
no such normalization on an individual radical line.

## 4. Noncircularity audit

The determinant construction itself does not prove (3.3). In particular:

* defining invertibility of `I-zA_(eta,f)` by the nonvanishing of (1.7) is
  only Proposition 1.1, not an equality-state law;
* triangularity of `A_(eta,f)` would imply (3.3), but a general rank-one
  feedback `u tensor ell_f` is not triangular;
* forcing that feedback to be triangular is already a support statement on
  `f`, closely related to the boundary-germ target;
* ordinary self-adjoint determinant theory is irrelevant here: `V` is a
  causal, nonnormal, quasinilpotent carrier.

The gain over the affine unit `1+epsilon K_F` is exact classification rather
than another zero-free assertion: the extra factor `z` permits nontrivial
zero-free deformations, and Theorem 2.1 identifies all of them. Tate
primitivity then removes them without using row (d).

## 5. Corpus audit and verdict

Phases 64, 80, 81, 101 and 106 contain self-adjoint relative determinants,
bordered secular determinants and cofactor encodings. Phase 121 contains a
Tate--Volterra invariance audit. A semantic search through phases 1--120
found no rank-one Volterra relative determinant (1.5), no classification
(2.1), and no use of a Tate moment to remove the interval-step exceptions.

```text
causal relative determinant (1.7)                 PROVED
zero-free/quasinilpotent equivalence               PROVED
complete zero-free source classification          PROVED
Tate exclusion of every nonzero exception         PROVED
fixed-eta law on the radical line                  TERMINAL EQUIVALENT
independent nonhomogeneous source normalization    NOT CONSTRUCTED
global square                                      OPEN
```

No modification of paper 42 follows until the last implication is derived.
