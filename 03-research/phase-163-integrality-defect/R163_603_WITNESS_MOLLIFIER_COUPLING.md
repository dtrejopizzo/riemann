# R163_603 — Coupling the first-contact witness with a mollified Hardy function

*Pure mathematics, no numerics. No . Only this file was written; no label of record moves.
Inputs: R163_401 (witness §2.4, light cone §3, balance §4.1, cell identity §4.7, falsifiers §6), R163_402 (lattice
model, Thm 4), R163_501 (audit of the witness structure). Notation is that of R163_401: $T=T_c$, $F$ is the real,
parity-definite, real-rooted witness, $G=\widehat F$ or $-i\widehat F$, $X$ the node set, $t_q=\gamma_q-i\delta_q$,
$w_x=W(H_x)/|\widehat F'(x)|^2\ge0$, and*
$$0=W_T(F)=\sum_{\rho\ \rm on}G(\gamma_\rho)^2+4\sum_q\mathrm{Re}\,G(t_q)^2 .\tag{3.1}$$

**Labels.** PROVED (proof here, in full); PROVED-CITED (reference given; record references not re-audited);
PROVED IN MODEL (inside the lattice model of R163_402); ARGUED (argument given, the load-bearing step named); OPEN.

## 0. Status table

| # | statement | label |
|---|---|---|
| L1 | Levinson–Conrey outputs used here: positive proportion, density, mean values on intervals of length $H\to\infty$ | PROVED-CITED |
| L2.1 | $Z$, $\Xi$ and $Z\cdot M$ are not of exponential type; the Riemann–Siegel main term at height $\gamma$ has local type $\pi\rho(\gamma)=\frac12\log\frac\gamma{2\pi}$ | PROVED (L2.1a); PROVED-CITED (RS formula) |
| L2.2 | Jensen cap: a type-$T$ function vanishes at no more than $eTL+\log(\lVert G\rVert_\infty/\lvert G(c)\rvert)$ ordinates in a window of length $2L$ | PROVED |
| C2.3 | (i) of the task: interlacing is free inside one cell and impossible over long windows unless $T\gtrsim\frac1{e\pi}\log\frac\gamma{2\pi}$. This is the opposite regime to (I1-T) | PROVED |
| L3.1 | node stationarity: sliding one node changes $W$ by $s^2w_xG'(x)^2$; minimality forces no node position at first order | PROVED |
| L3.2 | Stieltjes separation with off-line defect (an exact gap identity) | PROVED |
| C3.3 | every node gap with no on-line ordinate where $G\ne0$ is fed by a strictly negative off-line sum | PROVED |
| P4.1 | in the lattice model, a witness has a node exactly at an on-line zero which is also the vertex of an occupied light cone | PROVED IN MODEL |
| C4.2 | step (ii) of the task ("nodes at on-line zeros ⇒ off-line zeros outside the cones") is false in the model | PROVED IN MODEL |
| T5.1 | conditional exclusion: if every quartet lies outside the corrected cone of its nearest node, there is no witness | PROVED |
| R5.1a | at the witness, the hypothesis of T5.1 is equivalent to RH (circular) | PROVED |
| T5.2 | $M_m$ meta-obstruction: no argument whose inputs are on-line positions + Levinson–Conrey-type averages + off-line positions excludes the witness | PROVED (with the record input "$M_m$ has a first contact", Paper 48 Tab. 1) |
| R5.3 | finite-vector locality: at fixed $T_c$ the witness depends on $\Lambda$ only below $e^{2T_c}$; height-$\gamma_q$ arithmetic reaches it only through (1.1) | PROVED (from R163_401 §4.6) |
| §6 | falsifiers: $M_m$ blocks every positional/averaged step; DH is separated only at density level, which is not load-bearing; the two-atom curve fails (1.1) | PROVED by inspection |
| (A-loc) | the step that needs arithmetic: a cell-level, identity-level repulsion law for the witness | OPEN |
| Row D | | **OPEN** |

**Outcome in one sentence.** The coupling does not close: (i) holds trivially inside one cell and fails over long
windows below the Landau scale; (ii) is false in the lattice model; and every Levinson–Conrey output is shared by
$M_m$, which has a witness. What survives is a new exact identity (L3.2), node stationarity (L3.1), and a precise
statement of the arithmetic step (A-loc).

---

## 1. What the mollifier method supplies (PROVED-CITED)

Levinson (1974), Conrey (1989) and Bui–Conrey–Young (2011) study $V(s)=Q(-\frac1L\frac{d}{ds})\zeta(s)$ with a
mollifier $M(s)=\sum_{n\le y}\mu(n)P(\frac{\log y/n}{\log y})n^{-s}$, $y=R^\theta$. Two inputs give a lower bound
for the zeros of $V$ in $\sigma\le\frac12$, and hence for the zeros of $\zeta$ on the line:
- Littlewood's lemma on a rectangle $[\frac12-\frac aL,\,2]\times[R,2R]$;
- an asymptotic for $\int_R^{2R}|VM(\sigma_0+it)|^2dt$.

The outputs are:
- (L1-a) $N_0(R)\ge\kappa N(R)$, with a positive proportion simple;
- (L1-b) density statements of the type $\sum_{\gamma\le R}(\beta-\frac12)\ll R$ (Selberg; R163_502 Δ, already in R163_401 §4.2);
- (L1-c) mean values on intervals of length $H$, where at best $H\ge R^{a}$ for some fixed $a>0$ (short-interval versions; CITED, not audited).

Every output is an **average over a window of length $H\to\infty$**. Each output is either a statement about the
on-line *positions* (the sign changes of $Z$) or a linear, $\delta$-weighted count of off-line zeros. Note that
$Z(t)M(\frac12+it)$ is not real, so the real sign changes in Levinson's argument are those of $Z$ itself.

## 2. Part (i): a real-rooted Euler-product function of type ≤ $T_c$ interlacing with ζ's ordinates

**Lemma 2.1.**
- (a) **PROVED.** $\Xi(z)=\xi(\frac12+iz)$ is entire of order 1 and maximal type: $\log|\Xi(iy)|\sim\frac y2\log y$.
  So no function of the form $\Xi\cdot g$ with $g$ of finite order and nonzero is of exponential type, and neither is
  $Z\cdot M$.
  *Proof:* Stirling for $\Gamma(\frac s2)$ at $s=\frac12+y$, together with $\zeta(\frac12+y)\to1$. ∎
- (b) **PROVED-CITED** (Riemann–Siegel; Titchmarsh §4.17). On $[\gamma-L,\gamma+L]$ with $L=o(\gamma^{1/2})$,
  $Z(t)=2\sum_{n\le N}n^{-1/2}\cos(\theta(t)-t\log n)+O(\gamma^{-1/4})$ with $N=\lfloor\sqrt{\gamma/2\pi}\rfloor$ and
  $\theta'(t)=\frac12\log\frac t{2\pi}+O(t^{-2})$. So locally $Z$ is a trigonometric sum whose frequencies lie in
  $[0,\theta'+\log N]$. After the chirp is removed by $e^{\pm i\theta}$, the frequencies lie in a band of half-width
  $\frac12\log\frac\gamma{2\pi}=\pi\rho(\gamma)$, which is the Landau scale of R163_402. Mollification multiplies by
  a Dirichlet polynomial of length $y$ and adds $\log y$ to the type.

So the natural Euler-product object that resolves ζ's ordinates at height $\gamma$ has local type at least about
$\pi\rho(\gamma)$, and at least $13.4$ at every height where an off-line zero can sit ($\gamma_q>3\cdot10^{12}$,
R163_401 §4.2).

**Lemma 2.2 (Jensen cap). PROVED.** Let $G\not\equiv0$ be of exponential type $\le T$ and bounded on $\mathbb R$.
Let $c\in\mathbb R$ with $G(c)\ne0$. Then the number of zeros of $G$ in $[c-L,c+L]$ is at most
$$eTL+\log\frac{\lVert G\rVert_\infty}{|G(c)|}.$$
*Proof.* $|G(x+iy)|\le\lVert G\rVert_\infty e^{T|y|}$ (Phragmén–Lindelöf), so $\max_{|z-c|=eL}|G|\le\lVert G\rVert_\infty e^{eTL}$.
Jensen gives $n(L)\le\int_L^{eL}n(r)\frac{dr}r\le\log\max_{|z-c|=eL}|G|-\log|G(c)|$. ∎

**Corollary 2.3 (answer to (i)). PROVED.**
- (a) *Inside one cell it is free.* For any finite set $S\subset\mathbb R$ and any $G\in PW_T$ real-rooted,
  $G_S:=G\prod_{s\in S}(z-s)/\prod_{x\in X_S}(z-x)$ is again real-rooted, of type $T$ and in $PW_T$, for any
  $|X_S|=|S|$ nodes removed. So nodes can be placed on any finitely many on-line ordinates, in particular interlacing
  in one cell, with no arithmetic. A cell-level interlacing statement therefore carries no information.
- (b) *Over long windows it is impossible below a log scale.* By Riemann–von Mangoldt,
  $N(\gamma+L)-N(\gamma-L)=\frac L\pi\log\frac\gamma{2\pi}+O(\log\gamma)$. If $G$ (type $\le T$) vanishes at a
  fraction $\phi$ of these, then by Lemma 2.2
  $$\phi\,\tfrac L\pi\log\tfrac\gamma{2\pi}\le eTL+\log\tfrac{\lVert G\rVert_\infty}{|G(c)|}+O(\log\gamma).$$
  So with $L\to\infty$ at fixed $c$-ratio, $\phi\le e\pi T/\log\frac\gamma{2\pi}$. (By Cartwright–Levinson the global
  constant is $2T/\log\frac\gamma{2\pi}$, R163_401 (I1-b).) Interlacing ($\phi\approx1$) over windows with $L\gg1$
  needs $T\ge\frac1{e\pi}\log\frac\gamma{2\pi}$.
- (c) *Dichotomy.* R163_401's only candidate mechanism needs (I1-T): $T_c<\frac12\log\frac{\gamma_q}{2\pi}-C$. The
  coupling in (i) needs $T_c\gtrsim\frac1{e\pi}\log\frac{\gamma_q}{2\pi}$ (or $\frac12\log$ with the sharp
  constant). The two are therefore (up to the constant $e\pi$ against $2$) **mutually exclusive regimes**. In the
  regime where the witness *could* copy the Hardy sign changes, it can also absorb the on-line zeros next to the cone,
  which is exactly the failure mode (I1-b).

## 3. Rigidity of the witness: what minimality forces

**Lemma 3.1 (node stationarity). PROVED.** Let $x\in X$ be a simple node and $s\in\mathbb R$. Put
$G_s:=G\cdot\frac{z-x+s}{z-x}=G+s\,\widehat H_x$ (in the parity normalisation of R163_401 §4.4). Then $G_s$ is
real-rooted, of type $T$, in $\mathcal D_T$, and
$$W_T(G_s)=s^2\,W(H_x)=s^2\,w_x\,G'(x)^2 .$$
*Proof.* $W(F,H_x)=0$ because $F\in\ker W_T$ and $W_T\ge0$ (Cauchy–Schwarz; R163_501 §4(a)). Expand the quadratic
form. ∎

*Reading.* Every node position is a critical point; minimality imposes **no** first-order condition on where a node
sits. A node is rigid iff $w_x>0$. If $w_x=0$ then $H_x\in E_c$ and the node slides freely inside the kernel. So a
node-forcing lemma cannot come from the variational equation node by node. It can only come from the global identity
(3.1), equivalently from the full kernel equation R163_401 §4.6.

**Lemma 3.2 (Stieltjes separation with off-line defect). PROVED.** Let $a<b$ be consecutive simple nodes. Then
$$\sum_{\rho\ \rm on}\frac{G(\gamma_\rho)^2}{(\gamma_\rho-a)(\gamma_\rho-b)}
\;=\;-4\sum_q\mathrm{Re}\,\frac{G(t_q)^2}{(t_q-a)(t_q-b)} .\tag{3.2}$$
*Proof.* $W(H_a,H_b)=0$ (R163_401 §2.4(iii), Gauss orthogonality, R163_501 G(c)). By (1.1) and Lemma 3.1(b) of R163_401,
$W(H_a,H_b)=\sum_\rho G(t_\rho)^2/((t_\rho-a)(t_\rho-b))$, which converges absolutely by Lemma 3.0 there. A quartet
$\{t,\bar t,-t,-\bar t\}$ contributes the conjugate and parity images. With the parity of $G$, $(-t-a)(-t-b)=(t+a)(t+b)$,
and the images $-a,-b$ are also consecutive nodes. Pairing the terms gives $4\mathrm{Re}$ when $\{a,b\}=\{-b,-a\}$.
In general, write the right side as $-\sum_{t\in q}$ over the four points; the statement holds with this
reading, and the $4\mathrm{Re}$ form holds after symmetrising over the gaps $(a,b)$ and $(-b,-a)$. ∎

*Reading.*
- On the left, a term is $<0$ iff $\gamma_\rho\in(a,b)$. If all the $t_\rho$ were real, (3.2) would be the
  Chebyshev–Markov–Stieltjes separation: every gap between Gauss nodes contains a mass point.
- On the right, to first order (R163_401 Lemma 3.4(e)), an off-line point in the gap near $a$ contributes
  $\mathrm{Re}\,G'(a)^2\frac{t-a}{t-b}=G'(a)^2\frac{(\gamma-a)(\gamma-b)+\delta^2}{|t-b|^2}$. This is negative iff
  $(\gamma-a)(b-\gamma)>\delta^2$, i.e. iff the point is *outside* the cones of both endpoints. So in the gap identity
  an off-line zero outside the cones plays the role of an on-line zero, and an off-line zero inside a cone plays the
  role of mass outside the gap.

**Corollary 3.3 (empty gaps are fed off-line). PROVED.** If the gap $(a,b)$ contains no on-line ordinate with
$G(\gamma)\ne0$, then
$$\sum_{t\in\text{off-line}}\mathrm{Re}\,\frac{G(t)^2}{(t-a)(t-b)}=-\sum_{\rm on}\frac{G(\gamma)^2}{(\gamma-a)(\gamma-b)}<0 .$$
The inequality is strict because, by balance (R163_401 §4.1), some on-line $G(\gamma)\ne0$, and every on-line term is
$\ge0$ here. This applies to every node gap inside $(-\gamma_1,\gamma_1)=(-14.13,14.13)$. There $\delta=0$ for every zero with
$|\gamma|\le3\cdot10^{12}$, so a feeding quartet sits at distance $>3\cdot10^{12}$.

*Why this does not close.* For a gap near $0$, $(t_q-a)(t_q-b)=t_q^2(1+O(|a|+|b|)/\gamma_q)$. So the off-line sides of
all low gaps are one number $\Sigma_{\rm off}=\sum_q4\mathrm{Re}\,G(t_q)^2/t_q^2$, up to relative error
$O(10^{-11})$, and (3.2) asks only that it equal minus a positive on-line quantity. That is one sign condition on one
number, which is satisfiable. The model $M_m$ satisfies it (T5.2). L3.2 and C3.3 are structure, not sign.

## 4. Part (ii): forcing nodes onto on-line zeros does not empty the cones

**Proposition 4.1 (lattice witness with a node on an on-line zero inside the cone). PROVED IN MODEL.** Use the model
(M1)–(M2) of R163_402 with offset $\alpha=0$: the on-line points are $\gamma+n/\rho$, so $\gamma$ itself is an on-line
point, and the off-line pair sits at $\gamma\mp i\delta$. Suppose $T<\pi\rho$ and $S(T,\delta)=\pi\rho$. Then the
extremal $G(x)=-2\int_0^T\sinh(\delta u)\sin(xu)\,du$ is a model witness (form value $0$, form $\ge0$). Its node
$x_0=0$ coincides with the on-line point $\gamma$, and the off-line pair sits at the vertex of its light cone:
$|\gamma-x_0|=0<\delta$.
*Proof.* R163_402 Thm 4 holds for every $\alpha$, since Poisson summation is exact for type $2T<2\pi\rho$. At
$S=\pi\rho$ the infimum is $0$ and is attained at $a=0$, $b=\sinh\delta u$. $G$ is odd and real on $\mathbb R$,
$G(0)=0$, and $G(-i\delta)\in i\mathbb R$, so $\mathrm{Re}\,G(-i\delta)^2=-|G(-i\delta)|^2<0$. ∎

**Corollary 4.2. PROVED IN MODEL.** Step (ii), "if the witness's nodes coincide with on-line zeros, then off-line
zeros lie outside every light cone", is false. The light cone is measured from the node. A node may sit on an on-line
ordinate and still have an off-line ordinate within $\delta$, because $\delta$ is not bounded by the on-line spacing.
For $S(T,\delta)>\pi\rho$, continuity in the node shift (Lemma 3.1 with a negative base value) gives $W<0$ for every
node position near $\gamma$. So positivity also fails on the class
$\mathcal N_T=\{G\ \text{real-rooted, type}\le T,\ X(G)\subset\Gamma_{\rm on}\}$. The minimiser's nodes are pulled
**toward** the off-line ordinate, the cone vertex (R163_402 Thm 4), which is the opposite of the forcing sought.

## 5. What would close it, and why the mollifier cannot supply it

**Theorem 5.1 (conditional exclusion). PROVED.** Suppose that at a witness, every off-line quartet $q$ satisfies
$|E_q|<\pi/4$ and $|\gamma_q-x_0(q)|\ge\delta_q\cot(\pi/4-|E_q|)$, where $x_0(q)$ is the nearest node. Then the
witness does not exist.
*Proof.* By R163_401 Lemma 3.4(b), $\mathrm{Re}\,G(t_q)^2\ge0$ for every $q$. Then (3.1) gives $0\ge P_+>0$
(balance, §4.1), a contradiction. ∎
The hypothesis follows from: (H-node) $X\subset\Gamma_{\rm on}$; (H-sep) $|\gamma_q-\gamma|\ge\delta_q\cot(\pi/4-|E_q|)$
for every on-line $\gamma$; and $|E_q|<\pi/4$.

**Remark 5.1a (circularity). PROVED.** Under ¬RH, Cor 4.1 of R163_401 gives some $q$ with $\cos2\Theta_q<0$. So the
hypothesis of T5.1 at the witness is equivalent to RH (with Prop 4.0 there). As in R163_401 Rem 4.8a, T5.1 is
non-circular only if its hypothesis is proved for a class strictly larger than witnesses. P4.1 shows that the natural
class $\mathcal N_T$ fails without (H-sep), and (H-sep) is a zero-repulsion statement between on-line and off-line
ordinates on scale $\delta_q$. Nothing known gives it, and §4.2's densities do not localise.

**Theorem 5.2 ($M_m$ meta-obstruction). PROVED** (record input: $M_m$ has a first contact, Paper 48 Tab. 1; the
witness structure R163_501 applies verbatim to $M_m$, since it uses only (1.1), compact resolvent, monotonicity and
continuity).
Let $\mathcal A$ be any argument whose inputs are:
- (a) the on-line ordinate set, including the sign changes of $Z$;
- (b) statements averaged over windows of length $H\to\infty$, such as (L1-a)–(L1-c);
- (c) the positions $(\gamma_q,\delta_q)$ of the off-line zeros, with $\delta_q<\frac12$;
- (d) the identities L3.1, L3.2, (3.1), §4.7.

Then $\mathcal A$ does not exclude a witness.
*Proof.* $M_m=\xi\cdot\prod_{j\le m}(\text{rational quartet factor})$ has the same on-line zeros as $\zeta$, so (a)
holds verbatim. Its off-line zeros are $m$ chosen quartets, and averages over length $H$ change by $O(m/H)\to0$, so
(b) holds. Choosing $\delta_j<\frac12$ gives (c). (d) is class-level. Since $M_m$ has a witness, an argument from
(a)–(d) that excluded witnesses would exclude $M_m$'s. ∎
*Consequence for the task.* Everything Levinson–Conrey proves is of type (a) or (b). The proposed coupling compares
node positions with sign changes, which is (a). It therefore cannot work, whatever the extremality argument.

**Remark 5.3 (finite-vector locality). PROVED** (from R163_401 §4.6 and Selberg uniqueness, record).
- $W_{T_c}$, and hence $E_c$ and the witness with its nodes, depends on the arithmetic only through
  $(\Lambda(n))_{n<e^{2T_c}}$.
- A mollifier at height $\gamma_q$ uses $\mu(n)$ for $n\le\gamma_q^\theta$, and $\gamma_q^\theta\gg e^{2T_c}$
  unless $T_c\gtrsim\frac\theta2\log\gamma_q$, which is again the Landau-type regime of C2.3(c).
- So height-$\gamma_q$ arithmetic reaches the witness **only** through the global identity (1.1), that is, through
  the zero positions themselves. Since those are (a)+(c), T5.2 applies.
- Multiplying the witness by the mollifier, $GM$, raises the window to $T_c+\log y$, where $W\ge0$ is no longer
  available (λ may be negative beyond the contact), so no contradiction can be read off.

## 6. Falsifier checks

| model | (1.1) | L3.1–L3.2 | Levinson–Conrey outputs | where the coupling fails |
|---|---|---|---|---|
| $M_m$ | holds | hold | (a),(b) identical to ζ | T5.2: every positional or averaged step passes, and $M_m$ has a witness. The argument must use more than node positions and averages (the task's warning is confirmed as a theorem) |
| Davenport–Heilbronn | holds (own Γ) | hold | (L1-a) unknown at full strength; (L1-b) **fails**: $N(\sigma_1,\sigma_2;R)\gg R$ for $\frac12<\sigma_1<\sigma_2<1$ (Davenport–Heilbronn; Voronin; CITED) | DH is separated by the Euler product at **density level** only. A density bound is an (b)-input, and T5.2 shows (b) cannot be load-bearing. So the separation of DH sits where it cannot be used. The cell-level step is not separated (as in R163_401 §6) |
| two-atom curve | **fails** | — | — | §1 / (1.1). The coupling needs (1.1). Its contacts ($T\approx0.55$–$0.61$) are below the range $T_c>0.8047$ |
| lattice model | holds (model) | hold | n/a | P4.1: a witness with a node on an on-line point inside the cone refutes (ii) |

**Battery verdict.** No line of the coupling separates $M_m$. The only Euler-product input that separates DH is a
density, and that is exactly what $M_m$ shows to be inert. So an input that excludes both DH and $M_m$ must see
**individual** off-line zeros at cell scale.

## 7. The exact step that needs arithmetic

$$\boxed{\text{(A-loc)}\quad\text{For the witness at }T_c\text{ and each off-line quartet }q:\ \ \mathrm{dist}(\gamma_q,X)\ \ge\ \delta_q\cot(\tfrac\pi4-|E_q|),\ \ |E_q|<\tfrac\pi4,}$$
proved from an identity in which the atomic coefficients $\Lambda(n)$, $n<e^{2T_c}$ (the only arithmetic the witness
sees, R5.3), appear, and which fails for $M_m$'s added quartets. The requirements are:
- By T5.1, (A-loc) suffices.
- By R5.1a it is RH at the witness, so it must hold for a named class larger than $E_c$.
- By L3.1 it cannot come from node-by-node variation.
- By P4.1 it cannot come from (H-node), i.e. from placing nodes on on-line zeros.
- By T5.2 it cannot come from any Levinson–Conrey output.
- By C2.3 a mollified Hardy comparison function lives at type $\gtrsim\log\gamma_q$, in the regime where the 401
  mechanism (I1-T) already fails.

The new identity L3.2 is the natural place for (A-loc) to appear. By its first-order reading, an in-cone quartet acts
as "mass outside the gap". (A-loc) is equivalent to: no node gap's identity (3.2) receives a positive in-cone
contribution. **OPEN.**

**Row D: OPEN.** New here: the stationarity lemma L3.1, the separation identity L3.2 and C3.3, the model refutation
P4.1 of node forcing, the meta-obstruction T5.2 ruling out every Levinson–Conrey-type input, and the type dichotomy
C2.3(c) between the mollifier regime and (I1-T).
