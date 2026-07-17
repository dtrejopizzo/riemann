# Riemann Hypothesis Research Program — Complete Summary

**Author:** David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com
**Compiled:** June 2026 · **Updated:** 2026-07-17 (covers phases through 76)
**Purpose:** An exhaustive reference for everything investigated — roads traveled, blocks found,
routes exhausted, routes still live.
**Absolute honesty:** no proof of RH has been found. A false victory would be worse than a failure.

> This summary is organized as: the two empirical/theoretical arcs and the CCM framework
> (Parts 1–4), the structural walls (Part 5), the papers (Part 6, catalogued in
> [`04-papers/README.md`](04-papers/README.md)), what was proved
> unconditionally (Part 9), the honest final assessment (Part 10), and a compact verdict log
> for Phases 35–76.

---

## PART 0 — Program structure

Two empirical layers feed one theoretical program:

- **Research Programs 1–9** (`01-context/`): nine computational research programs (627
  tasks) — the descriptive base (resonance, ω-class, the localized Weil detector).
- **Program 10** (`03-research/`): the 61-phase theoretical program.

```
ARC A — ω-class program (Phases 0–9)
        Goal: bound the cross-sum B(N) ≤ N^ε → Lindelöf.  Result: circular, parity-blocked.  CLOSED.

ARC B — Inverse operator / Hilbert–Pólya (Phases 10–28)
        Goal: the self-adjoint operator with spectrum {γ_n}.  Result: arithmetic-propagation
        wall blocks every route.  CLOSED (except an adelic-Maslov fragment).

CCM FRAME — Connes–Consani–Moscovici (Phases 29–33)
        Goal: use the CCM trace T_λ = 0 ⟺ RH.  Result: three RH-equivalent routes, no proof
        (Hadamard barrier).  CLOSED.

PHASES 34–61 — new directions, Hodge/Spec-ℤ construction attempts, the wall-as-object attack,
        and the closure audits.  Net: the wall mapped from every side; no crossing.
```

---

## PART 1 — Arc A: the ω-class program (Phases 0–9)

**Central idea.** Decompose the Dirichlet polynomial $S_N(t)=\sum_{n\le N} n^{-1/2-it}$ by the
class $\omega(n)\bmod 2$ (parity of the number of prime factors). Hypothesis: the ω-even and
ω-odd classes cancel anti-constructively ⟹ $S_N=O(N^\varepsilon)$ ⟹ Lindelöf ⟹ RH.

**Blocks.**
- **Circularity (P2).** Proving $B(N)\le N^\varepsilon$ requires Lindelöf as a hypothesis — the
  target was *stronger* than Lindelöf.
- **Parity problem.** Selberg/Bombieri sieves cannot distinguish $\omega(n)\bmod 2$ — intrinsic
  to sieve theory.
- **Wrong sign.** Every unconditional tool gives *lower* bounds on positivity; RH needs an
  *upper* bound ($\lambda_{\min}(Q)\ge0$). Confirmed in 8 independent paradigms.
- **P5 refuted.** The r4/r5 phase transition at $N_c\approx1.18\times10^5$ was refuted by
  canonical re-verification; the honest result is that ζ is *more* constructive at peaks, no
  transition.
- **TDA refuted.** Persistent homology (H0/H1) does not detect off-line zeros.
- **Per-place positivity fails (Phase 6).** The local OS form $\int|\hat\psi|^2 G_p$ is
  indefinite ($G_p(0)>0$, $G_p(\pi/\log p)<0$; verified p=2,3,5,7).

**Valid partial result.** The **localized detector** (P7): an off-line zero at distance δ forces
$\lambda_{\min}(Q)\le -c(\delta,\sigma,J)<0$ (forced negativity). This does not prove RH but
establishes RH ⟺ positivity of a specific quadratic form.

---

## PART 2 — Arc B: inverse operator / Hilbert–Pólya (Phases 10–28)

**Central idea.** Find the Hilbert–Pólya operator $H$ with spectrum $\{\gamma_n\}$, or a
structural reason the Weil form $Q$ must be non-negative.

**Key phases.** Phase 10 (inverse Jacobi reconstruction); Phases 11–14 (arithmetic stability,
anatomy, ω-hierarchy, branching chaos — valid phenomenology); Phase 15 (relative bounded form,
blocked); Phases 16–18 (Pontryagin finite defect; unconditional finite bottom; loss
localization); Phases 19–20 (Euler-product anatomy; finite-to-full uniformity gap); Phase 21
(Lefschetz dichotomy); Phases 22–23 (Paley–Wiener barrier — the propagation wall); Phase 24 (15
classical mechanisms audited, all blocked); Phase 25 (Kreĭn / LP-Turán / de Bruijn–Newman);
Phase 26 (bridge theorem); Phase 27 (local-global, two walls); Phase 28 (four fronts, all reduce
to $\xi\in$LP).

**Main blocks.**
- **Arithmetic-propagation wall (central).** Euler product converges only for Re(s)>1;
  information does not reach Re(s)∈(1/2,1); zeros are global, no prime owns a zero. Identified
  from 5 independent directions.
- **Lefschetz dichotomy (P21).** The ample class cannot be supplied by Spec ℤ.
- **Local-global (Phase 27).** Two walls: $Q_{\mathrm{zero}}$ does not factor over primes;
  Hasse–Minkowski fails in infinite dimension. Phase 26's V.2 and Phase 27 are the same obstacle.

**Valid key result.** The **bridge theorem** (Phase 26): $\kappa(Q)=\mathrm{neg.ind}(H_C)$ in the
Pontryagin space $(K,Q)$; RH ⟺ κ=0 ⟺ neg.ind$(H_C)=0$.

---

## PART 3 — The CCM framework: Connes–Consani–Moscovici (Phases 29–33)

**Central idea.** Use the CCM construction: archimedean measure
$dm_\infty(s)=(2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$; exact Jacobi coefficients
$a_k^\infty=\tfrac12\sqrt{(2k+1)(2k+2)}$; full measure $dm_{\mathrm{full}}=|\zeta(1/2+is)|^2\,dm_\infty$;
Abel kernel $W_\lambda$; trace $T_\lambda=\int W_\lambda(dm_{\mathrm{full}}-dm_{\mathrm{full,on}})$.
**Main theorem:** RH ⟺ $T_\lambda=0$ for all λ>0.

**Eight conditions equivalent to RH** (Doc 89): RH; $d\nu=0$; Cauchy transform $\mathcal G=0$;
$T_\lambda=0\,\forall\lambda$; Jensen $\delta=0$; variational $\tilde\delta_\lambda^2=0$;
$\mathrm{KL}=0$; $d_{\mathrm{CCM}}=0$.

**The Hadamard barrier.** No property of ζ verifiable *without* knowing zero positions implies
$d\nu=0$. This is why the three CCM routes do not close: they are equivalent reformulations of
RH, not proof paths.

**Important later correction.** In Phase 38 the claim $W_\lambda\ge0$ was **refuted**
($\int W_\lambda\,dm_\infty=0$ exactly ⟹ $W_\lambda\ge0$ is false; an Abel-summation sign error
from Doc 63 had propagated into P39/P40/P41/P43). The trace criterion was **repaired** by a new
route: RH ⟺ $\Delta_n=\int|\mathcal P_n|^2\,d\nu$ constant, via moment rigidity
(Meixner–Pollaczek polynomials, Carleman determinacy, Hardy 1914); the refuted direction is
omitted from the corrected papers rather than kept as a standing erratum.

---

## PART 4 — Phase 34: new directions (Docs 90–97)

Four directions tested after the CCM routes:
- **A (external arithmetic info):** BLOCKED — the closing conjecture $\mathbf C_A$ is RH-equivalent.
- **B (Pontryagin space):** PARTIALLY LIVE — only the adelic Maslov-index angle ($\mu_\mathbb{A}=\mu_\infty+\sum_p\mu_p=0$, not obviously circular; needs the local theory of $H_C$ over $\mathbb Q_p$, undeveloped). Theorem 8.1: the negative index is localized in $\mathcal K_{\mathrm{off}}$.
- **C (inverse Jacobi):** CLOSED as a route, but yields the **sum rule** $\sum_k e_k^2=\int\log|\zeta|^2\,dm_\infty$ (new).
- **D (second variation):** PARTIALLY LIVE — the *shadow minimizer* $g^*$ is a new object; Theorem 7.5 (conditional): $g^*=f_0^{on}\iff$RH. *(Phase 35 later degraded D via the absorption theorem.)*

---

## PART 5 — The structural walls (recap)

| Wall | Statement |
|---|---|
| **MW-1** Weil positivity | $W(f\star\tilde f)\ge0$ ⟺ RH (Weil 1952). Appears on every front. |
| **MW-2** Arithmetic propagation (central) | Euler info from Re(s)>1 does not reach the critical strip; zeros are global. Blocks all local-to-global arguments. |
| **MW-3** Hasse–Minkowski in ∞ dimension | No HM theorem for infinite-dimensional Hermitian forms; local ≠ global positivity. |
| **MW-4** Hilbert–Pólya (wrong sign) | Unconditional tools give lower bounds; RH needs an upper bound. 8 paradigms. |
| **MW-5** Arithmetic site | $Q=Q_\infty+\sum_p Q_p$ needs $H^1(\mathrm{Spec}\,\mathbb Z,\mathcal F)$ — the unfinished Connes–Consani site. |
| **MW-6** Uniform spectral gap | $\sup_X|\lambda_{\min}(Q_X)-\lambda_{\min}(Q_\infty)|\to0$ is RH-equivalent. |
| **MW-7** Hadamard barrier (CCM) | No zero-position-free property of ζ implies $d\nu=0$. |

All seven are one obstruction in disguise: **the master quantifier** — RH is always the move from
"on average / for almost all / in the interior" to "for the specific / uniformly / on the
boundary." The arithmetic object lives in the measure-zero exceptional set of its own generic
behavior, and genericity cannot detect a measure-zero event.

---

## PART 6 — Papers

The full catalogue (titles, type, contents, dependencies) is
[`04-papers/README.md`](04-papers/README.md): **36 publishable papers**, numbered 01–36. The
corpus runs from 01 (the critical-line survey) through 36, the current culmination:
**36-obstruction-ledger**, "The Riemann Hypothesis: An Obstruction Ledger and the Arithmetic Pick
Architecture It Shaped" — a fifteen-step arithmetic Pick/Nevanlinna chain (ARP-P) reducing RH to
the single open input of Li–Keiper positivity ($\lambda_n\ge0$), already on arXiv. Paper 34
("The Architecture of Obstruction") is the pre-Pick synthesis that 36 builds on and supersedes as
the final ledger.

Corrections and retractions (e.g. the refuted $W_\lambda\ge0$ direction) are recorded inline in
the affected papers and in this document (see Part 7 above) rather than in a separate errata
file.

---

## PART 7 — Live routes (not exhausted)

- **Adelic Maslov index** (B-live): $\kappa=\kappa_\infty+\sum_p\kappa_p$; if each local $\kappa_p=0$, then $\kappa=0$. Needs the $p$-adic theory of $H_C$ — not built. Genuinely open.
- **The Hilbert–Pólya / Connes–Consani object** (the terminus): a spectral triple whose operator $D$ is *not* the flow of the primes (spectrum ≠ {log k}, partition ≠ ζ) with Chern character = κ = 2m. RH-hard by construction — any $D$ manufactured from the arithmetic of the primes has partition ζ (Bost–Connes), and a $D$ with spectrum {γ} already knows the zeros.
- **Deninger leafwise-Hodge** (Phases 42–43): the implication "Kähler–Riemann space ⟹ positivity ⟹ RH" is genuine geometry, but the antecedent "Spec ℤ *is* Kähler–Riemann" fails the non-circularity test in the only realized witness (it uses the Hasse analogue as input). Indeterminable, strong bias to circular.

---

## PART 9 — What the program proved (unconditional)

1. $d\nu\ge0$ (CCM measure difference non-negative).
2. $T_\lambda\ge0$ (CCM trace non-negative); absolute convergence of $T_\lambda$.
3. $b_k^{\mathrm{full}}=0$ (Jacobi diagonal, functional equation); $\sum_k e_k^2<\infty$ (Hilbert–Schmidt).
4. Completeness of $\{e^{i\gamma_n s}\}$ in $L^2(W_\lambda\,dm_\infty)$ (Carlson–Beurling).
5. Sum rule $\sum_k e_k^2=\int\log|\zeta|^2\,dm_\infty$; off-line zeros create no discrete eigenvalues in $J^{\mathrm{full}}$.
6. Negative index localized in $\mathcal K_{\mathrm{off}}$ (Theorem 8.1); $F(z)=F(1/z)$; $|\Theta(z)|\equiv1$.
7. Bridge theorem $\kappa(Q)=\mathrm{neg.ind}(H_C)$.
8. **Second-order results (Phase 54):** the balance law $\dot I=-2\kappa(t)-D(t)$ under the DBN flow with RH ⟺ $I(0^+)=0$ ($I=\sum b_j^2$); and $E(T)=\sum_{\gamma\le T}(\beta-\tfrac12)^2\ll T/\log T$ (Selberg density + layer-cake) — the first unconditional second-order result, escaping the integral-zero no-go that kills every first-order quantity.
9. **Local purity decidable (Phase 44):** for single-prime Euler objects, the positivity axiom H ⟺ $|\alpha|=\sqrt p$ (purity of weights). Corollary: the Euler product does *not* imply H — the discriminant is purity, not multiplicativity.
10. **Two-prime Weil positivity (Phase 45):** the first Weil-positivity theorem with two pure primes, $Q_X\ge0$, with the cross terms exactly zero — extends additively to $n$ primes.
11. ~18 further unconditional theorems across Phases 44–59 (logistic index law, semilocal positivity with archimedean term, the index identity $\mathrm{neg.ind}(Q_1\otimes Q_2)=p_1q_2+q_1p_2$, sub-resolution positivity, the pinned-moment identity $\equiv2/3$, $\int\Sigma^2\ll T_0$, the ceiling theorem, RvM-t).

---

## PART 10 — Honest final assessment

**What the program achieved.** It mapped the territory around RH with surgical precision:
named the structural walls (MW-1…MW-7) from many independent directions; proved real
unconditional results (Part 9); established new equivalences (the 8 CCM conditions, the bridge
theorem); and systematically explored the CCM framework, identifying exactly where its capacity
ends. It located RH in the sign of a single global scalar κ = #(off-line zeros): an upper-bound,
one-sided condition orthogonal to all symmetry data.

**What it did not achieve.** No proof of RH — not partial, not a useful conditional, not a new
unblocked path. The "live" routes (adelic Maslov, shadow minimizer, Deninger leafwise-Hodge) are
genuinely open but with no guarantee.

**The master obstruction.**
> No global property of ζ — its functional equation, the Euler product, growth estimates, the
> asymptotic zero distribution — implies that its zeros lie on the critical line, without
> assuming that localization a priori.

Any proof must find a property of ζ that crosses this barrier, and such a property, if it exists,
is genuinely new. Historically the only crossing was in function fields (Weil, Deligne), where
geometry counts the zeros one by one without averaging. For the integers that geometry — a
cohomology over Spec ℤ with the zeros as Frobenius eigenvalues — is not known. That is the
missing object.

---

## PART 11 — Phase verdict log (Phases 35–61)

Compact record of the post-Phase-34 arc. "PARTIAL/LIVE" = something survived; "CLOSED" = route
exhausted with a theorem or barrier.

| Phase | Theme | Verdict |
|---|---|---|
| 35 | Five fronts in parallel | D-route degraded (absorption theorem); CF-rigidity (E1/E5) and incremental semilocal Maslov (Conj 100.A) survive. New: $T_{\lambda_0}=0$ for a single $\lambda_0$ ⟺ RH ($W_\lambda$ strictly positive everywhere) — P41. |
| 36 | Forms A, B, C | A (2D propagation) and C (effective SR_d) CLOSED with theorems. B (amplification functor) the survivor: strictly superadditive index $p_1q_2+q_1p_2$, exponential amplification $(4m)^k/2$ on $\mathcal K_{\mathrm{off}}$. Decisive finite test (two-variable Weil) → live candidate Doc 107 (P42). |
| (Doc 108) | Sieve→index bridge | DEAD BRIDGE (closes Form B): the required bound is asymptotic with $o(1/\log T)$ uniformity — RH in disguise; the gap is the average→uniform quantifier in sieve coordinates (P43). |
| 37 | Physics mode | Architecture: RH = (m<∞) ∧ (m<∞ ⟹ m=0). Anti-Siegel (two quadruples cost more, never compete); spectral flow of the Euler filtration RH ⟺ sf{A_λ}=0; value-vs-inertia frontier is infinite-rank vs finite-rank-a-priori. |
| (Doc 112) | The dichotomy m<∞ ⟹ m=0 | Partial: LP-112 (sequential self-approximation) ⟹ m∈{0,∞}; combined with finiteness (L8) ⟹ RH. LP-112 strictly weaker than known sufficient conditions; the B²→pointwise gap is the master quantifier in sequential coordinates (P44). |
| 38 | Final adversarial audit | $W_\lambda\ge0$ REFUTED (propagated to P39/40/41/43); trace criterion REPAIRED (moment rigidity, Meixner–Pollaczek). P44 survived all four audits intact. New papers P45 (moment rigidity), P46 (ζ not Stepanov a.p.), NOTE-CC. |
| 39 | G1↔G2 interface | Backward-derived the required cohomology axioms. G1 ("they nearly have it" — obstruction predates their tolerance technique by years); G2 ("nobody has it" — zero signatures in the entire CC corpus). |
| 40 | Close G1 | G1 not closable independently of G2: their numerical core is the same object (the intersection form). Isolated the single missing link: a positive intersection form / polarization on $H^1$ of the square. |
| 41 | Build G2 | The toy $C_p\times C_p$ reproduces the Hodge index (signature (1,2)) — but Babaee–Huh (Duke 2017) show the tropical Hodge index is not automatic on the infinite lattice. The narrow non-circular path = a tropical Kähler package with continuous ℝ₊ flow — connects to Deninger. |
| 42 | Hodge dynamics/foliated | First non-circular signal: Forni/Teichmüller is CIRCULAR (the scale flow carries ζ); Deninger leafwise-Hodge is NON-CIRCULAR *as a framework* (positivity is derived, not postulated, in the Kähler–Riemann case). |
| 43 | Destruction test of the foliated route | REVOKES Phase 42's optimism to INDETERMINABLE (strong bias circular): the realized Deninger witness defines the leafwise metric *after* invoking Hasse — RH-for-E is input, not output. The bare space plausibly exists without RH; the polarized one plausibly does not. |
| 44 | New mathematics | Three new frameworks with proved theorems: the category 𝒜rith (local purity decidable); defect theory 𝒫ol_δ (finiteness as essential positivity, Fredholm-stable; κ=2m from computation to theorem); the exact logistic tower law $\sigma^{(k)}=\tfrac12(1-(1-2\sigma^0)^{2^k})$, RH ⟺ tower → 0. |
| 45 | Fredholm, two primes, logistic | New RH equivalence (both branches proved): RH ⟺ $\lim\sigma_{loc}^{(k)}=0$. First $n$-prime Weil positivity. The Weil–Toeplitz C*-algebra ("zeros live on the symbol/compact boundary") + new falsifiable non-RH lemma LP-134. |
| 46 | Audit + three attacks | Three real degradations (logistic loses the ¬RH branch; P48 novelty withdrawn; Thm 5.3(ii) falls). Two genuine positives: first semilocal positivity with archimedean term (uniform in S, includes ζ); the transmission identity (only the full Euler product sees the pole). |
| 47 | Five live fronts | Both halves of the Fredholm wall are arithmetic (LP-141 refuted analytically, the minimal pivot). H⁺ collapses toward RH (the finite-semilocal class is empty). Davenport–Heilbronn cleanly separates the two halves of RH: repulsion is *cheap*, purity is the live front. |
| 48 | Audit + purity front | Audit paid a fourth time. Two new results: the impurity spectrum (RH ⟺ single resonance; exact jurisdiction of Λ≥0; Landau inversion) and the self-scale excess (first swarm signal with proved sign). Rigidity now has two dual handles: LP-112 (recurrence) and LP-152 (prime correlation). |
| 49 | Attack the wall as object | PIVOT. The wall = the kernel N(A) of the averager. The 5 known crossing mechanisms (tauberian, positivity, equation, group/dynamics, index/K-theory) all COLLAPSE for the Weil form. Only escape = a new input (cohomology over Spec ℤ that reads inertia). New thread: ℚ-linear independence of {log p} as a candidate raw-arithmetic input. |
| 50–51 | Diophantine thread + functor | The diophantine thread is confined to the phase axis (RH-free transport exists). NO-GO WITH THEOREM: every canonical inertia metric on the crossed product of the primes carries ζ by modular structure (partition = ζ, Bost–Connes). The whole crossed-product family is closed. |
| 52 | Homotopy inertia | (A) — the best new idea, aimed at the root — confirmed the wall, did not cross it. The metric was not ζ's last hiding place: removing it (the metric-free e-invariant was genuinely built), ζ reappears one level deeper, in the fundamental class of the zeros↔primes duality. New parity obstruction (a ℚ/ℤ invariant cannot transport an integer). |
| 53 | Quantum import | Sharpest diagnostic: QM resolves its duality because its metric (Born positivity) is an axiom. The primes↔zeros duality lives in an indefinite Kreĭn space (κ=2m) where definiteness IS RH. Same structure, opposite epistemic direction. |
| 54 | Index dynamics κ | Certified theorems: the balance law $\dot I=-2\kappa-D$ (pure dissipation, ζ-free law); $E(T)\ll T/\log T$ (first unconditional second-order); the pinned-moment identity $\equiv2/3$; $\int\Sigma^2\ll T_0$; the ceiling theorem. Definitive closures: individual-window (false even under RH), almost-every-window (collapses onto E). |
| 55 | Two arrows | Program CLOSED honestly: the P41 trichotomy complete; the 7 walls unified into one master quantifier; no live routes in known argument forms. Delivers a complete wall map, the unconditional ledger (L1–L8), and the direction of the missing mechanism. |
| 56 | Two towers (recalibrated) | Each tower = a calibrated hard pillar + LP repulsion. Final symmetry of the towers. |
| 57–58 | Brick-A attempt + full audit | The architecture RH ⟸ A∧Dic and the tower-2 static pinch are AUDITED AND FIRM. ~5/40 refuted/degraded. Reopenings toward A: R1 (non-standard mollifiers), R2 (anisotropic edge flow — the new concrete front). |
| 59 | Full closure | Ledger: 4 THEOREM + 2 BARRIER + 5 EXACT-CALIBRATED + 1 disjunction + ~12 open-with-price; no hard leaks. Final: RH = A ∧ Dic, each half calibrated (A: Lindelöf-hard, prices S1/S2; Dic: purity, price S3); ~18 new unconditional theorems; the no-go axiomatized; the exact interface for an external attack. |
| 60 | The discriminant | NG-F1: the multiplicativity discriminant in the localized Weil form is REFUTED on both sides — the zero side is circular (location); the arithmetic side does not separate ζ from smooth non-multiplicative controls (the apparent separation was a smoothness artifact). A new variant of MW-2. (Reproducible code in `phase-60-discriminant/`.) |
| 61 | Open problems | Inventory of what remains genuinely open in the CCM frame (O1–O10): the wall = RH (O10), reachable only with a genuinely new structural idea; O8/O9 are its two accesses. Validated engine in `phase-60-discriminant/experiments/`. |
| 62 | Cesàro closure / quaternionic HR | NG-62: Cesàro-in-λ averaging of `b_bulk` is RH-equivalent, not RH-neutral (off-line growth is secular, not oscillatory) — relocates MW-2, does not cross it. NG-62b: a genuine quaternionic Hodge–Riemann polarization is present on the finite Weil window but is gapless (`e^{-cL}→0`); ζ sits exactly at the marginal threshold `μ_max=1`. Three faithful but gapless detectors of one wall. |
| 63 | Lefschetz realization | NG-63: MW-5 made precise by direct F_q-vs-ℤ contrast — real elliptic curves over F_q have a J-linear Frobenius isometry of a gapped polarization; the ζ window has neither (the scaling operator anti-commutes with J, and the polarization is gapless). Sharpest concrete statement of the master wall to date. |
| 64 | Connes' route | Task A confirmed, Task D proven a parity no-go. L1 reclassified: not a restatement but a genuine RH criterion. Pivots the target from a finite Weil-positivity gap to a *regularized* positivity (relative determinant / de Branges Schur) — the first reformulation in the arc that is not on MW-1. |
| 65 | Signature continuity | Construction phase (no computation): builds toward an index-graded regularized determinant `D̃` and a topology `τ_κ` in which the Hermite–Biehler class is closed and the rank-one pole renormalization converges. Identifies the decisive burden (`D8+D9`, Feshbach-shorting the positive divergent pole) without discharging it — the wall becomes "construct a renormalization-stable self-adjoint completion." |
| 66 | Rank-one escape (CAND-1) | Reframes the whole route: because CAND-1's operators are self-adjoint by construction, positivity is free and the open question is boundedness/convergence, a different category from MW-1. States the sharp escape dichotomy (uniform boundedness of `P_prim K_P P_prim` ⟺ RH) but the orthogonality of the off-line escape direction to the pole direction is not yet nailed; a crude numerical proxy failed for a stated, understood reason (not the right projection). |
| 67 | Quantum q-index | Candidate-only: isolates two auditable inputs for a prime current as a compact-quantum-group coefficient. E67.4: strict free-product Haar orthogonality destroys the arithmetic interference the route needs — a genuine no-go (Woronowicz/free-product), though the q-Gamma archimedean sector survives as reusable, zeta-free input. |
| 68 | GLT/Toeplitz symbol | The terminal defect is shown to be a GLT/pseudodifferential sequence with a 2-variable symbol; `Ω7 ⟺ κ(x,θ)≥0` everywhere. But the position-resolved symbol fails the GLT distribution law numerically (measure{κ<0}~0.4 while ind_-=0) — symbol positivity is gauge-fragile and does not close Ω7. |
| 69 | Exact signed index | Rebuilds the forcer on the gauge-robust *exact* object (not the fragile symbol): `ind_-(A_N-P_λ)=0 ⟺ RH`, verified gauge-uniform and precision-robust. Localizes the terminal difficulty to one frequency (θ~π/2). The forcing mechanism itself remains open; the detector is now solid and gauge-free. |
| 70 | Lee–Yang / de Bruijn–Newman | Positive: connects Ω7 to the classical dBN heat-flow forcing mechanism (RH ⟺ Λ=0, using Rodgers–Tao Λ≥0). Localizes Ω7 to the arithmetic direction Λ≤0 — a genuine forcing mechanism distinct from Hilbert–Pólya and Bost–Connes, not another no-go. |
| 71 | CAND-1 convergence | Positive: confirms CAND-1 is off the Weil-positivity wall (MW-1) — the CCM operators are real by construction (algebra, not RH content); the RH content is entirely in stable-divisor operator convergence `θ_x → k_λ`, reduced to a strong-resolvent estimate. First numerical evidence: 6 primes reproduce the first zero to 10⁻⁵⁵. |
| 72 | Feshbach leakage calculus | Positive: replaces the (too strong) global operator-norm convergence target with a pole-relative Feshbach leakage estimate, then a sharper reduced leakage; proves a leakage theorem that would close the Phase 71 bridge, isolating a genuinely smaller arithmetic estimate to supply. |
| 73 | Cauchy projection gate | Positive: reduces the transformed compact branch to one finite Cauchy–Schur nodal identity, NAT-PROJ, stated purely in terms of a finite Cauchy kernel matrix and the CCM pole-even structure — no analysis left, only a finite algebraic identity to prove. |
| 74 | Hilbert eigenline cancellation | Positive: reduces NAT-PROJ further to an exact finite Hilbert product rule, HPR-DIV, on the projected eigenline — the last open object of the whole ARP-P route at that point. |
| 75 | Arithmetic numerator divisibility | Positive: attacks HPR-DIV via a chain (ARITH-LOCK ⇒ CCM-ROOT-LOCK ⇒ CRIT-NUM-DIV ⇒ CAUCHY-EIG-LOC ⇒ HPR-DIV) using a new signed arithmetic identity; deliberately finite, excludes numerical root-matching and global positivity as proof. |
| 76 | Normalized adjugate arithmetic lock | Positive (autonomous, theorem-grade-audited): corrects the P75 endpoint to the scale-free ratio `A_L=|C_L|²`, then runs ~65 sub-steps of construction and autopsy, closing the route down to one remaining limit-point uniqueness statement (SAFE-LIMIT-POINT) in a directional (not norm) topology — the sharpest endpoint reached, and the direct input to paper 36's Step 5 / Ω7 analysis. |

**Status of the wall (final).** Phases 0–63 mapped the master quantifier with increasing
precision: the kernel N(A) of the averager; the 5 known crossing mechanisms provably collapsing
for the Weil form; the inertia metric carrying ζ by modular structure; culminating in NG-63, the
sharpest concrete statement of the wall (no J-linear gapped Frobenius on the ζ window). Phases
64–76 then did something the earlier phases could not: they built, via the one live candidate off
the positivity wall (CAND-1/CCM operator convergence) and a long chain of finite reductions
(Feshbach leakage, Cauchy projection, Hilbert eigenline cancellation, arithmetic numerator
divisibility, the normalized-adjugate lock), an independently constructed fifteen-step
arithmetic Pick/Nevanlinna architecture (ARP-P, paper 36) that is *proved* equivalent to RH, with
fourteen of its fifteen steps closed. The missing mathematics is no longer described only as "a
cohomology over Spec ℤ that reads inertia, not value" — it is now named precisely: the classical
**Li–Keiper criterion**, $\lambda_n\ge0$ for all $n$ (equivalently the terminal-defect positivity
$\Omega_7$). This is the concrete object the program's abstract "missing cohomology" cashes out
to, reached by an independent construction. It remains, honestly, exactly as hard as RH: the
crossing requires a proof of $\Omega_7$, and every attempt to supply one so far (Phases 64–76)
has returned to one of the structural walls MW-1 through MW-6.

---

*Compiled June 2026; updated 2026-07-17. Covers Phases 3–76. Author: David Alejandro Trejo
Pizzo. No proof of RH; this is a faithful record, including the corrections where the program
corrected itself.*
