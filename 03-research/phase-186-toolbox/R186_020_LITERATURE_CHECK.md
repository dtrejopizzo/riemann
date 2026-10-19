# R186.020 — Literature check (arXiv) for the semilocal chain S={∞,2}

Searches: au:Connes, au:Consani, au:Moscovici (complete lists, chronological
order), all:"Sonin" AND zeta, all:"Weil positivity" (2024–), all:prolate
AND "Riemann zeta", all:semilocal AND "trace formula". Texts checked:
2008.10974 (pdftotext), 2403.01247 (pdftotext), abstracts of 2511.22755,
2602.04022, 2608.24827 (Zhu), 2609.20367 (Desogus).

## 1. Overlaps that require citation (not ours)

| our result | prior source | relation |
|---|---|---|
| Thm C (R186_008): F_S = F_∞·e^{iφ(D)}, φ′ = −Σ v_{2^k}cos(kt log 2); M = m_∞U | **CC 2008.10974**, u = ρ_∞∏ρ_p, ρ_p(z)=γ_p(z)/γ_p(1−z); Lemma 3.1 (ρ_p periodic, period 2πi/log p) | **identical**: our U is ρ_2 in Mellin coordinates; cite as "CC's quasi-inner function" |
| F_S = I·M(D) and the Hankel block (1−P)M(D)P (R186_010) | CC 2008.10974 Def. (quasi-inner = (1−P)uP compact), Thm 2.1, Thm 2.3 (explicit rank-one series for (1−P)ρ_∞P, characteristic values with prolate decay), Lemma 3.5 / Prop 3.7 (explicit (1−P)κ_pP, kernel/cokernel via Blaschke), Thm 4.4 (ρ_∞ρ_p quasi-inner) | CC prove **compactness**; our R186_007/093 proves **not Hilbert–Schmidt**: stronger, compatible, new |
| Semilocal Sonin = ran(1−P)∩ran(1−P̂^S) (R186_009) | CC 2008.10974 main theorem: Sonin = ker u₂₂; semilocal filtering system; D(F,F′)=∏(1−p^{−z}) maps S(u(F))→S(u(F′)) (= CCM's θ_S) | **identical** as a definition; cite |
| Moment generating function 𝓜(u) and Hankel/Jacobi for S={∞,2} (R186_002 §2.4) | **CCM 2403.01247** Prop 3.2 (generating function), Prop 4.1 (Lambert), Thm 5.6/6.5 (integrality in ℤ[1/√2]) | **rederived**; cite; their result is more complete |

## 2. What does not appear in the checked literature (ours)

1. **A_S = PF_SP is not Hilbert–Schmidt; A_S ∈ S_p ∀p>2** (R186_007/011/093). CC only have compactness.
2. **Exact NO-GO** results for the candidates −𝔰²+λ²N_S and metaplectic as operators commuting with P^S_λ (R186_003/006). CCM 2310.18423 propose them; 2403.01247 does not address commutation.
3. **Operator gap** cos²θ_n = λ_n², 1 isolated, rate λ₁^{2n} (R186_009/095).
4. **L2_S**: logarithmic structure of the Halmos series density, β_j = 2^{j/2}(1−2^{−j})λ²/(2 log 2) (R186_012/097).
5. **(84)_S / Δ**: semilocal trace identity Tr ϑ(f)Π_S = W_∞(f) − comb₂(f) + ∫f(ρ⁻¹)d_S d*ρ, with ϑ(f)Π_S ∈ S₁ and T3 (R186_014/098). CC 2006.13771 prove (83)–(84) only at the archimedean place; 2602.04022 (2026 survey) confirms this in its own words ("in the simple case when no primes are involved", l.1196).
6. **Thm C′** (exact linear trace) is, as R186_094 noted, dual to R183_015 + the classical phase formula; it is not from CC, but it is also not new in substance.

## 3. Other 2025–2026 works reviewed

* CCM 2511.22755 (Zeta Spectral Triples): rank-one perturbations, convergence to the zeros only numerical; "a rigorous proof would establish RH". No semilocal positivity.
* Connes 2602.04022 (survey): extremization of a restriction of the Weil form with primes < 13; no new positivity result.
* Zhu 2608.24827: certified positivity up to 0.8 (numerical), Landau–Widom decay law. No semilocal construction.
* Desogus 2609.20367: finite windows, gate/Schur method. No Sonin, no semilocal.
* CC 2609.00299, 2606.06604, 2602.15941 (absolute geometry): no relation.

## 4. Actions

* Add citations to 2008.10974 and 2403.01247 in R186_002, 007, 008, 009, 010 and in the Paper 47 draft (the phase 186 files do not cite 2008.10974: a bibliographic gap).
* Relabel Thm C as "CITED (CC 2008.10974, ρ_p) + verification"; keep items §2.1–2.5 as new.

Status: check done against public arXiv; no access to journals.
