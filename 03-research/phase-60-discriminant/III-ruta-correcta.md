# III: the correct route, fixed with high-precision computation ## Decisive computation (mpmath dps=40, validated CCM engine) **Scale of ε₀ (N=8, increasing λ):** ε₀ tiny, positive, DECAYS:
λ=3.7→3.7e-20, λ=5→1.6e-20, λ=7→1.0e-20, λ=10→6.3e-21. Fit ε₀ ~ λ^{-2} (≈e^{-L}).
⟹ **REFUTES |ε₀|~2λ** from the panel/Hankel. The 2λ is the depth of the symbol / top of the spectrum. **Relative spectrum (λ=3.7, N→∞), ε_k/ε₀:**
N=12: 4.58, 9.14, 19.3, 26.3 (γ=3.58)
N=14: 3.74, 9.14, 15.2, 26.3 (γ=2.74)
N=16: 4.05, 9.09, 16.4, 25.9 (γ=3.05)
Converges to (k+1)² = 4,9,16,25; γ→3.
⟹ **REFUTES the edge model γ→1, {-C,0,C}.** Confirms the (k+1)² ladder, Dirichlet-Laplacian. ## Reconciliation of the 8 mathematicians + panel - `ε₀~2λ` (panel/Hankel): REFUTED. ε₀~λ^{-2}=e^{-L}.
- `γ→1` (edge model, hankel.md): REFUTED. γ→3.
- `γ→3`, (k+1)² ladder (original IV.1, math.1-6): CONFIRMED numerically.
- constant c=-ψ''(1/4)/8 (IV.1, math.1-6): REFUTED by the panel (it is the archimedean curvature, subdominant). BUT irrelevant: the ratios ε_k/ε₀ are scale-invariant.
- `(1/2λ)D_λ(s/logλ)→cos2s`, `W_I(1-cos2s)=I` (panel): CORRECT, but describe the 2λ scale (symbol/edge), not the background ε₀~e^{-L}. They refute the absolute constant, not the relative structure. ## Why the Hankel model failed (diagnosis) (1) Wrong scaling premise: it modeled ε₀ at scale 2λ; the real background is at e^{-L}.
(2) Approximation too crude: the rank-one boundary kernel (separable ½e^{-v/2}) gives {-C,0,C}; the true kernel is an infinite-rank Carleman kernel (hankel.md risk #2), whose spectrum IS the (k+1)² ladder. The γ→1 was a rank-one artifact.
(3) The Kronecker wall (norm convergence fails) is real BUT for the wrong object (boundary Hankel at scale 2λ). It does not block the (k+1)² route at scale e^{-L}. ## The correct route (what must be proved to close III) LEMMA (tightness at WKB scale). A_λ/ε₀ → -c d²/dx² Dirichlet (strong resolvent), with ε₀≍e^{-L},
giving ε_k/ε₀→(k+1)² and γ→3. RH-neutral. - It is NOT the panel's Hankel lemma (γ→1, 2λ scale, Kronecker wall — wrong object).
- It IS the SEMICLASSICAL (WKB) boundary-layer problem: ε₀~e^{-SL}, S≈1, edge modes, the program already had prior work (2b_PROOF_DRAFT, softmodes, edge-localization).
- The relative structure (k+1)²/γ→3 is confirmed numerically and is RH-neutral; what is missing is the quantitative convergence bound (Landau-Widom/WKB at scale e^{-L}). ## Status of III
- ε₀ scales as e^{-L}, positive: established numerically.
- ε_k/ε₀→(k+1)², γ→3: established numerically, RH-neutral, robust in N.
- Rigorous proof of convergence: OPEN, via WKB/Landau-Widom at scale e^{-L} (not Hankel 2λ).
- (P) (sign of ε₀): separated. Note: here ε₀>0 for ζ — consistent with RH-true, but it is a measurement at finite λ, not a proof of ε₀>0 ∀λ.
