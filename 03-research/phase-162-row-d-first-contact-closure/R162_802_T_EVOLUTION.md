# R162_802 — Round 8: evolution in T of the resolvent flow

Notation from Paper 46 (eq:form, eq:W, lem:monoT, thm:parityschur),
R162_504 (f_par, μ_k, Perron vector ψ_T) and R162_703 (g_par, Type I/II, T_W ≤ T_*).

**Status.**
- §2 exact collar increment law for f_par(0;T): **PROVED**.
- §3 index bookkeeping and the projective (Prüfer-type) flow: **PROVED**. §3.4 RH as two monotone
  limits: **PROVED**, conditional on Cor 2.1 of R162_504 (localisation caveat). It is an equivalent
  form of RH (E1).
- §4 how the arithmetic enters the flow (a switch-on term of size w_n = Λ(n)n^{-1/2} at T = ½log n,
  with amplitude equal to an edge trace): **PROVED** as a structural statement. The Dirichlet series
  of these jumps is **not** −ζ'/ζ.
- §5 a search for a monotone or invariant quantity that Λ*1 = log fixes and that forbids contact:
  **NO-GO**. Every monotone quantity of the flow holds for κ-models and finite modifications (F3).
  The one quantity with generating series −ζ'/ζ is linear in w, so it is killed by F4 and the
  sawtooth. Matching the pole at s = 1 is a PNT-level balance that finite modifications share (M, F3).
- §6 conjecture: the terminal values are pinned exactly by the polar term (f_ev(∞) = −½,
  f_odd(∞) = ½). RH would then say that the flow approaches its pinned asymptote from below and never
  overshoots.

No sign is claimed. Gate 1 remains OPEN.

## 1. Corpus check (not repeated here)

- Kreĭn/de Branges/canonical systems, the global Hamiltonian: phase 64
  (CONSTRUCTION-TW-canonical-system: the positive von Mangoldt Hamiltonian; the rank-one escape
  theorem is RH-strength), phase 120 (C.1), and R162_590 §1a row 2 (E1).
- Kreĭn indeterminacy: phase 155 round 5, Paper 46 thm:KEP3. RH ⟺ KEP(T) is indeterminate for all T.
- Riccati: phase 102 (Turán–Riccati), phase 104 (Selberg–Riccati, "Riccati identity without an
  independent Gamma term"), P122_006/008 (Riccati pole-order quantization, PROVED-CONDITIONALLY, no
  source theorem).
- Window variation: P124_004–010, R162_101 (the shrinking first variation is zero), R162_405/406
  (collar identity and Chebyshev edge coefficient), R162_407/408 (behaviour near T_*),
  R162_703 Lemma 2.1 (g_par is nonincreasing).

What is new here:
- the *finite-δ* exact increment of f (not the first variation at T_*);
- the global projective flow over **all** T, through eigenvalue crossings, with an index invariant;
- the reformulation of RH as two monotone limits;
- the explicit placement of the Λ-jump in the flux, together with a proof that its generating series
  is not −ζ'/ζ.

Everything is taken per parity sector, and the index par is suppressed when it causes no ambiguity.
- The window is I_T = (−T,T). φ = φ_par, and A_T = A_T^par.
- u_T = A_T^{-1}φ whenever 0 ∉ spec A_T. Then f(T) := f_par(0;T) = ⟨u_T, φ⟩.
- ũ denotes extension by zero.

## 2. Exact collar increment — PROVED

**Theorem 2.1.** Let T < T′, and suppose A_T and A_{T′} are both invertible in the parity sector.
Define the collar residual r ∈ D(a_{T′})* by

  r(G) = a_{T′}(ũ_T, G) − ⟨φ, G⟩.

Then:
- r vanishes on every G supported in I_T, so supp r ⊂ C = I_{T′} \ I_T;
- r(ũ_T) = 0;
- f(T′) − f(T) = ⟨A_{T′}^{-1} r, r⟩ exactly.

*Proof.*
- For G supported in I_T we have a_{T′}(ũ,G) = a_T(u,G) = ⟨φ,G⟩. This is the extension compatibility
  of lem:monoT: new contacts have log n ≥ 2T, so the autocorrelation vanishes there. Hence r(G) = 0.
- r(ũ) = a_T(u,u) − ⟨φ,u⟩ = 0.
- Write u′ = u_{T′}. Then a_{T′}(ũ − u′, G) = r(G), so ũ − u′ = A_{T′}^{-1}r.
- Therefore f(T′) − f(T) = ⟨u′ − ũ, φ⟩ = a_{T′}(u′, u′ − ũ) = −r(u′).
- Since u′ = ũ − A_{T′}^{-1}r and r(ũ) = 0, we get −r(u′) = r(A_{T′}^{-1}r). ∎

**Corollary 2.2 (Schur/Riccati form).** Split L²(I_{T′}) = L²(I_T) ⊕ L²(C) and let S_C be the Schur
complement of A_{T′} onto the collar. Then f(T′) − f(T) = ⟨S_C^{-1}ρ, ρ⟩, where ρ = r|_C. As
δ = T′ − T → 0, the local part of S_C is the archimedean form on an interval of length δ, whose bottom
is ≍ log(1/δ) → +∞. Provided dist(0, spec A_T) stays bounded below, S_C > 0, and the increment is
≥ 0. On any interval of invertibility, this gives the Kreĭn-type law df/dT ≥ 0, which is the
resolvent form of R162_703 Lemma 2.1 (a(h) = 1/f). The infinitesimal flux
𝔣(T) = lim ⟨S_C^{-1}ρ,ρ⟩/δ is the analogue of Kreĭn's 2|u_T(T)|² for a symbol of logarithmic order.
Its existence as a limit needs edge regularity of u_T, which is the (REG) of R162_407 and is not
proved here. The finite-δ identity needs no regularity.

## 3. The projective flow over all T — PROVED

**3.1 Monotone data.**
- μ_k(T) is nonincreasing, by min–max and extension by zero.
- f is nondecreasing on every interval where A_T is invertible and λ_par > 0 (§2 and Lemma 2.1).
- Near a simple crossing μ_k(T_c) = 0 with ⟨ψ_k, φ⟩ ≠ 0 we have f ≈ ⟨ψ_k,φ⟩²/μ_k. So f → +∞ as
  T ↑ T_c and f → −∞ as T ↓ T_c.

Hence f(T) moves monotonically on the projective line ℝ ∪ {∞}. It passes through ∞ exactly at the
crossings, and it passes through 0 exactly at the Type II contacts (R162_703 Prop 4.1).

**3.2 Index invariant (Haynsworth, bordered form).** Let N₋(T) = n₋(A_T^par), which is finite
(compact resolvent), and let ι(T) = n₋(A_T|Q^par) be the primitive index. Whenever 0 ∉ spec A_T and
f(T) ≠ 0,

  ι(T) = N₋(T) − 𝟙[f(T) < 0].

- Across a crossing, N₋ jumps by +1 and 𝟙[f<0] jumps from 0 to 1, so **ι is conserved**.
- When f crosses 0 upward, ι jumps by +1. This is the first contact.
- λ_par > 0 ⟺ ι = 0.

So ι is the conserved charge of the flow. Contact is the single event that is not charge-conserving.
This uses λ = 0 non-perturbatively, as the zero of f (F1 compliant). But it is a detector, not a
forcer.

**3.3 Complete form on the same line.** g_par = 1/f + 2ε_par. So:
- a complete-form contact happens when f_ev = −½ or f_odd = ½;
- a primitive contact happens when f = 0.

On the even branch, f increases from −∞ toward 0 and must pass −½ first. This proves T_W^ev ≤ T_*^ev
without any computation, recovering R162_703 §4. On the odd branch, f increases toward +∞ and must pass
½ before any odd crossing.

**3.4 RH as two monotone limits.** Assume R162_504 Cor 2.1 (RH ⇒ μ₂(A_T) ≥ 0 for all T, via the usual
localisation). Let T_P be the Perron crossing, the unique T with μ₁(T) = 0. Then:

- RH ⟺ (i) there is no crossing in either sector except T_P; and (ii) the limits
  f_ev(∞) := lim_{T→∞} f_ev(0;T) ≤ −½ and f_odd(∞) ≤ ½.
- Both limits exist in (−∞, +∞] by monotonicity.
- (i) is implied by (ii) together with ι ≡ 0.

*Proof.*
- (⇒) Under RH, λ_W ≥ 0 for all T. So λ_A > 0 (Paper 46), and ι ≡ 0. μ₂ ≥ 0 gives N₋^ev ≡ 1 past
  T_P and N₋^odd ≡ 0. Hence f has no poles, and it is monotone. g_par ≥ 0 gives the bounds.
- (⇐) Monotone and bounded with ι ≡ 0 gives g_par(T) ≥ 0 for all T. Thm 2.2 of R162_703 then gives
  λ_W ≥ 0 for all T, which is RH (thm:KEP3). ∎

This is E1: a clean equivalent form, not progress on the sign.

## 4. Where the arithmetic enters the flow — PROVED (structural)

For s ∈ C = (T, T+δ), the prime part of the residual is

  ρ_prime(s) = −Σ_{n: log n < s+T} w_n ũ_T(s − log n)   (plus the mirror term),

where w_n = Λ(n)n^{-1/2}.
- A contact n with ½log n ∈ (T, T+δ) is active only for s > log n − T.
- There it contributes w_n·u_T(−T + (s − log n + T)), which is w_n times the **edge trace** of u_T.
- So the flux switches on a term of size w_n at T = ½log n, with amplitude ε·u_T(T⁻) (parity).
- This is the requested jump structure. But the jump size is w_n × (edge trace at T_n), and the
  edge trace depends on the whole past flow.

Its Dirichlet series Σ_n w_n·u_{T_n}(T_n⁻)·n^{-s} is not −ζ'/ζ(s+½). It would be only if the edge
trace were constant in T, and it is not: at ½log5 the edge traces of the even and odd sectors differ
by orders of magnitude (R162_703 §3 table).

## 5. Search for an invariant fixed by Λ*1 = log — NO-GO

Candidates, each with the line where it fails:

1. **Kreĭn flux positivity (df/dT ≥ 0) and the charge ι.**
   - They use only extension compatibility and finite negative index.
   - Both hold verbatim for every a ≥ 0 supported on prime powers (the κ-models of R162_702), for
     finite modifications, and for DH. For DH the thresholds become f = 0/∞, because there is no polar
     term.
   - Failing line: §3.1. The deletion model a = Λ1_{n≥5} has f_odd crossing ½ at T = 0.4608
     (cor:convfail) while obeying every monotonicity above. **F3.**

2. **Pole matching.**
   - The Perron eigenvalue μ₁(T) ~ −Σ_{log n<2T} 2w_n·(overlap) ~ −4e^T. It is balanced against the
     Tate/polar term through Σ a(n)n^{-s} = 1/(s−1) + O(1).
   - This balance is the pole of −ζ'/ζ at 1, but it is a PNT-level (density) statement.
   - Any finite modification keeps the residue 1, and the κ-models of R162_702 can keep it too.
   - Failing line: the asymptotic μ₁ ~ −4e^T holds for the deletion model. **M, F3.**

3. **The flow-linear functional Σ_n w_n n^{-s}.**
   - Λ*1 = log enters the flow only as a *linear* relation among switch-on coefficients, through the
     window shifts T → T + ½log m (D4 Thm 5.1). This is the sawtooth ⌊X/d⌋ = the (PC) comb (R162_701).
   - Monotone quantities of the flow (flux, ι, the projective phase) are nonlinear in u_T and depend on
     w only through the operator. No monotone quantity is linear in w.
   - Failing line: linear graph limit. **F4.**

4. **A Riccati first integral.**
   - For truncated convolution operators with a positive-definite symbol, the Kreĭn–Bellman–Siegert
     system has the conserved Wronskian det = 1 (the de Branges structure). Here the symbol is the
     Weil distribution, which is positive-definite exactly under RH.
   - A conserved first integral of that type is phase 64 / thm:KEP3.
   - Failing line: positivity of the Hamiltonian is assumed. **E1.**

**Meta-statement (why the line is closed).** Every exact law of the T-flow comes from one of two
sources:
- (a) extension compatibility and min–max, which are weight-blind;
- (b) the explicit formula, where positivity is equivalent to RH.

Λ*1 = log is a convolution identity on tests, which is a window shift (D4 Thm 5.1), that is, a
reparametrisation of the flow itself. So inside the flow it can produce only a relation between
f(T) and f(T + ½log m) that is linear in w. Such relations are the (PC) comb (F4). A monotone quantity
that forbids contact must therefore be nonlinear in w at the switch-on edge traces of §4. No such
quantity is identified.

## 6. Conjecture (terminal pinning)

**Conjecture 6.1.** For ζ, lim_T g_par(T) = 0, that is, f_ev(∞) = −½ and f_odd(∞) = ½.

*Heuristic.*
- As T → ∞, W_T(F) = Σ_ρ Φ(ρ)Φ(1−ρ) can be made small while ℓ_par(F) = 1 (Beurling–Malliavin:
  exponential type 2T against zero density ~ log).
- Theorem M makes the margins super-exponentially small.

If the conjecture holds, RH says that the monotone flow approaches the asymptote fixed by the pole of
ζ from below and never overshoots. Overshoot is exactly what the deletion model does in the odd sector
at 0.4608. A proof of "no overshoot" would need a quantity that is nonlinear in the edge traces of §4.

**Open (O802.1).** Is there an identity, valid for a = Λ and failing for a = Λ1_{n≥5}, that ties the
edge traces u_{T_n}(T_n⁻) at the thresholds T_n = ½log n to u_T at the multiplicatively related
thresholds ½log(nm)? That is the only non-linear place left for Λ*1 = log in this flow.
