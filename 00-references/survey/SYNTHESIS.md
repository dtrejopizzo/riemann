# Synthesis of the literature survey for row D

Sources: `BRIEF.md` and the five reports S1–S5 with their addenda. Index: `05-meta-and-planning/ROUTES-TRIED-INDEX/`
(README, "Specification of the sign carrier", phases 194–198; `05_LITERATURE.md`, `05b_LITERATURE_EXTENSION.md`, now with L86–L110).
Row D is treated as a target in its own right: positivity of the window form 𝔞_T (archimedean term Γ_ℝ minus the
comb Σ v_n c_F(log n), v_n = 2Λ(n)/√n) on the primitive space 𝒫_T, for all T > 0. Labels: PROVED / CITED /
CONDITIONAL / OPEN / NO-GO / NUMERICAL / ARGUED / UNVERIFIED.

The four properties of the object sought are those of the BRIEF:
- **P1:** it reads the exact values of the comb (it fails for Beurling systems, for Λ without small primes and for cΛ).
- **P2:** it couples the small primes with the global functional equation, without passing through ζ(½+iτ) and not place by place.
- **P3:** it is not linear, not a cone over log ζ, not coefficientwise integrality, not a dual certificate, not an identity.
- **P4:** it carries a built-in positivity.

## 1. Coverage

| Domain | Titles seen | Read in depth | Note |
|---|---|---|---|
| S1 Weil / Connes / trace formula | 835 (OpenAlex, no homonyms) | ≈25 | |
| S2 spectral / de Branges / operators | ≈560 (463 arXiv ids + ≈95) | 14 + 2 full-text checks | |
| S3 analytic / Fourier | 455 | ≈30 | |
| S4 arithmetic geometry / F₁ / Hodge | ≈390 | ≈12 | most indexed domain |
| S5 cross-field | ≈810 (723 OpenAlex + ≈90) | 12 + Knauf test | |

About 2,500 titles in total, with overlap. The arXiv API returned 429 throughout and the Google Scholar citation
chains could not be followed. Hence arXiv coverage is by text search and OpenAlex, not exhaustive. The ≈120 Zenodo/SSRN
submissions on "Weil positivity" were screened by title, not one by one.

## 2. What others are doing

1. **Window certificates (class thm:Z, dual certificate).** The declared frontier has moved. These data are
   **UNVERIFIED** and are being checked separately:
   - Mori reports covering ½log15 ≈ 1.354 (Zenodo 23281235), with margin 2^{−2904}.
   - Senke reports covering 77/64 (22871383).
   - Liu's latest figure is 17/16.
   - Paper 47 has ½log5 certified.

   Mori also gives an upper bound λ_min ≲ μ^{9/2}log μ·e^{−4πμ} (23175060). If confirmed, it is consistent with
   BARRIER_EST_001. Guo Chen (23297284) proves there are ≥ m eigenvalues within e^{−πλ²} of zero. These are resolution
   data for any mechanism, not sources of sign.
2. **Reformulations.** Unchanged:
   - Connes–Consani–Moscovici (prolate functions, spectral triples, semilocal q-series);
   - Suzuki (screw function, canonical systems);
   - Burnol / Sonin;
   - Li / Keiper;
   - Nyman–Beurling;
   - Biane–Pitman–Yor and infinitely divisible laws.

   All are REF-D or cone conditions.
3. **Fourier analysis and optimisation.** The line Carneiro, Gonçalves, Kurasov–Sarnak, Wei and Lysen is linear on the
   zero side or requires positive measures on both sides.
4. **Absolute geometry.** Connes–Consani 2609.00299 and Haran remain at the level of the curve. No square
   Spec Z ⊗ Spec Z has a pairing with proved positivity. Choi (V185/V189) confirms the tropical wall from outside.
5. **Cross-field.** Ihara, MSS, Ruelle, the primon gas, multiplicative chaos and the Bost–Connes KMS states are not pieces
   of the object. The Knauf chain has positivity only at real β > 2 (OPEN, unpromising).
6. **Claims of complete proofs on Zenodo and SSRN.** All reduce to an unproved positivity step (family L81).

New NO-GOs entering the index:
- Bombieri–Garrett: PROVED from the structure of the paper. It is FE-generic, since a single CM point with an Epstein
  zeta function of class number h > 1 works the same way.
- Faddeev–Pavlov: ARGUED. The primes enter with weight Λ(n)/n at frequency 2 log n.
- MSS: NO-GO by type, through the ∃/∀ mismatch.

## 3. What nobody has

**No item of the survey has P1–P4 simultaneously, and none has P2 together with P4 and P1.** By property:

| Has | Examples | Lacks |
|---|---|---|
| P1 + P3 + P4 | CCM semilocal Jacobi, Knauf, Helson/Perfekt | P2 (local, or no FE) |
| P2 + P4 | Bombieri–Garrett, Faddeev–Pavlov, BPY | P1 (FE-generic or wrong weight) |
| P1 + P2 + P3 | Suzuki (canonical Hamiltonian), Selberg / Hamburger rigidity | P4 (the positivity is the target's, or there is no sign) |
| P2 as an identity | Chen's residue, Burnol's co-Poisson, BRS | P3 |

## 4. Connection layer: combinations across communities

The question is whether two or three results from different communities together have more properties than any one
alone. Answer: **no combination closes all four.** Two structural observations explain why, and three weak candidates
remain.

### Observation A: Rankin–Selberg sign and rigidity share the same blind spot (ARGUED)

S3 noted that the literature uses prime values either through their *sign* (Miller, Chenevier, OPS, Trudgian 2610.16010)
or through *rigidity without sign* (Selberg class, Hamburger). The natural question is whether anyone has combined sign
and rigidity.

Nobody has, and there is a reason. The Rankin–Selberg sign is |a_p|² ≥ 0, invariant under a_p ↦ −a_p. The
functional-equation defect is also invariant under d(p^j) ↦ (−1)^j d(p^j): this is Kronecker parity, X2 of
BARRIER_X_001, PROVED for distributional defects in σ-closed classes. Both tools are blind to the same parity twin. Hence
their conjunction does not separate Λ from its twins at odd levels, and the quantitative signed version is already closed
(BARRIER_D1_001 Thm 4, D2).

The only thing the combination could touch is the **even levels p^{2j} < e^{2T}**, already listed as a residue in X_001.

- **First concrete theorem:** in the window ½log4 < T ≤ ½log9 the only active even level is 4.
  1. Decide whether positivity of the coefficients of ζ×ζ at p² (that is, 1∗Λ evaluated at 4) together with the FE
     defect restricted to level 4 gives a one-sided constraint on a(4).
  2. Test against the falsifiers a_2 and 2Λ of CERT_FALSIFIERS_001.
- **Forecast:** a one-coordinate cone, which would fall by thm:shape. It is cheap.

### Observation B: the weight gap (ARGUED; a pattern, not a theorem)

Almost all the built-in positivities found read the primes at weight n^{−1} or beyond absolute convergence:
- Faddeev–Pavlov unitarity: Λ(n)/n;
- Bombieri–Garrett: boundary σ = 1;
- Ш/Poisson: it is the Euler product at σ = 1 (INV_V_001, V1.3, PROVED);
- Rankin–Selberg: σ > 1;
- Knauf: β > 2;
- CCM moments: local factors.

The comb of row D lives at weight n^{−1/2}. The only built-in positivity at critical weight is the multiplicative
Hilbert matrix 1/(√(mn)log(mn)) (Helson, Perfekt 2609.03855), and it has no functional equation.

The cell "weight ½ + global FE + built-in positivity" is empty in the literature. This restates P2 with a new datum:
the object has to produce positivity at weight ½ without analytic continuation from σ ≥ 1, because that continuation is
exactly where the cited positivities are lost (MW-4, FP).

### Combination candidates (ranked)

| # | Combination | What it would give | What is missing | First theorem | Verdict |
|---|---|---|---|---|---|
| C1 | CCM semilocal Jacobi (P1, P3, local P4) + Guo Chen's residual identity via the summation map u^{1/2}Σf(nu) (P2, identity) + cumulant scale e^{−πλ²} (Chen, Mori) as a constraint | The four properties distributed among pieces: global gluing by Poisson, sign by the local moment | That the gluing transports sign. This is the dead sub-route L81 ("semilocal stabilisation without a source of sign"); the Sonin chain (phase 183) is PROVED and has no sign; the local FE is O_6-stable (INV_L_001 L1) | Write 𝔞_T restricted to images of h* under the summation map as (semilocal form A_S with S = primes < e^{2T}) + (Chen residue). Prove the residue is ≥ −(margin of A_S) or falsify it with a_P | OPEN, unpromising. New reason relative to L81: the gluing term is explicit (not used before; Chen has one hit in the corpus). If the residue is comb-generic (Beurling), it dies immediately |
| C2 | RS sign (Miller/Chenevier) + Hamburger / Selberg rigidity | P1 + P2 + P4 | Blocked by Observation A (Kronecker parity) | Even-level-4 test described in Observation A | Only the even-level residue; the rest is closed (D1, D2, X2) |
| C3 | DH gate (Ziad, a = 9/5) + Beurling/cΛ/a_P + Elston's matched pair | Not an object: a **battery of falsifiers requiring P1 ∧ P2 simultaneously**. DH has FE without Euler product; a_P and Beurling have Euler form without FE | — | Certify the DH witness in the convention of def:PD and add it to CERT_FALSIFIERS_001 (F-DH already exists in the corpus, without explicit window) | **Useful and cheap.** Makes clause (5) operational |
| C4 | Multiplicative Hilbert matrix (Perfekt, weight ½) + Γ_ℝ term | The only positivity at critical weight that reads the (ℕ,·) structure, in line with the semiring principle | P2 (no FE) and crossing ∂log: Λ appears only through −ζ′/ζ, and INV_F_001 says free cones do not cross ∂log | Falsifier test first: does a Fejér–Riesz-type bound of the comb by the Hilbert form + Γ_ℝ distinguish Λ from a Beurling system with the same bound |Λ| ≤ log n? | Forecast: comb-generic. To be recorded |
| C5 | Integer-mass quasicrystals / Lee–Yang (Wei) + Kaltenbäck–Woracek index stability; Knauf + Bombieri–Garrett/FP | Integrality + integer index; semiring + FE | The explicit formula is not a Fourier quasicrystal (a.c. density of Γ_ℝ, signed comb); the integer invariant is dead (BARRIER_W_001); Knauf and BG/FP live at the wrong weight (Observation B) | — | Nothing combines |

## 5. Recommended constructions (in order)

1. **F-DH gate with window (C3).** Certify by interval arithmetic, in our convention, Ziad's negative Davenport–Heilbronn
   witness at a = 9/5. Then adopt it as a mandatory test for every carrier, together with Beurling, cΛ and a_P. Cheap and
   useful for everything that follows.
2. **Even-level-4 test (C2 / Observation A).** A finite statement. If it comes out as expected, it closes the "even levels"
   residue of X_001 at the first level.
3. **C1, only after a corpus check against L81, phase 183, INV_L_001 and CCM.** The new reason (Chen's explicit residue as
   gluing term) must be written down, and the Beurling falsifier must first be run on the residue.
4. **C4 as a recorded NO-GO.** An afternoon's work; the value is in documenting the weight gap.
5. **Mori, Senke and Chen:** await the verification report before citing them in Paper 47 or using the scale e^{−4πμ} as a
   constraint.

**Conclusion.** The survey did not find the object, nor a combination that assembles it. It leaves two contributions:
- the two structural patterns of §4 (the common blind spot of sign and rigidity, and the weight gap), which constrain
  where the object has to live: at weight ½, with global FE, and seeing Kronecker parity;
- a finer battery of falsifiers.

Row D remains OPEN.
