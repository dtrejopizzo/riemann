# O1_COMPOSITION_001 — Branch composition rule of Φ200 (phase 204p)

Pure mathematics only, no numerics.

## Summary (≤300 words)

The «branch composition rule» of Φ200 (META_200 Addendum A1, ARGUED) says that a construction combining several
inputs I1–I10 falls into one of five branches. This memo **refutes it as a barrier** and replaces it with a weaker
PROVED statement.

1. **Theorem O1.A (PROVED, elementary).** lem:transfer excludes a deduction with premise 𝒫 = P₁ ∧ … ∧ P_k only if there is a
   single falsifier that satisfies every P_i. If the catalog of falsifiers is {F₁,…,F_k} and F_i violates P_i, no
   instance of lem:transfer with those falsifiers excludes the conjunction. Moreover, the conjunction «Euler product over ℕ ∧ FE of degree 1
   and conductor 1 ∧ residue 1» has ζ as its only model in the Selberg class (CITED: Kaczorowski–Perelli). A deduction
   valid in ∩𝔗_i is a deduction about ζ, and every proof of D has that form. A rule that sends every conjunction to a
   death branch would exclude every proof. Therefore the rule, as a barrier, is **FALSE** (refuted by the
   «unique model» argument), and branch 2 only closes if it is shown that a premise is as strong as the goal.
2. **What remains: Φ200′ (PROVED piecewise).** No proof whose sign-fixing step uses premises with a common negative
   model. The sign step uses E over ℕ (mandatory because of the quartets) and F (mandatory because of a_P).
3. **Chaining or composing (formal criterion, Def. O1.2 + Prop. O1.C PROVED).** A conjunction chains if every inequality
   with margin uses a single channel and the others enter beforehand as identities. In that case the sign step is excluded with
   **abstract** falsifiers in the space of the intermediate object. The registered conjunctions are classified as follows:
   Lemma R ∧ gap (P2_SCHUR) chains; (H-b) ∧ (H-d) (phase 202, Lemma M) chains; co-Poisson mirror ∘ Möbius
   lattice (FF_001) is an identity and has no sign step; h_par (prop:WT, POLAR_CAP) is TRANSFER. None of them actually
   composed (ARGUED for FF).
4. **Constructive spec (OPEN).** An inequality is needed whose validity requires Euler and FE **in the same step**.
   I write the template (S1)–(S4). There is no candidate in the corpus.
Verdict O1: **refuted as a barrier; Φ200 degrades to Φ200′ (PROVED).**

---

## 0. Index and corpus check (mandatory)

Grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` for «composici», «conjunci», «cor:shape», «Φ200», «BARRIER_SOUND»,
«P2_SCHUR», «CPOS», «h_par», «prop:WT», «Kaczorowski». Relevant results:
- README l.421 BARRIER_001 (phase 197): Lemma 2 (conjunction) on the catalog 𝒜, «ARGUED as a set».
- l.545 SPEC_SIGN_OBJECT_006: Theorem Φ200, class 𝒦_Φ.
- l.550 DH_TRANSFER_001: channel (i) PROVED (Theorem 3.1, 𝔗₁).
- l.578 CPOS_CLASS_001: thm:noimport (i)–(ii) PROVED, (iv) ARGUED.
- l.594 BARRIER_SOUND_001: gap P2 = «composition rule», no proof.
- l.601 P2_SCHUR_001: Schur «Euler ⊕ gap» NO-GO PROVED, Lemma P2-S.3.
- l.598 POLAR_CAP_001: h_par = bordered Schur complement that inverts 𝔞_T|P_T (TRANSFER/NO).
- l.487 PROOF_L_SHARP_FF_001: «unpublished composition» of the co-Poisson mirror with the Möbius lattice (identity).
- COSH_DEFECT_001 l.216: degree 1 and conductor 1 ⇒ ζ (CITED, Kaczorowski–Perelli).

No entry proves or refutes the **rule**. BARRIER_SOUND §Gap 2 proposes precisely attacking the rule and not an object.
New reason against the index: this memo deals with the logical status of the rule (what lem:transfer can exclude), not a new
object. It does not retry any construction.

Definitions verified against P47: lem:transfer (l.7734), cor:shape (l.9048), thm:noimport (l.9341), prop:WT (l.4358).

---

## 1. Formal framework

**Def. O1.1.** A *channel* is a premise P about weight data a (the sequence that replaces Λ in the form 𝔞_T^a) that holds
for a = Λ. Its *set of falsifiers* is 𝔉(P) := {a in the certified catalog : P(a) and bottom(𝔞_T^a|P_T) < 0 for some T}.
The certified catalog of P47 / phase 200 is: DH (F_DH, rem:FDH), Epstein Q = x²+5y² (Lemma E, lem:shape-epstein), a_P and the
modifications of (A) (lem:shape-del…scale), Beurling and the quartet models (lem:shape-quartet). The *theory* of P is
𝔗(P) := {a : P(a)}.

An *argument* A with premises 𝒫 = P₁ ∧ … ∧ P_k is a deduction «∀a: 𝒫(a) ⇒ bottom(𝔞_T^a|P_T) ≥ c(T)». It is valid as a
deduction in 𝔛 = 𝔗(𝒫) = ∩𝔗(P_i).

lem:transfer (P47 l.7734) says: if q₀ = q_ζ and some q₁ ∈ 𝔛 have 𝖯 and bottom(q₁) < 0, no deduction
«𝖯 ⇒ bottom ≥ 0» is valid in 𝔛.

## 2. Composition theorem: exact status

### 2.1 What lem:transfer can and cannot do

**Theorem O1.A (PROVED).**
(a) The deduction A with premise 𝒫 = ∧P_i is excluded by lem:transfer with the catalog 𝒞 if and only if
∩_i 𝔉(P_i) ≠ ∅, that is, if some member of the catalog satisfies every P_i and has negative bottom.
(b) If for each i there exists F_i ∈ 𝒞 with ¬P_i(F_i), and 𝒞 ⊂ {F_1,…,F_k} ∪ {a : ∃ i, ¬P_i(a)}, then ∩𝔉(P_i) = ∅ and no
instance of lem:transfer with falsifiers from 𝒞 excludes A.
(c) For any finite or countable catalog 𝒞 of weights distinct from Λ there exists a finite conjunction of channels true
for ζ that excludes all of 𝒞. In the case of the P47 catalog, the minimal conjunction has two channels: E = «Euler product over ℕ with
completely multiplicative coefficients of modulus ≤ 1» and F = «FE of degree 1, conductor 1, Γ_ℝ(s), simple pole at 1».

*Proof.* (a) One direction is lem:transfer with q₁ = 𝔞^F for F ∈ ∩𝔉(P_i). For the other: if ∩𝔉 = ∅, no q₁ in the catalog
satisfies 𝖯 = 𝒫 with negative bottom, so the hypothesis of lem:transfer does not hold. (b) Is immediate from (a).
(c) Each F ∈ 𝒞 has a_F ≠ Λ. The channel «a = Λ» is true and excludes all of them, but it is trivial (see §2.2). In the
concrete case: DH has no Euler product (violates E). Epstein has degree 2 due to the factor Γ_ℝ(s)Γ_ℝ(s+1) and conductor 20, and also has no
Euler product because h(−20) = 2 (violates E and F). a_P, the modifications of (A) and Beurling have no FE of conductor 1 (violate F; if
Beurling is taken with a hypothetical FE, the classification of §2.2 covers it). The quartet models **preserve** the FE and break E as a Dirichlet series over ℕ: their arithmetic side has an absolutely
continuous part (P47 lem:shape-quartet, prop:shape-inputs(iv)). Hence they violate E. a_P preserves the comb over ℕ
and breaks F (prop:shape-inputs(i)). [Corrected after INTEGRATION_O1_001: the previous version said the quartets violate F.] ∎

### 2.2 Unique model and the refutation

**Prop. O1.B (CITED + PROVED).** Let 𝒮 be the Selberg class. If L ∈ 𝒮 has degree 1 and conductor 1, then L = ζ
(Kaczorowski–Perelli, «On the structure of the Selberg class I», Acta Math. 182 (1999); CITED, the same citation as
COSH_DEFECT_001 l.216). Note (INTEGRATION_O1_001): with conductor 1, KP leaves ζ(s+iθ), θ ∈ ℝ. θ = 0 is fixed by the pole at s = 1
and the reality of the coefficients, **not** I3. Hence 𝔗(E ∧ F) ∩ 𝒮 = {ζ}. For a sequence outside 𝒮 with an Euler product (E) and FE (F), Hamburger's theorem
fixes the function with a_n ≡ 1 once the pole and the FE at conductor 1 are fixed (CITED, Hamburger 1921, in its standard
form for ordinary Dirichlet series with the FE of ζ). Consequently 𝔗(E ∧ F ∧ «ordinary Dirichlet series») = {ζ}.

Question about the goal: Beurling with a hypothetical FE? A Beurling system with «FE of degree 1 and conductor 1» and
integer frequencies log n is an ordinary series, and then Hamburger forces ζ. With non-integer frequencies it falls outside Hamburger.
There, the integrality channel I3 excludes it (it is the third premise of cor:shape(b)). I know of no classification theorem
for Beurling with FE and generalized frequencies: **OPEN**, although it is irrelevant for the refutation, because it suffices to
add I3 to the conjunction.

**Theorem O1.D (refutation of the rule as a barrier; PROVED, conditioned only on the definition of «death branch»).**
Let 𝓡 be the statement «every construction in 𝒦_Φ that uses a conjunction of inputs falls into a branch ∈ {1,…,5}, and each branch
prevents concluding λ_A(T) ≥ 0». If branches 1, 3, 4 and 5 are defined by falsifiers (as in the pieces of Φ200) and branch 2
by «the input is as strong as the goal», then:
(i) for the conjunction 𝒫* = E ∧ F ∧ I3, branches 1, 4 and 5 in their falsifier-based version **do not apply** (O1.A(b));
(ii) branch 2 is not a barrier for 𝒫*: saying that «𝒫* implies the goal» is the thesis itself and not an objection. A
deduction valid in 𝔗(𝒫*) = {ζ} is a deduction about ζ, which is what is sought;
(iii) branch 3 (functional of h*) is a barrier only at first order (Theorem X) and for linear functionals in h*, and does not
restrict 𝒫*.
Therefore 𝓡 cannot be proved with the pieces method (lem:transfer + falsifiers). Moreover, if 𝓡 were
true for all of 𝒦_Φ, no proof of D whose inputs lie in I1–I10 would exist. Under the program's working premise
(positivity is true and we are constructing it with these inputs), 𝓡 is incompatible with the program.

*Proof.* (i) is O1.A(b) with the catalog of §2.1. (ii) A deduction «𝒫*(a) ⇒ bottom ≥ 0» is quantified over 𝔗(𝒫*), which
is {ζ} (O1.B), so it is literally a statement about ζ. For lem:transfer one would need q₁ ≠ q_ζ in 𝔗(𝒫*), and none exists.
(iii) Theorem X says that every first-order discriminant is a functional of h*, not of σ (index, phase 186). It says
nothing about arguments whose sign step is nonlinear in the data. ∎

**Remark O1.D′ (honesty).** O1.D does not say that a proof exists or that 𝒫* gives it. It only says that the composition
rule, understood as a barrier, is not a theorem and cannot be one with this method. The classification «the worst branch
2≻5≻4≻3≻1» of BARRIER_SOUND P2 is left as follows: branch 2 applied to a conjunction that only has ζ as a model is the
description of a proof, not a death.

### 2.3 What remains of Φ200

**Theorem Φ200′ (PROVED piecewise; replaces the class part of Φ200).** Let A ∈ 𝒦_Φ with premises in channels
I1–I10, and let s(A) be the set of channels used in the *sign step* of A: the only inequality with strictly
positive margin on which the conclusion depends (Def. O1.2 below). If ∩_{P∈s(A)} 𝔉(P) ≠ ∅, A does not prove λ_A(T) ≥ 0 in the range of
T where the common falsifier is negative (T ≥ 9/5 for DH, T ≥ 1.59 for Epstein; thm:noimport(i)). In particular:
(a) no proof uses a single channel in the sign step (the pieces of Φ200, each PROVED);
(b) every proof has a sign step with |s(A)| ≥ 2 and ∩𝔉 = ∅ over the certified catalog. With the current catalog, s(A)
must contain E (as a Dirichlet series over ℕ) and F. **Both channels are mandatory, each for a different
falsifier:** F by a_P (prop:shape-inputs(i): preserves the comb and breaks the FE); E by the quartets
(lem:shape-quartet, prop:shape-inputs(iv): preserve the FE and their arithmetic side has an absolutely continuous part).
[Corrected after INTEGRATION_O1_001.]

*Proof.* It is lem:transfer applied to the sign step (O1.A(a)) plus the corrected inventory of §2.1. For (b): a_P satisfies
everything except F, and the quartets satisfy everything except E over ℕ. ∎

This is exactly cor:shape(b) with the refinement «in the same sign step». It is the correct form of the open
question: **does there exist an inequality whose validity needs F and E (or I3) at the same time?**

---

## 3. Chaining or composing: formal criterion

**Def. O1.2 (sign step, chaining).** We write A as a finite sequence of steps A = A_m ∘ … ∘ A_1. Each A_j is
an *identity* (O_j = Ψ_j(O_{j−1}), valid under a set of channels u(A_j)) or an *inequality* (Ψ(O_{j−1}) ≥ Ψ′(O_j)
with margin, valid under u(A_j)). The *sign step* is the last inequality A_{j*} such that, if replaced by an
equality, the conclusion is lost. s(A) := u(A_{j*}).
- A **chains** P₁, …, P_k if |s(A)| = 1. The other channels enter only in previous identities, which fix the object
  O_{j*−1} on which a single channel acts.
- A **composes** if |s(A)| ≥ 2 and no reordering of identities brings it down to 1.

**Prop. O1.C (chains are excluded in the object space; PROVED).** If A chains, with s(A) = {P}, the sign
step is a deduction «P(O) ⇒ Ψ(O) ≥ 0» over the space 𝒪 of intermediate objects. lem:transfer applies in 𝒪 with
**abstract** falsifiers: any O′ ∈ 𝒪 with P(O′) and Ψ(O′) < 0, even if O′ does not come from any series L. In
particular, if 𝒪 is a space of closed forms over a quotient and P is a property of the structure (gap, support,
coordinate), a single form in the quotient with that structure and negative bottom suffices.

*Proof.* Step A_{j*} is used as a universal deduction over O_{j*−1} ∈ 𝒪, and its validity depends only on P. We apply
lem:transfer with 𝔛 = 𝒪 (the lemma is stated for arbitrary sets of forms). ∎

Remark: here is the difference from branch 1. In a chain, the falsifier does not have to be a weight
datum; the previous identities (which used Euler) can fail for DH without that saving the sign step.

**Application to the registered conjunctions.**

| Conjunction | Source | Previous identities | Sign step | Classification |
|---|---|---|---|---|
| Lemma R ∧ gap c_N = 0 | P2_SCHUR_001 | Lemma R/Guo: 𝒜 ⊂ rad, quotient | positivity of 𝒲 in the quotient, only with the gap as coordinate (𝒲_AA ≡ 0, 𝒲_AB ≡ 0, Lemma P2-S.1) | **CHAINS** (PROVED in P2_SCHUR); abstract falsifier = 𝒲 in the quotient with gap (V1) |
| (H-b) ∧ (H-d) exterior (★★) | phase 202, BUILD_R2_001 Lemma M | Poisson / Möbius correlation ⇒ Σμ(n)n^{−½}𝔅_n = ∫m\|r̂̃\|²D_N | single channel D_μ / C6 | **CHAINS** (Lemma M PROVED: the only multiplicativity is a character, so Euler collapses to a single channel) |
| co-Poisson mirror ∘ Möbius lattice | PROOF_L_SHARP_FF_001 | both are identities | no genuine sign step; the forbidden J.3 estimate is the one that would carry the sign | **no sign step** (ARGUED from index entry l.487) |
| Poisson over the Möbius comb | phase 202 | FE ⇒ 1/ζ | same as the previous row | **CHAINS** (collapse to 1/ζ) |
| h_par of prop:WT | POLAR_CAP_001 | 𝔄^{−1}χ (resolvent of the full form) | n₋(𝔄) and q | **TRANSFER**: inverting 𝔄 in P_T consumes λ_A > 0 (POLAR_CAP T6.1). It is not a composition: the sign is in the hypothesis |
| «near-radical» Schur Q-P2.2 | P2_SCHUR §5 | quantitative Guo L4.4 | 𝒲_AA ~ ε, 𝒲_AB ~ ε^{½} | **OPEN**. It would be a composition if block A had a sign without passing through 𝒲 (P2-S.3(iii)); it is subject to thm:shape(B′) |

**Conclusion §3 (ARGUED as an inventory, PROVED case by case where the source is).** No conjunction in the corpus
genuinely composes. All of them chain: Euler enters as an identity that reduces the object, and the sign is then carried by a single channel
(or the sign is hidden in an inverse hypothesis). That uniformly explains what P2_SCHUR and phase 202 saw
separately.

**Lemma O1.E (why they chain; PROVED).** If a channel enters in an identity linear in the weights a, its contribution is an
equality of measures on the window (lem:shape-lin(i)). After applying it, the intermediate object depends on a only through
the image of that identity. If moreover the sign step is linear in the object, s(A) reduces to one channel and A chains.
*Proof.* Composition of linear maps: the sign step acts on the image, and its validity depends only on the
property of the image that it uses. ∎
Corollary: a genuine composition requires that **the sign step be nonlinear in a, or that the channel enter as an
inequality rather than as an identity**. This agrees with cor:shape(a) («non-linearly»).

---

## 4. Constructive consequence: specification of a genuine composition (E, F)

What Φ200′ requires is a sign step A_{j*} with s(A) ⊇ {E (or I3), F}. Template:

**(S1) Object.** O = O(Λ, T) is built **with** multiplicativity (E) in a non-reducible way. «Λ as a vector» does not
count (the quartet also sees that), nor does a linear identity in Λ (Lemma O1.E). Legitimate options: the truncated Euler
product as an operator (multiplicative over ℕ^×), the Dirichlet convolution algebra acting on tests, or the
semiring structure (ℕ,+,·) at m ≈ kn (semiring principle, project memory).

**(S2) Use of F on O.** The FE is used as a **symmetry of O** (an operator U with U O U* = O + R, where R has a sign
or is controlled), and not as an identity on the scalar series. Forbidden: Poisson over the Möbius comb (collapses to
1/ζ, Lemma M) and the Poisson mirror over g* (FF_001: identity with no sign).

**(S3) Joint sign step.** The final inequality must fail for (i) the quartets, because it uses E over ℕ; (ii) DH, because it
uses E; (iii) a_P, because it uses F. That is, its proof must **break**, not merely weaken, if either one is
removed.

**(S4) Proof of non-chaining.** One must exhibit that no reordering turns E into a previous identity. A sufficient
criterion is that the inequality be nonlinear in a and that its margin depend on a product a_m a_n with m ≈ kn (which
connects with the semiring).

**Reviewed corpus candidates.**
- h_par (prop:WT): **does not work**. It is already recorded (POLAR_CAP_001) as TRANSFER, because h_par = 𝔄^{−1}χ/q inverts the
  full form and every use consumes λ_A > 0. Does h_par have its own FE symmetry? The only symmetry that the form 𝔞_T inherits
  from the FE is parity g ↦ g(−·), already incorporated into the sector decomposition. I see no other; the explicit
  computation remains OPEN, but any symmetry of 𝔄 carries over to 𝔄^{−1}, so it adds no new channel (ARGUED).
- Poisson identity applied to g*: this is FF_001 / T_001 (index l.465, l.487), an identity with no sign. Not retried.
- Functionals of h_par versus Theorem X: Theorem X blocks first-order functionals of h*, and h_par is not h*. But h_par
  already consumes the sign, so the question is vacuous.
- Q-P2.2 (quantitative near-radical): this is the only place where E enters as an **inequality** (Guo L4.4 rate) and not as an
  identity, so it satisfies the corollary of O1.E. It lacks F. **It is the only seed compatible with (S1)–(S4) in the
  corpus**, and it is subject to thm:shape(B′). OPEN, not constructed here.

There is no candidate in the corpus that has never been tried as a genuine composition (E, F). The template (S1)–(S4)
remains an OPEN specification.

---

## 5. Verdict and correction texts

**Verdict O1:** the branch composition rule is **REFUTED as a barrier** (Theorem O1.D, PROVED with O1.B CITED).
The class part of Φ200 is replaced by **Φ200′ (PROVED piecewise)**. The chain/compose criterion (Def. O1.2,
Prop. O1.C, Lemma O1.E) is PROVED. The inventory in §3 is ARGUED as a whole. The spec (S1)–(S4) is OPEN.

**Text for META_200_BARRIER_001 (Addendum A1, replace the line «Branch composition rule: ARGUED»):**
> Branch composition rule: REFUTED as a barrier (phase 204p, O1_COMPOSITION_001, Theorem O1.D). A conjunction whose
> only model is ζ (E ∧ F ∧ I3, Kaczorowski–Perelli / Hamburger) has no falsifier and cannot be assigned to a death
> branch. What remains is Φ200′: the sign step of every proof uses at least two channels with no certified common
> falsifier, and E (over ℕ) and F are mandatory, each for a different falsifier (quartets and a_P). The registered conjunctions chain (Prop. O1.C) and do not compose.
> Φ200: PROVED piecewise (Φ200′); the class version is withdrawn.

**Text for P47 sec:spec, after thm:noimport (new remark; thm:noimport does not change, because its (iv) already says «uses a premise
outside 𝔗₁», compatible with O1.D):**
> \begin{remark}[conjunctions] Lemma~\ref{lem:transfer} excludes a deduction from $P_1\wedge\dots\wedge P_k$ only when one
> falsifier satisfies every $P_i$. The barriers of this paper therefore exclude every proof whose sign-carrying inequality
> uses a single input, but they say nothing about a sign-carrying inequality that uses the Euler product and the functional
> equation at conductor $1$ jointly; by Hamburger's theorem the only Dirichlet series over $\mathbb N$ with that
> functional equation and pole is $\zeta$. The weights $a_P$ (Proposition~\ref{prop:shape-inputs}(i)) force the functional
> equation, and the quartet models (Lemma~\ref{lem:shape-quartet}) force the Euler product as a Dirichlet series over
> $\mathbb N$, to be among the inputs of that inequality. A use of one input only through an identity preceding the inequality does not count
> (it is excluded by an abstract falsifier on the intermediate object).
> \end{remark}
(The remark cites only Hamburger, because KP has no bibitem in P47. Before integrating, the editor has to verify it against lem:shape-quartet and cor:shape(b) of P47 itself.)

**Entry for ROUTES-TRIED-INDEX (for the editor to add):**
> - **O1_COMPOSITION_001 (phase 204p, O1): branch composition rule of Φ200 REFUTED as a barrier (PROVED; KP CITED).**
>   lem:transfer excludes a conjunction only with a common falsifier. E ∧ F ∧ I3 has ζ as its only model, so
>   there is no death branch. What remains is Φ200′: the sign step uses at least 2 channels with no common falsifier. F is mandatory because of
>   a_P and E over ℕ is mandatory because of the quartets (correction INTEGRATION_O1_001). Chain/compose criterion (Def. O1.2, Prop. O1.C, Lemma O1.E). Lemma R∧gap, (H-b)∧(H-d), Poisson-Möbius
>   and FF_001 CHAIN; h_par is TRANSFER. Spec (S1)–(S4) OPEN; only seed: Q-P2.2 + F. Do not retry «proving the rule».
