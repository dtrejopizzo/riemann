# R167_101 — A1: the exact quantitative target for (WS)

Phase 167, round 1, task A1. Pure mathematics, no numerics. The only arithmetic is hand arithmetic on
closed formulas. Inputs: R167_000, R166_802 (Thm 1–3, Prop 2.1), R164_601 (Props 1.1–1.3, 2.1, Thm 3.3), R165_101 (Det+),
R165_102 (Det−), R163_401 (Lemmas 3.1–3.4, Lemma 4.10, §4.2, §4.8), R164_501 (Prop 4). No other file was edited, and no
label of record moves.

Labels: PROVED / PROVED-CITED / ARGUED / OPEN.

**Corpus check (rule ).** The quartet/test bookkeeping repeats R166_802 §1 and R164_601 §2–3. New in this memo:
- C1: the corrected weight;
- Thm B: the exclusion criterion becomes an *upper* bound once the on-line sum is bounded above;
- Prop W: the window obstruction;
- Thm C: the amplification ceiling $Y^\delta/\delta$;
- Cor D: $X^{\delta}$ is bounded at the witness;
- §5: the regime map.

---

## 0. Outcome and status table

**Outcome in five lines.**
1. The quantity that (WS) must bound is the twisted sum over the **whole** range $1\le n\le Y:=Xe^{\Delta}$. The tail alone is not enough (Prop W).
2. The bound has to be one-sided ($\mathrm{Re}$), at **one** scale, with the boxed constant $B$ of §4.
3. The exponent condition $\eta<\delta$ appears exactly through the Poisson majorant $|\Phi(-i\delta)|\le Y^{\delta}I/(\pi\delta)$ (Thm C). The finite range never weakens it: every finite-range factor is $\le1$.
4. At a first-contact witness, $X^{\delta}$ is **not** a large power (Cor D). It is at most $(1.57\,\gamma_q/2\pi)^{\delta}$ (Det+), and in the lattice model it is $\asymp\max(e^{\delta L},\delta L T)$. So (WS) is an RH-quality bound (polylogarithmic in $\gamma_q$) on one twisted prime sum at frequency $\gamma_q\asymp X$. Known methods without zeros give only a subpolynomial saving over $X^{1/2}$.
5. $B>0$ at all requires the Det− regime, $Y^{\delta}\gtrsim\delta\,C_S L(2T+\Delta)$ (Prop E). Outside it, no bound on $\Lambda$-sums of any strength excludes the witness through this test. The obstruction there is the on-line count.

| # | Statement | Label |
|---|---|---|
| C1 | Correction to R166_802 Prop 2.1 / R167_000 §1: $w=(e^{-i\gamma_q\cdot}g)*\check k$, $\widehat w(s)=G(s+\gamma_q)^2k(s)\ge0$; it is not $(G^2)^\vee*\check k$ | PROVED |
| Thm A | Exact witness identity $4\,\mathrm{Re}\,\mathcal S_{\rm full}=\tfrac L\pi I-Q_K-R_K-O_K+\mathfrak p_K+\varepsilon_K$ | PROVED (explicit formula PROVED-CITED) |
| Lem Q | $Q_K=-4c_\Theta\lvert G(t_q)\rvert^2\lvert k(-i\delta_q)\rvert+O(\gamma_q^{-N})$; the phase can be rotated so that $c_\Theta\ge1/\sqrt2$ uniformly in the cone; exact cost | PROVED |
| Lem O | $O_K\le\tfrac L\pi I+2C_S(\gamma_q)(2T+\Delta)\lVert G\rVert_\infty^2\lVert k\rVert_1+\varepsilon'_K$ (via $S(t)$) | PROVED-CITED (Trudgian bound on $S$) + PROVED |
| Thm B | Under (Dom$_\theta$): witness $\Rightarrow 4\,\mathrm{Re}\,\mathcal S_{\rm full}\ge4B$; so the one-sided bound $\mathrm{Re}\,\mathcal S_{\rm full}<B$ excludes the witness. Refines R166_802 Thm 1(b) | PROVED given (Dom$_\theta$); (Dom$_\theta$) OPEN |
| Thm C | Amplification ceiling: $\lvert G(t_q)\rvert^2\lvert k(-i\delta)\rvert\le Y^{\delta}I/(\pi\delta)$, hence $B\le 2c_\Theta Y^\delta w(0)/\delta$; $\eta<\delta$ is forced | PROVED (Poisson majorant PROVED-CITED) |
| Prop W | A tail-only (WS) works only if $Y^\delta>1.04\,\delta X^{1/2}$, i.e. $\Delta>[(1-2\delta)T+\log(1.04\delta)]/\delta$ | PROVED (Rosser–Schoenfeld CITED) |
| Prop E | $B>0$ needs $(1-\theta)\tfrac{8c_\Theta}{\delta}Y^{\delta}w(0)>E_K$, which forces a Det−-type regime | PROVED (necessity, given the $S(t)$ input) |
| Cor D | At the witness, $X^{\delta_q}\le(1.57\gamma_q/2\pi)^{\delta_q}$; lattice model: $X^{\delta}\approx 2\delta L$ in the large-$y$ regime and $\le e^{y_0}\cdot1.25\approx11$ in the small-$y$ regime | PROVED-CITED (R165_101) / PROVED in model (Lemma 4.10) |
| §5.3 | Sanity: dlVP shape recovered from the trivial bound; Det− threshold recovered as $B>0$; lattice-model value of $B$ | PROVED (shape), constants ARGUED |
| §6 | Weight data for A2: support, size, smoothness, Bernstein, positivity of $\widehat w$ | PROVED |
| O167.101.1 | (Dom$_\theta$): other quartets near $\gamma_q$ outside their cones carry $\le\theta\lvert Q_K\rvert$ | OPEN (same as R165_102 (Dom)) |
| O167.101.2 | Small-$y$ regime: needs an on-line count sharper than $S(t)=O(\log t)$, not a $\Lambda$-bound | OPEN (= R165_102 small-$y$ row) |

---

## 1. Setting and normalisation

**Witness data.**
- $F$ is the witness of type $T=T_c$, with $G=\widehat F$ (or $-i\widehat F$) real-rooted, of type $T$, real on $\mathbb R$, of parity $(-1)^m$.
- $X=e^{2T}$. The lowest quartet sits at $t_q=\gamma_q-i\delta_q$, with $0<\delta_q<\tfrac12$ and $\gamma_q>3\cdot10^{12}$, inside its light cone (R163_401 Lemma 3.4): $\cos2\Theta_q<0$, where $G(t_q)^2=\lvert G(t_q)\rvert^2e^{2i\Theta_q}$ (Lemma 3.3).
- Write $\gamma=\gamma_q$, $\delta=\delta_q$, and $L=\log(\gamma/2\pi)$.

**Explicit formula (PROVED-CITED; Weil/Guinand, e.g. Iwaniec–Kowalski Thm 5.12).** Let $\Psi$ be even, real on $\mathbb R$, holomorphic in $\lvert\mathrm{Im}\,z\rvert<\tfrac12+\epsilon$, with enough decay. Put $\check\Psi(u)=\frac1{2\pi}\int\Psi(t)e^{iut}dt$ and $\Omega(t)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{it}2)-\log\pi$. Then
$$\sum_\rho\Psi(t_\rho)=2\Psi(\tfrac i2)+\frac1{2\pi}\int\Psi\,\Omega\,dt-2\sum_{n\ge1}\Lambda(n)n^{-1/2}\check\Psi(\log n).\tag{1.1}$$
A quartet contributes $4\,\mathrm{Re}\,\Psi(t_q)$. R167_000 writes "$2\mathrm{Re}$" per pair; here the full quartet is used.

**The test.**
- $h(z)=\frac1{2\pi}\int_{-\Delta/2}^{\Delta/2}\widehat h(u)e^{iuz}du$ with $\widehat h=A+iB$, $A$ even real, $B$ odd real. Then $h$ is real on $\mathbb R$, of type $\Delta/2$.
- $k:=h^2\ge0$ on $\mathbb R$, of type $\Delta$.
- $K(t):=k(t-\gamma)+k(-t-\gamma)$ is even, $\ge0$ on $\mathbb R$, and localised at $\pm\gamma$.
- $\Psi:=G^2K$ is of type $2T+\Delta$.
- $\widehat h\in C_c^\infty$ is taken when moments are needed (§6).
- The case $B=0$, $A\ge0$ is the "natural" localised test, the same as R164_601 Prop 2.1 up to the low-height Poisson term, which is not needed here (§2.4).

**C1 (correction, PROVED).** Put $g=(G^2)^\vee$, supported in $[-2T,2T]$. Define
$$w(u):=\frac1{2\pi}\int_{\mathbb R}G(s+\gamma)^2k(s)\,e^{ius}\,ds=\big((e^{-i\gamma\cdot}g)*\check k\big)(u).$$
Then $\check\Psi(u)=2\,\mathrm{Re}\,[e^{i\gamma u}w(u)]$, and
$$2\sum_n\Lambda(n)n^{-1/2}\check\Psi(\log n)=4\,\mathrm{Re}\,\mathcal S_{\rm full},\qquad \mathcal S_{\rm full}:=\sum_{1\le n\le Y}\Lambda(n)n^{-1/2+i\gamma}w(\log n),\quad Y:=Xe^{\Delta}.$$

*Proof.* Substitute $t=s+\gamma$ in $\int G^2(t)k(t-\gamma)e^{iut}dt$. Substitute $t=-s-\gamma$ in the second bump, and use evenness of $G^2$ and reality of $G^2k$ on $\mathbb R$, which gives $w(-u)=\overline{w(u)}$. The support of $w$ is $\subset[-2T-\Delta,2T+\Delta]$ by the supports of $g$ and $\check k$. ∎

R166_802 Prop 2.1 writes $w_K=(G^2)^\vee*\check k$. That drops the demodulation $e^{-i\gamma v}$ on $g$. The correct transform is $\widehat w=G(\cdot+\gamma)^2k\ge0$, the *shifted* product. The positivity that R167_000 relies on survives. The Tail statement of R166_802 holds verbatim with the corrected $w$.

Fix the notation
$$\Phi(s):=G(s+\gamma)^2k(s)\quad(\ge0\text{ on }\mathbb R,\ \text{type }2T+\Delta),\qquad I:=\int\Phi=2\pi\,w(0),\qquad \lvert w(u)\rvert\le w(0).$$

---

## 2. The terms of the identity

### 2.1 Thm A (exact witness identity). PROVED

$$4\,\mathrm{Re}\,\mathcal S_{\rm full}=\underbrace{\tfrac{L}{\pi}I+\varepsilon_K}_{\rm arch}\;+\;\underbrace{\mathfrak p_K}_{\rm polar}\;-\;Q_K-R_K-O_K,\tag{2.1}$$

The terms are:
- $Q_K=4\,\mathrm{Re}\,\Psi(t_q)$;
- $R_K$ is the sum over the other quartets;
- $O_K=\sum_{\gamma'\ \text{on-line}}\Psi(\gamma')\ge0$;
- $\mathfrak p_K=2G(\tfrac i2)^2K(\tfrac i2)$;
- $\lvert\varepsilon_K\rvert\le C\,\lVert G\rVert_\infty^2\int(1+\lvert s\rvert)k(s)ds/\gamma$ ($C$ absolute; Stirling: $\Omega(t)=\log(\lvert t\rvert/2\pi)+O(t^{-2})$ and $\log\frac{\gamma+s}{2\pi}=L+O(\lvert s\rvert/\gamma)$).

The polar term is negligible: $\lvert\mathfrak p_K\rvert\le2e^{T}\lVert G\rVert_\infty^2\sup_{\lvert y\rvert=1/2}\lvert k(-\gamma+iy)\rvert\ll_N e^{T+\Delta/2}\lVert G\rVert_\infty^2(\gamma\Delta)^{-N}$, using Phragmén–Lindelöf for $G$ and $\widehat h\in C^N_c$.

*Proof.* Insert C1 into (1.1) and split the zero sum. ∎

### 2.2 Lemma Q (the quartet term). PROVED

- $K(t_q)=k(-i\delta)+k(-2\gamma+i\delta)$, and the second term is $O_N((\gamma\Delta)^{-N}e^{\delta\Delta})$.
- $k(-i\delta)=h(-i\delta)^2=(a+ib)^2/4\pi^2$, with $a=\int A(u)\cosh\delta u\,du$ and $b=\int B(u)\sinh\delta u\,du$.
- Put $\vartheta=\arg(a+ib)$. Then
$$Q_K=-4\,c_\Theta\,\lvert G(t_q)\rvert^2\lvert k(-i\delta)\rvert+O(\gamma^{-N}),\qquad c_\Theta:=-\cos(2\Theta_q+2\vartheta).$$

**(i) What is known about the phase.** Lemma 3.4 gives only $\cos2\Theta_q<0$, i.e. $2\Theta_q\in(\pi/2,3\pi/2)$ mod $2\pi$, for a quartet that contributes negatively. The witness identity (3.1) of R163_401 forces at least one such quartet, since $P_+>0$. Nothing more is known at a first-contact witness.
- In the worst case, for the natural test ($\vartheta=0$), $c_\Theta=\lvert\cos2\Theta_q\rvert$ can be arbitrarily close to $0$ (cone edge).
- So **no uniform lower bound on $\lvert Q_K\rvert$ exists for the natural test.**
- In the central part, $\lvert 2\Theta_q-\pi\rvert\le\pi/2-2\epsilon'$, one has $c_\Theta\ge\sin2\epsilon'$.

**(ii) Phase rotation.** For any $2\Theta_q$ in the cone there is $\vartheta$ with $\lvert\vartheta\rvert\le\pi/8$ and $2\Theta_q+2\vartheta\in[3\pi/4,5\pi/4]$. Hence $c_\Theta\ge1/\sqrt2$ **uniformly**. Exclusion is per hypothetical configuration, so $K$ may depend on $\Theta_q$.

**(iii) Cost of the rotation.** Put $C_c=\lVert\cosh\delta\cdot\rVert^2_{L^2[-\Delta/2,\Delta/2]}=\tfrac\Delta2+\tfrac{\sinh\delta\Delta}{2\delta}$ and $C_s=\tfrac{\sinh\delta\Delta}{2\delta}-\tfrac\Delta2$. Then, with $\tau=\tan\lvert\vartheta\rvert$,
$$\sup_{\arg(a+ib)=\vartheta}\frac{\lvert k(-i\delta)\rvert}{\lVert k\rVert_1}=\frac{1+\tau^2}{2\pi\,(C_c^{-1}+\tau^2C_s^{-1})}.$$
- For $\vartheta=0$ this is $C_c/2\pi$.
- For $\tau=\tan\frac\pi8$ and $\delta\Delta\ll1$ it is $\approx0.57(\delta\Delta)^2\cdot C_c/2\pi$.
- For $\delta\Delta\gtrsim1$ the cost is $O(1)$.

*Proof.* $\lVert k\rVert_1=\lVert h\rVert_2^2=(\lVert A\rVert^2+\lVert B\rVert^2)/2\pi$. Apply Cauchy–Schwarz, $a\le\lVert A\rVert\sqrt{C_c}$ and $b\le\lVert B\rVert\sqrt{C_s}$, with equality for $A\propto\cosh$ and $B\propto\sinh$ on the interval. Then minimise $\lVert A\rVert^2+\lVert B\rVert^2$ under $b=\tau a$. ∎

(The sup is approached by $C_c^\infty$ data with loss $\epsilon$.)

### 2.3 Lemma O (upper bound on the on-line sum). PROVED-CITED + PROVED

Let $O^{\rm all}:=\sum_\rho\Psi(\mathrm{Re}\,t_\rho)\ge O_K$; this is valid because $\Psi\ge0$ on $\mathbb R$. Use:
- $N(t)=\frac t{2\pi}\log\frac t{2\pi e}+\frac78+S(t)+O(1/t)$;
- $\lvert S(t)\rvert\le C_S(t):=0.112\log t+0.278\log\log t+2.51$ (Trudgian 2014, PROVED-CITED);
- Stieltjes integration on each half-line.

These give
$$O_K\le O^{\rm all}=\tfrac L\pi I+\varepsilon'_K-2\!\int_0^\infty\!\Psi'(t)S(t)\,dt\le\tfrac L\pi I+2C_S(\gamma)(2T+\Delta)\lVert G\rVert_\infty^2\lVert k\rVert_1+\varepsilon'_K.$$

The last step uses:
- $\lVert(\Phi)'\rVert_1\le2\lVert G\rVert_\infty\lVert G'\rVert_\infty\lVert k\rVert_1+\lVert G\rVert_\infty^2\lVert k'\rVert_1$;
- Bernstein, $\lVert G'\rVert_\infty\le T\lVert G\rVert_\infty$ and $\lVert k'\rVert_1=2\lVert hh'\rVert_1\le2\lVert h\rVert_2\lVert h'\rVert_2\le\Delta\lVert h\rVert_2^2$ (Boas 11.1–11.3, CITED).

$C_S(\gamma)$ stands for the sup over the effective support; the tails of $k$ go into $\varepsilon'_K$. One may replace $\lVert G\rVert_\infty^2$ by the local sup of $G^2$ near $\gamma$ plus tails. ∎

The main terms $\frac L\pi I$ **cancel** between arch and $O$. What remains is the $S(t)$-discrepancy, of size $\asymp L(2T+\Delta)\lVert G\rVert_\infty^2\lVert k\rVert_1$, which is the frame-constant scale of R165_102 L3.

### 2.4 Other quartets

$R_K=\sum_{q'\ne q}4\,\mathrm{Re}[G^2K](t_{q'})$. Quartets inside their own cones give $R$-terms of the helpful sign. Only $S^+_K:=\sum_{q'}4(\mathrm{Re}[G^2K](t_{q'}))_+$ hurts. Define
> **(Dom$_\theta$)** $S^+_K\le\theta\lvert Q_K\rvert$ for some $\theta<1$.

This is OPEN (O167.101.1). It is the hypothesis (Dom) of R165_102. Localisation restricts it to $\lvert\gamma'-\gamma\rvert\lesssim$ (decay scale of $k$), where $N(\gamma+1)-N(\gamma)\ll\log\gamma$. The low Poisson term of R164_601 Prop 2.1 (needed there for a tail *sign*) is not needed here: we bound $\mathcal S$ in absolute value, not by sign.

---

## 3. The exclusion criterion and where $\eta<\delta$ comes from

### Thm B (exclusion criterion). PROVED given (Dom$_\theta$)

Assume the witness, with the quartet at $t_q$ in its cone, and use the test of §1 with $c_\Theta>0$. Then
$$4\,\mathrm{Re}\,\mathcal S_{\rm full}\ \ge\ 4(1-\theta)c_\Theta\lvert G(t_q)\rvert^2\lvert k(-i\delta)\rvert-E_K,\qquad E_K:=2C_S(\gamma)(2T+\Delta)\lVert G\rVert_\infty^2\lVert k\rVert_1+\lvert\mathfrak p_K\rvert+\lvert\varepsilon_K\rvert+\lvert\varepsilon'_K\rvert.$$

*Proof.* (2.1) gives $4\,\mathrm{Re}\,\mathcal S_{\rm full}=(\frac L\pi I-O_K)+\lvert Q_K\rvert-R_K+\mathfrak p_K+\varepsilon_K$, with $Q_K<0$ by Lemma Q. Then apply Lemma O to the first bracket and (Dom$_\theta$) to $R_K$. ∎

**Relation to R166_802 Thm 1(b).** Thm 1 used only $O_K\ge0$. Under that constraint the witness bounds Tail only from above, and no upper bound on Tail excludes. Once $O_K$ is also bounded **above**, the witness forces $\mathrm{Re}\,\mathcal S_{\rm full}$ to be **large**, and a one-sided *upper* bound excludes. The upper bound on $O_K$ comes from Lemma O, an unconditional zero-side input that contains no RH. This matches R167_000 §4 ("balance requires $\lvert\mathcal S\rvert\gtrsim X^\delta$").

Thm 2 of R166_802 (transfer) still applies. With the true data, the excluding inequality is equivalent to a zero-side statement. So the circularity verdict stands. What changes is only the *shape* of the needed $\Lambda$-statement: it is an upper bound.

### Thm C (amplification ceiling). PROVED

$\Phi$ is $\ge0$ on $\mathbb R$, integrable, and of type $2T+\Delta$. Hence, for $y\ne0$,
$$\lvert\Phi(x+iy)\rvert\le e^{(2T+\Delta)\lvert y\rvert}\,(P_{\lvert y\rvert}*\Phi)(x).$$
This is the Poisson majorant: $\log\lvert\Phi\rvert$ is subharmonic in the Cartwright class (Koosis, *The Logarithmic Integral* I, III.G; R163_401 Lemma 3.2, PROVED-CITED), followed by Jensen. With $P_\delta\le1/(\pi\delta)$ this gives
$$\lvert G(t_q)\rvert^2\lvert k(-i\delta)\rvert=\lvert\Phi(-i\delta)\rvert\le\frac{Y^{\delta}}{\pi\delta}\,I=\frac{2\,Y^{\delta}}{\delta}\,w(0),\qquad Y^\delta=e^{(2T+\Delta)\delta}=X^{\delta}e^{\delta\Delta}.$$

In the other direction, real-rootedness gives $\lvert G(t_q)\rvert\ge\lvert G(\gamma)\rvert$ (R164_601 Prop 2.1(iii)). There is no lower bound on the ratio $\lvert\Phi(-i\delta)\rvert/I$ beyond that. ∎

Define the **amplification exponent of the witness**:
$$\alpha=\alpha(F,K)\quad\text{by}\quad\lvert\Phi(-i\delta)\rvert=\frac{Y^{\alpha}}{\pi\delta}\,I,\qquad\alpha\le\delta\quad\text{(Thm C)}.$$

**Where $\eta<\delta$ arises (PROVED).** Suppose (WS) is stated as $\lvert\mathcal S_{\rm full}\rvert\le C\,Y^{\eta}\lVert w\rVert_\infty$, where $\lVert w\rVert_\infty=w(0)$ is the natural norm. By Thm B it excludes iff
$$C\,Y^{\eta}w(0)<(1-\theta)c_\Theta\frac{2Y^{\alpha}}{\delta}w(0)-\frac{E_K}4 .$$
Since $\alpha\le\delta$, this can only hold if $Y^{\eta}<\frac{2}{C\delta}Y^{\delta}$. That is $\eta<\delta$ up to the factor $\log(2/C\delta)/\log Y$. If the witness is not extremal ($\alpha<\delta$), the requirement is $\eta<\alpha$, which is stronger.

**The finite range does not give a weaker requirement.** Every finite-range factor is $\le1$:
- the cone phase, $c_\Theta\le1$;
- the localisation, $\lvert k(-i\delta)\rvert/\lVert k\rVert_1\le C_c/2\pi$, which is already inside $Y^\delta$ through $e^{\delta\Delta}$;
- the dominance factor, $(1-\theta)$.

The finite range helps only through the *constants* $2/\delta$, $c_\Theta$, and $E_K$ (Cor D below). In particular the phase rotation of Lemma Q(ii) is what makes $c_\Theta\ge1/\sqrt2$. Without it, the worst case (cone edge) makes $B\to-E_K/4<0$, and no (WS) helps.

---

## 4. The target

**Prop W (window obstruction). PROVED.**
- Split $\mathcal S_{\rm full}=\mathcal S_{\rm win}+\mathcal S_{\rm tail}$ at $n=X$.
- The window term is a fixed number, the same for the falsifier $f_t$ (R163_901). Its only zero-free bound is trivial: $\lvert\mathcal S_{\rm win}\rvert\le w(0)\sum_{n<X}\Lambda(n)n^{-1/2}\le2.078\,w(0)X^{1/2}$. This uses $\psi(x)<1.03883x$ (Rosser–Schoenfeld, PROVED-CITED) and partial summation.
- Combining Thm B with Thm C, a bound on $\mathcal S_{\rm tail}$ alone can exclude only if $\frac{2}{\delta}Y^{\delta}>2.078\,X^{1/2}$, that is, only if
$$\Delta>\frac{(1-2\delta)T+\log(1.04\,\delta)}{\delta}.$$
- With $T\approx L/2$ (Det+) this means $Y\gtrsim X^{1/(2\delta)}$. The "tail" then is the bulk of an asymptotic-size family, which is the regime of R166_802 Thm 3.

Otherwise (WS) must be proved for the **full** sum $1\le n\le Y$. Its window part has exactly the same nature, namely a twisted $\Lambda$-sum at frequency $\gamma$. ∎

**Prop E (positivity of the target). PROVED (necessity, given Lemma O as the only on-line input).** $B>0$ needs
$$(1-\theta)\,\frac{8c_\Theta}{\delta}\,Y^{\delta}\,w(0)\ \ge\ 4(1-\theta)c_\Theta\lvert\Phi(-i\delta)\rvert>E_K\ \ge\ 2C_S(\gamma)(2T+\Delta)\lVert G\rVert_\infty^2\lVert k\rVert_1 .$$
Since $2\pi w(0)=I\le\lVert G\rVert_\infty^2\lVert k\rVert_1$, this forces
$$Y^{\delta}\ \ge\ \frac{\pi\,\delta}{2(1-\theta)c_\Theta}\,C_S(\gamma)\,(2T+\Delta),$$
i.e. $e^{2\delta T}e^{\delta\Delta}\gtrsim\delta\cdot(0.11L)\cdot(2T+\Delta)$. This is the Det− threshold of R165_102 (amplification $e^{2\delta T}/\delta$ against the frame constant $O(LT)$). Below it, even $\mathcal S_{\rm full}=0$ does not exclude. ∎

> **Boxed target (WS$^\ast$).** At the witness $(F,G,T_c,t_q=\gamma_q-i\delta_q)$, under (Dom$_\theta$), with the phase-rotated test of §1 ($c_\Theta\ge1/\sqrt2$), $Y=e^{2T_c+\Delta}$, $w=(e^{-i\gamma_q\cdot}g)*\check k$:
> $$\boxed{\;\mathrm{Re}\sum_{1\le n\le Y}\Lambda(n)\,n^{-1/2}\,n^{i\gamma_q}\,w(\log n)\;<\;B:=(1-\theta)\,c_\Theta\,\lvert G(t_q)\rvert^2\,\lvert k(-i\delta_q)\rvert\;-\;\tfrac14E_K\;}$$
> with $E_K=2C_S(\gamma_q)(2T_c+\Delta)\lVert G\rVert_\infty^2\lVert k\rVert_1+(\text{terms }O(\gamma_q^{-1})\text{ of §2.1})$. If (WS$^\ast$) holds, the witness is excluded.
> 
> The size of $B$, via Thm C and Lemma Q(iii):
> $$B\le\frac{2c_\Theta}{\delta_q}\,X^{\delta_q}e^{\delta_q\Delta}\,w(0),\qquad \frac{\lvert k(-i\delta)\rvert}{\lVert k\rVert_1}\le\frac{\Delta+\sinh(\delta\Delta)/\delta}{4\pi},\qquad \lvert G(t_q)\rvert^2\le X^{\delta_q}\lVert G\rVert_\infty^2\ \text{(PL)}.$$
> For a tail-only version, Prop W applies.

A bound on $\lvert\mathcal S\rvert$ is more than needed: only $\mathrm{Re}\,\mathcal S<B$, a one-sided upper bound, is required. Note that the upper-bound sieves bound $\mathrm{Re}\,\mathcal S\le\sum\Lambda n^{-1/2}(\mathrm{Re}\,n^{i\gamma}w)_+$, which is of trivial size $\asymp X^{1/2}w(0)$ (R166_802 Thm 4).

**Cor D (the size of $X^{\delta}$ at the witness).**
- (a) PROVED-CITED (R165_101 Det+: $T_c\le T_L(\gamma)+\tfrac12\log\frac\pi2+o(1)$, $T_L=L/2$). This gives $X^{\delta}=e^{2\delta T_c}\le(\tfrac\pi2\,\tfrac{\gamma}{2\pi})^{\delta}(1+o(1))\approx(1.57\gamma/2\pi)^{\delta}$. So $B/w(0)\le\frac{2}{\delta}(1.57\gamma/2\pi)^{\delta}e^{\delta\Delta}$, against the trivial $2.078\,(1.57\gamma/2\pi)^{1/2}e^{\Delta/2}$. The required saving at one scale is the power $\gamma^{1/2-\delta}$.
- (b) PROVED in the lattice model (Lemma 4.10). Contact is at $S(T,\delta)=\frac{\sinh2\delta T}{2\delta}-T=\frac L2$.
  - Large $y=\delta L$: $e^{2\delta T_c}\approx2\delta L$. So $X^{\delta}\approx2\delta L$ and $B/w(0)\approx 4L$. **(WS$^\ast$) is then a polylogarithmic bound, of RH quality, at a single scale.**
  - Small $y\le y_0=2.1773$: no model contact before $T_L$. Det+ then gives $X^\delta\le e^{y_0}1.57^{\delta}\approx11$. But Prop E fails there ($Y^\delta$ is bounded while $E_K\asymp LT$), so $B<0$ for $\Delta=O(1/\delta)$: O167.101.2.
- (c) Consequence, ARGUED. At $T_c\approx T_L$ the twist $n^{i\gamma}$ on $n\asymp X\approx0.25\gamma$ has local frequency $\gamma/(2\pi n)\approx0.64$ per unit step. So $\mathcal S$ is locally a Vinogradov sum $\sum\Lambda(n)e(\alpha n)$ with slowly drifting $\alpha$. The classical minor-arc bound (Vinogradov–Vaughan, $N^{4/5}$) gives exponent $0.3$ in the $n^{-1/2}$ normalisation. The zero-free-region route (Vinogradov–Korobov) gives only a saving $\exp(-c(\log X)^{3/5-\epsilon})$ over $X^{1/2}$. Both fall short of $\delta$ for $\delta<0.3$, and of the log-size target in (b). This is a pointer for A2, not a theorem.

---

## 5. Sanity checks

**5.1 dlVP (R164_601 Thm 3.3).** Insert the trivial bound $\lvert\mathcal S_{\rm full}\rvert\le2.078\,w(0)Y^{1/2}$ into Thm B with the ceiling of Thm C. Exclusion is possible only if $\frac{2c_\Theta}{\delta}Y^{\delta}>2.078\,Y^{1/2}$. That is $(\tfrac12-\delta)\log Y<\log(0.96\,c_\Theta/\delta)$, so $\tfrac12-\delta\lesssim0.65/\log Y\asymp1/\log\gamma$. This is exactly the dlVP shape, with $\Lambda$ used only through its size. Consistent. PROVED (necessity); the constant is not optimised.

**5.2 Det− (R165_102).** In the large-$y$ regime, Thm 1 of R165_102 (the quartet wins by amplification $e^{2\delta T}/\delta$ against the frame constant $O(LT)$) is the statement that **$B>0$** (Prop E). There the requirement on the tail reads: the twisted $\Lambda$-sum must be smaller than the quartet's amplified mass, $\asymp(e^{2\delta T}e^{\delta\Delta}/\delta)\,w(0)$. At contact $e^{2\delta T_c}\approx\delta LT$, so the requirement is a bound $\ll L\,T\,e^{\delta\Delta}w(0)$. This is the logarithmic-size target of Cor D(b). In the small-$y$ regime R165_102 says "OPEN: needs a sub-Landau lower frame". Here that is O167.101.2: the deficit is in Lemma O (on-line counting), not in $\Lambda$.

**5.3 Lattice model (Lemma 4.10).** The model has no primes, so (2.1) is replaced by the Poisson-exact lattice sum. Lemma O holds with error $0$ (an exact lattice), so $E_K$ reduces to the $O(\gamma^{-1})$ terms. The model's version of Thm B is the contact criterion $S(T,\delta)>L/2$. The extremal ($G$ odd, node at $\gamma$, $b=\sinh\delta u$) has $\alpha\to\delta$, i.e. it saturates Thm C up to the factor $1/(4\delta)$ versus $1/(\pi\delta)$. So the model attains the ceiling: in the worst case, $\eta<\delta$ is sharp. Consistent. Labels: PROVED in the model; the identification of constants is ARGUED.

**5.4 Falsifiers.** For $f_t$, Thm A holds with $\Lambda_{f_t}$ on its own semigroup. Its witness satisfies (2.1), so (WS$^\ast$) is false for $\Lambda_{f_t}$ at its own witness. The same holds for $M_m$ with $\Lambda+\beta_m$. This is consistent with R167_000 §3. A3 locates the step.

---

## 6. The weight: data for A2 (all PROVED)

1. **Formula.** $w(u)=\int_{-2T}^{2T}g(v)e^{-i\gamma v}\check k(u-v)\,dv$. Here $g=(G^2)^\vee=\frac1{2\pi}(F*F^{\#})$-type autocorrelation, supported in $[-2T,2T]$, and $\check k=\frac1{2\pi}\widehat h*\widehat h$ (up to normalisation), supported in $[-\Delta,\Delta]$. The function $w$ is supported in $[-2T-\Delta,2T+\Delta]$, and $w(-u)=\overline{w(u)}$.
2. **Positivity of the transform.** $\widehat w(s)=G(s+\gamma)^2k(s)\ge0$ on $\mathbb R$, so $w$ is positive-definite. Hence $\lvert w(u)\rvert\le w(0)=\frac1{2\pi}\int G(s+\gamma)^2k(s)ds$, which is the local $L^2$-mass of $G$ at $\gamma$ seen through $k$.
3. **Size on the tail.** For $u\in[2T,2T+\Delta]$, $\lvert w(u)\rvert\le\lVert g\rVert_\infty\int_{u-2T}^{\Delta}\lvert\check k\rvert$, with $\lVert g\rVert_\infty\le\frac1{2\pi}\lVert G\rVert_2^2$. Thus $w\to0$ at the outer edge $u=2T+\Delta$; the tail weight is a "corner" piece.
4. **Smoothness.** $\lvert w^{(j)}(u)\rvert\le\frac1{2\pi}\int\lvert s\rvert^jG(s+\gamma)^2k(s)ds\le\frac{\lVert G\rVert_\infty^2}{2\pi}\int\lvert s\rvert^jk$. This is finite for all $j$ when $\widehat h\in C_c^\infty$; for example $\int s^2k=\frac1{2\pi}\lVert\widehat h'\rVert_2^2$.
5. **Bernstein for $\widehat w$.** $\widehat w=\Phi$ is entire of type $2T+\Delta$ and bounded on $\mathbb R$ by $\lVert G\rVert_\infty^2\lVert k\rVert_\infty$. So $\lVert\Phi'\rVert_\infty\le(2T+\Delta)\lVert G\rVert_\infty^2\lVert k\rVert_\infty$ and $\lVert\Phi'\rVert_1\le(2T+\Delta)\lVert G\rVert_\infty^2\lVert k\rVert_1$ (used in Lemma O).
6. **Duality.** $\mathcal S_{\rm full}=\frac1{2\pi}\int\Phi(s)\,\Big(\sum_{n\le Y}\Lambda(n)n^{-1/2+i(\gamma+s)}\Big)ds$. This is a $\Phi$-average, with $\Phi\ge0$, of the partial Dirichlet polynomial of $-\zeta'/\zeta$ on the critical line near height $\gamma$. It is the form A2 can attack by large-sieve or mean-value methods; the positivity of $\Phi$ makes it a positive average.
7. **Norms to use in (WS$^\ast$).** Use $w(0)=I/2\pi$, as in Thm C and Prop W, and $\lVert G\rVert_\infty^2\lVert k\rVert_1$, as in $E_K$. Their ratio $I/(\lVert G\rVert_\infty^2\lVert k\rVert_1)\in(0,1]$ measures how small $G$ is near $\gamma$. Placing $k$ where $G$ is small (near the node $x_0$ in the cone) lowers $w(0)$ but not $E_K$. So it helps against Prop W and hurts against Prop E.

---

## 7. Ledger

**PROVED:**
- C1, Thm A, Lemma Q (phase, rotation, exact cost);
- Thm B given (Dom$_\theta$), Thm C, Prop W, Prop E (necessity);
- the dlVP-shape check §5.1, and §6.

**PROVED-CITED:**
- explicit formula (1.1);
- Trudgian's bound on $S(t)$ and the Riemann–von Mangoldt formula;
- Rosser–Schoenfeld $\psi(x)<1.03883x$;
- Poisson majorant (Koosis; R163_401 Lemma 3.2);
- Bernstein (Boas);
- Det+ (R165_101);
- Lemma 4.10 (R163_401).

**ARGUED:**
- Cor D(c) (Vinogradov-type exponents as a pointer);
- the constant identification in §5.3.

**OPEN:**
- O167.101.1 (Dom$_\theta$);
- O167.101.2, the small-$y$ regime, which needs on-line counting beyond $S=O(\log t)$ rather than a $\Lambda$-bound;
- (WS$^\ast$) itself.

**Corrections recorded:**
- C1, the weight $w$ (R166_802 Prop 2.1, R167_000 §1);
- the range is $n\le Xe^{\Delta}$ for $k$ of type $\Delta$ (R167_000's $Xe^{2\Delta}$ corresponds to type $2\Delta$);
- (WS) must cover the full range $[1,Y]$, not only $[X,Y]$ (Prop W);
- the exponent formulation "$X^\eta$, $\eta<\delta$" is a single-scale statement, because $X^\delta\le(1.57\gamma/2\pi)^\delta$ at the witness (Cor D).

**Grid.** Cell "witness-weighted sieve (WS)": the target is now exact (WS$^\ast$). The symbol is unchanged, OPEN. Circularity per R166_802 Thm 2 persists: the target's truth for ζ is equivalent to a zero-side statement.
