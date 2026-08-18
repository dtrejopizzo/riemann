# 113.06 — The canonical Weil decomposition on $\mathcal A$, and the $\log p$ defect

> **What this file does.** It replaces 113_03's *definition* of $\mathfrak T$
> by a *theorem*. On the admissible class $\mathcal A$ the identity
> $$\widehat h(0)+\widehat h(1)-\sum_\rho m_\rho\widehat h(\rho)
>   \;=\;\sum_p\log p\,\bigl[A_p(h)+B_p(h)\bigr]\;-\;A(h)$$
> is proved from the Hadamard/functional-equation structure of $\xi$ alone,
> for every $h$ with $\tilde h\in\mathcal S_\eta$, $\eta>1$ — with **no
> assumption**, and in particular without $h(1)=0$. Along the way three
> defects in 113_01–113_04 are located and corrected: a missing $\log p$ at
> every finite place, a double count of the whole Weil right-hand side in
> 113_03 Definition 4.1, and the resulting mis-statement of Assumption T.
> What remains of Assumption T is isolated, named T2, and is strictly
> smaller than what 111_01 and 113_03 carried.

Status flags set by this file:

$$\boxed{\texttt{WEIL\_DECOMPOSITION\_ON\_SCHWARTZ\_DATA: PROVED}}$$
$$\boxed{\texttt{ASSUMPTION\_T1 (spectral side = arithmetic side on }\mathcal A): \texttt{DISCHARGED}}$$
$$\boxed{\texttt{ASSUMPTION\_T2 (operator-trace limit = arithmetic side): OPEN, REDUCED}}$$
$$\boxed{\texttt{ROW\_A\_STATUS: partial (unchanged by this file)}}$$

---

## 1. Conventions, the class, and the two elementary lemmas

Throughout, **convention B** of 113_05 Decision 1.1:

$$\widehat f(s)=\int_0^\infty f(u)\,u^{s}\,d^\times u=\int_{-\infty}^{\infty}\tilde f(x)e^{sx}\,dx,
\qquad \tilde f(x)=f(e^x),\quad d^\times u=\frac{du}{u}. \tag{1.1}$$

$$\mathcal S_\eta=\Bigl\{\tilde h\in\mathcal S(\mathbb R):\ \forall N\ \exists C_N,\
|\tilde h(x)|\le C_N(1+|x|)^{-N}e^{-\eta|x|}\Bigr\},
\qquad \mathcal S_{>1}=\bigcup_{\eta>1}\mathcal S_\eta. \tag{1.2}$$

$$\mathcal A=\bigl\{h:\ \tilde h\in\mathcal S_{>1},\ h(1)=\tilde h(0)=0\bigr\}
\qquad\text{(113\_03 Definition 1.1).} \tag{1.3}$$

$\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, entire of order one,
$\xi(s)=\xi(1-s)$; $Z$ is its zero set, $m_\rho$ the multiplicity.

> ### Lemma 1.1 (holomorphy and rapid decay in a strip)
> Let $\tilde h\in\mathcal S_\eta$ with $\eta>1$. Then $\widehat h$ is
> holomorphic on the strip $|\operatorname{Re}s|<\eta$, and for every
> $c<\eta$ and every $N$ there is $C=C(N,c)$ with
> $$|\widehat h(\sigma+i\tau)|\le C(1+|\tau|)^{-N}
> \qquad\text{for all }|\sigma|\le c,\ \tau\in\mathbb R. \tag{1.4}$$

**Proof.** For $|\sigma|\le c<\eta$ the function $x\mapsto\tilde h(x)e^{\sigma x}$
is Schwartz, with all its Schwartz seminorms bounded uniformly in $\sigma$ on
$|\sigma|\le c$ (each derivative of $\tilde h$ inherits the bound (1.2), and
$e^{(c-\eta)|x|}$ is bounded). Now $\widehat h(\sigma+i\tau)$ is the Fourier
transform of that function at $-\tau$, and the Fourier transform maps a
seminorm-bounded family of Schwartz functions to a seminorm-bounded family.
Holomorphy is Morera plus the same domination. $\square$

> ### Lemma 1.2 (Mellin inversion on every line of the strip)
> For $\tilde h\in\mathcal S_\eta$, every $c'$ with $|c'|<\eta$, and every
> $x>0$,
> $$\frac1{2\pi i}\int_{(c')}\widehat h(s)\,x^{-s}\,ds=h(x). \tag{1.5}$$

**Proof.** Write $s=c'+i\tau$. Then $\widehat h(c'+i\tau)$ is the Fourier
transform of $\tilde h(\cdot)e^{c'\cdot}$ at $-\tau$; (1.4) makes it integrable;
Fourier inversion at the point $y=\log x$ gives
$\tilde h(y)e^{c'y}=\frac1{2\pi}\int\widehat h(c'+i\tau)e^{-i\tau y}d\tau$,
which is (1.5). $\square$

These two lemmas are the only analytic input; everything below is contour
work. Neither uses a zero of $\xi$.

---

## 2. The canonical decomposition

> ### Definition 2.1 (the archimedean functional)
> For $\tilde h\in\mathcal S_{>1}$ put
> $$\boxed{\;A(h):=\frac1{2\pi}\int_{-\infty}^{\infty}
> \Bigl[\tfrac12\operatorname{Re}\psi\bigl(\tfrac14+\tfrac{it}2\bigr)-\tfrac12\log\pi\Bigr]
> \bigl[\widehat h(\tfrac12+it)+\widehat h(\tfrac12-it)\bigr]\,dt\;}
> \tag{2.1}$$
> and $W_\infty(h):=-A(h)$.

The bracketed kernel is $\operatorname{Re}\bigl(\Gamma_{\mathbb R}'/\Gamma_{\mathbb R}\bigr)(\tfrac12+it)$
for $\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)$: it is built from the
archimedean factor of $\xi$ and from nothing else. The integral converges
absolutely, since $\psi(\tfrac14+\tfrac{it}2)=O(\log(2+|t|))$ and
$\widehat h(\tfrac12\pm it)$ decays faster than every polynomial by Lemma 1.1.

> ### Theorem 2.2 (canonical Weil decomposition on $\mathcal S_{>1}$)
> Let $\tilde h\in\mathcal S_\eta$ with $\eta>1$. Then $\sum_\rho m_\rho\widehat h(\rho)$
> converges absolutely, $\sum_n\Lambda(n)\bigl[h(n)+h(1/n)n^{-1}\bigr]$
> converges absolutely, and
> $$\boxed{\;\widehat h(0)+\widehat h(1)-\sum_{\rho\in Z}m_\rho\widehat h(\rho)
> \;=\;\sum_{n\ge1}\Lambda(n)\Bigl[h(n)+\frac{h(1/n)}{n}\Bigr]\;-\;A(h).\;}
> \tag{2.2}$$
> No hypothesis on $h(1)$ is needed.

**Proof.** Fix $c$ with $1<c<\eta$ and put
$$G(s):=\widehat h(s)+\widehat h(1-s),$$
holomorphic on $1-\eta<\operatorname{Re}s<\eta$, a strip containing
$[1-c,c]\supset[0,1]$. By construction $G(1-s)=G(s)$; on the line
$\operatorname{Re}s=\tfrac12$ this says $G(\tfrac12+it)$ is **even in $t$**.
By Lemma 1.1, $G$ decays faster than every polynomial on every vertical line
of that strip, uniformly.

*Step 1 (the zero sum as a contour integral).* $\xi'/\xi$ is meromorphic with
simple poles exactly at $Z$, residues $m_\rho$, and no other singularity in
$\mathbb C$ apart from those (the trivial zeros and the pole of $\zeta$ are
cancelled inside $\xi$). Take the rectangle with vertical sides
$\operatorname{Re}s=c$ and $\operatorname{Re}s=1-c$ and horizontal sides at
$\pm T$. Since $c<\eta$, all zeros lie strictly inside the vertical strip
$0\le\operatorname{Re}s\le1$. On a sequence $T_j\to\infty$ chosen to avoid
ordinates of zeros one has $|(\xi'/\xi)(\sigma\pm iT_j)|=O(\log^2 T_j)$
uniformly for $1-c\le\sigma\le c$ — this is the standard unconditional bound
that accompanies the Riemann–von Mangoldt formula, quoted here, and it is used
only to discard horizontal segments, never to locate a zero. Against the
super-polynomial decay (1.4) the horizontal contributions tend to $0$. Hence
$$\sum_{\rho}m_\rho\widehat h(\rho)
=\frac1{2\pi i}\Bigl[\int_{(c)}-\int_{(1-c)}\Bigr]\frac{\xi'}{\xi}(s)\,\widehat h(s)\,ds,$$
absolutely convergent because $|\widehat h(\rho)|$ decays super-polynomially in
$|\operatorname{Im}\rho|$ uniformly for $0\le\operatorname{Re}\rho\le1$ while
$\#\{\rho:|\operatorname{Im}\rho|\le T\}=O(T\log T)$.
Substituting $s\mapsto1-s$ in the left integral and using
$(\xi'/\xi)(1-s)=-(\xi'/\xi)(s)$,
$$\sum_{\rho}m_\rho\widehat h(\rho)
=\frac1{2\pi i}\int_{(c)}\frac{\xi'}{\xi}(s)\,G(s)\,ds. \tag{2.3}$$

*Step 2 (split the logarithmic derivative).*
$$\frac{\xi'}{\xi}(s)=\underbrace{\frac1s+\frac1{s-1}}_{\text{polar}}
\;\underbrace{-\tfrac12\log\pi+\tfrac12\psi(s/2)}_{\text{archimedean}}
\;+\;\underbrace{\frac{\zeta'}{\zeta}(s)}_{\text{arithmetic}}. \tag{2.4}$$
Each of the three pieces, paired against $G$, is separately absolutely
convergent on $\operatorname{Re}s=c$: the first is $O(|s|^{-1})$, the second
$O(\log|s|)$, the third is bounded there since $c>1$.

*Step 3 (the polar piece contributes exactly $\widehat h(0)+\widehat h(1)$).*
Shift $\operatorname{Re}s=c$ to $\operatorname{Re}s=\tfrac12$. The only
singularity crossed is the simple pole of $1/(s-1)$ at $s=1$, of residue
$G(1)=\widehat h(1)+\widehat h(0)$. Hence
$$\frac1{2\pi i}\int_{(c)}\Bigl[\frac1s+\frac1{s-1}\Bigr]G(s)\,ds
=\widehat h(0)+\widehat h(1)
+\frac1{2\pi i}\int_{(1/2)}\Bigl[\frac1s+\frac1{s-1}\Bigr]G(s)\,ds .$$
On $s=\tfrac12+it$,
$$\frac1s+\frac1{s-1}=\frac{(s-1)+s}{s(s-1)}=\frac{2it}{-\tfrac14-t^2}
=\frac{-2it}{\tfrac14+t^2},$$
which is **odd** in $t$, while $G(\tfrac12+it)$ is **even** in $t$. With
$ds=i\,dt$ the remaining integral is
$\frac1{2\pi}\int_{\mathbb R}\frac{2t}{\frac14+t^2}G(\tfrac12+it)\,dt$,
an absolutely convergent integral of an odd function, hence $0$. So the polar
piece equals $\widehat h(0)+\widehat h(1)$ exactly.

> Note where the symmetrisation earns its keep: the vanishing uses only
> $G(1-s)=G(s)$, **not** reality of $h$. This is why the theorem holds for the
> complex $h=f\star\widetilde g$ that the pairing actually produces.

*Step 4 (the archimedean piece is $A(h)$).* $\psi(s/2)$ is holomorphic for
$\operatorname{Re}s>0$, so the shift from $c$ to $\tfrac12$ crosses nothing:
$$\frac1{2\pi i}\int_{(c)}\Bigl[\tfrac12\psi(s/2)-\tfrac12\log\pi\Bigr]G(s)\,ds
=\frac1{2\pi}\int_{\mathbb R}\Bigl[\tfrac12\psi\bigl(\tfrac14+\tfrac{it}2\bigr)-\tfrac12\log\pi\Bigr]G(\tfrac12+it)\,dt .$$
Since $G(\tfrac12+it)$ is even in $t$, only the even part of the kernel
survives, and the even part of $\psi(\tfrac14+\tfrac{it}2)$ is
$\operatorname{Re}\psi(\tfrac14+\tfrac{it}2)$ (because
$\psi(\bar z)=\overline{\psi(z)}$). This is exactly $A(h)$ of (2.1).

*Step 5 (the arithmetic piece).* For $\operatorname{Re}s=c>1$,
$\zeta'/\zeta(s)=-\sum_{n\ge1}\Lambda(n)n^{-s}$ absolutely, and
$\int_{(c)}|G|\,|ds|<\infty$, so we may interchange:
$$\frac1{2\pi i}\int_{(c)}\frac{\zeta'}{\zeta}(s)G(s)\,ds
=-\sum_n\Lambda(n)\,\frac1{2\pi i}\int_{(c)}\bigl[\widehat h(s)+\widehat h(1-s)\bigr]n^{-s}\,ds .$$
By Lemma 1.2 the first term gives $h(n)$. For the second, substitute $w=1-s$;
the contour $\operatorname{Re}s=c$ traversed upward becomes
$\operatorname{Re}w=1-c$ traversed upward (two sign reversals cancel), and
$$\frac1{2\pi i}\int_{(c)}\widehat h(1-s)n^{-s}ds
=\frac1n\cdot\frac1{2\pi i}\int_{(1-c)}\widehat h(w)\,(n^{-1})^{-w}dw
=\frac{h(1/n)}{n},$$
using Lemma 1.2 again with $c'=1-c$ (legitimate: $|1-c|<\eta$). So the
arithmetic piece is $-\sum_n\Lambda(n)[h(n)+h(1/n)/n]$, absolutely convergent
because $|h(n)|\le C n^{-\eta}$ and $\eta>1$.

*Conclusion.* Insert Steps 3–5 into (2.3):
$$\sum_\rho m_\rho\widehat h(\rho)
=\widehat h(0)+\widehat h(1)+A(h)-\sum_n\Lambda(n)\Bigl[h(n)+\frac{h(1/n)}n\Bigr],$$
which rearranges to (2.2). $\square$

---

## 3. The finite side, and the $\log p$ defect in 113_01–113_03

Group the prime powers. With 113_01 Theorem 2.1's notation
$$A_p(h)=\sum_{k\ge1}h(p^k),\qquad B_p(h)=\sum_{m\ge1}h(p^{-m})p^{-m},$$
one has $\Lambda(n)\ne0$ only for $n=p^k$, where $\Lambda(p^k)=\log p$, so

> ### Corollary 3.1 (the canonical finite side)
> $$\boxed{\;P(h):=\sum_n\Lambda(n)\Bigl[h(n)+\frac{h(1/n)}n\Bigr]
> =\sum_p\log p\;\bigl[A_p(h)+B_p(h)\bigr],\;}$$
> and (2.2) reads $\;\widehat h(0)+\widehat h(1)-\sum_\rho m_\rho\widehat h(\rho)=P(h)+W_\infty(h)$.

113_01 Theorem 2.1 computes the local term as $A_p+B_p+h(1)\bigl(\frac{p-2}{p-1}+K\bigr)$
— that is, **without** the factor $\log p$ — because it evaluates the Tate local
integral with $\operatorname{vol}(\mathbb Z_p^\times)=1$ rather than with the
normalisation that makes the product formula hold. 113_02 and 113_03 inherit it.

> ### Correction 3.2 (the $\log p$ defect)
> Everywhere in 113_01, 113_02 and 113_03 the local contribution of the prime
> $p$ must carry the weight $\log p$:
> $$\mathfrak T_{\rm fin}(h)=\sum_p\log p\,\bigl[A_p(h)+B_p(h)\bigr],$$
> not $\sum_p[A_p(h)+B_p(h)]$.

This is not a convention. 113_02 Proposition 3.1 had already *observed* the
numerical discrepancy — $0.624192732$ against $1.188538843$ — and filed it as
"different objects". It is one missing $\log p$ per prime. The verifier shows
that with the weight the identity closes to $10^{-13}$ on five probes, and
without it fails by $1.6\%$ to $28\%$ depending on the probe; and that the
error is not proportional to $\widehat h(1)$ (the ratio spread is
$0.0136$ to $0.1417$ across probes), so no single global rescaling can absorb
it. Independent confirmation at 40-digit precision, on probes designed so that
each of the three terms in turn dominates, is recorded in §7.

> ### Theorem 3.3 (the threshold $\eta>1$ survives the correction)
> For $\tilde h\in\mathcal S_\eta$: $\sum_p\log p\,|A_p(h)|<\infty$ iff the
> decay rate satisfies $\eta>1$, and $\sum_p\log p\,|B_p(h)|<\infty$ for every
> $\eta>0$. Hence 113_01 Theorem 4.1 and 113_02 Theorem 2.1 hold verbatim once
> the weight is inserted, with the same threshold and the same sharpness.

**Proof.** $|h(p^k)|\le C p^{-\eta k}$, so $|A_p|\le C'p^{-\eta}$ and the
weighted sum is dominated by $\sum_p(\log p)p^{-\eta}$, convergent iff
$\eta>1$ (and divergent at $\eta=1$, where it is $\sim\log\log X$ by Mertens).
For $B_p$ the extra $p^{-m}$ raises the exponent by one:
$|B_p|\le C'p^{-(\eta+1)}$ and $\sum_p(\log p)p^{-(\eta+1)}$ converges for
every $\eta>0$. $\square$

The verifier tests this in the sharp form: by the prime number theorem the
increment of $\sum_{p\le N}(\log p)p^{-a}$ over a block $[N,4N]$ is
$\sim\int_N^{4N}t^{-a}dt$, so successive block increments have ratio exactly
$4^{1-a}$, which is $<1$ iff $a>1$. Measured against predicted:
$\eta=1.4$: $0.5727$ vs $0.5743$; $\eta=1.2$: $0.7556$ vs $0.7579$;
$\eta=1.0$: $0.9967$ vs $1.0000$; $\eta=0.8$: $1.3137$ vs $1.3195$. The $B_p$
half at $\eta=0.5$ gives $0.4986$ against the predicted $4^{-1/2}=0.5$ while
its $A_p$ half is at $1.9746$ — the two halves are separated by a full power
of $p$, exactly as the proof says.

> ### Correction 3.4 (the double count in 113_03)
> 113_03 Definition 3.1 names the **entire** Weil right-hand side
> $\widehat h(0)+\widehat h(1)-\sum_\rho\widehat h(\rho)$ "the archimedean
> contribution $\mathfrak T_\infty$", and Definition 4.1 then sets
> $\mathfrak T:=\mathfrak T_\infty+\mathfrak T_{\rm fin}$. Since the Weil
> right-hand side already *contains* the finite places, this adds them twice.
> The corrected definition is
> $$\mathfrak T_\infty(h):=W_\infty(h)=-A(h),\qquad
> \mathfrak T(h):=W_\infty(h)+\mathfrak T_{\rm fin}(h),$$
> and by Corollary 3.1 the statement
> $\mathfrak T(h)=\widehat h(0)+\widehat h(1)-\sum_\rho m_\rho\widehat h(\rho)$
> is then a **theorem** on all of $\mathcal S_{>1}$, not a definition and not
> an assumption.

113_01, 113_02 and 113_03 Theorem 2.2 are otherwise untouched: they concern
$\mathfrak T_{\rm fin}$ alone, and Theorem 3.3 above preserves their content.

$W_\infty$ is defined here from the archimedean factor $\Gamma_{\mathbb R}$ of
$\xi$, not from a Tate local integral. That is deliberate: the Tate integral at
$\infty$ carries a choice of Haar normalisation on $\mathbb R^\times$ which the
finite places fix only through the product formula, and 113's earlier numerics
were contaminated by exactly that freedom (three probes gave $W_\infty$ values
$0.5$, $0.25$, $0.5$, which is the signature of a quadrature failing at the
$x=0$ jump rather than of a computed local integral). Reading $W_\infty$ off
the $\Gamma$-factor removes the freedom: the identity (2.2) then holds with no
residual constant, which the 40-digit run in §7 confirms on a probe with
$h(1)=1$, where any missing $\tfrac12h(1)$ or $h(1)\log2\pi$ term would show up
immediately and does not.

---

## 4. No renormalisation is needed on $\mathcal A$

107_239 (1.4) defines $\mathfrak T_S$ as a limit of truncated traces minus a
counterterm $2h(1)\log\Lambda$.

> ### Theorem 4.1 (the counterterm vanishes identically on $\mathcal A$, and every local term converges absolutely)
> Let $h\in\mathcal A$, so $h(1)=0$.
> 1. The counterterm $2h(1)\log\Lambda$ is identically zero for every $\Lambda$.
> 2. At each finite place, the two series $A_p(h),B_p(h)$ converge absolutely
>    and the scheme-dependent term $h(1)\bigl(\frac{p-2}{p-1}+K\bigr)$ of
>    113_01 Theorem 2.1 vanishes, so the local value is scheme-free.
> 3. At the archimedean place, the integrand $h(u^{-1})/|1-u|$ of the Tate
>    local integral is bounded near $u=1$ and integrable on $\mathbb R^\times$;
>    no principal value is required.

**Proof.** (1) is immediate. (2) is 113_01 Theorem 4.1 with the weight of
Correction 3.2, which does not affect a single place. For (3): $\tilde h$ is
smooth with $\tilde h(0)=0$, so $\tilde h(x)=O(|x|)$ as $x\to0$; writing
$u=e^{-x}$, $h(u^{-1})=\tilde h(x)=O(|x|)=O(|1-u|)$, hence
$h(u^{-1})/|1-u|=O(1)$ at $u=1$. Away from $u=1$ the numerator decays like
$|u|^{\pm\eta}$ with $\eta>1$, which dominates $1/|1-u|\to1$. $\square$

So on $\mathcal A$ the object is an candid sum of absolutely convergent local
terms, with the "renormalisation" of 107_239 (1.4) degenerate. This is the
positive content of the $h(1)=0$ condition: not a technical nuisance, but
exactly the condition that makes every place of $\mathbb Q$ contribute a
convergent integral with no regularisation at all.

Note the disambiguation flagged by 111_01 §3 is now settled by usage: the
$h(1)$ of 107_239 (1.4), of 113_01 Theorem 2.1, and of $\mathcal A$ is the
value $\tilde h(0)$ at the group identity — reading (a) — since that is the
quantity multiplying the local divergence at $u=1$. It is **not**
$\widehat h(1)$. By 113_05 Proposition 4.1, for $h=f\star\widetilde g$,
$$h(1)=\int_0^\infty f(u)\,\overline{g(u)}\,d u. \tag{4.1}$$

---

## 5. What is left of Assumption T

111_01 §3's Assumption T bundles two independent claims. Separate them.

**T1 (spectral side = arithmetic side on $\mathcal A$).** That
$\widehat h(0)+\widehat h(1)-\sum_\rho m_\rho\widehat h(\rho)$ equals the sum
of local Weil terms over all places, for $h$ merely Schwartz-with-exponential-decay
rather than compactly supported.

> **T1 is discharged.** It is Theorem 2.2 together with Corollary 3.1 and
> Correction 3.4. The proof needed nothing about compact support, only Lemma
> 1.1's decay in a strip of half-width $\eta>1$ — which is precisely why the
> threshold is $\eta>1$ and not something softer.

**T2 (operator-trace limit = arithmetic side).** That
$\lim_{\Lambda\to\infty}\operatorname{Tr}_{\mathcal H_S}(\theta(h)R_\Lambda)$
exists and equals that common value, for $h\in\mathcal A$.

T2 is not discharged here. But it is now strictly smaller than what 111_01 and
113_03 carried, and it can be stated sharply:

> ### Reduction 5.1
> Let $h\in\mathcal A$ and let $h_j$ be compactly supported with
> $\tilde h_j\to\tilde h$ in the $\mathcal S_\eta$ topology, $h_j(1)=0$. The
> published semilocal trace formula gives, for each $j$,
> $\lim_\Lambda\operatorname{Tr}(\theta(h_j)R_\Lambda)=P(h_j)+W_\infty(h_j)$.
> By Theorem 3.3 and Definition 2.1 the right-hand side is continuous in the
> $\mathcal S_\eta$ topology, so $P(h_j)+W_\infty(h_j)\to P(h)+W_\infty(h)$.
> **T2 is therefore equivalent to the interchange**
> $$\lim_{j\to\infty}\ \lim_{\Lambda\to\infty}\operatorname{Tr}(\theta(h_j)R_\Lambda)
> \;=\;\lim_{\Lambda\to\infty}\ \lim_{j\to\infty}\operatorname{Tr}(\theta(h_j)R_\Lambda),$$
> i.e. to uniformity in $\Lambda$ of the convergence $\theta(h_j)\to\theta(h)$
> against the cutoff $R_\Lambda$. It is no longer a claim about the *value* of
> anything; the value is fixed by Theorem 2.2.

That is the candid residue, and it is an operator-norm question about
$R_\Lambda$, not a question about $\xi$. Note also that T2 is irrelevant to
requirement d1 as such: d1 needs a bilinear form on divisors with the right
radical, and by 113_05 Theorem 3.1 and Theorem 2.2 above, the form
$$I_\partial(D_f,D_g)=\mathfrak T(f\star\widetilde g)
=\widehat f(0)\overline{\widehat g(1)}+\widehat f(1)\overline{\widehat g(0)}
-\sum_\rho m_\rho\widehat f(\rho)\overline{\widehat g(\rho')},\qquad \rho'=1-\bar\rho,$$
is now *defined and computed* on $\mathcal A$ without reference to any operator
trace. T2 is what would be needed to keep calling it a trace; it is not needed
to use it as a pairing.

---

## 6. Corrections issued against the corpus

| # | where | defect | correction |
|---|---|---|---|
| 1 | 113_01 Thm 2.1, 113_02 Thm 2.1, 113_03 Thm 2.2 | local term lacks the weight $\log p$ | Correction 3.2; threshold $\eta>1$ unchanged (Theorem 3.3) |
| 2 | 113_02 Prop 3.1 | filed the numerical gap $0.624192732$ vs $1.188538843$ as "different objects" | it is the missing $\log p$ |
| 3 | 113_03 Def 3.1 + Def 4.1 | the whole Weil RHS is named $\mathfrak T_\infty$ and then added to $\mathfrak T_{\rm fin}$: the finite places are counted twice | Correction 3.4: $\mathfrak T_\infty:=W_\infty=-A(h)$ |
| 4 | 113_03 §3, 113_04 §3, 113_99 | "Assumption T, undischarged" | split; T1 proved (Theorem 2.2), T2 reduced (Reduction 5.1) |
| 5 | 111_01 §3 | the $h(1)$ reading (a)/(b) left open | settled: reading (a), $\tilde h(0)$; see §4 and (4.1) |

Corrections 1–3 change no verdict of 113 and no status flag; correction 4
improves one. Nothing here bears on RH.

---

## 7. Scope

**Proved here.** Lemma 1.1, Lemma 1.2. Theorem 2.2 (the canonical
decomposition on all of $\mathcal S_{>1}$, no condition on $h(1)$).
Corollary 3.1. Theorem 3.3 (threshold unchanged, with the sharp
block-ratio form). Theorem 4.1 (no renormalisation on $\mathcal A$).
Reduction 5.1 (T2 as a pure interchange-of-limits statement).

**Read from source, not re-derived.** The Hadamard factorisation of $\xi$ and
its functional equation; the unconditional bound
$(\xi'/\xi)(\sigma\pm iT_j)=O(\log^2T_j)$ on a sequence of ordinates avoiding
zeros, and $N(T)=O(T\log T)$ — both quoted only to discard horizontal contour
segments and to bound a sum, never to locate a zero; 113_01 Theorem 2.1's
closed form for the local term; 113_05 Decision 1.1, Lemma 2.3, Theorem 3.1,
Proposition 4.1.

**Verified numerically.** Theorem 2.2 on five probes at float64 (residuals
$2.7\times10^{-14}$ to $1.7\times10^{-13}$) in the verifier below, and
independently at $\mathrm{dps}=40$ with $150$ zeros up to $\gamma=318.85$ and
primes to $10^6$, giving relative residuals $\sim4\times10^{-40}$ that scale
with working precision ($5.2\times10^{-31}$ at dps 30, $1.1\times10^{-59}$ at
dps 60 — the signature of an exact identity). Three probes were built so that
each term in turn dominates: $\tilde h(x)=xe^{-100x^2}$ (zero sum twice
$\widehat h(1)$, prime sum $3\times10^{-22}$); $\tilde h(x)=e^{-x^2}$, which has
$h(1)=1$ and still closes to 40 digits, ruling out any missing $h(1)$
counterterm; and $\widehat h(\tfrac12+it)=e^{-(t-14)^2/2}+e^{-(t+14)^2/2}$,
where $\widehat h(0)=\widehat h(1)=5\times10^{-43}$ so the identity is
essentially "zero sum $=A(h)-P(h)$", and it closes to 39 digits. A
complex-kernel variant of $A(h)$ (without the $\operatorname{Re}$) fails by
$27\%$–$97\%$, confirming (2.1) is the right functional. Theorem 3.3's
block ratios against their PNT predictions, as tabulated in §3.

**Not established, and explicitly not claimed.** T2. That $W_\infty$ equals the
Tate archimedean local integral under some specific Haar normalisation (not
needed: (2.2) is proved with $W_\infty$ as defined). Anything about the
existence of $h^0$, $H^1$, linear equivalence, Riemann–Roch, or effectivity.
Anything about RH.

## 8. Verifier

`113_06_the_canonical_weil_decomposition.py` — exits 0 with
`VERDICT: ALL CHECKS PASS`. It uses zeros of $\xi$ in one place only: inside
the numerical check of the classical identity that this file quotes and proves.
No definition in 113_06 uses a zero of $\xi$, a Li coefficient, or a positive
part of a Weil-type form.
