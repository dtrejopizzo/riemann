# Phase 66 / D3 — Face (A) is the sup-vs-mean-square gap; it maps to MW-2

**Goal:** locate face (A) of the escape theorem (central adelic large sieve at the critical exponent)
against what the *classical* large sieve unconditionally provides, and name the gap.

## 1. Face (A) in Fourier/symbol coordinates

Face (A): $\displaystyle \sup_X\Big\|\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\,\Pi_{\mathrm{prim}}
(F_{\log n})\Big\|<\infty$, where $F_{u}$ is the scaling/translation-by-$u$ operator on $L^2$ of the
scaling variable, and $\Pi_{\mathrm{prim}}$ removes the principal (pole/DC) channel.

The operator $\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}F_{\log n}$ is a Fourier multiplier with **symbol**
$$
   m_X(\xi)=\sum_{n\le X}\Lambda(n)\,n^{-1/2+i\xi}
   \;=\;\Big(-\tfrac{\zeta'}{\zeta}\Big)\!\big(\tfrac12-i\xi\big)\ \text{(truncated at $X$)} .
$$
Its operator norm is $\sup_\xi|m_X(\xi)|$. The pole of $-\zeta'/\zeta$ at $s=1$ (i.e. $\xi$ near the DC
channel) is exactly the principal channel that $\Pi_{\mathrm{prim}}$ removes. Hence
$$
   \Big\|\sum_{n\le X}\tfrac{\Lambda(n)}{\sqrt n}\Pi_{\mathrm{prim}}F_{\log n}\Big\|
   \;=\;\sup_{\xi}\Big|\,m_X(\xi)-(\text{pole part})\,\Big| .
$$
**Face (A) $=$ the $\sup_\xi$ (L$^\infty$-in-$\xi$) boundedness, uniform in $X$, of the primitive
partial sums of $-\zeta'/\zeta$ on the critical line.**

## 2. What the classical large sieve gives: the mean square only

The Montgomery–Vaughan large sieve controls the **mean square** (L$^2$-in-$\xi$, average over the dual
variable):
$$
   \int |m_X(\xi)|^2\,d\mu(\xi)\ \ll\ \sum_{n\le X}\frac{\Lambda(n)^2}{n}\ \sim\ \tfrac12(\log X)^2 .
$$
This is exactly the trace growth $\operatorname{Tr}K_P\sim\tfrac12(\log P)^2$ of phase-64: the
**mean** grows like $(\log X)^2$, and that entire growth **is the pole/principal channel** (the $H$
direction). Removing it (the $\Pi_{\mathrm{prim}}$ / $P_{\mathrm{prim}}$ projection) is precisely
subtracting this divergent mean.

## 3. The gap, named

| quantity | what controls it | growth |
|---|---|---|
| mean square $\int|m_X|^2$ | classical large sieve (unconditional) | $\sim\tfrac12(\log X)^2$ — the pole/$H$ channel |
| $\sup_\xi|m_X|$ off the pole (face A) | **open** | must be $O(1)$ for escape/RH |

So face (A) is the **sup-norm at the critical exponent** $\tfrac12$, while the large sieve delivers only
the **mean square**. The projection $\Pi_{\mathrm{prim}}$ removes exactly the divergent mean (the pole);
the claim that the *fluctuation* $\sup_\xi$ off the pole stays $O(1)$ is the **individual** statement,
not the **average** one.

**This is the master quantifier wall MW-2** (average $\to$ individual), in the sharpest analytic dress
the program has: the large sieve = average = trace = pole channel (unconditional); the escape = sup =
individual = fluctuation off the pole (RH-strength). A single $\xi$ (a zero of $\zeta$ pushed off the
line) spikes $\sup_\xi|m_X|$ without disturbing the mean — the same average/individual mechanism as
NG-62 (Cesàro) and CIR-1 (Selberg density bounds the count, not the individual).

## 4. Verdict (honest, below RH)

Face (A) does **not** sit below RH: it is MW-2 in critical-exponent large-sieve form. What is genuinely
gained (real orientation, not a proof step):
- **Precise identification:** face (A) $=$ uniform sup-boundedness of the primitive partial sums of
  $-\zeta'/\zeta$ on the critical line — an $L^\infty$-in-$\xi$, critical-exponent bound. This is a
  Lindelöf-adjacent statement, strictly stronger than any mean-square/zero-density input.
- **Why the classical large sieve cannot reach it:** it is an $L^2$ (mean) inequality; the escape needs
  $L^\infty$ (individual). The primitive projection removes the mean (the pole), leaving exactly the
  individual fluctuation.
- **Consequence for Phase 66:** among the three faces, (A) $=$ MW-2 and (B) $=$ MW-5; neither is below
  RH. The only pieces of this phase that are genuinely below RH are **D1** (the easy direction
  ¬RH$\Rightarrow$unbounded, sharpness) and **D2** (the faithful detector). Face (C) — canonical-system
  compactness at exponent $\tfrac12$ — is the operator-theoretic twin of (A) and inherits the same
  sup-vs-mean gap.

**Logged to NO-GO structure:** face (A) $\to$ MW-2 (critical-exponent large sieve = sup-vs-mean-square).
Do not attempt face (A) as an independent route; it is the average$\to$individual master quantifier.
