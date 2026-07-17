# B2 / M3 — The semi-local Connes residual, and the $PW_d$ ↔ prolate question (real or superficial?)

**Route B, Milestone M3 (the priority front after M1).** Author: David Alejandro Trejo Pizzo · 2026-06-03.
References: Connes–Consani arXiv:2006.13771 (§§4–6, Thms 1, 3, 6.11); Slepian–Pollak–Landau (prolate
spheroidal wave functions); P7 (`06-papers/P7-localized-weil-detector/`); P8.

**Two questions (B2.1, B2.2).**
1. **(B2.1)** Is $\mathrm{Id}-K_{\mathrm{CC}}\succeq0$ in the **semi-local** case (archimedean + all finite
   primes), where the analogue of Connes–Consani's archimedean theorem is *open* and $\iff$ RH?
2. **(B2.2)** Is the coincidence "**prolate** spheroidal functions appear in both CC and in band-limited
   ($PW_d$) analysis" a *real* technical bridge, or *superficial*?

**Answers, up front.**
- **(B2.2) Superficial for P8/global; real for P7/localized.** CC's prolates come from a *time-and-band*
  cutoff at the *fixed* archimedean scale $\Lambda=1$; P8's $PW_d$ is *band-only* at a *free* scale $d$, with
  no time-limit. The structures do **not** align (§2). But the **localized** detector P7 (Hermite–Gauss,
  time-and-band concentrated) is the natural $PW$-side partner of CC's prolates (§3). So the prolate bridge
  exists — to P7, not P8.
- **(B2.1) The semi-local residual positivity is exactly the open RH-frontier**, and the band-limited/prolate
  tools can at best **sharpen the estimate** of $\|K_{\mathrm{CC}}\|$, not establish $\le1$. By P8's
  magnitude-vs-sign lesson, an estimate sharpening that does not cross below $1$ is a *magnitude* result, not
  the sign (§4). The genuine open content is **cross-place cancellation** (archimedean square vs. prime
  negativity), which is Connes' actual hope and the real frontier (§5).

---

## 1. The semi-local residual, precisely

At the **single archimedean place** (test support $\subset(1/2,2)$, no primes), Connes–Consani **prove**
$$
W_\infty(g*g^*)\ \ge\ \underbrace{\mathrm{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)}_{\text{manifest square}}-\,c|\widehat g(0)|^2,\qquad 13<c<17\ \ (\text{Thm 6.11}),
$$
and the residual $E\circ Q\sim-2\epsilon'(1^+)(\mathrm{Id}-K_{\mathrm{CC}})$ is *controlled* — the archimedean
wall is solved. RH is the **semi-local** statement (Connes–Consani eq. (2)):
$$
\mathrm{RH}\iff \sum_v W_v(g*g^*)\le 0\quad\text{for } g\in C_c^\infty(\mathbf R_+^*),\ \widehat g\text{ vanishing on a finite set,}
$$
the sum over all places $v$ (archimedean + primes $p\le$ support bound). Including the finite primes adds the
local terms $W_p$; the manifest-square structure (Sonin trace) and the residual operator $K$ are claimed by
CC to "make sense in the general semi-local case," but **the semi-local $\mathrm{Id}-K\succeq0$ is not
proven** — that is RH. So:
$$
\boxed{\ \text{B2.1 target: }\ \mathrm{Id}-K_{\mathrm{CC}}^{\,\text{semi-local}}\ \succeq\ 0\ \iff\ \mathrm{RH}\ (\text{open}).\ }
$$

---

## 2. Why the $PW_d$ ↔ prolate coincidence is superficial (for P8/global)

**CC's prolates.** They arise from the pair of projections $\mathcal P_\Lambda$ (cutoff in the variable) and
$\widehat{\mathcal P}_\Lambda$ (cutoff in the dual variable) at $\Lambda=1$ — a **simultaneous time-and-band
limiting** at one fixed scale. The eigenfunctions of $\mathcal P_\Lambda\widehat{\mathcal P}_\Lambda$ are the
**Slepian prolate spheroidal wave functions**, with eigenvalues $\lambda_n\in(0,1)$; Sonin's space is the
$\lambda_n\to$ tail (orthogonal complement of the cutoff range). The scale $\Lambda=1$ is **fixed by the
archimedean conductor**, not free.

**P8's $PW_d$.** Band-limit $d$ **only** (functions on all of $\mathbb R$, no time-limit); $d$ is the
**free** test-function support parameter ($d>\tfrac12$). The relevant operator is the band-limiting alone;
its "prolates" would require *also* a time-limit, which P8 does not impose.

> **Conclusion B2.2-(a).** The two "prolate" appearances are **not the same structure**: CC = time∧band at
> fixed $\Lambda=1$; P8 = band-only at free $d$. The shared word "prolate" reflects only that band-limited
> harmonic analysis is universal here. A direct $PW_d$-native sharpening of $K_{\mathrm{CC}}$ via P8 is
> **not** available. *(This is itself a small no-go, in the P8-Thm-C spirit: the global band-limited
> structure does not align with the archimedean time-band cutoff.)*

---

## 3. The real bridge: CC prolates ↔ the localized detector P7

The natural $PW$-side partner of CC's time-and-band cutoff is **not** the global P8 but the **localized**
construction P7:
- **P7** uses **Hermite–Gauss** test functions centered at height $T_0$ with width $\sigma$ — *simultaneously
  concentrated in time and frequency* (a Gaussian is the ground state of the harmonic oscillator, i.e. the
  $c\to0$ limit of the prolate spheroidal functions). P7's localized Weil form $Q=M_{\text{zeros}}-M_{\text{arith}}$
  is exactly a *finite, time-band-limited* Gram matrix of the Weil functional.
- This is structurally the **same kind of object** as CC's $\vartheta(g)\mathbf S\vartheta(g)^*$ restricted to
  a finite-dimensional prolate subspace.

> **Observation B2.2-(b) (the useful redirection).** If the prolate connection is to be exploited, the
> $PW$-side object to use is the **localized P7 Gram matrix**, not the global P8 operator. Concretely: replace
> P7's Hermite–Gauss basis by the **exact Slepian prolate basis** at a matched time-band product, and compare
> the resulting finite Gram matrix to CC's compression $\mathbf S\vartheta(g)$. This is a concrete,
> computable experiment (finite-dimensional linear algebra + the explicit formula, exactly P7's engine).

This ties the program's two rigorous artifacts — P7 (localized detector) and the CC residual — through the
prolate basis, and is the one **operative** sub-task this milestone surfaces.

---

## 4. The magnitude-vs-sign trap, reapplied (the honest limit)

Even granting the P7↔CC prolate bridge, what could it deliver? CC's archimedean argument **estimates**
$\|K_{\mathrm{CC}}\|$ via Toeplitz/prolate spectral analysis and **lowers the top eigenvalue below 1** by
conditioning. In the **semi-local** case the same estimation could be attempted with the prime terms included.
But:

> **Caution B2.1-(c) (P8 lesson reapplied).** Sharpening the *estimate* of $\|K_{\mathrm{CC}}^{\text{semi-local}}\|$
> is a **magnitude** result. It yields RH **only if** it crosses below $1$ uniformly — and proving
> $\|K\|\le1$ semi-locally *is* RH. A bound that stays $\ge1$, or holds only on a finite-codimension
> subspace, is the same kind of B-2/magnitude progress P8 already mapped: useful, publishable as an estimate,
> **not the sign.** Do not mistake a sharper residual bound for the proof.

So the prolate/localized route is, at best, a path to a **sharper semi-local residual estimate** (a real
contribution) and, at worst, a **no-go** showing the estimate cannot cross $1$ by these means. Both are
results; neither is RH.

---

## 5. Where the genuine open content is: cross-place cancellation

The one place where the sign could genuinely appear — and where Connes' program actually bets — is
**cross-place cancellation**:
$$
\sum_v W_v(g*g^*)\le0 :\quad \text{the archimedean manifest square + the prime terms must combine to a sign},
$$
not place-by-place (place-by-place fails: the primes contribute negatively). The hope is a **global semi-local
positivity** invisible to any single place — exactly the structure that a square $\mathcal T=A^*A$ over the
*whole* adèle class space would provide (Connes' geometric program, the Frobenius correspondence / divisor on
the square of the Scaling Site). This is:
- **beyond** what the band-limited / prolate estimates can see (they are single-place / local);
- the **actual** RH frontier; and
- **not** obstructed by the P8 no-go (it is fully zero-independent, by construction).

> **Routing B2 → (future).** The operative, bounded sub-task is Observation B2.2-(b): the **P7-prolate vs CC
> compression** finite-dimensional experiment, expecting a sharper *estimate* or a *no-go*. The deep frontier
> (cross-place semi-local positivity) is the Connes geometric program itself and is beyond a bounded
> milestone — we flag it as the terminal target, with eyes open.

**Net for the panel.** *The semi-local Connes residual positivity is exactly the open RH-frontier; the
band-limited ($PW_d$) structure of P8 does not align with CC's archimedean time-band prolate cutoff (a small
no-go), but the localized detector P7 (Hermite–Gauss → Slepian prolates) is its natural partner and gives a
concrete finite-dimensional experiment (P7-prolate Gram vs. CC compression). By the P8 magnitude-vs-sign
lesson, that experiment can at most sharpen the residual estimate or produce a further no-go, not the sign.
The sign, if it exists, lives in cross-place (semi-local) cancellation — Connes' geometric program — which is
zero-independent (hence unobstructed by P8) but beyond a bounded milestone.*

---

### Status
- §1 (semi-local residual = open RH-frontier) — ✅ faithfully from CC (eq. 2, Thms 1, 3, 6.11).
- §2 (B2.2-(a): $PW_d$ vs CC prolate **superficial**) — ✅ argued (different cutoffs); a small no-go.
- §3 (B2.2-(b): P7 ↔ CC prolate **real**) — ◆ the operative redirection; concrete finite experiment proposed.
- §4 (magnitude-vs-sign caution) — ✅ P8 lesson reapplied; bounds the upside honestly.
- §5 (cross-place cancellation = the true frontier) — ⬜ Connes geometric program; terminal target.

*Next operative sub-task (if pursued): build the Slepian-prolate localized Gram matrix (P7 engine) and
compare to the CC Sonin compression — expect a sharper estimate or a no-go. Records to update: this folder,
`00-MAP.md`, the proof log.*
