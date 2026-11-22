# R186_038 — The S2 box: three seeds, a truncation lemma, and the edge fold as an object

Phase 186, round 18. No numerics (no number decides anything here; there is no script r038). Paper 46, grid and
crossword are not touched.

Read: R186_032 §4 (Ω: S1–S6); R186_036 (Lemma 1, Lemma 2, Theorem 3, Cor 3.2); R186_035 Lemma 3.1 (E_ψ = −2∫R₁φ′);
R186_022/023/103 (peak of ĥ*, phases cos(s log p), 3.7/T law of h_a, one FALSIFIED mode); R165_202 1.4–1.8 (virial, Hadamard,
real-rootedness, nodes); R162_407 (REG, Prop 4.3); R163_401 §4.8 ((★_cell), Rem 4.8a); R164 README ((TC), Thm R); R166_501
Cor A.2 ((G),(N)); R166_802 Thm 1–4, Prop 2.1; R166_801 (nodal identity of the fourth moment, Prop 3.1); R185_005 §1 (𝔐, atoms
L/D/C/Q); SIGN-REAUDIT §3 and I16 of the crossword (no Grönwall by dilation); R186_004 §Prop 2.1; grid §4 (M_m, f_t,
DMV, P_{a,c}); Paper 46 thm:A/eq:Aform, lem:K, lem:monoT, lem:mbounds, lem:contA, thm:Z.

Notation (Paper 46): I_T = [−T,T]; c_F(u) = ∫F(t)F(t+u)dt (F real), supp c_F ⊂ [−2T,2T]; 𝒩_T = {n: log n < 2T};
v_n = 2Λ(n)/√n; 𝔞_T(F) = C₀‖F‖² + Lev(c_F) − Σ_{𝒩_T} v_n c_F(log n); 𝒫_T = {A(F) = B(F) = 0}; λ_A(T) = min 𝔞_T|𝒫_T;
h*_T unit minimizer; T_n := ½log n (entry instant of n); G = F̂ = ĥ*; 𝒱_T the virial of R165_202 1.4.

## 0. One-line verdict

**None of the three seeds is Ω; the S2 box remains blank.** What is proved: (Lemma 0) in every quadratic form with
Toeplitz/Hankel kernel on L²(I_T), Λ beyond e^{2T} is invisible; therefore S2 forces (i) tests of support > 2T built
nonlinearly from F (degree ≥ 4: seed β, = fourth moment, closed), (ii) the zero side ((★_cell)/(TC), OPEN without an
object), or (iii) dynamics in T (seed α), where each prime power enters only at its own instant T_n and through the
*current* window: S2 holds with respect to T₀, never with respect to the moving window.
From (α) three new lemmas are left PROVED: **α.1** (the fold is the coefficient of cos(x log n) in the asymptotics
x²|ĥ*(x)|², i.e. the amplitude of the asymptotic nodal lattice, not the individual nodes), **α.2** (every prime power
enters as a cost in the even sector and as a payment in the odd sector; concave/convex fold according to parity),
**α.3** (Grönwall at the minimizer ⟺ 𝒱_T(h*_T) ≤ T c(T) λ_A(T); c superexponential by Thm M; at a contact 𝒱 = 0:
λ_A margin, S3 NO). From (γ): **γ.1** (the fixed-frequency alignment sum is dominated by the polar term; the
arithmetic enters at relative order e^{−T(1−2δ)}, this is R166_802 Thm 3). **No contact with the sign.**

## 1. Lemma 0 — where Λ beyond the window can enter (PROVED, elementary)

**Lemma 0.** Let 𝔔(F) = ∫∫ k(t,s)F(t)F(s) dt ds on L²(I_T) with k(t,s) = κ₁(t−s) + κ₂(t+s), κ_i tempered
distributions (Toeplitz + Hankel). Then 𝔔 depends on κ₁, κ₂ only through their restrictions to [−2T, 2T]. In
particular, if κ₁ = Σ_n v_n(δ_{log n} + δ_{−log n})·(weight), only n < e^{2T} contributes.
*Proof.* t, s ∈ I_T ⟹ t − s, t + s ∈ [−2T, 2T]. ∎
*Reading.* (a) The prime part of 𝔞_T, the archimedean part (Toeplitz with κ₁ = K) and the polar part (Hankel: A(F)B(F) =
∫∫e^{(t−s)/2}F F) are all within the reach of the lemma; that is why, with a test F of support I_T, the explicit
formula truncates on its own at e^{2T} and Λ|[e^{2T},∞) only appears through the zeros (thm:Z, cor:nontermwise). (b) A
quadratic form with general kernel k(t,s) can indeed carry any data, but it is "fixed basis with coefficients in Λ" and
falls into W-lin (R186_026 Thm 3.3, R186_031 Dom; CITED). (c) Hence **S2 ⟹ one of three**: degree ≠ 2 in F with
effective support > 2T (F∗F̃, G²K with K of type Δ: family P of R166_802), the zero side, or T-dependence of the
objects (family {h*_T}). The three seeds are exactly (iii), (i), (iii)+(i).

## 2. Seed (α): the entry fold as an equation

### (a) Precise object
Correction to the statement: the fold of R186_036 Lemma 2 acts on the **slope**, not on the value. Under
(REG) (R162_407 §3) and λ_A simple on an interval J with no entry instants, λ_A′(T) = −𝒱_T(h*_T)/T (R165_202 1.4, PROVED
under (REG)), with
 𝒱_T(F) = (1/2π)∫τ m′(τ)|F̂|² dτ − Σ_{log n<2T} v_n log n · c_F′(log n) + 𝒯_T(F), 𝒯_T polar.
The correct equation for (α) is the **slope budget** (CONDITIONAL (REG), simplicity):
 λ_A′(T⁺) = λ_A′(T₀⁺) − Σ_{T₀<T_n≤T} 2v_n h*_{T_n}(T_n) h*_{T_n}(−T_n) + ∫_{T₀}^T d[−𝒱_s(h*_s)/s]_{cont}, (α.0)
where the last term is the continuous variation between entries, and
 λ_A(T) = λ_A(T₀) − ∫_{T₀}^T 𝒱_s(h*_s) ds/s. (α.0′)
(α.0′) expresses λ_A(T) with the primes of all intermediate windows (n < e^{2s}, s ≤ T) and with the minimizers
h*_s; the prime power n enters starting at s = T_n, through c′_{h*_s}(log n) and through its initial fold.

### (b) S1–S6 verification
- S1: at each s, (α.0′) is quadratic in h*_s; the nonlinearity comes only from the selection of the minimizer (window
 data). Projective degree 2 per window. **NOT in the sense of R186_032 §1.**
- S2: Λ(n) with log n > 2T₀ enters, but only from s ≥ T_n, i.e. inside the current window (Lemma 0): never
 "beyond the window" in which it is evaluated. **NO with respect to the moving window; yes, vacuously, with respect to T₀.**
- S3: the inequality that would close (α) is Grönwall; by Lemma α.3 it is equivalent to 𝒱_T(h*_T) ≤ T c(T) λ_A(T): a
 sign of size λ_A. **NO.**
- S4: it is neither an identity nor one-sided positivity nor a class property; it is dynamics. Yes.
- S5: it couples the minimizer with atomic Λ only at the entry T_n, through the number h*_{T_n}(T_n)² (Lemma α.1): the
 node set enters only through its asymptotic lattice (universal). **Coupling of a single number per prime.**
- S6: f_t shares h*_s for s < T₁ (Theorem 3(a) of R186_036), so (α.0), (α.0′) and any inequality about them on
 [T₀, T₁) are identical for ζ and f_t; M_m shares the fold (same atomic part, lem:contA). (α) formally escapes Theorem 3
 (it uses h*_s, not only λ_A), but the only stretch that distinguishes ζ is [T₁, ∞), where for f_t the inequality
 must fail before T_c(f_t): its content is that of Lemma α.3(c). **Vacuous admission.**

### (c) Lemmas (proved in §5)
α.1 edge amplitude ↔ asymptotic nodal lattice; α.2 entry cost by parity; α.3 Grönwall ⟺ virial bound of
λ_A margin, superexponential c, 𝒱 = 0 at a contact; α.4 NO-GO of the uncertainty/Bernstein route.

### (d) Falsifier
From α.1–α.2: a minimizer h*_T with h* ∈ W^{1,1}(I_T), G real-rooted and |h*(T)| ≠ |h*(−T)| (impossible by α.1(ii)); or
an entry instant T_n in the even sector with a positive slope jump. From α.3: a bound 𝒱_T(h*_T) ≤ T c(T) λ_A(T) with
explicit c proved without a per-window certificate: this would be the S2 input (it does not exist; R186_036 §6).

### (e) Cross-check
R186_036 Lemma 2 (fold, value); R162_407 Prop 4.3 ("the sign near the endpoint depends on the product of boundary
values of F, not on the prime density": the same fact, in bound form); R165_202 1.5 (Hadamard: 𝒱 = 0 ⟺ no boundary
singularity, ARGUED); SIGN-REAUDIT §3 / I16 (there is no Grönwall q′₁ ≥ −Cq₁ by dilation at fixed F: PROVED
negative; here the version is about the minimizer, which is true if D is true, with c = 𝒱(h*)/(Tλ_A), and empty
without an independent bound); R186_004 Prop 2.1 ("Grönwall would need to bound ∫λ′, the same problem with one fewer
scalar"). The identification of the fold with the asymptotic Fourier coefficient and the nodal lattice (α.1) is not in
the corpus (grep "boundary values", "F(T)F(−T)", "edge amplitude" in phases 162–186: only R162_407 Prop 4.3 and R186_036).

## 3. Seed (β): the tail of the form at node frequencies (autocorrelation squared)

### (a) Precise object
By Lemma 0, the only way for the *form* to see Λ beyond e^{2T} at the node frequencies of G is a test of larger
support built from F. The simplest: H := F∗F̃ (autocorrelation), supp H ⊂ I_{2T}, Ĥ = G² (G real on ℝ),
 𝔖_T(F) := 𝔞_{2T}(F∗F̃) = C₀‖c_F‖² + Lev(c_F∗c_F) − Σ_{n<e^{4T}} v_n (c_F∗c_F)(log n).
Degree 4 in F; Λ up to e^{4T}; for log n ∈ (2T, 4T), (c_F∗c_F)(log n) = ∫c_F(u)c_F(log n − u)du couples pairs of
window scales with u + u′ = log n (multiplicative structure n = ab, log a + log b = log n). Ĥ = G² vanishes to order 4 at the nodes.
**Lemma β.1 (PROVED).** F ∈ 𝒫_T ⟹ F∗F̃ ∈ 𝒫_{2T}, and 𝔖_T(F) ≥ λ_A(2T)‖F∗F̃‖².
*Proof.* A(F∗F̃) = ∫∫F(t)F(s)e^{(t−s)/2} = A(F)B(F) = 0; B(F∗F̃) = B(F)A(F) = 0. The bound is the definition of λ_A(2T). ∎
**Lemma β.2 (zero side; PROVED).** For a quartet at t_q = γ_q − iδ_q the contribution to the zero side of 𝔖_T is
2Re G(t_q)⁴ + 2Re G(−t_q)⁴: the same Re(z²) structure as in 𝔞_T with z = G(t_q)², phase 4φ instead of 2φ.
*Proof.* Ĥ(z) = G(z)·\overline{G(z̄)} = G(z)² for G real on ℝ; the quartet computation of R166_802 §1 with G ↦ G². ∎

### (b) S1–S6 verification
S1 yes (projective degree 4). S2 yes (Λ in (e^{2T}, e^{4T}), evaluated through c_F∗c_F, with order 4 at the nodes). S3
**NO**: by β.1 the positivity of 𝔖_T on 𝒫_T is implied by λ_A(2T) ≥ 0 and is a sign of size λ_A(2T)‖H‖²; as a
statement for every T it is "D at 2T over the autocorrelation cone", class 𝔉 (R186_036 Theorem 3): regression. S4: it
is a restriction of D. S5: couples nodes (order 4) with Λ in (e^{2T}, e^{4T}); yes. S6: f_t with N₀ > e^{4T} shares
𝔖_T; M_m shares the atomic side; vacuous admission.

### (c) First lemma
β.1–β.2 (proved). With averaging over translations a ↦ e^{iau}F∗F̃, the quartet becomes positive ∫G⁴ and loses the
phase: R166_801 Prop 3.1 (PROVED there; NO-GO as a route, E1/f_t).

### (d) Falsifier
f_t (N₀ > e^{4T}): shares 𝔖_T and has a witness. For "positivity on the cone of squares ⟹ D at T": the cone
{F∗F̃} ⊊ 𝒫_{2T}, does not generate it (the elements of 𝒫_{2T} are differences of autocorrelations); no implication in
either direction except β.1.

### (e) Cross-check
R166_801 ("nodal identity of the fourth moment", Prop 3.1: positive, phaseless, does not constrain ω(E)); R164_491 F5 /
Cor SA.1 (polynomial staircase W(zΦ̂) = 0, E1); SIGN-REAUDIT §2 ("the fourth moment is a universal norm; none of it
contributes the sign"); grid item 46 (bispectrum, fourth moment NO-GO). **(β) is closed in the corpus; here only the
window form 𝔖_T and β.1–β.2 are written down.** NO-GO as Ω.

## 4. Seed (γ): phase alignment of future primes with the minimizer frequency

### (a) Precise object
ω := s*(T), peak frequency of |ĥ*_T|² (plateau ±0.5, R186_103 §1; window data, degree 0 in F: admissible by (G)).
For φ ∈ C_c^∞(2T, 2T+Δ), φ ≥ 0:
 𝔖_γ(T) := Σ_n v_n cos(ω log n) φ(log n) (smoothed: the raw sum Σ_{p≤x} v_p cos(ω log p) grows like x^{1/2}).
Connection with (α): if h*_s(t) = A cos(ωt) + r (one mode), h*_s(s)² = ½A²(1 + cos(2ωs)) + O(r), and at the entry
2T_p = log p: fold = −v_p A²(1 + cos(ω log p)) + O(r). The sum of folds on (T, T+Δ) is −A²Σ v_p(1 + cos(ω log p))φ: this
is 𝔖_γ plus the phaseless term. The one-mode model is FALSIFIED (R186_023 §2, R186_103 #9, #13).

### (b) Lemma γ.1 — polar dominance (PROVED-CITED: explicit formula + δ_q < ½)
For fixed ω and φ as above,
 𝔖_γ(T) = 2∫ e^{u/2} cos(ωu) φ(u) du − Σ_ρ Re[ φ̃(t_ρ − ω) + φ̃(t_ρ + ω) ] + O(1), φ̃(t) := ∫φ(u)e^{iut}du (without
weight e^{u/2}),
where the zeros on the line contribute O(‖φ̃‖_{decay}·log T) = O(1) uniformly (log γ density and decay of φ̃), and a
zero with β_ρ = ½ + δ contributes O(e^{2Tδ}). Since the main term is ≍ e^{T}·Re[e^{iωu₀}·(…)] (u₀ ∈ supp φ) and δ < ½
for every zero (I2 of R163_401, PROVED-CITED), **the sign of 𝔖_γ(T) is decided by the polar/archimedean term**, explicit
in (ω, T, φ), and the arithmetic (zeros, hence atomic Λ) enters at relative order ≤ e^{−T(1−2δ_max)}.
*Proof.* Explicit formula for the test u ↦ e^{−u/2}φ(u)cos(ωu) (compact support in (2T, 2T+Δ)): the Λ term is
Σ Λ(n)n^{−1/2}φ(log n)cos(ω log n) = ½𝔖_γ; the polar term is ∫e^{u/2}φ cos(ωu); the zeros enter through the transform
at t_ρ ± ω with weight e^{(β−½)u}; the archimedean term is O(1) by supp φ ⊂ (2T, ∞) and the decay of K. ∎

### (c) S1–S6 verification and verdict
S1: degree 0 in F (via ω): yes formally. S2: Λ beyond the window at a minimizer frequency: yes formally;
but the statement is **linear in Λ** at a fixed frequency: R166_802 Thm 1 (a single test: only a lower bound excludes,
and it is equivalent to an inequality on the sum over zeros) and Thm 3 (the fluctuation exponent is Θ − ½) apply
word for word with K localized at ω. S3: by γ.1 the sign of 𝔖_γ has no arithmetic content; the content is in the
remainder o(e^T), whose control at exponent < δ_q is zero localization. **NO.** S6: Beurling DMV (grid §4)
has PNT with error, the same polar term and zeros off the line: shares γ.1 and the sign of 𝔖_γ; M_m shares
atomic Λ. **Failed admission.** Equidistribution (Weyl/Vinogradov)? For fixed ω, {ω log p mod 2π} is equidistributed
with discrepancy of a zero-free region (dlVP/VK; CITED): that is precisely the remainder o(e^T) of γ.1, of exponent ½ − o(1)
(not ½ − δ′): it decides nothing by R166_802 Thm 3, and the transfer to Λ uses Perron. **NO-GO as Ω.**

### (d) Falsifier
Beurling DMV; any system with PNT and a quartet at δ < ½ (M_m). Falsifier of γ.1: a φ ≥ 0 on (2T, 2T+Δ) with
𝔖_γ(T) of sign opposite to the polar term for large T (impossible by the proof).

### (e) Cross-check
R186_022/023/103 (peak of ĥ*, plateau; cos(s log 2) on [½log2, ½log3]: window data); R186_036 Cor 3.2 (every alignment
condition is window data or an input on Λ outside the window); R166_802 Prop 2.1 and Thm 3 (twisted sum over γ_q:
exponent Θ − ½); phase 136 (sign = polar coupling: γ.1 reproduces it). The polar dominance of the alignment sum
was not written as a lemma; it is the quantitative form of the "the band does not decide" of prop:negtrace.

## 5. Choice: (α). Proofs of α.1–α.4

**Lemma α.1 (edge amplitude = asymptotic nodal lattice). PROVED.** Let h ∈ W^{1,1}(I_T) be real (absolutely continuous
up to the boundary), extended by 0, G = ĥ. Then, as |x| → ∞,
 x²|G(x)|² = h(T)² + h(−T)² − 2h(T)h(−T)cos(2Tx) + o(1) = |h(−T) − h(T)e^{−2iTx}|² + o(1).
Consequences: (i) the fold of R186_036 Lemma 2, Δλ_A′(T_n) = −2v_n h*(T_n)h*(−T_n), is v_n times the coefficient of
cos(x log n) in the asymptotics of x²|ĥ*_{T_n}(x)|²: **the prime power n couples to the minimizer, at its entry, through
the Fourier coefficient at frequency log n = 2T_n of the high-frequency tail of the spectral density**, i.e. through the
amplitude of the asymptotic nodal lattice (nodes at spacing π/T ⟺ oscillation of |G|² at frequency 2T). (ii) If moreover
G is real-rooted with zero density T/π (Cartwright), then |h(T)| = |h(−T)|, and the asymptotic nodes lie at kπ/T
(h(−T) = h(T)) or at (k+½)π/T (h(−T) = −h(T)); the coupling reduces to **one number per prime**, h*(T_n)², with sign
∓ according to parity: the *set* of nodes enters only through its asymptotic lattice, which is universal (it depends
on T and parity), and never through individual nodes.
*Proof.* By parts, ĥ(x) = ∫_{−T}^T h e^{−ixt}dt = [h(−T)e^{ixT} − h(T)e^{−ixT}]/(ix) + (ix)^{−1}∫h′(t)e^{−ixt}dt, and the
last term is o(1/x) by Riemann–Lebesgue (h′ ∈ L¹). Multiplying by x and taking the squared modulus gives the formula.
(ii): along the zeros x_k → ∞ of G, the left-hand side is 0, so the liminf of the right-hand side is 0; the minimum of
|h(−T) − h(T)e^{−iθ}|² over θ is (|h(T)| − |h(−T)|)², whence |h(T)| = |h(−T)|; with h(−T) = εh(T), ε = ±1, the
right-hand side is 2h(T)²(1 − ε cos 2Tx), vanishing at kπ/T (ε = 1) or (k+½)π/T (ε = −1). ∎
*Scope.* W^{1,1} up to the boundary is (REG) in the form used by R186_036 Lemma 2; it is OPEN for h*_T (domain H^{log}, no
trace: R186_036 §4). Real-rootedness of ĥ* is PROVED for the background of W_T at simple λ (R165_202 1.6) and is assumed
here for 𝔞_T|𝒫_T (CONDITIONAL).

**Lemma α.2 (entry cost by parity). PROVED.** Let F ∈ L²(I_T) be real, continuous at ±T. Then c_F(2T − ε) =
ε F(T)F(−T) + o(ε) as ε ↓ 0. Hence: (i) for F even with F(T) ≠ 0, c_F > 0 in a left neighborhood of 2T, and the
term of a prime power n with 2T − log n = ε small is −v_n c_F(log n) = −ε v_n F(T)² + o(ε) < 0 (**cost**); for F odd it
is +ε v_n F(T)² (**payment**). (ii) Under (REG) and simple λ_A, Δλ_A′(T_n) = −2v_n h*(T_n)² ≤ 0 if h*_{T_n} is
even, ≥ 0 if odd: in the even sector every entry is a **concave fold**; in the odd sector, convex. (iii) Between
consecutive entries λ_A′ = −𝒱_T(h*_T)/T ≤ 0 is continuous (if h*_T is continuous at T, lem:contA + simplicity).
*Proof.* c_F(2T − ε) = ∫_{−T}^{−T+ε}F(t)F(t + 2T − ε)dt = εF(−T)F(T) + o(ε) by continuity. (ii) is R186_036 Lemma 2 with
h*(−T_n) = ±h*(T_n) (𝒫_T and 𝔞_T are invariant under t ↦ −t: A ↔ B, c_F even; at simple λ the minimizer has definite
parity). (iii) R165_202 1.4 and lem:monoT. ∎
*Reading.* In the even sector (that of h* across the whole grid, R186_023 §1, NUMERICAL) the entering primes can only
worsen the slope; any "help" from the primes to λ_A lies in the continuous variation of (α.0), i.e. in the
readjustment of c′_{h*_s}(log n) after the entry, not in the entry itself.

**Lemma α.3 (Grönwall at the minimizer). PROVED (modulo CITED).** Let J = [T₀, T₁] without a contact, (REG) and λ_A
simple on J, c ∈ L¹(J), c ≥ 0. Then:
(a) λ_A′ ≥ −cλ_A on J ⟺ 𝒱_T(h*_T) ≤ T c(T) λ_A(T) = T c(T) 𝔞_T(h*_T) on J; and in that case λ_A(T₁) ≥ λ_A(T₀)exp(−∫_J c).
(b) If (a) holds for ζ on [T₀, T] with T ≥ T₀(ε), then ∫_{T₀}^T c ≥ e^{(2−ε)T} − log(1/λ_A(T₀)) (Paper 48 thm:M(b),
CITED: λ_A(T) ≤ exp(−e^{(2−ε)T})): c is superexponential on average; there is no c of polynomial size nor exponential
e^{aT}, a < 2.
(c) If λ_A(T_c) = 0 with λ_A > 0 to the left and (a) holds up to T_c with c finite, then 𝒱_{T_c}(h*_{T_c}) = 0 (from ≤ 0 and
𝒱 ≥ 0 by monotonicity): the flow stops at the contact; by R165_202 1.5 (ARGUED) that is "h*_{T_c} without boundary
singularity", and by α.1 that is equivalent to h*_{T_c}(±T_c) = 0 (zero lattice amplitude).
(d) The initial condition with an existing certificate is λ_A(½log5) ≥ 2.5·10⁻¹² (thm:log5A, CITED); with c ≡ 2e^{2T}·(1+o(1))
—the minimum compatible with (b)— bound (a) gives λ_A(T) ≥ 2.5·10⁻¹²·exp(−e^{2T} + 5) > 0 for every T: the scheme is
logically correct and **completely empty** without an independent proof of 𝒱_T(h*_T) ≤ 2T e^{2T} λ_A(T), which is a
statement of relative precision e^{−2T}·λ_A on the minimizer's virial (the archimedean virial (1/2π)∫τm′|ĥ*|² is
O(1) positive and must cancel against the comb's virial up to that margin): **the same cancellation of the form, in its
derivative**. S3 fails.
*Proof.* (a) λ_A′ = −𝒱/T (R165_202 1.4) and standard Grönwall (SIGN-REAUDIT §3 states the abstract lemma). (b) Integrate
(a) and use thm:M. (c) Pass to the limit in (a). (d) Arithmetic. ∎
*Escape from Theorem 3 (R186_036).* (a) is not a function of {λ_A(T′)} alone: it uses h*_T and 𝒱_T. But f_t shares h*_T
and 𝒱_T for T < T₁ (same form), so (a) on [T₀, T₁) is common; ζ and f_t differ only for T ≥ T₁, and there (a) must
fail for f_t before T_c(f_t) (by (c)). What distinguishes ζ is exactly (c) at every T: there is no contact with
𝒱 > 0; that is a statement about the size of λ_A.

**Lemma α.4 (uncertainty/Bernstein route). NO-GO (PROVED in the declared class).** There is no inequality of the form
h*_s(s)² ≤ κ(s)·λ_A(s) valid in the class {F ∈ 𝒫_s: F real-rooted} (nor in 𝒫_s) with finite κ: the form domain is
H^{log}, without a boundary trace (h ~ (T−t)^{−1/4} ∈ H^{log} with h(T) = ∞, R186_036 §4), and 𝔞_s is bounded below on the
sphere, so sup h(s)²/𝔞_s(h) = ∞. Restricted to the minimizer, the inequality is a statement about a single vector, of
margin λ_A (as in α.3(d)), and moreover it is not enough: Grönwall needs all of 𝒱, not only the folds (α.0). *Answer to
the question:* the fold lives at the **boundaries**, and by α.1 "boundary" = "asymptotic frequency of the nodal
lattice"; it does not live at individual nodes nor in Λ beyond the current window.

**Corollary α.5 (fold budget; CONDITIONAL (REG)).** From (α.0) and α.2(ii), in the even sector,
Σ_{T₀<T_n≤T} 2v_n h*_{T_n}(T_n)² = λ_A′(T₀⁺) − λ_A′(T⁺) + Var_cont[T₀,T], with Var_cont the variation of −𝒱/T between entries.
Without a bound on Var_cont nothing is deduced about h*(T_n)²; it is recorded as an accounting identity (W12).

## 6. Answer to the creation question and table

**What is the simplest object that satisfies S2 and has a provable first lemma?** By Lemma 0, an S2 object is one of
three types. Type (i), a test of support > 2T nonlinear in F: the simplest is 𝔖_T = 𝔞_{2T}(F∗F̃) (β), with β.1–β.2
proved; it is D at 2T over a cone (S3 NO) and is closed as a fourth moment. Type (ii), the zero side: (★_cell)/(TC),
without an object since phase 169. Type (iii), dynamics in T: the simplest is the entry fold (α), with α.1–α.3 proved;
it satisfies S2 only with respect to T₀ (each prime enters through its own window), and its closing inequality is of
λ_A margin (α.3). **The S2 box remains blank**; what this round adds is (1) the reduction S2 ⟹ (i)/(ii)/(iii) (Lemma 0),
(2) the exact identification of the prime ↔ minimizer coupling at entry: one number per prime, h*(T_n)², with sign by
parity, equal to the amplitude of the asymptotic nodal lattice at frequency log n (α.1–α.2), and (3) the polar
dominance of every fixed-frequency alignment sum (γ.1). None of the three is an arithmetic input: (1) is algebra, (2)
is a window identity (shared by M_m and f_t), (3) says the arithmetic enters at order e^{−T(1−2δ)}.

| object | label | S1 | S2 | S3 | S6 | verdict |
|---|---|---|---|---|---|---|
| Lemma 0 (Toeplitz/Hankel truncation) | PROVED | — | — | — | — | classification tool |
| (α) equation (α.0)/(α.0′) | CONDITIONAL (REG) | no | only vs T₀ | no | vacuous | NO-GO as Ω |
| α.1 edge amplitude ↔ nodal lattice | PROVED (W^{1,1}); (ii) CONDITIONAL real-rooted | — | — | — | — | new identity |
| α.2 entry cost by parity; concave fold | PROVED; (ii) CONDITIONAL (REG) | — | — | — | — | new identity |
| α.3 Grönwall ⟺ virial bound; superexp. c; 𝒱 = 0 at contact | PROVED (mod. thm:M, 1.4 CITED) | — | — | no | — | closes the Grönwall-at-the-minimizer route |
| α.4 Bernstein/uncertainty | NO-GO PROVED (traceless class) | — | — | — | — | — |
| (β) 𝔖_T = 𝔞_{2T}(F∗F̃); β.1, β.2 | PROVED (lemmas); NO-GO (route, CITED R166_801) | yes | yes | no | vacuous | closed (fourth moment) |
| (γ) 𝔖_γ(T); γ.1 polar dominance | PROVED-CITED | degree 0 | yes formal | no | fails (DMV, M_m) | NO-GO as Ω |

**Row D: OPEN.** No symbol of the grid changes; no new window is proposed; nothing is claimed about T > ½log5. **No
contact with the sign**: no statement in this file bounds λ_A from below nor produces a negative value.

## 7. Audit notes
1. α.1 uses h ∈ W^{1,1} up to the boundary; (REG) of R162_407 requires c_h ∈ C¹ near the comb, which is weaker at the
 boundary. Check whether c_h ∈ C¹ at 2T⁻ suffices for the asymptotics (yes for the coefficient of cos 2Tx: c_h′(2T⁻) =
 −h(T)h(−T) by R186_036 Lemma 2; the full formula of α.1 additionally needs h(T)² + h(−T)², i.e. c_h′ and the trace).
2. α.1(ii) assumes zero density T/π (full support); if conv supp h* = [−T′,T′] with T′ < T, replace T by T′
 (R165_202 1.7). 3. α.3(b) depends on thm:M(b) (Paper 48, CITED in the record); if it is withdrawn, (b) falls but (a),(c) do not.
4. γ.1: the O(1) of the zeros on the line requires φ̃ with decay ≥ 1/t² (φ ∈ C²); with φ only continuous it is O(log T).
5. Lemma 0 does not cover general kernels k(t,s); there W-lin is cited (R186_026 Thm 3.3), not reproved.
