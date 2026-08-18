# 106.94 — Mean-periodic bordered-minor exactness gate

## Purpose and conclusion

Documents 106.89--106.92 leave the radical-conditioned adaptive row at

\[
 G_J>\delta_J.
\]

The only structural datum not used by the abstract rational falsifier of
106.92 is the Riemann mean-periodic equation

\[
 (hq)*K=0,
 \qquad h(x)=\cosh(x/2),
\]

together with the literal displacement maps at the ordinary prime-power
lengths. This note checks whether that equation supplies an independent
sign for the bordered Christoffel minor.

It does not. There are two exact reasons.

1. The mean-periodic equation applies to the zero-mode residual
   \(q_J^*+d\). The finite radical correction used by the maximal
   anti-short leaves the mean-periodic space unless that correction is
   zero. Thus it is invalid to impose the convolution equation on the
   joint saddle residual \(\widetilde q_J^*\) without first proving that
   its radical coefficient vanishes.
2. Even with no nuisance mode and no radical correction, the sharp
   bordered-minor surplus is identically the completed shifted Weil form.
   If \(q\) is mean-periodic and \(\mathcal A_\infty(q,q)<0\), then every
   finite bordered minor misses the threshold. If an off-line zero orbit
   exists, 106.64 supplies exactly such a mean-periodic \(q\), with all
   literal ordinary-prime and Gamma channels unchanged.

Consequently mean periodicity and literal theta translations yield strict
detection, but not the comparison with \(\delta_J\). Any theorem deriving
that comparison for every physical row excludes the off-line channel and
has the force of the remaining RH sign theorem.

## 1. Which residual is mean-periodic

Let

\[
 \mathcal Q=(\mathbf 1\oplus\mathcal R)^\perp
\]

in the \(L^2(\mu_K)\) coordinate. By 106.43,

\[
 q\in\mathcal Q
 \quad\Longleftrightarrow\quad
 (hq)*K=0.                                           \tag{1}
\]

The finite elementary zero-mode space \(V_M\) lies in \(\mathcal Q\).
Hence the adaptive mode residual of 106.89 satisfies

\[
 q_J^*+d\in\mathcal Q
 \qquad(d\in V_{M-1}).                              \tag{2}
\]

The joint saddle residual, however, is

\[
 \widetilde q_J^*=q_J^*+r_J^*,
 \qquad r_J^*\in\mathcal R_J.                      \tag{3}
\]

### Lemma 1 — A nonzero radical correction destroys mean periodicity

For \(q\in\mathcal Q\) and \(r\in\mathcal R_J\),

\[
 \boxed{
 (h(q+r))*K=0
 \quad\Longleftrightarrow\quad r=0.}               \tag{4}
\]

#### Proof

By (1), the left side says that \(q+r\in\mathcal Q\). Since already
\(q\in\mathcal Q\), this implies \(r\in\mathcal Q\). But
\(r\in\mathcal R_J\subset\mathcal R\), and

\[
 \mathcal Q\cap\mathcal R=\{0\}.
\]

Thus \(r=0\). The converse follows from (1). \(\square\)

Therefore the affine vector in the augmented determinant splits as

\[
 q_J^*+d+r
 =\underbrace{(q_J^*+d)}_{\text{mean-periodic}}
 +\underbrace{r}_{\text{radical correction}},      \tag{5}
\]

and the total vector in (5) is mean-periodic only at \(r=0\). The common
radical correction in 106.91--106.92 must remain coupled to the literal
translations, but it cannot simultaneously be treated as another
mean-periodic vector.

This is not a technical distinction. The physical source identity for
\(\delta_J\) is evaluated on \(\widetilde q_J^*\), whereas the convolution
equation is satisfied by the zero-mode component \(q_J^*\). Passing the
equation from the latter to the former silently deletes the anti-short.

## 2. Exact one-row bordered-minor identity

The obstruction is already complete when there is no old nuisance mode
and no finite radical coordinate. Let \(0\ne q\in\mathcal Q\) belong to
the common form domain. Write

\[
 \mathcal T_X(q,q)
 =\sum_{p^k>X}\frac{\log p}{p^{k/2}}
   \mathcal J_{k\log p}(q,q)                     \tag{6}
\]

for the complete omitted ordinary-prime tail and

\[
 \mathcal A_X=\mathcal A_\infty-\mathcal T_X.     \tag{7}
\]

Assume the finite-head row is negative and put

\[
 \delta_X=-\mathcal A_X(q,q)>0.                   \tag{8}
\]

There is no adaptation loss in one dimension, so restoring the complete
tail gives

\[
 G_X=\mathcal T_X(q,q).                            \tag{9}
\]

### Theorem 2 — Mean-periodic exactness of the sharp surplus

For every such row,

\[
 \boxed{G_X-\delta_X=\mathcal A_\infty(q,q).}      \tag{10}
\]

For a finite captured block \(X<p^k\le Y\), put

\[
 \mathfrak C_{X,Y}(q)
 =\sum_{X<p^k\le Y}\frac{\log p}{p^{k/2}}
   \mathcal J_{k\log p}(q,q),                    \tag{11}
\]

and denote the uncaptured tail by \(\mathcal T_Y(q,q)\). Then

\[
 \boxed{
 \mathfrak C_{X,Y}(q)-\delta_X
 =\mathcal A_\infty(q,q)-\mathcal T_Y(q,q).}      \tag{12}
\]

#### Proof

Equations (7)--(9) give

\[
 G_X-\delta_X
 =\mathcal T_X(q,q)+\mathcal A_X(q,q)
 =\mathcal A_\infty(q,q),
\]

which is (10). Also

\[
 \mathcal T_X(q,q)
 =\mathfrak C_{X,Y}(q)+\mathcal T_Y(q,q).
\]

Substitute this identity into (10) to obtain (12). \(\square\)

In bordered-minor notation the nuisance dimension is zero, so

\[
 \tau_0(Y)=1,
 \qquad
 \tau_1(Y)=\mathfrak C_{X,Y}(q).
\]

Thus (12) is exactly

\[
 \boxed{
 \tau_1(Y)-\delta_X\tau_0(Y)
 =\mathcal A_\infty(q,q)-\mathcal T_Y(q,q).}      \tag{13}
\]

The literal theta envelope makes \(\mathcal T_Y(q,q)\downarrow0\). It
therefore selects a finite witness after a positive completed margin is
known, but it cannot change the sign of that margin.

## 3. Conditional physical falsifier from an off-line orbit

The preceding identity gives a falsifier inside the actual Riemann
mean-periodic and literal-translation system, conditional only on the
existence of the object that the desired theorem is meant to exclude.

### Theorem 3 — An off-line orbit defeats every one-row crossing

If \(\Xi\) has an off-line zero orbit, then there is a nonzero
\(q\in\mathcal Q\) in the common form domain such that, for every finite
head \(X\),

\[
 \mathcal A_X(q,q)<0,
 \qquad
 G_X<\delta_X,                                     \tag{14}
\]

and, for every finite \(Y>X\),

\[
 \boxed{
 \tau_1(Y)-\delta_X\tau_0(Y)<0.}                  \tag{15}
\]

#### Proof

By 106.64, Theorem 3, an off-line orbit supplies

\[
 F\in\mathcal N_K,
 \qquad
 \langle F,T_FF\rangle_{\omega_K}<0.
\]

Put \(q=F/h\). Then \(q\in\mathcal Q\), so \((hq)*K=0\), and

\[
 \mathcal A_\infty(q,q)<0.                        \tag{16}
\]

The tail is strictly positive. Indeed, if
\(\mathcal T_X(q,q)=0\), positivity of every ordinary-prime weight makes
\(q\) invariant almost everywhere under every displacement
\(\log p^k>X\). Choose two primes whose logarithms have irrational ratio.
The generated translation subgroup is dense, so strong continuity of
translations in the local \(L^2\) topology makes \(q\) translation
invariant, hence constant almost everywhere. Centering would then give
\(q=0\), a contradiction. Therefore \(\mathcal T_X(q,q)>0\), and (7)
gives

\[
 \mathcal A_X(q,q)
 =\mathcal A_\infty(q,q)-\mathcal T_X(q,q)<0.
\]

Equation (10) and (16) give \(G_X-\delta_X<0\), proving (14). Finally,
(13), (16), and \(\mathcal T_Y(q,q)\ge0\) give (15). \(\square\)

Every object in this theorem is physical: \(K\) is Riemann's theta
kernel, the displacement lengths are \(k\log p\), the weights are
\(\log p/p^{k/2}\), and the Gamma and polar terms remain inside
\(\mathcal A_\infty\). The theorem is not a counterexample to RH. It
proves that mean periodicity and literal theta translations are compatible
with failure of the bordered-minor inequality precisely in the hypothetical
off-line world.

## 4. What mean periodicity does prove

For a fixed finite elementary zero-mode space and a fixed finite radical
space, literal theta translations give strict observability. Equivalently,
each nonempty finite augmented Gram is positive definite and its
Christoffel ratio is positive. In the present notation this yields

\[
 G_J>0.                                             \tag{17}
\]

This is the injectivity theorem of 106.90--106.91. The mean-periodic
equation helps identify the admissible zero-mode space, while analyticity,
theta growth and nonperiodicity prove the strict kernel statement.

What it does not provide is a comparison with the physical source deficit:

\[
 G_J>0
 \quad\not\Longrightarrow\quad
 G_J>\delta_J.                                     \tag{18}
\]

The one-row identity (10) shows that the missing amount is not an
auxiliary conditioning loss. It is exactly the completed shifted form.
For the general adapted row, 106.91 gives the same statement with the
finite-exhaustion loss:

\[
 \mathfrak C_J(Y)-\delta_J
 =\sigma_\infty-\mathfrak L_J(Y),
 \qquad \mathfrak L_J(Y)\downarrow0.              \tag{19}
\]

Thus the no-nuisance calculation is the sharp core of the full determinant
identity, not a degenerate artefact.

## 5. Semantic audit

The closest earlier statements are the following.

* 106.43 identifies \(\mathcal Q\) with the convolution equation
  \((hq)*K=0\).
* 106.44 proves that mean periodicity and the arithmetic resonance equation
  can coexist unless one excludes the off-line channel.
* 106.64 writes that channel as a negative Krein evaluation and proves
  that an off-line orbit produces a negative mean-periodic state.
* 106.69 shows that vertical half-shift identities do not control the
  horizontal Toeplitz--Hankel Gram matrices.
* 106.70 shows that compact-open mean-periodic synthesis does not imply
  weighted form-core synthesis.
* 106.89--106.92 derive the radical-conditioned gain and the physical
  bordered-minor gate.

The new point isolated here is the exact compatibility calculation
(10)--(15): the mean-periodic equation does not add a positive term to the
bordered minor, and the finite radical correction used by that minor is
not itself mean-periodic.

## 6. Verdict

The Riemann mean-periodic equation constrains the bordered Christoffel
columns enough to prove injectivity and positive local determinants. It
does not constrain them enough to prove

\[
 G_J>\delta_J.
\]

Already in the one-row physical system, the desired surplus is exactly
\(\mathcal A_\infty(q,q)\). Under a hypothetical off-line orbit there is a
mean-periodic \(q\) for which this quantity is negative, and then no finite
ordinary-prime block crosses. Therefore a universal proof of the strict
minor domination from the coupled physical formula would itself exclude
the negative Krein channel. Mean periodicity is the correct domain
constraint, but it is not an independent source of the missing sign.
