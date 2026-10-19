# CA_M_001 — The prime-sited form: exact Chen-type shift identity, parity split, invisibility of integrality, and the exact mechanism of the anti-diamagnetic reversal (seeds M1, M2, M3, M5, M6, M7, M8)

Phase 193. Pen and paper; **no numerics run**. Notation: CA_M_000 §Setting.
**No sign contact. No certified negative value for ζ.**

## 1. The exact prime-sited form (M1)
Let s be supported on odd primes ≤ M (site 2 adds only finitely many boundary terms and is dropped; Thm 3.1 shows nothing is lost).
Put u_N := (s ∗ v)(N) = Σ_{p′q^a = N} s_{p′}v_{q^a} (q prime, a ≥ 1), a function supported on {p′q^a}, all with Ω(N) ≥ 2.

**Proposition 1.1 (PROVED).** Q(s) = Arch(s) − Near(s), with
 (a) Arch(s) = (1/2π)∫ m ĉ₀ |Σ_p s_p p^{iτ}|² dτ = Σ s_ps_{p′}α(log(p/p′)), with α̂ = mĉ₀ negative near τ = 0, so Arch is indefinite (CA_K_001 Prop 1.3(a));
 (b) Near(s) = Σ_p s_p Σ_N u_N c₀(log(N/p)) = Σ_{(p,p′,q,a): |log(q^ap′/p)| < 2T₀} s_ps_{p′}v_{q^a}c₀(log(q^ap′/p)); only p′ < p occurs;
 (c) **shift form:** Near(s) = Σ_{h∈ℤ} C_s(h), C_s(h) := Σ_{p − N = h} s_p u_N c₀(log(1 − h/p)), h ranging over (p(1 − e^{2T₀}), p(1 − e^{−2T₀})).
*Proof.* (a),(b): prop:AM(ii)–(iii) restricted to prime sites; Div ≡ 0 (CA_K_002 Cor 3.3(i)); N = p′q^a ≥ 2p′ and N < pe^{2T₀} < 2p force p′ < p;
N ≠ p since Ω(N) ≥ 2. (c) group the terms of (b) by h := p − N. ∎

**Combinatorics (exact, not estimates).** For s = indicator-type weights, C_s(h) is a weighted count of primes p with p − h ∈ {p′q^a}:
for a = 1 it is the correlation of the primes with the semiprimes P₂ = p′q at shift h — the object of **Chen's theorem** (p + 2 = P₂)
— and Near is the sum of these Chen correlations over **all** shifts |h| ≲ 2T₀p with the weight c₀(log(1 − h/p)). The terms a ≥ 2 are
correlations of primes with p′·(prime power). What Near does **not** contain: no prime–prime correlation at fixed shift (N is never prime:
no twin-prime / Hardy–Littlewood pair count p, p + h), no additive representation p + p′ (no Goldbach), no k-tuple with k ≥ 3. The
k-tuple structure enters only as the binary linear-form pair (x, q·x + h) with x = p′ prime and q·x + h prime, summed over q and h:
Hardy–Littlewood for the pair of forms (x, qx + h), first moment in h.

**1.2 Parity and residues (M2; PROVED).** For odd sites p, p′: h ≡ 1 − N (mod 2), and N is even iff q = 2. Hence
 Near(s) = Near^{h odd}(s) + Near^{h even}(s), Near^{h odd} = Near_{q=2} := Σ_a v_{2^a} Σ s_ps_{p′}c₀(log(2^ap′/p)) exactly.
For a prime ℓ: the terms with q = ℓ are exactly those with N ≡ 0 (mod ℓ), i.e. h ≡ p (mod ℓ). So every residue split of the shifts is a
re-indexing of the comb-prime decomposition Near = Σ_q Near_q, which is linear in Λ (H-anat, CA_H_002 Thm 3.2).
**Each Near_q is indefinite** (PROVED): Near_q = ½s^T(D_q + D_q^T)s with (D_q)_{pp′} = Σ_a v_{q^a}c₀(log(q^ap′/p)), zero diagonal (c₀(log q^a) = 0),
so trace 0, nonzero for M large; a nonzero trace-zero symmetric matrix is indefinite. So the parity fact "p − 2p′ is odd" isolates a
trace-zero piece; it constrains no sign. Same for every residue fact. NO-GO for parity/residue splits (PROVED).

**1.3 Resolution (M5; PROVED as a count).** The weight c₀(log(1 − h/p)) varies in h at scale ≍ T₀p (c₀ ∈ C², supported in (−2T₀,2T₀)).
The bounded-shift part |h| ≤ H of the window (the only part where twin/Chen/singular-series information is resolved) is a fraction
≤ H/((1 − e^{−2T₀})p) of the h-range at site p. Sharp form in the decisive class: Prop 3.3.

**1.4 Additive Fourier picture (M7; ARGUED).** Writing Near through Σ_h C_s(h) = ∫_0^1 S_s(θ) \overline{U(θ)}·(weight) dθ, the h-weight has
additive transform concentrated at |θ| ≲ 1/(T₀p), decaying like (T₀pθ)^{−4} (ĉ₀ = F̂₀² ≍ τ^{−4}). The major arcs a/r with r ≥ 2 (which carry
parity, residue classes, the singular series) enter with weight O((T₀p/r)^{−4}): only the arc θ ≈ 0, i.e. PNT-type counts in multiplicative
windows of relative width T₀, has non-negligible weight. ARGUED (the weight depends on p as well as h; §3 gives the PROVED version).


## 3. Integrality is invisible to the target (M3, M8) — main result
**Theorem 3.1 (real-sited independence; PROVED).** Let X = {x₁ < x₂ < …} ⊂ (1,∞) be any discrete set (not necessarily integers) with
x_{k+1}/x_k → 1. Then (eq:target) ⟺ [𝖡(log x − log x′)]_{x,x′∈F} ⪰ 0 for every finite F ⊂ X.
*Proof.* Verbatim CA_K_002 Thm 3.2 / P47 prop:AM(i): (⇒) is thm:oneprofile restricted to the points log x; (⇐) choose x_j ∈ X with
|log x_j − C − d_j| < ε (possible for C large since log X has gaps → 0), use continuity of 𝖡 and thm:oneprofile. Integrality is never used. ∎

**Corollary 3.2 (integrality, parity, residues and k-tuple structure of p − np′ are information-free; PROVED).** Let θ: primes → (0,1) be
arbitrary and X_θ := {p + θ_p}. Then [prime-sited matrices ⪰ 0 ∀M] ⟺ (eq:target) ⟺ [X_θ-sited matrices ⪰ 0 ∀M]. Choosing the θ_p
ℚ-linearly independent irrationals, no difference x − n·x′ (x, x′ ∈ X_θ, n ∈ ℕ) is an integer, and parity, residues mod ℓ, singular series,
Chen switching, sieve weights and the parity phenomenon are undefined on X_θ. Hence **the truth value of the prime-sited problem is the same
as on a site set on which none of these structures exists.** Entrywise the two matrices differ by ≤ Lip(𝖡)·max|log(1 + θ_p/p)| ≤ Lip(𝖡)/p_min
(𝖡 is Lipschitz: α is smooth, Ξ is a locally finite sum of translates of c₀ ∈ C² with uniformly bounded local count of n per unit
of log n ... per window, since v_n c₀ terms with |log n − D| < 2T₀ are finitely many for each D; Lip on compacta suffices for the proof).

**Proposition 3.3 (the decisive class has unbounded shifts; PROVED).** In the (⇐) construction with prime sites p_j ∈ (e^{C+d_j−ε}, e^{C+d_j+ε}),
the pairs (j,k) contribute to Near only through prime powers n with |log n − (d_j − d_k)| < 2T₀ + 2ε — a finite set independent of C — and
for each such n, |p_j − np_k| ≥ p_k(|e^{d_j−d_k} − n| − O(ε)) → ∞ as C → ∞ unless d_j − d_k = log n. In the exact case d_j − d_k = log n the
contribution tends to v_nc₀(0) = v_n whether or not p_j − np_k stays bounded. Hence twin-prime-like / Chen configurations with bounded shift
carry no weight in the limit forms Σs_js_k𝖡(d_j − d_k) that decide (eq:target).
*Proof.* p_j/p_k → e^{d_j−d_k} up to e^{±2ε}; c₀(log(np_k/p_j)) ≠ 0 needs |log n − log(p_j/p_k)| < 2T₀; continuity of c₀. ∎

**Reading (PRINCIPIO RECTOR; answer to the front's question).** The relation "p − n·p′ small" looks like a +/· object (the + of the difference
meets the · of n·p′), but the form sees only the real number log p − log p′ − log n at resolution 2T₀. The + side of that relation (the
integer h = p − np′) is invisible (Cor 3.2), and the bounded-h regime has zero weight in the decisive class (Prop 3.3). **The prime-sited
problem contains no arithmetic of the sites beyond p_{k+1}/p_k → 1 (PNT)**; all arithmetic is in Ξ (the comb {log n} with weights v_n),
i.e. in 𝖡 itself. In particular (M8) the observation "Beurling has no addition, so p − np′ is undefined there" does not separate ζ from O11:
the target is already independent of whether p − np′ is defined. The genuine +/· locus remains the one CA_H_002 found: the positions log n
of the comb (the successor structure (S⁺) of ℕ), which is site-free.

## 4. The anti-diamagnetic reversal: exact mechanism (M6)
K-D2 / K-A: α alone is not PD because its Bochner density w = mĉ₀/2π is negative near τ = 0 (m(0) = C₀ = ψ(¼) − log π < 0); with the comb,
𝖡 = α − ½Ξ is PD (premise). The primes "raise the bottom". Mechanism:

**Proposition 4.1 (the comb's continued symbol is the negative of the archimedean density; PROVED from the FE alone).** For real τ with
ζ(½+iτ) ≠ 0: m(τ) + 2Re(ζ′/ζ)(½+iτ) = 0. In particular C₀ = −2ζ′/ζ(½) (ζ(½) ≠ 0, CITED).
*Proof.* ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s) is real on Re s = ½ (FE + reality), so d/dτ ξ(½+iτ) = iξ′(½+iτ) is real and Re(ξ′/ξ)(½+iτ) = 0.
ξ′/ξ = 1/s + 1/(s−1) − ½log π + ½ψ(s/2) + ζ′/ζ, and Re[1/s + 1/(s−1)] = ½/(¼+τ²) − ½/(¼+τ²) = 0 on the line; ×2 and eq:m. ∎
(Corpus: the τ = 0 case is phase-159 G2_B1_R1 Lemma 2 and phase-188 L2_BUILD_010 §1, there via the Hadamard product; the proof above uses
only the FE and is valid for every τ.) Formally Σ_n v_n cos(τ log n) "=" −2Re(ζ′/ζ)(½+iτ), so the bracket m − Σv_n cos(τlog n) of prop:AM(ii)
has continued value **0** at every non-ordinate τ.

**Corollary 4.2 (the reversal is exact cancellation, with zero slack; PROVED as an identity, ARGUED as a route classification).**
(i) Anti-diamagnetism is not a surplus: the comb's (continued) symbol cancels the archimedean density exactly, in particular the
negative value C₀ at τ = 0; nothing is left at the absolutely continuous level. (ii) Hence any argument that proves Arch ≥ Near on
prime-sited tests through a comparison of a.c. symbol densities (pointwise in τ, under any regularization compatible with analytic
continuation) ends at 0 ≥ 0: the positivity of 𝖡 is not a density inequality. What carries it is not an a.c. density on the τ-line,
and its description is the zero side ((R)(4), excluded). (iii) Prop 4.1 uses only the FE and reality: it holds verbatim for every FE-class
L-function (O10, O12 survive). The reversal is FE-generic and is not a ζ-specific sign mechanism.

**Proposition 4.3 (what the near-coincidences must pay on prime sites; necessary, under the premise; ARGUED).** Fejér tests on prime
sites (s_j = K^{−½} at p_j ≈ e^{C+jδ}, L = Kδ) give Q(s) → Σ_{|r|<K}(1 − |r|/K)𝖡(rδ); in the Riemann-sum regime the archimedean part tends to
δ^{−1}∫α = δ^{−1}C₀ĉ₀(0) < 0, so the premise forces limsup_L ∫_0^L (1 − D/L)Ξ(D)dD ≤ C₀ĉ₀(0): **on average over log-distance, the
near-coincidences p ≈ np′ must contribute exactly the regularized centre value Σv_n "=" C₀**, Cesàro-summed. This is a one-sided smoothing
statement on Ξ (P47 Thm Z class): REF-D. Not computed (not strictly necessary).

## 5. Screens
| item | REF-D | (B″) | O7/O10/O11/O12 | (R) | PR | sign content |
|---|---|---|---|---|---|---|
| Prop 1.1 | exact restatement | any comb | survive | — | + and · both present, but see Cor 3.2 | none |
| 1.2 parity/residues | — | any comb | survive | (R)(3) linear in Λ | + mod ℓ = comb-prime index | NO-GO (trace zero) |
| Thm 3.1 / Cor 3.2 / Prop 3.3 | exact restatement | any comb (Beurling incl.) | survive | — | **removes the + of p − np′** | NO-GO for every site-arithmetic route (information-free, PROVED) |
| Prop 4.1 / Cor 4.2 | (ii) → zero side | — | O10/O12 survive (FE only) | (R)(4) | none | none: exact cancellation, zero slack |
| Prop 4.3 | Thm Z class | any comb | survive | — | — | necessary only |

## 6. Self-review
1. *Does Cor 3.2 forbid using primes as sites in a proof?* No. It shows the truth value is the same on X_θ; a proof may use prime sites as a
   convenience, but any fact about integers p − np′ it uses is not needed for the conclusion, which is the PD of the site-free 𝖡. Stated as
   "information-free", not as an impossibility theorem for all logic.
2. *Finite M.* For one fixed M, the prime-sited matrix is a different matrix from the X_θ one (entries differ by ≤ Lip/p_min). Only the
   ∀M statement is site-invariant. A route proving finite-M statements by induction on primes would still have to land on 𝖡 PD.
3. *Lipschitz claim in Cor 3.2* is cosmetic (the equivalence uses only continuity); flagged ARGUED for the explicit constant.
4. *Prop 4.1* uses ξ real on the line; standard (CITED: FE, Γ reflection). It is a statement about meromorphic continuation, not about
   the window form; the passage "continued symbol = bracket of prop:AM(ii)" is formal (Σv_n cos(τ log n) does not converge on the line):
   hence Cor 4.2(ii) is ARGUED as a route classification. No zero location is used;
5. *Prop 4.3* uses ∫α = C₀ĉ₀(0) (α ∈ L¹ with α̂ continuous: ARGUED) and a Riemann-sum limit (ARGUED). Necessary condition only.
6. *Twin primes / Goldbach.* Not encoded (Prop 1.1 combinatorics). Chen correlations are encoded as an exact sum over all shifts, but by
   Prop 3.3 the bounded shifts carry no weight in the decisive class.
**Verdict.** M1: exact identity (PROVED), no sign. M2: NO-GO (trace zero). M3/M8: PROVED that the site arithmetic is information-free; the +
of p − np′ is not a +/· object of the target. M5/M7: DISCARD (resolution; PROVED in decisive class). M6: reversal = FE cancellation with
zero slack (PROVED identity), FE-generic; no sign mechanism.
