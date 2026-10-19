# R170_000 — Global target and effective dependencies

**OPEN**. No proof of RH is claimed.

## 1. Self-contained statement

Let Λ(n) = log p if n = p^k, k ≥ 1, and zero otherwise. For T > 0,
extend F ∈ L²(−T,T) by zero to ℝ and set

$$
c_F(u)=\int_{\mathbb R}F(t)\overline{F(t-u)}\,dt,
\qquad \widehat F(\tau)=\int_{\mathbb R}F(t)e^{i\tau t}\,dt,
\qquad m(\tau)=\Re\psi(1/4+i\tau/2)-\log\pi.
$$

The goal is

$$
\boxed{\quad W_T(F):=
\frac1{2\pi}\int_{\mathbb R}m(\tau)|\widehat F(\tau)|^2\,d\tau
+2\Re\left(\int F(t)e^{t/2}\,dt\;
\overline{\int F(t)e^{-t/2}\,dt}\right)
-\sum_{2\le n<e^{2T}}\frac{2\Lambda(n)}{\sqrt n}\Re c_F(\log n)
\ \ge0.\quad}
$$

The domain of finite values is

$$\mathcal D_T=\left\{F\in L^2(-T,T):
\int_{\mathbb R}\log(2+|\tau|)|\widehat F(\tau)|^2\,d\tau<\infty\right\}.$$

Outside this domain the archimedean term is +∞ and the inequality is
interpreted in the extended reals. There is no ∞−∞ indeterminacy:
the polar and prime terms are finite and the negative part of m is bounded.
R170_101 proves these claims. The endpoint n = e^{2T}, if it is an integer,
can be included because c_F(2T) = 0.

By R163_401, Theorem 1.2, this goal for all T is equivalent to RH
(a result cited from the record). The spectral identity written there gives
positivity under RH, but using it while assuming that all ordinates
are real would be assuming the conclusion.

## 2. What is available and what needs correcting

**Certified range.** Paper 47, `thm:log5W`, and R163_401 §2.1 record
λᵂ_T ≥ 10⁻¹⁸ for 0 < T ≤ ½ log 5. This result is imported; the
certified computation was not re-run in this phase.

**First contact.** R163_401 §2.3 defines T_c = inf{T : λᵂ_T ≤ 0}.
At T_c, λᵂ_Tc = 0: the inequality still holds, with equality
for a nonzero vector. Hence "first failure" should be read as first
contact with zero, not as a strict counterexample at T_c.
The real-zero structure of the witness is imported from §2.4.

**Theorem M.** The exact statement of Paper 48, `thm:M(b)`, is

$$\forall\varepsilon>0\;\exists T_0(\varepsilon)\;\forall T\ge T_0(\varepsilon):
\quad\lambda_T^{\mathrm W}\le\lambda_T^{\mathrm P}
\le\lambda_T^{\mathrm A}\le\exp(-e^{(2-\varepsilon)T}).$$

It is an asymptotic upper bound for normalized infima. It is not an
asymptotic equivalence, it is not a bound for every F, and it does not by
itself describe the rate of approach to a finite T_c. By homogeneity,
W_T(aF)=|a|²W_T(F), so speaking of the size of the difference requires
normalizing F. Theorem M rules out certain arguments with a uniform
positive margin; it does not prove the impossibility of every technique
that uses estimates. Paper 48 notes that (b) is proved on the record and
not yet in a refereed article.

**Exact arithmetic.** The falsifiers on record prevent concluding the
sign from shared properties that they also satisfy. This does not amount
to a classification of every possible proof nor does it force a specific
identity. R169_000 v2 downgrades A8 to ARGUED-forced.
The determination of the tail via Eratosthenes is an exact identity;
R169_101 and R169_190 do not obtain the required sign from it.

**Uniformity.** The number of prime coefficients is finite for each T;
the space of tests remains infinite-dimensional. Finiteness of the
arithmetic support does not automatically prove termination of an
algorithm that decides all cases, especially when the infimum is zero.
Paper 47, `prop:decide`, assumes T computable and λᴾ_T ≠ 0 and deals with
λᴾ, not with an unrestricted decider for λᵂ or λᴬ.

## 3. The twisted reduction is still conditional

R167_101, Thm B, provides, given (Dom_θ),

$$\Re\mathcal S\ge B,\qquad
\mathcal S=\sum_{n\le Y}\Lambda(n)n^{-1/2+i\gamma_q}w(\log n),$$
$$B=(1-\theta)c_\Theta|G(t_q)|^2|k(-i\delta_q)|-E_K/4.$$

Hence a strict bound Re 𝒮 < B would exclude that configuration.
But the ledger itself keeps open:

1. (Dom_θ), control of the remaining quartets: O167.101.1.
2. The small regime, where this control of the on-line term does not
   ensure B > 0: O167.101.2; R169_000 §6 refers to P_gap.
3. The arithmetic bound (WS*).

It is not enough to replace the exact threshold B with "O(log γ)": one
needs the constants, the weight norms and the conditions that make B
positive. R167_101 Cor D(b) obtains the size ≈ 4 log(γ/2π) after
normalizing by w(0) in the lattice model; Cor D(a) only gives, in general,
the ceiling 2c_ΘY^δw(0)/δ. The model computation is not promoted to a
general theorem.

Moreover, R169_000 v2 corrects that γ_q is not determined by the window.
One cannot invoke independence of a frequency supposedly selected by it.

## 4. Result of the phase

The global inequality remains a single, well-defined goal. The route
via a twisted sum has not been unconditionally reduced to a single
pending lemma. This phase contributes a precise formulation and the
reductions of R170_101; it does not contribute the uniform-sign bound
nor does it extend the certified range.

Local references:

- [R163_401](../phase-163-integrality-defect/R163_401_D_CLOSURE_CANDIDATE.md).
- [R167_101](../phase-167-witness-weighted-sieve/R167_101_QUANTITATIVE_TARGET.md).
- [R169_000 v2](../phase-169-input-architecture/R169_000_INPUT_ARCHITECTURE.md).
- [R169_190](../phase-169-input-architecture/R169_190_AUDIT.md).
- [Paper 47](../../04-papers/47-row-d-dual-certificates/main.tex).
- [Paper 48](../../04-papers/48-row-d-route-map/main.tex).
</content>
