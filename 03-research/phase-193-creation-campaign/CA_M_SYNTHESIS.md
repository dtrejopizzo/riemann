# CA_M_SYNTHESIS — Front M (the prime-sited problem), phase 193

 Pen and paper; no numerics. **No sign contact. No certified negative value for ζ. No clause of (R) moved.**
Memos: CA_M_000 (8 seeds, screens, corpus check), CA_M_001 (exact form, parity, integrality invisibility, reversal mechanism).

## Answers
1. **Exact prime-sited form (PROVED).** Q(s) = Arch(s) − Near(s); Near(s) = Σ_p s_p Σ_N (s∗v)(N)c₀(log(N/p)), N = p′q^a (Ω(N) ≥ 2, p′ < p)
   = Σ_{h∈ℤ}C_s(h): a sum over **all** shifts |h| ≲ 2T₀p of Chen-type correlations of primes with P₂-type numbers p′q^a. Not encoded:
   twin primes / prime pairs at fixed shift (N is never prime), Goldbach, k ≥ 3 tuples. Encoded: Hardy–Littlewood for the form pair
   (x, qx + h), first moment in h only.
2. **Exact structural facts about p − np′ (parity, residues, singular series, Chen switching, sieve, parity phenomenon) cannot force
   Near ≤ Arch: they are information-free (PROVED).** Parity/residue splits re-index the comb-prime decomposition (linear in Λ) and isolate
   trace-zero, indefinite pieces (CA_M_001 §1.2). Decisively, Thm 3.1/Cor 3.2: the ∀M prime-sited statement is equivalent to the same
   statement on real sites p + θ_p with ℚ-independent θ_p, where no difference x − nx′ is an integer; and Prop 3.3: in the decisive
   configurations the shifts h → ∞, bounded-shift configurations have zero weight. W-sieve and NG-A4 are not even reached.
3. **The anti-diamagnetic reversal (PROVED identity; FE-generic).** m(τ) + 2Re(ζ′/ζ)(½+iτ) = 0 off ordinates (FE + reality only); C₀ = −2ζ′/ζ(½).
   The comb's continued symbol is exactly minus the archimedean density: the primes do not add a surplus, they cancel the negative C₀
   exactly, with zero slack (centre criticality, corpus G2_B1_R1/L2_BUILD_010, now for every τ). Whatever carries positivity is not an
   a.c. density — the zero side, (R)(4), excluded. O10/O12 share the identity.

## PROVED facts (usable elsewhere)
M-S. Real-sited independence: any discrete X ⊂ (1,∞) with ratios → 1 is decisive; integrality is never used.
M-I. Information-freeness of site arithmetic (Cor 3.2) and unbounded shifts in the decisive class (Prop 3.3).
M-P. Near^{h odd} = Near_{q=2} exactly; every Near_q is trace-zero, indefinite.
M-R. Reversal = FE cancellation m + 2Re ζ′/ζ(½+i·) ≡ 0; Cesàro necessary condition on Ξ (Prop 4.3, ARGUED, Thm Z class, REF-D).

## YES→NO moves proposed
- "near-coincidences p ≈ np′ are a genuine +/· object whose integer structure (parity, residues, Chen, HL) carries the sign" → NO (PROVED: integrality invisible).
- "Beurling's lack of addition (p − np′ undefined) separates ζ from O11 at the site level" → NO (PROVED, same theorem).
- "anti-diamagnetism = primes contribute positive surplus" → NO: exact cancellation with zero slack (PROVED identity), FE-generic.

## +/· reading (PRINCIPIO RECTOR)
The prime-sited arena removes Div and appears to expose a +/· locus p − n·p′. It does not: the + there is cosmetic. Prime sites are
decisive only through p_{k+1}/p_k → 1, and every site set with that property is equivalent. The only +/· content of the target is the comb
positions log n with weights Λ(n)n^{−½} (the successor structure (S⁺), CA_H_002), already site-free. Area exhausted; front M stops.
