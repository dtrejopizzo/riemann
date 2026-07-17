# Next phase — the Anatomy–Kreĭn–Hodge program: a spectral entry to the arithmetic Hodge index

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
A frontier pure-mathematics path toward RH, proposed in full knowledge of what the program has established. It is
not a shortcut and not a circle: it is the *one* direction that passes our own discriminator $D_0$, now equipped
with the new tools of this program (the anatomy, the Kreĭn/Pontryagin index, the Hodge–Riemann stability theorem)
as a genuinely new entry point into the geometric frontier where the one proven RH actually lives.

---

## 0. What we are allowed to propose (the honest constraint)

The program established, rigorously and from many sides:
- every RH-directed route collapses to **CAP** (Weil positivity, the wrong-sign capstone) or **SURF** (a missing
  arithmetic geometry over $\operatorname{Spec}\mathbb Z$);
- the discriminator $D_0$ shows a route can escape only with an **independent input carrying a decisive general
  theorem** ($I_{2a}\wedge I_{2b}$); the *only* known instance is the function-field proof, via a **surface
  $C\times C$ and the Hodge index theorem**;
- the finite-dimensional version is **obstructed under Linear Independence** of the zeros (P15): the model must be
  genuinely infinite-dimensional.

Therefore the only non-circular target is **SURF**: an arithmetic Hodge-index theorem for $\operatorname{Spec}
\mathbb Z$. This is RH-equivalent in difficulty and is the Connes–Consani / Deninger / Arakelov frontier. What is
*new* here is the **entry point**: this program produced three tools that the existing geometric approaches do not
have, and together they give a concrete, spectral, infinite-dimensional scaffold for that geometry.

## 1. The three tools, and why they fit the target

| Tool (this program) | Function-field analogue | Role in the target |
|---|---|---|
| **The anatomy** $\mathcal R_L$, with **Satake recovery** (P19) | the Frobenius eigenvalues on $H^1$ | a *spectral arithmetic Frobenius* for $\operatorname{Spec}\mathbb Z$: reads the local data the geometry would carry |
| **The localized Weil form as a Kreĭn/Pontryagin form**, negative index $\kappa$ (P16) | the **intersection form** on $\mathrm{NS}(C\times C)$, signature $(1,\rho-1)$ | the *intersection pairing* with its signature; $\kappa=$ off-line zeros $=$ failure of the Hodge index |
| **The Hodge–Riemann stability theorem** (P20) | Hodge index holds for *all* surfaces (AHK for matroids) | the criterion for *uniform* (full, infinite-order) positivity: a strictly-definite limit form |

The synthesis is exact: the function-field proof is *(intersection form) + (Hodge index = definiteness on the
primitive part)*. Our Kreĭn form **is** the intersection form; our anatomy **supplies its arithmetic content**
(the Frobenius/Satake data) without an a priori surface; our HR-stability theorem **is the definiteness criterion**,
now in the infinite-dimensional/tower setting the LI obstruction forces.

## 2. The program's central new idea

> **The anatomy is the missing arithmetic Frobenius.** In the function-field case the zeros *are* the Frobenius
> eigenvalues on $H^1$, and the Hodge index pins them by a definiteness theorem on a surface. For
> $\operatorname{Spec}\mathbb Z$ no such surface is known --- but the localized-Weil **anatomy recovers the full
> local data spectrally** (P19: Satake parameters, degree, local factors, Rankin--Selberg functoriality). So the
> ingredient the geometric programs seek to *construct* (a Frobenius / a cohomology carrying the zeros) is already
> available as a **spectral object**. The phase's thesis: build the arithmetic intersection theory *around the
> anatomy*, with the Kreĭn form as the pairing, and seek the Hodge-index definiteness by the HR-stability route.

This is genuinely new: it inverts the usual order. Connes–Consani/Deninger build a geometry and hope a Frobenius
and a positivity emerge; here the **Frobenius (anatomy) and the pairing (Kreĭn form) are already in hand**, and the
task is the *definiteness theorem* on the primitive part.

## 3. The milestones (with honest status markers)

**M1 — The arithmetic intersection pairing (achievable, non-circular).**
Construct, from the explicit formula and the anatomy, the data of an "arithmetic surface" for
$\operatorname{Spec}\mathbb Z$: a self-intersection, a *diagonal* class $\Delta$, and a *Frobenius-graph* class
$\Gamma$ (the prime-to-zero duality of the explicit formula), with the Kreĭn form as the intersection pairing.
Establish the axioms (symmetry, the Lefschetz trace identity $\Gamma\cdot\Delta=\sum_\rho 1$, the self-intersection
$\Gamma\cdot\Gamma$ in terms of the anatomy power sums). *Deliverable: a rigorous "arithmetic surface" pairing,
RH-independent.* This uses P16 + P19 directly.

**M2 — The ample cone and the edge positivity (achievable via de la Vallée Poussin).**
Identify the *positive/ample* directions: the **pole at $s=1$** (the de la Vallée Poussin anchor, P14's Landau
singularity) as the analogue of the fiber classes $f_1,f_2$ that span the hyperbolic plane $\langle f_1,f_2\rangle$
in $\mathrm{NS}(C\times C)$. The $H^0,H^2$ (trivial cohomology / poles) positivity is **unconditional** (this is
exactly the content of P14's anchor framework). *Deliverable: the hyperbolic-plane analogue, unconditional.*

**M3 — The Hodge-index step (this IS the capstone / RH).**
Prove the *primitive part* (the $H^1$ analogue, carrying the zeros) is negative-definite relative to the ample
cone --- the arithmetic Hodge index. **This is RH**, and we state it as such, not as a shortcut. The phase's
contribution is to attack it through two new channels:
- *(a) the HR-stability route (P20):* realize the primitive form as the limit of a **tower** of finite forms
  (the band-limited truncations of the Kreĭn form, $d\to\infty$); by Theorem (HR stability), uniform definiteness
  holds iff the **limit form is strictly definite**. The infinite-dimensional, self-similar criticality measured
  in P16/P18 is exactly the borderline $\delta_\infty=0$ case --- so M3 becomes the precise question: *is the
  limiting primitive form strictly definite or critically degenerate?*
- *(b) the functoriality route (P19):* the self-intersection $\Gamma\cdot\Gamma$ is governed by the **Rankin--Selberg
  anatomy** $s_k(\pi\boxtimes\bar\pi)=|s_k(\pi)|^2\ge0$ --- a positivity that holds *for free* (it is a square).
  In the function-field proof, $\Gamma\cdot\Gamma\ge0$ (effectivity) combined with the Hodge index forces
  $|\alpha|=\sqrt q$. Here the Rankin--Selberg positivity gives the analogue of effectivity unconditionally; the
  task is to combine it with M2's ample positivity to force the primitive definiteness. *This is the precise
  arithmetic form of the capstone, now with the Rankin--Selberg square as the effectivity input.*

**M4 — LI compatibility (a consistency check).**
Verify the construction is genuinely infinite-dimensional (the anatomy gives an infinite, $\mathbb Q$-independent
family of Satake data, no finite Frobenius), so it evades the finitization obstruction of P15. *Deliverable: the
construction is LI-consistent by design.*

## 4. What is honest about this

- **M1, M2, M4 are achievable and non-circular** (an arithmetic intersection pairing; the unconditional edge
  positivity; the LI-consistency). They are real, publishable, RH-independent or sub-RH partial results, and they
  assemble the scaffold.
- **M3 is RH** --- the wrong-sign capstone / the arithmetic Hodge index. We do **not** claim a shortcut. The phase's
  genuine novelty is the **two new attack channels** on M3 (the HR-stability limit question; the Rankin--Selberg
  effectivity square), which the existing geometric programs do not have, and which turn the capstone into a sharp,
  structured question rather than a blank wall.
- **The discriminator certifies the direction:** this is the *only* route with $I_{2a}$ (independent input: the
  anatomy/Satake data and the Kreĭn pairing) and a candidate $I_{2b}$ (the decisive theorem: an arithmetic Hodge
  index, attacked via HR-stability). Every other route the program enumerated fails $I_{2}$ a priori.

## 5. The one-paragraph thesis of the phase

The function-field RH is *(an intersection form) + (a Hodge-index definiteness theorem)*. This program has
independently produced the intersection form (the Kreĭn-realized localized Weil form) and its arithmetic content
(the anatomy's Satake recovery), and a criterion for the definiteness step (Hodge–Riemann stability under limits).
The next phase assembles these into an **arithmetic intersection theory built around the anatomy**, reduces RH to a
single **infinite-dimensional Hodge-index definiteness** (M3), and attacks it through two channels unavailable to
the geometric programs --- the HR-stability limit question and the Rankin--Selberg effectivity square. The early
milestones (M1, M2, M4) are achievable, non-circular, and real; the final one (M3) is RH itself, now sharply posed.
This is the honest frontier: not a promise of a proof, but the construction of the precise object a proof would
need, from the spectral side, where this program's tools give a genuinely new and certified entry.

## 6. For the team

- **M1 (intersection pairing):** an arithmetic-geometry/operator-theory team --- formalize the $\Gamma,\Delta$
  classes and the trace identity from the explicit formula + anatomy.
- **M2 (ample cone):** analytic number theory --- the de la Vallée Poussin / Landau anchor as the positive cone
  (largely in hand from P14).
- **M3a (HR-stability limit):** spectral theory / positivity --- decide strict-definiteness vs critical degeneracy
  of the limiting primitive Kreĭn form (the borderline measured in P16/P18).
- **M3b (Rankin--Selberg effectivity):** automorphic forms --- combine the unconditional Rankin--Selberg square
  with M2's ample positivity (the precise arithmetic capstone).
- **M4 (LI-consistency):** a short rigorous check.

This is where 55 mathematicians have a genuinely new, certified, frontier target --- and where partial victories
(M1, M2) are within reach while the capstone (M3) is attacked from two sides at once.
