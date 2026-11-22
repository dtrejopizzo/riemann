# R162_703 — Route D3: the per-window converse from the primitive form to the complete form

Route D3 of R160_010 / R160_020 Option 4 (never written before; R162_590 §2 item 2).

**Status.**
- §2 exact conditions: **PROVED** (a sharpening of thm:parityschur(c) and prop:polarcap across windows).
- §3 at T₀ = ½log5: **PROVED (certified, Arb ball arithmetic)**: λ_W(T₀) ≥ 10⁻¹⁸. This gives an
  unconditional complete-form result beyond Zhu's T ≤ 0.8. It is a certificate, not a mechanism.
- §4 structural part: **NO-GO**. A Type II first contact cannot be excluded using the minimality of T_*,
  so Gate 1 does not reduce to Type I. Type II is the case in which 0 is not in the spectrum, which is
  the generic case. Minimality holds verbatim in the deletion model, where the complete-form contact
  comes strictly before the primitive one (F3).

No sign mechanism is claimed.

Notation is Paper 46 §parityschur and R162_504:
- A_T^par is the operator of a_T on the whole parity sector L²_par(I_T).
- φ_ev = cosh(t/2), φ_odd = sinh(t/2), ℓ_par = ⟨·,φ_par⟩, ε_ev = +1, ε_odd = −1.
- Q^par = ker ℓ_par, and λ_par(T) = λ_min(A_T|P_T^par).
- h_par, g_par = a_T(h_par) + 2ε_par, and f_par(z) = ⟨(A^par − z)⁻¹φ_par, φ_par⟩.
- T_W = inf{T : λ_W(T) < 0} and T_* = inf{T : λ_A(T) < 0}. Both are +∞ under RH.

## 1. Corpus check

- thm:parityschur(c): if λ_A > 0, then λ_W ≥ 0 ⟺ g_ev ≥ 0 and g_odd ≥ 0.
- prop:polarcap: 𝔊_T = S^Sch + diag(2,−2), and the converse is the pair a_T(h_ev) ≥ −2, a_T(h_odd) ≥ 2.
- cor:convfail: the converse fails in the odd sector for a = Λ1_{n≥5} on [0.4608, 0.58].
- Phase 156 (the per-window converse is a 2×2 polar-capacity condition that fails in comb models) and
  R162_504 Prop 4.1 (resolvent form) are the same statements.
- New here: monotonicity of g_par in T (Lemma 2.1), the one-window reduction (Thm 2.2), the Perron
  sharpening in the odd sector (Prop 2.3), the certificate at ½log5 (§3), and the type/spectrum
  criterion together with the ordering T_W ≤ T_* (§4).

## 2. Exact conditions — PROVED

**Lemma 2.1 (g_par is nonincreasing).** On any interval where λ_par > 0, the function T ↦ g_par(T) is
nonincreasing.

*Proof.* By thm:parityschur(a3), g_par(T) = min{W_T(F) : F ∈ D_T^par, ℓ_par(F) = 1}.
- For T < T′, extension by zero maps D_T^par into D_{T′}^par.
- This map preserves ℓ_par, because φ_par is the same function restricted to the larger window.
- It preserves W, because the new contacts n with log n ∈ [2T, 2T′) have c_F(log n) = 0 when
  supp F ⊂ I_T. This is the argument of lem:monoT.

So the feasible set grows and the minimum does not increase. ∎

**Theorem 2.2 (one-window converse).** Suppose λ_A > 0 on (0,T₁]. Then:
1. λ_W ≥ 0 on (0,T₁] ⟺ g_ev(T₁) ≥ 0 and g_odd(T₁) ≥ 0.
2. λ_W > 0 on (0,T₁] ⟺ 𝔊_{T₁} ≻ 0.

In resolvent form, whenever 0 ∉ spec A^par_{T₁}, we have a_T(h_par) = 1/f_par(0), and:
- (ev) either μ₁^ev(T₁) > 0, in which case g_ev > 0 automatically; or μ₁^ev < 0, in which case
  g_ev ≥ 0 ⟺ f_ev(0) ≤ −½;
- (odd) g_odd ≥ 0 ⟺ 0 < f_odd(0) ≤ ½. This forces μ₁^odd(T₁) > 0.

*Proof.*
- (1)–(2): thm:parityschur(c) at T₁, together with the monotonicity of λ_W (cor:KEP08 proof) and
  Lemma 2.1.
- Resolvent form: h = A⁻¹φ/f(0) satisfies ℓ(h) = 1 and a(h,G) = ⟨φ,G⟩/f(0) = 0 on Q. So
  a(h) = 1/f(0).
- (ev) If μ₁ < 0, then f(0) < 0, because the zero of f on (μ₁, μ₂^ev) is λ_ev > 0 (R162_504 Prop 4.1).
  If μ₁ > 0, then f(0) = Σ⟨ψ_k,φ⟩²/μ_k > 0 and a(h) > 0.
- (odd) g_odd ≥ 0 means W_odd = A^odd − 2φφ* has nonnegative Schur value. With λ_odd > 0 this gives
  W_odd ≥ 0, hence A^odd ≥ 2φφ* ≥ 0, hence μ₁^odd ≥ 0. The value μ₁^odd = 0 is excluded by
  0 ∉ spec. Then f_odd(0) > 0, and a(h) = 1/f ≥ 2 ⟺ f ≤ ½. ∎

**Proposition 2.3 (Perron sharpening, odd sector).** Assume v_n ≥ 0, which covers ζ and every a ≥ 0.
Then λ_W,odd(T) ≥ 0 implies μ₂(A_T) ≥ 0 and f_odd(0) ≤ ½. So the odd converse is the single scalar
inequality ⟨(A_T^odd)⁻¹φ_odd, φ_odd⟩ ≤ ½ on a sector whose bottom lies above the second eigenvalue
(R162_504 Thm 2(a)).

Two cheap sufficient conditions fail:
- ‖φ_odd‖²/μ₁^odd ≤ ½ would require μ₁^odd ≥ 2(sinh T − T). At ½log5 this is 0.179, while
  μ₁^odd ≤ λ_odd ≈ 3·10⁻¹⁰.
- So no crude bound on the spectrum decides the converse. It is a statement about a resolvent value
  that must be tight to super-exponential precision (Theorem M).

## 3. The complete form at T₀ = ½log5 — PROVED (certified)

**Theorem 3.1.** At T₀ = ½log5 = 0.804719…:
- W_{T₀} ≥ 10⁻¹⁸ on L²_ev(I_{T₀});
- W_{T₀} ≥ 10⁻¹⁶ on L²_odd(I_{T₀}).

Hence λ_W(T₀) ≥ 10⁻¹⁸ > 0. By monotonicity, λ_W > 0 on (0, ½log5].

**Consequences.**
- 𝔊_{T₀} ≻ 0 and g_par(T₀) > 0 (Thm 2.2).
- By thm:KEP3(a), KEP(T) is indeterminate for every T ≤ ½log5. This extends cor:KEP08 from 0.8.
- The first complete-form zero satisfies T_W > ½log5 unconditionally.
- On [0.8, ½log5] the contact set is still {2,3,4}. So Zhu's range extends only through the window
  variable, not through a new prime.

*Method.* The method is R162_303 with one change: the parity border is absorbed exactly into an extra
variable ξ.
- Let b_μ be the certified lower form, a_T − μ ≥ b_μ, with frequency truncation at τ_N = 240, exact
  below τ_N. Put b(F,ξ) = b_μ(F) + 2ξℓ_par(F) + cξ² with c = −ε_par/2.
- Odd (c = +½): min_ξ b = b_μ − 2ℓ². So W_odd ≥ μ ⟸ n₋(b) = 0.
- Even (c = −½): b = b_μ + 2ℓ² − ½(ξ − 2ℓ)². So n₋(b) = n₋(b_μ + 2ℓ²) + 1, and W_ev ≥ μ ⟸ n₋(b) ≤ 1.
- The Y-elimination (K = 280, K₂ = 330, q_Y = 0.70079), the Gram/tail boxes and the quadrature bound
  are exactly those of R162_303 §§2–3. Only the ξξ entry changes: it becomes c − δ′ with
  δ′ ≥ ‖P_Yχ‖²/q_Y ≈ 10⁻¹⁹⁰. Lowering this entry preserves the direction of the inertia inequality.
- Odd sector: interval Cholesky of the full (E+ξ) matrix 𝖱 succeeds.
- Even sector: det B < 0 is certified, and the Haynsworth Schur complement S passes interval Cholesky.
  This is the path of R162_303 §3(c).

Precision is 640 bits; the maximum entry radius of 𝖱 is 4.4·10⁻⁴¹.

| sector | μ certified | min pivot | fails at (no claim) |
|---|---|---|---|
| even (W_ev) | 0, 10⁻²⁰, **10⁻¹⁸** | 4.47·10⁻⁴ | 10⁻¹⁶ |
| odd (W_odd) | 0, 10⁻²⁰, 10⁻¹⁸, **10⁻¹⁶** | 8.3·10⁻¹⁴ | 10⁻¹⁴ |

- The even bottom lies in [10⁻¹⁸, 10⁻¹⁶). This is consistent with Zhu's 8.9·10⁻¹⁸ at 0.8 and with
  λ_W ≤ λ_A.
- Compared with the primitive form, the complete form costs about six orders of magnitude, which is
  the polar capacity g_ev/‖h_ev‖² of thm:parityschur(a4).

**Files** (`scripts/c3/`):
- `d3_cert_W.py`: a diff of `c3_cert.py`, documented in its docstring.
- `d3W_log5_par{0,1}_tauN240_K280_N46.json`: the outputs.
- `d3W_run_par{0,1}.log`: the logs, about 400 s per parity.

**Audit.** A independent rerun is still needed, as R162_391 did for C3. The audit should check:
- the sign of c in each parity;
- the inertia bookkeeping for the even sector;
- that the certificate covers the full parity sector (E ⊕ Y = L²_par) and not only P_T.

## 4. Structure of first contacts — Type II is not excluded by minimality (NO-GO)

**Proposition 4.1 (type = spectrum).** Let F be a parity first-contact vector at T_*. Then:
- F is of Type I ⟺ 0 ∈ spec A^par_{T_*};
- F is of Type II ⟺ 0 ∉ spec A^par_{T_*} ⟺ f_par(0) = 0 with A^par invertible.

In the even sector this reads: Type I ⟺ μ₂^ev(T_*) = 0 = λ_ev(T_*), that is, equality in the
interlacing μ₁ < λ_ev ≤ μ₂^ev. Type II ⟺ μ₂^ev(T_*) > 0.

*Proof.*
- Type I (r = 0) makes F a 0-eigenvector of A^par, and F ⊥ ψ_T (R162_504 Thm 3). Then μ₂^ev ≤ 0 ≤ λ_ev ≤ μ₂^ev.
- Conversely, suppose 0 ∈ spec A^par with eigenvector E. The residue r = cφ satisfies c⟨φ,E⟩ = ⟨F,AE⟩ = 0.
  If c ≠ 0, then E ⊥ φ, so E ∈ Q is a primitive kernel vector with α(E) = 0. On span(E) the vector
  F − (projection) gives the same α. Since α is linear on 𝒩 and the kernel is spanned by vectors of
  either type, the statement is about the kernel. The clean statement is: α ≡ 0 on 𝒩 ⟺ 𝒩 ⊂ ker A^par.
  When 0 ∉ spec A^par, α ≢ 0 by Thm 3. ∎

**Theorem 4.2 (ordering of the two contacts).** Suppose RH fails. Then:
1. T_W ≤ T_*.
2. Type II at T_* ⟹ T_W < T_*, with λ_W < 0 on (T_W, T_*].
3. If T_W < T_*, then T_W is a *polar contact*: λ_A(T_W) > 0, some g_par(T_W) = 0, and the radical of
   W_{T_W} is spanned by h_par ∉ P_{T_W}.
4. If T_W = T_*, the contact at T_* satisfies the range condition in every degenerate sector, and
   𝔊_{T_*} ⪰ 0. By Prop 4.1 it is of Type I in every sector.

So ¬RH ⟹ (P) a polar contact at T_W < T_*, or (I₀) a Type I contact with T_W = T_*.

*Proof.*
- (1): λ_W ≤ λ_A.
- (2): Thm 3 of R162_504 gives λ_W(T_*) < 0. Then use continuity (lem:contT) and λ_W > 0 on (0, ½log5] (§3).
- (3): thm:parityschur(c) at T_W together with (a2).
- (4): λ_W(T_*) = 0 ≥ 0 and thm:parityschur(c). ∎

**What this means for Gate 1.** Excluding Type II is not a reduction step in its own right:
- The Type I condition 0 ∈ spec A^par_{T_*} is a coincidence of codimension two in a one-parameter
  family: an eigenvalue of the full sector reaches 0 at the same window where the compression does.
- Type II is the generic case. An argument that "excludes Type II" would have to force this
  coincidence.
- The statement that actually controls the dichotomy is the global D3 converse, "λ_A > 0 on (0,T] ⟹
  λ_W ≥ 0 on (0,T] for every T". It is equivalent to excluding (P), that is, to T_W = T_*.

**NO-GO (F3).** Take the deletion model a = Λ1_{n≥5}, with v_n ≥ 0.
- Every Perron input holds (R162_504 Thms 1–3).
- lem:contA, lem:monoT and the minimality of T_* hold verbatim.
- cor:convfail gives λ_W(a) < 0 on [0.4608, 0.58] while WP_T(a) holds strictly. So T_W(a) ≤ 0.4608 <
  0.58 ≤ T_*(a), which is case (P).

Therefore no argument that uses only minimality, continuity, the Perron ladder and a ≥ 0 can prove the
converse at T_* or exclude (P). The same holds for DH and Epstein, where the Perron ladder is lost as
well. A proof that Type II is impossible would additionally need the deletion contact at T_* ∈
[0.58, 0.60] to be of Type I. Its type is not certified here.

(O703.2) The deletion falsifier for the stronger claim "no Type II" becomes rigorous with one finite
certificate: μ₂^ev(Γ_{0.60}) > 0 for the archimedean operator. By Prop 4.1 and the monotonicity of μ₂^ev,
that certificate would show the deletion contact is of Type II. Not run: numerics only if needed, and
the NO-GO for the converse already stands without it.

## 5. Open residue

- (O703.1) Extend Theorem 3.1 to larger T in the same frame. The contact set {2,3,4,5} starts at
  ½log5, and the margin decays like exp(−e^{2T}) (Theorem M). This is value only, not a mechanism.
- (O703.2) The certificate described at the end of §4.
- (O703.3) The only ζ-specific scalar in D3 is f_par(0), the polar capacity. This coincides with
  O504.1: a sign-carrying input must act on ⟨(A^par)⁻¹φ,φ⟩ against the thresholds −½ (even) and +½
  (odd), and it must fail for Λ1_{n≥5}.

**Verdict for R162_590.** Add D3 to §1c with this entry:
- D3 exact conditions: g_par monotone, one-window form; this is a restatement of prop:polarcap.
- Certified λ_W(½log5) ≥ 10⁻¹⁸: M, value only.
- "Type II impossible by minimality": fails F3 (deletion model, T_W < T_*).
