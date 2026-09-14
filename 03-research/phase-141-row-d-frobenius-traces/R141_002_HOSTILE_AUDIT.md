# R141.002 — Hostile audit, round 1, phase 141

*Auditor: Claude Opus 5 (hostile). Date 2026-09-13. Object of audit: `R141_001_BUILDER_ROUND1.md`
(888 lines) and `README.md`. Inputs re-read independently: `R141_000`; `R140_005`; `R140_001`
§D.24 (Def. D.24.1/D.24.3, Prop. D.24.3a, Thm D.24.4, Thm D.24.5, Thm D.24.7, Cor. D.24.12);
Paper 46 `main.md` §§11–13 (Def. 11.4, Lem. 11.4a, Thm 11.5, Thm 11.7, Thm 11.8, Thm 11.10,
Thm 11.11, Thm 11.13, Thm 11.14, Thm 12.3 **and its proof**, Rem. 12.3a/12.3b, Lem. 12.4A,
Prop. 12.4B, §12.5, §13.1, Def. 13.4); Paper 45 Thm 10.4 as cited; Paper 44 §8bis as cited.
Every algebraic identity below was recomputed from Paper 46's normalization, not copied.*

**Standing method.** Every claim assumed wrong until reconstructed. Labels are challenged
independently of whether the underlying mathematics is right: a correct proof of a restatement is
still a restatement.

---

## 0. Summary

**Verdict: REVISE.** No finding invalidates a computation — the three nontrivial calculations of the
round (`χ = 3/16`, the `−1/16` minimum, the Serre-type cancellation implicit in D.27.3) are correct,
and Lemma D.26.4 / Theorem D.26.5 are genuinely proved. The failures are (i) one asserted-as-proved
screening claim that is not proved and is in fact a category error (H1), (ii) a systematic
**inversion of the sign of the round's own result**: the "dichotomy" is not an obstruction, it is the
shape of Weil's argument, already inside Paper 46 Theorem 12.3 (H2, H5), (iii) a repetition of the
non-sequitur Paper 46 §13.1 explicitly withdrew (H3), (iv) a technical error in D.28.1's operator
inverse (H4), and (v) a candidate the round should have found and did not, which overturns the
round's recommendation for phase 142 (H6).

| | count |
|---|---|
| FATAL | 0 |
| MAJOR | 7 (H1–H7) |
| MINOR | 7 (H8–H14) |

| item | verdict |
|---|---|
| **D.26** (traces, `ker T`, `𝔐`) | **ACCEPT with repairs.** D.26.1, D.26.3, D.26.4, D.26.5, D.26.6 are proved (H8, H10 are repairs of wording/citation, not of the conclusions). D.26.7–D.26.10 are correct but are **restatements**, not structure theorems; labels must be downgraded (H7). D.26.11 correct as stated about *proofs*; its gloss overshoots (H3). |
| **D.27** (the quadratic candidate) | **ACCEPT the computations, REJECT the framing and three labels.** D.27.1, D.27.3, D.27.6, D.27.8 verified line by line. D.27.4 and D.27.5 are true but carry no content beyond Thm 12.3 + Thm 11.13 (H2, H5). The FATAL-screen claim is **not proved** (H1). |
| **D.28** (O-17) | **ACCEPT modulo one repair.** The two checks named by R8 (non-real DH zero; bounded strip) are correct. The statement that `Π` is inverted by `G_{1/2}∗G_{1/2}` is **wrong** (H4); the repair is Paper 46 Lemma 3.1 and costs nothing. O-17 stays `CLOSED (modulo the 106_11 import)`, exactly the standing of Prop. 12.4B. |
| **D.29** (synthesis) | **REJECT the recommendation.** "An obstruction theorem, not an assembly" does not follow from what was proved, and is refuted by the candidate of H6. |
| README / labels / paper list | **REVISE** (H12, H13, H14, H11). |

---

## 1. Findings

### H1 — MAJOR. The FATAL screen is asserted, not proved, and as stated it is a category error.

*Location:* `R141_001` head matter ("FATAL screen, run first and reported first"), D.27.3 closing
box, D.29 §1 last bullet, README row D.27.6.

*Claim audited:* "*No clause (c) of this round closes unconditionally, for any `C`* … **The FATAL rule
is not triggered, and the reason is proved, not asserted.**"

*Why unproved.* The stated support is (1) Theorem D.27.6 — which concerns the **single** kernel
`C^{deg}` — and (2) Theorem D.27.5 — "for every `C` either (b′) is outright false or (c) implies RH".
(2) does not support the claim: in **case (A)** Theorem D.27.5 says *nothing whatever about (c)*. It
concludes only that (b′) fails. So for every `C` landing in case (A) — which, by Corollary D.27.5a(i),
is every PSD `C` with a nonzero `N_{≥1}`-block, i.e. the generic case — the round has **no** statement
about whether (c) holds unconditionally. The quantifier "for any `C`" is unearned.

The necessary condition the builder itself isolated, **(Q1)** `4Q_C(x(E)) ≥ I_∞(E,E)`, is exactly
where the missing proof would have to live, and D.27.3(iii) states (Q1) without ever deciding it.

*Why it is also a category error.* "(c) closes unconditionally" is a statement about *provability*,
not about truth. If RH is true then (c) for `h⁰_{deg}` **is** true, by D.27.6 itself; what is absent
is a proof of it not routed through RH. Restricted to primitive classes, (Q1) reads
`4Q_C(x(F)) ≥ −W(F)`, and deciding it for `Q_C ≡ 0` is precisely Weil positivity. So no argument of
the trace class can establish "(c) is not unconditional"; the honest screen is the opposite one.

*Repair.* Replace the claim by: *"(c) is nowhere proved in this round; for `C^{deg}` a proof of (c)
would be a proof of RH (D.27.6), and for every `C` in case (B) likewise (D.27.5(B)); for `C` in case
(A) the status of (c) is not decided here. The FATAL rule is therefore not triggered because **no
inequality with a sign is proved**, not because one is shown to be unprovable."* Delete "proved, not
asserted" or prove (Q1) false for some explicit `C` — which, per the paragraph above, cannot be done
unconditionally.

*Severity.* MAJOR: the round's first sentence claims a proof it does not have, on the one clause the
standing rules single out.

---

### H2 — MAJOR. The "dichotomy" (Thm D.27.5) has no content beyond Paper 46 Theorem 12.3, and it is stated with the sign of its conclusion inverted.

*Location:* Theorem D.27.5, Corollary D.27.5a, D.29 §1 and §4, README ("the dichotomy … PROVED",
"Row-D: the class is closed negatively").

*The mathematics is correct.* I reconstructed both branches:

* **(A)** is Theorem D.27.4 contrapositively; verified (see H5).
* **(B)**: `−F` is primitive when `F` is, so `Ψ(−x(F)) = Ψ(x(F)) = 0`; `h⁰(nF) = n²Ψ(x(F)) = 0`;
  `h⁰(K−nF) = Ψ(x(K)−n x(F)) = n²Ψ(n^{−1}x(K) − x(F))` by positive 2-homogeneity with `λ = n > 0`,
  and ray-continuity at `r = 0` gives `Ψ(n^{−1}x(K)−x(F)) → Ψ(−x(F)) = 0`, hence `h⁰(K−nF) = o(n²)`.
  Then (c) at `E = nF`, with `I_∞(nF,K) = ½n\deg F = 0`, gives `o(n²) ≥ ½n²I_∞(F,F) + χ`, so
  `I_∞(F,F) ≤ 0`, and Paper 45 Thm 10.4 gives RH. **The `o(n²)` step is correct** and the
  ray-continuity hypothesis is exactly what it needs; `max(Q_C∘x,0)` with `C` finitely supported has
  it (it depends on finitely many coordinates and is continuous). No gap.

*Why there is no content.* Theorem 12.3 already says: **any** `h⁰` with (a),(b′),(c) implies RH. So
"either (b′) is false, or (c) implies RH" is, for any `h⁰` satisfying (a), a tautology modulo
Theorem 12.3 — if (b′) holds and (c) holds, RH follows by 12.3 alone, with no homogeneity, no
continuity, and no traces. The only genuine increment of D.27.5(B) is that for the 2-homogeneous
ray-continuous subclass **(b′) is not needed** to reach RH: (c) alone suffices. That is a *weakening
of the hypotheses of the programme's central reduction*, i.e. **good news**, and the round records it
as the class's death.

*Why the dichotomy is not a dichotomy of outcomes.* Case (B) does **not** assert (b′) holds. The
round's own `h⁰_{deg}` is in case (B) (it vanishes on primitives) **and** fails (b′) (it is a
bidegree-function; `R140` Thm D.24.7 — or directly, `h⁰_{deg}(−K) = ¼ > 0` while `\deg(−K) = −1 < 0`).
So "exactly one of (A),(B)" is a partition of `Ψ`, not of failure modes, and the reading
"either (b′) is false or the candidate is alive with (c)=RH" is wrong: both can fail at once.

*Repair.* (i) State D.27.5 as: *for the 2-homogeneous ray-continuous class, (c) alone implies RH in
case (B), which removes (b′) from Theorem 12.3's hypotheses on that class; in case (A), (b′) fails.*
(ii) Delete every phrase presenting "(c) implies RH" as a failure. (iii) Add the observation that
case (B) does not imply (b′), with `h⁰_{deg}` as the example.

---

### H3 — MAJOR. "No branch survives the falsifiers" repeats the non-sequitur Paper 46 §13.1 withdrew (finding M1 of `R135_002`).

*Location:* D.27.5 acceptance tests (AT-1)(ii), (AT-2); D.29 §1 bullet 4 ("**No branch survives the
falsifiers**"); D.26.11's gloss ("`𝔐` and the trace framework … **can carry no sign**"); README
("the candidate class … closed **negatively and unconditionally**").

*The withdrawn inference.* Paper 46 §13.1, Restatement 13.3 + the bracketed withdrawal: *"a
model-uniform **definition** may satisfy (a)+(b′)+(c) for `ξ` and fail them for `Ξ_a`"*; what survives
is only the schema *no derivation of the clauses can be carried out inside the model-uniform data
alone*. The builder's Corollary D.28.2 is worded correctly (it quantifies over **proofs**: "any rule
whose (a)+(b′)+(c) **proof**, read at `Z = Ξ_Q`, concludes …"). But D.29 §1 and the README convert
this into a statement about the `ξ`-candidates: case (B) "is false at `Ξ_a` … and at `Ξ_Q` …
**No branch survives**". It does not follow. A 2-homogeneous `Ψ` of the `ξ`-traces landing in case (B)
is refuted at `Ξ_Q` only if its case-(B) property and its (c) are proved model-uniformly — which is
the schema, not a refutation.

*Concretely:* `h⁰_{deg}` is in case (B) for `ξ`, and (c) for it is **equivalent to RH** (D.27.6).
"Refuted at `Ξ_Q`" would say RH is refuted. What is actually refuted at `Ξ_Q` is the `Ξ_Q`-instance,
which is the standing T2 content and nothing more.

*Repair.* Restrict every "no branch survives" to: *no model-uniform proof of (c) for a case-(B) `Ψ`
can exist, since such a proof would apply at `Ξ_Q` and `Ξ_a` where the conclusion is false
(D.28.1, Prop. 12.4B).* Same edit in D.26.11's gloss: what is proved is that **the theorems of D.26
transport**, hence that no *proof* inside D.26 can carry a sign — not that the objects "can carry no
sign".

---

### H4 — MAJOR. D.28.1: the inverse of `Π` is wrong, and compact support of the inverse is asserted where it must be cited.

*Location:* D.28.1, paragraph *The operator*: "`Π : C_c^∞(I_T) → P_T^{(P)}` is a linear bijection with
inverse `F ↦ G_{1/2}∗G_{1/2}∗F`, `G_c(t) = \tfrac1{2c}e^{−c|t|}` with `c_1 = c_2 = ½` (the degenerate
case of Lemma 12.4A(iii))."

*Two errors.*
1. `Π = −∂_t² + ¼` is of **order 2**; its Green kernel is the **single** `G_{1/2}`, i.e.
   `Π(G_{1/2}∗F) = F`. The double convolution `G_{1/2}∗G_{1/2}` inverts `Π²`. Lemma 12.4A's operator
   is `(∂²−c_1²)(∂²−c_2²)`, order 4; its "degenerate case `c_1 = c_2 = ½`" is `(∂²−¼)² = Π²`, **not**
   `Π`. The degenerate case of 12.4A is therefore the wrong statement to invoke here.
2. More seriously, `G_{1/2}∗F` is **not compactly supported** for general `F ∈ C_c^∞` (the kernel is
   `e^{−|t|/2}`, supported everywhere). Compact support of the preimage is exactly the non-trivial
   content, and it holds **only on the primitive class**: Paper 46 Lemma 3.1 (quoted verbatim inside
   Thm 11.10's proof: *"by Lemma 3.1 every primitive `F ∈ C_c^∞(I_T)` is `ΠH` with `H ∈ C_c^∞(I_T)`,
   for every `T`"*). That is the statement D.28.1 needs, and it is the `P = \{0,1\}` case already in
   the corpus — so the repair strengthens the claim's provenance.

*Repair.* Replace the sentence by: *"`Π` maps `C_c^∞(I_T)` onto `P_T^{(\{0,1\})}` and is injective
there; surjectivity with compactly supported preimage is Paper 46 Lemma 3.1, the `P = \{0,1\}` case,
which is the exact analogue of Lemma 12.4A(iii) and needs no degenerate limit."* No downstream step
changes: the tail bump `D ↦ D+4` already corresponds to the order-2 symbol
`|π_P(ρ)|² = |ρ(1−ρ)|² = O((1+|z|)^4)`, which is consistent with `Π` and **inconsistent** with `Π²`
(that would give degree 8) — so the rest of the proof was written for the correct operator and only
this sentence is wrong.

---

### H5 — MAJOR. D.27.4 is Theorem 11.13 + (b′); it is not a theorem about the traces, and "strictly wider in scope than D.24.7" mis-describes it.

*Location:* Theorem D.27.4; the box after Cor. D.27.5a; README ("**(b′) forces `h⁰ ≡ 0` on the
primitive subspace** … PROVED (wider than D.24.7)"); P46-20.

*Reconstruction.* The proof is: `Ψ(x(F)) > 0` ⟹ (by D.26.8) `x(F) ∈ 𝔐` ⟹ (by D.26.9(iii)) both polar
coordinates positive ⟹ contradiction with `t_0(F) = 0`. Strip the traces out: (b′) at `F` gives
`E' ≥ 0`, `E' ≢ 0`, `F − E' ∈ 𝓝_∞`; `\deg` is `𝓝_∞`-invariant (Thm 11.13(ii),(iv)) so `\deg E' = 0`;
but `\deg E' > 0` (Thm 11.13(i)). Contradiction. **Two lines, no traces, no `𝔐`, no `T`.** The claim
holds verbatim for every `h⁰ : D^W → R_{≥0}` satisfying (b′), trace-built or not. So:

* `\deg` **is** `𝓝_∞`-invariant, and that **is** the whole argument (the lead's check: confirmed);
* the trace machinery of D.26 contributes nothing to D.27.4 beyond re-expressing `\deg` as
  `t_{0,1}+t_{0,2}`;
* this is Steps 2 and 4 of Theorem 12.3's own proof, which I re-read: Step 4 is literally *"By Thm
  11.13(ii),(iv) the degree is constant on `𝓝_∞`-cosets, so `\deg E' = \deg(nF) = 0`. By Thm
  11.13(i), `\deg E' > 0`. Contradiction."*

*On "wider than D.24.7".* D.24.7 **refutes (b′)** for every nonzero bidegree-function. D.27.4 refutes
nothing; it *constrains* any `h⁰` satisfying (b′). These are not comparable by scope, and calling
D.27.4 "strictly stronger in scope, weaker in conclusion" (builder's own box) while the README prints
"wider than D.24.7" is inconsistent. The label should be `RESTATEMENT (of Thm 12.3 Steps 2,4)`.

*What it actually says, correctly read:* `h⁰` vanishes on every class of degree `≤ 0`. That is the
classical fact `h⁰(D) = 0` for `\deg D < 0` and for non-trivial `\deg D = 0`. It is a **sanity check
passed**, not an obstruction — see §2 below.

---

### H6 — MAJOR. A candidate the round should have found: `h⁰_{RR}` and its degree-gated form. (a) and (c) are free; **all** the content is (b′); and the gated form survives both of the corpus's standing refutations.

*Location:* the gap is D.27.0 (the motivation for quadratic `Ψ`), D.29 §3 (iii) (the list of
"escapes"), and D.29 §4 (the recommendation).

**(1) The Serre-type symmetry of (c)'s right-hand side.** Put
`R(E) := ½I_∞(E,E) − ½I_∞(E,K) + χ`. From bilinearity and symmetry of `I_∞` alone (Def. 11.4,
Lem. 11.4a) — **no** value of `I_∞(K,K)` is needed:

    R(K−E) = ½[I_∞(K,K) − 2I_∞(K,E) + I_∞(E,E)] − ½[I_∞(K,K) − I_∞(E,K)] + χ
           = ½I_∞(E,E) − ½I_∞(E,K) + χ = R(E) .

`R(K−E) = R(E)` **identically, on all of `D^W`, unconditionally.** (With Thm 11.8(i) this reads
`R(E) = ab − ½W(E) − ¼\deg E + χ`, manifestly invariant under `(a,b,W) ↦ (½−a,½−b,W)` — the check the
lead asked for, done in Paper 46's normalization.)

**(2) Consequence: (c) is free.** Define `h⁰_{RR}(E) := \max(R(E),0)`. Then (a) is trivial and

    h⁰_{RR}(E) + h⁰_{RR}(K−E) = 2\max(R(E),0) ≥ R(E) ,

so **(c) holds unconditionally, for every `χ`**. Hence the entire content of Theorem 12.3's hypothesis
sits in (b′): *`R(E) > 0` ⟹ `E` is equivalent mod `𝓝_∞` to a nonzero effective class.*

**(3) The lead's "(b′) for `h⁰_{RR}` ⟺ RH" is false; here is the exact gap.** Forward: (b′) + (a) +
(c) ⟹ RH by Thm 12.3. Backward: **(b′) fails for `h⁰_{RR}` unconditionally**, for every `χ`. Witness:
`E = mK` with `m < 0`. Then `I_∞(mK,mK) = m²·½` and `I_∞(mK,K) = ½m`, so
`R(mK) = \tfrac{m²}{4} − \tfrac m4 + χ → +∞` as `m → −∞`, while `\deg(mK) = m < 0`, so `mK` is
equivalent to no nonzero effective class (Thm 11.13(i),(ii)). So the biconditional is wrong in the
`⟸` direction, and not by a repairable margin.

**(4) The repair, which is the phase's missing candidate.** Gate by degree:

    h⁰_{RR}^{+}(E) := \max(R(E),0)·\mathbf 1_{\{\deg E > 0\}} .

*(a)* trivial. *(c)*: `\deg K = 1`, so `\deg E ≤ 0 ⟹ \deg(K−E) = 1 − \deg E ≥ 1 > 0`, and both gates
cannot be off at once. Case `\deg E ≤ 0`: LHS `≥ h⁰_{RR}^+(K−E) = \max(R(K−E),0) = \max(R(E),0) ≥ R(E)`
by (1). Case `\deg E ≥ 1`: symmetric. Case `0 < \deg E < 1`: both gates on. **So (c) holds
unconditionally, with any `χ`, for `h⁰_{RR}^{+}`.** *(Note this is a second, independent refutation of
H1's headline claim: (c) does close unconditionally — for a `Ψ` outside the finitely-supported
quadratic class, which is precisely why the class was the wrong ansatz.)*

*It clears the growth wall on the nose:* `h⁰_{RR}^{+}(mK) = \tfrac{m²}{4} − \tfrac m4 + χ ~ \tfrac14m²`,
the `(P139)` constant.

*It vanishes on `P^W`* (degree 0) — consistent with D.27.4, as it must be.

*It is not 2-homogeneous* (the linear and constant terms), so it is outside D.27.5's class; it is a
member of the "escape" family D.29 §3(iii) names but does not populate.

*It survives `R140` Thm D.24.7's witness.* D.24.7 refutes bidegree-functions with `E_0 + tF`, `F`
primitive: the bidegree is frozen while `t` grows. Here `R(E_0+tF) = ab − ½W(E_0+tF) − ¼\deg E_0 + χ`
and `W(E_0+tF) = W(E_0) + 2t·(\text{cross}) + t²W(F)`, so under RH (`W(F) ≥ 0`) the value tends to
`−∞` and the gate never fires spuriously. **This is exactly Cor. D.24.12's requirement** — that an
admissible `h⁰` read `Z(E)` through pairings `I_∞(E,X)` with `Z(X) ≠ 0` — met by the single pairing
`X = E` itself, which the phase never tried.

*It survives the easy (b′) probes.* `K > 0` pointwise (Paper 46 Thm 11.7(i), elementary after the
phase-135 LF6 repair), so `mK` is **effective** for `m > 0` and the `m > 0` half of the `mK` ray is
unproblematic; the `m < 0` half is killed by the gate.

**(5) Corpus check performed by the auditor.** `grep -rn "RR-defined\|(RHS)_+\|Riemann–Roch defined\|
h⁰_RR\|h0_RR"` over `--include=*.md --include=*.tex --include=*.py`: **zero hits.** Paper 46 §13.1
(Def. 13.1, Thm 13.2, Restatement 13.3) is the `H⁰`-set candidate; §13.2 Def. 13.4 is the lattice
count `h⁰_{\mathbb Z}`; phase-135's `h0_candidate.py` certifies Def. 13.4. `R135_*` contain no
Riemann–Roch-defined `h⁰`. **`h⁰_{RR}` and `h⁰_{RR}^{+}` are not in the corpus.**

**(6) What this means for phase 142.** The round's recommendation ("an obstruction theorem, not an
assembly") is refuted by the existence of `h⁰_{RR}^{+}`: (a) and (c) are settled unconditionally, and
row D reduces to the **single** statement

> **(b′)⁺** `\deg E > 0` and `½I_∞(E,E) − ¼\deg E + χ > 0` ⟹ `E ≡ E' \pmod{𝓝_∞}` for some
> `E' ≥ 0`, `E' ≢ 0`,

which implies RH (Thm 12.3) and is refuted by nothing in the corpus. It is not known to follow from
RH — that is the open direction, and it is where phase 142 belongs. The trace framework of D.26
remains useful **as the language for (b′)⁺**: by Thm D.26.8 it is the containment
`\{R > 0,\ \deg > 0\} ⊆ 𝔐`, a zero-free statement about the moment cone — which is the one thing the
round built and then declined to point at its own target.

*Severity.* MAJOR: the round's principal conclusion (the recommendation) is wrong, and the object
that shows it is two lines from the round's own D.27.3.

---

### H7 — MAJOR. D.26.9(iv),(v) and D.26.10(iii) are restatements labelled as structure, and one clause is an overreach.

*Location:* Thm D.26.9(iv),(v); Prop. D.26.10(iii); README ("`𝔐` is … the moment cone of an explicit
curve, with dual `𝒫_g^*` … PROVED (O-15 answered)"); P46-19.

1. **(i)–(iii) are correct** and I verified them: convexity and `λ𝔐 = 𝔐` from linearity of `T` and
   convexity of `\{E ≥ 0\}`; pointedness from `\deg(E_1+E_2) > 0` versus `\deg = 0` on `𝓝_∞`;
   `x_{0,1}, x_{0,2} > 0` from `Φ_{E'}(1) = ∫E'e^{u/2}`, `Φ_{E'}(0) = ∫E'e^{−u/2}`. No objection.
2. **(iv) is a change of variable, not a structure theorem.** `x(E) = ∫v(u)dμ_E(u)` is (D.26.2)
   divided and multiplied by `2\cosh(u/2)`. Note that the **first two components of `v` already
   determine `u`**: their ratio is `e^{u}`. So `v` is an injective parametrization and the "curve"
   `𝒞` is a graph; `𝔐` is simply the image of the cone of positive measures with `D^W`-density under
   a fixed injective map. Calling this "the Markov moment cone of an explicit curve" adds vocabulary,
   not information. And `𝒞` is not **explicit**: `w_g` is given by (11.16), a sum over the zeros; it
   is zero-*free* in the sense of Def. 11.4 (it is `PRIME − ARCH`), but it is not written down.
3. **(v) has a closure/regularity gap the label hides.** `⟨λ,x⟩ ≥ 0` on `𝔐` for `λ ∈ 𝒫_g` is proved;
   "the two coincide up to closure" by "(iv) and mollification" is not proved — the density of
   `D^W`-densities in positive measures in the relevant topology is asserted. The `§ Label` table
   concedes this ("PROVED modulo mollification regularity in `⊇`"), but the README and P46-19 print
   "with dual `𝒫_g^*`" flat.
4. **D.26.10(iii)'s "These are **all** the linear conditions" is an overreach** given 3: it is exactly
   the unproved `⊇`. Delete "all", or state it as conditional on the closure claim.

*Repair.* Downgrade D.26.9(iv),(v) to `RESTATEMENT`; delete "explicit" before "curve"; delete "all"
in D.26.10(iii); align README and P46-19 with the `§ Label` table.

*What survives, and is worth keeping:* Theorem D.26.8 ((b′) `⟺ \{Ψ>0\} ⊆ 𝔐`, including the `E' ≢ 0`
clause, which is handled **correctly** — Def. D.26.7 builds `E' ≢ 0` into `𝔐` and D.26.9(ii) gives
`0 ∉ 𝔐`, so "`t ≠ 0`" is not an extra hypothesis but a consequence; the lead's check: **passed**),
and D.26.9(i)–(iii).

---

### H8 — MINOR. Lemma D.26.4: residue bookkeeping, an over-strong hypothesis, and a `ξ`-specific half-plane.

*Location:* Lemma D.26.4 and its transport in D.26.11(ii).

I reconstructed the proof and it is **correct**. Details:
* Interchange: `|n^{−w−s_ρ}| = n^{−\mathrm{Re}w−\mathrm{Re}s_ρ} ≤ n^{−\mathrm{Re}w+½}` since
  `\mathrm{Re}\,s_ρ > −½` by (E2); so `Σ_ρ|c_ρ|Σ_n n^{−\mathrm{Re}w+½} < ∞` for `\mathrm{Re}\,w > 3/2`.
  Correct.
* Meromorphy on compacts: finitely many `ρ` with `3/2−ρ` near `𝒦` (since `|γ_ρ| → ∞`), the rest
  bounded by `|c_ρ|(1+|γ_ρ|)^{A_0}C` via `|ζ(σ+it)| ≪_{σ_0}(1+|t|)^{A_0}` uniformly on `σ ≥ σ_0`,
  `|t| ≥ 1`. Correct, including the functional-equation growth for `σ_0 < 0`.
* Identity theorem on `C ∖ \{3/2−ρ\}` (connected), poles removable, residue at `w = 3/2−ρ_0` isolates
  `c_{ρ_0}` because `ρ ↦ 3/2−ρ` is injective and `\mathrm{Res}_{s=1}ζ = 1`. Correct.

Three defects, none fatal:
1. The residue is written `m(ρ_0)c_{ρ_0}`. Whether the multiplicity appears depends on whether the
   index set is the zero **multiset** or the set of distinct zeros. In D.26.5 the sum (D.26.1) is over
   the multiset (Thm 11.5), so the residue is `m(ρ_0)c_{ρ_0}` only if `c` is constant on the fibre —
   which it is (`c_ρ = Φ_E(ρ)Φ_g(1−ρ)` depends on `ρ` only). State the convention once; the
   conclusion is unaffected since `m(ρ_0) ≥ 1`.
2. The hypothesis "`Σ_ρ|c_ρ|(1+|γ_ρ|)^A < ∞` for **every** `A`" is stronger than the proof needs
   (`A` may be chosen per compact set, `A = A_0(𝒦)`). It is satisfied in the application, so this is
   cosmetic — but the lemma as stated has a smaller hypothesis class than it deserves, and the
   "right" class is: `Σ_ρ|c_ρ|(1+|γ_ρ|)^{A} < ∞` for every `A`, *or* any class with
   `\sup_ρ|\mathrm{Re}\,ρ − ½| < ∞` and `|c_ρ|` of rapid decay. Say so.
3. The half-plane `\mathrm{Re}\,w > 3/2` is `ξ`-specific. For a general `Z` it is
   `\mathrm{Re}\,w > 1 + θ_Z`. D.26.11(ii) patches this correctly, but Lemma D.26.4 should carry
   `θ` from the start rather than be "verbatim"-transported.

*The blueprint deviation (ζ-transform instead of Bohr) is correct and correctly justified:* the data
live on `\{\log n\}`, a discrete set of finite upper density in the Bohr sense with no continuum, and
a general-Dirichlet-series uniqueness theorem would need the exponents `\log n` on the *series* side,
which is precisely what the ζ-transform supplies. **Accepted.**

---

### H9 — MINOR. D.28.1: interpolation bookkeeping, and the untested positive contributions.

1. "*the construction imposes **four** interpolation conditions, one at each point of the quartet*"
   is inconsistent with the two-real-parameter family `(α,β)` used one line earlier. For real even
   `F`, `Φ_F(1−s) = Φ_F(s)` and `Φ_F(\bar s) = \overline{Φ_F(s)}`, so the value at `ρ_0` determines
   the values at all four quartet points: **one complex condition**, matched by the two real
   parameters. The `R`-linear isomorphism `R² → C` stated is exactly right; the "four conditions"
   sentence should be deleted.
2. The quartet's contribution is `4\,\mathrm{Re}[Φ_F(ρ_0)²]`, negative for `\arg Φ_F(ρ_0)` near
   `π/2` — fine. But the tail contains (i) the zeros of `Ξ_Q` **on** the critical line, contributing
   `|Φ_F|² ≥ 0`, and (ii) the real zeros of `Λ_Q` in `(0,1)` (R139 Cor. D.19.4a), contributing
   `Φ_F(β)² ≥ 0`. Both push the **wrong** way. The proof handles them only through absolute-value
   domination for large `N`, which is legitimate (the `106_11` bound is on `|·|`), but the text's
   parenthetical dismissal (*"they are other zeros, living in the tail, and no step needs `Ξ_Q` to
   have none"*) should say **why**: the domination is in modulus and is uniform on the strip
   `|\mathrm{Im}\,z| ≤ θ_Q`, so sign plays no role. One sentence.
3. The two checks named by R8 are **verified**: `Z_Q(σ) = Σ r_Q(n)n^{−σ} > 0` for real `σ > 1` since
   `r_Q(n) ≥ 0` and `r_Q(1) > 0`, and the archimedean factor and `½σ(σ−1)` are positive there, so
   every zero with `\mathrm{Re}\,s > 1` is non-real — **correct**, and it gives `γ_0 ≠ 0`,
   `β_0 ≠ ½`, `x_0y_0 ≠ 0`, four distinct quartet points. The strip: `Σ_{n≥2}r_Q(n)n^{−σ} → 0` as
   `σ → ∞` uniformly in `t`, so no zeros for `\mathrm{Re}\,s ≥ σ_1`, and the functional equation
   reflects — **correct**, `θ_Q < ∞`. Tail bump `D ↦ D+4` from `|ρ(1−ρ)|²` — **correct for `Π`**, and
   see H4.

---

### H10 — MINOR (statement, not conclusion). D.26.6's second map cites a decomposition Paper 46 does not give.

*Location:* Lemma D.26.6, *Second map*: "*by Theorem 11.10 and the last clause of Theorem 11.11 … this
puts `X ∈ 𝓝_∞ ⊕ Λ_ξ`, `Λ_ξ = span(K,K_{odd})`*".

Paper 46 Thm 11.10 states `I_∞(F,G) = 0` for all primitive `F ∈ C_c^∞` `⟺ Φ_G(ρ) = 0` at every zero —
**that is the whole perp**, and Paper 46 explicitly `REFUTED` (after Thm 11.10) the identification of
this space with `ξ·(\text{entire})`, i.e. with anything of the shape "`𝓝_∞ ⊕` a span of canonical
classes", unless all zeros are simple (`OPEN`). So `𝓝_∞ ⊕ Λ_ξ` is an unproved — and, per (11.13), an
over-strong — description of the perp.

*The conclusion is unaffected:* the proof only uses `Φ_X(ρ) = 0` at every zero, which is Thm 11.10(c)
directly. *Repair:* replace the sentence by "*by Thm 11.10, `Φ_X(ρ) = 0` at every zero of `ξ`*", and
delete `Λ_ξ`. The Langer / Riemann–von Mangoldt comparison that follows is correct as written
(`T\log N/π + O(1)` versus `(T/π)\log(T/2πe)+O(\log T)`).

---

### H11 — MINOR. Corpus-check citations partly unverified.

I re-ran the round's greps. Confirmed: "moment cone" occurs only in `R140`, `R141` (correct);
"Frobenius trace"/"trace of Frobenius" hits are phase-107 (`107_121` NO-GO, `107_171`), phase-120
`P3_*`, phase-17, phase-119 — none defining `I_∞(E,τ_{\log n}g)` (correct); "Bohr almost" hits
`NO-GO-LIST.md`, phase-25, `R140_001/003/004/005` — **`04-papers/32-*` does not appear** in the
`"Bohr almost"` grep, though the round cites "Paper 32". Either the citation is to a different string
("Bohr" alone) or it is wrong; state the string actually matched. Everything else in the corpus-check
box checks out, including the correct refusal to relabel `CORPUS_CHECK_ROW_D_PLAN` items 6, 7, 8.

---

### H12 — MINOR. Labels to change.

| item | round-1 label | audited label |
|---|---|---|
| D.26.8 | PROVED | PROVED (correct) — but it is a **definition-chase**; keep PROVED, drop "the answer to O-15" rhetoric |
| D.26.9(iv),(v) | PROVED | **RESTATEMENT** ((iv)); **PROVED `⊆` / OPEN `⊇`** ((v)) |
| D.26.10(iii) | PROVED | PROVED minus the word "all" |
| D.27.4 | PROVED, "wider than D.24.7" | **RESTATEMENT** (Thm 12.3 Steps 2,4 + Thm 11.13); delete the comparison to D.24.7 |
| D.27.5 | PROVED | PROVED, but **content restated** per H2: "(c) alone implies RH on the case-(B) class", not an obstruction |
| D.27.6 | PROVED, "FATAL screen passed" | PROVED (verified); "FATAL screen" claim per H1 |
| README "closed negatively and unconditionally" | — | **delete** (H3, H6) |

---

### H13 — MINOR. D.27.6: two omissions (the computation itself is correct).

I recomputed. With `d = a+b`, `\deg K = 1`:
`\tfrac14d² + \tfrac14(1−d)² = \tfrac12d² − \tfrac12d + \tfrac14`, and
`R(E) = ab − \tfrac12W − \tfrac14d + χ`, so
`LHS − RHS = \tfrac12d² − ab − \tfrac14d + \tfrac14 + \tfrac12W − χ
= \tfrac12(a²+b²) − \tfrac14(a+b) + \tfrac14 + \tfrac12W − χ` — **exactly as printed**;
`\min_a(\tfrac12a² − \tfrac14a) = −\tfrac1{32}`, twice `= −\tfrac1{16}`; `3/16 − χ ≥ 0`. Correct.
Converse at `E = nF`: `\tfrac14 + \tfrac12n²W(F) ≥ χ` for all `n` forces `W(F) ≥ 0`, i.e.
`I_∞(F,F) = −W(F) ≤ 0`, i.e. RH. Correct.

Omissions: (1) `χ = 3/16` is **optimal**, and the extremal class is `E = ½K` (`a = b = ¼`,
`W(½K) = 0` since `Φ_K(ρ) = ξ(ρ) = 0`) — worth stating, since D.24.4 states optimality for its
candidate; (2) `h⁰_{deg}` **fails (b′)** (it is a bidegree-function; directly,
`h⁰_{deg}(−K) = ¼ > 0`, `\deg(−K) < 0`), which must be printed next to the theorem or the reader
takes it for a live candidate.

**The `3/16` vs `1/8` question (lead item 3), answered.** They belong to **different candidates** and
are **both** suprema of admissible `χ` **under RH**:
* `χ = 1/8 = c²/2` (`c = ½`): `R140` Thm D.24.4, candidate `h⁰_□(E) = \max(a,0)\max(b,0)` — the
  **tensor square** of the bidegree, extremal at `(a,b) = (c,0),(0,c)`;
* `χ = 3/16`: this round, candidate `h⁰_{deg}(E) = \tfrac14(a+b)²` — the **square of the degree**,
  extremal at `(a,b) = (¼,¼)`.
They differ because `\tfrac14(a+b)² ≥ \max(a,0)\max(b,0)` pointwise (indeed `\tfrac14(a+b)² ≥ ab`,
with the gap `\tfrac14(a−b)²`, and `ab ≥ \max(a,0)\max(b,0)` where the latter is nonzero), so the
degree square is the **larger** `h⁰` and tolerates the **larger** `χ`. The round's statement that the
two "belong to different candidates" and that D.24.4 is not contradicted is **correct**; the ordering
`3/16 > 1/8` is not an improvement of D.24.4 but a consequence of comparing a larger function, and the
round should say so in one clause rather than leaving "it exceeds" to be misread.

---

### H14 — MINOR. The one place a zero is named: the admissibility of `g`.

`t_n(E) := I_∞(E,τ_{\log n}g)` is genuinely zero-free (Def. 11.4 is the polarized arithmetic bracket;
Lem. 11.4a). **But** the `g` of Lemma D.26.1 is selected by a condition stated over `Z(ξ)`
(`Φ_g(1−ρ) ≠ 0` for every zero). That is a non-vanishing condition, not a location statement, and the
Baire argument is correct (the even subspace `E_{T−δ}` is Fréchet, `h ↦ ∫h\cosh((½−ρ)t)dt` is a
nonzero continuous functional on it, `Z(ξ)` is countable, `U` is open and nonmeagre) — but it means
(i) the **trace map depends on a choice made through the zero set**, and (ii) for each falsifier `Z`
the `g` must be **re-chosen**, so `T` is not one object transported across models. D.26.11(i) says
this implicitly; it should be said explicitly, since the standing rule ("do not define anything
through zeros") is the phase's own. Also worth noting: only `Φ_g(1−ρ) ≠ 0` is used, and it is used
only in D.26.5's last line — nothing quantitative depends on `g`.

---

## 2. Explicit answer to the lead's question (item 4)

> *Is the dichotomy content beyond Paper 46 Theorem 12.3?*

**No.** I read Theorem 12.3's proof in full. It fixes a primitive real `F ∈ C_c^∞`, sets `E = nF`,
uses (b′) at `K−nF` with ampleness (Step 2), (c) at `nF` (Step 3), and closes with **`\deg E' = 0`
versus `\deg E' > 0`** (Step 4). That is: `E = nF` for primitive `F`, and the vanishing of `h⁰` on
degree-zero classes, are **already the two moving parts of Theorem 12.3**. Remark 12.3a even tabulates
them against Hartshorne V.1.9 (*"effective of degree 0 is 0 → Thm 11.13(i),(ii)"*), and Remark 11.13a
says in advance that these, not the effectivity of primitive classes, are what Weil's argument needs.

Consequently:

**(i) The phase proves nothing about impossibility.** What it proves is:
* **D.27.4** = Theorem 12.3 Steps 2/4, restated as a property of `h⁰` rather than as a contradiction
  (H5). In classical geometry this is `h⁰(D) = 0` for `\deg D < 0` and for non-trivial `\deg D = 0` —
  a **required feature**, not an obstruction. An `h⁰` that did *not* vanish on `P^W` would be wrong.
* **D.27.5(B)** = the conclusion of Theorem 12.3 with `(b′)` deleted from the hypotheses, on the
  2-homogeneous ray-continuous subclass. This is the **proof shape**, reached with weaker hypotheses;
  it is a small strengthening of the programme's reduction, reported as its refutation.
* **D.27.5(A)** = "if `Ψ > 0` somewhere on `P^W`, (b′) fails" = the contrapositive of the same.

The single true negative statement of the round is therefore: **positively 2-homogeneous
ray-continuous `Ψ` is the wrong ansatz** — and even that is thin, because the reason is not about
traces or homogeneity but about `h⁰(mK) ~ ¼m²` requiring a linear-and-constant part (the same reason
`h⁰_□` needs a nonzero polar part). No impossibility beyond the ansatz is established; in particular
nothing rules out a non-homogeneous `Ψ∘T`, and O-14′ is **not** answered in any meaningful direction.

**(ii) `h⁰_{RR}`.** Verified in H6: `R(K−E) = R(E)` identically, from bilinearity and symmetry of
`I_∞` alone, with no input about `I_∞(K,K)`. Hence `h⁰_{RR} := \max(R,0)` satisfies (a) and (c)
trivially and unconditionally, and the whole of row D is the single clause

> **(b′)** `R(E) > 0 ⟹ E` is `𝓝_∞`-equivalent to a nonzero effective class.

The lead's proposed equivalence "(b′) for `h⁰_{RR}` ⟺ RH" is **false in the `⟸` direction**, and not
by a fixable margin: `R(mK) = \tfrac{m²}4 − \tfrac m4 + χ → +∞` as `m → −∞` while `\deg(mK) < 0`, so
(b′) for `h⁰_{RR}` is **unconditionally false for every `χ`**. The gap is located exactly there, and it
is closed by **gating on degree**: `h⁰_{RR}^{+} := \max(R,0)\mathbf 1_{\{\deg > 0\}}` still satisfies
(a) and (c) unconditionally (proof in H6(4), using `\deg K = 1` so the two gates cannot both be off),
grows like `¼m²` on the ray, vanishes on `P^W`, is **not** 2-homogeneous (so it is outside D.27.5),
and is **not** a bidegree-function (so `R140` Thm D.24.7 does not touch it — and its `E_0 + tF`
witness is actively defeated by the `−½W(E)` term, which is Cor. D.24.12's requirement met).
`h⁰_{RR}` and `h⁰_{RR}^{+}` are **not in the corpus** (grep in H6(5): Paper 46 §13 has the `H⁰`-set
candidate 13.1 and the lattice count 13.4 only; `R135_*` and `h0_candidate.py` are Def. 13.4).

**What this means for phase 142.** Not an obstruction theorem. Row D reduces, unconditionally, to one
statement — **(b′)⁺** of H6(6) — which implies RH by Theorem 12.3 and is refuted by nothing known.
Phase 142 should (1) enter `h⁰_{RR}^{+}` into the corpus with (a),(c) proved and `χ` optimized, (2)
state (b′)⁺ as the row's single open clause, (3) run the three falsifiers on it — note that (a) and
(c) transport to every `Z` by §12.5, so **the entire model-dependence is inside (b′)⁺**, which is the
sharpest form of T2's demand the row has yet produced, and (4) use D.26.8 to read (b′)⁺ as the
zero-free cone containment `\{R > 0,\ \deg > 0\} ⊆ 𝔐`, which is the legitimate use of this round's
moment cone. The round's own "scissors" (*vanish on `P^W`, grow like `n²` on `K + P^W`*) is satisfied
by `h⁰_{RR}^{+}`, which is the direct refutation of D.29 §3's reading of it as an obstruction.

---

## 3. What the round got right (recorded, so the repair does not delete it)

* **Lemma D.26.4 / Theorem D.26.5 (`ker T = 𝓝_∞`)** — the ζ-transform separation of `n^{½−ρ}` is
  correct, the interchange and the pole/residue identification are correct, the decay hypothesis is
  verified in the application, and the deviation from the blueprint's Bohr route is justified. This is
  the round's one new, clean theorem.
* **Theorem D.26.8** — (b′) `⟺ \{Ψ>0\} ⊆ 𝔐`, with `E' ≢ 0` correctly absorbed into `𝔐` (`0 ∉ 𝔐`).
* **D.26.9(i)–(iii), D.26.10(i),(ii),(v)** — correct; (v)'s honest scope note (one-sided, and shared
  by `Ξ_Q` via A4) is exactly right.
* **Lemma D.26.6** — the Langer / Riemann–von Mangoldt surjectivity argument is correct (modulo H10's
  citation).
* **D.27.3, D.27.6, D.27.8** — all computations verified, including `γ_C > 0`, the zero-trace
  indefiniteness of `C^{Frob}`, and the `NAMED CHOICE` discipline around `C^{Frob}_{nn} := 0` with
  Rem. 8bis.1c, Cor. 8bis.1b′, residue R2 and Thm 8bis.4a + Rem. 8bis.4b(3) carried. The R2
  distinction (`Q_{fin}` on radial profiles vs the discrete Gram of `\{Frob_n^{sm}\}`) is stated
  correctly and is not blurred anywhere.
* **D.26.11 as a statement about proofs** — correct; A3 is used nowhere, A7/A8/A9 nowhere in a proof,
  and clause (N) is correctly called moot **because nothing with a sign is proved**. (The gloss is
  what overshoots — H3.)
* **D.28.0** — both R8 checks correct (H9(3)).
* **No label change for row D** — correct, and correctly justified.
