# Day 17 — Verification of the Days-16+ exploration: two errors found, and a milder corrected picture

The referee pushed RFB much further (operator form $\|A\|$; $T^{-1}$+Jaffard interpolation; GUE
$1/\delta$-integrability; a Montgomery-scale "reversal" of coercivity) and asked for a **double-checked
verification**. Done. **Verdict:** the *formulations* are right and valuable; **two arguments contain real
errors** (one would have reversed Days 14–16); and the corrected picture is **milder than the GUE-heavy
framing** — RFB is plausibly true with an $O(1)$ constant via cancellation, needing GUE only for the rare
deep zeros. **Tags:** ✅ verified · ❌ error · ◆ refined.

---

## A. VERIFIED correct
- **(Thread 1) RFB $\iff\|A\|_{\ell^2\to\ell^2}<\infty$**, $A_{\gamma\gamma'}=K(\gamma+ib,\gamma')/\sqrt{K(\gamma,\gamma)K(\gamma',\gamma')}$.
  ✅ Correct and is the right reduction. ($\widetilde{\mathfrak t}_-=\|Aa\|^2$, $\mathfrak t_+=\|a\|^2$.)
- **(Thread 2) Interpolation $c_{\gamma'}(z)=\langle T^{-1}k_{\gamma'},k_z\rangle$.** ✅ Construction correct
  (standard frame inversion). Jaffard would give $G^{-1}$ exponential decay — **but** Jaffard needs uniform
  separation, which the zeros lack (the referee flagged this; correct).
- **(Thread 3) GUE makes the $1/\delta$ singularity integrable:** $\int_0^1\frac1\delta\cdot\delta^2\,d\delta<\infty$
  (cubic repulsion $\Pr(\text{gap}<\epsilon)\sim\epsilon^3$, density $\sim\delta^2$, kernel-inverse blowup
  $\sim1/\delta$). ✅ Computation correct, genuinely suggestive — *but it concerns the $\ell^1/G^{-1}$ route*
  (see error 2).

---

## B. ❌ ERROR 1 (the consequential one): the Montgomery-scale "reversal" — coherence vs bandwidth
**Claim audited:** rescaling $x=\rho(T)(t-T)$, the kernel flattens $K_T\to$const, the "rescaled bandwidth"
$\Lambda=d\rho\to\infty$, Nyquist $\Lambda/\pi\to\infty$, zero density $1$, ratio $\to0$ $\Rightarrow$
**local under-sampling $\Rightarrow$ coercivity not free.**

**This is wrong.** The error: $\Lambda=d\rho$ is the rescaled **coherence length**, and **bandwidth is its
inverse**, $1/\ell_x=1/(d\rho)\to0$. So Nyquist $\sim1/(d\rho)\to0$, zero density $1\gg$ Nyquist $\Rightarrow$
**over-sampling** (not under). Three independent checks:
1. **Flat kernel = degenerate.** $K_T\to$const is a **rank-1** kernel (RKHS $=\operatorname{span}\{1\}$,
   $1$-dimensional). Sampling a $1$-dim space with infinitely many points is **extreme over-sampling**, not
   under. (The flatness signals the Montgomery scale is *too zoomed-in* to see kernel structure — not a real
   under-sampling.)
2. **$P=\rho\ell$ is scale-invariant.** Under $x=\lambda(t-T)$: $\rho_x=\rho/\lambda$, $\ell_x=\lambda\ell$,
   so $P_x=\rho_x\ell_x=\rho\ell=P$. **$P\to\infty$ cannot be rescaled away** — the over-sampling is the
   invariant ratio. There is no scale at which it "disappears."
3. **Displacements at the Montgomery scale are $O(\log T)$, not $o(1).$** $\gamma_n-\bar\gamma_n\sim S/\rho\sim1/\sqrt{\log}$
   in *physical* units (small vs coherence $d$ ✓ — so $G\approx G_0$ physically), but $\times\rho$ in
   Montgomery units $=S=O(\log)$ — large. So the "$G=G_0+o(1)$ at the Montgomery scale" reading is also off.

**Consequence:** Days 14–16 **stand**. Over-sampling is forced and scale-invariant; **coercivity (lower
frame bound) stays easy** (helped by over-density; the zeros leave no Nyquist cell of size $d$ unsampled,
since each contains $\sim\rho d=P\to\infty$ zeros and max gap $\sim1/\rho\ll d$). The "reversal" does not
occur.

---

## C. ❌ ERROR 2: no $\ell^1$/Schur/lattice route proves RFB — they all hit the $P$ wall
**Claim audited:** for a regular lattice $\gamma_n=nh$, $G_0^{-1}$ is tridiagonal/bounded $\Rightarrow$ "RFB
essentially done"; and Schur on $A$ closes it.

**Wrong in the over-sampling regime.** The lattice spacing is $h\sim1/\rho\to0$ (over-dense), so
$r=e^{-ah}\to1$ and
$$
\|G_0^{-1}\|\sim\frac1{1-r^2}\sim\frac1{2ah}\sim\frac{\rho}{a}\to\infty .
$$
The Gram is **nearly singular** (over-complete kernels are nearly dependent); $G_0^{-1}$ **blows up like
$\rho$**, not bounded. Likewise the **direct Schur bound** on $A$ (exponential magnitude decay
$|A_{\gamma\gamma'}|\sim\sqrt{\kappa(b)}\,e^{-c|\gamma-\gamma'|/\ell}$) gives
$$
\|A\|\le\sup_\gamma\sum_{\gamma'}|A_{\gamma\gamma'}|\asymp\sqrt{\kappa(b)}\,\rho\ell=\sqrt{\kappa(b)}\,P\to\infty .
$$
**Every $\ell^1$/absolute-value route (Schur, Jaffard-$G^{-1}$, lattice) carries the over-sampling factor
$P\to\infty$ and fails.** This is the *same* phenomenon as the Day-16 Step-3 hole — it is intrinsic, not a
fixable slip. **Schur does not prove RFB.**

---

## D. ◆ The corrected picture: RFB is plausibly TRUE with $O(1)$ constant — via cancellation, not Schur
The operator norm $\|A\|$ (with phases/cancellation) is **much smaller** than the Schur ($\ell^1$) bound
$\sim P$. Reason: $\widetilde{\mathfrak t}_-$ and $\mathfrak t_+$ **both over-sample by $P$**, which
**cancels in the ratio**:
$$
\frac{\widetilde{\mathfrak t}_-(F)}{\mathfrak t_+(F)}\ \approx\ \frac{P_{\mathrm{off}}\,\langle|F(\cdot+ib)|^2\rangle_{\mathrm{loc}}}{P\,\langle|F|^2\rangle_{\mathrm{loc}}}\ \le\ \frac{P_{\mathrm{off}}}{P}\,\kappa(b)\ \le\ \kappa(b)=O(1)\quad(|b|<d).
$$
So $\|A\|\asymp\sqrt{\kappa(b)}=O(1)$ is the **true** operator norm, and **RFB holds with a bounded
constant** — *provided the sampling sums approximate the local $L^2$ averages* (a regularity, not GUE).

**Why the regularity is mild (not full GUE).** In a coherence window of size $d>\tfrac12$ (fixed),
band-limiting gives only $O(1)$ Nyquist cells, sampled by $\sim P\to\infty$ zeros — a massively redundant
(LLN) regime. The local empirical average $\to$ true average provided no Nyquist cell is starved, i.e. **no
gap $\gtrsim d$** — which holds (max gap $\sim1/\rho\ll d$). So both coercivity and bulk-RFB follow from
**$S(T)=O(\log)$-level regularity alone**, *not* pair correlation. The over-sampling that *broke* the
$\ell^1$ routes is exactly what *makes* the cancellation route robust (redundancy).

**Where genuine arithmetic still enters (the honest residual):** the constant $\kappa(b)\to\infty$ as
$|b|\to d=\tfrac12+\epsilon$, so **deep off-line zeros** ($\beta\to0,1$) are amplified. Their contribution
is $\sum_{\text{deep}}\kappa(b_\rho)$ — controlled only by a **zero-density** bound on how many off-line
zeros lie near the critical-strip edge. This is exactly the §3.3 "zero-density tier," **not** full GUE.

---

## E. Net verdict (Day 17)

| referee thread | verdict |
|---|---|
| RFB $\iff\|A\|<\infty$ (operator form) | ✅ correct, right reduction |
| $c=T^{-1}k$ interpolation construction | ✅ correct |
| Jaffard $\Rightarrow G^{-1}$ decay | ◆ needs uniform separation (zeros lack it) — correctly flagged, blocked |
| GUE makes $1/\delta$ integrable | ✅ correct, but it is the $\ell^1/G^{-1}$ route (over-counts) |
| **Montgomery-scale "reversal" (coercivity not free)** | ❌ **ERROR** (coherence≠bandwidth; $P$ scale-invariant; flat kernel = over-sampling). Coercivity stays easy. |
| **lattice $G_0$ / Schur $\Rightarrow$ RFB** | ❌ **ERROR** ($G_0^{-1}\sim\rho\to\infty$; Schur gives $\|A\|\lesssim P\to\infty$). No $\ell^1$ route works. |
| RFB true? | ◆ **plausibly yes, $O(1)$ constant**, via $P$-cancellation (operator norm), needing only $S(T)$-level local regularity for the bulk + zero-density for deep zeros |

**Bottom line for the program.** The exploration's *instinct* — push into the fine geometry — is right, and
its *formulation* (RFB $=\|A\|$ bounded) is the correct target. But the two concrete reductions (Montgomery
reversal; Schur/lattice) are erroneous: **the over-sampling factor $P$ both forbids every $\ell^1$ proof and
guarantees the cancellation that makes RFB true.** So RFB is **less arithmetic-dependent than the GUE
framing suggested**: the bulk follows from classical $S(T)=O(\log)$ regularity, and **only the deep
off-line zeros need a zero-density input** (the long-standing §3.3 tier). Coercivity is **not** reopened.
**Montgomery/GUE is not the bottleneck for RFB; the deep-zero zero-density bound is** — and that was already
the named residual.

**Corrected next step:** make the cancellation/local-averaging argument rigorous (operator-norm bound on
$A$ via local LLN + $S(T)$), isolating the deep-off-line-zero term as the sole zero-density dependency.
