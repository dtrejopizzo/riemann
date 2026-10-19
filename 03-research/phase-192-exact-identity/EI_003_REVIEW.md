# EI_003 — Review

lem:shape-lin, cor:shape(a), prob:region(3)), SHAPE_THEOREM (B4, Cor (a)), index 04_ N_BUILD_005 / L2_011 row 8, R163_603. Pen and paper.

## Verdict
**Theorem 1 CONFIRMED PROVED (elementary); (2.1) CONFIRMED as identity with one FALSE size claim (FIX); Theorem 2 ("symbol rigidity") is NOT a theorem with a precise deduction class — it is the definition of σ_T (eq:symbol) restated, hence a tautology; as a NO-GO for the mandate's clause it is a category error, ARGUED at best. Object EXCLUDED (invariant under every O1–O15). The column move "non-linear in Λ → NO (PROVED impossible)" is REJECTED.** No SI-column property moves.

## 1. Line-by-line check
| claim | check | label |
|---|---|---|
| Thm 1(i) θ′ = ½m, σ_T = 2Θ_X′ | d/dτ Im log Γ(¼+iτ/2) = ½Re ψ(¼+iτ/2); minus ½log π ⇒ θ′ = ½m (prop:boundary/lem:K). Σv_n cos(τ log n) = 2(ΣΛ n^{−½} sin(τ log n)/log n)′. | CONFIRMED PROVED (elementary; θ′ = ½m is textbook Riemann–Siegel) |
| Thm 1(ii) Z_T real, R_X = Θ_X′ + iZ_T′/Z_T | arg ζ(½+iτ) = −θ mod π; arg Z_{<X}(½+iτ) = −ΣΛn^{−½}sin(τ log n)/log n; |Z_{<X}| = exp(ΣΛn^{−½}cos/log n); d/dτ log Z_X(½+iτ) = −iR_X and log Z_X = log|Z_T| − iΘ_X ⇒ R_X = Θ_X′ + iZ_T′/Z_T off ordinates. | CONFIRMED PROVED. Re R_X = ½σ_T agrees with EI_001 Thm 2(ii)/EI_002 Thm 1 |
| Thm 1(iii) comb absorbed into the Γ-factor | definitional (Z_X = ζ/Z_{<X}, Z_{<X} entire zero-free). | CONFIRMED (trivial; sign-free, = N_BUILD_005 NO-GO restated, as the memo says) |
| (2.1) | product of EI_002 (3.1) and Thm 1(i). | CONFIRMED as identity |
| §2 "for |τ| ≤ M^{1−ε} the test is c·ζ(½+iτ) up to M^{−Aε}" and "the beyond-Nyquist tail is the only place the spectral density differs from c²F̂₀²|ζ|²" | **FALSE**: (3.1) has the polar term M^{½−iτ}W(½−iτ), of size M^{½}|W(½−iτ)| ≫ |ζ(½+iτ)| for bounded τ (the length-M partial sum of ζ at bounded height is ≍ M^{½}; W(½−iτ) decays in τ, not in M). The family's spectral density at bounded height is ≈ M F̂₀²|W(½−iτ)|², the ℓ = 0 Poisson term, with c²|ζ|² and the cross term as corrections. Same error as EI_002's Corollary. The stationary-phase remark (saddle at τ ≈ 2πM) is heuristic and the memo labels it ARGUED. | **FIX**; nothing downstream depends on it except the narrative of §4 |
| **Thm 2 (symbol rigidity)** | The set 𝔖 is "expressions for σ_T obtained by …"; any expression *for* σ_T equals σ_T; σ_T = m − Σv_n cos is affine in (Λ(n))_{n<X} **by definition** (eq:symbol; prop:finite(iv)). So the statement "every member of 𝔖 is affine in Λ" is the definition of σ_T, independent of which operations are allowed. The "class" is not a deduction class in the sense of def:shape-class (no property set 𝖯 of form objects, no falsifier, no lem:transfer instance), and the proof's clause "operations linear on the functions they act on" excludes nothing: a chain may pass through ζ = exp(ΣΛn^{−s}/log n) (non-linear in Λ) and return to σ_T. The memo's own review item 3 concedes this and relocates it to "case (b)". | **NOT a theorem with a precise class. Tautology (PROVED as such). As a NO-GO: ARGUED, and aimed at the wrong clause** (see §2) |
| Corollary ("the conjunction {exact identity on the window form, non-linear in Λ, not through h*, not REF-D} is empty on the symbol side") | "symbol side" is undefined; counter-instances on the *form* side exist in the record: Schur complements on fixed finite subspaces (thm:coer-schur, lem:wh-schurabs) are exact identities on the window form, rational in Λ, not through h*, and REF-D only because the reduction is exact for the whole problem; thm:sos-type decompositions are exact identities whose certificate side is non-linear. Whether these are "symbol side" is a matter of words. | ARGUED |

## 2. Why Theorem 2 does not move the column
cor:shape(a) and prob:region(3) require that a valid proof **use** (Λ(n))_{n<X} non-linearly — "a linear use is a measure identity on the window (lem:shape-lin(i)) and so a certificate of class (D)". The clause is about the deduction, not about σ_T, which has always been affine in Λ (eq:symbol). EI_003 Thm 2 proves that σ_T is affine in Λ — known since the definition — and the README concludes "non-linear in Λ moved to NO on the symbol side, PROVED impossible". That is a category error: the admissible region never asked the symbol to be non-linear. What the three memos actually show is that **these three constructions** use Λ linearly (EI_001 at fixed h*, EI_002/003 in the symbol with the non-linearity parked in a chosen test vector). That is a failure of the constructions, recorded by cor:shape(a) in advance; it is not a new NO-GO and it moves nothing in Problem (R).

## 3. MUST-NOT clauses, tested
Property set: "Thm 1 and (2.1) hold". For any form object with a symbol σ (comb or not), define Θ := ∫σ/2 and Z_{<X} from its comb (signed allowed, Beurling positions allowed, random positions allowed): Thm 1(i) holds verbatim; (ii) needs a function playing ζ — for a_P, f_t, ζ̃, Epstein, ζ_K it exists (their own Dirichlet series / completed functions) and the phase identity holds with their θ; for quartets and Poisson combs there is no ζ-like function but (i) and (2.1) still hold. So the object survives O1–O15. **EXCLUDED (O1, O7, O11, O15; and O12: for ζ_K the identity holds with θ_K and the comb on log N(𝔞); "named, not exploited" = not met).** B4: Thm 1 is a rewriting of the symbol, hence linear (W7). B8: Thm 2 is not a deduction; nothing to restate.

## 4. MUST clauses
| clause | verdict |
|---|---|
| exact identity | met (Thm 1, (2.1)) |
| non-linear in Λ | **not met** (and the claimed impossibility is a tautology about σ_T) |
| Euler × FE × ℤ jointly as mechanism | **not met** ("as factors", memo concedes) |
| ℤ as mechanism | **not met** ("coefficients 1 in the test" is the choice of test) |
| margin from the identity | **not met** (memo concedes) |
| fluctuation not density | structure only (θ′ carries the density by the FE) |
| 10⁻⁵-sensitive | vacuous |
| separates ζ from ζ_K | named, not used ⇒ (R)(10) not met |

## 5. Retry check
Z_X, Z_{<X} are the partial Euler products of N_BUILD_005 / L2_011 row 8 (NO-GO: no sign) in Hardy-function dress; R163_603 (Hardy coupling, DEAD) is different in aim. The memo's claimed novelty is Thm 2, which is prop:finite(iv). Net content beyond the record: the phase identity σ_T = 2Θ_X′ and R_X = Θ_X′ + iZ_T′/Z_T (PROVED, elementary, no sign). Borderline retry of N_005; not a dead-route retry.

## 6. REF-D scepticism
Nothing here is D in other coordinates because nothing here is a statement with a sign. The memo's Corollary (b) channel "twisted second moment of the smoothed partial sum against the Euler tail" is (S) on the family = T*₃(η) (REF-D for η ≤ η₀), as EI_002 already records.
