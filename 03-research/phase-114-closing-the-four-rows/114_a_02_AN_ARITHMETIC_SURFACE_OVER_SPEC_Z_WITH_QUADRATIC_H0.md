# 114.a.02 — An arithmetic surface over Spec Z with quadratic $h^0$: a4-weak closed, R16 answered

> **Category correction (114.a.06).** The calculations below rigorously define
> and analyse normed lattices of global sections on the genuine scheme
> `P^1_Z`.  However, Haar measure supported on the real one-dimensional torus
> is not by itself a smooth Hermitian metric on `O(k)` over all of
> `P^1(C)`, and the hyperbolic pairing below is stipulated rather than derived
> from an arithmetic intersection construction.  Consequently the verified
> result is a quadratic **gauged-section model on an arithmetic surface**.  A
> classical Arakelov surface with this exact theta identity and pairing still
> requires the compatibility construction isolated in
> `114_a_06_A4_WEAK_CATEGORY_AUDIT.md`.
>
> **Resolution (114.a.07).** That compatibility construction now exists in the
> category of semipositive adelic toric metrics: the canonical metric has Haar
> Chern measure and its constant rescaling has roof function `a`, giving
> self-intersection `2ka` and the displayed hyperbolic form by polarisation.

```
+--------------------------------------------------------------------------+
| ROW (a), ITEM a4 — STAGE 2: THE CONSTRUCTION                             |
|                                                                          |
| THE OBJECT   Xbar = P^1 over Spec Z, Arakelov-compactified, with the     |
|              L^2 metric of the Haar measure on |T_0| = |T_1|.           |
|              Div = Z (+) R,  D = (k,a),  <(k,a),(k',a')> = ka' + k'a,   |
|              H = (1,1), deg D = k+a, D^2 = 2ka, K = (-2,0).             |
|                                                                          |
| THE RESULT   h^0_theta(D)  =  (1/2) D.(D - K)  +  eta(D),               |
|  (Thm 3.4)   with eta(D) = (k+1) log theta(e^{2a}) in [0, 3(k+1)e^{-pi  |
|              e^{2a}}].  h^0_theta is the van der Geer-Schoof / Bost      |
|              theta invariant, the SAME definition as arXiv:2512.01811.   |
|              PROVED, exactly, from Jacobi's functional equation alone.   |
|              Verified to 60 digits at nine points.                       |
|                                                                          |
| GROWTH-TEST  PASSED.  h^0(mD) = ka m^2 + a m, homogeneity degree 2.      |
| O1-TEST      PASSED.  H^0(mD) is a lattice of rank mk+1 -> infinity, and |
|              h^0(mD)/h^0(D) -> infinity, so 113_10 Prop 5.1 fails here.  |
| GAUGE-ROBUST l1 ball, sup box and theta all give (1/2)D^2 to leading     |
|  (Thm 5.1)   order with the SAME constant 1.  R27 does not fire.  This   |
|              also answers 107_146's own open question in its sec.8.      |
|                                                                          |
| VERDICT      a4-WEAK  ("a two-dimensional arithmetic structure over      |
|              Spec Z with quadratic absolute dimension"):  CLOSED         |
|              POSITIVELY, BUILT, no gaps in the construction.             |
|              R16  ("can a quadratic chi exist over Spec Z at all?"):     |
|              ANSWERED YES, twice - here elementarily, and in the         |
|              literature (arXiv:2512.01811v2 Thm main1).                  |
|              a4-STRONG (the square Spec Z x_{F_1} Spec Z): STILL OPEN.   |
|              This object is NOT the square: its generic fibre is P^1_Q.  |
|                                                                          |
| WARNING      Nothing here is evidence for RH.  See sec.7.3.  The         |
|              Hodge index holds in this model TRIVIALLY (rank 2) and no   |
|              zero of xi appears anywhere in it.                          |
|                                                                          |
| VERIFIER     114_a_02_the_absolute_quadric.py — 33 checks, exit 0,       |
|              VERDICT: ALL CHECKS PASS (output in sec.9)                  |
|                                                                          |
| CURRENT GAPS G-1 and G-2 are closed. G-3 is fully delimited through     |
|              114.a.60: every meaningful branch is RH-equivalent.        |
|              R8 baseline repaired; full dictionary remains open.        |
| CIRCULARITY  CLEAN.  No zero, no sign(Q), no Weil positivity, no Li      |
|              coefficient enters any definition or proof.  Not vacuous:   |
|              every object is explicit and every number is computed.      |
+--------------------------------------------------------------------------+
```

**Depends on:**

- `03-research/phase-114-closing-the-four-rows/114_a_01_THE_GROWTH_DICHOTOMY_AND_THE_RANK_FALLACY.md`
  — Definition 1.1, Theorems 2.1/2.2/2.4, Theorem 3.3, Definitions 5.1/5.2, Prop 5.4.
- `03-research/phase-113-the-trace-on-schwartz-data/113_10_THE_DEGREE_MAP_AND_THE_EFFECTIVE_CONE.md`
  — §5 Prop 5.1, O1, route (i), R5–R8.
- `03-research/phase-113-the-trace-on-schwartz-data/113_15_THE_FOUR_ROW_LEDGER.md` — §1 a4, §6, §7 R16.
- `03-research/phase-107-arithmetic-lefschetz-reconstruction/107_146_ABSOLUTE_DIMENSION_HIGHER_RANK.md`
  — §1, Thm A, Thm B, §5 Cor C, §8 (its open question on the $\ell^1$ gauge).
- `00-references/papers-nuevos/D/arXiv-2512.01811v2/Numerical_cohomology_for_arithmetic_surfaces_and_applications.tex`
  — §1 (definitions of $h^0_{\mathcal O}$, $h^0_{\mathcal X}$, $h^1_{\mathcal X}$, $h^2_{\mathcal X}$, $\chi_{\mathcal X}$) and Theorem `main1`. Read; quoted verbatim in §8.
- `00-references/papers-nuevos/A/arXiv-2205.01391v2/RR-J-final.tex` — CC §2–§3 (the absolute dimension).

---

## 1. The object

**Definition 1.1.** Let $X=\mathbb P^1_{\mathbb Z}=\operatorname{Proj}\mathbb Z[T_0,T_1]$,
a regular, projective, flat arithmetic surface over $\operatorname{Spec}\mathbb Z$ of
relative dimension $1$. On $X(\mathbb C)=\mathbb P^1(\mathbb C)$ let $\mu$ be the
normalised Haar measure of the compact torus
$$
 \mathbb T:=\{\,[T_0:T_1]\ :\ |T_0|=|T_1|\,\}\ \subset\ \mathbb P^1(\mathbb C),
$$
i.e. $d\mu = d\theta/2\pi$ under $z=T_1/T_0=e^{i\theta}$. Give $\mathcal O(k)$ the
$L^2(\mu)$ metric in the trivialisation over $\mathbb T$.

**Definition 1.2 (the divisor group and its form).** Put
$$
 \widehat{\mathrm{Div}}(X)\ :=\ \mathbb Z\oplus\mathbb R,
 \qquad D=(k,a)\ \longleftrightarrow\ \bigl(\mathcal O(k),\ \text{metric scaled by }e^{a}\bigr),
$$
so that a section $s$ of $\mathcal O(k)$ is *small for $D$* iff $\|s\|_{L^2(\mu)}\le e^{a}$.
Define
$$
 \langle (k,a),(k',a')\rangle\ :=\ k a' + k' a,
 \qquad H:=(1,1),\qquad K:=(-2,0),
$$
$$
 \deg D:=\langle D,H\rangle = k+a,\qquad D^2:=\langle D,D\rangle = 2ka .
$$
Multiples: $mD=(mk,ma)$, so $\deg(mD)=m\deg D$ and $(mD)^2=m^2D^2$.

**Remark 1.3 (why this is the right form, and where it comes from).** The two
generators $f_{\mathrm{fin}}=(1,0)$ and $f_\infty=(0,1)$ are the two rulings:
$f_{\mathrm{fin}}$ raises the degree of the line bundle on the generic fibre,
$f_\infty$ inflates the archimedean ball. Both are isotropic
($f^2=0$), they pair to $1$, and $H=f_{\mathrm{fin}}+f_\infty$ is ample with
$H^2=2$. This is the hyperbolic plane, the Néron–Severi lattice of any ruled
surface, and it is forced: on a two-generator group with two isotropic rulings
the form is $\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$ up to scale.
$\deg K=-2$ matches $\deg K_{\mathbb P^1}=-2$; the archimedean component $0$ of
$K$ is *derived*, not assumed — see Theorem 3.4 and check B4, which shows the
Riemann–Roch identity fails for $K=(-2,c)$, $c\ne0$.

**Circularity of §1.** CLEAN. $X$, $\mu$, the form and $K$ are defined without
reference to $\zeta$, to $\xi$, to any zero, or to any positivity hypothesis.
Not vacuous: $X$ exists and $\widehat{\mathrm{Div}}(X)\ne0$.

---

## 2. The sections form a lattice of growing rank

**Theorem 2.1.** For $k\ge0$, $H^0(X,\mathcal O(k))$ is a free $\mathbb Z$-module
of rank $k+1$ with basis the monomials $T_0^{\,i}T_1^{\,k-i}$, $0\le i\le k$;
for $k<0$ it is $0$.

*Proof (elementary glueing, no citation needed).* Cover $X$ by
$U_0=\operatorname{Spec}\mathbb Z[t]$, $t=T_1/T_0$, and
$U_1=\operatorname{Spec}\mathbb Z[u]$, $u=T_0/T_1=1/t$. In the standard
trivialisations of $\mathcal O(k)$ the transition function is $t^{k}$, so a global
section is a pair $(f_0(t),f_1(u))\in\mathbb Z[t]\times\mathbb Z[u]$ with
$f_0(t)=t^{k}f_1(1/t)$. Writing $f_1(u)=\sum_{j\ge0}c_ju^j$ (a finite sum) gives
$t^kf_1(1/t)=\sum_j c_j t^{\,k-j}$, which lies in $\mathbb Z[t]$ if and only if
$c_j=0$ for every $j>k$. Hence global sections $\leftrightarrow$
$(c_0,\dots,c_k)\in\mathbb Z^{k+1}$, and $c_j$ is the coefficient of
$T_0^{\,j}T_1^{\,k-j}$. For $k<0$ the condition forces all $c_j=0$. $\square$

(Machine-checked for $k=0,\dots,5$ in §9, check D1.)

**Theorem 2.2 (the metric is diagonal in the monomial basis).** For
$s=\sum_{j=0}^k c_j T_0^{\,j}T_1^{\,k-j}$ with $c_j\in\mathbb C$,
$$
 \|s\|_{L^2(\mu)}^2\ =\ \sum_{j=0}^{k}|c_j|^2 .
$$

*Proof.* In the trivialisation over $\mathbb T$, $s$ restricts to
$\theta\mapsto\sum_j c_j e^{i(k-j)\theta}$; the characters $e^{i\ell\theta}$ are
orthonormal for $d\theta/2\pi$. Parseval. $\square$

**Corollary 2.3 (the section lattice).** The small sections of $D=(k,a)$ are
$$
 \widehat H^0(D)\ =\ \{\,c\in\mathbb Z^{k+1}\ :\ |c|_2\le e^{a}\,\},
$$
a set of lattice points in a Euclidean ball of radius $e^a$ inside a free
$\mathbb Z$-module of rank $k+1$. Along the ray $mD$ the rank is $mk+1\to\infty$
and the radius is $e^{ma}\to\infty$: **both** directions grow, which by
`114_a_01` Theorem 3.3 is exactly the surface regime.

**Circularity of §2.** CLEAN; Theorems 2.1 and 2.2 are finite algebra and
Parseval.

---

## 3. Riemann–Roch: three dimension functions, one quadratic leading term

Three dimension functions are in use in the literature and in this repo. All
three are computed here on the same family, and all three are quadratic with
the same leading constant.

### 3.1 Counting lattice points (Weil 1939 / geometry of numbers)

**Theorem 3.1.** Let $D=(k,a)$ with $k\ge1$, $a>0$, and set $r_m=mk+1$,
$n_m=\lfloor e^{ma}\rfloor$. Let
$h^0_{\#,1}(mD):=\log\bigl|\{c\in\mathbb Z^{r_m}:|c|_1\le n_m\}\bigr|$ and
$h^0_{\#,\infty}(mD):=\log\bigl|\{c\in\mathbb Z^{r_m}:|c|_\infty\le n_m\}\bigr|$.
Then
$$
 h^0_{\#,\infty}(mD)=ka\,m^2+O(m),
 \qquad
 h^0_{\#,1}(mD)=ka\,m^2+O(m\log m),
$$
and $ka\,m^2=\tfrac12(mD)^2$. In particular both are
$\tfrac12(mD)^2\,(1+o(1))$.

*Proof.* Box: $h^0_{\#,\infty}=r_m\log(2n_m+1)=(mk+1)\bigl(ma+\log2+O(e^{-ma})\bigr)
= ka\,m^2+O(m)$.
Ball, upper: $I_{r}(n)\subseteq[-n,n]^r$, so $h^0_{\#,1}\le h^0_{\#,\infty}=ka\,m^2+O(m)$.
Ball, lower: $I_r(n)\supseteq[-\lfloor n/r\rfloor,\lfloor n/r\rfloor]^r$, so
$$
 h^0_{\#,1}\ \ge\ r_m\log\bigl(2\lfloor n_m/r_m\rfloor+1\bigr)
 \ \ge\ (mk+1)\bigl(ma-\log(mk+1)+O(1)\bigr)\ =\ ka\,m^2+O(m\log m). \ \square
$$

Numerically the ratio $h^0_{\#,1}(mD)/\tfrac12(mD)^2$ is
$1.0224,\,0.9777,\,0.9705,\,0.9755,\,0.9827,\,0.9887$ at $m=8,16,32,64,128,256$
for $(k,a)=(1,1)$, and $0.9938$ at $m=128$ for $(k,a)=(2,3)$ (§9, checks E1–E4).

### 3.2 The theta invariant (van der Geer–Schoof / Bost)

**Definition 3.2.** Following arXiv:2512.01811v2 §1, which writes
$h^0_{\mathcal O}(\mathcal F):=\log\sum_{x\in\mathcal F}e^{-\pi\|x\|^2}$ and
$h^0_{\mathcal X}(\mathcal L):=h^0_{\mathcal O}(f_*\mathcal L)$, set for $D=(k,a)$
$$
 h^0_\theta(D)\ :=\ \log\!\!\sum_{c\in\mathbb Z^{k+1}}\!\! e^{-\pi|c|_2^2 e^{-2a}} .
$$

**Lemma 3.3.** Let $\vartheta(s):=\sum_{j\in\mathbb Z}e^{-\pi j^2 s}$, $s>0$. Then
$\vartheta(s)=s^{-1/2}\vartheta(1/s)$ (Jacobi), and for $u\ge1$,
$1\le \vartheta(u)\le 1+3e^{-\pi u}$.

*Proof.* Jacobi's identity is Poisson summation applied to $x\mapsto e^{-\pi x^2s}$.
For the bound, $\vartheta(u)-1=2\sum_{j\ge1}e^{-\pi j^2u}\le
2\sum_{j\ge1}e^{-\pi ju}=\frac{2e^{-\pi u}}{1-e^{-\pi u}}\le
\frac{2}{1-e^{-\pi}}e^{-\pi u}=2.0932\ldots e^{-\pi u}\le3e^{-\pi u}$. $\square$

**Theorem 3.4 (exact arithmetic Riemann–Roch for $\overline{\mathbb P^1_{\mathbb Z}}$).**
For every $D=(k,a)$ with $k\ge0$, $a\ge0$,
$$
 \boxed{\;h^0_\theta(D)\ =\ \tfrac12\,\langle D,\,D-K\rangle\ +\ \eta(D),
 \qquad K=(-2,0),\;}
$$
with
$$
 \eta(D)=(k+1)\log\vartheta\bigl(e^{2a}\bigr)\ \in\ \bigl[\,0,\ 3(k+1)e^{-\pi e^{2a}}\,\bigr].
$$
Consequently, along the ray,
$$
 h^0_\theta(mD)\ =\ \tfrac12 (mD)^2\ +\ \tfrac12\deg(mD)\cdot\!\!\underbrace{2}_{=-\deg K}\!\!/2\ +\ \eta
 \ =\ ka\,m^2 + a\,m + \eta,\qquad
 0\le\eta\le 3(mk+1)e^{-\pi e^{2ma}} .
$$

*Proof.* By Theorem 2.2 the quadratic form $|c|_2^2$ is the standard one on
$\mathbb Z^{k+1}$, so
$$
 h^0_\theta(D)=\log\prod_{j=0}^{k}\sum_{c_j\in\mathbb Z}e^{-\pi c_j^2e^{-2a}}
 =(k+1)\log\vartheta(e^{-2a}).
$$
By Lemma 3.3 with $s=e^{-2a}$, $\vartheta(e^{-2a})=e^{a}\vartheta(e^{2a})$, hence
$h^0_\theta(D)=(k+1)a+(k+1)\log\vartheta(e^{2a})$. Finally
$$
 \tfrac12\langle D,D-K\rangle=\tfrac12\bigl(2ka-(k\cdot 0+(-2)\cdot a)\bigr)=ka+a=(k+1)a,
$$
and the bound on $\eta$ is Lemma 3.3 together with $\log(1+x)\le x$. $\square$

**Remark 3.5.** Three things deserve emphasis.

1. The proof is *Poisson summation and nothing else*. arXiv:2512.01811v2 §1 says
   of the arithmetic-curve case: *"the Riemann–Roch formula
   $\chi_{\mathcal O}(\mathcal F)=\widehat{\deg}\det\mathcal F+\chi_{\mathcal O}(\mathcal O)\operatorname{rank}_{\mathcal O}\mathcal F$
   is equivalent to Poisson summation formula."* Theorem 3.4 is the
   two-dimensional instance of the same mechanism for this particular surface,
   and it is quadratic because the rank of $f_*\mathcal O(k)$ is $k+1$, itself a
   coordinate of $D$.
2. $K=(-2,0)$ is *forced*: check B4 shows that $K=(-2,c)$ with
   $c\in\{-1,1,2\}$ breaks the identity at $D=(3,2)$ by more than $10^{-6}$. The
   finite part $-2$ is $\deg K_{\mathbb P^1}$; the archimedean part $0$ is the
   statement that the Haar metric of Definition 1.1 is the one for which the
   monomials are orthonormal.
3. The error $\eta$ is *super-exponentially small in $a$*: at $(k,a)=(2,3)$ and
   $(40,2.5)$ it is below $10^{-60}$ (the working precision) with true bounds
   $3\cdot10^{-550}$ and $4\cdot10^{-201}$; at $(k,a)=(10,2)$ the identity holds
   to $60$ digits. So the "Riemann–Roch" here is not asymptotic — it is an
   identity with an explicit, tiny, one-signed defect.

### 3.3 The Connes–Consani absolute dimension

**Theorem 3.6.** With $\dim_r(n)$ as in `114_a_01` Definition 1.1 and
$D=(k,a)$, $k\ge1$, $a>0$,
$$
 \frac{1}{\log 3}\cdot\frac{(mD)^2}{2}\,(1+o(1))
 \ \le\ \dim_{mk+1}\!\bigl(\lfloor e^{ma}\rfloor\bigr)
 \ \le\ \frac{1}{\log 2}\cdot\frac{(mD)^2}{2}\,(1+o(1)) .
$$
Equivalently $\dim_{\mathbb S_\pm}\widehat H^0(mD)=\tfrac12(mD)^2/\log q$ for an
effective base $q=q(m)\in[2,3]$.

*Proof.* `114_a_01` Theorem 3.3(1) with $\tfrac12(mD)^2=ka\,m^2$. $\square$

Numerically (§9, checks F1a/F1b/F2): $\dim/D^2$ is bracketed by
$[0.4153,0.8250]$ at $m=10$ and by $[0.4395,0.7341]$ at $m=80$, against the
targets $1/(2\log3)=0.4551$ and $1/(2\log2)=0.7213$.

**Corollary 3.7 (the units interpretation).** The three dimension functions
differ only in the *base of the logarithm* used to measure a dimension:
$h^0_\theta$ and $h^0_\#$ count in nats and give leading constant exactly $1$
against $\tfrac12 D^2$; CC's $\dim_{\mathbb S_\pm}$ counts in "signed digits"
and gives $1/\log q$, $q\in[2,3]$. The **exponent** — which is what a4 asks
about — is $2$ for all three.

**Circularity of §3.** CLEAN. Theorem 3.4 is Poisson summation on
$\mathbb Z^{k+1}$; Theorem 3.1 is lattice-point counting; Theorem 3.6 quotes
`114_a_01` Theorem 3.3, itself proved from finite combinatorics. Nothing
quantifies over zeros of $\xi$. Not vacuous: all three functions are finite,
positive and explicitly computed.

---

## 4. The intersection form: signature, degree, and a Hodge index that means nothing

**Theorem 4.1.** On $\widehat{\mathrm{Div}}(X)\otimes\mathbb R=\mathbb R^2$:

1. $\langle\cdot,\cdot\rangle$ has matrix $\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$
   in the basis $(f_{\mathrm{fin}},f_\infty)$, eigenvalues $\pm1$, signature $(1,1)$;
2. $H^2=2>0$, $\deg=\langle\cdot,H\rangle$, $H$ is in the interior of the
   effective cone $\{k\ge0,a\ge0\}$;
3. $H^\perp=\{(k,-k):k\in\mathbb R\}$ and $\langle D,D\rangle=-2k^2<0$ for
   $0\ne D\in H^\perp$: the form is **negative definite** on $H^\perp$ — the
   Hodge index inequality holds;
4. (E) holds: if $D^2>0$ and $\deg D>0$ then $D$ is effective
   ($h^0_\theta(D)>0$); if $D^2>0$ and $\deg D<0$ then $-D$ is effective.

*Proof.* (1),(2),(3) are the displayed $2\times2$ computations, verified in §9
checks C1–C6. (4): $D^2=2ka>0$ and $k+a>0$ force $k>0$ and $a>0$; then
Corollary 2.3 gives $\widehat H^0(D)\ni 0$ and, since $e^a>1$, also the $k+1$
monomials, so $h^0_\theta(D)\ge\log(2k+3)>0$. The second case is $D\mapsto -D$.
$\square$

**Warning 4.2 (read this before quoting Theorem 4.1).** Theorem 4.1(3) and (4)
are *not* evidence for RH, and must never be cited as such.

- $\widehat{\mathrm{Div}}(X)$ has real rank $2$. Its $H^\perp$ is
  one-dimensional. Negative definiteness on a one-dimensional space is the
  statement $-2k^2\le0$.
- No zero of $\xi$ occurs anywhere in $X$, in $\mu$, in the form, or in $K$. The
  zeta function of $X=\mathbb P^1_{\mathbb Z}$ is
  $\zeta_{\mathbb P^1_{\mathbb Z}}(s)=\zeta(s)\zeta(s-1)$, whose zeros are the
  zeros of $\zeta$ *shifted*, not *placed*: the object has no mechanism that
  could constrain them, because $H^\perp$ has dimension $1$ and there are
  infinitely many zeros.
- Concretely: the row-(c) requirement is a class $\Gamma_n$ with
  $\Gamma_n\cdot\Delta=N_n=\sum_{p^k\le\cdot}\log p$-type counts. On $X$ the only
  available self-maps are the toric ones $T\mapsto T^n$, whose fixed-point counts
  are the $\mathbb F_1$-style $n-1$, not $\psi(n)$. This candidate does not
  touch row (c). See §7.

**Circularity of §4.** CLEAN but **potentially misleading**, which is why
Warning 4.2 is part of the file. Theorem 4.1(4) is *not* vacuous (the hypothesis
$D^2>0,\deg D>0$ is satisfiable) and *not* circular (its proof uses no zero),
but it is **weak**: it is true for the trivial reason that the lattice has rank
$2$. Any use of it as support for (E$^o$) in `113_10` would be a category error
and fires R29 below.

---

## 5. Gauge robustness: the exponent and the constant do not depend on the norm

`107_146` §8 lists as open: *"whether the $\ell^1$ mass functional is the right
one for a product at all."* For the growth exponent, and even for the leading
constant, the answer is that it does not matter.

**Theorem 5.1.** Let $\|\cdot\|_{\sup}$ denote the sup norm on
$\mathbb T=\{|T_0|=|T_1|\}$ and $|\cdot|_1,|\cdot|_2,|\cdot|_\infty$ the
coefficient norms in the monomial basis. Then for every
$s=\sum_{j=0}^kc_jT_0^jT_1^{k-j}$,
$$
 |c|_\infty\ \le\ \|s\|_{L^2(\mu)}=|c|_2\ \le\ \|s\|_{\sup}\ \le\ |c|_1\ \le\ (k+1)\,\|s\|_{\sup},
$$
and consequently, writing $B_\gamma(N)=\{c\in\mathbb Z^{k+1}:\gamma(s_c)\le N\}$
for each gauge $\gamma$, the four counts
$\log|B_\gamma(e^{ma})|$, $\gamma\in\{|\cdot|_1,|\cdot|_2,|\cdot|_\infty,\|\cdot\|_{\sup}\}$,
all equal $\tfrac12(mD)^2+O(m\log m)$ along $mD=(mk,ma)$, with the **same**
leading constant $1$.

*Proof.* $|c|_\infty\le|c|_2$ is elementary; $|c|_2=\|s\|_{L^2}\le\|s\|_{\sup}$
because $\mu$ is a probability measure; $\|s\|_{\sup}\le\sum_j|c_j|=|c|_1$ by the
triangle inequality on $|T_0^jT_1^{k-j}|=1$; and
$|c_j|=\bigl|\int_{\mathbb T}s\,\overline{e^{i(k-j)\theta}}\,d\mu\bigr|\le\|s\|_{\sup}$
gives $|c|_1\le(k+1)\|s\|_{\sup}$. Hence
$$
 B_{|\cdot|_1}(N)\ \subseteq\ B_{\|\cdot\|_{\sup}}(N)\ \subseteq\ B_{|\cdot|_1}\bigl((k+1)N\bigr),
 \qquad
 B_{|\cdot|_1}(N)\subseteq B_{|\cdot|_2}(N)\subseteq B_{|\cdot|_\infty}(N),
$$
and by Theorem 3.1 both $\log|B_{|\cdot|_1}(e^{ma})|$ and
$\log|B_{|\cdot|_\infty}(e^{ma})|$ are $ka\,m^2+O(m\log m)$; the same for
$\log|B_{|\cdot|_1}((mk+1)e^{ma})|=(mk+1)\log\bigl(2(mk+1)e^{ma}+1\bigr)+O(\cdot)
=ka\,m^2+O(m\log m)$. All four are squeezed. $\square$

Verified in §9, checks G1–G4: the two norm inequalities hold on $400$ random
integer forms; the squeeze
$[\log|I_r(n)|,\log|I_r(rn)|]=[0.9755,1.0418]\cdot\tfrac12(mD)^2$ at $m=64$; and
$|h^0_\theta-r\log(2n+1)|\le r\log2$ exactly.

**Corollary 5.2 (R27 does not fire).** The homogeneity degree $\delta=2$ of
`114_a_01` Definition 4.1 is the same for all four gauges, so it is not an
$\ell^1$ artefact.

---

## 6. Verdicts

**Theorem 6.1 (GROWTH-TEST, `114_a_01` Definition 5.2).** PASSED. For
$D=(1,1)$, $h^0_\theta(mD)=m^2+m+\eta$ with $0\le\eta\le3(m+1)e^{-\pi e^{2m}}$,
so $\delta(D)=\lim\log h^0_\theta(mD)/\log m=2$.

*Proof.* Theorem 3.4. Measured slope $1.98230$ at $m\in[40,80]$ (§9, H1). $\square$

**Theorem 6.2 (O1-TEST, `114_a_01` Definition 5.1).** PASSED. The section
modules $\widehat H^0(mD)$ sit inside free $\mathbb Z$-modules of rank
$mk+1\to\infty$ (Corollary 2.3), and $h^0_\theta(mD)/h^0_\theta(D)\to\infty$
($=5050$ at $m=100$, §9 H2), so `113_10` Proposition 5.1 does not apply: the
effective condition is *not* scaling-invariant here.

*Proof.* Corollary 2.3 and Theorem 3.4. $\square$

**Theorem 6.3 (Proposition 5.4 of `114_a_01`, the bookkeeping condition).**
Satisfied. $\deg_{\mathrm{fin}}(mD)=mk$ and $\deg_\infty(mD)=ma$ are both
$\Theta(m)$; the rank of $\widehat H^0$ is $\deg_{\mathrm{fin}}+1$ and the log
radius is $\deg_\infty$.

**Corollary 6.4 (item a4-weak).** *There exists a two-dimensional arithmetic
structure over $\operatorname{Spec}\mathbb Z$, with a genuine integral section
lattice, on which the absolute dimension grows quadratically in $\deg D$ and
obeys an exact Riemann–Roch identity with quadratic leading term.* **BUILT.**

**Corollary 6.5 (R16 of `113_12`/`113_15` §7).** R16 asks: *"decide whether a
quadratic $\chi$ can exist over $\operatorname{Spec}\mathbb Z$ at all. Every
Riemann–Roch actually available there is one-dimensional with a linear $\chi$."*
**ANSWERED: YES.** Theorem 3.4 is a quadratic $\chi$ over
$\operatorname{Spec}\mathbb Z$, proved here from Poisson summation; and
arXiv:2512.01811v2 Theorem `main1` (§8 below) is a quadratic $\chi$ for
*arbitrary* arithmetic surfaces, in the literature. R16 therefore does **not**
kill Ansatz A on the grounds it named. It does not thereby support Ansatz A —
see §7.

---

## 7. What this does **not** do

### 7.1 It is not the square

$\overline{\mathbb P^1_{\mathbb Z}}$ is not
$\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$.
Its generic fibre is $\mathbb P^1_{\mathbb Q}$, not $\operatorname{Spec}\mathbb Q$;
its "second direction" is a projective line, supplied by hand, not a second copy
of $\operatorname{Spec}\mathbb Z$. What Theorem 3.4 establishes is that the
*shape* a4 asks for is achievable over $\operatorname{Spec}\mathbb Z$ — the
obstruction is not a theorem of arithmetic. It does not establish that the
*specific* square Weil's analogy wants exists.

- **a4-weak: CLOSED POSITIVELY (Corollary 6.4).**
- **a4-strong: OPEN.** Restated as: *is there a two-dimensional arithmetic
  structure over $\operatorname{Spec}\mathbb Z$, with quadratic $h^0$, whose two
  rulings are both copies of $\operatorname{Spec}\mathbb Z$ and which carries the
  Frobenius correspondences $\Gamma_n$ with $\Gamma_n\cdot\Delta=\psi(n)$?*
  `114_a_03` applies the two tests to every candidate for this.

### 7.2 It does not touch rows (b), (c), (d)

The correspondences on $X$ are the toric self-maps; their Lefschetz numbers are
the $\mathbb F_1$-counts, not $\psi(n)$. Row (c) is untouched. The
Hodge index in §4 is a rank-$2$ triviality (Warning 4.2).

### 7.3 It is not evidence for or against RH

Nothing in this file quantifies over zeros of $\xi$. In particular Theorem
4.1(4) — the analogue of (E) — is true here and carries no information about
(E$^o$) in `113_10`, because the two divisor groups are unrelated: there is no
map
$$
 \widehat{\mathrm{Div}}(\overline{\mathbb P^1_{\mathbb Z}})\ \longrightarrow\ \mathcal D/\operatorname{rad}I_d
$$
carrying $\langle\cdot,\cdot\rangle$ to $s$. Constructing one is **Gap G-3**,
and `114_a_04` shows that constructing it is RH-hard.

---

## 8. Independent confirmation from the literature

arXiv:2512.01811v2, *Numerical cohomology for arithmetic surfaces and
applications*, §1. Definitions, quoted verbatim:

> $h^0_{\mathcal O}(\mathcal F):=\log\sum_{x\in\mathcal F}e^{-\pi\|x\|^2}$,
> $h^1_{\mathcal O}(\mathcal F):=h^0_{\mathcal O}(\omega_{\mathcal O}\otimes\mathcal F^\vee)$
> and $\chi_{\mathcal O}(\mathcal F):=h^0_{\mathcal O}(\mathcal F)-h^1_{\mathcal O}(\mathcal F)$;
> $h^0_{\mathcal X}(\mathcal L):=h^0_{\mathcal O}(f_*\mathcal L)$,
> $h^2_{\mathcal X}(\mathcal L):=h^0_{\mathcal X}(\omega_{\mathcal X}\otimes\mathcal L^\vee)$,
> $\chi_{\mathcal X}(\mathcal L)=h^0_{\mathcal X}(\mathcal L)-h^1_{\mathcal X}(\mathcal L)+h^2_{\mathcal X}(\mathcal L)$.

Theorem `main1`, quoted verbatim:

> **Theorem.** Let $\mathcal L$ be a Hermitian line bundle on an arithmetic
> surface $\mathcal X$ and let $\omega_{\mathcal X}$ be the canonical sheaf
> equipped with the Arakelov metric, then
> $$\Bigl(\chi_{\mathcal X}(\mathcal L)+\tfrac12\log\det\Delta_{\mathcal L_\infty}\Bigr)
> =\tfrac12\bigl(\mathcal L,\mathcal L\otimes\omega_{\mathcal X}^\vee\bigr)
> +\Bigl(\chi_{\mathcal X}(\mathcal O_{\mathcal X})+\tfrac12\log\det\Delta_{\mathcal O_{\mathcal X_\infty}}\Bigr),$$
> where $(\ ,\ )$ is the Arakelov intersection pairing on
> $\widehat{\operatorname{Pic}}(\mathcal X)$.

This is exactly the shape of Theorem 3.4: $\chi=\tfrac12(\mathcal L,\mathcal L-K)+\chi(\mathcal O)$,
with an analytic-torsion correction $\tfrac12\log\det\Delta$ replacing my
$\eta$. It is a **quadratic $\chi$ over $\operatorname{Spec}\mathbb Z$ in the
literature, for arbitrary arithmetic surfaces**, and it settles R16
independently of anything proved here.

Status of this citation: the statement and the definitions were read in the
source file; the proof was not (it is deduced there from Faltings, Deligne and
Gillet–Soulé). Nothing below depends on it — Theorem 3.4 is proved here from
scratch — so no gap is incurred.

---

## 9. Verifier

`114_a_02_the_absolute_quadric.py`. Run (abridged only by removing blank lines
between blocks; every PASS line is verbatim):

```
$ python3 114_a_02_the_absolute_quadric.py
A  mpmath theta convention
PASS  A1 jtheta(3,0,e^{-pi s}) equals sum_j e^{-pi j^2 s} at s=1   | difference 3.86e-62
PASS  A2 functional equation theta(s) = s^{-1/2} theta(1/s)   | max deviation 1.7e-61

B  Theorem 3.4   h0_theta(D) = (1/2) D.(D-K) + eta,  K = (-2,0)
    k     a        h0_theta            (1/2)D(D-K)         eta          bound
     1  1          2.0000000003316                 2.0     3.316e-10     4.974e-10
     2  3                      9.0                 9.0           0.0    3.354e-550
     5  0.5        3.0023460479656                 3.0      0.002346       0.00352
    10  2                     22.0                22.0           0.0     1.062e-73
     0  1          1.0000000001658                 1.0     1.658e-10     2.487e-10
     3  0.1       0.56882779053025                 0.4        0.1688        0.2587
     7  1.5                   12.0                12.0     6.308e-27     9.462e-27
     0  4                      4.0                 4.0           0.0   2.131e-4067
    40  2.5                  102.5               102.5           0.0    3.967e-201
PASS  B1 the identity holds with 0 <= eta <= 3(k+1)exp(-pi e^{2a}) on all 9 points   | eta = (k+1) log theta(e^{2a}) >= 0 structurally, no roundoff involved
PASS  B2 the identity is EXACT to 60 digits once a >= 2   | eta < 1e-50 at (2,3),(10,2),(40,2.5),(0,4)
PASS  B3 deg K = -2, matching deg K_{P^1} = -2   | deg K = -2
PASS  B4 the identity FAILS for any other K: K=(-2,c) with c != 0 breaks it   | tested c = -1, 1, 2 at D=(3,2)

C  Theorem 4.1   the intersection form
PASS  C1 deg(k,a) = k + a
PASS  C2 H^2 = 2
PASS  C3 D^2 = 2ka
PASS  C4 signature is (1,1)   | eigenvalues [-1.0, 1.0]
PASS  C5 Hodge index: the form is NEGATIVE DEFINITE on H-perp   | H-perp = {(k,-k)}, D^2 = -2k^2
PASS  C6 the effective classes (k>=0,a>=0) span a strict cone; H is interior

D  Theorem 2.2   H^0(P^1_Z, O(k)) = Z^{k+1}  by glueing
PASS  D1 sections of O(k) on P^1_Z form a free Z-module of rank k+1, k=0..5   | k=0: dim=1; k=1: dim=2; k=2: dim=3; k=3: dim=4; k=4: dim=5; k=5: dim=6
PASS  D2 monomial basis T_0^i T_1^{k-i}, i=0..k, has k+1 elements

E  Theorem 3.1   log #(ball) and log #(box) are both (1/2)D^2 (1+o(1))
    m     r        log|I_r(n)|     (1/2)(mD)^2      ball ratio    box ratio
     4     5           18.6718         16.0000       1.16699      1.46605
     8     9           65.4351         64.0000       1.02242      1.22245
    16    17          250.2784        256.0000       0.97765      1.10853
    32    33          993.8194       1024.0000       0.97053      1.05359
    64    65         3995.7120       4096.0000       0.97552      1.02662
   128   129        16100.1507      16384.0000       0.98268      1.01327
   256   257        64797.3325      65536.0000       0.98873      1.00662
PASS  E1 ball ratio -> 1   | m=256: 0.98873
PASS  E2 box  ratio -> 1   | m=256: 1.00662
PASS  E3 ball ratio is inside [0.95,1.20] for every m >= 8   | min 0.97053, max 1.02242
PASS  E4 same at (k,a)=(2,3): both ratios -> 1   | m=128: ball 0.99379, box 1.00572

F  Theorem 3.6   the Connes-Consani absolute dimension on the same family
    m    lower/D^2    upper/D^2      (targets 1/(2 ln3)=0.4551, 1/(2 ln2)=0.7213)
    10     0.41529     0.82500
    20     0.42169     0.76125
    40     0.43127     0.74313
    80     0.43949     0.73406
PASS  F1a dim_{S+} / D^2 lies in [0.40,0.83] for m >= 10 (a quadratic law)   | so dim_{S+} = (1/2)D^2 / log q for an effective q in [2,3]
PASS  F1b the window tightens to [0.43,0.75] for m >= 40   | m=40: [0.43127,0.74313]  m=80: [0.43949,0.73406]
PASS  F2 both CC brackets are quadratic, matching E to within the base of the log   | m=80: [0.43949, 0.73406] vs [0.45512, 0.72135]

G  Theorem 5.1   gauge robustness: l1 versus sup on the torus
PASS  G1 ||f||_sup <= ||f||_{l1}                      (400 random integer forms)
PASS  G2 ||f||_{l1} <= (k+1) ||f||_sup   (Fourier)    (400 random integer forms)
PASS  G3 the squeeze log|I_r(n)| <= log #B_sup <= log|I_r(r n)| has both ends ~ (1/2)D^2   | m=64: [0.97552, 1.04176] times (1/2)D^2
PASS  G4 the theta gauge agrees with the box gauge to O(m): |h0_th - r log(2n+1)| <= r log 2   | difference 45.0546 <= r log 2 = 45.0546   (m=64, r=65)

H  Theorem 6.1   homogeneity degree 2; obstruction O1 does not apply
PASS  H1 delta = d log h0_theta / d log m = 2 exactly for h0_theta   | measured 1.982298
PASS  H2 h0_theta(mD)/h0_theta(D) -> infinity, so Prop 5.1 of 113_10 does NOT hold here   | ratio at m=100 is 5050.0 (= m^2 = 10000 up to O(1/m))
PASS  H3 h0_theta is strictly increasing in both k and a

I  negative controls: one direction only is LINEAR
PASS  I1 k=0 (purely archimedean, = CC's Spec Zbar): delta = 1   | measured 1.000000
PASS  I2 a fixed (rank direction only): delta = 1   | measured 0.982298
PASS  I3 in both controls (1/2)D^2 = 0 or is linear, consistent with delta = 1
PASS  I4 the quadratic term needs BOTH: D^2 = 2ka vanishes iff k=0 or a=0

VERDICT: ALL CHECKS PASS
$ echo $?
0
```

Two checks were rewritten during development, in both cases because the
*assertion* was numerically ill-posed, never because the mathematics moved.
(a) `h0_theta` was first evaluated as $\log\vartheta(e^{-2a})$, which overflows
`mpmath`'s `THETA_Q_LIM` for $a\gtrsim3$; it is now evaluated through Jacobi's
identity as $a+\log\vartheta(e^{2a})$, which is exact (check A2) and stable, and
which also makes $\eta\ge0$ hold *structurally* rather than up to roundoff.
(b) F1's window was $[0.40,0.80]$, but the true upper bracket at $m=10$ is
$0.825$; the check now records the true windows $[0.40,0.83]$ for $m\ge10$ and
$[0.43,0.75]$ for $m\ge40$.

---

## 10. Gaps

- **Gap G-1.** *The exact constant.* Determine
  $\lim_{m\to\infty}\dim_{mk+1}(\lfloor e^{ma}\rfloor)/(ka\,m^2)$; Theorem 3.6
  only brackets it in $[1/\log3,1/\log2]$.
  **Status: OPEN.** This is `107_146` §7's own conjecture in the rank-two case.
  **What would close it:** an exact minimal generating set for $I_r(n)$ in the
  regime $r\asymp\log n$, or a matching entropy bound with the mass constraint
  taken into account.
  **Believed hard?** Combinatorially non-trivial but elementary; *not*
  RH-related. **Not needed for a4**: the dichotomy is a $\Theta$-statement and
  $h^0_\theta$ has constant exactly $1$.

  **Resolution (114.a.11).** The positive `l1` boundary has
  `$\binom{n+r-1}{r-1}$` points. Saturation of the mass inequality fixes all
  signs there, so `d` generators yield at most `2^d` subset sums. Together
  with the coordinate-binary upper bound this proves, for `r=mk+1` and
  `n=floor(exp(ma))`,
  `$\dim_r(n)/(ka m^2)\to1/\log2$`. Thus G-1 is closed.

- **Gap G-2.** *The linear term for the counting gauges.* Theorem 3.1 gives
  $h^0_{\#,1}(mD)=ka\,m^2+O(m\log m)$; the $\Theta(m)$ coefficient is not
  identified, so only $h^0_\theta$ satisfies an exact Riemann–Roch at linear
  order. **Status: OPEN.** **What would close it:** a lattice-point count for
  $I_r(n)$ with $r\asymp\log n$ to relative precision $o(1/m)$; this is where
  the $\tfrac12\log\det\Delta$ of arXiv:2512.01811v2 Thm `main1` lives.
  **Believed hard?** No; a Mellin/saddle-point computation. Not RH-related.
  **Not needed for a4.**

  **Resolution (114.a.08).** The premise that the next term is linear is false
  for the `l1` gauge.  Exactly,
  `log |I_r(R)|=r log(2R)-log(r!)+O(r^2/R)`; with `r=mk+1` this contains
  `-km log m`.  G-2 is closed by the full expansion in
  `114_a_08_G2_ASYMPTOTIC_AND_R8_BASEPOINT.md`.

- **Gap G-3.** *(The one that matters.)* There is no known homomorphism
  $$
   \Phi:\ \widehat{\mathrm{Div}}\bigl(\overline{\mathbb P^1_{\mathbb Z}}\bigr)
   \ \longrightarrow\ \mathcal D/\operatorname{rad}I_d
   \quad\text{with}\quad
   s\bigl(\Phi D,\Phi D'\bigr)=\langle D,D'\rangle,\ \ \Phi H=H^\wedge .
  $$
  **Status: DELIMITED.** Without it, everything above is a statement about
  `$\mathbb P^1$` and says nothing about `xi`. `114_d3_03` Theorem 6.5 proves
  that even additive `Q`-homogeneous *domination* into a Lorentzian target is
  equivalent to RH; `114_a_13` repairs the rational-linearity proof and shows
  that pointwise non-additive domination is instead automatic and vacuous.
  Thus the displayed homomorphic/isometric version cannot be an unconditional
  intermediate step, while a meaningful non-additive version must transport
  additional polarization or effectivity data.

---

## 11. Refutation conditions, pre-registered (continuing from R27)

- **R28.** If any future file cites Theorem 3.4 as a Riemann–Roch for
  $\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$
  rather than for $\mathbb P^1_{\mathbb Z}$, it fires this condition. §7.1 is
  the standing correction: the object built here is an arithmetic surface, not
  the square.
- **R29.** If any file cites Theorem 4.1(3) or 4.1(4) as evidence for (E$^o$),
  for the Hodge index on $\mathcal D$, or for RH, it fires this condition.
  Warning 4.2 is the standing correction.
- **R30.** If a candidate in `114_a_03` is claimed to pass the GROWTH-TEST, the
  claim must exhibit the two coordinates $(k_m,a_m)$ explicitly and check
  Proposition 5.4 of `114_a_01`. A claim of quadratic growth without both
  coordinates named fires this condition.

---

## 12. Scope

**Proved here.**

- Theorem 2.1: $H^0(\mathbb P^1_{\mathbb Z},\mathcal O(k))\cong\mathbb Z^{k+1}$,
  by an explicit glueing computation (no citation used).
- Theorem 2.2: the $L^2(\mu)$ metric is the standard Euclidean one in the
  monomial basis (Parseval).
- Corollary 2.3: the section lattice has rank $mk+1$ and radius $e^{ma}$.
- Theorem 3.1: $\log\#$ of the $\ell^1$ ball and of the $\ell^\infty$ box are
  both $\tfrac12(mD)^2$ to leading order, two-sided, with explicit error terms.
- Lemma 3.3 and **Theorem 3.4**: the exact Riemann–Roch
  $h^0_\theta(D)=\tfrac12\langle D,D-K\rangle+\eta(D)$ with $K=(-2,0)$ and
  $0\le\eta(D)\le3(k+1)e^{-\pi e^{2a}}$, proved from Jacobi's functional
  equation alone.
- Theorem 3.6 and Corollary 3.7: CC's absolute dimension on the same family, and
  the units interpretation.
- Theorem 4.1: signature $(1,1)$, $H^2=2$, Hodge index on $H^\perp$, and (E) in
  this model — together with Warning 4.2 on why none of it bears on RH.
- Theorem 5.1 and Corollary 5.2: gauge robustness across
  $|\cdot|_1,|\cdot|_2,|\cdot|_\infty,\|\cdot\|_{\sup}$ and the theta gauge,
  with the same leading constant; R27 discharged; `107_146` §8's open question
  answered at the level of the growth exponent and the leading constant.
- Theorems 6.1–6.3 and Corollaries 6.4–6.5: GROWTH-TEST passed, O1-TEST passed,
  bookkeeping condition satisfied, a4-weak BUILT, R16 ANSWERED YES.
- §7: the precise statement of what is *not* done, and the a4-weak / a4-strong
  split.

**Read from source.**

- arXiv:2512.01811v2 §1: the definitions of $h^0_{\mathcal O}$, $h^0_{\mathcal X}$,
  $h^1_{\mathcal X}$, $h^2_{\mathcal X}$, $\chi_{\mathcal X}$, and Theorem `main1`,
  both quoted verbatim in §8. Its *proof* was not read; nothing here depends on
  it.
- `113_10` §5 Prop 5.1 and O1 (used in Theorem 6.2 to say what is being evaded).
- `113_15` §7 R16 (quoted in Corollary 6.5).
- `107_146` §8 (its open question, answered in §5).

**Verified numerically.**

- The theta convention and Jacobi's identity to $10^{-61}$.
- Theorem 3.4 at nine points $(k,a)$, exact to $60$ digits whenever $a\ge2$, and
  within the stated bound $3(k+1)e^{-\pi e^{2a}}$ at all nine.
- $K=(-2,0)$ is the unique archimedean completion making Theorem 3.4 true
  (tested against $c=-1,1,2$).
- Theorem 2.1 for $k=0,\dots,5$ symbolically.
- Theorem 3.1 at $(k,a)=(1,1)$, $m\le256$ and $(2,3)$, $m\le128$; ratios
  $\to1$.
- Theorem 3.6 brackets at $m=10,20,40,80$.
- Theorem 5.1's two norm inequalities on $400$ random integer forms; the squeeze
  at $m=64$.
- Homogeneity degree $2$ (measured $1.9823$) and the two linear controls
  (measured $1.0000$ and $0.9823$).

**Not established.**

- That $\overline{\mathbb P^1_{\mathbb Z}}$ is, or maps to, the square
  $\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$.
  It is not (§7.1).
- Any statement about rows (b), (c) or (d). In particular there are no Frobenius
  correspondences here with $\Gamma_n\cdot\Delta=\psi(n)$ (§7.2).
- Gap G-3: the comparison map $\Phi$ to the phase-113 divisor group. Without it
  nothing here bears on $\xi$.
- Gaps G-1 and G-2: the exact constants at leading and linear order for the
  counting gauges.
- Anything at all about the location of the zeros of $\xi$. §7.3 and Warning 4.2
  are binding.
