# R163_402 — Light-cone lemma and resolution law for one off-line quartet

Status: §1 PROVED. §2 PROVED inside a stated lattice model, HEURISTIC for actual zeros. §3 is uncertified float numerics.
Scripts: `scripts/r163_402_light_cone.py`, `scripts/r163_402_saturation.py` (zeros cached in `scripts/zeta_zeros_600.npy`).

Conventions: $\hat F(z)=\int_{-T}^{T}F(u)e^{izu}\,du$ and $t_\rho=(\rho-\tfrac12)/i$. An off-line quartet $\rho=\tfrac12\pm\delta+i(\pm\gamma)$ gives $t=\pm\gamma\mp i\delta$. If $\hat F$ is real on $\mathbb R$, then $\hat F(\bar t)=\overline{\hat F(t)}$, so each $t$ contributes $\hat F(t)^2$. The pair $\gamma\mp i\delta$ contributes $2\,\mathrm{Re}\,\hat F(\gamma-i\delta)^2$ in total, and the quartet contributes $4\,\mathrm{Re}\,\hat F(\gamma-i\delta)^2$ when $\hat F$ is even.

## 1. Light-cone lemma (PROVED)

**Setting.** Let $\hat F\not\equiv0$ be entire of exponential type $\le T$, real on $\mathbb R$, with only real zeros $\{x\}$ (counted with multiplicity), and let $\hat F|_{\mathbb R}\in L^2$. Then $\hat F$ is in the Cartwright class. By the Cartwright–Levinson factorisation (Levin, *Lectures on entire functions*, Lect. 17),
$$\hat F(z)=c\,z^m e^{ibz}\lim_{R\to\infty}\prod_{0<|x|<R}(1-z/x).$$
Here $b$ is real. Real-valuedness on $\mathbb R$ forces $e^{ibz}$ to be real on $\mathbb R$, so $b=0$. Hence $\hat F$ lies in the Laguerre–Pólya class with no exponential factor, and $\hat F'/\hat F(z)=\mathrm{p.v.}\sum_x (z-x)^{-1}$, where the sum converges symmetrically.

**Lemma 1 (phase law).** Fix $\delta>0$. Then $\hat F$ has no zeros on the line $\mathrm{Im}\,z=-\delta$. Let $\theta_\delta(\gamma)$ be a continuous branch of $\arg\hat F(\gamma-i\delta)$. Then:

1. $\theta_\delta'(\gamma)=\sum_x \dfrac{\delta}{(\gamma-x)^2+\delta^2}=\pi\,P_\delta*\nu(\gamma)>0$. Here $\nu=\sum_x\delta_x$ is the node measure and $P_\delta$ is the Poisson kernel. So the phase is strictly increasing, and its speed is $\pi$ times the node density smoothed at scale $\delta$.
2. If $\gamma$ is not a node: $\theta_\delta(\gamma)\equiv-\,\mathrm{p.v.}\sum_x\arctan\dfrac{\delta}{\gamma-x}\pmod\pi$, with principal arctan. Also $|\hat F(\gamma-i\delta)|^2=\hat F(\gamma)^2\prod_x\bigl(1+\delta^2/(\gamma-x)^2\bigr)$.
3. $\mathrm{Re}\,\hat F(\gamma-i\delta)^2=|\hat F(\gamma-i\delta)|^2\cos2\theta_\delta(\gamma)$. So it is $<0$ iff $\theta_\delta(\gamma)\in(\pi/4,3\pi/4)+\pi\mathbb Z$, and it is $=0$ exactly on the discrete set $\theta_\delta\in\pi/4+\tfrac\pi2\mathbb Z$.

*Proof.*
- (1) Differentiate: $\theta'=\mathrm{Im}\,(\hat F'/\hat F)(\gamma-i\delta)=\sum_x\mathrm{Im}\,(\gamma-x-i\delta)^{-1}=\sum_x\delta/((\gamma-x)^2+\delta^2)$. The convergence is absolute because $\sum 1/(1+x^2)<\infty$ in the Cartwright class.
- (2) Take $\hat F(\gamma-i\delta)/\hat F(\gamma)=\lim_R\prod_{|x|<R}\bigl(1-i\delta/(\gamma-x)\bigr)$. Each factor has argument $-\arctan(\delta/(\gamma-x))\in(-\pi/2,\pi/2)$ and modulus $\sqrt{1+\delta^2/(\gamma-x)^2}$. The modulus product converges absolutely. The argument sum converges as a principal value because $\arctan y=y+O(y^3)$ and $\mathrm{p.v.}\sum 1/(\gamma-x)$ converges. Finally, $\arg\hat F(\gamma)\in\{0,\pi\}$.
- (3) Immediate. ∎

**Corollary 2 (light cone).** Write $x_0$ for the node nearest to $\gamma$ and $d=\gamma-x_0$. Write $\epsilon(\gamma,\delta)=\mathrm{p.v.}\sum_{x\ne x_0}\arctan(\delta/(\gamma-x))$ for the far-node phase. Then $\mathrm{Re}\,\hat F(\gamma-i\delta)^2<0$ iff
$$\arctan(\delta/d)+\epsilon\in(\pi/4,3\pi/4)\pmod\pi .$$
When $|\epsilon|$ is small (for example $|\epsilon|\le\delta\,|\mathrm{p.v.}\sum_{x\ne x_0}(\gamma-x)^{-1}|+O(\delta^3)$ is small), this is the *light cone* $|\gamma-x_0|<\delta$ up to $O(\epsilon)$. Exactly: $|d|<\delta$ is equivalent to $\arctan(\delta/|d|)>\pi/4$. So an off-line pair is seen negatively exactly when a node of the test function lies within distance about $\delta$ of $\gamma$. In the $(\gamma,\delta)$ half-plane the negative region near each isolated node is the cone $\{\delta>|\gamma-x_0|\}$ of slope 1, bent by the far-node phase $\epsilon$.

**Corollary 3 (exact half-duty law).** Lemma 1(1) gives $\theta_\delta$ as a strictly increasing map. Under it the negative set $N_\delta=\{\gamma:\mathrm{Re}\hat F(\gamma-i\delta)^2<0\}$ is the preimage of half of every period. Therefore, for every interval $I$ whose endpoints sit at phase $\equiv\pi/4 \pmod\pi$,
$$\int_{N_\delta\cap I}\theta'_\delta\,d\gamma=\tfrac12\int_I\theta'_\delta\,d\gamma .$$
In words: measured in Poisson-smoothed node count, exactly half of the line $\mathrm{Im}=-\delta$ is negative. The phase advances by $\pi$ for each node crossed, so whole windings occur only with node density about $1/\delta$ on scale $\delta$. For a type-$T$ function the average node density is at most $T/\pi$ (Levinson density theorem), so the mean phase speed is at most $T$.

*Remark (what this does and does not say).* The lemma is purely about the sign of one term. It does not show that $W_T<0$. The on-line terms $\sum|\hat F(\gamma_n)|^2$ penalise putting a node within $\delta$ of $\gamma$ while keeping $|\hat F|$ small on the nearby on-line zeros. That trade-off is §2.

## 2. Resolution law

**Local model (assumptions).**
- (M1) Localise near $\gamma$: $\hat F(z)=G(z-\gamma)\pm G(-z-\gamma)$, where $G$ has type $T$ and is real on $\mathbb R$. The cross terms between the $\pm\gamma$ copies are dropped; they are $o(1)$ as $\gamma\to\infty$ for fixed $G\in PW_T$. Both sides then double, which leaves the threshold unchanged.
- (M2) The on-line ordinates near $\gamma$ are an exact lattice $\gamma+(n+\alpha)/\rho$ with $\rho=\frac1{2\pi}\log\frac{\gamma}{2\pi}$.

**Theorem 4 (exact threshold in the model).** Assume (M1)–(M2) and $T<\pi\rho$. Then
$$\inf_{G}\Bigl[\sum_n G\bigl(\tfrac{n+\alpha}\rho\bigr)^2+2\,\mathrm{Re}\,G(-i\delta)^2\Bigr]<0
\iff S(T,\delta):=\int_{-T}^{T}\sinh^2(\delta u)\,du=\frac{\sinh 2\delta T}{2\delta}-T>\pi\rho .$$

*Proof.* Write $G(z)=\int_{-T}^T f(u)e^{izu}du$ with $f=a+ib$, $a$ even and $b$ odd (both real), which is the condition for $G$ to be real on $\mathbb R$.

1. The function $G^2$ has type $2T<2\pi\rho$. By Poisson summation, $\sum_n G((n+\alpha)/\rho)^2=\rho\int_{\mathbb R}G^2=2\pi\rho\int(a^2+b^2)$ exactly, because the only alias that survives is the $k=0$ term.
2. Next, $G(-i\delta)=\int f e^{\delta u}=A+iB$ with $A=\int a\cosh\delta u$ and $B=\int b\sinh\delta u$. So $2\mathrm{Re}\,G(-i\delta)^2=2A^2-2B^2$.
3. Cauchy–Schwarz gives $B^2\le S\int b^2$. Hence the form is $\ge 2\pi\rho\int a^2+(2\pi\rho-2S)\int b^2$.
4. Equality holds for $a=0$ and $b=\sinh(\delta u)$. ∎

The extremal $G(x)=-2\int_0^T\sinh(\delta u)\sin(xu)\,du$ is odd. Its node sits exactly at $x=0$, i.e. at $\gamma$, as Corollary 2 requires.

**Corollary 5 (resolution law).** $S=\tfrac23\delta^2T^3\,(1+O(\delta^2T^2))$. So in the regime $T^*<\pi\rho$,
$$T^*=\Bigl(\frac{3\pi\rho}{2\delta^2}\Bigr)^{1/3}(1+O(\delta^2T^{*2}))=\Bigl(\tfrac34\log\tfrac{\gamma}{2\pi}\Bigr)^{1/3}\delta^{-2/3}\,(1+o(1)),$$
which is the expected $T\asymp(\log\gamma)^{1/3}\delta^{-2/3}$. The mechanism has two parts:
- the gain from a node at $\gamma$ is $\delta^2G'(0)^2$;
- the cheapest cost of $G'(0)=1$ at density $\rho$ is $\rho\,\min\|G\|^2\asymp\rho/T^3$.

**Domain of validity: the Landau ceiling.** The law is self-consistent only while $T^*<\pi\rho=\frac12\log\frac\gamma{2\pi}$. That holds iff $\delta\gtrsim(3/2)^{1/2}/(\pi\rho)\approx 2.45/\log(\gamma/2\pi)$, i.e. for $\delta$ larger than a constant times the mean zero spacing. *(Erratum, R163_590 D1: the cubic value is only an upper bound, $T^*\le(\tfrac34L/\delta^2)^{1/3}$ with $L=\log(\gamma/2\pi)$, since $\sinh y-y\ge y^3/6$; it is not asymptotic in the self-consistent regime, where $\delta T^*\gtrsim1.2$. For fixed $\delta$ and $L\to\infty$, $T^*\sim\log(2\delta L)/(2\delta)$, so $T^{*3}=O(\log^3L)=o(L)$. The exact self-consistency threshold is $\delta L>y_0=2.1773\ldots$, $\sinh y_0=2y_0$, not $2.45$. See R163_401 Lemma 4.10 and Cor 4.10a.)* For smaller $\delta$ the window exceeds the Landau sampling density. Then the sampling (frame) lower bound fails: there are $G$ with $\sum G(\gamma_n)^2\ll\|G\|^2$. The threshold becomes **density-limited**:
$$T^*=\pi\rho+\Delta(\delta),$$
where $\Delta$ grows only slowly (heuristically like $\log(1/\delta)$, because the sampling constant beyond critical density decays exponentially in $T-\pi\rho$). HEURISTIC; not proved.

Summary: $T^*(\gamma,\delta)\asymp\max\{(\log\gamma)^{1/3}\delta^{-2/3},\ \tfrac12\log\gamma\}$, read as follows:
- the first branch is exact in the lattice model (Theorem 4);
- the second branch is heuristic.

For every off-line zero, the first branch is dominated by the second once $\delta\lesssim 1/\log\gamma$.

## 3. Numerics (UNCERTIFIED float, K=40 Legendre modes)

Setup:
- Basis: $\phi_k(u)=i^kP_k(u/T)$. Then $G_k(z)=2T(-1)^kj_k(Tz)$ exactly (spherical Bessel functions), and $G_k$ is real on $\mathbb R$.
- On-line zeros: the first 600 zeta ordinates (mpmath), shifted to $\gamma_0$. Here $\gamma_0$ is the midpoint of consecutive zeros $n=101/102$, $301/302$, $501/502$.
- Artificial pair: the single pair at $\gamma_0\mp i\delta$.
- Output: $\lambda(T)=\min W/\|f\|^2$ (relative to the top eigenvalue). $T^*$ is the first grid $T$ (step 0.01) at which $\lambda<-10^{-9}$.

| $\gamma_0$ | $\pi\rho$ | δ | $T^*$ zeta | $T^*$ sinh-law | $T^*$ cubic |
|---|---|---|---|---|---|
| 238.7 | 1.82 | 0.1 / 0.2 / 0.4 | 2.22 / 2.15 / 2.09 | 6.32 / 3.92 / 2.42 | 6.49 / 4.09 / 2.57 |
| 238.7 | 1.82 | 0.8 / 1.2 | 1.48 / 1.16 | 1.48 / 1.10 | 1.62 / 1.24 |
| 545.0 | 2.23 | 0.1 / 0.2 / 0.4 | 2.68 / 2.63 / 2.51 | 6.74 / 4.18 / 2.57 | 6.94 / 4.37 / 2.76 |
| 545.0 | 2.23 | 0.8 / 1.2 | 1.42 / 1.10 | 1.57 / 1.17 | 1.74 / 1.33 |
| 813.4 | 2.43 | 0.1 / 0.2 / 0.4 | 2.94 / 2.87 / 2.69 | 6.92 / 4.29 / 2.63 | 7.15 / 4.50 / 2.84 |
| 813.4 | 2.43 | 0.8 / 1.2 | 1.62 / 1.18 | 1.60 / 1.19 | 1.79 / 1.36 |

Lattice control ($\gamma_0=500$, exact lattice of density $\rho$):

| δ | $T^*$ numerics | sinh-law |
|---|---|---|
| 0.8 | 1.566 | 1.557 |
| 1.2 | 1.167 | 1.159 |
| 0.4 | 2.38 | 2.55 (above $\pi\rho=2.2$, so Theorem 4 does not apply) |

The control validates the code and Theorem 4.

Small δ at $\gamma_0\approx545$ ($\pi\rho=2.23$), zeta / lattice:

| δ | $T^*$ zeta | $T^*$ lattice |
|---|---|---|
| 0.1 | 2.68 | 2.54 |
| 0.01 | 2.88 | 2.75 |
| 0.001 | 3.04 | 3.02 |

$T^*$ saturates just above the Landau ceiling and grows roughly $+0.2$ per decade of $1/\delta$. This fits $\pi\rho+O(\log 1/\delta)$; it does not fit $\delta^{-2/3}$.

**Reading.**
- (i) The $\delta^{-2/3}(\log\gamma)^{1/3}$ law is correct, with the constant $(3/4)^{1/3}$, only in the large-δ branch ($\delta\gtrsim 2.5/\log\gamma$). Actual zeta zeros match the lattice prediction there to within about 10%.
- (ii) For realistic (small) δ, the controlling scale is the Landau density $T\approx\frac12\log(\gamma/2\pi)$, plus a slowly growing $\log(1/\delta)$ excess.
- (iii) Consequence for row D: a quartet at height γ is detectable by $W_T$ already at $T=O(\log\gamma+\log1/\delta)$. Below the Landau ceiling it is invisible unless $\delta\gtrsim(\log\gamma)^{1/2}T^{-3/2}$.

Caveats: float only; truncation at K=40 is not error-controlled for δ ≤ 0.01; the one-sided model ignores the $-\gamma$ mirror and the archimedean/prime side entirely. This is a zero-side statement only and claims nothing about RH.
