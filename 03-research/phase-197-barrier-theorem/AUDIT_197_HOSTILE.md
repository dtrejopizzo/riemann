# AUDIT_197_HOSTILE — audit of BARRIER_001 (phase 197)

Checked against Paper 47 main.tex (lem:degen l.3252, lem:shape-scale, prop:shape-eulerdel,
lem:shape-epstein (O10), lem:shape-margin, lem:shape-lin, prop:shape-inputs, thm:D1, §spec, minimizer existence l.555) and the index
(README l.404–405 INV_P/INV_Q, l.421 BARRIER_001; AUDIT_PHASE193_CERTAINTY rows O10/O11). no
equivalence with anything else is used.

## Key structural observation (overrides several items)
By window collapse, every uniform method at T is decided iff π_N S ⊆ K_T := {x∈ℝ^N : μ_T(x) ≥ 0}, with μ_T the concave function of
lem:degen. K_T is a **convex** superlevel set (PROVED, lem:degen concavity). Theorem 5's H_T is just the supergradient half-space
containing K_T. Consequences: (1) "separating Λ from a_P" at window T means separating π_NΛ from π_N a_P = 0 (P>N) in ℝ^N, which
requires no functional equation; (2) 0 and a_P (P>N) are the *same* point of ℝ^N, hence the same falsifier.

## (a) Method class — PARTLY SOUND, mislabelled "trichotomy"
- Def. 1 is broad enough (any S∋Λ, any sound Ψ) and Ψ=λ_A(T;·) shows it is not too narrow. "Uniform = Ψ constant" is non-vacuous:
  it encodes "premises ⇒ WP_T", decided iff π_N S ⊆ K_T.
- But Theorem 3 only covers uniform ∪ 𝓛_lin; every non-affine estimate is relegated to door (D2), so the theorem says nothing about
  the bulk of conceivable proofs. Must be stated as a restricted classification, not a barrier for "row-D methods".
- "Exactly one holds" is FALSE: an 𝓛_lin method whose S contains a_P is in (i) and (ii). Replace by "at least one".
- (ii) is not an obstruction: Ψ(Λ) ≤ λ_P and λ_P's sign at T ≥ 0.60 beyond the certified windows is unknown. Label (ii) as
  "reduces to the dual program", not as a failure mode.

## (b) Lemma 2 — (a) FALSE as stated; (b) ARGUED (inherits O10); (c) PROVED/CITED; (d) not exhaustive
- (a): prop:shape-eulerdel PROVED that a_P breaks only FE *among def:shape-class*. The catalogue omits **support/prefix atoms**:
  e.g. A4 ∧ "support contains every prime" forces a=Λ (Euler product with a(p^k)=log p on all p) without any FE; "a(2)=log 2"
  alone excludes π_N a_P = 0. Neither is type P nor A1–A9, and a_P ∉ S. So "no P atom ⇒ a_P∈S" is false. Fix: add type P′
  (support / prefix value atoms); prefix atoms on fewer than all window primes fall to O_5/O_4^ε, which are CONDITIONAL (κ_T≠0,
  c_{F⋆}(log n₀)≠0) — so Lemma 2 becomes CONDITIONAL for these conjunctions.
- (b): Ξ_Q is CITED (Weil 52 + Davenport–Heilbronn) only for the **complete** window form, negative "at some window and all larger";
  the primitive bottom λ_A on P_T is ARGUED (lem:shape-epstein, last sentence; AUDIT_193 row O10 = CIRC). Theorem 3 uses λ_A(T;f) at
  the given T. Hence case (b) and every (i)-kill via Ξ_Q: ARGUED (inherits O10 circularity), and even the complete-form kill is not
  located at each T ≥ 0.60.
- A2 ∧ loose-FE sub-case: invokes Ξ_Q or a Beurling Γ(s/2)^c system = O10-primitive/O11, both ARGUED/CIRC. ARGUED, correctly
  labelled, but it is circular in the AUDIT_193 sense.
- (c): window Euler/𝒞_1 by Möbius PROVED; A4 ∧ ζ-FE ⇒ ζ by Hamburger CITED (prop:shape-inputs(iv), Titchmarsh §2.13 — needs finite
  order, which the atom must include). "Exact thm:Z on all flat-top tests" is NOT a comb-pinning atom: it is a restatement of the
  target (lem:shape-restate); remove from P (it is REF-D as a premise).
- A8: "a_P is an integral Beurling system" PROVED; but Beurling *falsifiers* are O11 ARGUED, so A8-kills are CIRC.

## (c) Theorem 3 for T ≥ 0.60 — CONDITIONAL/ARGUED, not PROVED
Proof correct for A1–A7 conjunctions without prefix/support atoms (a_P route, PROVED via cor:Tarch). Downgrades: (i)-via-Ξ_Q ARGUED;
prefix atoms CONDITIONAL; "exactly one" → "at least one". Remark (½log2, 0.60): correct — cΛ large fails for T>½log2 (lem:shape-scale,
PROVED; kΛ with k∈ℕ also, so A3 covered); a_P and 0 do not fail there (λ_P^inf ≥ 0 below 0.60 is what cor:Tarch's threshold says
only in one direction — the memo should say "are not known to fail", not "do not fail").

## (d) Proposition 4 — minimality FALSE for {a_P, 0}; cΛ item to be rewritten
- 0 and a_P (P>N) coincide in ℝ^N (window collapse): the generators are not independent; drop 0 as a separate generator.
  The "0" item's class A3(𝒞_01) without pole also contains a_P, so 0 is not its only falsifier.
- cΛ item, clean version: S = {cΛ : c>0} (A2 ∧ "a(p^k)/log p independent of p,k"). Contains Λ and no a_P, Ξ_Q. Falsified by c large
  for T>½log2 and c small for T ≥ 0.60 (lem:shape-scale, PROVED). If c ∈ (1−ε,1+ε) only, falsifier O_4^ε CONDITIONAL on κ_T≠0.
  Delete the garbled "shows O_4 cannot be dropped below 0.60? no:" sentence. Require c>0 explicitly (c=0 is the zero comb).
- a_P item: PROVED. Ξ_Q item: CITED complete form / ARGUED primitive. "Minimal forcing set" claim: ARGUED only.

## (e) Theorem 5 — inequality PROVED; consequences OVERSTATED
- Existence of F⋆: λ_A = min spec H_T is attained (Paper 47 l.555, compact resolvent); a real minimizer exists (real part or
  imaginary part of a minimizer is one, the form being real). PROVED. Uniqueness: NOT known; H_T depends on the choice — state
  π_N S ⊆ ∩_{F⋆} H_T(F⋆).
- Direction: lem:degen gives μ_T(v) ≤ μ_T(v⁰) − Σ(v_n−v⁰_n)c_{F⋆}(log n); with v_n=a(n)/√n this is λ_A(T;a) ≤ λ_A(T;Λ) − ⟨a−Λ,w_T⟩.
  Soundness + Ψ≡c≥0 ⇒ ⟨a−Λ,w_T⟩ ≤ λ_A(T;Λ). CORRECT. Note lem:degen's inf is over P_T ∩ D_T; same value (form domain) — fine.
- It is an immediate corollary of lem:degen (a supporting half-space of the convex set K_T); "new" is overstated — it is the
  multi-direction form of O_5 (lem:shape-weight).
- Margin bound: lem:shape-margin(i), inputs CITED (Platt–Trudgian) — label "PROVED, inputs cited", not PROVED.
- "Pinned to precision e^{−15.4T}" requires |w_T| bounded below; in the degenerate case w_T=0 (lem:degen: not known not to occur),
  H_T = ℝ^N and Theorem 5 is vacuous. CONDITIONAL on w_T≠0.
- "a_P, cΛ, 0 are outside H_T at T ≥ 0.60" is UNPROVED: they lie outside K_T (PROVED), but outside H_T needs
  ⟨a−Λ,w_T⟩ > λ_A(T;Λ), i.e. sign information on Σ_n Λ(n)c_{F⋆}(log n)/√n = κ_T-type quantity — CONDITIONAL (same as O_4^ε/O_5).

## (f) Admissible class D1/D2 — D1.a FALSE; D2 well-posed only after fixing Δ_T; borderline retry
- (D1.a) "separating Λ from a_P forces the global FE at conductor 1, PROVED": FALSE at window level (π_N a_P = 0; any prefix atom
  separates). The FE is forced only for atoms that are *global* properties invariant under prime deletion — a restriction the memo
  did not state.
- (D1) "Δ_T a functional of π_N a built from the global FE" is internally inconsistent: a global FE is not a function of π_N a.
  Either Δ_T reads the full comb (then the inequality must hold fibrewise, i.e. inf over a's with given π_N a), or it reads π_N a
  only (then it is a description of the convex set K_T and is REF-D in coordinates).
- (D2) λ_A(T;a) ≥ −C_T Δ_T(a) on Euler combs near Λ with Δ_T(Λ)=0: at a=Λ this *is* WP_T(Λ); it is a strengthening of the target,
  not REF-D, but ill-posed until Δ_T, "near", C_T are fixed. Candidate Δ_T = D_{S_N} defect is the INV_P_001/INV_Q_001 object
  (index l.404–405: low-band separation ARGUED, (Π_L)=REF-D, PW/Bernstein/Nehari on log|ξ_S/ξ_S(1−s)| not to be retried). A signed
  stability inequality for the bottom is new as *form* (no index entry for "Łojasiewicz/stability Hamburger"), but any concrete Δ_T
  from D_{S_N} is a retry of INV_P/INV_Q unless a new reason is written. Label: OPEN, near-retry flag.
- "Quantitative Hamburger with a sign in direction w_T": well-posed only as: for Dirichlet series a over ℕ with Euler product,
  finite order, π_N a ∉ K_T ⇒ FE-defect ≥ δ_T > 0. Not REF-D (it is a rigidity statement about non-ζ series), but its interest
  is conditional on w_T≠0 (degenerate case) and on the FE being genuinely needed (see D1.a).

## Label corrections (summary)
Lemma 2(a): FALSE as stated → CONDITIONAL after adding P′ atoms. Lemma 2(b): CITED → ARGUED (O10 primitive). Lemma 2(c): PROVED/CITED,
remove thm:Z atom. Theorem 3: PROVED → ARGUED/CONDITIONAL; "exactly one" → "at least one". Prop 4: minimality FALSE for 0 vs a_P;
cΛ item rewritten. Theorem 5: half-space PROVED (corollary of lem:degen, inputs cited for the margin); localisation consequences
CONDITIONAL on w_T≠0 and κ-type signs. D1.a: FALSE. D2: OPEN, ill-posed until Δ_T fixed, near-retry of INV_P/INV_Q.
No sign obtained. Row D: OPEN.
