# Document 186 — Adversarial audit of Docs 174 and 177

**Program:** Riemann Hypothesis — Phase 58 (full audit)
**Mandate:** adversarial audit of D174 (coercivity/backward) and D177 (Hermite takeoff). Independent reconstruction of each proof before reading; the constants matter; backward-only with respect to the DBN flow in chart $H_t$. Includes the structural classification ordered by the director (COERCIVE / CORRELATIONAL / MIXED / REDUNDANT).
**Audited and accepted conventions:** chart $H_t$ (Polymath 15), $\partial_tH_t=-\partial_z^2H_t$; backward $\sigma=t_0-t$, $H_t=e^{\sigma\partial_z^2}H_{t_0}$; $\dot z_k=2\sum'(z_k-z_j)^{-1}$; balance law $\dot I=-2\kappa-D$, $D\ge0$ (Doc 167, certified, not re-audited); $\kappa$ = number of upper zeros (2 per quadruple: $z$, $-\bar z$) — convention verified consistent in both documents.

---

## 1. Audit of Doc 174

### 1.1. [PROP 174.1] Non-coercivity $D\ge cI$ — **CERTIFIED**

Independent reconstruction. For $z_1=\alpha+i\beta$ in the quadruple $\{\pm z_1,\pm\bar z_1\}$:
- conjugate $\bar z_1$: $2/(2i\beta)=-i/\beta$ ⟹ contribution to $\dot\beta$: $-1/\beta$;
- antipode $-z_1$: $2/(2z_1)=\bar z_1/|z_1|^2$ ⟹ contribution $-\beta/|z_1|^2$;
- mirror $-\bar z_1$: $2/(2\alpha)$ real ⟹ contribution $0$.

$\dot\beta=-1/\beta-\beta/|z_1|^2$; with two upper modes, $\dot I=4\beta\dot\beta=-4-4\beta^2/|z_1|^2$, $D=4\beta^2/|z_1|^2$, $D/I=2/|z_1|^2\to0$. Matches the document term by term. The counterexample to $D\ge cI$ is correct. ✓

### 1.2. [THM 174.2] Exponential coercivity — **CERTIFIED-WITH-ERRATUM** (E-186.4, wording)

The point of attack was the direction of the chain $\dot I\le-2I/M\le-2I$. Verified: $I\le\kappa M$ ⟹ $-2\kappa\le-2I/M$; and $-2I/M\le-2I$ **requires $M\le1$**, which the document does establish (strict band $|\mathrm{Im}\,z|<1$ at $t=0$ + Lemma 174.3 ⟹ $M(t)<1$ for $t\ge0$). The chain is in the correct order and the band hypothesis is used explicitly, not tacitly. **Scope warning that the statement already respects:** the inequality $-2I/M\le-2I$ would be reversed if $M>1$; the theorem only applies forward from $t\ge0$, where $M<1$. For backward readings ($t<0$, where $M(t)\ge2|t|$ can exceed 1) the document correctly uses only the form $\dot I\le-2I/M$ with $M\le\bar M$ (§2.1) — no error.

Integration verified: $d\log I\le-2\,dt/(M_0-2(t-t_0))$ ⟹ $I\le I_0\bigl(1-2(t-t_0)/M_0\bigr)$; the direction $M(s)\le M_0-2(s-t_0)$ ⟹ $-2I/M(s)\le-2I/(M_0-2(s-t_0))$ is correct. ✓

**Units/charts verified:** $I_\zeta=I/4$, $\tau=t/4$ ⟹ $dI_\zeta/d\tau=dI/dt$; $-2I=-8I_\zeta$ ✓; $M_\zeta=M/4<1/4$ ✓; $-2I_\zeta/M_\zeta=-2I/M$ ✓. The conversion is consistent (the E-171.x pattern does not repeat).

**E-186.4 (minor):** "exact linear extinction" — the formula is a linear upper bound, not an exact law (equality is only attained in the isolated pair). Wording, not mathematics.

### 1.3. [LEMMA 174.3] Maximum principle — **CERTIFIED**

Reconstructed: for maximal $\beta_k$, proper conjugate $=-2$ exactly; cross terms $-4\beta_k(\beta_k-\beta_l)/d^2\le0$ and $-4\beta_k(\beta_k+\beta_l)/d^2\le0$ without symmetrizing (correct: maximality gives the sign directly); antipode and reals $\le0$ (imaginary part of $1/(z-x)$ is $-\beta/|z-x|^2$). Absolute convergence of the sum over the real sea requires the RvM density of the class — hypothesis present via Thm 167-2.3. The direct attribution to de Bruijn Thm 13 is correct. ✓

### 1.4. [THM 174.4] Closed quadruple model — **CERTIFIED**

Full reconstruction:
- $H=z^4+az^2+c=(z^2-w)(z^2-\bar w)$ ⟹ $a=-2\mathrm{Re}\,w$, $c=|w|^2$; $\mathrm{Re}\,w=-a/2$, $(\mathrm{Im}\,w)^2=c-a^2/4$ ✓.
- $\partial_z^2H=12z^2+2a$ ⟹ $\dot a=-12$, $\dot c=-2a$ ✓.
- $\frac{d}{dt}\mathrm{Re}\,w=6$ ✓; $\frac{d}{dt}(\mathrm{Im}\,w)^2=\dot c-\tfrac{a\dot a}2=-2a+6a=4a=-8\mathrm{Re}\,w$ ✓.
- $t_c$: $24t^2+8R_0t-(\mathrm{Im}\,w_0)^2=0$ ⟹ the boxed formula ✓.
- **Expansion (where sign errors usually hide):** with $R=\alpha^2-\beta^2$, $\mathrm{Im}\,w_0=2\alpha\beta$: $\sqrt{R^2+6\alpha^2\beta^2}\approx R+3\alpha^2\beta^2/R-\tfrac92\alpha^4\beta^4/R^3$; $t_c\approx\frac{\alpha^2\beta^2}{2R}-\frac34\frac{\beta^4}{\alpha^2}=\frac{\beta^2}2+\frac{\beta^4}{2\alpha^2}-\frac{3\beta^4}{4\alpha^2}=\frac{\beta^2}2-\frac{\beta^4}{4\alpha^2}$ — **the term $-\beta_0^4/4\alpha_0^2$ and its sign (interaction accelerates) are correct**.
- Cross check: $\dot I=2\mathrm{Re}\,w/|w|-6=(-4\alpha^2-8\beta^2)/|z_1|^2=-4-4\beta^2/|z_1|^2$ = Prop 174.1 ✓.

The answer to the director ($t_c=\beta_0^2/2$, not $\beta_0^2/4$; $=I_0/4$ per quadruple) is arithmetically correct. ✓

### 1.5. [THM 174.5] Forward closure — **CERTIFIED** (combination of certified pieces + [KKL]).

### 1.6. [THM 174.8] Lifetime budget — **CERTIFIED**

Mandatory point of attack: the overlap of lifetimes. **Verdict: the overlap does not break anything because the proof does not use temporal disjointness.** The identity $\int_0^\Lambda\kappa\,dt=2\sum_j\ell_j$ is Fubini–Tonelli for indicator functions: $\kappa(t)=\sum_j2\cdot\mathbf 1_{\{j\text{ off}\}}$ is additive over simultaneous quadruples, and the integral counts each lifetime with correct multiplicity. If two quadruples overlap, $\kappa\ge4$ during the overlap and $\dot I\le-8$ there — which makes the inequality $I(0^+)\ge2\int\kappa$ **looser, never tighter** (the extra slack goes into the term $\int D\ge0$ and into the fact that integrating up to $\Lambda$ discards $I(\Lambda)\ge0$... in fact $I(\Lambda)=0$). The chain $I(\varepsilon)=\int_\varepsilon^\Lambda(2\kappa+D)\ge2\int_\varepsilon^\Lambda\kappa$ and monotone convergence: correct. The validity of the law through collisions rests on repair 5 of Doc 168 (certified, prerequisite). ✓

### 1.7. [THM 174.10] Moment hierarchy — **CERTIFIED** (the mandate's top suspicion resolves favorably)

Reconstruction of the cross term for $n\ge2$, which was the designated weak point:
$$\dot I_{2n}=-4n\sum_k\sum_{w\ne z_k}\beta_k^{2n-1}\frac{\beta_k-\mathrm{Im}\,w}{|z_k-w|^2}.$$
- Proper conjugate: $\beta_k^{2n-1}\cdot2\beta_k/(4\beta_k^2)=\beta_k^{2n-2}/2$ ⟹ $-2nI_{2n-2}$ ✓.
- Cross terms of type $(z_k,z_l)$: the denominators are **identical** ($|z_k-z_l|^2$); symmetrized numerator $\beta_k^{2n-1}(\beta_k-\beta_l)+\beta_l^{2n-1}(\beta_l-\beta_k)=(\beta_k-\beta_l)(\beta_k^{2n-1}-\beta_l^{2n-1})\ge0$ — **valid for every $n$ because $x\mapsto x^{2n-1}$ is increasing** (no need for a perfect square; monotonicity suffices: it is a 2-point Chebyshev inequality). The worry that "the binomial is not a perfect square for $n\ge2$" is unfounded: the $n=1$ proof did not use the square per se, but the monotonicity of $x\mapsto x$, and this scales.
- Cross terms of type $(z_k,\bar z_l)$: denominators $|z_k-\bar z_l|=|z_l-\bar z_k|$ (conjugation) ✓; numerator $(\beta_k+\beta_l)(\beta_k^{2n-1}+\beta_l^{2n-1})\ge0$ ✓. Same for the pairs with mirrors $-z_l,-\bar z_l$.
- Antipode and reals: trivially correct sign ($\beta_k^{2n}\ge0$).

$D_{2n}\ge0$ term by term **survives for every $n$**. Verified in the isolated pair ($D_{2n}=0$, free cascade) ✓. **The family $D_{2n}\ge0$ is sound; what falls is the virial corollary:**

### 1.8. [COR 174.11(2)] Virial family — **REFUTED in its proof; DOWNGRADED in its statement** (E-186.1, the main casualty of this audit)

**The false step, exhibited.** The proof claims: "$(I_{2n}/\kappa)^{1/n}\le(I_{2n-2}/\kappa)^{1/(n-1)}$ (power-mean monotonicity)", from which it deduces $I_{2n-2}\ge\kappa^{1/n}I_{2n}^{(n-1)/n}$. **Power-mean monotonicity says exactly the opposite:** for $a_k=\beta_k^2\ge0$ and exponents $n-1<n$,
$$\Bigl(\tfrac1\kappa\sum a_k^{\,n-1}\Bigr)^{1/(n-1)}\;\le\;\Bigl(\tfrac1\kappa\sum a_k^{\,n}\Bigr)^{1/n},$$
that is, $I_{2n-2}\le\kappa^{1/n}I_{2n}^{(n-1)/n}$ — the inequality used is **inverted**.

**Counterexample to the deduced differential inequality.** Two pairs with heights $a\gg b$ ($\kappa=4$, but the minimal case suffices): $I_{2n-2}\approx2a^{2n-2}$, $I_{2n}^{(n-1)/n}\approx(2)^{(n-1)/n}a^{2n-2}$. The inequality the proof needs, $I_{2n-2}\ge2^{1/n}I_{2n}^{(n-1)/n}$, requires $2\ge2^{1/n}\cdot2^{(n-1)/n}=2$ — exact equality in this case; but with a single dominant pair and $\kappa=2$ (a quadruple with $\beta_2\ll\beta_1$ after perturbation, or in the general class two pairs with disparate heights): $I_{2n-2}\approx a^{2n-2}<2^{1/n}a^{2n-2}\approx2^{1/n}I_{2n}^{(n-1)/n}$. The ODE $\dot I_{2n}\le-2n\,2^{1/n}I_{2n}^{(n-1)/n}$ **does not follow** from $\dot I_{2n}\le-2nI_{2n-2}$; the surplus would have to come from $D_{2n}$, which has no lower bound (Prop 174.1).

**What survives (downgraded version):**
1. The extremes are theorems via independent routes: $n=1$ ($\Lambda\le t_0+I/4$, Cor 167-2.4) and $n=\infty$ ($\Lambda\le t_0+M/2$, Lemma 174.3).
2. For intermediate $n$, a version with a worse constant holds: $I_{2n}\ge M^n$ (the maximal term) ⟹ $I_{2n}^{1/n}\ge M$ ⟹ by the band, $\boxed{\Lambda\le t_0+\tfrac12 I_{2n}(t_0)^{1/n}}$ — denominator $2$, not $2^{1+1/n}$. This version is **trivial modulo Lemma 174.3** (it adds no new information about the extremes).
3. Cor 174.11(1) ($\dot I_{2n}\le-2nI_{2n}$, decay $e^{-2nt}$) is **correct**: it uses only $I_{2n}\le M\,I_{2n-2}$ and $M<1$, verified.

**Impact:** the narrative "the hierarchy interpolates exactly between virial and band — a single family" is **downgraded to rhetoric**: the extremes are theorems, the interpolating interior is not proved with the announced constant (and the improvement $2^{1+1/n}$ vs $2$ is exactly what would make the family non-trivial). The "best theorem of the document" by its own verdict loses its star corollary; Theorem 174.10 ($D_{2n}\ge0$) remains intact.

### 1.9. [§3.3] Refutation of "$I<\infty\Rightarrow m<\infty$" in the class — **CERTIFIED** (load-bearing, verified)

Audit of the Hadamard configuration ($\gamma_j=2^j$, $b_j=e^{-\gamma_j}$, real zeros at RvM points), the three mandate items:

(i) **Class and convergence.** Zeros: real network of RvM density ($x_n\asymp$ solution of $N(x)=n$) plus quadruples $\{\pm\gamma_j\pm ib_j\}$. $\sum1/|z|^2<\infty$ (logarithmic density) ⟹ Hadamard product of genus $\le1$ converges; order $\le1<2$; symmetries (real on $\mathbb R$, even) constructible. The semigroup $e^{-t\partial_z^2}$ acts on order $<2$ (de Bruijn §2). ✓

(ii) **RvM.** The quadruples add $O(1)$ zeros per dyadic block $[2^j,2^{j+1}]$, which contains $\asymp2^j\log2^j$ real zeros: the RvM density is preserved with relative error $O(2^{-j})$. ✓

(iii) **Does it flow?** Potential objection: at $t=0$, $\kappa=\infty$ and the ODE system with infinitely many non-real zeros is not justified. **Correct resolution (implicit in the doc, made explicit here):** the flow is defined by the semigroup acting on the *function*, not by the ODEs; the ODEs are only invoked where $\kappa<\infty$. And for every $t>0$: quadruple $j$ lands at $t_j\approx b_j^2/2=e^{-2^{j+1}}/2$, summable and super-exponentially decreasing, so for every $t>0$ only the finitely many $j$ with $t_j>t$ remain off: $\kappa(t)<\infty$ — the configuration satisfies the KKL analogue by construction. Lifetimes $\ell_j\approx b_j^2/2$ with $\sum\ell_j\ll I/4$: consistent budget. ✓ (The super-exponential isolation makes the quadruples effectively independent: the model of Thm 174.4 applies with correction $O(b_j^2/\gamma_j^2)$.)

**The refutation holds.** The "ζ-free impossibilities" hanging from it (D176, D177 §4.3 double consistency, the two-tower architecture) retain their support.

### 1.10. Rest of Doc 174

- **[Calculation 174.6]** ($t_c=-g^2/8$): $H=z^2-g^2/4-2t$, zeros $\pm\sqrt{2t+g^2/4}$ ✓. **CERTIFIED** (elementary calculation).
- **[Prop 174.7]** (fixed-point network): $\partial_t(e^t\cos z)=e^t\cos z=-\partial_z^2(e^t\cos z)$ ✓. **CERTIFIED.** Note: $\cos z$ has zeros at $\pi(k+\frac12)$, constant spacing — not of growing RvM density; the *reading* ("density doesn't buy takeoffs") is legitimate as a counterexample to the density heuristic, but the fixed point is a highly non-generic configuration (every symmetry exact). Correct as used.
- **[Calculation 174.9]** ($\ell^2$ cluster): heuristic and labeled CALCULATION, not THEOREM — admissible under the contract. The exclusion of real–real collisions by repulsion ($\dot g=4/g+O(1)$) is correct for the minimal gap.
- **[Prop 174.12]** (entropy): $\varphi(\beta)=2\beta\log(1/\beta)-\beta$ ✓; $\varphi\ge0\iff\beta\le e^{-1/2}$, $\varphi'\ge0\iff\beta\le e^{-3/2}$ ✓; the symmetrization with monotone weight is the same (sound) mechanism of Thm 174.10. **CERTIFIED** (conditional on $\sup\beta\le e^{-3/2}$, declared).
- **[§2.3, GAP-174.B, orphans]:** speculation labeled GAP — no claims to audit; the slope-$2k$ heuristic of §2.3(b) was refuted by D177 itself, see below.

---

## 2. Audit of Doc 177

### 2.1. [THM 177.1] Exact Hermite takeoff — **CERTIFIED**

Identity $e^{s\partial_z^2}z^n=(-s)^{n/2}H_n\bigl(z/(2\sqrt{-s})\bigr)$, verified by hand:
- $n=2$: $(-s)H_2(z/2\sqrt{-s})=(-s)\bigl(4\cdot\frac{z^2}{4(-s)}-2\bigr)=z^2+2s$; direct: $e^{s\partial^2}z^2=z^2+2s$ ✓.
- $n=3$: $(-s)^{3/2}\bigl(8\frac{z^3}{8(-s)^{3/2}}-12\frac{z}{2\sqrt{-s}}\bigr)=z^3+6sz$; direct: $z^3+s\cdot6z$ ✓.
- $n=4$ (not requested by the doc, added here): direct $e^{s\partial^2}z^4=z^4+12sz^2+12s^2$; formula with $H_4=16x^4-48x^2+12$: $s^2\bigl[16\frac{z^4}{16s^2}\bigr]=z^4$; $(-s)^2(-48)\bigl(\frac{-z^2}{4s}\bigr)=12sz^2$; $12s^2$ ✓. Exact match.

Zeros $z=x_0+2i\sqrt\sigma\,h_j$ ✓ ($w=(z-x_0)/(2i\sqrt\sigma)$). Cross-check of moments: $\frac{d}{d\sigma}\sum z_k^2=-2n(n-1)$ via the symmetrization $\frac{z_k}{z_k-z_j}+\frac{z_j}{z_j-z_k}=1$ ✓; in the model $\sum z_j^2=-4\sigma\sum h_j^2$ and $\sum h_j^2=n(n-1)/2$ (from $H_n=2^nx^n-n(n-1)2^{n-2}x^{n-2}+\cdots$, $e_1=0$, $\sum h^2=-2e_2$; check $H_4$: $n(n-1)2^{n-2}=48$ ✓; check $H_3$: zeros $0,\pm\sqrt{3/2}$, sum $3=3\cdot2/2$ ✓) ⟹ $-2n(n-1)\sigma$ ✓. Perfect consistency.

### 2.2. [§1.2] Table and asymptotics — **CERTIFIED**

- $c(2)$: $H_2$ zeros $\pm1/\sqrt2$, $4\cdot\frac12=2$ ✓.
- $c(3)$: $h_{\max}^2=3/2$, $c=6$ ✓.
- $c(4)$: $16x^4-48x^2+12=0\iff4x^4-12x^2+3=0\iff x^2=\frac{3\pm\sqrt6}2$; $c(4)=4\cdot\frac{3+\sqrt6}2=2(3+\sqrt6)\approx10.899$ ✓.
- $c(5)$: $32x^4-160x^2+120=0\iff4x^4-20x^2+15=0\iff x^2=\frac{5\pm\sqrt{10}}2$; $c(5)=2(5+\sqrt{10})\approx16.32$ ✓.
- Asymptotics: $h_{\max}^2=(2n+1)-2^{2/3}|a_1|(2n+1)^{1/3}+O(1)$ ⟹ $c(n)=8n+4-2^{8/3}|a_1|(2n+1)^{1/3}+O(n^{-1/3})$ ✓ (the factor $2^{8/3}=4\cdot2\cdot2^{-1/3}$ verified). Bound $c(n)\le8n+4$ from $h_{\max}<\sqrt{2n+1}$ (classical) ✓.

**[PROP 177.2]** (refutation of the $2k$ constant of GAP-174.B): immediate consequence of the table, both readings of $k$ treated candidly. **CERTIFIED.** The heuristic of Doc 174 §2.3(b) correctly dies.

### 2.3. [PROP 177.3] Model with remainder — **CERTIFIED-WITH-RESERVATION**

The proof is a sketch (Rouché + Gaussian representation). The ingredients are standard and the logic correct, but: the separation of the rescaled Hermite zeros in the *bulk* is $\asymp\sqrt\sigma/\sqrt n$, not $\sqrt\sigma$ — the document acknowledges this in parentheses ("except for the local semicircle density factor") without propagating that factor into the displacement constant. For the quantity used downstream ($\beta_{\max}$, edge zeros, separation $\asymp\sqrt\sigma\,n^{-1/6}$) the loss is polynomial in $n$ and gets absorbed if $\sqrt{n\sigma}/d$ is small with polynomial margin. Reservation: the statement as written ($O(\sqrt{n\sigma}\cdot\sqrt{n\sigma}/d)$ uniform in $j$) is not proved for the bulk with that constant. It is not used quantitatively in 177.6–177.8 (which proceed term by term), so the reservation does not propagate.

### 2.4. [LEMMA 177.4] Sea bound — **CERTIFIED** (sum inside/outside the window $|x-\alpha|\le\beta$ reconstructed: $\rho\beta$ terms of size $\le1/\beta$ plus integrable tail ⟹ uniform $C\rho$ ✓; absolute convergence under RvM ✓).

### 2.5. [PROP 177.5] Stacked quartet — **CERTIFIED**

Reconstruction: with $w_i=-\beta_i^2$ roots of $X^2+aX+c$: $S=\beta_1^2+\beta_2^2=a$, $P=c$. Backward ($\sigma$): $a'=12$, $c'=2a$ ⟹ $S'=12$, $P'=2S$ ✓; $P=P_0+2S_0\sigma+12\sigma^2$ ✓; $(S^2-4P)'=24S-8S=16S>0$ ✓ (no fusion at height); asymptotics $S\sim12\sigma$, $P\sim12\sigma^2$, $\sqrt{S^2-4P}\sim4\sqrt6\,\sigma$, $\beta_2^2\sim(6+2\sqrt6)\sigma=c(4)\sigma$ ✓ — the exact saturation of the Hermite law of the fused cluster is a notable consistency check and passes. Bound $\beta_2^2\le S\le S_0+12\sigma$ trivial from $P\ge0$ ✓. "Theft" fractions $(6\pm2\sqrt6)/12$ ✓.

### 2.6. [THM 177.6] Global bound $2n^2\sigma$ — **CERTIFIED-WITH-ERRATUM** (E-186.2, conservative constant)

Blocks reconstructed:
1. Proper conjugate: $4\beta_k\cdot2\beta_k/(4\beta_k^2)=2$ per upper mode ⟹ $2\kappa_W$ ✓.
2. Cross terms: per unordered pair $(k,l)$, symmetrizing over identical denominators: numerators $(\beta_k-\beta_l)^2$ and $(\beta_k+\beta_l)^2$, each $\le d^2$ because $|z_k-z_l|\ge|\beta_k-\beta_l|$ and $|z_k-\bar z_l|\ge\beta_k+\beta_l$ (the complex distance dominates the vertical component — correct as written). With the factor $4$: $\le8$ per unordered pair ⟹ total $\le8\cdot\binom{\kappa_W}2=4\kappa_W(\kappa_W-1)$. **The document writes $8\kappa_W(\kappa_W-1)$: a factor-2 slack** (it counts ordered pairs). As it is an upper bound, the theorem remains valid; the actual inner sum is $\le2\kappa_W(2\kappa_W+2r_W-1)$, better than announced. Harmless erratum in the safe direction.
3. Reals: $4\beta_k^2/|z_k-x|^2\le4$ ✓ ($|z_k-x|\ge\beta_k$); total $\le4\kappa_Wr_W$ ✓.
4. Final arithmetic: $2\kappa(1+4\kappa-4+2r)=2\kappa(4\kappa+2r-3)$ ✓; with $n=2\kappa+r$: $4\kappa+2r-3=2n-3$ exact ✓; $2\kappa(2n-3)\le n(2n-3)\le2n^2$ ✓.
5. Exterior via Lemma 177.4 + Cauchy–Schwarz ✓; Grönwall with small multiplicative term: standard ✓.

Calibration against the monomial ($dI_W/d\sigma=n(n-1)$ exact: upper half of $2n(n-1)$... verified: $I_W=\sum_{\beta>0}\beta^2=-\frac12\mathrm{Re}\,\sum z_j^2$ in the purely vertical case, $\frac{d}{d\sigma}=n(n-1)$ ✓): factor $\approx2$ of energy slack, as claimed. ✓

### 2.7. [THM 177.7] Landings at the corner — **CERTIFIED-WITH-ERRATUM** (E-186.3, conditional on Lemma 177.B)

**Contradiction logic (the two cases):** if $\gamma_c\ge\Gamma(t_c)$ then, since $\Gamma$ decreases in $t$, $\gamma_c\ge\Gamma(t_c+\delta)$ for every $\delta>0$ and Lemma 177.B applies to the newly born gap at $t_c+\delta$: $C\sqrt\delta\log\gamma_c\ge c\,(t_c+\delta)^\theta\ge c\,t_c^\theta$. Taking $\delta\to0^+$ the left side $\to0$: contradiction. Hence $\gamma_c<\Gamma(t_c)$. **Correct**, including the sign note (the lemma forbids small gaps *above* $\Gamma$; the landing creates them; therefore the landing lives *below*). The direction of the unfolding is used as an upper bound of the gap ($g\le C\sqrt\delta$, from the normal form), which is the direction needed. The intermediate sentence with $\delta=t_c$ is an unnecessary detour but not false.

**Exponent algebra in (2), reconstructed:**
- $\gamma_j\le\exp(t_j^{-(1/2-\theta)})$ ⟹ $t_j\le(\log\gamma_j)^{-2/(1-2\theta)}$ ✓.
- **E-186.3:** the document writes "$n_j\le C\rho(\gamma_j)\sqrt{n_jt_j}$ ... i.e. $n_j\le C\sqrt{t_j}\log\gamma_j$". Solving the self-consistency gives $\sqrt{n_j}\le C\rho\sqrt{t_j}$, that is $\boxed{n_j\le C^2\rho^2t_j=C\,t_j\log^2\gamma_j}$ — **not** $C\sqrt{t_j}\log\gamma_j$. The "i.e." is false as a direct implication. **However**, in the regime imposed by the chain, $x:=t_j\log^2\gamma_j\le(\log\gamma_j)^{2-2/(1-2\theta)}<1$ (since $2/(1-2\theta)>2$), and for $x<1$ one has $x\le\sqrt x$, so the bound as written is *weaker than the correct one* and hence valid a posteriori. With the correct bound the result improves: $n_j\le\max(2,Ct_j\log^2\gamma_j)=2$ eventually ⟹ $b_j^2\le Ct_j\le C(\log\gamma_j)^{-2/(1-2\theta)}$ ⟹ $b_j\le(\log\gamma_j)^{-1-\eta'}$ with $\eta'=\frac{2\theta}{1-2\theta}>0$. With the chain as written: $b_j^2\le Ct_j^2\log^2\gamma_j\le C(\log\gamma_j)^{2-4/(1-2\theta)}$, exponent $<-2$ for $\theta<\frac12$ ⟹ $b_j\le(\log\gamma_j)^{-1-\eta}$, $\eta=\frac{4\theta}{1-2\theta}>0$ ✓. **The qualitative conclusion ($b_j\le(\log\gamma_j)^{-1-\eta}$, $\eta>0$) is correct via both routes**; the erratum affects the value of $\eta$ and the tidiness of the step, not the theorem.
- The validity of the far-sea range ($t_j\ll(n_j\log^2\gamma_j)^{-1}$) guaranteed a posteriori by the chain: with $n_j\le2$ and $t_j\log^2\gamma_j\to0$, ✓.
- $m=\infty$ + KKL ⟹ $t_j\to0^+$; bounded heights only host finitely many quadruples ✓.

**Candid conditional status:** Lemma 177.B is declared as an unproved literature GAP, and the diffusive plausibility ($\Gamma(t)=\exp(t^{-(1/2-\theta)})<\exp(t^{-1/2})$ = the side where heat has already acted) is reasonable but not a proof. Correctly labeled.

### 2.8. [COR 177.8] — **CERTIFIED** (conditional on 177.B ∧ LP-134; the logical implication is immediate from Thm 177.7(2) and is valid). The double consistency against the Hadamard counterexample verified: $b_j=e^{-\gamma_j}$ violates LP-134 ($b_j\log\gamma_j\to0$) and its landings ($t_j\approx e^{-2^{j+1}}/2$, $\gamma_j=2^j$) are astronomically below $\Gamma(t_j)$ — the cut is clean and neither hypothesis is redundant ✓.

### 2.9. [THM 177.10] Orphans — **CERTIFIED-WITH-RESERVATION**

(1) and (3) are a direct application of 177.6 + superadditivity of §2.2 (verified: $G(n)=2n^2$ and $G=c(n)$ superadditive ✓; the monotone gluing at fusions is correct). (2): $M(t)\ge M(0)+2|t|\ge b_{\max}^2$ via Lemma 174.3 backward ✓; the carrier of $M$ is orphaned when $|t|<b_{\max}^2/(4n(t)^2)$ ✓. **Structural reservation (not an erratum):** the whole theorem is conditional on the "current-scale separation hypothesis" at $(t,0)$, which is not proved for any concrete configuration and which, in the dense ζ regime ($n(t)\asymp\rho\sqrt{|t|}$ growing), is exactly the hard part. The document declares it; the detection window $|t|\lesssim\min(b_{\max}^2,\rho^{-2})$ is non-empty but its useful non-emptiness depends on $b_{\max}$ vs $\rho^{-1}$ — for the corner pathology of Thm 177.7 itself ($b\le(\log\gamma)^{-1-\eta}\ll\rho^{-1}$) the window is minuscule and the backward census inoperative in practice. Consistent with the doc's conclusion that the forward route is the good one.

---

## 3. Structural classification (ordered by the director)

Key question: does the dynamical apparatus produce information that is NOT a reformulation of "the off zeros exist/do not exist"?

| Piece | Class | ζ-free | Comment |
|---|---|---|---|
| Thm 174.2 + Lemma 174.3 (coercivity, maximum) | **COERCIVE** | yes | Genuine inequalities, but ζ-free ⟹ by §3.3 cannot decide RH alone |
| Thm 174.8 (budget $\sum\ell\le I/4$) | **COERCIVE** | yes | Real energy↔lifetime conversion; same limitation |
| Thm 174.10 (hierarchy $D_{2n}\ge0$) | **COERCIVE** | yes | Sound; its intermediate virial corollary fell |
| Cor 174.11(2) (virial family) | **REDUNDANT** (after downgrade) | yes | Surviving version trivial modulo band; extremes already known |
| Thm 174.4 / Prop 174.1 / Calc 174.6 | **COERCIVE** (exact models) | yes | Calibrate constants; the content is model-based |
| Thm 174.5(3) ("RH lives in $t\le0$") | **CORRELATIONAL** | yes | Reformulation: relocates the dichotomy, does not reduce it |
| §2.3(c) (transport of the dichotomy) | **CORRELATIONAL** | — | The doc itself admits it: the backward computes $I(0)$ |
| Prop 174.7 (fixed-point network) | **MIXED** | yes | Coercive in itself; its *reading* (gap fluctuations = arithmetic gate) is the valuable correlational content |
| §3.3 (welding refutation) | **COERCIVE-NEGATIVE** | yes | Closure by counterexample; load-bearing, verified |
| Thm 177.1/177.5, table $c(n)$ | **COERCIVE** (exact model) | yes | New-to-the-program mathematics, flawless |
| Thm 177.6 (bound $2n^2\sigma$) | **COERCIVE** | yes | The central technical theorem of D177 |
| Thm 177.10 (orphans) | **CORRELATIONAL** | yes | It is the dynamical *definition* of ¬RH-finite; adds no information, organizes |
| Thm 177.7 + Cor 177.8 | **MIXED** | **no** | **The only piece of the block that produces non-reformulative information**: quantitative confinement of the pathology ($\gamma$ super-exponential, $b\le(\log\gamma)^{-1-\eta}$) conditional on 177.B; the welding 177.B∧LP-134⟹$m<\infty$ reduces the needed arithmetic input to a single repulsion |

**Answer to the director's question:** everything unconditional in D174/D177 is ζ-free and, by the (verified) counterexample of §3.3, **incapable by construction of deciding RH**: it is geometry of the class. The non-reformulative value of the block is concentrated in a single point: the pair (Lemma 177.B, LP-134) as minimal separate hypotheses — the dynamics reduced the *size* of the needed arithmetic input, which is real progress even if conditional. The rest of the coercive apparatus (budgets, hierarchies, virials) bounds *how long* off zeros live if they exist, never *whether* they exist: correlation with the dichotomy, not resolution.

---

## 4. Table of verdicts

| Result | Verdict |
|---|---|
| Prop 174.1 (non-coercivity $D\ge cI$) | **CERTIFIED** |
| Thm 174.2 (coercivity $\dot I\le-2I/M\le-2I$) | **CERTIFIED-WITH-ERRATUM** (E-186.4, wording) |
| Lemma 174.3 (maximum principle) | **CERTIFIED** |
| Thm 174.4 (exact $t_c$ of the quadruple) | **CERTIFIED** (expansion and sign verified) |
| Thm 174.5 (forward closure) | **CERTIFIED** |
| Calc 174.6 / Prop 174.7 | **CERTIFIED** |
| Thm 174.8 (budget $\sum\ell_j\le I(0^+)/4$) | **CERTIFIED** (overlap: the identity counts it exactly) |
| Calc 174.9 (clusters) | no theorem label; admissible heuristic |
| Thm 174.10 (hierarchy, $D_{2n}\ge0$ ∀n) | **CERTIFIED** (the symmetrization scales: monotonicity of $x^{2n-1}$, not squares) |
| Cor 174.11(1) (decay $e^{-2nt}$) | **CERTIFIED** |
| **Cor 174.11(2) (virial family $2^{1+1/n}$)** | **REFUTED in its proof / DOWNGRADED** (E-186.1: inverted power mean; $\Lambda\le t_0+I_{2n}^{1/n}/2$ survives, trivial, + extremes $n=1,\infty$) |
| Prop 174.12 (entropy) | **CERTIFIED** (declared conditional) |
| §3.3 refutation "$I<\infty\Rightarrow m<\infty$" in the class | **CERTIFIED** (the mandate's three checks pass) |
| Thm 177.1 (exact Hermite) + table §1.2 | **CERTIFIED** ($n=2,3,4$, moments, $c(2..5)$, asymptotics: all verified by hand) |
| Prop 177.2 (refutation of $2k$) | **CERTIFIED** |
| Prop 177.3 (model with remainder) | **CERTIFIED-WITH-RESERVATION** (sketch; bulk separation not propagated; not used downstream) |
| Lemma 177.4 (sea) | **CERTIFIED** |
| Prop 177.5 (stacked quartet) | **CERTIFIED** (saturates $c(4)\sigma$: strong consistency check, passes) |
| Thm 177.6 (bound $2n^2\sigma$) | **CERTIFIED-WITH-ERRATUM** (E-186.2: cross terms $\le4\kappa(\kappa-1)$, the doc writes $8\kappa(\kappa-1)$ — slack, safe direction) |
| Thm 177.7 (corner) | **CERTIFIED-WITH-ERRATUM** (E-186.3: step "$n_j\le C\sqrt{t_j}\log\gamma_j$" mis-derived but valid a posteriori; conclusion and $\eta>0$ correct; conditional on 177.B) |
| Cor 177.8 (177.B ∧ LP-134 ⟹ $m<\infty$) | **CERTIFIED** (conditional; implication valid; double consistency verified) |
| Thm 177.10 (orphans) | **CERTIFIED-WITH-RESERVATION** (separation hypothesis unproved; detection window minuscule in the relevant regime) |

## 5. Errata

- **E-186.1 (Cor 174.11(2), SERIOUS):** the proof invokes "power-mean monotonicity" in the reverse direction: the truth is $(I_{2n-2}/\kappa)^{1/(n-1)}\le(I_{2n}/\kappa)^{1/n}$, i.e. $I_{2n-2}\le\kappa^{1/n}I_{2n}^{(n-1)/n}$, the opposite of what is used. The ODE $\dot I_{2n}\le-2n\,2^{1/n}I_{2n}^{(n-1)/n}$ fails for profiles with one dominant pair. The virial family $\Lambda\le t_0+I_{2n}^{1/n}/2^{1+1/n}$ is left unproved for $2\le n<\infty$; correct Doc 174 §4.2 and its verdict ("interpolates exactly" ⟶ "the extremes are theorems; the interior, open").
- **E-186.2 (Thm 177.6, minor):** the correct cross-term bound is $4\kappa_W(\kappa_W-1)$ (unordered pairs), not $8\kappa_W(\kappa_W-1)$; the theorem improves to $2\kappa_W(2\kappa_W+2r_W-1)$, still $\le2n^2$.
- **E-186.3 (Thm 177.7(2), minor):** "$n_j\le C\rho\sqrt{n_jt_j}$ i.e. $n_j\le C\sqrt{t_j}\log\gamma_j$" — the correct resolution is $n_j\le C\rho^2t_j=Ct_j\log^2\gamma_j$; the form as written only holds a posteriori in the regime $t_j\log^2\gamma_j<1$. With the correct form, $\eta$ improves to $2\theta/(1-2\theta)$ and in fact $n_j\le2$ eventually. Conclusion intact.
- **E-186.4 (Thm 174.2, wording):** "exact linear extinction" should be "linear extinction bound".

## 6. Downstream impact

- **Fall of Cor 174.11(2):** affects only the narrative "a single interpolating family" (cited in D174's verdict and in the phase summary as "moment hierarchy interpolates from de Bruijn ($n=\infty$)"). **Nothing technical hangs on the intermediate $n$'s**: D176 and D177 use $n=1$ (energy budget/virial) and $n=\infty$ (band), both intact. Correct the phase memory: the interpolation is conjectural, the extremes are theorems.
- **177.7/177.8 (feed tower 2 via D178/179): SURVIVE.** Errata E-186.2/3 do not touch the conclusion $b_j\le(\log\gamma_j)^{-1-\eta}$ nor the welding 177.B∧LP-134⟹$m<\infty$. The second tower remains standing with its declared conditional status (177.B open, LP-134 conjectural).
- **§3.3 (Hadamard flows) verified:** all the "ζ-free impossibilities" of the program that rest on it (D176, D177's double consistency, the two-tower architecture) retain their support.
- **Thm 174.10 ($D_{2n}\ge0$) certified:** available as a tool; but note that after the fall of the intermediate virial, its only non-trivial consumer today is Cor 174.11(1).

**Audit balance:** 1 proof refutation with downgrade (Cor 174.11(2)), 2 certified-with-reservation, 4 errata; the core of both documents (174.2/3/4/8/10, §3.3, 177.1/5/6/7/8) withstands term-by-term reconstruction. Casualty rate within the historical pattern (~1/4 counting the star corollary).
