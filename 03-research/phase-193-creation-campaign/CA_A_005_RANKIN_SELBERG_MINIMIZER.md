# CA_A_005 — Candidate (e): regularized Rankin–Selberg with the minimizer's Dirichlet polynomial as test vector

Phase 193. Pen and paper. Applies the round-1 lessons: line doubling is not a barrier, O8 coupling,
openness at scale λ_A/κ_T.

## 0. Corpus check
EI_002 (phase 192): Q=(1/π)∫F̂₀²|ζ_w|²Re R_{X′}, which is the second-moment form (S), a restatement of D.
Phase 190: minimizer h* ≈ m^{−½}w(m/M). CA_A_001 Cor. 3: the Maass–Selberg symbol sits at abscissa 1.
06_OPEN_RESIDUES "(M) propagation" (L2_027): OPEN. The record has no Rankin–Selberg construction with a minimizer-built
test vector.

## 1. Construction
Let g(τ)=F̂₀(τ)D_h(τ), with D_h(τ)=Σ_{m≤M}b_m m^{−½−iτ} the minimizer's Dirichlet polynomial. Form the Eisenstein wave packet
f_g(z)=(1/4π)∫g(τ)E*(z,½+iτ)dτ, where E*=ξ(1+2iτ)E (completed; entire on the line). For real w>1, E(z,w)>0, and
  RS_w(g):=∫^reg_{Γ\ℍ}|f_g|²E(·,w)dμ ≥ 0.
Unfold and Mellin-transform in y (CITED, standard: Zagier's renormalization, and the Ramanujan identity
Σσ_{a}(n)σ_{b}(n)n^{−s}=ζ(s)ζ(s−a)ζ(s−b)ζ(s−a−b)/ζ(2s−a−b)):
  RS_w(g)=∫∫ g(τ)conj g(τ′) K_w(τ,τ′) dτdτ′ + (degenerate terms from the constant terms),
  K_w(τ,τ′)=c(w,τ,τ′) · Π_{±,±}ζ(w±iτ±iτ′)/ζ(2w),
with c a ratio of Gamma factors. For the conjugate pairing (−τ′) the shifts are w±i(τ−τ′) and w±i(τ+τ′).

## 2. Trap (B″): is the positivity test-generic and comb-generic? — YES, so the trap closes (PROVED)
**Prop 1.** RS_w(g)≥0 holds for every g∈L²∩(decay), i.e. for every test vector. Λ does not occur in K_w except through
ζ at abscissa w>1 (absolute convergence). Hence the inequality is unchanged under O1–O8 applied to the comb, because
the comb does not appear, and it holds for every h*, whether or not h* is the minimizer.
*Proof.* Pointwise positivity of E(·,w) for w>1 and |f_g|²≥0; the right-hand side does not contain v_n. ∎
So the positivity is open in the weights only vacuously: it is independent of them. It does not couple to 𝔞_T at the sign
step. The only coupling would be the identification of RS_w with 𝔞_T.

## 3. Trap (S): is the identification just EI_002 again? — YES (PROVED for the diagonal, ARGUED for the full kernel)
**Prop 2 (no kernel equals the window form).** For w>1, K_w is continuous on ℝ² (the ζ-values are at abscissa ≥w>1). A
continuous kernel is not a multiplication operator. Hence RS_w(g)≠(1/2π)∫σ_T|F̂|² as forms, for any choice of g=F̂₀D_h
except on a set of tests where both vanish. *Proof.* A multiplication operator with σ_T≢0 is not Hilbert–Schmidt on any
interval; a continuous kernel on compact τ-ranges is. ∎
**Prop 3 (where the window symbol shape appears).** The only diagonal (multiplication-type) contributions to RS_w come from
(i) the residue at w=1, which gives Plancherel ∫|g|²dτ with a constant symbol, and (ii) the constant term of E(·,w) at w=1
(Kronecker limit), which gives, via Maass–Selberg, the symbol −(φ′/φ)(½+iτ)=4Re(ξ′/ξ)(1+2iτ). Its comb is Λ(n)/n at
abscissa 1, not 2Λ(n)/√n. (PROVED from CA_A_001 Cor. 3.)
**Prop 4 (continuation to the window abscissa).** Continuing w→½ puts the ζ-values on the critical line,
ζ(½±i(τ−τ′))ζ(½±i(τ+τ′)), but E(·,w) is no longer positive (for w<1 near 1 the pole term (3/π)/(w−1) is negative), so
positivity is lost. On the near-diagonal τ′≈τ the kernel is ζ(½)²|ζ(½+2iτ)|²-type: second-moment data. Weighted with
|g|²=F̂₀²|D_h|², this is exactly the shape of EI_002 Thm 1, (1/π)∫F̂₀²|ζ-type|²·(symbol). The trap closes.
(ARGUED: the off-diagonal part of the continued kernel is not evaluated.)

## 4. The coordinator's escape criterion
"The Eisenstein/Hecke structure acts on the product test × symbol in a way O1–O8 destroy, and remains true on the
ℓ^∞-ball of radius λ_A/κ_T." Neither half holds:
(a) RS_w acts on g only. The symbol σ_T, which carries the comb, never enters RS_w (Prop. 1). Nothing is destroyed by O1–O8.
(b) Positivity is uniform over all weights (vacuous openness), not openness that carries the sign.

**Result: NO-GO for (e) (Props. 1–3 PROVED, Prop. 4 ARGUED).**
Moves YES→NO: "Rankin–Selberg/Petersson positivity with a minimizer-built test couples to the window form" → NO. The
positivity is test-generic and comb-blind. The symbol that does appear is at abscissa 1 (Prop. 3), and continuing to ½
loses positivity and gives the second moment (S).

## 5. Self-review
- Could g be chosen to depend on the comb, e.g. g=σ_T^{1/2}F̂? σ_T has a negative set U_T≠∅ (phase 192), so σ_T^{1/2} is not
  real there. Writing σ_T=σ⁺−σ⁻ and putting σ⁺ in the test gives RS_w(σ⁺^{1/2}F̂)≥0. That is still a positivity for every
  test, and it says nothing about σ⁻. Dead.
- Prop. 3 is the only place where the comb's log-derivative appears with positivity, and it is at abscissa 1. That points to
  the next seed.
- No sign contact. No negative value for ζ.

## 6. Next seed (proposed, not pre-screened): abscissa transport 1 → ½ with Hecke structure
Maass–Selberg gives an exact positive form whose symbol is the abscissa-1 analogue of σ_T: weights Λ(n)/n, archimedean
part ψ at shifted argument, and positivity for every truncation height Y≥1 (PROVED, CA_A_001). The record's open problem
"(M) propagation P_prof(σ)⇒P_prof(σ′), σ′<σ, at comb level" (L2_027, OPEN; conjugation NO-GO; must not pass through
residues at zeros) asks exactly for a transport from σ=1 to σ=½. Proposal: look for a positivity-preserving operator
on the Eisenstein spectrum that maps the abscissa-1 symbol to the abscissa-½ symbol, i.e. Λ(n)/n ↦ Λ(n)/√n. Candidates:
(i) the Hecke average Σ_n n^{−½}T_n restricted to the Eisenstein part, whose eigenvalue on E(·,½+iτ) is ζ(½+iτ)ζ(½−iτ)…
(this risks (S));
(ii) a Mellin convolution in the truncation height Y with a positive measure (the Y-family of MS inequalities is a cone,
and integrating over Y keeps positivity; whether it can shift the abscissa is the question).
The pre-screen must check O8 coupling (the transport must act on the form, not the comb) and openness. Recorded as the
next seed.
