# R158_004 — Audit of R158_002 (the adèle class space as an MW-5 object), phase 158

Object: `R158_002_ADELE_CLASS_FOLIATION.md`. Every claimed `PROVED` item was re-derived,
and every citation was opened at its place. No paper, README or R158_001 was touched. Amendments A1–A25 are applied in
place to R158_002, each marked "[amended per R158_004]", with struck text kept. A pre-audit copy is in the scratchpad
scratchpad. **No sign is claimed, asserted or suggested. Row D: no label; the endpoint of record is unchanged.**

**Sources opened this review.**
* Meyer math/0412277: local source; l.139–215, 290–360, 580–745, 1184.
* CCM math/0703392: full text; Thm 4.16, (4.40)–(4.45), Lemma 4.17, Rem 4.18, §5, Thm 6.1, (6.2)–(6.12), Prop 6.2,
  Cor 6.3, Prop 6.4, §7.1, Def 7.1, Prop 7.2, (7.6)–(7.8).
* Connes math/9811068: full text; introduction l.50–108, Thm 1 and the Jordan remark l.574–645, (18) l.499–505 and
  l.2000, Thm 5 l.1960–1990, number-field paragraph l.2205–2215, Remark d l.2370.
* Leichtnam 1307.3851: local source; §2 eq. (6) l.375–425, axioms 3]–8] l.1000–1110, Comment 6.
* CCM 2310.18423: title and abstract, local PDF.
* P46 `main.tex` l.114–150 (`eq:symbol`, `eq:form`, `eq:W`) and l.750–765 (`lem:roughEF`).
* P47 `main.md` (11.6) l.2136, (18.2) l.4826, Thm 20.37–20.38 l.8480–8530, §21.7 l.9327–9390, (X19) l.4019,
  (X25a) l.4027.
* `ROW-D-REDUCED-STATEMENT.md` §1.
* Corpus: phase 63 (README, R1-VERDICT), phase 62 E94 (`E94_RESULTS.md` l.8, `E94_Jcompat.py` l.30–34), phase 64
  `RESULTS.md` Task D, MAP_1 NG-63, MAP_3 rows 62–63, 106.156/106.157, 107.204, 114 D.37/D.39/D.191, R157_002 row 60,
  R157_004 M5.
* R158_001 and R158_003 (both final), read only.

## §1 Verdict table

| # | item (R158_002) | verdict | fix |
|---|---|---|---|
| 1 | **Lemma A** (i) | **CORRECT**, and a dimension count: 0-dimensional leaves carry no 1-forms | A2, A9: scoped to `C_Q` |
| 1′ | **Lemma A** (ii), doubt 7 | **CORRECT, and coefficient-independent.** Cartan: `L_V = d_𝓕ι_V + ι_V d_𝓕` with `V` tangent to the orbit leaves, so `Θ = 0` on orbit-foliation `H^•` for every coefficient space stable under `V`. Only the size of `H¹` depends on the coefficients | A9 |
| 1″ | **Lemma A** (iii) | **Not a consequence** of (i)–(ii). It is CCM §5's analogy. In that analogy `C_K` plays the *hypersurface* `Y`, so "open stratum" is not CCM's picture. "On `X`" beyond `C_Q` is ANALYSIS: no leafwise complex on `X ∖ C_Q` exists in the sources | A2, A9 |
| 2 | **Fact 2.4a**, doubt 8 | **CORRECT.** Checked against Meyer Thm "Lap_range" l.653, including the line `Re s = ½`, where both quotients are the Γ-part. The functionals `h^{(j)}(ρ)` kill `I` by Meyer's parenthetical (no poles of `h/ζ`). The matrix is triangular. **Notation clash:** Meyer's `ξ = π^{−s/2}Γ(s/2)ζ(s)` has poles at `0, 1`, while R158_002's `ξ` is Riemann's entire one. Meyer's eigenvalue statement is about `ᵗD_-` | A10 |
| 3 | **Lemma D**, identity | **CORRECT**: `σΘσ^{−1} = 1 − Θ`, and `I` is `σ`-stable | — |
| 3′ | Lemma D, realiser | **WRONG attribution.** `σ` is Meyer's `J` (`(Jf)^(s) = f̂(1−s)`, l.594), not `J𝓕`. `𝓕J` has multiplier `γ(s)` and does **not** descend (corpus 114 D.39 §§3–6). The identity quoted from Meyer's proof is the functional equation on `Z𝓗_∩` | A13 |
| 3″ | Lemma D, "the only involution intrinsic to `X`" | **UNPROVED** (complex conjugation is another, antilinear one); struck | A3 |
| 4 | phase-63 reading, doubt 6 | **Identification wrong, conclusion right.** Phase 62/63's `J e_n = sgn(n)e_{−n}` has `J² = −1`, so it is not `σ`. It factors as `J = σ∘(i⋆_win)`, where `⋆_win` is the Hilbert transform on the window, i.e. Construction C's `⋆`, which commutes with `D_log`. The ratio 2.000 comes from the `σ` factor, i.e. Lemma D. Phase 64 Task D already proves this parity lemma *for this `J`* | A14 |
| 4′ | "does any corpus statement extend 'no J-linear Frobenius'?" | **No theorem does.** MAP_1 NG-63 ("for this specific construction") and R1-VERDICT ("does not prove no Frobenius exists in a larger/true … realization") are correctly scoped. **Overreaching phrasings**, J-specific but unscoped: "the wrong type to be Frobenius" (R1-VERDICT; MAP_3 l.232; R151_001 l.553; CORPUS_CHECK_R145 l.22), and MAP_3 row 63 "PROVED-IMPOSSIBLE" with "over-generalized? No". Reported, not edited | A15 (recorded in R158_002) |
| 5 | **Construction C** | **CORRECT and trivial**: generalized eigenspaces are preserved, and `⋆` commutes with conj and `Θ`. **OT-3 fails for `⋆`:** it is the spectral splitting, and it is undefined on the topological `H¹` (there is no holomorphic "sign of `Im s`"). Zero-free only on the window, as the Hilbert transform. Precedent: 106.157 (`J = i`, `Θ^†+Θ = I`). The table row "zero-free definition" held for `B_{Φ₀}`, not for `⋆` | A15 |
| 6 | Fact 4.6a.1–6 | **CORRECT**, re-derived: well-definedness; cup relation `B(sa,b)+B(a,sb) = B(a,b)`; alternation under `s ↦ 1−s`; `⋆`-isometry; isotropy of `H^{1,0}`; `S(h,h) = 2iB(a,ā)` | — |
| 6′ | **Fact 4.6a.7** | **FALSE as stated** (with `Φ` even). Compatible forms on `E_ρ×E_{1−ρ}` and `E_{1−ρ}×E_ρ` are independent. **Counterexample: CCM's trace pairing**, `h(a,a′) = Σ m_ρ a(ρ)\overline{a′(1−\barρ)} = B_{ξ′}(a, ā′)`, whose multiplier `ξ′` is odd, so the form is symmetric and compatible. Corrected: every compatible form is `B_Φ` with `Φ` arbitrary entire; even ↔ alternating, odd ↔ symmetric | A4, A16 |
| 7 | **Lemma E**, doubt 3 | **CORRECT for even `Φ`.** Sign computation verified: `ē_ρ(1−s) = ξ(s)/(ρ−s) → −ξ′(ρ) = iΞ′(γ)`, with `Ξ′(t) = iξ′(½+it)`, so `iB = −Φ(ρ)Ξ′(γ) ∈ R`. The off-line block `[[0,c],[c̄,0]]` and the Jordan isotropy `H(w,w) = (1−2Reρ)H(v,w)` are correct. **Reach:** the off-line and Jordan cases use only compatibility, so "definite ⇒ RH ∧ SZ" holds for every compatible hermitian form, CCM's included. That is Lemma U, i.e. classical. Only the sign clause is `B_Φ`-specific; for odd `Ψ` it reads `iΨ(½+iγ)Ξ′(γ)` of constant sign (CCM: `Ξ′² > 0`). The hypothesis `Φ(ρ) ≠ 0` is superfluous for necessity. The lemma uses nothing arithmetic, so it holds verbatim for `Ξ_Q` | A4, A17 |
| 8 | **E-i** | **CORRECT; the numerical import is unnecessary and was miscited.** Unconditional proof: definite ⇒ RH ∧ SZ ∧ constant sign of `Ξ′(γ)`, but under RH ∧ SZ, `Ξ′` alternates at consecutive zeros (at least two exist). P47 (X19) certifies `γ₁` and excludes `|Im| ≤ 21`; it does **not** cover `γ₂ = 21.022…`. Canonicity: the conclusion is robust under positive-on-the-line multipliers (`e^g`, `g` even and real), but `B_1` is not a positivity candidate of any source. CCM's `h` is the canonical one | A5, A18 |
| 9 | **E-ii** | **CORRECT.** `Σ m_ρ(ρ−½)a(ρ)b(1−ρ)` holds for all multiplicities; semidefinite ⟺ RH. Identity: `B_{Φ₀} = B_{ξ′}((Θ−½)·,·)`. Orientation: negative semidefinite with this `⋆`. **Precision:** the zero-free "geometric side" includes the pole terms `g(0)+g(1)`, and applying Meyer's identity (proved for `C_c^∞`) to `g = (s−½)a(s)b(1−s)` needs its continuity extension: ANALYSIS | A19 |
| 10 | **Prop H**: Jensen step | **CORRECT.** `n(r) ≤ ∫_r^{er} n(t)dt/t ≤ log M(er) − log|G(0)| ≤ eτr + O(1)`, against `n(r) ≥ N(r) − 1 ≍ (r/2π)log r`. Paley–Wiener–Schwartz is correct. The conclusion is independent of the representing `Φ` (all share the sign pattern), and it holds for odd `Ψ` too | A21 |
| 10′ | Prop H: "not a finite product of local factors and Γ-data" | **NOT PROVED by the stated argument**: `Γ` and `1/Γ` are of infinite type. Replaced by a zero-count statement: `O(T)` zeros on the line for finite Euler polynomials × `1/Γ(as+b)` (`a, b` real) × `e^{poly}` | A21 |
| 10″ | "finite-window datum" vs P46 windows | **Consistent once stated.** The datum is the *multiplier*, not a P46 test. P46's `W_T` is CCM's form (infinite-type multiplier `ξ′`) on tests in `I_T`. The analogy with `thm:finZ` is ANALYSIS | A21 |
| 11 | **Lemma U** | **CORRECT; content CLASSICAL.** (a)⇒RH is Serre's argument (Leichtnam §2 eq. (6), l.401–422; Comment 6, "the first six Assumptions imply the Riemann hypothesis"; corpus 114 D.37 Thm 2.1 and §4; 106.157 (18)). The Jordan part is Connes 1999 l.642–645: "When the zeros of L have multiplicity … D is not semisimple and has a non trivial Jordan form … compatible with the almost unitary condition (22) but not with skew symmetry for D". (b)⇒(a) is linear algebra. `c = ½` is verified with Meyer's `λ_t f(x) = f(t^{−1}x)`, so `ρ_-(λ)e_ρ = λ^ρ e_ρ`. **Reach (doubt 2):** necessity restricts to the invariant subspace `H¹_alg`, so it holds on `H¹` and on every completion into which `H¹_alg` injects. Density of `H¹_alg` (`I` = its hull ideal) is **open**, and possibly RH-adjacent (lower bounds for `|ζ|`). Residue forms vanish on `J/I` | A6, A22 |
| 11′ | R158_000's point (2): Connes' Jordan blocks vs Lemma U | **They agree.** Lemma U's Jordan step is Connes' remark, made on Meyer's `H¹` with all zeros; R158_003 1″ records the same. Lemma U is not novel (earlier Lemma T note) | A6 |
| 12 | **function-field remark**, doubt 5 | **The example is real** (PROVED, classical): `y² = x³ − x` over `F_{p²}`, `p ≡ 3 mod 4`, has `π_p² = −p`, `Frob_{p²} = [−p]` scalar on `H¹_ét` and `Z = (1+pu)²/((1−u)(1−p²u))`, hence double zeros on the line. **The adelic Jordan block** in characteristic `p` is **ANALYSIS**: CCM Thm 4.16 gives the multiplicity; cyclicity (`C[u^{±1}]/(P)`) is not verified in a source | A20 |
| 12′ | a **stronger falsifier** (new) | `K/Q` Galois with group `S₃`: `ζ_K = ζ·L(sgn)·L(ρ)²` (P47 X25a). `L(ρ)` is an entire Hecke `L`-function with infinitely many zeros, so `ζ_K` has infinitely many zeros of order `≥ 2`: PROVED classically. On `X_K`'s trivial sector the Lemma U structure therefore **cannot exist, whatever RH says**, modulo the `K`-analogue of Meyer's Laplace-range theorem (cyclicity; ANALYSIS). With T1, field-uniform unitarity routes prove something false. N-b now rests on this | A20, A24 |
| 13 | **Prop B** normalisations, doubt 1 | Structure correct; **three corrections.** (a) The map is **exactly** `F(t) = e^{t/2}g(e^t)` with CCM (4.40), (6.9): `(g^♯)^(s) = \overline{ĝ(1−\bar s)}` and `g⋆g^♯(1) = ‖F‖²`, with no extra `Δ^{±1/2}` (Prop 6.2's `Δ^{−1/2}` is `W ↔ ϑ_m`, absorbed in Cor 6.3). (b) `Z•_trans Z = 2Re(A\bar B) − W_T = −𝔞_T`: **sign error** in R158_002. (c) Over `Q`, `log|a| = −log D = 0`, so CCM's `Δ•Δ` term vanishes. P46's `C₀ = ψ(¼) − log π` sits inside the archimedean principal value, not in `Δ•Δ` | A12 |
| 13′ | "Prop 7.2 = P47 (18.2) = E6" | **WITHDRAWN.** Over `Q`, (7.6) ⟺ `W_T(F) ≥ 0` test by test: E1 in Castelnuovo form (fibre classes). P47 (18.2) is Hodge index against `K`: `I_∞(F,K) = ½(Φ_F(0)+Φ_F(1))`, `I_∞(K,K) = ½`, so it reads `W(F) ≥ −½(Φ_F(0)−Φ_F(1))²`, strictly weaker per test and equal on even `F`. The two are equivalent only globally. Also: Cor 6.3 is for all Grössencharaktere; its trivial-sector restriction is Weil's criterion for `ζ` (Weil; P45 Thm 10.4), not a CCM statement | A7, A12 |
| 14 | citations | **Verified verbatim:** Connes Thm 1 (multiplicity `n < (1+δ)/2`), Thm 4 (S-local), Thm 5 (char `p`; number fields by stated analogy l.2215, no proof: doubt 4 confirmed), (18) isometry, Remark d; CCM Thm 4.16 ("all zeros contribute … natural multiplicity"), (4.41), Rem 4.18, Thm 6.1, Prop 6.2, Cor 6.3, Prop 6.4, §7.1, Prop 7.2; Meyer Thm "Lap_range", Cor "Dminus_eigenvalues", the character statement l.176–203. `ξ ∈ 𝒪` and `ξ ∈ I` confirmed | A10, A11 |
| 15 | R158_000's point (1): OT-2 | **Accepted, with a nuance.** OT-2 **fails** on Connes' Hilbert-space realisation (the global trace formula ⟺ RH). It **passes** on the Meyer–CCM nuclear `H¹`, where Meyer's character identity, equated with the spectral side, gives the classical explicit formula. That is not Connes' global formula, and it costs the Hilbert structure (114 D.191: the critical Plancherel completion is zero). "Fails only OT-5′" is struck | A1, A11, A24 |
| 16 | R158_000's point (3): OT-4/OT-5 | **Accepted.** "Pass by undefinability" is struck. `Ξ_Q` has a Meyer-type nuclear quotient (lattice Poisson), on which Lemmas D, E, U, C and Prop H hold verbatim. The break is the Euler-product line of Meyer's character computation (l.1184), a named line. OT-5 passes vacuously and excludes nothing by itself | A1, A23 |
| 17 | exhaustiveness, doubt 9 | **Five candidates added, none escapes.** (i) CCM's hermitian trace form without `⋆`: 4.3, RESTATEMENT. (ii) Bost–Connes KMS states and the modular Hamiltonian `log n`: positive and zero-blind (they see `ζ(β)`, `β > 1` real). (iii) The dual trace on the II_∞ factor: Weil is the *difference* `Tr_X − Tr_Y` of positive traces (CC 1805.10501 l.887), so its positivity is the trace pairing: RESTATEMENT, compression family. (iv) ζ-cycles and prolate operators (2106.01715, 2310.18423): F3 per `L`/`S`, the limit is EQUIV (R157 row 60, M5). (v) The critical Plancherel completion: void (D.191). Exhaustiveness stays ANALYSIS | A23 |
| 18 | **corpus check** (working rule) | **FAILED to find** phases 106 (106.156/157: CCM Rosati pseudo-polarization, `J = i`, `Θ^†+Θ = I`, "an indefinite Hermitian form also satisfies …"), 107.204 ("Meyer supplies … not Hodge positivity"), 114 D.37 (polarization ⇒ unitarity ⇒ RH on Meyer's quotient), D.39 (`𝓕J` does not descend), D.191 (Plancherel completion void), and 64 Task D (parity lemma). The results agree with them; the novelty of Lemma U and Construction C is reduced to zero | A8 |
| 19 | **N-a / N-b / N-c** vs R158_001 and P47 | **N-a** is consistent with OT-5′ and §21.7 (`deg = #ker`, "must deliver the count, never the positivity", l.9387); "leaves of dim ≥ 2" is HEURISTIC (it holds only for the harmonic-norm option). **N-b** is scoped to the P-HS / (D3) route. The P-HI/Rosati route needs only semidefiniteness, which tolerates Jordan tails (E-ii, CCM). "Non-cyclic ⟸ `+`" is HEURISTIC: §21.7's `+` is about the effective cone. N-b is not on R158_001's OT list and is proposed as an OT-1 clause. **N-c** = P7/OT-9, and must carry R158_003 A12/A15: the constructive clause is RH-strength. §4.4's "must read zero data (W1)/(W2)" becomes "carry information outside `(a,b,deg,R)`": reading (W1)/(W2) fails OT-3, proving them is the problem (Thm 20.38) | A24 |

## §2 Answers to R158_002's doubts

1. **Normalisations.** Resolved (row 13).
   * `F(t) = e^{t/2}g(e^t)` is exact.
   * `•_trans = −𝔞_T`.
   * `log|a| = 0` over `Q`; `C₀` is archimedean principal-value normalisation.
   * E1 ↔ Cor 6.3 holds for real tests. E6 ↔ Prop 7.2 is withdrawn: Prop 7.2 is E1 test by test.
2. **`H¹_alg` vs `H¹`.** Resolved on the necessity side: restriction to an invariant subspace needs no density. Open
   on the sufficiency side: density of `H¹_alg`, i.e. spectral synthesis for `I`. Residue forms see only `H¹_red`.
3. **Canonicity of `B_1`.** The sign computation is correct. The alternation needs simplicity and consecutiveness, but
   E-i needs neither once Lemma E is used (A18). The canonical positivity candidate is CCM's `B_{ξ′}` form, which
   4.6a.7 had excluded (A16).
4. **Connes Thm 5.** Confirmed. It is proved in characteristic `p`; for number fields there is only the sentence
   "This gives the analogue of Lemma 1, Theorem 5, and Lemma 3" (l.2215).
5. **Function-field remark.** The curve example is genuine. The adelic Jordan block is ANALYSIS. The `S₃` number field
   gives a stronger falsifier (A20).
6. **Phase 63.** `J = σ∘(i⋆_win)`, not `σ`. No corpus *theorem* extends beyond that `J`; four phrasings and one MAP
   label overreach (row 4′).
7. **Lemma A (ii).** Coefficient-independent by Cartan (A9).
8. **Fact 2.4a.** Confirmed at `Re s = ½` (A10).
9. **Exhaustiveness.** Five rows added (A23); none escapes.
10. **Prop H** is conditional, as stated. Its hypothesis is Lemma E's conclusion. Correct.

## §3 Verdict after audit

**The verdict of R158_002 stands, corrected.** On `X = A_Q/Q^×`, every positivity structure on the list, as enlarged
by A23, is one of the following:
* a restatement of RH: CCM's trace form; Rosati; Prop 7.2 = E1 test by test; `B_{Φ₀}`; the relative trace of the
  II_∞ factor;
* a restatement of RH ∧ SZ: any definite compatible form; Deninger unitarity. Over an `S₃` field these are impossible,
  modulo cyclicity;
* a proved compression, or a zero-blind positivity, that does not transfer: `Δ_Λ`, the Sonin trace, ζ-cycles, KMS;
* false: `B_1`;
* void: the critical Plancherel completion.

**Labels.**

| item | label |
|---|---|
| `X` | `RESTATEMENT` (on `X`) |
| Lemma A | `PROVED` (on `C_Q`) |
| Fact 2.4a | `PROVED` |
| Lemma D | `PROVED` (identity) |
| Construction C | `PROVED` (trivial; OT-3 fails for it) |
| Fact 4.6a.1–6 | `PROVED` |
| Fact 4.6a.7 | `PROVED` as corrected |
| Lemma E | `PROVED`; its necessity half is `CLASSICAL` |
| E-i | `PROVED`, unconditional, no numerics |
| E-ii | `PROVED` + `RESTATEMENT`, with an `ANALYSIS` continuity step |
| Prop H | `PROVED` as amended |
| Lemma U | `PROVED`; content `CLASSICAL` |
| Prop B | `PROVED` computation, `CITED` equivalences |
| function-field Jordan block | `ANALYSIS` |
| `S₃` falsifier | `PROVED` modulo `ANALYSIS` (cyclicity) |
| exhaustiveness | `ANALYSIS` |

In R158_001's OT language, `X` fails OT-2 in Connes' realisation. In the Meyer–CCM realisation it fails OT-5′, where
OT-5′ is Weil's criterion. The MW-5 cluster stays **NOT EXCLUDED, unbuilt**. **No row-D label change, no sign claim.**

## §4 Cleared for Paper 47

The following is cleared for a **Part IV remark on MW-5 / the adèle class space**, labelled `RESTATEMENT`, with
classical content attributed.

1. **The trace form is Weil's form.** On Meyer's nuclear `H¹` (CCM `H¹`), CCM's trace form under
   `F(t) = e^{t/2}g(e^t)` is `W_T(F)` for real `F`. Over `Q`, CCM Prop 7.2 is E1 test by test, in Castelnuovo form
   (`Δ•Δ = 0`), and P47 (18.2) is its weaker `K`-Hodge-index form.
2. **Definiteness forces RH ∧ SZ.** Every definite `Θ`-compatible hermitian form on `H¹_alg` forces RH ∧ SZ. This is
   Serre's argument and Connes 1999's Jordan remark. It extends to any completion into which `H¹_alg` injects.
3. **Definite polarizations have infinite type.** The multiplier of any definite polarization is of infinite
   exponential type (Prop H, Jensen). No multiplier built from finitely many Euler polynomials and real-shift Γ-data
   works.
4. **The canonical residue polarization is indefinite**, unconditionally (A18 proof).

**Cleared only with its `ANALYSIS` flag:** the `S₃`-field remark (cyclicity over `K`).

**Not cleared:**
* any novelty claim for Lemma U or Construction C;
* "`X` fails only OT-5′";
* "Prop 7.2 = (18.2) = E6";
* the function-field Jordan block as a theorem;
* Lemma A beyond `C_Q`;
* the uniqueness claim of Lemma D.

## §5 Open items (outside this audit's write scope)

* **Scoping of phase 63.** MAP_3 row 63 ("PROVED-IMPOSSIBLE", "over-generalized? No") and the phrase "the wrong type to
  be Frobenius" (R1-VERDICT, MAP_3 l.232, R151_001 l.553, CORPUS_CHECK_R145 l.22) should be scoped to
  `J e_n = sgn(n)e_{−n}`, as MAP_1 NG-63 already is.
* **A new OT-1 clause for R158_001:** for a P-HS / (D3) route, `H¹` must not be cyclic at multiple zeros. The `S₃`
  field shows why.
* **Optional follow-up (O0):** verify the `K`-analogue of Meyer's Laplace-range theorem. That is all A20 needs.
