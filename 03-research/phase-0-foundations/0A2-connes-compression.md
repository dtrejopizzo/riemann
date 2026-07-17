# Phase 0.A.2 — Is Q a *faithful* compression of the Weil operator?

**Status:** this is no longer just "the Connes dictionary." After the advisor discussion it is the
**central open question of the program**: whether the localized form $Q$ is a faithful
finite-dimensional compression of an operator equivalent to RH, or a useful-but-partial
approximation. ⚑ = requires a specialist in Connes' spectral realization. This draft states the
question precisely and splits it into its two genuinely distinct parts.

> **The reframing (advisor, 2026-06).** The methodological worry "$Q$ may detect artificial
> displacements without capturing the real difficulty of RH" is *equivalent* to the precise
> mathematical question: **is the compression identity $Q=P_J\,\mathcal{T}\,P_J$ correct, in both
> the algebraic and the spectral senses?** This converts a vague concern into a verifiable
> statement — and makes $\mathcal{T}$, not RH, the object under judgment now.

---

## 1. The Connes trace operator (recap)

Connes (1999) realizes the Weil functional as a trace: there is a (regularized) Hilbert space
$\mathcal{H}=L^2_\delta(X)$, $X=\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times$, on which the idèle class
group acts, and a densely defined self-adjoint operator $\mathcal{T}$ whose quadratic form is the
Weil functional $B$. Weil's criterion becomes
$$
\mathrm{RH}\iff B\succeq0\iff \mathcal{T}\succeq0\iff \inf\operatorname{spec}(\mathcal{T})\ge0 .
$$
Our localized $Q(T_0,\sigma,J)$ is the Weil form on the Hermite–Gauss family $\{\varphi_j\}_{j<J}$.

---

## 2. Faithfulness has TWO parts (do not conflate them)

The claim "$Q$ is a faithful compression of $\mathcal{T}$" is really two claims, of different
character and difficulty.

### Part I — the *algebraic* compression identity ⚑
$$
\boxed{\;Q \;=\; P_J\,\mathcal{T}\,P_J\;}\qquad P_J=\text{orth. proj. onto }\operatorname{span}\{U(\varphi_j)\}.
$$
This is a statement about matrix entries: that $B(\varphi_j,\varphi_k)=\langle\varphi_j,\mathcal{T}\varphi_k\rangle_{\mathcal{H}}$.
What must be checked: (a) the $\varphi_j$ lie in the form domain of $\mathcal{T}$; (b) the
regularization $\delta$ is the one for which the explicit formula equals the trace; (c) the sign
convention $M_{\mathrm{zeros}}-M_{\mathrm{arith}}$ matches $\mathcal{T}$. This is laborious but, in
principle, decidable by direct comparison. **Modulo domains, Part I is the "easy" half.**

### Part II — *spectral* faithfulness (no spectral pollution) ⚑⚑
Even granting Part I, the finite compressions need not see the bottom of the spectrum:
$$
\boxed{\;\inf\operatorname{spec}\!\big(P_J\mathcal{T}P_J\big)\ \xrightarrow[J\to\infty]{}\ \inf\operatorname{spec}(\mathcal{T})\;?\;}
$$
This is a **separate analytic question**, and it is where the advisor's sharpest point lands.
By the variational principle $\lambda_{\min}(P_J\mathcal{T}P_J)\ge\inf\operatorname{spec}(\mathcal{T})$
*always* (compression raises the bottom). Convergence from above holds **if** $\mathcal{T}$ is
self-adjoint, bounded below, and the family $\{U(\varphi_j)\}$ is *form-complete* for $\mathcal{T}$.
But:
- $\mathcal{T}$ **bounded below is positivity is (part of) RH** — we cannot assume it;
- the regularization makes even the self-adjoint realization delicate (Connes' hard point);
- generic finite-section schemes exhibit **spectral pollution** — spurious eigenvalues, or
  failure to capture the true infimum — when convergence is merely strong/weak rather than
  norm-resolvent, or when domains are subtle.
So Part II is genuinely open in this setting *precisely because the good behavior of $\mathcal{T}$
is entangled with the conclusion we want.* **Part II is the hard half, and it is the real wall.**

### 2.1 Faithfulness is logically WEAKER than RH (the key refinement)

Part II must be decomposed further, or one over-states where RH lives. Three statements of
*different* logical strength are involved:
- **(II-a)** $\mathcal{T}$ admits a **self-adjoint, bounded-below** realization (bounded below by
  *any* constant, possibly negative). — construction / regularization. **Not RH.**
- **(II-b)** the Hermite–Gauss family $\{U(\varphi_j)\}$ is **form-complete** for $\mathcal{T}$ and
  the bottom-eigenvalue convergence is pollution-free. — spectral approximation. **Not RH.**
- **the value:** $\inf\operatorname{spec}(\mathcal{T})\ge0$. — **this is RH.**

By the min-max principle, the *bottom* eigenvalue is captured from above under (II-a)+(II-b)
alone (spectral pollution lives in essential-spectrum gaps, not below the infimum). Hence
$$
\text{(II-a)}\wedge\text{(II-b)}\ \Longrightarrow\ \lambda_{\min}(Q)\to\inf\operatorname{spec}(\mathcal{T})
\ \text{ faithfully, \emph{whatever the sign}.}
$$
**Faithfulness does not require positivity.** RH does not live in the faithfulness; it lives in
the *sign* of the faithfully-computed infimum. If (II-a)+(II-b) held, the program would deliver a
genuine new object — a *faithful spectral reformulation*:
$$
\boxed{\ \text{RH}\iff \operatorname{sign}\Big(\inf_{T_0,\sigma}\lim_{J}\lambda_{\min}\big(Q(T_0,\sigma,J)\big)\Big)\ge0\ }
$$
RH as the sign of a limit of *computable* eigenvalues.

### 2.2 The entanglement question (the real, expert-answerable target) ⚑⚑

Where, then, is the danger the advisor identified? Not in faithfulness per se, but in a possible
**entanglement**: the regularization that yields (II-a) might itself require positivity. The
sharpest achievable target — and the precise question for a specialist — is therefore *not*
"prove $\inf\operatorname{spec}\ge0$" (that is RH, hopeless directly) but:

> **Can the self-adjoint, bounded-below realization (II-a) and the form-completeness (II-b) be
> established WITHOUT assuming positivity (RH)?**
> - **Yes** ⟹ faithful spectral reformulation above; RH becomes the sign of a convergent
>   computable quantity. A real new handle, RH-independent.
> - **No** (entanglement unbreakable; the construction needs positivity) ⟹ Part II genuinely
>   *is* where RH hides, in its strongest form.

This converts "Part II is hard" into a decidable yes/no. The highest-value theoretical goal of
the whole program is now to **break the entanglement** — establish (II-a)+(II-b) unconditionally
— not to prove positivity.

### 2.3 Consequence for v9
A clean uniform-in-$T_0$ signal (H1) is consistent with (II-b) *on the GRH controls* but says
nothing about (II-a) or the entanglement. So even a perfect v9 leaves the decisive core
untouched; the entanglement question is pure theory for the expert hand-off.

### 2.4 v9 verdict (delivered) — the falsifier did not fire
Lise Science run 9 ran the stability probe. Outcome, calibrated against the logic above:
- **H1 (uniformity in $T_0$): supported.** In the resolved regime ($\sigma\ge1$ with adequate
  prime cutoff), $\lambda_{\min}(Q(T_0,\sigma,J))$ collapses to the numerical floor as $J$ grows,
  and $\sup_{T_0}|\lambda_{\min}(J)-\lambda_\infty|\to$ floor ($\sim10^{-12}$ at $\sigma=1$,
  $<3.5\times10^{-14}$ at $\sigma=2$). **The sharpest empirical falsifier of faithfulness did NOT
  fire.** By the one-way implication (§3), this is *evidence for, not proof of*, faithfulness.
- **H2 (monotonicity): supported, and the Conrey–Li obstruction is ABSENT.** $\lambda_{\min}$ is
  non-decreasing in $\sigma$ and under nested windows, saturating at the floor, across all three
  GRH controls, with no de Branges/Conrey–Li dip. This *re-weights the de Branges flank upward*.
- **Small-$\sigma$ negativity is truncation, not pollution.** At $\sigma=0.5$, $\lambda_{\min}$
  grows *more* negative as the prime cutoff $X$ rises — the opposite of spectral structure — so the
  localization is **not injecting spurious geometry**. This is genuine evidence *against* Scenario 2
  in the tested regime (both finite-$X$ and finite-$J$ artifact channels were probed and both are
  benign once resolved).

**What v9 did NOT do (the line held):** it tested the GRH controls, where $\lambda_{\min}\approx0$
trivially — the *weak confirmer* case of §2.2. It did **not** touch the **entanglement question**
(II-a), did not test the off-line amplification (the sharp Part-II probe), and does not move the
probability of RH (R7). Both scenarios remain open; Scenario 1 (faithful) is strengthened, Scenario
2 (localized-scheme artifact) is pushed against but not excluded. **The entanglement question is now
the entire game, and it is pure theory — the Phase 4 hand-off.**

---

## 3. The implication is one-way (the corrected logic)

Combining, and writing **(0A2)** for "Part I and Part II both hold":
$$
\boxed{\;(0A2)\ \Longrightarrow\ \text{H1 (uniform }J\text{-stability of }\lambda_{\min}\text{)}\;}
\qquad\text{but}\qquad
\boxed{\;\text{H1 observed}\ \not\Longrightarrow\ (0A2)\;}
$$
- **Forward:** if the compression is faithful (I) and pollution-free (II), then
  $\lambda_{\min}(Q)\to\inf\operatorname{spec}(\mathcal{T})$, and uniformity in $T_0$ is expected.
- **No converse:** many compression schemes converge cleanly on test cases yet fail spectral
  faithfulness in the limit (this *is* spectral pollution). So a clean H1 on the GRH controls is
  **evidence for**, not **proof of**, (0A2). The reverse direction needs theory, not numerics.

Logic, in one diagram:
```
        0A2 correct
             │  (⟹)
             ▼
        H1 expected
                          H1 observed ──(⇏)──►  0A2 proved
```

---

## 4. What H1 (uniformity in T₀) actually tests — and what it doesn't

The decisive curve from the v9 probe is **not** $\lambda_J\to\lambda_\infty$ but
$$
\sup_{T_0}\bigl|\lambda_J(T_0)-\lambda_\infty(T_0)\bigr|\ \xrightarrow{?}\ 0 .
$$
Reason (advisor): the real danger of localization is not losing *local* information but losing
*global* information **in a center-dependent way**. If $\sup_{T_0}|\lambda_J-\lambda_\infty|\not\to0$,
that is strong evidence the localization injects an artificial, center-dependent geometry — i.e.
a direct strike against Part I/II faithfulness. Conversely, clean uniform decay is the *best
empirical signal available* that the local object is approximating a genuine global one. It does
not certify Part II (pollution can hide in the limit), but its **failure** would be near-decisive
against faithfulness. So H1 is a powerful *falsifier*, a weak *confirmer*.

---

## 5. The wall, stated correctly

The earlier slogan "the wall is RH" must be conditioned:
$$
\boxed{\;\text{the wall}=\text{RH}\quad\text{if and only if (0A2) holds (Parts I and II).}\;}
$$
Two honest scenarios:
- **Scenario 1 — (0A2) correct.** $Q$ is the faithful localized avatar of Weil; the program has
  reached the genuine obstacle; the named inequality (LB) *is* RH. The remaining task is the
  structural positivity (Connes/de Branges).
- **Scenario 2 — (0A2) fails subtly** (Part II / spectral pollution). The wall is a wall of the
  localized scheme, not of RH. The detector P7 remains a correct, publishable result about $Q$,
  but the bridge to RH is partial.

Deciding between these scenarios is now **the most important mathematical question of the
program** — more important than H1 or H2 in isolation, since it determines whether everything
downstream studies a faithful avatar of Weil's criterion or a useful approximation.

The revised central chain:
```
  P7 (rigorous detector)
        │
        ▼
  0A2 :  is Q a faithful compression of  𝒯 ?   ◄── the box under judgment
        │   (Part I algebraic ⚑ ; Part II spectral / pollution ⚑⚑)
        ▼
  (LB) :  inf spec(𝒯) ≥ 0
        │   (iff 0A2 holds)
        ▼
  RH
```

---

## 6. The hand-off, split by part

1. **Part I (algebraic) ⚑** — an expert in \[Connes99\] verifies $Q=P_J\mathcal{T}P_J$: form
   domain of $\mathcal{T}$, the regularization $\delta$, the sign. *Laborious but decidable.*
2. **Part II (spectral) ⚑⚑** — frame it as §2.2's **entanglement question**, not as "prove
   positivity": can the self-adjoint, bounded-below realization (II-a) and the form-completeness
   of $\{U(\varphi_j)\}$ (II-b) be established **without assuming RH**? A *yes* gives a faithful
   spectral reformulation (RH = sign of a computable limit); a *no* locates RH's difficulty here.
   This — not positivity — is the precise, RH-independent target for the operator theorist.
3. **Numerics (v9)** — treat the uniformity-in-$T_0$ curve as a *falsifier* of faithfulness:
   clean uniform decay keeps both scenarios open (Part II still to be settled theoretically);
   center-dependent blow-up is strong evidence for Scenario 2.

**References to pin.** A. Connes (1999); E. Bombieri, *Remarks on Weil's quadratic functional*;
A. Connes & C. Consani, *Riemann–Roch for $\mathbb{Z}$* (2024); on spectral pollution and
finite-section spectra: A. C. Hansen, *On the approximation of spectra of linear operators*
(2008); M. Lewin & É. Séré, *Spectral pollution and how to avoid it* (2010); E. B. Davies &
M. Plum, *Spectral pollution* (2004).
