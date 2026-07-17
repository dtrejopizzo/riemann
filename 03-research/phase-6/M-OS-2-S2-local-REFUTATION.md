# M-OS-2 / Step S2 — Per-place reflection positivity: COMPUTED and REFUTED (an honest no-go)

**Phase 6, moonshot step S2.** Author: David Alejandro Trejo Pizzo · 2026-06-03.
S2 was to prove **local reflection positivity at each place** (the heart of the Euler-lattice mechanism:
each local factor RP + tensor gluing ⟹ global RP ⟹ RH). I computed the local prime form explicitly. **It is
indefinite.** So per-place RP **fails** for the finite primes, and the naive Euler-lattice mechanism does not
apply. This is a rigorous no-go for the mechanism as stated; it also forces two corrections to S1. Reported
in full, because a clean refutation of an attractive route is worth more than a month of hope.

---

## 1. The local prime form, computed

The prime side of the explicit formula is $W_{\mathrm{prime}}(\phi)=\sum_{p,k\ge1}\frac{\log p}{p^{k/2}}\big[\phi(k\log p)+\phi(-k\log p)\big]$.
Group by prime: the **local form at $p$** is $W_p(\phi)=\sum_{k\ge1}\frac{\log p}{p^{k/2}}[\phi(k\ell_p)+\phi(-k\ell_p)]$,
$\ell_p=\log p$. The associated Hermitian (Weil) form on test functions $\psi$ (with $\widehat\psi(r)=\int\psi(u)e^{iur}du$) is
$$
\langle\psi,\psi\rangle_{W_p}=W_p(\psi*\tilde\psi)=\int_{-\infty}^\infty |\widehat\psi(r)|^2\,G_p(r)\,dr,
\qquad
G_p(r):=2\sum_{k\ge1}\frac{\log p}{p^{k/2}}\cos(kr\log p).
$$

**Closed form.** With $z=e^{ir\log p}/\sqrt p$ ($|z|=p^{-1/2}<1$),
$$
\sum_{k\ge1}\frac{\cos(kr\log p)}{p^{k/2}}=\mathrm{Re}\frac{z}{1-z}=\frac{\mathrm{Re}\,z-|z|^2}{|1-z|^2}=\frac{p^{-1/2}\cos(r\log p)-p^{-1}}{|1-z|^2},
$$
so
$$
\boxed{\ G_p(r)=\frac{2\log p}{p\,|1-z|^2}\Big(\sqrt p\,\cos(r\log p)-1\Big).\ }
$$

> **Proposition S2.1 (the local prime form is indefinite).** $G_p(r)\ge0\iff\cos(r\log p)\ge 1/\sqrt p$.
> Since $\cos$ ranges over $[-1,1]$ and $1/\sqrt p<1$, $G_p$ is **positive** near $r\log p\in2\pi\mathbb Z$ and
> **negative** wherever $\cos(r\log p)<1/\sqrt p$ (a positive-measure set of $r$). Explicitly:
> $$
> G_p(0)=\frac{2\log p}{\sqrt p-1}>0,\qquad G_p\big(\tfrac{\pi}{\log p}\big)=-\frac{2\log p}{\sqrt p+1}<0.
> $$

**Consequence.** The local prime quadratic form $\langle\psi,\psi\rangle_{W_p}=\int|\widehat\psi|^2 G_p$ takes
**both signs** (choose $\widehat\psi$ concentrated where $G_p>0$, or where $G_p<0$). So **each finite-prime
factor is NOT reflection-positive** (nor positive in any sense) — it is genuinely indefinite.

---

## 2. Why this refutes the Euler-lattice mechanism

The mechanism (PLAN §2) was: *each local factor reflection-positive* + *tensor/Markov gluing* ⟹ global RP.
S2.1 kills the first hypothesis for every finite prime. Therefore:

> **No-go S2.2.** The naive Euler-lattice route fails: the local factors at finite primes are individually
> **indefinite**, so global Weil positivity is **not** a tensor product of local positivities. The positivity
> is a **cross-place phenomenon** — the (large, positive) archimedean term $R_\infty$ must dominate the **sum**
> of the indefinite prime forms $\sum_p\langle\cdot\rangle_{W_p}$. This is exactly the cross-place
> cancellation identified in M3 §5 and is *not* a Markov/transfer structure.

This is the same wall, reached from the OS side: positivity = archimedean beats the integrated indefinite
primes = a conspiracy, not a factorization.

**The honest residue (the only possible salvage, and it is Connes' problem).** S2.1 refutes RP of the
*additive* local distribution $W_p$ (the log-derivative). It does **not** refute a deeper RP of the
*multiplicative* local factor $L_p(s)=(1-p^{-s})^{-1}$ read as a **local partition function** (a Bost–Connes
KMS state, whose positivity is structural). But making that precise — and gluing the KMS states across places
— is precisely the Connes–Bost–Connes program. So the OS route, pushed honestly, **reduces to Connes**, with
no new mechanism gained. The pretty $J=$reflection recasting is correct (S1.1) but does not, by itself, supply
the sign.

---

## 3. Corrections forced on S1 (caught here)

1. **S1.1 — reflection is the Weil involution itself (corrected).** The reflection providing OS positivity is
   $\psi\mapsto\tilde\psi=\overline{\psi(-\cdot)}$ *itself* (it carries the conjugation that makes
   $\langle\psi,\psi\rangle_W=W(\psi*\tilde\psi)=\sum_\rho|\widehat\psi(\gamma_\rho)|^2\ge0$). The first draft's
   "second equivalence" applied a *separate* linear $\Theta$ and claimed $\langle\Theta\psi,\psi\rangle_W=\langle\psi,\psi\rangle_W$;
   that is **wrong** — for a separate linear $\Theta$, $\langle\Theta\psi,\psi\rangle_W=\sum_\rho\overline{\widehat\psi(\gamma_\rho)}^{\,2}$,
   a sum of **squares (indefinite)**, not a norm. The correct statement: *Weil's form is already the
   reflection-positive form, with the reflection = the Weil involution.* (Recasting still valid; the bogus
   intermediate step removed.)
2. **S1.4 — the "Hilbert–Pólya for free" payoff is RETRACTED (overclaimed).** The Weil two-point function
   $\widetilde W(u)=\sum_\rho e^{i\gamma_\rho u}$ is **oscillatory** (pure phases, under RH), *not* of the
   reflection-positive **decaying** type $\int e^{-E|u|}d\rho(E)$ that OS reconstruction needs to produce a
   contraction semigroup $e^{-\tau H}$. So OS reconstruction does **not** hand us a self-adjoint $H$ with
   spectrum $\{\gamma_\rho\}$ for free; the time/generator identification is the subtle Connes problem, not an
   OS corollary. The "prize" was illusory.

---

## 4. Honest verdict on the moonshot (after one real step of computation)

| Claim | Status after S2 |
|---|---|
| $J$ = the functional-equation reflection | ✅ true, and a genuine insight |
| Weil's criterion = reflection positivity (for the Weil involution) | ✅ correct recasting (S1.1 corrected) |
| Euler product = reflection-positive lattice (per-place RP + gluing) | ❌ **REFUTED** — local prime forms are indefinite (S2.1) |
| OS reconstruction ⟹ Hilbert–Pólya for free | ❌ **retracted** — oscillatory two-point function, not OS-decaying |
| Net: a new mechanism to force the sign | ❌ no — reduces to cross-place cancellation = Connes' problem |

**Conclusion (no sugar).** The moonshot's *recasting* is correct and elegant, but its two load-bearing
*mechanisms* — per-place reflection positivity and free Hilbert–Pólya reconstruction — **both fail on direct
computation**. The OS route, pushed rigorously, lands back exactly where every route lands: the sign is a
cross-place conspiracy (archimedean vs. the indefinite primes), and the only structural hope is the
Connes–Bost–Connes KMS/partition-function positivity, which is the field's open core, not something our
$J$-reflection insight unlocks. **This is a rigorous no-go for the OS-lattice mechanism, computed, not
guessed.** It is the durable output of attempting the moonshot honestly.

**What survives, what to do.**
- *Survives:* the recasting (Weil = RP for the involution) and the precise reason it does not help (oscillatory
  + indefinite primes). A short, honest note "Why reflection positivity does not localize for $\zeta$" is a
  legitimate small result.
- *To do:* either (i) attack the **multiplicative/KMS** salvage (Bost–Connes — but that *is* Connes, low odds),
  or (ii) accept that the program's durable deliverables (P9 stability; the validated detector; the precise map
  of the wall) are the harvest, and that the sign requires an idea neither we nor the field currently has.

---

### Status
- S2.1 (local prime form indefinite, $G_p$ computed) — ✅ proved.
- No-go S2.2 (Euler-lattice mechanism fails; positivity is cross-place) — ✅ proved.
- S1 corrections (S1.1 reflection; S1.4 retraction) — ✅ logged.
- Salvage (multiplicative/KMS per-place positivity) — ⬜ = Connes/Bost–Connes; low odds; the honest frontier.
