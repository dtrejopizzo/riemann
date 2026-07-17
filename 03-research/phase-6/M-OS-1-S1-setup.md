# M-OS-1 / Step S1 — The Weil form as an Osterwalder–Schrader reflection-positive form (rigorous setup)

> **⚠️ CORRECTIONS (forced by S2, `M-OS-2-S2-local-REFUTATION.md`). Read first.**
> Two claims below were caught wrong when S2 was computed:
> 1. **§2 (S1.1) second equivalence is bogus and removed.** The reflection that makes the form positive is the
>    **Weil involution $\tilde\psi=\overline{\psi(-\cdot)}$ itself** (it carries the conjugation:
>    $\langle\psi,\psi\rangle_W=W(\psi*\tilde\psi)=\sum_\rho|\widehat\psi(\gamma_\rho)|^2$). Applying a
>    *separate linear* $\Theta$ gives $\sum_\rho\overline{\widehat\psi(\gamma_\rho)}^2$ — a sum of **squares
>    (indefinite)**, NOT a norm. So "$\langle\Theta\psi,\psi\rangle_W=\langle\psi,\psi\rangle_W$" is false.
>    Correct recasting: *Weil's form is already the reflection-positive form, reflection = the involution.*
> 2. **§5 (S1.4) "Hilbert–Pólya for free" is RETRACTED.** The two-point function $\widetilde W(u)=\sum_\rho e^{i\gamma_\rho u}$
>    is **oscillatory**, not the reflection-positive **decaying** type OS reconstruction needs; it does NOT
>    yield a self-adjoint $H$ with spectrum $\{\gamma_\rho\}$ for free.
>
> **And S2 REFUTES the mechanism:** the local prime form is $\int|\widehat\psi|^2 G_p$, with
> $G_p(r)=\tfrac{2\log p}{p|1-z|^2}(\sqrt p\cos(r\log p)-1)$ **indefinite** ($G_p(0)>0$, $G_p(\pi/\log p)<0$;
> verified numerically to all digits). So per-place reflection positivity **fails**, the Euler-lattice route
> collapses, and positivity is cross-place (Connes' problem). The recasting (S1.1, corrected) survives; the
> *mechanism and the prize do not.* Keep S1 below for the (correct) recasting and the dictionary only.



**Phase 6, moonshot step S1.** Author: David Alejandro Trejo Pizzo · 2026-06-03.
Plan: `riemann-program/PLAN-RH-MOONSHOT-OS-reflection.md`. Goal of S1: set up, rigorously, the structure in
which **Weil positivity = OS reflection positivity** for the functional-equation reflection, identify the
"time", the reflection, and the form, and state the OS-reconstruction payoff. Honest from the start: S1 is a
faithful **recasting** of Weil's criterion into OS language (which is solid and opens the machinery); the
*content* — proving the positivity — is S2–S3.

---

## 0. OS reflection positivity, in one paragraph

A (Euclidean) reflection-positive structure is: a vector space $\mathcal D$ of "fields", a **reflection**
$\Theta:\mathcal D\to\mathcal D$ with $\Theta^2=\mathrm{id}$, a sesquilinear form $\langle\cdot,\cdot\rangle$,
and a distinguished subspace $\mathcal D_+$ ("positive time") such that
$$
\langle \Theta f, f\rangle\ \ge\ 0\qquad\forall f\in\mathcal D_+ \tag{OS-RP}
$$
together with $\Theta$-invariance of the form and covariance under a "time-translation" semigroup
$T_\tau$. **OS reconstruction:** (OS-RP) yields a Hilbert space $\mathcal H=\mathcal D_+/\mathcal N$
(quotient by the null space of $\langle\Theta\cdot,\cdot\rangle$) on which $T_\tau$ acts as a self-adjoint
contraction semigroup $e^{-\tau H}$, $H=H^*\succeq0$. **The reconstructed $H$ is the prize.**

---

## 1. The dictionary (fields, time, reflection, form)

**Fields.** $\mathcal D:=$ a dense space of test functions $\psi$ on the multiplicative line $\mathbb R_+^*$,
written in the additive (log) variable $u=\log x$, so $\psi=\psi(u)$, $u\in\mathbb R$. (This is the
Weil–Connes test class; the spectral variable is the Mellin/Fourier dual of $u$.)

**Reflection.** The functional equation $s\leftrightarrow 1-s$ acts on $\mathbb R_+^*$ as the **inversion**
$x\leftrightarrow 1/x$, i.e. on the log variable as $u\leftrightarrow -u$. Define
$$
(\Theta\psi)(u):=\overline{\psi(-u)}\qquad(\text{the conjugate-reflection involution }\psi\mapsto\tilde\psi).
$$
This is exactly the involution $\tilde\psi$ appearing in Weil's criterion (Weil 1952; Suzuki, eq. (1.2)).

**Time.** Euclidean time $\tau$ = the additive translation $u\mapsto u+\tau$ (multiplicatively, the
**dilation** $x\mapsto e^{\tau}x$). $\Theta$ reflects time: $\Theta T_\tau=T_{-\tau}\Theta$. **Positive
time** $\mathcal D_+:=\{\psi:\operatorname{supp}\psi\subset[0,\infty)\}$ (i.e. $x\ge1$).

**Form.** The Weil distribution $W$ (the explicit formula read as a distribution: $W(\psi)=\sum_\rho\widehat\psi(\gamma_\rho)$
$=$ archimedean $+$ pole $-$ primes) defines the **Weil Hermitian form**
$$
\langle\psi,\phi\rangle_W:=W(\psi * \tilde\phi),\qquad (\psi*\phi)(u)=\int\psi(v)\phi(u-v)\,dv .
$$

---

## 2. Proposition S1.1 — Weil's criterion IS reflection positivity

> **Proposition S1.1.** $\ \langle\psi,\psi\rangle_W=W(\psi*\tilde\psi)$, and
> $$
> \mathrm{RH}\ \iff\ \langle\psi,\psi\rangle_W\ge0\ \ \forall\psi\in\mathcal D
> \ \iff\ \langle\Theta\psi,\psi\rangle_W\ge0\ \ \forall\psi\in\mathcal D ,
> $$
> i.e. **Weil positivity is reflection positivity for $\Theta$** (the functional-equation reflection),
> *unrestricted in time*.

*Proof.* The first equivalence is Weil's criterion (Weil 1952; Bombieri; Suzuki Thm in §1):
$W(\psi*\tilde\psi)=\sum_\rho|\widehat\psi(\gamma_\rho)|^2$ on-line plus the indefinite off-line quartet
terms, $\ge0\ \forall\psi\iff$ RH. The second is the identity $\langle\Theta\psi,\psi\rangle_W=W((\Theta\psi)*\tilde\psi)$;
since $\widetilde{\Theta\psi}=\overline{(\Theta\psi)(-u)}=\overline{\overline{\psi(u)}}=\psi$, and the
convolution/distribution are bilinear, $\langle\Theta\psi,\psi\rangle_W=W(\Theta\psi*\psi)=\overline{W(\psi*\tilde\psi)}=\langle\psi,\psi\rangle_W$
(real). $\square$

**This is the load-bearing recasting:** Weil's criterion is *literally* a reflection-positivity statement,
because Weil's own involution $\tilde\psi$ *is* the functional-equation reflection $\Theta$. No new
mathematics yet — but the object is now an OS form.

---

## 3. Proposition S1.2 — the Weil distribution is $\Theta$-invariant (the functional equation)

> **Proposition S1.2.** $\ W\circ\Theta=W$ (the form's measure is reflection-invariant): $W(\tilde\psi)=\overline{W(\psi)}$,
> equivalently the zero multiset is symmetric $\{\gamma_\rho\}=\{-\gamma_\rho\}$ and the archimedean$+$pole
> terms are $\Theta$-even.

*Proof.* The completed $\xi(s)=\xi(1-s)$ gives $\{\rho\}=\{1-\rho\}$, hence the spectral points
$\{\gamma_\rho\}$ are symmetric under $\gamma\mapsto-\gamma$ (the $\Theta$ action on the dual variable); the
archimedean factor $\mathrm{Re}\,\psi_\Gamma(\tfrac14+\tfrac{ir}2)$ is even in $r$, and the pole term is
$\Theta$-symmetric. $\square$

**Why this matters for OS.** Reflection invariance of the form/measure is the OS axiom that makes the
**positive-time** reflection positivity equivalent to the full positivity (next), so the OS setup loses no
information.

---

## 4. Lemma S1.3 — positive-time RP is faithful (no loss restricting to $\mathcal D_+$)

> **Lemma S1.3.** Under S1.2 ($\Theta$-invariance), the **positive-time** reflection positivity
> $\langle\Theta f,f\rangle_W\ge0\ \forall f\in\mathcal D_+$ is **equivalent** to the full Weil positivity
> $\langle\psi,\psi\rangle_W\ge0\ \forall\psi\in\mathcal D$. Hence
> $$
> \boxed{\ \mathrm{RH}\ \iff\ \text{(OS-RP): }\ \langle\Theta f,f\rangle_W\ge0\ \ \forall f\in\mathcal D_+ .\ }
> $$

*Proof sketch (standard OS-type, using $\Theta$-invariance).* ($\Leftarrow$ full $\Rightarrow$ positive-time)
is trivial ($\mathcal D_+\subset\mathcal D$). ($\Rightarrow$) Write any $\psi=\psi_++\Theta\psi_-$ with
$\psi_\pm\in\mathcal D_+$ (decompose by support around $u=0$, using $\Theta$ to fold the negative-time part).
By $\Theta$-invariance and bilinearity, $\langle\psi,\psi\rangle_W$ expands into a $2\times2$ block with
diagonal $\langle\Theta\psi_\pm,\psi_\pm\rangle_W\ge0$ (positive-time RP) and off-diagonal terms controlled by
the same RP via Cauchy–Schwarz for the (pre-)inner product $\langle\Theta\cdot,\cdot\rangle_W$ on
$\mathcal D_+$. Positivity of the block follows. $\square$

*(This is the one genuinely-new little lemma in S1: it certifies that the OS positive-time formulation is
faithful — RH is exactly OS-RP, not a weaker shadow. The Cauchy–Schwarz step needs the form to be a genuine
pre-inner product on $\mathcal D_+$, which is the content of positive-time RP itself; the argument is the
standard OS bootstrap and we flag it for a full write-up.)*

---

## 5. The payoff: OS reconstruction $\Rightarrow$ Hilbert–Pólya

> **Theorem S1.4 (conditional, the prize).** *If* (OS-RP) holds (i.e. RH, by S1.3) *and* the remaining OS
> axioms hold for $(\mathcal D,\Theta,T_\tau,W)$ — reflection invariance (S1.2 ✓), time-translation covariance
> of $W$ under the dilation $T_\tau$, and regularity — then OS reconstruction yields:
> $$
> \mathcal H=\mathcal D_+/\mathcal N,\qquad T_\tau\rightsquigarrow e^{-\tau H},\qquad H=H^*\succeq0,
> $$
> a self-adjoint, non-negative generator $H$ whose spectrum is the set of zero-ordinates $\{\gamma_\rho\}$ —
> **the Hilbert–Pólya operator**, with real spectrum, re-proving RH from the constructed self-adjointness.

*Remark (the logic is not circular as a program).* S1.4 reads "RH $\Rightarrow$ Hilbert–Pólya $H$." The
*program* is the converse direction of the machinery: **prove (OS-RP) by the lattice route (S2–S3) without
assuming RH**, then S1.4's reconstruction *delivers* $H$ and hence RH. S1.4 is stated here to fix the payoff
and the covariance/regularity axioms that S2–S3 must respect (in particular, the dilation-covariance of $W$,
which is the scaling structure Connes uses).

---

## 6. Anchors: Connes (the archimedean place) and the validated engine

**Connes–Consani is the archimedean S2.** CC restrict to test functions supported in $(1/2,2)\subset\mathbb R_+^*$;
under $\Theta$ (inversion) this is $(1,2)\leftrightarrow(1/2,1)$ — exactly the **positive/negative-time split
about $u=0$**. CC's archimedean positivity (the Sonin manifest square) is therefore precisely the
**archimedean local reflection positivity** — the $v=\infty$ case of S2. This is not a coincidence: CC's
support condition *is* the OS positive-time window.

**The validated engine tests OS-RP directly.** Our Phase-3 engine computes the localized Weil form on
configurations displaced off the critical line by $\delta$. The displacement $\delta$ breaks the time-zero
($u\!\leftrightarrow\!-u$ symmetric) slice; **the $\delta^2$ forced-negativity curve we measured *is* the
failure of (OS-RP) as one leaves the slice** — i.e. the engine is an (OS-RP) detector. At $\delta=0$ (RH-true
slice) it sits at the floor (RP holds); at $\delta\ne0$ it goes negative (RP fails). So every later step
(S2 per-place, S3 gluing) is numerically falsifiable on this instrument.

---

## 7. Honest status of S1

| Item | Status |
|---|---|
| S1.1 Weil's criterion $=$ reflection positivity for $\Theta$ | ✅ rigorous **recasting** (Weil's $\tilde\psi$ is the reflection) |
| S1.2 $\Theta$-invariance of $W$ (functional equation) | ✅ proved |
| S1.3 positive-time RP $\iff$ full positivity ($=$ RH) | ◆ proved modulo the standard OS bootstrap (Cauchy–Schwarz step flagged) |
| S1.4 OS reconstruction $\Rightarrow$ Hilbert–Pólya | ✅ conditional/standard (fixes the covariance + regularity axioms to respect) |
| The content — **proving** (OS-RP) | ⬜ S2–S3 (per-place RP + adelic gluing) |

**Net.** S1 puts Weil's criterion into the Osterwalder–Schrader frame *faithfully*: RH $\iff$ (OS-RP) for the
functional-equation reflection, with Connes' archimedean positivity sitting exactly at the archimedean place
and our validated engine serving as the (OS-RP) detector. **No new positivity is proved here** — S1 is the
rigorous scaffolding that (i) makes the OS-reconstruction prize precise (a Hilbert–Pólya $H$) and (ii) fixes
the axioms S2–S3 must respect. **Next: S2** — prove local reflection positivity at a finite prime $p$ (the
new, finite-dimensional, Ramanujan-controlled check), with the archimedean case anchored by Connes.

---

### Status / next
- S1.1–S1.2 — ✅. S1.3 — ◆ (OS bootstrap to finish). S1.4 — ✅ conditional.
- **S2 (next, `M-OS-2-S2-local.md`):** per-place reflection positivity; archimedean $=$ CC; finite primes new.
- Engine: the $\delta$-curve is the (OS-RP) detector — use it to stress-test S2/S3.
