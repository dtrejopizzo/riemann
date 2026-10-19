# O-4b: analytic derivation of the effective operator 𝓛 (in progress, with markers) Goal (reformulation): identify 𝓛 = lim (1/ε_0)A_λ. Method: let the operator
reveal its equation, deriving from A_λ = M_θ − V in coordinate w (then x=w/L). ## Step 1 [DERIVED] — the second order comes from M_θ, exact coefficient Archimedean symbol Ω(t) = −logπ + Re ψ(¼+it/2). By the Lévy representation (proved in
H1): Ω(t) − Ω(0) = ∫_0^∞ (1−cos tξ) dν(ξ), dν(ξ)=2e^{−ξ/2}/(1−e^{−2ξ})dξ ≥ 0. On semiclassical modes (smooth at scale L; frequency t ~ (k+1)/L → 0), 1−cos(tξ)≈½(tξ)²: Ω(t) ≈ Ω(0) + (C_2/2) t², C_2 = ∫ξ² dν(ξ).
Multiplying by t² IS −d²/dw². Therefore: **M_θ ≈ Ω(0) I + c (−d²/dw²), c = C_2/2 = −ψ''(¼)/8 = 16.16597… (exact).**
Verified: C_2 (Lévy integral) = −ψ''(¼)/4 = 32.33193498 (match to 12 digits). c>0 ⟹ elliptic. **This is the analytic, non-imposed origin of the 2nd-order operator.** The coefficient is a
special value of ψ. [Rigorous for M_θ on smooth modes.] ## Step 2 [STRUCTURAL] — the boundary is essential; the potential arises from the primes Analogous expansion of V f(w)=Σ_{n≤λ²}Λ(n)n^{−1/2}[f(w−log n)+f(w+log n)] for smooth f would give V ≈ 2P_λ I + Q_λ d²/dw², P_λ=Σ Λ(n)/√n ~ 2λ → ∞ (PNT).
⟹ A_λ would have constant Ω(0)−2P_λ → −∞, **contradicting A_λ ≥ 0**. The bulk expansion FAILS. **Resolution:** translations by large log n **fall outside the support** [−L/2,L/2]; the boundary
truncates them. That is why (a) the modes are edge-localized; (b) the problem is a BOUNDARY LAYER one; (c) the
effective prime term is **w-dependent**: the set {n: w±log n ∈ support} depends on
w. Near the center w=0 (u=1) more primes fit (symmetric) ⟹ **accumulation ⟹ potential W(w)
singular at the center** = the observed central singularity (reveal_L.py: V→∞ at x=0). ## Conjectured effective form (to be derived in Step 3) 𝓛 ∝ (c) (−d²/dx²) + W(x), W(x) singular at x=0 (centrifugal/Bessel),
at x=w/L ∈ [−½,½]. The 2nd order [Step 1, derived]; W from the sum of primes truncated by the
boundary [Step 2, structural]; spectrum (k+1)² and scale ε_0~e^{−L} arise from the archimedean↔primes
balance (= Weil's explicit formula), residual = horizon (Lemma 2). ## Step 3a [DERIVED + VERIFIED] — the arithmetic boundary law N_λ(w) (Narrowing of: first derive the count of allowed translations from w.) Support I=[−L/2,L/2]=[−logλ,logλ]. Conditions w±log n ∈ I ⟺ n ≤ λe^{−|w|} (< λ², non-binding).
By partial summation with ψ(t)~t (PNT): Σ_{n≤X}Λ(n)/√n = 2√X − 1 + o(1) ~ 2√X. With X=λe^{−|w|}: **N_λ(w) = Σ_{n≤λe^{−|w|}} Λ(n)/√n ~ 2√(λe^{−|w|}) = 2λ^{1/2−|x|}, x=w/L ∈[−½,½].** VERIFIED numerically: ratio N_λ/(2λ^{1/2−|x|}) → 1 as λ→∞ (λ=50,200,1000 gives 0.82,0.93,
0.96 at x=0; converges for each x, more slowly at large x due to subdominant terms). DERIVED from PNT. Refines the conjecture F(x)·λ: it is **λ^{1/2−|x|}** (variable exponent). Explains:
- center x=0: N~2√λ maximum ⟹ barrier ⟹ central singularity.
- edge x=±½: N~O(1) minimum ⟹ edge localization. **Nature:** N_λ(w) is the HOPPING strength (total weight of translations) from w — a
position-dependent kinetic term, NOT a direct potential. ⟹ 𝓛 is Sturm–Liouville with variable
coefficient −(p(w)u')'+… with p(w) tied to N_λ(w), not −∂²+V with V=N_λ. (Consistent with:
"many −(pu')'+q give a quadratic spectrum".) ## Step 3b [DERIVED + frank correction]: moments M_0,M_2 and NON-LOCALITY (: compute moments 0 and 2 of the allowed translations before identifying 𝓛.) M_0(w)=Σ_{n≤X}Λ(n)/√n ~ 2√X = 2λ^{1/2−|x|} (verified, ratio→1).
M_2(w)=Σ_{n≤X}Λ(n)/√n(log n)² ~ 2√X(log X)² = 2λ^{1/2−|x|}(logλ)²(1−2|x|)² (verified).
⟹ M_2/M_0 ~ (log X)² = (logλ)²(1−2|x|)². **Both with the λ^{1/2−|x|} geometry** (hope confirmed ✓). **BUT the local expansion FAILS [correction]:** 85% of V's weight is at LARGE hops
(log n > ½ log X), not small steps. ⟹ Taylor f(w±log n)≈f+½h²f'' INVALID ⟹ **V is NON-LOCAL**,
not the differential operator M_0+M_2∂². Third conceptual correction (after fixed-layer and tunneling). **Firm distinction:**
- M_θ IS localizable: Lévy measure with finite 2nd moment C_2 (dominated by ξ→0) ⟹ c(−∂²) rigorous.
- V (primes) is NOT localizable: dominated by large hops ⟹ NON-LOCAL operator. ⟹ **𝓛 = c(−∂²) − V_nonlocal** (local kinetic vs non-local prime term). The spectrum
(k+1)² emerges from that competition, NOT from a local ODE. Correct framework: **non-local
(sampling / de Branges, P7/P8)**, not a differential equation. The moments M_0,M_2 (geometry
λ^{1/2−|x|}) are the data, but the identification of 𝓛 is as a non-local operator. ## Step 3c [MECHANISM + open core] — non-local confinement ⟹ Dirichlet (k+1)² Unifying mechanism: 𝓛 = c(−∂²) − V_nonlocal, with V_nonlocal ~ M_0(w)~2λ^{1/2−|x|} ENORMOUS in
the bulk/center, O(1) at the edge. V_nonlocal **confines** (kills modes where M_0 is large) ⟹ imposes
an **effective Dirichlet** condition at the boundary of the support region. ⟹:
- (k+1)² RELATIVE = spectrum of the LOCAL kinetic c(−∂²) with those Dirichlet BCs (2nd order from M_θ, V only confines). Alternating parity = Dirichlet eigenfunctions. Central singularity = M_0 max at x=0 ⟹ node. Edge localization = modes where M_0~O(1). ALL reconciled. **Open core (= missing step of), 2 asymptotics:**
- (3c-a) prove that non-local confinement gives EXACTLY the Dirichlet spectrum (k+1)².
- (3c-b) prove that the sampling residual (Lemma 2) gives ε_0 ~ e^{−L} with S=1. (The scale e^{−L} does NOT come from simple confinement —width W~1/logλ would give eigenvalues growing in L— but from the sampling residual beyond the horizon; a different mechanism.)
Both = de Branges asymptotics/concentration, research level. NOT fabricated. ## FRANK SYNTHESIS (after all rounds)
Reduction achieved: RH ⟸ Link 2 ⟸ (i) exact + (ii) (1/ε_0)A_λ→𝓛, 𝓛 characterized with
DERIVED coefficients: kinetic c=−ψ''(1/4)/8, non-local arithmetic potential M_0~2λ^{1/2−|x|}
(PNT), horizon T*~2πλ². The open core: 2 asymptotics (3c-a),(3c-b) of an explicit non-local
operator. We converted "missing convergence" (vague) into "2 concrete asymptotics missing, with all
the ingredients derived". Real/publishable reduction; the closure is genuine research. ## Step 4 [DERIVED] — Beurling–Deny decomposition (framework of Goal A,) Reorganization (): attack the FORM EQUIVALENCE c₁𝓔_D≤A_λ≤c₂𝓔_D, not the spectrum directly;
the spectrum (k+1)² comes afterward via Mosco/Γ-convergence. Using the Lévy rep. of M_θ (H1) and 2∫f(w)f(w+h)dw=2‖f‖²−∫|f(w)−f(w+h)|²: A_λ(f,f) = ∫(Ω(0)−2M_0(w))|f|²dw + 𝓔_θ(f) + 𝓔_prime(f), [RIGOROUS] - q(w)=Ω(0)−2M_0(w): potential, M_0~2λ^{1/2−|x|} (PNT), deep well, maximum at center.
- 𝓔_θ(f)=½∫∫|f(w+ξ)−f(w)|²dν(ξ)dw ≥0 (archimedean jump, ν from H1).
- 𝓔_prime(f)=Σ_n Λ(n)/√n ∫|f(w)−f(w+log n)|²dw ≥0 (prime jump).
Two positive non-local Dirichlet forms + an arithmetic well. A_λ≥0 ⟺ jumps compensate the well. **Upper bound [PROVED]:** 𝓔_θ(f) ≤ C_2 ∫|f'|² (from ∫ξ²dν=C_2<∞ + Cauchy–Schwarz). ⟹ the
archimedean part ≤ C_2·𝓔_Dirichlet. **Goal A [OPEN, well framed]:** form lower bound + control of 𝓔_prime (non-local)
against the effective 𝓔_D in the edge region ⟹ form equivalence ⟹ (via Mosco) spectrum
(k+1)². = Dirichlet-form / de Branges theory. Localized, rigorous, not closed. **Goal B [OPEN]:** ε_0~e^{−L} = minimum residual of f∈PW_{L/2} forced to vanish at the
zeros up to T*~2πλ² = Beurling–Selberg/de Branges extremal problem. Localized. ## (remainder: detailed identification of the non-local operator) Derive the explicit W(w) = the sum over primes resolved by the boundary (which primes "fit" at
each w), and show that the bottom of the resulting operator gives ε_0 ~ e^{−L} with relative
spectrum (k+1)². This is the boundary-layer computation / the asymptotics of the archimedean−prime
balance. It is the remaining analytic heart of O-4b. NOT closed. ## Frank status
- [DERIVED] 2nd order from M_θ, c=−ψ''(¼)/8 exact.
- [STRUCTURAL] boundary essential ⟹ w-dependent potential ⟹ central singularity (consistent with the data). Explains why it is NOT flat Dirichlet (caution confirmed).
- [OPEN] the explicit boundary balance (W(w) + scale e^{−L} + spectrum (k+1)²) = Step 3.
- 𝓛 = 2nd-order operator with singular central potential; 2nd-order coefficient derived; potential characterized but not derived in closed form.
