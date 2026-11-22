# AUDIT_CONSTRAINTS_001 — audit of the constraint list 1–28 (AUDIT_L_SHARP_16 §6)

Pen and paper only; no new numerics.
NO-GO / NUMÉRICO. Sources traced: AUDIT_L_SHARP_1 §6.3 (1–7), _2 §7 (8–11), _3 §7 (12–13), _4 §8 (14–15), _5 §6 (16–17), _6 §4 (18),
_7 §7 (19, restriction of 7), _8 §9 (20), _9 §9 (21), _10 §6 (22), _12 (24), _13 §6 (25), _14 (26), _15 §5 (27), _16 §6 (28);
AUDIT_199 (e); phase-197 BARRIER_EST_001, BARRIER_001, AUDIT_197_HOSTILE (O_4^ε).

**Question.** Which of the 28 could a *correct* proof of L′♯ / (★★) violate?
**Verdict in one line.** 9 are HARD (theorem with checked hypotheses, inside a stated class), 11 are SOFT (rest on ARGUED,
NUMÉRICO at μ = 15, a narrow class, or a CONDITIONAL/CITED input), 8 are MISLABELLED (test-design rules, tool limitations,
open questions, or empty). No constraint excludes an exact-identity proof in the exterior variable as such. No sign claimed.

## 0. Two upstream dependencies
- **rem:moriceiling** (Paper 46, CITED, PLAUSIBLE-UNVERIFIED, uses zero data; AUDIT_199 (e)). It enters only the *size*
  κ₊μ^{9/2}e^{−4πμ} of the TV slack in constraint 1. The qualitative barrier r ≤ λ_A (BARRIER_EST Thm 4) is PROVED without
  it. No other constraint depends on it. The base case μ ≤ 15 (H Prop H.1) depends on Mori Theorem O (CITED), not on the ceiling.
- **O_4^ε** (cΛ with |c−1| < ε; CONDITIONAL on κ_T ≠ 0, AUDIT_197_HOSTILE). Constraints 2 and 5 exclude "comb-generic"
  premises by the falsifiers cΛ, a_P, Beurling. cΛ for fixed c ≠ 1 and a_P are certified by intervals (CERT_FALSIFIERS_001)
  at specific T; for premises that only survive c → 1 the exclusion is CONDITIONAL. Beurling is NUMÉRICO, F-DH UNVERIFIED.

## 1. Table

| # | statement (short) | source | label of argument | class excluded / hypothesis | legitimate escape | verdict |
|---|---|---|---|---|---|---|
| 1 | TV-slack of comb premises ≤ λ^W_T on the window carrier | AUD_1 §6.3; BARRIER_EST Thm 4 | PROVED (qualitative); size CONDITIONAL on rem:moriceiling | premises about W_T robust in TV around Λ, *window carrier* | exact-arithmetic premises; exterior carrier (no doubly-exp barrier there, AUD_1 §4.3(b), ARGUED) | HARD in class; does not bind exterior-carrier proofs |
| 2 | no identity + Bochner/C–S/Schur that is comb-generic | AUD_1; N_018 | PROVED as meta-statement, given falsifiers | arguments whose every step holds for cΛ, a_P, Beurling | use a step false for the falsifiers; for c→1 only CONDITIONAL (O_4^ε) | HARD (tautological core) |
| 3 | "not symbolic" | AUD_1 (A Rem 3.3, C Thm 3.1, C Rem 2.1(ii)) | PROVED for the scalar diagonal symbol of the full Weil distribution on Re s = ½; "not a square" off-line ARGUED | W_T = ∫w(τ)|F̃|², w ≥ 0, on the critical line, full distribution | matrix/operator-valued symbols, symbols of the *truncated* or Π-projected form, other contours, symbols on the exterior variable (the 𝔴-weight of SYNTHESIS is one) | SOFT (name overstates: only scalar diagonal Mellin weights are excluded) |
| 4 | not multiplier bounds / classwise SOS / Bochner-Lévy+C–S / Son≥0+remainder / uniformised certificate | AUD_1 | mixed: multiplier NO-GO **ARGUED only** (C Thm 6.1 RETRACTED); E.5 PROVED on fixed-shape data; B Thm 4.2 PROVED; D Prop 3.1 PROVED | each sub-class as named | multiplier bounds on the exterior carrier: not excluded by any theorem | SOFT (sub-item "multiplier"); rest HARD |
| 5 | must use a_n≡1, residue 1, Γ_ℝ conductor 1, aliasing at n≈λ/u together; must fail for cΛ,a_P,Beurling | AUD_1/2 | "sufficient list" PROVED; "must use each, *together*, *at* n≈λ/u" ARGUED; "fail for" HARD only for certified falsifiers | proofs not distinguishing Λ | use the inputs elsewhere than the boundary (e.g. residue globally via GG polar ≡ 0) | SOFT (localisation/conjunction); HARD (fail-for-falsifiers part) |
| 6 | quadratic leakage scale μ^{−A}dist² | AUD_1; Guo Thm 1.6 CITED | ARGUED ("only compatible shape"); finite-block dimension ARGUED | it is the *definition* of L′♯, not a class | prove row D by a lemma with sub-exponential loss if Prop 3.2 tolerates it (OPEN) | MISLABELLED (target shape) |
| 7 | cross-ratio-class cancellation required | AUD_1; restricted AUD_7 §4.3 | ARGUED; forced only on gauge-like data (E.5) | per-class diagonal arguments on data with low-Mellin components | work on Π-projected data (S1), where it is "ARGUED both ways" | SOFT |
| 8 | no antisymmetric Hilbert kernel in integer index | AUD_2 (J Thm J.2) | PROVED as stated; "Toeplitz/large-sieve = comb-generic" ARGUED | Hilbert/Montgomery–Vaughan type bounds | none for Hilbert class | HARD (narrow) |
| 9 | deep-mode value 0.046 B_φ² | AUD_2 (J Thm J.3) | PROVED given PNT; AUD_2 itself: "test object, not a constraint" | none (radical direction for PW data) | — | MISLABELLED |
| 10 | pole term couples the Q-null vector | AUD_2 (F Thm F.2) | PROVED *in F-type splits* (full-line null part + defect) | block arguments ignoring 2AB in that split | translate basis FF.1/GG: polar term ≡ 0 (GG, PROVED, f(0)=f̂(0)=0) | SOFT (split-dependent; vacuous in FF.1 basis) |
| 11 | no flow/continuation without virial bound | AUD_2 (H Thm H.5) | H.5 PROVED mod Lemma 4.1; class NO-GO ARGUED | Grönwall in T or c without (H) ρ_N ≤ ρ_L + A/c | prove (H) itself (necessary & sufficient, so a flow proof that proves it is legal) | SOFT |
| 12 | no E-image of one prolate with small repair | AUD_3 (K.1b) | PROVED given CITED prolate asymptotics (classical) | "Eψ₀ + small" | multi-prolate / repaired span (allowed) | HARD |
| 13 | pole couples only through rank-one residues | AUD_3 (P) | F₀-piece rank one PROVED; "no proved finite rank" of J_c′, I_c = absence of a result; μ=5 low rank NUMÉRICO | none (a structural *positive* fact) | — | MISLABELLED (fact, not exclusion) |
| 14 | harmonics = dilations, no per-harmonic sign | AUD_4 (S.4) | dilation identity PROVED; "no per-harmonic sign" ARGUED/NUMÉRICO; PD on span{k≥3} NUMÉRICO | free-amplitude per-harmonic sign | grouped sign: {1,2} jointly + PD block k≥3 with forced coefficients | SOFT |
| 15 | (C_G)(b) self-dual, not a reduction | AUD_4/5 | mirror PROVED on C_c^∞(1,∞); CONDITIONAL on PW tails | counting (b) as a reduction | on PW (window) data the mirror is not proved ⇒ (b) may be a genuine reduction there | SOFT |
| 16 | Sonin/PW transfer gap | AUD_5 | 𝒮∩C_c={0} PROVED; transfer = OPEN lemma | sector formula used without a transfer | supply the transfer (open, not excluded) | MISLABELLED (open prerequisite) |
| 17 | gauge must be fixed before comparing forms | AUD_5 | coset unboundedness PROVED mod NUMÉRICO vector | comparisons of non-gauge-invariant pieces | fix any gauge (cost-free) | HARD (hygiene) |
| 18 | sector reduction = parity only | AUD_6 §4 | standard 𝔉: PROVED-empty; exact 𝔉_μ: PROVED false (PW); approximate 𝔉_μ: ARGUED (from shipped profile) | exact sector reductions | approximate sector reduction with error ≪ leakage scale | SOFT (approximate version) |
| 19 | semiclassical on Π-data; edge channel leading order | AUD_7 §7 | (a) PROVED (E.5 + non-invariance); (b) NUMÉRICO μ=15 (51–78 %); (c) hygiene | (a) raw-r stationary phase; (b) asymptotics dropping the edge | (b): an asymptotic theorem μ ≥ μ₀ where the edge share is proved sub-leading | (a) HARD; (b) SOFT |
| 20 | single-cell data test nothing of interference | AUD_8 (X.1/X.3) | PROVED | evidence from single-cell data | — | MISLABELLED (rule on evidence, not on proofs) |
| 21 | (1,n) resonances: uniform stationary phase with remainder | AUD_9 | geometry PROVED; smallness ARGUED | P2-type estimates without explicit remainder | avoid stationary phase (exact identity) | SOFT (binds only P2-type proofs) |
| 22 | P3b test needs Schur against block with v, without bottom eigvec | AUD_10 | test-design rule | — | — | MISLABELLED |
| 23 | (no record) | — | — | — | — | MISLABELLED (empty) |
| 24 | Möbius-lattice structure; single-line models invalid | AUD_12; AA_001 Thm D | (a),(b) PROVED; (c),(d) NUMÉRICO | single-tail (m=1 only) bounds on (1,n) | none for (a)/(b) | HARD (a,b) |
| 25 | lattice/class forms must respect the 33-digit cancellation | AUD_13, AUD_16 | identity Σμ(m)σ^{(m)}+φ̂₀ = O(ρ_p) PROVED; digit count and "Gram inertia blind" NUMÉRICO μ=15 | coefficient-level / inertia arguments in the line basis | exact arithmetic in a basis where the cancellation is built in (exterior variable ρ of EE_001, or symbolic Möbius tail) | SOFT (property of bases/conditioning, not of proofs) |
| 26 | thm:ext-layer(iii) explicit η only N≳130 | AUD_14 | PROVED limitation of a lemma | none | sharper constants (actual η ~400× smaller) | MISLABELLED (tool gap) |
| 27 | Schur plank needs exact resolvent; operator coupling OPEN | AUD_15 §5 | crude failure NUMÉRICO (θ_50 = 1.0075, μ=15, J=50); coupling OPEN | crude 1/c_Q Schur on V_50 | sign-sensitive substitute; other subspace; the "OPEN" half is not a constraint | SOFT (+ MISLABELLED half) |
| 28 | edge jet not a coordinate for ω ≲ 54m | AUD_16 §6 | NUMÉRICO μ=15; kink-tail NO-GO for orders 0–2 + resummation at μ=15; a_P gap PROVED | jet/kink coordinates at μ=15 | asymptotic regime (threshold 54m vs data window scaling unproved) | SOFT |

Counts: HARD {1,2,8,12,17,24} + HARD parts of {4,5,19(a)} ; SOFT {3,4(mult.),5(loc.),7,10,11,14,15,18,19(b),21,25,27,28};
MISLABELLED {6,9,13,16,20,22,23,26}. (Rows with split verdicts counted once under SOFT where any part is SOFT.)

## 2. Internal consistency and pair effects
- **10 vs FF.1/GG (tension, resolved).** 10 says 2AB cannot be ignored; GG proves the polar term ≡ 0 in the translate basis.
  Not a contradiction: 10 is a statement about F-type splits. It must be relabelled "split-dependent".
- **10 + 13 permit, not exclude:** together they say the pole coupling is unavoidable *and* rank one in its F₀-piece — this
  licenses a rank-one Schur/Sherman–Morrison treatment of the pole; no constraint forbids it.
- **7 vs 19(a):** consistent after AUD_7: 7 is restricted to gauge-like data and 19(a) moves every semiclassical argument to
  Π-data, where 7 is unproved. Jointly they leave the Π-projected diagonal (𝔴) route open.
- **19(b) + 26 + base case (pair exclusion).** An "asymptotic theorem + certified base" proof needs μ₀ ≤ 15 (H.1 base).
  19(b) forces the edge at leading order at μ=15, and 26 makes the only explicit layer bound non-vacuous for N ≳ 130. Each
  alone permits the asymptotic route; together they exclude it **unless** the window 15 < μ ≲ 130 is covered by new certificates
  or the η-constants of thm:ext-layer(iii) are improved ~10×. This is the one genuine pair exclusion found.
- **25 + 28:** both NUMÉRICO at μ=15 in the same data; together they exclude any *floating-point line/jet* decomposition at
  μ=15, but neither binds an exact symbolic computation.
- **16 vs 18:** no conflict (Sonin is a support condition, not an 𝔉-eigen sector).
- No contradiction between any two constraints was found.

## 3. SOFT constraints ranked by escape value (with the new reason required by the index rule)
1. **7 (cross-class cancellation, ARGUED).** Escape: per-class/diagonal bound on Π-projected data. Reopens SYNTHESIS_MECHANISM
   M3 / T1 (diagonal weight 𝔴). New reason: the killing argument (E.5) uses gauge-like fixed-shape bumps; after Π (U.2) that
   object has no component, and AUD_7 itself records the forcing as unproved there.
2. **10 (pole coupling, split-dependent).** Escape: write the proof in the FF.1/GG translate basis, polar ≡ 0. Reopens
   P_001/(C_G) block splitting, now in the translate basis. New reason: the object changes (FF.1 translate basis, polar
   identically zero, PROVED), which removes the exact reason (2AB coupling) block arguments were killed.
3. **25 (33-digit cancellation).** Escape: exact-arithmetic proof in the exterior variable ρ (EE_001) where the cancellation is
   an identity. Reopens the AA_001 D(iv) class-vs-diagonal programme *only* in that basis. New reason: the kill was a
   conditioning fact of the line basis (NUMÉRICO), not a theorem about the form.
4. **11 (virial).** Escape: prove (H) via the CC_001 envelope (ρ_N controlled asymptotically). Reopens H_001 Grönwall. New
   reason: CC_001 (later than H_001) supplies an explicit tail quantity of the type (H) needs; still blocked by the 19(b)+26 pair.
5. **14 (per-harmonic).** Escape: grouped sign {1,2} ⊕ {k≥3} with forced coefficients. Reopens S_001. New reason: the NO-GO
   was for free amplitudes; the k≥3 block is NUMÉRICO-PD with coefficients ≡ 1.
6. **15 (self-duality on PW).** Escape: (C_G)(b) on PW data where the mirror is only CONDITIONAL. Reopens S_001/T_001 (b).
7. **3 (symbolic).** Escape: operator-valued / exterior-variable symbols. Reopens the symbol family only for non-scalar symbols.
8. **18 (approximate sectors), 21, 27, 28, 4 (multiplier on exterior carrier), 5 (localisation), 19(b):** lower value; each
   escape is either open-ended (approximate 𝔉_μ, exterior multipliers — reopen C_001 only with an exterior-carrier argument
   avoiding N_018) or blocked by the 19(b)+26 pair (21, 28, 19(b)).

**Upshot.** The HARD core is: not TV-robust on the window carrier (1), not comb-generic (2), lattice structure exact (24),
gauge fixed (17), no Hilbert kernel (8), no single-prolate repair (12). Everything else is violable by a correct proof that
works with exact identities on Π-projected or translate-basis data. No sign of row D is claimed. L′♯ OPEN. **Row D OPEN.**
