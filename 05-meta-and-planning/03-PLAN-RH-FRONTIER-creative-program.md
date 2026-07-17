# PLAN — RH Creative Frontier: mixing the Connes program with new, falsifiable, ambitious ideas

**Author:** David Alejandro Trejo Pizzo · **Opened:** 2026-06-03 · **Status:** the forward program after
M1–M3 closed the identification phase of Route B.

This continues `PLAN-RH-ROUTE-B-structural-positivity.md`. M1–M3 (`phase-5-structural/`) established the
honest map: the **only** zero-free, unobstructed structural attack surface is the **Connes–Consani
semi-local residual**, and the sign — if it exists — lives in **cross-place cancellation** (archimedean
manifest square vs. prime negativity), i.e. a *global* square over the adèle class space (Connes' geometric
program). de Branges and the P8 zero-side are spent.

**The thesis of this plan.** Pure frontier-chasing (re-deriving Connes) yields diminishing returns; pure
new-idea speculation is crankery. The science is in the **mix** — and we have one combination **no one else
has**: a *computable, semi-local, localized* Weil-form engine (**P7**) and an *explicit RH-violator*
(**$L_{\mathrm{DH}}$**, from P3), together with the **Kreĭn/angular** picture (P8) and the **Connes residual**
target (M1–M3). We use these to attack the frontier from an angle the modern literature has not: **compare
the residual operator across L-functions to isolate the arithmetic invariant that forces positivity.**

---

## 0. The single organizing question (sharper than "prove RH")

> **What property of the arithmetic (the Euler product / functional equation) makes the semi-local residual
> operator $K$ satisfy $\|K\|\le1$ for $\zeta$, while $\|K\|>1$ for an RH-violating L-function?**

This is well-posed, falsifiable, and *new*: the Connes program studies $\zeta$ in isolation; it never
contrasts the residual of an RH-true vs an RH-false L-function, because it has no explicit violator to hand.
**We do** ($L_{\mathrm{DH}}$, P3). Isolating that invariant is (i) a genuine structural result even short of
RH, and (ii) the most plausible route to a *sufficient condition* for the sign.

---

## 1. Four ambitious directions (ranked; each falsifiable, honest prior)

### α — The semi-local spectral flow (operative, do first)
**Idea.** P7's localized Gram matrix $Q=M_{\text{zeros}}-M_{\text{arith}}$ is *already semi-local* (it carries
the prime sum). Recast it in the **Slepian prolate basis** (matched to Connes' Sonin geometry, M3 Obs
B2.2-(b)). Study the top eigenvalue of the residual $\mathrm{Id}-K$ (equivalently $\lambda_{\min}(Q)$, which
P7 already computes) as a function of: (i) the **prime cutoff** $X$, (ii) the **localization height** $T_0$,
(iii) the **time–band product** $c$.
**Question.** Does the data show the residual structurally *hugging* $\le1$ (the primes "cooperate") or
robustly trying to exceed it? Does adding primes push the top eigenvalue toward or away from $1$ — is there a
**monotone spectral flow**?
**Falsifiable / outcomes.** A clean monotone flow toward $\le1$ = strong structural evidence (and a precise
conjecture); an anomaly = a numerical no-go signal worth chasing; flat = consistency.
**Prior:** high value as structure, ~0% RH. **Uses:** P7 engine directly.

### δ — The discriminant: $\zeta$ vs the RH-violator (new, our unique asset)
**Idea.** Run α for **both** $\zeta$ and $L_{\mathrm{DH}}$ (known off-line zeros, $\lambda_{\min}\approx-9\times10^4$
in P7). For $\zeta$ the residual should have $\|K\|\le1$ on the relevant conditioned subspace; for
$L_{\mathrm{DH}}$ it must exceed $1$ (an off-line zero forces it, P7's forced-negativity theorem). **Compare
the two residual operators term by term** and isolate *which* arithmetic feature flips the sign: the Euler
product (multiplicativity), the conductor/$\Gamma$-factor (archimedean square geometry), or the
coefficient architecture (P4's entropy/parity discriminant, now at operator level).
**Falsifiable / outcomes.** An explicit operator-theoretic invariant separating RH-true from RH-false
L-functions = a genuinely new **necessary** (possibly sufficient) condition. Even a partial separation is
publishable and frontier-relevant.
**Prior:** moderate for a real discriminant, low-but-nonzero for a sufficient condition. **Uses:** P3 + P4 +
P7. **This is the most novel direction and the one the modern literature structurally cannot do.**

### β — Sine-kernel / GUE identification of the residual (frontier bridge)
**Idea.** Connes' Sonin/prolate spectrum and the **Dyson sine kernel** (GUE local statistics; Montgomery–
Odlyzko zero correlations) are both governed by prolate/band-limiting operators. Conjecture: the CC residual
$K_{\mathrm{CC}}$, in the appropriate scaling limit, is the **sine-kernel (Dyson) operator**, so its
eigenvalue-near-$1$ structure is the GUE gap structure. CC themselves invoke an "emission/absorption
spectrum" picture (their §0, ref. to Berry–Keating) — the absorption spectrum removed leaves the zeros.
**Falsifiable.** Compute $\mathrm{spec}(K)$ (from α) and compare to sine-kernel eigenvalues at matched $c$.
**Outcomes.** A match ties Weil positivity to **GUE universality** — a real frontier bridge (not RH); a
mismatch sharpens what is *not* sine-kernel about the residual.
**Prior:** decent for a partial match. **Uses:** α output + classical random-matrix spectra.

### γ — The global square: GNS/Stinespring over the adèle class algebra (terminal, the dream)
**Idea.** Cross-place positivity ($\sum_v W_v\le0$) is the statement that the Weil functional is a **positive
state** on the right convolution algebra (Bost–Connes / adèle class). Seek the **GNS representation**
$\mathfrak t(g)=\langle\Omega,\pi(g)^*\pi(g)\Omega\rangle$ that *is* the global square $\mathcal T=A^*A$, with
$A=\pi(\cdot)\Omega$. The obstruction (or its absence) is whether $\mathfrak t$ is positive-definite on that
algebra — RH — but the GNS framing may expose a natural completion / a completely-positive-map structure that
makes cross-place cancellation manifest. This is Connes' geometric bet, recast operator-algebraically.
**Prior:** $<1\%$ for RH; but it is *the* terminal target and frames everything else. **Uses:** the whole
program; beyond a bounded milestone — kept as the north star, attacked only if α/δ/β surface a handle.

---

## 2. The one combined first experiment (touches α, β, δ at once — maximal information per unit effort)

**Build the Slepian-prolate localized residual spectrum, for $\zeta$ and for $L_{\mathrm{DH}}$, and read off
three things at once.** Concretely, using and extending the P7 engine:

1. **Basis.** Replace P7's Hermite–Gauss test functions by the exact **Slepian prolate spheroidal functions**
   $\psi_n^{(c)}$ at time–band product $c$, centered at height $T_0$. *(Hermite–Gauss is the $c\to0$ limit;
   prolates are the $\Lambda=1$-matched basis to Connes' Sonin geometry, M3.)*
2. **Operator.** Assemble the localized Weil Gram $Q^{(c,T_0,X)}=M_{\text{zeros}}-M_{\text{arith}}$ in this
   basis (semi-local: prime cutoff $X$), for both $\zeta$ and $L_{\mathrm{DH}}$. The angular/residual operator
   is read from the Kreĭn split (P8 §7) of $Q$.
3. **Read-outs.**
   - **(α)** $\lambda_{\min}(Q)$ / top eigenvalue of $K$ vs $(X,T_0,c)$ → the spectral flow; monotone toward
     $\le1$?
   - **(δ)** $\zeta$ vs $L_{\mathrm{DH}}$: where exactly does the violator's spectrum cross $1$, and which
     matrix entries (which primes / which archimedean block) carry the difference → the discriminant.
   - **(β)** the full $\mathrm{spec}(K)$ vs sine-kernel eigenvalues at matched $c$ → GUE bridge.

**Deliverables (any of which is a result):** a sharper semi-local residual estimate; an explicit
RH-true/false operator discriminant; a sine-kernel identification (or its falsification); or a clean no-go.
**What it is not:** a proof of RH. By the P8 magnitude-vs-sign lesson, a numerical $\|K\|\le1$ for $\zeta$ is
evidence and structure, never the sign.

**Engine.** Extend `06-papers/P7-localized-weil-detector/` (its explicit-formula + Gram + $\lambda_{\min}$
machinery already exists; add the prolate basis and the $L_{\mathrm{DH}}$ data from P3). Output folder:
`phase-5-structural/experiments/`.

---

## 3. Guardrails (unchanged, hard-won)

- **Zero-independence (B0):** every admissible positive structure must be writable without assuming RH.
- **Magnitude ≠ sign:** a numerical/analytic bound $\|K\|\le1$ for $\zeta$ is magnitude/evidence; the sign is
  RH. Never present a sharper estimate as the proof.
- **Audit before pillarizing; retraction is cheap, false victory is expensive.** The panel sees every claim.
- **Honest priors up front.** RH from any of these: $<1\%$. Real structural results: plausible. That asymmetry
  is the point — we are mining the frontier for durable structure, with RH as the north star, not the
  deliverable.

---

## 4. Milestones

1. **M4 (α+δ+β combined experiment):** the Slepian-prolate localized residual spectrum for $\zeta$ and
   $L_{\mathrm{DH}}$; the spectral flow, the discriminant, the sine-kernel comparison.
   → `phase-5-structural/experiments/M4-prolate-residual-spectrum.md` (+ code).
2. **M5 (δ deepened):** if a discriminant appears, formalize the arithmetic invariant (Euler-product vs
   $\Gamma$-factor vs coefficient-architecture) separating RH-true/false residuals.
3. **M6 (β/γ):** if the sine-kernel match lands, pursue the GUE/Connes-emission bridge; otherwise probe γ
   (GNS/global-square) for a handle surfaced by M4–M5.
4. **Each milestone** → `00-MAP.md`, the proof log, project memory. Share with the panel immediately.

**One-line framing for the panel.** *Having mapped where the advance is not (P8 zero-side, de Branges) and
where the only zero-free surface is (the Connes semi-local residual), we now mix that frontier with an asset
the literature lacks — a computable semi-local localized Weil engine and an explicit RH-violator — to ask the
sharper, falsifiable question: which arithmetic invariant forces the residual operator's norm below 1 for
$\zeta$ but not for an RH-false L-function? The first experiment reads the spectral flow, the RH-true/false
discriminant, and a possible GUE/sine-kernel identification simultaneously. Honest prior: durable structure,
not RH — with the global adèle-class square as the declared north star.*
