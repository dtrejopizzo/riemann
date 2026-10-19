# Paper 47 — A Dual Theory of Weil Positivity at Finite Support

> ** — §20 *The shape of a proof* and Problem (R) (DEFINITIVE_CHANGES.md, section dated ; source memo SHAPE_THEOREM.md after its independent adversarial review).** Backup `main_pre_shape.tex`; now 155 pp., 0 errors, 0 undefined references, 0 overfull boxes. Theorem `thm:shape` (three tiers: transfer PROVED for O₁–O₄, O₆–O₈, O₁₃–O₁₅; labelled for O₄^ε, O₅, O₉–O₁₂; structure), new PROVED pieces `prop:shape-eulerdel` (Euler-preserving prime deletion), `prop:shape-twist` (FE-preserving twist ζR, pointwise curvature barrier, not a window falsifier), `prop:shape-crit`(c) (mean square of the comb = 4T²), `prop:shape-inputs`; Problem `prob:region` (the admissible region) in §Open problems; bibitems Paper46, Titchmarsh1986.

> ** — secondary items of §19 (SECONDARY_ITEMS.md).** Backup `main_pre_secondary.tex`; now 133 pp., 0 errors, 0 undefined references. PROVED: (H_G) (`lem:sl-HG`; `thm:sl-L2`, `cor:sl-split` unconditional), (H_f) (`prop:ftprim`; `thm:famFE` unconditional), rate O(1/log M) of the lattice ceilings (`thm:R` sharpened, `cor:Rrate`, `cor:CP` updated), 𝔊_T ≻ 0 on a right neighbourhood of ½log5 (`cor:beyond5`), the variational characterization of the optimal multipliers and of λ^prim = λ^W (`thm:mult`, new §11.4), and the equivalence of Problem `prob:annihilate` with window positivity (`prop:annihilate-equiv`). OPEN with precise statements: the dual-side deficit of Problem A, a certified window beyond ½log5, the two-sided law with sign, and λ^prim = λ^W at a given window (reduced to a finite condition; numerical evidence at ½log3 only).

> ** — integration of the two verified draft sections (author decision ).** `DRAFT_SECTION_INERTIA_BARRIERS.tex` (parts I–II: §16 *Inertia, remainders and barrier theorems*, §17 *The semilocal Sonin decomposition at the first prime*) and `DRAFT_SECTION_COERCIVITY_REDUCTION.tex` (§18 *Archimedean coercivity on Tate-orthogonal blocks and the finite reduction*) pasted into `main.tex` between §15 (positivity at ½log5) and the concluding remarks; one new item in Open problems. Backup: `main_pre_integration.tex/.pdf` (88 pp.); now 104 pp., 0 errors, 0 undefined references/citations, 0 overfull boxes. Conflicts of `CHECK_TABLE.md` resolved with the paper's definitions: N1 (absolute semilocal trace formula asserted at level λ = 1 only, `rem:sl-level`); N3 (only the δ-version of the finite index, no "compact ⇒ n₋ < ∞"); N4 (Γ_T + Π_T^{(2)} = 𝔞_T only for T < ½log3, stated after `cor:sl-split`); C1 (cross term with factor 1 per unordered pair, quadratic coupling π/2, bilinear π; the ordered-pair convention noted in `rem:coer-nogo`(a)); C2 (‖Π_T‖ ≤ 𝒜_T/2 only for T ≤ log 2, `prop:coer-prime`, 1.6740 on (log 2, ½log5]); C3 (everything stated for λ_A(τ), nothing for λ^prim; the ARGUED extension to K^prim removed per R186_105); C4–C9 as in the drafts (form domain, lem:mbounds, lem:contA coverage, Dirichlet-basis Poincaré, closed-form C_B, form-domain Schur with sandwich). Adversarial corrections R186_105 applied: C_B ≤ 1.74 uniform, θ ≈ 0.22, λ_A(τ) = log(1/τ) − 0.510 and all Galerkin values marked numerical; "chain ∈ [π, 2π]" and the λ^prim extension not integrated; (L-W) of R186_047 not integrated (third draft). Precedents cited at Theorems A/B (`rem:coer-prec`): Yoshida 1992 Lemma 3, Connes–Consani Thm 3.6 / Cor 3.8 / Rem 3.9, Kim et al. 2607.24830 (numerical), Connes–van Suijlekom 2511.23257; finite-reduction precedents Zhu Thm 1.1/1.4, Groskin. New bib entries: Carleman 1923, CC 2008.10974, CCM 2310.18423, CCM 2403.01247, CvS 2511.23257, HLP Thm 316, Kim et al. 2026, Simon Trace Ideals. Held back: the detection theorem (R184_006, check table item 8: proof to be rewritten, Trudgian constants unverified) and the "Q ⟺ …" dichotomy (item 9); the "inertia alone" exclusion is stated with its model index as argued, not proved; `thm:sl-L2` notes two estimates used without full detail. All memo references (R18x_xxx) removed from the integrated text, as in the  revision; `Π_T` in §9.1 now written with Re. Forbidden-vocabulary grep on the new text: 0 hits.

> ** — readability revision of `main.tex`.** Rewritten for publication style: new abstract and introduction; status tags, label table, repository paths, withdrawn/verdict paragraphs and programme vocabulary removed; the former Section 9 split into four sections plus concluding remarks; numerical (non-certified) values collected in Appendix C; `phase161_first_contact.tex` rewritten inline as the final section (continuity of λ_A made an explicit hypothesis in the first-contact lemma); citations to Papers 45/46 updated or replaced. No statement or proof changed otherwise. 91 → 83 pp. Backup: `main_pre_readability.tex.bak`.

**David Alejandro Trejo Pizzo.** LaTeX, ; phase-161 first-contact construction integrated inline in `main.tex` on 2026-09-28.

**Canonical row-D manuscript.** This is now the single current construction paper for row D. Paper 46 remains the historical campaign/method-constraint record; new row-D mathematical claims and the current terminal gate belong here.

**Phase 161 integration.** The final section consolidates the finite Poisson--Chebyshev anomaly, renormalised continuum modulo Tate, faithful Gamma-pole Hankel observation, exact compressed collars, the equality-state balance and the spectral sign audit. It records that the strict Gamma--Euler contraction gives no independent closure: each proposed return inequality is equivalent to detector annihilation. The genuine open tasks are direct Gamma-moment annihilation using minimal first contact and oriented arithmetic, plus either continuity of the primitive bottom or a transfer from the continuous complete-form first contact. No closure of D or extension of the unconditional positivity range is claimed.
Adversarial review R1: `TEX_ADVERSARIAL_REVIEW_R1.md` — verdict ACCEPT WITH REPAIRS, no FATAL, 8 MAJOR / 11 MINOR / 4 COSMETIC; all 23 repairs applied  (a priori ε_fp bound for Theorem C, abstract narrowed to λ^prim, K^prim moment conditions corrected, Identity M 'bounded' → band-limited, Prop. 8.1 proof added and negative branch corrected, envelope threshold with/without ‖ν‖_TV separated, phase references removed, etc.).

**What it contains (phase 153–154 results of record, plus §7–8 written for the paper):**
* §2 the archimedean multiplier as a Lévy exponent (`K = ½/sinh(u/2)+½/cosh(u/2)`, complete Bernstein in `τ²`,
  pure jump), the form as a Lévy energy (Theorem A), monotonicity and the subordination upper bound;
* §3 the primal/dual programmes, **strong duality with finitely atomic dual sequences (D1)**, **non-attainment (O)**
  (paired with Bombieri's primal attainment), the Wiener–Hopf Euler–Lagrange equation (W), the polar multiplier `β₀ = 2` (P);
* §4 tail lemmas F1 (graded periodic), T (exponential columns, monotone), Hybrid; exhaustion by exponential columns (E);
  Identity M; the second-order cover (F3);
* §5 **Theorem C**: explicit 437-atom certificate, `λ_min(A_{½log3}|P_T) ≥ 8.8577·10⁻⁵`, machine-verified; comparison with Zhu 2026;
* §6 Lemma W (moment interior), **Theorem V′** (`Θ(log R)` mass–value exchange), the envelope threshold `2πe^{A_T}` (doubly
  exponential in `T`), and the honest state of the two-prime windows (nothing certified at `T = 0.58`; best `−3.20·10⁻³`);
* §7 **Theorem Z (new)**: the dual certificate is the Weil explicit formula evaluated on `w(u)cos(τu)` for a flat-top weight
  `w ≡ 1` on the window; `f_w(τ) = Σ_ρ ŵ(τ − γ_ρ)`; exhaustion; **RH ⟺ for every window a flat-top one-sided smoothing of the
  zero measure exists**; certificates are unconditional inequalities about zeros; the certificate at infinity is the primes outside
  the window;
**New in §7 (finite zero sets).** The section now closes, unconditionally, the question of whether a finite set of zeros can carry a flat-top certificate. Lemma `lem:fdict` turns non-negativity of `Σ_{γ∈Z} ŵ(τ−γ)` into positive definiteness of `w·g_Z`, and Theorem `thm:finZ` proves that for every window `T`, every finite symmetric multiset `Z ⊂ ℝ∖{0}` with `|Z| ≥ 2` (multiplicities allowed) and every even continuous integrable `w ≡ 1` on `[−2T,2T]` with `w(u) → 0`, that function takes negative values — with no support, regularity or genericity hypothesis. The proof puts a lattice of step `a ≤ 2T/|Z|` inside the window, reads off a rank-`r` Toeplitz block at the `r` distinct nodes `e^{iγa}`, and shows that positive semidefiniteness propagates the order-`r` recursion for ever, forcing `w·g_Z` to repeat the almost periodic `g_Z` (Cesàro mean `Σ m_j² ≥ r`) instead of decaying. The old asymptotic statement survives as Remark `rem:loc`, which gives the *location* of the negativity (phase corrected by `(−1)^k`, decay hypothesis on `w^{(j)}` added). Corollary `cor:infinite` draws the consequence — row D is intrinsically infinite: a zero table can evaluate `f_w` but never certify it, and the negativity of a truncation at height `Γ` sits at `|τ| ≳ Γ/2` — and Proposition `prop:finuniv` records the trivial converse, that in a finite universe the dual certificate is the spectrum itself, unique among symmetric measures, positivity being Bochner. Compiles at 34 pages, 0 errors.

**New in §7 (the extension problem) and §8 (the negative index, and the nodal law of the atoms).** The unnumbered Kreĭn remark of §7 is replaced by a subsection `subsec:KEP` that makes the identification precise: the window datum `g` is the explicit-formula distribution (Lévy pair `C₀δ₀ − ½ Pf K`, polar `2cosh(u/2)`, prime atoms `−(v_n/2)δ_{±log n}`), `KEP(T)` asks for the positive symmetric tempered measures whose transform agrees with `g` on `(−2T,2T)`, and Lemma `lem:polar` records that the polar kernel has Gram rank 2 and signature `(1,1)`, so solvability is automatic at no window. Theorem `thm:KEP1`: every flat-top certificate gives an absolutely continuous solution, and a strict one gives a continuum, by perturbing the weight outside the window where `D = 2cosh(u/2) − K/2 > 0`. Theorem `thm:KEP2`: solvability implies `λ^W_T ≥ 0` (with the form-core step written out). Theorem `thm:KEP3`: the dichotomy, hence **RH ⟺ KEP(T) indeterminate for every T > 0** — a reformulation of `cor:RH`, not a step. Corollary `cor:KEP08`: unconditionally, `KEP(T)` is indeterminate for every `T ≤ 0.8`, via Zhu's certificate for the complete form (cited, not re-verified); a remark explains why Theorem C does not give this (its `β = (2.0026, −0.0097) ≠ (2,0)` solves a perturbed datum, defect `5.9·10⁻³ ≫ c`). Theorem `thm:finDet` is now proved first — a finite zero set is **determinate**, `μ_Z` being the unique finite positive symmetric solution with no decay or product hypothesis — and `thm:finZ` is derived from it in a few lines, so the decay hypothesis is seen to be inessential. In §8, Theorem `thm:J` gives the matching **lower** bound on the negative index, `n₋(Γ_T) ≥ ⌈2Tτ₀/π⌉ − 1` and `n₋(A_∞|P_T) ≥ ⌈2Tτ₀/π⌉ − 3` (Dirichlet modes, Plancherel, Jensen on the concave `φ`, `φ(τ₀²) = −C₀`); the `P_T` bound is vacuous at `½log3` and `log 2`, the asymptotic is `4.004·T + O(log T)`, and any window range on which `n₋ = 1` ends at `T₂ ≤ 2π/τ₀ = 0.9989426`. Remarks record that Jensen on a concave `φ` yields ceilings only, and that `tr M₋ = 4.495774·T` with `M₊ > 0` gapless, so Birman–Schwinger counting is unavailable. Lemma `lem:N` writes each prime atom as a one-sided overlap `∫_{a−T}^{T} F(z−a)e(z)dz`, Proposition `prop:G` forces its sign beyond `a* = T + max(z_F,z_e)`, and a DIAGNOSTIC remark reads the `76 %` cancellation at `log 2`: the overlap vanishes at `0.2128, 0.6087, 1.0225`, `log 2` and `log 3` straddle the third zero, `a* = 1.1717` is missed by `6.65 %`, and the nodes `±0.3152` of `F*` are forced by the Tate constraints — so the 2-plane positivity is an archimedean nodal condition, not an arithmetic coincidence of 2 and 3. No sign is claimed at any window. Compiles at 51 pages, 0 errors.

**New in §7 (the decay tail).** Theorem `thm:Dtail` bounds the tail of a flat-top certificate by decay instead of by total variation. It is the extension of Lemma `lem:T` in which the atomic term is split: for `w ∈ W_T ∩ C²` the absolutely continuous part of `ν̂_w + 2ĝ₀` is `O(D(w)τ⁻²)` with `D = D_c + D_K` explicit, while the prime atoms outside the window carry no decay and are bounded only by their mass `E_at(w)`. The regrouping with `2ĝ₀` is forced — `ν̂_w` alone has a `2cosh T` jump at the window edge and is only `O(τ⁻¹)` — and the canonical `β₀ = 2` is exactly what removes it. Corollary `cor:comb`: if `w` vanishes at every prime power outside the window (finitely many linear conditions on a compactly supported `w`), then `E_at = 0` and the verification interval is `τ_stop ≤ max{2πe^{A_T+1+…}, √D + 2} = O(√D)` — polynomial in the size of the weight, against the doubly exponential `2πe^{A_T+‖ν‖_TV}` of Prop. `prop:env`. Corollary `cor:bprof`: a bounded profile controls `D` and not `E_at`. Remark `rem:comblp` records, as DIAGNOSTIC, that the linear programme over the comb-vanishing spline class is negative at all four windows on `[0,200] ⊃ [0,τ_stop]`, so for those weights the failure is a statement about all of ℝ. No sign claimed. Compiles at 36 pages, 0 errors.

* §8 what a closing argument must do (reduction chain; decidability per window; the work lives on `[0, 2πe^{A_T}]` at the
  near-alignment ordinates of the prime comb) and cannot be (O, V′, envelope, monotonicity, prime-side ≡ zero-side);
  Problem A (class-dependent value bound → phase 155) and Problem B (arithmetic certificate = RH); **Proposition TK** (phase 155
  round 1, audited): ν-independent ceiling on every lattice class = λ_min of an M×M Toeplitz matrix, concave in β; no lattice of step
  ≥ 2T/8 certifies ½log3; Theorem C's certificate is at 15 % of its class ceiling (numbers DIAGNOSTIC).

**New  (round 3 of the class-dependent programme; 41 pp., 0 errors).** Five additions.
(1) §4 **Theorem P3 + Corollary A^P + Corollary C^P**: since (P) has no minimiser, the bounded-set
reduction is made uniform over the near-optimal feasible set — every `μ` of value `≤ λ^P + ε` has
`∫(m−C₀)dμ ≤ G(ε) = λ^P + ε + B` and `μ(|τ| ≥ R) ≤ η` for the explicit
`R(ε,η) = 2π exp(1 + C₀ + G(ε)/η)`; a certificate verified only on `[−R,R]` is worth at most
`(λ^P + ε + Wη)/(1−η)`; the exponential in `1/η` is forced by Theorem V′(ii) (constant open); and the
ceiling rate is `O(1)` unconditionally, `O(K(log M)^{−δ})` on the sub-family with a `(1+δ)`-moment,
`K` non-explicit. PROVED.
(2) §8 **Theorem N′**: no lattice certificate of step `2T/M` with `M ≤ 24` has non-negative value at
`T = 0.68` or `T = log 2`, β-uniformly, for any range, atom count or tail lemma;
`Ceil(24, 0.68) ≤ −7.49·10⁻⁶`, `Ceil(24, log 2) ≤ −6.58·10⁻⁷`. Sixteen interval enclosures per window
(composite Gauss–Legendre with the classical panel remainder, derivative bounds
`|m^(j)| ≤ 2^{−j} j! ζ(j+1,¼)`, guarded nodes, test kernel optimised against the β-box), the rest by
sublattice inclusion in 20 and 24; binding error the quadrature, `≤ 6.7 %`; the bound survives any
`B ≤ 4.7·10⁹`. PROVED (machine-verified). The class `M = 24` that carries the endpoint of record at
`½log3` is provably empty at both two-prime windows.
(3) §8 **Proposition (two archimedean thresholds)**: `A_∞` on `L²(−T,T)` and on `P_T`, both bottoms
non-increasing, both `≤ C₀ + φ((3π/2T)²)` (Theorem SC with `A = 0`), hence negative past
`T₀(0) = 0.74921` and `≥ 0` for `2T < log 2`, so thresholds `T*_∞ ≤ T*_{∞,P}` exist in
`[½log2, 0.749]`. DIAGNOSTIC Galerkin upper bounds: `T*_∞ ≤ 0.3716`, `T*_{∞,P} ≤ 0.5958`. Reading: at
`½log3` the archimedean form on `P_T` is positive alone (`≈ 0.083`) and the primes are a cost; at
`log 2` it is indefinite (`≈ −0.154`) and the prime form `Π_T` supplies `≈ 0.188` on the ground-state
direction — the primes are necessary, not a perturbation. `‖Π_T‖ ≤ A_T` PROVED.
(4) §8 **Schur reduction + a proved value at `log 2`**: `W ≥ 0` on `P_T` ⟺ the Schur complement along
a pivot of positive value is `≥ 0`; the reduction is a congruence, parity confines the correction to
the even sector. For the archived even degree-17 direction `F*`,
`W_{log2}[F*] ∈ [0.0342113430, 0.0342182500]` by interval arithmetic on the Lévy form (exact
polynomial autocorrelation, affine sandwich of `K` per panel, closed-form tail, exact atoms, pole
defect `≤ 3.4·10⁻²⁸`). PROVED (machine-verified) — **one direction at `log 2`, not a sign for the
form**; the endpoint of record is unchanged. DIAGNOSTIC: the crude sufficient condition fails by
`1.07`–`1.49`, and even the ideal even-sector condition `λ₃ − c²/w₁₁ > 0` fails by `0.064`–`0.310` —
positivity on the complement is a cancellation, never a margin.
(5) §9 labels and the abstract updated accordingly.

**2026-09-22.** Four additions and one withdrawal.
(a) §8 **Remark (what the numerics do not say)** — WITHDRAWAL, mandatory. Galerkin (Rayleigh–Ritz)
values on nested subspaces are upper bounds on the infimum of the form on `P_T` and, at the two-prime
windows, have not stabilised in the basis size (at fixed dimension the bottom moves by more than an
order of magnitude between `N = 18` and `N = 36` and keeps falling). **No numerical value of
`inf W_{log2}|P_T` is supported by this paper, positive or negative**; the printed
`λ_A(log 2) ≈ 10⁻⁷` and the `10³`–`10⁵` ratio are deleted. Theorem C's certified lower bound at
`½log3` is unaffected.
(b) §8 **Theorem (nested even subspaces at `log 2`)**: `W_{log2}` is positive definite on
`E_k = span{e₁, e₃, …, e_{2k−1}}`, `k = 1,…,7`, for the archived even archimedean eigenvectors, with
certified `λ_min ≥ 3.4212·10⁻², 2.1136·10⁻³, 4.0453·10⁻⁴, 9.0763·10⁻⁵, 4.0951·10⁻⁵, 2.2156·10⁻⁵,
6.5687·10⁻⁶`; 2-plane determinant `≥ 2.10·10⁻⁴`; `E₅` also certified at `T = 0.62` (`≥ 3.92·10⁻⁴`)
and `0.65` (`≥ 1.70·10⁻⁴`). Polarisation (only quadratic values enclosed), the Lévy-form enclosure of
the `w₁₁` theorem, interval Cholesky with bisection. PROVED (machine-verified) — positivity on
explicit finite-dimensional subspaces, **not** positivity of the form. With it: the Schur coupling is
purely arithmetic (`b = P_V Π_T F*`), and `Π_T = −Σ_n v_n Re(R_T τ_{log n} R_T)` is a non-compact sum
of truncated shifts with row bounds `|π_ij| ≤ A_T`, `Σ_j π_ij² ≤ A_T²`. DIAGNOSTIC: `π₁₃ = +0.1867
(atom 2) − 0.1410 (atom 3)` — a `76 %` cancellation is what makes the 2-plane determinant positive
(with the `log 2` atom alone it is `−0.033`); the near-zero Galerkin bottom sits on the last even mode
of every truncation, so no fixed number of archimedean modes captures the obstruction.
(c) §8 **Theorem (lattice sampling of a flat-top certificate)**: for a (D)-feasible flat-top density
`G = (1−w)K` with `C^{r−1}` contact at both ends, the sampled measure `ν_lat` is feasible and
`c_lat(M) ≥ min{c_w, m(πM/2T) − V₀} − ε_r(M)`, `ε_r(M) = 2(1−2^{−r})ζ(r) V_r (πM/2T)^{−r}` (Poisson
summation). At fixed `w` the lattice costs `O(M^{−r})`: the Problem-A deficit is the continuous
problem `sup_w c_w`, not attained (Theorem O, which holds for `v = 0` — the primes are not necessary
for the obstruction). DIAGNOSTIC: archimedean ceilings approach `λ^{∞,P}_min` from below with deficit
`≈ 0.28·M^{−1.2}` over `8 ≤ M ≤ 64`, essentially `T`-independent; suggests `D ≍ M^{−1}`, not proved.
Also §8 **Proposition (negative index)**: `n₋(A_∞|P_T) ≤ ⌊2Tτ₁/(πθ(τ₁))⌋` for every `τ₁ > τ₀ =
6.28983599`, minimised at `τ₁ = 14.8815`: `n₋ ≤ 68.51·T`, i.e. `37` at `½log3`, `47` at `log 2`, `54`
at `0.80`; prolate counts `4/5/5` DIAGNOSTIC; `n₋ = 1` above `T*_{∞,P}` remains a hypothesis.
(d) §7 **Corollary (the Li kernel is outside the class)**: `λ_n = Σ_ρ Φ_n(γ_ρ)`,
`Φ_n = 1 − cos(nθ) ≥ 0`, `Φ_n = ŵ_n` with `w_n(u) = −½ e^{−|u|/2} L_n′(|u|)`; `w_n ∉ W_T` for every
`n, T` (nonnegative transform, `δ = 0`, no flat top), and in sharp form `ŵ_n(±i/2) = ∞` with a
divergent prime sum, so `λ_n` is the zero-sum half only, not a Weil-functional evaluation. §8
**Remark**: the Li analogue of the sub-comb theorem fails — the `{2,3}` sub-comb sequence is eventually
positive unconditionally (prime side `−1.24, +0.63, −0.31, −1.64` at `n = 1, 10, 10², 10³`) because the
Li weights `m^{−1}` are subcritical where the Weil weights `m^{−1/2}` are critical; under RH the two
differ by `o(n log n)` (Bombieri–Lagarias, Coffey — bibliography extended).
(e) §9 labels and the abstract updated accordingly.

**New  (round 6a: the arena, the nodal structure, and the PF₂ no-go; 53 pp., 0 errors).**
Four additions. (i) §8, next to the two archimedean thresholds, **Proposition (nodal structure of
`P_T`)**: the ground state of `Γ_T = C₀‖·‖² + 𝔈` on all of `L²(I_T)` is simple and a.e. strictly
positive — `𝔈` is a pure-jump Dirichlet form `¼∬K(|x−y|)|F(x)−F(y)|² + ½∫κ|F|²` with killing
`κ(x) = ∫_{|y|>T}K(|x−y|)dy`, so Beurling–Deny plus irreducibility gives a positivity-improving
semigroup and the resolvent is compact since `m(τ) → ∞` on a fixed compact window — while
`{e^{u/2}, e^{−u/2}}` is a Chebyshev system of order 2, so **every** nonzero `F ∈ P_T` has at least
two sign changes (defined in the `L²` sense) and the bottom on `P_T` is never of one sign; the nodes
`±0.3152` at `log 2` are the diagnostic instance. PROVED.
(ii) §8, after the truncated-shift proposition, **Theorem (log-slow archimedean gaps)**: on the even
part of `P_T`, where the two Tate constraints coincide and the codimension is 1,
`λ^ev_{k+1}(A_∞|P_T) ≤ m((2k+3)π/2T) = log k + O(1)` (even Dirichlet modes, min–max, Jensen on the
concave `φ`); and **Corollary (the arena)**: the number of even archimedean modes the prime form, of
norm `≤ A_T`, can reach is `N*(T) ≥ ⌊Tτ_*/π − ½⌋`, `τ_* = m^{−1}(A_T)`, which by
`lem:mbounds`(ii) at the exact frequencies gives `N* ≥ 12` at `log 2` (`m(τ₁₁) ≤ 2.2168 ≤ A_T =
2.24889`, `m(τ₁₂) ≥ 2.2596`) and `N* ≥ 2` at `½log3` (`m(τ₁) ≤ 0.8928 ≤ 0.98026`, `m(τ₂) ≥ 1.1075`),
and, since `A_T ~ 4e^T`, `N*(T) ≥ 2T e^{A_T}(1+o(1)) = exp(4e^T(1+o(1)))` — doubly exponential in `T`.
PROVED. The reading is a proved no-go for truncation: no fixed finite truncation in the archimedean
basis can decide the sign of the even Schur complement, and the certified `E₇` at `log 2` sits
strictly inside an arena of at least 12 modes — the structural reason behind the Galerkin
withdrawal. DIAGNOSTIC: Galerkin `N = 60` finds exactly 12 competing even modes at `log 2`.
(iii) §8, after the nodal remark, a DIAGNOSTIC remark on the sign rule from the nodes: the
largest-common-cell rule predicts `100 %` of the entries of the `8×8` even prime matrix with
`|I| ≥ 0.10`, carrying `89–96 %` of the mass, and fails only on the small near-cancelling entries;
the `k`-th even mode has `k` nodes in `(0,T)` for `k ≤ 8` with interlacing (a conjecture whose base
case is the proposition above); Lemma N reproduces the prime matrix to `1.7·10⁻⁵`.
(iv) §2, closing remark, **no-go for total positivity**: `K` completely monotone ⇒ log-convex ⇒
`K(|·|)` is not a Pólya frequency function of order 2 (Schoenberg), so Karlin's total-positivity
oscillation theory does not apply to the archimedean kernel. One hypothesis, two opposite
consequences: complete monotonicity gives every ceiling in the paper and forbids the oscillation
route. Stated as a route closure, not an impossibility theorem; the semigroup variant is OPEN.
Bibliography extended (Schoenberg 1951, Karlin 1968). §9 labels updated; abstract unchanged; no sign
claimed at any window.

**Rules:** no sign claimed for ζ beyond `T ≤ log 2` for the **primitive** form (`λ^A ≥ 0`, Paper 42; `T ≤ 0.8` only through Zhu, cited); for the **complete** form (`λ^W ≥ 0`) the classical range is `T ≤ ½log 2` (Yoshida/Bombieri) and `(½log 2, 0.8]` rests on Zhu 2026 Thm 1.2 alone (cited, not re-verified) — corrected in phase 156; no statement about zeros; labels PROVED / PROVED (machine-verified) /
DIAGNOSTIC; Zhu 2026 (larger window, Galerkin) cited where our window is announced; Bombieri 2000, Yoshida 1992, Suzuki cited
from primary reading (`phase-154/R154_031`).


**Major revision R2.** Adversarial review `TEX_ADVERSARIAL_REVIEW_R2.md` — verdict MAJOR REVISION,
1 FATAL, 4 MAJOR, 11 MINOR, a restructuring proposal and a claim-by-claim abstract table; all 16
findings and all 22 exact edits applied, plus two audited additions.

* **Retraction and replacement (the FATAL finding).** The printed lattice-sampling theorem and its
  corollary were wrong on three independent counts: the hypothesis `w ≡ 1 on [U,∞)` contradicts the
  decay required of a flat-top weight and makes `ν_w` infinite; the density of `ν_w` was taken to be
  `(1−w)K`, dropping both the factor `½` and the whole polar block `2w cosh(u/2)`; and the prime
  atoms were never sampled. They are **retracted**, and with them the reading "the lattice is never
  the deficit". The replacement theorem (same label) is proved for comb-vanishing weights
  `w ∈ W_T ∩ C^{r−1}`, compactly supported, `w^{(r−1)}` locally absolutely continuous, with the
  end-point-corrected sampling `ν_lat = Σ_{|j|≥M} d κ_j G(jd) δ_{jd}`, `κ_{±M} = ½`, of the true
  density `G = ½(1−w)K + 2w cosh(u/2)` — a signed measure with countably many atoms and finite total
  variation, feasible with `β = (2,0)`. The cost is **not** a smoothness effect but an edge effect:
  `c_lat ≥ c_w − E_edge(M) − ε_r(M)` with `E_edge = (4/π)cosh T·d + O(d²)` sharp and
  `ε_r = O_r(V_r M^{−r})`; the mechanism is the coherent aliasing of the window cut of the polar
  block (`π cot πz − 1/z`, regular at the origin). Without the end-point correction the sharp
  constant is `cosh T·√(4+16/π²) = 2.37 cosh T`. Whether the *optimised* lattice class also loses
  `Θ(1/M)` is stated as open. Two further errors of the same family are corrected: the edge rate is
  **not** compared with the archimedean ceiling deficit `0.28 M^{−1.17}` (a different programme,
  where there is no polar block and hence no edge), and the difference `f_lat − f_w` is **not** a
  trigonometric polynomial, so the reading that the test-kernel ceiling need not bind flat-top
  certificates is labelled a reading and not a theorem.
* **New: a Ky Fan ceiling for the time–band limiting operator** (self-contained, likely folklore, no
  priority claimed). In the Legendre basis the diagonal of `S_c` is `R_j(c) = (2(2j+1)/π)∫₀^c j_j²`
  with `Σ_j R_j = 2c/π = tr S_c`, so Ky Fan gives `λ_k(S_c) ≤ Λ_k(c) = (2/π)∫₀^c(1 − Σ_{j<k}(2j+1)j_j²)`
  and, quadrature-free, `λ_k ≤ (2/π)Σ_{j≥k} c^{2j+1}/((2j+1)!!)²`. Combined with the trace bound this
  yields `n₋(A_∞|P_T) ≤ 5, 7, 8` at `½log3, log 2, 0.80` as THEOREM values, against `37, 47, 54` from
  the trace; the sharper grid counts `5, 6, 7` are recorded as DIAGNOSTIC and nothing depends on
  them. With the lower bound already in the paper this gives the first two-sided brackets,
  `n₋(Γ_T) ∈ [2,5], [2,7], [3,8]` on `L²(I_T)`. A remark records that the two-value relaxation cannot
  return less than `5` at `log 2` — the residue is charged to the relaxation and to `codim P_T = 2`,
  not to prolate theory — and names the multi-band relaxation as the untested refinement.
* **Constants and ranges.** `A_T = 2.24883` at `log 2` everywhere (one printed `2.24889` corrected;
  the conclusion `N* ≥ 12` survives); `−3.20·10⁻³` unified; the unconditional indeterminacy for
  `T ≤ 0.8` now covers `T < ½log2` by the small-`T` device, and is attributed in the abstract to
  Zhu's certificate for the complete form; the necessity of the primes is stated where it is proved
  (`T > 0.74921`) and only suggested at `log 2`; "the first window in which a prime is coupled" →
  "the largest window with a single prime contact"; four enclosures, not three; a Galerkin upper
  bound is no longer called "a truth"; the first certified eigenvalue of the nested tower is rounded
  down; the factor `½` in the perturbation `r_χ`; the open lattice interval in the determinacy
  proof; the branch of `arg` in the Li computation; the archimedean threshold `(iv)` weakened to the
  upper bounds it proves; `Γ_T` defined once; the limitation `T < arccosh√2` of the affine sandwich
  stated; a notation paragraph fixes `A_T`/`𝖠_T`, `B(F)`/`B_*`, `d`/`ℓ`, `D`/`d_*`/`ϱ` once and for
  all.
* **Restructure.** The former §8 is split into three sections — class impossibilities, the
  archimedean form (structure and index), and what a closing argument must do — and three appendices
  are added: A, the enclosure methods (the second-order cover, the Bernstein grid bound, the interval
  enclosures of the two class impossibilities); B, the Li and Nyman–Beurling dictionary; C, the
  diagnostic record, which collects the measured numbers and their label rows so that the proved and
  the measured never share a page. All labels are preserved, so every cross-reference survives.
  Compiles at 57 pages, 0 errors, no undefined or multiply-defined references.

**R3 applied.** Adversarial review `TEX_ADVERSARIAL_REVIEW_R3.md` — verdict ACCEPT WITH MINOR
REPAIRS; all eight residual edits applied. The substantive one (R3-1): Theorem AL′ carried a
comb-vanishing hypothesis that missed the boundary atom when `2T = log n` — which is exactly the
paper's headline window `T = ½log3` (`n = 3`), where `Def. W` forces `w(2T) = 1` so the atom cannot
be hypothesised away. Rather than exclude the case, the boundary atom `−Σ_{log n = 2T}(v_n/2)(δ_{2T}
+ δ_{−2T})` is now carried inside `ν_lat`, where it is reproduced exactly and cancels in
`f_lat − f_w`; the rate, the constant and feasibility are unchanged, and `G` is now called the
absolutely continuous density. `Cor. AL-def` is stated for `M ≥ M₀(w)` (the second branch of the
minimum in Theorem AL′ does not bind for large `M`). Exposition: Appendix B gains an opening
sentence and its dangling "the corollary" becomes `Cor. nontermwise`, which in turn now points
forward to Appendix B for why its flat-top qualifier is not vacuous; the two body uses of
`Prop. TAY` name Appendix A; the `thm:finDet` chain reads `ra ≤ ℓa < 2T`; the `prop:arch`(iv)
commentary moves to a remark after the proof; and §9 is split into 9.1 thresholds and nodal
structure, 9.2 the negative index, 9.3 the arena and the no-go (the log-2 direction was already its
own subsection §10.4). Compiles at 57 pages, 0 errors, no undefined or multiply-defined references.


**Round 8 integrated (integrating editor).** Order (b) of `R155_060` §4: what the round-8
adversarial audits cleared (`R155_058` for 8b, `R155_059` for 8d; `R155_057` for 8c, one sentence only) is
now in the paper, each statement checked against the paper's own definitions (`def:W`, `def:PD`,
`eq:nuw`, `P_T`, `\lamP`/`\lamA`/`\lamW`, `𝒲_T`). Round 8a (the negative index) is **not** integrated,
and §9.2 is untouched. **§2** Lemma `lem:monoT`: `λ_min(A_T|P_T)`, `λ^prim_T`, `λ^W_T` are nonincreasing
across contact thresholds (the fixed-contact clause of `cor:mono` dropped). **§3** Lemma `lem:roughEF`:
the explicit formula for rough tests under absolute convergence of the zero sum (mollification of
Paper 45 Thm 9.4); the intro's `L²(I_T)` explicit formula now points to it. **§10.3 The margin decays**
(beside the Landau–Widom paragraph): an import table — (X19) as in Paper 46 §15, **(X19′)**
Platt–Trudgian (RH verified to `3·10¹²`, a clause Paper 46 does not import) and **(X-N)** Rosser 1941
Thm 19 (`0.137 log t + 0.443 log log t + 1.588`, `t ≥ 2`) — then Lemma N, the zero-sum lemma, the test
family, **Theorem `thm:margin`** and **Corollary `cor:margin1`**, `λ^W ≤ λ^prim ≤ λ_min(A_T|P_T) ≤
4·10⁹·T·e^{−15.449T}` for `T ≥ 1`, and **Corollary `cor:margin2`**: no `T`-uniform margin, the limits
exist in `[−∞,0]`, **RH ⟺ lim λ_min(A_T|P_T) ≥ 0** (`L^A = −∞` under ¬RH OPEN); a remark calls it the
trivial half of Zhu's law, exponentially weaker. **§10.4 Row D at a window is a finite condition**:
`RD_T` (renamed from the memo's `D_T`, which clashes with the dual value `D_T` of `def:PD`) is membership
of `v_T(Λ)` in a closed convex `𝒱_T` of Γ-data (`prop:finite`); finite modifications of `Λ` (deletion,
amplification) keep `a ≥ 0`, `ψ` up to a constant and every zero and the pole, yet fail `RD_T` at
explicit windows (`lem:cpos`, `thm:finmod`, with the audit's withdrawal of the positive clause on
`[½log2, log2]`), finitely supported combs fail for large `T` (`prop:finsupp`), so classical prime-side
hypotheses decide no window (`cor:void`, METHOD-CONSTRAINT in the sense of Paper 46 Thm 18.1), and the
**arithmetic content of row D is uniformity in `T`** (`prop:uniform`); `rem:twohalves` adds the Paper 46
FE-side half and the one-sentence pointer to the D-HS exclusion by Paper 46 Thm 19.25. **§10.5** the
negative set of `σ_T` is a finite band, `τ_last ≤ τ^lo` (`prop:band`), the Diophantine bracket
`|k log3 − l log2| < ¼log6` with `≤ 6 / 12` arcs (`prop:align`), `τ_last ∈ [45.642, 60.544]` and
`[108.723, 120.087]` PROVED modulo double precision, and `Neg_T` trace class with the band not deciding
the sign (`prop:negtrace`; see the report for the corrected (v)). **§10.6** the alignment inequality
`Al_T(w)` (renamed from the memo's `𝖠_T(w)`, which clashes with `\Aconst = 𝖠_T`), its band form, the
complete-form non-attainment lemma `lem:Onat`, and **Theorem `thm:Al`**: per window `[∃w: Al_T(w)] ⟺
λ^W_T > 0` (`T ≥ ½log2`), the chain `∀T RD_T ⟹ RH ⟹ λ^W > 0 ⟹ ∃w Al_T(w) ⟹ ∀T RD_T`; the per-window
converse `λ_min(A_T|P_T) ≥ 0 ⟹ λ^W_T ≥ 0` stays OPEN. **§10.7** item 4 made quantitative; Remark
`rem:Cheb` (on `P_T` the comb is the Chebyshev remainder). Appendix C: the DIAGNOSTIC band table,
trace values and the loss of the margin proof. Labels table extended; intro gains one paragraph;
abstract unchanged. Bibliography: Paper 46, Platt–Trudgian 2021, Rosser 1941, Rosser–Yohe–Schoenfeld
1968. No sign for ζ beyond `log 2`; endpoint of record unchanged. Backup `main_pre_R4.tex.bak`.
Compiles at 67 pages, 0 errors, no undefined or multiply-defined references, 0 labels deleted.
Next: whole-paper review R4.

**Round 8a integrated (integrating editor).** What the adversarial audit `R155_061` cleared from
`R155_052` (amended in place) is now in the paper, each statement checked against the paper's own
definitions (`\Ainf = 2AB + Γ_T`, `Γ_T` of `prop:nodes`, `P_T`, `\laminfP` = bottom on the unit sphere of
`P_T`, `m`, `C₀`, `K`, `S_c`, `Λ_k` of `thm:P`) and translated to its notation (the memo's `W`, `γ`, `K`,
`ℓ`, `B`, `g_0/g_1` collide with paper symbols and are renamed `ω`, `q_Y`, `k₁`, `⟨·,χ⟩`, `𝔟`, `χ_ev/χ_odd`).
**§9.1:** parity-sector notation; **Lemma `lem:strict`** (λ_ev, λ_odd, `\laminfP` attained and strictly
decreasing; `λ_par < 0 ⟺ n_par ≥ 1`), PROVED; **Corollary `cor:Tarch`**: `0.58 ≤ T*_{∞,P} ≤ 0.60`,
`\laminfP(½log3) > 0`, `\laminfP < 0` for `T ≥ 0.60`, PROVED (machine-verified), value `≈ 0.083` DIAGNOSTIC;
`prop:arch` (i),(iv) and its remark point to them; the DIAGNOSTIC `0.5958` paragraph now keeps `0.5958` as
a Galerkin upper bound inside the certified bracket, and "primes necessary at log 2" is unconditional in
exactly one sense: `A_∞` is indefinite on `P_{log2}` with one negative direction. **§9.2:** **Lemma
`lem:parity`** (with the real/complex remark), **Theorem `thm:index`** (index 0/1/2 on `(0,0.90]`,
`T*_ev ∈ [0.58,0.60]`, `T*_odd ∈ [log2,0.81]`, `n₋ = 1` at `0.60` and `log 2`, `= 2` at `0.81, 0.82, 0.90`)
replacing "the hypothesis `n₋ = 1` … is not proved here"; `rem:P4` addendum (multi-band relaxation gives the
exact count 1 at `log 2`; the "untested" clause removed); the brackets paragraph after `thm:J` gains the
exact values; **Corollary `cor:H1`** replaces `T₂ ≤ 0.9989426` by `sup T₂ = T*_odd ∈ [log2, 0.81]` (the
`thm:J` bound kept as a remark). **§10.4:** `prop:finite(iii)` and `thm:finmod(i)` updated (deleted comb:
`RD_T` holds for `T ≤ 0.58`, fails on `[0.60, ½log N]`). **§10.7:** one pointer sentence in
`subsec:schur`. **App. A.4** (new, `subsec:enclindex`): `lem:border`, `lem:multiband`, `prop:haynsworth`,
`rem:signfix`, `prop:negplane`, `lem:polround`, `lem:zeroext`, `lem:rzero`, certified margins.
**App. C:** `rem:odd080` (n_odd(0.80), (H1)(0.80) OPEN; residual attribution and Galerkin bottoms
DIAGNOSTIC); the τ_N ≈ 60 extrapolation is not in the paper. Certificates of record:
`03-research/phase-155-row-d-flat-kernel-criterion/scripts/r8a/r8a_01_<T>_par<p>_rerun.json` (upper) and `03-research/phase-155-row-d-flat-kernel-criterion/scripts/r8a/r8a_03_recheck.json` (lower; the flag
of `r8a_02` is not a certificate). Abstract and intro gain one clause each; "What is not claimed" one
sentence; labels table and reproduction section updated. No sign for ζ beyond `log 2`; nothing here is about
`W_T` or zeros; endpoint of record unchanged. Backup `main_pre_8a.tex.bak`. Compiles at 73 pages, 0 errors,
no undefined or multiply-defined references, 15 labels added, 0 deleted.

**R4 applied (`TEX_ADVERSARIAL_REVIEW_R4.md`, verdict minor revision).** Backup `main_pre_R4apply.tex.bak`.
**R4-1:** `03-research/phase-155-row-d-flat-kernel-criterion/scripts/r8d/r8d_margin_bound.py` fixed (`H⁸ → H⁹`), re-run by the editor (7.6 s, JSON regenerated);
`rem:margin` and the label-table row now read crossings `1.430`, `2.054` (were `1.226`, `1.852`), with the script
named; App. C "five to eight" → "six to ten" orders (measured `6.3`–`9.6`); `thm:margin`, `eq:Bmargin`, `cor:margin1`
unaffected (Cor. 1 ratio `0.7550 ≤ 1`); erratum appended to `R155_055`. **R4-2:** `cor:RH` (a)⇒(c) rewritten: Fatou on
the mollification of `lem:roughEF` for a rough minimiser, real minimiser via `W_T(u+iv)=W_T(u)+W_T(v)`, distinct
ordinates via `S(t)=O(log t/log log t)` under RH (new `\bibitem{Titchmarsh}`, Thm 14.13; the supplied sentence was
made precise: the multiplicity bound is stated as a consequence of the bound for `S`). **R4-3:** `thm:SC` negative
for `T > T₀(A)`, nonpositive at `T₀(A)`; `prop:arch`(ii) endpoint via `cor:Tarch`. **R4-4:** `prop:P` zero-sum clause
restricted to real `F` with absolutely convergent zero sum; bridge sentence and intro updated. **R4-5:** `cor:H1`
domain `T₂ > T*_{∞,P}`, `T₂ ≤ log 2` via `thm:index`(i); label row updated. **R4-6:** `rem:Cheb` reading corrected.
**R4-7:** intro "any window" → "any window `T > ½log2` (`T > 0.74921` for sieve hypotheses)". **R4-8:** certificate
files of `thm:N`, `thm:Bbeta`, `thm:Np` (`03-research/phase-155-row-d-flat-kernel-criterion/scripts/r3b/r3b_enclosure_<T>_M<M>.json`, `r3b_beta_box.json`),
`thm:w11` (`03-research/phase-155-row-d-flat-kernel-criterion/scripts/r3c/r3c_04_enclosure_iv.json`, vector `r3c_02.json`), `thm:nest`
(`03-research/phase-155-row-d-flat-kernel-criterion/scripts/r4a/r4a_02_<T>.json`, vectors `r4a_01.json`) and the margin script named; every path checked. **New
(editor):** `thm:Np` displayed `Ceil(24,·)` values were the `a`-endpoints without the `β`-allowance, contradicting the
proof's own sentence; corrected to the files' `ceiling_upper_bound`: `−7.493129·10⁻⁶`, `−6.584323·10⁻⁷` (the memo's
`−6.584324` rounds the wrong way). **R4-9:** real splitting inlined in `lem:strict`; `lem:parity` remark points
there. **R4-10:** `rem:margin` names (X19′) and "whenever `λ^A > 0`". **R4-11:** `7.2151·10⁻⁶`, `4.02·10⁻²⁰`,
`10–56 s`, `c_* = 16`. **R4-12:** applied (`c₀` not needed; one-line remark that `λ_∞` and the bottom of `Γ_T` are
strictly decreasing as well, not used); note added to `R155_061`. **R4-13:** `R_T` defined at first use. **R4-14:**
`\label{subsec:where}` replaces three hardcoded `§…​.2`. **R4-15:** `lem:mbounds` pointer, `prop:finite` label
row, unused macros `\dd`, `\AT` deleted, abstract/intro threshold-bracket wording. Compiles at 74 pages, 0 errors,
no undefined or multiply-defined references, every `\cite` ↔ `\bibitem`; 1 label added (`subsec:where`), 0 deleted.
Row-D label unchanged; endpoint of record unchanged; no sign for ζ beyond `log 2`.

**Phase 156 integrated ( item 156c as cleared by `03-research/phase-156-row-d-per-window-converse/R156_004_AUDIT_CONVERSE.md`, from `R156_001_CONVERSE.md` as amended A1–A16).** Backup `main_pre_156.tex.bak`. Notation renamed per A15 (`𝔊_T`, `𝔤_ev/𝔤_odd`, `S^Sch_T`, `F^odd_T`), since `prop:finsupp` already uses `G_T`, `F_T`; the complete form is cited as `eq:W` throughout (`def:W` is the weight class).
* §9.1 **`prop:archneg`** (Prop. 9.7): `𝒜_∞(t·1_{I_T}) ≤ U(T)` (elementary closed form), `U(0.4608) ∈ [−7.0159575, −7.0159574]·10⁻⁶` in interval arithmetic, hence `λ^∞ < 0` for `T ≥ 0.4608` and **`T*_∞ ≤ 0.4608 < 0.58 ≤ T*_{∞,P}`**. PROVED; certificate `03-research/phase-156-row-d-per-window-converse/scripts/r156/audit_r156_witness_t.py` (re-run by the editor, 1.2 s). It improves the proved bound `T*_∞ ≤ 0.60`; the Galerkin `0.3716` stays DIAGNOSTIC (not "improved"). `prop:arch`(iv) now points to it.
* §10.4: the **comb-level complete form** `W_T(a) := 𝔞^{(v(a))}_T + 2Re(AB̄)` defined next to `RD_T(a)`, with the statement that it is **not** the zero sum of `ζ_a` (A7).
* §10.6 **`thm:parityschur`** (Thm 10.24; Lemma 1.0 + Thm 1.1 with the self-contained compact-resolvent/Lax–Milgram step A1, the sandwich only for `𝔤 > 0` A2, the range condition A3): per window `λ^W > 0 ⟺ [λ^A > 0 ∧ 𝔊_T ≻ 0]`, `λ^W ≥ 0 ⟺ [RD_T ∧ range ∧ 𝔊_T ⪰ 0]`, `n₋(W_T) = n₋(𝔞_T|P_T) + n₋(𝔊_T)`. PROVED. **`prop:polarcap`** (Prop 10.25): `𝔊_T = S^Sch_T + J` is the polar capacity `E_T(Φ_F(0),Φ_F(1))`. PROVED. **`cor:convfail`** (Cor 10.26; Cor 3.2 / Thm 3.3 / Cor 3.4 with A6–A9): the converse fails for `Λ1_{n≥5}` on `[0.4608, 0.58]` (odd-sector form on `[0.4608, log 2]`) and for `a_θ` at `½log 3` for every `θ ≤ 0.8148` (quintic witness, `03-research/phase-156-row-d-per-window-converse/scripts/r156/audit_r156_theta_quintic.py`, re-run 1.0 s; margin `2.8·10⁻⁸`); failure set `[0, θ_*)`, `0.8148 < θ_* < 1` (Zhu for `θ_* < 1`); method constraint (deletion-closed classes on `[0.4608, 0.58]`; classes closed under lowering one term at `½log 3`, one-sided `18.5 %`). PROVED as comb-level method constraints.
* §10.6 OPEN paragraph rewritten with the corrected chain A12: `∃Al_T ⟺ λ^W > 0 ⟺ [λ^A > 0 ∧ 𝔊_T ≻ 0] ⟹ KEP(T) indeterminate ⟹ λ^W ≥ 0`; OPEN: `RD_T ⟹ λ^P ≥ 0` per window, the effective window shift for ζ, the converse for ζ at `T > 0.8`. §11.1 item (5) no longer says indeterminacy is "exactly" `λ^W > 0`; §10.1 gains a sentence that the chain is an all-`T` statement.
* **Citation slip A14 corrected** (no mathematics changed): `prop:arch`(iii) now cites the complete form at autocorrelation support `≤ log 2` [Yoshida, Bombieri] (and, certified, [Zhu, Thm 1.2]), Paper 42 dropped; "What is not claimed", intro l.148, §5 opening, §6.4 and `rem:twohalves` now name the form (primitive: `T ≤ log 2` Paper 42, `½log 3` Thm C, `≤ 0.8` via Zhu; complete: `T ≤ ½log 2` classical, `(½log 2, 0.8]` Zhu alone; nothing in the paper proves `λ^W ≥ 0` at any `T > ½log 2`).
* App. C **`rem:polarcapdiag`** (DIAGNOSTIC only): Galerkin `𝔤_±` (upper bounds; positive values carry nothing), `S^Sch ≈ −J`, `θ_* ≈ 0.99991`, channel crossings `≈ 0.372 / 0.44`. Not integrated: the doubly-exponential thinness heuristic, the zero-side Remark 2.2, the extension of the failure to all of `(T*_∞, T*_{∞,P})`.
* Format fix: the §11.2 label table was a single `tabularx` overflowing its page (pre-existing `Overfull \vbox 1444pt`; every row after `cor:Tarch` was cut off in the PDF); it is now a `longtable`. Label rows added for the five new labels and the chain.
Compiles at 84 pages, 0 errors, no undefined or multiply-defined references, every `\cite` ↔ `\bibitem`; 5 labels added (`prop:archneg`, `thm:parityschur`, `prop:polarcap`, `cor:convfail`, `rem:polarcapdiag`), 0 deleted. Row-D label unchanged; endpoint of record unchanged; no sign for ζ at any new window.


**Phase 157 integrated (integrating editor; items cleared by `03-research/phase-157-row-d-mechanism-search/R157_004_AUDIT_SEARCH.md` §5 and `R157_006_AUDIT_BERKOVICH.md` §12, from `R157_002` (O3, O4, Lemmas C, D) and `R157_005` (Lemma 3.3) as amended).** Backup `main_pre_157.tex.bak`. Checked against the paper's own definitions (`eq:W`, `eq:Aform`, `𝔞_T`, `P_T`, `\lamA`, `λ^W`, `c_F(u) = ∫F(t)F̄(t−u)dt`, `thm:finmod`, `cor:margin1/2`, `lem:cpos`, `thm:Z`, `def:PD` (D), `prop:P`). The autocorrelation `c_{F⋆}` is used throughout, not `Φ` (`Φ_F` is the Mellin-type transform of `eq:W`).
* §2 **`lem:contT`**: `T ↦ λ^W_T` is continuous (dilation `U_r` plus the relative form bound `‖F‖²_Q ≤ W_T(F) + C′‖F‖²`; R157_004 Lemma C, written in the paper's normalisation), stated as a direct proof of Bombieri 2000 Thm 5 (`λ^W = min(μ₊, μ₋)`); also for `λ^∞`; nothing for `λ^A`, `λ^P` (`U_r` does not preserve `P_T`). PROVED, no novelty claimed.
* §7.1 **`rem:normline`** after `thm:Z`: norm-line kernels `H(ℓ(x) − ℓ(y))` on `A^{1,an}_Z` realising `W_T` are exactly problem (D) at `β = (2,0)` (R157_006 Lemma B.3); "⇐" weak duality, "⇒" `thm:Zexh`(i) in ε-form; complete form; restatement, not a new object. Bibitem `Poineau2010` added.
* §7.4 **`rem:nonzero`** after `thm:KEP3`: one-sentence RESTATEMENT, RH ⟺ `λ^W_T ≠ 0` for every `T` (Bombieri Thms 1, 3, 5; P45 Thm 10.4); if RH fails, `{T : λ^W = 0}` is a nonempty compact interval (compactness via Zhu, cited). **No "determinate" clause; no novelty claim.** Lemma E of R157_004 is **not** integrated: §5 of the audit does not clear it for the paper, and small-window positivity is already cited (`prop:arch`(iii), `cor:KEP08`).
* §10.4 **`cor:Qp`** after `lem:cpos`: `Q_p(F^±_φ) = ∓v_p‖φ‖²`; each local prime form is negative definite on an infinite-dimensional subspace of `P_T` for every `T > ½log p` (R157_006 §4, stronger form of R157_005 Lemma 3.3), with the (b′) reading: positivity is never place by place, indefinite summands do not forbid a positive sum. PROVED, no sign.
* §10.4 **`rem:resweights`** + **`lem:degen`** after `thm:finmod` (O3 amended A1–A5): `ε_*(T,n₀) = √n₀ λ^A_T/(2|c_{F⋆}(log n₀)|) ≤ 2·10⁹Te^{−14.449T}/|c_{F⋆}(log n₀)|` (`15.449`, prefactor `2√2·10⁹` at `n₀ = 2`); an upper bound (≤, not ≍); vacuous for `T ≤ 1.51`; sign restriction (lowering needs `Λ(n₀) ≥ ε`); primitive form, complete form through the `W_T`-minimiser `F^W`; non-degeneracy OPEN; Lemma D PROVED (if a minimiser has `c ≡ 0` on `log N_T`, `v_T(Λ)` globally maximises `V_T(v) = λ_min(A^{(v)}_T|P_T)`). **Placement:** the audit proposed "after `cor:margin2`", but the remark uses `RD_T(a)`, `𝔞^{(v)}_T`, `v_T(Λ)`, `W_T(a)` of §10.4, defined after §10.3; it sits after `thm:finmod` (whose proof it applies), and `rem:margin` now ends with a pointer to it.
* **Sentences changed:** `prop:arch` proof ("no continuity being asserted" → continuity for `λ^∞` by `lem:contT`, not asserted for `λ^{∞,P}`, not used); §10.2 class-value paragraph ("no continuity in `T` is claimed for it" → continuous by `lem:contT` / Bombieri Thm 5, no continuity claimed for the sub-classes); `rem:margin` (pointer sentence); "What is not claimed" (one sentence on the new items). Label table: 5 rows added.
Compiles at 86 pages (84 before), 0 errors, no undefined or multiply-defined references, every `\cite` ↔ `\bibitem`, overfull boxes unchanged (9, all pre-existing); 6 labels added (`lem:contT`, `rem:normline`, `rem:nonzero`, `cor:Qp`, `rem:resweights`, `lem:degen`), 0 deleted. Row-D label unchanged; endpoint of record unchanged; no sign for ζ at any window, in either form.
