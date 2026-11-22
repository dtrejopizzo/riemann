# ROUND_004_E — Selection: indefinite forms (Kreĭn/Pontryagin) with a non-radical neutral vector

Selection memo, not a construction memo. Notation from `../phase-211-sign-sandbox/STATEMENT_001.md` and from
P46 §sec:complete; N = e^{2T}. 𝔪_T(F) = (1/2π)∫m|F̂|² (archimedean form, comb deleted; in P46 𝒜_∞ on
P_T), Π_T(F) = −Σ_{n<N} v_n Re c_F(log n), a_T = 𝔪_T + Π_T, W_T = a_T + 2Re(A B̄) (complete form with
polar term). For a weight a one writes a_T^{(a)}; for cΛ, a_T^{(c)} = 𝔪_T + cΠ_T. n_-(q|V) is the
largest dimension of a subspace of V ∩ 𝒟_T on which q < 0. Labels: PROVED / CITED / CONDITIONAL /
ARGUED / OPEN / NO-GO / NUMERICAL.

## Cross-check

### Search performed

- Read in full: `BRIEF_CONSTRUCTOR.md`, `README.md`, `RULES_AVOID.md`, `OBJECT_SPEC.md`, `LEDGER.md`,
  `REVIEW_003.md`, `ROUND_003_4.md`, `STATEMENT_001.md`.
- P46 as primary source: §sec:complete in full (lem:Onat, thm:Al, thm:parityschur, prop:polarcap and the paragraph
  that follows); thm:index, cor:Tarch, prop:NC, cor:P3, thm:J, cor:nasym, cor:H1 and remarks
  (l. 2420–2780); §sec:inertia (thm:inertia-finite, thm:inertia-quartet, thm:inertia-rank,
  §subsec:inertia-excl "Inertia alone (conditional)"); lem:polar; statement of thm:coer-schur;
  statement of cor:convfail.
- grep in `03-research/` (all phases), P46, P48 and `05-meta-and-planning/` for "Pontryagin",
  "Krein–Langer", "generalized Nevanlinna", "N_κ", "Π_κ", "Kreĭn signature", "firma de Kreĭn",
  "negative squares", "n_-", "inertia", "polar capacity". Opened (header and central section):
  `phase-197-barrier-theorem/BARRIER_W_001_…NO_GO.md` §§0–4; `phase-16-surf-witness-variety/
  07-pontryagin-the-indefinite-object.md`; `phase-186-toolbox/R186_004_KREIN_FLOW_FIRST_THRESHOLD.md`;
  `phase-162-…/R162_1301_KREIN_JORDAN.md` §0.
- Phases 170 and 161: R170_854 only by grep as primary source (lines 236, 372, 410: "every completion by
  squares is indefinite", (3.4)) and via `ANNEX_170_FILES_3.md` (entries 854, 861, 862); R161_032 only
  by grep ((4.2) at l. 114, "OPEN / TERMINAL" at l. 146); R161_023, 061–063 only via
  `ANNEX_161_FILES_3.md` and `RULES_AVOID.md` §K4. R170_866–870 only via `ROUND_003_4.md` and §I1–I3.
- Not opened: the memos of phase 156 (per-window converse; their content is in P46 thm:parityschur and
  prop:polarcap, which I did read); round 5 of phase 155 ("Kreĭn indeterminacy"); the memos of phases
  15/16 other than 07; `POLAR_CAP_001` (cited in 211 ROUND_008_A l. 26 as "bordered Schur
  complement that inverts a_T|P_T itself — consumes λ_A > 0"; there is no file with that name); the ledger
  and the memos of round 21 of 211 except row C43 of `LEDGER.md`.

### (1) Closest antecedent

- **P46 thm:parityschur (a1)–(a2), (c) and prop:polarcap.** It is exactly the Pontryagin format of the
  task, already written and PROVED: n_-(W_T) = n_-(a_T|P_T) + n_-(𝔊_T), 𝔊_T = S^Sch_T + diag(2, −2), with
  S^Sch_T the compression of a_T to the a_T-orthogonal of P_T (Schur complement on P_T), and the
  "polar capacity" reading E_T(β, α). The following paragraph reduces the per-window converse to two signs.
- **P46 §subsec:inertia-excl, "Inertia alone (conditional)".** Conditional exclusion of the class
  "decomposition a_T = 𝔪_T − C_ε + Π_T + properties stable under finite rank + inertia arithmetic
  (Sylvester, Haynsworth, interlacing, lem:monoT)", via thm:inertia-rank.
- **Phase 197, BARRIER_W_001 Thms. W1–W3** (PROVED in the memo): the index n_-(a_T|P_T) is monotone in T,
  all crossings have the same Kreĭn sign; "constant index" is equivalent to the target; the
  von Neumann–Wigner codimension gives nothing.
- **RULES_AVOID §C1** records "coercivity, Schur, inertia, Wiener–Hopf … as a sign source" and
  "defect/continuation, Morse index, Kreĭn signature" among the closed families; §K4 records that in
  phase 161 no memo studies a non-radical neutral vector; R3-c (`ROUND_003_4.md` Lemma 1) leaves
  indefinite forms outside its class.
- **Phase 16, memo 07; R162_1301 §0:** Pontryagin spaces whose index counts spectral data
  external to the sandbox; recorded there as detectors, not as sign sources. Not used here.

### (2) Genuinely new object

None with a mechanism. What is new relative to the corpus are five short lemmas (§2), all without
sign, which close the zone as the task formulates it:

- the resolution of the tension "κ(T) > 2" (Prop. 1): the counts that grow with T are of 𝔪_T, not of
  a_T; under the target, n_-(a_T|L²(I_T)) ≤ 2 for all T;
- every upper bound on a negative index is a positivity on a subspace of finite
  codimension (Lemma 2): "inertia instead of an inequality" does not exist as an alternative;
- a neutral vector inside a nonnegative subspace is radical there (Lemma 3), and a neutral vector
  whose coefficient component passes through the rows of 𝒟_N is radical in any signature
  (Lemma 4);
- in each window with λ_A(T) > 0 all indices of the format are constant in c near 1
  (Lemma 5), and their jumps are exactly at the endpoints of the positivity window in c (Lemma 6):
  an inertia argument does not satisfy O4 in any fixed window and only reads the sign through a
  value.

I do not write ℋ_T, V_T nor ρ_T: the Kreĭn format, in all its readings examined, reduces to
thm:parityschur/prop:polarcap (already in P46), to thm:coer-schur (L2), or to (G) with another embedding.

### (3) Does it avoid the antecedent's difficulty?

No. The difficulty of prop:polarcap is that, given WP_T, the sign of W_T is that of two numbers
𝔤_ev, 𝔤_odd that nobody controls, and that the converse fails for modified weights (cor:convfail). The requested
Pontryagin format (positivity on P_T ⟺ the 2×2 matrix of the inverse form on the Tate vectors
has as many negative eigenvalues as the ambient form has negative squares) is the same
inertia identity with a_T in place of W_T (Prop. 1(b)), and requires knowing two integers that are only
known by computing values (Lemmas 2 and 6). The non-radical neutral vector does not change this (Lemmas 3 and 4).

### (4) Connection with global positivity

The connecting identity is exact and already known: for the operator Q of a_T on L²(I_T), if 0 is not
in the spectrum of Q nor of a_T|P_T,

    n_-(a_T|P_T) = n_-(a_T|L²) − n_-(Γ_T),   Γ_T = [⟨Q^{-1}χ_i, χ_j⟩]_{i,j}, χ_{1,2} = e^{±t/2}1_{I_T},

(Prop. 1(c)). (★) at T is "n_-(a_T|L²) = n_-(Γ_T)". Neither of the two integers is known without the sign.

### (5) cΛ and a_P: why the remainder stops being ≥ 0

There is no remainder: an inertia argument has no term that stops being ≥ 0; it has integers. Lemma 5
proves that in each window with λ_A(T) > 0 the integers do not change in a neighbourhood of c = 1, so the
count is the same for cΛ with |c − 1| small: no line breaks at c ≠ 1 near 1.
Lemma 6 says where it breaks: at c_±(T), the zeros of c ↦ λ_A(T; c). For a_P the same holds with the
homotopy Λ + s(a_P − Λ). The window of 211 LEDGER C43 that closes on c = 1 from both sides
(NUMERICAL, cell forms R = 2…8) is compatible with the count only as a degeneration in the limit
T → ∞ of the jump points c_±(T), and those points are value information (§3).

## 1. Answer to question (i): how many negative squares and of which form

| Form | Space | n_- | Source |
|---|---|---|---|
| 𝔪_T (no comb) | L²(I_T) | ≥ ⌈2Tτ_0/π⌉ − 1; ≤ 5, 7, 8 at ½log3, log 2, 0.80; ~ 4.0042 T | P46 thm:J, cor:P3, cor:nasym (CITED) |
| 𝔪_T | P_T | ≥ ⌈2Tτ_0/π⌉ − 3; = 0, 1, 2 up to 0.90; ~ 4.0042 T | P46 thm:J, thm:index, cor:nasym (CITED; thm:index with interval verification) |
| a_T (with comb) | L²(I_T) | finite for each T | P46 thm:inertia-finite with η = 1, k = 0 (CITED) |
| a_T | P_T | the target is that it equals 0 | — |
| W_T | L²(I_T) | n_-(a_T|P_T) + n_-(𝔊_T) | P46 thm:parityschur (c) (CITED) |
| 2Re(AB̄) | L²(I_T) | exactly 1 (signature (1,1)) | P46 lem:polar (CITED) |

The apparent tension is due to the form with which one counts. "Theorem P, n_- ≤ 5/7/8" (cor:P3) and the
linear growth in T (cor:nasym) refer to 𝔪_T, the archimedean form with the comb deleted. That is
why cor:Tarch says that 𝔪_T is negative on some vector of P_T for T ≥ 0.60: there the comb is the
source of positivity, not a perturbation (remark after cor:Tarch). For a_T there is no growing
count. On the contrary, under the target the count is bounded by 2 (Prop. 1(b)).

## 2. Lemmas

**Proposition 1 (inertia with Tate border).** Fix T. Let q = a_T (or W_T) on its domain 𝒟_T.

(a) (CITED, P46 thm:parityschur (a2), (c).) If 0 is not in the spectrum of the operator of a_T|P_T,
n_-(W_T) = n_-(a_T|P_T) + n_-(𝔊_T).

(b) (PROVED.) With the same hypothesis and S^Sch_T = diag(a_T(h_ev), a_T(h_odd)),
n_-(a_T|L²(I_T)) = n_-(a_T|P_T) + n_-(S^Sch_T). In particular, if λ_A(T) > 0 then
n_-(a_T|L²(I_T)) = n_-(S^Sch_T) ≤ 2.

(c) (PROVED, finite-dimensional; ARGUED in the form version.) Let Q be the operator of a_T on L²(I_T),
with 0 ∉ σ(Q), and let Γ_T be the 2×2 matrix of (b) of Cross-check (4). If moreover a_T|P_T is nondegenerate, then
n_-(a_T|P_T) = n_-(Q) − n_-(Γ_T). Thus, a_T|P_T > 0 ⟺ n_-(Γ_T) = n_-(Q), which requires n_-(Q) ≤ 2.

*Proof.* (b) It is the proof of thm:parityschur (a1)–(a2) with ε_par = 0. That proof only uses the
structure of a closed form bounded below with compact resolvent, parity and the functional
ℓ_par. In each sector, 𝒟^par_T = 𝒬^par ⊕ ℝh_par, a_T-orthogonally, and
a_T(G + xh_par) = a_T(G) + a_T(h_par)x². One sums over the two sectors (P46 thm:parityschur (o), which holds
for a_T without polar term). (c) Bordered matrix M = [[Q, X], [X*, 0]], X = [χ_1, χ_2] of rank 2. By
Haynsworth with respect to Q: In(M) = In(Q) + In(−X*Q^{-1}X) = In(Q) + In(−Γ_T). With respect to the
subspace ker X* = P_T: In(M) = In(Q|P_T) + (2, 2, 0) (a full-rank border r adds r squares of
each sign when the restriction is nondegenerate). Equating the numbers of negative squares:
n_-(Q|P_T) + 2 = n_-(Q) + n_+(Γ_T), and with Γ_T nonsingular n_+ = 2 − n_-. In infinite dimension it
applies to the finite spectral decomposition of the negative part (compactness of the resolvent). I do not
rewrite that reduction: ARGUED. ∎

Reading: the Pontryagin condition of the task ("Γ_T ⪯ 0 in the right amount") is the same
identity as prop:polarcap, with a_T in place of W_T. Γ_T and S^Sch_T are inverse in ℓ coordinates (the
Schur complement on P_T is the inverse of the compression of Q^{-1} to the space of functionals).
It is not a new object.

**Lemma 2 (an upper bound on the index is a positivity).** Let q be a Hermitian form on a
space E and κ ∈ ℕ. Then n_-(q) ≤ κ if and only if there exists a subspace U ⊂ E of codimension ≤ κ with
q ≥ 0 on U, in the case where q has a spectral decomposition with finite-dimensional negative
part (closed forms bounded below with compact resolvent, like all those of
this memo).

*Proof.* (⇐) If N is a negative subspace with dim N > κ, then N ∩ U ≠ {0} by
dimension, and on a nonzero vector of that intersection q is < 0 and ≥ 0 at once. (⇒) Let E_- be the sum of
the eigenspaces of negative eigenvalue, of dimension n_-(q) ≤ κ. U = E_-^⊥ ∩ 𝒟 (orthogonal in L²; it is
q-orthogonal since these are spectral spaces) has codimension n_-(q) and q ≥ 0 on U. ∎ PROVED.

Consequence: "extracting positivity from a signature count and not from an inequality" is impossible
in the literal sense. Every upper bound on a negative index that enters the argument is a
positivity on a finite-codimension subspace of some form. Inertia arithmetic
(Sylvester, Haynsworth, rank-r perturbation) only transports those positivities. Lower
bounds on the index come from exhibiting negative vectors and do not serve to conclude n_- = 0. The
finite-codimension positivities of a_T that the corpus has written are:

- thm:inertia-finite: positivity on the orthogonal of the eigenvectors of time–band limiting
  with eigenvalue ≥ A′/(A′ + L);
- thm:coer-schur: coercivity on 𝒱_k, of codimension 2k − 2.

Transporting them to P_T by Haynsworth leaves exactly a finite Schur complement: it is (L2),
thm:coer-schur (iii). P46 §subsec:inertia-excl already says so for the first one ("the finite structure of
Theorem coer-schur with a larger dimension").

**Lemma 3 (a neutral vector inside a nonnegative subspace is radical there).** Let 𝔊 be Hermitian
on E, of any signature, U ⊂ E a subspace with 𝔊 ≥ 0 on U and v ∈ U with 𝔊(v) = 0. Then
𝔊(x, v) = 0 for all x ∈ U and 𝔊(x + v) = 𝔊(x). Conversely, if V is nonnegative and v is neutral,
V + ℂv is nonnegative only if 𝔊(x, v) = 0 for all x ∈ V with 𝔊(x) = 0. If V is positive definite, the
condition is vacuous for x ≠ 0, and then the exact criterion is |𝔊(x,v)|² ≤ 0·𝔊(x), i.e., again
𝔊(x,v) = 0.

*Proof.* The first part is `ROUND_003_4.md` Lemma 1 applied to 𝔊|_U, which is semidefinite. For
the converse: 𝔊(x + tv) = 𝔊(x) + 2Re(t̄𝔊(x, v)) is ≥ 0 for all t ∈ ℂ only if 𝔊(x, v) = 0, because the
term in t is linear and has no quadratic term to compensate it (𝔊(v) = 0). ∎ PROVED.

Consequence for task item (iii). That a_T(F) = 𝔊(ι_T F) with ι_T(F) = w_T(F) + ê_T(F),
ê_T(F) = ((Λ,1)⊗F, β_T(F)) neutral, gives a_T ≥ 0 on P_T is the statement that the subspace
ι_T(P_T) is nonnegative for 𝔊. There are two cases.

- The ê_T(F) lie in a nonnegative subspace containing ι_T(P_T). Then the anchor is radical
  there (Lemma 3) and one returns to the invisibility of R3-c.
- They do not. Then the anchor acts only through the cross term 2Re𝔊(w_T F, ê_T F), which is
  one more quadratic form in F inside the embedding ι_T. Nonnegativity of ι_T(P_T) is the
  target with another embedding: it is (G) when 𝔊|ι_T(P_T) is written as a sum of squares, and it is a
  reformulation when not (B3).

Neutrality of the anchor forces neither of the two cases. That the vector is neutral and non-radical does not
by itself give any sign information about the subspace one wants to prove nonnegative.

**Lemma 4 (the rows of 𝒟_N make the anchor radical in any signature).** If 𝔊(x, y) = 𝔥(Dx, Dy)
for a linear map D and any sesquilinear form 𝔥 (indefinite included), then
ker D lies in the radical of 𝔊. PROVED (trivial: 𝔊(x, k) = 𝔥(Dx, 0) = 0).

With R170_866 (ker 𝒟_N = ℝ(Λ,1), PROVED there) and R170_867–868 (every linear row annihilating (Λ,1)
factors through 𝒟_N; RULES_AVOID §I1), the following results. In every 𝔊 whose dependence on the
coefficient coordinate passes through linear rows annihilating (Λ,1), the anchor (Λ,1)⊗F is radical
even if 𝔊 is indefinite. A non-radical neutral vector requires that the nullity of 𝔊 on (Λ,1)⊗F be a
condition quadratic in the weight that does not factor through rows. By O2 (`ROUND_001_D.md` Lemma A), that
condition lies in the ideal of the atoms Σ_{d|n}a(d) − log n. Nothing in it indicates a sign.

**Lemma 5 (the indices are constant in c near 1 in each window).** Fix T with λ_A(T) > 0. Let
V_T := Σ_{n<N} |v_n|. Then:

(a) λ_A(T; c) ≥ λ_A(T) − |c − 1|V_T, so that n_-(a_T^{(c)}|P_T) = 0 for |c − 1| < λ_A(T)/V_T;

(b) c ↦ a_T^{(c)}(h_par(c)) is continuous on that interval. If a_T(h_par) ≠ 0 at c = 1 for both
parities, n_-(a_T^{(c)}|L²) and n_-(S^Sch_T(c)) are constant in a neighbourhood of c = 1. If 𝔤_par ≠ 0 at
c = 1, the same holds for n_-(W_T^{(c)}) and n_-(𝔊_T(c)).

*Proof.* (a) |Π_T(F)| ≤ V_T‖F‖², because |c_F(log n)| ≤ ‖F‖² (P46, proof of thm:parityschur,
"Solvability"). Then a_T^{(c)} = a_T + (c − 1)Π_T ≥ (λ_A(T) − |c − 1|V_T)‖·‖² on P_T. (b) On the
interval of (a), part (a3) of thm:parityschur (with ε = 0 for a_T, which is the same proof) gives
a_T^{(c)}(h_par(c)) = min{a_T^{(c)}(F) : F ∈ 𝒟^par_T, ℓ_par(F) = 1}. It is an infimum of affine functions
in c, hence concave, and it is finite on an open interval, hence continuous. Likewise for
𝔤_par(c) = a_T^{(c)}(h_par(c)) + 2ε_par. A nonzero value keeps its sign in a neighbourhood. One concludes
with Prop. 1(b) and with thm:parityschur (a2). ∎ PROVED.

**Lemma 6 (the jumps of the count are at the zeros of λ_A(T; ·)).** Fix T. J(T) := {c ≥ 0 :
λ_A(T; c) ≥ 0} is a closed interval; n_-(a_T^{(c)}|P_T) = 0 if and only if c ∈ J(T). Suppose an
inertia identity

    n_-(a_T^{(c)}|P_T) = κ(c) − n_-(Γ(c)),

valid on an interval of c, with κ(c) and Γ(c) integers and matrices given by a construction. If κ is
constant on that interval (for example, if it counts polar or Tate squares, which do not depend on c),
then Γ(c) is singular, or the identity ceases to hold, at each point c_±(T) of ∂J(T) in the
interval. If Γ(c) depends continuously on c, the sign of Γ(1) is decided by the position of 1
relative to c_±(T), i.e., by the sign of λ_A(T; 1).

*Proof.* λ_A(T; c) is an infimum of affine functions in c: it is concave and continuous (Lemma 5(a) gives
the modulus), so {≥ 0} is a closed interval. n_- = 0 ⟺ λ_A ≥ 0 (P46 lem:parity, compactness
of the resolvent). At c_+(T), the left-hand side passes from 0 to ≥ 1 (λ_A(T; ·) is concave and not identically
zero, hence changes sign at the endpoint, unless it vanishes on a whole interval; that case is excluded
by the nonzero slope of `ROUND_003_4.md` Lemma 4, ARGUED there). With κ constant, n_-(Γ(c)) jumps.
A continuous matrix only changes its inertia by passing through a singular matrix. ∎ PROVED except for the case
of zero slope, which is ARGUED.

## 3. Closed class and answer to (iii)–(iv)

NO-GO with class (PROVED: Lemmas 2, 3, 5 and 6; Prop. 1(b); part (c) is ARGUED in infinite dimension).
**Class 𝓘:** arguments concluding n_-(a_T|P_T) = 0 in a window T from (1) one or several
Hermitian forms of any signature, linked to a_T by exact identities or by restriction,
(2) neutral vectors, radical or not, and (3) inertia arithmetic: Sylvester, Haynsworth, interlacing,
finite-rank perturbations and the bordered identity of Prop. 1. In that class:

(a) sign information enters only through upper bounds on the index, which are positivities on
finite-codimension subspaces (Lemma 2). The only ones for a_T written in the corpus lead to (L2)
(thm:coer-schur);

(b) a neutral vector contributes nothing. Inside the nonnegative subspace it is radical (Lemma 3). Outside
it, it is part of the embedding and nonnegativity of the image subspace is the target. And if 𝔊 passes
through rows of 𝒟_N, it is radical in any signature (Lemma 4);

(c) in every window with λ_A(T) > 0, the verdict is the same for cΛ with |c − 1| < λ_A(T)/V_T
(Lemma 5), so that clause O4 is not satisfied in any fixed window;

(d) the jumps of the integers are at the zeros of c ↦ λ_A(T; c) (Lemma 6). A κ "by construction",
constant in c, forces the small matrix Γ (the polar capacity or its inverse) to contain
exactly the position of c_±(T). Reading its sign at c = 1 is reading the sign of λ_A(T). That is the
circularity. It is not an "as hard as" argument: it is the equality of Prop. 1(c).

Answer to C43. A positivity window J(T) that closes on c = 1 from both sides
(NUMERICAL in the cell forms of 211 ROUND_021_A; on a_T, README §1.1) means that
c_±(T) → 1. At each finite T there is no degeneration at c = 1 (Lemma 5). In the limit, the point c = 1 is
the limit of two degeneration points. This does not refute an inertia argument in the limit, but shows
that such an argument needs, for each T, the position of c_±(T), which is value information
(Lemma 6). An index that jumps exactly at c = 1, and not near it, could only come from a
form degenerate at c = 1. That is an exact identity at the true weight, of the type
(c − 1)·(…) = 0. By R3-e and R3-i, such an identity is a combination of atoms and does not fix the sign.

**What the class does NOT exclude.**

1. Upper bounds on the index that come not from a written positivity but from a count by the argument
   principle of an explicit function of a spectral parameter, built with window data
   and without knowing the spectrum of a_T. For the natural function, Γ_T(z) = [⟨(Q − z)^{-1}χ_i, χ_j⟩], a 2×2
   Nevanlinna matrix, the eigenvalues of a_T|P_T are the zeros of det Γ_T(z) (Weinstein–Aronszajn,
   CITED as a standard fact; its application here is ARGUED). Counting them in (−∞, 0) requires the negative
   spectrum of Q, and the count returns to Prop. 1(c). I know no other function with that property. The
   Kreĭn–Langer / de Branges type constructions of the corpus (phase 16 memo 07; R162_1301) count
   data outside the sandbox and are not used.
2. Arguments uniform in T that do not read only integers. For example, a value bound on
   λ_A(T; c) that fixes c_±(T) on both sides of 1. That is no longer inertia: it is the target with margin.
3. Indefinite forms used for something other than concluding by counting, for example an indefinite Green
   identity (R170_854 (3.4)) whose negative part cancels exactly against an
   identified term. This is (G) and is not excluded by this memo; R3-g only covers the
   resolvent-type class.
4. The joint accounting R161_032 (4.2), OPEN / TERMINAL in the source, unrelated to this memo.

## Result

No new mechanism, plus a NO-GO with class (𝓘, inertia with neutral vectors), PROVED in its
central parts (Lemmas 2–6, Prop. 1(b)). The Pontryagin format of the task is already in P46
(thm:parityschur, prop:polarcap) with W_T, and here it is repeated with a_T. The tension "κ(T) > 2" is due to counting
with 𝔪_T: under the target, n_-(a_T|L²) ≤ 2 for all T. The candidate does not pass the gate: it does not write (2)
and its point (5) is answered negatively (Lemma 5).

## What was proved

- Prop. 1(b): n_-(a_T|L²) = n_-(a_T|P_T) + n_-(S^Sch_T); under λ_A(T) > 0 it is ≤ 2. PROVED (same proof
  as thm:parityschur with ε = 0). Prop. 1(c), the form with the resolvent matrix Γ_T: PROVED in
  finite dimension, ARGUED in the form version.
- Lemma 2: n_-(q) ≤ κ ⟺ q ≥ 0 on a subspace of codimension ≤ κ. PROVED.
- Lemma 3: a neutral vector in a nonnegative subspace is radical there; a neutral vector can only be
  added to a nonnegative subspace if it is 𝔊-orthogonal to it. PROVED.
- Lemma 4: if 𝔊 factors through D, then ker D is in the radical, in any signature. With R170_866–868,
  the anchor (Λ,1)⊗F is radical in every 𝔊 that sees the coefficients through rows annihilating (Λ,1). PROVED.
- Lemma 5: constancy of all indices of the format for |c − 1| < λ_A(T)/V_T. PROVED.
- Lemma 6: the jumps are at ∂J(T); with κ constant, Γ(c) is singular there. PROVED, except for the case of
  zero slope, which is ARGUED.
- Table of §1 (which form has which index): CITED from P46, checked in the primary source.

## What failed and why

- Positivity cannot come "from a count and not from an inequality". Upper bounds on the
  index are positivities (Lemma 2), and the only one that would be needed here is that of P_T itself, or that of a
  coercive subspace leading to (L2).
- The non-radical neutral vector has no function. Inside the nonnegative subspace it is radical. Outside
  it, the target is nonnegativity of the image subspace. And the natural route through rows of 𝒟_N
  makes it radical in any signature.
- The count is stable in c around 1 in each window. O4 can only come from the position of
  c_±(T), which is a value datum.

## Concrete next step

Do not relaunch "inertia / Pontryagin / neutral vector" as a sign source. None of the three non-excluded
exits has an object. The only one that is neither (G) nor the target with margin is 1: an
explicit function of a spectral parameter, built with window data without knowing the spectrum of
a_T, whose count of zeros or poles on a half-line bounds n_-(a_T|L²) by 2 and fixes the inertia of Γ_T.
Before proposing it one would have to write that function and explain why its count does not go through
Prop. 1(c).

Suggested annotation for the index and the grid (not made from here): "P212-4E: indefinite forms with
non-radical neutral vector / Pontryagin count — NO-GO with class PROVED (upper bound on index =
positivity in finite codimension; neutral in nonnegative subspace = radical; indices constant in c
near 1 per window; jumps at ∂J(T)). The Pontryagin format = P46 thm:parityschur/prop:polarcap
with a_T; under the target n_-(a_T|L²) ≤ 2. Does not exclude: argument-principle count of a window function
without the spectrum of a_T; (G) with indefinite Green form and exact cancellation".
