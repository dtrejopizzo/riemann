# BARRIER_W_001 — Track W: non-crossing / spectral-flow mechanisms along (H1) T-homotopy and (H2) comb homotopy

Phase 197. Memo (pure mathematics, no numerics), not yet reviewed.
positivity of 𝔞_T on P_T is assumed true. This memo closes a *method class*, not the target.
Notation of Paper 47: 𝔞_T^{(v)} (eq:Aform), P_T={A=B=0}, λ_A(T)=μ_T(v_T(Λ)) (lem:degen),
n₋(T):=n₋(𝔞_T|P_T) (number of negative eigenvalues of the closed lower-bounded form with compact resolvent, as in thm:index).

## 0. Corpus / index check and written new reason
- Index hits: AUDIT_193 #101 (CA_A_008 integer invariant / spectral flow; "no-crossing = positivity", C); README Fase 193
  "invariante entero / flujo espectral / Maslov (constancia = positividad, REF-D)"; P35-3 semilocal Maslov μ_A=2κ (PARTIAL);
  P49-2 Maslov probe (NO-GO); P37-2, P51-1, P52-1 inertia readers (NO-GO); ES-18 finite Pontryagin index (DEAD); phase 155
  round 5 Kreĭn indeterminacy; Theorem P / thm:index (n₋(A_∞|P_T) archimedean); A14a-5 (Sylvester inertia class-blind, NO-GO);
  R155_046/047 Sturm/nodal/Karlin (dead); W-det, lem:flowdet (Hellmann–Feynman flow, NO-GO), W-coh; BARRIER_D2_001 Thm 2 and its
  residual R2 ("openness at crossings"); INV_U_001 (U0 entry invisibility, U2 modulus).
- **New reason (written).** #101 and the Fase-193 line record the slogan "constancy = positivity" for a *fixed* invariant without
  proof and without the two concrete homotopies. Nothing in the index (i) proves monotonicity/irreversibility of the index along
  (H1), (ii) settles residual R2 of BARRIER_D2_001 (kernel acquisition at s<1 on (H2)), (iii) treats the von Neumann–Wigner
  codimension argument or Kreĭn signature of zero-crossings, or (iv) runs the falsifier test (an invariant must be violated by
  O_6/O_4/Beurling/finite combs) to locate the Λ-specific datum. Those four items are the object of this memo; Sturm/nodal and
  determinants are only located against the existing dead entries, not re-run.

## 1. Structural class 𝒮 shared by every comb (PROVED, collected)
For every real weight vector v (in particular every comb a ≥ 0 with Σ a(n)n^{−1/2−δ}<∞: Λ, a_P, finite truncations, O_6, O_4,
Beurling-type combs supported on log-grids):
(S1) zero-extension: P_T ↪ P_{T'} isometrically with equal form values for T<T' (proof of lem:monoT uses only c_F=0 on |u|≥2T);
(S2) concavity of v ↦ μ_T(v), d_v-1-Lipschitz (lem:degen, BARRIER_D2_001 §2);
(S3) continuity in T (proof of lem:contA uses only Σ_{n<e^{8T}}|v_n|<∞), entry invisibility at T_n (U0) and modulus
     v_n C_T/log(1/2η) (U2), uniform over v_n ≥ 0;
(S4) parity splitting (symbol and comb even; thm:parityschur(o) structure);
(S5) compact resolvent / attained minimum on P_T (lem:compact).
None of (S1)–(S5) reads the value of any v_n beyond summability.

## 2. Theorem W1 (index along (H1) is monotone; irreversibility) — PROVED
For every v in 𝒮: T ↦ n₋(T) and T ↦ n₋(T)+dim ker(T) are nondecreasing; T ↦ λ_A(T) is nonincreasing; hence the zero set
{λ_A<0} is an up-ray (T_*,∞) and the spectral flow of 𝔞_T|P_T on [T_0,T] equals n₋(T)−n₋(T_0) with **every crossing of the
same (downward) Kreĭn signature**.
*Proof.* Min–max: if 𝔞_T<0 on a k-dim subspace E⊂P_T, its zero-extension E′⊂P_{T'} has 𝔞_{T'}=𝔞_T<0 (S1), so n₋(T')≥k; same with
≤0. Monotonicity of λ_A is lem:monoT. A crossing can only increase n₋, so all crossings have the same sign. ∎
**Corollary W1′ (partial positivity beyond ½log5; PROVED, non-explicit).** n₋(T)=0 and ker=0 on (0,T_5+ε) for some ε>0
(thm:log5A + continuity S3). Quantitative ε: OPEN (constants of lem:contA not explicit; U2 controls only contact instants and
the next contact after T_5 is T_7, Λ(6)=0, so on (T_5,T_7) the comb is frozen and only window growth acts).
**Reading.** There is no conserved integer to exploit: the only possible invariant is n₋ itself, it is monotone, and the target at
T is exactly n₋(T)=0. "Morse index constant on [T_5,T]" ⟺ WP_T(Λ). This is #101 made PROVED, and it is uniform on 𝒮.

## 3. Theorem W2 (residual R2 of BARRIER_D2_001 is the target) — PROVED
Let a_s=(1−s)a_0+sΛ with μ_T(a_0)>0. Then s ↦ μ_T(a_s) is concave on [0,1] and:
(a) μ_T(a_s)=0 for some s′<1 (kernel acquired before the endpoint) ⟹ μ_T(Λ) ≤ −μ_T(a_0)(1−s′)/s′ < 0;
(b) μ_T(Λ) ≥ 0 ⟹ μ_T(a_s)>0 for all s<1 (no kernel, no crossing before s=1);
(c) μ_T(Λ) < 0 ⟹ exactly one crossing s_*∈(0,1), downward, and μ<0 on (s_*,1].
Hence "openness at crossings for s<1" on straight segments ⟺ μ_T(Λ) ≥ 0 = WP_T(Λ).
*Proof.* Concavity (S2). (a) slopes of a concave function decrease: (μ(1)−0)/(1−s′) ≤ (0−μ(0))/s′. (b) μ(s) ≥ (1−s)μ(0)+sμ(1)>0.
(c) continuity + concavity (a concave function changes sign at most once from + to −). ∎
For a general path the crossing set is the exit set from the convex K_T (AUDIT_197); exits before s=1 can be avoided by
re-routing inside K_T iff Λ∈K_T. So R2 is REF-D on every path class; residual closed (NO-GO as a sign source).

## 4. Theorem W3 (codimension / von Neumann–Wigner gives nothing) — PROVED (finite-dim), ARGUED (form level)
(a) In a real-symmetric 1-parameter family, a simple eigenvalue reaching 0 is a codimension-1 event (one real equation μ_1=0);
von Neumann–Wigner (codim 2 for real symmetric) concerns *coincidence of two eigenvalues*, not a zero crossing. So vNW forbids
only multi-dimensional kernels (codim 3 for dim 2): it predicts that a first failure, if any, has a 1-dim kernel of definite
parity — exactly Paper 47's statement (abstract; primitive null vector of definite parity), no exclusion.
(b) To push a zero crossing to codim ≥2 one needs an extra real condition L(h)=0 on every kernel vector, independent of the
Euler–Lagrange equation. Candidates checked: Tate moments (already in P_T); dual-certificate complementary slackness
(∫f_w|ĥ|²=0 with f_w≥0 and ĥ entire forces f_w≡0, impossible ⇒ no attained certificate at a crossing; this constrains certificates,
not h, and holds for every comb in 𝒮); lem:degen (c_h(log n)=0 ∀n) — not forced, and if it held it would put Λ at the max of μ_T
(no contradiction at λ_A=0). No independent condition exists in 𝒮.
(c) Even with codim 2, a genericity argument says nothing about one specific family: (H1) for Λ is a single non-generic path,
and by W1 a touching at T_* is tangential/one-sided (λ_A nonincreasing), i.e. exactly the non-transversal case genericity ignores.

## 5. Determinants and Sturm (located, not re-run)
- A fixed-sign Fredholm/Birman–Schwinger quantity vanishing exactly at a crossing: W-det (P47 thm:wh-det) — every sign-deciding
  determinant factors as λ_A·R; lem:flowdet — the flow coefficient is ⟨A′h*,h*⟩/λ_A. The finite version (det S_{T,k}) is residue
  (L2), OPEN. No new reason, not re-run.
- Sturm/nodal count of the minimizer: P_T imposes no clamping (INV_U_001 §1); the operator is nonlocal (Lévy kernel ~1/(2|u|)),
  where Courant/Sturm oscillation theorems are not available; any nodal count bounded by index is again n₋ (W1). Index entries
  R155_046/047 cover it; not re-run.

## 6. Falsifier test and location of the Λ-specific datum
Every invariant in §§2–5 is built from (S1)–(S5), which hold verbatim for a_P, finite truncations (prop:finsupp: μ_T→C_0−A_S<0,
so they cross), O_6, O_4 and Beurling combs. Those cross 0 while satisfying W1–W3, so **no invariant definable on 𝒮 forbids a
crossing** (PROVED as a meta-statement: any obstruction must use the values v_n). The only Λ-reading datum at a crossing is the
Hellmann–Feynman / supergradient pairing
  dμ/ds = −Σ_{n∈𝒩_T} (v_n(Λ)−v_n(a_0)) c_{h*}(log n)  (simple bottom; lem:degen, lem:flowdet),
a functional of the minimizer h* — the same wall as W-fam / Theorem X / rem:bar-loc. Between contacts (H1) the comb is frozen and
the drift is the archimedean window growth (which alone drives every finite comb negative); at contacts the entry is invisible
(U0) with modulus U2. So for Λ the crossing is prevented, if at all, only by the *continued arrival* of contacts with the right
values c_{h*_T}(log n); no index/signature/codimension object carries that information.

## 7. Self-check
- **Six clauses (prop:spec).** W1–W3 invariants: (1) comb-generic — FAIL (hold on all of 𝒮); (6) falsifier-separating — FAIL.
  As expected: they are structural, not sign-carrying.
- **BARRIER_001 trichotomy.** Index/flow/signature conclusions are comb-generic (branch (i)) except "n₋(T)=0", which is REF-D
  (branch (iii)). No branch-(ii) certificate arises.
- **Semiring principle.** No additive/multiplicative interplay enters; filtered out.
- No D⟺(other statement) equivalence used anywhere.

## 8. Labels and exact obstruction
PROVED: §1 collection; W1, W1′ (qualitative ε); W2 (a)–(c) and path version; W3(a),(b) in finite dimension and at form level for
the listed candidates; §6 meta-statement. ARGUED: W3(c) (genericity reading). OPEN: explicit ε in W1′; (L2).
**Exact obstruction (one line):** along both homotopies the index is monotone with all crossings of one signature, zero crossings
are codimension 1, and every such structure is shared by crossing falsifiers; the sole Λ-specific crossing datum is the
pairing Σ v_n c_{h*}(log n), a minimizer functional. **NO-GO class 𝒦_W** (index / spectral flow / Kreĭn signature /
vNW codimension / determinant-zero non-crossing arguments on 𝒮). Residual R2 of BARRIER_D2_001: CLOSED (= REF-D, W2).
Row D: OPEN; no sign obtained.

## 9. Response to AUDIT_197_2 (received during writing)
- *Weights.* Paper 47 uses v_n = 2a(n)/√n (main.tex l.3093). All statements above are in v-coordinates, so the factor 2 only rescales
  the comb-space Lipschitz constant (d_v := Σ|v_n(a)−v_n(b)| = 2Σ|a(n)−b(n)|/√n); W1–W3 and §6 are unchanged.
- *"R2 is a restatement of #101."* Agreed, and W2 is the proof of that restatement on (H2) (concavity gives exactly one downward
  crossing iff μ_T(Λ)<0). Recorded as closure of R2, not as a new route.
- *(a) conserved index/nodal count provable on an explicit interval beyond ½log5.* Result: the only invariant with crossing
  content is n₋ itself (W1: monotone, one signature), so conservation on [T_5,T] is WP on [T_5,T]. What is provable without the
  target is W1′: n₋=0 on (0,T_5+ε) with ε>0 non-explicit (continuity). An explicit ε needs a quantitative lem:contA on the
  contact-free interval (T_5,T_7); this is a sign-free modulus estimate (OPEN, not attempted; it would only move the proven
  window, never past T_7 without a new certificate). A nodal count is not conserved on 𝒮 (nonlocal operator, no Sturm theory)
  and would be bounded by n₋ anyway. Falsifiers: a_P / finite truncations satisfy W1 and do cross, confirming non-specificity.
- *(b) ℤ-specific codimension at a putative crossing.* None found: the candidate constraints (Tate moments, certificate slackness,
  lem:degen vanishing) are either already in P_T, constrain the certificate rather than h, or hold for every comb (W3(b)).
  Zero crossings remain codimension 1.
- Both (a) and (b) reduce to #101: **NO-GO 𝒦_W recorded cleanly.**
