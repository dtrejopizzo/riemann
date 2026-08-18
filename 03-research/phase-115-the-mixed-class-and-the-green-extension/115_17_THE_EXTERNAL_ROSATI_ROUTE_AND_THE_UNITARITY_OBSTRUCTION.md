# 115.17 — Audit of the external row-(d) programme (v3–v7), and the unitarity obstruction that covers the whole family

Record of a single working session auditing five external notes on row (d),
produced outside this repository and supplied by DATP for scrutiny:

| tag | file | route |
|---|---|---|
| v3 | `row_d_bridge_attack_v3.md` | Sonin Bridge / conservative colligation |
| v4 | `row_d_threshold_defect_attack_v4.md` | threshold induction, newborn-cell capacity |
| v5 | `row_d_spectral_transversality_v5.md` | spectral transversality, polar cancellation |
| v6 | `row_d_conservative_reconstruction_v6.md` | scattering reconstruction, Rosati metric |
| v7 | `row_d_rosati_attack_v7.md` | Möbius graph metric on Meyer's quotient |

Nothing below is a review of style.  Every claim is either verified by hand,
refuted by computation, or proved here.  **Row (d) remains OPEN**; the main
result of this note is §7, which closes the entire *family* of routes v6–v7
rather than one of its members.

---

## 0. What was verified as correct in the external notes

These are recorded because they are true, non-trivial, and were not written
down anywhere in this repository before.

* **v3 (5.5), = v6 (3.2).**  The localized row-(d) operator has symbol
  \[
   -m_\infty(\tau)-2\sum_{n<e^{2T}}\frac{\Lambda(n)}{\sqrt n}\cos(\tau\log n),
  \]
  i.e. row (d) is the positivity of a compressed Fourier multiplier with
  explicit symbol, restricted to codimension 2.  A truncated-Toeplitz /
  finite-section problem.
* **v3 Thm 2.1.**  \(P_r(U)=\sum_m r^{|m|}U^m\): the truncated Euler square is
  exactly the compression of the bilateral Poisson kernel.
* **v3 Thm 7.2** (no Fourier multiplier can be the Bridge).  Checked
  numerically: \(m_0=\log\pi-\psi(1/4)=5.37219\),
  \(\frac{1+2^{-1/2}}{1-2^{-1/2}}=5.8284\),
  \(\frac{1+3^{-1/2}}{1-3^{-1/2}}=3.7321\), \(L_5(0)=13.512\), ratio
  \(7.5413\); Lemma 7.1 via \((e^{\pm t/2})''=\tfrac14e^{\pm t/2}\).
* **v4 Lemma 3.1** (translated-cell overlap).  Correct, and sharper than
  stated: if \(J+\log n\) and \(J+\log(n+2)\) meet, then
  \(\log(1+2/n)\le\log(1+1/N)\), so \(n>2N\), excluded.  Multiplicity
  \(\le2\) per orientation, not 3.
* **v4 §4** (arithmetic Bessel bound).  \(\|B_N^{\rm arith}\|=O(\log N)\),
  from \(\sum_{n\le N}\Lambda(n)^2/n=\tfrac12(\log N)^2+O(\log N)\) (partial
  summation on \(\sum_{p\le x}\log p/p\sim\log x\)).  A genuine improvement
  over the triangle bound \(\asymp\sqrt N\).
* **v4 Lemma 6.1** (Euler innovation).  The Schur complement of the
  Kac–Murdock–Szegő matrix \((r^{|i-j|})\) is exactly \(1-r^2=1-p^{-1}\).
  This fixes the local Euler gauge and removes the free Douglas parameter
  that was the gap of v3.
* **v6 §1–§2, §11 (11.1).**  Verified both channels.  With
  \(z_p=p^{-i\tau}\), \(r_p=p^{-1/2}\),
  \(\frac{b_{r}(z)}{z}=\frac{1-rz^{-1}}{1-rz}=\frac{\zeta_p(s)}{\zeta_p(1-s)}\),
  unimodular since numerator and denominator are conjugate;
  \(\arg(1-rz)=\sum_k\frac{r^k}{k}\sin k\theta\) gives
  \(\frac{d}{d\tau}\arg\Theta_p=-2\log p\sum_k p^{-k/2}\cos(k\tau\log p)\).
  Archimedean: \(\arg\Theta_\infty=2\arg\Gamma_{\mathbb R}(\tfrac12+i\tau)\),
  derivative \(=-\log\pi+\Re\psi(\tfrac14+\tfrac{i\tau}2)=-m_\infty\).  Hence
  \[
   \boxed{\;A_T=P_T\;\frac{d}{d\tau}\arg\Bigl[\tfrac{\Gamma_{\mathbb R}(s)}{\Gamma_{\mathbb R}(1-s)}\textstyle\prod_{p<e^{2T}}\tfrac{\zeta_p(s)}{\zeta_p(1-s)}\Bigr]\;P_T.\;}
  \]
  Exact, no estimate.  **But it is v3's (5.5) repackaged** — the same symbol,
  now written as a phase derivative of a truncated \(\Lambda(s)/\Lambda(1-s)\).
* **v6 §4.**  Unimodularity does not imply a positive phase derivative, so
  "conservative colligation \(\Rightarrow\) Douglas budget 1" is invalid.
  This correctly kills the central inference of the original (v1/v2) route.
* **v6 §9.**  No absolutely continuous \(L^2\) measure on the critical line
  can serve as the Rosati metric: multiplication by \(\zeta(\tfrac12+i\tau)\)
  has dense range (its zero set is Lebesgue-null), so the Hilbert quotient by
  \(\overline{Z\mathcal H_\cap}\) collapses to \(0\).  Meyer's Fréchet
  quotient is non-trivial precisely because it sees the **divisor**, not the
  a.e. values.

---

## 1. v3 route: the no-crossing mechanism is impossible

v3 proposed \(\lambda_1(T_0)=0\Rightarrow\lambda_1'(T_0)>0\).

> **Proposition 1.**  \(\lambda_1(T):=\inf\{\langle A_TF,F\rangle:F\in\mathcal P_T,\|F\|=1\}\)
> is **non-increasing** in \(T\).
>
> *Proof.*  For \(T<T'\) and \(F\in\mathcal P_T\) of unit norm, the
> zero-extension \(\tilde F\) has \(\|\tilde F\|=1\); the Tate moments are
> unchanged, so \(\tilde F\in\mathcal P_{T'}\); the Gamma part is the
> compression of the same full-line multiplier and \(\tilde F\) has the same
> Fourier transform; and every new term has \(\log n\ge2T\), hence zero
> overlap on \(\mathrm{supp}\,\tilde F\).  So
> \(\langle A_{T'}\tilde F,\tilde F\rangle=\langle A_TF,F\rangle\), and the
> Rayleigh quotients on \(\mathcal P_T\) form a subset of those on
> \(\mathcal P_{T'}\). \(\square\)

Hence \(\lambda_1'\le0\) wherever it exists, and **no theorem can produce
\(\lambda_1'(T_0)>0\)**.  Notably this is the same nesting argument the
manuscript already contains and v3 itself cites.

**Correct reformulations.**  Row (d) \(\iff\lim_{T\to\infty}\lambda_1(T)\ge0\)
(a *limit* question), equivalently \(n_-(A_T|_{\mathcal P_T})=0\) for all
\(T\), with \(n_-\) non-decreasing (a *count* question).  v3's \(n_-=0\)
formulation is right; its mechanism is not.

**Wiener–Hopf.**  v3's second proposal fails at the premise: the symbol
\(a(\tau)=-m_\infty(\tau)-2\sum\frac{\Lambda(n)}{\sqrt n}\cos(\tau\log n)\)
is **real** and changes sign, so it passes through \(0\) and has no winding
number; the classical factorization \(a=a_+a_-\) and its index are undefined.
For real symbols the relevant classical result runs the other way
(half-line Toeplitz with real symbol has spectrum containing the essential
range).

*Subtlety worth keeping.*  \(A_T\) **is** the finite section of a fixed
operator (terms with \(\log n\ge2T\) annihilate themselves), but the symbol of
that fixed operator is not a function — by the explicit formula it is the
zero-counting measure.  So Szegő does not apply (no contradiction), and
equally there is no symbol to factorize.

**Connection to the literature.**  (5.5) identifies \(A_T\) with Suzuki's
operator \(A_a\) (arXiv:2606.09096), where Thm 1.3 (continuity of
\(\lambda_a\)) and Thm 1.4 (\(\lambda_a>0\) for small \(a\), on the **full**
space, no moment conditions) are unconditional and published.  That gives an
independent cross-check of the interval \(0<T\le\log2\) on which the whole
external programme rests.

---

## 2. v4 route: the \(\sqrt N\) obstruction

v4 estimates the newborn-cell capacity with \(R_0^{-1}\) (the *positive
reference* inverse) in place of \(A_N^\dagger\) (the *signed core*
pseudoinverse).  §8 of v4 declares that substitution circular; §10 then uses
it to call the target lemma "plausible".  The two sections are incompatible,
and the size of the incompatibility is exact.

> **Proposition 2.**  With \(A_N=R_0-L_0\), \(D_0=I-R_0^{-1/2}L_0R_0^{-1/2}=R_0^{-1/2}A_NR_0^{-1/2}\),
> and \(R_0\ge\alpha_N I\):
> \[
>  \lambda_{\min}(D_0)\;\le\;\frac{\lambda_{\min}(A_N)}{\alpha_N},
>  \qquad\text{hence}\qquad
>  \|D_0^{\dagger}\|\;\ge\;\frac{\alpha_N}{\lambda_{\min}(A_N)} .
> \]
> *Proof.*  Take \(\phi_N\) a unit minimizer of \(A_N\) and
> \(y_N=R_0^{1/2}\phi_N\); then
> \(\langle D_0y_N,y_N\rangle/\|y_N\|^2=\lambda_{\min}(A_N)/\langle R_0\phi_N,\phi_N\rangle\le\lambda_{\min}(A_N)/\alpha_N\). \(\square\)

By Proposition 1, \(\lambda_{\min}(A_N)\le\lambda_{\min}(A_{\log2})=\)const.
With v4's own \(\alpha_N\sim\sqrt N\) this gives \(\|D_0^\dagger\|\gtrsim\sqrt N\).

**Consequences.**

1. v4's Target Lemma 9.1(2) asks for \(\|D_0^{\dagger/2}u_e\|^2\le C(\log N)^2/\sqrt N\)
   while \(\|D_0^{\dagger/2}\|^2\gtrsim\sqrt N\).  It therefore demands
   transversality of strength \(N^{-1}\), not a size bound.  Nothing in v4
   §3–§7 addresses transversality.
2. **The norm-only route fails unconditionally.**  Granting the legitimate
   \(A_N\ge\lambda_{\min}I\) and v4's own two estimates,
   \(\|A_N^{\dagger/2}B_N\|^2\le\|B_N\|^2/\lambda_{\min}\approx\frac{(\log N)^2/2}{\lambda_{\min}}\)
   against \(D_N\ge\tfrac12\log N\), the Schur complement is positive only if
   \(\lambda_{\min}(A_N)>\log N\).  But \(\lambda_{\min}\) is non-increasing
   and bounded.  Off by a factor \(\log N\), in the wrong direction, for all
   large \(N\).
3. The larger \(\alpha_N\) is, the better (5.1) looks and the **worse** the
   distance between \(R_0^{-1}\) and \(A_N^\dagger\) — because that distance
   *is* \(\alpha_N/\lambda_{\min}\).  v4 reads its worst obstruction as its
   best estimate.

---

## 3. v5 route: the archimedean channel closes; the finite one reduces to a
zero-free region

v5 accepts Proposition 2 and rebuilds.  Two findings, opposite in direction.

### 3.1 The Gamma cross is resolved (favourable)

Model the singular part of the archimedean kernel near a boundary by
\(K(x,y)=-\tfrac1{2(x+y)}\) (the symbol grows like \(\log|\tau|\), whose
kernel is \(-\tfrac12\,\mathrm{f.p.}\,|u|^{-1}\)), and let
\(e_\delta=\delta^{-1/2}\mathbf 1_{(0,\delta)}\).

* **Adjacent cells.**
  \(\langle Ke_\delta,e'_\delta\rangle=-\frac1{2\delta}\int_0^\delta\!\!\int_0^\delta\frac{dx\,dy}{x+y}=-\log2\).
* **Leakage into the whole core.**
  \((Ke_\delta)(s)=-\frac1{2\sqrt\delta}\log(1+\delta/s)\), so
  \(\|Ke_\delta\|_2^2=\frac14\int_0^{L/\delta}\log^2(1+u^{-1})du\to\frac{\pi^2}{12}\),
  using \(\int_0^\infty\log^2(1+u^{-1})du=\pi^2/3\).
  (Verified: substitute \(u=1/v\), integrate by parts to
  \(2\int_0^\infty\frac{\log(1+v)}{v(1+v)}dv\), then \(t=1/(1+v)\) gives
  \(2\int_0^1\frac{-\log t}{1-t}dt=2\sum_{n\ge0}(n+1)^{-2}=\pi^2/3\).)
  Hence \(\|B_N^\Gamma\|=O(1)\).
* **Against smooth modes — the decisive one.**  The low-spectrum modes of
  \(A_N\) are band-limited (that is *why* they are low), hence smooth at
  scale \(O(1)\gg\delta\).  With \(\psi\) smooth,
  \[
   \langle Ke_\delta,\psi\rangle\simeq-\frac{\psi(0)}{2\sqrt\delta}\int_0^L\log\Bigl(1+\frac\delta s\Bigr)ds
   =-\frac{\psi(0)\sqrt\delta}{2}\Bigl(1+\log\frac L\delta\Bigr)
   =O\bigl(\sqrt\delta\log\tfrac1\delta\bigr),
  \]
  using \(\int_0^X\log(1+1/u)du=X\log(1+1/X)+\log(1+X)\to1+\log X\).
  With \(\delta\asymp1/N\) this is \(O(N^{-1/2}\log N)\), against a budget of
  \(\|u_e\|\lesssim N^{-1/4}\) (from Proposition 2).

> **The archimedean channel needs no cancellation theorem.**  Norm \(O(1)\),
> pairing \(O(N^{-1/2}\log N)\): the newborn leakage is a boundary-layer
> object of width \(\delta\), nearly orthogonal to everything varying on
> scale \(\gg\delta\).  v5's §10 warning ("(7.1) cannot hold for the raw
> Gamma cross") is right but its repair is unnecessary — the two crosses need
> **different** mechanisms, not a combined one.

### 3.2 The polar cancellation is real — and it is the PNT main term

v5 conjectures (7.1): the zeroth-order newborn leakage lies in
\(\mathrm{span}\,\{e^{\pm t/2}\}\).  For the **arithmetic** cross this is
true, and the mechanism is explicit.  With \(\phi\) an old mode and
\(\delta\) the newborn width,
\[
 \langle B_N^{\rm arith}e,\phi\rangle\simeq\sqrt\delta\sum_{n<e^{2T}}\frac{\Lambda(n)}{\sqrt n}\,\overline{\phi(T-\log n)} .
\]
The density of \(\Lambda(n)/\sqrt n\) at \(\log n=y\) is \(e^{y/2}dy\), because
\(\sum_{n\le x}\Lambda(n)n^{-1/2}=2\sqrt x+O(\cdot)\).  Substituting \(u=T-y\):
\[
 \boxed{\;\simeq\sqrt\delta\,e^{T/2}\!\int_{-T}^{T}\!e^{-u/2}\overline{\phi(u)}\,du
  =\sqrt\delta\,e^{T/2}\,\overline{M_-\phi}=0\quad\text{on }\mathcal P_T.\;}
\]

This is a genuine exact cancellation and it explains why the two Tate moments
are the *right* two conditions and not two arbitrary ones.

**But the remainder is the error term of the prime number theorem.**  With
\(E_*(x)=\sum_{n\le x}\Lambda(n)n^{-1/2}-2\sqrt x\), partial summation from
\(\psi(x)=x+E(x)\) gives
\(E_*(x)=\frac{E(x)}{\sqrt x}+\tfrac12\int_1^x\frac{E(t)}{t^{3/2}}dt-1\),
and \(E(x)/\sqrt x=-\sum_\rho x^{\rho-1/2}/\rho+\cdots\) — **literally the sum
over the zeros**.  Integrating by parts,
\(\|u_e\|\lesssim\sqrt\delta\,\sup_{x\le N}|E_*(x)|\).  If
\(\psi(x)-x\ll x^\theta\) then \(\|u_e\|\ll N^{\theta-1}\), and the budget
\(\|u_e\|\lesssim N^{-1/4}\) requires

\[
 \boxed{\;\theta\le\tfrac34\;}\qquad\text{i.e. a zero-free region }\Re\rho<\tfrac34 .
\]

Weaker than RH, but wide open: the best known is \(\theta=1-o(1)\)
(\(\psi(x)-x\ll xe^{-c\sqrt{\log x}}\)), giving \(N^{-o(1)}\), nowhere near
\(N^{-1/4}\).  Conversely v5's claimed gain \(\Delta_N\asymp N^{-1}\) would
require \(E_*(N)=O(\log N)\), which is **stronger** than RH.

### 3.3 v5's falsifier at \(T=\tfrac12\log5\) tests nothing

At \(N=4\) the active channels are \(2,3,4\) and
\[
 \sum_{n\le4}\frac{\Lambda(n)}{\sqrt n}=0.4901290+0.6342515+0.3465736=1.4709541,
 \qquad 2\sqrt5-1=3.4721360 .
\]
The "main term" is off by a factor \(2.36\).  The asymptotic mechanism is
invisible at \(N=4\); the test will show an order-one component outside the
polar span for reasons that say nothing about large \(N\).

---

## 4. v6 route: the continuation defect is the zero divisor

v6 observes that \(\prod_p\Theta_p\) "\(=\)" \(\zeta(s)/\zeta(1-s)\), so
formally \(\Theta_{\rm formal}=\Lambda(s)/\Lambda(1-s)\), which the functional
equation makes \(\equiv1\); yet the termwise phase derivative is the non-zero
Weil symbol.  v6 calls the difference an infinite-dimensional "continuation
defect" and proposes it as a new state space.

**It is the explicit formula.**  \(\Lambda(\tfrac12+i\tau)\) is *real*:
\(\overline{\Lambda(s)}=\Lambda(\bar s)=\Lambda(1-s)=\Lambda(s)\) on the line.
So \(\arg\Lambda\in\{0,\pi\}\), jumping exactly at the zeros, and
\[
 \lim_{T\to\infty}\frac{d}{d\tau}\arg\Theta_T=2\frac{d}{d\tau}\arg\Lambda(\tfrac12+i\tau)
 =\text{the delta comb on the zeros}.
\]
The "missing infinite-dimensional state" is \(\ell^2\) of the zeros, and
"the limit is a positive measure on \(\mathbb R\)" is "the divisor lies on the
critical line".  §5–§6 of v6 rediscovers the explicit formula and presents it
as a no-go.

**The Rosati Completion Theorem is RH.**  Condition (8.2),
\(\lambda(f^\vee)=\lambda(f)^*\) for all \(f\), after \(\rho\to\rho^{-1}\) in
the integral, is \(\lambda(\rho)^*=\lambda(\rho)^{-1}\): the scaling
representation is **unitary**.  Combined with (3) (trace compatibility, which
prevents the completion from discarding spectrum) and row (c)'s spectral
identification — the spectral parameter of \(\rho=\beta+i\gamma\) is
\(-i(\rho-\tfrac12)=\gamma+i(\tfrac12-\beta)\), real iff \(\beta=\tfrac12\) —
this is equivalent to RH.  The chain (8.3) is correct and trivial;
\(\|\lambda(f)\|_{HS}^2\ge0\) always.  All the weight is in the hypothesis.

---

## 5. v7 route: the graph metric uses no \(\zeta\)

* **§1 is standard.**  \((\lambda_tu)(x)=u(t^{-1}x)\) on \(L^2(dx)\) gives
  \(\lambda_t^*=t\lambda_{t^{-1}}\), \(U_t=t^{-1/2}\lambda_t\) unitary, and
  \(\lambda(h)^*=\lambda(h^\vee)\) with \(h^\vee(r)=r^{-1}\overline{h(r^{-1})}\).
  This is the Mellin–Tate normalization, present in every treatment.
* **Theorem 3.1 uses exactly one property: \([M,\lambda(h)]=0\).**  It holds
  for \(M=0\), for \(M=I\), for any scaling multiplier.  **\(\zeta\) does not
  enter any step.**  The adjunction was already true on \(L^2(dx)\) alone; the
  graph term contributes nothing to it and only shrinks the domain.
* **"Positivity" is \(\|u\|^2+\|Mu\|^2\ge0\)** — a sum of two squares.  That
  is a norm, not a Rosati structure.  The arithmetic content is entirely in
  the trace identity, which §13 leaves unproved.
* **§10 is a tautology.**  \(W u=x^\varepsilon u\) is an isometry
  \(L^2(x^{2\varepsilon}dx)\to L^2(dx)\) with
  \(W\lambda_tW^{-1}=t^{\varepsilon}\lambda_t\): the two representations differ
  by the character \(t^\varepsilon\), i.e. by the shift of the Mellin line.
  "The Tate involution forces \(\varepsilon=0\)" says that the involution
  defined to make \(\Re s=\tfrac12\) self-dual makes \(\Re s=\tfrac12\)
  self-dual.
* **§4 points the wrong way.**  \(Z\mathcal H_\cap\subset\mathscr D_M\) is true
  and trivial (\(M(Zf)=f\)), but \(Z\mathcal H_\cap\) is the *denominator* of
  the quotient.  Containing what is quotiented away is not evidence of
  density in the quotient.
* **§5–§6 is the real content, and it closes the route.**  If \(\hat u/\zeta\)
  reaches \(\Re s=\tfrac12\) without non-removable poles, then every
  \(u\in\mathscr D_M\) satisfies \(\hat u(\rho)=0\) at each zero with
  \(\Re\rho>\tfrac12\), i.e.
  \[
   \mathscr D_M\subset\bigcap_{\Re\rho>1/2}\ker\mathrm{ev}_\rho .
  \]
  So \(\mathscr D_M\) is, essentially, *defined by killing the bad
  directions*.  Positivity on it carries no arithmetic input.  This is a
  sharper form of v6 §9 and is worth keeping as a criterion against any
  future attempt to Hilbertize Meyer's quotient.

---

## 6. The trace discrepancy, computed

v7 proposes next to force trace preservation from Meyer's nuclearity rather
than from the spectrum.  This is decidable now, without doing it.

Meyer's nuclear trace on \(\mathcal H_-^0\) is \(\sum_\rho m_\rho\hat f(\rho)\)
over **all** zeros with multiplicity.  By §5 the graph completion annihilates
the off-line ones.  The two traces therefore differ by exactly
\[
 \boxed{\;\sum_{\Re\rho\neq1/2} m_\rho\,\hat f(\rho).\;}
\]
Nuclearity is a topological property; it does not determine which eigenvalues
survive a completion, and cannot annihilate that sum.  **"Trace preservation"
is "no off-line zeros" in other words.**

---

## 7. The general obstruction

The following covers v6, v7, and every construction of that shape.

> **Proposition 3 (unitarity obstruction).**  Let \(\mathscr K\) be a Hilbert
> space carrying a **unitary** representation \(t\mapsto U_t\) of
> \(\mathbb R_+^\times\), and suppose \(\lambda(f)\) is trace class on
> \(\mathscr K\) with
> \(\mathrm{Tr}_{\mathscr K}\lambda(f)=\sum_\rho m_\rho\hat f(\rho)\)
> (Meyer's trace).  Then every \(\rho\) has \(\Re\rho=\tfrac12\).
>
> *Proof.*  By Stone/SNAG, \(U_t=\int_{\mathbb R}t^{i\tau}dE(\tau)\) with
> \(\tau\) **real**, so
> \(\mathrm{Tr}_{\mathscr K}\lambda(f)=\int_{\mathbb R}\hat f(\tfrac12+i\tau)\,d\nu(\tau)\)
> for a measure \(\nu\) on \(\mathbb R\).  Equating with
> \(\sum_\rho m_\rho\hat f(\rho)\) for all test \(f\) forces the divisor onto
> \(\Re s=\tfrac12\). \(\square\)

> **Unitarity is what buys positivity, and unitarity is what excludes
> off-line zeros.  They enter through the same door.**

Consequently v7's claimed separation into two blocks is not a separation:
the first block (adjoint + positivity) is free — it holds on any \(L^2\) with
the right normalization, and v7's own proof uses only commutativity — while
the second block (exhaustivity + trace preservation) is the whole problem.

**Working filter.**  *Does the construction make the scaling group unitary?*
If yes, RH has already been assumed, however elaborate the path.  If no, there
is no automatic positivity and the source of the sign must be named.

---

## 8. v8 route: the Sonin excursion — escapes §7, but closes at depth one
without primes

v8 (`row_d_sonin_excursion_v8.md`) accepts Proposition 3 and changes the
positivity mechanism: instead of a unitary representation it compresses the
normalized dilation to the Sonin defect sector,
\[
 \Sigma=\mathcal P_1\vee\widehat{\mathcal P}_1,\qquad \mathbf S=I-\Sigma,
 \qquad T_a:=\mathbf S U_a\mathbf S .
\]
Each \(T_a\) is a contraction (compression of a unitary), and they do **not**
form a semigroup.  **This genuinely escapes Proposition 3** — the sign would
not come from a real spectrum of a generator.  It is the first route in the
sequence to do so, and that should be recorded as a real advance in
diagnosis.

### 8.1 What is true, including one thing v8 does not prove

The multiplicativity defect is exact:
\(T_aT_b-T_{a+b}=-\mathbf S U_a\Sigma U_b\mathbf S\).  With \(T_b^*=T_{-b}\),
\[
 T_aT_{-b}=T_{a-b}-\mathbf S U_a\Sigma U_{-b}\mathbf S .
\]

> **Proposition 4.**  Put \(L_c:=\Sigma U_{-c}\mathbf S\).  Then, using
> \(\Sigma^2=\Sigma\) and \(U_a^*=U_{-a}\),
> \(\mathrm{Tr}(\mathbf S U_a\Sigma U_{-b}\mathbf S)=\mathrm{Tr}(L_a^*L_b)=\langle L_b,L_a\rangle_{HS}\),
> so
> \[
>  \mathfrak D(f,f)=\iint f(e^a)\overline{f(e^b)}\langle L_b,L_a\rangle_{HS}\,da\,db
>  =\Bigl\|\int\overline{f(e^b)}L_b\,db\Bigr\|_{HS}^2\ \ge\ 0 .
> \]

Hence v8's (6.2) is an exact decomposition into two nonnegative pieces:
\[
 \boxed{\;\mathrm{Tr}_{\rm reg}T(f\star f^\vee)=\|T(f)\|_{HS}^2+\mathfrak D(f,f).\;}
\]
v8 asserts \(\mathfrak D\ge0\) only as part of its target; the proof above is
elementary and makes it unconditional.

### 8.2 Why this cannot be row (d)

**Only one insertion occurs.**  \(T(f)T(f)^*\) has two factors, so the
identity above is already complete: there is no depth two, no words, no
series.  And \(T(g)=\mathbf S\vartheta(g)\mathbf S\), so by cyclicity
\(\mathrm{Tr}\,T(h)=\mathrm{Tr}(\vartheta(h)\mathbf S)\) — which is
**Connes–Consani's Theorem 3**.  With the sign dictionary of `115_08`
(\(W_\infty^{CC}=-G_\infty\)):
\[
 -G_\infty(f,f)+E(f)=\|T(f)\|_{HS}^2+\mathfrak D(f,f)\ \ge\ 0 .
\]

> **\(K(f,f)\) does not appear.**  The left side of v8's (12.1) is
> \(-B_{\rm nuc}=-K-G_\infty\); the right side, once the exact identity closes
> at depth one, is purely archimedean.  The word terms \(c_w\|K_w(f)\|^2\)
> have no equation to sit in, because (6.2) is already an equality.

Incidentally the identity gives \(E(f)\ge G_\infty(f,f)\) — a *lower* bound on
\(E\), while row (d) needs \(E\le0\).  It constrains \(E\) from the wrong side.

### 8.3 The higher-depth expansion has alternating signs

Expanding \(\prod(I-\Sigma)\), a \(k\)-fold excursion carries \((-1)^{k+1}\).
At depth two, explicitly:
\[
 \mathbf S U_{a+b+c}\mathbf S-T_aT_bT_c
 =\mathbf S U_a\Sigma U_{b+c}\mathbf S+\mathbf S U_{a+b}\Sigma U_c\mathbf S
  -\mathbf S U_a\Sigma U_b\Sigma U_c\mathbf S .
\]
So the hypothesis \(c_w\ge0\) of (12.1) contradicts the path expansion of §8
of v8 directly.

### 8.4 Two further defects

* **§10 gives no sign to individual terms.**  \(\mathbf S U_a\Sigma U_b\mathbf S=K_w^*K_v\)
  with \(w\ne v\) generically: an **off-diagonal** entry of a positive
  semidefinite Gram, which has no sign.  Only integration against
  \(f\otimes\bar f\) produces a diagonal — which is Proposition 4, the one
  place positivity actually appears.
* **§14 is malformed.**  \(\mathrm{Tr}(\mathbf S U^*_{k\log p}\Sigma U_{k\log p}\mathbf S)\)
  is independent of \(f\), while (14.2) depends on \(h=f\star f^\vee\); they
  cannot agree for all \(f\).  The proposed "decisive depth-1 calculation" is
  not a test of (12.1), and need not be run.

### 8.5 What to keep from v8

* **The Krein/Fredholm index no-go (v8 §1).**  Each off-line mirror pair adds
  a hyperbolic plane, \((n_+,n_-)\mapsto(n_++1,n_-+1)\), so \(n_+-n_-\) is
  unchanged.  **No argument based on a Fredholm index, Euler characteristic,
  or net Krein signature can distinguish RH from the presence of off-line
  pairs**; a successful indefinite-metric proof must control the absolute
  positive index.  This closes an entire further family of attempts and was
  not written down here before.
* **Proposition 4 and the corrected §6**: \(\mathrm{Tr}(\vartheta(h)\mathbf S)=\|T(f)\|_{HS}^2+\mathfrak D(f,f)\),
  an exact decomposition of CC's archimedean Sonin trace into two nonnegative
  pieces.  Not in their paper.  It bounds \(E\) from below; whether it can be
  turned against `115_15`'s question (the growth of \(\#\{\lambda_j(K_I)>1\}\))
  is untested.
* The contraction-semigroup criterion (v8 §2) is correct as stated — a
  strongly continuous contraction semigroup plus the mirror involution
  \(\rho\mapsto1-\bar\rho\) forces \(\beta=\tfrac12\) — but §4 shows the
  \(T_a\) are not a semigroup, so §3 does not meet §2's hypothesis.

---

## 9. v10 route: the Weyl \(m\)-functions — the reduction is right, the target
is false, and the polar defect is hyperbolic

v10 (`row_d_global_green_weyl_v10.md`) reduces the first crossing to two scalar
functions.  The reduction is correct.  Its proposed closing identity is not,
and the reason is an exact computation that also produces the sharpest
falsifier in this whole phase.

### 9.1 Verified in v10

* **The gcd law.**  \(a_n=\Phi_n(1)\) equals \(p\) for \(n=p^k\) and \(1\)
  otherwise, so \(\log\gcd(a_m,a_n)=\Lambda(mn)\).  Correct.  The conditional
  negativity is \(x^\top dx=-2x^\top Kx=-2\sum_p\log p\bigl(\sum_{n=p^k}x_n\bigr)^2\)
  on \(\sum x_n=0\) — but this is just the statement that \(K\) is block
  diagonal, rank one per prime, PSD.  That is the **obstruction** already
  recorded in the manuscript (one positive direction per prime, unbounded
  positive index), not a new Hodge theorem.
* **The kernel equation.**  A primitive zero mode satisfies \(A_TF=M^*\lambda\),
  \(\lambda\in\mathbb C^2\), not \(A_TF=0\).  Correct, and it does kill
  unique-continuation arguments.
* **The Weyl matrix.**  \(\mathcal W_T(0)=MA_T^{-1}M^*\) and
  \(0\in\sigma(A_T|_{\mathcal P_T})\iff\det\mathcal W_T(0)=0\), valid where
  \(A_T\) is invertible on the full space.  Correct.
* **Parity.**  \(A_T\) has even symbol, hence commutes with \(t\mapsto-t\);
  \(h_e=\cosh(t/2)\), \(h_o=\sinh(t/2)\) diagonalize \(\mathcal W_T\), so
  \(\det\mathcal W_T(0)=m_e m_o\).  Correct.
* **\(\partial_zm=\|(A-z)^{-1}h\|^2>0\).**  Standard Weyl monotonicity, correct.
* **Poisson has rank-two defect.**  \(Z\phi-\mathscr JZ\mathcal F\phi=\tfrac12(x^{-1}\widehat\phi(0)-\phi(0))\)
  follows from \(\sum_{n\in\mathbb Z}\phi(nx)=x^{-1}\sum_n\widehat\phi(n/x)\).
  Under \(u(t)=e^{t/2}\phi(e^t)\) the two defect states are \(e^{\pm t/2}\),
  i.e. \(\mathrm{span}\,\{h_e,h_o\}\).  Correct, and it is v10's best
  structural observation: \(M^*\) **is** the Poisson defect map.

### 9.2 The exact hyperbolic decomposition

Write the Riemann–Weil formula with \(h=|\widehat F|^2\).  The polar terms are
\(h(i/2)+h(-i/2)=2\Re(a\bar b)\) with \(a=M_-F\), \(b=M_+F\); since
\(\langle F,h_e\rangle=\tfrac{a+b}2\), \(\langle F,h_o\rangle=\tfrac{b-a}2\) and
\(|a+b|^2-|b-a|^2=4\Re(a\bar b)\):

> **Proposition 5.**  For every \(F\in L^2(-T,T)\),
> \[
>  \boxed{\;\langle A_TF,F\rangle=\sum_\rho\widehat h(\rho)
>   -2\bigl|\langle F,h_e\rangle\bigr|^2
>   +2\bigl|\langle F,h_o\rangle\bigr|^2 .\;}
> \]

**The Poisson defect is not \(-M^*M\); it is hyperbolic, of signature
\((1,1)\)** — negative on the even port, **positive** on the odd one.  Poisson
says which two ports; the explicit formula says with which signs.

Under RH (\(\sum_\rho\widehat h(\rho)=\sum_\gamma|\widehat F(\gamma)|^2\ge0\)):

* \(A_{T,o}=P_o+2h_o\!\otimes\!h_o\ge0\): **the odd sector carries no negative
  direction**, so \(m_o(T;0)>0\) for every \(T\), free of charge;
* \(A_{T,e}=P_e-2h_e\!\otimes\!h_e\): a **rank-one** negative perturbation, so
  \(n_-(A_T)\le1\).

### 9.3 Inertia: the equivalence upgraded to a count

Haynsworth additivity applied to the bordered matrix
\(\bigl(\begin{smallmatrix}A_T&M^*\\M&0\end{smallmatrix}\bigr)\) with \(M\) of
full row rank 2 gives \(\mathrm{In}=\mathrm{In}(A_T|_{\ker M})+(2,2,0)\)
on one side and \(\mathrm{In}(A_T)+\mathrm{In}(-\mathcal W_T)\) on
the other, hence

> **Proposition 6.**
> \[
>  \boxed{\;n_-\bigl(A_T|_{\mathcal P_T}\bigr)=n_-(A_T)+\#\{m_e(T;0)>0\}+\#\{m_o(T;0)>0\}-2 .\;}
> \]
> Row (d) at level \(T\) \(\iff n_-(A_T)+\#\{m_e>0\}+\#\{m_o>0\}=2\).

This upgrades v10's equivalence (which only detects a crossing) to a full
count, and immediately gives:
\[
 m_e>0\ \text{and}\ m_o>0\ \ \forall T
 \iff n_-(A_T)=0\ \ \forall T .
\]

### 9.4 v10's target is false inside the certified interval

Script: `scripts/115_17_v10_hyperbolic_defect.py` (+`.out`).  With \(F\) the
normalized indicator of \((-T,T)\) (even, so \(\langle F,h_o\rangle=0\)),
60 zero pairs, \(\gamma\le163.031\) (tail \(\sim10^{-2}\), does not affect the
sign):

| \(T\) | \(\sum_\gamma\vert\widehat F(\gamma)\vert^2\) | \(2\vert\langle F,h_e\rangle\vert^2\) | \(\langle A_TF,F\rangle\) |
|---|---|---|---|
| 0.05 | 0.9016857923 | 0.2000416701 | **\(+0.7016441221\)** |
| 0.10 | 0.4604046585 | 0.4003334445 | **\(+0.0600712141\)** |
| 0.20 | 0.1637865563 | 0.8026702248 | **\(-0.6388836684\)** |
| 0.35 | 0.1531356167 | 1.4143501520 | **\(-1.2612145350\)** |
| \(\log2\) | 0.0567159090 | 2.8853900820 | **\(-2.8286741730\)** |

So \(n_-(A_T)\ge1\) already for \(T\lesssim0.2\), **inside the certified
interval \(T\le\log2\)**.  By Proposition 6, v10's desired identity
\(m_e(T;0)=c_e(T)+|R_{e,T}|^2\) with \(c_e>0\) would prove something false.
(v10 declines to derive it, correctly.)

### 9.5 The corrected target

\[
 \boxed{\;m_o(T;0)>0\ \ \forall T;\qquad
 m_e(T;0)\ \text{has exactly one pole and no zero.}\;}
\]

The pole mechanism is automatic and favourable:
\(m_e(T;0)=\sum_j|\langle h_e,\psi_j(T)\rangle|^2/\mu_j(T)\), so when a
full-space eigenvalue \(\mu_1\) crosses zero downward, \(m_e\to+\infty\),
reappears at \(-\infty\), and stays negative — exactly what Proposition 6
requires when \(n_-(A_T)=1\).  The danger is not the pole but the **return**:
as \(\mu_1\) becomes more negative, \(c_1^2/\mu_1\to0^-\) and the positive
terms recover, so \(m_e\) can cross zero again.  Row (d) is therefore not
"\(m_e\ne0\)" but *"\(m_e\) crosses \(\infty\) once and never returns to
\(0\)"*.  And the odd sector is settled under RH — all the difficulty is even,
and of rank one.

### 9.6 A rigorous, computable falsifier of RH

> **Proposition 7.**  If \(n_-(A_T)\ge2\) for some \(T>0\), then RH is false.
>
> *Proof.*  Under RH, Proposition 5 writes \(A_T=P-2h_e\!\otimes\!h_e+2h_o\!\otimes\!h_o\)
> with \(P\ge0\), whose negative part has rank at most one. \(\square\)

This needs only the **full-space** operator — no moment conditions, no
constrained eigenvalue problem, no \(\mathcal W_T\).  And \(n_-(A_T)\) is
non-decreasing (the zero-extension of Proposition 1 does not use the moment
conditions), so it suffices to follow one integer upward.  This is far cheaper
than anything attempted in v3–v10 and has not been computed by anyone.

### 9.7 What Poisson can and cannot supply

Poisson identifies the two ports, and that is correct and useful.  But it is an
**exact algebraic identity containing no inequality**, so it cannot produce the
sign of a resolvent.  The sign appears only when one asks the explicit formula
with what signature those two ports enter — and the answer is \((1,1)\).  With
that, Poisson has given everything it has.

---

## 10. The Witt adjoint: \(F_nV_n\neq nI\), and the norm \(\|\phi_r\|^2=\varphi(r)\)

Asked whether the repository develops \(F_nV_n=nI\).  **It does not** — but row
(b) *was* developed, in phase 114, and two of its notes settle the question.

* **`114_a_36_I7_WITT_OPERATOR_CORRESPONDENCES.md`** — the operator development
  of row (b).  Eq. (1.2): \(\mathcal H=\widehat{\mathcal W}_{\mathbb C}\),
  \(\langle\phi_m,\phi_n\rangle=\delta_{mn}\varphi(n)\), cited to Haran (12.35);
  (1.3) \(V_n=F_n^*\), \(V_n\phi_m=\phi_{nm}\); (1.4) \(V_mV_n=V_{mn}\);
  Thm 2.1 (faithfulness, by orthogonality on the cyclic vector); Thm 3.1
  (\(\Lambda(n)=\log|\Phi_n(1)|\)); and the open gate **H7-I7-REAL** (no
  divisor/cycle realization on the square).
* **`114_d_194_WITT_FOCK_DEFECT_AND_TORSION_TRACE_GATE.md`** — the Hilbert
  analysis.  See below; it already runs and closes the isometry route.

`row-b-witt-lefschetz.tex` (31–36) carries only the citation, without norms.

> **Correction of record.**  Proposition 9 below is a *rederivation*: the norm
> \(\|\phi_r\|^2=\varphi(r)\) was already ours, `114_a_36` (1.2).  What is new
> here is Proposition 8, \(F_nV_n\), which appears nowhere.

The source has it.  Haran, `arXiv-2209.08536v3`, (12.20):
\[
 F_p\phi_n=\begin{cases}\phi_n & p\nmid n\\ p\,\phi_{n/p}& p^2\mid n\\ (p-1)\phi_{n/p}& p\,\|\,n\end{cases}
\]
and generally (12.21)
\(F_m\phi_n=(m,n)\prod_{p\mid(m,n),\,p\nmid n/(m,n)}(1-p^{-1})\phi_{n/(m,n)}\).

> **Proposition 8.**  With \(V_n\phi_r=\phi_{nr}\) and \((n,nr)=n\), \(nr/n=r\):
> \[
>  \boxed{\;F_nV_n\,\phi_r=n\!\!\prod_{p\mid n,\ p\nmid r}\!\!\Bigl(1-\frac1p\Bigr)\phi_r .\;}
> \]
> Diagonal but **not scalar**: it equals \(nI\) only where every prime of \(n\)
> already divides \(r\); on the cyclic vector \(F_nV_n\phi_1=\varphi(n)\phi_1\).
> For \(n=p\): \(F_pV_p\phi_r=(p-1)\phi_r\) if \(p\nmid r\), \(=p\,\phi_r\) if
> \(p\mid r\).

> **Proposition 9 (the norm is forced).**  \(V_n=F_n^*\) with orthogonal basis
> \(\|\phi_r\|^2=w_r\) requires \(w_{pr}=(p-1)w_r\) for \(p\nmid r\) and
> \(w_{pr}=p\,w_r\) for \(p\mid r\).  With \(w_1=1\) this is Euler's recursion:
> \[
>  \boxed{\;\|\phi_r\|^2=\varphi(r).\;}
> \]
> Independent confirmation: Haran gives \(\chi_T(\phi_r)=\Phi_r(T)\) and
> \(\deg\Phi_r=\varphi(r)\) — the norm is the degree of the cyclotomic
> polynomial.  There is no gauge freedom here.  **Already recorded as
> `114_a_36` (1.2)**; this is a consistency check on it, not a new result.

### 10.1 The isometry route was already run and closed in phase 114

`114_d_194` builds the *other* Hilbertization — the Fock one,
\(\mathscr F_W=\ell^2(\mathbb N^\times)\) with the \(\phi_r\)
**orthonormal** — in which \(V_n^*V_n=I\), i.e. \(V_n\) **is** an isometry,
exactly what the external note wants.  It then shows the defect is wrong:

* \(I-S_p^kS_p^{*k}=\sum_{j<k}|j\rangle\langle j|\) has rank \(k\), while
  \(\Lambda(p^k)=\log p\) is independent of \(k\) — (2.1)–(2.3);
* for \(n=p^kq^\ell\) the vacuum lies in \(\mathrm{Ran}\,D_n\), so
  \(\langle\Omega,D_n\Omega\rangle=1\) while \(\Lambda(n)=0\) — (2.4)–(2.5);
* on the full tensor product \(D_n\) has infinite rank.

And (2.6)–(2.7) is **literally the proposed operator**:
\(\widetilde V_n=n^{-1/2}V_n\), \(I-\widetilde V_n^*\widetilde V_n=(1-n^{-1})I\)
— "the half-Tate factor is the correct metric character, but it is not a
finite-contact defect index".  Verdict (4.5):
\[
 \boxed{\text{Hilbert isometry defect}\ne\text{derived reduced contact determinant}.}
\]

| | norm | \(F_nV_n\) | \(V_n\) |
|---|---|---|---|
| Haran's state (`114_a_36`) | \(\|\phi_r\|^2=\varphi(r)\) | \(n\prod_{p\mid n,\ p\nmid r}(1-p^{-1})\) | contraction, not isometric |
| Fock (`114_d_194`) | \(\phi_r\) orthonormal | \(I\) | isometry |

**Neither gives \(nI\), and the two properties cannot be had together**: the
Fock normalization buys the isometry and loses the prime-power law; Haran's
state carries the right number \(1-1/p\) and loses the isometry.  That
dichotomy was already proved in phase 114.

What survives, and `114_d_194` §5 confirms from the other side: **local
contact positivity is not the obstacle** (that note builds a positive GNS
algebra realizing \(\Lambda(mn)\) exactly).  What is missing is the
trace-exact Poisson gluing to the Witt translations and the Gamma boundary —
which is the same thing Proposition 5 says on the row-(d) side: the real
defect is hyperbolic of signature \((1,1)\), not a positive defect index.

**Consequence for the proposed Euler channel.**  In the normalized basis
\(e_r=\phi_r/\sqrt{\varphi(r)}\), with \(W_p:=p^{-1/2}V_p\),
\[
 W_p^*W_p=I-\tfrac1p P_{\{p\nmid r\}},\qquad
 \|W_pe_r\|=\begin{cases}\sqrt{1-1/p}&p\nmid r\\ 1&p\mid r.\end{cases}
\]
On the pure orbit \(\{e_1,e_p,e_{p^2},\dots\}\), \(W_p\) is a **weighted
unilateral shift** with weights \((\sqrt{1-1/p},1,1,\dots)\) — a contraction,
isometric except on the first step.  So \(W_p\) is **not** an isometry and the
inference "\(F_pV_p=pI\Rightarrow W_p^*W_p=I\)" fails.

But the defect is \(1-1/p\): the same number as v4's Kac–Murdock–Szegő Schur
innovation (§0) and as the \(\varphi\) norm.  Three independent appearances of
the local Euler density.  **The (b)\(\to\)(d) bridge exists, but it is
Sz.-Nagy dilation, not isometry**: \(W_p\) is a contraction, its minimal
unitary dilation is the *bilateral* shift \(U\), and \(P_r(U)=\sum_m r^{|m|}U^m\)
is exactly v3's Theorem 2.1 (verified, §0).  Row (d)'s Euler channel needs
\(S_{k\log p}+S_{-k\log p}\) — both directions — while the Witt module is
unilateral.  The unreduced orbit supplies one half; the dilation supplies the
other.  Nothing has to be invented: the weights are fixed by \(\varphi\).

*Also noted from the same exchange:* the primitive-potential reading
(\(F\in\mathcal P_T\iff F=L_0G\), \(G\in H^2_0(-T,T)\), \(L_0=-\partial_t^2+\tfrac14\),
Green kernel \(e^{-|t|/2}\) whose two tails outside \([-T,T]\) carry \(M_\pm F\))
is correct and is a clean restatement of the two Tate ports as clamped boundary
conditions.  And the "Witt Hodge theorem"
\(q_W(\delta_m,\delta_n)=(\log m)(\log n)-\Lambda(mn)\), \(n_+(q_W)\le1\), is the
same per-prime rank-one structure as §9.1 — true, but it is the finite-contact
obstruction, and by Proposition 5 the actual defect in row (d) is hyperbolic of
signature \((1,1)\), not of the form \(dd^\top-K\).

---

## 11. Status

| item | state |
|---|---|
| v3 no-crossing via \(\lambda_1'>0\) | **REFUTED** (Prop. 1: \(\lambda_1\) non-increasing) |
| v3 Wiener–Hopf index | **ILL-POSED** (real symbol, changes sign) |
| v3/v6 exact symbol & phase-derivative identity | **VERIFIED**, and identical in both |
| v4 overlap lemma, Bessel bound, Euler innovation | **VERIFIED** (overlap sharpened to \(\le2\)) |
| v4 threshold induction | **REFUTED** (Prop. 2; norm-only route off by \(\log N\)) |
| v5 archimedean channel | **RESOLVED, favourable**: \(\|B_N^\Gamma\|=O(1)\), \(\pi^2/12\); \(O(N^{-1/2}\log N)\) against smooth modes |
| v5 polar cancellation \(\sqrt\delta\,e^{T/2}M_-\phi=0\) | **PROVED**, and identifies why the two Tate moments are the right ones |
| v5 remainder size | **= PNT error**; route needs \(\theta\le3/4\), open |
| v5 falsifier at \(N=4\) | **NON-INFORMATIVE** (main term off by \(2.36\)) |
| v6 continuation defect | **= the zero divisor** (\(\Lambda\) real on the line) |
| v6 Rosati Completion Theorem | **EQUIVALENT TO RH** (Prop. 3) |
| v7 Theorem 3.1 | **TRUE BUT VACUOUS** — no \(\zeta\) in the proof |
| v7 §10 rigidity | **TAUTOLOGY** (\(W u=x^\varepsilon u\) intertwines) |
| v7 domain obstruction \(\mathscr D_M\subset\bigcap\ker\mathrm{ev}_\rho\) | **CORRECT**, and closes the route |
| v8 escapes Proposition 3 | **YES** — first route in the sequence to do so |
| v8 Krein/Fredholm index no-go | **CORRECT**, and closes a further family |
| v8 \(\mathfrak D(f,f)\ge0\) and the depth-1 decomposition | **PROVED** (Prop. 4), stronger than v8 states |
| v8 Excursion Hodge Theorem (12.1) | **REFUTED**: identity closes at depth one with no \(K\); \(c_w\ge0\) contradicts the alternating expansion |
| v8 §14 depth-1 falsifier | **MALFORMED** (\(f\)-independent vs \(f\)-dependent) |
| v10 gcd law \(\Lambda(mn)=\log\gcd(\Phi_m(1),\Phi_n(1))\) | **VERIFIED**, but it is the known per-prime obstruction |
| v10 kernel equation \(A_TF=M^*\lambda\) | **CORRECT**, kills unique-continuation arguments |
| v10 Weyl reduction \(\det\mathcal W_T(0)=m_em_o\) | **CORRECT** |
| v10 Poisson rank-two defect | **CORRECT**: \(M^*\) is the Poisson defect map |
| Hyperbolic decomposition (Prop. 5) | **PROVED**: signature \((1,1)\), not \(-M^*M\) |
| Inertia count (Prop. 6) | **PROVED** |
| v10 target \(m_e,m_o>0\ \forall T\) | **REFUTED** numerically at \(T\lesssim0.2\) |
| Corrected target (§9.5) | odd sector free under RH; even is rank one, one pole, no return |
| Falsifier \(n_-(A_T)\ge2\Rightarrow\neg\)RH (Prop. 7) | **PROVED**, and computable on the full space |
| \(F_nV_n=nI\) | **NEVER DERIVED HERE**, and **FALSE** in both normalizations — Prop. 8 |
| \(\|\phi_r\|^2=\varphi(r)\) | **ALREADY OURS**, `114_a_36` (1.2); Prop. 9 is a rederivation |
| \(W_p=p^{-1/2}V_p\) isometric | **FALSE** in Haran's state; **TRUE** in Fock — and Fock was closed in `114_d_194` (2.1)–(2.7) |
| (b)\(\to\)(d) Euler bridge | exists, but via **Sz.-Nagy dilation**, not isometry |
| **Row (d)** | **OPEN** |

**What survives and is ours to keep**

1. Proposition 3 and the unitarity filter (§7).
2. The Krein/Fredholm index no-go (§8.5): net signature cannot see off-line
   pairs; only the **absolute** positive index will do.
3. The archimedean channel is *not* the obstruction (§3.1).  This agrees, from
   the opposite direction, with `115_08` §4.2 Corollary 7 (the archimedean
   no-go): all the weight in row (d) is on the finite term.
4. The identity \(\sqrt\delta\,e^{T/2}M_-\phi=0\) (§3.2).
5. Proposition 4 and the exact decomposition
   \(\mathrm{Tr}(\vartheta(h)\mathbf S)=\|T(f)\|_{HS}^2+\mathfrak D(f,f)\)
   into two nonnegative pieces (§8.1) — not in Connes–Consani.
6. \(\mathscr D_M\subset\bigcap_{\Re\rho>1/2}\ker\mathrm{ev}_\rho\) as a
   criterion against Hilbertizations of Meyer's quotient (§5).
7. The Euler innovation \(1-p^{-1}\) as a gauge-fixing device (§0).
8. The Suzuki cross-check for \(0<T\le\log2\) (§1).
9. **Propositions 5–7 (§9)** — the hyperbolic form of the polar defect, the
   inertia count, and the falsifier \(n_-(A_T)\ge2\Rightarrow\neg\)RH.  These
   are the most useful things to come out of the audit: the odd sector is free
   under RH, the even obstruction is rank one, and there is now a cheap
   full-space computation that can refute RH outright.

**The shape of the failure.**  Across six versions the hole relocated six
times — \(Z_F\) (v3) → \(A_N^\dagger\) vs \(R_0^{-1}\) (v4) → the PNT
remainder (v5) → the metric (v6) → exhaustivity of the graph domain (v7) →
the coefficient identification \(c_w\) (v8) — while the underlying identity
never changed.  Each version rewrites the explicit formula in a new language,
and the hole reappears in whichever object that language leaves undefined.
The language changes; the hole is invariant.  What is missing is the sign.

v8 is the first to relocate the hole into a **falsifiable** object rather than
a free one: \(c_w\) is determined on both sides, so the identity is a
conjecture and not a gauge.  That is a real improvement in kind.  It is also
already falsified, by §8.2–§8.3.

**A second filter, for routes that pass §7's.**  Ask where the primes enter.
A construction built from the archimedean Sonin geometry (\(\mathcal P_1\),
\(\widehat{\mathcal P}_1\), \(U_a\), \(\mathbf S\)) can only reproduce
\(-G_\infty+E\); the finite term \(K\) has to be *put in*, and if the
governing identity closes without it, no later expansion can add it.

**Live leads, unchanged from `115_15`.**  (i) The eigenvalue count of
\(K_I\) for \(|I|>\log2\) — never examined by anyone in six years, decidable by
computation, with \(\mathrm{tr}\,K_I=0\) (CC Remark 5.6) as the favourable
structural hint.  (ii) Point 6: \(A(f)\prec0\) from a non-single-place
realization.
