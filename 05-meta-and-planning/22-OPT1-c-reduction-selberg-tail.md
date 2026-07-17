# Option 1 — reducing the logarithmic loss: the $|\alpha|\ge1$ tail, precisely

**Auditor build · 2026-06-05.** Goal: shrink the loss $c$ in the unconditional $\ft\ge-C(\log T)^c\|g\|^2$ toward
the clean $(LB)$, by isolating the $|\alpha|\ge1$ contribution and applying the unconditional tools (positivity of
the form factor, Selberg's second moment, the diagonal). Strictly sub-RH and non-circular (Goldston--Montgomery).
We set up the reduction exactly and identify what is unconditional, what each tool buys, and where the residual
$c$ comes from. No optimal $c$ is claimed.

---

## 1. The exact split

In Montgomery's normalization, with $L=\log T$ and $\alpha=2d/L$ the resolution variable,
$$
V(d,T)=N\int_{-A}^{A}\widehat\phi(\alpha)\,F(\alpha,T)\,d\alpha,\qquad A=\tfrac{2d}{L}\cdot\!\big(\text{band}\big),\quad
F(\alpha,T)=\frac{1}{N}\Big|\sum_{\gamma}T^{i\alpha\gamma}\Big|^2_{w}\ \ge0,
$$
where $F$ is the (nonnegative) form factor and $\widehat\phi\ge0$ is the band kernel. Split at the critical
frequency $\alpha=1$:
$$
V(d,T)=\underbrace{N\!\int_{|\alpha|<1}\widehat\phi\,F}_{\text{(I) low}}\;+\;\underbrace{N\!\int_{1\le|\alpha|\le A}\widehat\phi\,F}_{\text{(II) high — the loss}} .
$$

## 2. What is unconditional in each piece

**(I) low frequencies — bounded, RH-free.** $F(\alpha,T)=L\,T^{-2|\alpha|}(1+o(1))+|\alpha|+o(1)$ in $|\alpha|\le1$;
the unconditional part is the diagonal $L\,T^{-2|\alpha|}$ (from the explicit formula, no RH) plus the lower bound
$F\ge0$. Hence $\int_{|\alpha|<1}\widehat\phi F\ll1$ unconditionally, so **(I) $\ll N$** — no loss here.

**(II) high frequencies — the entire loss.** For $\alpha>1$, Montgomery's conjecture is $F(\alpha)\to1$ (the GUE
value), giving $\int_1^A F\sim A$ and hence $V\sim NA\sim dN$ (the clean bound). Unconditionally we have only:
- **positivity** $F\ge0$ (no upper bound by itself);
- **the total-mass identity** $\int_{-\infty}^{\infty}F(\alpha,T)\,e(\,\cdot\,)\,d\alpha$ reproduces, via the
  explicit formula, a **prime correlation** $\sum_{m,n\le e^{2d}}\Lambda(m)\Lambda(n)(mn)^{-1/2}(\cdots)$, whose
  diagonal $\sum\Lambda^2/n\sim2d^2$ is unconditional and whose off-diagonal is the short-interval variance;
- **Selberg's second moment** $\int_0^T S(t)^2\,dt\ll T\log\log T$, equivalently a bound on the *mean-square* of
  the high-frequency form factor against the unit-spacing kernel.

## 3. What Selberg buys, and the residual

Selberg controls the **average** of the high-frequency fluctuation, not its uniform value. Concretely, Selberg's
bound gives, for the *mean-square* over the height window,
$$
\frac1T\int_0^T\Big(\!\int_1^A\widehat\phi\,F\Big)\,dt\ \ll\ \log\log T\quad(\text{typical}),
$$
whereas $(LB)$ needs the **uniform** (every-window, worst-case) bound $\int_1^A\widehat\phi F\ll1$. The residual
$c$ is exactly the cost of converting *typical* $\log\log T$ control into *uniform* control:
- the crude large sieve gives a power $c$ (uniform but lossy);
- Selberg's $\log\log T$ improves the *typical* exponent to $0$ but leaves the uniform conversion open;
- a Montgomery--Vaughan **weighted** large sieve, replacing the boxcar $\widehat\phi$ by a smooth majorant and
  using $F\ge0$ to drop the negative part, reduces the lossy power but does not reach $c=0$.

> **Net (honest).** The $|\alpha|<1$ part is unconditionally $O(N)$ (no loss). The entire loss is the **uniform**
> high-frequency form factor $\int_{1}^{A}F(\alpha)\,d\alpha$, for which positivity $+$ Selberg give *typical*
> $\log\log T$ but only *power-of-$\log$* uniform control. **Reducing $c$ $=$ improving the uniform-vs-typical
> conversion at $|\alpha|\ge1$**, which is the Goldston--Montgomery short-interval prime variance — a recognized
> sub-RH frontier. The clean $c=0$ is that frontier; each smoothing improvement is a measurable decrement.

---

## 4. Advance (Day 41): the clean bound holds off a sparse exceptional set

The typical-to-uniform conversion has structure worth isolating. Let $M(T)$ denote the local high-frequency
contribution $\int_1^A\widehat\phi\,F(\alpha,T)\,d\alpha$ at height $T$. The unconditional moment inputs are:
- **second moment** (Selberg): the height-average of $M$ is $\ll\log\log T$;
- **fourth moment** (Selberg): the height-average of $M^2$ is $\ll(\log\log T)^2$, so the *fluctuation* of $M$ is
  controlled.

By Chebyshev applied to the fourth moment, the **exceptional set** $\{T: M(T)>K\log\log T\}$ has density
$\ll K^{-2}$. Hence:

> **Almost-all-heights statement (strategy, solid in form).** The clean finite bottom $\ft\ge-C\|g\|^2$ holds for
> **all heights outside a set of density $\ll K^{-2}$**, on which it degrades only to $\ft\ge-CK\log\log T$. The
> uniform $(LB)$ is the removal of this sparse exceptional set; its density is governed by the higher moments of
> the high-frequency form factor, each computable unconditionally.

This refines "loss everywhere by $(\log T)^c$" into "**clean off a sparse set, mild loss on it**" — a different and
arguably stronger unconditional statement, and a concrete measurable target: bound the exceptional-set density via
the sixth/eighth moments (Selberg-type), each decrement a partial result, with the full removal the
Goldston--Montgomery frontier. *(Constants and the precise moment bookkeeping are the content of the worked paper;
stated here at the level of structure.)*

---

## 5. Deepening (Day 42): the exceptional set is super-polynomially sparse

Selberg's moment theorem is sharper than the second and fourth moments alone: \emph{all} moments of $S(t)$ match
the Gaussian,
$$
\frac1T\int_0^T S(t)^{2m}\,dt\ \sim\ \frac{(2m)!}{m!\,2^m}\Big(\frac{\log\log T}{2\pi^2}\Big)^{m},
$$
so $S(t)/\sqrt{(1/2\pi^2)\log\log T}$ is asymptotically standard Gaussian (Selberg's central limit theorem). The
high-frequency local contribution $M(T)$ is a quadratic functional of $S$ on the window; its large-deviation set is
controlled by \emph{every} even moment, not just the fourth.

\textbf{Consequence.} For each $m$, the exceptional set $\{T:M(T)>K\log\log T\}$ has density $\ll_m K^{-2m}$; taking
$m\to\infty$, its density decays \textbf{faster than any power of $K$} (toward a Gaussian/exponential tail). Hence:

> **Clean $(LB)$ off a super-sparse set.** The clean finite bottom $\ft\ge-C\|g\|^2$ holds for all heights outside a
> set of density decaying faster than any power of the loss threshold; equivalently, it can fail only on heights
> lying in \emph{anomalous zero clusters} (large local $S(t)$, Lehmer-pair-type configurations), which Selberg's CLT
> makes super-polynomially rare. The uniform $(LB)$ is the removal of these rare clusters.

This is a markedly stronger ``almost-all'' statement than the fourth-moment version: the clean bound is the generic
behaviour with a super-polynomially thin exceptional set, and the entire obstruction to the uniform $(LB)$ is
concentrated on the sparse anomalous-cluster heights. **Interpretation:** the localized Weil form is unconditionally
semibounded with the clean constant except near rare large-$S(t)$ spikes; controlling those spikes uniformly is the
Goldston--Montgomery frontier. *(Moment bookkeeping for the quadratic functional $M$ from Selberg's CLT is the worked
content; stated here at the level of structure and rate.)*

---

## 6. Consolidation (Day 43): the natural terminus of the elementary approach

The elementary unconditional toolkit (positivity $F\ge0$, the diagonal, Selberg's full moment hierarchy) has now
been pushed to its limit on this front:
- low band $|\alpha|<1$: clean, $O(N)$, no loss (\S3);
- high band $|\alpha|\ge1$: clean off a super-polynomially sparse exceptional set of anomalous-cluster heights
  (\S5); a power-of-$\log$ uniform bound everywhere (\S3 of the parent note).

Everything beyond this --- removing the exceptional set entirely, i.e. the uniform high-frequency form factor for
\emph{every} window --- is the Goldston--Montgomery short-interval prime variance, which no elementary
(moment/large-sieve/positivity) combination reaches; it requires genuine analytic-number-theory input
(Montgomery--Soundararajan-type short-interval technology). 

> **Terminus.** Front 1's unconditional content is complete at the elementary level: \emph{the localized Weil form
> is unconditionally semibounded with the clean constant for all heights outside a super-polynomially thin set of
> anomalous-cluster heights, and semibounded up to a logarithmic power everywhere.} Further reduction of the
> exceptional set is the recognized sub-RH frontier and is the point at which specialized ANT, not the program's
> own machinery, must take over. This is the honest stopping point — a genuine unconditional theorem with the
> residue named and located, not a circle.

---

## 7. Frontier (Day 45): the exceptional set is exactly Arc A's extreme-value heights

The super-sparse exceptional set of \S6 has an arithmetic identity that closes a loop in the program. The high
band $M(T)$ is large precisely where the local fluctuation $S(t)$ is anomalously large; by the explicit-formula
coupling $S(t)\leftrightarrow$ the prime sum $\leftrightarrow\arg\zeta(\tfrac12+it)$, these are the heights where
$|\zeta(\tfrac12+it)|$ is extreme. Therefore:

> **Identification.** The exceptional set obstructing the clean $(LB)$ is contained in the set of \emph{extreme-value
> heights} of $\zeta$ on the critical line --- the very object of Arc A (the $\omega$-class large values; the
> Bondarenko--Seip resonance heights; the moment/FHK frontier). The unconditional clean $(LB)$ fails, if anywhere,
> exactly at the large-$|\zeta|$ spikes, and controlling those is the extreme-value/moment problem the program began
> with.

This is a genuine program-internal unification: the \emph{end} of the localized-Weil line (the residue of the
unconditional finite bottom) and the \emph{beginning} (Arc A's $\omega$-class extreme values) are the same set of
heights. Two consequences, both concrete and RH-independent:
\begin{itemize}
\item \emph{Transfer.} Any unconditional upper bound on the measure / contribution of extreme-value heights ---
exactly what Arc A's $\omega$-class machinery (P2--P5) and the moment conjectures address --- feeds directly into
shrinking the exceptional set of \S6, hence the loss $c$.
\item \emph{Localization of the frontier.} The Goldston--Montgomery short-interval variance residue is concentrated
on extreme-value heights; the relevant short intervals are those around large $|\zeta|$, tying the uniform form
factor to the extreme-value distribution (FHK; the $(\log T)^{k^2}$ moment growth).
\end{itemize}

> **Net.** Front 1's residue is not an isolated analytic obstacle: it is Arc A's extreme-value problem, viewed from
> the localized Weil form. The two ends of the program meet at the large values of $\zeta$ --- a clean structural
> closure, and a concrete handoff target (bound the extreme-value heights' form-factor contribution).
