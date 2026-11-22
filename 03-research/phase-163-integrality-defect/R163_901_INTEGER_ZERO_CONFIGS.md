# R163_901 — Integer zero configurations with ζ's window functional: the R163_801 §6 question decided

*Pure mathematics, no numerics, no , no commits. Only this file was written; no label of record moves.
Inputs: R163_801 (§6 items 8–10, Thm 5, Prop 5.1), R163_603 (T5.1, R5.1a, R5.3, box (A-loc)), R163_401 (box, 4.8 $(\star_{\rm cell})$,
Rem 4.8a), R163_102 (Thm R), R163_803 (rounding), R163_113 (Hamburger collapse), R163_501 (witness structure).*

*Revision v2: the nine record edits of the audit R163_991 §5 applied (balance hypothesis in Prop 1.2; Bochner /
Kahane–Mandelbrojt citation for Lemma 2.1 and Thm F.1; Thm F.2 relabelled trivial; Thm F.3 support and agreement window corrected;
Thm F.4 frequency list and $A=0$ case; Cor F split; Var F′ coefficient formula; §3 split into three statements with three labels; the
"only structural separator" and R163_114 overclaims removed). v1 backed up as R163_901_v1.md. No label of record moves.*

**Question (R163_801 §6, OPEN).** Is there a configuration $Z$ with positive integer multiplicities, symmetric under
$\rho\mapsto1-\bar\rho$, with an off-line quartet, whose zero-side window functional coincides with ζ's and whose first-contact
witness violates (A-loc)? (a) means "yes, by construction", (b) means "integrality plus window data force (A-loc)".

**Decision.** The question as posed is **equivalent to the failure of RH at window scale**, with ζ itself the realiser (§1). So it can
be neither constructed (a) nor obstructed (b) without deciding RH, and **integrality has no role in it**. The reduction in R163_801 §6
("only integrality can separate") is therefore vacuous. The meaningful version, where the configuration agrees with ζ on a window
and has its own contact, has answer (a), and the answer is unconditional (§2, Theorem F). The separating information is the exact
value of the finite vector $(\Lambda(n))$ at the contact level, that is, the positivity of $W_{T_c}$ itself (§3). The
(A-loc) clauses of Cor F and §3 depend on an unproved property of $f_t$ (on-line abundance, "balance") and are ARGUED, not proved
(R163_991 §3.5, §4).

## 0. Status table

| # | statement | label |
|---|---|---|
| Prop 1.1 | witness, nodes and first contact of any configuration depend only on its window functional | PROVED (= R163_603 R5.3, R163_801 Thm 3(b)) |
| Prop 1.2 | every **balanced** configuration (positive integer multiplicities, $\gg R\log R$ distinct on-line ordinates in $(0,R)$) with a witness violates (A-loc) at that witness | PROVED (contrapositive of T5.1; balance hypothesis added, R163_991) |
| Thm 1.3 | the §6 question ⟺ ζ has a first contact below the window ⟺ ¬RH at window scale; ζ is the realiser; integrality plays no role | PROVED (balance holds for ζ: Levinson/Conrey) |
| Rem 1.4 | the real-weight configuration "ζ + q − ν" of R163_801 §6 has ζ's witness, and so violates (A-loc) only if ζ does | PROVED |
| Lem 2.1 | self-dual lattice measures with a spectral and spatial hole at 0 | PROVED; new in the record, classical in the literature (finite-lattice instance of Bochner / Kahane–Mandelbrojt) |
| Thm F | for every $N_0$, a real Dirichlet series $f=\zeta+t\,g$ with ζ's exact completed functional equation, integer zero multiplicities (trivially: F.2), atomic prime side on a discrete semigroup (not on $\log\mathbb N$), $W^{f_t}_T=W^\zeta_T$ for $T\le\frac12\log\lambda_1$ (so on $\lvert u\rvert<\log N_0$), off-line zeros and a finite contact | PROVED (explicit formula: standard, cited; fixes of R163_991 §3.3–3.4 applied) |
| Cor F, $(\star_{\rm cell})$ clause | at $f$'s witness $(\star_{\rm cell})$ fails | CORRECT given witness existence (witness existence for $f$: ARGUED, transfer of R163_501) |
| Cor F, (A-loc) clause | at $f$'s witness (A-loc) fails | **ARGUED**; two gaps: witness existence (transfer), on-line abundance (balance) of $f_t$ — OPEN |
| Var F′ | variant whose prime side up to the contact level is supported on $\log$ of integers (not on prime powers in general) | ARGUED (dimension count; coefficient formula corrected) |
| §3(i) | no argument from the listed inputs proves Row D ($W_T\succeq0$ for all $T$) | PROVED, unconditional (F.4 alone) |
| §3(ii) | no argument from the listed inputs proves $(\star_{\rm cell})$ at the witness | CORRECT given witness existence for $f_t$ (ARGUED) |
| §3(iii) | no argument from the listed inputs proves (A-loc) at the witness | **NOT PROVED**; ARGUED, conditional on witness existence and on-line abundance of $f_t$ |
| (A-loc), $(\star_{\rm cell})$, Row D | | **OPEN** |

## 1. The literal question collapses onto RH

**Proposition 1.1 (window locality). PROVED.** Let $Z$ be a configuration whose zero-side identity (R163_801 (0.1)) holds with
symbol $\sigma$. Then $W_T$ for $T\le T_0$, the first contact $T_c$ (if $T_c<T_0$), the witness $F\in E_c$, $G$ and the node set $X$
are functions of the restriction of the window functional $\Psi\mapsto\sum_{\rho\in Z}\Psi(t_\rho)$ to products of $PW_{T_0}$.
*Proof.* $W_T(F)=\sum_\rho(\widehat F\widehat F^\#)(t_\rho)$ for $F\in PW_T$ is that restriction, and $T_c,E_c,F,X$ are defined from
$\{W_T\}_{T\le T_c}$ alone (R163_401 §1.1; R163_603 R5.3). ∎

**Proposition 1.2. PROVED.** If $Z$ has positive integer multiplicities, satisfies the zero-side identity, is **balanced** — i.e.
$Z$ has $\gg R\log R$ distinct on-line ordinates in $(0,R)$ (R163_401 §4.1; for ζ this is Levinson/Conrey), or at least more distinct
on-line points in $(-R,R)$ than $\frac{2T_c}{\pi}R+o(R)$, the Cartwright–Levinson zero density of the witness (R163_501 FC(i)) — and
has a first-contact witness, then some off-line quartet of $Z$ violates the (A-loc) box (the conjunction $|E_q|<\pi/4$ and the
distance bound), so (A-loc) fails for $Z$.
*Proof.* T5.1 (R163_603 §5) uses (1.1), the positivity of on-line weights $\mathrm{mult}\cdot\mathrm{Re}\,G(\gamma)^2\ge0$ (Lemma 3.4(b)) **and
balance** ($P_+>0$, R163_401 §4.1: $G\ne0$ has $O(R)$ zeros in $(0,R)$, so $G(\gamma)\ne0$ at some on-line $\gamma$): if every quartet is
outside its corrected cone, there is no witness. Take the contrapositive. Without balance the contrapositive only yields: either some
quartet violates the box, **or** $G$ vanishes at every on-line point of $Z$ and $\sum_q\mathrm{Re}\,G(t_q)^2=0$. For a general integer
configuration balance is an extra hypothesis (R163_991 §1). ∎

**Theorem 1.3 (collapse). PROVED.** Fix $T_0$. The following are equivalent:
- (i) there is $Z$ as in the question whose window functional equals ζ's on $PW_{T_0}$-products and which has a witness at a level $T_c<T_0$;
- (ii) ζ has a first contact $T_c<T_0$;
- (iii) $W_T^\zeta\not\succeq0$ for some $T<T_0$ (¬RH at window scale, R163_603 R5.1a).

Moreover, in (i) the witness of $Z$ *is* ζ's witness, and ζ itself is such a $Z$.
*Proof.* (i)⇒(ii) by Prop 1.1. (ii)⇒(i): take $Z=$ the zeros of ξ. These have integer multiplicities and the symmetry, they contain an
off-line quartet (otherwise $W^\zeta_T\succeq0$ for all $T$), they are balanced (Levinson/Conrey, R163_401 §4.1), and they violate (A-loc) by Prop 1.2. (ii)⇔(iii) is the definition of contact. ∎

*Consequences.* (a) in the literal sense is a disproof of RH. (b) in the literal sense ("window data and integrality force (A-loc)")
is the statement $W^\zeta_T\succeq0$ for $T<T_0$, which is RH at that scale. Integrality does no work in either direction. Whether
ζ's window functional has a contact is a property of the functional alone, and once it does, *every* integer realisation violates (A-loc).

**Remark 1.4 (on R163_801 §6). PROVED.** The real-weight configuration $\zeta+q-\nu$ has ζ's window functional, so by Prop 1.1 its
witness is ζ's: it exists iff ζ has a contact. Its "violation of (A-loc)" is therefore not an extra phenomenon. The sentence
"an argument … can separate only through the integrality of zero multiplicities" should read: *on the exact window functional of ζ
there is nothing left to separate. (A-loc) at ζ's witness is decided by $W^\zeta$ alone.* The rounding programme (R163_803, R163_102
Thm R as an integrality constraint) is not needed for this question. It is moot here rather than refuted.

## 2. The meaningful version: agreement on a window, own contact. Answer (a)

The question that has content: can a configuration with every structural property used in R163_401/603/801 (integer
multiplicities, ζ's exact archimedean and polar terms, an **atomic** prime side (on a discrete semigroup — this is what 401/603/801 *used*;
ζ's prime side is moreover on $\log$ of prime powers, which $f_t$'s is not), an exact zero-side identity, real coefficients,
the functional equation) agree with ζ on a prescribed window and still have a witness that violates $(\star_{\rm cell})$, and (A-loc)? Yes for
$(\star_{\rm cell})$ given witness existence; for (A-loc) only ARGUED, with the balance gap (Cor F).

**Lemma 2.1 (self-dual hole measures). PROVED.** Let $N_0\ge2$. Let $M$ be a non-square integer with $\sqrt M>4N_0+4$, and put $R=\lfloor N_0\sqrt M\rfloor$.
There is a real, even, nonzero $c:\mathbb Z/M\to\mathbb R$ with $\mathcal F_Mc=c$ for the unitary DFT and $c(r)=0$ for $|r|\le R$. The measure
$\nu=\sum_{n\in\mathbb Z}c(n)\delta_{n/\sqrt M}$ then satisfies $\widehat\nu=\nu$ (with $\widehat\mu(\xi)=\int e^{-2\pi i x\xi}d\mu$), $\nu=0$ on $(-N_0,N_0)$, and $\sum_rc(r)=0$.
*Proof.* Poisson summation over $n\equiv r\ (M)$ gives $\widehat\nu=\sum_k(\mathcal F_Mc)(k)\delta_{k/\sqrt M}$. The eigenvalue $1$ of $\mathcal F_M$ has multiplicity
$\ge\lfloor M/4\rfloor$, and its eigenvectors are even and can be taken real, since $\mathcal F_M$ restricted to even vectors is the real
symmetric cosine matrix. There are $R+1$ constraints $c(0)=\dots=c(R)=0$, and $R+1<\lfloor M/4\rfloor$ because $\sqrt M>4N_0+4$. Since $2R<M$,
the points $n/\sqrt M\in(-N_0,N_0)$ have distinct residues $|r|\le R$. Finally $\sum_rc(r)=\sqrt M\,(\mathcal F_Mc)(0)=\sqrt M\,c(0)=0$. ∎

*Remarks (R163_991 §2).* (a) $\sum_rc(r)=0$ forces sign changes in $c$: the new prime-side atoms of $f_t$ have both signs. (b) **New in the
record, classical in the literature.** Self-dual tempered measures are exactly the objects behind Riemann's functional equation, and the
solution space of the FE is infinite-dimensional once non-integral support is allowed: Bochner, *Some properties of modular relations*
(Ann. of Math. 1951; Hecke's theory for signature $(\lambda,\frac12,1)$, $\lambda>2$); Kahane–Mandelbrojt, *Sur l'équation fonctionnelle de
Riemann et la formule sommatoire de Poisson* (Ann. Inst. Fourier 1958); Chandrasekharan–Narasimhan. Lemma 2.1 is a clean finite-lattice
instance of this fact, not a new mechanism; the exact multiplicity of the eigenvalue $1$ of $\mathcal F_M$ is $\lfloor M/4\rfloor+1$ (McClellan–Parks).

**Theorem F (window-agreeing integer falsifier). PROVED** (the explicit formula for $f$ is the standard Weil/Barner derivation, CITED;
it uses no Euler product).
With $\nu,c$ from Lemma 2.1, put $g(s)=\sum_{m>R}c(m)(m/\sqrt M)^{-s}$ and $f_t=\zeta+t\,g$ for $t\in\mathbb R$. Then:
1. $\Lambda_t(s):=\pi^{-s/2}\Gamma(\tfrac s2)f_t(s)$ satisfies $\Lambda_t(s)=\Lambda_t(1-s)$, and $\Lambda_t+\frac1s+\frac1{1-s}$ is entire of order 1. The proof is
   Riemann's, applied to the self-dual measure $\mu_t=\sum_{n\in\mathbb Z}\delta_n+t\nu$: $\theta_t(1/x)=\sqrt x\,\theta_t(x)$, $\theta_t-1$ decays exponentially, and the
   residues are ζ's because $\nu(\{0\})=0$. The coefficients are real. (Infinite-dimensionality of the FE solution space over non-integral
   frequencies is classical: Bochner, Kahane–Mandelbrojt, Hecke; see the remark after Lemma 2.1.)
2. (*Trivial.*) The zero-side measure of $f_t$ is $\sum\mathrm{mult}\cdot\delta_{t_\rho}$ with weights in $\mathbb Z_{>0}$, as for every nonzero meromorphic
   function; the zeros are invariant under $\rho\mapsto1-\rho$ and $\rho\mapsto\bar\rho$ (FE, real coefficients), hence under $\rho\mapsto1-\bar\rho$. The item
   is kept because its role is to record that the configuration is a *genuine zero set*, which is what separates $f_t$ from the real-weight "ζ+q−ν".
3. $f_t=1+\sum_{\lambda\ge2}a(\lambda)\lambda^{-s}$ is a general Dirichlet series, absolutely convergent for $\sigma>1$; hence $-f_t'/f_t=\sum_\lambda b_t(\lambda)\lambda^{-s}$ converges
   absolutely for $\sigma\ge\sigma_1(t)$, over the discrete multiplicative semigroup generated by $\mathbb N$ and $\{m/\sqrt M\}_{m>R}$ (all generators $\ge2$). The
   prime side of the explicit formula (R163_801 (0.1); Weil/Barner, which uses only meromorphy, FE, order 1 and this absolutely convergent series) is the
   coefficient measure $\sum_\lambda b_t(\lambda)\lambda^{-1/2}\delta_{\pm\log\lambda}$: **atomic on a discrete semigroup, not supported on $\log\mathbb N$ and not on
   prime powers** (the atoms have both signs, Lemma 2.1 rem. (a)). Let $\lambda_1=m_1/\sqrt M$ be the least new frequency ($m_1>R$ minimal with $c(m_1)\ne0$). Since
   $g/\zeta=g\sum\mu(d)d^{-s}$ and hence $\log(1+tg/\zeta)$ have all frequencies $\ge\lambda_1$, we get $b_t(\lambda)=\Lambda(\lambda)$ for **all** $\lambda<\lambda_1$ (zero off
   $\mathbb N$). So the explicit formula for $f_t$ has ζ's polar term, ζ's archimedean term $m$, and $W^{f_t}_T=W^\zeta_T$ **exactly for $T\le\frac12\log\lambda_1$**;
   in particular it equals ζ's on $|u|<\log N_0$.
4. With $\lambda_1\notin\mathbb Z$ as in 3. For $|t|$ large, $f_t$ has a zero off the critical line (possibly with $\sigma>1$: no Euler product forbids it), and
   $W^{f_t}_T\not\succeq0$ for $T=\frac12\log\lambda_1+\varepsilon$. So $f_t$ has a finite first contact $T_c(f_t)\le\frac12\log\lambda_1+\varepsilon$.

*Proof of 4.* Take $\varepsilon>0$ with $2\varepsilon<\log2$, and also smaller than the log-distance from $\lambda_1$ to every other frequency of $-f'_t/f_t$ below $\lambda_1^2$.
The frequencies below $\lambda_1^2$ are the integers, the single atoms $m/\sqrt M$ ($m>R$), and the products $n\cdot m/\sqrt M$ with $2\le n<\lambda_1$; the latter are
$\ge2\lambda_1$, at log-distance $\ge\log2>2\varepsilon$ from $\lambda_1$, so they are harmless. This is a discrete set independent of $t$. Below $\lambda_1^2$,
$b_t(\lambda_1)=t\,c(m_1)\log\lambda_1$ (the coefficient of $\log f_t$ at $\lambda_1$ is $a(\lambda_1)=tc(m_1)$; no product of smaller frequencies hits $\lambda_1$), and the other
$b_t$ within $2\varepsilon$ of $\log\lambda_1$ vanish.
Let $0\le\phi_0\in C_c^\infty(-\varepsilon,\varepsilon)$, $k_0=\phi_0*\tilde\phi_0$, $a=\log\lambda_1$, $\phi=\phi_0+\eta\,\tau_a\phi_0$ ($\eta\in\mathbb R$). The Weil form is
$Q(\eta)=(1+\eta^2)A+2\eta B_t$. Here $A$ (polar plus archimedean on $k_0$, no prime term since $\mathrm{supp}\,k_0\subset(-2\varepsilon,2\varepsilon)$) is independent of $t$, and
$B_t=B_0-t\,c(m_1)\log\lambda_1\,\lambda_1^{-1/2}k_0(0)$ with $B_0$ independent of $t$ and $k_0(0)=\lVert\phi_0\rVert_2^2>0$. If $A<0$ we are done ($\eta=0$). If $A=0$, then
$Q(\eta)=2\eta B_t$ and $B_t\ne0$ for $|t|$ large, so $Q$ takes negative values. If $A>0$,
$\min_\eta Q=A-B_t^2/A<0$ once $|B_t|>A$, which holds for $|t|$ large. On the zero side, $Q=\sum_\rho\widehat\phi(t_\rho)\overline{\widehat\phi(\bar t_\rho)}$, which is $\ge0$ if all $t_\rho\in\mathbb R$.
So some $t_\rho\notin\mathbb R$. The test has support in $|u|\le a+2\varepsilon$; by translation invariance of $|\widehat F|$ on $\mathbb R$, of $A\bar B$ and of $c_F$
(R163_501 §3.3) it lies in $L^2(I_T)$, $T=\frac a2+\varepsilon$. Since $W^{f_t}_T=W^\zeta_T>0$ on $(0,\frac12\log5]$ (Paper 46 certificate; $N_0\ge5$ may be assumed), $T_c(f_t)$ is well
defined and finite. ∎

*Remark (sign of the atoms is not a separator at contact level).* Below $e^{2T_c}\le\lambda_1e^{2\varepsilon}<2\lambda_1$ the only non-ζ atom is $\lambda_1$, and item 4 works
for either sign of $t$; choosing $t\,c(m_1)>0$ makes every atom below the contact positive. So "all atoms $\ge0$" does not separate ζ from $f_t$ below the contact.

**Corollary F.** Suppose $f_t$ has a (real-rooted first-contact) witness at $T_c(f_t)$. Witness existence for $f_t$ — form structure (finite comb symbol,
closedness, compact resolvent), the zero-side identity (1.1) on $\mathcal D_T$ (R163_401 Lemma 3.0 adapted to a disc containing the zeros with $\sigma>1$),
$T_c<\infty$ (item 4), monotonicity/continuity in $T$, real-rootedness (R163_501 Thms B, R: $|\widehat F|$ on $\mathbb R$, the polar pair at $\pm i/2$, parity;
$\Lambda_t(\frac12+it)\in\mathbb R$ by FE + real coefficients) — transfers from R163_501 as applied to $M_m$ in R163_603 T5.2: **ARGUED**, no obstruction seen.

- **$(\star_{\rm cell})$ clause. CORRECT given witness existence (ARGUED).** Rem 4.8a's identity $\sum_j(P_j-N_j)=W(F)=0$ is a partition of (1.1); cells without
  off-line ordinates have $N_j=0$, $P_j\ge0$; one cell contains an off-line ordinate (item 4), and $(\star_{\rm cell})$ there would give $W(F)>0$. No balance needed.
- **(A-loc) clause. ARGUED, with a second open input.** Via Prop 1.2, hence via T5.1, hence via **balance**: if (A-loc) held at $f_t$'s witness, then
  $\mathrm{Re}\,G(t_q)^2\ge0$ for all $q$ and $0=\sum_{\rm on}\mathrm{mult}\,G(\gamma)^2+\sum_{\rm off}$ would force $G$ to vanish at every on-line zero of $f_t$. To
  exclude this one needs $f_t$ to have more distinct on-line zeros in $(-R,R)$ than $\frac{2T_c}\pi R+o(R)$ (the witness's zero density, R163_501 FC(i)). For ζ this is
  Levinson/Conrey ($\gg R\log R$). For $f_t$ — a generalised Dirichlet series without Euler product — **no such result is on record**: for ordinary non-Euler series
  with FE (Epstein with $h>1$, Davenport–Heilbronn) only $\gg R$ on-line zeros are known unconditionally (Voronin; Karatsuba), with no control of the constant against
  $2T_c/\pi$; for $f_t$ not even a Hardy-type "infinitely many" is on record. The degenerate alternative ($G$ vanishing at all on-line zeros of $f_t$) is implausible
  but not excluded, and it is exactly the case in which (A-loc) would hold. Gaps: (1) witness existence (transfer, ARGUED); (2) on-line abundance of $f_t$ (OPEN).

If ζ has no contact below $\tfrac12\log\lambda_1$, then $T_c(f_t)\in[\tfrac12\log\lambda_1,\tfrac12\log\lambda_1+\varepsilon]$, pinned at the first new atom (if ζ does have a
contact below, $f_t$'s witness is ζ's by Prop 1.1 and Cor F says nothing new). Since $N_0$ is arbitrary, the agreement window can be made as long as wanted.

**Variant F′. ARGUED.** Take $\sqrt M=K\in\mathbb N$, and also impose $c(n)=0$ for $|n|<N_1K$, $K\nmid n$ (about $N_1K$ more constraints, against $K^2/4$; fine for $K>8N_1$).
If the solution space has some $c(n_0K)\ne0$ with $N_0\le n_0<N_1$, then $f_t$ has integer frequencies below $N_1$. The coefficient of $tg/\zeta$ at an integer $n<N_1$ is the
Möbius convolution $t\sum_{d\mid n,\ n/d\ge N_0}\mu(d)\,c((n/d)K)$ (the other divisors of $nK$ give $c$ at non-multiples of $K$, which vanish below $N_1K$); so in general
$b_t(n)\ne\Lambda(n)+t\,c(nK)\log n$, but at the **minimal** $n_0$ with $c(n_0K)\ne0$ the formula $b_t(n_0)=\Lambda(n_0)+t\,c(n_0K)\log n_0$ is correct, and that is all item 4 uses.
Item 4 with $a=\log n_0$ gives a contact at a level where **the prime side is supported on logs of integers** (but not on prime powers in general: $n_0$ composite is
allowed, so even F′ does not reproduce the Euler-product structure of R163_114), and differs from ζ's only in the values at $n\in[N_0,n_0]$. The non-vanishing of the
coordinate is the unproved step (a dimension count makes it generic). With $\sqrt M=K$ the FE of conductor 1 for $K^s\sum c(m)m^{-s}$ is Hecke's signature
$(K,\frac12,1)$, whose solution space is infinite-dimensional for $K\ge3$; consistent.

**Why this is not ζ (Hamburger).** An integer-frequency Dirichlet series with ζ's functional equation is $c\zeta$ (Hamburger; R163_113, Bombieri–Ghosh form: it
assumes an *ordinary* Dirichlet series). $g$ has irrational frequencies $m/\sqrt M$ ($M$ non-square), so the theorem does not apply — the classical escape (Bochner) —
and $f_t=c'\zeta$ is impossible by uniqueness of general Dirichlet series (disjoint frequency sets $\mathbb N$ versus irrationals). So $\nu$ must leave $\mathbb Z$
at some height, and F′ only pushes that height above the contact. The separation of ζ from $f_t$ is a statement about **all** levels, not about any window.

## 3. What a proof of (A-loc)/$(\star_{\rm cell})$/Row D must use. Three statements, three labels

Let $\mathcal A$ be an argument whose inputs are: integer multiplicities; the zero-side identity; ζ's Γ-factor, polar term and functional equation;
atomicity of the prime side; real coefficients; the values $\Lambda(n)$ for $n<e^{2T_0}$ with $T_0<T_c$ (the prime side on $|u|<2T_0$); and every structure of
R163_401/603/801 (T5.1, L3.1–L3.2, Thm 1 collapse, Prop 4, Prop 5.1 with $V_T$ replaced by the actual atomic mass) **except** balance.

- **(i) Unconditional. PROVED.** $\mathcal A$ does not prove Row D ($W_T\succeq0$ for all $T$). This follows from Thm F.4 alone: $f_t$ has FE with $\Gamma_{\mathbb R}$ and
  ζ's pole, real coefficients, a genuine integer zero set, an atomic prime side equal to ζ's below $\lambda_1$, and $W^{f_t}_T\not\succeq0$ at $T=\frac12\log\lambda_1+\varepsilon$.
  No witness theory, no balance.
- **(ii) Given witness existence for $f_t$ (ARGUED). CORRECT.** $\mathcal A$ does not prove $(\star_{\rm cell})$ at the witness (Cor F, first clause).
- **(iii) NOT PROVED; ARGUED.** $\mathcal A$ does not prove (A-loc) at the witness. This needs, besides witness existence, on-line abundance (balance) of $f_t$, which is
  OPEN (Cor F, second clause). Moreover balance ($\gg R\log R$ distinct on-line ordinates, Levinson/Conrey) is itself one of the inputs of R163_401 §4.1 / R163_603 T5.1;
  a falsifier excludes an argument only if it satisfies every input the argument uses, and $f_t$ is not known to satisfy this one.

With F′, "atoms on log-integers up to the contact" is also not enough (ARGUED). What is left among the listed inputs is the numerical vector
$(\Lambda(n))_{e^{2T_0}\le n<e^{2T_c}}$, which by Thm 1.3 means exactly proving $W^\zeta_{T_c}\succeq0$. Integrality is satisfied by all the falsifiers $f_t$ (trivially),
and on ζ's exact window it is idle (Thm 1.3).

*Separators.* Hamburger rigidity is the only separator of ζ from the $f_t$ family **identified among the listed inputs**; it is not the only structural separator.
Properties of ζ that are *not* among the listed inputs and that do separate ζ from every $f_t$: (a) the Euler product / prime-power support of $-f'/f$
($\log\mathbb N$-support is the weak form; R163_114 shows it has RH strength for the exchange; F′ has it only below the contact and only generically);
(b) on-line abundance (Levinson/Conrey), used by balance and not available for $f_t$; (c) the Riemann–Siegel / approximate-functional-equation structure of $Z(t)$
used in R163_603 §2 (Dirichlet-polynomial length $\sqrt{t/2\pi}$ refers to integer frequencies). Each is global in the same sense as Hamburger (none is a window
statement), so the conclusion that no *window-level* structural input separates survives; the uniqueness claim does not.

*Caveat on the integrality-defect programme.* The phase-163 programme (R163_102 Thm R, R163_803) concerns integrality **together with** $\log\mathbb N$-support of the
prime side (R163_114), which $f_t$ lacks and F′ has only below the contact and only generically. So "the programme cannot supply (A-loc)" is established only against
the *atomic* abstraction of that programme, not against its actual hypothesis.

**(A-loc): OPEN. $(\star_{\rm cell})$: OPEN. Row D: OPEN.**
New here: the collapse Thm 1.3 (the §6 question is ¬RH at window scale, with ζ as the realiser, and integrality is idle); the self-dual hole measures
(Lemma 2.1; finite-lattice instance of Bochner / Kahane–Mandelbrojt); the falsifier family $f_t=\zeta+tg$ (Thm F) with exact Γ_R functional equation, integer zeros,
atomic prime side on a discrete semigroup agreeing with ζ's below $\lambda_1$, off-line zeros and a finite contact — a strictly better falsifier than DH (own Γ and
coefficients) and than $M_m$ (non-atomic); variant F′; the three-way split of the meta-statement; the list of candidate separators.
