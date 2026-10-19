# R165_201 — Critical interlacing (§2.1–§2.2 of R165_000): exact phase identity and the cone question

**Status:** memo A3. Pure math, no numerics. Cells **7A** (D.16-γ "cone cut by the zero data") and
**2A**. Corpus check: "interlacing" of zero sets (witness nodes against on-line zeros) is absent from the corpus
(R165_000 header). Hermite–Biehler and Chebotarev are classical and are CITED.

**Verdict, in one line.** Critical interlacing does **not** force the quartet out of the light cone. Theorem 3 gives an exact
counterexample at exactly critical density: perfect global interlacing together with a strictly negative quartet. What
interlacing does give is an exact identity (Theorem 2). It fixes the quartet sign by three quantities: the phase of
$Z_{\rm on}$ at $t_q$, the harmonic measure $\omega$ of the node–zero offset set, and an outside remainder.
The offset measure ranges over an interval of length $>\pi/2$. So the sign is carried by **where the nodes sit inside their
cells**, which is witness data (Rem 4.8a circularity, unchanged).

## Status table

| Item | Statement | Label |
|---|---|---|
| Conv. 0 | conventions: $G$, $\Xi$, $Z_{\rm on}$, $Q_q$, $\theta_t$ | definitions |
| Prop 1(a) | real zero set of $\Xi$ $=\Gamma$; $N_\Gamma(T)=N(T)-2\#\{q:\gamma_q\le T\}$ | PROVED |
| Prop 1(b) | "local gap of two zeros" is not determined by $N$ (an $S$-increment of size ≥ 2 is not excluded) | PROVED (as a non-implication) / gap heuristic ARGUED |
| Prop 1(c) | local HB: $P_I,Q_I$ interlace ⇒ $Q_I+i\epsilon P_I$ has all zeros in one open half-plane | PROVED-CITED (Hermite–Biehler/Obreschkoff) |
| Prop 1(d) | global: $G,Z_{\rm on}$ interlace on ℝ ⇒ $G/Z_{\rm on}=c\cdot$(Pick function) | PROVED-CITED (Chebotarev; Levin Ch. VII) + PROVED (no exponential factor) |
| Prop 1(e) | what breaks: $G/\Xi$ is never Pick under ¬RH (poles at $\pm t_q,\pm\bar t_q$); the real-zero interlacing does not see the quartet | PROVED |
| Lemma 2.0 | $\theta_t(x)=\pi\,\omega_{\bar t}((x,\infty))$ | PROVED |
| **Thm 2** | exact identity $\Theta_X(t)=\Theta_\Gamma(t)+\pi\,\omega_{\bar t}(E^+)-\pi\,\omega_{\bar t}(E^-)+\Psi_{\rm out}$; under (EC) one orientation, so $0\le\Theta_X-\Theta_\Gamma-\Psi_{\rm out}<\pi\,\omega_{\bar t}(\mathrm{hull}\,I)$ | PROVED |
| Prop 2.1 | $\Phi_Z\equiv\arg\Xi'(t_q)+\tfrac\pi2+\beta_q\pmod\pi$, $\beta_q=\arctan(\delta_q/\gamma_q)$ | PROVED |
| Cor 2.2 | $4\,\mathrm{Re}\,G(t_q)^2=4|G(t_q)|^2\cos2\big(\Phi_Z+\pi\omega_{\bar t_q}(E)+\Psi_{\rm out}\big)$ | PROVED |
| **Thm 3** | (EC) ⇏ quartet positive: (a) the explicit pair $\sin(\pi\rho z)$, $\cos(\pi\rho z)$; (b) for any $\Gamma$, $t$ and $I$ with $\omega_{\bar t}(\mathrm{hull}\,I)>\tfrac12$, interlaced finite moves of the nodes realise both signs | PROVED |
| Cor 3.1 | when the cell is narrow ($|x_1-x_0|\ll\delta$), the sign is locked to $\cos2(\Phi_Z+\Psi_{\rm out})$; this is a property of the on-line data + outside nodes | PROVED (with explicit error) |
| §4 lattice model | (EC) is impossible in Lemma 4.10's regime ($T<\pi\rho$); consistent | PROVED |
| §4 $M_m$ | no contradiction; the content moves to the offset measure $\omega(E)$, not to "interlaced or not" | PROVED (logic) |

---

## 0. Conventions

- $F$ is a witness at $T=T_c$: real, parity-definite and real-rooted. $G:=\widehat F$ (even case) or $G:=-i\widehat F$ (odd case).
  $G$ is real on ℝ, has parity and $G=c\,z^m\prod_{X_+}(1-z^2/x^2)$, with no exponential factor (R163_401 Lemma 3.1(a)).
  The witness only enters through $G$, since $\widehat F\widehat F^\#=G^2$.
- $\Xi(z):=\xi(\tfrac12+iz)$. A zero $\rho=\tfrac12+\delta_q+i\gamma_q$ ($\delta_q>0$) maps to $z=\gamma_q-i\delta_q=:t_q$.
  Its quartet maps to $\{t_q,\bar t_q,-t_q,-\bar t_q\}$.
- $Q_q(z):=(1-z^2/t_q^2)(1-z^2/\bar t_q^2)$ is real-even, and on ℝ we have $Q_q(x)=|1-x^2/t_q^2|^2>0$. Define
  $$Z_{\rm on}:=\Xi\Big/\prod_qQ_q .$$
  This is even, real, of order 1, with only the real zeros $\Gamma$ (the on-line ordinates), so it lies in Laguerre–Pólya (LP).
  (The product over quartets converges because $\sum|t_q|^{-2}<\infty$. When only one quartet matters, divide only by
  that one; the other quartets enter as smooth factors in $\Psi_{\rm out}$.)
- For $t=\gamma-i\delta$, $\delta>0$, and real $x$, put $\theta_t(x):=\arg(x-t)\in(0,\pi)$. By R163_401 Lemma 3.3,
  $\arg G(t)\equiv\Theta_X(t):=\sum_{x\in X}\theta_t(x)\pmod\pi$. Here we use $\theta_t(x)\equiv\arctan(\delta/(x-\gamma))$ mod
  π and pair the $\pm x$ terms. Likewise $\arg Z_{\rm on}(t)\equiv\Theta_\Gamma(t)=:\Phi_Z$ and $\Phi_F:=\Theta_X(t)$.
- Throughout, $\operatorname{sign}\mathrm{Re}\,G(t)^2=\operatorname{sign}\cos2\Phi_F$ (Lemma 3.3), and the quartet is
  negative iff $\Phi_F\in(\pi/4,3\pi/4)$ mod π.

## 1. Algebra (§2.1 made precise)

**Prop 1.**

(a) **PROVED.** The real zero set of $\Xi$ is $\Gamma$ (with multiplicity), since $\prod Q_q>0$ on ℝ.
$N(T)$ counts $\rho$ and $1-\bar\rho=\tfrac12-\delta_q+i\gamma_q$, both of which have ordinate $\gamma_q$. Hence
$N_\Gamma(T)=N(T)-2\#\{q:0<\gamma_q\le T\}$ exactly, and $N$ jumps by 2 at $\gamma_q$ from the quartet. In the $z$-plane
these are the two points $\gamma_q\mp i\delta_q$ at abscissa $\gamma_q$.

(b) **PROVED (non-implication).** For $I=[\gamma^*-\Delta,\gamma^*+\Delta]$,
$\#(\Gamma\cap I)=\frac{\Delta}{\pi}\log\frac{\gamma^*}{2\pi}+[S]_{\gamma^*-\Delta}^{\gamma^*+\Delta}-2+O(\Delta^2/\gamma^*)$.
The two zeros are therefore missing **from the count**, not from a definite place. Whether $\Gamma$ has a visible
"hole" near $\gamma^*$ depends on the increment of $S$. That increment is $O(\log\gamma^*)$ and is not known to be
$<2$ in absolute value on any prescribed short window (Selberg: its typical size is $\asymp\sqrt{\log\log\gamma}$).
The picture "the pair that moved off leaves a gap" is HEURISTIC (ARGUED); no statement below uses it.

(c) **PROVED-CITED** (Hermite–Biehler for polynomials; Obreschkoff, *Verteilung und Berechnung der Nullstellen reeller
Polynome*, Satz on interlacing). Let $P_I=\prod_{x\in X\cap I}(z-x)$ and $Q_I=\prod_{g\in\Gamma\cap I}(z-g)$, with simple
roots that strictly interlace. Then $Q_I+i\epsilon P_I$ ($\epsilon=\pm1$, fixed by the orientation) has all its zeros in
one open half-plane. Equivalently, $P_I/Q_I$ maps $\mathbb C_+$ into a half-plane.

(d) **PROVED-CITED + PROVED.** Suppose $X$ and $\Gamma$ (simple) strictly interlace on all of ℝ. By Chebotarev's theorem
(Levin, *Distribution of Zeros of Entire Functions*, Ch. VII §1; *Lectures on Entire Functions*, Lect. 27),
$$G/Z_{\rm on}=e^{h}\cdot c\,\frac{z-a_0}{z-b_0}\prod_k\frac{1-z/a_k}{1-z/b_k},$$
where the product is $\pm$ a Pick function and $h$ is entire and real. Both $G$ and $Z_{\rm on}$ are even or odd with
Hadamard products free of exponentials (Lemma 3.1(a); $\Xi$ is even of genus 1, and dividing by the even $Q_q$ keeps
this). The canonical products then pair the $\pm$ roots and $h$ is constant. So $G/Z_{\rm on}=c\cdot$Pick, and
$Z_{\rm on}-i\epsilon cG$ is of Hermite–Biehler class.

(e) **What breaks. PROVED.** For the pair $(G,\Xi)$: $G/\Xi=(G/Z_{\rm on})/\prod Q_q$ has non-real poles at
$\pm t_q,\pm\bar t_q$, so it is never Pick under ¬RH, whatever the interlacing. The pair $(G,Z_{\rm on})$ is a
genuine HB pair under global (EC). The quartet is **invisible to the real-zero interlacing**. It enters only through
the factor $Q_q$ and through the evaluation point $t_q$. The claim of R165_000 §2.1 ("the quartet cell is the unique
cell where the pair loses HB") is therefore correct only in this sense: HB fails for $(G,\Xi)$ because of $Q_q$, not
because of a defect in the real interlacing. ∎

## 2. Geometry (§2.2): the exact phase identity

**Lemma 2.0. PROVED.** Let $w:=\bar t=\gamma+i\delta\in\mathbb C_+$ and let $\omega_w$ be the harmonic measure of
$\mathbb C_+$ at $w$, i.e. the Poisson measure $P_\delta(\cdot-\gamma)\,du$. Then $\theta_t(x)=\pi\,\omega_w((x,\infty))$.
So $\theta_t$ is strictly decreasing, with $\theta_t(a)-\theta_t(b)=\pi\,\omega_w((a,b))$ for $a<b$.
*Proof.* $x-t=-\overline{(w-x)}$, so $\arg(x-t)=\pi-\arg(w-x)$, and $\arg(w-x)=\pi\,\omega_w((-\infty,x))$ (the
classical angle formula). ∎

**Theorem 2 (exact phase identity). PROVED.** Let $I$ be a bounded interval. Pair $X\cap I$ with $\Gamma\cap I$ by
a bijection $x_k\leftrightarrow g_k$ (finite; the counts are assumed equal, which (EC) gives up to one endpoint;
otherwise put the unmatched point into $\Psi_{\rm out}$). Let $E^+=\bigcup_{x_k<g_k}(x_k,g_k)$ and
$E^-=\bigcup_{g_k<x_k}(g_k,x_k)$. Then, modulo π,
$$
\Phi_F\equiv\Phi_Z+\pi\,\omega_{\bar t}(E^+)-\pi\,\omega_{\bar t}(E^-)+\Psi_{\rm out},\qquad
\Psi_{\rm out}:=\sum_{x\in X\setminus I}\theta_t(x)-\sum_{g\in\Gamma\setminus I}\theta_t(g)
$$
(symmetric summation, with the $\pm$ mirror points included; convergent as in Lemma 3.3).
- Under **(EC)** on $I$ (alternation), all pairs can be taken with one orientation, and the intervals are disjoint. So
  $$0\le\pm\big(\Phi_F-\Phi_Z-\Psi_{\rm out}\big)=\pi\,\omega_{\bar t}(E)<\pi\,\omega_{\bar t}(\mathrm{hull}(I))<\pi.$$
  Cell by cell, the pair in cell $C_k$ contributes $\le\pi\,\omega_{\bar t}(C_k)$.
- **Remainder.** $\Psi_{\rm out}=\delta\big(S^{\rm out}_X-S^{\rm out}_\Gamma\big)+R$, where
  $S^{\rm out}_Y=\sum_{y\in Y\setminus I}(y-\gamma)^{-1}$ (symmetric) and
  $|R|\le\frac{\delta^3}3\sum_{y\in(X\cup\Gamma)\setminus I}|y-\gamma|^{-3}$.
  If (EC) holds on all of ℝ, then exactly $\Psi_{\rm out}=\pm\pi\,\omega_{\bar t}(E\setminus I)$.

*Proof.* Sum Lemma 2.0 over the pairs. The outside terms are the definition of $\Psi_{\rm out}$. The expansion is
$|\arctan u-u|\le|u|^3/3$, as in R163_401 Lemma 3.4(c). Disjointness under alternation is immediate. ∎

So the "alternating sum of arctan over interlaced pairs" of R165_000 is exactly π times a harmonic measure. The bound is
not "one cell's worth" but $\pi\,\omega_{\bar t}(\mathrm{hull}\,I)$, which is $\ge\pi/2$ as soon as
$I\supset[\gamma-\delta,\gamma+\delta]$.

**Prop 2.1 (the on-line phase at the quartet point). PROVED.** $Z_{\rm on}(t_q)=\Xi'(t_q)/\big(Q_q'(t_q)\prod_{q'\ne q}Q_{q'}(t_q)\big)$
and $Q_q'(t_q)=-\frac2{t_q}\big(1-t_q^2/\bar t_q^2\big)$. With $\beta_q=\arctan(\delta_q/\gamma_q)$,
$1-t_q^2/\bar t_q^2=2i\sin2\beta_q\,e^{-2i\beta_q}$, so $\arg Q_q'(t_q)\equiv\frac{3\pi}2-\beta_q$. Hence
$$\Phi_Z\equiv\arg\Xi'(t_q)+\tfrac\pi2+\beta_q-\sum_{q'\ne q}\arg Q_{q'}(t_q)\pmod\pi.$$
(Assume $t_q$ is a simple zero. At order $k$, replace $\Xi'$ by $\Xi^{(k)}/k!$ and $Q_q'$ by the matching quotient.)
*Proof.* Direct differentiation; $\arg(-2/t)=\pi+\beta$. ∎

**Answers to the questions in the brief.**
- **Is $\Phi_Z$ computable?** Only through $\arg\Xi'(t_q)$, which is a free datum of ζ (no identity fixes it).
- **What constrains $\Phi_Z$?** $Z_{\rm on}$ is LP, so R163_401 Lemma 3.4 applies to it verbatim: $\mathrm{Re}\,Z_{\rm on}(t_q)^2<0$ essentially iff
  $t_q$ lies in the light cone $|\gamma_q-g_0|<\delta_q$ of the nearest on-line ordinate $g_0$ (with the $E_\Gamma$
  correction). The heuristic gap of Prop 1(b) would put $t_q$ outside that cone, but this is not proved.
- **The value on the line.** $\Xi(\gamma^*)$ is real and nonzero, which gives no phase information at $t_q$. A Taylor
  expansion from the line, $\Xi(t)=\Xi(\gamma)-i\delta\Xi'(\gamma)+\dots$, does not converge usefully, because it must vanish at $t$.

**Cor 2.2 (identity for the quartet mass). PROVED.**
$$4\,\mathrm{Re}\,G(t_q)^2=4\,|G(t_q)|^2\cos2\big(\Phi_Z\pm\pi\,\omega_{\bar t_q}(E)+\Psi_{\rm out}\big),\qquad
|G(t_q)|=|Z_{\rm on}(t_q)|\cdot|G/Z_{\rm on}(t_q)|.$$
Under global (EC), $|G/Z_{\rm on}(t_q)|=|c|\cdot|\Pi(t_q)|$ with Π the Pick product of Prop 1(d). This is the requested
identity, relating the (possibly negative) quartet mass to on-line data ($Z_{\rm on}$, $\Phi_Z$) and the offset set
$E$. ∎

## 3. The cone question: interlacing does not decide the sign

**Theorem 3. PROVED.**

(a) **Explicit counterexample at exactly critical density.** Let $\rho>0$, $G(z)=\sin(\pi\rho z)$ (odd, real-rooted,
type $\pi\rho$, nodes $\mathbb Z/\rho$, node density $\rho$) and $Z(z)=\cos(\pi\rho z)$ (even, LP, zeros
$(\mathbb Z+\frac12)/\rho$, density $\rho$). They interlace perfectly on ℝ. This is (EC) on every interval, at
$T=\pi\rho$, which is the Landau crossing. At $t=\gamma-i\delta$ with $\gamma\in\mathbb Z/\rho$ (a node),
$$\mathrm{Re}\,G(t)^2=-\sinh^2(\pi\rho\delta)<0,$$
for every $\delta>0$: the quartet is strictly negative. The identity of Thm 2 checks this exactly. With $\gamma=0$,
$E=\bigcup_k(k/\rho,(k+\frac12)/\rho)$ and $E\cup(-E)=\mathbb R$ a.e., so $\omega_{i\delta}(E)=\frac12$. Also
$\Phi_Z\equiv0$ by symmetry. So $\Phi_F\equiv\pi/2$, the centre of the cone. Exchanging the roles of the two sets
(nodes at $(\mathbb Z+\frac12)/\rho$) gives $\mathrm{Re}=+\cosh^2>0$. Under (EC) both signs occur, with identical
on-line data.

(b) **General non-forcing.** Fix $\Gamma$, $t=\gamma-i\delta$, a real-rooted $G$ that interlaces $\Gamma$ on $I$, and
$\omega_{\bar t}(\mathrm{hull}\,I)>\frac12$ (e.g. $I\supset[\gamma-\delta,\gamma+\delta]$, which gives exactly
$\ge\frac12$). Move each node $x_k\in(g_{k-1},g_k)$ inside its own cell, together with its mirror $-x_k$ (parity), and
keep all other nodes. The result $G_{\mathbf x}=G\prod_k\frac{(z^2-x_k'^2)}{(z^2-x_k^2)}$ is real, has the same parity
and the same exponential type, and still satisfies (EC). Under such moves:
- the map $\mathbf x'\mapsto\Phi_{F}(\mathbf x')$ is continuous on a connected product of open cells;
- its local part $\pi\,\omega_{\bar t}(E)$ tends to $0$ (all $x'_k\to g_k$) and to $\pi\,\omega_{\bar t}(\mathrm{hull})$ (all
  $x'_k\to g_{k-1}$);
- the mirror points change $\Psi_{\rm out}$ by at most $\epsilon_{\rm mir}\le\sum_k\frac{2\delta|\mathrm{hull}\,I|}{(2\gamma-|I|)^2}$.

So the range contains an interval of length $\ge\pi\,\omega_{\bar t}(\mathrm{hull}\,I)-2\epsilon_{\rm mir}>\pi/2$ for
$\gamma$ large. Every interval of length $>\pi/2$ mod π meets both $(\pi/4,3\pi/4)$ and its complement, so (EC)
configurations of both signs exist. ∎

**Cor 3.1 (where interlacing does bite). PROVED.** If the cell of the quartet $[x_0,x_1]\ni\gamma^*$ is narrow
compared with δ, its pair contributes $\le\pi\,\omega_{\bar t}([x_0,x_1])\le|x_1-x_0|/\delta$. The quartet's sign is then
$\operatorname{sign}\cos2(\Phi_Z+\Psi'_{\rm out})$ up to that error; the far pairs are moved into $\Psi'$. At the
critical density, however, the cell has length $\approx\pi/T_c\approx2\pi/\log(\gamma/2\pi)$. Narrowness
$\ll\delta$ means $\delta\log\gamma\gg1$, and then the far pairs within distance ≈δ carry harmonic measure ≈ ½. That is
case (b): no lock. Interlacing locks the phase to the on-line data only in a regime where it is not local, so the
lock is not a useful constraint.

**Main answer (task 2).** **No.** (EC) does not force $\Phi_F\notin(\pi/4,3\pi/4)$. The quartet sign under (EC) is
exactly $\operatorname{sign}\cos2(\Phi_Z\pm\pi\,\omega_{\bar t_q}(E)+\Psi_{\rm out})$ (Cor 2.2). It is decided by the
**offset measure** $\omega_{\bar t_q}(E)$, i.e. by where each node sits inside its cell between consecutive on-line
zeros, and not by the interlacing itself.

## 4. Tests

**Lattice model (R163_401 Lemma 4.10). PROVED.** There $T^*<\pi\rho$: the node density $T^*/\pi$ is below the on-line
density ρ. On any $I$ of length $>1/(\rho-T^*/\pi)$ there are more zeros than nodes, so (EC) **fails** (two
consecutive zeros with no node between). The model witness has its node at the cone vertex ($\varphi_0=\pi/2$) and a
negative quartet. Thm 2 has no hypothesis there, so there is no conflict. Thm 3(a) is the "critical-density
completion" of the model: at $T=\pi\rho$ with lattice nodes, the vertex node gives the negative sign *with* perfect
interlacing. Pushing $T_c$ up to the Landau crossing (Det±) would therefore not, by geometry alone, rescue
$(\star_{\rm cell})$.

**$M_m$ (decisive check). PROVED (logic).** The real zero set of $M_m$ is ζ's $\Gamma$, and its first-contact witness
satisfies $\sum_q4\,\mathrm{Re}\,G(t_q)^2=-P_+<0$, so some quartet is negative.
- Had "(EC) ⇒ quartet positive" been proved from $\Gamma$, $t_q$ and real-rootedness, it would force every
  negative-quartet witness of $M_m$ (and of ζ) to be non-interlaced in that cell. The content would then move to A4's
  question ("does first contact force (EC)?").
- Thm 3 shows that the implication is **false** already for entire real-rooted pairs. So the $M_m$ check is passed
  trivially: nothing here separates ζ from $M_m$, and nothing is claimed to.
- The precise relocation of the content: A4 must control the **offset measure**, i.e. prove
  $\Phi_Z\pm\pi\,\omega_{\bar t_q}(E)+\Psi_{\rm out}\notin(\pi/4,3\pi/4)$ mod π at a first contact. Controlling (EC)
  alone is not enough. Node positions inside cells at the witness are fixed by the node identity 2.4(iv) and
  $W_{T_c}(F)=0$. Any such statement at the witness is again Rem 4.8a (E1, circular), unless it is proved for a named
  larger class using data that $M_m$ lacks.

## Ledger

- **New, PROVED:**
  - Thm 2: the phase difference between witness and on-line function is exactly π·(harmonic measure of the node–zero
    offset set), plus an explicit remainder;
  - Prop 2.1: $\Phi_Z$ in terms of $\arg\Xi'(t_q)$;
  - Cor 2.2: the quartet-mass identity;
  - Thm 3: (EC) ⇏ positive quartet, with an explicit critical-density example and general both-sign realisability;
  - Prop 1(e): the quartet is invisible to real interlacing.
- **Corrected in R165_000 §2:**
  - "the bound is one cell's width" → $\pi\,\omega(\mathrm{hull}\,I)$, which is $\ge\pi/2$;
  - "the quartet cell is the only cell where HB fails" → HB fails for $(G,\Xi)$ through $Q_q$, not through the
    interlacing;
  - "Z has two fewer zeros there" → only in the count (Prop 1(b)).
- **Closed negative:** the route "critical interlacing removes the quartet from the cone by geometry" (R165_000 §3, success
  criterion, first branch). It is refuted by Thm 3. The refutation is geometric, not a witness-level counterexample;
  whether a real witness of ζ realises the negative offset is the original question.
- **Open (handed to A4):** a constraint on $\omega_{\bar t_q}(E)$ at first contact. By Rem 4.8a it is RH-strength at
  the witness.
- **Cells:** 7A — cone cut by zero data: answered. Zero data plus interlacing cuts the phase to an interval of length
  $\pi\,\omega(\mathrm{hull}\,I)$, which never decides the sign once it exceeds π/2. 2A — no change of label.
