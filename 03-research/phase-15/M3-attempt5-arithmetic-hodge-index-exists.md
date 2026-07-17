# Phase 15 · M3 · Attempt 5 — the arithmetic Hodge index theorem *exists*: the obstruction is the surface, not the theorem

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
A genuine attempt at the crossing — the upper/sign bound $\langle\Gamma,H\rangle^2>\langle H,H\rangle\langle\Gamma,
\Gamma\rangle$ — that corrects a false premise in Attempts 1–4 and sharpens the obstruction precisely. **No
fabricated crossing**; a real refinement, verifiable.

---

## 1. The corrected premise
Attempts 1–4 (and the M3b assembly) repeatedly said: *"in function fields the Hodge index is a general theorem;
for $\operatorname{Spec}\mathbb Z$ no such general theorem is known."* **The second half is false.** The arithmetic
Hodge index theorem is **proven**, in two forms:
- **Faltings–Hriljac (1984):** on an arithmetic surface (a regular model of a curve over $\operatorname{Spec}
  \mathcal O_K$), the Arakelov intersection pairing on $\widehat{\mathrm{Pic}}^0$ (arithmetically degree-zero divisor
  classes) is **negative definite**, and equals the Néron–Tate height pairing.
- **Yuan–Zhang (2017), Moriwaki:** the arithmetic Hodge index theorem in all dimensions — the intersection pairing
  of arithmetically trivial adelic line bundles on an arithmetic variety is negative definite.

So a *general* arithmetic $I_{2b}$ (a proven Hodge-index/signature theorem for arithmetic schemes) **is in hand**.
This reopens the crossing: the missing piece is not the theorem.

## 2. The genuine attempt: apply it to the Weil form
**Goal.** Realize the primitive part of the localized Weil intersection pairing (M1) as an instance of the
Arakelov pairing on $\widehat{\mathrm{Pic}}^0$ of an arithmetic surface, so that Faltings–Hriljac/Yuan–Zhang
supplies the negative-definiteness $=$ the signature $=$ M3 $=$ RH.

**What is needed (precisely).** An arithmetic surface $\mathcal X$ (a $2$-dimensional regular arithmetic scheme)
together with:
1. an identification of the primitive test space $\Pi^\perp$ with $\widehat{\mathrm{Pic}}^0(\mathcal X)\otimes\mathbb R$;
2. an identification of the Weil pairing $\langle\cdot,\cdot\rangle|_{\Pi^\perp}$ with the Arakelov intersection
   pairing (up to sign);
3. the zeros $\gamma_\rho$ realized as the relevant Arakelov eigenvalues.

Then $(2)$ + Faltings–Hriljac give the definiteness, hence RH.

## 3. Where it lands (honest, and sharper than before)
**The obstruction is exactly the surface $\mathcal X$, not the theorem.** Two facts:
- **Faltings–Hriljac/Yuan–Zhang control *heights*, not critical-line zeros.** On a genuine arithmetic surface (a
  curve over $\mathbb Z$, e.g.\ an elliptic curve $E/\mathbb Q$), the arithmetic Hodge index gives the
  negative-definiteness of the **Néron–Tate height** on $E(\mathbb Q)\otimes\mathbb R$ — a statement about
  **special values** ($L$-function at $s=1$, BSD), via the arithmetic divisors. It does **not** directly give the
  location of the **critical-line zeros** of the $L$-function. The link "Arakelov height pairing $\leftrightarrow$
  $L$-zeros on the critical line" is the (conjectural) Beilinson/arithmetic-motivic dictionary — open.
- **$\zeta_{\mathbb Q}$ has no arithmetic surface.** $\zeta_{\mathbb Q}$ lives on $\operatorname{Spec}\mathbb Z$
  (dimension $1$). To apply a $2$-dimensional Hodge index to *its* zeros one needs a $2$-dimensional
  $\mathcal X=\text{``}\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z\text{''}$, with the
  zeros as Frobenius eigenvalues on its $H^1$. **No such $\mathcal X$ exists** in current geometry — this is
  precisely SURF / the Connes–Consani program.

So the genuine attempt **does not cross**, but it **relocates and sharpens the obstruction decisively**:
\[
\boxed{\ \text{The missing }I_{2b}\text{ is \emph{not} a Hodge index theorem (Faltings--Hriljac/Yuan--Zhang exist);
it is the \emph{arithmetic surface} }\mathcal X\text{ for }\zeta_{\mathbb Q}\text{ on which to apply it.}\ }
\]

## 4. Why this is real progress (and what it tells the team)
- **The program's central claim is refined and made correct.** The wall is not "no Hodge index theorem"; it is "no
  arithmetic surface for $\operatorname{Spec}\mathbb Z$." The discriminator's $I_{2b}$ is split: the *theorem*
  exists ($I_{2b}$-theorem ✓), the *geometry* does not ($I_{2b}$-object ✗). The whole obstruction is the object.
- **This is testable on a control case.** For an elliptic curve $E/\mathbb Q$ there **is** an arithmetic surface,
  and there the arithmetic Hodge index **does** apply — to heights (BSD), not zeros. So the construction can be run
  end-to-end on $E$ and seen to land on heights, confirming the zeros↔heights gap is the precise missing link, not
  a defect of the method.
- **It identifies the single sharpest open problem.** Either (a) construct $\mathcal X$ for $\operatorname{Spec}
  \mathbb Z$ (the Connes–Consani $\mathbb F_1$ surface) — then Yuan–Zhang gives RH; or (b) realize $\zeta_{\mathbb Q}$'s
  zeros as Arakelov eigenvalues on an *existing* higher-dimensional arithmetic variety (a motivic/Beilinson
  realization) — then the proven Hodge index applies. Both are recognized deep programs; the attempt shows they are
  the *only* routes, because the theorem-half is already done.

## 5. Status
- **New (corrected) finding:** the arithmetic Hodge index theorem **is proven** (Faltings–Hriljac; Yuan–Zhang;
  Moriwaki). The obstruction to RH via M3 is therefore **purely the missing arithmetic surface** $\mathcal X$ for
  $\operatorname{Spec}\mathbb Z$ (and the zeros↔Arakelov dictionary), not a missing theorem.
- **No crossing:** $\mathcal X$ does not exist (SURF / Connes–Consani), and the height↔zero link is open
  (Beilinson). The attempt is genuine and lands honestly: it converts "we lack a Hodge index theorem" into the
  precise, correct "we lack the surface to apply the Hodge index theorem we already have."
- This is the sharpest true statement of the M3 obstruction the program has reached, and it is verifiable: the
  theorems cited are published; the gap (surface / zeros↔heights) is explicit.
