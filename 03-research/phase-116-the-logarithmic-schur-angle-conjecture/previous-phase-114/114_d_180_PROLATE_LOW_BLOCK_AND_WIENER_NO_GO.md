# D.180 — Exact prolate low block and the uniform-Wiener no-go

## Verdict

The complete positive reference does not form a uniformly bounded family
in any standard solid Wiener/Jaffard algebra.  There are two independent
reasons:

\[
 \sum_{p^j\le N}{\log p\over p^{j/2}}\asymp\sqrt N,  \tag{0.1}
\]

and the cell matrix of the Gamma screw has the critical near-diagonal tail
(1/|i-j|), whose solid row sum grows logarithmically.  Consequently a
generic inverse-closed theorem, whose constants depend on the algebra norm
and the spectral gap, cannot transfer the simplex constants of D.178
uniformly.

There is nevertheless an exact replacement.  Let (C_{T,R}) be the
time--band concentration operator on the two-Tate primitive source, let
(0<\eta<1), and put

\[
 P_{\rm lo}=\mathbf1_{(\eta,1]}(C_{T,R}),qquad
 P_{\rm hi}=I-P_{\rm lo}.                            \tag{0.2}
\]

Then

\[
 \boxed{
 \operatorname {rank}P_{\rm lo}
 \le {2TR\over\pi\eta},}                            \tag{0.3}
\]

while the exact reference

\[
 \mathcal R_T=\mathcal H_{5/4}
 +\sum_{p^j\le e^{2T}}{\log p\over p^{j/2}}
                  J_{p^j,-}^*J_{p^j,-}              \tag{0.4}
\]

satisfies the Feshbach estimate

\[
 \boxed{
 P_{\rm hi}\mathcal R_T^{-1}P_{\rm hi}
 \le {1\over(1-\eta)h_{5/4}(R)}P_{\rm hi}.}         \tag{0.5}

All low--high mixing and every prime-power channel are retained in (0.5):
it is a bound for the corresponding shorted inverse, not for the naive
high diagonal block.

Moreover there is an exact decomposition

\[
 \boxed{
 \mathcal R_T^{-1}=G_{\rm hi}+G_{\rm lo},qquad
 \|G_{\rm hi}\|\le{1\over(1-\eta)h_{5/4}(R)},qquad
 \operatorname {rank}G_{\rm lo}\le2\operatorname {rank}P_{\rm lo}.} \tag{0.6}

Thus every return word splits into a pure high-mode word, with an explicit
Gamma denominator at every inverse, and words containing at least one
finite-rank low-mode insertion.  The latter are the only place where the
PNT/Tate centered estimate is needed.

This is a proved low/high reduction, not yet the summable return bound.
The remaining high-mode task is a localized (rather than solid-Wiener)
word estimate; the remaining low-mode task is finite-dimensional of rank
(O(TR/\eta)) and carries the complete centered discrepancy (E_N).

## 1. Exact concentration operator on the primitive source

Let (I_T=[-T,T]), let (\mathcal F) be the unitary Fourier transform, and
let (B_R) be multiplication by (\mathbf1_{[-R,R]}).  On
(L^2(I_T)), with zero extension, define

\[
 C_{T,R}=P_T\mathcal F^{-1}B_R\mathcal F P_T,         \tag{1.1}
\]

where now (P_T) also denotes the support projection.  This is a positive
compact contraction with

\[
 \operatorname {Tr}C_{T,R}={2TR\over\pi}.            \tag{1.2}

Restrict it to the exact two-Tate primitive subspace.  Compression cannot
increase the trace, so the same upper bound holds.  Since every eigenvalue
on (P_{\rm lo}) is greater than (\eta),

\[
 \eta\operatorname {rank}P_{\rm lo}
 \le\operatorname {Tr}C_{T,R},                       \tag{1.3}

which proves (0.3).  The two Tate conditions are present before the
spectral split; no ambient low mode is reintroduced.

## 2. Gamma coercivity on the exact high block

For every supported primitive (F), Plancherel and monotonicity of
(h_{5/4}) give

\[
\begin{aligned}
 \mathcal H_{5/4}(F)
 &\ge h_{5/4}(R){1\over2\pi}
       \int_{|\tau|>R}|\widehat F(\tau)|^2d\tau\\
 &=h_{5/4}(R)\langle F,(I-C_{T,R})F\rangle.          \tag{2.1}
\end{aligned}
\]

The spectral definition (0.2) gives the operator inequality

\[
 I-C_{T,R}\ge(1-\eta)P_{\rm hi}.                    \tag{2.2}

Every antisymmetric prime-power term in (0.4) is positive.  Combining
(2.1)--(2.2), on the primitive source,

\[
 \boxed{
 \mathcal R_T\ge a_RP_{\rm hi},
 \qquad a_R=(1-\eta)h_{5/4}(R).}                    \tag{2.3}

This inequality acts on the **whole** low--high sum.  Therefore for a
fixed high vector (f_{\rm hi}),

\[
 \inf_{f_{\rm lo}}
 \langle f_{\rm lo}+f_{\rm hi},
          \mathcal R_T(f_{\rm lo}+f_{\rm hi})\rangle
 \ge a_R\|f_{\rm hi}\|^2.                           \tag{2.4}

The left side is the Feshbach short of (\mathcal R_T) through the low
block.  Inverting (2.4) proves (0.5).  Hence arbitrary low--high mixing by
the Gamma kernel, the boundary killing and all (J_{p^j,-}) cannot weaken
the displayed constant.

## 3. Finite-rank inverse decomposition

Put (G=\mathcal R_T^{-1}) on its supported range and define

\[
 G_{\rm hi}=P_{\rm hi}GP_{\rm hi},
 \qquad
 G_{\rm lo}=P_{\rm lo}G+GP_{\rm lo}-P_{\rm lo}GP_{\rm lo}. \tag{3.1}

Then (G=G_{\rm hi}+G_{\rm lo}).  Equation (0.5) bounds the first
summand.  The range of (P_{\rm lo}G) lies in
(\operatorname {Ran}P_{\rm lo}), and the range of (GP_{\rm lo}) has
dimension at most (\operatorname {rank}P_{\rm lo}).  Hence

\[
 \operatorname {rank}G_{\rm lo}
 \le2\operatorname {rank}P_{\rm lo},                 \tag{3.2}

which proves (0.6).

The operator (G_{\rm lo}) need not be positive.  It is a finite-rank
ledger for every word which enters the dangerous low block.  The pure
high word uses only (G_{\rm hi}) and receives the explicit factor
(a_R^{-1}) at each occurrence.

## 4. Why a standard uniform Wiener/Jaffard theorem does not apply

The prime part of the reference contains the positive differences

\[
 w_nJ_{n,-}^*J_{n,-},
 \qquad w_n={\Lambda(n)\over\sqrt n}.                 \tag{4.1}

In any solid convolution algebra whose norm dominates the total variation
of the shift coefficients, its norm is bounded below by

\[
 \sum_{n\le N}w_n.                                   \tag{4.2}

The prime number theorem and partial summation give

\[
 \sum_{n\le N}{\Lambda(n)\over\sqrt n}
 =2\sqrt N+o(\sqrt N).                               \tag{4.3}

Thus (4.2) is not uniformly bounded.  This already includes all powers
(p^j); omitting them changes lower-order terms but not the obstruction.

For the Gamma part, use integer-cell width (\ell\asymp N^{-1}).  On
normalized cell indicators at separation (m), (2.4) of D.134 gives

\[
 |(\mathcal H_{5/4})_{i,i+m}|
 \asymp \ell\gamma_{5/4}(m\ell)
 \asymp {1\over2m}
 \quad(1\le m\ll\ell^{-1}).                         \tag{4.4}

Therefore its solid off-diagonal row sum is at least
(c\sum_{m\le c/\ell}m^{-1}\asymp\log(1/\ell)).
The Jaffard norm with cell-index exponent (s>1) also diverges, since the
maximum of (m^{s-1}e^{-c\ell m}) is of order
(\ell^{1-s}).

The two-Tate compression changes an operator by finite rank, but the
standard inverse-closed constants depend on both the diverging solid norm
and the inverse gap.  A rank-two correction does not provide a uniform
bound for either quantity.  Consequently the hypotheses needed to infer a
uniform (\ell^1) inverse kernel from a generic Wiener/Jaffard lemma are
absent.

This does not say that the particular inverse has no localized tail.  It
says that such localization must be proved after the exact prolate split
(0.2), exploiting the compensated Dirichlet structure and the centered
arithmetic word Gram; it cannot be read off from a standard solid algebra.

## 5. Return-word consequence

Insert (0.6) at every inverse in an exact return word.  The expansion is a
sum over (\{\mathrm{hi},\mathrm{lo}\})-marked words.

* The all-high word has an explicit inverse norm
  (a_R^{-k}).  To retain D.178's simplex constant one still needs a
  high-frequency almost-convolution estimate for the Hankel boundary
  blocks.
* Every other word factors through (\operatorname {Ran}P_{\rm lo}) at
  least once.  Its nontrivial alignment is therefore contained in a block
  of rank at most (2TR/(\pi\eta)), where the low-frequency PNT estimate for
  (E_N) and the exact two Tate moments apply.

Choosing (R=R_0(N)\to\infty) slowly, as in D.167, makes
(h_{5/4}(R)\sim\log R) while keeping the low rank
(O(R_0(N)\log N)).  This is the exact low/high tradeoff now to optimize.

The accompanying verifier checks the concentration-rank estimate, the
Feshbach inverse bound and finite-rank decomposition on noncommuting
matrices.  It also records the divergent Gamma and prime solid-algebra
ledgers along growing integer cells.
