# R184_009 — Local 2025–2026 literature: inputs not used for row D

No web, no numerics. Sources: `00-references/arxiv-math-nt-2026-review/` (27 works, abstracts + .txt), `papers-nuevos/{A,B,C,D,Puente,extension-clase-test,mas-papers}`, `papers-ref-2/`, `arXiv-2511.11199v1/RH.tex`.
Walls and specification: R162_2300_MASTER_GRID §3 (W1–W12, W-identification, W-jet, W-sieve, (N′)), §4, §7 (S1–S12).
Does not duplicate R168_001, R160_S1/S5, R166_400–405, R169_000, R170_801–805, NO-GO-LIST §VII–VIII, phases 183–184.

## State

**No entry survives.** All 27 works in the 2026 review folder are already cited in the corpus (R170_804 §5, plus R170_801/802/803 and Paper 47 for Suzuki, Groskin, Zhu and Freedman). What this document adds is the wall proof, which R170_804 did not do. I left three entries as NEW: (a) zero-forcing by large values from Granville–Soundararajan, in the Dong–Wang–Wang–Zhang version, (b) the rank–trace inequality with Sylvester inertia on a finite compression of the Weil form (Alpöge–Furman), as mechanism rather than citation, and (c) the joint degree–derivative hyperbolicity window of Holland and the cubic Toeplitz-minor tail of Michalowski. All three fail S4 or S11. The closest ones are (a) and (b) (§3).

## 1. Inventory (CITED = statement taken from the work; "corpus" = file that already uses the entry)

### 1.1 `arxiv-math-nt-2026-review` folder (27)

| id | topic | main result (CITED) | entry in corpus? |
|---|---|---|---|
| 2606.09096 Suzuki v3 | Weil / screw function | Weil quadratic form via the screw function and nonlocal operators; conjectured spectral positivity | YES: R154_013, R157_002, R170_804 (31 files) |
| 2606.24924 Covei | Riccati–Γ, conditional criteria | bilateral vertical concavity of Ξ′/Ξ does not prove RH; conditional finite spectral average | YES: R170_804; E1 (conditional criterion) |
| 2606.29555 Freedman | Weyl-positive phase kernel, Volterra | finite-kernel reductions with boundary repair | YES: R170_803/804 (the repair transfers: J*KJ+(RJ)*D(RJ)≥0) |
| 2607.02828 Groskin | finite Guinand–Weil | finite dictionary and order of the archimedean tail | YES: Paper 47, R154_012 |
| 2607.04632 Turnage-Butterbaugh | zero density (Guth–Maynard) | exposition | YES: R170_804 |
| 2607.05560 Fragkos–Krause–Miheisi–Sun | Carleson along primes | maximal/variational operator | YES: R170_804 §4 (additive phase, ℓ^p) |
| 2607.15311 Croot–Mao–Pohoata–Yip | quadratic inverse large sieve | sharp inverse theorem | YES: R170_804; W-sieve |
| 2607.15574 Menon | multiplicative in short intervals | almost all intervals | YES: R170_804; W2 (average ⇏ uniform) |
| 2607.16795 Michalowski | Pólya frequency / Toeplitz | D_{r,k}>0 for k ≥ 10¹⁸r³, uniform in r | Pólya frequency YES (phase-11-hyperbolicity-total-positivity M11.2, R162/R164_501); the uniform cubic tail is treated in §2(c) |
| 2608.08682 Holland | Jensen | J^{d,n} hyperbolic if n³log²(n+2) ≥ Kd⁵; conjectured semicircle | Jensen YES (phase-11-hyperbolicity-total-positivity, R138, R164_501); the window is treated in §2(c) |
| 2608.13637 Alpöge–Furman | Weil / rank–trace / inertia | ≥ 2/3 of zeros simple and on the line; rank–trace on a finite compression of the Hermitian Weil form + Sylvester | citation YES (P122_003, R170_804); the mechanism is treated in §2(b) |
| 2608.14777 Maynard–Pandey–Radziwiłł | primes, additive phase | Σ Λ(n)e(nα) ≪ N^{o(1)}(N/B^{1/2}+N^{19/24}) | YES: R170_804; W-sieve / b_θ (upper bound that b_θ also satisfies) |
| 2608.14852 Tang | twisted second moment | reciprocity | YES: R170_804; W2 |
| 2608.24827 Zhu v2 | Weil positivity on compact windows | finite reduction, certified bounds, Landau–Widom decay | YES: Paper 47, R160_001 (45 files) |
| 2608.26814 Tardy | two-point correlations | logarithmic density | YES: R170_804 |
| 2608.31060 Dong–Wang–Wang–Zhang | large values ⇒ zeros | \|S(x,t)\|=x/N ⇒ ≥ L/360 zeros in a disk at 1+iφ, \|φ−t\|≪N | citation YES (R170_804, one line); the forcing mechanism (Granville–Soundararajan) does not appear in the corpus → §2(a) |
| 2609.00537 Dhiman–Kadiri–Quesada-Herrera | explicit exponential sums | constants of the approximate functional equation | YES: R170_804; W2/M (margin) |
| 2609.11070 Robles | sums with multiplicative coefficients | effective estimates | YES: R170_804 |
| 2609.17875 Dubon | zero density, Dirichlet polynomials | anticoncentration under Haar | YES: R170_802 (Eν Re S ≤ √(VH)) |
| 2609.20367 Desogus | "Three Gates", Weil | claims RH by Schur induction | YES: R170_801/805 (not validated) |
| 2609.22624 Fiori | short zero density | explicit density near the boundary | YES: R170_804 |
| 2609.25879 / 25885 Ramaré | large sieve via Parseval | regularity near saturation | YES: R170_804; W-sieve |
| 2609.33278 Liu | prime detection | Dirichlet inversion identities | YES: R170_804; W12 (identity with no sign) |
| 2609.33692 Freiberg | biases in short intervals | conditional on Hardy–Littlewood | YES: R170_804 |
| 2609.33953 Irfan | Λ^{*k}, U(N), random matrices | δ_k(c) as a matrix integral (function-field analogue) | YES: R170_804; falsifier F_q / W8 |
| 2610.01035 de Faveri–Pandey | sixth moment | moment + large values | YES: R170_804; W2, R164_502 (moments DEAD) |

### 1.2 `papers-nuevos`, `papers-ref-2`, RH.tex

| id | topic | result (CITED) | in corpus? |
|---|---|---|---|
| A: 1502.05580, 1507.05818, 1709.05831, 1805.10501, 2205.01391, 2602.15941, 2606.06604, 1405.4527, 1509.05576, 2207.10419, 2401.08401 | arithmetic/scaling site, RR for Spec ℤ̄, ζ-cycles, knots | Connes–Consani | YES (2–136 files each; phase 183) |
| B: 1807.06400, 2508.05329 | rational Witt vectors | — | YES |
| B: math0204110, math0505354, 2301.11643 | Deninger | (locally empty folders) | Deninger YES: R158_001 §4; W10 |
| B: 2504.15767 | "BSD for ζ_K" | residue/value formula at s=0 | NO by id; special value, no sign content about zeros → W-identification/T1, not a candidate |
| C: 1307.3851, math0412277, 1712.04181, 1912.02159, 1905.12912, 2410.20758 | foliations, dynamical zetas (Leichtnam, Kim) | foliated cohomological expression | YES: R158_001/002; W10 (the object postulates positivity) |
| D: 1810.06342, 2512.01811, 1304.3538/9 | arithmetic Hodge index (Yuan–Zhang), numerical cohomology | — | YES (phase 135, R158) |
| D: 2403.09266 | quadratic Riemann–Roch | — | NO; W10 (MW-5 absent) |
| D: 2510.08033 | Riemann–Hurwitz on arithmetic surfaces | ramification formula in Arakelov geometry | NO; surface geometry over Spec ℤ, gives no sign for the Weil term → W10 / Thm 19.25 |
| extensión-clase: math-0404394 Lagarias | Li for GL(N) | λ_n(π) ⟺ RH for L(s,π) | YES (148 files); E1 |
| math-9810169, math-9902080 Burnol | conductor operator | H = log\|x\|+log\|y\| | YES: phase-47/145, E101_090; 1D residue O2702.1 |
| 2006.13771, 1910.14368, 2310.18423, 2511.22755 | CCM prolate / Sonin | — | YES; phase 183 NO-GO beyond log 2 |
| mas-papers (tropical: 1308.3813, 1506.02023, 1511.00650, 1711.07900, 2007.07826, math0612267; 2209.08536, 2105.12216, 1703.02325) | tropical complexes, tropical Hodge | — | Cartwright YES (PHASE_136 S5, 2H residue); W10 |
| Puente 2508.15971 | — | — | YES (11) |
| ref-2: 2106.01715, 2112.05500, 2310.18423 | spectral triples, prolate | CCM | YES |
| ref-2: 2402.13082 Connes | heat expansion | full expansion of Tr e^{−tD²} under RH | NO by id; heat trace YES in R164_502 (DEAD: window datum, Szegő–Widom); moreover it assumes RH → E1 |
| 2511.11199 (RH.tex) | DQPT | zeros ↔ quantum phase transitions, numerical verification | YES: R160_S5, phase-70, R157_002 row 32 (Hilbert–Pólya-type reformulation) |

Requested topics with no new work in the local folder: Nyman–Beurling, de Branges/Kreĭn, Bombieri–Garrett, Moscovici (only via CCM, already in the corpus), Selberg class, generalized Beurling (only `beurling-dmv/`, already CITED in R157/R163).

## 2. Wall proof for the three NEW entries

### (a) Zero-forcing by large values (Dong–Wang–Wang–Zhang 2608.31060, Granville–Soundararajan mechanism)
Entry: if \|Σ_{n≤x} n^{it}\| ≥ x/N, then there are ≥ L/360 zeros of ζ in a disk of radius ≍ L/log x around 1+iφ.
- S1 yes (no jet). S2 yes (nonlinear threshold). S3 yes. S4: **partial.** It uses actual ℤ (the sum runs over all n ≤ x), so it separates Λχ₂ and in principle DMV. But it only localizes zeros as σ → 1. **M_m** has the same zeros as ζ in the region σ ≥ 1 − o(1), and its quartets lie in the interior of the strip, so the conclusion does not see them. Fails S4 against M_m.
- Wall: **(N′)**. To exclude the witness one must control Λ at frequency γ_q with exponent Θ − ½. This forcing only works with exponent 1 − O(1/log x), at Vinogradov–Korobov scale. Moreover, the direction is "large value ⇒ zero," the same one that gives the zero itself, and so it confirms the witness rather than excluding it (R166_802). Also **W2/M**: the threshold x/N with N ≤ (log x)^{1/100} is doubly-exponentially far from the margin λ^A_T ≤ exp(−e^{(2−ε)T}).
- S11: it is not ⟺ RH (it is weaker), nor does it couple with the archimedean place at height ½.
- Verdict: **NO-GO (N′ + M_m)**.

### (b) Rank–trace + Sylvester inertia on a finite compression of the Weil form (Alpöge–Furman 2608.13637)
Entry: a rank–trace inequality on a finite compression of W replaces the positive reading of the zero side; Sylvester bounds the contribution of the off-line pairs. Result: ≥ 2/3 of the zeros are simple and on the line.
- S1 yes. S2 no: it is quadratic in the test. S3 yes. S4: **no**. Inertia is blind to the class (phase 183, R184_004 CB inertia). The negative index of the compression counts quartets the same way in M_m and in ζ, with κ(M_m) = κ(ζ) + 4m: Sylvester sees the difference only if it knows the index of ζ beforehand, and that is RH. DH: abundance separator removed in grid parts 12–13 (Bombieri–Hejhal: there is 100% conditionally and still infinitely many off-line zeros).
- S11: it pushes the proportion to 1 only with full rank of the compression ∀ size → **E1** (∀T of a per-window law).
- Wall: **W3 (inertia blind to class) + E1**. Non-separating falsifier: **M_m** (and DH for the proportion form).
- Verdict: **NO-GO**. It is the closest candidate structurally because it is the only one that genuinely works on the Weil form itself.

### (c) Hyperbolicity / PF windows (Holland 2608.08682, Michalowski 2607.16795)
Entry: an explicit region of (d,n) (or of (r,k)) where the RH-type property holds unconditionally.
- S5 no: "∀(d,n)" is E1 (Pólya frequency ⟺ RH). The finite complement of each row collides with **W2 (quantifier)** and finZ/M. The low n are exactly the ones that see M_m's quartets, and a tail bound does not reach them.
- S4 no: the tails hold for any function in the asymptotic Laguerre–Pólya class, including Ξ_a and M_m (off-line zeros at bounded height do not alter the asymptotics of γ(n)).
- Verdict: **NO-GO (E1 + W2; falsifier M_m/Ξ_a)**.

## 3. Survivors

**None.** The two closest:
1. **(b) Rank–trace + Sylvester** (Alpöge–Furman). It is the only one that acts on the Weil form itself and does not use RH to read the zero side. It collides with **W3 (inertia blind to class, R184_004) + E1**, and does not separate **M_m**.
2. **(a) Zero-forcing by large values** (Dong–Wang–Wang–Zhang). It is the only one that uses the integrality of ℕ in a "value ⇒ zero" direction. It collides with **(N′)**: it works at σ→1 and not with exponent Θ−½ at γ_q. It also does not separate **M_m**, and its margin is incompatible with Theorem M.

What would be needed to revive (a), and is not in the local literature: a version of the forcing in the interior of the strip, whose hypothesis is a one-sided inequality on Re Σ Λ(n) n^{−1/2−iγ_q} and which first contact would produce. That is (N′) and hence (★_cell). It is not proposed.

## For the audit

- The claim that "all 27 are in the corpus" relies on grepping by id: each id appears at least in R170_804. That does not prove that every mechanism was actually read. R170_804's review was mostly of statements, and it says so itself.
- The classification of (a) as NEW is based on "Granville," "pretentious" and "zero-forcing" not appearing in connection with this work. There are mentions of Halász/Granville in R164_201/503 (Beurling) that I did not review in depth. If the forcing was already used there, (a) moves to REPEATED and the verdict does not change.
- In (b), the argument "inertia blind to class" is taken from R184_004 and from phase 183. Not re-auditable here: the sentence "κ(M_m)=κ(ζ)+4m ⇒ Sylvester does not separate without knowing κ(ζ)" — verify that the Alpöge–Furman compression does not use an arithmetic datum (Aryan; Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh) that M_m does not share. If that datum is the second moment of pairs, it falls into 7C (R166_801, DEAD [E1/f_t]).
- Folders B/math0204110, math0505354, 2301.11643, C/1905.12912, 2410.20758 and mas-papers/2105.12216 are **empty** in the local copy. They were not read; their status was taken from the corpus (R158_001).
- 2402.13082 (Connes, heat expansion) assumes RH in its statement. I classify it as E1 + R164_502 without having read the section on the prolate.
- No numerics were done and no web was consulted.

## Note (R184_093)

* Dong–Wang–Wang–Zhang: the real radius is L·log T/(log x)², not ≍ L/log x; the NO-GO holds (count without abscissa, does not separate M_m). Alpöge–Furman: NO-GO because it is a density result.
