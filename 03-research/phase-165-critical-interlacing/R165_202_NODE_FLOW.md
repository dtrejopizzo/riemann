# R165_202 — Node flow in T and the node–zero Cauchy identity (task A4, R165_000 §2.3)

* Pure mathematics, no numerics. No file outside this one was edited. No label of record moves.*
*Inputs: R165_000 §2.3; R163_401 §1, §2.2–2.4, §3, §4.6–4.7, Lemma 4.10; R163_501 Thm B, Thm R; R162_407 §3 (REG, virial);
R164_501 Thm SA / Cor SA.1; Paper 47 `lem:monoT`, `lem:contT`, `lem:firstcontact`.*

Labels: **PROVED** (full proof here), **PROVED-CITED** (record reference, not re-audited), **ARGUED** (argument given, the
unproved step named), **OPEN**. **Code E1**: the statement uses only (1.1), the kernel equation and W ≥ 0. So it holds verbatim
for M_m, f_t and f_χ, and it cannot separate ζ.

## Status table

| # | statement | label |
|---|---|---|
| 1.1 | **No jumps.** For T<T′, W_{T′}\|_{L²(I_T)} = W_T (zero extension). The family is one form W_∞ on growing domains | PROVED |
| 1.2 | Activation of n at 2T = log n: the new term is −v_n Re⟨a,b⟩ on the two edge strips of width ε = 2T′−log n. It is bounded with norm v_n/2 and spectrum {−v_n/2, 0, +v_n/2}, with infinite multiplicity in both signs (also in each parity sector). It is not finite rank and it is indefinite | PROVED |
| 1.3 | Rescaled family Q_T on L²(−1,1) has a fixed form domain. Q_{T′}−Q_T is relatively form-bounded with relative bound → 0 (rate C/log(1/\|T′−T\|)). So the resolvent is norm-continuous and on a simple stretch the eigenprojection is continuous | PROVED |
| 1.4 | Virial / Hellmann–Feynman: D⁺λ(T) ≤ −𝒱_T(F_T)/T ≤ D₋λ(T), and λ′ = −𝒱_T(F_T)/T where λ is differentiable | PROVED under (REG) for the single vector F_T (R162_407) |
| 1.5 | Formal Hadamard principle: 𝒱_T(F_T) = 0 whenever DF_T := ½F_T + tF_T′ lies in 𝒟_T. A strict decrease of λ is therefore carried by the edge singularity of F_T | ARGUED (the differentiability of T ↦ F_T in form norm is not proved) |
| 1.6 | **Real-rootedness along the whole flow.** At every T, a bottom eigenvector of W_T has at most dim E_T − 1 non-real zeros. If λ_T is simple, the bottom eigenvector is real-rooted | PROVED (transfer of R163_501 Thm B + R(a)–(e) to any T) |
| 1.7 | On every T-interval where λ_T is simple, the nodes x_j(T) move continuously (Hurwitz) and stay real. They cannot leave the axis or be born on it from complex pairs. New nodes enter only from ∞ | PROVED |
| 1.8 | Node velocity ẋ_j = −(1/T)[x_j + Ĝ_T(x_j)/F̂_T′(x_j)], G_T = R_T^⊥𝒱_TF_T: an inward dilation drift plus a virial correction | ARGUED (needs (REG) and 𝒱_T F_T ∈ 𝒟_T*) |
| 1.9 | Monotone (inward or outward) motion of the nodes | OPEN. Only the dilation part is signed (inward) |
| 1.10 | Simplicity of the bottom eigenvalue inside one parity sector | OPEN. At parity crossings the bottom vector changes and the nodes jump |
| 2.1 | **Generalised Gauss quadrature at every T**: (W_T−λ_T)(H_x,H_y)=0 for x≠y; W(G)−λ‖G‖² = Σ_x w_x(λ)\|Ĝ(x)\|² on span{H_x}, w_x(λ) ≥ 0 | PROVED |
| 3.1 | **Node–zero Cauchy identity.** S(z):=Σ_ρ G(t_ρ)²/(t_ρ−z) − (λ_T/2π)∫G(τ)²/(τ−z)dτ satisfies S(x)=0 and S′(x)=d_x(λ) ≥ 0 at every node | PROVED (E1) |
| 3.2 | **Separation by Rolle.** At the contact, if two consecutive nodes x<x′ have no charged on-line zero between them, then some ξ∈(x,x′) satisfies Σ_on G(γ)²/(γ−ξ)² = −S_off′(ξ) ≤ Σ_off \|G(t_ρ)\|²/\|t_ρ−ξ\|² | PROVED (E1) |
| 3.3 | **Local interlacing theorem.** On an interval where S_on′ > \|S_off′\|, nodes and charged on-line zeros strictly interlace: at most one node per gap of charged zeros, and at least one charged zero between consecutive nodes | PROVED (E1) |
| 3.4 | **Crowding hierarchy.** On a gap where S_on^{(2j+1)} > \|S_off^{(2j+1)}\| there are at most 2j+1 nodes. For off-line zeros at distance ≥ D from a gap of length ℓ the hypothesis improves geometrically in (ℓ/D)² | PROVED (E1) |
| 3.5 | **Quartet sign lemma.** A negative-mass pair (Re g²<0, g=G(t_q)) contributes positively to S′ near γ_q (at ξ=γ_q its contribution is +2\|Re g²\|/δ²) and negatively for \|ξ−γ_q\| ≫ δ. The quartet's own core reinforces separation; it can break separation only at distance ≳ δ | PROVED |
| 3.6 | Finite-configuration count: nodes ≤ (number of charged poles) + 2k (k = number of off-line pairs) | PROVED for finite configurations. The localisation to ζ is ARGUED |
| 3.7 | **Does the contact force critical interlacing (EC) in the quartet cell?** No, in the form stated in R165_000 §2. The forced notion is separation from *charged* zeros outside off-line domination zones. EC with all on-line zeros is not forced (nodes may sit on zeros, which then carry no charge), and EC fails in the lattice model | PROVED (model, 4.1), E1 |
| 2.2 | Counts: \|nodes in [γ*±Δ]\| ≈ 2ΔT_c/π and \|zeros\| ≈ 2Δρ do not localise (Cartwright density is global; the S(t) error is O(log γ*)) | PROVED (as a negative statement) |
| 4.1 | Lattice model (Lemma 4.10): the quartet cell is separated but not interlaced (L/(2T*) > 1 zeros per node gap; ratio → 1 only as δL ↓ y₀). The model satisfies 3.5 (S_off′(γ)=2\|g\|²/δ² > 0) | PROVED in the model (asymptotic node spacing; the first gaps are ARGUED) |
| 4.2 | M_m: 3.1–3.6 hold verbatim, and M_m has a first contact (R163_801 Thm 5). Separation/interlacing is therefore compatible with contact and cannot prove RH | PROVED-CITED (E1) |
| (★_cell) | | OPEN (unchanged) |

## §1 The family in T

**1.1 (No jumps). PROVED.** Let F ∈ L²(I_T), extended by zero, and T<T′. Then c_F(u)=0 for |u| ≥ 2T. So every comb term
with log n ∈ [2T, 2T′) vanishes on F, and σ_{T′} and σ_T give the same value. A, B and the archimedean part do not depend
on T. Hence W_{T′}(F)=W_T(F). Write W_∞(F) := (1/2π)∫m|F̂|² − Σ_{n≥2}v_n Re c_F(log n) + 2Re(A B̄). For each compactly
supported F the sum is finite. Then W_T = W_∞|_{L²(I_T)}, and the jumps of σ_T at 2T = log n are invisible to the forms. ∎
(This is the structural reason behind `lem:monoT` and `lem:contT`.)

**1.2 (Activation; sign structure). PROVED.** Let 2T′ = log n + ε with 0 < ε < 2T′ − log n′ for the next activating
n′. For F ∈ L²(I_{T′}), c_F(log n) = ∫_{T′−ε}^{T′}F(t)\overline{F(t−log n)}dt. Put a(s)=F(T′−ε+s) and b(s)=F(−T′+s) on [0,ε].
Then c_F(log n)=⟨a,b⟩, and the new term is q_n(F) = −v_n Re⟨a,b⟩. As a form on L²(strip_R)⊕L²(strip_L) this is
−(v_n/2)[[0,1],[1,0]], with eigenvalues ∓v_n/2 on a = ±b, each of infinite multiplicity, and 0 on functions supported
off the strips. Hence ‖q_n‖ = v_n/2 and q_n is indefinite and not compact.
In the parity sectors: if F is even, b(s) = F(T′−s) = a(ε−s), so c = ⟨a,Ra⟩ with R the reflection of [0,ε]. Then
q_n = −v_n⟨a,Ra⟩ is negative on strip profiles symmetric about the strip midpoint and positive on antisymmetric ones,
both with infinite multiplicity. If F is odd, the sign is reversed. Size: |q_n(F)| ≤ v_n‖F 1_{edge strips}‖². ∎
*Reading.* An activation lowers the form exactly on functions whose two edge strips are log n-translates of each other
(log n-periodic at the edge). The effect is first order in the edge mass, not in ε.

**1.3 (Fixed-domain rescaling; continuity). PROVED.** Put F(t)=T^{−1/2}f(t/T) with f ∈ L²(−1,1). This map is unitary.
Then F̂(τ)=T^{1/2}f̂(Tτ), c_F(u)=c_f(u/T), and
Q_T(f) := W_T(F) = (1/2π)∫m(s/T)|f̂(s)|²ds − Σ_{log n<2T}v_n Re c_f(log n/T) + 2T Re(A_T(f)\overline{B_T(f)}),
with A_T(f)=∫f(u)e^{Tu/2}du and B_T(f)=∫f(u)e^{−Tu/2}du. The form domain 𝒟 = {∫log(2+|s|)|f̂|²<∞} does not depend on T.
Differences, for |T′−T| = h small:
- the archimedean part: |m(s/T′)−m(s/T)| ≤ sup|τm′(τ)|·|log(T′/T)|, since τm′ is bounded. This is a bounded form of size O(h);
- the polar part: rank 2, entries continuous in T;
- the old comb points: |c_f(u′)−c_f(u)| ≤ (1/2π)∫min(2,|s||u′−u|)|f̂|² ≤ C(1/log R + Rh)‖f‖_𝒟². Choosing R = h^{−1/2} gives
  C′/log(1/h);
- newly activated points: |c_f(u)| ≤ ‖f1_{strip_{2−u}}‖². By compactness of 𝒟 ↪ L² (proof of `thm:O`) and 1_{strip_ε} → 0
  strongly, sup_{‖f‖_𝒟≤1}‖f1_{strip_ε}‖ → 0.
So Q_{T′}−Q_T has relative form bound → 0. By Kato (VI §3, form version), R(Q_{T′}) → R(Q_T) in norm. An isolated simple
eigenvalue therefore has a norm-continuous spectral projection, and the eigenvector f_T (suitably phased) is continuous in L²,
and in 𝒟 as well. ∎ (The rate C/log(1/h) is the same as R162_407 §2.)

**1.4 (Virial derivative). PROVED under (REG) for F_T.** For a fixed f, d/dT Q_T(f) = −(1/T)𝒱_T(F), with F = U_Tf and
𝒱_T(F) = (1/2π)∫τm′(τ)|F̂|²dτ − Σ_{log n<2T}v_n log n·Re c_F′(log n) + 𝒯_T(F),
𝒯_T(F) = −2T·Re[Ȧ B̄ + A \overline{Ḃ}], with TȦ = ½A + ∫F(t)(t/2)e^{t/2}dt and TḂ = ½B − ∫F(t)(t/2)e^{−t/2}dt.
(Archimedean part: ∂_T m(s/T) = −(s/T²)m′. Comb part: ∂_T c_f(log n/T) = −(log n/T²)c_f′(log n/T) = −(log n/T)c_F′(log n).
Polar part: direct differentiation.) Except for the convention on the Tate term, this is the virial form (3.1) of R162_407.
Envelope: λ(T±h) ≤ Q_{T±h}(f_T)/‖f_T‖² with equality at h=0. This gives D⁺λ(T) ≤ −𝒱_T(F_T)/T ≤ D₋λ(T) (unit F_T),
provided T ↦ Q_T(f_T) is differentiable, i.e. c_{F_T} ∈ C¹ near the comb points (REG). Monotonicity then gives
𝒱_T(F_T) ≥ 0 wherever λ′ exists. ∎ At an activation instant (log n = 2T) the comb derivative enters through c_F′(2T⁻).
For F continuous up to ±T this equals −F(T)\overline{F(−T)}, which vanishes when F vanishes at the edge.

**1.5 (Hadamard principle). ARGUED.** With f fixed, ∂_TU_Tf = −(1/T)DF, where D = ½+t∂_t is anti-symmetric on
L²(ℝ). D preserves supp ⊂ [−T,T]. So formally d/dT Q_T(f) = −(2/T)Re W_∞(F,DF). If DF ∈ 𝒟_T, the eigen-equation gives
W(F,DF) = λ⟨F,DF⟩, and Re⟨F,DF⟩ = ½‖F‖² − ½‖F‖² + boundary terms [t|F|²]_{−T}^{T} = 0, because DF ∈ L² forces
F(±T)=0. Hence 𝒱_T(F_T) = 0. A strictly decreasing λ (as on the approach to T_c, where λ ↓ 0) requires DF_T ∉ 𝒟_T, i.e.
an edge singularity. *Unproved step:* the identification of d/dT Q_T(f_T) with the formal commutator in form sense.
The boundary behaviour of ground states of log-symbol forms is not established here; R162_407's (REG) is the same gap.

**1.6 (Real-rootedness at every T). PROVED.** R163_501 Thm B (the Blaschke flip M_w preserves ‖F‖, L²(I_T) and W_T,
because |b_w|=1 on ℝ and b_w(i/2)\overline{b_w(−i/2)} = 1) does not use λ = 0. The variational characterisation
"F ∈ E_T ⟺ W_T(F)=λ_T‖F‖²" (compact resolvent) holds at every T. Hence R(a)–(c) of R163_501 apply verbatim to E_T =
bottom eigenspace of W_T. If F ∈ E_T has k non-real zeros, the functions F̂P/Q (deg P ≤ k) lie in Ê_T and give dim E_T ≥ k+1.
So k ≤ dim E_T − 1, and when λ_T is simple, k = 0. The proof of R(c),(e) runs in a single parity sector. ∎
*Consequence.* Real-rootedness is not a special property of the contact. It holds along the whole bottom branch wherever
the branch is simple.

**1.7 (Continuity of nodes). PROVED.** On a simple stretch J, F_T → F_{T₀} in L² with supports in a fixed compact set. So
F̂_T → F̂_{T₀} locally uniformly on ℂ. By Hurwitz, the zeros in each bounded window vary continuously (as a multiset). By
1.6 they are all real for each T ∈ J, so no pair can leave or enter the axis. A real zero of a real (resp. imaginary)
function on ℝ can only collide with another and stay real. The number of nodes in [−R,R] (endpoints not nodes) is locally
constant. When full support holds, the Cartwright/Levinson density n_T(R) = (2T/π)R + o(R) increases with T, so nodes
come in from ∞. ∎ (Full support holds at every T where λ is strictly decreasing from the left. If conv supp F_T =
[−T′,T′] with T′ < T, then λ is constant on [T′,T].)

**1.8 (Node velocity). ARGUED.** Let λ_T be simple, assume (REG), and suppose 𝒱_T extends to an operator with
𝒱_TF_T ∈ 𝒟_T*. First-order perturbation in the rescaled frame gives ∂_Tf_T = (1/T)R_T^⊥𝒱̂_Tf_T. Then, from
F̂_T(x) = T^{1/2}f̂_T(Tx) and the implicit function theorem at a simple node,
  ẋ_j = −(1/T)·[ x_j + Ĝ_T(x_j)/F̂_T′(x_j) ],  G_T := R_T^⊥𝒱_TF_T  (original variables).
The first term is the pure dilation drift (inward at speed |x_j|/T, exactly the densification T/π). The second term is the
virial correction. **1.9:** a sign for x_j + Ĝ_T(x_j)/F̂_T′(x_j) is not available. Monotone motion is OPEN, and nothing in
the record forces it. (In a de Branges chain the zeros move monotonically, but W_T is not a de Branges chain: R163_401
§4.11, Kreĭn/dB are E1.)

**1.10 (Crossings). OPEN.** Even and odd bottoms can cross (this is the parity-crossing count of R163_501). At a crossing the
bottom vector changes and the nodes jump. Simplicity within one parity sector is not proved.

## §2 Quadrature along the flow; counts

**2.1 (Gauss quadrature at every T). PROVED.** Let F ∈ E_T be real-rooted with simple nodes, Ĥ_x = F̂/(z−x), and
K̂ = F̂/((z−x)(z−y)), x ≠ y. W_T and ⟨·,·⟩ both depend on a pair only through Φ̂Ψ̂^# (eq. (1.1) and Plancherel). Hence
(W−λ)(H_y,H_x) = (W−λ)(K,F) = 0, because F is an eigenvector. Since W − λ ≥ 0, on span{H_x}:
W(G) − λ‖G‖² = Σ_x w_x(λ)|Ĝ(x)|², with w_x(λ) = (W−λ)(H_x)/|F̂′(x)|² ≥ 0. ∎ At λ = 0 this is 2.4(iii).

**2.2 (Counts do not localise). PROVED (negative).** The Cartwright density of nodes is asymptotic. A real-rooted type-T
function can have arbitrarily long zero gaps (divide sin Tz by finitely many of its factors: the type is unchanged and
the result stays in PW). So the number of nodes in [γ*±Δ] is not determined by T_c. The on-line count has error
O(log γ*) (S(t) = O(log t)), which exceeds the difference 2Δ|T_c/π − ρ| = O(Δ) unless Δ ≫ log γ*. Hence "interlacing by
counting, cell by cell" (R165_000 §2) cannot be derived from T_c = T_L(γ*) + O(1), even if (Det±) is assumed. The right
local object is the identity of §3.

## §3 The node–zero Cauchy identity and what it forces

Let F be real, parity-definite and real-rooted in E_T, with simple nodes X. Put G = F̂ (even) or −iF̂ (odd); G is real on ℝ
and F̂F̂^# = G². Write g_ρ := G(t_ρ). By Lemma 3.0 of R163_401, Σ_ρ|g_ρ|² < ∞.

**Theorem 3.1 (Cauchy identity). PROVED (E1).** Put
S(z) := Σ_ρ g_ρ²/(t_ρ − z) − (λ_T/2π)∫_ℝ G(τ)²/(τ−z)dτ.
S is meromorphic, real on ℝ off its poles. Its poles are the *charged* on-line ordinates (G(γ) ≠ 0) and the off-line
t_ρ. The integral is regular on ℝ at nodes, since G(x)=0. For every node x: S(x) = 0 and S′(x) = d_x(λ) := (W−λ)(H_x) ≥ 0.
*Proof.* (W−λ)(F,H_x) = 0 because F is an eigenvector. By (1.1) and Plancherel, with F̂Ĥ_x^# = G²/(z−x), this equals
S(x). Likewise (W−λ)(H_x) = Σ g_ρ²/(t_ρ−x)² − (λ/2π)∫G²/(τ−x)² = S′(x), and it is ≥ 0 by 2.1. Convergence: Σ|g_ρ|²/|t_ρ−z|
converges locally uniformly off the poles. ∎
At the contact λ = 0 and S = S_on + S_off, where
S_on(z) = Σ_{charged γ}G(γ)²/(γ−z) and S_off(x) = Σ_{off-line pairs}2Re[g²/(t−x)] (real-analytic on ℝ).
*Before the contact* the Lebesgue term −(λ/2π)∫G²/(τ−x)² < 0 opposes the monotonicity of S_on. As T ↑ T_c it vanishes.

**Theorem 3.2 (separation by Rolle). PROVED (E1).** At T_c, let x<x′ be consecutive nodes with no charged on-line
ordinate in (x,x′). Then S is analytic on [x,x′] and S(x)=S(x′)=0. By Rolle there is ξ with S′(ξ)=0, i.e.
  Σ_{charged γ}G(γ)²/(γ−ξ)² = −S_off′(ξ) ≤ Σ_{ρ off}|g_ρ|²/|t_ρ−ξ|².
So a node gap with no charged zero is possible only where the off-line field has a negative derivative at least as large
as the full on-line Cauchy–Poisson sum. ∎

**Theorem 3.3 (local interlacing). PROVED (E1).** Let J be an interval with S_on′ > |S_off′| on J ∖ {poles}. On each gap
of consecutive charged zeros in J, S increases from −∞ to +∞ (S_off is bounded there), so it has exactly one zero. Hence
J contains at most one node per gap. By 3.2, every gap between consecutive nodes in J contains a charged zero. So X∩J and
the charged on-line zeros in J strictly interlace. ∎ If the whole line were off-line-free, the whole configuration would
interlace. That case is vacuous, because under RH there is no contact.

**Theorem 3.4 (crowding hierarchy). PROVED (E1).** Since S_on^{(2j+1)}(x) = (2j+1)!Σ G(γ)²/(γ−x)^{2j+2} > 0, if on a
charged gap S_on^{(2j+1)} > |S_off^{(2j+1)}|, then S^{(2j+1)} > 0. So S′ has at most 2j zeros, and S has at most 2j+1
zeros (an odd number), in particular at most 2j+1 nodes. Since |S_off^{(2j+1)}(x)| ≤ (2j+1)!Σ_off|g|²/|t−x|^{2j+2}, the
hypothesis holds as soon as G(γ_k)²/ℓ^{2j+2} > N_off/D^{2j+2}, where γ_k is an endpoint of the gap, ℓ its length,
D = dist(gap, off-line ordinates) and N_off = Σ_off|g|². This holds for j ≳ log(N_off/G(γ_k)²)/(2log(D/ℓ)). ∎
*Reading.* Far below γ* (D ≥ γ* − x ≥ 3·10¹² − x) a node gap without charged zeros needs the charged masses there to be
smaller than N_off(ℓ/D)^{2j+2}. The witness *can* do this: it can be negligible at low heights and have few nodes there
(2.2). So there is no contradiction, only a quantitative localisation.

**Lemma 3.5 (quartet sign). PROVED.** For an off-line pair with t = γ_q − iδ and g² = |g|²e^{iθ}, the contribution to
S_off′ at ξ is 2Re[g²/(t−ξ)²] = 2|g|²cos(θ+2φ)/r², where t−ξ = re^{−iφ}. At ξ = γ_q (φ = π/2) it equals −2Re(g²)/δ². For
|ξ−γ_q| ≫ δ (φ → 0 or π) its sign is that of cos θ. Negative mass (Re g² < 0, the light cone of R163_401 Lemma 3.1)
therefore *reinforces* separation on a δ-core around γ_q (for θ = π, exactly on |ξ−γ_q| < δ). It can only break
separation outside the core, with strength ≤ 2|g|²/(ξ−γ_q)². ∎

**Lemma 3.6 (finite count). PROVED for finite configurations.** If S_on has N real poles with positive residues and
S_off is a real rational function of degree d = 2k vanishing at ∞, then S has at most N + d − 1 real zeros. *Proof.*
S_on = −A/B, with deg B = N and deg A = N−1, and S_off = P/Q, with deg P < deg Q = d. The numerator −AQ + PB has degree
≤ N+d−1. ∎ So nodes exceed charged poles by at most 2k − 1. *Localisation to ζ (infinitely many terms): ARGUED only.*
The far field is analytic but not a rational function of bounded degree, and the bound would need a Jensen lower value
of G at a centre, which is not available.

**Theorem 3.7 (answer to the key question). PROVED (E1 + model).** At the first contact:
(i) separation is forced in every interval where |S_off′| < S_on′ (3.2–3.3). It fails at most inside off-line negative
zones, at distance ≳ δ from negative-mass quartets (3.5);
(ii) critical interlacing in the sense of R165_000 §2 (EC: one *on-line zero of ζ*, charged or not, between consecutive
nodes, and conversely) is **not** forced. Nodes may sit on zeros, which then drop out of S. Two or more charged zeros
per node gap cost nothing (S just has extra non-node zeros). In the lattice model (4.1) the contact is strictly
sub-Landau and EC fails in the quartet cell;
(iii) no direction of (i) gives (★_cell). All of §3 is E1 and holds at M_m's contact (4.2). ∎
*Reformulation of the proposal's object.* EC should be replaced by **(SEP_J)**: on J, nodes are separated by charged
on-line zeros. Then (SEP_J) ⟸ S_on′ > |S_off′| on J, and ¬(SEP_J) ⟹ the Rolle inequality 3.2 at some ξ ∈ J. The
Hermite–Biehler remark of R165_000 §2.1 is this: under 3.3, G and the product over charged zeros have interlacing real
zeros, and S is their Herglotz ratio.

## §4 Tests

**4.1 Lattice model (R163_401 Lemma 4.10). PROVED in the model.** For T < πρ = L/2, a type-2T function sampled at rate ρ
gives Σ_nG((n+α)/ρ)² = ρ∫G² (Poisson, no aliasing). The extremal is G(s) ∝ ∫_0^T sinh(δu)sin(su)du, which is odd with
a node at γ (local 0). Asymptotically its nodes are spaced π/T* (zeros of the leading term cos(sT)sinh(δT)/s). The
lattice spacing is 2π/L, so a node gap holds ≈ L/(2T*) > 1 lattice points. The quartet cell is therefore **separated
but not interlaced**. The ratio tends to 1 only as δL ↓ y₀ (T* → L/2), and for δL ≫ 1, T* ~ log(2δL)/(2δ) ≪ L/2.
The single pair ±iδ has g² = −|g|² (G odd, real: G(iy) ∈ iℝ). So S_off(x) = 2|g|²x/(x²+δ²) and S_off′(0) = 2|g|²/δ² > 0,
as Lemma 3.5 predicts. The node at the cone vertex sits in the reinforcing core. (The node spacing of the first few gaps is
ARGUED, from the explicit integral, not computed.)

**4.2 M_m. PROVED-CITED (E1).** M_m has ζ's on-line zeros and off-line zeros and a first contact (R163_801 Thm 5,
record). Theorems 3.1–3.6 use only (1.1), the kernel equation and W ≥ 0, so they hold there verbatim. Hence separation and
interlacing, in any form derivable here, coexist with a contact. They are not a contradiction mechanism.

## Ledger

- New PROVED tools: 1.1 (no jumps), 1.2 (activation spectrum ±v_n/2), 1.3 (norm-resolvent continuity, rate 1/log),
  1.6 (real-rootedness for every T with simple bottom), 1.7 (continuous real nodes), 2.1 (quadrature at λ ≠ 0),
  3.1 (Cauchy identity S(X)=0, S′=d_x), 3.2 (Rolle separation), 3.3 (local interlacing), 3.4 (crowding hierarchy),
  3.5 (quartet sign), 3.6 (finite count), 3.7 (EC not forced).
- ARGUED: 1.5 (Hadamard: dλ/dT is an edge effect), 1.8 (node velocity), the localisation of 3.6.
- OPEN: 1.9 (monotone nodes), 1.10 (simplicity within a parity sector), (REG), (★_cell).
- Corrections to R165_000: (b) "jump" is wrong: activation is continuous and indefinite (1.1–1.2). The counting route to
  cellwise interlacing does not localise (2.2). EC is the wrong object; (SEP_J) for charged zeros is the forced one (3.7).
- Code: §3 is entirely **E1**. Row D stays OPEN.

## Grid cells

- **7E** (zero side × flow/family in T): +PROVED-TOOL 1.1, 1.3, 1.6, 1.7, 2.1. Route "monotone node flow ⟹ interlacing at
  T_c": OPEN at 1.9, and even a positive answer would only give 3.7(i), which is E1. Mark PARTIAL/E1.
- **7A** (zero side × one window): +PROVED-TOOL 3.1–3.6. Route "the contact forces EC in the quartet cell": DEAD [E1;
  lattice-model counterexample 4.1; M_m 4.2]. Residual: (SEP_J) is forced off negative zones. This does not move (★_cell).
