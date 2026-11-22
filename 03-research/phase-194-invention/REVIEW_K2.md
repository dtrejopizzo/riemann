# REVIEW_K2 — line-by-line review of Theorem K2 (INV_K_001 §3)

 no equivalence with any other statement is
used or mentioned. No numerics.

## Verdict: **ARGUED** (not PROVED). PL and Borel–Carathéodory steps are correct (minor fixes F1–F3). The final step — the
"one-line adaptation" of Titchmarsh 8.12 — is a genuine gap (G1): the cited Ω-theorem does not give large |ζ| at points where
Q_φ is simultaneously aligned. K2 therefore stays at the level of INV_H_001 H1(iii) (ARGUED); the "upgrade ARGUED→PROVED" is withdrawn.

## 1. Conventions (checked)
- Paper 46 eq:symbol: s_T = m − Σ v_n cos(τ log n), v_n = 2Λ(n)n^{−1/2}, m = Re ψ(¼+iτ/2) − log π. INV_H_001 H1:
  Q_φ = −Σ φ(d)μ(d)(log d)d^{−s}, a_φ = coefficients of ζQ_φ, a_φ = Λ on n < N; s_φ = m − 2Re[ζQ_φ(½+iτ)]. Signs agree. OK.
- Class 𝓖_ac: Σ|φ(d)|(log d)d^{−1/2} < ∞ is exactly absolute convergence of Q_φ on σ ≥ ½ (coefficient φμ log). OK.
- s_φ ≥ −C ⇔ Re(ζQ)(½+it) ≤ ½(m(t)+C). Comparison correct. Fix F1: Paper 46 (l. 462) gives m = log(τ/2π) + O(1/τ),
  not O(1/τ²); harmless.

## 2. Phragmén–Lindelöf (correct)
- G_0 = ζQ − Q(1)/(s−1): holomorphic on ½ < σ, continuous to σ = ½ (Q absolutely convergent there). OK.
- u = Re G_0 − ½log|s+2| − C″ is subharmonic (harmonic minus harmonic), ≤ 0 on σ = ½ (hypothesis + Re of polar term bounded)
  and on σ = 2 (G bounded there; −½log|s+2| ≤ 0 helps). Finite order: |G_0| ≪ |t|^{1/2}, far below the double-exponential
  PL threshold for a strip of width 3/2. Conclusion Re G ≤ ½log|t| + O(1) on ½ ≤ σ ≤ 2, |t| ≥ 2. OK.

## 3. Borel–Carathéodory (correct with fix F2)
- Disc centre 3/2+it, R = 1 covers ½ ≤ σ ≤ 5/2, i.e. leaves the PL strip on 2 < σ ≤ 5/2. Fix F2: there G is bounded by
  absolute convergence, so Re G ≤ ½log|t| + O(1) holds on the whole disc. Pole s = 1 avoided for |t| ≥ 2.
- B–C: |G(s)| ≤ 2r/(R−r)·A + (R+r)/(R−r)|G(s_0)| with A = ½log|t|+O(1) ≥ 0, r = 1−δ: |G| ≪ δ^{−1}log|t| on σ ≥ ½+δ
  (factor 2/δ lost, correctly absorbed in ≪_δ). OK.

## 4. Ω-step (GAP G1)
- Titchmarsh Thm 8.12 is unconditional and stated for fixed ½ < σ < 1: log|ζ(σ+it)| = Ω((log t)^{1−σ−ε}). Range and
  status correct.
- The smooth-d alignment itself is fine (F3: write it): if ‖t log p/2π‖ ≤ 1/q for all p ≤ X, then
  |d^{−it} − 1| ≤ 2πΩ(d)/q ≤ 2π log d/(q log 2) for d ≤ X (all d ≤ X are X-smooth, so there are no "non-smooth d ≤ X"),
  hence |Q_X(σ+it) − Q_X(σ)| ≤ (2π/(q log 2))Σ|φ(d)|log²d·d^{−σ} (finite for σ > ½), and the tail Σ_{d>X}|φ(d)|log d·d^{−σ}
  → 0 uniformly in t. Uniform smallness of the tail: OK.
- **Gap.** The argument needs t with BOTH |ζ(σ+it)| ≥ exp((log t)^{1−σ−ε}) AND alignment for all p ≤ X(t) → ∞. Theorem 8.12
  only asserts existence of a sequence where ζ is large. Its proof (via Dirichlet's theorem and an averaging/mean-value
  comparison of log ζ with a short prime sum, using a zero-density input) yields a large value somewhere in a range
  attached to the aligned point, not at the aligned point, and the alignment for p ≤ X is not stable over that range
  (|t − t_0| must be ≪ 1/(q log X)). So "for such t, d^{−it} → 1" is not a corollary of the cited statement; it is a joint
  Ω-theorem for (ζ, (p^{−it})_{p≤X}) that must be proved — exactly the "not proved jointly with Q_φ" caveat of H1(iii).
- Not a fix: Bohr–Jessen/Bagchi joint value distribution gives positive density of t with |ζ| > A and Q aligned for each
  FIXED A, which does not beat the ≪ log t bound.

## 5. Possible repairs (OPEN)
R1. Re-run the 8.12 proof (or Montgomery's / resonance-method Ω proof) with the resonator multiplied by the alignment
condition for p ≤ X, carrying Q_φ through the averaging (Q_φ appears linearly; with X = (log t)^{c}). Needs to be written.
R2. Avoid Ω: work directly on σ = ½ with the hypothesis Re G ≤ ½log t + C and a high moment of ζQ (e.g. resonance method
for Re(ζQ) with Q in the resonator weight, Bondarenko–Seip type). Also to be written.
Either repair would upgrade K2 to PROVED; until then K2 = ARGUED and the exact-obstruction paragraph ("certifying gauge must
be a strict mollifier") is CONDITIONAL on G1.

## 6. K1 / §2
Not under review here; nothing in them depends on K2.
