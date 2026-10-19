# S5 — Cross-field hunt: has someone already built the missing object?

Brief: `BRIEF.md` (row D, λ_A(T) ≥ 0 on P_T; four properties P1 exact comb values, P2 small primes coupled to the global FE
not via ζ(½+iτ) nor place by place, P3 not linear / not cone / not dual certificate / not identity, P4 built-in positivity
not assuming the target). The index (`05-meta-and-planning/ROUTES-TRIED-INDEX/`) was grepped for every family before verdicts.

**Coverage, stated honestly:** 22 web queries and 6 abstract fetches, about 90 distinct items seen in result lists, 12 read at
abstract level or more. This is **below the brief's ≥200 target**. The domains where the index already has an entry were
checked against it rather than re-swept.

## (a) Scanned items (compact)

| # | Item | Field | Status | In index? | Verdict |
|---|---|---|---|---|---|
| 1 | Ihara/Hashimoto/Bass zeta; Ramanujan ⟺ graph RH (Ihara 1966, Sunada, Kotani–Sunada 2000, Terras) | graphs | PROVED (definitional) | no (grep "Ihara" empty) | IRRELEVANT as object (see b1) |
| 2 | LPS 1988; Margulis; MSS Interlacing I–IV (Ann. Math. 2015; 2018); arXiv 2412.20721 survey | graphs | PROVED | no | KNOWN-type / IRRELEVANT (b2) |
| 3 | arXiv 2406.17505 discrete trace formulas, adjacency calculus | graphs | PROVED | no | IRRELEVANT |
| 4 | Selberg trace formula, Hejhal | automorphic | PROVED | L31 | KNOWN |
| 5 | LP bounds for hyperbolic surfaces arXiv 2302.02540; LP in homogeneous spaces arXiv 2505.23572 | spectral geometry | PROVED | no | KNOWN mechanism (dual certificate, thm:Z) |
| 6 | Connes–Consani "Weil positivity and trace formula, archimedean place" arXiv 2006.13771 | NCG | PROVED (archimedean) | yes (semilocal) | KNOWN |
| 7 | Connes–Consani–Moscovici "Zeta spectral triples" arXiv 2511.22755; prolate arXiv 2310.18423 | NCG | PROVED / partial | prolate yes | KNOWN |
| 8 | Bost–Connes KMS; Yalkinoglu arXiv 2507.23759 (BC and periodic Witt vectors); CM KMS math/0501424 | QSM | PROVED | L29 | KNOWN |
| 9 | Knauf number-theoretic spin chain, Z(β)=ζ(β−1)/ζ(β) (CMP 1993, 1998); Contucci–Knauf (positivity of the interaction function); Guerra–Knauf (correlations); Fiala–Kleban–Özlük Farey chain cond-mat/9808182; Kleban et al. math-ph/0503030 | stat-mech | PROVED (positive interactions, phase transition at β=2) | **no** (grep "Knauf" empty) | weak NEW-CANDIDATE (b3) |
| 10 | Julia primon/Riemann gas; bosonic/fermionic, ζ(s)/ζ(2s); arXiv 1101.3116, 1401.8190, 2502.02661 | stat-mech | heuristic | no | IRRELEVANT (partition function = ζ, linear in log ζ) |
| 11 | Lee–Yang, GKS/FKG, Newman | stat-mech | PROVED | L32, frente J | KNOWN (dead: frustration) |
| 12 | 2D Ising ↔ ζ zeros "equivalence" arXiv 2411.16777 | physics | CLAIMED | no | IRRELEVANT (claim, not read in depth) |
| 13 | Lee–Yang for Blume–Capel arXiv 2607.16958; antiferromagnetic Lee–Yang 2309.14562, 1907.07479 | stat-mech | PROVED | no | IRRELEVANT (no arithmetic) |
| 14 | Deligne Weil I/II; Drinfeld/L. Lafforgue/V. Lafforgue Ramanujan–Petersson | arithmetic geometry | PROVED | L25 (Deligne); Lafforgue no | KNOWN (positivity = weights/Hodge index; function-field wall phase 149) |
| 15 | Delsarte LP; Cohn–Elkies; Viazovska; CKMRV; dual LP dim 36 arXiv 2607.11319; 2206.09876; 2501.04854; binary codes 2609.03736 | packing/coding | PROVED | L54, thm:O, README | KNOWN (dual certificate) |
| 16 | Arithmetic QUE: Lindenstrauss, Soundararajan, Holowinsky–Sound. | quantum chaos | PROVED | SURVEY_MODERN row | KNOWN |
| 17 | Nevanlinna–Pick / Schur with arithmetic data | function theory | — | Schur covered widely | KNOWN |
| 18 | Bochner / positive definite distributions on LCA groups (1712.07264, 2009.02802, 1507.02547 Jorgensen–Pedersen–Tian) | harmonic analysis | PROVED | Bochner, L20 Kreĭn | KNOWN |
| 19 | Saksman–Webb, ζ and Gaussian multiplicative chaos (Ann. Probab. 2020, arXiv 1609.00027); critical chaos for |ζ|² | probability | PROVED (statistical) | grep "Saksman" empty | IRRELEVANT (b4) |
| 20 | Biane–Pitman–Yor (BAMS 2001, math/9912170); Lévy–Khintchine for ξ-type laws; arXiv 2306.08317 (inf. divisible ⟺ RH); Nakamura arXiv 1504.03438; Letac et al. Wald couples (AIF 2005) | probability | PROVED / reformulation | grep "Biane" empty | KNOWN-type (REF-D) (b5) |
| 21 | Morán Ledezma arXiv 2311.08519 (Weil sums as covariances on the Bohr compactification) | probability | PROVED (identity) | yes (R184_009) | KNOWN |
| 22 | Helson; Hedenmalm–Lindqvist–Seip H²(Dirichlet); Pushnitski "Three families of matrices" arXiv 2401.14802; Helson zeta arXiv 2408.15713; Helson forms arXiv 2608.22882 | Dirichlet series | PROVED | Helson in audit | IRRELEVANT / KNOWN (b6) |
| 23 | Ruelle/Selberg zeta of hyperbolic flows, RH-type for Ruelle L-functions of cuspidal systems (arXiv 0804.2715 context), Dyatlov–Zworski 1606.04560 | dynamics | PROVED (via Selberg) | grep "Ruelle" empty | IRRELEVANT (positivity inherited from self-adjoint Laplacian) |
| 24 | Smale / Artin–Mazur dynamical zeta | dynamics | — | no | IRRELEVANT |
| 25 | Lapidus–Maier (JLMS 1995), Lapidus–van Frankenhuijsen; Herichi–Lapidus spectral operator arXiv 1210.0882; fractal cohomology 1705.06222 | fractal geometry | PROVED (reformulation) | only as Hilberdink–Lapidus (Beurling, phase 150) | KNOWN-type (REF-D, zero-free strips) |
| 26 | Nyman–Báez-Duarte; Bellemare–Langlois–Ransford "A positivity conjecture related to ζ" (Amer. Math. Monthly 2019, arXiv 2011.02847) | approximation | CONJECTURE (numeric, 10⁹ entries) | NB family L18/L61; BLR itself not found | KNOWN family; side note (b7) |
| 27 | Kreĭn strings / de Branges canonical systems; arXiv 2408.15135, 2406.01828, 2606.13932, 2608.28801, 2503.09644 | spectral theory | partial / heuristic | L16, L20, L44 | KNOWN |
| 28 | Zhu arXiv 2608.24827 (compact windows) | NT | PROVED-numeric | yes | KNOWN |
| 29 | Chirre–Gonçalves–de Laat positivity technique arXiv 2503.15832 | NT | PROVED | L53 | KNOWN |
| 30 | Suzuki arXiv 2206.03682 | NT | PROVED | yes | KNOWN |

About 60 further result-list titles in the same queries (Ising numerics, hyperbolic-function laws, Farey trees CMP 2007,
graph-zeta coefficients, physics primon variants) were IRRELEVANT on title or abstract and are not listed one by one.

## (b) Deep-read notes

**b1. Ihara / graph RH.** The positivity is the spectral bound |λ| ≤ 2√(q) of a *finite self-adjoint* adjacency operator. The
"primes" (closed primitive cycles) are *produced by* the operator. There is no analogue of an independent comb that has to be
read. The data run operator → primes, which is the opposite of what we need (P1 fails in the sense that it is no theorem *about*
a given comb, and P2 holds only trivially). The Kotani–Sunada / Bass identities are exact identities, so P3 fails. Verdict: not a
piece of the object. It is a further instance of the closed "find the operator" family (Hilbert–Pólya, frente D).

**b2. MSS interlacing.** Positivity comes from real-rootedness that is preserved under averaging (real-stable polynomials). It
gives *existence* of a good member of a family, not positivity for one fixed object. Applied to row D, it would show that
*some* comb in a family is positive. This is comb-generic and fails P1. Verdict: IRRELEVANT. The index has no "interlacing" entry;
we recommend adding one line.

**b3. Knauf's number-theoretic spin chain (no index hit).** The Hamiltonian on chains of length k is built from products of the
matrices A = (1 0;1 1) and B = (1 1;0 1). The partition function summed over k is ζ(β−1)/ζ(β), and the energies are log n with
restricted-divisor multiplicities. **Proved:** the interaction coefficients in the spin (Fourier–Walsh) expansion are all
≥ 0 (Contucci–Knauf), so the chain is ferromagnetic and GKS correlation inequalities hold. The phase transition at β = 2 is
also proved.
- P1: yes. The multiplicities are exactly the integer structure of ℕ (SL₂(ℕ) words), which is semiring-shaped, compatible with
  the author's semiring principle (ℕ,+,·). A Beurling system has no such matrix model.
- P2: **no**. The functional equation of ζ plays no role in the chain. The positivity lives at real β > 2, inside the region of
  absolute convergence.
- P3: yes. GKS positivity is non-linear in the Boltzmann weights.
- P4: yes, proved.
- Gap: the target needs a statement on a window of the *critical* line paired with c_F. Knauf himself notes that extending
  the chain approximation into the strip is open. Any use would require an analytic continuation that keeps the ferromagnetic
  sign. We know of no mechanism that does this. Frente J died on frustration, but there the spins were prime blocks with a
  ±1 gauge. Knauf's spins are *Farey/continued-fraction letters*, which is a different object. That difference is the only
  written reason this is not a repeat of frente J.

**b4. Multiplicative chaos (Saksman–Webb).** These are distributional limits of |ζ(½+i(t+τ))|^γ under random shifts. They are
statistical and use the factor ζ(½+iτ) directly, so P2 fails and P4 does not apply. IRRELEVANT.

**b5. Biane–Pitman–Yor and infinitely divisible laws.** ξ-related functions are Laplace transforms of positive laws, and
infinite divisibility is a cone condition on log ξ. arXiv 2306.08317 is an exact reformulation. P3 fails because it is a cone
condition on log ζ. This is REF-D. KNOWN-type. The positivity of the BPY theta-laws in the half-plane holds unconditionally but is
comb-generic: it comes from the Jacobi theta modularity alone, so it reads the FE and not the comb.

**b6. Helson / H² of Dirichlet series.** The positivity results (Helson's inequality, bounded multiplicative Hankel forms)
concern the *multiplicative* Toeplitz structure on the infinite torus (Bohr lift). They read exact multiplicativity, so P1
holds in part. They carry no archimedean FE coupling, so P2 fails. This is the closest "semiring" positivity in the list. It
already appears in the PHASE193 audit and adds nothing new.

**b7. Bellemare–Langlois–Ransford.** They observe numerically that more than 10⁹ entries of an infinite triangular matrix
attached to the Nyman–Báez-Duarte Gram–Schmidt are positive. This is entrywise positivity (P3 fails: coefficientwise). It is
unproved, and it sits inside the NB family (L18/L61). Record it in the index as a literature item. It is not a route.

## (c) Ranked "possible missing object"

None of the items has all four properties. Ranked by how many properties each has, honestly:

1. **Knauf spin chain (P1, P3, P4; no P2)**: weak NEW-CANDIDATE. First theorem to attempt: express the window form
   𝔞_T restricted to an explicit finite family of F (for example F = Farey-interval indicators of length ≤ 2T) as a
   GKS-type correlation of the chain at complex β with Re β = ½+1 = 3/2 shift, and prove or falsify that the Contucci–Knauf
   interaction positivity persists for |Im β| ≤ π/T. The expected outcome is a falsifier, because the sign has to break before
   the strip. A clean falsifier would still be a new index entry.
2. **Helson / multiplicative Hankel positivity (P1 partial, P3, P4; no P2)**: KNOWN. A possible test is a single-window
   Hankel restriction combined with the Γ_ℝ term. It is likely comb-generic after the archimedean term is added.
3. **Selberg/hyperbolic-surface LP and pretrace positivity** (P4 only, through Σ|φ_j(z)|² ≥ 0): KNOWN (L31, semilocal Connes–Consani).
4. **MSS interlacing** (P3, P4; no P1): family-existence only. Add to the index as NO-GO-by-type.
5. **BPY / infinitely divisible laws** (P4 on the FE side only): REF-D.

Not pieces of the object: Ihara/Ramanujan graphs, Ruelle/Smale, primon gas, multiplicative chaos, Lapidus–Maier
(reformulation), Bost–Connes KMS (L29), Delsarte/Cohn–Elkies follow-ups 2025–26 (dual certificates, thm:Z/thm:O).

**Index additions suggested** (not yet entered in the index): Knauf chain (pending test), MSS
interlacing (NO-GO by type: existence in families), Ihara/graph RH (operator → primes, opposite direction), Saksman–Webb, BPY/2306.08317
(REF-D), Lapidus–Maier (REF-D), Bellemare–Langlois–Ransford (NB family, entrywise).

---

# Addendum A: extended sweep and the Knauf literature test

## A.1 Sweep, stated honestly
The arXiv API and Semantic Scholar answered 429 or an empty body. I used **OpenAlex** instead: 20 queries × 40 results = 800
records, **723 distinct titles**, of which about 128 are Zenodo/SSRN/figshare/preprint deposits (mostly unrefereed RH claims).
Combined with section (a), the total is above the 200-item target. I screened the titles by keyword. Full list (query, year, title,
DOI): scratchpad `s5/all.tsv`, not committed. Queries: positive definite zeta primes; positive definite Dirichlet series;
explicit formula positivity; Weil quadratic form primes; Weil positivity; number-theoretic spin chain; Farey fraction spin
chain; Lee–Yang + ζ; multiplicative Hankel forms; Beurling generalized primes zeros; trace formula positivity primes; KMS +
ζ; Ruelle zeta RH; dynamical zeta positivity; infinitely divisible + ζ; Nyman/Báez-Duarte; graph zeta RH; Ramanujan/Ihara;
fractal strings RH; multiplicative chaos ζ. The MathOverflow searches returned no thread on Weil positivity, only arXiv
mirrors.

## A.2 New items worth recording (verdicts)

| Item | Status | Properties (P1–P4) | Verdict |
|---|---|---|---|
| Perfekt, "A Fejér–Riesz inequality for Dirichlet series", arXiv 2609.03855 (2026). For Dirichlet polynomials, the integral on the critical line is bounded by the integral on the imaginary axis; the multiplicative Hilbert matrix 1/(√(mn)·log(mn)) has a bounded symbol | PROVED (unrefereed preprint) | P3, P4; P1 partial (all of ℕ, multiplicative); no P2 | **closest new operator-theory item**. A Hankel form in log(mn), i.e. a kernel on log m + log n like c_F. Test: is the window form's prime comb dominated by such a Hankel form plus the Γ_ℝ term? Probably comb-generic, but **not in the index** |
| Multiplicative Hilbert matrix spectra / Bergman Dirichlet series, arXiv 2608.22882; Nehari failure for multiplicative Hankel forms in Schatten classes II, arXiv 2610.06728; positive integral Hankel operators, arXiv 2606.08264 | PROVED | P3, P4 partial | KNOWN-type (Helson family, b6) |
| Letemplier–Simon(?) "A new class of solutions to the van Dantzig problem, the Lee–Yang property, and RH", Ann. Inst. Fourier 2023 | PROVED + reformulation | Laguerre–Pólya class | REF-D (L23 family) |
| "Beurling integers with RH and large oscillation" (Broucke–Debruyne–Vindas, Adv. Math. 2020); Diamond–Montgomery–Vorhauer (Math. Ann. 2006); Beurling zero-density 2407.12746 | PROVED | — | KNOWN (Beurling, phase 150). Confirms that RH-type positivity exists for Beurling systems, so a proof must be able to fail comb-genericity in either direction |
| Positive limit-Fourier transform of Farey fractions (J. Number Theory 2014); SL(2,ℕ)-saturated Farey fractions arXiv 2502.03243, 2508.07951 (Anderson–Boca–Cobeli–Zaharescu) | PROVED | P1 (SL(2,ℕ) words, semiring), P4 | IRRELEVANT for now (no FE). Same arithmetic substrate as Knauf |
| Optimal cosine polynomials for zero-free regions, arXiv 2411.01385 | PROVED | uses only Λ ≥ 0 | comb-generic (Mertens 3+4cos+cos2). KNOWN-type |
| Ihara/graph additions (towers of Ramanujan graphs, reciprocity 1905.03417; isogeny graphs; non-backtracking Ramanujan) | PROVED | — | IRRELEVANT (b1) |
| "Equivalence between ζ zero distribution and a competing two-…" Phys. Lett. A 2026; "Counting fluctuations of Lee–Yang zeros … prime-logarithmic fields" (Zenodo) | CLAIMED / model | — | IRRELEVANT (physics model or claim) |
| arXiv 2609.04908 "Finite Hilbert–Pólya matrices from Weil's explicit formula"; 2610.08965 (83.9% distinct zeros) | numeric / PROVED | — | KNOWN (L52 family / frente D); 2610.08965 belongs with L52 |
| About 120 Zenodo/SSRN "Weil positivity" deposits (certified windows, even-dominance, positive-part operators, "arithmetic bosonization") | CLAIMED, unrefereed | — | not reviewed one by one. Same certificate families as Zhu/Paper 47 |

## A.3 Knauf test (literature level)
Papers checked: Knauf CMP 153 (1993); J. Stat. Phys. 73 (1993); J. Math. Phys. 35 (1994); Contucci–Knauf Forum Math. 9 (1997); Knauf
CMP 196 (1998) "The number-theoretical spin chain and the Riemann zeroes"; Kleban–Özlük CMP 203 (1999); Fiala–Kleban–Özlük
(2003–05, math-ph/0310016, math-ph/0503030); Fiala–Kleban cluster approximation (2006); the 2009 J. Stat. Phys. paper on the
critical point; Contucci–Knauf "fully magnetizing phase transition" math-ph/9811020; Prellberg–Fiala–Kleban (Farey/Ruelle,
Nonlinearity 2014).
- **No paper proves GKS/ferromagnetic positivity at complex inverse temperature.** All the positivity results (interaction
  coefficients ≥ 0, monotone magnetization, the phase transition at β=2) are at real β.
- Knauf (1998) states, as an **empirical** observation, that the chain approximates ζ in the critical strip. He reduces that
  approximation to the **spectral radii of a family of Markov chains / whether certain graphs are Ramanujan**. This is
  CONDITIONAL, with no sign mechanism proved. That reduction links item 9 to item 1 (Ihara).
- The Lee–Yang hope is explicitly left open in this literature (Knauf 1998; Wolf's survey arXiv 1410.1214). As I recall, and
  have not re-verified: the classical Lee–Yang circle theorem needs pair interactions in a magnetic-field variable, whereas Knauf's
  interactions are many-body and the relevant variable is the temperature. No Lee–Yang-type theorem for this chain is known.
- **Verdict:** the Knauf candidate is downgraded from weak NEW-CANDIDATE to **OPEN-unpromising**. Its one live residue is
  Knauf's 1998 graph/Markov spectral-radius reformulation. That residue is a reformulation (REF-D type) and does not carry its
  own positivity. Record it in the index as "Knauf chain: positivity only at real β>2; strip version = Ramanujan-type
  spectral-radius problem, open since 1998".

## A.4 Updated ranking
1. Perfekt's Fejér–Riesz / multiplicative Hilbert matrix (new, P1-partial + P3 + P4). First test: whether the prime comb part of
   𝔞_T is dominated by the multiplicative Hilbert form on P_T. Expected to be comb-generic, but cheap to settle.
2. Knauf chain: OPEN-unpromising (A.3).
3. Helson/Hankel family; 4. Selberg pretrace/LP; 5. MSS interlacing (NO-GO by type). Still no item has P2.
