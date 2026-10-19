# Doc 117 — Adversarial audit: the tensor index identity (Doc 106, Prop. 3.5)

**Phase 38 — Final audit.**

**Audited object:** Proposition 3.1 / Corollary 3.2 / Proposition 3.3 / Proposition 3.5
of Doc 106 (`phase-36-ABC-forms/106-amplifier-functor-systematic-search.md`), as
cited in P42 (Theorems 4.2 `thm:tensor-index` and 4.3 `thm:amplify`,
`06-papers/P42-amplification-survivor/main.tex`) and in P43 (ledger, item L3,
`06-papers/P43-master-quantifier/main.tex`, lines 330–332). Input: the signature
$(2m,2m)$ of $Q|_{\mathcal{K}_{\mathrm{off}}}$ (Doc 98, Prop. 6.1; Doc 96, Thm. 8.1).

**Mandate:** destroy, if possible, statements (A), (B), (C) described below.

---

## 0. Verdict

**SURVIVES WITH CORRECTIONS.**

- **(A)** the identity $\mathrm{neg.ind}(Q_1\otimes Q_2)=p_1q_2+q_1p_2$: **SURVIVES
  INTACT**. Classical linear algebra, correct proof, consistent with the
  multiplicativity of the signature in the Witt ring.
- **(B)** $\kappa(\psi^{\otimes k})=(4m)^k/2$ for signature $(2m,2m)$: **SURVIVES
  INTACT as algebra**; the *input* (the signature $(2m,2m)$ of the off-block) is
  conditional on the framework (V.1 / Hypothesis D) and P42 states it with less caution than the
  source documents.
- **(C)** superadditivity: the *defect identity* is correct, but the
  **Corollary 3.2 of Doc 106 is false as written** (it claims $\geq 0$ without the
  hypothesis $p_1,p_2\geq 1$; counterexample: $\langle-1\rangle\otimes\langle-1\rangle$),
  and its strictness "i.e." clause also fails without that hypothesis. **Item L3 of
  P43** overstates ("strictly superadditive" without qualifier). P42's Theorem 4.2,
  by contrast, is phrased with the exact condition and is correct.

None of the corrections touches the use case ($p=q=2m$, $m\geq 1$, where everything holds
with room to spare), but two publishable statements (Cor. 3.2 of Doc 106 and L3 of
P43) need fixing, and the conditionality of the input must be declared in P42.

---

## 1. Statement (A): $\mathrm{neg.ind}(Q_1\otimes Q_2)=p_1q_2+q_1p_2$

### 1.1 Verification of the proof (Doc 106, Prop. 3.1; P42, Thm. 4.2)

The proof via Sylvester bases is correct in every step, verified one by one:

1. **Existence of orthonormal bases with signs $\pm1$.** For a nondegenerate Hermitian
   form on a finite-dimensional $\mathbb{C}$-vector space, Sylvester's law of inertia
   holds in Hermitian form: there is a $Q$-orthogonal basis with
   $Q(e_a,e_a)=\varepsilon_a\in\{\pm1\}$ and the pair $(p,q)$ is invariant. Standard
   reference: Bognár, *Indefinite Inner Product Spaces* (Springer 1974), Chap. I; also
   Gohberg–Lancaster–Rodman [GLR83], Chap. I (already cited in Doc 98).
2. **The tensor product of Hermitian forms is Hermitian.** With
   $(Q_1\otimes Q_2)(u_1\otimes u_2, v_1\otimes v_2)=Q_1(u_1,v_1)Q_2(u_2,v_2)$ and
   sesquilinear extension: the Hermitian symmetry of the product is inherited
   ($\overline{Q_1(v_1,u_1)Q_2(v_2,u_2)} = Q_1(u_1,v_1)Q_2(u_2,v_2)$), and the
   sesquilinear extension to $V_1\otimes V_2$ is well defined (bilinearity of the tensor in each
   factor; the sesquilinearity is in the *second* entry of each $Q_i$
   simultaneously, with no conflict). No hidden subtlety between the real symmetric case and
   the complex Hermitian one: the signature formula is the same.
3. **The product basis is $(Q_1\otimes Q_2)$-orthogonal with values
   $\varepsilon^{(1)}_a\varepsilon^{(2)}_b$.** Immediate from the product formula.
4. **Counting.** The value is $-1$ iff exactly one factor is negative:
   $p_1q_2+q_1p_2$ negative directions, $p_1p_2+q_1q_2$ positive. Total
   $(p_1+q_1)(p_2+q_2)=\dim$, correct.
5. **Non-degeneracy of the product.** Orthogonal basis without isotropic vectors ⟹ Gram
   matrix diagonal with entries $\pm1$ ⟹ invertible. Correct. **The non-degeneracy
   hypothesis on the factors is stated** in Prop. 3.1 of Doc 106
   ("nondegenerate Hermitian forms") — without it the argument fails (a direction
   in the radical of $Q_1$ tensored with anything lands in the radical of the product,
   and "neg.ind" is no longer given by Sylvester's count). P42 Thm 4.2 says
   "quadratic forms of signature $(p_i,q_i)$" without the word "non-degenerate";
   it is implicit in that the signature exhausts the dimension, but it is worth
   making explicit (minor wording correction, not of content).

### 1.2 Independent checks

- **Minimal example:** $(1,1)\otimes(1,1)$: dimension 4, formula
  $1\cdot1+1\cdot1=2$ ⟹ signature $(2,2)$. By hand: hyperbolic plane ⊗ hyperbolic
  plane = two hyperbolic planes. ✓
- **Negative-definite case:** $\langle-1\rangle\otimes\langle-1\rangle$: the formula gives
  $0\cdot1+1\cdot0=0$ and indeed $(-1)(-1)=+1$: the product is positive definite. The
  *formula* (A) handles even this case correctly. (What fails here is
  superadditivity; see §3.)
- **Consistency with the Witt ring** (literature sanity check): the signature
  $\mathrm{sig}=p-q$ is multiplicative under ⊗ — a classical fact, Lam, *Introduction to
  Quadratic Forms over Fields* (AMS GSM 67, 2005), Chap. II (signature homomorphism
  of the Witt ring). Verification:
  $p'-q'=(p_1p_2+q_1q_2)-(p_1q_2+q_1p_2)=(p_1-q_1)(p_2-q_2)$. ✓ Formula (A) is
  exactly the unique one compatible with multiplicativity of $p-q$ and of $p+q$ (dimension).

**Conclusion (A): INTACT.** No crack found. The formula is correct, the proof is
correct, and it repackages classical literature (which Doc 106 itself does not hide).

---

## 2. Statement (B): $\kappa(\psi^{\otimes k})=(4m)^k/2$ for $\mathrm{sig}(\psi)=(2m,2m)$

### 2.1 The recursion and the closed form

Signature recursion under ⊗ (a direct consequence of (A)):
$p'=p_1p_2+q_1q_2$, $q'=p_1q_2+q_1p_2$. With $p_1=q_1=p_k$, $p_2=q_2=2m$ and induction
on the hypothesis $p_k=q_k=(4m)^k/2$:
$$p_{k+1}=q_{k+1}=\tfrac{(4m)^k}{2}\cdot 2m+\tfrac{(4m)^k}{2}\cdot 2m
=2m\,(4m)^k=\tfrac{(4m)^{k+1}}{2}.$$
Base $k=1$: $(2m,2m)$, and $(4m)^1/2=2m$. ✓ Alternatively, via the closed form of
Prop. 3.3 of Doc 106: $\mathrm{neg.ind}(Q^{\otimes k})=\frac{(p+q)^k-(p-q)^k}{2}$, which
with $p=q=2m$ gives $\frac{(4m)^k-0^k}{2}=(4m)^k/2$ for $k\geq1$. (The term $0^k$ is $0$
for $k\geq1$; the formula does not apply to $k=0$ and the doc restricts it to $k\geq1$. ✓)

Prop. 3.3 was checked in general with an asymmetric case by hand: $(p,q)=(1,2)$, $k=2$:
negative directions = pairs with exactly one negative factor = $2\cdot(1\cdot2)=4$;
formula: $\frac{3^2-(-1)^2}{2}=4$. ✓ The binomial identity of the proof is standard. ✓

- **Integrality:** $(4m)^k/2$ is an integer for $k\geq1$ ($4m$ even); for $m=0$ it gives $0$. ✓
- **Structural coherence:** $\mathrm{sig}(\psi)=0$ (neutral) ⟹ by Witt multiplicativity
  all powers are neutral ⟹ $p_k=q_k=\dim/2=(4m)^k/2$. The formula is
  *forced* by the structure: half the space negative at every power. ✓
- **Case $m=0$:** $\mathcal{K}_{\mathrm{off}}=0$, all powers trivial,
  $\kappa=0$: the final clause of P42's Thm 4.3 is correct. ✓

### 2.2 The input $(2m,2m)$: where the real conditionality lies

Prop. 3.5 is unconditional algebra **given** that
$\mathrm{sig}(Q|_{\mathcal{K}_{\mathrm{off}}})=(2m,2m)$ and that the restriction is
nondegenerate. Audit of the input (Doc 98, Prop. 6.1):

1. **Non-degeneracy.** Proved in Doc 98 Prop. 6.1(c): if some pairing
   $q_i=Q(v_{z_i},v_{\bar z_i})$ were $0$, the $Q$-orthogonal decomposition of Doc 96
   Thm. 8.1 would be degenerate. The argument is correct *within the framework* (it depends on
   the global non-degeneracy of Thm. 8.1, which in turn depends on V.1).
2. **Collisions and multiplicities.** What happens with special configurations
   ($\gamma_i=\gamma_j$, multiple zeros, Jordan blocks for $\delta>0$)? Here the
   structure is **robust**, and it is worth writing down since none of the
   documents states it with the exact reference: for a nondegenerate Hermitian form
   $Q$ and a $Q$-symmetric operator, the root subspaces of **non-real** eigenvalues
   (in the parameter $z$; equivalently $\rho\notin\frac12+i\mathbb{R}$ after the
   pairing $z\leftrightarrow\bar z$) pair up as $\lambda,\bar\lambda$ with
   $Q$ restricted to the pair nondegenerate and **neutral** — the sign
   characteristic only attaches to real eigenvalues [GLR83, Chap. I, canonical
   form of Hermitian pairs]. Hence the signature $(d,d)$ of the off-block (with
   $2d=\dim$) survives quadruple collisions and non-semisimplicity, as long as the
   eigenvalues stay off the axis. The only degeneration is $\delta\to0$ (collision
   *on* the critical axis), which is exactly the change of $m$ — and GAP G4 of
   Doc 98 declares it. No new crack.
3. **Is Hypothesis D declared?** In **Doc 106, yes**, exemplarily: §2 says
   "Under Hypothesis D with $m$ orbits… (P35, bridge conjecture, **assumed as framework**)".
   In **P42 the caution is lost**: §2.4 (Framework) says "the bridge theorem
   \cite{P35} *identifies*…" — P35 is a *bridge conjecture* with an open
   verification program V.1–V.4, not a theorem. And Thm 4.3 opens with "With $m\geq1$
   off-critical quadruples, $\psi$ *has* signature $(2m,2m)$" and the following text
   calls it "unconditional". What is unconditional is the *algebraic implication*
   (signature $(2m,2m)$ ⟹ $\kappa$ of the powers); the *attribution* of that signature
   to the program's object $(\mathcal{K}_{\mathrm{off}},Q)$ inherits V.1 (via Doc 96
   Thm. 8.1 and Doc 98 Prop. 6.1, whose own frankness table says "V.1 of P35
   implicit"). **Correction required in P42**: either declare V.1/the framework in the statement
   of Thm 4.3, or rephrase it as conditional ("If $\psi$ has signature $(2m,2m)$ —
   as it does under the framework of §2.4 — then…").

**Conclusion (B): INTACT as algebra; conditionality of the input under-declared in
P42** (not in Doc 106, which is frank).

---

## 3. Statement (C): superadditivity — here there is blood

### 3.1 The defect identity is correct

$$\mathrm{neg.ind}(Q_1\otimes Q_2)-(q_1+q_2)=p_1q_2+q_1p_2-q_1-q_2
=(p_1-1)q_2+(p_2-1)q_1.$$
Exact algebraic identity, verified. From this, **P42's Theorem 4.2** ("strictly
superadditive *whenever* $(p_1-1)q_2+(p_2-1)q_1>0$") is **literally correct**: the
strict inequality holds exactly when that quantity is positive, because it *is* that
quantity.

### 3.2 Corollary 3.2 of Doc 106 is FALSE as written

Cor. 3.2 claims, with no hypothesis beyond those of Prop. 3.1 (non-degeneracy):
$$(p_1-1)q_2+(p_2-1)q_1\;\geq\;0.$$
**Counterexample:** $Q_1=Q_2=\langle-1\rangle$, i.e. $(p_i,q_i)=(0,1)$. Then
$\mathrm{neg.ind}(Q_1\otimes Q_2)=0$ but $q_1+q_2=2$: the defect is
$(0-1)\cdot1+(0-1)\cdot1=-2<0$. The negative index is **not** superadditive in general:
negative ⊗ negative = positive. The strictness "i.e." clause also fails without
the hypothesis: with $(p_1,q_1)=(2,5)$, $(p_2,q_2)=(0,1)$, "$p_1\geq2$ and
$q_2\geq1$" holds but the defect is $(2-1)\cdot1+(0-1)\cdot5=-4<0$ (subadditive).

**Correction:** add the hypothesis $p_1,p_2\geq1$. With it both terms
$(p_i-1)q_j$ are $\geq0$, superadditivity holds, and strictness is equivalent to
"($p_1\geq2$ and $q_2\geq1$) or ($p_2\geq2$ and $q_1\geq1$)". In the program's use case
($p_1=p_2=2m\geq2$ for $m\geq1$, or $p=\infty$ in the full space) the hypothesis
holds with room to spare: **the damage does not propagate to any application**, but the
corollary as published, as a quotable piece, is mis-stated.

### 3.3 P43, ledger L3: overstated

L3 says: "for indefinite quadratic forms of signatures $(p_i,q_i)$,
$\mathrm{neg.ind}(Q_1\otimes Q_2)=p_1q_2+q_1p_2$, **strictly superadditive**". Two
problems: (i) even restricting to *indefinite* forms ($p_i,q_i\geq1$),
superadditivity **is not always strict**: $(1,1)\otimes(1,1)$ gives
$\mathrm{neg.ind}=2=q_1+q_2$, exact additivity; (ii) if "indefinite" is not assumed
(the identity holds in general), the counterexample of §3.2 applies. **Minimal
correction in P43:** "strictly superadditive whenever $(p_1-1)q_2+(p_2-1)q_1>0$" (the
wording of P42 Thm 4.2, which is the correct one).

### 3.4 $\kappa(\psi^{\otimes k})\geq k\,\kappa(\psi)$

For the stated case ($\mathrm{sig}=(2m,2m)$, $m\geq1$):
$(4m)^k/2\geq 2mk\iff(4m)^{k-1}\geq k$, true for all $k\geq1$ by induction
($4^k\geq 4k\geq k+1$), with equality only at $k=1$. The clause "with equality only at
$k=1$" of P42's Thm 4.3 is correct for $m\geq1$. ✓ Adversarial note:
$k$-superadditivity is **false in general** (with $(p,q)=(0,1)$:
$\kappa(\psi^{\otimes k})$ alternates $1,0,1,0,\dots<k$), but neither P42 nor Doc 106
claims it outside the $(2m,2m)$ case — in fact Prop. 3.6 (sterility) *uses*
that pathological case correctly. No crack.

---

## 4. The use in P42 §5 / P43 / P44 (scoped, without re-auditing Doc 107)

- **P42 Thm 5.4 (`thm:signature`)** claims signature "exactly $(8,8)$ … with no
  degeneration" for the double block. Doc 107 (Thm. 5.5 + **Obs. 5.7**) proves this
  with three declared caveats that P42 omits: (i) the statement is about the form $B$ of
  the off×off block in the evaluation quotient, and the doubled localization is inherited
  "modulo V.1-doubled" (same status as G4/G5 of Doc 98); (ii) weights 1 for
  simple zeros (with multiplicities the signature does not change — that is
  covered); (iii) the pairing convention $z\leftrightarrow-\bar z$. Also, the
  surjectivity of the evaluation map (Lemma 5.4 of Doc 107), which guarantees that
  the weight $\hat\varphi$ does not degenerate the realization, requires non-vanishing
  conditions of $\hat\varphi$ at the 16 difference points — a genericity
  condition on $\varphi$ that P42 does not state. **Recommendation:** a sentence in
  Thm 5.4 like "for $\varphi$ with $\hat\varphi$ nonvanishing at the relevant
  difference points; inherited-framework caveats as in [Doc 107, Obs. 5.7]".
- **P43 L3:** correction of §3.3. The rest of the item ($\kappa(\psi^{\otimes k})
  =\frac12(4m)^k$ on $\mathcal{K}_{\mathrm{off}}$) is faithful to what is proved, modulo the same
  observation about the conditionality of the input as in P42. P43's Thm B (around line 160)
  says "amplifies exponentially **and unconditionally**" — same correction: the
  amplification is unconditional *given* the signature; the signature belongs to the framework.
- **P44:** does not cite the tensor identity directly (only mentions the amplification
  in passing, lines 228–233, as a "transplanted" mechanism); nothing to correct there.

---

## 5. Summary of required corrections

| # | Location | Defect | Correction |
|---|---|---|---|
| 1 | Doc 106, Cor. 3.2 | "$\geq0$" false without $p_1,p_2\geq1$ ($\langle-1\rangle\otimes\langle-1\rangle$) | add hypothesis $p_1,p_2\geq1$; rewrite the "i.e." clause |
| 2 | P43, L3 | "strictly superadditive" without qualifier (false for $(1,1)\otimes(1,1)$ and for negative-definite forms) | add "whenever $(p_1-1)q_2+(p_2-1)q_1>0$" |
| 3 | P42, §2.4 + Thm 4.3 | "the bridge theorem" (P35 is a conjecture, V.1–V.4 open); "unconditional" without separating algebraic implication from input | declare the framework/V.1 in the statement or make it conditional |
| 4 | P42, Thm 4.2 | "quadratic forms" without "non-degenerate" (and they are Hermitian) | one word |
| 5 | P42, Thm 5.4 | omits caveats of Doc 107 Obs. 5.7 and the genericity of $\hat\varphi$ | one referring sentence |

No defect touches the mathematical content in the use case $(2m,2m)$, $m\geq1$:
Prop. 3.5 and its chain of consequences are correct, classical algebra
(Lam, *Introduction to Quadratic Forms over Fields*, GSM 67, Chap. II;
Bognár, *Indefinite Inner Product Spaces*, Chap. I; [GLR83], Chap. I).

**VERDICT: SURVIVES WITH CORRECTIONS** — (A) and (B) intact as algebra; (C) and the
citations require the fixes in the table; the conditionality of the input $(2m,2m)$ must
be declared where P42/P43 omit it.
