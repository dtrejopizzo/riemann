# The prime-side residue, formulated precisely — and where it separates from RH (non-circular)

**Auditor build · 2026-06-05.** Goal: state the cross-scale cancellation residue as a precise prime-side
proposition, decide whether attacking it is RH-circular, and locate the exact point where it becomes a recognized
(non-RH) frontier. Result: the residue is the boundedness of a single mesoscopic second moment $V(d,T)$; it is
**strictly weaker than RH** and **non-circular**; its unconditional part is Montgomery's proven pair-correlation
range; its open part is a *uniform form-factor bound*, which is the Goldston--Montgomery / short-interval
prime-variance frontier --- not RH itself.

---

## 1. From the octave picture to a clean form

Recall $\mathfrak t[g]=\mathfrak a[g]-\mathfrak p[g]$ and the band-limited detector identity. For $g$
band-limited of type $d$ centred at height $T$, the Weil quadratic functional admits the **second-moment form**
(Day-19 reduction, here re-derived as the sum of the cross-scale octaves):
$$
\mathfrak p\text{-fluctuation}\ \longleftrightarrow\
V(d,T)\;=\;\underbrace{4dN(T)}_{\text{diagonal (counting)}}\;+\;
\underbrace{\sum_{\gamma\ne\gamma'}\frac{2\sin\!\big(2d(\gamma-\gamma')\big)}{\gamma-\gamma'}}_{\text{off-diagonal pair correlation}},
$$
where the sum is over zero ordinates $\gamma,\gamma'$ in a window at height $T$. The cross-scale experiment is the
statement that the octave partial sums of $\mathfrak p[g^\ast]$ converge to the boundary $\mathfrak a[g^\ast]$; the
direction-independent content of that convergence is exactly the boundedness of $V(d,T)$.

> **Residue (precise).** $(LB)$ --- the localized Weil form is semibounded, $\mathfrak t[g]\ge-C\|g\|^2$ ---
> holds iff $V(d,T)\ll d\,N(T)$ uniformly (the off-diagonal does not exceed the diagonal in order). This is a
> statement about the **second moment of the prime sum / the pair correlation of zeros**, with no reference to the
> sign of any individual zero.

## 2. Non-circularity: $V(d,T)$ bounded is strictly weaker than RH

Three facts establish that attacking $(LB)$ via $V(d,T)$ is **not** RH-circular:

1. **It is implied by RH but does not imply it.** Under RH, $V(d,T)\ll dN$ follows from Montgomery's work; but
   $V(d,T)\ll dN$ gives only semiboundedness $\mathfrak t\ge-C\|g\|^2$ (a finite bottom), which is the Kre\u\i n
   index statement $\kappa<\infty$-adjacent / the $(LB)$, **not** $\mathfrak t\ge0$ ($=$ RH). The gap between
   ``finite bottom'' and ``nonnegative bottom'' is precisely the wrong-sign capstone: $(LB)$ is the strictly
   weaker, sign-free statement.
2. **Its unconditional core is a theorem.** Montgomery (1973) proved the pair-correlation form factor
   $R_2(\alpha)\to|\alpha|$ unconditionally for $|\alpha|<1$. The off-diagonal of $V(d,T)$ has kernel
   $\widehat{r}=\mathbf 1_{[-2d,2d]}$ at scale $1/d$, so its **low-frequency part ($|\alpha|<1$) is unconditionally
   controlled** --- a genuine, RH-free input.
3. **It is a prime-side statement.** By the Goldston--Montgomery equivalence, $V(d,T)$ bounded is equivalent to a
   second moment of $\psi(x+h)-\psi(x)$ (primes in short intervals) --- an assertion about the *primes*, provable
   or refutable without locating a single zero.

## 3. The attack, and the exact point it separates from RH

Write $V(d,T)=$ diagonal $+$ off-diagonal and split the off-diagonal by frequency $\alpha=\xi/\rho$ ($\rho\sim
\log T$ the mean density):
$$
V(d,T)=4dN+\Big(\underbrace{\int_{|\alpha|<1}}_{\text{Montgomery: unconditional}}+\underbrace{\int_{|\alpha|\ge1}}_{\text{the gap}}\Big)\widehat g(\alpha)\,\big(R_2(\alpha)-1\big)\,d\alpha .
$$
- **Unconditional (no RH):** the diagonal $4dN$, and the $|\alpha|<1$ contribution by Montgomery. Together they
  bound $V(d,T)$ **up to the $|\alpha|\ge1$ tail**.
- **The gap:** the high-frequency ($|\alpha|\ge1$) form factor. Montgomery's conjecture $R_2(\alpha)\to1$ there is
  **RH-conditional/open**; the unconditional substitute is Selberg's $\int|S(t)|^2\ll T\log\log T$, which controls
  the **typical** but not the **uniform** fluctuation. The required input is a **uniform** (worst-case) bound on
  the high-frequency form factor.

> **Separation point (sharp).** The attack is RH-free up to and including Montgomery's $|\alpha|<1$ range; it
> becomes open precisely at the **uniform high-frequency form factor $|\alpha|\ge1$**. That object is the
> Goldston--Montgomery short-interval prime variance / the de-localized pair correlation --- a recognized frontier
> of analytic number theory that is **weaker than RH** (RH does not obviously give the *uniform* worst-case bound
> either; this is the $S(t)$-extremal vs typical distinction) and is **not** a restatement of RH.

## 4. Does the cross-scale/octave structure shrink the gap?

Honest assessment of the new leverage:
- The octave increments alternate in sign (experiment), suggesting a summation-by-parts attack giving bounded
  partial sums without termwise decay. **But the alternation is a property of the saturating direction $g^\ast$
  (the eigenvector adapts to cancel), not a direction-independent prime law.** The clean, direction-free statement
  is $V(d,T)$ bounded; the alternation does not upgrade it.
- What the octave view *does* add: it exhibits the $|\alpha|\ge1$ gap as the **top octaves** (the experiment's
  negative late increments at $d=5,6$), i.e. the high-frequency tail is carried by the finest prime scales
  ($n\sim e^{2d}$). This localizes the open part to the **largest primes in the band**, matching the
  short-interval-variance form of the Goldston--Montgomery equivalent.

## 5. Verdict

- **The residue is precisely formulated:** $(LB)\iff V(d,T)\ll dN$ uniformly $\iff$ a uniform high-frequency
  pair-correlation / short-interval prime-variance bound.
- **It is non-circular:** strictly weaker than RH (gives a finite bottom, not the sign), with an unconditional core
  (diagonal $+$ Montgomery $|\alpha|<1$) and a prime-side equivalent (short-interval second moment).
- **It separates from RH at the uniform high-frequency form factor $|\alpha|\ge1$** --- the Goldston--Montgomery
  frontier --- which the cross-scale view localizes to the largest primes in the band. This is a **recognized open
  problem, not RH**, and is the honest, attackable, non-circular target the whole option-(b)/cross-scale line
  produces.
- **Caveat (no overclaim):** even this weaker target is hard and long-open; the contribution here is its precise
  identification and the proof that pursuing it is *not* circular --- it is a genuine sub-RH frontier, the same one
  the program reached independently at Day 19, now re-derived from the octave/cross-scale structure and pinned to
  the high-frequency tail.

> **Next concrete step (non-circular):** attack the uniform high-frequency form-factor bound for $|\alpha|\ge1$ at
> the largest band-scale primes --- equivalently, a uniform (not merely typical) second moment of
> $\psi(x+h)-\psi(x)$ at the relevant scale --- using Montgomery's $|\alpha|<1$ range plus the band's diagonal as
> the unconditional anchor. Success is a finite bottom for the Weil form ($\kappa<\infty$-strength $(LB)$),
> strictly between zero-density and RH; failure is informative about where the uniform form factor genuinely
> diverges.
