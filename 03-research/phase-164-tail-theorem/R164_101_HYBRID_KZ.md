# R164_101 — The hybrid Euler–Hadamard cut at the window edge: the kernel equation as a statement about $Z_X$ — **(KZ) is (1.1) rewritten; wall E1, DEAD (PROVED)**

*Line L1, question 1 and the (KZ) lemma of R164_000. Pure mathematics, no numerics, no commits. Only this file was written. No label of record changes.*
*Read first: R164_000 (§0–§1); R163_401 (§1, §2.4, §4.6, §4.8, Rem 4.8a, §4.11); R163_801 (Thm 3, Cor 3.1); R163_1001 (Thm C.3, Thm O); grid R162_2300 §3 (E1, W3), §4, §7 (S1–S12).*
*Corpus check.* I grepped for "Gonek–Hughes–Keating / hybrid Euler / Euler–Hadamard": hits only in R164_000 and phase-37 doc 113 (LP112 against the literature, which does not touch row D). I grepped for "phase derivative / arg Z": the nearest prior route is **phase-64 FACE-C** (spectral shift). There, the phase derivative of the *finite Euler determinant* $D_P$ is the explicit-formula prime sum, and the route closed at first order. FACE-C is the $P_X$ half of the present split. The $Z_X$ half (the zero factor of the hybrid product, paired with the witness) is new to the corpus. It dies here for a different reason (§3).

## 0. Status table

| # | statement | label |
|---|---|---|
| GHK | Gonek–Hughes–Keating hybrid product, statement and error (§1.1) | PROVED-CITED **from memory** (exact form of the error terms to be verified at page level; the editor, L3, has this) |
| Lem H | exact hybrid identity $\zeta=\widetilde P_X\,Z_X\,E_X$ for every smooth cutoff, no error term, valid on all of $\mathbb C$ (§1.2) | PROVED |
| Lem L | on the critical line: $\tfrac12\sigma^g_T(\tau)=-\theta_X'(\tau)-\mathrm{Re}\,M(\tfrac12-i\tau)+\sum_{k\ge1}\mathrm{Re}\,M(-2k-\tfrac12-i\tau)$ pointwise, $\theta_X:=\arg Z_X(\tfrac12+i\tau)$ (§2.1) | PROVED |
| Lem P | **pairing lemma**: for $h=\widehat G\widehat H^\#$, $G,H\in\mathcal D_T$, and cutoff $g\equiv1$ on $[0,2T]$: $\int h\,\mathrm{Re}\,M(\rho-\tfrac12-i\tau)\,d\tau=\pi[h(t_\rho)+h(\bar t_\rho)]\mathbf 1_{\delta_\rho>0}+\pi h(\gamma_\rho)\mathbf 1_{\delta_\rho=0}$, and $0$ if $\delta_\rho<0$ (pole and trivial zeros likewise) (§2.2) | PROVED |
| **Thm KZ** | $W_T(F,H)=-\dfrac1\pi\displaystyle\int_{\mathbb R}\widehat F(\tau)\overline{\widehat H(\tau)}\ \theta_{X'}'(\tau)\,d\tau$ for all $F,H\in\mathcal D_T$, $X'=e^{2T+\eta}$, any $\eta>0$, any admissible cutoff. **At the witness: $\int\widehat F\,\overline{\widehat H}\,\theta'_{X'}=0$ for all $H$, in particular $\int|\widehat F|^2\theta'_{X'}=0$.** (§2.3) | PROVED |
| Thm E1 | (KZ) is (1.1) term by term: the pairing of $\theta'_{X'}$ against $PW_T$-products is a functional of the zero multiset alone and does not depend on $X'$, on $\eta$ or on the cutoff. Row D $\iff$ the compression of the symbol $-\theta'_{X(T)}$ to $PW_T$ is $\succeq0$ for every $T$, which is RH (§3) | **PROVED: question 1 answered, DEAD (E1)** |
| Cor E1′ | the $\log\lvert Z_X\rvert$ / complex variant: $\int h\,(-Z_X'/Z_X)(\tfrac12+i\tau)\,d\tau=\pi\sum_{\delta=0}h(\gamma)+2\pi\sum_{\delta>0}h(t_\rho)$. It is the one-sided zero sum of R163_801 (3.1). On the diagonal of parity-definite real tests it reduces to $\pi W_T(F)$. It carries no information beyond R163_801 Cor 3.1 / R163_1001 Thm C.3 (§3.2) | PROVED (restatement, E1) |
| Prop EB | **Euler-blindness**: the proof of Thm KZ uses only (a) $-f'/f$ has a Dirichlet expansion in some right half-plane, (b) a Hadamard product with the stated archimedean factor, and (c) the support of $-g'$ in $[2T,\infty)$. It never uses the Euler product or the sign of the tail coefficients of $\log Z_X$. Hence (KZ) holds verbatim for $f_t$, $f_\chi$ and $M_m$, and with an explicit non-zero-side correction for Λχ₂ and deletion (§4) | PROVED |
| Prop D | deletion $\Lambda\mathbf 1_{n\ge5}$ has **literally the same** $Z_X$ as $\zeta$ (for $X>4$) and a negative window form at $T\le0.4608$. Hence no statement of the form "property of $Z_X$ ⟹ sign of $W_T$" exists. The sign lives in the $P_X$/window coupling, never in $Z_X$ alone (§4) | PROVED (the deletion value is record, PROVED-CITED) |
| Prop θ | $\zeta_\theta$ has a tail $-Z_X'/Z_X$ that is a Dirichlet series with **nonnegative** coefficients on $(\log X,\infty)$ (Bernstein / complete monotonicity in $\sigma>1$), and infinitely many zeros off $\mathrm{Re}\,s=\tfrac12$. So candidate (c) of R164_000 §1, read as "tail-only", is false; it can survive only coupled to ζ's window **and** a functional equation about $\tfrac12$ (§4) | PROVED |
| O164.101 | is there a system with ζ's window $(\Lambda(n))_{n<X}$, ζ's FE about $\tfrac12$ with $\Gamma(s/2)$, a tail with nonnegative coefficients (Beurling-positive), and an off-line zero in a cone of its witness? (the decisive test of L1, R164_000 "riesgo principal"; for R164_102) | OPEN |
| $(\star_{\rm cell})$, (TC), row D | | **OPEN** |

**Grid cells.** 4F (Euler product × global transforms in $T$) and 7F (tail by zeros), as declared in R164_000. Both receive one DEAD route (killer E1) and one sharpened residue (O164.101). **Walls met:** E1 (Thm E1, Cor E1′), W3 (Prop EB: the identity is class-blind), W12 (exact identity, no sign). The specification fails at S2 (the statement is linear in $\widehat F\overline{\widehat H}$), at S4 (Prop EB) and at S7 (the Euler product never enters the pairing; Prop EB).

---

## 1. The hybrid product, stated exactly

### 1.1 Gonek–Hughes–Keating (Duke Math. J. 136 (2007), 507–549), Theorem 1. PROVED-CITED, **from memory**

Let $u\ge0$ be smooth with mass $1$, supported in $[e^{1-1/X},e]$. Put
$$U(z)=\int_0^\infty u(x)\,E_1(z\log x)\,dx,\qquad E_1(z)=\int_z^\infty e^{-w}\frac{dw}{w}.$$
Let $X\ge2$, $s=\sigma+it$ with $\sigma\ge0$, $|t|\ge2$, and $K\ge1$ fixed. Then
$$\zeta(s)=P_X(s)\,Z_X(s)\Big(1+O\Big(\frac{X^{K+2}}{(|s|\log X)^K}\Big)+O\big(X^{-\sigma}\log X\big)\Big),$$
$$P_X(s)=\exp\Big(\sum_{n\le X}\frac{\Lambda(n)}{n^s\log n}\Big),\qquad Z_X(s)=\exp\Big(-\sum_\rho U\big((s-\rho)\log X\big)\Big).$$
The implied constants depend on $u$ and $K$ only, uniformly in $\sigma\ge0$. Since $E_1(z)=-\gamma-\log z+O(z)$, $\exp(-U((s-\rho)\log X))$ vanishes to first order at $s=\rho$, so $Z_X$ carries all the nontrivial zeros.
*Flagged from memory:* the support convention for $u$, the exact pair of error terms, and the range $\sigma\ge0$, $|t|\ge2$. Nothing below depends on them, because §1.2 replaces Thm 1 by an exact identity.

*Where the error comes from (ARGUED, consistent with the GHK proof as I recall it).* The $O(X^{K+2}/(|s|\log X)^K)$ term is the trivial zeros plus the pole, i.e. $\log E_X$ below. The $O(X^{-\sigma}\log X)$ term is the replacement of the smoothed weights on $(X^{1-1/X},X]$ by the sharp sum $n\le X$. Before these two bounds GHK's formula is an identity. That is Lemma H.

### 1.2 Lemma H (exact hybrid identity). PROVED

Let $L>0$ and let $g\in C^\infty([0,\infty))$ satisfy $g\equiv1$ on $[0,L_0]$ and $g\equiv0$ on $[L,\infty)$, with $0<L_0<L$. Put
$$M(z):=\frac1z\int_{L_0}^{L}\big(-g'(u)\big)e^{uz}\,du .$$
$M$ is meromorphic with a single simple pole at $0$ of residue $\int(-g')=1$. By repeated integration by parts, $|M(z)|\ll_{g,k}e^{L\max(\mathrm{Re}\,z,0)}(1+|z|)^{-k}$ for every $k$, uniformly in vertical strips. Then, as meromorphic functions on $\mathbb C$,
$$\sum_{n\ge1}\Lambda(n)\,g(\log n)\,n^{-s}=-\frac{\zeta'}{\zeta}(s)+M(1-s)-\sum_\rho M(\rho-s)-\sum_{k\ge1}M(-2k-s),\tag{H}$$
and the sum over $\rho$ converges absolutely and locally uniformly off the zeros. Integrating from $+\infty$:
$$\zeta=\widetilde P_X\,Z_X\,E_X,\quad -\frac{\widetilde P_X'}{\widetilde P_X}=\sum\Lambda(n)g(\log n)n^{-s},\quad -\frac{Z_X'}{Z_X}=\sum_\rho M(\rho-s),\quad -\frac{E_X'}{E_X}=-M(1-s)+\sum_{k\ge1}M(-2k-s),$$
with $X=e^{L}$. **This is exact; there is no error term.**

*Proof.* The left side of (H) is a finite Dirichlet polynomial, hence entire. For $c>0$, $\frac1{2\pi i}\int_{(c)}e^{(u-\ell)z}\frac{dz}{z}=\mathbf 1_{u>\ell}$, so $\frac1{2\pi i}\int_{(c)}M(z)n^{-z}dz=g(\log n)$. For $\mathrm{Re}\,s>1$ and $c>0$, this gives $\sum\Lambda g(\log n)n^{-s}=\frac1{2\pi i}\int_{(c)}(-\zeta'/\zeta)(s+z)M(z)dz$. Shift the contour to $\mathrm{Re}\,z=-A$ and let $A\to\infty$ along the standard sequence avoiding the ordinates. The integrand decays there: $|M|\ll(1+|z|)^{-2}$ for $\mathrm{Re}\,z\le0$, and $\zeta'/\zeta\ll\log^2$ on the chosen contours. The residues are: at $z=0$, $-\zeta'/\zeta(s)$; at $z=1-s$, $+M(1-s)$; at $z=\rho-s$, $-M(\rho-s)$ with multiplicity; at $z=-2k-s$, $-M(-2k-s)$. The zero sum converges absolutely by $N(R+1)-N(R)\ll\log R$. Both sides of (H) are meromorphic on $\mathbb C$, so (H) holds everywhere. The same contour shift as GHK (their $U'$ is our $M$ up to the change of variable $x=e^{u/\log X}$). ∎

*Choice for the window.* With $T$ fixed, take $L_0=2T$ and $L=2T+\eta$, i.e. $X'=e^{2T+\eta}=Xe^\eta$. **Then $\widetilde P_{X'}$ is exactly the window datum** in the sense of R163_401 §4.6: the pairing of its log-derivative with any $PW_T$-product depends only on $(\Lambda(n))_{n<e^{2T}}$ (Lemma L below). GHK's own normalisation, with the smoothing *below* $X$, would change the window by the finite comb $\Lambda(n)(1-g(\log n))$ on $(X^{1-1/X},X)$. That is an explicit correction, and it changes nothing in §3.

---

## 2. The kernel equation as a statement about $Z_{X'}$

### 2.1 Lemma L (the window symbol is minus the phase derivative of $Z_{X'}$, plus explicit terms). PROVED

Write $\theta_{X'}(\tau):=\arg Z_{X'}(\tfrac12+i\tau)$, so that $\theta_{X'}'(\tau)=\mathrm{Re}\,(Z_{X'}'/Z_{X'})(\tfrac12+i\tau)=-\sum_\rho\mathrm{Re}\,M(\rho-\tfrac12-i\tau)$. For an on-line $\rho$, $\mathrm{Re}\,M(i(\gamma-\tau))=\frac1{\gamma-\tau}\int(-g')\sin(u(\gamma-\tau))du$ is smooth. So $\theta'_{X'}$ is a smooth function on $\mathbb R$, $O(\log(2+|\tau|))$. Put $\sigma^g_T(\tau)=m(\tau)-\sum_n\frac{2\Lambda(n)g(\log n)}{\sqrt n}\cos(\tau\log n)$. Then for every real $\tau$
$$\tfrac12\sigma^g_T(\tau)=-\theta_{X'}'(\tau)-\mathrm{Re}\,M(\tfrac12-i\tau)+\sum_{k\ge1}\mathrm{Re}\,M(-2k-\tfrac12-i\tau).\tag{L}$$
*Proof.* Take real parts in (H) at $s=\tfrac12+i\tau$. Since $\xi(\tfrac12+i\tau)$ is real, $\xi'/\xi(\tfrac12+i\tau)\in i\mathbb R$. Also $\mathrm{Re}[\frac1s+\frac1{s-1}]=0$ on the line. With $\zeta'/\zeta=\xi'/\xi-\frac1s-\frac1{s-1}+\frac12\log\pi-\frac12\psi(\frac s2)$ this gives $-\mathrm{Re}\,\zeta'/\zeta(\tfrac12+i\tau)=\tfrac12m(\tau)$ identically. Rearrange. ∎

### 2.2 Lemma P (pairing lemma). PROVED

Let $G,H\in\mathcal D_T$, $h:=\widehat G\,\widehat H^\#$ (entire, of type $\le2T$, $h\in L^1(\mathbb R)$, $\int\log(2+|\tau|)|h|<\infty$), and $\mathsf H(w):=\int h(\tau)e^{-iw\tau}d\tau$. $\mathsf H$ is continuous, supported in $[-2T,2T]$, and $h(z)=\frac1{2\pi}\int\mathsf H(w)e^{iwz}dw$ for all $z\in\mathbb C$. Let $-g'$ be supported in $[2T,2T+\eta]$. For $t\in\mathbb C$:
- if $\mathrm{Im}\,t<0$: $\int h(\tau)M(i(t-\tau))d\tau=2\pi h(t)$ and $\int h(\tau)M(-i(\bar t-\tau))d\tau=2\pi h(\bar t)$;
- if $\mathrm{Im}\,t>0$: both integrals vanish;
- if $t=\gamma\in\mathbb R$: $\int h(\tau)\,\mathrm{Re}\,M(i(\gamma-\tau))\,d\tau=\pi h(\gamma)$.

Since $M(\bar z)=\overline{M(z)}$ ($g$ real), $\mathrm{Re}\,M(i(t-\tau))=\frac12[M(i(t-\tau))+M(-i(\bar t-\tau))]$ for real $\tau$. Hence, with $t_\rho=-i(\rho-\tfrac12)=\gamma-i\delta$,
$$\int h\,\mathrm{Re}\,M(\rho-\tfrac12-i\tau)\,d\tau=\begin{cases}\pi\,[h(t_\rho)+h(\bar t_\rho)]&\delta_\rho>0,\\ \pi\,h(\gamma_\rho)&\delta_\rho=0,\\ 0&\delta_\rho<0.\end{cases}$$
The pole ($\rho\to1$, $t=-\tfrac i2$) gives $\pi[h(-\tfrac i2)+h(\tfrac i2)]$. Each trivial zero ($t=i(2k+\tfrac12)$, $\mathrm{Im}\,t>0$) gives $0$.

*Proof.* Take $\mathrm{Im}\,t<0$. Then $\frac1{t-\tau}=i\int_0^\infty e^{-i(t-\tau)v}dv$, which converges absolutely. Fubini applies ($h\in L^1$) and gives
$$\int h(\tau)\frac{e^{-iu\tau}}{t-\tau}d\tau=i\int_0^\infty e^{-itv}\,\mathsf H(u-v)\,dv .$$
For $u\ge2T$ the support of $v\mapsto\mathsf H(u-v)$ lies in $[u-2T,u+2T]\subset[0,\infty)$. So the integral runs over $\mathbb R$ and equals $ie^{-itu}\int e^{itw}\mathsf H(w)dw=2\pi i\,e^{-itu}h(t)$. Multiply by $\frac1i e^{iut}(-g'(u))$ and integrate in $u$ ($\int-g'=1$) to get $2\pi h(t)$.
Now take $\mathrm{Im}\,t>0$. Then $\frac1{t-\tau}=-i\int_{-\infty}^0e^{-i(t-\tau)v}dv$, and $\mathsf H(u-v)\ne0$ forces $v\ge u-2T\ge0$. The intersection has measure zero, so the integral is $0$. The conjugate integrals are handled the same way with $v\mapsto-v$.
For real $\gamma$: $\mathrm{Re}\,M(i y)=\int(-g')\frac{\sin uy}{y}du$ and $\frac{\sin uy}{y}=\frac12\int_{-u}^{u}e^{ivy}dv$. Hence $\int h(\tau)\frac{\sin u(\gamma-\tau)}{\gamma-\tau}d\tau=\frac12\int_{-u}^ue^{iv\gamma}\mathsf H(v)dv=\pi h(\gamma)$, because $u\ge2T$. All interchanges are justified by $h\in L^1$ and the compact support of $-g'$. ∎

### 2.3 Theorem KZ. PROVED

For $F,H\in\mathcal D_T$, $X'=e^{2T+\eta}$ ($\eta>0$) and any cutoff as in Lemma H with $L_0=2T$:
$$\boxed{\;W_T(F,H)=-\frac1\pi\int_{\mathbb R}\widehat F(\tau)\,\overline{\widehat H(\tau)}\;\frac{d}{d\tau}\arg Z_{X'}(\tfrac12+i\tau)\,d\tau\;}\tag{KZ}$$
In particular, $F$ is a first-contact witness at $T_c$ if and only if $W_{T_c}\ge0$ and $\int\widehat F\,\overline{\widehat H}\,\theta'_{X'}\,d\tau=0$ for every $H\in\mathcal D_{T_c}$. On the diagonal, $\int|\widehat F|^2\,\theta'_{X'}=0$. The guess of R164_000 §1 is therefore exactly right, with $X'$ slightly above $X=e^{2T_c}$, and it is an **identity**: no $(1+o(1))$ enters.

*Proof.* Pair (L) with $h=\widehat F\widehat H^\#$ (on $\mathbb R$, $h=\widehat F\,\overline{\widehat H}$) and divide by $\pi$. Exchanging $\int$ with $\sum_\rho$ is justified because $|\mathrm{Re}\,M(\rho-\tfrac12-i\tau)|\ll(1+|\gamma-\tau|)^{-2}$ uniformly ($|\delta|<\tfrac12$), $\sum_\rho(1+|\gamma-\tau|)^{-2}\ll\log(2+|\tau|)$, and $\int\log(2+|\tau|)|h|<\infty$ on $\mathcal D_T$. Since $g=1$ on $[0,2T]$ and $\mathsf H$ is supported in $[-2T,2T]$ with $\mathsf H(\pm2T)=0$, $\frac1{2\pi}\int\sigma^g_Th=\frac1{2\pi}\int\sigma_Th=\mathfrak a_T(F,H)$. Lemma P then gives
$$\mathfrak a_T(F,H)=-\frac1\pi\int h\,\theta'_{X'}-\big[h(\tfrac i2)+h(-\tfrac i2)\big]\quad\text{and}\quad -\frac1\pi\int h\,\theta'_{X'}=\sum_\rho h(t_\rho).$$
For the second identity: the zeros with $\delta>0$ contribute $h(t_\rho)+h(\bar t_\rho)=h(t_\rho)+h(t_{1-\bar\rho})$, the on-line zeros contribute $h(\gamma)$, and the zeros with $\delta<0$ contribute $0$. Their partners have already been counted, so each zero is counted exactly once. Since $h(-\tfrac i2)=A(F)\overline{B(H)}$ and $h(\tfrac i2)=B(F)\overline{A(H)}$, the first identity is $\mathfrak a_T(F,H)+A\bar B+B\bar A=-\frac1\pi\int h\,\theta'_{X'}$, i.e. (KZ). The witness statement is R163_401 §4.6. ∎

---

## 3. Question 1 decided: (KZ) is wall E1

### 3.1 Theorem E1. PROVED

(i) The proof of Thm KZ gives, along the way,
$$-\frac1\pi\int h\,\theta'_{X'}\,d\tau=\sum_\rho h(t_\rho)\qquad(h=\widehat G\widehat H^\#,\ G,H\in\mathcal D_T),$$
which is (1.1). So (KZ) **is** the zero-side identity (1.1), composed with the window identity $W_T=\mathfrak a_T+$polar. No term of (KZ) is not a term of (1.1).
(ii) The left side depends neither on $\eta$ nor on the cutoff $g$ (subject to $g\equiv1$ on $[0,2T]$). So the hybrid parameter $X'$ and the GHK smoothing are invisible to $PW_T$-products. The only datum of $Z_{X'}$ that the pairing reads is its zero multiset, and that multiset is ζ's.
(iii) Consequently, row D $\iff$ for every $T$ the Toeplitz compression of the symbol $-\theta'_{X'(T)}/\pi$ to $PW_T$ is $\succeq0$. That is (1.1) $\ge0$ for all $T$, i.e. RH (R163_401 Thm 1.2). The symbol $-\theta'_{X'}$ has no pointwise sign even under RH: under RH, $-\theta'_{X'}=\sum_\gamma\mathrm{Re}\,M(i(\gamma-\tau))$, and $\mathrm{Re}\,M(iy)=\int(-g')\frac{\sin uy}{y}du$ changes sign. So positivity is only in the compressed sense, which is row D itself.
(iv) "$\int|\widehat F|^2\theta'_{X'}=0$ at the witness" is the statement $W_{T_c}(F)=0$, i.e. the existence of the witness (Rem 4.8a). Any contradiction drawn from it must use information not present in (KZ).

*Proof.* (i)–(ii) are Lemma P and the proof of Thm KZ. Lemma P's values are independent of $g$ beyond $\int(-g')=1$ and $\mathrm{supp}(-g')\subset[2T,\infty)$. (iii) follows from (i) and R163_401 Thm 1.2. For (iv), see R163_401 Rem 4.8a. ∎

*Interpretation (PROVED as a reading of Lemma P).* $-\theta'_{X'}/\pi=\frac1\pi\sum_\rho\mathrm{Re}\,M(i(t_\rho-\tau))$ is a GHK-regularised zero-counting density, a smoothing of $dN$ at scale $1/\log X'$. Its kernel $M$ has Fourier support at frequencies $u\ge2T$ only, which is outside the spectral window of $PW_T$-products. Hence type-$2T$ tests cannot distinguish the regularised density from the true one, and they see exactly the Weil sum. This is the mechanism of E1 for the hybrid cut. The cut at the window edge is precisely the scale at which the regularisation becomes invisible.

### 3.2 Corollary E1′ (the $\log|Z_X|$ and complex variants). PROVED (restatement)

Lemma P without the real part gives
$$\int h(\tau)\Big(-\frac{Z'_{X'}}{Z_{X'}}\Big)(\tfrac12+i\tau)\,d\tau=\pi\sum_{\delta_\rho=0}h(\gamma_\rho)+2\pi\sum_{\delta_\rho>0}h(t_\rho)\qquad(\text{on-line terms as principal values}).$$
The imaginary part is $\int h\cdot\frac{d}{d\tau}\log|Z_{X'}(\tfrac12+i\tau)|$. Up to the factor $\pm\pi$, it is the antisymmetric one-sided sum $\mathcal A(h)=\sum_{\delta_\rho>0}[h(t_\rho)-h(\bar t_\rho)]$.
- For parity-definite real $F$ (the witness, R163_401 2.4(ii)), $h=\widehat F\widehat F^\#$ is even with $h(\bar z)=\overline{h(z)}$. Then for each quartet $h(t)+h(-\bar t)=2\,\mathrm{Re}\,h(t)$, so $\mathcal A(h)=0$ and the complex pairing equals $\pi W_T(F)$. **The $\log|Z_X|$ variant is identically $0$ on the witness diagonal.**
- Off the diagonal, $\mathcal A(h)$ is the one-sided zero sum, i.e. the residue data of R163_801 (3.1). There, the zeros with $\delta>0$ are the poles of the tail $\mathcal T_X$ in the lower half-plane. Its vanishing for all $h$ is RH, and its content is (TC) itself (R163_1001 Thm C.3: E1). It is sign-free (W12) and defined for every member of the explicit-formula class (W3; §4).

*Proof.* As in Lemma P, keeping $J_1$ and $J_2$ separately. The quartet computation uses $h(-z)=h(z)$ and $h(\bar z)=\overline{h(z)}$. ∎

**Verdict on question 1. (KZ) is exactly the zero-side identity (1.1) rewritten, with ζ's zero sum replaced by the phase derivative of the hybrid zero factor. It is wall E1 and is declared DEAD, with proof (Thm E1). It carries no structure absent from $\sum_\rho(\widehat F\widehat F^\#)(t_\rho)$. Its complex/$\log|Z_X|$ companion carries the one-sided sum, which is R163_801 Cor 3.1, already E1 by R163_1001 Thm C.3.**

---

## 4. Question 3 and the falsifier battery

### 4.1 Proposition EB (Euler-blindness: the exact property of $Z_X$ used). PROVED

The proofs of Lemmas H, L, P and Thm KZ use exactly the following:
- (a) $-f'/f$ is a (generalised) Dirichlet series in some right half-plane. This is needed only to start the contour shift.
- (b) $f$ has a Hadamard factorisation with the stated archimedean factor and pole. Writing out the polar and trivial terms requires the FE.
- (c) $\mathrm{supp}(-g')\subset[2T,\infty)$.

The proofs **never** use the Euler product, the support of the coefficients on prime powers, the sign of the coefficients of $\log Z_X$, or the identity $-Z_X'/Z_X(\sigma)=\sum_n\Lambda(n)(1-g(\log n))n^{-\sigma}$ for $\sigma>1$ (the "Euler product above the window"). That identity is true by (H). But it is a statement in $\mathrm{Re}\,s>1$, and the pairing of Lemma P is evaluated by closing in $\tau$ using only the zero expansion of $Z_X$.
*Proof.* Inspection of §§1.2–2.3. ∎

So **what (KZ) loses when ζ is replaced by $f_t$ or $f_\chi$: nothing.** For $f\in\{f_t,f_\chi\}$, define $\widetilde P^f_{X'}$ and $Z^f_{X'}$ by (H), with $f$'s coefficients $b_f(\lambda)$ (atomic; frequencies $m/\sqrt M$ for $f_t$, conductor $7$ for $f_\chi$ with $m$ shifted by $\log 7$). Then (KZ) holds verbatim with $W^f_T$ and $\theta^f_{X'}$, and $f$'s zero sum appears in place of ζ's. The tail of $Z^f$ ($-Z^{f\prime}/Z^f$ in $\mathrm{Re}\,s$ large) has coefficients of mixed sign for both. The proposal (R164_000 §1, Q2) correctly identifies this as the only place where they differ from ζ. But (KZ) does not read it.

### 4.2 Falsifier table. PROVED (deletion and Λχ₂ contact values are record, PROVED-CITED)

| model | (KZ) holds? | what $Z_X$ is | separates? | why |
|---|---|---|---|---|
| **$f_t$** (R163_901) | yes, verbatim (Prop EB) | zeros of $f_t$ (off-line ones included); tail coefficients of mixed sign | no | for $N_0>e^{2T_c}$ same window, same witness, same $T_c$ (R163_1001 Prop A.1). (KZ) at the witness is the same equation, and $(\star_{\rm cell})$ fails for $f_t$ (Cor F) |
| **$f_\chi$** (R163_1001 Lem 1.1) | yes, verbatim | zeros of $f_\chi$, $\asymp T$ off-line (Lem 1.2, cited) | no | E1: the identity holds for every FE-member; any sign extracted from (KZ) alone would give RH for $f_\chi$, which is false |
| **$M_m$** | yes, with $Z^M=Z^\zeta\times$(regularised quartet factors), $\widetilde P^M$ = ζ's comb + the density $\beta_m$ | ζ's zeros + $4m$ added | no | (KZ) is (1.1) for $M_m$ (R163_801 Thm 5(c)) |
| **Λχ₂** (ζ's Γ and pole, χ₂ comb) | only with a correction: there is no matching zero side (R163_401 §6). (H) holds for $L(s,\chi_2)$ with its own Γ. The model's symbol differs from $L(s,\chi_2)$'s by an explicit archimedean+polar term $\Delta$, so (KZ) becomes $W^{\Lambda\chi_2}=-\frac1\pi\int h\,\theta'^{\chi_2}_{X'}+\Delta(h)$ | zeros of $L(s,\chi_2)$ | no | the contact $T_c\le0.38$ (record) is produced by $\Delta$, which is non-zero-side, not by $Z_X$ |
| **deletion $\Lambda\mathbf 1_{n\ge5}$** | yes, with a correction: $D:=\zeta\exp(\sum_{n<5}\Lambda(n)n^{-s}/\log n)$ has ζ's zeros. (H) for $D$ gives $Z^D_{X'}=Z^\zeta_{X'}$ **identically** ($X'>4$), $\widetilde P^D=\widetilde P^\zeta/\exp(\cdots)$. $W^D_T=W_T-\sum_{n<5}v_n\cdot(\text{comb at }\log n)$, a finite comb, not a zero term | **the same as ζ's** | no | Prop D below |
| **$\zeta_\theta$** | yes, with its own archimedean factor (FE about $\frac{1+\theta}2$) | zeros $\theta+(1-\theta)\rho$; tail coefficients $\ge0$ | no | Prop θ below |

**Proposition D (identical $Z_X$, opposite signs). PROVED** (the deletion bound is record). For $X'>4$, $Z^D_{X'}=Z^\zeta_{X'}$ as functions on $\mathbb C$. This holds because $-D'/D=-\zeta'/\zeta-\sum_{n<5}\Lambda(n)n^{-s}$, the added term is entire, and (H) for $D$ has the same zero sum and the same $M(1-s)$, $M(-2k-s)$ terms. Yet $\lambda^{\rm W}(D)<0$ for $T\le0.4608$ (grid §4, record), while $\lambda^{\rm W}_T(\zeta)>0$ for $T\le\tfrac12\log5$ (R163_401 §2.1). Hence **no property of $Z_X$ alone determines the sign of the window form.** Any L1 mechanism has to read the coupling of $Z_X$ with $\widetilde P_X$, i.e. the window. This is the requirement R164_000 §1 Q3 imposes. It is proved here, not assumed.

**Proposition θ (positive tail does not localise zeros). PROVED.** $-\zeta_\theta'/\zeta_\theta(s)=\sum_n\frac{\Lambda(n)}{1-\theta}n^{\theta/(1-\theta)}\,(n^{1/(1-\theta)})^{-s}$ has nonnegative coefficients. Applying (H) to $\zeta_\theta$, its tail $-Z^{\theta\prime}_{X'}/Z^\theta_{X'}(\sigma)$ for $\sigma$ large is a Dirichlet series with coefficients $\ge0$ supported on frequencies $\ge X'^{1-\eta'}$. It is therefore completely monotone in $\sigma$ (Bernstein). The zeros of $\zeta_\theta$ are $\theta+(1-\theta)\rho$. Hardy's theorem (unconditional, CITED) gives infinitely many $\rho$ on $\mathrm{Re}=\tfrac12$, hence infinitely many zeros of $\zeta_\theta$ on $\mathrm{Re}\,s=\frac{1+\theta}2\ne\tfrac12$. So candidate (c) of R164_000 §1, read as "positive Laplace tail ⟹ zeros on $\mathrm{Re}=\tfrac12$", is false. *Caveat (stated honestly):* $\zeta_\theta$ satisfies an FE about $\frac{1+\theta}2$, not about $\tfrac12$, and its window is not ζ's. So it kills only the *tail-only* reading. The coupled reading (positive tail + ζ's window + ζ's FE) is O164.101 and is OPEN.

### 4.3 What survives for L1. ARGUED (reading; no new claim)

(KZ) is dead, but L1 is not. By Prop EB, the only thing that distinguishes ζ from $f_t$/$f_\chi$ in the hybrid picture is the tail sign in $\mathrm{Re}\,s>1$, and (KZ) does not read it. By Prop D, the window alone with the same $Z_X$ gives either sign. By Prop θ, the tail sign alone does not localise zeros. A surviving L1 mechanism must therefore be **non-linear in $Z_X$** (S2) and must couple three things at once: the tail sign in $\mathrm{Re}\,s>1$, ζ's FE about $\tfrac12$, and ζ's exact window $(\Lambda(n))_{n<X}$. Transporting the tail sign from $\mathrm{Re}\,s>1$ to the cone $\mathrm{Im}\,x\in(-\tfrac12,0)$ by any linear pairing with $PW_{T_c}$-products reduces to Lemma P, i.e. to the zero sum (Thm E1). The decisive test is O164.101: a Beurling-positive system with ζ's window and FE and an off-line zero in a cone would kill L1. Its nonexistence would be a genuine class lemma (S11). This is R164_102's question, not settled here.

---

## 5. Ledger

| statement | label | depends on |
|---|---|---|
| GHK Thm 1 (form, error, uniformity) | PROVED-CITED, from memory, page-level check pending | — |
| origin of GHK's error terms | ARGUED | GHK proof as recalled |
| Lemma H (exact hybrid identity) | PROVED | contour shift, $N(R+1)-N(R)\ll\log R$ |
| Lemma L (window symbol = $-2\theta'_{X'}$ + explicit) | PROVED | Lemma H, $\Xi$ real |
| Lemma P (pairing) | PROVED | Paley–Wiener support of $\mathsf H$, Fubini |
| Thm KZ (the identity, and the witness form $\int\widehat F\overline{\widehat H}\theta'_{X'}=0$) | PROVED | L, P, R163_401 §4.6 |
| Thm E1 ((KZ) = (1.1); cutoff/$X'$-independence; row D ⟺ compressed $-\theta'\succeq0$) | PROVED | P, R163_401 Thm 1.2 |
| Cor E1′ ($\log|Z_X|$ / complex: zero on the witness diagonal; off-diagonal = R163_801 one-sided sum) | PROVED (restatement, E1) | P, R163_1001 Thm C.3 |
| Prop EB (Euler-blindness; exact property used) | PROVED | inspection |
| Prop D (deletion: same $Z_X$, different sign) | PROVED; deletion value PROVED-CITED (record) | H, grid §4 |
| Prop θ (positive tail, zeros off ½) | PROVED (Hardy CITED); kills only the tail-only reading | H |
| falsifier table §4.2 | PROVED; Λχ₂/deletion contact values record | EB, D, θ |
| §4.3 surviving form of L1 | ARGUED | — |
| O164.101 | OPEN | — |
| $(\star_{\rm cell})$, (TC), row D | OPEN | — |

**For the grid (editor, L3).** 4F/7F: add the DEAD route "R164_101 hybrid cut (KZ)", killer E1 (Thm E1), with secondary walls W3 (Prop EB) and W12. Add residue O164.101 to 4F. Add to §4 the row "**deletion ≡ ζ at the level of $Z_X$**" (Prop D). It refutes "any property of the zero factor $Z_X$ decides the sign".
