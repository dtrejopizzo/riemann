# SPEC_SIGN_OBJECT_011 — Round 23, phase 200: oscillation counts as an h⁰ candidate ("window Courant–Sturm")

Synthesizer. Pure mathematics; no new numerics.

## 0. Summary (≤300 words)

Question: can an integer oscillation count N(E) (zeros or sign changes of a function built from the test and the
comb) serve as h⁰ in a quadratic window RR? Can negativity 𝔞_T(g) < 0 force a function with fewer oscillations
than Sturm–Hurwitz or Eremenko–Novikov require?

Verdict: **class NO-GO (ARGUED, with two PROVED lemmas).** Three facts support it.

1. **Genuine escape from Theorem 3′.** Theorem 3′ kills the exact identity χ_n(E) = ½n²I_∞ + O(n) for analytic
invariants. A nodal count is semialgebraic and locally constant, but its *asymptotics* in n can be continuous
(Weyl-law type). That gap exists. It is the only genuine novelty of this family.
2. **The available counts do not see the comb (S5).** The spectral gap of the high-frequency part r exists by
definition (support in |ξ| > λ). The Eremenko–Novikov bound, sign-change density ≥ λ/π, depends only on λ = e^T.
It is comb-generic and holds the same for Epstein (Lemma E).
3. **The directions do not oppose each other, and negativity lives at low frequency.** Courant says "index k ⇒ ≤
k+1 nodal domains". Sturm says "gap ⇒ many zeros". The two inequalities act on different eigenvectors: the
negative ones are low index, and the gap ones are high index. So they never chain against n₋. By Theorem P
(phase 155), the negative subspace of A_∞|P_T lies within the first ≤ 8 prolate modes. There, any oscillation
lower bound from a gap is vacuous.

Moreover, Courant on the block requires a Sturm–Liouville operator commuting with the full form W_T. For the
archimedean part it exists (the Slepian "miracle", CITED). For the form with the comb it is OPEN and probably
false (Lemma CS-0).

Descartes (R162_1501, DEAD), Pólya frequency (DEAD, fails PF₂) and Kreĭn (REF-D) are already in the index.

**First exact lemma proposed:** CS-0, the second-order differential commutant of W_T on [−T,T] (bispectral
rigidity). If it is trivial, the Courant–Sturm route is closed as NO-GO PROVED. High risk, low cost. Nothing goes
to P46.

## 1. Corpus check (mandatory grep, with line number)

Index `05-meta-and-planning/ROUTES-TRIED-INDEX/`:

- README.md:36 — "**Total positivity / PF / Karlin / Sturm / nodal measure**: 104_21 (fails PF₂), 104_83,
  R155_046/047, R162_1701 §2.4, R186_041/113." Closed family.
- 04_PHASES_100-189.md:395 — `G8D-155 thm:arena/P8 | Nodal/Sturm criterion, fixed finite truncation | DEAD
  [arena ≥12 modes, not PF₂] | Karlin unavailable; semigroup PF₂ t≥1 open.`
- 04_PHASES_100-189.md:672 — `G8D-R160_S4 §2.D#45-46 | Nodal/Sturm criterion; finite archimedean truncation |
  DEAD [arena N*>=12, not PF2]`.
- 04_PHASES_100-189.md:264 — `G3F-phase-105/105_04,05 | prefix compression, Delta-Laguerre, nodal flux/Bregman |
  DEAD [OTHER:Sturm and Hard…]`; :221 `P105 Nodal flux / Bregman resonance | PARTIAL`.
- 04_PHASES_100-189.md:32 — `W-jet | Nodal data at witness quartet | NO-GO` (the (★_cell) quantity is not
  polynomial in nodal data).
- 04_PHASES_100-189.md:853 — `G7B-R162_1501 | … Lemma D (Descartes) infinite sign changes | DEAD`.
- 04_PHASES_100-189.md:58 — `thm:KEPdich | Kreĭn extension problem indeterminacy | REF-D (coincide except
  λ_W=0) | indeterminacy ⇔ certificate`; :393 `G7F-155 thm:KEP3 | REF-D`; :622, :1035 (same); :864
  `G8B-R162_2201c | Node measure μ_F as determinate positive Krein extension | REF-D`.
- README.md:59, :387 — Hamburger: rigidity 𝔐={ζ} = R162_2601c, "RETRY without a new reason".
- README.md:426 — W1 PROVED (n₋ non-decreasing); :536 SPEC_004 N3 "block inertia"; 04_PHASES:59
  `inertia-nogo | n₋ = ∞ for T>½log2 | NO-GO`; :132 `R186-index | n₋=1 in the full form, scalar criterion =
  REF-D`.
- "Theorem P": phase 155, R155_051:8–9: Theorem P (λ_k(S_c) ≤ Λ_k(c), prolate floor, PROVED) and Cor P3
  (n₋(A_∞|P_T) ≤ 5/7/8 at ½log3/log2/0.80, PROVED).
- "Courant" and "Eremenko": **0 results** in the index. "Hurwitz" only appears as Kronecker–Hurwitz
  (README:61, :392), a different object. "oscillation": README:429 (BARRIER_X, tangent cone), which is not
  nodal.
- Phase 200: AUDIT_200_DCONS_001:73–81 (Theorem 3′; "The nodes of the minimizer … are functionals of h*, so
  REF-D applies. The nodes of an arbitrary g are not REF-D, but Theorem 3/3′ leaves them blind"). HORN_B_BIGSHARP_001:180–205
  (S1–S6). LEMMA_E_EPSTEIN_001:11 (Lemma E, PROVED). SPEC_SIGN_OBJECT_003:52 and _001:108, :286 (Mori extremal
  at ψ₀, ψ₄).

**New reason written out** to revisit the "Sturm/nodal" family, which is closed in README:36 and in G8D:
(a) The recorded attempts use Sturm as a *criterion* on a fixed finite truncation or on a PF kernel. Here it is
used as an *asymptotic integer invariant*, playing the role of h⁰ of a quadratic RR. That evades Theorem 3′,
which only kills exact identities.
(b) The chaining Courant × Sturm–Hurwitz (Eremenko–Novikov) does not appear in any record: 0 hits for Courant
and for Eremenko.
(c) The object is the block of the full form, not truncated A_∞.

If (a)–(c) do not survive the analysis below, the family closes with a new reason and is recorded. Descartes, PF
and Kreĭn have **no** new reason and are treated only in the inventory.

## 2. Cited facts (CITED), exact statements

**C1 (Sturm–Hurwitz).** Let f be real, 2π-periodic, continuous, with Fourier coefficients vanishing for
|k| < N. Then f has at least 2N sign changes in a period. (Sturm 1836; Hurwitz 1903; modern proof in
Pólya–Szegő, Aufgaben II; Katriel 2008.)

**C2 (Sturm, combinations of eigenfunctions).** Let L be a regular Sturm–Liouville operator on [a,b] with
eigenfunctions u_1, u_2, … (u_k with k−1 interior zeros). Every nonzero real combination Σ_{k=m}^{n} c_k u_k has
at least m−1 and at most n−1 zeros in (a,b). (Sturm 1836; rigorous reconstruction and survey in Bérard–Helffer,
"Sturm's theorem on zeros of linear combinations of eigenfunctions", Expo. Math. 2020.) Bérard–Helffer's remark:
in dimension ≥ 2 the lower bound fails (counterexamples by Arnold and Viro).

**C3 (Eremenko–Novikov 2004).** Let f be real and locally integrable on ℝ, f ≠ 0, with (distributional) Fourier
transform vanishing on (−a, a). Then the lower density of sign changes of f is ≥ a/π:
liminf_{R→∞} (1/2R)·#{sign changes in [−R,R]} ≥ a/π.
(A. Eremenko, D. Novikov, "Oscillation of Fourier integrals with a spectral gap", J. Math. Pures Appl. 83 (2004)
313–365; announcement in PNAS 101 (2004) 5841–5845.) It answers a question of Grinberg and is the ℝ-version of
C1. It is an *asymptotic* density bound. It does **not** give a bound on a fixed interval [−T,T]. For that one
needs a gap plus a growth or support hypothesis, and on a finite window there is no uniform version without
losses: a short interval may have no zero at all.

**C4 (Courant).** The k-th eigenfunction of a self-adjoint second-order elliptic Dirichlet problem has ≤ k nodal
domains. In 1D it is exact (k domains, by C2). **Courant needs a local second-order differential operator.** It
does not hold for general integral operators nor for abstract quadratic forms: there is no "index ⇒ ≤ nodes"
principle for Toeplitz or convolution forms (standard counterexamples: non-oscillatory kernels in the
Gantmacher–Kreĭn sense).

**C5 (Gantmacher–Kreĭn, oscillatory kernels).** If K is an oscillatory kernel (TP at every order, in the strict
sense), then its k-th eigenfunction has exactly k−1 zeros and the analogue of C2 holds. It is the only
substitute for Courant for integral operators. It needs total positivity.

**C6 (Slepian, prolate "miracle").** The time-band concentration operator Q_c = χ_{[−1,1]} 𝓕^{−1} χ_{[−c,c]} 𝓕
χ_{[−1,1]} commutes with the differential operator P_c = −(d/dx)(1−x²)(d/dx) + c²x². Hence ψ_k(c,·) has exactly
k zeros in (−1,1), and C2 and C4 hold for Q_c. (Slepian–Pollak 1961; Grünbaum, bispectrality.)

**C7 (Descartes–Laguerre for Dirichlet series).** Let D(s) = Σ a_N N^{−s} be absolutely convergent for
s > σ₀. Then the number of real zeros in (σ₀, ∞) is ≤ the number of sign changes of (a_N). (Laguerre;
Pólya–Szegő V.)

**C8 (Pólya frequency / Schoenberg).** A translation kernel is PF_∞ if and only if its Laplace transform is the
reciprocal of a Laguerre–Pólya function of type I. Variation diminishing holds for PF.

## 3. Task A — inventory of nodal counts with filter verdicts

Filters: S1 (do not define χ by the form), S2 (integer and sees (ℕ,+,·)), S3 (quadratic in E), S4 (lives in P_T,
compatible with the window), S5 (discontinuous in the comb; must fail for Epstein for a localizable reason),
S6 (feels Λ_cosh). Plus **Theorem 3′** (AUDIT_200_DCONS_001:73): an analytic χ in E is generic. A nodal count is
semialgebraic, not analytic, so 3′ does not kill it *in the asymptotics* (see §4.1).

| # | Count | Function | Depends on the comb? | S1 | S2 | S3 | S4 | S5 | S6 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Sturm–Hurwitz / Eremenko–Novikov over r = f̂|_{|ξ|>λ} | 𝓕^{−1}r | No: the gap is fixed by λ = e^T | ✓ | ✗ (integer, but does not see (ℕ,+,·)) | ✗ (linear in λ, not ½n²I_∞) | ✓ | ✗ comb-generic | ✗ | **NO-GO** (PROVED, Lemma N1) |
| A2 | Eremenko–Novikov over Ψ̌ = Σ_{N≥μ} c_N N^{−½} g(·−log N) + gauge | Ψ̌ | Yes (c_N) | ✓ | partial | ✗ | ✗ (Ψ̌ has no support in the window) | ? | ✗ | **NO-GO**: no gap, because 𝓕Ψ̌(t) = ĝ(t)D_μ(½+it) and D_μ(½) = ζ(½)M_μ(½) − 1 ≠ 0 generically. Without a gap, C3 gives nothing (PROVED, Lemma N2). |
| A3 | Sturm over Z r (aliasing datum) | Zr on (0,1/λ) | Yes (Z = comb) | ✓ | partial | ✗ | ✓ | ✓ in principle | ✗ | **NO-GO**: Zr lives on (0,1/λ), a bounded interval. C3 is asymptotic, and on a finite interval there is no lower bound of zeros without a spectral gap *of the restriction*, which does not exist because restricting destroys the gap. ARGUED. |
| A4 | Descartes on D_μ(s) = Σ_{N≥μ} c_N N^{−s} | real zeros of D_μ | Yes | ✓ | ✓ (sign changes of c_N = Σ_{m|N,m<μ} μ(m)) | ✗ | ✗ (real zeros at σ > 1; the form lives at σ = ½) | ✓ | ✗ | **DEAD with no new reason**: 04_PHASES:853 (R162_1501, Lemma D). Moreover C7 gives an *upper* bound of real zeros, while the form needs information on the critical line. No bridge. |
| A5 | Block Courant / index ↔ nodes | eigenvectors of W_T|_{P_T} | Yes | ✓ | ✓ | ✗ | ✓ | ? | ✓ (via prolates) | **Main candidate** (§4). Requires a commuting differential operator, or an oscillatory kernel C5. |
| A6 | Pólya frequency / TP / Gantmacher–Kreĭn | kernel of W_T | Yes | — | — | — | — | — | — | **DEAD**: README:36, G8D:395 (fails PF₂, arena ≥ 12 modes). C5 would act as Courant if the kernel were oscillatory, and it is not. No new reason. |
| A7 | Kreĭn: positivity ⟺ indeterminacy of the extension problem | — | — | ✗ (it is the form) | — | — | — | — | — | **REF-D** (04_PHASES:58, :393, :622, :1035; :864). Indeterminacy is not a count; its "index" κ (Pontryagin) is n₋ itself. Valid objective, not a new tool. |
| A8 | Hamburger / moments | — | — | — | — | — | — | — | — | **DEAD/REF-D** (README:387: RETRY without a new reason). |
| A9 | Nodes of the minimizer h* / Theorem X | h* | Yes | ✗ | — | — | ✓ | — | — | **REF-D** (AUDIT_200_DCONS_001:80–81; W-jet NO-GO 04_PHASES:32). |

**Lemma N1 (PROVED).** For every g ∈ P_T with representative f and r = f̂·1_{|ξ|>λ} ≠ 0, the lower density of
sign changes of 𝓕^{−1}r is ≥ λ/π. The same bound holds, word for word, for any measure in place of the comb:
Beurling, a_P, Epstein. *Proof.* C3 with a = λ. The function 𝓕^{−1}r does not contain the comb. ∎
Consequence: A1 violates S5. If an RR relied only on A1, it would give (W⁰) for Epstein, against Lemma E
(LEMMA_E_EPSTEIN_001:11).

**Lemma N2 (PROVED).** 𝓕Ψ̌(t) = ĝ(t)·D_μ(½+it) + gauge, with D_μ = ζM_μ − 1. If D_μ(½) ≠ 0 and ĝ(0) ≠ 0, then
𝓕Ψ̌ does not vanish near 0 and Ψ̌ has no gap. To have a gap on (−a,a) one would need ĝ = 0 on (−a,a). By
Paley–Wiener that is impossible for g ≠ 0 with compact support (ĝ is entire). *Proof.* thm:ext-half plus
analyticity. ∎
So **no function built linearly from a compactly-supported g has a spectral gap**, unless frequencies are cut by
hand, as in A1. And cutting frequencies by hand is comb-generic. This dichotomy, PROVED, is the backbone of the
NO-GO: *gap ⇒ the cut is exogenous to the comb; comb ⇒ no gap.*

## 4. Task B — main candidate: the "window Courant–Sturm theorem"

### 4.1 Why there is a gap (escape from Theorem 3′)

Theorem 3′ (AUDIT_200_DCONS_001:73–76) says χ_n is constant on a dense open set for each n, so the exact
identity χ_n = ½n²I_∞ + O(n) fails. A nodal count N(E) is also locally constant outside the discriminant
(multiple zeros form a semialgebraic set of codimension 1, ARGUED). 3′ applies equally to the exact identity.

There is a way out: an **asymptotic law**, N(E_n)/n² → ½I_∞(E,E), where the O(n) term absorbs local constancy.
This is how Weyl laws work: the count is integer and stepped, and the asymptotics is continuous. For nodal
counts this is genuine: by C2 and C6, in the prolate family with c = nT, the number of eigenvalues of Q_c greater
than ½ is (2/π)c + O(log c), and it coincides with the number of zeros of ψ_k at the threshold. **This is the
only point where the nodal family contributes something new relative to Theorem 3′. I mark it ARGUED.** But it
gives a *linear* law in c, not a quadratic one: it violates S3. For it to be quadratic one would need a
"surface", i.e., two-variable counts, and then C2 fails in dimension ≥ 2 (Bérard–Helffer, C2). **First wall: S3
against the dimension-1 nature of Sturm.**

### 4.2 Statement of the candidate

**Conjecture CS (window Courant–Sturm).** Let W_T be the self-adjoint operator on L²[−T,T] associated with the
full window form 𝔞_T restricted to P_T. Suppose:
(H1) there exists a regular Sturm–Liouville operator L_T on [−T,T] (possibly singular at ±T, like P_c) with
[L_T, W_T] = 0 and simple spectrum;
(H2) the map "k-th eigenfunction of L_T ↦ eigenvalue w_k of W_T" is monotone (compatible order).
Then n₋(W_T) = #{k : w_k < 0} = #{k : the eigenfunction with w_k < 0 has ≤ k zeros}. If in addition
(H3) (gap bound) every negative vector v of W_T satisfies 𝓕v = 0 on (−a,a) for some a > 0,
then Sturm (C2, lower bound) gives ≥ (2/π)aT zeros, and Courant gives ≤ n₋ zeros. Hence n₋ ≥ (2/π)aT. That is a
*lower* bound of n₋, in the opposite direction to what we are looking for.

**Honest reading.** The two integer inequalities are
- Courant: (index k) ⇒ (zeros ≤ k),
- Sturm/E–N: (gap a) ⇒ (zeros ≥ (2/π)aT).

Chained over the *same* vector they give (2/π)aT ≤ k, i.e., **gap ⇒ high index**. To *bound n₋ from above* one
would need every negative vector to have index ≥ something and, at the same time, few high-index vectors. Neither
theorem gives that information. **The objective's "opposition of directions" is apparent:** both inequalities say
"many zeros ⇔ high index" and are consistent, not contradictory. ARGUED, but it is pure logic on statements
C2–C4.

The only way to get a contradiction is an inequality of the form **"𝔞_T(v) < 0 ⇒ v has a gap (H3)"** together
with **"v negative ⇒ low index"**. Let us look at each.

### 4.3 Where negativity lives: at low frequency (PROVED via Theorem P)

Cor P3 of phase 155 (R155_051:9, PROVED): n₋(A_∞|P_T) ≤ 5/7/8 at ½log3/log2/0.80. The proof is the prolate
floor λ_k(S_c) ≤ Λ_k(c) (Theorem P, R155_051:8). Direct consequence:

**Lemma CS-1 (PROVED, rewriting of Cor P3).** In those windows, the negative subspace of A_∞|P_T is orthogonal
to the prolate tail {ψ_k : k ≥ K(T)}, with K = 6/8/9. In particular every negative vector is a combination of
ψ_0, …, ψ_{K−1}. By C2 it has at most K−1 zeros in (−T,T).

**Corollary CS-1′ (PROVED).** (H3) is *false* for A_∞: a negative vector is a finite combination of prolates,
its transform is entire and does not vanish on any interval. Hence it has no gap and Sturm/E–N gives no lower
bound at all. **Negativity lives in the low band, exactly where oscillation bounds from a gap are vacuous.**

For the full form 𝔞_T (with primes), R186-index (04_PHASES:132) gives n₋ = 1 in the full form without
restricting to P_T. Mori, at μ = 15, certifies n₋ = 0 in the block. The same logic holds: a negative vector, if
it exists, has energy concentrated at frequencies ≲ λ, because the archimedean term grows like log|ξ| (Λ_cosh)
and penalizes high frequency. This is ARGUED: it requires the prime block to be bounded in norm by O(√μ)
relative to the window, which AUDIT_13 of PROOF_L_SHARP_D gives as polynomial size (README:453).

### 4.4 Where would Λ enter? (H1) is the Λ step, and it probably fails

In Theorem CS, the only place where the comb can enter without being comb-generic is **(H1): the existence of a
differential operator commuting with the full form.**
- For A_∞ alone, C6 gives L = P_c (the Slepian miracle): Courant holds exactly. That is why Theorem P works with
  prolates.
- For 𝔞_T = A_∞ + (prime block) + pole: the prime block is Σ Λ(n)n^{−½}(τ_{log n} + τ_{−log n}) compressed to
  [−T,T], a sum of truncated translations. A local differential operator L commuting with τ_h compressed to
  [−T,T] and with Q_c at the same time is heavily overdetermined. Grünbaum's bispectral theory (CITED in spirit:
  concentration kernels admitting a commuting differential form rare families, tied to Duistermaat–Grünbaum
  bispectral equations) suggests none exists for T > ½log2, when the prime block is nontrivial. ARGUED.
- Substitute without a differential: C5 (oscillatory kernel). It requires TP, and TP fails (README:36, fails
  PF₂). DEAD.

**Lemma CS-0 (OPEN, first exact lemma; §5).** For T > ½log2, the only order-≤2 differential operator on
(−T,T) commuting with W_T is a multiple of the identity.

If CS-0 is true, Courant does not apply to the form with primes. The Courant–Sturm route is reduced to A_∞,
which is comb-generic, and falls as NO-GO PROVED: it fails S5, because A_∞ is the same for ζ and for Epstein
with the same Γ-factor.

If CS-0 is false, i.e., if a commuting L_T exists, that would be a new object of enormous interest (an
"arithmetic prolate"). Its spectrum would be integer in the C2 sense (index = zeros) and would indeed satisfy S2
(sees the comb) and S4. **That is the only live branch.**

### 4.5 Falsifiers

- **Epstein (Lemma E, LEMMA_E_EPSTEIN_001:11).** The window form of x²+5y² is negative in P_T for T ≥ 1.59,
  PROVED certificate. Any Courant–Sturm chain using only (C2, C3, C6, A_∞) gives the same conclusion for
  Epstein. Since there the conclusion is false, the chain must break at a step that uses ζ's comb. By §4.2–4.4
  the only candidate step is (H1). With Epstein, the "prime" block is Σ a_Q(n) n^{−½} τ_{±log n}, with a_Q of
  variable sign. If (H1) held for ζ and not for Epstein, the chain would fail for a localizable reason: existence
  or not of L_T. That satisfies S5 *formally*. But there is no mechanism in sight by which the existence of a
  commuting differential depends on Λ ≥ 0 rather than a_Q. Commutation is a *linear* condition in the comb's
  coefficients, so it is comb-generic in the linear sense: if it commutes for Λ and for a_Q, it commutes for any
  combination. **If (H1) holds, it holds on a linear subspace of combs.** Lemma E, together with a dichotomy
  "subspace closed under cΛ" (Thm 4.1 of PROOF_L_SHARP_D, README:453: Sonin invariant under Λ ↦ cΛ), suggests
  that (H1) would give positivity also for cΛ, c > 1, which has a certified λ^W < 0. **Contradiction ⇒ either
  (H1) fails for Λ, or (H2)/(H3) fail.** ARGUED, and it is the class falsifier: **cΛ (c > 1)** kills every
  version of CS in which Λ enters only via linear commutation.
- **Scaled F-DH combs (Davenport–Heilbronn, README:440).** Same argument.

### 4.6 Test on Mori μ = 15

Extremal f* = 1.106ψ₀ − 1.822ψ₄ (SPEC_SIGN_OBJECT_003:52; _001:286: a₄/a₀ = −1.6466). By C2 and C6 (combination
of P_c eigenfunctions with indices 0 and 4), f* has between 0 and 4 zeros in (−T,T). It is even, so it has 0, 2
or 4. Evaluate at 0: f*(0) = ψ₀(0)(1.106 − 1.822·0.6073) = ψ₀(0)(1.106 − 1.1065) ≈ 0, because
r = ψ₄(0)/ψ₀(0) = 0.6073 (SPEC_003:52). **f* has a zero at the origin (even order by symmetry, and almost
exactly double).** This is consistent with the extremal's design (which vanishes at 0, with boundary contact
ℓ(f*) ≈ d₄‖f*‖²/(1+r²)). The exact count, 2 or 4 zeros, remains a pending NUMERICAL question: it is not computed
in this round because it decides nothing. What it does decide is that n₋ = 0 in Mori's certified block and that
f* has ≤ 4 zeros: **low-index count with low nodes. No tension with Sturm/E–N; the test is vacuous.** Gap
λ = √15 ≈ 3.87: f* has no gap (finite combination of prolates, CS-1′), so C3 does not apply.

### 4.7 Lemma E: how does the chain break at the negative witness?

Epstein's witness is F = G(t/T), with G a degree-56 polynomial. F is a polynomial on [−T,T], with at most 56
zeros. Its effective prolate index is ≈ 56, and its transform is entire, with no gap. The Courant–Sturm chain
applied to the witness says: "F is negative and has ≤ 56 zeros." There is no contradiction with anything:
neither Sturm nor E–N demand zeros without a gap. **The chain does not break at Lemma E: it never gets to speak
on the matter.** That is the class diagnosis: oscillation counts are mute in the regime of negativity.

### 4.8 Sturm-type inequality over (★★)

(★★): 𝒜[Zr] + 2AB − 2⟨Zr, Z_log r⟩ ≥ κμ^{−A}dist²(r, 𝒢̄).

- 𝒜[Zr] (archimedean plus the death term ∫|Ψ|²κ_a, correction E_001, README:452) is a form of H^{½}·log type:
  with Λ_cosh it grows like log|ξ|. A Sobolev-type norm **does control oscillations from above**: if Zr has N
  well-separated sign changes in (0,1/λ), then 𝒜[Zr] ≳ log N · ‖Zr‖² (ARGUED, standard: each oscillation of
  scale δ costs log(1/δ) in H^{½}). This is the "every oscillation costs" inequality.
- ⟨Zr, Z_log r⟩ only gains if Zr is in phase with the comb weighted by log n, i.e., if r concentrates near the
  truncation nodes ξ = nλ (semiring, README:452: "all the value is truncation defect at n ≈ λ/u").
- For the inequality "oscillation costs, the comb only pays if there is resonance" to give (★★), a bound on the
  resonant gain from oscillations is needed: |⟨Zr, Z_log r⟩| ≤ (1−ε)·𝒜[Zr] + C·dist-error. But the term
  ⟨Zr, Z_log r⟩ is a Toeplitz form with symbol Σ Λ(n) log n n^{−½}cos(ξ log n), and its size in the resonant band
  is ~ log λ. It is of the same order as 𝒜. **The comparison is one of constants, not of counts**: the number of
  oscillations appears as log N on both sides and cancels. The count adds nothing to the form; it is REF-D in the
  sense of AUDIT_SPEC_001:47 (P7). ARGUED.

## 5. Task C — ranking and first lemma

| Rank | Route | Status | Cost | Prob. of contributing to D |
|---|---|---|---|---|
| 1 | **CS-0** (differential commutant of W_T; "arithmetic prolate") | OPEN, new (0 hits for Courant, Grünbaum or bispectral in the index) | low: commutator algebra with truncated translations | very low; its value is closing the family with a proof |
| 2 | Two-variable nodal asymptotic law (escape from 3′, §4.1) | ARGUED; clashes with S3 against Bérard–Helffer (dim ≥ 2) | medium | very low |
| 3 | "Oscillation costs" in (★★) (§4.8) | REF-D (constants, not counts) | — | zero as a count |
| — | A1, A2, A3 | NO-GO (Lemmas N1, N2 PROVED; A3 ARGUED) | — | — |
| — | Descartes, PF, Kreĭn, Hamburger, nodes of h* | DEAD/REF-D in the index, no new reason | — | — |

**First exact lemma (CS-0, statement for construction).** Let T > ½log2. Let W_T be the operator on
L²(−T,T) of the form 𝔞_T: W_T = A_∞ − Σ_{2≤n≤e^{2T}} Λ(n)n^{−½} P(τ_{log n} + τ_{−log n})P + (pole, finite
rank), with P the restriction to (−T,T). Let L = −(d/dx)p(x)(d/dx) + q(x), with p, q analytic on (−T,T) and
p ≥ 0. Statement: if [L, W_T] = 0 on a common dense domain, then p ≡ 0 and q ≡ const.

*Proof strategy.*
(i) [L, Pτ_hP] = 0 for h ∈ (0,2T): the kernel of Pτ_hP is δ(x−y−h)1_{(−T,T)²}. Commuting with L forces
p(x) = p(x−h) and q(x) = q(x−h) on the overlap, plus conditions at the boundary jumps x = −T+h and x = T−h. The
jumps give p(T−h) = p(−T+h) = 0 (ARGUED).
(ii) With two incommensurable translations h₁ = log2 and h₂ = log3 (T > ½log3 so both are in the window), the
double periodicity with irrational period forces p and q constant in the central part, and the boundary zeros
force p ≡ 0.
(iii) But the commutation is with the *sum* W_T, not with each term. One must separate scales by their
singularity: the A_∞ term is a pseudodifferential operator (kernel with a log singularity on the diagonal), and
the τ_h have δ singularity off the diagonal at x−y = ±h. Commuting with L (local), the singularities on the
lines x−y = h separate from the diagonal. Hence [L, Pτ_hP] = 0 *for each h separately*, as long as Λ(n) ≠ 0.
That is the only use of Λ: support, not sign.
(iv) Conclusion: CS-0 holds for T > ½log3. In ½log2 < T ≤ ½log3 there is only h = log2 and the boundary needs
separate treatment.

Expected label: **PROVED is attainable** (it is singularity analysis of kernels, with no arithmetic).
Consequence if proved: **NO-GO PROVED for the window Courant–Sturm family for T > ½log3.** Courant (C4) does not
apply to W_T; the only substitute is C5 (oscillatory), which is DEAD (fails PF₂). What remains of the nodal
family is comb-generic (Lemma N1) or lacks a gap (Lemma N2).

**Risk.** High: the route produces no sign with probability ≈ 1. Its usefulness is to close, by proof (not by
intuition), a family marked as "Sturm/nodal" (README:36), with a new and localizable reason: no local arithmetic
prolate exists. An honest warning: (iii) uses that the τ_h appear with nonzero coefficients. That holds also for
Epstein and for cΛ, so the NO-GO is a class result (support of the comb) and does not depend on the sign of Λ.
Consistent with S5: the family dies *before* reaching the point where the sign would be needed.

## 6. Conclusion and annotations

- **Class NO-GO (ARGUED; Lemmas N1, N2, CS-1, CS-1′ PROVED):** oscillation counts cannot serve as h⁰ for the
  window form. There are four reasons. (a) Gap ⇒ exogenous cut ⇒ comb-generic (N1); comb ⇒ no gap (N2,
  Paley–Wiener). (b) Negativity lives at low frequency (CS-1, Theorem P), where oscillation bounds are vacuous.
  (c) Courant and Sturm point in the same direction ("zeros ⇔ index"), so there is no contradiction to chain.
  (d) Courant on the block needs a commuting differential, and its existence (CS-0, OPEN, with a sketched proof)
  is false with at least one translation in the window.
- Genuine escape from Theorem 3′: asymptotic nodal laws. Recorded, but linear (dim 1) against S3.
- Mori μ = 15: f* has a (nearly double) zero at 0 and ≤ 4 zeros. Vacuous test (no gap). Lemma E: the chain does
  not speak (degree-56 polynomial witness, no gap).
- Nothing goes to P46 this round. If CS-0 is proved, it may enter as a class observation in P46's barrier
  section (a tool, not a closure).
- **For the index** (record in ROUTES-TRIED-INDEX/README.md, phase 200 section): "SPEC_SIGN_OBJECT_011
  (round 23): nodal/oscillation counts as h⁰ — class NO-GO (N1 comb-generic via Eremenko–Novikov; N2 no gap via
  Paley–Wiener; CS-1 negativity in the low band via Theorem P; Courant×Sturm do not oppose). Residue: CS-0 (no
  2nd-order differential exists commuting with W_T for T > ½log3; OPEN, proof by singularities sketched). Do not
  retry: Sturm–Hurwitz/E–N over r, Ψ̌ or Zr; Descartes on D_μ; block Courant without CS-0." (This synthesizer
  only writes this file; the annotation remains pending.)

Row D: OPEN.
