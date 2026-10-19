# Document 185 — Adversarial audit of Documents 173 and 176 (Green–Littlewood, the Cesàro limit, A ⟹ Lindelöf, the density barrier)

**Program:** Riemann Hypothesis — Phase 58 (total audit)
**Objects:** Doc 173 (`173-structural-representation-of-sum-rules.md`) and Doc 176 (`176-attack-on-problem-a-via-green-littlewood.md`), read in full, line by line.
**Method:** independent reconstruction of each proof BEFORE reading the document's own; verification of constants and factors; structural classification by the director's order.
**Verified conventions:** both docs use $I(T)=E(T)=\sum_{\gamma_j\le T}b_j^2$, one representative per quadruple, $b\in(0,\tfrac12)$, $\gamma>0$. The convention is **consistent across 173, 175, 176** and with the counting of step (3) of 173.C's proof (see §1.3 below: the quadruple contributes exactly $b^2$ to the symmetric rectangle, i.e. $b^2/2$ for each of the two members with $\beta>\tfrac12$, $|\gamma|<T$). ✓

---

## 0. Executive verdict

| Result | Verdict |
|---|---|
| [Thm 173.C] Green–Littlewood | **CERTIFIED** (with remarks O-1, O-2) |
| [Thm 173.A] shadow–signal | **CERTIFIED** |
| [Lemma 173.B] Stieltjes rigidity | **CERTIFIED** |
| [Prop 173.D] class $X_2$ | CERTIFIED (rigor level: correct outline, weak-holomorphy technicalities not spelled out — acceptable under contract) |
| [Prop 173.E] Dirichlet dichotomy | **CERTIFIED** |
| [Prop 173.Cr] Cramér | CERTIFIED (trivial) |
| [Prop 176.1] region $\sigma\ge1$ | **CERTIFIED** |
| [Lemma 176.2] local integrability | **CERTIFIED** |
| [Lemma 176.3] $\Xi(T)\ll\log T$ | **CERTIFIED** (real improvement on 173.C) |
| [Thm 176.4] Cesàro limit | **CERTIFIED** (the delicate boundary point is correctly resolved; see §2.2) |
| [Cor 176.5] lower bound | CERTIFIED (immediate consequence) |
| [Thm 176.6] inverse theorem | **CERTIFIED-WITH-ERRATA** (E-185.1, harmless) |
| [Thm 176.7] A ⟹ Lindelöf | **CERTIFIED** (the Backlund citation is correct; see §3) |
| [Prop 176.8] layer-cake / GAP-A | **CERTIFIED** |
| [Prop 176.9] barrier | **CERTIFIED-WITH-ERRATA** (E-185.2 at point 4, minor) |
| [Cor 176.10] dichotomy of means | CERTIFIED conditional (inherits LP-112, declared) |

**Nothing falls. No result degrades in statement.** Two constant erratas (one in an auxiliary statement of 176, one in 176.9's saturation configuration), neither load-bearing. The serious criticism is **structural**, not one of correctness: 173.C and 176.4 are a change of currency (§5).

---

## 1. [THEOREM 173.C] — the Green–Littlewood identity

### 1.1. Independent reconstruction (done before reading the doc's proof)

Let $u=\log|\zeta|$, $v=\tfrac12(\sigma-\tfrac12)^2$ (note: $\Delta v=\partial_\sigma^2 v=1$ ✓, $v$ does not depend on $t$). In the **symmetric** rectangle $R=[\tfrac12,A]\times[-T,T]$, $\Delta u=2\pi\big(\sum_{\text{zeros}}\delta_\rho-\delta_1\big)$ as a distribution (the trivial zeros lie in $\sigma<0$, outside; the pole $s=1$ is **interior** to $R$ because $-T<0<T$ — an important point: in the symmetric rectangle there is no pole on the boundary). Green:
$$\iint_R u\cdot 1-2\pi\Big[\sum_{\rho\in R^\circ,\beta>1/2}v(\rho)-v(1)\Big]=\oint_{\partial R}(u\,\partial_nv-v\,\partial_nu).$$
Counting: for each quadruple with $\gamma<T$, the members with $\beta>\tfrac12$ in $R$ are $\tfrac12+b\pm i\gamma$ (two), each with $v=b^2/2$: total $b^2$ per quadruple ⟹ $\sum v(\rho)=I(T)$ with the "once per quadruple" convention. ✓ $v(1)=\tfrac12\cdot\tfrac14=\tfrac18$ ✓ — **the $+1/8$ is exactly the pole evaluated at the quadratic weight**, not $\int_{1/2}^1(1-\sigma)d\sigma$ (that is the form in which it reappears in the alternative proof; both give $1/8$, see §1.2).
Boundaries: $\sigma=\tfrac12$: $v=v'=0$, nothing (and on-line zeros fall there with $v=0$: consistently handled). $\sigma=A\to\infty$: $|u|,|u_\sigma|\ll2^{-\sigma}$ against $v\ll\sigma^2$: zero. $t=\pm T$: $\partial_nv=0$; left with $-2\int_{1/2}^\infty v\,\partial_tu(\sigma,T)\,d\sigma$ by symmetry $u(\sigma,-t)=u(\sigma,t)$. With $\partial_tu=-\mathrm{Im}\,\zeta'/\zeta$ and $\iint_R u=2D(T)$:
$$2D(T)-2\pi I(T)+\tfrac\pi4=\int_{1/2}^\infty(\sigma-\tfrac12)^2\,\mathrm{Im}\,\tfrac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma
\;\Longrightarrow\;I(T)=\tfrac1\pi D(T)+\tfrac18-\Xi(T).$$
**Matches exactly the document's boxed result, factors $\pi$, $2$ and sign included.** ✓

**Additional differential verification (mine, not in the doc):** differentiating the identity in $T$ (a.e.): $0=\tfrac1\pi\int u(\sigma,T)d\sigma-\Xi'(T)$, and $\partial_T\,\mathrm{Im}\,\tfrac{\zeta'}{\zeta}=\mathrm{Re}\,(\zeta'/\zeta)'=\partial_\sigma^2u$; integrating by parts twice $\tfrac1{2\pi}\int(\sigma-\tfrac12)^2u_{\sigma\sigma}=\tfrac1\pi\int u$ (boundaries vanish: $v=v'=0$ at $\tfrac12$, decay at $\infty$). The identity is self-consistent term by term. ✓

### 1.2. The "two independent proofs" and the $T\to0$ check

- **Main proof (Green):** complete and correct (§1.1). Step (1) (local decomposition $u=\sum\log|s-\rho|-\log|s-1|+h$, $h$ harmonic) is legitimate: $h=\log|\zeta\cdot(s-1)/\prod(s-\rho)|$ with the quotient holomorphic and zero-free in a simply connected neighborhood of the rectangle. Step (2) (Green piecewise, boundary zeros excluded via "$T$ unordered") is the classical treatment of the potential. ✓
- **Cross-check (iterated Littlewood):** it is a **one-line outline, not a second complete proof** (the display literally contains "$\dots$"). I reconstructed it: Littlewood on a symmetric rectangle gives $\int_0^T\log|\zeta(\sigma_0+it)|dt=2\pi\sum_{\beta>\sigma_0,0<\gamma<T}(\beta-\sigma_0)-\pi(1-\sigma_0)+O(\log T)$ — **pole with factor $\pi$, not $2\pi$** (the sum over zeros doubles via conjugation when folding $|t|<T$ to $0<t<T$; the pole, which sits at $t=0$, does not double). Integrating over $\sigma_0\in[\tfrac12,\infty)$: $\sum_j\int_{1/2}^{\beta_j}(\beta_j-\sigma_0)d\sigma_0=\sum b_j^2/2$ per upper zero $=\sum_jb_j^2/2$... with one zero per quadruple in $0<\gamma<T$ this gives $2\pi\cdot\tfrac{I}{2}=\pi I$ ✓, and the pole $\int_{1/2}^1\pi(1-\sigma_0)d\sigma_0=\pi/8$ ✓. The doc's arithmetic ("$+\tfrac18$ reappears as $\frac1\pi\int\pi(1-\sigma_0)d\sigma_0$") uses the **correct** constant $\pi(1-\sigma_0)$. It matches Green. ✓ (Contrast with Doc 176 §1.2 — errata E-185.1, see §4.)
- **Check at $T\to0^+$:** $\mathrm{Im}\,\zeta'/\zeta(\sigma+iT)\to$ mass $\pi\delta_{\sigma=1}$ (from the pole, $\mathrm{Im}[-1/(\sigma-1+iT)]=T/((\sigma-1)^2+T^2)$, Poisson kernel of mass $\pi$ on the half-line); flux $\to-\tfrac1{2\pi}\cdot\tfrac14\cdot\pi=-\tfrac18$, cancels the $+\tfrac18$, $I(0)=0$. ✓ Verified.

### 1.3. Truncation at $T$ and zeros near the cutoff

A necessary question: do zeros with $\gamma$ near $T$ contribute "partially"? **There is no partial atomic contribution**: with $T$ unordered, each zero is strictly inside or outside $R$ and contributes the whole $v(\rho)$ or nothing — the sum is exactly $I(T)=\sum_{\gamma\le T}b^2$ with no truncation weight. The influence of zeros near the cutoff lives **entirely in the flux $\Xi(T)$** (which is why it blows up near ordinates and is only $O(\log^2T)$ at good heights in 173.C). The doc handles this correctly and does not sweep it under the rug; the existence of good heights in $[n,n+1]$ ($O(\log n)$ ordinates ⟹ gaps $\gg1/\log n$) is correct. ✓

**Verdict 173.C: CERTIFIED.**
Remarks: **O-1**: the "independent cross-check" is a verifiable outline, not a self-contained complete proof; the claim of "two proofs" is generous but the outline reconstructs without surprises. **O-2**: the flux bound $O(\log^2T)$/good heights becomes obsolete thanks to [Lemma 176.3] ($O(\log T)$, every height) — not an error, a later improvement.

---

## 2. Document 176: the Cesàro limit and the machinery

### 2.1. [Prop 176.1], [Lemma 176.2], [Lemma 176.3]

- **176.1:** reconstructed: $\int_0^T\cos(t\log n)dt=\sin(T\log n)/\log n$, $\int_1^\infty n^{-\sigma}d\sigma=1/(n\log n)$, product $\Lambda(n)\sin(T\log n)/(n\log^3n)$ ✓; Tonelli justified by $\sum\Lambda(n)/(n\log^2n)<\infty$ ✓. The three ingredients of the "reading" (zero mean, frequencies $\ge\log2$, $\ell^1$ amplitudes) are exactly what the proof uses. **CERTIFIED.**
- **176.2:** standard local factorization (Titchmarsh §3.9) + integrable logarithmic singularity + $O(\log T)$ zeros. Valid for **every** $T$, ordered or not — this is what carries the weight in 176.4. **CERTIFIED.**
- **176.3:** the trick is real and I verified it: $\int_{1/2}^2(\sigma-\tfrac12)^2\big|\mathrm{Im}\tfrac1{\sigma+iT-\rho}\big|d\sigma\le\tfrac94\int_{\mathbb R}\tfrac{|T-\gamma|dx}{x^2+(T-\gamma)^2}=\tfrac{9\pi}4$, Poisson mass **independent of $|T-\gamma|$** — the prior integration in $\sigma$ eliminates the need for a good height. $(\sigma-\tfrac12)^2\le\tfrac94$ on $[\tfrac12,2]$ ✓; $O(\log T)$ zeros with $|\gamma-T|\le1$ ✓; the rest of the partial fractions and tail $\sigma\ge2$ ✓. **CERTIFIED. Genuine strict improvement on 173.C.**

### 2.2. [THEOREM 176.4] — the audit's most delicate point

**The risk flagged in the mandate** (Littlewood's boundary at height $T$ involves $\int\log|\zeta(\sigma+iT)|d\sigma$, NOT uniformly bounded near ordinates) **is correctly neutralized**, and via the honest route:

1. The vertical FTC $\int_{T_0}^{2T_0}\mathrm{Im}\tfrac{\zeta'}{\zeta}(\sigma+iT)dT=\log|\zeta(\sigma+iT_0)|-\log|\zeta(\sigma+2iT_0)|$ holds for every abscissa $\sigma$ not carrying a zero in the segment (all but countably many); the logarithmic singularities are integrable and piecewise absolute continuity suffices. ✓
2. The Fubini exchange $\int dT\int d\sigma$ is justified: $|\zeta'/\zeta|\sim|s-\rho|^{-1}$ is **locally integrable in 2D** (not in 1D — exactly why averaging tames what the individual height cannot). ✓
3. Crucial: the final bound uses [Lemma 176.2] **at both heights $T_0$, $2T_0$ without assuming they are good** — if there is a zero at exactly ordinate $T_0$, the singularity in $\sigma=\beta$ is logarithmic and integrable in $\sigma$. The doc does NOT assume "good heights" where it cannot. ✓
4. A detail I verified and the doc does not need to spell out: at an exact ordinate $T=\gamma$, $\mathrm{Im}\tfrac1{\sigma-\beta+i\cdot0}=0$ for $\sigma\ne\beta$ — $\Xi$ has no non-integrable singularity at $T$; the integral $\int\Xi\,dT$ is well defined. ✓

**(b):** $I(T_0)\le\overline I(T_0)\le I(2T_0)$ by monotonicity, also valid with $I(0^+)=\infty$ (the Cesàro mean diverges **cleanly to $+\infty$**, without oscillation: the monotonicity of $I$ plus the error $O(\log T_0/T_0)$ force this). ✓
**(c):** "limit $=-\pi/8\Rightarrow$ RH": requires strict positivity of a single quadruple — an off zero has $b>0$ strictly, hence $b^2>0$ and $I(0^+)>0$. Trivial but correct; verified. ✓

**Verdict 176.4: CERTIFIED.** It is the document's central technical result and withstands the mandate's targeted attack.

### 2.3. [Cor 176.5], [Thm 176.6], [Cor 176.10]

176.5: immediate from $I\ge0$ + 176.3/176.4. ✓ 176.6: (a) = 176.3.1 + 170.5 ✓; (b) Chebyshev $b\le b^2/s$ if $b>s$ ✓; uses the Littlewood-by-abscissa of §1.2 — E-185.1's pole errata lives within $O(1)\subset O(\log T)$, harmless here. The honesty declaration ("new in statement, not in method", declared folklore GAP) is exemplary. **CERTIFIED-WITH-ERRATA.** 176.10: cleanly conditional on LP-112, inheritance declared. ✓

---

## 3. [THEOREM 176.7] — A ⟹ Lindelöf (the load-bearing calibration)

Independent reconstruction, identical to the doc's:
1. $I<\infty\Rightarrow N(\tfrac12+s,\infty)\le I/s^2<\infty$ for every $s>0$ (Chebyshev over $b^2\ge s^2$). **Stronger than needed**: for each fixed $\sigma>\tfrac12$ there are only **finitely many** zeros to the right in total.
2. Hence $N(\sigma,T+1)-N(\sigma,T)\to0$ ($T\to\infty$) for each fixed $\sigma>\tfrac12$ — in fact it is eventually $0$.
3. Backlund's criterion: **LH $\iff$ for every $\sigma>\tfrac12$, $N(\sigma,T+1)-N(\sigma,T)=o(\log T)$.** I verified the citation: it is the classical Backlund equivalence (1918–19), as found in Titchmarsh ch. XIII (§13.5, where the equivalence is proved in both directions — it is indeed an equivalence, not just an implication). The direction used here (count $o(\log T)\Rightarrow$ LH) is the direction proved by Backlund via Hadamard three circles/Borel–Carathéodory. The citation is correct and the cited version is the one needed.
4. $\to0$ is much stronger than $o(\log T)$ ⟹ LH. $\square$

**Verdict 176.7: CERTIFIED.** Without reservation. Auditor's note: the doc even underexploits its step 1 — under A, *every* half-plane $\sigma\ge\tfrac12+s$ contains finitely many zeros; A is "quasi-RH" in a sense stronger than the chain needs. The self-assessment "trivial once stated, new as the program's observation" is honest. The chain RH⟹$m<\infty$⟹A⟹LH⟹DH: every arrow verified (the last is Ingham 1940 ✓); "strict" is used in the sense of "converses unknown", declared in §4.1 ✓.

---

## 4. [PROP 176.9] — the barrier, and the erratas

**The integral:** $\int_0^{1/2}s\,e^{-cs\log T}ds\le\int_0^\infty s\,e^{-cs\log T}ds=(c\log T)^{-2}$ ✓ ($\Gamma(2)=1$). Exact layer-cake of 176.8(a) verified ($b^2=\int_0^b2s\,ds$ + Tonelli ✓). Conclusion $E(T)\le\tfrac{2C}{c^2}T(\log T)^{\kappa-2}$ ✓; **$c$ only enters the constant** ✓ (the shape of the ceiling is fixed by $\kappa$); Selberg $c=\tfrac14,\kappa=1\Rightarrow T/\log T$ ✓ — coherence with 170.5 verified. Point 3 (LH/Halász–Turán vacuous at $s\asymp1/\log T$, where $T^{-cs}\asymp1$): correct, it is the fatal-mass observation. **Honest formulation?** Yes: it is explicitly framed as a barrier of the **density→energy conduit** ("it cannot give less without new information at $s\asymp1/\log T$"), not of statement A — the layer-cake uses density as its only input, and this is stated.

**Minor errata (E-185.2):** at point 4, the consistency check of the saturated configuration asserts "$T^{1-cs}\log T=e^{-c}T\log T\le N(T)$ for $\kappa\le1$" at $s=1/\log T$: with $N(T)\sim\tfrac{T}{2\pi}\log T$ this requires $e^{-c}\le\tfrac1{2\pi}$, false for small $c$ (e.g. Selberg $c=\tfrac14$). It is trivially repaired by inserting a small constant into the configuration ($N\asymp\epsilon\,T^{1-cs}\log T$), which does not alter the conclusion $E(T)\asymp_\epsilon T/\log T$. The optimality survives; only the consistency line is careless.

**Verdict 176.9: CERTIFIED-WITH-ERRATA (E-185.2).**

**MAIN ERRATA (E-185.1), Doc 176 §1.2:** the "Littlewood lemma by abscissa" is stated with pole term $-2\pi(1-\sigma)$. **The correct constant is $-\pi(1-\sigma)$** (reconstruction §1.2 of this doc: when folding the symmetric rectangle from $|t|<T$ to $0<t<T$, the zeros double by conjugation but the pole at $t=0$ does not; equivalently, Doc 173 §6.1 uses $\pi(1-\sigma_0)$ and obtains the correct $1/8$ — the two documents contradict each other on this constant, and 173 is right). Impact: only the lower-bound display of §1.2 and the proof of 176.6(b), where the pole is $O(1)$ absorbed into $O(\log T)$: **no theorem affected**. If the $2\pi$ constant were correct, 173.C's cross-check would give $1/4$ instead of $1/8$ and would contradict the Green proof — this is not the case.

---

## 5. Audit of 173.A, 173.B, 173.D, 173.E (mandate point 5)

- **[Thm 173.A]:** Lemma 173.0 verified (even Taylor expansion in $b$; $\varphi''(t)=-\Phi''(\tfrac12+it)$ via $i^2=-1$ ✓; remainder $b^4/6$ ✓; cross-check with the resolvent §2.1: $(1-12\gamma^2)/a^3$ recomputed, matches ✓). (b): $w\ge0\Rightarrow\varphi_r$ concave; the exclusion argument for $\varphi_r'<0$ and the evaluation $\int w=2\varphi_r'(0)$ correct. (c): the IBP and $X\varphi_r'(X)\le2\int_{X/2}^X\varphi_r'\to0$ correct. (d): correct (localized concavity + real-analyticity of $\varphi_r$). **CERTIFIED.** It is the obstruction theorem with real content in Doc 173.
- **[Lemma 173.B]:** verified step by step: $\partial_a[a/(a^2+t^2)]=(t^2-a^2)/(a^2+t^2)^2$ ✓ (correct sign in the doc); IBP boundaries vanish ✓; the change $u=a^2$ gives exactly $\tfrac12m'(\sqrt u)/(u+t^2)$ ✓; the hypothesis $\int(1+a)|m'|<\infty$ is precisely what makes $g\,du$ a finite measure for Widder ✓. The beta illustration: $\int_0^\infty x^4/(1+x^2)^4=\int x^2/(1+x^2)^4=\pi/32$ (verified by the symmetry $x\mapsto1/x$), $\int(1+x^2)^{-4}=5\pi/32$, $1-6+5=0$ ✓. **CERTIFIED.**
- **[Prop 173.D]:** the outline (parity ⟹ no linear term; coefficient of $b^2$ coupled to $F_0$; autonomous term $=O((\sum b^2)^2)$) is correct as proved; the weak-holomorphy technicalities in $\mathcal H$ are not detailed but the contract allows it and nothing downstream leans on them. Structural diagnosis (3) — "$I=\|F\|^2$ requires breaking the quadruple's parity = a non-holomorphic operation" — is the document's best sentence and it is correct. **CERTIFIED** (rigorous-outline level).
- **[Prop 173.E]:** the direction RH ⟹ $\tilde d\equiv0$ trivial; the divergence with one atom ($\int_0^{r_0}2\pi r\,dr/r^2=\infty$) correct; the local bound on the remaining series uses $E(T)\ll T/\log T$ — plausible and sufficient for local uniform convergence of harmonics (which controls gradients). **CERTIFIED.** The "atomicity obstruction" (linear-in-measure vs quadratic-in-field) is a correct and honest diagnosis of why $I\ne\|F\|^2$ here.
- **Anti-circularity:** neither document assumes RH, Lindelöf, nor LP-112 outside the results marked conditional (176.10). The inputs are Hadamard, Littlewood, Selberg, Backlund, von Mangoldt — all unconditional and backward. No circularity detected. ✓

---

## 6. Structural classification (director's order)

| Result | Class | Unsparing justification |
|---|---|---|
| 173.A + 173.B + 173.D | **negative COERCIVE** (no-go) | They exclude a class of representations. Real content: they explain ceiling 172.9 without windows. They do not move closer to RH; they close doors with proof. |
| 173.C | **REDUNDANT with cartographic value** | Exact identity = **currency change**. The two sides ($\sum b^2$ and $\iint\log\|\zeta\|$) are *the same object* via Green; neither is softer than the other — controlling $\iint\log\|\zeta\|$ down to $O(1)$ in the strip IS controlling the zeros (and the program itself confirmed this later: 180.4, collapse of the integral route). What is NOT redundant: the $m=0,1,2$ taxonomy of transversal moments and the identification of the two non-holomorphic operations (real part + half-quadruple) — that is genuine cartography of the wall. But as a *route to A*, it is a local reformulation of A. |
| 173.E | **degenerate-REDUNDANT** (declared by the doc itself) | "RH = membership" with norm $\{0,\infty\}$: the atomic dichotomy empties the content. The doc says so; the auditor confirms it. |
| 176.1–176.3, 176.5, 176.6 | **CORRELATIONAL** (type A, fine second order) | Unconditional technical control of the integrand/boundary. 176.3 is the most valuable technical piece of the pair of documents. |
| 176.4 | **REDUNDANT with a real technical improvement** | "A ⟺ a finite limit of something that always exists" is a repackaging of A — the limit *is* $\pi I-\pi/8$ by construction, the currency's difficulty did not change. The real, non-redundant improvement: the **unconditional elimination of the boundary** ($O(\log T_0/T_0)$, with no good heights) — that is a technical theorem, not a tautology. But the phrase "A is converted" oversells: A is *rewritten*. |
| 176.7 | **MIXED — genuine bridge. The pair's only real calibrator.** | Connects two statements of heterogeneous difficulty (A, a new node; LH, a classical node) with a complete proof. It establishes "A is Lindelöf-hard": the only new and exportable *position* information. Indeed: **176.7 is the only result with genuine calibrating content**, a direct answer to the director's question. |
| 176.8 | **useful REDUNDANT** | Exact repackaging of A (layer-cake); its value is naming GAP-A precisely. |
| 176.9 | **negative COERCIVE** | Method barrier, honest, with the exact account. Together with 176.7 it forms Doc 176's real deliverable: A lies *between* $m<\infty$ and LH, and the density conduit *does not reach*. |

**Judgment on the central question:** 173.C and 176.4 are identities, not bridges: they equate two descriptions of the same object without either side being more tractable (the wall of the strip $\tfrac12<\sigma\le1$ reappears intact in 173 §6.2 — the doc itself admits this in the form "prime field"). The package that survives as progress is: **proved obstruction (173.A) + proved position (176.7 + 176.9)**. That is coercive cartography of the wall, not progress toward crossing it — and it is stated with unusual honesty in both documents.

---

## 7. Impact on the architecture

- **Nothing falls**: the representation of I (173.C) and the reformulation of A (176.4) stand certified; the architecture RH ⟸ A ∧ LP-112 (175) is unaffected.
- **A's position is consolidated**: the chain RH ⟹ $m<\infty$ ⟹ A ⟹ LH ⟹ DH stands audited arrow by arrow; "A is Lindelöf-hard" is now a certified program fact, usable as calibration in later phases.
- **Structural warning**: since 173.C/176.4 are a currency change, any plan that attacks A "from the integral side" (bounding $\overline D$ above) must declare where information that is not about zeros will come from — barrier 176.9 plus the later collapse (180.4) indicate that this side is no softer. The actionable residue this audit endorses: GAP-A (density uniform in $T$, finiteness genus) and PIVOT 176.P1 (log-free near $\sigma=\tfrac12$).

## 8. Erratas

- **E-185.1** (Doc 176 §1.2): pole term of the Littlewood-by-abscissa lemma: it says $-2\pi(1-\sigma)$, should say $-\pi(1-\sigma)$ (in the normalization with zeros counted in $0<\gamma\le T$). Contradicts Doc 173 §6.1, which uses the correct constant. Impact: $O(1)$, no theorem affected; fix before publishing 176.6.
- **E-185.2** (Doc 176, Prop 176.9, point 4): the saturated configuration requires a small constant ($N\asymp\epsilon T^{1-cs}\log T$) to be compatible with $N(T)\sim\tfrac T{2\pi}\log T$ when $e^{-c}>\tfrac1{2\pi}$; as written ("$\le N(T)$ for $\kappa\le1$") it is false for $c<\log2\pi$. The barrier's optimality is unaffected.
- **E-185.3** (Doc 173 §6.1, minor): the "independent cross-check" of the $+1/8$ is an outline with an ellipsis, not a second complete proof; reconstructible and correct, but the executive summary's label "two independent proofs" (if exported) should say "proof + consistency check in two forms".

The pair's weakness is not one of correctness but of nature: two mirror identities and two position/obstruction theorems; the only bridge between genuinely different difficulties is 176.7.
