# Document 184 — Adversarial audit of D175 (energy dichotomy) and D181 (GAP 175.A / minimal LP-112)

**Program:** Riemann Hypothesis — Phase 58 (total audit)
**Mandate:** audit-to-destruction of the chain that holds up the energy tower: [Lemma 175.1] → [Thm 175.2 / Obs 175.3 / Cor 175.4–175.5] → [Thm 175.6] → [Prop 175.7–175.8] → [Thm 181.1 / Thm 181.2 / Cor 181.3]. Director's question: **did LP-112 truly die as an independent input, or does it revive?**
**Sources read in full, line by line:** D175 (`phase-55-two-arrows/175-energy-dichotomy-lp-112-i-0.md`), D181 (`phase-56-two-towers/181-gap-175-a-the-minimal-instance.md`). Load-bearing citations verified at source: D112 §2.2 (LP-112 and LP-112⁻ statements, Theorem 2.3, lines 219–256 of the source file) — match D175 §1's reproduction word for word; Thm 170.5 ($E(T)\ll T/\log T$) accepted as certified by the Phase 54 audit (not re-audited here).
**Stance:** adversarial. Every step was attacked with intent to break it. Where I say CERTIFIED, the proof was verified term by term, constants included.

---

## 0. Executive verdict

**The chain HOLDS.** After systematic attack on the mandate's nine points (Rouché replica, direction of the translate, witness separation, quadruple conventions, factors of 2/4, bounding of the intervals $T_z$, 175↔181 definition mismatch, vacuity of Bagchi at $I=0$, circularity 175.2↔175.8↔181.1), **no fatal or degrading error was found**. Two harmless erratas were found (E-184.1, E-184.2) and one structural classification observation that D181 itself already half-states: **Thm 181.1 is mathematically redundant (exact contrapositive of Thm 175.2 in its strong form Obs 175.3), but its strategic reading is correct and decisive**. Answer to the director: **LP-112 truly died as a shortcut; it does not revive.** The tower $\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}$ is the correct formulation.

---

## 1. [LEMMA 175.1] (Rouché–Hurwitz with rate) — **CERTIFIED**

Term-by-term verification.

**(i).** Hypotheses: $g$ holomorphic in a neighborhood of $\bar D(z_0,R)$, unique zero $z_0$ of multiplicity $m_0$, $\eta(\delta)=\min_{|z-z_0|=\delta}|g|>0$ (positive because $g$ does not vanish on $\bar D\setminus\{z_0\}$ and the circle $|z-z_0|=\delta\le R$ does not pass through $z_0$). If $\sup_{\bar D}|f-g|<\eta(\delta)$, then on the circle $|z-z_0|=\delta$, $|f-g|<\eta(\delta)\le|g|$ holds: classical Rouché ([T39 §3.42]) gives that $f$ has in $D(z_0,\delta)$ as many zeros with multiplicity as $g$, i.e. $m_0$. ✓ No gaps.

**(ii).** $g=c(z-z_0)^{m_0}h$, $h(z_0)=1$, $|h|\ge\tfrac12$ on $\bar D(z_0,\delta_1)$ by continuity. On $|z-z_0|=\delta\le\delta_1$: $|g|\ge\tfrac{|c|}2\delta^{m_0}$, hence $\eta(\delta)\ge\tfrac{|c|}2\delta^{m_0}$. With $\delta(\varepsilon)=(4\varepsilon/|c|)^{1/m_0}$: the condition $\varepsilon\le\tfrac{|c|}4\delta_1^{m_0}$ guarantees $\delta(\varepsilon)\le\delta_1$, and $\eta(\delta(\varepsilon))\ge\tfrac{|c|}2\cdot\tfrac{4\varepsilon}{|c|}=2\varepsilon>\varepsilon\ge\sup|f-g|$. The application of (i) is legitimate. Arithmetic verified: the factor $4$ in $\delta(\varepsilon)$ is exactly what is needed for the margin to be $2\varepsilon$, not $\varepsilon$ (strict). ✓

Attack attempted: could $\delta_1$ fail to exist if $h$ oscillates? No: $h$ is holomorphic (removable extension) with $h(z_0)=1$; continuity suffices. What if $f$ has zeros in the annulus $\delta(\varepsilon)<|z-z_0|\le R$? Irrelevant: the lemma only asserts the count INSIDE $D(z_0,\delta)$. There is no overstatement.

---

## 2. [THEOREM 175.2] + [Obs 175.3] (energy dichotomy) — **CERTIFIED**

**Constants of the zero (§2.2).** $r=\tfrac12\min(b_0,\ \tfrac12-b_0,\ \mathrm{dist}(\rho_0,Z(\zeta)\setminus\{\rho_0\}))$. Three consequences verified:
1. $r\le b_0/2$ ⟹ $D_0\subset\{\sigma>\tfrac12+\tfrac{b_0}2\}$: **the whole disk is strictly to the right of the line** — this answers mandate attack point 1(b): no replicated zero inside $D(\rho_0+i\tau,r)$ can be on-line; the zero is off by construction of the radius, not by a later argument. ✓
2. $r\le\tfrac12(\tfrac12-b_0)$ ⟹ $D_0\subset\{\sigma<1\}$, within the open strip (Hadamard–dVP gives strict $b_0<\tfrac12$, so the slack exists). ✓
3. $r\le\tfrac12\mathrm{dist}(\rho_0,Z(\zeta)\setminus\{\rho_0\})$ ⟹ $\zeta$ does not vanish in $D_0\setminus\{\rho_0\}$ — the exact hypothesis of Lemma 175.1, including uniqueness of the zero. ✓ **Positive finding not flagged in D175:** since $\bar\rho_0\in Z(\zeta)$ and $\mathrm{dist}(\rho_0,\bar\rho_0)=2\gamma_0$, the definition of $r$ automatically gives $r\le\gamma_0$; this guarantees (without extra argument) that the translated disks $D(\rho_0+i\tau,r)$ with $\tau>0$ live in $\{\mathrm{Im}>0\}$ — used tacitly in 175.6 ("only the upper-right member of the quadruple can fall in the disk"). The tacit claim is correct.

**Step 1 (direction of the replica — attack point 1(b)).** Carefully verified logical direction: $\sup_{D_0}|\zeta(\cdot+i\tau_k)-\zeta|=\varepsilon_k<\eta$ ⟹ (Lemma 175.1(i), $g=\zeta|_{D_0}$, $f=\zeta(\cdot+i\tau_k)|_{D_0}$, $\delta=R=r$) ⟹ $\zeta(\cdot+i\tau_k)$ has $m_0$ zeros in $D(\rho_0,r)$ ⟹ if $\zeta(s'+i\tau_k)=0$ with $s'\in D(\rho_0,r)$, then $s'+i\tau_k$ is a **genuine zero of $\zeta$** in $D(\rho_0+i\tau_k,r)$, at height $\in(\gamma_0+\tau_k-r,\gamma_0+\tau_k+r)$. ✓ The bound $b(\rho_k)\in(\tfrac{b_0}2,\tfrac{3b_0}2)$ follows from $|\mathrm{Re}\,\rho_k-(\tfrac12+b_0)|<r\le\tfrac{b_0}2$. ✓ The fine rate $|\rho_k-(\rho_0+i\tau_k)|\le\delta(\varepsilon_k)$ is a direct application of 175.1(ii); D175 correctly states it is a refinement, not an input (Obs 175.3). ✓

**Step 2 (separation — attack point 3).** Passing to the subsequence $\tau_{j+1}>\tau_j+2r+1$ is legitimate ($\tau_k\to\infty$). Intervals $(\gamma_0+\tau_j-r,\gamma_0+\tau_j+r)$: disjoint (center separation $>2r$). The "distinct quadruples" argument: the two upper members of a quadruple ($\rho$ and $1-\bar\rho$) share the imaginary part; imaginary parts in disjoint intervals ⟹ distinct quadruples. Attack: could $\rho_j$ be the LEFT member ($1-\bar\rho$, with $\sigma<\tfrac12$) of a quadruple whose right representative was already counted in another interval? No: $\rho_j\in D(\rho_0+i\tau_j,r)\subset\{\sigma>\tfrac12\}$, so $\rho_j$ is always the upper-right member, and the count by Im-intervals is a collision-free count of quadruples. ✓ Distinct from $\rho_0$'s quadruple: for $\tau_j>r$ (eventually), $\mathrm{Im}\,\rho_j>\gamma_0$. Apparent gap: what about $1-\bar\rho_0$ at the SAME height $\gamma_0$? Irrelevant: same quadruple as $\rho_0$, and heights $>\gamma_0$ exclude it just the same. ✓

**Step 3 (energy count — attack point 1(d)).** $I=\sum_j b_j^2$ with ONE representative per quadruple (convention fixed in the header, identical to D170). Each replica quadruple is distinct (Step 2) and its representative has $b\ge b_0/2$, contributing $\ge b_0^2/4$. **No double counting and no phantom factor of 4**: the proof uses one replica per shift and one term per quadruple; Obs 175.3 correctly states that the quadruple's symmetry is not used (it would multiply the bound by 4 — but the lower bound $\infty$ does not need it). If $I$ were summed with multiplicity, the lower bound would only grow. ✓ Divergence: series of terms $\ge b_0^2/4>0$ in infinite quantity. ✓

**Obs 175.3.** Verified against the proof: the only use of the hypothesis is $\varepsilon_k<\eta$ for $k\ge k_0$ with $\{\tau_k\}$ unbounded — exactly LP-112[$\rho_0$]. The instance really is at fixed precision and a single disk. ✓ **No definition mismatch**: LP-112[$\rho_0$] (D175 §1b) and the one used in D181 §0 are identical letter for letter (same canonical $D_0$, same $\eta$, "ONE fixed $\varepsilon<\eta$", unbounded sequence).

**Verification against D112 at source.** The LP-112 and LP-112⁻ statements of D175 §1 match D112 (lines 219–224 of the source, including the clause $\tau>\mathrm{height}(D)$). D175 §2.2's "honesty about the novelty" is exact: Theorem 2.3 of D112 already implicitly contained the replica with $b\ge b_0-r$; what is new is the reading in terms of $I$ and the rate. ✓

---

## 3. [COR 175.4] (LP-112⁻ suffices) — **CERTIFIED-WITH-ERRATA** (E-184.2, harmless)

The summable-radii induction, attacked step by step:
- $r_k\le b_0 2^{-k-2}$ ⟹ $\sum_{j\ge0} r_j\le b_0\sum 2^{-j-2}=b_0/2$ ⟹ $b^{(k+1)}\ge b^{(k)}-r_k\ge b_0-\sum_{j\le k}r_j\ge b_0/2$. The arithmetic is correct and the conceptual point (without summability the abscissa would drift geometrically) is genuine — this is the corollary's non-trivial content. ✓
- The other arms of the $\min$ guarantee $D_k\subset$ open strip and uniqueness of the zero in $D_k$ (hypothesis of 175.1). ✓
- Strict growth of heights: $\gamma^{(k+1)}>\gamma^{(k)}+\tau-r_k$ and $\tau>\mathrm{height}(D_k)=\gamma^{(k)}+r_k>r_k$ ⟹ $\gamma^{(k+1)}>\gamma^{(k)}$. ✓ Strictly increasing heights ⟹ distinct quadruples (same argument as Step 2; the replicas live in $\sigma>\tfrac12$, $\mathrm{Im}>0$ — they are representatives). ✓
- Application of LP-112⁻ with $(D_k,\eta_k/2)$: legal instance of the "for every $D$ and every $\varepsilon$" quantifier verified in D112. ✓

**E-184.2 (harmless errata).** The parenthetical "$\tau>\mathrm{height}(D_k)\ (>2r_k+1)$" is not justified in general ($\mathrm{height}(D_k)=\gamma^{(k)}+r_k$, and $\gamma^{(k)}>r_k+1$ is not argued; it holds for ζ because every zero has $\gamma>6$, but the text does not invoke this). It is decorative: the proof only needs $\tau>r_k$, which does follow. Inline correction: delete the parenthetical or replace it with "$>r_k$".

---

## 4. [COR 175.5] (architecture) — **CERTIFIED-WITH-ERRATA** (E-184.1, harmless)

(1) $I\in\{0,\infty\}\Rightarrow m\in\{0,\infty\}$: if $1\le m<\infty$, $I$ is a finite sum of terms in $(0,\tfrac14)$ ⟹ $0<I<\infty$, contradiction. ✓ The subsumption of D112's Thm 2.3 with the same hypothesis is correct. (2) The tower's logic is trivially valid given the dichotomy. ✓ $m<\infty\Rightarrow I<\infty$ trivial. ✓

**E-184.1 (harmless errata, repeated in 175.7.3).** The counterexample "$b_j=1/j$" violates the constraint $b\in(0,\tfrac12)$ at $j=1,2$ ($b_1=1$, $b_2=\tfrac12$). Inline correction: $b_j=1/(j+2)$ (or any tail). The strict cardinality-vs-moment separation illustrated by the counterexample remains correct. **Adversarial note the document omits:** it does not discuss whether a configuration $b_j\to0$ is realizable by a function with ζ's functional equation and zero density — but the corollary only needs that $I<\infty$ does not formally imply $m<\infty$ *in the class of a priori configurations*, which is how it is used (the first arrow is weakened as a STATEMENT). Legitimate use.

---

## 5. [THEOREM 175.6] (rarity with rate) — **CERTIFIED**

Mandate attack point 4: the exponent and the mechanism.

**The replica map.** For $\tau\in A_\varepsilon$ ($\varepsilon<\eta$ — note: $A_\varepsilon$ with $\le\varepsilon$, and 175.1(i) requires $<\eta(\delta)=\eta$; since $\varepsilon<\eta$ strictly, the margin exists ✓), replicated zero with $b\ge b_0/2$, $\mathrm{Im}\,\in(\gamma_0+\tau-r,\gamma_0+\tau+r)$. Quadruple identification: the disk lives in $\{\sigma>\tfrac12\}\cap\{\mathrm{Im}>0\}$ (the latter because $r\le\gamma_0$, §2 above), so only the representative can fall in it. ✓ (The text's argument via "radius $<\tfrac14$" is weaker than needed but the fact is true by the observation $r\le\gamma_0$; I do not count it as an errata because the phrase "lives in $\sigma>\tfrac12$" already excludes the left members and, with $\mathrm{Im}>0$, the lower ones.)

**The covering (attack point 2c).** $T_z=\{\tau:|\beta+i\gamma-\rho_0-i\tau|<r\}$: the condition on $\mathrm{Im}$ gives $|\gamma-\gamma_0-\tau|<r$, hence $T_z\subset(\gamma-\gamma_0-r,\gamma-\gamma_0+r)$, an interval of length $\le2r$, **bounded, with endpoints determined by the fixed height $\gamma=\gamma_z$ of the quadruple**. ✓ $A_\varepsilon\cap[0,T]\subset\bigcup_{z\in\mathcal Z(T)}T_z$: every witness replicates to a quadruple with $b\ge b_0/2$ and $\gamma\le T+\gamma_0+r$ ✓ (the slack $+\gamma_0+r$ in the truncation is exactly what is needed). $\mathrm{meas}\le 2r\#\mathcal Z(T)$ ✓.

**The two bounds on $\#\mathcal Z(T)$.**
- Selberg: $\#\mathcal Z(T)\le N(\tfrac12+\tfrac{b_0}2,T+\gamma_0+r)$ — each quadruple contributes at least its representative to the count of $N$ ✓ (in fact $N$ may count more; the inequality goes the right direction). **Origin of the $1/8$:** [S46] gives $N(\sigma,T)\ll T^{1-\frac14(\sigma-\frac12)}\log T$; with $\sigma-\tfrac12=b_0/2$ the exponent is $1-\tfrac14\cdot\tfrac{b_0}2=1-b_0/8$. ✓ The $\tfrac18=\tfrac14\times\tfrac12$ is (Selberg's constant)×(Rouché's loss in the abscissa). Verified.
- Chebyshev: $\#\mathcal Z(T)\le\sum_{\gamma_j\le T+\gamma_0+r}b_j^2/(b_0/2)^2=4E(\cdot)/b_0^2$ — Chebyshev legitimate because $E$ sums over representatives, one per quadruple, exactly the population of $\mathcal Z$. **The factor 4 is $(b_0/2)^{-2}$, not a quadruple convention** — verified, no collision of conventions. ✓
- (iii) injectivity: $|\tau_k-\tau_{k'}|>2r$ ⟹ translated disks disjoint ⟹ the replicated representatives (unique points per quadruple) are distinct. ✓

(ii) uses Thm 170.5 — certified in Phase 54, backward-only citation chain in order. Readings 1–4 of §3 are sober; GAP 175.B is well declared as a gap. ✓

---

## 6. [PROP 175.7] — **CERTIFIED-WITH-ERRATA** (the same E-184.1 at 175.7.3). Chebyshev and tails of a convergent series; no attackable content.

## 7. [PROP 175.8] (anti-recurrence) — **CERTIFIED**. The master link.

It is Thm 175.6(ii)–(iii) with $T\to\infty$, legitimate because under $I<\infty$ the global Chebyshev bound gives $\#\mathcal Z(\infty)\le 4I/b_0^2<\infty$ **over the full series** — here is the answer to the mandate's fine point 2(c): the finiteness is NOT due to bounded height of the replicas (their heights grow with $\tau$) but because the total population of quadruples with $b\ge b_0/2$ in the WHOLE half-plane is finite when $I<\infty$. Each of those $\le 4I/b_0^2$ quadruples has a fixed height $\gamma_z$ and can only serve witnesses in its interval $T_z\subset(\gamma_z-\gamma_0-r,\gamma_z-\gamma_0+r)$. A finite union of bounded intervals ⟹ $A_\varepsilon$ bounded ⟹ no unbounded sequence. ✓ Measure $\le 2r\cdot 4I/b_0^2=8rI/b_0^2$ ✓ (arithmetic verified). Separate count $\le 4I/b_0^2$ ✓.

**Attacks 2(d):** (a) Replicas that coincide for different $\tau$? Allowed and handled: the covering by $T_z$ does not require injectivity — several witnesses may share a quadruple, but then they live in the SAME interval $T_z$ of length $2r$; the measure absorbs them and the separate count excludes them by disk disjointness. ✓ (b) $2b_0>\tfrac12$ (disk leaving the strip)? Impossible by construction: $r\le\tfrac12(\tfrac12-b_0)$ keeps $D_0$ in $\sigma<1$, and the relevant strip is $\sigma>\tfrac12$, guaranteed by $r\le b_0/2$; no case of $b_0$ breaks anything (all arms of the $\min$ scale accordingly). ✓ (c) Multiplicity of $\rho_0$? $\eta>0$ does not see it; 175.1(i) handles it; the count is of quadruples, not of zeros with multiplicity — and if $I$ is defined with multiplicity, the bounds only improve. ✓ (d) A hidden $\varepsilon$ tending to 0? **No**: the whole proof is at fixed $\varepsilon<\eta$; the only threshold is $\eta$, and D175 §5 further proves it is exact (with $\varepsilon\ge\eta$ Rouché gains nothing — correct, and frank). ✓

## 8. [THEOREM 181.1] — **CERTIFIED** (with classification: redundant as mathematics, decisive as reading)

Three-line proof, verified: $0<I<\infty$ ⟹ an off zero $\rho_0$ exists; LP-112[$\rho_0$] would give an unbounded sequence in $A_\varepsilon$ (some $\varepsilon<\eta$); 175.8 (valid for EVERY $\varepsilon<\eta$, in particular that one) forbids it. For full LP-112: the instance at $D_0$ gives uniform convergence, eventually $<\eta/2<\eta$, an unbounded sequence in $A_{\eta/2}$. ✓ **No mismatch** (point 2a): same canonical disk, same constants, same witness definition as 175.8 — verified character by character between D181 §0/§1 and D175 §1b/§2.2/§5. **No hidden $\varepsilon\to0$** (point 2b): confirmed. **D181 §1's anti-circularity test:** correct — 181.1 uses only 175.8 (unconditional) and the definition of LP-112[$\rho_0$]; it does not use 175.2.

**But it must be said without any half-voice:** 181.1 is exactly the contrapositive of the strong form of Thm 175.2 (Obs 175.3: LP-112[$\rho_0$] ⟹ $I=\infty$ given $I>0$). D181 admits this ("contrapositives of each other"). The NEW mathematical content of 181.1 is nil; the STRATEGIC content (GAP 175.A asked to prove a statement that is false in the only world with content; LP-112 is not an independent input) is the correct extraction, and it had not been done before. It is not circular: it is the same coin viewed from the other side, and the program needed to view it that way.

## 9. [THEOREM 181.2] and [COR 181.3] — **CERTIFIED**

**The Bagchi test (attack point 6) — the suspicion of vacuity FAILS.** LP-112 is not conditional on existence: it quantifies over ALL closed disks of the strip (verified in D112 source, line 219), with no mention of zeros. Under RH ($I=0$) there is no disk-with-an-off-zero, but the full statement still demands self-approximation in every disk — and that is a genuine, non-vacuous theorem: it is Bagchi's RH ⟹ strong recurrence direction (positive lower density for every $\varepsilon$, from which unbounded sequences follow via the diagonal $\tau_k\in A_{1/k}$, $\tau_k>k$). The "by Bagchi" of 181.2(1) is correct and necessary, not sloppiness. ✓ 181.2(2)=181.1 ✓; 181.2(3) declared a gap ✓.

**Cor 181.3.** (1) forward = 175.2 ✓; converse-at-$I=0$ = 181.2(1) ✓; "⟺ modulo GAP 181.A" is exact bookkeeping. (2) Conditional on $A$ ($I<\infty$): LP-112 ⟹ (by 181.1) ¬($0<I<\infty$) ⟹ $I=0$ ⟹ RH; converse Bagchi. ✓ (3) is a reading, and the correct one: any proof of LP-112 contains an exclusion of the intermediate state. ✓ The D–H test of §3 is frankly labeled ([literature GAP 181.C], joint universality not verified at source — well declared, not counted as a claim).

**Consistency attack 175.2↔175.8↔181.1 (point 5).** Final logical map verified: 175.2 is proved directly (iterated replica); 175.8 is proved by counting (covering); they are two INDEPENDENT proofs of two sides of the same partial biconditional. 181.1 adds no proof; it adds the name. Neither invokes the other circularly. ✓

---

## 10. (i) Summary table

| Piece | Verdict | Note |
|---|---|---|
| Lemma 175.1 | **CERTIFIED** | quantitative Rouché–Hurwitz; constants verified |
| Thm 175.2 + Obs 175.3 | **CERTIFIED** | conditional on LP-112[$\rho_0$], declared; no double counting |
| Cor 175.4 | **CERTIFIED-WITH-ERRATA** | E-184.2 (unjustified decorative parenthetical) |
| Cor 175.5 | **CERTIFIED-WITH-ERRATA** | E-184.1 ($b_j=1/j$ violates $b<\tfrac12$) |
| Thm 175.6 | **CERTIFIED** | exponent $1-b_0/8$ = Selberg $\tfrac14\times$ Rouché $\tfrac12$, verified |
| Prop 175.7 | **CERTIFIED-WITH-ERRATA** | same E-184.1 |
| Prop 175.8 | **CERTIFIED** | the master link HOLDS against every mandate attack |
| Thm 181.1 | **CERTIFIED** | redundant as mathematics (contrapositive), decisive as reading |
| Thm 181.2 | **CERTIFIED** | case $I=0$ is NOT vacuous; "by Bagchi" is correct |
| Cor 181.3 | **CERTIFIED** | exact bookkeeping; GAPs 181.A/181.C well declared |

## 11. (ii) Structural classification (director's order)

- **Lemma 175.1:** quantified classical tool — outside the taxonomy (contributes no information about ζ).
- **Thm 175.2 / Cor 175.4:** **conditional COERCIVE** (exclusion of the state $0<I<\infty$ under an axiom). BUT, in light of 181.1/181.3: its hypothesis is equivalent (modulo GAP 181.A, and exactly under $A$) to its conclusion — **as an axiom→conclusion pair it is REDUNDANT: it is the dichotomy under the name of recurrence**. The director's suspicion is confirmed here: LP-112-as-input was a disguised local equivalence of RH (conditional on $A$, LP-112 ⟺ RH). Doc 181 is precisely the one that uncovers it.
- **Thm 175.6:** genuine **CORRELATIONAL** — unconditional, second order, transfers the certified $E(T)$ to rarity of self-approximation. D175's only piece with genuinely new unconditional content. It is the real bridge between energy and universality.
- **Prop 175.8:** unconditional **COERCIVE** — genuine exclusion of states (unbounded recurrence) within the world $0<I<\infty$. It is not a tautology: the budget $4I/b_0^2$ is real information about that world.
- **Thm 181.1:** mathematically **REDUNDANT** (contrapositive reread of strong-175.2); its value is metatheoretic.
- **Thm 181.2 / Cor 181.3:** **MIXED** — a correct assembly whose function is to demolish a false strategic reading. The "result" is the demolition, not a new theorem.

## 12. (iii) Direct answer to the director: did LP-112 die, or does it revive?

**It died, and the death is certified.** The chain 175.8 → 181.1 has no error: in the world $0<I<\infty$ — the only one where the tower needed LP-112 with content — LP-112 (even its minimal instance at fixed precision in a single disk) is **false**, unconditionally. Hence: (a) LP-112 cannot be used as an independent input, because proving it requires first excluding the intermediate state, which was the job assigned to it; (b) conditional on $A$, LP-112 ⟺ RH (Cor 181.3.2, verified): it is a local equivalence of RH, not a partial lemma; (c) the only crack of life is GAP 181.A ($I=\infty\Rightarrow$ LP-112), which in both scenarios S1/S2 leaves LP-112 without input status. **It does not revive.**

## 13. (iv) Impact on the architecture

**$\mathrm{RH}\Longleftarrow A\wedge\mathrm{Dic}$ is the correct formulation and stands confirmed.** Nuances: (1) the tower was NOT weakened by the rewrite — Dic was already LP-112's effective content in the relevant range; what was lost is an illusion, not an asset; (2) the phase's real unconditional asset is the pair {Thm 175.6, Prop 175.8} plus the 170.5 certificate: D181's successor direction (attack Dic via D174 coercivity / D176 Cesàro) is the correct consequence of this audit, not merely of initial enthusiasm; (3) warning: Dic = $I\in\{0,\infty\}$ is, under $A$, equivalent to RH — the director should watch that Phase 57+ does not rebaptize Dic under a third name and declare it an "attackable lemma" (the pattern LP-112 just exemplified). This audit's criterion: a statement is a legitimate input only if it has content in some world where it is not equivalent to the conclusion.

## 14. (v) Erratas

- **E-184.1** (D175, Cor 175.5.2 and Prop 175.7.3): the counterexample "$b_j=1/j$" violates $b\in(0,\tfrac12)$ at $j=1,2$. Correction: $b_j=1/(j+2)$. Harmless (the cardinality-vs-moment point survives intact).
- **E-184.2** (D175, Cor 175.4): the parenthetical "$\tau>\mathrm{height}(D_k)\ (>2r_k+1)$" is not justified; the proof only needs $\tau>r_k$, which does follow from $\tau>\mathrm{height}(D_k)=\gamma^{(k)}+r_k$. Correction: delete the parenthetical. Harmless.
- (Non-errata recorded): in Thm 175.6 the exclusion of lower members of the quadruple rests tacitly on $r\le\gamma_0$, which follows from $\bar\rho_0\in Z(\zeta)$ in the definition of $r$ — correct but worth making explicit in a future revision of D175 §3.

**Overall verdict: the chain 175.1→175.2→175.6→175.8→181.1→181.3 is CERTIFIED. No result falls or degrades. Phase 55–56, in this chain, breaks the 1-in-4 statistic.**
