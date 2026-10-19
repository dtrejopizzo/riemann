# R170_101 — Domain, real tests, and scale quantifier

**PROVED here, elementary results; not a closure of D.**
Notation: R170_000. No novelty over the corpus is claimed.

## 1. The extended form is well defined

By Cauchy–Schwarz, |c_F(u)| ≤ ‖F‖²₂. Translation is continuous in L²,
so c_F is continuous. The supports of F(t) and F(t−u) intersect only in
a null set when |u| ≥ 2T. So c_F(u) = 0 there, even at the endpoints.
The prime sum is finite and its absolute value does not exceed
(Σ_{n<e^{2T}}2Λ(n)/√n)‖F‖²₂.

Also

$$|A(F)|,|B(F)|\le\sqrt{2\sinh T}\,\|F\|_2,
\qquad |2\Re(A(F)\overline{B(F)})|\le4\sinh T\,\|F\|_2^2.$$

The digamma expansion gives
m(τ) = log(|τ|/(2π)) + O(|τ|⁻²) at infinity.
Primary source: [NIST DLMF, 5.11.2](https://dlmf.nist.gov/5.11.E2).
The line 1/4+iτ/2 contains no poles of ψ. By continuity and the expansion,
m is bounded below and m(τ)−log(2+|τ|) is bounded on ℝ.
Plancherel then proves that the archimedean integral is finite exactly
on 𝒟_T, and is +∞ on its complement. ∎

## 2. It suffices to prove the sign for real tests

Write F=f+ig with f,g real. The domain is stable under conjugation,
since its Fourier weight is even, and hence f,g ∈ 𝒟_T if F ∈ 𝒟_T.
Since m is even, the cross term of |f̂+iĝ|² is odd and its integral
vanishes. This is justified by Cauchy–Schwarz with weight log(2+|τ|).
Directly,

$$\Re c_F(u)=c_f(u)+c_g(u),$$
$$\Re(A(F)\overline{B(F)})=A(f)B(f)+A(g)B(g).$$

Hence W_T(F)=W_T(f)+W_T(g). Positivity for real tests is equivalent to
positivity for complex tests. Neither parity nor real zeros of the
transform need to be assumed for this reduction. ∎

## 3. An unbounded sequence of windows suffices

If S ≥ T and F is supported in (−T,T), its extension to (−S,S) has the
same transform, the same moments and the same autocorrelation.
The additional terms of the prime sum vanish. Hence

$$W_S(F)=W_T(F),\qquad\mathcal D_T\subset\mathcal D_S.$$

For any sequence T_j → ∞,

$$[\forall T>0,\ W_T\ge0]\quad\Longleftrightarrow\quad
[\forall j,\ W_{T_j}\ge0].$$

Indeed, given T one chooses j with T_j ≥ T and applies the identity.
In particular T_j=j suffices. No spectral continuity is needed for
this argument. The infinite quantifier persists: checking a finite
number of j only covers windows up to their maximum. ∎

## 4. Why exact arithmetic still does not give the sign

The unique-factorization identity is

$$\sum_{d\mid n}\Lambda(d)=\log n\quad(n\ge1).$$

For any finite Y and any complex weight a(n), Möbius inversion and a
finite rearrangement give exactly

$$\sum_{n\le Y}\Lambda(n)a(n)
=\sum_{dm\le Y}\mu(d)\log m\,a(dm).$$

Substituting a(n)=n^{-1/2+iγ}w(log n), the twist factors as
d^{-1/2+iγ}m^{-1/2+iγ}, but μ(d) and the real part of the weight have no
fixed sign. The identity is not a sum of squares and does not prove
Re 𝒮 < B. The missing step is an inequality on this exact expression.
This computation coincides with the difficulty of R169_101; it opens no
new route nor does it prove that every possible exploitation of Möbius
is impossible. ∎

## 5. Verification and limits

The Fourier conventions, the real/complex decomposition, the support
endpoints and the quantifiers were checked algebraically.
The imported hypotheses were cross-checked against the statements of
Papers 47–48 and the R167_101 ledger. No numerical experiment was used
as proof, and the earlier certificates were not re-run.
</content>
