# Document 181 — GAP 175.A: the minimal instance of LP-112 is the dichotomy in disguise

**Program:** Riemann Hypothesis — Phase 56 (two towers)
**Mandate:** attack GAP 175.A (the minimal instance of LP-112): prove it, prove the weaker version that still feeds the energy dichotomy, or identify the exact obstruction. Three routes: Bagchi-without-RH, Hurwitz/without-Euler (Davenport–Heilbronn test), quantitative (witness measure).
**Prerequisites read at source:** Doc 175 in full (Lemma 175.1, Thm 175.2, Obs 175.3, Cor 175.4–175.5, Thm 175.6, Prop 175.7–175.8, GAP 175.A/175.B, §4 frank status of LP-112), Doc 112 via its citations in D175.
**Contract:** [THEOREM]/[PROP]/[LEMMA] only with complete proof; [GAP]/[literature GAP] declared with statement form; no numerics; total honesty — a false victory is worse than a failure. Backward-only: Voronin 1975, Bagchi 1981/1987, Reich 1980, Steuding 2007, Garunkštis–Karikovas 2014, Selberg 1946, Docs 112/170/175.

**Coordinates (identical to D170/D175).** Off zero $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, one representative per quadruple; $I=I(0^+)=\sum_j b_j^2$; $I=0\iff$ RH. For an off zero $\rho_0$: canonical constants $r=r(\rho_0)\le b_0/2$, $D_0=\bar D(\rho_0,r)$, $\eta=\min_{\partial D_0}|\zeta|>0$ (D175 §2.2). **LP-112**: for every closed disk $D\subset\{\tfrac12<\sigma<1\}$ there exists $\tau_k\to\infty$ with $\sup_D|\zeta(s+i\tau_k)-\zeta(s)|\to0$. **LP-112[$\rho_0$]**: there exists an unbounded sequence with $\sup_{D_0}|\zeta(\cdot+i\tau_k)-\zeta|\le\varepsilon$ for ONE fixed $\varepsilon<\eta$. **Dic** := $I(0^+)\in\{0,\infty\}$ (the energy dichotomy).

---

## 0. Executive summary and verdict

**GAP 175.A is NOT proved — it DISSOLVES.** The central finding, which Doc 175 already contained without extracting it:

1. **[THEOREM 181.1] $0<I<\infty\;\Longrightarrow\;\neg$LP-112** (in fact $\neg$LP-112[$\rho_0$] for EVERY off zero). This is the clean closure of Route 3: Prop 175.8 gives finiteness of witnesses at *fixed radius* $r$ and *fixed precision* $\varepsilon<\eta$, and LP-112 (which asks for convergence, which is stronger) implies infinitely many witnesses at that fixed quality. The proof is three lines but the consequence is structural.
2. **Hence LP-112 ⟹ Dic (Thm 175.2) is NOT an implication between an axiom and a conclusion: it is half an equivalence.** What is proved stands as: $\mathrm{LP\text{-}112}\Rightarrow\mathrm{Dic}$ and $\;\mathrm{Dic}\Rightarrow\mathrm{LP\text{-}112}$ *except in the case $I=\infty$* ([THEOREM 181.2]: the converse in the case $I=0$ is Bagchi). The exact residue is **[GAP 181.A]**: does $I=\infty\Rightarrow$ LP-112? Modulo that gap, **LP-112 ⟺ Dic: LP-112 is ANOTHER NAME for the dichotomy, not an independent input.**
3. **Brutal corollary for the tower:** conditional on A ($I<\infty$), **LP-112 ⟺ RH** ([COR 181.3]). The "second arrow" is not a shortcut: any proof of LP-112 must, in the world $0<I<\infty$, be false — hence **LP-112 is unprovable without first excluding the intermediate state**, which is exactly what the tower wanted to use LP-112 for. GAP 175.A ("prove the minimal instance") was asking to prove a statement that is FALSE in the only world where the tower needs it with content. The tower is reconfigured: $\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}$, and Dic must be attacked directly (coercivity D174, Green–Littlewood D173/176), not via recurrence.
4. The mandate's apparent paradox is resolved (§1), the D–H test is consistent with the equivalence (§3, with [literature GAP 181.C]), and the genuine minimal residual statement is GAP 181.A — interesting only as a *reformulation certificate*, not as a route to RH.

---

## 1. Route 3 first (it decides everything): the finiteness of Prop 175.8 at fixed quality

Re-read at source, the proof of Prop 175.8 (D175 §5) operates as follows: for fixed $\rho_0$ with canonical constants $(r,\eta)$ and ANY fixed $\varepsilon<\eta$, the replica map (Rouché, Lemma 175.1(i) with $\delta=R=r$) injects the $2r$-separated witnesses of $A_\varepsilon$ into quadruples with $b\ge b_0/2$, of which there are $\le 4I/b_0^2<\infty$ by Chebyshev over the full series; $A_\varepsilon$ is then contained in $\le 4I/b_0^2$ intervals of length $\le 2r$, hence bounded. **Confirmed: finiteness holds for FIXED $r$ (the canonical one) and fixed $\varepsilon$ — it requires neither $\varepsilon\to0$ nor $r\to0$.** This answers the mandate's question: in the state $0<I<\infty$, every unbounded sequence of witnesses is excluded *already at a single fixed quality* $(r,\varepsilon)$ with $\varepsilon<\eta$; a fortiori every uniformly convergent sequence (which demands eventual quality $<\varepsilon$ for every $\varepsilon$, in particular for one fixed $<\eta$).

**[THEOREM 181.1] (anti-recurrence decides the minimal instance).** *If $0<I(0^+)<\infty$, then LP-112[$\rho_0$] is false for every off zero $\rho_0$, and a fortiori LP-112 is false.*

*Proof.* Let $\rho_0$ be an off zero (it exists: $I>0$), with canonical $(r,\eta)$. LP-112[$\rho_0$] asserts an unbounded sequence $\{\tau_k\}\subset A_\varepsilon$ for some $\varepsilon<\eta$. By Prop 175.8 (unconditional, valid under $0<I<\infty$), $A_\varepsilon\subset\bigcup_{z\in\mathcal Z}T_z$ with $\#\mathcal Z\le 4I/b_0^2<\infty$ and each $T_z$ a bounded interval (contained in $(\gamma_z-\gamma_0-r,\gamma_z-\gamma_0+r)$); a subset of a finite union of bounded intervals is bounded: it admits no unbounded sequence. Contradiction. For full LP-112: applied to disk $D_0$ it produces $\tau_k\to\infty$ with $\sup_{D_0}|\zeta(\cdot+i\tau_k)-\zeta|\to0$, in particular $<\eta/2$ for large $k$ — an unbounded sequence in $A_{\eta/2}$, impossible. $\blacksquare$

**Resolution of the mandate's apparent paradox.** "Off zeros are rare ⟹ the generic translate has no zero near $\rho_0-i\tau$ ⟹ self-approximation generically fails" — correct, and in the state $0<I<\infty$ it fails not only generically but *cofinitely* (Thm 181.1). There is no paradox with Thm 175.2: **175.2 and 175.8/181.1 are contrapositives of each other** (Obs 175.3 already half-said this). The real logic of the dichotomy is: *LP-112 is an axiom that EXCLUDES the intermediate state because in the intermediate state it is false.* There is no positive replication mechanism that LP-112 "activates"; there is a logical incompatibility between unbounded recurrence and a finite energy budget.

**Anti-circularity test.** Thm 181.1 uses no RH nor ζ-input beyond: isolated zeros, Hadamard–dVP ($b<\tfrac12$), Rouché, and the definition of $I$. The Prop 175.8 it invokes is unconditional (Chebyshev + Rouché). No circularity: the theorem holds in every world, and in each world it says something different about LP-112 (false in $0<I<\infty$; true in $I=0$ by Bagchi; open in $I=\infty$). What would be circular is what GAP 175.A asked for: "prove LP-112[$\rho_0$]" unconditionally — that is EQUIVALENT to proving the world is not $0<I<\infty$ (more precisely: it implies that if an off zero exists, $I=\infty$), which is the dichotomy itself. The requested input was the conclusion.

---

## 2. Route 1: the equivalence and its exact residue

We gather the pieces into the three-state statement.

**[THEOREM 181.2] (status of LP-112 by energy state).**
1. $I=0$ (RH): **LP-112 is true** — Bagchi: under RH, $\zeta|_D$ is non-vanishing for every disk $D$ of the strip, lies in the support of its limiting measure, and strong recurrence gives positive lower density of witnesses for every $\varepsilon$ [Bag81, Bag87; Ste07 §8.3]; in particular unbounded sequences.
2. $0<I<\infty$: **LP-112 is false** (Thm 181.1).
3. $I=\infty$: **open** ([GAP 181.A]).

*Proof.* (1) citation verified against D175 §4 (which verified it at source); (2) Thm 181.1; (3) is a gap declaration. $\blacksquare$

**[COR 181.3] (LP-112 is not an independent input).**
1. $\mathrm{LP\text{-}112}\;\Longrightarrow\;\mathrm{Dic}$, and $\;\mathrm{Dic}\Rightarrow\mathrm{LP\text{-}112}$ in the case $I=0$; hence **LP-112 ⟺ Dic modulo GAP 181.A**, and *unconditionally* $\;\neg(0<I<\infty)\;\Longleftarrow\;\mathrm{LP\text{-}112}\;$ with the converse broken only at $I=\infty$.
2. **Conditional on A ($I<\infty$): LP-112 ⟺ RH.** (⟸: Bagchi. ⟹: with $I<\infty$, case (2) of Thm 181.2 is excluded by the truth of LP-112, hence $I=0$.)
3. Hence the tower $\mathrm{RH}\Longleftarrow A\wedge\mathrm{LP\text{-}112}$ is, *as a proof target*, identical to $\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}$: any proof of LP-112 contains a proof of "the state $0<I<\infty$ does not exist" (if it existed, what was proved would be false). **LP-112 is not a shortcut: it is the dichotomy under the name of recurrence.**

*Proof.* (1) forward = Thm 175.2; converse-case-$I=0$ = Thm 181.2(1); the identification "LP-112 ⟹ ¬(0<I<∞)" is Thm 181.1 contraposed. (2) and (3) are direct readings. $\blacksquare$

**Honesty about what changes and what does not.** Thm 175.2 remains correct as it stands; what dies is its *strategic reading* ("only LP-112 is missing, a universality lemma plausibly attackable by ergodic theory"). The Bagchi-without-RH route of the mandate is closed *negatively* without needing to enter the torus $\Omega=\prod_p\mathbb T$: there is no need to examine whether Kronecker–Weyl equidistribution produces an exceptional sequence, because we know *a priori* that in the state $0<I<\infty$ it does NOT produce one (it does not exist), and in the other two states LP-112 is either already a theorem or GAP 181.A. The wall of P43 §3.1 ("produce an element of an exceptional set") was the wrong diagnosis for this gap: the set is not exceptional but *finite* — there is nothing to produce. The better error (the real wall) lies in GAP 181.A or, equivalently, in Dic directly.

**Is GAP 181.A plausible ($I=\infty\Rightarrow$ LP-112, or even LP-112[$\rho_0$] for some $\rho_0$)?** In favor: $I=\infty$ gives an infinite budget of replicas — bounds 175.6/175.8 obstruct nothing; with $E(T)\to\infty$ there are infinitely many quadruples with $b\ge b_0/2$ available at unbounded heights. Against (the exact obstruction): Rouché only gives the direction witnesses⟹zeros; the direction zeros⟹witnesses requires the translate to approximate *the entire function* on $D_0$, not merely to have a well-placed zero — it is the universality-outside-Bagchi's-support problem (Euler compresses the support to non-vanishing functions; D175 §4.3), now in the world $I=\infty$, where the limiting measure still has zero-free support (limit theorems hold unconditionally in $\sigma>\tfrac12$ on average, [Lau96]) while the actual function has infinitely many off zeros. Nothing in the distributional machinery sees those zeros. **No visible route; nor refutation: a world $I=\infty$ could be so pathological that self-approximation holds by brute abundance, or could fail equally.** We leave it as a genuine gap with the two outcomes labeled below (Scenarios S1/S2).

---

## 3. Route 2: the without-Euler test (Hurwitz and Davenport–Heilbronn)

**Hurwitz.** For $\zeta(s,\alpha)$ with $\alpha$ transcendental (and rational cases $\ne\tfrac12,1$), self-approximation is a theorem *even in disks with zeros* — [GK14] (Garunkštis–Karikovas, *Self-approximation of Hurwitz zeta-functions*, Funct. Approx. Comment. Math. 51, 2014; verified only against the citation already audited in D175 §4.3 — the exact attribution of the rational case is left to D175's citation, not re-audited here). Mechanism: without an Euler product, the limiting measure has full support in $H(D)$ (strong Bagchi universality): the target *with zeros* is generic for its own flow. Consistency with equivalence 181.3: $\zeta(s,\alpha)$ has infinitely many zeros in $\tfrac12<\sigma<1$ with abscissas that do NOT accumulate at $\tfrac12$ (there are strips $\sigma\in(\tfrac12+\delta,1-\delta)$ with $\gg T$ zeros — classical for Hurwitz, via the same strong universality), hence its analogue of $I$ is trivially $\sum b_j^2=\infty$. **Hurwitz lives in the case $I=\infty$ and DOES have an LP-112-analogue: the only external data available is consistent with "$I=\infty\Rightarrow$ self-approximation" (S1).** But the mechanism (full support) does NOT transfer to ζ: it is exactly what Euler destroys. The test calibrates, it does not prove.

**Davenport–Heilbronn.** $f_{DH}$ (combination of two $L(s,\chi)$ mod 5 with a functional equation, without Euler) has infinitely many off zeros with $b$ bounded below — "fat zeros", Doc 146/150 —, in fact $\gg T$ zeros in strips $\sigma>\tfrac12+\delta$; hence $I_{DH}=\infty$. ✓ Consistent with the dichotomy (if $f_{DH}$ satisfies an LP-112-analogue, its $I$ must be $\infty$ — it is). Does it satisfy sequential self-approximation? The expected mechanism: JOINT universality of $L(s,\chi_1),L(s,\chi_2)$ [Vor75; Ste07 ch. 10] gives strong universality (full support, targets with zeros allowed) for the linear combination — it is the standard mechanism used to explain its off zeros —, and full support + $f_{DH}$ itself in the support would give strong recurrence, hence an LP-112-analogue. **[Literature GAP 181.C]:** I cannot verify at source here a published statement "self-approximation of $f_{DH}$ in disks containing its off zeros" (the strong universality theorems for linear combinations — the Kaczorowski–Kulas line and successors — I know only from memory; the step "the target $f_{DH}$ itself is in the joint support" requires a non-degeneracy check). I record it as pending verification, with a falsifiable prediction: **if equivalence 181.3 + S1 is correct, $f_{DH}$ MUST have sequential self-approximation in its off disks.** A refutation of this would refute S1 (not the equivalence: $f_{DH}$ is not ζ).

**Intermediate object (partial Euler $\zeta_S\cdot$remainder).** Not developed: any partial Euler product still compresses the support of the $\zeta_S$ factor but the remainder decompresses it; the object inherits cleanly neither full support nor compression. No lever is visible; not pursued.

---

## 4. Verdict

**GAP 175.A is CLOSED NEGATIVELY: the requested statement is unprovable-without-proving-the-dichotomy because it is false in the state $0<I<\infty$** (Thm 181.1). It was not "the minimal instance of a universality lemma": it was the dichotomy in disguise. Results:

1. **[THEOREM 181.1]** (unconditional): $0<I<\infty\Rightarrow\neg$LP-112[$\rho_0$] $\forall\rho_0$ $\Rightarrow\neg$LP-112. (Extraction from Prop 175.8; the finiteness at fixed quality $(r,\varepsilon<\eta)$ verified in the source proof.)
2. **[THEOREM 181.2]** LP-112 by states: true at $I=0$ (Bagchi), false at $0<I<\infty$, open at $I=\infty$.
3. **[COR 181.3]** LP-112 ⟺ Dic modulo GAP 181.A; conditional on A, **LP-112 ⟺ RH**. The energy tower is reconfigured: $\boxed{\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}}$ with Dic = $I\in\{0,\infty\}$ as a direct target; LP-112 stops being a shortcut and becomes a *candidate reformulation* of Dic.

**Numbered GAPs:**
- **[GAP 181.A]** (the equivalence's exact residue): *$I=\infty\Rightarrow$ LP-112* (it suffices: there exists an off zero $\rho_0$ with LP-112[$\rho_0$]). Value: would certify LP-112 ⟺ Dic exactly. Scenarios: **S1** (true — supported by Hurwitz and presumably D–H): LP-112 = another name for Dic. **S2** (false): LP-112 ⟺ RH plainly (sequential LP-112 would then be equivalent to RH, closing the open question of D112 §4 — also valuable!). In both scenarios LP-112 is NOT an independent input. Obstruction identified: universality outside Bagchi's support; abundance of zeros ($I=\infty$) gives the replicas but not the approximation of the whole function.
- **[Literature GAP 181.C]**: self-approximation of Davenport–Heilbronn in disks with off zeros (strong universality of linear combinations + $f_{DH}$ in the support). Falsifiable test of S1.
- GAP 175.B (automaticity of density) is *downgraded*: in the state $0<I<\infty$ there is no sequence to densify (181.1 makes it vacuous there); it only retains content at $I=\infty$.

**Successor direction.** All the weight returns to **direct Dic**: excluding $0<I<\infty$ without recurrence. The program's assets for this are those from the other face of Phase 55: coercivity $\dot I\le-2I$ (D174), the Cesàro limit $\pi I-\pi/8$ (D176.4), and the dynamical tower (177.B∧LP-134 ⟹ $m<\infty$ — note that $m<\infty\Rightarrow I<\infty$, so the dynamical tower pushes toward the state where 181.1 makes LP-112 false: the two towers now *cooperate* against the intermediate state instead of sharing the axiom). Suggested successor document: 182 — is D174's coercivity ($\dot I\le-2I$, D167 balance law) compatible with a steady state $0<I<\infty$, or does the flow itself exclude the intermediate state? That is now the dichotomy question in its natural habitat.
