# R162_405 — G1.4: right minimality at the enlarged window T_* + δ

Round 4, mechanism G1.4.

Status: **NO-GO (PROVED) for sign extraction, with three PROVED STEPS.** Gate 1 is not closed.

- PROVED STEP 1 (§2, exact collar identity). Let F ∈ N_{T_*} and let F_δ be any eigenvector at
  T' = T_* + δ, H_{T'}F_δ = λ_δF_δ. Then **λ_δ⟨F_δ, F⟩ = ⟨ξ_F^{δ}, F_δ⟩_{collar}**, where ξ_F^δ is
  the exterior residual of F on the two collars C_δ = {T_* < |t| < T'}. There is no interior term,
  no Tate term and no λ-dependence in ξ_F^δ.
- PROVED STEP 2 (§3, right minimality = non-extendability). (R) holds at T_* iff some F ∈ N_{T_*}
  has ξ_F^δ ≠ 0 for every δ > 0. Equivalently, the zero extension of that F is not in ker H_{T'} for
  any T' > T_*. The Lemma-5 limit vector G of R162_101 is such an F. Plateaus to the right are
  excluded by the definition of T_*. Interior plateau windows are exactly the windows where every
  kernel vector extends.
- PROVED STEP 3 (§4, the limit of the divided identity). Dividing the identity of Step 1, or the
  Brown–Halmos identity (R162_404 Thm 4.1) at T', by λ_δ and letting δ → 0 gives only the
  normalization 1 = lim ⟨ξ_F, F_δ⟩/λ_δ. The Tate-jet term λ_δ⟨Γ_PF_δ, φ⟩ converges to 0 after
  division and gives the tautology ⟨Γ_PF, φ⟩ = ⟨Γ_PF, φ⟩. With the Möbius-conjugated tests
  Φ = ΠZ_{T_*}^{±1}F, every correction is a collar pairing ⟨ξ_Φ, F_δ⟩. None of these identities
  constrains R_LF.
- NO-GO (§5). The sign λ_δ < 0 is the strict version of lem:monoT. It is the sign of the collar
  pairing ⟨ξ_F, F_δ⟩. That pairing involves the collar profile of F_δ, which F does not determine, and
  only one scalar combination of the Gamma residues. The same sign holds for the ground state at
  **every** window where λ_A strictly decreases, including windows with λ_A > 0 (F1). All identities
  depend on λ only through λ_δ − λ(T_*). λ_δ/δ is not determined: on the available domain
  λ_δ = o(δ^{1/2}), and the first δ-derivative vanishes when ξ_F is bounded.

Notation follows R162_404 (form 𝔞_T = 𝔪_T − ⟨(B_T + B_T^*)·,·⟩; κ(x) = −Σ_j e^{−a_j|x|} is the
off-diagonal kernel of M; μ_F(a) = ∫e^{at}F; K_F(a) = ∫e^{−at}F; μ_F = εK_F; a_j = 2j + ½; ℓ_d =
Λ(d)d^{−1/2}). E is zero extension from I_{T_*} to I_{T'}. N = N_{T_*} = ker H_{T_*}, and
H_{T_*} ≥ 0.

## 0. Corpus check

- **P124_004.** That note uses dilation transport and a crossing quotient (1.1) with no sign. The Euler
  quotients cannot be differentiated on 𝒬 (§4 there), and birth terms carry no rate. The present note
  uses **no** transport and **no** derivative. Step 1 is an exact identity at fixed δ. It pairs the
  *true* ground state at T' against the *zero extension* of F. That is admissible because
  E𝒫_{T_*} ⊂ 𝒫_{T'} isometrically (lem:monoT). This is the identity that P124_004 §3 tried to reach
  through (3.3)–(3.4): the "Tate-normal term" there is replaced here by ξ_F, and the Tate multiplier
  cancels exactly (Lemma 2.1).
- **R162_101 §3, Lemma 5.** (R) gives only upper bounds on λ_A, and a kernel vector is a right limit.
  This note sharpens both. The upper bound becomes an exact identity, Step 1. Selection becomes a
  characterization: the limit vector is non-extendable, Step 2.
- **R162_404 §§4–6, §8.** Thm 4.1 and Cor. 5.2 are used at T'. The "Möbius-conjugated test" that
  §8 asked for is treated in §4.3.
- **R160 survey / R161.** No entry treats the exterior residual as the carrier of (R).

## 1. The exterior residual

For F ∈ N and δ > 0 define a distribution ξ_F^δ on C_δ = (−T', −T_*) ∪ (T_*, T'):

    ξ_F^δ(t) = MF(t) − ((B_{T'} + B_{T'}^*)F)(t) − r(t),       t ∈ C_δ,               (1.1)

where r ∈ span{e^{±t/2}} is the Tate vector of F at T_* (eq:localweak), extended by the same
exponential formula. Explicitly, since F vanishes on C_δ:

- on (T_*, T'): MF(t) = −Σ_j e^{−a_jt}μ_F(a_j) (R162_404 §4), B_{T'}^*F = 0, and
  (B_{T'}F)(t) = Σ_{d<e^{2T'}} ℓ_d F(t − log d);
- on (−T', −T_*): MF(t) = −Σ_j e^{a_jt}K_F(a_j), B_{T'}F = 0, and
  (B_{T'}^*F)(t) = Σ_{d<e^{2T'}} ℓ_d F(t + log d).

The j-series converges for |t| > T_*. Its sum is ∫κ(t − u)F(u)du. It has at most the Hilbert-type
singularity ½∫F(u)du/(t − u) as |t| ↓ T_*. For |t| < T' it defines an element of the dual of
𝒬 ∩ L²(C_δ), by Hilbert's inequality as in the proof of R162_404 Thm 4.1.

**Lemma 1.1 (Gamma tail is faithful).** If F ≠ 0, the Gamma part −Σ_j e^{−a_jt}μ_F(a_j) does not vanish
identically on any interval (T_*, T_* + δ).

*Proof.* It equals −e^{−t/2}g(e^{−2t}), where g(z) = Σ_j μ_F(a_j)z^j. The series g is analytic on
|z| < e^{2T_*}, because |μ_F(a_j)| ≤ e^{a_jT_*}‖F‖_{L¹}. Suppose it vanished on an interval. Then
g ≡ 0 on the disc of convergence, so every μ_F(a_j) = 0. By faithfulness of R (Paper 47),
F = 0. ∎

## 2. The exact collar identity (PROVED STEP 1)

**Lemma 2.1.** For F ∈ N and η ∈ 𝒫_{T'} ∩ 𝒬,

    𝔞_{T'}(EF, η) = ⟨ξ_F^δ, η|_{C_δ}⟩.                                               (2.1)

*Proof.* Split η = η_i + η_c, with η_i = P_{T_*}η and η_c = η1_{C_δ}. Both parts lie in 𝒬 by
R162_404 Lemma 1.2.

(a) Interior part. Zero-extension invariance of the form gives 𝔞_{T'}(EF, η_i) = 𝔞_{T_*}(F, η_i).
The new integers d ∈ [e^{2T_*}, e^{2T'}) contribute ⟨ℓ_dV_{log d}F, η_i⟩ = 0, because V_{log d}F is
supported in t > log d − T_* ≥ T_*. By eq:localweak (the equation holds for every test in 𝒬∩L²(I),
with H_{T_*}F = 0), this equals ⟨r, η_i⟩. Now η is primitive on I_{T'}, so
⟨e^{±t/2}, η_i⟩ = −⟨e^{±t/2}, η_c⟩. Hence ⟨r, η_i⟩ = −⟨r, η_c⟩.

(b) Collar part. F and η_c have disjoint supports, apart from a null set. So 𝔪(F, η_c) is the
kernel pairing ∫∫κ(t − u)F(u)η_c(t). The local parts of M (the constant −log π and the constants in ψ)
do not contribute. The prime part is −⟨(B_{T'} + B_{T'}^*)F, η_c⟩.

Adding (a) and (b) gives (2.1). ∎

**Theorem 2.2 (collar identity).** Let F_δ ∈ 𝒫_{T'} ∩ dom H_{T'} with H_{T'}F_δ = λ_δF_δ. Then for
every F ∈ N,

    λ_δ ⟨F_δ, EF⟩ = ⟨ξ_F^δ, F_δ|_{C_δ}⟩.                                               (2.2)

*Proof.* EF ∈ 𝒫_{T'} ∩ 𝒬 is an admissible test in the eigen-equation of F_δ, and ⟨r_δ, EF⟩ = 0.
So 𝔞_{T'}(F_δ, EF) = λ_δ⟨F_δ, EF⟩. The form is symmetric (real pairing), so apply (2.1) with η = F_δ. ∎

Remarks. (i) ξ_F^δ contains neither λ_δ nor λ(T_*) = 0. For an eigenvector F with H_{T_*}F = λF at
an arbitrary window, the same proof gives

    (λ_δ − λ)⟨F_δ, EF⟩ = ⟨ξ_F^δ, F_δ|_{C_δ}⟩,                                          (2.2λ)

with the same formula (1.1). This is the source of the F1 failure in §5.
(ii) The Gamma residues μ_F(a_j) enter (2.2) only through the collar pairings
∫_{C_δ}e^{∓a_jt}F_δ. These are moments of F_δ on a set of measure 2δ.

## 3. Right minimality is non-extendability (PROVED STEP 2)

Let V_δ = {F ∈ N : ξ_F^δ = 0 in (𝒫_{T'}-collar)′}. Equivalently, EF ∈ ker H_{T'}, by (2.1) and the
Cauchy–Schwarz argument of R162_101 Lemma 2.

**Theorem 3.1.** (a) If ξ_F^δ ≠ 0 for some F ∈ N, then λ_A(T_* + δ) < 0.
(b) V_δ is a subspace of N that increases as δ ↓ 0. It stabilizes at some V_0 for δ < δ_0.
(c) (R) holds at T_* iff V_0 ≠ N, that is, iff some F ∈ N has ξ_F^δ ≠ 0 for every δ > 0.
(d) Let F_{δ_k} be negative ground states with F_{δ_k} → G (R162_101 Lemma 5). Then G ⊥ V_0, and
ξ_G^δ ≠ 0 for all δ > 0.
(e) Let T_1 < T_* with λ_A = 0 on [T_1, T_*] (a left plateau). At an interior window T of the plateau,
every kernel vector extends: V_0(T) = N_T. A right plateau does not exist, because
T_* = inf{λ_A < 0}.

*Proof.* (a) Pick η ∈ 𝒫_{T'} ∩ 𝒬 with c := 𝔞_{T'}(EF, η) ≠ 0. Then
𝔞_{T'}(EF + sη) = 2sc + s²𝔞_{T'}(η), because 𝔞_{T'}(EF) = 𝔞_{T_*}(F) = 0. This is negative for small
s with sign(s) = −sign(c).
(b) The restriction of a functional vanishing on the δ-collar vanishes on the δ′-collar for δ′ < δ, so
V_δ increases as δ decreases. N is finite-dimensional.
(c) If V_0 = N, then for δ < δ_0 the whole of EN lies in ker H_{T'}. By (R), λ_δ < 0, and (2.2) gives
⟨F_δ, EF⟩ = 0 for all F ∈ N. The Lemma-5 limit of F_δ lies in N (unit norm) and is orthogonal to N.
That is a contradiction. The converse is (a).
(d) Apply (2.2) with F ∈ V_0: λ_{δ_k}⟨F_{δ_k}, EF⟩ = 0 and λ_{δ_k} ≠ 0, so ⟨G, F⟩ = 0. Then
G ∉ V_0, and V_δ ⊂ V_0 gives ξ_G^δ ≠ 0.
(e) Let T < T_2 be windows in the plateau. Then H_{T_2} ≥ 0 and 𝔞_{T_2}(EF) = 0, so EF ∈ N_{T_2}
(R162_101 Lemma 2). The second statement is the definition of T_*. ∎

So (R) is equivalent to the open condition "N ≠ V_0". By Lemma 1.1, failure of this condition would
require an exact cancellation on the collar: MF = (B + B^*)F + r on C_δ. The Gamma tail is analytic
there, while the comb term consists of translates of F. This is the precise distinction between first
contact and a plateau window. The task statement asked for exactly this distinction, and it is PROVED.

## 4. Dividing by λ_δ and passing to the limit (PROVED STEP 3)

Take δ = δ_k → 0 with F_δ → G ∈ N, G ⊥ V_0.

**4.1 (Collar identity.)** (2.2) with F = G gives ⟨ξ_G^δ, F_δ⟩/λ_δ = ⟨F_δ, EG⟩ → 1. This is a
statement about the *rate* at which the collar pairing vanishes. It contains no equation on G.

**4.2 (Exterior/Tate-jet channel, R162_404 Cor. 5.2 at T').** For φ ∈ C_c^∞((−∞, −T_* − δ_1)) and
δ < δ_1,
λ_δ⟨Γ_PF_δ, φ⟩ = 𝔞_{T'}(F_δ, Γ_P^*φ) − ⟨Γ_Pr_δ, φ⟩ (take P ≥ e^{2T'}). Divided by λ_δ, the left
side is ⟨Γ_PF_δ, φ⟩ → ⟨Γ_PG, φ⟩, because Γ_P is bounded on L². So the right side divided by λ_δ
converges to the Tate-jet/polar functional of G. But that functional is a *linear function of G*
(R162_404 Prop. 5.1). The limit statement is therefore "lim (RHS_δ/λ_δ) = ⟨Γ_PG, φ⟩". It is a
statement about the right side, which is 0/0 in the limit, and it places no condition on the jets of G.
The jets do enter with coefficient λ_δ ≠ 0, as the task anticipated. After division they occur on
both sides with coefficient 1, and they cancel.

**4.3 (Möbius-conjugated tests.)** For Φ ∈ 𝒫_{T_*} ∩ dom, (2.1) with EΦ in place of EF gives
λ_δ⟨F_δ, EΦ⟩ = ⟨H̃Φ, P_{T_*}F_δ⟩ + ⟨ξ_Φ^δ, F_δ|_{C_δ}⟩. Here H̃ is the interior action including r_Φ,
and ξ_Φ^δ is defined by (1.1) with the Tate vector of Φ. For Φ = ΠZ_{T_*}G, Thm 4.1 gives
H̃Φ = Π(Z_{T_*}r − 𝔡(G, ·)). Two further effects occur:
- Z_{T'} differs from EZ_{T_*}. The new integers n ∈ [e^{2T_*}, e^{2T'}) and the overflow of old shifts
  add pieces supported in C_δ.
- The defect 𝔡_{T'} gains the new Gamma weights n^{−s_j}.
Every one of these extra terms is a collar pairing ⟨·, F_δ|_{C_δ}⟩. Since ⟨H̃Φ, G⟩ = 𝔞(Φ, G) = 0,
dividing by λ_δ gives

    ⟨G, Φ⟩ = lim [⟨H̃Φ, P_{T_*}(F_δ − G)⟩ + ⟨ξ_Φ^δ, F_δ|_{C_δ}⟩] / λ_δ.                (4.1)

Suppose the response vector w = lim (P_{T_*}F_δ − G)/λ_δ existed. It does not exist on the available
domain: P124_004 §4 shows the Euler quotients have no rate. Then (4.1) would be the linear-response
equation (H_{T_*})w = G − (collar source), modulo N. By (2.2λ), that equation holds with H − λ in
place of H for every simple branch at every window. So it constrains G no more than the eigen-equation
does.

**4.4 (Order in δ.)** From (2.2) and Cauchy–Schwarz,
|λ_δ| ≤ (1 + o(1))‖ξ_G^δ‖_{𝒬′(C_δ)}‖F_δ‖_{𝒬(C_δ)}. If ξ_G is bounded near ±T_*, then ‖ξ_G^δ‖_{L²} =
O(δ^{1/2}). Since ‖F_δ|_{C_δ}‖_{L²} → 0, this gives λ_δ = o(δ^{1/2}). The exact ratio λ_δ/δ is
⟨ξ_G^δ, F_δ⟩/δ. It depends on the collar profile of F_δ, which G does not determine. Heuristically, the
Schur complement on the collar gives λ_δ ≈ −⟨ξ, 𝒞_δ^{−1}ξ⟩, where the collar block satisfies
𝒞_δ ≳ log(1/δ) (log-Sobolev on an interval of length δ). That would give λ_δ = O(δ/log(1/δ)), so
λ_δ/δ → 0 and there is no first-order term. This is not claimed as PROVED, because it needs a lower
bound for the collar block on 𝒫_{T'}.

## 5. Decision (NO-GO, PROVED)

**Theorem 5.1.** Every consequence of (R) that can be obtained from the identities (2.1), (2.2) and
(4.1), from R162_404 Thm 4.1 or Cor. 5.2 at T' = T_* + δ, and from the limit δ → 0, is one of the
following:
(a) the eigen-equation at T_* or at T';
(b) the non-extendability N ≠ V_0 of Thm 3.1;
(c) the sign statement sign⟨ξ_G^δ, F_δ|_{C_δ}⟩ = sign λ_δ < 0.
None of (a)–(c) implies R_LF = 0, for any L injective on N.

*Proof.* (a) R162_404 Thm 3.1 and Thm 6.1. (b) is an open, nonvanishing condition. By Lemma 1.1 it
holds as soon as the comb and Tate terms fail to cancel the analytic Gamma tail on the collar. That is
compatible with μ_F(a_j) ≠ 0 for all j, and it is even implied by F ≠ 0 together with non-cancellation.
It cannot produce the closed condition R_LF = 0. (c) Write m_δ = ∫_{C_δ^+}F_δ. Freezing e^{−a_jt} at
t = T_* expresses the Gamma part of the pairing through the one scalar Σ_j e^{−a_jT_*}μ_G(a_j), times
m_δ, plus errors controlled by the collar profile. m_δ is a datum of F_δ, and its sign is not fixed
by G. So (c) is one inequality between collar data of F_δ and one linear functional of G. The
L-vector R_LG remains free, and no equation on it results.

Finally, (2.2λ) shows that (c) is the strict monotonicity λ_A(T + δ) < λ_A(T). That holds for the
ground state at every window where λ_A strictly decreases (F1 below). ∎

**Exact obstruction.** λ_δ < 0 supplies a **sign**, but it is the sign of the spectral difference
λ_δ − λ_A(T_*), not of λ_A itself. Every identity derived here is covariant under λ ↦ λ − c. The sign
of λ_A(T_*) enters only through eq:Qspectral, and eq:equivgate has already exhausted it. So right
minimality adds exactly one thing beyond H_{T_*} ≥ 0 and N ≠ 0: the open non-extendability condition
(Thm 3.1).

## 6. Falsifiers

- **F1 (spectral).** Take a window T with λ_A(T) > 0, a ground state F, and λ_A strictly decreasing at
  T. By continuity (R162_001) and lem:monoT, strict decrease holds except on plateaus. Then (2.2λ)
  gives (λ_δ − λ)⟨F_δ, EF⟩ = ⟨ξ_F, F_δ⟩ < 0, which is the same sign as in (c). Thm 3.1 also holds
  verbatim, with "F does not extend as an eigenvector with eigenvalue λ". By eq:Qspectral, such F has
  R_LF ≠ 0 for L injective on span F. So any argument through (a)–(c) would prove a false statement at
  such T. Plateau windows: interior plateau windows are excluded by Thm 3.1(e), since all their kernel
  vectors extend. That is the only thing (R) distinguishes, and it is **not** a vanishing statement.
- **F2 (Weil sign).** Replacing 𝔞 by −𝔞 exchanges the ground state with the top of the spectrum, and
  (2.2) holds verbatim. The mechanism has no orientation.
- **F3 (finite modifications, Davenport–Heilbronn).** Replace Λ by a = Λ + η_0 with η_0 finitely
  supported. Lemma 2.1, Thm 2.2 and Thm 3.1 use only three facts: zero-extension invariance,
  disjointness of supports in the collar, and the eigen-equation. So they hold with ℓ_d → a(d)d^{−1/2}.
  Lemma 1.1 involves only M. For the Davenport–Heilbronn form, the Gamma factor is the same up to the
  archimedean parameters, the Dirichlet coefficients enter only through the comb in (1.1), and first
  contacts do occur. At the Davenport–Heilbronn first contact, Thm 3.1 gives a non-extendable kernel
  vector with nonzero residues. Nothing in §§2–5 is Λ-specific, and Λ*1 = log is never used. The
  step that would have to be Λ-specific is the one this note shows to be missing: an *equation*
  forced on the non-extendable vector. That would require the collar residual (1.1) to be linked to
  R_LF by a Λ*1 = log identity. The candidate is the compressed Chebyshev identity B^*Z_T = K_T
  (R162_404 Prop. 2.3) applied to ξ, which is not used here.
- **F4.** Only δ → 0 limits of exact identities are taken. The only unproved heuristic, §4.4, is
  marked as such and is not used.

## 7. Next sub-lemma

Minimality is now fully spent. Left minimality is equivalent to H_{T_*} ≥ 0 (R162_101 Lemma 1). Right
minimality is equivalent to non-extendability N ≠ V_0 (Thm 3.1). Neither yields an equation. Gate 1
through minimality needs an *arithmetic* statement about the collar residual.

**G1.5 (collar residual and the Chebyshev identity).** Compute ξ_G^δ, for the non-extendable vector
G, through the compressed Chebyshev identity B^*Z_{T'} = K_{T'} applied across the threshold e^{2T_*}.
Then decide whether there is a Λ-specific identity relating
(i) the boundary data of the analytic Gamma tail Σ_j e^{−a_jt}μ_G(a_j) at t ↓ T_* to
(ii) the comb term Σ_d ℓ_dG(t − log d).
Such an identity must fail for Λ + η_0. If G1.5 is also NO-GO, the minimality line (G1.x) is
exhausted, and Gate 1 needs an independent lower bound on λ_A to the right of T_* (R162_101 §6.2).

GATE 1: OPEN. Row D: OPEN.

Files edited: this file only.
