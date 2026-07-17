# Phase 15 — Synthesis (M1 → M3), the precise gap, and paths for the team

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
A self-contained account of the Anatomy–Kreĭn–Hodge program from M1 to Attempt 8, the exact missing object, and
concrete routes to unblock it. Written for independent verification and for proposing a path.

---

## Part A — What we built and proved (M1–M2, unconditional, verified)

**The goal.** Transcribe Weil's function-field proof of RH to $\operatorname{Spec}\mathbb Z$: build an
intersection pairing whose signature is RH, with the *anatomy* (P19) as the arithmetic Frobenius, the *Kreĭn form*
(P16) as the pairing, and *Hodge–Riemann stability* (P20) as the definiteness criterion. Weil's proof is
**(intersection form) + (Hodge index = definiteness on the primitive part)**.

**M1 — the arithmetic intersection pairing.** *(Proved + verified to $10^{-12}$.)*
- Pairing $\langle f,g\rangle=\sum_\rho\widehat f(\gamma_\rho)\overline{\widehat g(\gamma_\rho)}$ on test
  functions, completing to a Kreĭn space; negative index $\kappa=\#$off-line zeros.
- **Theorem A (Lefschetz trace identity):** the pairing $=$ poles $-2\sum_n\tfrac{\Lambda(n)}{\sqrt n}g(\log n)+$
  archimedean — the explicit formula as a sum of local intersection numbers (places of $\mathbb Q$). The primes are
  the Frobenius, the poles are $H^0\oplus H^2$, the archimedean is the place at $\infty$.
- **Theorem B (effectivity $\Gamma\cdot\Gamma\ge0$):** the Frobenius self-intersection $=\int_{-2d}^{2d}|S|^2\ge0$
  $=\sum_p\sum_k|s_k(p)|^2$ (Rankin–Selberg square; $s_k$ are the anatomy power sums). The analogue of
  "effective cycles have $\ge0$ self-intersection."
- **Proposition C:** RH $\iff$ the pairing is $\succeq0$ on the primitive part $\Pi^\perp$ — **the arithmetic
  Hodge index**.

**M2 — the ample cone.** *(Proved + verified.)*
- **Theorem:** the trivial/pole part is $2\bigl(\int f e^{-u/2}\bigr)^2\ge0$ — the **ample cone is positive,
  unconditionally**; it is the de la Vallée Poussin / Landau edge positivity, and the analogue of the fiber classes
  $f_1,f_2$ spanning the hyperbolic plane, with $f_1+f_2$ ample.

So **M1 + M2 = the full Weil scaffold for $\operatorname{Spec}\mathbb Z$**, all proved: the pairing, the trace
identity, the effectivity, the ample cone. RH reduces — by an equivalence — to **M3 = the arithmetic Hodge index**.

## Part B — M3 is RH, and the three faces (proved equal)

**M3 = RH:** positivity of the pairing on the primitive part. We proved it has three equivalent faces:
\[
\underbrace{\text{signature on }\Pi^\perp\succeq0}_{\text{geometry (Weil)}}
\iff\underbrace{\text{uniform form factor }F(\alpha)\ll1}_{\text{analysis (Montgomery/P18)}}
\iff\underbrace{\text{strictly-definite HR limit }\delta_\infty>0}_{\text{positivity (HR-stability)}}\iff\RH.
\]
We also obtained the **first partial arithmetic Hodge index** (unconditional): semibounded modulo a $\log$, and
clean off a super-polynomially sparse set of extreme-value heights (from P18).

## Part C — The eight attempts on M3, and what each proved

1. **$2\times2$ Hodge determinant.** RH $=$ reverse Cauchy–Schwarz $a^2>2\lambda^2V$ ($a=\langle H,\Gamma\rangle$).
   Lands on the core.
2. **Bochner positivity.** The sine kernel is positive-definite $\Rightarrow V\ge0$ (lower bound) only; the upper
   bound needs a zero-diagonal positive-definite kernel — impossible. The one-sidedness is structural.
3. **dBN flow.** Relaxation gives a lower bound (wrong direction); N5 (arithmetic-blindness) forbids the flip.
4. **Symmetric-power tower.** Controls the Satake (Ramanujan, local axis), not the archimedean zeros.
5. **The arithmetic Hodge index *exists*.** Faltings–Hriljac (1984), Yuan–Zhang (2017): a *proven* general
   arithmetic Hodge index. So the missing piece is **not a theorem**.
6. **Elliptic control ($E/\mathbb Q$).** Where the surface exists, the proven Hodge index controls **heights**
   (Néron–Tate $\Rightarrow$ special values, BSD), **not** the critical-line zeros (GRH). The proven theorem is on
   the **wrong cohomology**: the Arakelov $\widehat{\mathrm{Pic}}^0$ (heights), not the zero-carrying $H^1$.
7. **Built the zero-carrying cohomology.** Explicitly: the Kreĭn space $\mathcal H_W$, the flow $\mathcal T$ with
   $\operatorname{spec}(\mathcal T)=\{\gamma_\rho\}$, the Lefschetz trace formula, the anatomy as local Frobenius,
   the ample cone, and a candidate weight-$1$ Hodge structure $(J,Q)$. RH $=$ this structure is **polarized** (the
   Riemann bilinear relation $Q(x,Jx)>0$) $=$ a Kähler form $\omega$ exists.
8. **The Kähler form.** $\omega=Q(J\cdot,\cdot)$ is determined but its positivity $=$ RH; $\mathcal T$ is **not**
   the Lefschetz grading (its spectrum is the dense zeros, not integer weights); $\mathcal T$ is **unitary**, not a
   contraction. So $\omega$ is an **independent** hard-Lefschetz $\mathfrak{sl}_2$, not generable from the flow.

## Part D — THE PRECISE GAP (exactly what is missing)

We have constructed, on the primitive cohomology $\mathcal H_W^{\mathrm{prim}}$ (a real, **infinite-dimensional**
Kreĭn space):
- an indefinite polarization $Q$ (the Weil pairing), negative index $\kappa=\#$off-line zeros;
- a self-adjoint **Frobenius operator $\mathcal T$** with $\operatorname{spec}(\mathcal T)=\{\gamma_\rho\}$;
- a complex structure $J$ (the spectral splitting) and the functional-equation involution.

**The single missing object:**
> A **hard-Lefschetz $\mathfrak{sl}_2$-action** $(L,\Lambda,H)$ on $\mathcal H_W^{\mathrm{prim}}$ — equivalently a
> positive Kähler $(1,1)$-form $\omega$ — that (i) is **independent of** $\mathcal T$ (it cannot be built from the
> flow; Attempt 8), (ii) **commutes appropriately with** $\mathcal T$ (Frobenius acts on the cohomology), and
> (iii) is **positive**, so the Hodge–Riemann bilinear relations hold and force $Q\succeq0$ on primitives $=$ RH.

This $L$ is exactly the **ample class of the arithmetic surface $\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}
\operatorname{Spec}\mathbb Z$**. In the function-field case $C\times C$ supplies it for free (the polarization of the
surface); for $\operatorname{Spec}\mathbb Z$ it is the lone missing input.

**Why it is hard (the structural tension):** $L$ must be an integer-graded hard Lefschetz **coexisting with the
Frobenius $\mathcal T$ whose spectrum is the dense, $\mathbb Q$-independent set of zeros** (Linear Independence,
P15). A *finite-dimensional* Lefschetz is excluded (LI: no finite model). So $L$ must be an **infinite-dimensional
hard-Lefschetz structure** compatible with an infinite, independent Frobenius spectrum — an exotic object that
exists in no current geometry for $\operatorname{Spec}\mathbb Z$.

## Part E — Paths for the team (concrete, non-circular sub-targets)

1. **Construct $L$ from the scaling action (Connes' route, with our $\mathcal T$).** Connes realizes the zeros via
   the scaling action of $\mathbb R_+^\times$ on the adele class space. Is the *generator of the scaling action* (or
   a transverse Kähler structure of the associated foliation, à la Deninger) the missing Lefschetz $L$? Test
   whether it commutes with our $\mathcal T$ and induces a positive $\omega$. **This is the most direct: we have
   $\mathcal T$; find $L$ in the scaling/foliation geometry.**
2. **Beilinson realization (use Yuan–Zhang).** Realize $\mathcal H_W^{\mathrm{prim}}$ as an Arakelov
   $\widehat{\mathrm{Pic}}^0$ (or an adelic line-bundle space) of an *existing* higher-dimensional arithmetic
   variety whose Frobenius/regulator eigenvalues are the $\zeta$-zeros. Then Yuan–Zhang's *proven* Hodge index
   gives the positivity. The obstruction (Attempt 6) is the **zeros↔heights dictionary** (Beilinson conjectures):
   make the zeros, not the heights, the relevant eigenvalues.
3. **Infinite-dimensional hard Lefschetz.** Hard-Lefschetz $\mathfrak{sl}_2$ structures exist in
   infinite-dimensional settings (loop groups, Kähler geometry of infinite type). Construct one on $\mathcal H_W$
   compatible with a dense Frobenius spectrum — the LI-compatible version of the ample class.
4. **Kähler from the archimedean place.** The archimedean term $W(r)=\operatorname{Re}\psi(\tfrac14+\tfrac{ir}2)
   -\log\pi$ (the $\infty$-place) is the one *positive*, smooth ingredient. Does it define the Kähler metric? Test
   whether $\omega$ built from $W$ (the archimedean polarization) is positive and gives hard Lefschetz.
5. **Disprove from the LI side (a clean negative is also progress).** Show rigorously whether an integer-graded
   hard Lefschetz can coexist with a $\mathbb Q$-independent dense Frobenius spectrum — if it cannot, RH would need
   a fundamentally non-Lefschetz mechanism, sharpening the obstruction to a theorem.

## Part F — One-paragraph statement for the team
We have built, explicitly and unconditionally, the zero-carrying arithmetic cohomology of $\zeta$ — a Kreĭn space
$\mathcal H_W$ with an indefinite polarization $Q$, a Frobenius operator $\mathcal T$ whose spectrum is the zeros, a
complex structure $J$, the Lefschetz trace formula (the explicit formula, verified), and the anatomy as the local
Frobenius/Satake data — and reduced RH to **one missing structure**: an independent, positive, hard-Lefschetz
$\mathfrak{sl}_2$-action (a Kähler class $\omega$) commuting with $\mathcal T$, the ample geometry of
$\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z$. We proved this $\omega$ cannot come from the flow
alone. The team's task is to **supply $\omega$** — from the scaling/foliation geometry (Connes/Deninger), from a
Beilinson-type realization that activates the proven Yuan–Zhang Hodge index on the zeros (not the heights), or from
an infinite-dimensional hard-Lefschetz structure compatible with the $\mathbb Q$-independent zero spectrum — or to
prove no such $\omega$ exists, which would itself be a theorem about why RH resists.
