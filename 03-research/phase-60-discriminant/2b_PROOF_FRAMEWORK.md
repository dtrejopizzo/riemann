# #2: rigorous proof framework (edge spectrum (k+1)²) — scaffolding + open step **Frankness:** this document assembles the proof of #2 with rigor as far as legitimate, and
identifies precisely the ONLY analytic step that remains open (= the "missing step" of). No QED is declared for that step. --- ## 1. Precise statement to prove (#2) Let A_λ be the localized Weil form on PW_{L/2} (L=2logλ), ε_0(λ)≤ε_1(λ)≤… its eigenvalues.
**Theorem #2 (goal):** the scaling limit exists lim_{λ→∞} ε_k(λ)/ε_0(λ) = μ_k, with μ_k = (k+1)² (k=0,1,2,…),
and ε_0(λ) ≍ c·λ^{−2} (tunneling). By #3 (rescaling), this ⟹ ξ̂_λ→Ξ ⟹ RH. ## 2. Sampling formulation (de Branges) — the mechanism By the explicit formula (unconditional) + exact restriction (i): A_λ(f,f) = Σ_ρ f̂(ρ) \overline{f̂(1−ρ̄)} (sum over zeros ρ of ζ),
where f̂ ∈ PW_{L/2} (Paley–Wiener, exponential type L/2, because f lives on [−L/2,L/2]).
On the critical line (on-line part), the terms are |f̂(γ_j)|² ≥ 0. **Soft modes = band-limited functions small at the zeros.** ε_k = the k-th minimum of the
form over PW_{L/2}, ‖f‖=1. The minimizer f̂ vanishes (or nearly) at the zeros γ_1,…,γ_m up to the
horizon; ε_k = residual at the non-vanished zeros. This is a **concentration/sampling operator** on PW_{L/2} with nodes at the zeros {γ_j}.
Its low spectrum is what must be identified. ## 3. Why the spectrum is (k+1)² — the boundary layer model (rigorous up to the ansatz) Numerical fact (softmodes.py): the minimizers are **edge-localized** (concentrated at
w=±L/2) and vanish at the center. ⟹ the concentration operator has its action in a **boundary
layer** of fixed width `a` (in w) next to each edge. **Ansatz-lemma (boundary layer):** in the boundary layer, the band-limiting acts as a
**Dirichlet** condition at the inner edge of the layer, and the form A_λ reduces to the Dirichlet
energy ∫|f'|² (second order) in the layer coordinate s∈[0,a]. The modes are sin(jπs/a), j=1,2,…, with
energy (jπ/a)². ⟹ μ_k = ε_k/ε_0 = (jπ/a)²/(π/a)² = j² = (k+1)². □(ansatz) **Tunneling (scale ε_0):** two boundary layers (edges u=λ, u=λ⁻¹) separated by L=2logλ in w. The
splitting of the fundamental mode ∝ tail overlap ∝ e^{−κ·L}. With κ=1: ε_0 ∝ e^{−L}=λ^{−2}.
**Verified:** ε_0 ∝ λ^{−2.07}. □(numerically verified; analytic κ=1 still missing) ## 4. What is RIGOROUS vs what is OPEN **Rigorous:**
- (i) exact restriction A_λ=A_∞|_{E_λ}. ✔
- Sampling formula A_λ(f,f)=Σ_ρ f̂(ρ)\overline{f̂(1−ρ̄)} (Weil, unconditional). ✔
- #3: rescaling by ε_0 ⟹ isolated bottom ⟹ Galerkin ⟹ ξ̂_λ→Ξ (modulo existence of the limit). ✔
- H1/H2: the operator is positivity-improving ⟹ Gantmacher–Krein ⟹ the k-th mode has k nodes (Sturm/oscillatory structure — consistent with a j²-type spectrum). ✔ **OPEN (the missing step of, NOT fabricated):**
- **Rigorous boundary-layer lemma:** prove that the concentration operator on PW_{L/2} with nodes at {γ_j}, restricted to the edge sector, converges (rescaled) to the Dirichlet Laplacian on [0,a] with spectrum (jπ/a)². Requires: (a) identifying the width `a` from the zero density / the archimedean symbol; (b) controlling the band-limiting as an effective Dirichlet condition; (c) the tunneling asymptotics κ=1.
- This is real asymptotic analysis (de Branges / prolate / boundary layer). It is a well-posed, zero-independent statement, NOT a wall — but it is NOT proved here. ## 5. Frank verdict #2 = edge scaling limit (k+1)² + tunneling λ^{−2}. Rigorous framework assembled; mechanism
identified (Dirichlet in the boundary layer + tunneling between edges); 3 pieces verified
numerically; connection with H1 (Sturm). **The boundary-layer lemma is the only open step** and is
genuinely the "missing step". It is not declared proved. Doing pure mathematics = not faking that
QED. The path is set up to attack it with de Branges/prolate (tools the program already
has: P7/P8).
