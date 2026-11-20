# Reverse-engineering dossier of the window-positivity sign (Papers 43–48)

Source files (read-only): `04-papers/47-row-d-dual-certificates/main.tex` (cited as P47:line),
`04-papers/48-row-d-route-map/main.tex` (P48:line), READMEs/section lists of Papers 43–46.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. Every new idea in this file is OPEN.
Convention: window positivity is treated as a standalone statement about an explicit quadratic form. Zeros of
zeta appear only where a paper's *tool* is an explicit-formula identity; no equivalence with any other statement is used.

---------------------------------------------------------------------------------------------------------------------
## 1. The exact open statement (self-contained definitions)

### 1.1 Basic objects (P47:105–150, 393–470, 370–392)
- T>0, I_T=(-T,T). For F in L^2(I_T) (extended by 0): \hat F(τ)=∫F(t)e^{iτt}dt; autocorrelation
  c_F(u)=∫F(t)\overline{F(t-u)}dt (supported in [-2T,2T], \hat c_F=|\hat F|^2).
- Archimedean symbol m(τ)=Re ψ(1/4+iτ/2) − log π. Lévy form (Lemma lem:K, P47:395):
  m(τ)=C_0+∫_0^∞(1−cos τu)K(u)du, C_0=ψ(1/4)−log π=−5.3721834…,
  K(u)=1/(2 sinh(u/2))+1/(2 cosh(u/2))=2Σ_{k≥0}e^{−(2k+1/2)u} (positive, completely monotone, K=u^{-1}+O(1) at 0).
  m−C_0=φ(τ^2), φ(x)=Σ_{k≥0} x/(a_k(x+4a_k^2)), a_k=k+1/4, complete Bernstein (thm:S, P47:421). m increasing in |τ|,
  unique positive zero t_0=6.2898… (numerical), m(τ)=log(|τ|/2π)+O(1/|τ|).
- Contacts N_T={n≥2: log n<2T}; weights v_n=2Λ(n)/√n; A_T:=Σ_{n∈N_T}v_n.
- Window symbol σ_T(τ)=m(τ)−Σ_{n∈N_T}v_n cos(τ log n).
- Form a_T(F)=(1/2π)∫σ_T|\hat F|^2dτ = C_0‖F‖^2+Lev(c_F)−Σ_{n∈N_T}v_n Re c_F(log n),
  Lev(Φ)=∫_0^∞(Φ(0)−ReΦ(u))K(u)du (thm:A, P47:444, eq:Aform). Domain D_T={∫log(2+|τ|)|\hat F|^2<∞}.
- Tate moments A(F)=∫F e^{t/2}, B(F)=∫F e^{−t/2}; primitive subspace P_T={A=B=0}.
- Complete form W_T(F)=a_T(F)+2Re(A(F)\overline{B(F)}).
- λ_A(T)=inf{a_T(F): F∈P_T∩D_T, ‖F‖=1};  λ^W_T=inf{W_T(F): F∈D_T, ‖F‖=1}; λ^W_T ≤ λ_P(T) ≤ λ_A(T).
- **Target (eq:target, P47:136):** λ_A(T) ≥ 0 for every T>0 (and the complete version λ^W_T ≥ 0).
- Status: PROVED λ_A ≥ 2.5·10^{-12}, λ^W ≥ 10^{-18} on (0,½log5] (thm:log5A/log5W, P47:4680–4710, ball arithmetic);
  CITED: Zhu T≤0.8, Liu T≤17/16 (unrefereed), Mori T≤½log15=1.35402 (unrefereed, computational part reproduced).
  OPEN beyond ½log15.
- Structural facts (PROVED): T↦λ_A nonincreasing (lem:monoT, P47:534) and continuous (lem:contA, P47:621); target ⇔
  lim_{T→∞}λ_A ≥ 0 ⇔ λ_A ≥ −ε(T) with ε→0 ⇔ λ_A(½log n_k)≥0 along one sequence (thm:wit-Tc(iv), P47:995).
  Dichotomy (thm:wit-Tc(v)): either 0 ≤ λ_A ≤ 4·10^9 T e^{−15.449T} for all T≥1, or λ_A ≤ −c<0 eventually.
  At each T the problem depends only on (Λ(n))_{n<e^{2T}} (prop:finite, P47:3156); the feasible set of weight vectors is
  closed convex (ibid. (ii)).

### 1.2 Reduced form (L2): the finite Schur matrix (P47 §coer, 4876–5339)
- Blocks: k≥1, r=T/k, B_j=(−T+2(j−1)r, −T+2jr). e_j^±=e^{±t/2}1_{B_j}.
  V_k={F∈L^2(I_T): ∫_{B_j}F e^{t/2}=∫_{B_j}F e^{−t/2}=0 ∀j}; E_k=P_T⊖V_k = span{e_j^±}∩P_T, dim E_k=2k−2 (lem:coer-decomp).
- Coercivity (thm:coer-B, P47:5104; PROVED): for r≤1, m_T(F) ≥ (log(1/r) − C_B(r))‖F‖^2 on V_k, C_B(r)→1.6399 as r→0.
  c(T,k):=inf{a_T(F): F∈V_k∩D_T, ‖F‖=1} ≥ log(k/T) − C_B(T/k) − ‖Π_T‖ (cor:coer-L1, P47:5197), ‖Π_T‖ ≤ A_T
  (prop:coer-prime); hence c(T,k)>0 for k ≥ k_0(T) (admissible k > T e^{A_T+C_B}, doubly exponential in T; k=25 at ½log5).
- Schur complement (thm:coer-schur, P47:5239): for c(T,k)>0, K:E_k→V_k defined by a_T(Ke,v)=a_T(e,v) ∀v∈V;
  s_{T,k}(e)=a_T(e)−a_T(Ke)=a_T(e)−sup_{u∈V}[2Re a_T(e,u)−a_T(u)]; S_{T,k}= matrix of s_{T,k} in an orthonormal basis of E_k
  ((2k−2)×(2k−2) real symmetric).
- **(L2) [OPEN]: for every T>½log5 (now: >½log15 granting Mori), S_{T,k(T)} ⪰ 0.** ⇔ λ_A(T)≥0 (PROVED, thm:coer-schur(iii)).
  Note: entries are not closed form (a sup over V); Galerkin gives upper bounds only (rem:coer-honest, P47:5298).

### 1.3 Reduced form (N): signed twisted Chebyshev bound at Nyquist points (P47 §nyq 6049–6439, §wit 7164–7308)
- ω_k=πk/(2T). Truncated symbol s_T(τ)=C_0+∫_{2T}^∞K+∫_0^{2T}(1−cos τu)K(u)du−Σ_{N_T}v_n cos(τ log n) (eq:nyq-sT, P47:6060).
- Nyquist identity (thm:nyq, PROVED): a_T(F)=(1/4T)Σ_k|\hat F(ω_k)|^2 s_T(ω_k), exact (with σ_T there is an aliasing term,
  prop:nyq-alias).
- Coherence: ϱ_T=Σ_{N_T}v_nδ_{log n}−2e^{u/2}1_{(0,2T)}du; C_T(ω)=−(1/4T)∫cos(ωu)dϱ_T(u)
  =(1/4T)[Re(2(e^{(1/2+iω)2T}−1)/(1/2+iω)) − Σ_{N_T}v_n cos(ω log n)].
  b_T(F)=C_0‖F‖^2+Lev(c_F)−2∫_0^{2T}Re c_F(u)e^{u/2}du, so a_T=b_T−∫Re c_F dϱ_T.
- prop:wit-coh (P47:7224, PROVED): ∫Re c_F dϱ_T = −Σ_k|\hat F(ω_k)|^2 C_T(ω_k); F∈P_T is a witness (a_T(F)<0) iff
  Σ_k|\hat F(ω_k)|^2 C_T(ω_k) < −b_T(F).
- Equivalent polar-free form (prop:sharp, P47:7361, PROVED): m^♯(τ)=m(τ)+1/(1/4+τ^2)=Re ψ(5/4+iτ/2)−log π
  (=C_0+4+Σ_{k≥1}τ^2/(a_k(τ^2+4a_k^2)); m^♯(0)=C_0+4=−1.3721834…), a^♯(F)=(1/2π)∫m^♯|\hat F|^2,
  F_T(F)=Σ_{N_T}v_n Re c_F(log n) − 2∫_0^{2T}Re c_F(u)e^{u/2}du = 2∫_{[1,e^{2T})}y^{−1/2}c_F(log y)d(ψ(y)−y) (prop:wit-cheb).
  On P_T: a_T = a^♯ − F_T. **(N) [OPEN]: F_T(F) ≤ a^♯(F) for all F∈P_T∩D_T, all T.** λ^♯(T)=bottom of a^♯ on P_T ↓ C_0+4<0.
- Primal cone (thm:nyq-cone, PROVED): P_T=(1/4−∂^2)H^2_0(I_T), \hat F=(τ^2+1/4)\hat G; the sample cone
  K_T={(|\hat F(ω_k)|^2)_k} = samples of entire f≥0 of type ≤2T, integrable, vanishing to order ≥2 at ±i/2; Σ(−1)^k a_k=0.

### 1.4 Reduced form (S): near-coincidence matrices / one profile (P47 §combs 7759–7847)
- Profile (P47:7760–7770): a>0, |b|>1/2, g(t)=e^{bt}1_{[0,a]}, c_g=g*\tilde g, G_0=c_g*c_g, T_0=2a, F_0=(1/4−∂^2)G_0 ∈ P_{T_0};
  \hat F_0(τ)=(τ^2+1/4)|\hat g(τ)|^4>0 on R, \hat g(z)=(e^{(b+iz)a}−1)/(b+iz). c_0:=c_{F_0}, \hat c_0=\hat F_0^2.
  (Normalise ‖F_0‖=1; see §6(b).)
- **One explicit function of one real variable (thm:oneprofile, P47:7773, PROVED):**
  B(d)=a(F_0,V_dF_0)=(1/2π)∫m(τ)\hat F_0(τ)^2 cos(τd)dτ − ½Σ_{n≥2}v_n[c_0(log n−d)+c_0(log n+d)]
  (finite sum for each d). **Target ⇔ B is a positive definite function on R.**
- Integer-lattice matrices (prop:AM, P47:7811, PROVED; needs 2T_0<log2): A_M=[B(log m−log k)]_{m,k≤M};
  target ⇔ A_M ⪰ 0 ∀M; s^T A_M s=(1/2π)∫\hat F_0^2|Σ_{m≤M}s_m m^{iτ}|^2[m(τ)−Σ_{2≤n<Me^{2T_0}}v_n cos(τ log n)]dτ;
  A_M=Arch_M−Div_M−Near_M, Arch_M(m,k)=(1/2π)∫m\hat F_0^2 cos(τ log(m/k)); Div_M=½(V_M+V_M^T), (V_M)_{mk}=v_{m/k} if k|m,k<m;
  Near_M(m,k)=½Σ_{n≥2, kn≠m}v_n c_0(log(kn/m)) (m>k): integers n≠m/k in (m/k·e^{−2T_0}, m/k·e^{2T_0});
  (Div+Near)_{mk}=½Ξ_{F_0}(log(m/k)), Ξ_{F_0}(D)=Σ_{n≥2}v_n c_0(log n−D)=2∫_{[1,∞)}y^{−1/2}c_0(log y−D)d(ψ(y)−y).
- **(S) [OPEN]: Arch_M − Div_M − Near_M ⪰ 0 for every M.**

### 1.5 Further exact restatements (all OPEN, all ⇔ target or its complete version)
- (L) leakage coercivity (prob:ext-L, P47:9972): find κ>0, A_0≥0 with W_T(g) ≥ κ N^{−A_0} ℓ(g), N=e^{2T}≥5, g in the core
  (definitions §5.3 below). Implies λ^W_T ≥ (κ/4)N^{−A_0−1}(1−χ_0(2πN))>0 ∀T (thm:ext-margin, PROVED conditional).
- Node (P48 prob:node, P48:361): for T>½log15 and every real even F with ℓ_T(F)=∫F cosh(x/2)=0:
  Q_T(F)=(m_T+e_T)(F)+Φ_T(F) ≥ 0, e_T(F)=(1/2π)∫|\hat F|^2/(1/4+τ^2), Φ_T(F)=−∫_{[1^-,e^{2T}]}2t^{−1/2}c_F(log t)d(ψ(t)−t)
  (even-sector statement only; LMI/spectrahedron in (v_n)).
- Even inertia (prop:H, P47:6561): W^{ev}_T ⪰ 0 ∀T ⇔ n_−(A_ev(T)) ≤ 1 ∀T, A_ev = a_T on even D_T without Tate constraint.
- Gamma-moment annihilation (prob:annihilate, P47:6887) ⇔ target (prop:annihilate-equiv).
- Kreĭn indeterminacy at every window; flat-top certificate at every window (thm:KEPdich, thm:Zexh; lem:shape-restate P47:8910).
- Two-sector exact Schur form S_η (thm:nyq-schur(ii), P47:6367) — see §6(h): it is an exact finite reduction not listed in §open.

---------------------------------------------------------------------------------------------------------------------
## 2. PROVED tools (name — statement — label — lines)

Duality / certificates
- thm:D1 (P47:716) strong duality, finitely atomic dual sequences: λ_P = sup over (ν even finite measure on |u|≥2T, β∈R^2)
  of inf_τ[σ_T+\hat ν+β_0\hat g_0+β_1\hat g_1], g_0=cosh(u/2)1_{|u|<2T}, g_1=u sinh(u/2)1_{|u|<2T}. PROVED.
- thm:O (P47:775) dual never attained; thm:E (1088) exponential columns exhaust; prop:P (869) β=(2,0) unique for complete form.
- thm:C (P47:1146) explicit 437-atom certificate: λ_A(½log3) ≥ 8.8577·10^{-5}. PROVED (computer-assisted).
- thm:Z/thm:Zexh (1240,1302): certificate for flat-top weight w (w≡1 on [−2T,2T]) is the explicit formula on tests
  w(u)cos(τu); sup_w inf f_w = λ^W_T. PROVED (uses explicit formula as a tool).
- lem:Rrig, cor:nontermwise (1335,1358): no flat-top kernel is positive. thm:finZ (1488): no finite symmetric set of
  frequencies carries a flat-top certificate. thm:KEP1/2, KEPdich (1790–1840): certificates = a.c. solutions of a Kreĭn
  extension problem.
- prop:TK, thm:R, cor:Rrate, thm:latedge (1879–2281): lattice ceilings, convergence O(1/log M), edge cost Θ(1/M).

Archimedean structure
- thm:S, thm:A, lem:K, lem:mbounds (395–534) Lévy/complete Bernstein structure; explicit bounds
  log(τ/2π)−1/τ−1/(2τ^2) ≤ m(τ) ≤ log(τ/2π)+1/τ+½log(1+1/(4τ^2)).
- prop:arch, thm:index, cor:Tarch (2323–2587): archimedean form positive on P_T iff T < T*_{∞,P} ∈ [0.58,0.60]; negative index
  exactly computed for T≤0.90; prop:archneg: archimedean complete form negative from T=0.4608.
- thm:J, cor:nasym (2694–2735): negative index grows; lem:archcount (6454): n_−(m_T) ≥ ⌈2Tt_0/π⌉−1 ≈ 4T on Dirichlet sines.
- prop:band (2869): negative set of σ_T is a finite band ⊂ [0, τ^lo], τ^lo>2πe^{A_T}.

Finite reductions / operator structure
- lem:coer-lowpass, thm:coer-B, cor:coer-L1, thm:coer-schur (5081–5339): §1.2. (Caveat §6(a).)
- lem:wh-schurabs, thm:wh-LW, thm:wh-schur (5674–5746): prolate-block Schur reduction, λ_A>0 ⇔ ρ_T<1; coupling carries
  exactly the margin (iii).
- thm:wh-pencil, thm:wh-det, thm:wh-detinherit (5399–5900): Birman–Schwinger pencil; λ_A>0 ⇔ β_1<1; determinants inherit margin.
- thm:nyq, prop:nyq-alias, prop:nyq-LK, thm:nyq-sectors, thm:nyq-cone, thm:nyq-schur (6101–6439).
  Two sectors: a_T=½(s^per+s^anti), s^per=Σ_j s_T(ω_{2j})|⟨F,e_j⟩|^2, s^anti with odd ω; bases related by real unitary
  Laurent matrix H, h_m=2(−1)^m/(π(2m+1)) (symbol e^{iθ/2}); a_T=½⟨c,(D_e+H^T D_o H)c⟩.
- thm:parityschur, prop:polarcap, prop:onewindow, cor:beyond5 (4205–4799): complete vs primitive via 2×2 polar capacity G_T:
  λ^W>0 ⇔ λ_A>0 and G_T≻0; one window controls all smaller ones.
- prop:WT, cor:H1minus, prop:H (6497–6561): inertia by sectors via q_par=⟨A^{-1}χ_par,χ_par⟩; even sector: n_−(A_ev)≥1 for
  T≥0.12 (χ_ev=cosh(t/2)1_{I_T} is a negative vector; interval arithmetic at T=0.12); W^{ev}_T has positive bottom iff
  (n_−(A_ev)=0 & q>−½) or (n_−(A_ev)=1 & q<−½).
- lem:combsine (6468): comb on Dirichlet sines e_k=T^{−1/2}sin(ω_k(t+T)) is Toeplitz(divided differences of
  D_T(ω)=Σv_n sin(ω log n)) + Hankel, diagonal C_T(ω_k)+D_T(ω_k)/(2Tω_k), C_T(ω)=Σv_n(1−log n/2T)cos(ω log n). Exact.
- thm:geo-index (9381): n_−(T), n_−+z nondecreasing; crossings only downward; (W2) concavity along weight segments.
- lem:degen (3294): bottom μ_T(v) concave in weights; supergradient −(c_{F*}(log n))_n.

Reformulation tools
- lem:firstcontact (6591): a first failure window T_* carries a primitive null vector of definite parity.
- thm:PCfinite (6667): finite Poisson–Chebyshev operator identity (uses Λ*1=log); prop:GEgap (6829): strict Gamma–Euler
  contraction q_0<0.236.
- thm:wit-Tc, thm:wit-asym (6995–7037): witness windows form (T_c,∞); asymptotic conditions are fixed-window conditions.
- prop:wit-Egamma, prop:Egamma-exact, prop:boundary (7194, 7389, 7405): necessary (E_γ): limsup F_T(F_T)/‖F_T‖^2 ≤ m^♯(γ),
  exactly critical (rem:critical).
- lem:polarelim (7330): on P_T, 2∫_0^{2T}Re c_F e^{u/2} = −e(F); e(F)=‖G'‖^2+¼‖G‖^2 if F=(¼−∂^2)G.
- prop:Cplus, thm:kappa, thm:atomic (7449–7564): ρ_κ=2κe^{u/2}du is positive at every window iff κ≥κ_*, κ_*≥|C_0|/4>1;
  purely atomic combs positive at every window exist.
- lem:reson, thm:ceiling (7575–7640): nonnegative comb on log N positive at every window has density ≤ 1 (Λ is at the ceiling).
- prop:nearfree (7642): on resonators F_b=Σ_{m≤M}b_m V_{log m−½log M}ψ_ε, ε=1/(8KM(2+log M)), a_T(F_b)≥c_0‖F_b‖^2 uniformly
  (positivity where near-coincidences are invisible; uses Λ*1=log and Mertens).
- lem:transl, thm:band, thm:poisson, thm:oneprofile, prop:AM (7682–7847).
- thm:spec-gauge, thm:spec-carrier (9538–9567): divisor gauge s_φ(τ)=m(τ)−2Re[ζ(½+iτ)Q_φ(½+iτ)], Q_φ=−Σφ(d)μ(d)(log d)d^{−s},
  φ≡1 on d<N; every window comb has a symbol with the same factor ζ(½+iτ).
- lem:strip-L1, thm:strip-L3, thm:strip-R1, thm:strip-T1, cor:strip-T1p (9618–9697): holomorphic/Green identities on the
  strip; thm:strip-T3 contractive gauges impossible; thm:strip-T4 gauge methods = dual certificates; prop:strip-R4 no
  Hermite–Biehler; prop:strip-Q2 exact band formula.
- §ext tools (9899–10646): lem:ext-mob (Möbius bijection), thm:ext-half (half-line identity, given Guo2026), prop:ext-gauge,
  lem:ext-ellbound, prop:ext-consol, prop:ext-univ, thm:ext-margin (cond.), prop:ext-base (given Mori), lem:ext-hf,
  thm:ext-line, thm:ext-EM, prop:ext-residue, prop:ext-pointwise, prop:ext-dual, thm:ext-mirror (proved for C_c^∞ data),
  prop:ext-contour, prop:ext-pairs, prop:ext-deep, prop:ext-K1b, prop:ext-flow, lem:ext-weight, lem:ext-cell, lem:ext-osc,
  thm:ext-cell, cor:ext-cellpos, cor:ext-cfals, lem:ext-phase, thm:ext-multi, lem:ext-envelope, thm:ext-layer(i–iii),
  thm:ext-lattice, prop:ext-grouped, prop:ext-latred.

Upper bounds on the margin
- thm:margin, cor:margin1 (3530–3561): λ^W ≤ λ_P ≤ λ_A ≤ 4·10^9 T e^{−15.449T} for T≥1 (zero-side test family; PROVED).

Rows A–C and Paper 46 (READMEs; no sign claimed anywhere)
- P43 (row A): semilocal idele carrier, canonical trace Σ_v W_v, symbol bounded above with Tate poles ±½, Tate boundary
  sequence (B_T,β_T), Riemann–Roch biextension, signature infinite of both signs. Tool value for the sign: none direct
  (the trace form restricted to a window *is* a_T; the signature result says the global form has no finite-index
  positivity to transfer).
- P44 (row B): Frobenius family with diagonal contact Λ(n)n^{−1/2}; Möbius cofiber; Gram forms; thm:qfinpositive (44:3132ff):
  finite-place form positive at τ=0 with ω_fin(0)=Σ_{p∈S}2log p·p^{−1/2}/(1−p^{−1/2}) — the same local Euler-factor bound
  used in P47 rem:boxes for Div_M on multiplicative boxes. Tool value: local (one-prime Toeplitz) bounds only.
- P45 (row C): explicit formula in the trace normalisation without crossing zeros (Thm B); comparison
  I_∞(Γ_F,Γ_F)=β_T(M,M)−Σ_ρΦ_F(ρ)Φ_F(1−ρ) (Thm C); polar term from residues of the Euler-product symbol (Thm E);
  a zero-side detection lemma (Thm F). These are the identities P47 uses in thm:Z, lem:roughEF, prop:H.
- P46: Pólya class K, affine duality, Hodge-index transfer CONDITIONAL on an h^0 with three clauses; frame defect theorem:
  no such h^0 (cosh inequality constant 0.99846…<1); defect also on an elliptic curve over F_2. Barrier, not a tool.
  The six-clause adelic object (§28.4 of the research notes) remains unbuilt (P48:407).

---------------------------------------------------------------------------------------------------------------------
## 3. Barrier / NO-GO theorems: exact class excluded and what is NOT excluded

Mechanism of all of them: lem:transfer (P47:7856): if ζ's form and a form with negative bottom share property P, no deduction
"P ⇒ bottom ≥ 0" is valid. A conjunction P_1∧…∧P_k is excluded only by one falsifier having all P_i (rem:conjunctions, P47:~9475).

| barrier (label, lines) | class excluded | falsifier | NOT excluded (paper's own words where available) |
|---|---|---|---|
| thm:finmod, cor:void (3228, 3336) PROVED | any property preserved by finite deletion Λ1_{n≥N} or one-term amplification: PNT with error terms, zero-free regions, zero densities, sieve upper bounds; T>0.75 | deletion; Λ+c1_{n=2} | arguments using exact values at every window |
| lem:shape-scale O_4 (8640) PROVED (c large/small); CONDITIONAL on κ_T≠0 for c→1 | properties of ζ^c, cone conditions on log ζ or −ζ'/ζ, support, relative sizes | cΛ | non-homogeneous use (first non-homogeneous exact relation: Selberg ΛL+Λ*Λ=μ*L^2, rem:spec-scope P47:9853) |
| prop:shape-eulerdel O_6 (8665) PROVED | Euler product + zeros + pole + integer coefficients without the functional equation; T∈[0.60,½log P] | a_P=Λ1{p≥P} (for P>e^{2T} its comb on the window is EMPTY) | use of (F) jointly with (E) |
| lem:shape-epstein O_10 (8736) CITED for complete form | (F)+(I)+nonnegative coefficients without Euler product | Epstein x^2+5y^2, T≥1.59 | (E) used at the sign step |
| rem:FDH (P47:~8540) PROVED (ball arithmetic) | (F)+Γ-factor+bounded real Dirichlet coefficients without multiplicativity, T≥9/5 | Davenport–Heilbronn mod 5 | multiplicativity used |
| O_7 quartets, O_8 self-dual f_t (8680–8692) PROVED | zero-set statements; finite windows of the prime side; f_t keeps Λ(n), n<λ_1, and (F) | ξ_{z,k}, f_t | property not shared by zero-side models; integrality (f_t breaks (I)) |
| O_11 Beurling (8769) ARGUED | (E) as comb identity Λ*1=log without integers | Beurling systems | integrality of Z |
| prop:summable, cor:wtail (8347–8380) PROVED | summable combs, exact small values + sieve upper bounds, Euler products over finite S | Λ1_{n<n0}, a_S | — |
| prop:prog (8380) PROVED | progression statistics (SW, BV, BDH, Brun–Titchmarsh) | via cor:void | joint Near/Arch control |
| prop:relative (8400) PROVED | KLMN relative form bounds on F_T | trivial | — |
| prop:opcalc + thm:sos (8419–8490) PROVED | operator identities + Cauchy–Schwarz; sums of squares of Dirichlet (any almost periodic) polynomials with a constant archimedean payment, T≥½log3 | pointwise bound v_2 | squares with a free positive-definite part (= certificates); (½log2,½log3) (see §6(e)) |
| prop:cone (8491) PROVED | monotone Möbius-resolvent iterations | atom at log2 vs density | — |
| prop:nearfree + rem:boxes (7642, ~7700) PROVED | tests that do not see near-coincidences m≈kn | positive anyway | vectors that see Near_M |
| thm:Vp, prop:env (2986, 3058) PROVED | pointwise envelopes; threshold 2πe^{A_T} | — | — |
| lem:half, cor:directbound, thm:posext, prop:primeblind (7875–7974) PROVED | norm bounds of the prime form in a fixed frame; complete certificates with positive exterior measure; termwise bounds | — | **signed exterior measures; primitive certificates with ν≥0 and free β** (rem:bar-lin P47:7988) |
| thm:famblind, thm:famFE (8023, 8113) PROVED | properties of T↦λ on a bounded range of windows | amplification, f_t | **two-sided laws λ_A=L(T)(1+o(1)) on unbounded ranges** (rem:bar-fam P47:8129) |
| cor:pattern (8215) PROVED | finite lists of window observables | quartet models | — |
| thm:nolocal (8255) PROVED | criteria depending on σ_T only near its negative set | σ^{(η)}=min(σ_T,η) | **criteria using the positive part on all of R jointly with the negative set; exact Schur reductions** (rem:bar-loc P47:8328) |
| thm:X (8281) PROVED | pointwise new-contact conditions | — | integrated conditions |
| thm:inertia-nogo (3439) PROVED | positive part + bounded-convolution remainder (Sonin/Connes–Consani) for T>½log2 | n_−=∞ | quantitative use of the compact term (P47:3745) |
| lem:wh-T, thm:wh-detinherit (5799, 5865) PROVED | determinant/moment/trace criteria of the pencil | margin inheritance | — |
| thm:geo-tv (9254) PROVED | premises robust in total variation radius r>λ_A | atom near 0 | classes with an exact support axiom (supp⊂log N) (P47:9266) |
| thm:geo-parity (9425) PROVED | distributional (Bohr-distribution) defects on σ_P-closed classes, at odd prime-power levels | σ_Q sign flips | non-distributional functionals; coupling R to ζ itself |
| thm:noimport (9460) (i)-(ii) PROVED, (iii) if κ_T≠0, (iv) ARGUED | positivity imported via a construction uniform in the degree-one weight data | DH, Epstein | constructions using exact multiplicativity at the sign step |
| thm:spec-noatom (9515) PROVED | exact identity a_T = pair count measure on log Q_{>0} | — | limit identities |
| thm:spec-K2 ARGUED (gap: joint Ω-result) | absolutely convergent divisor gauges as pointwise certificates | — | genuine mollifiers |
| prop:strip-R4, thm:strip-T3/T4 PROVED | Hermite–Biehler, contractive gauges; expansive gauges = dual certificates | — | F-dependent gauges, identities with sources (argued only) |
| thm:shape (9126), cor:shape (9167) | union of the above (A) PROVED, (A') labelled, (B') partly argued, (B'') PROVED | | Problem (R) |

---------------------------------------------------------------------------------------------------------------------
## 4. The shape of the solution (Problem (R) + prop:spec, read constructively)

### 4.1 The eleven clauses of Problem (R) (prob:region, P47:10720–10736), verbatim content
(1) exact Λ(n), n<e^{2T}, at every T, not class membership closed under any O_i; (2) Euler product over N and
functional equation with Γ(s/2) at conductor 1 jointly; (3) non-linear in Λ (not a certificate/lattice/flat-top/operator
identity+C–S), squares only with a free PD part; (4) not reducible to zero-free regions/densities/finitely many zeros,
and pointwise curvature statements on log|ξ| must use holomorphy+order one jointly or the Euler product on the line;
(5) not a bounded functional of weights/symbol, not local on the negative set, not a leading determinant term, not a
pattern, not a bounded-range law; (6) sensitive at scale λ_A/κ_T, precision ≤ 4·10^9Te^{−15.449T}; (7) exact at the
centre and integer resolution, wins from fluctuation not density; (8) uses the positive part of σ_T on all of R with the
negative set (correlation inside P_T at all frequencies up to e^{2T}); (9) not a symmetrization of D_σ; (10) beyond axioms
A1–A6 (A2^+), field-uniform only if it names the separator from ξ_K; (11) ζ-specific at the sign step: not an inequality on
prime sums with a remainder, not an identity valid for every weight vector.

### 4.2 The six clauses of prop:spec (P47:9794–9846)
(1) not linear, not comb-generic (PROVED; exclusion of PD/hyperbola/Dirichlet-algebra class CONDITIONAL on an itemised
Beurling check); (2) not a cone condition on log ζ (PROVED); (3) not coefficientwise integrality (PROVED); (4) not sparse-stable
(PROVED); **(5) couples (Λ(n))_{n<N} with the functional equation by a route other than the factor ζ(½+iτ) (OPEN)**;
(6) crosses the logarithmic derivative without losing positivity (ARGUED; only infinitely-divisible cones cross).

### 4.3 What clause (5) means, exactly
- The "factor ζ(½+iτ) route": thm:spec-gauge/spec-carrier (P47:9538–9567, PROVED) show that for every comb b (Λ, a_P, the
  zero comb on the window, …) the window form equals (1/2π)∫|\hat F|^2[m−2Re(ζ(½+iτ)Q(½+iτ))] with Q a Dirichlet polynomial
  fixed on d<N by μ*b. So writing the comb through ζ on the critical line (where the functional equation acts, |χ|=1)
  "uses" the functional equation, but identically for combs that fail positivity: for P>N, a_P is the empty comb on the
  window, whose form is the pure archimedean form, negative for T≥0.60. Hence the factor ζ(½+iτ) cannot be where the sign
  comes from; the only gauges that could make s_φ pointwise ≥0 are genuine mollifiers (thm:spec-K2, ARGUED; missing step:
  a joint Ω-result for (ζ(σ+it),(p^{−it})_{p≤X(t)})).
- "Route other than ζ(½+iτ)": an object in which the *specific values* Λ(n), n<N (not merely the identity Λ*1=log on N_T,
  which is comb-generic), are linked to the reflection s↦1−s/Poisson summation by a mechanism that (a) is not one of the
  comb-generic strip identities, (b) does not reduce to a dual certificate, (c) separates Λ from a_P on N_T (trivially:
  a_P vanishes there for P>N; nontrivially: must also separate from Λ1_{n≥N'}, cΛ, Λ+c1_{n=2}).
- Routes already ruled out for clause (5) (with labels):
  * divisor gauges / mollifier pointwise bounds — thm:spec-K2 ARGUED;
  * Green identity, sourceless energy identity, gauged identity, entire gauge q_T (thm:strip-L3/R1/T1, cor:strip-T1p) —
    meet the wording but are comb-generic (valid for Beurling systems and a_P) and their gauge freedom returns exactly the
    dual certificates (thm:strip-T4) — PROVED in declared class;
  * contractive gauges (thm:strip-T3), Hermite–Biehler (prop:strip-R4) — PROVED;
  * Hamburger rigidity — identification, not an inequality (prop:spec(5) text; P48 thm:Rid: every global separator identifies);
  * symmetrization of D_σ=2Re ξ'/ξ(σ+iτ) — antisymmetric, D_{1−σ}=−D_σ (rem:fe, P47:~8515) PROVED;
  * curvature/Poincaré ceilings, real stability (remarks after strip-S2) — NUMERICAL/PROVED respectively;
  * exterior "symbol calculus": on-line symbol of the full form vanishes off the zeros (thm:ext-line; §ext-constraints 3);
  * P48 Table compose (P48:~840): FE as symmetry of the polar vector (chains), Euler defect with a seminorm
    2δ_E(Λ;f)^2=ℓ(Ef) ((E) identity + (F) fixed seminorm), reciprocity objects (Hecke, theta, Rankin–Selberg, Voronoi with
    |g|^2 holds for Epstein, Kuznetsov, Estermann, Kronecker–Hurwitz), weight-½ forms with J=χ(½+it)·reflection
    (empty cell, P48:414–422): all NO-GO.

### 4.4 Concrete template of an admissible argument (assembled from cor:shape, rem:conjunctions, P48 req:spec)
- Inputs: the vector (Λ(n))_{n<e^{2T}} with its *Dirichlet-series* Euler product (not only Λ*1=log), the archimedean
  data (C_0,K) at conductor 1, the pole/Tate moments, integrality of frequencies.
- Sign step: a non-linear (at least quadratic in Λ, or an inequality whose hypothesis is non-homogeneous in the comb)
  inequality that holds for ζ and fails for each of: cΛ (both sides of c=1), a_P, Λ1_{n≥N}, Λ+c1_{n=2}, DH, Epstein,
  quartet models, f_t, Poisson combs, Beurling systems. Its slack must be ≤ the margin (≤4·10^9Te^{−15.449T}), so in
  practice the sign step must be an *exact* identity/inequality (no remainder) at the decisive line.
- Where in the reduced forms the sign is located (paper's own pointers): (S) the near-coincidence part Near_M on vectors
  seeing m≈kn (rem:bar-arith P47:8534); (L) the non-integer Möbius-lattice classes a≥2 and their coupling to φ_0
  (rem:ext-latno P47:10642); the node of P48 (even sector, c^⊥); the Schur coupling ρ_T<1 (thm:wh-schur).
- Output: a lower bound for a_T on P_T (or W_T) valid for every T, with no T-uniform slack.

---------------------------------------------------------------------------------------------------------------------
## 5. Where the authors themselves point to live, unexcluded directions (quotes)

1. P47:10690–10692 (L2): "they do not exclude an argument outside those classes. A first test case is the window
   T=½log5+ε at which the contact 5 enters."
2. P47:10699–10701 (N): "what is needed is cancellation of exponent ½ in the twisted sum, with sign, at about e^{2T}
   frequencies. A first case is the inequality (E_γ) … for one fixed γ, which is necessary".
3. P47:10715–10717 (S): "What remains is a statement about Near_M, … coming from integers that are close to m/k but not
   equal to it, tested jointly with Arch_M on vectors that see these near-coincidences."
4. P47:10738–10744: "Objects that this paper does not exclude and that lie in the region: two-sided laws λ_A=L(T)(1+o(1)) on
   unbounded ranges; signed exterior measures and primitive certificates with ν≥0 and free β; arithmetic squares on
   (½log2,½log3); the exact Schur reductions …, which carry the whole margin; the problems (L2), (N) and (S)".
5. P47:8534–8536 (rem:bar-arith): "They do not exclude an exact inequality F_T ≤ a^♯ on P_T proved from the vector
   (Λ(n))_{n<e^{2T}} jointly with the archimedean form, for instance the positive definiteness of B … on test vectors that see
   Near_M."
6. P47:9853 (rem:spec-scope): "The open clause (5) is the one not covered by any falsifier of this paper." Also: "The first
   exact relation in (1,Λ) that is not homogeneous is of degree two (Selberg's ΛL+Λ*Λ=μ*L^2)."
7. P47:10641–10643 (rem:ext-latno): "the sign has to come from the non-integer classes a≥2 and their coupling to φ_0, through
   the shape of σ_g. Whether v^TGv ≥ 2κN^{−A_0}dist^2 holds is open."
8. P47 rem:conjunctions (≈9472–9488): "The conjunction of (E) and (F) … has ζ as its only model up to a constant
   (Hamburger), so no falsifier exists for it … the sign-carrying inequality … uses at least two inputs with no certified
   falsifier in common … a genuine conjunction requires a non-linear sign step or an input entering as an inequality."
9. P47 thm:noimport (9460–9470): "the sign … must be derived from a construction that uses the exact multiplicativity of Λ
   itself"; P48:437–438: "it leaves constructions that use the exact multiplicativity of Λ at the sign step."
10. P47 rem:bar-lin (7988–7997): not excluded: "signed exterior measures, which is where the certificate of Theorem C lives,
    nor primitive certificates with ν≥0 and free β".
11. P47 rem:bar-fam (8129–8137): "two-sided asymptotic laws … are neither shared by f_t … nor by the falsifiers …
    This class is open."
12. P47 rem:bar-loc (8328–8339): not excluded: "criteria that use the positive part of σ_T on all of R together with the
    negative set, such as the exact reductions …; these carry the whole margin".
13. P47 §inertia-excl (3745–3747): the inertia exclusion "does not cover arguments that use quantitative properties of the
    compact term, such as a T-uniform bound on ‖C_ε‖ or a sign."
14. P47 §open secondary list (10746–10786): Gamma-moment annihilation; class-dependent value bounds (deficit D(T,d,U));
    certified G_T≻0 beyond ½log5; certified lower bound for S_{T,k}; asymptotic law with sign; multiplier convergence
    β→(2,0); atomic Beurling combs in C^+; arithmetic squares on (½log2,½log3).
15. P48:328–330: at the node the a_P falsifier makes every premise inherited by all Euler products with a pole fail for
    T>π/2. P48:424–429 (the live gate): "What neither excludes is a premise that is a theorem *only* for logarithmic
    derivatives of L-functions with an Euler product over all primes, not inherited by a_P, used with precision at most
    4·10^9Te^{−15.449T}, and leading to Problem node for every T. No candidate is known."
16. P48 scope remark (≈P48:560–568): "there are exact, elementary separators of Λ from deleted Euler products
    [Σ_{d|n}b^{(p)}(d)=log n−v_p(n)log p]; what is open is turning identification into the quadratic bound."
17. P48:397–412 "Statements weaker in appearance": (Ω_0), (E_γ), (Ω_{t0}) damped interpolation, lower half of a two-sided
    law, a non-linear multiscale inequality outside single tests and power families, the §28.4 adelic object, an inequality
    at σ=1 using multiplicativity on the line, arithmetic squares on (½log2,½log3).
18. ROUTES-TRIED-INDEX/README (phase 190): residue Q_M(w)=s_w^T A_M s_w, s_w=m^{−1/2}w(m/M): "decide whether the boundary is
    PNT-error size ([void] → REF-D) or margin size M^{−3} (a new inequality on Λ at scale M)". (NUMERICAL: λ_min(A_M) ≍ M^{−3}.)

---------------------------------------------------------------------------------------------------------------------
## 6. Internal inconsistencies, mislabelled steps, overlooked consequences

(a) **thm:coer-schur, eq:coer-sandwich (P47:5255–5278) and lem:wh-schurabs(ii) lower bound (P47:5684–5695) are wrong when
λ_S<0.** [PROVED here, elementary]
  Claim in paper: min{c,λ_S}/(1+‖K‖)^2 ≤ λ_A ≤ min{c,λ_S}. Proof text (5275–5278): "taking v=−Ke gives a_T(F)=s(e) with
  ‖F‖^2≥‖e‖^2, so λ_A≤λ_S" and "if λ_S≤0 the lower bound is implied by λ_A≤λ_S".
  Correct facts: (i) a_T(v+e)=a_T(v+Ke)+s(e) ≥ s(e) ≥ λ_S‖e‖^2, and if λ_S≤0 then λ_S‖e‖^2 ≥ λ_S‖F‖^2; so λ_A ≥ λ_S.
  (ii) with e a unit eigenvector, v=−Ke: a_T(F)/‖F‖^2=λ_S/(1+‖Ke‖^2) ≥ λ_S when λ_S<0.
  So for λ_S<0: λ_S ≤ λ_A ≤ λ_S/(1+‖Ke_S‖^2); both inequalities of eq:coer-sandwich are reversed (unless Ke_S=0).
  Same flaw in the lower bound of lem:wh-schurabs(ii) (multiplying a²+‖e‖² ≥ ‖F‖²/(1+k)² by a negative λ_S reverses it).
  Impact: none on the sign equivalences (iii) (λ_A>0⇔S≻0, λ_A≥0⇔S⪰0 remain true) nor on (L2), (B'), rem:coer-honest,
  which use only the λ_S≥0 regime; but the displayed inequality is stated as PROVED for all cases. Fix: state the sandwich
  for λ_S ≥ 0 and add λ_S ≤ λ_A ≤ λ_S/(1+‖Ke_S‖^2) for λ_S<0. (lem:wh-schurabs already states "λ_q≤λ_S if λ_S≥0" correctly.)

(b) **Normalisation gap in subsec:oneprofile / prop:AM.** F_0 is defined (P47:7760–7767) without ‖F_0‖=1, but
  prop:AM(iii) proof uses "the term n=m/k has c_0(0)=1" (P47:7835) and thm:band takes F_0 "as in lem:transl" (unit norm).
  As written, Div_M=½(V+V^T) is off by the factor ‖F_0‖^2. Trivial fix: normalise F_0. [PROVED observation]

(c) **"Exactly one negative eigenvalue for every window" is false for small T.** prop:H final sentence (P47:~6569) and
  P48 thm:eveninertia(ii),(iii) (P48:205–207) state n_−(A_ev(T))=1 for every T. For small T, A_ev>0 (|\hat F|^2 has mass ≲
  2TR/π below R, and m(R)>0 large), so n_−=0; the correct statements are "≤1 for all T" (P47 prop:H first sentence, correct)
  or "=1 for all T≥0.12" (with cor:H1minus). P48 (ii) also drops the alternative (n_−=0, q>−½) of prop:WT. Minor. [PROVED]

(d) **§ext-constraints item 2 (P47:10654–10657) over-claims comb-genericity.** It lists the half-line identity among
  identities that "hold for the comb cΛ, for prime deletions and for Beurling systems with their own summation map".
  But thm:ext-half rests on Guo's radical lemma (Poisson summation over Z with the exact comb), and P47:10146 itself says
  "The identity is exact only for the weight 1 on the comb: replacing Λ by cΛ adds 2(1−c)…"; rem:ext-killing(ii) says the
  comb enters only through Λ*1=log with coefficients a_n≡1 on N. For cΛ the matching summation map would need
  coefficients d_c(n) (series ζ^c), for which no radical/Poisson identity is available. So the exterior form is an object
  in which (E) [Λ*1=log on N], (F) [Poisson/radical] and (I) [integers] are *fused*, i.e. it is not comb-generic; only the
  algebraic pieces (Möbius bijection, Λ*1=log) are. [ARGUED] Consequence: the exterior form 𝔔 is a natural candidate for
  the "route other than ζ(½+iτ)" of clause (5) — though thm:ext-line and prop:ext-pointwise re-express its on-line symbol
  through ζ'/ζ and |ζ(½+iτ)|^2, so whether it really escapes clause (5) is OPEN.

(e) **Secondary problem "arithmetic squares on (½log2,½log3)" reduces to one number.** [PROVED here + NUMERICAL]
  On that range N_T={2}. thm:sos needs Σ_i|D_i|^2=μ_0−v_2cos(τlog2) and m_T ≥ μ_0 on P_T. Necessity gives μ_0 ≥ v_2;
  sufficiency: μ_0−v_2cos(τ log2)=|x_1+x_2 2^{iτ}|^2 with x_1^2+x_2^2=μ_0, 2x_1x_2=−v_2, solvable iff μ_0≥v_2 (Fejér–Riesz,
  degree one). Hence an arithmetic square decomposition exists at T∈(½log2,½log3) **iff λ^{∞,P}_min(T) ≥ v_2=√2 log2=0.98026**.
  λ^{∞,P}_min is strictly decreasing (lem:strict); rem:directbound (P47:~7911, NUMERICAL) gives λ^{∞,P}_min ≈ 0.49 at T≈0.367,
  so the threshold T_sos (if >½log2 at all) is a single certified eigenvalue computation at T just above ½log2=0.3466.
  Either way the question is far below the certified range and carries no new sign; it should be closed rather than
  listed as open.

(f) **Monotonicity of the even pole-free index.** [PROVED, same proof as thm:geo-index(W1)] Extension by zero preserves
  A_ev values (no Tate constraint is involved and c_F is unchanged), so T↦n_−(A_ev(T)) is nondecreasing. With cor:H1minus,
  prop:H becomes: the even complete form stays nonnegative at every window iff the pole-free even form never acquires a
  second negative direction; a failure has a first "birth window" T_2 with a nonzero kernel vector of A_ev orthogonal (in
  A_ev) to the χ_ev-direction. This is a first-contact statement for the even complete form parallel to lem:firstcontact;
  not stated in P47 (rem:completecontact only treats λ^W). Restatement, no sign.

(g) **Content of (L) at a fixed window; consequence for minimizers.** [PROVED here]
  At a fixed T with λ^W_T>0, lem:ext-ellbound (ℓ ≤ C_1N^2‖g‖^2) gives W_T ≥ (λ^W_T/(C_1N^2))ℓ, so (ext-L) holds at each fixed
  window; Problem ext-L is *only* the uniformity of (κ,A_0). Conversely, since λ_A ≤ 4·10^9 T N^{−7.72} (cor:margin1, N=e^{2T}),
  (ext-L) forces every unit near-minimizer g to have gauge-minimised leakage ℓ(g) ≤ (4·10^9T/κ)N^{A_0−7.72}: near-minimizers
  must be E-images of almost band-limited f modulo the gauge. This is a checkable structural prediction (NUMERICAL test
  possible with existing Galerkin minimizers); a failure of it at moderate N with small A_0 would rule out small exponents.
  Note also that the lower bound of thm:ext-margin, (κ/4)N^{−A_0−1}(1−χ_0(2πN)) ~ e^{−4πN}, is doubly exponentially
  small — consistent with, and far below, the upper bound.

(h) **A smaller exact finite reduction than (L2) is already proved but not listed in §open.** [PROVED in paper; reading new]
  thm:nyq-schur(ii) (P47:6367–6380) holds for *every* η>0: λ_A≥0 ⇔ S_η⪰0 on N'_η, dim ≤ d_η=#{k even: s_T(ω_k)<η}+#{k odd:
  s_T(ω_k)<η}. Letting η↓0 the dimension is the number of Nyquist samples (in the two sectors) at which the truncated symbol
  s_T is negative, which is ≤ (4T/π)·τ_last+1 with τ_last ≤ τ^lo (prop:band), versus 2k−2 with k > T e^{A_T+C_B} for (L2).
  The numerically large d_η of rem:nyq-schur-num (45–59 at ½log5) comes from the larger η needed by the *inversion-free*
  bound S^low, not by the exact S_η. The coercive complement constant c_η=½(s^e_++s^o_+) is explicit from samples; the
  sign question becomes "S_η⪰0" on a space whose dimension is governed by the negative set of s_T on the mesh. Whether
  the Nyquist negative set grows like O(T) or like e^{A_T} is OPEN (NUMERICAL check cheap). Worth adding as (L2').

(i) Minor label/consistency notes. cor:shape(c) (P47:~9190) and P48:405 say "a relative change of 10^{-5} flips the sign at
  log2", rem:wit-sens (P47:~7300) says ~10^{-6} (λ_A/κ ≈ 9.8·10^{-8}/0.09 ≈ 1.1·10^{-6}); both are NUMERICAL and consistent
  (10^{-5} > threshold) but the statements differ. The (½log2,½log3) clause of Problem (R)'s "not excluded" list becomes
  vacuous after (e) if λ^{∞,P}_min(½log2^+) < v_2.

(j) No step labelled PROVED was found to rely on an unproved claim beyond (a); CONDITIONAL/ARGUED labels on spec-K2,
  ext-mirror (Paley–Wiener tails), ext-layer(iv), ext-flow, O_4^ε, O_5, O_10/O_11, thm:noimport(iv), prop:spec(1)
  (Beurling itemisation), (5), (6) are accurate as stated.

---------------------------------------------------------------------------------------------------------------------
## 7. Item-by-item examination (requested objects): unexploited angles (all OPEN)

### 7.1 Exterior form / leakage lemma (prob:ext-L, prop:ext-consol, prop:ext-latred)
Exact data: λ=e^T, N=e^{2T}; admissible f even, supp⊂[−λ,λ], C^2, f(0)=Ff(0)=f(λ)=0 (Ff(ξ)=∫f e^{−2πixξ});
Φ_f(x)=e^{x/2}Σ_{n≥1}f(ne^x), Ef=Φ_f|_{I_T}; tail Ψ_f=Φ_f|_{(−∞,−T)}; r_f=Ff|_{(λ,∞)}; gauge G_T={φ even C^2, supp⊂[−1/λ,1/λ],
φ(0)=Fφ(0)=0}; ℓ(g)=inf{leak(f): Ef=g}=2dist^2(r_f, \bar G_T). Half-line identity: W_T(Ef)=𝒲[\check Ψ_f] with 𝒲 the complete form
on the line with the full comb. Universal frame (prop:ext-univ): all T-dependence sits in the data class PW_N.
Status: base case N≤15 given Mori; high-frequency part comb-generic (lem:ext-hf); positive regions on chirps (thm:ext-cell,
thm:ext-multi) and caustic layer (thm:ext-layer) — none on PW_N mod gauge.
Angles:
- (A1) By §6(d), the exterior form fuses (E),(F),(I); the "key cancellation" H_J log t − 2H_1(J)=O(log J) (thm:ext-cell proof)
  is Λ*1=log over Z and detects c'>1 (cor:ext-cfals(ii)): the exterior form is one of the very few objects in the corpus
  where a positivity statement automatically fails for (1+δ)Λ. What is missing is a statement on PW_N modulo the gauge.
  ROUTES-TRIED-INDEX shows this was the subject of phase 199 (Lemma L′♯; MM_001 Barkhausen/passivity, K1 OS reflection
  NO-GO, K3 Γ-limit NO-GO, SQ tautological). Any new attempt must state a new reason vs those memos.
- (A2) Use §6(g) as a filter: (ext-L) predicts small gauge-minimised leakage of near-minimizers; testing it numerically on
  existing minimizers (N≤15) would tell whether A_0 can be small (OPEN, NUMERICAL).
- (A3) prop:ext-latred writes W_T(g)=v^TG(g)v with v=(μ(m))_{m<N squarefree}⊕1 — a *fixed arithmetic vector* tested against a
  g-dependent Gram matrix. rem:ext-latno excludes size/limit arguments on class coefficients; it leaves the coupling of
  non-integer classes a≥2 to φ_0. No further angle beyond the authors' pointer.

### 7.2 One-profile equivalence (thm:oneprofile) — "one explicit function of one real variable"
Exact statement: §1.4. Remarks:
- Because \hat F_0>0 on R, Bochner positivity of B is positivity of the distribution \hat F_0^2·(full symbol) — the
  profile is a device that turns the Weil-type distribution into a function of one variable; positive definiteness forces
  |B(d)| ≤ B(0) (bounded), i.e. the band |Ξ_{F_0}(D)| ≤ 2a(F_0)+O(e^{−5(D−2T_0)/2}) at every scale (thm:band) — a fixed
  square-root-size bound for a smoothed Chebyshev fluctuation, necessary for the target.
- Restriction to S-unit groups: since B(log(m/k)) depends only on m/k, positivity on N is positive definiteness on the
  discrete group Q_{>0}^× ≅ ⊕_p Z, i.e. (Bochner on the compact dual ∏_p S^1) for every finite set S of primes the multivariate
  Fourier series Σ_{q∈⟨S⟩}B(log q)χ(q) must be a positive measure on T^S; |S|=1 gives one-variable necessary conditions
  f_p(θ)=B(0)+2Σ_{j≥1}B(j log p)cos jθ ≥ 0. ROUTES-TRIED-INDEX: Bohr/Kronecker-torus constructions (prime-site LP on the
  torus CA_L_002 = REF-D; "one-prime Toeplitz test" P124 DEAD; rem:boxes covers Div on boxes). Likely REF-D; not a new route
  without a new reason.
- Not excluded (rem:bar-arith): an exact inequality proving positive definiteness of B on vectors that see Near_M.

### 7.3 Near-coincidence matrix (S)
- prop:nearfree: positivity with margin on resonator vectors (no near-coincidences). Phase 190 (NUMERICAL): A_M(Λ)⪰0 for
  M≤3000, λ_min ≍ M^{−3}, minimizer ≈ m^{−1/2}w(m/M); Near statistics not ζ-specific (identical under 10^{−5} perturbations).
- Identity C3 (phase 190, PROVED): s^T(Div+Near)s=2Σ_N N^{−1/2}log N·E_M(N) for s=m^{−1/2}; balance against Arch carried by
  defects at N=2,3,4.
- Live residue (authors): decide whether the boundary term of Q_M(w) is PNT-error size or M^{−3}. Angle (OPEN): the
  minimizer family s_w=m^{−1/2}w(m/M) is the Dirichlet polynomial Σ m^{−1/2+iτ}w(m/M) (a smoothed partial sum on the line);
  by prop:AM(ii) Q_M(w)=(1/2π)∫\hat F_0^2|P_{s_w}|^2[m−Σ_{n<Me^{2T_0}}v_n cos(τ log n)]dτ. The remaining question is a mean-value
  statement for |P_{s_w}(τ)|^2 against the truncated symbol, at resolution set by \hat F_0^2 (fixed) — a quantity where
  approximate functional equations (which carry (F) through χ(½+iτ)) could enter non-linearly (|P|^2), i.e. a candidate
  for clause (5). Check P48 "empty cell" (J-involution route NO-GO for w≥0 and argued for indefinite w) before proposing.

### 7.4 thm:band
2×2 case of (S); necessary only (L2_023). Unexploited: none beyond its use as a battery test (Poisson combs fail it with
probability 1−O(D^{−1/2}) per scale, thm:poisson).

### 7.5 prop:nearfree
Mechanism: near-free tests cost archimedean energy log(1/ε) ≈ log M + log K against comb ≤ log M + E (Schur test +
Λ*1=log + Mertens). It shows the comb is "harmless at exact coincidences"; sign must come from near-coincidences. No new angle.

### 7.6 thm:sos (arithmetic squares)
See §6(e): the open interval is a single eigenvalue comparison λ^{∞,P}_min(T) vs v_2. With a free PD part, squares = dual
certificates (thm:D1). Remark sosatoms: squares of the prime comb have atoms at log(p^j/q^i) off log N that must be paid by
other squares — excluded for constant archimedean payment. No angle.

### 7.7 Two-sector Schur reduction (thm:nyq-sectors, thm:nyq-schur)
See §6(h): exact S_η with η↓0 is the smallest proved exact reduction; dimension = negative Nyquist samples of s_T in the two
sectors. Structure a_T=½(D_e+H^TD_oH) with H the Laurent operator of e^{iθ/2} (H^2=shift) is a "two diagonal forms in two
bases" problem; prop:nyq-nopoint shows no common diagonalisation. Angle (OPEN): sign of a compression of
½(D_e+H^TD_oH) to P_T on the finite negative block, with explicit coupling through h_m=2(−1)^m/(π(2m+1)); entries are
absolutely convergent series in samples s_T(ω_k) (thm:nyq-schur(iii)). The arithmetic enters only through
s_T(ω_k)=c_T+ψ_T(ω_k), ψ_T(ω)=∫(1−cos ωu)dρ_T, ρ_T=K1_{(0,2T)}du+Σ v_nδ_{log n} (prop:nyq-LK). The Nyquist samples of the
comb are Σ_n v_n cos(πk log n/2T): at log n/2T rational (n=4 at T=log2, etc.) they are periodic in k; the "near-rational"
structure of log n/(2T) is the mesh analogue of near-coincidences. Not found in the index under this form; must be checked
against R160/R162 Nyquist entries (P48 Table operator: "Nyquist sampling, two sectors — coherence inequality equals the
target, REF").

### 7.8 cor:H1minus / prop:H
Exact: for T≥0.12, n_−(A_ev(T))≥1 (χ_ev is negative: a_{0.12}(χ_ev)/‖χ_ev‖^2 ∈ [−0.047±3.5·10^{-4}], interval arithmetic);
W^{ev}_T⪰0 ∀T ⇔ n_−(A_ev(T))≤1 ∀T. With §6(f): ⇔ no second even negative direction is ever born. Zero-side reading
(P48 eq:zeroside): A_ev(F)=Z_T(F)−2⟨F,χ_ev⟩^2. The node (P48) = A_ev ≥ 0 on χ_ev^⊥∩{ℓ=0} via the polar-free split.
Note: prop:H's converse direction is proved with the zero sum (lem:roughEF, 0<Reρ<1, Σ|ρ|^{−2}<∞) — a tool use, unconditional.
Angle (OPEN): the even sector has an explicit negative vector χ_ev with all Dirichlet-sine coefficients positive
(rem:chiev-sine); positivity of the even complete form is "rank-one perturbation of a form with exactly one negative
square" — Kreĭn/Pontryagin Π_1-space structure. A Π_1-type argument (Pontryagin space with one negative square, e.g.
Kreĭn–Langer / de Branges–Rovnyak with κ=1) would need the inertia n_−(A_ev)=1 as input, which is the target again (REF).

---------------------------------------------------------------------------------------------------------------------
## 8. Summary for the phase
- The open problem, in every form, is one non-linear, margin-exact inequality on the fixed vector (Λ(n))_{n<e^{2T}} plus the
  archimedean data at conductor 1; the corpus proves that no single-input (E) or (F) argument, no linear/certificate
  argument, no estimate with slack and no bounded functional can carry the sign.
- The only places the authors locate the sign: Near_M on vectors seeing near-coincidences; the non-integer Möbius-lattice
  classes of the exterior form; the even-sector node orthogonal to χ_ev; the Schur coupling ρ_T.
- Corrections to make in P47 (no effect on the target): eq:coer-sandwich and lem:wh-schurabs(ii) for λ_S<0 (§6(a));
  normalisation of F_0 (§6(b)); "exactly one negative eigenvalue for every T" → "≤1" or "T≥0.12" (§6(c), also P48);
  §ext-constraints item 2 comb-genericity of the half-line identity (§6(d)); secondary problem 8 reducible to one eigenvalue
  (§6(e)); add the exact two-sector reduction S_η (η↓0) as a fourth reduced form (§6(h)).
