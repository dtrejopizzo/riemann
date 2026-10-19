# R168_202 — The two never-attacked residues: O-151.4 (summand vs numerator) and Q27 (E_(∞,T))

Phase 168, untried inputs. Pure mathematics, no numerics. Labels: PROVED / PROVED-CITED / ARGUED / OPEN.
No other file edited. No label of record moves. Row D: no label, no sign claimed.

Sources read: R168_001 §1 rows 1, 3; R166_190 §0, Thm A (R166_501), requirements (G)+(N′); R166_405 Q19, Q27;
R166_404 rows 8, 16, 77; R168_102 (single-height wall, Thm 4, Thm 5);
R151_001 §2.4 (T6, Def 2.6, Thm 2.7) and §4 (four-row classification); R151_002 §end (O-151.4 as opened);
R151_005 §2 (reading of record); P122_D_SPECIFICATION §§6–10; P122_014 (graph-determinant curvature = q_T);
R163_901 Thm F (f_t); R163_113 (Hamburger collapse); 00-references/beurling-dmv/README (DMV, BDV).

## 0. Status

| residue | precise question | verdict | label |
|---|---|---|---|
| O-151.4 | Is Hilbert–Pólya positivity on the *summand* side of T6 (and so a restatement), or on the *numerator* side? | **Summand side, and a restatement: the a priori input is the zero bound itself (Thm 1.1).** The numerator side, with Beurling-valid inputs, is capped at the dlVP region (Thm 1.3). Adding integrality and FE puts it on the identification wall (Thm 1.4) | **CLOSED with proof** (PROVED + PROVED-CITED) |
| Q27 / E_(∞,T) | Build the relative correspondence Bohr ⟷ quarter-Γ Calderón with b_∞ in its cocycle, Tate descent, and the two gates of P122.020 | Does not evade the walls. With (E1)+(E3) its hypothesis class is {ζ} (Hamburger), so it sits on the identification wall (Thm 2.2). Its comparison positivity is q_T, so it is a restatement (Thm 2.3). Its constructed part without (E3) is FE-blind (Prop 2.4). All its sign content is the two gates, which are RH-sufficient window statements that the corpus already records | **CLOSED as a route** (PROVED / PROVED-CITED); the gates are OPEN and not new |

Nothing here survives to a build stage. Both residues are closed with proofs, not left open.

---

## 1. O-151.4 — summand vs numerator

### 1.1 Source and the question as it was opened

R151_002 (end) states: "The four-row classification of §4 does not separate row (α) from the additive row:
⟨Hf,f⟩ = Σ_j λ_j|⟨f,e_j⟩|² is itself a nonnegative additive expansion whose 'fibres' are the zeros. Formulate the
distinction that T6 actually uses — the zero-carrying object is a **summand** of the positive form, versus it enters
through a **numerator** — and decide whether a Hilbert–Pólya positivity falls on the summand side … or the numerator
side." R151_005 §2 adds the reading: Deligne's mechanism is numerator-sign (odd cohomology); over ℤ the numerator
mechanism is de la Vallée Poussin, with depth O(1/log γ).

### 1.2 Precise definitions

Fix the explicit-formula normalisation W(g) = Σ_ρ ĝ(γ_ρ), where ρ = ½ + iγ_ρ and the sum runs over the nontrivial zeros of ζ.
W(g) equals the prime side plus the archimedean side.

* **(S) Summand mechanism.** There is a family identity Φ = Σ_{f∈𝔉} w_f·P_f with w_f ≥ 0, P_f ≥ 0 *for free* (by
  construction, independent of where the zeros are). The zeros enter through one summand: the zeros determine an
  analytic invariant of that summand (T6: the abscissa of its Mellin transform). The conclusion is drawn from an a priori bound on Φ.
* **(Nu) Numerator mechanism.** There is a Dirichlet series D(s) = exp(Σ_n b_n n^{−s}) with b_n ≥ 0 (free positivity) such
  that the zeros of ζ are **zeros** of D. For example, D = ζ(σ)³ζ(σ+it)⁴ζ(σ+2it) has
  log D = Σ Λ(n)/(n^σ log n)·(3+4cos(t log n)+cos(2t log n)). Positivity gives |D(σ)| ≥ 1 for σ > 1. A zero of ζ forces D → 0,
  and this contradicts the bound against a pole of controlled order.
* **(Sp) Spectral mechanism.** This is a self-adjoint H whose spectrum is {γ_ρ} and which satisfies a trace formula Tr ĝ(H) = W(g).

### 1.3 Theorem 1.1 (Hilbert–Pólya is on the summand side, and is a restatement). PROVED (Weil criterion PROVED-CITED)

*(a) If an operator (Sp) exists, then for every test g of positive type (g = h * h̃*),
W(g) = Tr(ĥ(H)* ĥ(H)) = Σ_j |ĥ(γ_j)|² ≥ 0.
This is a nonnegative additive family whose index set is the zeros and whose summands are |ĥ(γ_j)|².
(b) Given H, this positivity is free. The existence of H, a self-adjoint operator with this spectrum, is equivalent to RH.
(c) The auditor's form ⟨Hf,f⟩ = Σ λ_j|⟨f,e_j⟩|² is **not** the positivity in question. Its spectrum {γ_j} is symmetric
under γ ↦ −γ, so ⟨Hf,f⟩ is indefinite. The positive object is ‖ĥ(H)f‖².*

*Proof.* (a) Write ĝ = ĥ·ĥ*, where ĥ*(z) is the conjugate of ĥ(z̄). On the real spectrum this is |ĥ(γ_j)|², and the trace
formula gives the identity. (b) "⇒": self-adjoint operators have real spectrum, so every γ_ρ is real, which is RH.
"⇐": under RH, let H be multiplication by γ_j on ℓ²(zeros with multiplicity). The trace formula is then the explicit
formula (convergent for the Weil class). (c) Take f = e_j + e_{j′} with γ_{j′} = −γ_j. ∎

**Consequence (answer to O-151.4).** The Hilbert–Pólya positivity falls on the **summand side**. As in T6(ii), the
"a priori input" that makes the summands nonnegative is the zero bound itself; here it is self-adjointness, which is RH.
T6 is stated for fibre sums over ℤ (Def 2.1 of R151_001), so it does not apply *literally*. Thm 1.1 is the exact analogue
with k removed. §4 row (α) is therefore **not** a positivity mechanism that T6 fails to touch. Its positivity is a
restatement, and its whole content is the *existence* problem "construct H without RH". That problem is MW-5,
already recorded as the identification/object problem (phase 157–158: MW-5 open without an object; adèle class space a restatement).
The §4 table shrinks: row (α) = existence of the object; it is not a sign mechanism.

### 1.4 Theorem 1.2 (where the zeros sit in the three shapes). PROVED

The real axis is **where the zero sits relative to the free positivity**:
- (S): zeros are singularities (poles/abscissae) of a free-positive summand ⇒ a priori bound ≡ zero bound (T6(ii), PROVED in R151_001).
- (Sp): zeros are the **index set** of the summands, and positivity is not free ⇒ ≡ RH (Thm 1.1).
- (Nu): zeros are **zeros** of a free-positive object and are repelled by a pole ⇒ the conclusion holds only where
  free positivity is usable, i.e. σ > 1 (abscissa of absolute convergence of Σ b_n n^{−s}), and it is transported inward.

Proof: the definitions in §1.2 together with T6(ii) and Thm 1.1. ∎ This is the formulation that O-151.4 asked for.

### 1.5 Theorem 1.3 (numerator side with Beurling-valid inputs: dlVP cap). PROVED-CITED (secondary source)

*Let ℳ be any mechanism whose hypotheses hold for every Beurling system 𝒫 with Λ_𝒫 ≥ 0, a simple pole at s = 1, and
N_𝒫(x) = ρx + O(x^θ) with θ < 1. Then ℳ cannot prove a zero-free region larger than σ > 1 − c/log|t|, for any c. In particular, ℳ proves no strip σ > 1 − δ and no RH.*

*Proof.* Diamond–Montgomery–Vorhauer (Math. Ann. 334 (2006)) construct such a 𝒫 whose ζ_𝒫 has infinitely many zeros
on a curve σ = 1 − c′/log t. The construction is restated as §1 of Broucke–Debruyne–Vindas, arXiv 2004.11501, in
00-references/beurling-dmv. The hypotheses of ℳ hold for 𝒫, so the conclusion of ℳ would exclude those zeros, which is a contradiction. ∎
(The DMV primary text was not read, so the label is CITED (secondary). This is the same falsifier as R168_102 Thm 5.)

dlVP itself is of type (Nu) and uses only Λ ≥ 0 and the pole. Thm 1.3 is therefore the proof that "dlVP is capped by
archimedean density" (R151_005 §2.2) cannot be improved inside the numerator shape without new input. This promotes
that statement from "classical, recorded" to a theorem about the shape.

### 1.6 Theorem 1.4 (numerator side with integrality and FE: identification). PROVED-CITED

*Suppose the hypotheses of a (Nu)-mechanism include: support on log ℕ (ordinary Dirichlet series), the Γ_ℝ functional
equation, finite order, and finitely many poles. Then the hypothesis class is {cζ}.*

*Proof.* Hamburger's theorem, in the formulation of Bombieri–Ghosh §1.1 as verified in R163_113. ∎

Any (Nu)-mechanism therefore either keeps a Beurling-valid hypothesis class and is capped (Thm 1.3), or has class {ζ}.
In the second case it is on the **identification wall** (R166_501 Thm A, R166_190 §0): H ⇒ S reduces to "S(ζ)", and the
required input is (N′), which is RH-localised. The intermediate regime (integrality without FE, e.g. Vinogradov–Korobov exponential sums) improves the
region to 1 − c/(log t)^{2/3}(log log t)^{1/3} (PROVED-CITED, classical) but stays inside (N′) and below any strip. This is
the single-height wall R168_102 Thm 4: γ-uniform inputs.

### 1.7 Wall check

| wall | (S) | (Sp) = HP | (Nu) |
|---|---|---|---|
| identification | — | the existence of H is MW-5 (identification) | Thm 1.4 |
| E1 / f_t / M_m | T6 | M_m: zeros on the line plus quartets have no self-adjoint H, consistent | M_m has the same Λ beyond window ⇒ no discrimination; DMV does discriminate |
| W2/M, W-sieve, W-jet | not used | not used | not used (no window, no nodes) |
| (N′) | — | — | Thm 1.3/1.4 |
| single-height (R168_102) | — | — | Thm 1.3 is its Beurling form; Thm 1.4 is its integral form |

**O-151.4: CLOSED with proof.** HP is on the summand side and is a restatement (Thm 1.1). The numerator side is capped
(Thm 1.3) or identifies ζ (Thm 1.4). Thm 1.2 records the real axis. There is no residue specific to O-151.4.

---

## 2. Q27 — the relative correspondence E_(∞,T)

### 2.1 Source: what was specified

P122_D_SPECIFICATION §7. The finite-place subobject is
D^fin_{T,sf} = (L^∞(𝕋^{S_T}) ⋊_α ℝ, τ_{S_T}, D_α, P_+, c_{S_T}, {L_p, L_p^∨}_{p∈S_T}).
It has a Kronecker log-flow, a semifinite trace, a Hardy projection, relative Euler scatterings, and local graph-determinant lines.
"A full object must enlarge (7.1) by a relative correspondence E_(∞,T)" with the following requirements:
- **(E1)** left boundary: the semifinite Bohr module; right boundary: the quarter-Γ Calderón module;
- **(E2)** the relative cocycle contains b_∞;
- **(E3)** it descends both Tate constraints (the functional equation);
- **(E4)** equality-state anomaly cancellation. By §8 (P122.019–020) this is made precise as **Gate R**: a critical Calderón trace
  theorem putting the completed incoming current in H^{1/2}(I_T);
- **(E5)** **Gate S**: horizontal gluing. Zero incoming trace identifies two distinct active prime fibres before the scalar supertrace;
- **(E6)** comparison with B_nuc ("proved last").

P122.020 states: (E4)+(E5)+P122.002 ⇒ row (d).

### 2.2 Why it was never built (record)

Each partial build stopped:
- P122.014: adding the known Γ Gram column gives virtual curvature exactly q_T, so positivity = row (d).
- §9 / P122.022: the archimedean relative determinant D^rel_∞ exists, but "the symmetric mixed cocycle still vanishes by
  parity" (cf. P122.018, parity no-go). There is no morphism between the finite and infinite sides.
- P122.025: the finite residue determinants have no log p anomaly. The anomaly lives only at the infinite Γ end.
- P122.027: the path-vector Gram log min(p,q) has mixed terms absent from row C.

After phase 122 the program moved to other fronts, and no phase returned to the contract (R166_404 row 16).

### 2.3 Precise question

Does there exist a correspondence E satisfying (E1)–(E6) such that (E4) and (E5) are proved as structural theorems, not postulated on the radical?

### 2.4 Theorem 2.2 (identification). PROVED-CITED

*Let E satisfy (E1) and (E3). Its finite side is built over the actual prime set with weights (log p)p^{−k/2}, i.e. on an
ordinary Dirichlet series. Its Tate descent imposes the Γ_ℝ functional equation. Then the class of zeta data that
E admits is {cζ}.*

*Proof.* The Euler data of (7.1), cofinal in T, determine −ζ′/ζ as an ordinary Dirichlet series on ℕ. (E3) gives the Riemann
FE, and finite order with one pole is part of the specification (completed incoming current). Hamburger's theorem applies (R163_113). ∎

So the hypothesis class H of the mechanism (H, S = row (d)) is {ζ}. By R166_501 Thm A, the mechanism gives no reduction:
proving (E4)+(E5) for E is proving facts about ζ itself, and (N′) is required (R166_190 §0). This is the
**identification wall**.

### 2.5 Theorem 2.3 (comparison ⇒ restatement). PROVED

*Suppose the positivity output of E is the curvature of a determinant line on the primitive window space V_T. Suppose
also that (E6) holds as an identity of Hermitian forms, Θ_E = −B_nuc,T = q_T. Then "E semipositive" ⟺ q_T ≥ 0 ⟺ row (d) at T.*

*Proof.* P122.014 (1.3)–(2.4): the graph-determinant functor returns the Gram form, curvature is additive under ⊗,
and duality changes the sign. Under (E6) these give Θ_E = q_T. ∎

Hence the only non-restatement content of E is (E4)+(E5) used as an **inequality-producing** route (P122.020), not E's
own curvature.

### 2.6 Proposition 2.4 (the constructed part is FE-blind). PROVED

*Every component marked "constructed" in the P122 table is defined verbatim for any finite prime set S, not only S_T:
the Bohr algebra, the Kronecker flow, the trace, the Hardy projection, c_S, L_p, the port swap, D^rel_∞, and the affine
relations V_pS = S^pV_p, e^{−βH}V_pe^{βH} = p^{−β}V_p.*

*In particular they are built identically for the deleted datum S_T∖{p_0}. That datum is the Euler data of
ζ·(1−p_0^{−s}), which has zeros on Re s = 0 and no Riemann FE.*

*Proof.* Each definition in P122.013/.016/.022/.024 uses only the individual primes p ∈ S and the archimedean place, and
never uses completeness of S. ∎

Without (E3), E cannot tell ζ apart from deletions, whose zeros are off the line (R166_103: the deletion has the same
𝒯^new). With (E3), Thm 2.2 applies. This is the pinch: **blind or identification**.

### 2.7 Wall check for the gates

(E4) and (E5) are defined on the window I_T (P122.020). For T below the agreement height of f_t (R163_901 Thm F), the
Weil form is the same for ζ and f_t. However, f_t has no Euler fibres on log ℕ, so (E5) is not even defined for it. The gates
are therefore integrality-dependent window statements whose cofinal conjunction implies RH. This is exactly (N′):
control of Λ beyond every fixed window with zero-localising strength. P122.021 has already shown that (E4) is not generic
regularity, because sharp-window translation destroys the endpoint class. The walls W2/M, W-sieve, and W-jet are not reached, because E has no
node set (R166_404 row 16: "not global in X"). Hence E also fails (G).

**Q27: CLOSED as a route.** Thm 2.2 (identification) + Thm 2.3 (restatement) + Prop 2.4 (blindness). Gates R and S
remain recorded RH-sufficient OPEN statements (P122.020), not new and not reopened.

---

## 3. Ledger

| item | statement | label |
|---|---|---|
| Thm 1.1 | HP positivity = nonnegative family over zeros; its input (self-adjoint H) ⟺ RH; ⟨Hf,f⟩ indefinite | PROVED (Weil criterion PROVED-CITED) |
| Thm 1.2 | the true axis: zero as singularity of a summand / index of summands / zero of a free-positive series | PROVED |
| Thm 1.3 | numerator shape with Beurling-valid inputs capped at the dlVP region | PROVED-CITED (DMV, secondary source) |
| Thm 1.4 | numerator shape with integrality + FE has class {ζ} | PROVED-CITED (Hamburger) |
| Thm 2.2 | E_(∞,T) with (E1)+(E3) has class {ζ} | PROVED-CITED (Hamburger, R163_113) |
| Thm 2.3 | E's comparison positivity = q_T | PROVED (from P122.014) |
| Prop 2.4 | constructed part of the P122 contract is FE-blind (deletion) | PROVED |
| Gates R, S | RH-sufficient window statements | OPEN (record, P122.020) |
| O-151.4 | — | **CLOSED with proof** |
| Q27 / E_(∞,T) | — | **CLOSED as a route with proof** |

Grid action proposed for the editor: R166_404 row 8 and row 16, and R166_405 Q19 and Q27, become CLOSED, citing this file.
Row 77 gains the note "(Sp) = summand side, Thm 1.1". (★_cell) and row D remain OPEN.
