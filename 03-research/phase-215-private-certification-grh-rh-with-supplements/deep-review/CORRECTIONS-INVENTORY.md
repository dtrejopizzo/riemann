> **V1: historical record, revised in V2.** Do not apply its character objections or its propagation statuses to the corrected manuscripts without consulting the [V2 status](../review-v2/STATUS.md). The specialised cancellation of characters corrects the global impact attributed in V1; the remaining results are being consolidated.

# Corrections inventory for the author

Consolidation of 28-11-2026. It refers to the sources `04-papers/NN-*/main.tex` examined; the numbers below are lines of those sources. The papers were not modified. The verdicts **(b)** apply to the statement or inference expressly identified, and not by automatic extension to all the theorems of the paper. A repair reconstructed by the audit must be incorporated into the text before it is described as correct as written.

## 1. Critical priority for the global conclusion

### P53 — characters of `pcu:product` and the subsequent period

**(b), equality 3351–3352; first invalid inference 3359–3360.** With the definition `ω_{α,β}(g,h)=α(det g)⁻¹β(det h)ω_Hom(g,h)`, the quotient between the two sides is

`α(det g) α(det y) β(det l)`.

It is not a normalisation constant. In `pcu:period` 3407–3410, l=u is an integrated variable: the factor β(det u) remains inside the period and cannot be taken out on the grounds that it has modulus one. The defect also appears in P58:37993–37994. It was checked independently by two lines of review.

**What to correct:** fix the source/target characters on each block; recompute `pcu:period` and `pcu:coeff`; identify the resulting period with the one needed by the equal-rank ratio; prove non-vanishing and exact modulus of the constant. Then redo `P-top`, `P-std`, `P-equal` and `pcx:X`. Changing only one character name does not preserve the two periods used: a single target character restricts in the same way to both blocks.

**Status:** there is no proved global repair. The written route to the exchange, and through it to the Covolume Theorem and to the global conclusion, is not certified. This does not prove that exchange is false nor that RH is false. [Computation and chain of dependencies](ERROR-53-CHARACTERS.md); [additional use in `pct:vantop`, 5632–5634](MAP-53.md).

## 2. Proved local repairs

| Paper / point | Verdict and first line | Change to be incorporated | Effect checked |
|---|---|---|---|
| 46, complex polar pairing | **b**, 277: `2Re(a conjugate(b′))` is called Hermitian | Write `a conjugate(b′)+b conjugate(a′)`. The former expression gives 2 in one order and 0 in the reverse for (1,0),(0,1). | The diagonal 2Re(a conjugate(b)) is already correct; W_T does not change. |
| 46, `thm:coer-A` | **b** local 2094: maximum at (2R²−a)/3 for all R | If R²<a/2 the point is outside the interval. Bound with y=x+a and `y²(R²+a−y)≤4(R²+a)^3/27` on the larger interval [0,R²+a]. | Same bound M_R for all R; same constants; R=2 was already in the interior range. |
| 49, Flensted–Jensen | **b**, 2250–2251: changing F(xh) by declared right translation R(x)F(h)=F(hx) | Start directly from `F(g)=∫e(h)F(gh)dh`; substitute x=gh and use `e(h)=d c(h⁻¹)`. The result is `F(g)=d∫F(x)c(x⁻¹g)dx`. | Avoids the incorrect double integral; preserves the constant and Steps 2–4, without centrality of F. |
| 51, `pm:siegel(c)` | **b**, 4453, repeated 4511–4512: uniform convergence for all g | Require g and x in compact sets for uniform convergence of the series. Keep separately the global bound of the total sum. | Local continuity and convolution by e∈L1 remain justified. Do not confuse a uniform bound of sums with uniformly small tails. |
| 51, `pbo:tube` | **b**, 10499–10500: incorrect homogeneous dimension | Replace `Q=2ρk+ρ²` by `Q=2ρk+2ρ²`, since σ scales by t². | Still Q≤r²/2, `(1+1/Q)^Q<3`, norm≤T⁹≤T¹⁰; preserves the factor 3 and the exponent 10⁵n⁴ of O1. |
| 52, `pff:offT` | **b**, 4364–4365: u→0 makes the frequency cut contract | Take u=varpi₁^(−j), j→∞, or use directly the exhaustion B_l of `pfg:orth/fibres`, 4970–5080. | Frequencies exhaust the space and duals contract. The uniform domination already proved preserves the constant of Siegel→fibres→orbital squares. |
| 52, action of `U_(<l)` | **b**, 1810: says that it fixes each e_b, b<l | Replace by preservation of the flag and unitriangular action; it may send e₁ to e₁+a e₀. | The effective uses require congruence modulo the lower flag and triviality on Y^(l), which remain valid. |
| 53, `pcx:decay` | **b** in scope 2257–2269; inference 2622–2627 requires a place that does not exist if P=∅ | Add P≠∅ to the convergence hypothesis and propagate it to `pcx:conv` when it is cited outside the exchange context. | In `pcx:X` the non-trivial modulus already supplies a place. The literal empty statement does have a counterexample: source 0, hyperbolic target, theta=1 and unbounded height. |
| 53, `pcu:mixedmodel/slicedecay` | **b**, 4409–4410: Hilbert-bounded pointwise evaluation | Define sl(x) on coherent translates and extend in moment norms. Prove `(1+|x|)^M||sl(x)v||_N≤C||v||_(N+M)` before exchanging integrals. | In the L2 model, φ(x/ε)v₀ has norm→0 and fixed value at 0, refuting the Hilbert phrase. The reconstruction in moment norms preserves M1, `P-slice` and its constant κ. |
| 55, M3 | **b**, 883: all the roots have order dividing p_i^r−1 | For a factor of degree d_k use p_i^(d_k)−1; d_k|r is not assumed. The prime dividing that order divides #GL_rt and N_ch. | Preserves `v_l(det(R(γ)−1))≤r v_l(N_ch)`; M4/M5 use a primitive place and require no change. |
| 55, G4 | **b** in the justification 3946–3949: norm F_(q^n)→F_(q^d), d=lcm(d_k), non-existent if d does not divide n | Choose a tame topological generator and compatible roots; use directly θ_d(s) and its projections to d_k|d. | Degrees 2,3 give n=5,d=6. The repair preserves G4; choosing only θ_n(s) as generator is not enough. |
| 55, `pri:BL(c)` | **b**, 2271 and 6556–6560: a fixed polynomial kills all s∈I_w | Restrict to the normalised tame generator needed in `pri:columns`, 2855–2865, or define o_(w,s) with roots evaluated at s. | For s=γ² the roots are squared. The application uses one generator and preserves its bounds. P56 already distinguishes M_s,q_s and does not contain this same error. |

Evidence and proofs: [46](CHECKLIST-46-PURE.md), [49/51/52](SPANNING.md), [uniformity of 51](MULTIPLICITIES.md), [convergence and topology of 53](COVOLUME.md), [55](SELMER.md). These repairs do not solve the critical incompatibility of characters of 53.

### P55 — make "base level" uniform and preserve the type e_c

**Discrepancy of formulation and omitted construction, repaired in the audit; not a counterexample to theorem pg:III.** `prm:def-level` 7527–7543 defines F(O) without the condition e_c. `prm:label` 7606 does require e_cy=y. `pri:BL(c)` 2265–2273 and the choice of Y at 3094–3098 speak of all systems of base level; the proof 6467–6471 needs the type e_c. Subsection 6430–6437 declares a restricted convention, but it must be propagated to the statements and to Y.

It is not enough to project the Higman operator by e_c, because that would introduce uncontrolled denominators. The reconstructed repair is to work at free level J₁ and to average the indicator Ψ₁ over `D=Π_(w chosen)GL_n(F_w)`:

`Ψ_D=Σ_(d∈D)d⁻¹Ψ₁d`.

The actions of D and of the auxiliary group Γ commute, since they have disjoint supports. Ψ_D is integral and D-invariant; it preserves the invariants of the level and the type e_c. Its sum of auxiliary conjugates equals #D. One takes c₀=#D, and #D divides N_ch; the estimates only needed that divisibility. Thus β_l is preserved and nothing is paid for a fractional projector.

**Action for the author:** restrict BL and Y explicitly to the type e_c and replace the construction of the operator by this one, proving the commutations and divisibilities. Do not describe the original operator as if it already had that invariance. [SELMER§11.2](SELMER.md).

### Two additional repairs of the auxiliary estimates of P53

- **(b) `pgq:slice`, 13740–13742:** the product `(g(r₀⊕1))⁻¹g(r⊕1)` is `(r₀⁻¹r)⊕1`, not `(rr₀⁻¹)⊕1`. Replace `rr₀⁻¹` by `r₀⁻¹r` throughout the proof and integrate by **left** invariance. Since `||g(r₀⊕1)||=t₀`, the norm of its inverse is also t₀ and t₀≤||g(r⊕1)||. The same domination results and exactly `2·16^(n²)Vτ`, by `pgq:balls` with s/2. The lemma is preserved; the equality as written is incorrect.
- **(b) `pgk:lat(c)`, 14549–14551:** preserving the unimodular form does not imply that `det x_f` is a unit at each place of E. At a split place, U(1)(F_v) contains `(π,π⁻¹)`. Replace that sentence by the computation of the total modulus: the absolute values of the determinants at two conjugate places cancel, and at a non-split place the determinant has norm one and valuation zero. Hence the total finite Jacobian is one; the declared covolume and its constant are preserved. See [AUXCORE-53-54](AUXCORE-53-54.md).

## 3. Gaps (c) and obligations not replaced by an erratum

- **P53, consequences of the twisted period:** besides the failure (b) already demonstrated, a new proof preserving non-vanishing and the L-factor of exchange after correcting the characters remains unverified. There is no mathematical authorisation here to regard the Covolume Theorem as repaired.
- **P46:2405–2409, finite comparisons:** the text declares them without proof. Neither the positivity for up to four arbitrary exponents nor the bound for thirteen poles with multiplicities was verified. They are not used in the ladder proposition. The all-degree identity 2411–2428 was indeed reconstructed, but it is explicitly conditional on the arithmetic input; it does not remove the global obligation of 53.
- **P49, stronger formula W4 for δ_g:** the decomposition of the coefficient into a root of unity, a power of an index and a value of υ was not collated literally. THETA reconstructs separately the consequences actually used: modulus at each conjugate and local integrality. It is advisable to prove the complete formula or to state only the justified consequences; this limited scope should not be confused with a failure of those consequences.
- **Novelty and priority:** a reconstructed connection does not prove historical priority. The claims of integral novelty require specialised comparison with primary sources; the report on connections distinguishes antecedents, verified mechanisms and pending proposals.

This section does not revive historical pending items that the later passes have already closed. For the verdict on each question and the certificate of T=2.8022 one should consult the final matrix of the main front and WINDOW-28022, not an old list of tasks.

## 4. Editorial data and presentation of certificates

1. **P46:1896–1899.** ε9≤0.01567 is true with the precise value of γ1, certified in `evidence/Z1_margin_46_arb.json`. But it does not follow from γ1≥14.13 alone: this gives 0.0157505828. Using ε≤0.016 preserves exactly the denominator 0.484 and the final bound; alternatively declare the precise interval used. It is a precision about dependence, not a refutation of the true decimal.
2. **P46, certificates of log5/2.** Incorporate or link the programs and outputs with version, precision, remainders and effective method. The four inertias passed with preconditioned congruence and Gershgorin; the naive interval factorisation failed through accumulation of dependency. Do not present that computational failure as a negative sign nor claim that that algorithm passed. NUMERICS-46 documents the positive certificate that did pass.
3. **Illustrative roundings.** Separate descriptive decimal numbers from the rational/interval bounds used. Do not automatically replace an exact constant by its rounding down in a certificate.
4. **P58 and appendices.** Propagate the corrections to the reproductions of statements and proofs; in particular, the character failure is also in 58. Check again the hypotheses P≠∅, type e_c, tame generator and moment topology at the junctions, in addition to textual equality.
5. **Attribution of review.** The specialists mentioned by the author have not endorsed this report. No messages were sent to them. This audit and the reproduced certificates must be identified as such.

## Practical order of revision of the manuscript

First resolve the character identity and its period: it is the obligation that prevents the global chain from being certified. In parallel the proved local repairs can be incorporated, each with its short proof. Then update appendices/58 and verify again the junctions affected. Finally incorporate the reproducible certificates and decide whether the auxiliary statements without proof are kept. None of these steps requires modifying the cut-off values T fixed by the author.
