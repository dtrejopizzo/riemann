# CHANGES_BRIDGE — Paper 47, positive regions of the exterior form and the Möbius lattice

Backup: `main_pre_bridge.tex`. New subsection `subsec:ext-pos` (§22.4, pp. 165–171 of 186) inside `sec:ext`, before
`subsec:ext-constraints`. Notation adapted to the paper: memo μ (bandwidth) → N (μ(·) is Möbius in sec:ext); cell index → J;
prolate concentration χ_k (paper), ODE eigenvalue ϑ_k; Lévy kernel ν = K/2 (lem:K); comb weight c′ (𝔔^{c′}); weights v_n = 2Λ(n)/√n.

Contents and labels (audited sources only):
- Conventions: Hermitian extension of 𝔔, w(t,ν), 𝔴_N, prolate phase φ_c, 𝔔^{c′}.
- lem:ext-weight (weight lemma: F(J) ∈ [0, γ log J + 1], 𝔴_N ≥ log 2N for N ≥ 4) — proved.
- lem:ext-cell (disjoint dilates, gap 2δ/J; exact comb −2‖ρ‖²Σ(w∗1)(n)/n; exact decomposition) — proved.
- lem:ext-osc (oscillatory log-symbol, corrected K₂ coefficients 1,6,2,12) — proved given Stirling remainder (sketch).
- thm:ext-cell (single-cell chirps, explicit E_arch/E_cross/E_pole) — proved; key log² cancellation explained.
- cor:ext-cellpos (positive region, logarithmic threshold) — proved.
- cor:ext-cfals ((i) scope note: high-frequency single-cell cone only; (ii) falsifier for every c′ > 1 uniform in J, also a
  window-form negative direction at T₀ = ½log(J+1); (iii) fixed J) — proved.
- lem:ext-phase (s_n = √(1+n⁻²), Hessian, concavity, no stationary point 2 ≤ m < n, resonant weight log(N(1+n⁻²))) — proved.
- thm:ext-multi (multi-cell chirps) — proved as asymptotic (fixed η, X, profile); non-uniformity in X stated.
- thm:ext-layer ((i) closed form (2/3)log 4N − Cl₂(2π/3)/(2π), proved; (ii) regular singular point, J₀, width c⁻², proved;
  (iii) layer diagonal, conditional on the cited uniform envelope and normalisation; (iv) amplitude product exact,
  resonance leading term with w₂, w₃ — stationary-phase remainder not proved); comb-weight remark (algebra).
- thm:ext-lattice (Möbius-lattice structure + jets) — proved, full proof.
- prop:ext-grouped (grouped identity, c_{b/a} = μ(a)M̃_a(N/a)/a, d_{b/a}, coincident-line coefficient μ(m)μ(nm)/(nm²),
  |M̃₁| ≤ 1, Euler-factor identity) — proved.
- prop:ext-latred (exact reduction vᵀGv on the lattice class) — proved; the inequality itself open.
- rem:ext-latno (three excluded mechanisms, falsifier transport) — proved.
- rem:ext-latnum (N = 15 numbers) — numerical, not used in proofs.
- Bibliography: Stein1993, Olver1974, Dunster1986, OsipovRokhlinXiao2013.

Not integrated: real-chirp remark (argued), Fresnel worst case (argued), truncation-jump estimate (argued), the coprime
bound |M̃_a| ≤ 1 for a ≥ 2 (cited only in the source; replaced by the proved Euler-factor identity), the coefficient table at
N = 15, the "semiring" reading of the layer. No sign of row D is claimed; no closing chapter added.
Compiled pdflatex ×3: no errors, no undefined references, 186 pages.

## : uniform envelope for thm:ext-layer(iii) (backup `main_pre_cc.tex`)

Source: `03-research/phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_CC_001_ENVELOPE.md`, adversarial audit
`AUDIT_L_SHARP_14.md` (verdict: ACCEPTED WITH ERRATA). New lemma `lem:ext-envelope` ("the uniform prolate envelope; proved")
inserted in §22.4 immediately before `thm:ext-layer`, replacing the cited Olver/Dunster uniform asymptotic expansion by a
self-contained adiabatic-invariant (modified Prüfer) argument on $t>1$:
- exact identities $(\log G)'=2\varepsilon\cos2\phi$, $\phi'=\Omega-\varepsilon\sin2\phi$ for
  $G=\sqrt P\psi^2+(p\psi')^2/\sqrt P$, $P=(t^2-1)(c^2t^2-\vartheta_k)$ ($\vartheta_k$ the differential eigenvalue, not the
  concentration $\chi_k$), and the monovariant $E=G/\sqrt P$ decreasing, giving $|\psi(t)|\le|\psi(1)|$;
- explicit envelope $G=G_\infty e^x$, $|x|\le(1.45/\sqrt{t^2-1}+2.77)/c$; Langer bound $1.57\,C_c(t^2(t^2-1))^{-1/4}$ for
  $c\sqrt{t^2-1}\ge2$; uniform Bessel-zone bound $10.3\,C_c\sqrt c\,(1+z)^{-1/2}$ via $\psi(1)^2\le35\,G_\infty$;
- normalisation $C_c^2=\frac2\pi(1-\chi_k)(1+e_1)$ and layer diagonal $\int_1^2\mathfrak w_N\psi_k^2=\tfrac12(1-\chi_k)D_{\mathrm
  lay}(N)(1+\eta)$ with explicit $|\eta|\le(21.4\log c+1.54\vartheta_k/c+523)/(c(1-|e_1|))$, $|e_1|\le0.77\nu+(5.14\log(c/2)
  +106.2)/c$, $\nu=\vartheta_k/c^2$, valid under $(H_\nu)$: $\vartheta_k\le c^2/4$, $c\ge200$.

`thm:ext-layer` retitled "(i)–(iii) proved under the hypothesis $(H_\nu)$ ..., (iv) open" (was "conditional on the uniform
prolate envelope"); part (iii) restated with the explicit $\eta$-bound in place of "$(1+o(1))$" under the assumed expansion,
citing `lem:ext-envelope`(d) instead of Olver1974/Dunster1986/OsipovRokhlinXiao2013 for the diagonal (OsipovRokhlinXiao2013
is kept only for the $\vartheta_k$ asymptotic used to verify $(H_\nu)$ for fixed $k$); proof sketch of (iii) now points to
the lemma. Part (iv) is unchanged and stays open (stationary-phase remainder not controlled; it also still uses the full
oscillatory phase expansion, which `lem:ext-envelope` does not supply).

Honest remark added: the explicit $\eta$-bound is non-vacuous (i.e. $<1$) only for $c\gtrsim820$ ($N\gtrsim130$); for
$200\le c<820$ the statement is proved but the bound is vacuous, and at $N\le130$ any numerical use of the layer diagonal
stays NUMÉRICO, not PROVED. Per errata in AUDIT_L_SHARP_14: the Bessel-zone constant $\kappa=1.159$ (not 1.156, the
constant $35$ survives unchanged); the wording "meaningful but crude at $c=200$" from the source proof memo is NOT carried
into the paper, since the audit found the bound exceeds 1 at $c=200$.

Notation checked against the paper: $\chi_k$ = $L^2(\R)$ concentration (one-sided mass $\tfrac12(1-\chi_k)$), $\vartheta_k$
= differential eigenvalue of the prolate ODE (distinct from $\chi_k$); $\mathfrak w_N(t)=\log(Nt^2/\sqrt{t^2-1})$ on $(1,2)$
unchanged. No sign of row D is claimed; row D remains open.

Compiled pdflatex ×3: no errors, 187 pages (was 186).
