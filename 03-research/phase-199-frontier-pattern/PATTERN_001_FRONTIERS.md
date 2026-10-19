# PATTERN_001 — what repeats across the certified frontiers (½log5, 17/16, ½log10, ½log12, ½log15)

Phase 199, analyst memo.
The only script is `scripts_pat199.py` (mpmath, prolate-model
arithmetic only).

## Corpus check
- ROUTES-TRIED-INDEX: "Frontera certificada" (Mori ½log15 CITED; ceiling exp(−4πe^{2T})).
  AUDIT_ZENODO_FRONTIER (B1 Fuchs check, B2 ceiling, B3 Guo clusters). AUDIT_LIU.
  Survey SYNTHESIS §4 C1 (Guo summation-map identity, "connection candidate", OPEN, falls on L81).
  Phase 198 (Lemma M, CERT_FALSIFIERS_001). Phase 197 BARRIER_W_001 (W1).
- Mori's repository README and paper V Table 1 (scratchpad `zen/pwb`, `zen/moriV.txt`) give Galerkin ratios that the
  index did not yet record. These are used below as NUMÉRICO, with Mori as the source.
- Not used: Mori paper IV, which has a lower bound conditional on a global hypothesis. It is excluded.
- New with respect to the index: (i) the contact-sawtooth reading of Mori's ratio table; (ii) the cost law for the next
  windows; (iii) the conjecture κ-band (§3) stated as a two-sided comparison with the prolate defect. None of these is
  a construction route, so the no-retry rule is not triggered.

## 1. Table of frontiers (μ = e^{2T}; contacts are n < μ with Λ(n) ≠ 0)

| frontier | μ | contacts | next contact | quantity certified | finite margin | Galerkin N | precision | status |
|---|---|---|---|---|---|---|---|---|
| Paper 47 | 5 | 2,3,4 | 5 | λ_A ≥ 2.5e−12, λ^W ≥ 1e−18 | λ_A ≈ 3.10e−12 (primitive form) | k = 25 | double/interval | PROVED |
| Liu Thm B | 8.37 (T = 17/16) | 2,3,4,5,7,8 | 9 | λ^W ≥ 2^{−49162} | not reported (224×224 integer Gram) | 224 | exact integer | CITED |
| Mori VI | 10 | …,9 | 11 | λ^W ≥ 2^{−49162} | not in hand | N = 640 | ? | CITED (not audited) |
| Mori VII | 12 | …,11 | 13 | λ^W ≥ 2^{−1518} | not in hand | N = 832 | ? | CITED (not audited) |
| Mori VIII | 15 | …,11,13 | 16 | λ^W ≥ 2^{−2904} | 2.40e−70 even / 3.95e−66 odd (≈2^{−232}/2^{−218}) | N = 1664, Ω = 736 | 3328 bits | CITED, reproduced |

(Liu and Mori VI report the same final constant 2^{−49162}. That constant is the out-of-band δ of the shared Liu
framework, not a margin. The coincidence is worth flagging but is not an error.)

**Contact hypothesis.** The claim "every frontier stops just before the next contact" holds only weakly. Each frontier lies in
a contact-free interval (n_k, n_{k+1}]:
- ½log5 lies at the right endpoint μ = 5 exactly. Since 5 enters only for μ > 5, this is the optimal endpoint.
- 8.37 lies in (8, 9], 10 in (9, 11], 12 in (11, 13], and 15 in (13, 16].
- Only Paper 47 sits on the endpoint itself. Liu, Mori VI and Mori VII stop short of it, at 9, 11 and 13 respectively.

**Structural reason (PROVED, elementary).** Inside a contact-free interval the comb is fixed. By Lemma M
(AUDIT_198; P47 lem:monoT), λ is nonincreasing in T. A certificate at the right endpoint μ = n_{k+1} therefore covers
the whole interval, and the matrix family (the shifts) does not change inside it. The cost driver is μ itself (the archimedean
bandwidth c = 2πμ), not the comb. Two consequences follow:
- Certificates are naturally piecewise between contacts.
- The cheapest improvement is always to push to the next endpoint with the same comb. For example, 15 → 16 adds no
  new shift, because 16 enters only for μ > 16.

The "onset ~ η/log(1/η)" of a new contact is not needed for this argument.

## 2. Margin law (NUMÉRICO unless stated)

Prolate model: λ_min(μ) ≈ κ(μ)·(1 − λ₄(2πμ)). Fuchs gives 1 − λ₄(c) ≈ (4√π·8⁴/4!) c^{9/2} e^{−2c} with c = 2πμ, so
λ_min ≈ κ·const·μ^{9/2} e^{−4πμ}. Mori's Theorem K proves the matching upper bound for μ ≥ 50 (CITED).

Data:
- **Mori paper V, Table 1** (Galerkin, quadrature not enclosed, NUMÉRICO, CITED source).

  | μ | 7 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
  |---|---|---|---|---|---|---|---|---|---|---|---|
  | κ | 4.21 | 4.72 | 4.11 | 4.94 | 4.55 | 4.63 | 4.49 | 4.70 | 4.38 | 5.34 | 4.90 |

  At μ = 20, λ_min = 1.09899e−96, computed with 1300 bits; 840 bits gave a *negative* value, which was a precision
  artefact.
- **Certified Schur margin at μ = 15:** 2.40e−70. This is 1.9 × Fuchs(15) = 1.27e−70. It is a different quantity, the
  bottom of a compressed Schur complement, and it is of the same order (CITED, reproduced).
- **Slopes of log λ:**
  - between μ = 15 and 20, the slope is −12.13 per unit μ;
  - the model slope, including the μ^{9/2} factor, is −12.31;
  - 4π = 12.566.

  So **c ≈ 4π is confirmed**: the decay is exp(−4πμ) up to polynomial factors.
- **The Paper 47 point at μ = 5 is not comparable.** It is the primitive form λ_A, which is about 10⁶ × the Fuchs value.
  The prolate model applies to λ^W, the complete form.

**New observation (NUMÉRICO, a reading of Mori's table): contact sawtooth.** In every case κ is high at μ = p, where the contact
p is still excluded, and drops at the next integer, after p has entered:
- 11 → 12: 4.72 → 4.11
- 13 → 14: 4.94 → 4.55
- 16 → 17: 4.49 → 4.70 (16 is still excluded at 16; it enters for 17)
- 17 → 18: 4.70 → 4.38
- 19 → 20: 5.34 → 4.90

This matches Lemma M exactly. Each new shift can only lower λ, while the smooth defect 1 − λ₄ is contact-blind. Mori notes
the fluctuation but did not test the arithmetic explanation. The sawtooth is consistent with Lemma M plus an O(1) jump in κ
at each contact, of relative size roughly 8–15%.

**Predicted cost of the next windows** (prediction = 4.6 × Fuchs; "bits" means bits needed just to see the margin; the
certificate needs ≈ 2N working bits):

| μ | 16 | 17 | 19 | 23 | 25 | 27 | 29 | 31 | 32 |
|---|---|---|---|---|---|---|---|---|---|
| λ_min (pred.) | 3e−75 | 1e−80 | 3e−91 | 9e−113 | 2e−123 | 3e−134 | 4e−145 | 7e−156 | 3e−161 |
| margin bits | 248 | 265 | 301 | 372 | 408 | 444 | 480 | 515 | 533 |
| Galerkin N ≈ 2.3·(½log μ)·2πμ | 320 | 348 | 404 | 521 | 581 | 642 | 705 | 769 | 801 |

The margin bits grow like 4πμ/ln2 ≈ 18.1μ, minus a log correction.

The certificate N (Liu–Mori bounded comparison) is about 5× the Galerkin N: 1664 against 293 at μ = 15. Ω grew from 416
at μ = 12 to 736 at μ = 15. Extrapolating log-linearly, which is crude:
- μ = 16: Ω ≈ 890, N ≈ 2060, about 4100 bits.
- μ ≈ 20: N ≈ 3500.
- μ ≈ 32: N above 10⁴.

**What kind of asymptote this is.** It is a **computational-cost asymptote**:
- The margin decays doubly exponentially in T: log(1/λ) ≈ 4πe^{2T}.
- The certificate cost per window is polynomial in μ, roughly N³·bits^{1.6} ~ μ⁴, so exponential in T.
- The number of contact intervals up to T grows like e^{2T}/(2T).

Nothing in the data points to a sign change. Every computed κ lies in [4.1, 5.4], a positive band with no downward
drift. Mori's one negative value came from too few precision bits and disappeared at 1300 bits. **No sign claim is made.**

## 3. Mathematical content: is exp(−4πμ) comb-generic?

**No, not in the relevant sense.**
- The upper bound (Mori II/III/V) and the cluster theorem (Guo) both use test vectors that are images of prolates under
  the summation map f ↦ u^{1/2}Σ_{n≥1} f(nu). Their exact residual identity (Poisson summation plus explicit formula) holds
  for the Λ comb. It is the multiplicative–additive coupling of ℕ, in line with the semiring principle.
- For any other comb a, the same vectors carry an extra term Σ(a(n) − Λ(n))(…) of size O(1), not e^{−4πμ}.
- This fits the certified falsifiers (CERT_FALSIFIERS_001, PROVED): cΛ with c > 1, a_2, a_3, deletions and the zero comb
  have bottoms between −0.0027 and −1.05 at T ≤ 1, that is, O(1) below zero.

So the archimedean prolate structure sets the *scale* e^{−4πμ} (the prolate defect with bandwidth·time = 2πμ). It is the
arithmetic, through the summation-map identity, that places Λ *within that scale of 0*.

**Quantitative sign signature.** For the Λ comb, the bottom sits at +κ·(1 − λ₄(2πμ)) with κ ≈ 4–5. For each falsifier,
the bottom sits at −Θ(1).

**Conjecture κ-band (OPEN).** There are constants 0 < κ₋ ≤ κ₊ < ∞ such that for every μ ≥ 5:

  κ₋ (1 − λ₄(2πμ)) ≤ λ^W_{½logμ}(Λ) ≤ κ₊ (1 − λ₄(2πμ)).

- The upper half is CITED for μ ≥ 50, with a non-sharp constant (Mori Theorem K, up to log μ).
- The ratio κ(μ) is expected to have **no limit**. By Lemma M it has downward jumps at every contact and drifts upward
  between contacts, so the right statement is a liminf/limsup band.
- The numerics suggest κ₋ ≈ 4.1 and κ₊ ≈ 5.4 on 7 ≤ μ ≤ 20 (NUMÉRICO).

**What the lower half would require.**
- The index 4 means that, in the model, the four lowest prolate directions behind the residual identity are absorbed. A
  lower bound must prove *coercivity of the form on the complement of the span of the summation-map images of ψ₀,…,ψ₃*,
  with constant ≥ κ₋(1 − λ₄).
- That is an inverse (stability) estimate for the Guo residual identity. In effect it is a Poisson-summation
  large-sieve-type inequality at resolution e^{−4πμ}, uniform in μ, which has to cross every contact jump.
- No such inverse estimate exists in the corpus or the literature we have.
- It is the quantitative form of survey C1, which is OPEN and falls on L81 unless the gluing term supplies the sign. It remains to decide whether to open it, given a new reason: C1 asked for a sign, while κ-band asks for a *comparison
  with a known archimedean quantity*, which is a different class of statement.
- Guo's growing cluster multiplicity is also relevant. In the model, κ₋ must survive m near-zero eigenvalues inside
  [−δ_m, δ_m] at larger μ. Any lower-bound method has to separate them.

## 4. Feasibility of μ = 16 (T = log 4)

The comb is the same as at μ = 15 (contacts up to 13), because 16 enters only for μ > 16. Predicted figures:
- margin ≈ 3e−75 (≈ 2^{−248});
- certificate N ≈ 2000–2100;
- about 4100 working bits;
- source-matrix time ≈ 2.5–3 × 7800 s per parity, about 6 h;
- memory ≈ 9–10 GB per parity.

This is **feasible** on a 32–64 GB workstation with Mori's public code (v1.6.2), with Ω retuned so that C > u·E holds.
Pushing on to μ = 17 (adding 16) and μ = 19 needs N ≈ 2500–3000 and is still feasible but slow. Each window adds about
5–6 orders of magnitude of resolution per unit μ.

Value for row D: a range record only. It is not a mechanism for all T (class: dual certificate / bounded comparison, KNOWN).

## Verdict
- Pattern: piecewise certificates between contacts (PROVED, via Lemma M), with a margin law of exp(−4πμ)·poly(μ) (NUMÉRICO,
  c ≈ 4π confirmed) and a contact sawtooth in κ (NUMÉRICO, new).
- The asymptote is computational.
- The sign signature (Λ sits at +κ·defect while the falsifiers sit at −O(1)) is formulated as Conjecture κ-band (OPEN).
  Its lower half is the precise target: an inverse estimate for the summation-map residual identity.
- Row D OPEN.
