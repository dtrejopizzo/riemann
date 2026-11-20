# Round 1 — Candidate K3: enlarged system of squares for the non-resonant crossings

Selection memo. Notation of `../phase-211-sign-sandbox/STATEMENT_001.md` and of
`../phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md` (cited "GRAM"); the note
`../phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md` is cited "GLOBAL". Labels: PROVED / CITED /
CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. "CITED" is also used for results PROVED in the
corpus that are not proved again here.

Design question. The resonant part R_res of the complete kernel A on integer scales is an exact sum of
squares indexed by the squarefree class (GRAM §17.2, RES-SOS). Is there an
ENLARGED system of squares, indexed additionally by exact arithmetic data (additive characters, components
of Ramanujan sums, gcd/lcm lattice with Möbius inversion inside the square), in which the
non-resonant crossings Off = A − R_res are absorbed exactly, so that
A = Σ squares + (manifestly non-negative remainder) is an identity?

Short answer. No, within the class declared in §3 (arithmetic selection or twisting in the node index
or in the mode index): NO-GO PROVED (Theorem R and corollaries). Outside that class no new
mechanism was identified; what remains is the complete form in the variable t, already recorded.

---

## 0. Cross-check

**(1) Closest antecedent.** Three pieces, all three in phase 211:

- GRAM §18.7, (TAIL-ZERO) and (NO-FIN-MARGIN) with its corollary: there is no single identity
  A_0[c] = Σ_α w_α|ℓ_α(c)|², w_α ≥ 0, with all ℓ_α of finite support; no observable of finite
  support sustains a margin. This already excludes the enlarged system when all its squares depend on
  a finite number of coefficients.
- GLOBAL, "Factorial extension before resonance": it is literally the natural enlarged system (the
  products of distinct frequencies are kept before completing squares; exact identity
  Q = Σ_m Λ(m)‖P_m b − R_m b‖²_K + b*Db + E(b)); the remainder D + E is not non-negative, and the "Consequence
  for the joint remainder" of "Squarefree scales" proves that these squares are not continuous in
  the graph norm and that Q ≥ εS_sq is false for every ε > 0.
- GLOBAL, "Control of the orthogonal substitution": when the coordinate selection P_m is replaced by the
  orthogonal projection the sum of squares diverges.

Other antecedents consulted: GRAM §§17.6–17.7 (margins and separate payment), GLOBAL "The resonant
budget requires a one-sided comparison", "Grouped divisorial covariance", "The divisorial remainder is
indefinite"; routes index 06, residues R1 and R9 (dead subroutes: exact matrix identity of
1∗Λ = log beyond divisors, Near as a separate operator, subspaces balanced by residues,
conductor-q > 1 family by twisted vectors); phase 188 L2_BUILD_030 and N_BUILD_021; memory of
rejected selections (all eight). Search for "Müntz", "Carlson", "soporte finito", "NO-FIN-MARGIN"
in index, grid, crossword and Papers 47–48: the general statement of §3 of this memo does not appear; its
squarefree case appears (GLOBAL, "Squarefree scales") and its finite-support case
(GRAM §18.7). A search without literal coincidence does not prove conceptual novelty: Theorem R is the
common generalization of those two cases with the same instrument.

**(2) Really new object or claim.** There is no new constructive object. The constructive reading
of K3 (enlarging the index of the squares of RES-SOS with arithmetic data of the nodes or of the modes)
is **repetition** of the factorial extension and of its two controls; by rule 3 of the brief that
reading ends here. What the memo does contribute is the answer to the class question that the assignment
asks to decide: a rigidity theorem (Theorem R, §3) that excludes at once every square, of finite or infinite
dependence, obtained by arithmetic selection or twisting, and that explains why the three
antecedents failed for the same reason.

**(3) Why the change avoids the difficulty of the antecedent.** It does not avoid it: it identifies it. The common
difficulty is that exactness with non-negative remainder forces each square to be continuous in the graph
norm of A, and continuity forces its coefficients to be the values at the integers of a
holomorphic function of polynomial growth in a half-plane. No arithmetic selection has that
property.

**(4) Identity or inequality that connects with global positivity.** No new one. The result is
a necessary condition on the operator V of the identity (G) of `OBJECT_SPEC.md` on the carrier of
integer scales (reduction PROVED, GRAM §18 and §18.9): V is continuous in the graph norm and its
coefficients are analytic sequences in the sense of §3.

**(5) Line that breaks for cΛ and a_P.** There is no sign step, hence no line that must break.
Theorem R is a barrier and, as it should be, it does not distinguish weights: it only uses the continuity of the form
in the graph (§8).

**Relation with the rejected selections of the memory.** K3, read constructively, coincides with
"Factorial squares and physical projections". It does not touch "(m,n) → (m+n, m−n)" nor "discrete summation by parts
in theta" nor "compensation between scales": there is no reindexing, no telescoping and no proposed
bound on the remainder. The memo reopens none of the eight.

---

## 1. Framework (CITED)

We work at y = 0, with complex coefficients c = (c_k)_{k ≥ 1} of finite support on the positive
integers, and

    A_0[c] = Σ_{k,l} c_k conj(c_l) A(½ log k, ½ log l).

Facts used, all PROVED in phase 211:

(M1) **Graph** (GRAM §18.1). With P_κ(t) = κ^{5/4} Σ_{n≥1} n² e^{−πκn²t}, T = πt^{5/4}(−2tD − 3),
F(P) = TP, G(P) = ½T Lg P − C TP and P(c) = Σ_k c_k P_k, one has

    A_0[c] = ∫_1^∞ [log t |F|² + 2 Re(G conj F)] dt/(2t),   F = F(P(c)), G = G(P(c)).   (A-GRAPH)

(M2) **Continuity** (GRAM §18.2). For fixed 0 < a < π and ‖P‖_{a,2} = max_{j≤2} sup_{t≥1} e^{at}|P^{(j)}(t)|
(Banach space B_a²), there exists C_a with

    |A_0[c]| ≤ C_a ‖P(c)‖²_{a,2}   for every finite c.

It does not presuppose a sign of A_0.

(M3) **Holomorphy** (GLOBAL, "Squarefree scales"). For a/π < δ < 1, z ↦ P_z is holomorphic from
{Re z > a/π} into B_a², with ‖P_z‖_{a,2} ≤ C_δ(1 + |z|)^{13/4} on Re z ≥ δ. (Each term
z^{5/4}n²e^{−πzn²t} is holomorphic with values in B_a² and of norm ≤ |z|^{5/4}n²(1 + π|z|n²)²e^{a − πδn²};
the series converges locally uniformly.) Likewise E_z(t) = e^{−πzt} is holomorphic with
‖E_z‖_{a,2} ≤ (1 + π|z|)² e^{a − πδ}.

(M4) **Modes** (GRAM §17, §18.3). With b_λ(c) = Σ_{kn²=λ} n^{−1/2} c_k one has
P(c) = Σ_{λ≥1} λ^{5/4} b_λ(c) E_λ, absolutely in B_a²; and E_k = k^{−5/4} Σ_n μ(n) n^{−1/2} P_{kn²},
absolutely in B_a² (MOB-P). For λ = dq² with d squarefree, b_λ = q^{−1/2} f_{d,q},
f_{d,q} = Σ_{a|q} √a c_{da²}. R_res is the diagonal part in λ, Off the part λ ≠ μ.

(M5) **RES-SOS** (GRAM §17.2–17.5). R_res[c] = Σ_d √d [Σ_q D_q|f_{d,q}|² + Σ_q Σ_{m|q, m≥2}
Λ(m) I_q |f_{d,q} − f_{d,q/m}|²], with D_q ≥ c_* I_q > 0.

---

## 2. Systems of squares and forced continuity

**Definition (exact system of squares).** A system of squares is a pair (ℋ, V) with ℋ a Hilbert
space and V linear from the space of finite coefficients into ℋ; its energy is 𝒮[c] = ‖Vc‖².
This includes discrete sums Σ_α w_α|ℓ_α(c)|² (ℋ = weighted ℓ²) and integrals ∫|ℓ_t(c)|² dμ(t)
(ℋ = L²(μ)). The system is **exact for A_0** if

    A_0[c] = ‖Vc‖² + ρ[c],   ρ[c] ≥ 0   for every finite c.                         (EX)

It is the identity (G) of `OBJECT_SPEC.md` §1 on the carrier of integer scales.

**Lemma 1 (forced continuity). PROVED.** If (ℋ, V) satisfies (EX), or only ‖Vc‖² ≤ M·A_0[c] for some
finite M and every finite c, then ‖Vc‖² ≤ M C_a ‖P(c)‖²_{a,2}. In particular, for each g ∈ ℋ the
functional ℓ_g(c) = ⟨Vc, g⟩ satisfies |ℓ_g(c)| ≤ (M C_a)^{1/2} ‖g‖ ‖P(c)‖_{a,2}.

*Proof.* ‖Vc‖² ≤ M A_0[c] ≤ M|A_0[c]| ≤ M C_a‖P(c)‖² by (M2); the rest is the Cauchy–Schwarz
inequality in ℋ. ∎

Remark. It is not used that A_0 is non-negative; only that the square stays below A_0. A
square that is not continuous in the graph norm cannot appear in any identity (EX), with
any non-negative remainder, whatever the remainder is.

---

## 3. Rigidity theorem

Fix 0 < a < π and a/π < δ < 1. Call **divergent** a set Z of positive integers with
Σ_{k∈Z} 1/k = ∞.

**Theorem R. PROVED.** Let (ℋ, V) satisfy ‖Vc‖² ≤ M‖P(c)‖²_{a,2} for every finite c (by Lemma 1, every
exact system satisfies it). Then, for each g ∈ ℋ:

(R0) *Interpolation at nodes.* There exists N_g holomorphic on Re z > a/π, with
|N_g(z)| ≤ C(1 + |z|)^{13/4} on Re z ≥ δ, such that ⟨Vδ_k, g⟩ = N_g(k) for every integer k ≥ 1.

(R0′) *Interpolation at modes.* There exists n_g holomorphic on Re z > a/π, with |n_g(z)| ≤ C(1 + |z|)^{13/4} on
Re z ≥ δ, such that ⟨Vc, g⟩ = Σ_{λ≥1} b_λ(c) n_g(λ) for every finite c (absolutely convergent series).

(R1) *Uniqueness on divergent sets.* If N_g(k) = 0 for every k in a divergent set,
then ⟨Vc, g⟩ = 0 for every c. The same if n_g(λ) = 0 for every λ in a divergent set.

(R2) *No arithmetic twisting.* Let (ℋ, V′) be another system with the same bound and θ: ℕ → ℂ such that
there exists α ∈ ℂ with {θ = α} and {θ ≠ α} both divergent. If Vδ_k = θ(k)V′δ_k for every k, then
V = V′ = 0. The same in modes: if n_g(λ) = θ(λ) n′_g(λ) for every λ and every g, then V = V′ = 0.

*Proof.* (R0). ℓ_g vanishes where P(c) = 0, hence it defines a linear functional on the subspace
{P(c)} ⊂ B_a², bounded by (M)^{1/2}‖g‖. By Hahn–Banach it extends to a continuous functional ℓ̃_g on
B_a². Set N_g(z) = ℓ̃_g(P_z). By (M3), N_g is holomorphic and has the indicated bound; N_g(k) = ℓ_g(δ_k)
because P(δ_k) = P_k.

(R0′). Set n_g(z) = z^{5/4} ℓ̃_g(E_z), holomorphic with the bound indicated by (M3). By (M4) and the
continuity of ℓ̃_g, ℓ_g(c) = ℓ̃_g(P(c)) = Σ_λ λ^{5/4} b_λ(c) ℓ̃_g(E_λ) = Σ_λ b_λ(c) n_g(λ).

(R1). Let N be holomorphic on Re z > a/π with |N(z)| ≤ C(1 + |z|)^{13/4} on Re z ≥ δ and N(k) = 0 for k ∈ Z,
Z divergent; one may assume Z ⊂ (δ, ∞). Set H(z) = N(z)/(z + 1)⁴. Since |z + 1|² ≥ (1 + |z|)²/2 on
Re z > 0, H is bounded on Re z ≥ δ, and it is holomorphic in a neighbourhood of that closed half-plane. For a
finite subset Z₀ ⊂ Z, each factor β_k(z) = (z − k)/(z + k − 2δ) has modulus 1 on Re z = δ, modulus
< 1 on Re z > δ and tends to 1 at infinity. The quotient H/Π_{k∈Z₀} β_k is holomorphic and bounded on
Re z > δ, continuous up to the boundary, and of modulus ≤ ‖H‖_∞ on the boundary; by the
Phragmén–Lindelöf principle for bounded functions on a half-plane, it is so on the whole half-plane. For real z₀,
z₀ > δ, z₀ ∉ Z:

    |H(z₀)| ≤ ‖H‖_∞ Π_{k∈Z₀} |k − z₀|/(k + z₀ − 2δ).

For k > z₀ the factor is 1 − 2(z₀ − δ)/(k + z₀ − 2δ), and Σ_{k∈Z} 1/(k + z₀ − 2δ) = ∞; the product tends
to 0 as Z is exhausted. Hence H(z₀) = 0 on a set with accumulation points and N ≡ 0. Applied to N_g:
N_g(k) = ⟨Vδ_k, g⟩ = 0 for every k, hence ℓ_g = 0. Applied to n_g: n_g ≡ 0 and ℓ_g = 0 by (R0′).

(R2). Fix g. N_g − αN′_g is holomorphic with the same bound and vanishes on {θ = α}, divergent; by (R1)
N_g = αN′_g on the whole half-plane. Then (θ(k) − α)N′_g(k) = 0 for every k, hence N′_g vanishes on
{θ ≠ α}, divergent, and N′_g ≡ 0, N_g ≡ 0. Since g is arbitrary, Vδ_k = V′δ_k = 0 for every k. The case
of modes is identical with n_g, n′_g. ∎

Comment. (R1) is a Müntz-type uniqueness statement in dual form; here only the direction
"Z divergent ⟹ uniqueness" is used and proved. The case Z = tail of squarefrees is GLOBAL, "Squarefree
scales"; the case "complement of a finite set" gives GRAM §18.7 without using (TAIL-ZERO). The
instrument is the same; no novelty is attributed to it.

---

## 4. Excluded classes

**Class 𝒜 (declared).** Systems of squares (ℋ, V) that contain a non-zero component of one of
the following types, in the node index k or in the mode index λ:

(a) *selection*: a component ⟨V·, g⟩ whose coefficients vanish on a divergent set;
(b) *twisting*: a component of the form θ·V′ with V′ continuous in the graph and θ as in (R2);
(c) *selection or twisting plus continuous term*: V = V₁ + V₂ with V₂ continuous in the graph and V₁ of type
    (a) or (b).

**Corollary 2 (NO-GO, class 𝒜). PROVED.** No system of class 𝒜 is exact for A_0, with any
non-negative remainder. Moreover, none satisfies 𝒮 ≤ M·A_0 with finite M.

*Proof.* If it were, V would be continuous in the graph (Lemma 1). In case (c), V₁ = V − V₂ would also
be. Then (R1) or (R2) force the component to be zero. ∎

Instances, all with the same proof:

1. **Finite dependence** (finite support in k): the complement is divergent. Recovers GRAM §18.7.
2. **Squarefree class index.** A square that only uses the c_{da²} of one class d (or of a
   finite number of classes), with any number of coefficients: its complement contains all the
   integers of other classes, divergent. In particular **none of the squares of RES-SOS** (D_q|f_{d,q}|²
   nor Λ(m)I_q|f_{d,q} − f_{d,q/m}|²) can survive, alone or accompanied, in an exact identity
   for the complete A. The index "squarefree class" cannot be part of the index of any
   exact system.
3. **Residue classes and characters.** Squares supported on k ≡ r (mod q), q ≥ 2; squares with
   coefficients e(rk/q)·N(k), χ(k)·N(k), c_q(k)·N(k) (Ramanujan sum) or φ(gcd(k,q))·N(k) with N the
   coefficients of a continuous functional and non-constant twisting: excluded by (R1) and (R2). A
   family of squares indexed by additive characters modulo q with common amplitude admits at most
   one non-zero member.
4. **gcd/lcm lattice with Möbius inside the square.** Squares supported on the multiples of g ≥ 2,
   on the divisors of q, on the k with given gcd(k,q); squares with weight μ(k)·N(k), μ²(k)·N(k) or
   Λ(k)·N(k): excluded ({μ = 0} and {μ ≠ 0} are divergent; {Λ = 0} and the primes are divergent).
5. **Selection of modes.** Every coordinate projection onto the modes λ divisible by m² (m ≥ 2), or
   onto any set of modes with divergent complement, applied to a continuous operator. In the
   factorial extension, V_m c = Σ_λ [(P_m b)_λ − (R_m b)_λ] h_λ ∈ L²([1,∞), dt/(2t)); the term R_m is
   continuous (‖R_mF‖ ≤ m^{−1/2}‖F‖) and the term P_m is the selection 1_{m²|λ} of the continuous embedding
   c ↦ F: case (c). Thus each square Λ(m)‖P_m b − R_m b‖²_K, separately, is incompatible with (EX);
   this recovers the discontinuity of S_sq of GLOBAL without using the squarefree density.
6. **Non-negative diagonal weights** Σ_k w_k|c_k|² or Σ_λ w_λ|b_λ|² with some positive weight: case 1.

The only classical arithmetic function that passes the filter (R0) as a twisting is log k, which is holomorphic:
this is consistent with g_q using log a and with the separator Σ_{d|n}Λ(d) = log n being the point where the
arithmetic enters (A-GRAPH). This is an observation, not a mechanism.

---

## 5. Direction of strictly negative energy of the remainder

**Proposition 3. PROVED.** Let (ℋ, V) be a system with a component ℓ = ⟨V·, g⟩, ‖g‖ = 1, not continuous
in the graph norm (for example, any system of class 𝒜). Then there exist finite c^{(n)}
with

    ‖P(c^{(n)})‖_{a,2} → 0,   ℓ(c^{(n)}) = 1,   A_0[c^{(n)}] → 0,
    limsup (A_0 − 𝒮)[c^{(n)}] ≤ −1.

For V = RES-SOS system: for fixed d, q, there exist c^{(n)} with f_{d,q}(c^{(n)}) = 1, A_0[c^{(n)}] → 0 and

    limsup Off[c^{(n)}] ≤ −√d·D_q < 0,    (Off + R_res)[c^{(n)}] → 0.

*Proof.* That ℓ is not bounded with respect to ‖P(c)‖ means that for each n there is c with
|ℓ(c)| > n‖P(c)‖_{a,2}; dividing by ℓ(c) gives c^{(n)} with ℓ(c^{(n)}) = 1 and ‖P(c^{(n)})‖ < 1/n.
(M2) gives A_0[c^{(n)}] → 0, and 𝒮 ≥ |ℓ|² = 1. For RES-SOS, f_{d,q} is a non-zero functional of finite
support; if it were bounded with respect to ‖P(c)‖ it would be zero by (R1), hence it is not. Moreover
R_res ≥ √d·D_q|f_{d,q}|² by (M5), and Off = A_0 − R_res. ∎

Reading. Off is not "small compared with R_res": in these directions Off cancels R_res completely
(zero slack, no margin). The critical inequality Off ≥ −R_res is neither refuted nor proved; it is
proved that no splitting of R_res into squares of class 𝒜 can be preserved when Off is added.

---

## 6. Answer on GRAM §17.6–17.7

- §17.6 excludes Off ≥ −C·E_y and A ≥ δ·R_res: comparisons with margin. §17.7 excludes paying the
  dilation operator C with the energy ∫(1 + log t)|F|². Neither of the two by itself excludes an
  exact absorption. **PROVED** (reading of their statements).
- Exact absorption in class 𝒜 is excluded by Corollary 2. **NO-GO, PROVED**, class 𝒜.
- Outside 𝒜 exact absorption is not excluded and cannot be by a class argument:

**Proposition 4. PROVED (elementary).** A_0 ≥ 0 on every finite c if and only if there exists an exact
system (ℋ, V) with ρ = 0. In that case all its components are continuous in the graph and satisfy (R0),
(R0′).

*Proof.* If A_0 ≥ 0, take ℋ as the completion of the quotient of the finite c by the kernel of
the seminorm A_0^{1/2} and V the canonical map. The converse is trivial and the rest is Lemma 1 with
Theorem R. ∎

Thus, the existence of an exact enlarged system outside 𝒜 **is** the target, without additional sign
information; the corresponding triangular factorization appears in the closed families as a
reformulation (`RULES_AVOID.md` §C, sign object of phase 200: Cholesky).

---

## 7. What is not excluded and why it is not a candidate

(i) **Squares on the t side.** The functionals continuous in the graph are functionals of the function
P (or F = TP) on t ≥ 1: values F(t₀), differences F(t₀) − m^{−1/2}F(m²t₀), integrals against measures.
The arithmetic can enter there through the DILATION index m (weights Λ(m), characters in m), not through
nodes or modes. Theorem R says nothing about that class. But that form is the complete causal form in
the variable t (GLOBAL, "Operational control of deduplication of §18.5"), where the following are already recorded:
the divergence Σ_m Λ(m)‖F − R_mF‖² = ∞ (GLOBAL, "Control of the orthogonal substitution"), the loss of
positive rates after T (GRAM §18.5), the unfavourable sign of the causal potential (GRAM §19.12) and the
residue R9 of the index. No explicit operation was found in this memo that decomposes
T Lg T^{−1} + log t into terms that pair with Λ(m) m^{−1/2} D_{m²} for each m. **No new
mechanism.** OPEN.

(ii) **Formulation (S).** Theorem R depends on the holomorphy of z ↦ P_z and does not transfer to the
matrix 𝔸_M = [B(log m − log k)] of P47 prop:AM. There only the following elementary restriction holds.

**Remark 5. PROVED.** If a functional ℓ(x) = Σ_m w_m x_m on finite vectors satisfies
|ℓ(x)|² ≤ M·x*𝔸x (every size), then |w_m − w_k|² ≤ 2M[B(0) − B(log(m/k))]. Since B is even and C²
near 0 (for |d| < log 2 − 2T₀ the arithmetic part of B(d) is zero, and in the archimedean part
F̂₀² = O(τ^{−4}) and m(τ) = O(log τ), so that τ² m(τ) F̂₀(τ)² is integrable),
|w_{m+1} − w_m| ≤ C_B M^{1/2}/m for m ≥ m₀(T₀).

*Proof.* Apply the hypothesis to x = δ_m − δ_k: x*𝔸x = 2B(0) − 2B(log(m/k)). Taylor of order
two in d = log(1 + 1/m). ∎

It is a modulus-of-continuity condition, not an exclusion: a square twisted by an additive
character is not forbidden in (S). The admissible direction of R9 (additive-character components of the
defect m − kn, at resolution e^{2T}) **is not closed** by this memo and is not
constructed either.

(iii) **Other remainders.** Identities A = Σ squares + ρ with ρ non-negative only on a subspace, or
with ρ of non-manifest sign, fall outside the statement. The factorial extension is of this type
(D + E indefinite).

---

## 8. Falsifier battery

There is no sign step in this memo. Theorem R and Corollary 2 use a single property of A_0: the
bound (M2). That bound holds for the analogous form of any comb whose operator
C_a = Σ a(m) m^{−1/2} D_{m²} is bounded on H_γ, in particular for cΛ, a_P, finite deletion and amplification
and b_θ. The barrier is therefore generic in the comb (type B1 of `RULES_AVOID.md`), as befits
a NO-GO, and it neither contributes nor claims to contribute a sign. For Davenport–Heilbronn, Epstein,
quartets, f_t and Beurling the analogous form on the carrier of integer scales has not been written; nothing
is claimed about them.

Consistency check with positive results: RES-SOS is exact for R_res, which is not continuous
in the graph (Proposition 3 applied to its own squares); there is no contradiction because (M2) is a
property of the complete A_0, not of R_res nor of Off separately.

---

## 9. Closing

**Result.** NO-GO with class, PROVED: no system of squares containing a component
obtained by arithmetic selection or twisting in the node or mode index (class 𝒜 of §4: finite
dependence, squarefree class, residue classes, additive or multiplicative characters,
Ramanujan sums, gcd/lcm lattice, weights μ or Λ, coordinate projections of modes) can appear in an
exact identity A_0 = Σ squares + non-negative remainder. Outside that class: **no new mechanism**.
K3 does not pass to construction.

**What was proved.** Lemma 1 (exactness with non-negative remainder ⟹ continuity in the graph); Theorem R
(coefficients = integer values of a holomorphic function of polynomial growth; uniqueness on
sets of divergent reciprocal sum; no arithmetic twisting); Corollary 2 (NO-GO of class
𝒜, which contains as cases GRAM §18.7 and the discontinuity of S_sq of the factorial extension);
Proposition 3 (directions in which Off exactly cancels R_res); Proposition 4 (outside 𝒜 the
existence of an exact system is the target itself); Remark 5 (modulus-of-continuity
restriction in formulation (S)).

**What failed and why.** The exact absorption of Off into squares with arithmetic index fails because
every component of an exact identity is continuous in the graph norm of A, and that norm does not see the
arithmetic of the nodes nor of the modes: it only sees the function P(t). The resonant squares live
precisely in coordinates that this norm does not control; that is why Off has to cancel them completely
in the directions of Proposition 3 and admits no splitting.

**Next concrete step.** (1) Record the NO-GO of class 𝒜 in the routes index (06, residue R9,
dead subroutes) and in the grid; the memo does not edit those files. (2) If K3 is to be reopened, the only
non-excluded reading is (i) of §7: an identity in the variable t with dilation index m, and it requires
first writing the decomposition of T Lg T^{−1} + log t that pairs term by term with
Λ(m) m^{−1/2} D_{m²} with a cutoff that avoids the recorded divergence; without that explicit operation there
is no candidate. (3) The direction of R9 in formulation (S) remains open with the restriction of
Remark 5.

**Not verified.** The facts (M1)–(M5) are taken from the corpus as PROVED and were not re-derived
(in particular the continuity bound (M2) of GRAM §18.2 and the holomorphy (M3)). No
computation was done. Remark 5 uses the formula for B of STATEMENT_001 §2 and the decay F̂₀ = O(τ^{−2}) read
from F̂₀ = (τ² + ¼)|ĝ|⁴; it was not cross-checked against the text of Paper 47. The analogous form of (M2) for the battery models without Euler product was not checked.
