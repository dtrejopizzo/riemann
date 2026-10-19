import json,collections,re
P='/home/trabajo/Documentos/research/riemann/03-research/phase-162-row-d-first-contact-closure/grid/'
d=json.load(open(P+'R162_2300_MASTER_grid.json'))
S={'P':'PINTADA','R':'MUERTA_CON_RESIDUO','A':'ABIERTA','V':'VACIA'}
SYM={'P':'■','R':'◩','A':'◧','V':'□'}
# cell: (code, [live residuals], comment)
C={
'1A':('R',['λ_W>0 beyond ½log5 (P47 Open 5): certificate, not mechanism; collides with M','Conjecture C_B (34/91) → lives in 8F'],'B3-KREIN and 34/91 absorbed by E1'),
'1B':('R',['R161_011 (4.2) global Sonin rank (R161_011; R162_1201): E1 sink of columns B/C'],'P121 current/strainer = tools'),
'1C':('P',[],''),
'1D':('P',[],'64 C,D tool (valid for DH)'),
'1E':('A',['Conj. A.15 (phase-28-four-fronts/01): Λ=max b_j²/2, monotonicity of the Kreĭn index under dBN, 0 later citations','D-109 critical anchoring (37/109): falsifiable partition, no mechanism'],'polarcap 156 → 703 (closed)'),
'1F':('P',[],'2200 gave it □; it has 6 DEAD routes [E1/F3]'),
'1G':('R',['converses/Hamburger as a sign mechanism in a family (only dictionary in 1203); must be uniform in the field (T1)'],'2200 gave it □'),
'1H':('A',['P122_D_SPECIFICATION: relative correspondence E_(∞,T) Bohr↔quarter-Γ Calderón (L6), never constructed','P25 V.2: Pontryagin completion with characters x^{b+iγ} (bridge κ(Q)=ind₋ H_C)','P152.1 Dolgopyat for Mayer via Lewis–Zagier (only desk EXCL in 157)'],''),
'2A':('R',['global semilocal CC (phase-5/B2) — not run; coincides with PATH-TO-D (ii) in 8D','115_13-16 derivative of the semilocal Sonin trace phase: favourable sign, exact identity nonexistent'],'P35 L1 = ε₀≥0 (E1)'),
'2B':('P',[],'60 CCM: last link ε₀≥0 ⟺ RH'),
'2C':('P',[],''),'2D':('P',[],''),
'2E':('P',[],'Pick/Schur: passivity at ω→0 = RH'),
'2F':('R',['complete monotonicity / Bernstein of λ_A(T) or of its transform as a global object (2200)'],'2200 gave it □; 4 DEAD routes'),
'2G':('A',['P46 §28.4: six-clause object on the adelic square — no candidate constructed','T3 Beurling (150): conditional on H-DMV, already CITED (157)'],''),
'2H':('A',['phase-15-arithmetic-hodge-index/M10: Arakelov witness variety 𝒳 (not constructed)','PHASE_136 S5: Cartwright tropical Hodge index at chart level (never run)'],''),
'3A':('A',['P47 Problem A: class-dependent lower bound (only ceilings proved)','R154_030: two-prime window at 0.58, off-machine package (numerical)','S1 (141.G1/199): per-window arithmetic beyond Montgomery–Vaughan — ceiling 172.9, predecessor of M'],'114 ½log5 → DONE in R162_303/703'),
'3B':('P',[],'continuity of λ_A and rate 407 = tools'),
'3C':('R',['Option 3 of R160_020: sign bound uniform in T for the low-frequency block outside the contact vector (M7 Prop 5.2(c) suggests E1)'],'C_D (34/93) without support'),
'3D':('A',['GAP-196.A: near-doubles of Λ_f of DH below the mean spacing (never attacked)','22/03 GMC rigidity (conditional)'],'LP-134 dies at scale 1/log T'),
'3E':('A',['GAP-157.A: discrepancy of the Kronecker flow (2 of 3 routes dead; central implication undecided)'],'Tower 1: A ⟹ Lindelöf; Dic undetectable (198.2)'),
'3F':('R',['A1 (103_13, Laguerre of ψ−x, n≥8): open but of RH strength (105: subexponential bound = RH)','nonlinear global transform (Mellin in T) (2200)'],'2200 gave it □; 10 DEAD routes'),
'3G':('P',[],''),'3H':('P',[],''),
'4A':('A',['GAP-135.A / doc 148: incommensurable frames (Seip, Olevskii–Ulanovskii), never resumed','159 G2_B8 Thms L,L′,L″,D: local Euler threshold ½log3≤T_loc≤0.5925, unaudited'],'Thm A 153 separates only from Ξ_a'),
'4B':('R',['distributional carrier (83–84, ker X=span δ₀) not excluded by the domain obstruction','minimal cut A1–D3 (phase 80) — the anchor is ⟺ RDI (93, E1)'],''),
'4C':('R',['doc 107 (Weil in two variables, "LIVE CANDIDATE"): seems absorbed by 108 (E1) and MW-7 — NOT CONFIRMED','R160_020 Option 6 (Meyer mixed class S+D): never run; D2 declares it sterile'],''),
'4D':('A',['Exclusion conjecture (21/01-02): all on the line or infinitely many off; neither proved nor refuted, never resumed'],''),
'4E':('A',['P30: lemmas L8 (m<∞) + LP-112 (sequential rigidity); both open, not ⟺ RH','90: projective Kato current PROJECTIVE-KATO-EULER','prime-by-prime insertion flow coupled by Euler (2200)'],'2200 gave it □'),
'4F':('R',['global generating object with Euler entering before regularizing (2200) — never attempted'],'only route: 103_16-21 (five truncation no-gos)'),
'4G':('P',[],'T2 tool'),
'4H':('A',['phase-27-adelic-rigidity: local-global adelic rigidity, walls A and B open (objects, not signs)','36/106+38/117 amplifier functor ⊠ with corrections'],''),
'5A':('R',['Problem A (P47) — same residual as 3A'],''),
'5B':('P',[],''),
'5C':('A',['discontinuous functional separating ℤ from Beurling and 1 from χ₂, not a unipotent invariant (residual of R162_903)'],''),
'5D':('R',['integrality in the spectrum: multiplicities / Smith form of the contact Gram (2200)'],'2200 gave it □; 3 DEAD routes'),
'5E':('A',['O1802.3: width ≥0 of the residual window via NONlinear integrality in c, followed in T (1902 closed only the linear one)'],''),
'5F':('V',['periodization/Poisson in the variable T of a global object (2200)'],'only truly empty cell'),
'5G':('P',[],'2200 gave it □; 107 atlas c_p, mod-32, Galois ring 147'),
'5H':('A',['o-minimality / Pila–Wilkie / rigidity of ×p measures versus W_T (157: desk EXCL only)','torsion cocycle Φ_Λ (R162_1001) with non-band-limited tests','THE_BACKWARD_MAP a4/R16 (quadratic χ over Spec ℤ)','Quillen K_n(ℤ)/regulators, RO(G), A¹-motivic (AUDIT_A §3), untouched','P42 arithmetic Lefschetz programme: global sign argument open'],''),
'6A':('A',['157 O3 lem:degen: degenerate case (Λ maximizes concave V_T), untouched','O-D4.2: kernel of 𝒲 / cone 𝒞′ on decreasing tests of unbounded support'],''),
'6B':('A',['P47 prob:annihilate = Gate 1 of phase 162 (annihilation of Γ moments at first contact)'],'all routes of 162 in the cell dead'),
'6C':('A',['R162_901: difference channel |Σw_n n^{it}|² of Selberg at the edge, without resumming to Σ_ρ'],''),
'6D':('A',['155 P2: structural identity for S_even at log 2 ("no identity attempted")'],''),
'6E':('P',[],''),
'6F':('A',['P47 Problem B: arithmetic certificate w_T from exterior primes (no construction)','114 D.260-262: centred Chebyshev channel dΨ−dx, exact residual, sign open'],'A1 = E1'),
'6G':('R',['coefficient separator 119 (P0/P1/P2) separates ζ from DH but does not suffice'],'2200 gave it □'),
'6H':('R',['Option 6 / O-B5.1′ Borger W(R): never constructed (C4 only reformulated it)','P40 strict excess g>δ — it is the sign (E1)'],'2200 gave it □'),
'7A':('A',['D.16-γ (138): cone cut by the zero datum in class 𝒫 (repaired form R138_004 C2), never attempted'],'122 two gates fail for Ξ_a'),
'7B':('R',['159 G2_B6_R4 BRS uniqueness mod Lemma S (unaudited), Thm X extreme point unaudited'],'121 F2 = global square'),
'7C':('R',['nonlinear functional with pair correlation as exact input (2200)'],'2200 gave it □; P121 D_T^crit = global square'),
'7D':('R',['R-C.b for ζ needs input from the zero side; per window it collides with M (2101, 2190)','P23: reverse inclusion J_∞ ⊂ zeros of C_∞'],''),
'7E':('A',['77–80: (c) pencil compatibility, (d) ℓ² class, (e) simplicity, (f) assembly, FIXED-L-WEYL, SAFE-GAMMA-IDENT','P19 Hyp D: m<∞ ⟹ m=0 (C_B; see 8F)'],''),
'7F':('A',['KEP: Nevanlinna parametrization of 𝔖(T) across T (never written)','P33: finiteness A and purity D of the Cesàro −π/8'],'803 = Herglotz (E1)'),
'7G':('P',[],''),
'7H':('A',['113_12 Ansatz A: χ(D)=D²/2 (implies RH, passes the tests, never attacked)'],''),
'8A':('A',['pending audit: 159 G2_B8_R5 Thm L″, G2_B2_R4 Thm U, R5 (Lemma S, Cor M1, Prop J)','GAP-198.1: non-factorizable inter-currency combinations outside 𝔄'],''),
'8B':('A',['R160_X_C1: rigid negative Blaschke witness (CF/CvS) at first contact, without margin'],'R162_408 (NE) exact = tool'),
'8C':('A',['O-151.4: summand-vs-numerator axis as a mechanism (never developed)'],''),
'8D':('A',['PATH-TO-D (ii): A_T as compression of an explicit self-adjoint operator (semilocal CC)','115_15: Connes–Consani Sonin count #{λ_j(K_I)>1}'],'R-C.b dead by the Type I curve (2001/2190)'),
'8E':('R',['92 CA-1 fixed-L convergence; Ω₇ (66) fails at the critical endpoint'],'P39 gap without cut ⟺ target'),
'8F':('A',['dichotomy m<∞ ⟹ m=0 (37/112-113, 38/115-116, LP-112, Stepanov): a single lemma, not ⟺ RH'],'P29 master quantifier = tool/wall'),
'8G':('R',['field-uniform proofs allowed by T1 (157)'],'2200 gave it □'),
'8H':('A',['160 D1: Torelli-failing lamination with fixed points (only carrier class not excluded by Thm Z/Thm H)','28/02 APS η-invariant; 28/03 class [H_C] in KK','108 Stage 7 scale compatibility','boundary triples for W_λ / uniqueness of B_CCM (AUDIT_CONSOLIDATED §2)','121 conservation law of the Kreĭn flow (L4/M11)','42/128 Deninger with Kähler–Riemann foliation','159 unaudited: non-ergodic DK_α, Prop BL ℤ[ℚ/ℤ]'],''),
}

# ---- part6 (phases 160-161 sub-audit) merge + corrections ----
import os
ids={r['id'] for c in d['cells'] for r in c['routes']}
cmap={f"{c['row']}{c['col']}":c for c in d['cells']}
p6=P+'R162_2300_part6.jsonl'
if os.path.exists(p6) and not d.get('part6_merged'):
    for l in open(p6):
        if not l.strip(): continue
        x=json.loads(l)
        if x['id'] in ids: continue
        x['source_part']=6; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
    d['part6_merged']=True
for c in d['cells']:
    for r in c['routes']:
        if r['id']=='R161_016': r['killer']='F2'; r['note']=(r.get('note','')+' [corrected by part6: killer F2 (orientation), not F1]').strip()
        if r['id'] in('R161_018',) or r['id'].startswith('R161_008-011,017-018'):
            r['note']=(r.get('note','')+' [R161_075: the general exclusion by linear limit is "unproved as written"]').strip()
        if r['id']=='R161_068-070': r['note']=(r.get('note','')+' [069 is not a no-go: corrected by 070]').strip()
upd={
'1C':('R',['R161_020-021: scalar terminal target X_T=½‖(I+εC_log)g‖², not realized from finite (PC-ren)'],'formerly ■'),
'1D':('A',['NG-D4 / I15: identity Q(f,g)+Q(f̂,ĝ)=0 (Fourier anticommutation), posed and never attacked','phase-60 §4.B: boundary triples for W_λ (deficiency (4,4)), RH-neutral, never attempted'],'formerly ■'),
'2C':('R',['P41 thm:doob: nonlocal corridor with sign, never executed (E1: RH ⟺ a sharp Poincaré)'],'formerly ■; R161_026-028 F3 (Λ≥0 does not suffice)'),
'2E':('A',['prop:polarcap: polar capacity 𝔊_T as a function of T (S^Sch≈−J), never analysed in T; D3 follow-up of M4 never run','P47: effective window shift RD_{T′} ⟹ λ^W_T≥0 (at comb level requires T′≥T*_{∞,P})'],'formerly ■'),
'3F':('A',['GAP-157.A nonlocal Tauberian with LI input (F40; Beurling–Malliavin on p^{iτ})','rem:Dgrade: union of graded and tail techniques'],'A1 = RH strength; formerly ◩'),
'4C':('A',['doc 107 / I7: Weil form in two variables W_2 (prime×prime block with sign +; Lemma 5.2 open) — S1 lists it live; absorption by 108 NOT CONFIRMED','L5 (114): Z_{N,ε} with R=Z*Z without pseudoinverse, never constructed','G2_B3_R5 Cor S2: Hecke-type algebra on L²(ℝ) with archimedean multipliers (coupled square), no candidate','R160_020 Option 6 (Meyer S+D): never run; D2 declares it sterile','R161_030-032: source of the oriented variance gate open'],'formerly ◩'),
'4D':('A',['Exclusion conjecture (21/01-02)','R161_068-070: Γ–Euler detector −ζ′/ζ(2m+1), faithful; primitive Weil comparison open (069 corrected by 070, not a no-go)'],''),
'4E':('A',['P30: L8 + LP-112','O8 (61) / S2 §3.2: 2×2 Tate transfer canonical system, index collapse κ₀+|S|→0 (partially constructed)','R153_005 Thm A cross term as a sign mechanism uniform in T (P153.2), never attempted','90 PROJECTIVE-KATO-EULER'],''),
'4F':('A',['GAP-157.A: condition C1 of Doc 159 (nonlocal Tauberian), neither known nor excluded','global generating object with Euler before regularizing (2200)'],'formerly ◩'),
'5F':('A',['R161_075-079: local Weil limit / Poisson domain / weak renormalization in primitive L² — limit constructed (PNT remainder), value not proved zero, radicality not preserved'],'formerly □ (only empty one); part6 fills it'),
'6E':('A',['G2_B6_R5 Prop C: RH-free pointed cone of rigid perturbations C≠{0}','P153.14 stepped Kreĭn-band admissibility of the atom w_N (only N=3,4,5 measured; uniform = RH)'],'formerly ■'),
'6G':('A',['O-D4.3: transposition of identity (C′) to ζ_K, routine, never done','separator 119 (P0/P1/P2) insufficient'],'formerly ◩'),
'6H':('A',['Paper 43 Thm 10.8b: global Mertens hyperbolic ruling pairing (excluded from row A by A.10, not from row D)','106.203-205: Tate boundary loaded with corrected mass log p/p^{k/2} (non-isometric resonant completion)','O-B5.1′ Borger W(R) not constructed'],'formerly ◩'),
'7D':('A',['Target L8/C_B/EX: m≤C quadruples; m<∞ ⟹ m=0 (see 8F)','phase-69: gauge-invariant signed Cayley index (named, not constructed)','R-C.b for ζ needs input from the zero side (2101)'],'formerly ◩'),
'8B':('A',['R160_X_C1 rigid negative Blaschke witness (class level: passes Λχ₂ and comb; exclusion OS-1 = RH)','slot M11 (never written): opposite-metric monodromy trace as a conservation law'],'R161_016: killer corrected to F2'),
'8G':('R',['field-uniform proofs (T1)','36/106 tensor amplification: finiteness sub-lemma R-FIN missing'],''),
'5H':('A',C['5H'][1]+['Paper 44 §6bis: lattice from the integral shadow Sh_Z with finite I_A','Paper 43 §11bis: non-invertible correspondences (graphs of degree q)'],''),
'8H':('A',C['8H'][1]+['Request 122.A: natural self-duality of H¹(D) in 2D=K','I14 (40/123): Čech complex of D_0, never executed','R158_001 laminated carrier with fixed points + ALK polarization'],''),
'2H':('A',C['2H'][1]+['S1 I1: entangled (non-product) OS model of all of W_T, never attempted','Chinburg–Rumely: energies outside 𝔄⁺ (Berkovich kernels), not read'],''),
'4A':('A',C['4A'][1]+['Paper 44 (H_L): negative primitive on Dirichlet profiles'],''),
'4H':('A',C['4H'][1]+['Paper 44 Thm 8bis.4a: L1 colimit version of the pure Frobenius form','I11 (34/96): absorbing-channel torsion / symplectic curvature'],''),
'8C':('A',C['8C'][1]+['Lemma 108: bound κ_W(Q_2)≤C n_W (not ⟺ RH), never attacked'],''),
'6A':('A',C['6A'][1],''),
'3A':('A',C['3A'][1]+['S5 §5#14: web hit "Certified Weil positivity beyond the unit window" unread','I6 (36/108): dimension bound of the negative block under resolution'],'114/D.172 (old ½log5) DOWNGRADED; the certificates of 162 at ½log5 (303/391 primitive, 703/791 complete; Arb, full audit reruns) are independent of D.172'),
}
C.update(upd)

# ---- part7 (phase 162 rounds 22-24: R162_2201, 2202, 2301, 2302, 2401, 2402) merge ----
p7=P+'R162_2300_part7.jsonl'
if os.path.exists(p7) and not d.get('part7_merged'):
    for l in open(p7):
        if not l.strip(): continue
        x=json.loads(l)
        if x['id'] in ids: continue
        x['source_part']=7; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
    d['part7_merged']=True
H90=' [R162_2290 audit: 2201 Thm N3 downgraded to a proposition about the three listed routes (F6); N1(a) factor 2, N1(b) only ⟹; 2202 Thm NI correct (only n<e^{T_c}); Thm ND requires ι-invariance (F12); example of Prop T false (F11)]'
for c in d['cells']:
    for r in c['routes']:
        if r['id'] in('R162_2201a','R162_2201b','R162_2201c','R162_2202a','R162_2202b') and 'R162_2290' not in r.get('note',''):
            r['note']=(r.get('note','')+H90).strip()
        if 'R160_X_C1' in str(r['id']) and r['status'] in('OPEN','PARTIAL'):
            r['status']='DEAD'; r['note']=(r.get('note','')+' [superseded by R162_2201/2202/2401 (part7)]').strip()
d['part7_tools']=['Thm NI (2202): w_x=L(x)/F̂′(x), only n<e^{T_c}','Thm ND (2202, with ι-invariance): there is no descent','Thm N1 (2201): atomic object 𝒜(s;G)=Σq_x(−ζ′/ζ)(s+ix)','Lemma S (2301): Selberg identity ⟺ a=Λ (recursive)','Thm Q (2301): exact nodal quadrature in type ≤2T_c (Akhiezer)','Thm HV (2401): H = sum channel of the witness mean','Lemma U (2401): witness+μ^< determine the hidden comb','Thm N (2302): weak limit ≡0 via ζ(1−ρ)=0','Thm V (2302): radicality ⟺ Gate 1']
upd7={
'8B':('R',['O2201.1: asymmetric nodal weight = Z′/Z with sign at the nodes (zero side)','slot M11 (never written): opposite-metric monodromy trace'],'part7: Blaschke–torsion DEAD (R162_2201a/c, 2401a); formerly ◧'),
'5C':('R',['O2201.1: asymmetric nodal weight = Z′/Z with sign (zero side)'],'part7: R162_2201b DEAD (FE + nodal symmetry erase the atoms); formerly ◧'),
'6C':('R',['OS-2: parity of the witness (Prop P2 of 2401: H(F^ev)=−H(F^odd); only parity fixes the sign)'],'part7: R162_2301 (Lemma S, Thm Q) + 2401 closes O2202.2; formerly ◧'),
'5F':('R',['O2302.2: c_f≠0 from integrality (left exterior Tate moment in the radical)','O2302.1: remainder at finite N (Li type, E1 expected)'],'part7: R162_2302 Thm N (limit ≡0 via ζ(1−ρ)=0), Thm V; formerly ◧'),
'5H':('A',[x for x in C['5H'][1] if not x.startswith('o-minimality')],'part7: o-minimality/Pila–Wilkie DEAD (R162_2402: W10+W8)'),
'6B':('A',C['6B'][1]+['O2202.1: [prim] version of Thm NI'],'part7: Thm NI tool; Euler/Möbius self-similarity DEAD (2202b)'),
'7D':('A',C['7D'][1]+['O2401.1: individual sizes of V(F_M), H(F_M)'],'part7: margin of Thm M does not come from hidden contacts (2401b)'),
}
C.update(upd7)

# ---- part8 (phase 162 rounds 25-26: R162_2501, 2502, 2601, 2602 + audit 2590) merge ----
p8=P+'R162_2300_part8.jsonl'
if os.path.exists(p8) and not d.get('part8_merged'):
    for l in open(p8):
        if not l.strip(): continue
        x=json.loads(l)
        if x['id'] in ids: continue
        x['source_part']=8; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
    d['part8_merged']=True
SUP8={'R161_068-070':'R162_2502','phase-115/115_15':'R162_2602b','PATH-TO-D (ii)':'R162_2602a','phase-37/112-113 +38/115-116':'R162_2501'}
H2590=' [R162_2590 audit: nothing WRONG; 2501 Prop 1 upper bound repaired (θ in ellipse), law 2β* holds; M_m correct (2m pairs); Prop 3 E restricted to quartet type; 2502 Thm K only "(4.1) at least as strong as Gate 1"]'
for c in d['cells']:
    for r in c['routes']:
        if r['id'] in SUP8 and r['status'] in('OPEN','PARTIAL'):
            r['status']='DEAD'; r['note']=(r.get('note','')+f' [superseded by {SUP8[r["id"]]} (part8)]').strip()
        if r['id'] in('R162_2501','R162_2501a','R162_2501b','R162_2502','R162_2502a') and 'R162_2590' not in r.get('note',''):
            r['note']=(r.get('note','')+H2590).strip()
d['part8_tools']=['Exponent law (2501a): under H(m) lim (1/T)log(−λ_A)=2β*, floor −4e^T','Model M_m (2501b): ξ × quartet factors, κ=κ(ζ)+4m, shares the whole class structure','Thm K (2502a): faithful comparison without division ⟺ Gate 1, ‖K_T‖≥c/λ(T)','Thm T (2601b): m=0 ⟺ D tempered; exponential type of D mod S′ = β*','Hamburger rigidity (2601c): atomic log-derivative + FE conductor 1 + finite order ⟹ F=cζ (cited from memory)','Sonin count N(T) (2602b): n₋(A_T|P_T) nondecreasing, first jump = first contact, lim N=2κ_off']
O26='O2601.1: individual property of the Euler product of ζ that uses the exact values of Λ nonlinearly and bounds the off-line count (fails for deletion, M_m, Λ̃)'
upd8={
'4D':('A',['Exclusion conjecture (21/01-02): all on the line or infinitely many off — it is C_B, converges to O2601.1'],'part8: Γ–Euler detector R161_068-070 NO-GO (R162_2502 Thm D/K, Prop A); residual folded into R162_1603 (d)'),
'8F':('R',[O26],'part8: route (a) of C_B DEAD (R162_2501: law 2β*, model M_m, Thm 3); O2501.1 false as stated (2601a, Λ̃); formerly ◧'),
'8D':('R',[O26+' (= O2602.1: sup N<∞ ⟹ N≡0)','O2602.2: δ=2?'],'part8: R162_2602 PATH-TO-D (ii) and CC Sonin count DEAD (E1/F3); formerly ◧'),
'7E':('A',[x if not x.startswith('P19 Hyp D') else 'P19 Hyp D: m<∞ ⟹ m=0 (C_B) → O2601.1 (8F)' for x in C['7E'][1]]+['O2501.2: e<1 ⟹ Θ<1 without finiteness'],'part8: exponent law 2β* (2501a) tool'),
'5F':('R',C['5F'][1],C['5F'][2]+'; part8: atomicity does not exclude E (2601a, falsifier Λ̃)'),
}
C.update(upd8)
# ---- part9 (phase 162 rounds 27-28: R162_2701, 2702a-c, 2801, 2802 + audit 2890) merge ----
p9=P+'R162_2300_part9.jsonl'
if os.path.exists(p9) and not d.get('part9_merged'):
    for l in open(p9):
        if not l.strip(): continue
        x=json.loads(l)
        if x['id'] in ids: continue
        x['source_part']=9; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
    d['part9_merged']=True
SUP9={'R160_S2 §3.2 phase-61 O8':'R162_2701','phase-36/107':'R162_2702a','R160_S1 §5 I7 phase-36/107':'R162_2702a','R160_S1 §2.5#35 phase-28-four-fronts/02 NG-D4':'R162_2702c','R160_S2 §3.2 phase-60 §4.B':'R162_2702b'}
for c in d['cells']:
    for r in c['routes']:
        if r['id'] in SUP9 and r['status'] in('OPEN','PARTIAL'):
            r['status']='DEAD'; r['note']=(r.get('note','')+f' [superseded by {SUP9[r["id"]]} (part9)]').strip()
        if r['id']=='R162_2701' and 'R162_2890' not in r['note']:
            r['note']=r['note'].replace('phase-61 kappa0+|S| = free back-propagation artefact, uncertified grid count','phase-61 kappa0+|S|: uncertified; index 0 after normalization')+' [R162_2890 audit: the "artefact" claim is WRONG; replaced by "uncertified; index 0 after normalizing"; NO-GO stands]'
        if r['id']=='R162_2702b' and 'R162_2890' not in r['note']:
            r['status']='DEAD'
            r['note']+=' [R162_2890 audit: WRONG — ±∞ are limit-circle, deficiency (4,4) not (2,2) (the phase-60 count should be (6,6)); U(2), B_CCM=B_∞ and the Weyl function must be REDONE; tool downgraded to "to be redone". Prop 2.5 (Λ-free invariants) survives ⟹ NO-GO for O2601.1 (W3) stands]'
        if r['id'] in('R162_2702a','R162_2702c','R162_2801','R162_2802') and 'R162_2890' not in r.get('note','') and r['id'] in ('R162_2702a','R162_2702c'):
            r['note']+=' [R162_2890: stands]'
d['part9_tools']=['Thm TC (2701): 2×2 Tate canonical system, H_S=½exp(2Θσ₁), Θ=Σ artanh p^{-1/2} (Euler only at s=½, independent of z)','Thm P (2701): H≻0 for every chain of boosts (J-inner, κ=0 after normalizing; RH-neutral)','Lemma 1 (2801): −ζ₀′/ζ₀ = Dirichlet + canonical rational (almost periodicity), ζ₀=ζ/R','Lemma 2 (2801): ζ₀ is not a Dirichlet series, outside S (Beurling type)','Lemma 3 (2801): Hamburger with symmetric rational defect returns c·ζ·R for every m','Thm PB (2802): Piltz Perron with integer k does not see zeros; H(m) ⟹ LH ⟹ α_k≤½ ∀k','Thm L (2802): exact terminating identity Σ Λ/log = Σ_j (−1)^{j+1}/j Σ_i (−1)^{j−i}C(j,i)D_i (formal, blind to m)','(to be redone) boundary triple of W_λ (2702b): deficiency (4,4) according to 2890; only Prop 2.5 (Λ-free) certified']
O28a='O2801.1 (sub-form of O2601.1): can the generalized-integer measure dN₀ of ζ₀=ζ/R be ≥0 with all zeros real? (nonlinear in Λ)'
O28b='O2802.1 (sub-form of O2601.1, row 5): non-formal property, uniform in k≍log x, of the integer book b≡1 (Piltz up to k≍log x = bound on ψ, E1 expected)'
upd9={
'4E':('A',[x for x in C['4E'][1] if not x.startswith('O8')],'part9: O8 Tate 2×2 CLOSED (R162_2701 NO-GO: Thm TC, Thm P, Thm I; W12); phase-61 index uncertified, 0 after normalizing (2890)'),
'1D':('R',['redo the boundary triple of W_λ with deficiency (4,4) (2890; RH-neutral tool, not a mechanism)','O2702.1: comparison with Burnol (RH-neutral)'],'part9: NG-D4 DEAD (2702c, index count); boundary triples/B_CCM NO-GO for O2601.1 (2702b, Λ-free invariants, W3) but the deficiency computation (2,2) is WRONG (2890: (4,4), limit circle at ±∞); formerly ◧'),
'4C':('A',[x for x in C['4C'][1] if not x.startswith('doc 107')],'part9: doc 107 / W_2 CLOSED by doc 108 (R162_2702a, W2+E1; it is not MW-7)'),
'4F':('A',C['4F'][1]+[O28a,O28b],'part9: R162_2801 (quantitative Hamburger, Thm NG) and R162_2802 (multiplicative book, Thm PB/L) NO-GO; sub-forms of O2601.1'),
'5E':('A',C['5E'][1]+[O28b.replace(', row 5','; route in 4F')],'part9: O2802.1 folds into row 5 (integrality b≡1)'),
'8D':('A',['phase-37/110 (PARTIAL; the entry R160_S1 §2.2#12 gives it DEAD — unreconciled duplicate)','phase-35/99 (R160_S1 §2.7#45, PARTIAL)','phase-63 (R160_S2 F9, PARTIAL)','R160_010 D1/D3/D5 (OPEN)'],'part9: rule §8 — 4 PARTIAL/OPEN routes not superseded ⟹ ◧ (part8 had lowered it to ◩ by mistake); O2601.1 (= O2602.1) and O2602.2 remain attached via 8F'),
}
C.update(upd9)
# ---- part10 (round 29: R162_2901, 2902a-c) + part11 (phase 163: R163_001-003, 101, 102, audit 190) merge ----
for n in (10,11):
    pn=P+f'R162_2300_part{n}.jsonl'
    if os.path.exists(pn) and not d.get(f'part{n}_merged'):
        for l in open(pn):
            if not l.strip(): continue
            x=json.loads(l)
            if x['id'] in ids: continue
            x['source_part']=n; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
        d[f'part{n}_merged']=True
SUP10={'155 P2 even Schur':'R162_2902a','157 O3 lem:degen':'R162_2902b'}
for c in d['cells']:
    for r in c['routes']:
        if r['id'] in SUP10 and r['status'] in('OPEN','PARTIAL'):
            r['status']='DEAD'; r['note']=(r.get('note','')+f' [superseded by {SUP10[r["id"]]} (part10)]').strip()
d['part10_tools']=['Structural identity S_even at log 2 (2902a): Π^even=−½(v₂R₂+v₃R₃), ‖Π_log2‖=0.9009276','lem:degen D1–D3 (2902b): degenerate case ⟺ v(Λ)∈argmax V_T, λ^A_T=M_T (Λ-blind)','2902c: spec S={0,±½}, V concave ½-Lipschitz, Danskin derivative','R162_2901 Props 1–2: dΠ₀ of ζ₀=ζP₀/P; Thm B: ζS₁^K P₀/P positive Beurling with RH (no contradiction)']
d['part11_tools']=['Canonical exchange E and D_test (R163_001, 7F)','Positive factorization support lemma (R163_002, 5F)','Lemma R (R163_101): rational modifications of ζ do not answer BF_θ','Thm R (R163_102): N=⌊x⌋+c eventually ⟹ ℕ','Lemma S (R163_102): ζ·A, Σ|a|<∞ ⟹ N=A(1)x+O(1)','Thm T + Cor F (R163_102, ρ>0): transfer of zeros; finite perturbations ⟹ RH_B ⟺ RH','Révész 2207.00665 Rem. 7 via Hilberdink 2010 (R163_191a, cited): discrete with θ<½ ⟹ zeros with β>θ']
BFD='BF_θ^disc (sharpened O2601.1, discrete Beurling frontier): does every discrete system (integer multiplicities) with N=ρx+O(x^θ), θ<θ₀≈1/3, satisfy Beurling RH? (ℤ: θ=0; ζ_θ refutes it in the extended class)'
upd10={
'4F':('A',[x for x in C['4F'][1] if not x.startswith('O2801.1')],'part10: O2801.1 CLOSED negative (R162_2901 Thm A/B NO-GO; residual = integrality/atomicity of dN, O2601.1)'),
'6D':('P',[],'part10: P2 DONE (R162_2902a, exact structural identity, Λ-blind; tool)'),
'6A':('A',['lem:degen case log 2 (R162_2902b): two-sided enclosure of the minimizer of the complete form','O-D4.2: kernel of 𝒲 / cone 𝒞′ on decreasing tests of unbounded support'],'part10: 2902b lem:degen PARTIAL (D1–D3), 2902c P153.17 NO-GO'),
'5G':('A',[BFD,'O163.101a: Conjecture C_{1/3} (control of the exp_* chaos of random rounding)','O163.101b: discrete construction with Θ<1/3 and zeros off, or integrality obstruction at θ<1/3','O163.101c: Révész Rem. 7 / Hilberdink 2010 (discrete θ<½ ⟹ zeros with β>θ, R163_191a) and the exponent matching of Hilberdink 2005: do they sharpen towards the line?','O102.1–3: non-lattice system with ρ=1; (BF_0) with σ_τ>½; Thm T modulo multiplicative cancellation'],'part11 (phase 163): Beurling frontier; ζ_θ refutes the (extended) class branch; Lemma R, Thm R, Lemma S, Thm T/Cor F tools; analytic and perturbative NO-GO; formerly ■'),
'5F':('R',C['5F'][1],C['5F'][2]+'; part11: support lemma (R163_002a) tool, falsifier K (002b)'),
'7F':('A',C['7F'][1],C['7F'][2]+'; part11: canonical exchange + D_test tool (R163_001); property 2 ⟺ RH (R163_003a, E1)'),
'8F':('R',[C['8F'][1][0]+' → sharpened in part11 to BF_θ^disc (5G)'],C['8F'][2]),
}
C.update(upd10)
# ---- part12 (round 31: R163_201-203, audit 290) + part13 (phase 163 rounds 32-37: R163_401-1001) merge ----
for n in (12,13):
    pn=P+f'R162_2300_part{n}.jsonl'
    if os.path.exists(pn) and not d.get(f'part{n}_merged'):
        for l in open(pn):
            if not l.strip(): continue
            x=json.loads(l)
            if x['id'] in ids: continue
            x['source_part']=n; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
        d[f'part{n}_merged']=True
d['part12_tools']=['Prop 2.1/Cor 2.2 (R163_201a): joint homogeneous modes H^P = residues on Re s=0; invariant space e^{u/2}C','Lemma U (R163_202): trivial (one prime with log p>2T suffices; audit R163_290)']
d['part13_tools']=['Light cone + law sinh(2δT)−2δT=δL (R163_402, erratum D1)','Existence of the real-rooted witness (R163_501, repair R(d′))','Unconditional Q0, Σδ²≪R/logR (R163_502)','Thm 1 of R163_601: exact cell decomposition of P_loc','R163_801 Thm 3/Cor 3.1: the tail 𝒯_X of −ζ′/ζ carries every off-line residual','Theorem C (R163_803): discrete systems with θ∈(1/3,½) and zeros on Re s=(1+θ)/2','Thm F (R163_901): family f_t with the window of ζ and zeros off','Thm O + f_χ (R163_1001): integrality = identification or sign-blind (W3′)']
BFD13='BF_θ^disc, θ≤1/3 (sharpened by Theorem C of R163_803: for θ∈(1/3,½) there exist discrete systems with zeros off): does every discrete system with N=ρx+O(x^θ), θ≤1/3, satisfy Beurling RH? (ℤ: θ=0). Line L2 of R164_000'
upd13={
'5G':('A',[BFD13,'O163.803a: rounding with negative correlation to push the error below x^{1/3} (L2a of R164_000)']+[x for x in C['5G'][1] if x.startswith(('O163.101b','O163.101c','O102'))],C['5G'][2]+'; part12: Euler gate (R163_202) NO-GO; part13: Theorem C (R163_803, audit 891 VALID WITH FIXES) closes O163.101a on (1/3,½)'),
'1G':('R',['converses/Hamburger as a sign mechanism in a family: sharpened by Thm O.2 (R163_1001) — it would have to be GRH in degree one, uniform in χ (W9/T1)'],C['1G'][2]+'; part13: Thm O + f_χ (R163_1001O) tool, wall W3′'),
'5E':('A',C['5E'][1],C['5E'][2]+'; part13: R163_1001a (deformation) DEAD [E1 + decoupled invariants]; the residuals O1802.3/O2802.1 are not touched by R163_1001 (§7), the cell stays ◧'),
'5F':('R',C['5F'][1],C['5F'][2]+'; part13: R163_1001b/c (theta periodicity, window Hamburger) DEAD [W3′ + E1]; residuals O2302.1/2 untouched'),
'5A':('R',C['5A'][1],C['5A'][2]+'; part13: R163_901 (f_t, Thm F) DEAD [F3:f_t]'),
'7B':('A',['R163_401: (★_cell) at the first-contact witness (⟺ RH at the witness, Rem 4.8a); tail form (TC) in R164_000'] + C['7B'][1],C['7B'][2]+'; part13: R163_401 PARTIAL (closure candidate), R163_402 tool; formerly ◩'),
'7F':('A',C['7F'][1],C['7F'][2]+'; part13: R163_801 Thm 3/Cor 3.1 tool (the tail 𝒯_X carries the off-line residuals)'),
}
C.update(upd13)
# ---- part14 (phase 164 rounds 1-2: R164_101, 102, 201, 401, 402; audit R164_190; audit 291) merge ----
for n in (14,):
    pn=P+f'R162_2300_part{n}.jsonl'
    if os.path.exists(pn) and not d.get(f'part{n}_merged'):
        for l in open(pn):
            if not l.strip(): continue
            x=json.loads(l)
            if x['id'] in ids: continue
            x['source_part']=n; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
        d[f'part{n}_merged']=True
d['part14_tools']=['Thm R (R164_401): sinc annihilation of self-dual measures with gap (−X,X), X>1, and sign ≥0 outside ℤ ⟹ support in ℤ ⟹ f=ζ (Hamburger with positivity instead of integer support)','Theorem L (R164_201, audit 291): in 𝒦_θ, θ<1/3, error ≫ x^{θ+δ(θ)} for every bounded-deviation rounding','Thm L Landau–Pringsheim of the tail, Thm H, Prop D (R164_102, R164_101)']
O201a='O164.201a: discrete Beurling system outside the Witt lattice with error O(x^{θ′}), θ′≤1/3, and a zero with β>½ (ARGUED that it must be outside the lattice, via L*)'
upd14={
'5G':('A',[C['5G'][1][0],O201a]+[x for x in C['5G'][1] if x.startswith(('O163.101b','O163.101c','O102'))],C['5G'][2]+'; part14: R164_201 Theorem L PROVED (audit R164_291): L2a/O163.803a CLOSED NEGATIVE in 𝒦_θ; Thm R (R164_401) tool: integrality of the support forced by positivity+gap+FE'),
'4F':('A',C['4F'][1],C['4F'][2]+'; part14: R164_101 (KZ) DEAD [E1], R164_102 positive tail DEAD [Thm A], R164_402 superseded; R164_401 Thm R closes O164.101 by identification (O164.101 ⟺ ¬RH); other residuals untouched, the cell stays ◧'),
}
C.update(upd14)
# ---- part15 (phase 164 rounds 3-4: R164_501, 502, 503, 601, 491; audit R164_190; phase closed) merge ----
for n in (15,):
    pn=P+f'R162_2300_part{n}.jsonl'
    if os.path.exists(pn) and not d.get(f'part{n}_merged'):
        for l in open(pn):
            if not l.strip(): continue
            x=json.loads(l)
            if x['id'] in ids: continue
            x['source_part']=n; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
        d[f'part{n}_merged']=True
d['part15_tools']=['Thm SA (R164_501): every test ≥0 annihilated by the kernel equation is ĤĤ^#, H∈E_c (critical node density); Cor SA.1 ladder','Prop 4 (R164_501): tail of Λ with sign at real height, Σ_ρΨ_y(t_ρ)=𝔄_y−G(iy)²𝒯(iy)','L1/L4/L5/L6 (R164_502): spectral invariants of A_T = window datum; heat trace; Stieltjes=Krylov; Widom identity','Props 1.1/1.3 (R164_601): exact tail sign condition for G²K; Thm 3.1 discarded-term principle']
O601='O164.601.1: lower bound of Σ_{q′}Re[G(t_{q′})²K(t_{q′})] for K Poisson/trig localized at γ_q (= (★_cell) weighted by K; R164_601)'
O503='O164.503a–d (R164_503): mean-square bound §3.3; Huxley exponent; non-rescaled θ<1/3 system; "returns to" clause §4.2'
upd15={
'5G':('A',C['5G'][1]+[O503],C['5G'][2]+'; part15: R164_503 Goal B ≥ RH + quadratic GRH (rejected as a route), rounding by primes capped at x^{1/2} ARGUED, Goal A OPEN'),
'7A':('A',C['7A'][1],C['7A'][2]+'; part15: R164_501 sinc on the zero side DEAD [E1, no room]; Thm SA, Cor SA.1 tools'),
'7F':('A',C['7F'][1]+[O601],C['7F'][2]+'; part15: Prop 4 tool (R164_501); O164.501.1 CLOSED (R164_601 Prop 2.1, dlVP on G²); route DEAD [W2/M + Thm 3.1]'),
'4A':('A',C['4A'][1],C['4A'][2]+'; part15: R164_502 moments/Selberg DEAD [W3, L1/L6]'),
'4E':('A',C['4E'][1],C['4E'][2]+'; part15: R164_502 det/heat trace DEAD [W12, E1]'),
'8D':('A',C['8D'][1],C['8D'][2]+'; part15: R164_502 Szegő–Widom DEAD [W4/W6]; L4, L5, L6 tools'),
'2A':('R',C['2A'][1],C['2A'][2]+'; part15: Props 1.1/1.3 of R164_601 tool'),
'4F':('A',C['4F'][1],C['4F'][2]+'; part15: audit R164_491 accepted (Thm R PROVED after F3/F1)'),
}
C.update(upd15)
# ---- part16 (phase 165: R165_101, 102, 201, 202; audit R165_190; phase closed) merge ----
for n in (16,):
    pn=P+f'R162_2300_part{n}.jsonl'
    if os.path.exists(pn) and not d.get(f'part{n}_merged'):
        for l in open(pn):
            if not l.strip(): continue
            x=json.loads(l)
            if x['id'] in ids: continue
            x['source_part']=n; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
        d[f'part{n}_merged']=True
d['part16_tools']=['Det+ (R165_101): T_c ≤ min_ρ τ(ρ), τ ≤ T_L(γ)+½log(π/2)+o(1) (clustering caveat); bracket 0.8047 < T_c','Thm 1 (R165_102): sub-Landau detection T_det for a dominant zero; Cor 2(c) contact = min_ρ T_det','Thm 2 / Cor 2.2 (R165_201): exact phase identity; sign variable ω(E)','R165_202: no jumps, real-rooted at every simple T, quadrature and Cauchy at every T, separation by charged zeros']
OWE='ω(E) at contact = Rem 4.8a (position of the node in its cell; R165_201 Cor 2.2)'
O102='O102.1 (explicit Gevrey γ₁(ψ), does H=3·10¹² suffice?); O102.2 (Det− with δ*Λ*≤y₀; needs O701.2 and Cor 2(c)); O701.1 (remove (Dom)), O701.2 (sub-Landau lower frame), O701.3 (middle regime) (R165_102)'
upd16={
'7A':('A',[OWE if x.startswith('D.16-γ') else x for x in C['7A'][1]],C['7A'][2]+'; part16: D.16-γ DONE negative (R165_201 Thm 3(a), R165_202); Det− DEAD (R165_102); Det+ tool (R165_101); "interlaced ⇒ quartet outside the cone" and "contact ⇒ EC" DEAD'),
'7D':('A',C['7D'][1]+[O102],C['7D'][2]+'; part16: Det+ (R165_101) and Thm 1 (R165_102) tools; bracket 0.8047 < T_c ≤ min_ρ τ(ρ) PROVED (clustering caveat)'),
'7E':('A',C['7E'][1]+['R165_202: node monotonicity and simplicity by parity OPEN'],C['7E'][2]+'; part16: R165_202 node flow PARTIAL/E1'),
'2A':('R',C['2A'][1],C['2A'][2]+'; part16: Prop 4/Cor 2 of R165_102 tool'),
}
C.update(upd16)
# ---- part17 (phase 166 rounds 6–7: R166_101, 102, 103, 201, 202; audit R166_190; phase closed) merge ----
for n in (17,):
    pn=P+f'R162_2300_part{n}.jsonl'
    if os.path.exists(pn) and not d.get(f'part{n}_merged'):
        for l in open(pn):
            if not l.strip(): continue
            x=json.loads(l)
            if x['id'] in ids: continue
            x['source_part']=n; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
        d[f'part{n}_merged']=True
d['part17_tools']=['Thm 2.1 (R166_101): |G(t)/(t−x₀)| ≤ e^{Tδ}‖G′‖_∞, no pole singularity at the nodes','B1–B2 (R166_103): tail split 𝒯_X = 𝒯^det + 𝒯^new, 𝒯^new = −ζ′_{≥X}/ζ_{≥X} (X-rough zeta)','Falsifier P_{a,c} (R166_103 G1)','Thm 1.3 / Cor 1.4 / Prop 2.2 (R166_201): jet hierarchy, Re G(t_q)² = jet k=−1','Thm 3 (R166_202): W_T(F^ev)+W_T(F^odd) = 4W_{T/2}(Φ)']
O202='O202.1: T_e = T_o for ζ (R166_202; no sign)'
upd17={
'6C':('R',[O202 if x.startswith('OS-2') else x for x in C['6C'][1]],C['6C'][2]+'; part17: OS-2 CLOSED negative (R166_202, vacuous/E1); R166_103 (α) DEAD [f_t/M_m]'),
'7A':('A',C['7A'][1],C['7A'][2]+'; part17: R166_101 DEAD [E1, Thm 2.1]; R166_201 DEAD [E1, jet hierarchy: Re G(t_q)² = jet k=−1]; ω(E) reformulated as global phase of G at t_q'),
'7E':('A',C['7E'][1],C['7E'][2]+'; part17: R166_102 flow in s DEAD [W2/M]; R166_201E Lyapunov of the sine DEAD [E1]'),
'7F':('A',C['7F'][1],C['7F'][2]+'; part17: R166_102F DEAD [W2/M]'),
'1F':('P',C['1F'][1],C['1F'][2]+'; part17: R166_102I DEAD [W2/M]'),
'4F':('A',C['4F'][1],C['4F'][2]+'; part17: R166_103 (β) DEAD [Thm A/Cor R.1/Landau]; split 𝒯^det + ζ_{≥X} tool (B1–B2)'),
'2F':('R',C['2F'][1],C['2F'][2]+'; part17: R166_103 (γ) DEAD [falsifier P_{a,c}]'),
'2A':('R',C['2A'][1],C['2A'][2]+'; part17: R166_201S atomic sampling DEAD [Cor 1.4, ψ-blind]'),
}
C.update(upd17)
# ---- part18 (phase 166 rounds 9–12: R166_501, 502, 601, 701, 702, 801, 802; phase 167: R167_101–103, audit 291; audits R166_190, R167_190) merge ----
for n in (18,):
    pn=P+f'R162_2300_part{n}.jsonl'
    if os.path.exists(pn) and not d.get(f'part{n}_merged'):
        for l in open(pn):
            if not l.strip(): continue
            x=json.loads(l)
            if x['id'] in ids: continue
            x['source_part']=n; cmap[f"{x['row']}{x['col']}"]['routes'].append(x); ids.add(x['id'])
        d[f'part{n}_merged']=True
d['part18_tools']=['Thm A (R166_501): (iii) alone ⇒ (ii); B(5) exact obstruction','Lemma PT (R166_702): Parseval for Besicovitch means','T3/T4 (R166_701): coboundaries; ℕ+q never θ=0','fourth-moment nodal identity (R166_801 (4.1))','Thm 0/3/4 (R166_802): general discarded term, localized Landau, sieves without zeros','Thm A, Lemma Q, Thm C, Prop W (R167_101)','Thm B/B′ (R167_102): blindness of sieves, b_θ','Theorem S / Cor S′ (R167_103): sieves in Beurling; DMV/Zhang falsifier']
C701='C1/C2 (R166_701): C1 every θ=0 system is ζ up to finite Euler modification (OPEN); C2 there exists θ=0 with a zero off (OPEN); T6: if C1, C2 ⟺ ¬RH'
O167='O167.101.1 (Dom_θ): other quartets near γ_q carry ≤ θ|Q_K|; O167.101.2: small-y regime, on-line count finer than S=O(log t) (R167_101)'
upd18={
'7C':('P',[x for x in C['7C'][1] if not x.startswith('nonlinear functional with pair correlation')],C['7C'][2]+'; part18: R166_801 second moment over translations DEAD [E1/f_t]; residual "pair correlation as exact input" (§6 item 46) DONE negative; tool fourth-moment nodal identity'),
'5G':('A',C['5G'][1]+[C701],C['5G'][2]+'; part18: R166_702 position/replacement DEAD [DMV barrier θ≥β, Lemma PT]; R166_701 θ=0 NO-GO as a route to D [(N)], tools T3/T4; R166_601 NO-GO'),
'7D':('A',C['7D'][1]+[O167],C['7D'][2]+'; part18: (Dom_θ) of R167_101 = (Dom) of R165_102'),
'3A':('A',C['3A'][1]+['O166.802.1: extension of the circularity to arbitrary nonlinear B (linked to O166.501.1)','(WS*) (R167_101): one-sided polylogarithmic bound at a single scale on Re Σ_{n≤Y}Λ(n)n^{−½+iγ_q}w(log n); unreachable by sieves (Thm B′), uniform ⟺ zero-free (Thm C), at one scale = explicit formula (Thm E)'],C['3A'][2]+'; part18: R166_802 inequality on Λ DEAD [circular]; R167_102 sieves DEAD [W-sieve]; R167_291 Lemma K downgraded; tools R166_802T, R167_101'),
'7B':('A',C['7B'][1]+['O166.501.1 (meta): is every non-confinement separating H whose proof does not use Z^off nonlinear in Λ beyond the window?'],C['7B'][2]+'; part18: Thm A of R166_501 (iii) ⇒ (ii); requirements (G)+(N′)'),
'4F':('A',C['4F'][1],C['4F'][2]+'; part18: R166_601 rough zeta + Legendre DEAD [E1, tautology]'),
'6C':('R',C['6C'][1],C['6C'][2]+'; part18: R166_502 P7+Q25 REPEATED [E70_11/12]'),
'3G':('P',C['3G'][1],C['3G'][2]+'; part18: Theorem S (R167_103) tool; DMV/Zhang falsifier of sieve proofs'),
}
C.update(upd18)
for c in d['cells']:
    k=f"{c['row']}{c['col']}"; code,res,com=C[k]
    c['status_2200_merge']=c.get('status_2200_merge',c.get('status'))
    c['status']=S[code]; c['live_residuals']=res; c['editor_note']=com
    c['counts']=dict(collections.Counter(r['status'] for r in c['routes']))
d['legend']={'PINTADA':'■ all routes dead, no live residual','MUERTA_CON_RESIDUO':'◩ dead but a precise residual survives','ABIERTA':'◧ live OPEN/PARTIAL route not superseded','VACIA':'□ no routes'}
d['version']='R162_2300 refined (part18)'
json.dump(d,open(P+'R162_2300_MASTER_grid.json','w'),ensure_ascii=False,indent=1)
# grid md
cols='ABCDEFGH'
rows={1:'identity/FE',2:'positivity/support',3:'estimation',4:'Euler',5:'integrality ℤ',6:'values of Λ',7:'zero side',8:'no arithmetic'}
cm={f"{c['row']}{c['col']}":c for c in d['cells']}
out=['| row \\ col | A | B | C | D | E | F | G | H |','|---|---|---|---|---|---|---|---|---|']
tot=collections.Counter()
for r in range(1,9):
    line=f'| {r} {rows[r]} |'
    for col in cols:
        k=f'{r}{col}';code=C[k][0];tot[code]+=1
        line+=f" {SYM[code]} {len(cm[k]['routes'])} |"
    out.append(line)
print('\n'.join(out)); print(tot)
open('grid.md','w').write('\n'.join(out))
# per cell sections
sec=[]
colsn={'A':'form of one window','B':'kernel vector (linear in F)','C':'quadratic/higher functionals','D':'spectrum','E':'flow/family in T','F':'global transforms in T','G':'L-families/fields','H':'geom./dynamical objects'}
for r in range(1,9):
  for col in cols:
    k=f'{r}{col}';c=cm[k];code,res,com=C[k]
    rs=c['routes'];ids={x['id'] for x in rs}
    kl=collections.Counter()
    for x in rs:
        if x['status']=='DEAD':
            for t in re.split(r'[;,]',x['killer']):
                t=t.strip()
                t=re.sub(r'^OTHER:.*','OTHER',t)
                if t: kl[t[:22]]+=1
    dead=[x['id'] for x in rs if x['status']=='DEAD' and not (x.get('supersedes_or_dup') in ids)]
    dups=[x['id'] for x in rs if x.get('supersedes_or_dup') in ids]
    tools=[x['id'] for x in rs if x['status']=='PROVED-TOOL']
    cnt=' · '.join(f'{a} {b}' for a,b in sorted(c['counts'].items()))
    s=f"**{k}** {SYM[code]} ({rows[r]} × {colsn[col]}) — {len(rs)} routes: {cnt}"
    if kl: s+="  \n  killers: "+', '.join(f'{a}×{b}' for a,b in kl.most_common(4))
    if dead:
        dd=dead if len(dead)<=10 else dead[:10]+[f'(+{len(dead)-10})']
        s+="  \n  dead: "+'; '.join(dd)
    if dups: s+="  \n  duplicates: "+'; '.join(dups)
    if tools: s+="  \n  tools: "+'; '.join(tools[:6])
    for x in res: s+="  \n  → live residual: "+x
    if com: s+="  \n  note: "+com
    sec.append(s)
open('cells.md','w').write('\n\n'.join(sec))
