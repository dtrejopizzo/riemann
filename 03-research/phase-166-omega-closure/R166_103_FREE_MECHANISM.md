# R166_103 — Free mechanism: bilinear/Selberg (α), power-determined tail (β), θ−1 moments (γ)

Phase 166, round 6. Single pass, pure mathematics.
Labels: PROVED / PROVED-CITED / ARGUED / OPEN. **No sign is asserted; (★_cell) and row D remain OPEN.**

Prior reading (grid rule §0): R162_2300 §0, §3, §4, §7; phase-166 README and R166_190 §0; R164_190 (round 2
synthesis and rounds 3–4); R165_190; R163_401 §§1–4, box, §4.11; R163_801 Thm 3, Cor 3.1, Thm 5. Paper 48 only
for the tab:falsifiers rows collected in grid §4.

Notation: $X=e^{2T_c}$, $z=-\tfrac12+ix$, $s=\tfrac12-ix$ (so $\mathrm{Im}\,x>\tfrac12\iff\mathrm{Re}\,s>1$),
$G=\widehat F$ of the witness (real-rooted, type $T_c$, nodes $X$ = real zeros of $G$),
$\mathcal T_X(x)=\sum_{n\ge X}\Lambda(n)n^{z}$ R163_801 (3.1)'s tail,
$\Phi(x)=\sum_\rho G(t_\rho)^2/(t_\rho-x)=C_T(x)-iG(x)^2\mathcal T_X(x)$.

---

## Status table

| # | statement | label | wall stopping it |
|---|---|---|---|
| L1 | Locality of convolution: on $(0,U)$, $\mu*\nu$ depends only on $\mu|_{(0,U)},\nu|_{(0,U)}$; every bilinear/Selberg identity with tests of type $\le 2T$ is window data | PROVED | f_t (W3, window datum) |
| L2 | Selberg $F''/F=(F'/F)'+(F'/F)^2$ is formal (holds for anything meromorphic); its zero side is the divided-difference form of $h$ over the zero set; the quartet pair $(\rho,1-\bar\rho)$ contributes $\mathrm{Im}\,G(t_q)^2/\delta_q$, not $\mathrm{Re}\,G(t_q)^2$ | PROVED | M_m (zeros only) + wrong phase |
| L3 | ζ's own content in Selberg = $\mu*\log^2$, i.e. integer coefficients of $1/\zeta$ on ℕ | PROVED (reading) | W3′ / W-identification |
| B1 | **Tail decomposition.** $\mathcal T_X=\mathcal T^{\rm det}_X+\mathcal T^{\rm new}_X$; $\mathcal T^{\rm det}_X$ is an explicit finite sum of window data, holomorphic for $\mathrm{Im}\,x>-\tfrac12$; $\mathcal T^{\rm new}_X=-(\zeta_{\ge X}'/\zeta_{\ge X})(s)$ with $\zeta_{\ge X}$ the zeta of $X$-rough integers | PROVED | — (tool) |
| B2 | Every off-line residue of (3.1) is carried by $\zeta_{\ge X}$: $\Phi=C^+_T-iG^2\mathcal T^{\rm new}_X$ with $C^+_T$ holomorphic for $\mathrm{Im}\,x>0$ except $x=\tfrac i2$ | PROVED (given (3.1); at the witness ARGUED as (3.1)) | — (tool) |
| B3 | Separation: f_t, f_χ do not admit the decomposition with a new part ≥ 0 of prime support; M_m has new part = ζ's plus a non-atomic, mixed-sign density; deletion has **the same** new part as ζ | PROVED (f_t via Cor R.3: PROVED-CITED) | — |
| B4 | Positivity of the new part is blind to zeros without FE (Thm A's ζ_B) and with FE + window identifies ζ (Cor R.1) | PROVED-CITED | W-Landau / W-identification |
| B5 | Individual use of positivity: (i) as an inequality = Prop 4 with the new tail, falls under Thm 3.1 (discarded term); (ii) in its strongest form = Landau's one-sided criterion over new primes, ⟺ a zero-free half-plane | (i) PROVED-CITED; (ii) PROVED-CITED (Landau) | W2/M + Thm 3.1; E1 |
| G1 | Falsifier $P_{a,c}=\zeta(s)\,[1+c\cosh((s-\tfrac12)\log a)]$: θ−1 > 0, exact FE with Γ(s/2), order 1, pole at 1, infinitely many off-line zeros in the strip | PROVED | (γ) dies without the window |
| G2 | $W_T$ is not a moment of θ−1: the map coefficients ↦ $W$ is not affine; only $\xi(\rho)=0$ is a linear moment | PROVED | Markov–Krein premise false |
| G3 | With the comb's exact window + positivity + FE: class {ζ} (Thm R) | PROVED-CITED | W-identification |
| Σ | No mechanism of (α)(β)(γ) evades R166_190 §0's dichotomy; stops at the §4 box | ARGUED (synthesis of L1–G3) | — |

---

## §0 Declared cells and walls (grid rule §0)

- (α) row 6 (Λ values) × column C (quadratic functionals): **6C ◩**; nearest route R162_2301 (Selberg
  difference channel, NO-GO) and R163_802 (Selberg invariant regions, NO-GO). Wall it had to evade: E1 (the
  product test is a test) and W3 (Selberg holds under Beurling DMV).
- (β) row 4 (Euler) × column F (global transforms): **4F ◧**; nearest routes R163_801 Thm 3, R164_102 (positive
  tail, Thm A), R164_401 (Thm R), R164_501 Prop 4, R164_601 Thm 3.1. Wall it had to evade: W-Landau (Thm A) via
  the determined part, which f_t and f_χ lack.
- (γ) row 2 (positivity) × column F: **2F ◩**, and 5F for theta periodicity (R163_1001). Nearest route: grid §4
  "positive theta kernels with off-line zeros" (103_15–30). Wall it had to evade: W3′ (f_χ has mixed-sign theta).

---

## §1 Direction (α): bilinear identities and Selberg

**Lemma L1 (locality of convolution). PROVED.** Let μ, ν be measures (or finite-order distributions) supported
on $(0,\infty)$. Then $(\mu*\nu)|_{(0,U)}$ depends only on $\mu|_{(0,U)}$ and $\nu|_{(0,U)}$.
*Proof.* $\langle\mu*\nu,\varphi\rangle=\iint\varphi(u+v)\,d\mu(u)d\nu(v)$; if $\mathrm{supp}\,\varphi\subset(0,U)$ and $u,v>0$, the
integrand vanishes except for $u,v<U$. ∎

*Consequences (PROVED).* (a) The coefficients of $(F'/F)^2$, of $F''/F$ and of $1/F$ on $(0,U)$ (in log scale)
depend only on $F$'s log measure on $(0,U)$ (Dirichlet: $\exp_*$ and inverses are convolution series). (b)
Hence, for every bilinear test $h=h_1h_2$ or tensor test $h_1\otimes h_2$ whose prime side lives at $|u|<2T$
(tests of type $\le2T$, e.g. the witness's $G^2$), the arithmetic side of the bilinear identity is **window
data**: $\Lambda*\Lambda$ and $\mu*\log^2$ at $n<e^{2T}$. (c) f_t (R163_901 Thm F) has the same log measure as ζ
on $(0,2T_0)$, so the same bilinear identities for $T\le T_0$. **(α) with Paley–Wiener tests dies by f_t.**

**Lemma L2 (Selberg is formal; zero side = divided differences). PROVED.**
(i) For any meromorphic $F$, $F''/F=(F'/F)'+(F'/F)^2$. So Selberg's identity
$\Lambda*\Lambda=\mu*\log^2-\Lambda\log$ holds, with its own coefficients, for every Dirichlet series with
non-zero constant term (Beurling DMV, f_t, f_χ).
(ii) At a simple zero ρ, $F'/F=\frac1{s-\rho}+A_\rho+O(s-\rho)$ with $A_\rho=F''(\rho)/(2F'(\rho))$. For $F$ of
order 1, Hadamard gives $A_\rho=B+\tfrac1\rho+\sum_{\rho'\ne\rho}\big(\tfrac1{\rho-\rho'}+\tfrac1{\rho'}\big)+(\Gamma\text{ and pole})$:
**a datum of the zero set**. The residue of $h\,(F'/F)^2$ at ρ is $h'(\rho)+2h(\rho)A_\rho$, and the pair part is
$\sum_{\rho\ne\rho'}\frac{h(\rho)}{\rho-\rho'}=\tfrac12\sum_{\rho\ne\rho'}\frac{h(\rho)-h(\rho')}{\rho-\rho'}$, the
Loewner/divided-difference form of $h$ over the zeros (R163_801 Prop 4's world).
(iii) *Quartet contribution.* In variable $t$, the pair $t_q=\gamma-i\delta$, $\bar t_q=\gamma+i\delta$ with $h$
real on ℝ ($h(\bar t)=\overline{h(t)}$) gives $\frac{h(t_q)-h(\bar t_q)}{t_q-\bar t_q}=\frac{2i\,\mathrm{Im}\,h(t_q)}{-2i\delta}=-\frac{\mathrm{Im}\,h(t_q)}{\delta}$.
With $h=G^2$: $-\mathrm{Im}\,G(t_q)^2/\delta=-|G(t_q)|^2\sin2(\cdot)/\delta$ in R165_201 Cor 2.2's notation. **The
quartet's singular $1/\delta$ term carries the sine of the phase, not the cosine that decides (★_cell).** ∎

*Reading (PROVED as a consequence of L2(ii)).* Any claim about the bilinear identity's zero side is a claim
about the zero set and holds for M_m with its zeros (R163_801 Thm 5). If a Cauchy kernel $h=G^2/(\cdot-x)$ is
used to exit the window, the prime side is $(\Lambda*\Lambda)$ above $X$, which is (3.1)'s tail squared plus
window terms (L1): nothing new.

**Lemma L3 (ζ's own content in Selberg). PROVED (reading).** By L2(i), the only thing distinguishing Selberg's
identity for ζ is the term $\mu*\log^2$ with $\mu$ ℕ's Möbius function, i.e. that $1/\zeta$ be a Dirichlet series
with bounded integer coefficients supported on ℕ. That is frequency/coefficient integrality: W3′ (f_χ with
conductor 7) or identification (Hamburger/Thm O at conductor 1). Matches R163_802 and R164_502 L7.

**Verdict (α): DEAD.** Type-≤2T tests: window data (f_t, L1). Zero side: zero-set datum (M_m, L2(ii)), and the
quartet's singular term has the wrong phase (L2(iii)). ζ's own arithmetic content: W3′/identification (L3). No
wall evaded.

---

## §2 Direction (β): tail determined by the window + new primes

**Theorem B1 (tail decomposition). PROVED.** For $X>2$ and $\mathrm{Im}\,x>\tfrac12$,
$$
\mathcal T_X(x)=\underbrace{\sum_{p<X}\log p\;\frac{p^{k_pz}}{1-p^{z}}}_{\mathcal T^{\rm det}_X(x)}\;+\;
\underbrace{\sum_{p\ge X}\log p\;\frac{p^{z}}{1-p^{z}}}_{\mathcal T^{\rm new}_X(x)},\qquad k_p=\min\{k\ge1:p^k\ge X\}.
$$
(a) $\mathcal T^{\rm det}_X$ is a **finite** sum whose data ($\{p<X\}$, $\log p$) are the window's
$(\Lambda(n))_{n<X}$; since $|p^z|=p^{-1/2-\mathrm{Im}\,x}$, each summand is holomorphic for $\mathrm{Im}\,x>-\tfrac12$
(poles only at $\mathrm{Im}\,x=-\tfrac12$, where $p^z=1$).
(b) $\mathcal T^{\rm new}_X(x)=-\frac{\zeta_{\ge X}'}{\zeta_{\ge X}}(s)$, with
$\zeta_{\ge X}(s)=\zeta(s)\prod_{p<X}(1-p^{-s})=\sum_{P^-(n)\ge X}n^{-s}$ (the zeta of $X$-rough integers,
coefficients in $\{0,1\}$, log-coefficients $\Lambda(n)\mathbf 1_{P^-(n)\ge X}\ge0$).
(c) $\zeta_{\ge X}$ has exactly ζ's zeros for $\mathrm{Re}\,s>0$, with multiplicity, and the simple pole at $s=1$.
*Proof.* The $n\ge X$ with $\Lambda(n)\ne0$ are $p^k\ge X$: if $p\ge X$, every $k\ge1$; if $p<X$, $k\ge k_p$.
Summing the geometric series gives (a)–(b). (c): the finite product $\prod_{p<X}(1-p^{-s})$ is entire and
non-vanishing for $\mathrm{Re}\,s>0$. ∎

**Corollary B2 (where off-line residues live). PROVED given (3.1)** (at the witness, ARGUED to the same degree
as (3.1)). $\Phi(x)=C^+_T(x)-iG(x)^2\mathcal T^{\rm new}_X(x)$, with $C^+_T:=C_T-iG^2\mathcal T^{\rm det}_X$. By
R163_801 Cor 3.1(a) and B1(a), $C^+_T$ is holomorphic for $\mathrm{Im}\,x>0$ except the pole at $x=\tfrac i2$,
which cancels $\mathcal T^{\rm new}_X$'s (the pole $s=1$ lives in $\zeta_{\ge X}$). Every off-line residue
$G(t_q)^2$ is carried by $\zeta_{\ge X}$; the determined part, though above the window, is holomorphic on the
whole strip and carries none. ∎

*This is what (β) contributes, new relative to R163_801 Cor 3.1(c):* the tail is not "all Λ above X" but only
the new-primes part; the window's prime powers are resolved explicitly and are harmless.

**Proposition B3 (falsifier separation). PROVED unless noted.**
- f_t: has no Euler product; its log measure has atoms off $\log\mathbb N$ and negative coefficients off ℕ
  (R164_401 Cor R.3, PROVED-CITED). It does not admit $\mathcal T=\mathcal T^{\rm det}_\zeta+(\text{measure}\ge0\text{ on }p^k,\ p\ge X)$.
- f_χ: no Euler product, 7-periodic mixed-sign coefficients; does not admit the decomposition (PROVED,
  R163_1001 Lem 1.1).
- M_m: $-M_m'/M_m=-\xi'/\xi-\sum_jR_j'/R_j$; above the window its new part is ζ's plus the density
  $\sum_j4\cos(\gamma_ju)\cosh(\delta_ju)$ (R163_801 Thm 5 extended to $u\ge2T$), non-atomic and mixed-sign.
  Separated.
- Λχ₂: Euler product, new part $\Lambda(n)\chi_2(n)$ mixed-sign. Separated by sign (not an off-line-zero
  falsifier).
- **Deletion** $D=\zeta\exp(\sum_{n<5}\Lambda(n)n^{-s}/\log n)$: **the same new part as ζ** (deletion only touches
  the window) and a negative form at $T\le0.4608$ with no off-line zeros (R164_101 Prop D). So the new part
  alone does not give the sign: the sign demands window + FE, as Prop D already said.

**Proposition B4 (positivity of the new part as a class property). PROVED-CITED.**
(i) Without FE: R164_102 Thm A's $\zeta_B=\zeta\cdot E$ has ζ's window, the same determined part as ζ (window
prime powers unchanged), new part $\ge0$ (ζ's plus the positive density $r$), and an off-line zero at arbitrary
$\beta+i\gamma$. The new part's positivity is blind to the zeros (W-Landau: it only sees the real-axis pole).
(ii) With ζ's FE, Γ_ℝ and simple poles: every positive Beurling system with ζ's window is ζ (R164_401 Cor R.1).
The class defined by (β) is {ζ}: **W-identification**.

**Proposition B5 (individual use of positivity). (i) PROVED-CITED; (ii) PROVED-CITED.**
(i) *As an inequality.* Combining B1 with R164_501 Prop 4:
$\sum_\rho\Psi_y(t_\rho)=\big[\mathfrak A_y-G(iy)^2\mathcal T^{\rm det}_X(iy)\big]-G(iy)^2\mathcal T^{\rm new}_X(iy)$,
$y>\tfrac12$. The bracket is explicit (window datum) and the last term carries a sign. Discarding it is an
inequality holding for ζ's true zeros whatever they are (R164_601 Thm 3.1); excluding a quartet requires a lower
bound independent of the other terms, which is weighted (★_cell) (Thm 3.2), and the Fejér ceiling + archimedean
term only give $\tfrac12-\delta_q\le c/\log\gamma_q$ (Thm 3.3; W2/M). The determined part changes nothing: it
only moves an explicit term between the bracket and the tail.
(ii) *In its strongest form.* Since $\psi(x)-\psi^{\rm new}_X(x)=\sum_{p<X,\ p^k\le x}\log p\le\pi(X)\log x$, for
every $\theta\in[\tfrac12,1)$: $\psi^{\rm new}_X(x)\ge x-Cx^{\theta}$ for $x\ge x_0$ implies ζ has no zeros for
$\mathrm{Re}\,s>\theta$ (Landau's theorem for Laplace–Stieltjes integrals of measures $\ge0$, applied to
$d(\psi^{\rm new}_X(x)-x+Cx^\theta)$; classical one-sided criterion, Ingham ch. IV / Montgomery–Vaughan §15.1,
CITED), and the converse holds with $x^\theta\log^2x$. That is: new-prime positivity controls complex poles only
once the convergence abscissa is lowered to $\theta$, and lowering it while keeping a sign is a one-sided
criterion **equivalent** to a zero-free half-plane. For $\theta=\tfrac12$ it is RH: **E1**. (Mertens's 3–4–1
version only sees poles on the convergence axis $\mathrm{Re}\,s=1$.)

**Verdict (β): DEAD as a route, with a new tool (B1–B2).** The determined part exists and separates
f_t/f_χ/M_m, but it is holomorphic on the whole strip (B1(a)), so it carries no information about the quartet:
all the information is in $\zeta_{\ge X}$, whose positivity is blind without FE (B4(i)), identifies with FE
(B4(ii)), and used individually is Thm 3.1 or Landau (B5). Deletion shares exactly the new part (B3). Wall
evaded: none; the determined part evades f_t but not W-Landau, and W-Landau + FE is W-identification.

---

## §3 Direction (γ): positivity of θ−1 and moment space

Let $\psi_a(x)=\sum_n a_ne^{-\pi n^2x}$ (more generally $\sum_\lambda c_\lambda e^{-\pi\lambda^2x}$); for ζ,
$a\equiv1$ and $\psi=\tfrac12(\theta-1)>0$, $\pi^{-s/2}\Gamma(s/2)\zeta(s)=\int_0^\infty\psi(x)x^{s/2-1}dx$
($\mathrm{Re}\,s>1$).

**Proposition G1 (theta-positive falsifier with FE). PROVED.** Let $a>1$, $L=\log a$, $0<c<1$ with
$\operatorname{arccosh}(1/c)<L/2$, and $K(s)=1+c\cosh((s-\tfrac12)L)$, $P_{a,c}=\zeta\cdot K$. Then:
(i) $P_{a,c}(s)=\sum_n n^{-s}+\tfrac c2a^{-1/2}\sum_n(n/a)^{-s}+\tfrac c2a^{1/2}\sum_n(na)^{-s}$: frequencies on
$\mathbb N\cup a^{-1}\mathbb N\cup a\mathbb N$, coefficients $>0$; its theta $\sum c_\lambda e^{-\pi\lambda^2x}$ is $>0$.
(ii) $K(1-s)=K(s)$, so $\pi^{-s/2}\Gamma(s/2)P_{a,c}(s)$ is invariant under $s\mapsto1-s$; simple poles at $0,1$;
order 1.
(iii) $K(s)=0\iff\cosh(wL)=-1/c$, $w=s-\tfrac12$, $\iff wL=\pm\operatorname{arccosh}(1/c)+i\pi(2k+1)$; since $1/c>1$,
$\mathrm{Re}\,w=\pm\operatorname{arccosh}(1/c)/L\in(-\tfrac12,\tfrac12)\setminus\{0\}$: infinitely many off-line
zeros in the strip.
*Proof.* Direct computation. ∎
It violates Thm R's gap (frequencies $n/a<1$ and new atoms on $[1,X)$), so it does not contradict Thm R. It
belongs to the grid §4 family "positive theta kernels with off-line zeros" (103_15–30); possibly a duplicate,
here with an exact FE and Γ(s/2). f_χ has mixed-sign theta, but $P_{a,c}$ takes its place as a falsifier:
**positivity of θ−1 + FE + Γ(s/2) does not separate.**

**Proposition G2 (W is not a moment of θ−1). PROVED.** The map $a\mapsto W^{a}_T(F)$ (the Weil form of the
series $A=\sum a_nn^{-s}$, defined via its log-derivative measure) is not affine in $a$, while
$a\mapsto\psi_a$ and $a\mapsto\int\psi_a x^{s/2-1}dx$ are.
*Proof.* $-A'/A$'s coefficients are $b_2=a_2\log2$, $b_4=\log2\,(2a_4-a_2^2)$ (with $a_1=1$): quadratic in
$a_2$. For $T>\tfrac12\log4$, the term $v_4$ enters $\sigma_T$ and $W^a_T(F)$ depends on $a_2^2$ with
coefficient $\propto\int c_F(u)\delta_{\log4}$, non-zero for generic $F$. ∎
*Consequence.* (γ)'s premise — "two exact vanishings of Mellin-type integrals of the positive function θ−1" —
is false: $\xi(\rho^*)=0$ is a moment (linear in ψ), but $W_{T_c}(F)=0$ is linear in Λ, a non-affine function of
ψ. A Chebyshev/Markov–Krein argument (convexity of a positive measure's moment space) only controls conditions
linear in the measure; over the single condition $\xi(\rho^*)=0$ with ψ > 0 and FE, G1 gives countermodels.
(That the complex condition $\int\psi K_{\rho}=1/(\rho(1-\rho))$ is compatible with ψ > 0 is what G1(iii) shows
explicitly.)

**Proposition G3 (with the comb's exact window). PROVED-CITED.** If, moreover, the frequency measure matches
ζ's comb on $[1,X)$, $X>1$, and is $\ge0$ off ℕ, with ζ's FE and poles, then it is ζ (R164_401 Thm R). Class
{ζ}: W-identification. "Using the exact window part" of self-duality, as (γ) proposes, is exactly Thm R's
hypothesis.

**Verdict (γ): DEAD.** Without a window: G1. With a window: G3. The "moments" form is inapplicable by G2. Wall
evaded: W3′ indeed (f_χ is separated by θ's sign), but it falls under G1 and W-identification.

---

## §4 Stop (box)

$$
\boxed{\begin{array}{c}
\text{(α), (β), (γ) closed. Tool B1–B2 localizes every off-line residue in }\zeta_{\ge X}=\zeta\prod_{p<X}(1-p^{-s})\\
\text{(the window-determined tail part is holomorphic on the whole strip). What is missing is an exact relation,}\\
\text{non-linear and non-Paley–Wiener, between }\zeta_{\ge X}\text{ on }\tfrac12<\mathrm{Re}\,s<1\text{ and the witness reading }\cos2(\Phi_Z\pm\pi\omega(E)+\Psi_{\rm out}),\\
\text{and not its sine (L2(iii)); every sign property of }\zeta_{\ge X}\text{ is either blind (B4(i)), identifies (B4(ii)), or is Landau (B5(ii)).}
\end{array}}
$$

Precise form of the stop: a closing mechanism has to (1) be non-affine in Λ above $X$ (otherwise it is (3.1)'s
tail: E1/Thm 3.1); (2) not factor through type-$\le2T$ tests (L1: f_t); (3) not be a function of the zero set
(L2: M_m); (4) use the new part $\zeta_{\ge X}$ below its convergence axis without going through a one-sided
bound (B5(ii): E1); (5) read $G(t_q)^2$'s real part. None of the three candidates satisfies (1)+(4).

---

## §5 Falsifiers

| model | (α) bilinear | (β) det + new ≥ 0 | (γ) θ−1 > 0 |
|---|---|---|---|
| M_m | shares (L2(ii): zero datum) | separated (mixed density) | n/a (not Dirichlet) |
| f_t | shares at type ≤2T (L1) | separated (Cor R.3) | separated if coef. <0 in its theta (unverified) |
| f_χ | shares formal Selberg (L2(i)) | separated | separated (mixed theta) |
| Λχ₂ | shares formal Selberg | separated by sign | — |
| deletion | shares on the window except $n<5$ | **same new part as ζ** | — |
| ζ_B (Thm A) | — | **shares** (no FE) | — |
| $P_{a,c}$ (G1) | — | — | **shares** (with FE) |

---

## §6 Ledger

| item | label |
|---|---|
| L1 convolution locality; (α) PW = window datum | PROVED |
| L2 formal Selberg; zero side = divided differences; quartet ↦ $-\mathrm{Im}\,G(t_q)^2/\delta$ | PROVED |
| L3 ζ's own content = $\mu*\log^2$ = W3′/identification | PROVED (reading) |
| B1 decomposition $\mathcal T=\mathcal T^{\rm det}+\mathcal T^{\rm new}$; det holomorphic for $\mathrm{Im}\,x>-\tfrac12$; new = $-\zeta_{\ge X}'/\zeta_{\ge X}$ | PROVED |
| B2 off-line residues only in $\zeta_{\ge X}$ | PROVED given (3.1); ARGUED at the witness |
| B3 falsifier separation; deletion shares the new part | PROVED (f_t via Cor R.3, PROVED-CITED) |
| B4 blind without FE / identification with FE | PROVED-CITED (R164_102 Thm A, R164_401 Cor R.1) |
| B5(i) Thm 3.1 with the new tail; B5(ii) one-sided Landau ⟺ zero-free half-plane | PROVED-CITED |
| G1 $P_{a,c}$ | PROVED |
| G2 W non-affine in the coefficients | PROVED |
| G3 comb's window ⟹ ζ | PROVED-CITED (Thm R) |
| §4 box | ARGUED (synthesis) |
| (★_cell), row D | OPEN |

## §7 Grid entries (editor)

- 6C: R166_103α — bilinear/Selberg, DEAD [W3:f_t (L1); M_m (L2); W3′/W-identification (L3)]; supersedes nothing;
  partial dup R162_2301, R163_802.
- 4F: R166_103β — determined tail + new primes, DEAD [W-Landau; W-identification; Thm 3.1; E1 (Landau)];
  PROVED-TOOL B1–B2 (localization in $\zeta_{\ge X}$).
- 2F: R166_103γ — θ−1 moments, DEAD [G1 $P_{a,c}$; G2; W-identification]; possible dup of 103_15–30.
- grid §4: add the $P_{a,c}$ row (θ−1>0, exact FE Γ(s/2), off-line zeros; refutes "theta positivity + FE
  suffices").
- No cell symbol changes; no live residual closes.
