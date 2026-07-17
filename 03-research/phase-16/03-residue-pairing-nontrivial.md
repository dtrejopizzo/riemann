# Phase 16 · Route A resonance weights — NON-trivial space, but the residue sign is not the κ-detector

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Attacking the resonance realization directly. The scattering matrix $\varphi(s)=\xi(2s-1)/\xi(2s)$ has poles at
$s=\rho/2$ with residue $r_\rho=\xi(\rho-1)/(2\xi'(\rho))$ — the candidate Kreĭn self-weight of each resonance. Two
findings: **(1) the resonance space is genuinely non-trivial** ($|r_\rho|=O(1)$, escaping the Phase-4 de Branges
trivialization); **(2) self-refuted:** the residue sign is **not** the negative-index detector ($\operatorname{Re}(r_\rho)$
is sign-stable across $\beta$, so it does not witness RH). The Kreĭn sign $\varepsilon_\rho$ must be a different,
$\beta$-sensitive real quantity — still open.

---

## Finding 1 (solid): Route A does NOT trivialize
$|r_\rho|$ for the first 15 zeros is $O(1)$ (0.52 → 0.66, slowly increasing, **not** decaying). The exponential
factors cancel exactly: $\xi(\rho-1)\sim e^{-\pi\gamma/4}$ and $\xi'(\rho)\sim e^{-\pi\gamma/4}$, so
$r_\rho=\xi(\rho-1)/(2\xi'(\rho))=O(1)$ (decay-corrected $|r_\rho|e^{+\pi\gamma/4}$ blows up to $10^{19}$ —
confirming no decay). **Consequence:** the Kreĭn space of modular-surface resonances has genuine, bounded-below
self-weights — it does **not** collapse the way Phase-4's de Branges space $H(E_\xi)$ did (there $|E|\sim e^{-\pi t/4}
\to0$ forced a trace-class, vacuous form). Route A is a genuinely distinct, non-vacuous object. *(Certificate:
`pillar2_residue_pairing.py`.)*

## Finding 2 (self-refutation): the residue sign is not the κ-detector
$\operatorname{Re}(r_\rho)<0$ for all 15 on-line zeros — a consistent sign, naively suggesting a definite (RH-true)
form. **But the sensitivity probe kills this:** evaluating the analytic weight $r(s_0)=\xi(s_0-1)/(2\xi'(s_0))$ at
$s_0=\beta+i\gamma_1$ for $\beta=0.30,0.40,0.50,0.60,0.70$ gives $\operatorname{Re}(r)=-0.56,-0.50,-0.43,-0.37,-0.31$
— **negative throughout, no sign flip off the line.** So an off-line zero would also give $\operatorname{Re}(r)<0$:
the residue sign does **not** detect off-line-ness. The consistent negativity of $\operatorname{Re}(r_\rho)$ is a
$\beta$-stable property of the analytic weight, **not** a witness for $\kappa=0$. *(Certificate:
`pillar2_residue_sign.py`.)*

> **Lesson (logged):** the residue $r_\rho$ supplies the resonance **magnitude** (Finding 1, non-trivial), not the
> Kreĭn **sign** $\varepsilon_\rho$. The negative index $\kappa$ — the indefiniteness that equals RH — must come from
> a **$\beta$-sensitive real** pairing that flips sign according to which side of $\operatorname{Re}(s)=1/4$ the
> resonance sits. The scalar residue is sign-stable and cannot be it.

## Where this leaves Route A
- **Encouraging:** unlike every prior spectral home (Phase-4 de Branges trivialized; Arakelov gave definite heights),
  the modular-surface resonance space is **non-trivial and naturally indefinite** (Pillar-2 prototype) with $O(1)$
  weights. It clears the triviality, heights, and independence filters.
- **Open core (unchanged, sharpened):** the actual Kreĭn self-pairing $\varepsilon_\rho$ (the $\beta$-sensitive real
  quantity detecting the resonance's side) is **not** the residue. In resonance theory this is the **bilinear
  (Gamow-vector) pairing**, not the scalar residue — the natural Kreĭn form on resonance states. Finding it, and
  showing its negative index $=\kappa$, is the next concrete sub-problem and the remaining content of Pillars 1–2.
- **Next step:** compute the bilinear resonance pairing $\langle v_\rho, v_{\rho'}\rangle$ from the Maass–Selberg
  relation in the resonance limit (the off-diagonal $\varphi(s)\varphi(s')$ terms at $s,s'\to\rho/2,\rho'/2$), and
  test whether *that* real form is $\beta$-sensitive and reproduces $Q$.
