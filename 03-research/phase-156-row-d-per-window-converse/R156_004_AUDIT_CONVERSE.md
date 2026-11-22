# R156.004 — Audit of 156c (`R156_001`, the per-window converse)

*Phase 156.*

**Object.** `R156_001_CONVERSE.md` (373 lines as delivered) and `scripts/r156/` (README and 8 scripts).

**Reference texts read (the paper's own definitions, rule `feedback-check-against-paper-definitions`).** Paper 46
`main.tex`:
* l.114–150: `eq:symbol`, `eq:form`, Tate moments, `\PT`, `eq:W`, `\lamA`, `\lamW`, the intro positivity sentence;
* l.268–312: related work, "What is not claimed";
* l.399–440: `thm:A`, `eq:Aform`, `eq:Kprim`, `rem:Kprim`;
* l.640–700: `thm:W`, `prop:P`, `lem:roughEF`;
* l.955–1000: `thm:C`;
* l.1585–1710: `lem:polar`, `thm:KEP1–3`, `cor:KEP08`;
* l.2348–2720: `\Ainf`, `\laminf`, `\laminfP`, `prop:arch`, `prop:nodes`, `lem:strict` and the paragraph after it,
  `cor:Tarch`, `lem:parity`, `thm:index`;
* l.2950–2990: the reduction chain;
* l.3154–3160: `cor:margin1`;
* l.3207–3378: `RD_T(a)`, `prop:finite`, `thm:finmod`, `prop:finsupp`, `cor:void`, `rem:twohalves`, `prop:uniform`;
* l.3525–3552: `thm:Al`, the OPEN paragraph.

Other texts read:
* Paper 42 `main.tex` l.4040–4065, 4164–4215, 4340–4360 (`thm:certifiedendpoints`, `rem:yoshidacalibration`,
  `cor:certifiedinitialinterval`);
* `P124_011` l.235–335;
* `R154_013` l.10, 20;
* `R155_023` l.50, 87, 328–329;
* `R155_031` l.51;
* `R155_061`, closing note;
* Paper 45: the `thm:sufficiency` label exists (l.1996).

**Compute done, strictly one script at a time.**
* Two new interval scripts: `scripts/r156/audit_r156_witness_t.py` (1.3 s) and
  `scripts/r156/audit_r156_theta_quintic.py` (1.1 s).
* Re-runs of its `r156_green_matrix.py` (`½log 3`, `N = 20` prime-free and `N = 24` with primes),
  `r156_inertia_check.py` and `r156_theta_family.py 16 0.9999 1 1.001`.
* One throw-away Galerkin evaluation of `‖h_-‖²` (for A2).

No paper was edited. Only `scripts/r156/README.md` was changed, by appending an audit section and making one fix.

**Verdict in one line.** The algebraic core survives intact: Lemma 1.0, Theorem 1.1(a)–(c), Remark 1.2 and Prop 2.1
are **correct**, and doubt 1 is closed with a self-contained argument (no restriction needed). Both load-bearing
witnesses **re-verify in interval arithmetic**, with the stated conclusions: `T^*_∞ ≤ 0.4608`, and `θ < 0.8148` at
`½log 3`. The sign `2AB = −2s²` for odd `F` is derived from `eq:W` and confirmed independently on the Fourier side.
There is **one FAIL as stated**, §5.1: "∃ certificate ⟺ KEP indeterminate" is not proved, and `thm:KEP3`(a) gives
only a sandwich. There are **fifteen further AMENDs** (A1–A11, A13–A16). They include one unsafe-direction rounding
(`−0.0061378`), one typo that inverted a sign reading (`κ_+ ≈ −2.0000001`), and a sandwich stated without its
hypothesis `g > 0`. They also include scope wording for the models: `W_T(a)` is **not** the zero sum of `ζ_a`. The
citation slip of doubt 6 is **confirmed**, and the precise ruling is below.

---

## Per-claim findings

### (i) Definitions against Paper 46 — PASS
`eq:W` (l.134–136) is `W_T = 𝔞_T + 2Re(AB̄)`. `def:W` (l.1152) is the weight class `𝒲_T`, so doubt 9 is confirmed and
every integration must cite `eq:W`. `\lamW ≤ \lamP ≤ \lamA` holds (`rem:Kprim` together with `thm:A`). Its
`𝒜_∞` equals P46 `\Ainf` (l.2358–2362). `RD_T(a)` is as at l.3210–3214.

P46 defines **no** complete form `W_T(a)` for a general comb. Its `λ^W_T(a)` is therefore a new definition,
`W_T(a) := 𝔞^{(v(a))}_T + 2Re(AB̄)`, which must be stated. This is part of A7.

### (ii) Lemma 1.0 (parity splitting) — PASS
Put `c = ⟨F,cosh(t/2)⟩` and `s = ⟨F,sinh(t/2)⟩`. Then `A = c + s` and `B = c − s`, since
`e^{±t/2} = cosh(t/2) ± sinh(t/2)`. So `2AB = 2c² − 2s²`, and `c` (resp. `s`) vanishes on odd (resp. even) `F`. The cross
term is `c(F_e)(−s(F_o)) + c(F_e)s(F_o) = 0`. This checks against the P46 parity paragraph (before `lem:strict`):
`A = B = c` for even `F`, and `A = −B = s` for odd `F`.

### (iii) Doubt 3: the sign `2AB = −2s²` for odd `F` — PASS (derived, and checked independently)
From `eq:W` and `prop:P` (the polar term is `2Φ_F(0)Φ_F(1) = 2AB` for real `F`): for odd real `F`,
`A = ∫F e^{t/2} = ∫F sinh(t/2) = s` and `B = ∫F e^{−t/2} = −s`. Hence `2AB = −2s²`. This is the negative square of
`lem:polar`.

An independent check bypasses the Lévy representation entirely. `audit_r156_witness_t.py` part (c) evaluates
`(2π)^{-1}∫ m|F̂|² + 2AB` at `F = t`, `T = ½log 3`, with `m = Re ψ(¼ + iτ/2) − log π`,
`|F̂|² = 4(sin x − x cos x)²/τ⁴` and `x = τT`, and gets `−0.026876865`. Its mpmath and Galerkin values are
`−0.0268768653`. This is DIAGNOSTIC (float64), but it rules out any `O(1)` convention error.

### (iv) Theorem 1.1(a) and doubt 1 (Lax–Milgram/Kato) — PASS; AMEND A1 (self-contained step, no restriction)
Its appeal to "Kato VI plus the spectral gap" is correct but compressed. A1 replaces it with a complete
argument, which I checked.
1. `𝔞_T = Γ_T + Π_T` with `‖Π_T‖ ≤ 𝐀` (P46, after `cor:Tarch`). So `𝔞_T` is closed, bounded below, and has the form
   domain of `Γ_T`, which embeds compactly (proof of `prop:nodes`(i)).
2. `Q = P^{par}` is form-closed. It is also dense in `ker ℓ ∩ L²_{par}`, by the one-line argument in A1. So `𝔞|Q` is a
   closed semibounded form with compact resolvent in that Hilbert space.
3. The negative spectral subspace `Q_-` is finite-dimensional.
4. If `0 ∉ spec`, then `𝔞 ≥ δ‖·‖²` on `Q_+`, which gives coercivity in the form norm with constant `δ/(δ+M+1)`.
   Lax–Milgram then applies on `Q_+`, and finite linear algebra on `Q_-`.
5. `G ↦ 𝔞(H_0,G)` is form-bounded because `H_0` lies in the form domain.

So no restriction of the statement is needed. In particular it does not need `thm:index`: the finiteness of the
negative index comes from the compact resolvent, and the statement holds at every `T`.

Items (1)–(4) of (a) check:
* (1): `W(h,G) = 𝔞(h,G) + 2εℓ(h)ℓ(G) = 0` on `Q`.
* (2): immediate.
* (3): a negative subspace of dimension `> dim Q_- + [g<0]` projects with nontrivial kernel onto the first summand,
  giving a nonzero vector in the `W ≥ 0` summand. This is valid in infinite dimension because the first summand is
  finite-dimensional. The radical statement uses `ker L = 0`.
* (4): `𝔞(G + h) = 𝔞(G) + 𝔞(h)`.

The headline "𝔞-orthogonal complement of `P_T` = `span(h_+, h_-)`" also holds. If `F = G_0 + xh_+ + yh_-` is
`𝔞`-orthogonal to `P_T`, then `𝔞(G_0,·) = 0` on `P_T`, so `G_0 ∈ ker L = 0`.

### (v) Theorem 1.1(a5), the sandwich — AMEND A2 (missing hypothesis)
The lower bound `λ^W ≥ ½min(λ_par, g/‖h‖²)` uses `‖G + xh‖² ≤ 2(‖G‖² + x²‖h‖²)` and needs `g > 0`. The "Hence …
`g/‖h‖² ≤ 2λ^W`" line was printed outside that hypothesis. It is **false** for `g < 0`, and there is a DIAGNOSTIC
counterexample. In the prime-free case at `½log 3`, odd sector, `N = 20`: `‖h_-‖² = 57.10`, `g_- = −20.078`, so
`g_-/‖h_-‖² = −0.352`, while `2λ^W_odd = −0.861` and `2λ^W < λ_odd` holds. The fix, applied, restricts the sandwich to
`λ_par > 0, g_par > 0`. Its only use (§2, for ζ at `½log 3`) has `g_+ > 0` by Zhu (Prop 4.1(ii)), so nothing
downstream breaks.

### (vi) Theorem 1.1(b), the degenerate case — PASS; AMEND A3 (the P124 identification)
The linear algebra is correct:
* `F_0 ∈ N` lies in the radical of `𝔞|Q` (Cauchy–Schwarz for a nonnegative form).
* A functional vanishing on `ker ℓ` is a multiple of `ℓ`.
* `W(F_0) = 0`, so `W(xF_0 + H)` is affine in `x` and unbounded below when `α(F_0)ℓ(H) ≠ 0`.
* If `α ≡ 0`, then `N` lies in the radical of `W^{par}`. `h` is unique modulo `N`, so `g` is well defined.

A3 makes two corrections to the wording.
* `Π_{ker}ρ = 0 ⟺ ρ ∈ Ran L^{1/2}` holds here only because the compact resolvent gives a gap above `0`. In general
  only `⟸` holds.
* The column `ρ(G) = 𝔞(H_0,G)` has the *same bordered shape* as P124's (4.4). But P124's column
  `ρ_{+,T} = P_T(e^{t/2}Φ_{+,T})` belongs to a different (collar) decomposition, and its identity with `ρ` is not
  shown. So "exactly the range condition of P124" becomes "a range condition of the same shape".

### (vii) Theorem 1.1(c) — PASS
* The inertia sum follows from Lemma 1.0 and (a3) per sector.
* `λ^W > 0 ⟺ λ^A > 0 ∧ g_± > 0`. Sufficiency is (a5) with `g > 0`. Necessity is `λ^W ≤ λ^A`, then
  `g = W(h) ≥ λ^W‖h‖²`.
* `λ^W ≥ 0 ⟺ RD_T ∧ range ∧ G ⪰ 0`. `⟹`: in each sector `λ_par > 0`, where (a3) applies, or `λ_par = 0`, where (b)
  forces the range condition. `⟸`: (a3) and (b).

Doubt 8 is correct: `S_T` (D.47's Green matrix, hyperbolic when `n_-(𝔞_T) = 1`) and `G_T = S_T + J` are different
matrices. No statement in P46, `R155_*` or `R156_*` conflates them. (Grep found no "Green matrix"/`G_T` usage in P46
other than the unrelated `G_T(t) = g(t/T)` of `prop:finsupp`, for which see A15.)

### (viii) Remark 1.2 and Prop 2.1 — PASS
The moment-coordinate matrix `G^{AB} = ¼[[g_++g_-, g_+−g_-],[g_+−g_-, g_++g_-]]` follows from `c = (A+B)/2` and
`s = (A−B)/2`, and `J^{AB} = [[0,1],[1,0]]` checks.

On the resolvent formula `g = 1/⟨W^{-1}φ,φ⟩`: `⟨W^{-1}φ,φ⟩ ≠ 0` is automatic under the nondegeneracy of `𝔞|P`. If it
were `0`, then `W^{-1}φ ∈ P` would lie in `ker(𝔞|P)`.

The Wiener–Hopf reading `𝒜h = 𝔞(h)φ_par` on `I_T` is correct, since `𝔞(h,·)` and `⟨φ_par,·⟩` both vanish on the other
parity. Prop 2.1 is (a4) scaled; for `x = 0` the infimum over `P` is `0`, attained. `Φ_F(0) = B` and `Φ_F(1) = A`
(`lem:roughEF`).

### (ix) §2 readings — AMEND A4
* The typo `S_T ≈ diag(−2.0000001, …)` would mean `κ_+ < −2`, i.e. `g_+ < 0`. That contradicts the reported
  `g_+ ≈ +8.6·10^{-8}`. The re-run `r156_green_matrix.py 0.5493061443 24` gives `κ_+ = −2.000000`,
  `g_+ = +8.697·10^{-8}`, `κ_- = +2.001353`. Corrected to `−1.99999991`.
* "Hyperbolic whenever `n_-(𝔞_T) = 1`" needs `𝔞_T` nondegenerate and `𝔞_T|P_T > 0`.
* The HEURISTIC `g_+/‖h_+‖² ≤ 2λ^W → 0` needs `2λ^W < λ^A`. But `cor:margin1` bounds `λ^A` itself by
  `4·10^9 T e^{−15.449T}`, so the premise is undecided at every `T ≥ 1`. This is noted, and the label stays HEURISTIC.
* Remark 2.2 (zero-side reading): PASS as a reading.

### (x) Theorem 3.1 and doubt 2 (rigour of the `t`-witness) — PASS; AMEND A5 (wording and rigour upgrade)
* **Closed forms.** `audit_r156_witness_t.py` (b) re-derives exactly: `c_F(u) = (2T−u)(2T²−2Tu−u²)/6`,
  `g = u(6T²−u²)/6`, `‖F‖² = 2T³/3`, `∫_0^{2T} g(1/u + ½) = 2T³(3T+7)/9`, `s = 4T cosh(T/2) − 8 sinh(T/2)`.
* **Bounds used.** `K ≤ 1/u + ½` holds for all `u > 0`, since `sinh x ≥ x` and `cosh ≥ 1`. It is used against
  `g ≥ 0` (Cauchy–Schwarz, `|c_F(u)| ≤ ‖F‖²`), so it bounds `𝔈` from **above**; the direction is correct.
  `∫_{2T}^∞ K = log coth(T/2) + π − 2arctan e^T` holds (primitives `log tanh(u/4)` and `2arctan e^{u/2}`).
  `C_0 = ψ(¼) − log π = −γ − π/2 − 3log 2 − log π` holds.
* **Interval values.** Outward rounding, 40 digits; `π − 2arctan e^T = 2arctan e^{−T}` is enclosed by the alternating
  series with a remainder term.
  * `U(0.461) ∈ [−3.593820147085192·10^{-5}, −3.593820147085191·10^{-5}]`;
  * `U(0.4608) ∈ −7.0159574772684·10^{-6} (±10^{-40})`;
  * `U(0.47) ∈ −1.404753027365·10^{-3}`;
  * `U(½log 3) ∈ −0.02005264397468545…`.
* **Conclusion.** `\laminf(T) < 0` for every `T ≥ 0.4608` (`prop:arch`(i): `\Ainf` is `T`-free and the feasible sets
  grow). So **`T^*_∞ ≤ 0.4608`, PROVED.** Its "`= −3.6·10^{-5}`" should read `−3.59·10^{-5}`.

**Wording (the requested check).** A PROVED `0.461` is *numerically weaker* than P46's DIAGNOSTIC
`0.3716`, but it is a proof. The right comparison is with P46's *proved* bound, `T^*_∞ ≤ T^*_{∞,P} ≤ 0.60`
(`prop:arch`(iv), `cor:Tarch`). Thm 3.1 improves that to `0.4608`. Its real content is the certified strict separation
`T^*_∞ ≤ 0.4608 < 0.58 ≤ T^*_{∞,P}`. Its sentence ("where P46 records only the DIAGNOSTIC `≤ 0.3716`") is
true but invites the misreading "improving 0.3716". A5 fixes it.

### (xi) Corollary 3.2 (deletion model) — PASS; AMEND A7 (scope and definition), A8 (odd-sector sentence)
**Range check (requested).**
* For `T ∈ [0.461, 0.58]`, `N_T = {n : n < e^{2T} ≤ e^{1.16} = 3.19} ⊂ {2,3}`, and `a = Λ1_{n≥5}` vanishes there.
  In fact the comb is empty for every `T < ½log 5 = 0.8047`, so the form is purely archimedean plus polar:
  `W_T(a) = \Ainf` and `λ^W_T(a) = \laminf(T) < 0` (Thm 3.1).
* `RD_T(a)` is **literally** `thm:finmod`(i): `λ^A_T(a) = \laminfP(T)`. This is `> 0` for `T ≤ 0.58` by
  `thm:index`(i)/`cor:Tarch`, which are `T ≤ 0.58 ≤ T^*_{∞,P}`, PROVED (machine-verified).
* So the counter-model is **exactly the archimedean analogue**. The converse fails for the empty comb on
  `[0.4608, 0.58]`.

**Is it genuinely "a model with the same zeros and pole as ζ"?** In the sense of `thm:finmod`(iii), yes. The
construction is valid on this range with `N = 5`, and `ζ_a = ζ·E` with `E` entire and zero-free. But the phrase
invites a false reading. For `ζ_a`, the explicit-formula zero sum `Σ_ρ Φ_F(ρ)Φ_F(1−ρ)` runs over the zeros of ζ, so
it equals `W_T(Λ)(F)`, and **not** `W_T(a)(F)`. Contour integration of `ζ_a'/ζ_a = ζ'/ζ + E'/E` gives
`W_T(a) = W_T(Λ) + Σ_{n∈N_T, n<5} v_n c_F(log n)`. On `[0.461, 0.58]`, `W_T(Λ) ≥ 0` (Zhu), while `W_T(a)` has negative
directions. So `W_T(a)` is not a Weil functional of `ζ_a`. `λ^W_T(a) < 0` says nothing about zeros, and it is not
tied to the missing functional equation alone.

The counter-model refutes the **comb-level implication** `RD_T(a) ⟹ λ^W_T(a) ≥ 0` over nonnegative combs, in exactly
the sense in which `cor:void` refutes comb-level derivations of `RD_T`. That is what Cor 3.4 uses, and it is sound.
A7 makes this explicit, together with the definition of `W_T(a)`.

**Novelty.** For the empty comb the failure *is* `T^*_∞ < T^*_{∞,P}`. P46 shows this DIAGNOSTICALLY after `cor:Tarch`
(`0.3716` vs `0.5958`). The new content is the proof, and A7(iv) says so.

**A8.** On `(T^*_{∞,P}, log 2]`, `RD_T(a)` fails (`λ_ev < 0` from `0.60`), so the full converse is vacuous there. Only
the odd-sector implication is refuted on `[0.461, log 2]`. The sentence is reworded as a sector statement.

### (xii) Theorem 3.3 (one-contact family at `½log 3`) — PASS; AMEND A6 (unsafe rounding)
**(i)**
* `N_T = {n : log n < log 3} = {2}`. The contact `n = 3` sits on the boundary and is excluded, since `c_F(log 3) = 0`.
* `λ^A(θ) = inf_{F∈P, ‖F‖=1}[\Ainf(F) + θΠ(F)]` is an infimum of affine functions of `θ`, finite since `‖Π‖ ≤ v_2`,
  hence **concave** on `ℝ`.
* At `θ = 0` it is `\laminfP(½log 3) > 0` (`cor:Tarch`, PROVED machine-verified).
* At `θ = 1` it is the true primitive bottom `λ^A_{½log3} ≥ λ^P ≥ 8.8577·10^{-5}` (`thm:C`). `thm:C` is stated for
  `σ_T` with the actual comb `v_2` at `T = ½log 3` (P46 l.955–972), so it is the primitive form with the true comb.
* A concave function is `≥` the minimum of its endpoint values on `[0,1]`. PASS.

**(ii)** `audit_r156_theta_quintic.py` uses exact rationals `b_3, b_5`, exact sympy polynomials, and interval
evaluation at `T = iv.log(3)/2`, 50 digits. It gives:
* `‖F‖² ∈ 0.0184539062097933…`;
* `U_0 ∈ [−0.006137784435690034414…, −0.006137784435690034414…]`;
* `Π(F) = −v_2 c_F(log 2) ∈ 0.00753283781432786993…`;
* `−U_0/Π ∈ 0.8148037415614647…`;
* `U_0 + 0.8148·Π ∈ −2.818457568599·10^{-8} < 0`.

For `F = t`: `U_0 ∈ −0.0200526…`, `Π ∈ 0.0422949974…`, `−U_0/Π ∈ 0.4741138474…`, and
`U_0 + 0.4741·Π = −5.86·10^{-7} < 0`. DIAGNOSTIC: the exact `\Ainf(F)` of the quintic is `−0.00723196`.

So **`λ^W_T(a_θ) < 0` for every `θ ≤ 0.8148`, PROVED.** "`𝒜_∞(F) ≤ −0.0061378`" is rounded in the unsafe direction
(`−0.0061377844 > −0.0061378`) and becomes `≤ −0.00613778`. The threshold statement is unaffected. The margin at
`θ = 0.8148` is `2.8·10^{-8}`, not the `6·10^{-3}` of doubt 3; it is safe only because it is now interval-verified.

**(iii)** `θ ↦ λ^W(a_θ)` is concave on `ℝ` for the same reason, hence continuous. It is positive at `θ = 1` by Zhu
(cited). So `{λ^W ≥ 0} ∩ [0,1]` is an interval containing `1`, the failure set is `[0, θ_*)`, and
`0.8148 < θ_* < 1`. PASS.

The DIAGNOSTICS were re-run: `g_-(0.9999) = −2.9·10^{-4}`, `g_+(1.001) = −4.9·10^{-5}`, `g_+(1) = +1.0·10^{-7}`. They
reproduce, and they stay DIAGNOSTIC; see A16 on the direction of Galerkin bounds. The same comb-level scope applies
(A7).

### (xiii) Corollary 3.4 (method constraint) — PASS; AMEND A9 (class hypothesis of the `½log 3` clause)
The `[0.461, 0.58]` clause is correct under deletion-closure: `Λ1_{n≥5}` deletes `n = 2, 3, 4`. The `½log 3` clause
needs `a_θ ∈ 𝒞` for some `θ < 0.8148`, which deletion-closure does not give, since it gives only `θ = 0`. The fix
states the right closure: lowering one term within `[0, Λ(n)]`. `𝒞_BT`, `𝒞_zeros` and `𝒞_PNT(ε)` all have it.
"Relative precision 18.5%" is made one-sided: it concerns weights *below* `Λ(2)`.

### (xiv) The archimedean analogue paragraph — PASS; AMEND A10 (label source)
The failure on `[0.4608, 0.58]` is PROVED. The extension to `(T^*_∞, T^*_{∞,P})` uses the strict decrease of
`\laminf`. P46 asserts this in the unnumbered paragraph after `lem:strict`, with its argument: test against `G_0` with
vanishing moments, so the pole term drops out. The `R155_061` closing note confirms that it holds on `L²`. So it is
not an "unproved remark". It is a proved but unnumbered statement, and it needs a number before any paper cites it.
Its label row is otherwise correct.

### (xv) Prop 4.1 — PASS; AMEND A11/A11b
* (i) P42 `cor:certifiedinitialinterval` is primitive, which is correct, and `λ^A > 0` holds (strict, compact
  resolvent).
* (ii) Zhu, then Thm 1.1(c): correct.
* (iii) The Yoshida primary text was not read on record (`R154_013` l.20). Bombieri Thm 12 covers `|I| < log 2`. The
  certified backstop is Zhu. The conclusion stands.
* (iv) "exactly on the directions `G_T` measures" overclaims. `G_T` sees `A, B` only, while `thm:C`'s `β_1` term also
  involves `A', B'`. The wording is fixed (A11b).

### (xvi) §5 (reduction chain) — §5.1 **FAIL as stated** (A12); §5.2–5.4 PASS; §5.5 AMEND A13
* **§5.1.** "[∃ flat-top certificate] ⟺ [KEP(T) indeterminate] ⟺ [RD_T strictly ∧ G_T ≻ 0]" is not proved.
  `thm:Al`(b) gives `∃ Al_T(w) ⟺ λ^W > 0`. `thm:KEP3`(a) gives only `λ^W > 0 ⟹ indeterminate ⟹ λ^W ≥ 0`, and P46
  itself says the two notions coincide "except on `{T: λ^W = 0}`". The corrected chain is applied in place.
* **§5.2** follows from Thm 1.1(c). **§5.3** is correct (`λ^W ≤ λ^P`). **§5.4:** P45 `thm:sufficiency` exists, and
  P46 cites it as [Paper45, Thm 10.4]; the statement is correct.
* **§5.5.** For `max(T,T') ≥ ½log 5` the model must be `Λ1_{n≥N}` with `N ≥ e^{2max(T,T')}`. Stated precisely, the
  shift must satisfy `T' ≥ T^*_{∞,P}`, and `≥ 0.58` is PROVED.

### (xvii) Doubt 4 (models lack the functional equation) — resolved by A7
The missing functional equation is not the only gap. The model's form is not the zero sum of its own `ζ_a`. The
correct scope is "comb-level counter-model / class statement", as in `cor:void` and `rem:twohalves`. A functional-
equation model (Epstein/Dedekind) was not attempted, and this stays an open remark.

### (xviii) Doubt 6 (float64 Galerkin) — PASS as labelled; AMEND A16
* On finite matrices the inertia check is Haynsworth's identity, which holds exactly, so it checks code, not the
  theorem.
* Galerkin `κ`, and hence `g`, are **upper** bounds. A negative Galerkin `g` is evidence (up to float and quadrature
  error), but a positive one, such as `g_+ ≈ 8.6·10^{-8}`, is not.
* All small ζ numbers stay DIAGNOSTIC. Re-runs reproduce: prime-free `½log 3`: `g_+ = −0.4509`, `g_- = −20.08`,
  `λ^A_ev/odd = +0.0825/+0.3816`; the six inertia cases; the `θ`-family.

### (xix) Doubt 7 (`S_T` vs `G_T`) — PASS (see (vii))

### (xx) Doubt 8/9 (`def:W` vs `eq:W`) — PASS; AMEND A15 (notation clash for integration)
P46 already uses:
* `G_T(t) = g(t/T)` and `F_T` (`prop:finsupp`);
* `S_{T,τ_1}` and `S_c` (time–band limiting);
* `Γ_T` (the pole-free archimedean form);
* `κ(x)` (the killing density, `prop:nodes`).

For the paper, rename `G_T → 𝔊_T` (or `G^{\mathrm{pol}}_T`), `S_T → S^{\mathrm{Sch}}_T` and `F_T → F^{\mathrm{odd}}_T`.
Keep `κ_±`, which is safe because it is subscripted.

---

## Citation ruling (doubt 5, item 6 of the report)

**Confirmed slip.** P46 `prop:arch`(iii) (l.2375–2377) reads: "`\laminf(T) ≥ 0` by the known positivity of `W_T` for
`T ≤ log 2` [Paper42, Yoshida1992, Bombieri2000]". The citations do not support that sentence.

1. **Paper 42.** `thm:certifiedendpoints` (l.4164–4172) and `cor:certifiedinitialinterval` (l.4355–4360) prove
   strict positivity **on `P_T`** of the operator with the *complete prime comb*. "Complete" in P42 means all
   contacts included, not the complete Weil form. The ranges are `0 < T ≤ ½log 3`, `T = log 2`, and then
   `0 < T ≤ log 2` by nesting. **Primitive only.** It says nothing about `W_T` on `L²(I_T)`.
2. **Yoshida 1992.** Thm 1 is strict positivity on `K(a)` at `a = ½log 2`, i.e. autocorrelation support `log 2`, i.e.
   `T = ½log 2` in P46's notation. The comb is empty there. Lemma 2 is qualitative for small windows. The primary text
   is not in `00-references` (`R154_013` l.20), and P46 l.274 calls the computation "approximate finite-matrix".
3. **Bombieri 2000 Thm 12.** Quantitative for `|I| < log 2`, the prime-free range, i.e. `T < ½log 2`.

**What is known for the complete form `W_T` (i.e. `λ^W ≥ 0`), exactly:**
* `0 < T ≤ ½log 2` (`2T ≤ log 2`, empty comb): classical (Yoshida; Bombieri Thm 12), with the rigour caveat on
  Yoshida's primary text. It is also covered by Zhu.
* `½log 2 < T ≤ 0.8`: **only** Zhu 2026 Thm 1.2 (`W_{0.8} ≥ 8.9·10^{-18}`, certified matrix computation, cited, not
  re-verified). Nothing in the programme proves `λ^W ≥ 0` at any `T > ½log 2`, whether P42, `thm:C`, `thm:index`, or
  R156. Passing from P42's primitive sign to the complete sign at a fixed window is precisely the per-window converse,
  and R156 shows it is not structural.
* `T > 0.8`: nothing.

**What is known for the primitive form (`λ^A`):**
* `0 < T ≤ log 2`: P42 `cor:certifiedinitialinterval` (Arb-certified, in-programme).
* `T = ½log 3`: independently by P46 `thm:C` (`λ^A ≥ λ^P ≥ 8.8577·10^{-5}`).
* `T ≤ 0.8`: through Zhu, since `λ^A ≥ λ^W`.

**The standing phrase "no sign beyond `T ≤ log 2`"** is correct only as a statement about the **primitive form**
`\lamA` (row D proper, `RD_T`). There it records the programme's own proved range, P42, beyond which the programme
claims nothing and only cites Zhu. For the **complete form** `\lamW`, the programme's proved or classical range is
`T ≤ ½log 2`. Everything in `(½log 2, 0.8]` rests on Zhu, cited. Where the complete form is meant, the phrase must read
"`T ≤ ½log 2` (classical), `T ≤ 0.8` (Zhu, cited)".

**Where the slip occurs:**
* P46 l.2377 (`prop:arch`(iii));
* P46 l.308 ("Positivity at `T ≤ log 2` is known [Paper42, Yoshida1992, Bombieri2000]", with the form unspecified);
* `R155_031` l.51 and `R155_023` l.87, 328.

P46 l.148–150 (intro) is **correct** as worded: P42 for `T ≤ log 2`, Yoshida/Bombieri "for the complete form at
autocorrelation support `log 2`", Zhu at `1.6`. The blueprint phrase quoted by the report was not found verbatim in
`R156_000` or the plan file.

**Consequence for P46's mathematics: none.** `prop:arch`(iii) needs only `2T < log 2`, which Yoshida, Bombieri and
Zhu cover. `thm:finmod`(i) uses it in the same range. `cor:KEP08` already rests on Zhu, correctly.

**Paper fix, for the editor, not applied here.** In `prop:arch`(iii), replace "`W_T` for `T ≤ log 2`
[Paper42, Yoshida1992, Bombieri2000]" with "the complete form at autocorrelation support `≤ log 2`
[Yoshida1992, Bombieri2000] (and, certified, [Zhu2026, Thm 1.2])". Drop Paper42 there. At l.308, split the sentence
into "the primitive form for `T ≤ log 2` [Paper42]" and "the complete form for `T ≤ ½log 2` [Yoshida1992,
Bombieri2000] and `T ≤ 0.8` [Zhu2026]".

---

## Verdicts

| statement (`R156_001`) | verdict | label after audit |
|---|---|---|
| Definitions vs P46 (`eq:W`, `𝔞_T`, `P_T`, `\lamA`, `\lamP`, `\lamW`, `\Ainf`, `RD_T`) | PASS (A7: define `W_T(a)`) | — |
| L1.0 parity splitting `W = (𝔞+2c²) ⊕ (𝔞−2s²)` | PASS | PROVED |
| T1.1(a) nondegenerate: `D = P ⊕ span(h_±)`, `𝔞`- and `W`-orthogonal; `In(W) = In(𝔞|P) + In(G_T)` | PASS (A1: self-contained proof; no restriction) | PROVED |
| T1.1(a4) `g = min{W : ℓ = 1}` | PASS | PROVED |
| T1.1(a5) sandwich | **AMEND** (A2: needs `g > 0`; false for `g < 0`) | PROVED as amended |
| T1.1(b) degenerate case; range condition | PASS (A3: "same shape as P124"; gap needed for `Ran L^{1/2}`) | PROVED |
| T1.1(c) `λ^W>0 ⟺ λ^A>0 ∧ g_±>0`; `λ^W≥0 ⟺ RD_T ∧ range ∧ G_T⪰0` | PASS | PROVED |
| R1.2 `G_T = S_T + J`; resolvent formulas | PASS | PROVED |
| P2.1 polar capacity | PASS | PROVED |
| §2 `S_T ≈ −J`, doubly-exponential thinness | **AMEND** (A4: typo `−1.99999991`; `cor:margin1` also bounds `λ^A`) | DIAGNOSTIC / HEURISTIC |
| R2.2 zero-side reading | PASS | HEURISTIC (reading) |
| **T3.1** `\Ainf(t) ≤ U(T) < 0`, `T^*_∞ ≤ 0.4608` | **PASS**, interval-verified (A5 wording: proved 0.60 → 0.4608; weaker than the diagnostic 0.3716) | **PROVED** |
| **C3.2** deletion model, converse fails on `[0.461, 0.58]` | **PASS** (A7 scope and definition; A8 odd-sector wording) | **PROVED** (comb-level; primitive side machine-verified import) |
| **T3.3(i)** `λ^A(a_θ) > 0` on `[0,1]` by concavity | PASS | PROVED (imports `cor:Tarch`, `thm:C`) |
| **T3.3(ii)** quintic, `λ^W(a_θ) < 0` for `θ ≤ 0.8148` | **PASS**, interval-verified (A6: `≤ −0.00613778`, margin `2.8·10^{-8}`) | **PROVED** (comb-level) |
| T3.3(iii) failure set `[0,θ_*)`, `0.8148 < θ_* < 1` | PASS | PROVED (Zhu cited for `θ_* < 1`) |
| T3.3 `θ_* ≈ 0.99991`, window `≈ 10^{-4}` | PASS as labelled (A16) | DIAGNOSTIC |
| **C3.4** method constraint | **AMEND** (A9: class hypothesis of the `½log3` clause; one-sided precision) | PROVED (method constraint) |
| §3 archimedean analogue on `(T^*_∞, T^*_{∞,P})` | PASS (A10) | PROVED on `[0.4608,0.58]`; the rest rests on P46's unnumbered strict-decrease paragraph |
| P4.1(i)–(iv) | PASS (A11: Yoshida caveat; A11b "exactly" dropped) | PROVED resting on imports / Zhu (cited) |
| **§5.1** "certificate ⟺ KEP indeterminate ⟺ …" | **FAIL as stated** → corrected chain (A12) | PROVED as corrected |
| §5.2–5.4 | PASS | PROVED |
| §5.5 window shift | **AMEND** (A13: `N` depends on `T,T'`) | PROVED / OPEN (ζ) |
| §6 novelty | PASS with A7(iv) (empty-comb failure = `T^*_∞ < T^*_{∞,P}`, diagnostic in P46; new is the proof) | — |
| §7 diagnostics | PASS (A16) | DIAGNOSTIC |
| §9 item 6 citation slip | **CONFIRMED** (A14; ruling above) | — |
| OPEN items (`RD_T ⟹ λ^P ≥ 0`; effective shift for ζ; converse for ζ at `T > 0.8` ⟺ `RD_T ⟹ G_T ⪰ 0 (+range)`) | PASS | OPEN |

---

## Mandatory fixes (all applied in place to `R156_001`, marked "[amended per R156_004]")

* **A1** (Thm 1.1(a) proof). The self-contained Lax–Milgram/spectral-splitting step.
* **A2** (Thm 1.1(a5), label table). The sandwich holds only under `g_par > 0`.
* **A3** (Thm 1.1(b)). "A range condition of the same shape as P124_011". The gap justifies `Π_{ker}ρ = 0 ⟺
  ρ ∈ Ran L^{1/2}`.
* **A4** (§2). Correct the typo `S_T ≈ diag(−1.99999991, +2.00135)`; add the hyperbolicity hypotheses; note that
  `cor:margin1` bounds `λ^A`.
* **A5** (Thm 3.1, label table). Correct the wording of the proved bound; make the interval values the certificate of
  record; state the result from `0.4608`; replace `−3.6` by `−3.59`.
* **A6** (Thm 3.3(ii)). Replace `≤ −0.0061378` by `≤ −0.00613778`; add the interval values; state the true margin
  `2.8·10^{-8}`.
* **A7** (verdict paragraph, after Cor 3.2, Thm 3.3). Define `W_T(a)`; state that it is not the zero sum of `ζ_a`; mark
  the counter-models as comb-level class statements; add the novelty note; record the range check.
* **A8** (Cor 3.2). Make the odd-sector sentence sector-wise.
* **A9** (Cor 3.4). Give the `½log 3` clause its class hypothesis; make the precision one-sided.
* **A10** (§3). Correct the label source for the strict decrease of `\laminf`.
* **A11/A11b** (Prop 4.1(iii),(iv)). Add the Yoshida caveat and the Zhu backstop; drop "exactly".
* **A12** (§5.1). Correct the chain. The original was FAIL as stated.
* **A13** (§5.5). Make `N` depend on `max(T,T')`.
* **A14** (§9.6). Confirm the slip, list its locations, and note that the quoted blueprint phrase was not found.
* **A15** (§9.6/9). Rename the notation for integration.
* **A16** (§7). The Galerkin inertia check tests code, not the theorem; Galerkin `g` values are upper bounds.

`scripts/r156/README.md`:
* "Thm 3.2" is corrected to "Thm 3.3".
* The 30-digit float witness scripts are marked superseded as certificates.
* An "Audit re-verification" section lists `audit_r156_witness_t.py` and `audit_r156_theta_quintic.py` (new files).
* A note records the unsafe rounding.

No paper and no other README was touched.

---

## What is cleared for Paper 46 §10.6 (`subsec:alignineq`, the OPEN paragraph at l.3549–3552), with one item for §9.1

These are cleared with the proposed labels. Use the renamed notation (A15), and check every sentence against `eq:W`,
`\PT`, `\lamA`, `\lamW`, `\Ainf` and `RD_T(a)` as printed.

1. **`thm:parityschur`** (Lemma 1.0 and Thm 1.1(a)–(c), with A1–A3). The parity splitting. For `0 ∉ spec(A_T|P_T)`:
   `In(W_T) = In(A_T|P_T) + In(𝔊_T)`, with `𝔊_T = diag(g_+, g_-)`, `g_± = W_T(h_±)`. Per window:
   `\lamW > 0 ⟺ [\lamA > 0 ∧ 𝔊_T ≻ 0]`, and `\lamW ≥ 0 ⟺ [RD_T ∧ range ∧ 𝔊_T ⪰ 0]`. The sandwich goes in only with
   `g > 0`. **PROVED.**
2. **`prop:polarcap`** (Prop 2.1 and Remark 1.2's `𝔊_T = S^{\mathrm{Sch}}_T + J`). The polar capacity
   `E_T(B,A) = (A,B)𝔊^{AB}(A,B)^T`. **PROVED.**
3. **`prop:archneg`**, for **§9.1** `subsec:arch` as `prop:arch`(v) or right after `cor:Tarch` (Thm 3.1, with A5).
   `\laminf(T) < 0` for every `T ≥ 0.4608`, by the explicit witness `F = t` and the elementary bound `U(T)`. Hence
   `T^*_∞ ≤ 0.4608 < 0.58 ≤ T^*_{∞,P}`. **PROVED** (elementary; certificate `audit_r156_witness_t.py`). Keep
   `0.3716` as the DIAGNOSTIC bound, and do not write "improves 0.3716".
4. **`cor:convfail`** (Cor 3.2, Thm 3.3, Cor 3.4, with A6–A9). For the comb-level form
   `W_T(a) := 𝔞^{(v(a))}_T + 2Re(AB̄)` (define it in the paper next to `RD_T(a)`, and say that it is not the zero sum
   of `ζ_a`), the implication `RD_T(a) ⟹ λ^W_T(a) ≥ 0` fails in two cases:
   * for `a = Λ1_{n≥5}` at every `T ∈ [0.4608, 0.58]`;
   * for `a_θ` at `T = ½log 3` for every `θ ≤ 0.8148`.

   Consequently no derivation of the per-window converse from deletion-closed class membership exists on
   `[0.4608, 0.58]`, nor at `½log 3` for classes containing some `a_θ` with `θ < 0.8148`. **PROVED** (method
   constraint, in the sense of `cor:void`; imports `thm:index`/`cor:Tarch`, `thm:C`, and Zhu only for `θ_* < 1`;
   certificate `audit_r156_theta_quintic.py`).
5. **Rewrite of the OPEN paragraph** (l.3549–3552). "Per window, `RD_T` implies `\lamW ≥ 0` if and only if `𝔊_T ⪰ 0`
   (and the range condition in a degenerate sector), by `thm:parityschur`. This is not a comb-class consequence at any
   `T ∈ [0.4608, 0.58]` (`cor:convfail`). For ζ it holds for `T ≤ 0.8` because its conclusion is Zhu's certificate.
   For `T > 0.8` it is OPEN." Also the corrected chain of A12, if a chain is printed:
   `∃ Al_T ⟺ \lamW > 0 ⟺ [\lamA > 0 ∧ 𝔊_T ≻ 0] ⟹ KEP(T) indeterminate ⟹ \lamW ≥ 0`. **PROVED.**

**Not cleared** (they stay out of the paper, or enter only with their labels):
* the values `g_± (½log 3) ≈ 8.6·10^{-8} / 1.35·10^{-3}`, `S_T ≈ −J`, `θ_* ≈ 0.99991`, the `10^{-4}` window, the
  channel crossings `≈ 0.372 / 0.44` (DIAGNOSTIC);
* the doubly-exponential thinness of the converse (HEURISTIC);
* Remark 2.2 (reading);
* the extension to all of `(T^*_∞, T^*_{∞,P})`, until the strict decrease of `\laminf` gets a numbered statement;
* §5.1 in its original form (FAIL).

Separately, and independent of R156, the editor should apply the **citation fix** to `prop:arch`(iii) and l.308 given
in the ruling above. It changes no mathematics.

Row-D label and endpoint of record are unchanged. Nothing here is a sign for ζ at any new window, or a statement about
the zeros of any `ζ_a`.
