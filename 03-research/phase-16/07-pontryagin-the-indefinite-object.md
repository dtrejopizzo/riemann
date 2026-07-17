# Phase 16 · The indefinite object found — it is the de Branges/Pontryagin space $H(E_\xi)$

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
The geometric hunt converges. The indefinite object that carries the off-line index $\kappa$ — the one the modular
surface provably cannot supply (P22; the unified $\beta$-blind/definite negative) — **is the de Branges/Pontryagin
space $H(E_\xi)$**, with Frobenius $=$ multiplication-by-$z$ (spectrum $=$ the zeros) and $\kappa=$ Pontryagin index
$=$ off-line count. We demonstrate it genuinely detects off-line zeros (where every modular-surface pairing failed).
It is the canonical Hilbert--P\'olya object (already the subject of P16). The catch is honest: $\kappa$-detection is
by construction; proving $\kappa=0$ is RH, and equals the de Branges positivity $=$ the program's wrong-sign capstone.

---

## The object and the map
Under $z=-i(s-\tfrac12)$ the zero $\rho=\beta+i\gamma$ maps to $z=\gamma-i(\beta-\tfrac12)$:
- **on-line** ($\beta=\tfrac12$) $\to$ $z=\gamma$ real;
- **off-line** ($\beta>\tfrac12$) $\to$ $\Imag z<0$ (lower half-plane); ($\beta<\tfrac12$) $\to$ $\Imag z>0$ (upper).

Set $E_\xi(z)=\xi(\tfrac12+iz)$ (entire, order 1). Its zeros are the $z_n$ above. The de Branges space $H(E_\xi)$ has:
- **Frobenius:** multiplication by $z$, with spectrum $\{z_n\}=\{\gamma_\rho\}$ (the zeros) — the Hilbert--P\'olya
  operator;
- **negative (Pontryagin) index** $\kappa=\#\{$zeros of $E_\xi$ in the upper half-plane$\}=$ off-line count;
- **RH** $\iff\kappa=0\iff E_\xi$ Hermite--Biehler $\iff\Xi(z)=\xi(\tfrac12+iz)\in$ Laguerre--P\'olya (all zeros
  real) $\iff$ full Jensen-polynomial hyperbolicity (cf. P13/P20).

## It genuinely detects $\kappa$ (where the modular surface could not)
The de Branges reproducing-kernel diagonal $K_w(w)=\big(|E(w)|^2-|E^*(w)|^2\big)/(4\pi\Imag w)$ ($E^*(z)=\overline{E(\bar
z)}$) satisfies $K_w(w)\ge0$ for all $w$ $\iff\kappa=0$. Demonstrated (`pontryagin_kernel_detector.py`):
- **all zeros on-line** (roots in the lower half-plane): $K_w(w)>0$ at every probe $\Rightarrow\kappa=0$;
- **one zero moved off-line** (into the upper half-plane): $K_w(w)<0$ at a probe $\Rightarrow\kappa\ge1$ **detected**.

So $H(E)$ is the indefinite object with the correct $\kappa$ — in sharp contrast to every modular-surface pairing
(Petersson definite; bilinear Kre\u\i n definite; Klein--Gordon $\beta$-blind), none of which sees off-line-ness. The
hunt's conclusion: **the indefinite Hilbert--P\'olya object is $H(E_\xi)$**, and the modular surface failed precisely
because its $L^2$/symplectic pairings are definite and cannot be $H(E_\xi)$.

## The honest catch — and the wall
$\kappa$-detection is **by construction**: $K_w(w)$ is built from $E_\xi$, whose zeros *are* the spectrum. Knowing
$K_w(w)\ge0$ (i.e. $\kappa=0$, RH) requires an **independent** reason the zeros are on-line — which is RH itself.
Concretely, $K_w(w)\ge0$ for all $w$ is equivalent to the Weil positivity / $Q\succeq0$ (the de Branges and Weil
forms are the same Kre\u\i n/Pontryagin structure, P8/P16); proving it is the **de Branges structure-function /
canonical-system positivity**, for which:
- de Branges' specific sufficient condition was **refuted** (Conrey--Li, 1998);
- the general statement is the program's **finite-to-full uniformity gap** (each finite de Branges Gram matrix is
  positive unconditionally; the full positivity is RH) $=$ the Laguerre--P\'olya/Jensen hyperbolicity of P13/P20 $=$
  the **wrong-sign capstone** (CAP).

## Status (honest, and the convergence)
- **Found (the hunt's payoff):** the indefinite object is $H(E_\xi)$ — Pontryagin space, $\kappa=$ off-line count,
  Frobenius $=$ mult-by-$z$, spectrum $=$ zeros. It genuinely detects $\kappa$ (demonstrated). This *is* the
  Hilbert--P\'olya indefinite structure; the modular surface could not be it (P22). The object is **not missing** — it
  is de Branges/P16.
- **The wall (unchanged):** proving $\kappa=0$ is RH and equals the de Branges/Weil positivity $=$ CAP/P20; the naive
  de Branges condition is refuted (Conrey--Li). No independent positivity is in hand.
- **Net of the Phase-16 geometric hunt:** the indefinite object exists and is identified ($H(E_\xi)$); it is *not* on
  the modular surface (P22 + the unified negative); and its positivity is the standing wrong-sign capstone. The hunt
  converges back to the program's core — the Weil/de Branges positivity — now reached from the geometric/indefinite
  side and tied to a concrete, known object.
