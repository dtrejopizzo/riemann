# Day 22 — Coercivity (§2½) as pure sampling theory: $D^-=\infty$ is insufficient; the depth split

Per the referee: attack coercivity (§2½) as a **pure sampling problem in $PW_d$** — forget $\zeta$. The
question: does $\mathfrak t_+=\sum_{\gamma}|F(\gamma)|^2\ge c\,\rho\,\|F\|_2^2$ follow from the zeros' lower
density $D^-=\infty$, or is a gap/separation condition genuinely needed? **Answer (the referee's instinct
confirmed): $D^-=\infty$ does NOT suffice** — a single Nyquist-size gap kills the lower frame bound. But the
**interaction with off-line zeros** (which is all coercivity is *for*) reveals a finer structure — a **depth
split** — that the Day-21 "no gaps" framing missed, and that points back toward unconditional B-2 via *local*
zero-density. **Tags:** ✅ rigorous (the negative) · ◆ the depth split / to-execute · ⬜.

---

## 1. $D^-=\infty$ does NOT give the lower frame bound ✅ (referee was right)
Pure sampling fact (Beurling–Landau): for $\Lambda\subset\mathbb R$ and $PW_d$,
$$
\sum_n|F(\lambda_n)|^2\ge A\|F\|^2\ \forall F\quad\text{(set of sampling)}\quad\Longleftarrow\quad \sup_n(\lambda_{n+1}-\lambda_n)<\frac\pi d\ \text{(Beurling gap theorem)},
$$
and the lower density $D^-(\Lambda)\ge d/\pi$ is **necessary but not sufficient.** A sequence can have
$D^-=\infty$ yet a single gap $>\pi/d$: a function $F$ concentrated in that gap (a Nyquist-localized bump)
has $\|F\|=1$ but $F(\lambda_n)\approx0$ for all $n$ — the lower bound fails. **So the gap dependence of Day
21 is genuine; density alone does not remove it.** The referee's §2½ caution is correct.

---

## 2. The refinement Day 21 missed: coercivity is only needed *near off-line zeros* ◆
B-2 is $\widetilde{\mathfrak t}_-\le C\,\mathfrak t_+$. **Where $\widetilde{\mathfrak t}_-(F)=0$ (no off-line
zero in $F$'s support), no coercivity is needed** — there $\mathfrak t=\mathfrak t_+\ge0$ already (a large
on-line gap with no off-line zeros is **harmless**: the form is small but non-negative). So coercivity is
only required where off-line zeros sit. This **re-poses** the question: *not* "are there large on-line gaps?"
but "near each off-line zero, is $\mathfrak t_+$ comparable to $\widetilde{\mathfrak t}_-$?"

**The dangerous configuration** is a **Nyquist window full of off-line zeros and few on-line** ($\mathfrak t_+$
small, $\widetilde{\mathfrak t}_-$ large there). A $PW_d$ function has width $\sim1/d\gg1/\rho$ (mean
spacing), so it always spans $\sim\rho/d=P$ total zeros; coercivity fails only if those $P$ are
(essentially) all off-line. So:
$$
\text{coercivity fails}\ \iff\ \exists\text{ a Nyquist window where off-line zeros dominate (remove the on-line samples).}
$$

---

## 3. The depth split: deep off-line zeros are the only danger, and they are locally rare ◆
Split off-line zeros by depth $|b|=|\beta-\tfrac12|$:

| off-line type | $\kappa(b)=e^{2d|b|}$ | role in coercivity | local count |
|---|---|---|---|
| **shallow** $|b|<\delta$ | $\le e^{2d\delta}\approx1$ | **harmless** — $F(\gamma+ib)\approx F(\gamma)$, behaves like an on-line sample | up to $\rho$ (may cluster) |
| **deep** $|b|\ge\delta$ | up to $e^d$ | **dangerous** (amplified, distinct from on-line) | $o(\rho)$ per unit, by **short-interval zero-density** (unconditional) |

- **Shallow off-line zeros** sit essentially on the line ($|b|<\delta$), so $F(\gamma+ib)\approx F(\gamma)$
  and they act as extra on-line samples — they *help* coercivity, don't hurt. They may cluster (local count
  up to $\rho$), harmlessly.
- **Deep off-line zeros** ($\beta\ge\tfrac12+\delta$) are, by **classical short-interval zero-density**
  ($N(\sigma,T+1)-N(\sigma,T)=o(\log T)$ for fixed $\sigma>\tfrac12$, unconditional), **locally $o(\rho)$** —
  they *cannot fill* a Nyquist window. So they remove at most $o(P)$ of the $\sim P$ on-line samples.

**Therefore** every Nyquist window retains $\sim P-o(P)$ samples that are on-line or shallow-off-line
(both $\kappa\approx1$), so $\mathfrak t_+\gtrsim\rho\|F\|^2$ — **coercivity holds**, and the deep-off-line
amplified part is $o(P)\cdot e^d\|F\|^2=o(\mathfrak t_+)$:
$$
\boxed{\ \text{B-2}\ \Longleftarrow\ \text{deep off-line zeros are locally rare}\ (\text{short-interval zero-density for }\sigma>\tfrac12+\delta).\ }
$$
This is **far better than "no gaps"** (which was too crude) and **unconditional in spirit** (short-interval
zero-density is classical) — *but it needs careful execution* (§4).

---

## 4. Honest status — recalibrated
The Day-21 promise ("B-2 $\Leftarrow$ no Nyquist gaps, all else unconditional") was **too clean**. The
truth, from attacking §2½:
- $D^-=\infty$ alone is **insufficient** (referee right);
- coercivity is needed only **near off-line zeros**; large gaps without off-line zeros are harmless;
- the residual is a **depth-split local zero-density**: deep off-line zeros (large $\kappa$) must be
  locally $o(\rho)$ — controlled by **classical short-interval zero-density** (plausibly unconditional);
  shallow off-line zeros are harmless.

**To execute (the genuine remaining work):**
1. **Pin the depth threshold $\delta$ and the short-interval zero-density strength.** Need: for $\sigma\ge\tfrac12+\delta$,
   $\#\{\rho:\beta\ge\sigma,\ |\gamma-T|\le\tfrac1d\}=o(\rho)$ uniformly. Is the *uniform* (every $T$) version
   unconditional, or only on average? **This is the precise frontier.**
2. **The shallow term.** Confirm shallow off-line ($|b|<\delta$) really contributes $\le(1+O(\delta))\mathfrak t_+$
   (they sample like on-line); bound the $\delta$-error.
3. **Coercivity from the retained samples.** $\sim P-o(P)$ samples with $\kappa\approx1$ in each Nyquist
   window $\Rightarrow$ lower frame bound $c\rho\|F\|^2$ — make rigorous (a quantitative Beurling-type
   argument with the $o(P)$ deficit).

**Recalibrated probabilities (post-§2½, vs Day 21):**
| outcome | Day-21 | Day-22 |
|---|---|---|
| unconditional B-2 (depth split + short-interval density closes) | ~50% | **~45%** |
| needs a near-frontier (uniform short-interval) zero-density input | ~20% | **~35%** |
| surprise / collapse | ~30% | ~20% |

I lowered the optimism because the referee's coercivity worry was right: it does **not** come free from
density; it needs the depth split + a *uniform* short-interval zero-density, which is at the frontier.

---

## 5. Net (Day 22)
Attacking coercivity as pure sampling: **$D^-=\infty$ does not give the lower frame bound** (a single
Nyquist gap kills it — the referee's instinct). But coercivity is only needed *near off-line zeros*, and the
**depth split** shows the only danger is **deep** off-line zeros (large $\kappa$), which are **locally rare**
by classical **short-interval zero-density** — while shallow off-line zeros are harmless. So
$$
\text{B-2}\ \Longleftarrow\ \text{(uniform) short-interval zero-density for }\sigma>\tfrac12+\delta,
$$
a classical, plausibly-unconditional input — **much weaker than RH, sharper than "no gaps."** The Day-21
"no gaps" framing was too crude; the real residual is local deep-off-line density. **Still not a theorem**:
the uniform short-interval density (§4.1) is the precise frontier to settle. Next: execute §4, starting with
whether the *uniform* short-interval zero-density for fixed $\sigma>\tfrac12$ is unconditional.
