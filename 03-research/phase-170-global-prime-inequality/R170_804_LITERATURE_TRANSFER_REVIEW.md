# R170_804 — What can be transferred to D after the reading

Order preserved: Dubon, Freedman, additional candidates.
Versioned sources and local texts in
[the registry](../../00-references/arxiv-math-nt-2026-review/README.md).
This document distinguishes reading statements, reconstructing steps,
and full validation. **There is no complete audit of the 27 works.**
Nor was a proof of global positivity of Paper 46 obtained.

## 1. Dubon: quantifying the cost of selecting the witness

The proofs of lemma 4.1 and proposition 5.1 of
[2609.17875v1](https://arxiv.org/abs/2609.17875v1) were reviewed.
The anticoncentration uses coordinates independent under Haar. It is
not a pointwise inequality at the frequency that produces the first
contact.

Our own adaptation in
[R170_802](R170_802_DUBON_SELECTION_TRANSFER.md) gives a quantitative
proof of the difficulty: for S=ΣaₚZₚ, V=Σ|aₚ|² and a selection with
law ν of relative entropy H with respect to Haar,

    Eν Re S ≤ √(VH).

A deterministic pointwise selection is singular and this bound does
not control it. It would be usable if the extremal geometry provided a
selection law with controlled entropy and a proved relation to the
critical value. Neither of those two properties is available.

## 2. Freedman: accounting for the boundary repair

The lifting steps and the enlarged traces of appendices C–D of
[2606.29555v1](https://arxiv.org/abs/2606.29555v1) were examined. The
status declared in the appendices must be distinguished from the open
items of the introduction. Not every certificate or operator was
audited.

[R170_803](R170_803_BOUNDARY_REPAIR_AND_EXACT_RESPONSE.md) proves that
a repaired positivity K+R*DR≥0 also transports the repair: with J the
inclusion, one obtains J*KJ+(RJ)*D(RJ)≥0. To deduce the original sign,
that second term must be annihilated or paid for. The continuous
counterexample written there also shows why positivity on ker R does
not guarantee a bounded repair without rank conditions.

## 3. Three Gates: one useful lemma and a transport still unverified

The focused audit is in [R170_801](R170_801_THREE_GATES_AUDIT.md). The
most usable independent reconstruction is in
[R170_805](R170_805_COMMON_COMPLEMENT_CAPACITY.md): for equal disjoint
windows of length ε, the document's explicit energy r satisfies

    r[u] ≥ Σν [log(1/(2ε))−Δν] ||fν,0||²,
    Δν = (1/2)Σμ≠ν [log(1+1/Dνμ)−1/(Dνμ+1)] ≤ 1−γ_E.

The proof subtracts each pair's interaction exactly once. Together
with the exact minimization of l₀ over the same complement, it keeps
the mean and fluctuation sectors in a single bound. This is reusable
mathematical material from the model, not a validation of its
arithmetic induction.

What remains missing is identifying the transported form of the
Paper 46 operator with that model, including the primes and the polar
term. The audit neither proves nor refutes the identification of
lemma 8.4 of Three Gates.

## 4. Tools that allow selection: also check phase and norm

The modulation supremum of the operator of
[Fragkos–Krause–Miheisi–Sun](https://arxiv.org/abs/2607.05560v1) does
allow selecting the frequency according to the spatial point within
its ℓᵖ estimate. This is a real difference from a Haar average. But
its additive phase and its weight Λ(n)/n are not those of our problem.

A direct application exposes the cost. To represent, at x₀, the Mellin
sum over a positive block of integers, one can take

    f(x₀−n)=√n w(log n) n^(iγ) exp(−2πiλ₀n).

Then the input norm is

    ||f||ₚ = (Σ n^(p/2)|w(log n)|ᵖ)^(1/p).

On a block of length comparable to X and weight of order one, this has
size X^(1/2+1/p), not log γ. That the maximum allows selection does not
remove this cost. No better transfer has been constructed.

A linearization of log n around X on [X,X+H] introduces a phase error
of at most |γ|H²/(2X²). Hence the absolute error is bounded by

    [|γ|H²/(2X²)] Σ Λ(n)n^(−1/2)|w(log n)|.

That error and the sum over blocks must be paid for; an analogy of
phases is not enough.

In [Robles](https://arxiv.org/abs/2609.11070v1), proposition 6.2 and
its use of prime-dependent prefixes were reviewed. It is an
interesting selection tool, but the bilinear oscillation is additive.
Substituting (pn)^(iγ)=p^(iγ)n^(iγ) separates that phase: the mechanism
is not imported with the same gain. Moreover Λ does not automatically
satisfy the hypotheses of the multiplicative class of the main
theorem.

## 5. Coverage of the remaining candidates

The table records what was actually examined, not an acceptance of
every proof. Links and versions are in the bibliographic registry.

| Work | Depth of this review | Consequence for D |
|---|---|---|
| Suzuki 2606.09096v3 | Introduction and representation theorems | Operator associated with the Weil form; constructing its extension does not prove its positivity. |
| Groskin 2607.02828v3 | Statements and test transport | Tail control for compressions; does not replace the infinite complement. Already cited by Paper 46. |
| Zhu 2608.24827v2 | Comparison with its earlier incorporation | Already cited by Paper 46; a new audit of v2 was not completed. |
| Maynard–Pandey–Radziwiłł 2608.14777 | Main theorem and proof architecture | Excluding critical configurations is a structural idea; the additive bound does not prove the Mellin sign. |
| Dong–Wang–Wang–Zhang 2608.31060 | Theorems 1.1–1.2 | Near-maximal values of unweighted sums force zeros; that threshold still needs to be derived from our failure. |
| Ramaré 2609.25879 and 2609.25885 | Hypotheses and main results | Regularity near sieve saturation and residual restrictions; it was not proved that our witness satisfies those hypotheses. |
| Croot–Mao–Pohoata–Yip 2607.15311 | Main inverse theorem | Requires a large integer set with modular restrictions; not constructed from the extremal F. |
| Menon 2607.15574 | Main statements | Averages over intervals; an exceptional witness remains possible. |
| Dhiman–Kadiri–Quesada-Herrera 2609.00537 | Introduction and location of theorems 8–10 | Possible improvement of computable errors; its full proof not audited nor its constants incorporated. |
| Fiori 2609.22624 | Statements | Explicit density near the boundary, not pointwise exclusion. |
| Irfan 2609.33953 | Results and model separation | Do not convert a matrix integral or a functional model into a theorem for integers. |
| Tang 2608.14852 | Main theorem | Reciprocity of an average in height, not of the selected value. |
| Tardy 2608.26814 | Introduction and statements | Logarithmic density; pointwise transfer pending. |
| Holland 2608.08682 | Hyperbolicity theorem region | Does not cover every index. |
| Michalowski 2607.16795 | Minors theorem region | Does not cover every index; certificates not reproduced. |
| Liu 2609.33278 | Main criterion | Detection identity, not an energy inequality. |
| Freiberg 2609.33692 | Hypotheses and main theorem | Uses uniform Hardy–Littlewood; not an unconditional input. |
| de Faveri–Pandey 2610.01035 | Moment and large values | Still need to prove the first contact forces a sufficiently large set of values. |
| Turnage-Butterbaugh 2607.04632 | Expository reading | Context for large values; no additional sign input identified. |
| Covei 2606.24924v2 | Earlier sieving and conditional comparison | Proof audit pending; no conclusion is imported. |
| Alpöge–Furman 2608.13637 | Results and selected sections | Rank and trace control proportions; they do not by themselves exclude a negative direction. |

## 6. Concrete proof that the next attempt should supply

With the real decomposition of the energy, let B>0 be the eliminated
block, G the coupling, and C the preserved budget. For an
arithmetically constructed response X₀ and residual R₀=G−BX₀, the
exact complement is

    C−G*B⁻¹G
      = C−X₀*BX₀−X₀*R₀−R₀*X₀−R₀*B⁻¹R₀.

In infinite dimension the domains and rank conditions are needed; with
a positive gap B≥bI the expression is direct. Near the contact, the
possible divergence of B⁻¹ must not be hidden.

R170_805 may supply a lower bound for the budget **if the transport is
proved**. The arithmetic construction must control the residual in
that same metric and with its cross terms. None of the works reviewed
yet supplies that inequality for our witness. A reusable lemma and
more precise transfer conditions were obtained; Paper 46 was not
closed, nor was the full reading of all 27 manuscripts completed.
