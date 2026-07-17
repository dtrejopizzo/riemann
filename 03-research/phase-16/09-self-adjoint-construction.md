# Phase 16 · The self-adjoint / Herglotz realization — setup, the precise open step, and the line

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
Engaging the construction the Herglotz criterion (P23) points to: a self-adjoint operator whose Weyl function is
$\xi'/\xi$, spectrum $\{\gamma_\rho\}$, real $\iff$ RH. We set it up precisely, identify its two unconditional
ingredients, connect it to the program's core (Phase-4 Problem B), and state the exact open step — which is RH. We do
not fabricate the completion.

---

## The construction (precise)
In the spectral variable $z$ with $s=\tfrac12+iz$ (so $\sigma>\tfrac12\leftrightarrow\Im z>0$), put
$$
m(z):=\frac1{i}\,\frac{\xi'}{\xi}\!\left(\tfrac12+iz\right).
$$
Then $m$ is meromorphic with:
- **poles exactly at $z=\gamma_\rho$** (the $\zeta$-zeros in the $z$-variable);
- **all residues $+1$** (unconditional: $\xi'/\xi$ has residue $+1$ at each simple zero);
- **$\Im m=0$ on the real $z$-axis** (unconditional: the boundary identity, P23 Thm — functional equation).

By the Nevanlinna/Kre\u\i n--de Branges theorem, $m$ is the **Weyl $m$-function of a self-adjoint operator** (equiv.\
a canonical system $\frac{dY}{dx}=zJH(x)Y$, $H(x)\succeq0$) **iff** $\Im m(z)\ge0$ for $\Im z>0$ — i.e.\ iff the poles
$\{\gamma_\rho\}$ are real — i.e.\ **iff RH**.

## The two unconditional ingredients (and why they are only ``half'')
- **Positive residues ($+1$):** a meromorphic function with all positive residues and \emph{real} poles is
  automatically Herglotz (partial-fraction criterion). So positive residues is the ``easy half.''
- **$\Im m=0$ on the axis:** the spectral axis is the boundary of the Herglotz region; this is the edge condition.

The missing half is the **reality of the poles**. A positive-residue function with a complex pole pair
$\gamma_0\pm i\delta$ has $\Im m<0$ somewhere above the axis (verified structurally) — it is \emph{not} Herglotz.
Reality of the poles is exactly RH.

## Two routes to build the operator
- **(A) Inverse spectral (from the zeros).** Reconstruct the canonical system $H(x)$ from the spectral measure
  $\sum_\rho\delta_{\gamma_\rho}$ via Kre\u\i n/Gelfand--Levitan. **Circular:** it presupposes the $\gamma_\rho$ real.
  (Fails the program's independence filter, P21.)
- **(B) Forward (from the primes).** Build the operator from the explicit formula — the Phase-4 pinned operator
  $\mathcal T=\Omega(D)+\Pi-2\sum_n\frac{\Lambda(n)}{\sqrt n}\,\Re\,T_{\log n}$, whose Weyl function is $m$. Its
  self-adjoint realization **exists** unconditionally (von Neumann deficiency-index argument, Phase-4 **B-1**); its
  spectrum is real / the form is semibounded **iff RH** (Phase-4 **B-2**).

## The precise open step (and that it is RH)
Route (B) is the non-circular one, and it is **exactly Phase-4 Problem B**:
$$
\text{(self-adjoint realization of }\mathcal T\text{ with real spectrum)}\iff\text{B-2 (semiboundedness)}\iff
\Im m\ge0\iff\RH.
$$
Phase 4 reduced B-2 to a **relative form bound (RFB)** — a Carleson/zero-density comparison of the off-line vs
on-line zero contributions, in the de Branges/$H(E)$ geometry — which it further reduced (Days 14--18) to a
**uniform low-frequency form factor / uniform pair correlation** of the zeros. That input is either RH-conditional
(Montgomery, proven only under RH) or a recognized open frontier (uniform Selberg/Goldston--Montgomery). The Herglotz
framing (P23) contributes the clean unconditional boundary identity ($\Im m=0$ on the axis) and the positive-residue
fact, but the interior positivity ($\Im m\ge0$) is RH.

## The honest line
Completing the construction — exhibiting the self-adjoint operator with **real** spectrum, built non-circularly —
**is a proof of RH**. The unconditional half (existence of a self-adjoint realization, B-1; positive residues;
boundary identity) is in hand; the other half (real spectrum / semiboundedness, B-2 / the RFB) is the open core, and
no amount of validation makes the object exist before that is proved. I will not present a completed realization,
because a self-adjoint operator with provably real spectrum here would be RH, and I have no unconditional proof of
B-2.

**What is genuinely workable (for the team, sub-RH or frontier):**
1. **The RFB as a Carleson condition** in $H(E_\xi)$ — the cleanest open sub-problem (Phase-4 Day 16): off-line zero
   contributions bounded by on-line ones via a Schur/interpolation regularity of the zero set.
2. **The canonical-system Hamiltonian $H(x)$** — study its structure from the explicit formula (the forward map),
   seeking a positivity ($H(x)\succeq0$ with the right monotonicity) that is the de Branges ordering; Conrey--Li
   refuted the specific de Branges condition, so a \emph{new} monotonicity is what is needed.
3. **Uniform pair correlation** — the decisive analytic input; unconditional progress here (a uniform low-frequency
   discrepancy bound for $\{\gamma_\rho\}$) would settle B-2.

## The RFB frontier, characterized (work toward the analysts)
- **Unconditional Herglotz region:** $\Im m>0$ holds unconditionally for $\sigma>1$ (zero-free) and in the de la
  Vallée Poussin region $\sigma>1-c/\log|t|$. **RH $=$ extending it to $\sigma>\tfrac12$**; the gap is the strip
  $\tfrac12<\sigma<1$. (Verified: $\Im m>0$ throughout $(\tfrac12,\infty)$ in range — RH true there.)
- **The RFB is vacuous on real data (decisive):** the relative form bound $|\mathfrak t_-(g)|\le a\,\mathfrak t_+(g)
  +C\|g\|^2$ concerns the **off-line** contribution $\mathfrak t_-$; when RH holds in the computed range there are
  **no off-line zeros**, so $\mathfrak t_-\equiv0$. The RFB is therefore a statement about *hypothetical* off-line
  zeros, provable only as an **abstract analytic inequality**, never by computing with the actual $\gamma_\rho$. It is
  not script-attackable.
- **The reduction (Phase-4 Days 14–18, reconfirmed):** B-2 / RFB $\Leftarrow$ a **uniform low-frequency form factor**
  $F(\alpha)\ll1$ of the zeros (uniform pair correlation). Montgomery's $F(\alpha)$ is proven only **under RH** for
  $|\alpha|>1$; the unconditional versions (Goldston–Montgomery, Selberg $\int|S|^2\ll T\log\log T$) are
  **average/typical, not uniform**. So the frontier is a uniform pair-correlation bound — an **analytic** problem,
  RH-conditional or open, for the team's analysts. (`rfb_frontier_characterization.py`.)

## Status
- **Set up cleanly:** the Herglotz/Weyl construction, with two unconditional ingredients (positive residues, boundary
  identity) and the precise reduction to Phase-4 B-2 / the RFB / uniform pair correlation.
- **Open core (= RH):** the reality of the poles / $\Im m\ge0$ / semiboundedness. Not fabricated.
- **Consistent** with the program's standing map: the construction is Hilbert--P\'olya $=$ Phase-4 Problem B $=$ the
  RFB frontier $=$ the wrong-sign capstone. The genuine next work is the RFB / uniform pair correlation, sub-RH and
  hard, where the program (and the field) sits.
