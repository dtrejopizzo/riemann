# Document 173 — The structural representation of $I(0^+)$: sum rules, the shadow–signal theorem, and the Green–Littlewood identity

**Program:** Riemann Hypothesis — Phase 55 (two arrows)
**Mandate (Problem A / Phase A):** represent $I(0^+)=\sum_j b_j^2$ as a natural arithmetic functional — ideally $I=\|F\|_{\mathcal H}^2$ — so that $I<\infty$ (and ultimately $I=0$) is a question of regularity/membership and not of zero localization. RH or any positivity is NOT attempted.
**Accepted machinery (not re-derived):** balance law $\dot I=-2\kappa-D$ (Phase 54); $E(T)=\sum_{\gamma\le T}b^2\ll T/\log T$ (Selberg, certified); RH $\iff I(0^+)=0$; ceiling $T/\log T$ for window certification (Theorem 172.9 — windows are not retried here).
**Contract:** [NEW-DEFINITION] free; [THEOREM]/[PROP]/[LEMMA] with full proof or unlabeled; [BRIDGE] honest; [GAP] declared.

**Coordinates (identical to Doc 170/175).** Off-critical zero $\rho=\tfrac12+b+i\gamma$, $b\in(0,\tfrac12)$, $\gamma>0$; one representative per quadruple $\{\rho,\bar\rho,1-\rho,1-\bar\rho\}$. On-line zeros: pairs $\{\tfrac12\pm i\gamma\}$.
$$I=I(0^+):=\sum_{\text{quad. }j} b_j^2,\qquad I(T):=\sum_{\gamma_j\le T}b_j^2 .$$

---

## 0. Executive summary and verdict

**The hard deliverable is met in its two complementary strands:**

1. **[THEOREM 173.A] (shadow–signal — the obstruction).** In the class $X$ of self-contained holomorphic representations ($\sum_\rho\Phi(\rho)$ with $\Phi$ holomorphic, the class reaching the explicit formula), the quadratic weight multiplying $b^2$ is **exactly the curvature of the shadow**: $w_\Phi(\gamma)=-2\,\varphi_r''(\gamma)$ where $\varphi_r=\mathrm{Re}\,\Phi$ on the critical line. Exact consequences: *no signal without a shadow*; if $w_\Phi\ge0$ then $\int_0^\infty w_\Phi=2\varphi_r'(0)<\infty$ (every admissible weight is **integrable**: neither constant weight nor even $1/\gamma$ is reachable) and $\int_0^\infty t\,w_\Phi(t)\,dt=2|\varphi_r(0)|$ (**mass-height law**: weight up to height $T$ costs shadow depth $T^2$). This is the structural reason for ceiling 172.9 seen from another face: it is not an artifact of windows but of the **holomorphy of the probe**. The extension to quadratic functionals (Parseval, $\int|\mathcal E|^2$) is [PROP 173.D].

2. **[THEOREM 173.C] (the Green–Littlewood identity — the representation).** The way out is **non-holomorphic** ($\log|\zeta|=\mathrm{Re}\log\zeta$; taking the real part is not holomorphic, exactly the escape 173.A predicts). Exact, unconditional identity, **with weight 1 in $\gamma$** (no decaying weight):
$$\boxed{\;I(T)\;=\;\frac1\pi\int_{1/2}^{\infty}\!\!\int_0^T \log|\zeta(\sigma+it)|\,dt\,d\sigma\;+\;\frac18\;-\;\frac{1}{2\pi}\int_{1/2}^\infty\!\Big(\sigma-\tfrac12\Big)^2\,\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma\;}$$
for every $T$ that is not a zero ordinate. The residue is no longer a **multiplicative weight** but an **additive boundary flux** at height $T$, of size $O(\log^2 T)$ at good heights. $I$ is the **transversal second moment of the Riesz measure of $\log|\zeta|$** in the right half-strip; the first moment is classical Littlewood, the zeroth moment is the density $N(\sigma,T)$.

3. **[PROP 173.E] (membership, dichotomous form).** With $\tilde d$ = the Green potential of the off zeros in the half-plane $\sigma>\tfrac12$ (pole subtracted): RH $\iff \|\nabla\tilde d\|_{L^2}^2<\infty$, and the norm only takes the values $\{0,\infty\}$. It is the first literal formulation of "RH = membership in a space" within the program — but degenerate: the atomic dichotomy prevents the norm from **grading** $I$. The obstruction to exact $I=\|F\|^2$ is identified: **the infinite self-energy of the atoms** (the zeros are point charges). A desingularization program at the end.

**Best representation achieved:** 173.C. **Weight left over:** none in $\gamma$; the residue is the boundary flux $O(\log^2T)$ plus the exact constant $1/8$ (from the pole at $s=1$), and the defect that the integrand $\log|\zeta|$ is *signed* (it is a moment of a positive measure, not yet a quadratic norm of an arithmetic object).

---

## 1. Preliminaries: the quadruple and the class of representations

**[NEW-DEFINITION] (class $X$ of self-contained holomorphic representations).** $\mathcal F\in X$ if there exists $\Phi$ holomorphic in the open strip $0<\mathrm{Re}\,s<1$ with
(i) real symmetry: $\Phi(\bar s)=\overline{\Phi(s)}$ and $\Phi(1-s)=\Phi(s)$;
(ii) decay: $\varphi(t):=\Phi(\tfrac12+it)$ satisfies $\varphi(t)\to0$, $\varphi'(t)\to0$ ($t\to\infty$), and $\sum_\rho|\Phi(\rho)|<\infty$ for every zero configuration compatible with $N(T)\sim\frac{T}{2\pi}\log T$;
(iii) $\mathcal F=\sum_\rho\Phi(\rho)$.
We write $\varphi_r:=\mathrm{Re}\,\varphi$ (the **shadow** of $\Phi$). Class $X$ is exactly the one reaching Weil's explicit formula: for $\Phi$ of Mellin type, $\sum_\rho\Phi(\rho)$ is an explicit arithmetic functional (prime side + archimedean term). *Symmetrization remark:* the zero multiset is invariant under $\rho\mapsto1-\rho$ and $\rho\mapsto\bar\rho$; hence, for any holomorphic $\Phi_0$, $\sum_\rho\Phi_0(\rho)=\sum_\rho\Phi(\rho)$ with $\Phi:=\tfrac14[\Phi_0(s)+\Phi_0(1-s)+\overline{\Phi_0(\bar s)}+\overline{\Phi_0(1-\bar s)}]$, which satisfies (i). Hypothesis (i) loses no generality within $X$.

**[LEMMA 173.0] (quadruple expansion).** Let $\Phi$ be as in (i), holomorphic in a neighborhood of the segment $[\tfrac12-b,\tfrac12+b]\times\{\gamma\}$. Then the contribution of the quadruple $\{\tfrac12\pm b\pm i\gamma\}$ is real and **even in $b$**, with
$$\Sigma_{\mathrm{quad}}(b,\gamma)\;=\;4\,\varphi_r(\gamma)\;+\;b^2\,w_\Phi(\gamma)\;+\;R_4,\qquad
w_\Phi(\gamma):=2\,\mathrm{Re}\,\Phi''(\tfrac12+i\gamma)=-2\,\varphi_r''(\gamma),$$
$$|R_4|\;\le\;\frac{b^4}{6}\max_{|x|\le b}\big|\Phi^{(4)}(\tfrac12+x+i\gamma)\big| .$$
An on-line pair $\{\tfrac12\pm i\gamma\}$ contributes exactly $2\varphi_r(\gamma)$.

*Proof.* By (i), $\Phi(\tfrac12+b-i\gamma)=\overline{\Phi(\tfrac12+b+i\gamma)}$, hence
$\Sigma_{\mathrm{quad}}=2\,\mathrm{Re}\big[\Phi(\tfrac12+b+i\gamma)+\Phi(\tfrac12-b+i\gamma)\big]$.
Taylor in $b$ around $\tfrac12+i\gamma$: odd orders cancel between $+b$ and $-b$; what remains is $2\,\mathrm{Re}[2\Phi+b^2\Phi''+\tfrac{2b^4}{4!}\Phi^{(4)}(\xi)]$ with Lagrange remainder on the segment. The identity $\mathrm{Re}\,\Phi''(\tfrac12+i\gamma)=-\varphi_r''(\gamma)$ follows from $\varphi(t)=\Phi(\tfrac12+it)\Rightarrow\varphi''(t)=-\Phi''(\tfrac12+it)$. The parity in $b$ is also visible structurally: $b\mapsto-b$ permutes the quadruple. $\square$

**Reading.** Throughout class $X$: the **zeroth order** (the shadow $4\varphi_r(\gamma)$, evaluated at the true ordinates, which are not a separate arithmetic datum) and the **signal** ($b^2w_\Phi$) are welded by $w_\Phi=-2\varphi_r''$. Everything that follows in §2–§4 exploits or suffers this weld.

---

## 2. Hadamard's sum rules: the exact algebra of the quadruple

### 2.1. The basic sum rule and the exact extraction of $b^2$

From the Hadamard product of $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$ (Hadamard 1893; Davenport, *Multiplicative Number Theory*, ch. 12):
$$\sum_\rho\frac1\rho\;=\;1+\frac{\gamma_E}2-\frac12\log 4\pi,\qquad\Longrightarrow\qquad
\sum_\rho\frac1{\rho(1-\rho)}\;=\;2+\gamma_E-\log 4\pi\;\approx\;0.0462,$$
using $\frac1{\rho(1-\rho)}=\frac1\rho+\frac1{1-\rho}$ and that $\rho\mapsto1-\rho$ permutes the zeros. **Unconditional and arithmetic.**

**Quadruple algebra (exact, real).** With $a:=\tfrac14+\gamma^2$, $A:=a-b^2$, $B:=2b\gamma$: for $\rho=\tfrac12+b+i\gamma$ one has $\rho(1-\rho)=\tfrac14-(b+i\gamma)^2=A-iB$, and $\rho$, $1-\rho$ give the same value; $\bar\rho$, $1-\bar\rho$ give $A+iB$. Hence
$$\Sigma_{\mathrm{quad}}\Big[\tfrac1{\rho(1-\rho)}\Big]\;=\;\frac{4A}{A^2+B^2}
\qquad\text{(real, exact)} .$$
The exact extraction of $b^2$ against the on-line value (with the quadruple's multiplicity 4):
$$\frac{4A}{A^2+B^2}-\frac4a\;=\;-\,\frac{4\,b^2\,\big(3\gamma^2-\tfrac14+b^2\big)}{a\,\big(A^2+B^2\big)}
\;=\;\frac{b^2\,(1-12\gamma^2)}{(\tfrac14+\gamma^2)^3}\;+\;O\!\Big(\frac{b^4}{\gamma^6}\Big).$$
*(Cross-check with Lemma 173.0: $\Phi=1/(s(1-s))=(\tfrac14-u^2)^{-1}$, $u=s-\tfrac12$, gives $2\,\mathrm{Re}\,\Phi''(\tfrac12+i\gamma)=(1-12\gamma^2)/a^3$. Matches.)*

**Conclusion of the basic sum rule:** the energy appears with exact weight $w(\gamma)=(1-12\gamma^2)/(\tfrac14+\gamma^2)^3\sim-12/\gamma^4$ — weight $1/\gamma^4$, **negative** for $\gamma>1/\sqrt{12}$, and welded to the non-arithmetic shadow $\sum_j 4/a_j$. Exactly as the director's pointer had anticipated.

### 2.2. The full family of moments at $s=\tfrac12$

$\xi(\tfrac12+w)$ is even and entire of order 1; its zeros in $w$ are $\pm(b_j\pm i\gamma_j)$ (on line: $\pm i\gamma_j$). Taking $\log$ of the Hadamard product ($\xi(\tfrac12+w)=\xi(\tfrac12)\prod_j(1-w^2/w_j^2)$, $w_j$ the zeros of the upper half-plane):
$$\log\xi(\tfrac12+w)-\log\xi(\tfrac12)\;=\;-\sum_{k\ge1}\frac{M_k}{k}\,w^{2k},
\qquad M_k:=\sum_j\frac1{w_j^{2k}} .$$
The $M_k$ are **arithmetic and unconditional** (Taylor coefficients of $\xi$ at $\tfrac12$, computable from the $\eta$-series/Stieltjes constants; e.g. $M_1=-\,\xi''(\tfrac12)/(2\,\xi(\tfrac12))$). Similarly $\sum_\rho(\rho(1-\rho))^{-k}$ is expressed polynomially in $M_1,\dots,M_k$ via $\rho(1-\rho)=\tfrac14-w^2$.

**Quadruple algebra for $M_k$ (exact).** The two upper zeros of the quadruple are $b+i\gamma$ and $-b+i\gamma$, and $(-b+i\gamma)^{2k}=(b-i\gamma)^{2k}$:
$$\Sigma_{\mathrm{quad}}\Big[\tfrac1{w^{2k}}\Big]\;=\;2\,\mathrm{Re}\,(b+i\gamma)^{-2k}
\;=\;\frac{2(-1)^k\cos\!\big(2k\arctan(b/\gamma)\big)}{(b^2+\gamma^2)^k}
\;=\;\frac{2(-1)^k}{\gamma^{2k}}\Big(1-\frac{2k^2b^2}{\gamma^2}+O\big(\tfrac{k^2b^2}{\gamma^2}\big)^2\Big)\Big(1+O\big(\tfrac{kb^2}{\gamma^2}\big)\Big).$$
**Signal:** $b^2$ with weight $\asymp k^2/\gamma^{2k+2}$. Raising $k$ concentrates the weight on the first zero and decays even faster in $\gamma$: the family of moments at a fixed point **does not de-weight**; it moves the weight further down. De-weighting requires superposition (moving point / infinite family) — §3 and §4 say exactly how far this can go.

---

## 3. The shadow–signal theorem: the exact obstruction within class $X$

**[THEOREM 173.A] (shadow–signal).** Let $\Phi$ be of class $X$ (Def. §1), with $\varphi_r\in C^2[0,\infty)$ and $w_\Phi:=-2\varphi_r''$. Then:

**(a) (weld)** In the expansion of Lemma 173.0, the quadratic weight is $w_\Phi=-2\varphi_r''$: the signal is exactly $(-2)\times$ the curvature of the shadow. In particular $w_\Phi\equiv0\iff\varphi_r$ affine $\iff$ (by $\varphi_r\to0$) $\varphi_r\equiv0$: **no signal without a shadow**, and the shadow $\sum_j4\varphi_r(\gamma_j)$ is evaluated at the true ordinates (it is not an arithmetic datum separate from $\sum_\rho\Phi(\rho)$ itself).

**(b) (mass law)** If $w_\Phi\ge0$ on $[0,\infty)$, then $\varphi_r$ is concave, $\varphi_r\le0$, $\varphi_r'\ge0$ decreasing, and
$$\int_0^\infty w_\Phi(t)\,dt\;=\;2\,\varphi_r'(0)\;<\;\infty .$$
**Every non-negative weight of class $X$ is integrable.** Constant weight, $w\sim1$, and even $w\sim1/\gamma$, are unreachable.

**(c) (mass-height law)** Under (b), moreover
$$\int_0^\infty t\,w_\Phi(t)\,dt\;=\;-2\,\varphi_r(0)\;=\;2\,|\varphi_r(0)|\;\le\;2\,\|\varphi_r\|_\infty .$$
Placing weight mass $\ge\delta$ at heights $\sim T$ costs shadow depth $\gtrsim\delta T^2$ at $t=0$.

**(d) (negative tail)** If instead $\varphi_r\ge0$ and $\varphi_r\to0$ with $\varphi_r\not\equiv0$, then $w_\Phi<0$ along a sequence $t_n\to\infty$ (every decreasing positive shadow has a convex tail). "Natural" sum rules (positive resolvents, §2.1) **necessarily** have negative weight in the tail.

*Proof.* (a) is Lemma 173.0 plus: $\varphi_r$ affine and $\to0$ $\Rightarrow$ $\varphi_r\equiv0$.
(b) $w_\Phi\ge0\Rightarrow\varphi_r''\le0$: concave. If $\varphi_r'(t_1)<0$ for some $t_1$, concavity gives $\varphi_r'\le\varphi_r'(t_1)<0$ on $[t_1,\infty)$ and $\varphi_r\to-\infty$, contradicting $\varphi_r\to0$. So $\varphi_r'\ge0$ everywhere and decreasing; its limit is $0$ (if it were $>0$, $\varphi_r\to\infty$). Then $\varphi_r$ is increasing with limit $0$, hence $\varphi_r\le0$; and $\int_0^\infty w_\Phi=-2\int_0^\infty\varphi_r''=2(\varphi_r'(0)-\lim\varphi_r')=2\varphi_r'(0)$.
(c) $\int_0^X t\,w_\Phi=-2\int_0^X t\varphi_r''=-2X\varphi_r'(X)+2(\varphi_r(X)-\varphi_r(0))$. Since $\varphi_r'\ge0$ decreases and $\int\varphi_r'=\varphi_r(\infty)-\varphi_r(0)$ converges, $X\varphi_r'(X)\le2\int_{X/2}^X\varphi_r'\to0$. What remains is $-2\varphi_r(0)$.
(d) $\varphi_r\ge0$, $\to0$, $\not\equiv0$: if $w_\Phi\ge0$ from some $T_0$ on, by localized (b) $\varphi_r\le0$ on $[T_0,\infty)$, hence $\varphi_r\equiv0$ there; analytic continuation of $\Phi$ (its real part on the line is real-analytic since $\Phi$ is holomorphic in a neighborhood) forces $\varphi_r\equiv0$. Contradiction. $\square$

**[COROLLARY 173.A.1] (unconditional blindness of class $X$).** If $w_\Phi\ge0$ is admissible (hence integrable and, say, piecewise decreasing), then by partial summation against Selberg's certificate $E(T)\ll T/\log T$:
$$\sum_j b_j^2\,w_\Phi(\gamma_j)\;\ll\;\int_1^\infty w_\Phi(t)\,d\Big(\frac{t}{\log t}\Big)\;<\;\infty\qquad\textbf{unconditionally}.$$
Every weighted energy representable in $X$ is finite whether or not RH holds: within class $X$, the question "is $I_w<\infty$?" **has no content**; only the exact value does. Representing $I$ (weight 1) as a membership question requires leaving $X$. *(It is the same frontier as ceiling 172.9, seen without windows: there the limit was ordinate noise in the shadow; here it is the forced integrability of the weight.)*

**[LEMMA 173.B] (Stieltjes rigidity: de-weighting by superposing real probes dies).** Let $m\in C^1(0,\infty)$ with $m(a)\to0$ ($a\to\infty$), $\int_0^\infty(1+a)\,|m'(a)|\,da<\infty$. If the superposition of resolvents on the real axis $\Phi_m:=\int_0^\infty \tilde\Phi_a\,m(a)\,da$ (where $\tilde\Phi_a(s)=\tfrac12[(\tfrac12+a-s)^{-2}+(s+a-\tfrac12)^{-2}]$, with shadow $\varphi_{r,a}(t)=(a^2-t^2)/(a^2+t^2)^2$) **cancels the shadow**, i.e.
$$\int_0^\infty m(a)\,\frac{a^2-t^2}{(a^2+t^2)^2}\,da\;=\;0\qquad\forall\,t>0,$$
then $m\equiv0$.

*Proof.* $\frac{a^2-t^2}{(a^2+t^2)^2}=-\partial_a\frac{a}{a^2+t^2}$. Integrating by parts (boundaries vanish: at $a=0$ by the factor $a$, at $\infty$ by the decay of $m$): $\int_0^\infty m'(a)\frac{a}{a^2+t^2}\,da=0$ for every $t>0$. With $u=a^2$, $g(u):=\tfrac12 m'(\sqrt u)$: $\int_0^\infty\frac{g(u)}{u+t^2}\,du=0$ for every $t^2>0$. The Stieltjes transform of $g\,du$ (defined by the integrability hypothesis) vanishes on $(0,\infty)$, hence on $\mathbb C\setminus(-\infty,0]$ by continuation, hence $g\,du=0$ by Perron–Stieltjes inversion (Widder, *The Laplace Transform*, ch. VIII). Thus $m'\equiv0$, $m$ constant, and decay gives $m\equiv0$. $\square$

**Exact illustration of rigidity (the $J=0$ computation).** The only "superposition" cancelling the shadow without decaying is $m\equiv$ const (Lebesgue, excluded from the lemma for not decaying): indeed $\int_0^\infty\frac{a^2-t^2}{(a^2+t^2)^2}\,da=\big[-\tfrac{a}{a^2+t^2}\big]_0^\infty=0$. But Lebesgue **also cancels the signal**: the second-order weight of the family is $\propto\frac{(a^2-\gamma^2)^2-4a^2\gamma^2}{(a^2+\gamma^2)^4}$ and, with $a=\gamma x$ and the beta integrals $\int_0^\infty\frac{x^4\,dx}{(1+x^2)^4}=\int_0^\infty\frac{x^2\,dx}{(1+x^2)^4}=\frac{\pi}{32}$, $\int_0^\infty\frac{dx}{(1+x^2)^4}=\frac{5\pi}{32}$:
$$\int_0^\infty\frac{x^4-6x^2+1}{(1+x^2)^4}\,dx\;=\;\frac{\pi}{32}-\frac{6\pi}{32}+\frac{5\pi}{32}\;=\;0 .$$
(Structural reason: $\int_0^\infty(a-i\gamma)^{-2k}\,da=\frac{(-1)^k\,i^{\,1}\,\gamma^{1-2k}}{2k-1}\cdot(-1)$ is **purely imaginary** for every $k\ge1$, so its real part — shadow and signal alike — vanishes.) Verdict: in the family of probes on the real axis, *shadow and signal die together or live together*; there is no de-weighting by superposition. Moving the probes to the critical line = windows = ceiling 172.9 (not retried).

---

## 4. The de-weighting program: where it crosses and where it dies

### 4.1. Li coefficients: the maximal de-weighting within $X$

$\lambda_n=\sum_\rho[1-(1-1/\rho)^n]$ (Li 1997, *J. Number Theory* 65; Bombieri–Lagarias 1999, *J. Number Theory* 77: RH $\iff\lambda_n\ge0\ \forall n$; the $\lambda_n$ are arithmetic via Stieltjes constants — Bombieri–Lagarias, and the Voros/Coffey asymptotics [literature GAP: exact reference of Voros, *c.* 2004, "Sharpenings of Li's criterion"]).

**Exact quadruple algebra.** $z:=1-1/\rho$ sends the critical line to the unit circle and the quadruple to $\{z,\bar z,1/z,1/\bar z\}$ (direct computation: $z(\bar\rho)=\bar z$, $z(1-\bar\rho)=1/\bar z$). With $z=e^{-u+i\theta}$:
$$\Sigma_{\mathrm{quad}}\big[1-(1-1/\rho)^n\big]\;=\;4-4\cosh(nu)\cos(n\theta)\qquad\text{(exact, real)},$$
and under $b\mapsto-b$ (which permutes the quadruple): $u\mapsto-u$, $\theta\mapsto\theta$ — even in $b$, as it must be. Exact data: $|z|^2=1-\frac{2b}{(\frac12+b)^2+\gamma^2}$, hence $u=\frac{b}{\frac14+\gamma^2}+O(b^2/\gamma^2)$ (odd in $b$), and $\theta=\theta_\gamma+O(b^2)$ with $\theta_\gamma=\pi-2\arctan(2\gamma)\sim1/\gamma$. Expansion:
$$\Sigma_{\mathrm{quad}}\;=\;\underbrace{\big[4-4\cos(n\theta_\gamma)\big]}_{\text{shadow}}\;\underbrace{-\;2\,n^2u_1^2\cos(n\theta_\gamma)\,b^2\;+\;O(nb^2)}_{\text{signal}},\qquad u_1=\frac1{\frac14+\gamma^2}.$$
**The de-weighting that IS achieved:** the signal's weight is $\asymp n^2\cos(n/\gamma)/\gamma^4$. Averaging $\sum_n c_n\lambda_n$ with $c_n=g(n/N)$, the cosine localizes $\gamma\asymp N$ and the effective weight mass at $\gamma\sim N$ scales as $N^3/\gamma^4\sim1/\gamma$: the Li family **tilts** the weight from $1/\gamma^4$ to (nearly) $1/\gamma$ dyadically.

**Where it dies:** exactly at the frontier of Theorem 173.A. The superposition remains within $X$ ($\Phi(s)=\sum_nc_n[1-(1-1/s)^n]$), its shadow is $\sum_nc_n[4-4\cos(n\theta_\gamma)]$ — massively non-zero at $\gamma\lesssim N$ — and the mass-height law (173.A.c) prices the crossing: weight $\sim1$ up to height $T$ requires shadow depth $\sim T^2$, whose value at the true ordinates is exactly the non-arithmetic information. The reachable limiting weight is the integrable frontier; note that **even weight $1/\gamma$ would fall short and is simultaneously unreachable**: with $E(T)\ll T/\log T$, $\sum b^2/\gamma\ll\log\log T$ — it barely diverges; the entire gap between "representable in $X$" and $I$ is logarithmic. (Same house constant: the $T/\log T$ ceiling.)

### 4.2. Verdict on de-weighting

[THEOREM 173.A] + [LEMMA 173.B] + 4.1: within the holomorphic class the de-weighting moves along the frontier $\{\,w\ge0,\ \int w<\infty\,\}$ and **does not cross it**; the structural reason is the weld signal = shadow curvature, not the choice of windows (a new face of ceiling 172.9). Crossing requires non-holomorphic probes — §6.

---

## 5. Cramér and the impurity window: second order in Laplace coordinates

### 5.1. The Cramér function: exact factorization of the quadruple

$V(t):=\sum_{\mathrm{Im}\,\rho>0}e^{i\rho t}$ ($t>0$), studied by Cramér ("Studien über die Nullstellen der Riemannschen Zetafunktion", *Math. Z.* 4 (1919), 104–130): $V$ continues meromorphically with logarithmic singularities at $t=m\log p$ (the primes enter as singularities) and a principal singularity at $t=0$. [Literature GAP: the exact constants of the singularity at $0$ are not cited here from memory; they are not used.]

**[PROP 173.Cr] (the energy is the $t^2$ coefficient of Cramér).** For $t>0$, grouping by quadruples/pairs (the zeros with $\mathrm{Im}\,\rho>0$ of a quadruple are $\tfrac12\pm b+i\gamma$):
$$e^{-it/2}\,V(t)\;=\;\sum_{\text{pairs}}e^{-\gamma t}\;+\;\sum_{\text{quad.}}2\,e^{-\gamma_j t}\cos(b_j t)
\;=\;C(t)\;-\;t^2\,I_L(t)\;+\;O\big(t^4{\textstyle\sum}b^4e^{-\gamma t}\big),$$
where $C(t):=\sum_{\mathrm{Im}\rho>0}e^{-\gamma_\rho t}$ (the Laplace shadow) and $I_L(t):=\sum_j b_j^2e^{-\gamma_jt}$, with $I(0^+)=\lim_{t\to0^+}I_L(t)$ (monotone). In particular $e^{-it/2}V(t)$ is **real** for $t>0$.

*Proof.* $e^{i(\frac12\pm b+i\gamma)t}=e^{it/2}e^{-\gamma t}e^{\pm ibt}$; sum and use $2\cos(bt)=2-b^2t^2+2\cdot\frac{(bt)^4}{4!}\cos(\xi)$. $\square$

**Honest reading.** Cramér's probe is in class $X$ (family $\varphi_t(\gamma)=e^{-\gamma t}$): its weight is $w_t(\gamma)=-2\,\partial_\gamma^2$-curvature $=-2t^2e^{-\gamma t}$, of total mass $|\int w_t|=2t\to0$ — the limit $t\to0^+$ illustrates the mass law (173.A.b) in action: the Laplace window loses all of its weight mass exactly when trying to capture $I(0^+)$. And the $t^2$ coefficient of $V$ is contaminated by the $t^2$ coefficient of the shadow's fluctuation $C(t)$ (the true ordinates), of the same size: the weld again. **Closed computation requested by the director: yes, Cramér's singularity at $t=0$ carries $I$ in its second-order coefficient ($-t^2I_L(t)$, Prop. 173.Cr), and no, it is not extractable within $X$ (Theorem 173.A applied to $\varphi_t$).**

### 5.2. Quadratic functionals: the obstruction goes up an order

**[PROP 173.D] (class $X_2$).** Let $\mathcal H$ be a Hilbert space, $s\mapsto f_s\in\mathcal H$ weakly holomorphic in the strip with the quadruple symmetry in each variable of the kernel $K(s,s'):=\langle f_s,f_{s'}\rangle$, and $F:=\sum_\rho f_\rho-A$ with $A$ (centered) fixed. Then, in the simultaneous expansion of all quadruples:
$$\|F\|^2\;=\;\|F_0\|^2\;+\;2\sum_j b_j^2\,\mathrm{Re}\big\langle F_0,\;\partial_s^2f\big|_{\frac12+i\gamma_j}\big\rangle\;+\;O\Big(\big({\textstyle\sum}b^2\big)^2\sup\|\partial^2f\|^2\Big),$$
where $F_0=\sum_j(\text{shadow})-A$ is the **shadow fluctuation**. No term $\sum b_j^2\,(\text{autonomous weight}\ge0)$ appears: the term linear in the displacements vanishes (quadruple parity, as in 173.0), the coefficient of $b^2$ is **multiplicatively coupled to $F_0$**, and the first autonomous term in the $b$'s is $O\big((\sum b^2)^2\big)$ — of type $\sum b^4$ and cross terms.

*Proof.* $f(\tfrac12+b+i\gamma)+f(\tfrac12-b+i\gamma)=2f(\tfrac12+i\gamma)+b^2f''(\tfrac12+i\gamma)+O(b^4)$ (even in $b$, as in 173.0, now with values in $\mathcal H$; the conjugate partners of the quadruple are treated likewise). Then $F=F_0+\delta$, $\delta=\sum_jb_j^2\,f''_j+O(\sum b^4)$, and $\|F\|^2=\|F_0\|^2+2\mathrm{Re}\langle F_0,\delta\rangle+\|\delta\|^2$ with $\|\delta\|^2=O((\sum b^2)^2\cdot\sup\|f''\|^2)$. $\square$

**Consequences.** (1) The bias of the impurity spectrum (D152: bias $\sim-2\sqrt\pi\,m\,Te^{b^2T^2}$ at $\tau=\gamma$) squared produces $\sum b^4$-type, consistent with 173.D: quadratic norms of arithmetic objects capture $I_2=\sum b^4$ as an autonomous term, **not** $I$. (2) The director's candidate $I\overset{?}=\int_0^\infty|\mathcal E(x)|^2dx$ with $\mathcal E$ arithmetic falls into $X_2$ (kernels $K(\rho,\bar\rho')=\int x^{\rho+\bar\rho'}d\mu$, holomorphic per variable): obstructed in the same way. (3) **Structural diagnosis:** $I=\|F\|^2$ would require $F$ to be *linear* in the displacements $b_j$ — but every holomorphic functional of the zero multiset is even in each $b_j$ (quadruple symmetry). Breaking parity = selecting **half a quadruple** (only $\beta>\tfrac12$) = a non-holomorphic operation. That is exactly what $\log|\zeta|$ does via $N(\sigma,T)$. We enter.

---

## 6. The non-holomorphic way out: $I$ as a moment of the Riesz measure (Green–Littlewood)

### 6.1. The exact identity

**[THEOREM 173.C].** Let $T>0$ not be the ordinate of any zero. Then, unconditionally,
$$I(T)\;=\;\frac1\pi\int_{1/2}^{\infty}\!\!\int_0^T \log|\zeta(\sigma+it)|\,dt\,d\sigma\;+\;\frac18\;-\;\frac{1}{2\pi}\int_{1/2}^\infty\!\Big(\sigma-\tfrac12\Big)^2\,\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma,$$
with all integrals absolutely convergent. Moreover, for each $n$ there exists $T\in[n,n+1]$ ("good height", at distance $\gg1/\log n$ from every ordinate) with
$$\Big|\tfrac{1}{2\pi}\int_{1/2}^\infty(\sigma-\tfrac12)^2\,\mathrm{Im}\,\tfrac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma\Big|\;\ll\;\log^2T .$$

*Proof.* Let $u(s):=\log|\zeta(s)|$, $v(\sigma):=\tfrac12(\sigma-\tfrac12)^2$, and $R=R_{A,T}:=[\tfrac12,A]\times[-T,T]$ with $A>2$. **(1) Local structure of $u$.** By the partial-fraction decomposition of $\zeta'/\zeta$ (Davenport, ch. 15–16) and integration, in a neighborhood of $R$ one has $u(s)=\sum_{\rho\in\mathcal Z}\log|s-\rho|-\log|s-1|+h(s)$ with $\mathcal Z$ the (finite) set of zeros in a slightly larger rectangle and $h$ harmonic in that neighborhood (logarithm of a zero-free holomorphic function, locally single-valued). **(2) Green by pieces.** Green's identity $\iint_R(u\Delta v-v\Delta u)=\oint_{\partial R}(u\,\partial_nv-v\,\partial_nu)$ holds for $h$ and $v$ (classical, both smooth) and for each piece $\log|s-w|$ against smooth $v$ (classical potential computation: contributes the term $2\pi v(w)$ if $w\in R^\circ$; the zeros/pole on $\partial R$ are excluded by the hypothesis on $T$, and zeros with $\beta=\tfrac12$ fall on the edge $\sigma=\tfrac12$ where $v=v'=0$, contributing $2\pi v(\rho)=0$ — consistent). With $\Delta v=1$:
$$\iint_R u\;-\;2\pi\Big[\sum_{\rho\in R,\ \beta>1/2} v(\rho)\;-\;v(1)\Big]\;=\;\oint_{\partial R}\big(u\,\partial_nv-v\,\partial_nu\big).$$
**(3) Counting.** Each quadruple with $|\gamma|<T$ has exactly two members with $\beta>\tfrac12$ in $R$ ($\tfrac12+b\pm i\gamma$), each with $v=b^2/2$: $\sum v(\rho)=I(T)$. And $v(1)=\tfrac18$.
**(4) Boundaries.** (i) $\sigma=\tfrac12$: $v=0$ and $\partial_nv=-v'(\tfrac12)=0$: nothing. (ii) $\sigma=A\to\infty$: $|u|,|\partial_\sigma u|\ll2^{-\sigma}$ and $v\ll\sigma^2$: both pieces $\to0$ and $\iint_Ru$ converges absolutely (near $s=1$, $\log|s-1|$ is integrable). (iii) $t=\pm T$: $\partial_nv=\pm\partial_tv=0$; what remains is $-\oint v\,\partial_nu=-2\int_{1/2}^\infty v\,\partial_tu(\sigma,T)\,d\sigma$ using the symmetry $u(\sigma,-t)=u(\sigma,t)$ (from $\zeta(\bar s)=\overline{\zeta(s)}$), which also gives $\iint_Ru=2\iint_{0<t<T}u$.
**(5) Assembly.** $2\iint_{0<t<T}u-2\pi I(T)+\tfrac{2\pi}8=-2\int_{1/2}^\infty v\,\partial_tu(\sigma,T)\,d\sigma$, and $\partial_tu=\mathrm{Re}[i\zeta'/\zeta]=-\mathrm{Im}\,\zeta'/\zeta$. Solving for $I(T)$ gives the identity.
**(6) Flux bound.** For $\tfrac12\le\sigma\le2$: $\zeta'/\zeta(\sigma+iT)=\sum_{|\gamma-T|\le1}(\sigma+iT-\rho)^{-1}+O(\log T)$ (Davenport, ch. 15); there are $O(\log T)$ terms and at good heights each is $O(\log T)$: total $O(\log^2T)$. For $\sigma\ge2$: $|\zeta'/\zeta|\le\sum\Lambda(n)n^{-2}\cdot(n/2)^{-(\sigma-2)}\ll2^{-\sigma}$, and $\int_2^\infty\sigma^22^{-\sigma}d\sigma=O(1)$. $\square$

**Consistency check as $T\to0^+$** (control of the $\tfrac18$ term): $I(T)\to0$ and $\iint\to0$; the flux: near $s=1$, $\zeta'/\zeta\sim-1/(s-1)$, hence $\mathrm{Im}\,\zeta'/\zeta(\sigma+iT)=\frac{T}{(\sigma-1)^2+T^2}+O(1)\to\pi\delta_{\sigma=1}$, and the flux term $\to-\frac1{2\pi}\cdot(\tfrac12)^2\cdot\pi=-\tfrac18$, which exactly cancels the $+\tfrac18$. ✓ *(Independent cross-check: iterating the classical Littlewood lemma (Littlewood 1924; Titchmarsh, **The Theory of the Riemann Zeta-Function**, §9.9) at $\sigma_0\in[\tfrac12,1]$ via the layer-cake identity $\sum_jb_j^2=2\int_{1/2}^\infty\sum_j(\beta_j-\sigma_0)_+^{\phantom{1}}\,$…$\,d\sigma_0$, the term $+\tfrac18$ reappears as $\frac1\pi\int_{1/2}^1\pi(1-\sigma_0)\,d\sigma_0=\tfrac18$, coming from $\arg\zeta=\pi$ on $(\sigma_0,1)$ — the pole again. They match.)*

### 6.2. Structural reading: the three transversal moments

**[NEW-DEFINITION] (right Riesz measure).** $\mu^+:=\frac1{2\pi}\Delta\log|\zeta|\,\big|_{\{\sigma>1/2\}}+\delta_1$-corrected $=\sum_{\beta>1/2}\delta_\rho$: the (atomic, positive) measure of the zeros of the right half-plane. The transversal coordinate is $x(\rho):=\beta-\tfrac12=b$.

Then the Green family with $v_m=(\sigma-\tfrac12)_+^m$ gives exactly:
- $m=0$: densities $N(\sigma,T)$ — the entry point of density theorems;
- $m=1$: $\sum_{\gamma\le T}b_j=\frac1{2\pi}\int_0^T\log|\zeta(\tfrac12+it)|\,dt+O(\log T)$ — **classical Littlewood lemma** (Littlewood 1924; Titchmarsh §9.9): the first moment is the mass of $\log|\zeta|$ **on the line**;
- $m=2$: **[THEOREM 173.C]** — the second moment ($=I$) is the mass of $\log|\zeta|$ **over the half-strip**. The $m=2$ piece assembled as a representation of $I$ is this document's contribution; the ingredients are classical (it is the same machinery with which Selberg proves $E(T)\ll T/\log T$ — honesty of provenance).

**Why 173.C evades 173.A:** $\log|\zeta|=\mathrm{Re}\log\zeta$ is not holomorphic, and the restriction to $\sigma>\tfrac12$ selects half a quadruple — exactly the two operations class $X$ (and $X_2$, Prop. 173.D) forbid. The price changed shape: there is no longer a multiplicative weight in $\gamma$ (it is weight 1), there is (a) an **additive boundary flux** at the height of the cut, $O(\log^2T)$ at good heights, and (b) a **signed** integrand (not yet a norm).

**[COROLLARY 173.C.1] (RH as an exact integral equation).** RH $\iff$ for every good height $T$:
$$\int_{1/2}^\infty\!\!\int_0^T\log|\zeta(\sigma+it)|\,dt\,d\sigma\;=\;-\frac\pi8\;+\;\frac12\int_{1/2}^\infty(\sigma-\tfrac12)^2\,\mathrm{Im}\,\frac{\zeta'}{\zeta}(\sigma+iT)\,d\sigma .$$
($\Rightarrow$ by 173.C with $I\equiv0$; $\Leftarrow$ because $I(T)\ge0$ is non-decreasing and 173.C makes it vanish at every height.) The energy is the defect of this equation.

**"Prime field" form [BRIDGE].** Integrating by parts in $\sigma$ (boundaries vanish as in (4)):
$$\frac1\pi\iint u\;=\;\frac1{2\pi}\iint_{\sigma>1/2,\,0<t<T}(\sigma-\tfrac12)\;\mathrm{Re}\Big(-\frac{\zeta'}{\zeta}(\sigma+it)\Big)\,d\sigma\,dt\;+\;\text{(boundary at }\sigma=\tfrac12\text{)},$$
and $\mathrm{Re}(-\zeta'/\zeta)(\sigma+it)=\sum_n\Lambda(n)n^{-\sigma}\cos(t\log n)$ for $\sigma>1$: $I$ is the pairing of the **prime field** with the lever arm $(\sigma-\tfrac12)$ across the strip. For $\sigma>1$ the integral in $t$ is bounded ($\int_0^T\cos(t\log n)dt\ll1/\log n$): **all the mass of $I$ lives in $\tfrac12<\sigma\le1$**, the zone where the Dirichlet series does not converge. The status of the series in the strip is the same wall as always, now in Phase A coordinates; the logarithmic divergence at the boundary ($\int(\sigma-\tfrac12)\,d\sigma/(2\sigma-1)^2$ when normalizing second moments) once again reproduces the house constant $T/\log T$. [GAP: turning this form into an identity with the regularized series — not done here.]

### 6.3. Membership and the self-energy obstruction

**[NEW-DEFINITION].** Let $G(s,w)=\frac1{2\pi}\log\big|\frac{s-(1-\bar w)}{s-w}\big|$ be the Green function of the half-plane $\Omega=\{\sigma>\tfrac12\}$, and
$$\tilde d(s)\;:=\;2\pi\sum_{\beta_\rho>1/2} G(s,\rho)\qquad(s\in\Omega)$$
the **potential of the off zeros** (the pole $s=1$ no longer appears: it is subtracted by construction; the on-line zeros are on $\partial\Omega$ and do not contribute). $\tilde d\ge0$; $\tilde d\equiv0\iff$ RH; and $\tilde d=u_h-u-(\text{explicit pole term})$ where $u_h$ is the harmonic (Poisson) extension of $t\mapsto\log|\zeta(\tfrac12+it)|$ to $\Omega$ — that is, $\tilde d$ measures the **harmonicity defect** of $\log|\zeta|$ to the right of the line: a quantity of pure regularity.

**[PROP 173.E] (dichotomous membership).**
$$\mathrm{RH}\iff\tilde d\in\mathcal D(\Omega):=\{\text{Dirichlet space}\},\qquad\text{and}\qquad\|\nabla\tilde d\|_{L^2(\Omega)}^2\in\{0,\infty\}\ \text{always}.$$

*Proof.* If RH, $\tilde d\equiv0$. If there is an off zero $\rho_0$ (with $b_0>0$), then near $\rho_0$: $\tilde d(s)=-\log|s-\rho_0|+O(1)$ (the other summands of the Green series are harmonic and bounded near $\rho_0$: the series converges locally uniformly away from the atoms because $\sum G(s,\rho)\le C(s)\sum b_\rho/((\sigma_s-\dots)^2+(\gamma_s-\gamma_\rho)^2)$, summable by $E(T)\ll T/\log T$ and $b<\tfrac12$). Then $|\nabla\tilde d|\ge\frac{1}{|s-\rho_0|}-O(1)$ in a punctured disk, and $\int|\nabla\tilde d|^2\ge\int_0^{r_0}\frac{2\pi r\,dr}{r^2}(1-o(1))=\infty$. $\square$

**Reading and final obstruction of Phase A.** 173.E is literally the "$I<\infty$ as membership" form requested by the mandate — but **degenerate**: the Dirichlet norm does not grade $I$, it jumps from $0$ to $\infty$ with the first atom. (Curious echo of the LP-112 dichotomy $\Rightarrow I\in\{0,\infty\}$ of Doc 175: here the dichotomy is **unconditional** but lives in the norm, not in $I$.) The reason $I\ne\|F\|^2$ in this class is precisely identified:

> **Atomicity obstruction.** $I=\int_\Omega(\sigma-\tfrac12)^2\,d\mu^+$ is a **linear** moment of the zero measure (Theorem 173.C); every natural **quadratic** energy of that measure ($\|\nabla\tilde d\|^2=4\pi^2\sum_{\rho,\rho'}G(\rho,\rho')$) includes the self-energies $G(\rho,\rho)=\infty$ of the point charges. Linear-in-measure vs. quadratic-in-field: that is the exact defect separating the achieved representation from the requested norm.

**Desingularization program [BRIDGE toward Phase 54].** The natural smoothing of the atoms comes from the DBN flow itself (scale $\sqrt t$): the per-atom renormalized energy is $2\pi\log(2b_j/\varepsilon)+O(1)$ when smoothed at scale $\varepsilon$; with $\varepsilon\sim\sqrt t$ this connects the regularized Dirichlet norm with $\sum_j\log(b_j/\sqrt t)$ — a first concrete candidate for a "grading norm" compatible with the balance law $\dot I=-2\kappa-D$. Not developed here; it is named as the next step of Phase A.

---

## 7. de Branges / Hermite–Biehler: where $I$ lives and where it does not

Framework: $E(z):=\xi(\tfrac12-iz)$ is entire; its zeros are $z=\pm\gamma_j+ib_j$ and $\pm\gamma_j-ib_j$ (on line: $\pm\gamma_j$ real). RH $\iff E$ has all its zeros real (limiting case of the Hermite–Biehler class; de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall 1968; for the dictionary with $\zeta$: Lagarias, "Hilbert spaces of entire functions and Dirichlet L-functions", in *Frontiers in Number Theory, Physics, and Geometry I*, Springer 2006 — [literature GAP: dictionary details cited from memory; the computations below are self-contained]).

**(a) The natural HB defect is of FIRST order in $b$.** The offending zeros (upper half-plane) are $\pm\gamma_j+ib_j$. The Blaschke mass at the point $z=i$ (corresponding to $s=\tfrac32$), exact per quadruple:
$$\mathfrak B\;:=\;-\log\Big|\prod_j\frac{(i-z_j)}{(i-\bar z_j)}\Big|\;=\;\sum_j\log\frac{\gamma_j^2+(1+b_j)^2}{\gamma_j^2+(1-b_j)^2}\;=\;\sum_j\frac{4b_j}{1+\gamma_j^2}\,\big(1+O(b_j^2)\big).$$
First order in $b$, Poisson weight $1/(1+\gamma^2)$. The Blaschke condition is the natural membership condition of the theory — and it is **linear in $b$**, not quadratic.

**(b) $I$ is NOT a natural de Branges defect: the Cauchy variance computation.** The phase measure of $E$ sees an on-line zero as $\delta_\gamma$ and an off quadruple as the pair of Cauchy densities $\frac1\pi\frac{b}{(t\mp\gamma)^2+b^2}\,dt$. The second moment of Cauchy is **infinite**; truncated:
$$\int_{|t-\gamma|\le1}(t-\gamma)^2\,\frac{b/\pi}{(t-\gamma)^2+b^2}\,dt\;=\;\frac2\pi\,b\,\Big(1-b\arctan\frac1b\Big)\;=\;\frac{2b}\pi+O(b^2),$$
again **linear** in $b$. HB/dB theory measures phase blurriness at first moment; $b^2$ is not its currency. Honest verdict: de Branges is the natural home of $J:=\sum b_j$ (and of $\mathfrak B$), not of $I$.

**(c) But $J$ controls $I$ and $J$ already has a representation (it is the $m=1$ of §6.2).** Since $b_j<\tfrac12$: $I(T)\le\tfrac12 J(T)$, and $J(T)=\frac1{2\pi}\int_0^T\log|\zeta(\tfrac12+it)|\,dt+O(\log T)$ (Littlewood). **Proposed pivot (recorded, not executed):** if Phase A accepts the first-order energy $J$ as an intermediate target — also equivalent to RH ($J=0\iff$RH) and an upper bound of $2I$ — then the Branges/HB home and Littlewood's representation on the line (a single integral, not double) are available right away, with the Blaschke mass $\mathfrak B$ as its exact weighted version.

---

## 8. The hard deliverable: final balance

**(i) Representation achieved.** [THEOREM 173.C]: $I(T)$ = explicit arithmetic-analytic functional of $\log|\zeta|$ on the right half-strip, **weight 1 in $\gamma$**, unconditional, exact. What remains as residue, declared: (1) the cut at $T$ with boundary flux $O(\log^2T)$ at good heights (local to the height of the cut, averageable); (2) the exact constant $\tfrac18$ (the pole); (3) the signed integrand: $I$ remains a **linear moment of a positive measure** ($I=\int(\sigma-\tfrac12)^2d\mu^+$), not yet $\|F\|^2$.

**(ii) Obstruction theorem.** [THEOREM 173.A] (+ [LEMMA 173.B], [PROP 173.D]): every self-contained representation of the holomorphic class $X$ (the one reaching the explicit formula) has weight $w=-2\varphi_r''$ welded to the shadow; if $w\ge0$ then $\int w<\infty$ and $\int t\,w\,dt=2|\varphi_r(0)|$ — necessarily decaying (integrable) weight, with a quantitative shadow-height cost law. The structural reason for ceiling 172.9 reappears without windows: **holomorphy of the probe + quadruple parity**. The quadratic class $X_2$ inherits the obstruction and its autonomous term is $\sum b^4$, not $\sum b^2$.

**(iii) The exact frontier between (i) and (ii).** The pair of operations separating success from the wall: *taking the real part* ($\log|\zeta|$) and *selecting half a quadruple* ($\sigma>\tfrac12$) — both non-holomorphic. The price of crossing: the multiplicative weight disappears and reappears as an additive boundary flux + a signed integrand. The residual obstruction toward $I=\|F\|^2$ is **atomic self-energy** ([PROP 173.E]): $I$ is linear in the zero measure; norms are quadratic in the field and diverge at the atoms.

**Next named steps (Phase A, continuation).**
1. **DBN desingularization of 173.E:** Dirichlet energy of $\tilde d$ smoothed at the flow's $\sqrt t$ scale; compute its renormalization ($\sum\log(b_j/\sqrt t)$-type) and confront it with $\dot I=-2\kappa-D$.
2. **Averaging the boundary flux of 173.C in $T$** (Cesàro at the cut) to lower $O(\log^2T)\to O(\log T)$ and isolate the average arithmetic part of the flux.
3. **The pivot $J=\sum b_j$** (§7c): decide whether Phase A accepts the first-order energy as an intermediate target; if so, the Littlewood + Blaschke package ($\mathfrak B$) is ready.
4. **Regularize the "prime field" form** (§6.2): give a summable meaning to $\iint(\sigma-\tfrac12)\sum\Lambda(n)n^{-\sigma}\cos(t\log n)$ on $\tfrac12<\sigma\le1$ (Abel/Cesàro in $n$) and measure what part of the flux it absorbs.

---

## References

- J. Hadamard, *Étude sur les propriétés des fonctions entières et en particulier d'une fonction considérée par Riemann*, J. Math. Pures Appl. (1893). [Hadamard product of $\xi$.]
- H. Davenport, *Multiplicative Number Theory*, 3rd ed., GTM 74, Springer. Chs. 12 (sums $\sum1/\rho$, constants), 15–16 (partial fractions of $\zeta'/\zeta$, bounds in strips).
- H. Cramér, "Studien über die Nullstellen der Riemannschen Zetafunktion", *Math. Z.* 4 (1919), 104–130.
- J. E. Littlewood, "On the zeros of the Riemann zeta-function", *Proc. Cambridge Philos. Soc.* 22 (1924), 295–318. [Littlewood's lemma.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (Heath-Brown), Oxford. §9.9 (Littlewood's lemma), ch. 9 (densities).
- A. Selberg, "Contributions to the theory of the Riemann zeta-function", *Arch. Math. Naturvid.* 48 (1946). [Origin of the certificate $E(T)\ll T/\log T$.]
- X.-J. Li, "The positivity of a sequence of numbers and the Riemann hypothesis", *J. Number Theory* 65 (1997), 325–333.
- E. Bombieri, J. C. Lagarias, "Complements to Li's criterion for the Riemann hypothesis", *J. Number Theory* 77 (1999), 274–287.
- L. de Branges, *Hilbert Spaces of Entire Functions*, Prentice-Hall, 1968.
- J. C. Lagarias, "Hilbert spaces of entire functions and Dirichlet L-functions", in *Frontiers in Number Theory, Physics, and Geometry I*, Springer, 2006. [Literature GAP: used only as context.]
- D. V. Widder, *The Laplace Transform*, Princeton, 1941. Ch. VIII (inversion/uniqueness of the Stieltjes transform).
- A. Voros, "Sharpenings of Li's criterion for the Riemann hypothesis", *Math. Phys. Anal. Geom.* (c. 2004). [Literature GAP: exact reference not verified; not used in any proof.]

**Internal documents:** Doc 152 (impurity spectrum $S_T(\tau)$), Doc 170 (coordinates), Doc 172 (ceiling $T/\log T$, Theorem 172.9), Doc 175 (LP-112 dichotomy), Phase 54 (balance law $\dot I=-2\kappa-D$).
