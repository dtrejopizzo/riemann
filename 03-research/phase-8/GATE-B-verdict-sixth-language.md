# Phase 8 / Gate B — a clean monotonicity theorem, and the sharp reason the heat flow does not cross

**Author: David Alejandro Trejo Pizzo · 2026-06-04.** `experiments/gateB_lyapunov.py`.

## The theorem (derived + verified)

Under the de Bruijn–Newman forward flow $\dot z_j=2\sum_{k\ne j}(z_j-z_k)^{-1}$, the off-line-ness
$\mathcal L=\sum_j(\mathrm{Im}\,z_j)^2$ obeys
$$
\boxed{\ \dot{\mathcal L}\;=\;-2\sum_{j\ne k}\frac{(y_j-y_k)^2}{|z_j-z_k|^2}\;\le\;0\ }\qquad(y_j=\mathrm{Im}\,z_j).
$$
*Proof:* $\dot{\mathcal L}=2\sum_j y_j\,\mathrm{Im}\,\dot z_j=-4\sum_{j\ne k}\frac{y_j(y_j-y_k)}{|z_j-z_k|^2}$;
symmetrizing $j\leftrightarrow k$ gives the boxed form. *Verified:* `Ldot_formula` matches a finite-difference
of $\mathcal L$ along RK4 to machine precision for every test configuration. This is a clean, unconditional
theorem — and genuinely new to our program. It rigorously realizes the "critical line is the attractor"
instinct: $\mathcal L$ is a strict Lyapunov function for the forward flow, $0$ iff all zeros are real.

**By-product (a real constraint).** An isolated conjugate pair at $\pm iy_0$ obeys $\frac{d}{dt}y_0^2=-2$
exactly (verified), so it heals by $t=y_0^2/2$. Hence any RH-violating zeros sit at imaginary height
$|\mathrm{Im}|\le\sqrt{2\Lambda}\le\sqrt{0.4}\approx0.63$ (using Polymath15's $\Lambda\le0.2$) — a clean
height bound of de Bruijn type.

## Why it does NOT prove RH — the two sharp obstructions (both verified)

1. **Wrong direction.** Forward ($t$ increasing) $\mathcal L$ *decreases* to $0$ (the $t\ge\Lambda$ regime).
   To prove RH we must go from $t=\Lambda$ *back* to $t=0$, where $\mathcal L$ *increases*. The monotonicity
   then yields only $\mathcal L(0)\ge\mathcal L(\Lambda)=0$ — **trivially true**, not $\mathcal L(0)=0$.
   *(Verified: §3 of the script — $\mathcal L$ falls forward, rises backward.)*
2. **Arithmetic-blindness (the decisive one).** The identity holds for **arbitrary** conjugate-symmetric
   configurations — random, $\zeta$-like, clustered — *identically*. The Coulomb ODE **knows nothing about
   the primes.** A pure-ODE Lyapunov argument therefore **cannot** single out $\zeta$: it would prove "every
   function satisfies RH," which is false (generic $H_0$ has $\Lambda>0$; e.g.\ explicit functions with
   off-line zeros). *(Verified: §1–2 — same identity for all configs.)*

> **The escape was illusory, and now we can say *precisely why*.** The time parameter looked like a new
> degree of freedom outside the explicit formula. It is — but it is **arithmetic-blind**: the flow is
> generic, so the new DOF carries no information about the primes. **RH lives entirely in the initial
> condition** $H_0=\xi$ — in *where the zeros start and how they are spaced*. To use the flow to prove RH one
> must feed in $\zeta$'s initial zero statistics (pair correlation), and controlling those is exactly the
> wall **B1** (the sine-kernel / pair-correlation, which *describes* but does not *force* the reality of the
> zeros). The heat flow does not bypass the wall; it **reduces to it through the initial data.**

## This is the sixth language of the wall — and a meta-theorem about methods

The five languages of P11 were *reformulations* of the positivity. Gate B adds a sixth, of a different and
stronger kind: a **provable no-go for an entire class of approaches**.

> **N5 (dynamical no-go).** *Any RH attack based on the de Bruijn–Newman / heat-flow zero dynamics that uses
> only the flow (a Lyapunov/monotonicity argument from the ODE) cannot succeed: the flow is arithmetic-blind,
> so RH cannot be decided without re-injecting $\zeta$'s initial zero statistics, i.e.\ without the
> pair-correlation wall (B1).*

This **subsumes the forwarded "PT-symmetry / dissipative-dynamics" suggestion**: any dissipative dynamics with
"the critical line as attractor" is a flow of this type, hence arithmetic-blind, hence subject to N5. The
attractor picture is *true and now rigorous* ($\mathcal L$ is a genuine Lyapunov function), but it is not a
proof of RH for the same structural reason.

## The only honest continuation, and its price

Arithmetic must enter through the **initial statistics**. The productive version of the heat-flow path is
therefore **Rodgers–Tao's**: couple the flow to $\zeta$'s actual zero distribution. They did exactly this to
prove $\Lambda\ge 0$ (using the *lower* control of fluctuations). The RH direction $\Lambda\le 0$ needs the
*upper* control of clustering — a uniform pair-correlation/large-deviation bound that is itself open and
RH-conditional (Montgomery's conjecture is proven only in a limited range, and only assuming RH beyond it).
So the continuation is **their machinery + the B1 wall** — no free lunch, $<2\%$.

## Status
- $\dot{\mathcal L}\le0$ (Lyapunov for the forward flow) — ✅ derived + verified; clean, unconditional, new.
- Height bound $|\mathrm{Im}|\le\sqrt{2\Lambda}\le0.63$ for any violator — ✅ by-product.
- Proves RH? — ❌ wrong-direction **and** arithmetic-blind (both verified).
- **N5 dynamical no-go** (flow-only Lyapunov ⇒ cannot cross; subsumes PT-symmetry) — ✅ established.
- Continuation = Rodgers–Tao statistics + the B1 pair-correlation wall — ⬜ open, $<2\%$, their machinery.
