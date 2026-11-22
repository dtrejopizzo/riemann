# CA_H — Self-review of front H (memos 000, 001, 002)
Checked against P46 def:shape-ops, lem:shape-quartet, prop:shape-inputs, prop:AM, thm:oneprofile, rem:boxes, thm:ceiling; CA_E_001; SPEC_B; EI_002.
To be re-checked against CAMPAIGN_LEDGER.

| claim | check | label |
|---|---|---|
| H0 (+/· test) | (a) = G1; (b) Epstein FE is ℤ²-Poisson (Hecke) ✓; (c) = lem:shape-quartet ✓ | PROVED (definitional) |
| 001 Prop 1.1 | ring endomorphism of ℤ is id; p-torsion free ✓ | PROVED |
| 001 Lem 1.2(i) | p^{e−1}u − p^{ep−1}u^p, ep−1 > e−1 ✓ | PROVED |
| 001 Prop 2.2(iii) | W_p(a,c) − W_p(a,b) = a(a^p+b^p−c^p)/p re-derived from (i) ✓ | PROVED |
| 001 Prop 2.2(iv) | x^n − (x−1)^n ≥ x^{n−1} ⇔ (x−1)^{n−1} ≤ x^{n−1} ✓; p = 2 gives |a−b| ≥ 1 ✓ | PROVED |
| 001 Cor 2.3 | product case only; general case ARGUED ✓ labelled | PROVED / ARGUED |
| 001 Prop 3.2 | ℤ/p-necklace count of ordered factorizations ✓ | PROVED |
| 001 Prop 3.3 | Λ(q^j)/log q^j = 1/j; φ_p reindexing j′ = pj ✓; Σ_{N p-th power}Λ(N)N^{−s} = −ζ′/ζ(ps) ✓ | PROVED |
| 001 Prop 3.5 | v_{n^p} = 2Λ(n)n^{−p/2} ✓; bound by 2|ζ′/ζ(p/2)|‖F‖², p ≥ 3 ✓ | PROVED |
| 001 Prop 5.1 | degree argument ✓; non-vanishing CITED (Deligne–Illusie) | PROVED + CITED |
| 001 Prop 5.3 | Γ_n = n f₁ + f₂ from Γ·f₁ = 1, Γ·f₂ = n ✓; Γ·Δ = n+1 ✓; decomposition ((n+1)/2)H + ((n−1)/2)(f₁−f₂) ✓ | PROVED |
| 002 Thm 2.2 | Erdős CITED; O12 inert prime witness ✓; O10 r_Q(2) = r_Q(3) = 0, r_Q(6) = 4 ✓ | PROVED from CITED |
| 002 Prop 2.4 | N/(nM) < e^{2T₀}/2 for n ≥ 2, N < Me^{2T₀} ✓; E_s(N) = 0 beyond ✓ | PROVED (a = Λ case = SPEC_B §1.3, retry; new: arbitrary prime-power comb) |
| 002 Thm 3.1 | Haar picks m = kn ✓; ν̂₀(q) = c₀(log q) ✓; ‖F₀‖ = 1 ⇒ ν₀ probability ✓ | PROVED |
| 002 Thm 3.2 | expansion of Arch ✓ | PROVED |
| 002 Prop 3.4 | |ĝ| ≍ |τ|^{−1} uniformly (numerator bounded above and below for b ≠ 0) ✓ | PROVED; reading ARGUED |
| 002 Cor 3.5 | E Thm 1 + Thm 3.1 + rem:boxes ✓ | REF-D |

**Objections raised and answered.**
1. *Front H re-derives phases 188–192.* Partly: Prop 2.4 (a = Λ) is SPEC_B's collapse and §3.1's shifted-convolution form is L2_030; both are
   flagged as retries in the memo. New items: the δ-structure results (001 §§1–5), the separating invariant (S⁺) with its full falsifier
   table, the Haar/line identification and the anatomy theorem, the M^{−3} tail reading, and the 𝒦_δ NO-GO for the G-F bridge.
2. *Is any statement a sign step?* No. Every object is (B″), comb-only (O7), linear in Λ, REF-D, or a NO-GO.
3. *Zero information, equivalences, numerics.* None used; EXP_005 numbers quoted as NUMÉRICO only.
4. *Depth.* Two survivors developed with definitions, statements and proofs (001: 11 numbered results; 002: 9). The area seeds H2, H3, H4,
   H7, H9, H10 were screened with the full table and the reason for each discard is stated.
**Verdict:** labels CONFIRMED at memo level. No certified negative value for ζ.

**FIXes of CA_H_000_REVIEW applied:** H0(b) relabelled ARGUED; CA_H_002 §3 now cites CA_C_002 Prop 2(d) as the box version and states what is added; H1 relabelled 'developed to record the death'.
