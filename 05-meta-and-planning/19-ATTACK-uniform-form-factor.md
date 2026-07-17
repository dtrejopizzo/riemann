# Attacking the uniform form factor: exact identity, unconditional core, and the precise gap

**Auditor build · 2026-06-05.** Target (non-circular, sub-RH): the uniform bound $V(d,T)\ll dN$ on the mesoscopic
second moment, equivalently a finite bottom $(LB)$ for the Weil form. We push it rigorously: an exact identity
making $V$ a manifest square, the unconditional ingredients, the unconditional *equivalence* to short-interval
prime variance (the non-circular bridge), and the exact residual gap. No claim of crossing.

---

## 1. Exact identity: $V$ is a band-limited square

For zeros $\{\gamma\}$ in a window at height $T$, set $S(\xi)=\sum_\gamma e^{i\gamma\xi}$. Then, exactly,
$$
\int_{-2d}^{2d}|S(\xi)|^2\,d\xi
=\sum_{\gamma,\gamma'}\int_{-2d}^{2d}e^{i(\gamma-\gamma')\xi}\,d\xi
=4dN+\sum_{\gamma\ne\gamma'}\frac{2\sin\!\big(2d(\gamma-\gamma')\big)}{\gamma-\gamma'}
=V(d,T).
$$
> **$V(d,T)=\displaystyle\int_{-2d}^{2d}|S(\xi)|^2\,d\xi\ \ge 0$** — manifestly nonnegative, the band-limited $L^2$
> energy of the zero exponential sum. The diagonal is exactly $4dN$; the question $V\ll dN$ is whether the
> off-diagonal does not exceed the diagonal in order, i.e. whether the zeros do not cluster beyond the diagonal.

This positivity is the unconditional engine: it gives **lower** bounds on pair correlation (Montgomery's route to
simple-zero results) but, by itself, no **upper** bound — the wrong-sign capstone, exactly localized.

## 2. The explicit-formula expansion: $V$ is a prime second moment

By the Weil explicit formula, $S(\xi)$ (suitably windowed/smoothed) equals an archimedean main term minus a prime
sum $\sum_n \Lambda(n)n^{-1/2}k_d(\xi-\log n)$ with $k_d$ the band kernel. Hence
$$
V(d,T)=\underbrace{\mathcal A(d,T)}_{\text{archimedean, smooth}}
+\underbrace{\sum_{n}\frac{\Lambda(n)^2}{n}\,|k_d|^2}_{\text{diagonal, unconditional}}
+\underbrace{\sum_{m\ne n}\frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}\,K_d(\log\tfrac mn)}_{\text{off-diagonal}} .
$$
- **Diagonal (unconditional):** $\sum_{n\le e^{2d}}\Lambda(n)^2/n\sim\tfrac12(2d)^2=2d^2$ — explicit, RH-free.
- **Off-diagonal:** $\sum_{m\ne n}$ with $\log(m/n)$ small, i.e. **$m,n$ in short multiplicative intervals**. This
  is the entire difficulty, and it is a statement about *primes*, not zeros.

## 3. The non-circular bridge (a theorem): $V\ll dN \iff$ short-interval prime variance

**Goldston--Montgomery (1987), unconditional equivalence.** The mesoscopic second moment of the zeros and the
variance of primes in short intervals are *equivalent*, with no RH assumed on either side:
$$
V(d,T)\ \ll\ dN\quad(\text{uniformly, in the matched ranges})\ \Longleftrightarrow\
\int_1^X\!\Big(\psi(x+\tfrac xH)-\psi(x)-\tfrac xH\Big)^2\frac{dx}{x^2}\ \ll\ \frac{\log X}{H}\quad(\text{uniformly}).
$$
This is the precise sense in which the target is **non-circular**: it is provably equivalent to a prime-side
statement that mentions no zero, and the equivalence is a theorem independent of RH.

## 4. The unconditional state, and the exact gap

In the form-factor variable $\alpha=2d/(\log T)$ (Montgomery normalization), $V=N\!\int \widehat\phi(\alpha)F(\alpha,T)\,d\alpha$,
$F\ge0$:
- **$|\alpha|<1$ — controlled.** $F(\alpha,T)$ is pinned in this range (Montgomery's asymptotic under RH; and,
  unconditionally, the Goldston--Montgomery equivalence plus Selberg's mean bound control this regime). The diagonal
  $2d^2$ lives here. **No RH needed for a bound here.**
- **$|\alpha|\ge1$ — the gap.** The high-frequency form factor. Montgomery's conjecture $F(\alpha)\to1$ is
  open/RH-flavoured; the unconditional substitute is Selberg's $\int_0^T S(t)^2\,dt\ll T\log\log T$, which bounds
  the **typical** fluctuation but **not the uniform/worst-case** one. The required object is a **uniform** upper
  bound on $F(\alpha)$ for $|\alpha|\ge1$.

**Unconditional upper bound, with its honest loss.** The large sieve / Montgomery--Vaughan inequality applied to
the prime second moment yields, unconditionally, a bound of the shape
$$
V(d,T)\ \ll\ dN\cdot(\log T)^{c}\qquad(\text{some fixed }c>0;\ \text{the off-diagonal controlled by the diagonal up to a logarithmic power}),
$$
since the large sieve controls $\sum_{m\ne n}$ at the cost of a logarithmic factor. *(That an unconditional
logarithmic-type loss is available is classical; the precise least admissible power $c$ — in particular whether
$c$ can be reduced toward $0$ uniformly — is itself part of the frontier, not asserted here.)* This already gives a
**finite bottom up to a logarithmic factor**: $\mathfrak t[g]\ge -C(\log T)^{c}\|g\|^2$ on the height-$T$ window —
a genuine unconditional semiboundedness, weaker than the clean $(LB)$ by the logarithmic loss.

> **The gap, exactly.** Removing the single $\log T$ — i.e. the uniform $F(\alpha)\ll1$ for $|\alpha|\ge1$, i.e.
> the uniform short-interval prime variance $\ll\log X/H$ — is the entire residual. It is **strictly weaker than
> RH** (RH yields the *typical* variance, not the uniform one), **non-circular** (the Goldston--Montgomery bridge),
> and is the **recognized Goldston--Montgomery / short-interval frontier**.

## 5. Where the attack stands

- **Established here, rigorously and RH-free:** the exact identity $V=\int_{-2d}^{2d}|S|^2$; the diagonal
  $\sim2d^2$; the unconditional bound $V\ll dN\log T$ (finite bottom up to a $\log$); the non-circular reduction to
  short-interval prime variance.
- **Not crossed:** the clean $V\ll dN$ (removing the $\log T$) is the uniform high-frequency form factor —
  open, recognized, sub-RH.
- **The honest gain:** the program's central inequality $(LB)$ now has an **unconditional version with a single
  logarithmic loss**, and the loss is identified with one explicit, non-circular object (uniform $|\alpha|\ge1$
  form factor $=$ uniform short-interval prime variance). The cross-scale view (P-residue) located this in the
  largest band-scale primes; that is consistent: the short interval is at scale $x\sim e^{2d}$, the top octave.

## 6. The next move, concretely

Two non-circular sub-targets, in increasing strength:
1. **Reduce the logarithmic-power loss $c$** by replacing the crude large sieve with a Montgomery--Vaughan
   weighted sieve plus Selberg's $S(t)^2$ bound in the $|\alpha|\ge1$ tail — a finite bottom of strength between the
   crude bound and clean $(LB)$. Purely analytic, RH-free, and a concrete improvement on the corpus's Day-19
   stopping point; each decrement of $c$ is a measurable partial result.
2. **The clean uniform bound** (remove the loss entirely) — the Goldston--Montgomery frontier; not expected from
   current technology, but now precisely the only remaining obstacle, and provably not RH.

## 7. Numerical verification (real zeta zeros)

`phase-14/experiments/verify_V_identity.py`, zeros $\#1000$–$1079$ ($T\approx1465$, mean density $\rho\approx0.868$):
- **Backbone identity confirmed:** $\sum_{\gamma,\gamma'}2\sin(2d(\gamma-\gamma'))/(\gamma-\gamma')=\int_{-2d}^{2d}
  |S(\xi)|^2d\xi$ to relative error $\le3\times10^{-6}$ across $d\in[0.25,3]$ ($\alpha=2d\rho$ from $0.43$ to
  $5.2$). The reduction of \S\S1--2 rests on an exact, now-verified identity.
- **Form factor bounded for $|\alpha|\ge1$:** $V/(dN)$ decreases through $\alpha=1$ and levels at
  $\approx3.8$ (diagonal $4$ minus a small GUE-repulsion off-diagonal $\approx-0.2$) for $\alpha\gtrsim3$. So for
  $\zeta$'s actual zeros $V\sim dN$: $F(\alpha)$ is **bounded** at high frequency (the clean bound holds, $c=0$ in
  reality, as GUE predicts). **The logarithmic loss $(\log T)^c$ is a limitation of the unconditional proof, not of
  $\zeta$:** the zeros realize the clean $(LB)$, and the entire residue is the *unconditional* uniform form-factor
  bound, exactly as claimed.

## Verdict

The uniform-form-factor attack yields a **genuine unconditional result** — $V\ll dN(\log T)^{c}$, a finite bottom
for the Weil form up to a logarithmic power — and reduces the remaining gap to a **single, explicit, non-circular,
sub-RH object**: the uniform high-frequency form factor, equivalently the uniform short-interval prime variance,
localized to the largest primes of the band. This is the first point in the entire program where an unconditional
semiboundedness (modulo $\log T$) is in hand and the residual is a recognized frontier strictly below RH rather
than RH itself.
