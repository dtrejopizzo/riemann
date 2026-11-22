# R166_201 — Sine/cosine coupling at the contact node, along the T-flow, and the atomic-sampling test

Phase 166, round 7. Inputs: R166_190 §0 + round-6 synthesis; R166_101 Thm 2.1; R166_103 L2; R165_201 Thm 2, Cor 2.2;
R165_202 Thm 3.1; R163_401 §1.1, 2.4(iii)–(iv), Lemma 3.1, Lemma 3.3, Lemma 3.4, §4.4, Lemma 4.10. Corpus check: the
cancellation in Thm 1.1 below is the exact-phase form of R166_101 Thm 2.1 / R163_401 §4.4; Thm 1.3 (jet hierarchy) and
Thm 1.2 (tautology of S′ = d) are not stated in prior memos in this form (grep of phase-163..166 for "jet", "S^{(k)}",
"tautolog": no hit on this content).

## Status

| # | Statement | Label |
|---|---|---|
| 1.1 | **Exact node-term phase.** Quartet term of S′(x₀) = 2Re Q(t_q)², Q := G/(z−x₀); arg Q(t_q) ≡ E (mod π). The geometric angle ψ cancels exactly: 2φ+2ψ ≡ 2E | PROVED |
| 1.2 | "S′(x₀) = d_{x₀}" with d from 2.4(iv) is (1.1) applied to the test H_{x₀}; it holds for **every** real-rooted F (witness or not), carries no constraint. The witness content at nodes is only S(x)=0 (kernel equation) and d_x ≥ 0 | PROVED (E1) |
| 1.3 | **Jet hierarchy.** Quartet term of S^{(k)}(x₀) = 2k!\,\|Q(t)\|² r^{1−k} cos(2E+(k−1)ψ); Re g² = \|Q\|² r² cos(2E−2ψ) is the formal level k = −1, below every node jet | PROVED |
| 1.4 | Hence no quantity built from d_{x₀} (any bound, atomic or not) reads sign Re g²; ψ enters node data only through S^{(k)}(x₀), k ≠ 1, i.e. through the kernel equation (k=0) and its jets — E1 | PROVED |
| 2.1 | Im g² does not occur in W_T(F_T), B(T), or dλ_T/dT; no sign of sin2Θ implies a sign of cos2Θ | PROVED |
| 2.2 | Lattice extremal (node at γ_q): Im g² = −2δ³G′(x₀)²S₀(1+O(δ)), S₀ = −G″/(2G′)(x₀); the R166_103 singular term −Im g²/δ is O(δ²): dormant; its sign is sign(S₀), set by node asymmetry, indefinite | PROVED |
| 2.3 | Sine-channel Lyapunov route: DEAD (E1; M_m's flow satisfies every identity used) | PROVED |
| 3.1 | Atomic sampling Σ v_n k_F(x₀, log n): no sign property usable — k_F(x₀,·) oscillates with period 2π/x₀; the atomic-minus-density part is the explicit-formula oscillation (zeros again) | ARGUED |
| 3.2 | Even granted any bound on d_{x₀} separating ζ from β_m, 1.4 makes it ψ-blind: it cannot decide (★_cell) | PROVED |
| (★_cell), row D | | OPEN (unchanged) |

## §1 The sine–cosine coupling at the node

Notation: G real LP (R163_401 Lemma 3.1(a)), X its nodes, t = t_q = γ − iδ, x₀ ∈ X nearest γ, Q(z) = G(z)/(z−x₀),
t − x₀ = r e^{−iψ}, r > 0, ψ ∈ (0, π) (ψ = arctan(δ/(γ−x₀)) when γ > x₀; ψ = π/2 when γ = x₀).
By Lemma 3.3: g = G(t) = ±|g|e^{iΘ}, Θ = φ₀ + E, φ₀ = arctan(δ/(x₀−γ)) ≡ −ψ (mod π), E = Σ_{x≠x₀} arctan(δ/(x−γ)).

**Theorem 1.1. PROVED.** Q has nodes X∖{x₀}; by Lemma 3.3 applied to Q (same proof, one factor removed) arg Q(t) ≡ E
(mod π). Hence g²/(t−x₀)² = Q(t)² = |Q(t)|² e^{2iE}, and the quartet's contribution to S′(x₀) is
2Re Q(t)² = 2|g|² cos2E / r² (partners at −x₀ analogous). Equivalently with φ = arg g: 2φ + 2ψ ≡ 2E (mod 2π). The
proposed mixed term 2|g|²cos(2φ+2ψ)/r² is therefore exactly 2|Q|²cos2E: the node's own angle cancels identically. ∎
(This is R166_101 Thm 2.1 at the level of phases.)

**Theorem 1.2 (tautology). PROVED, E1.** For any F ∈ D_T and x ∈ X, H_x ∈ D_T, and W(H_x) is computed two ways: by the
prime-side form (eq:form; Paper 46) and by (1.1) (zero side). Both equal W(H_x) for every F. 2.4(iv) is the prime-side
evaluation of W(H_x,·) paired with F (R162_2202), hence also an identity valid for ζ. So "S′(x₀) = d_{x₀}(window)" holds
for all real-rooted F at all T and constrains nothing; F_1(X,Γ) = d_{x₀}(window) is not an equation on X. The only
witness-specific node data are S(x) = 0 ∀x ∈ X (W(F,H_x) = 0, the kernel equation) and W ≥ 0. For M_m the same holds
with its own window (β_m). ∎

**Theorem 1.3 (jet hierarchy). PROVED.** S^{(k)}(x₀) = k! Σ_ρ g_ρ²/(t_ρ−x₀)^{k+1}. Quartet term:
g²/(t−x₀)^{k+1} = Q(t)² (t−x₀)^{1−k} = |Q|² r^{1−k} e^{i(2E+(k−1)ψ)}. So the term is 2k!|Q|²r^{1−k}cos(2E+(k−1)ψ):
k=0 (kernel equation S(x₀)=0): cos(2E−ψ)·r; k=1 (weight d): cos 2E; k=2: cos(2E+ψ)/r; and
Re g² = |Q|² r² cos(2E−2ψ), the k = −1 slot. ∎

**Corollary 1.4. PROVED.** The sign of Re g² (decides (★_cell)) is cos(2E−2ψ). The weight d_{x₀} sees only cos2E; with
(|Q(t)|, E) fixed, ψ ranges over (0,π) by moving γ inside the cell and cos(2E−2ψ) takes both signs. Therefore any
inequality on d_{x₀} — in particular every prime-side bound via 2.4(iv), atomic or not — is ψ-blind. ψ reaches node data
only through the jets k ≠ 1, the first being S(x₀) = 0 (kernel equation, E1; M_m satisfies it, R165_202 §4.2). Decomposing
cos(2E−ψ) = cos2E cosψ + sin2E sinψ: the sine channel at node level is exactly the kernel equation's ψ-part. ∎

## §2 The flow T < T_c

B(T) = λ_T‖F_T‖² = W_T(F_T) = Σ_on |G_T(γ)|² + 2Σ_q Re G_T(t_q)² (+polar), continuous, B(T_c) = 0 (R165_202).

**Theorem 2.1. PROVED.** Im G_T(t_q)² does not occur in B(T) (W depends on Ĝ Ĝ^# at t_ρ, and quartet pairing gives
4Re g², Lemma 3.1(c)). dλ_T/dT (Hellmann–Feynman, Paper 46 lem:monoT) is a boundary/kernel expression with no Im g² term
either. Any statement "sin2Θ_T has a fixed sign for T < T_c" leaves cos2Θ_T free: for Θ ∈ (0,π/2), sin2Θ > 0 and cos2Θ
takes both signs. So no implication sine-sign ⟹ cosine-sign at T_c exists without an extra relation, and the only
available relations are 1.2–1.4 (E1). ∎

**Proposition 2.2 (lattice extremal). PROVED.** R163_401 Lemma 4.10 / R166_101 2.4: node at γ_q, ψ = π/2. Then
Θ = π/2 + E (mod π), E = δS₀ + O(δ³), S₀ = Σ_{x≠x₀}1/(x−x₀) = −G″(x₀)/(2G′(x₀)) (Lemma 3.4(c)), |g|² = δ²G′(x₀)²(1+O(δ)).
So Re g² = |g|²cos(π+2E) = −δ²G′²(1+O(δ)) < 0 and Im g² = |g|² sin(π+2E) = −2δ³G′(x₀)²S₀(1+O(δ)). The sine channel
vanishes to first order; the R166_103 L2 singular term −Im g²/δ = 2δ²G′²S₀ = O(δ²), not singular. Its sign is that of S₀
(left/right asymmetry of the neighbouring nodes): indefinite, model-dependent. In the extremal configuration where (★_cell)
fails most, the sine channel is dormant. ∎

**Corollary 2.3. PROVED.** The sine-Lyapunov route is DEAD: (i) Im g² is absent from B, λ, dλ/dT (2.1); (ii) its
sign is indefinite and its size O(δ³) at the cone vertex (2.2); (iii) the only ties between the channels are 1.1–1.4, all
zero-side identities satisfied by M_m's continuous flow (R165_202: no jumps, simple λ, continuous nodes — all E1). Killer: E1.

## §3 Falsifier test: atomic sampling at the adjacent node

2.4(iv): w_{x₀}F̂′(x₀) = 𝔄_F(x₀) + Σ_{n<e^{T_c}} v_n k_F(x₀,log n) − 2A(F)x₀/(x₀²+¼), v_n = 2Λ(n)/√n ≥ 0.

**3.1 (sign structure). ARGUED.** k_F(x₀,u) = ∫_u^{T} F(s) sin(x₀(s−u)) ds is O((T−u)²) at the edge and oscillates in u
with period 2π/x₀; for γ_q at height x₀ ≫ 1 and the sampled range log n ∈ [log 2, T), it changes sign O(x₀T) times, so
v_n ≥ 0 gives no sign of the sum. Atomic minus density: Σ v_n k(log n) − ∫ k(u)·2e^{u/2}du = −Σ_ρ (Mellin of k at ρ) +
archimedean (explicit formula on the window), i.e. the difference is again the zero sum — the same quantity d being
evaluated. A ζ-vs-β_m separation via this sum is W2/E1, not new.

**3.2 (decisive). PROVED.** Independently of 3.1: whatever true bound d_{x₀} ≤ B_ζ(window) ζ satisfies and β_m violates,
Cor 1.4 shows d_{x₀}'s quartet part is 2|Q|²cos2E, ψ-blind, while (★_cell) is sign cos(2E−2ψ). A bound on d cannot decide
(★_cell). Λ ≥ 0 enters non-linearly through x₀ = x₀(F), but only into ψ-blind data. This is the exact stop of the
proposed non-linear entry point of Λ ≥ 0. ∎

## Exact stop

The quartet sign is the k = −1 member of the jet hierarchy cos(2E+(k−1)ψ) at the adjacent node. Node weights (k = 1)
are ψ-blind; ψ enters only via S(x₀) = 0 and higher jets, which are the kernel equation (E1), satisfied by M_m. The
prime side reaches the node only through d (k = 1) by 2.4(iv). So the atomic arithmetic cannot reach ψ at the node.
**Required (not available):** a prime-side identity evaluating the k = 0 jet (i.e. W(F,H_{x₀}) or ∫ of S) with a
ψ-sensitive atomic term — but W(F,H_x) = 0 is identically the kernel equation, whose prime-side form is F's own
eigen-equation (window data, f_t). Both walls of §0 are met: zero side (1.2–1.4, M_m), prime side (3.1–3.2, f_t/W2).

## Ledger

- PROVED: 1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 3.2.
- ARGUED: 3.1 (sign structure of k_F; atomic − density = explicit-formula zero sum).
- DEAD: sine-cosine node coupling (E1); sine-channel Lyapunov along the T-flow (E1); atomic sampling at the adjacent node
  as non-linear Λ ≥ 0 entry (ψ-blind; E1/W2).
- OPEN: (★_cell); row D.

## Grid cells

- **7A** (zero side × one window): +PROVED-TOOL 1.1 (exact phase cancellation), 1.3 (jet hierarchy cos(2E+(k−1)ψ)),
  2.2 (sine channel dormant at cone vertex, O(δ³)). Routes "sine/cosine coupling at node", "sine Lyapunov": DEAD [E1].
- **7E** (flow in T): +2.1 (Im g² absent from B, λ, dλ/dT); route DEAD [E1].
- **2A** (prime side × one window, node identity 2.4(iv)): +1.2 (S′ = d is a tautology for every F), +3.2 (d is ψ-blind;
  no bound on it decides (★_cell)); 3.1 ARGUED. Route "atomic sampling at adjacent node": DEAD [ψ-blind].
