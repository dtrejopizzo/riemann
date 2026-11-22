# R163_590 — Final audit of R163_401 (revised D-closure candidate)

*Referee report. Pure reading, plus one scalar root-finding check that confirms counterexample D1 (the
analytic argument is given below and does not depend on it). No , no commits. Only this file was written.
Compared against R163_401_v1, R163_490, R163_501, R163_502 and R163_402, against Paper 46 (`main.tex`: `eq:symbol`,
`eq:form`, `eq:W`, `lem:roughEF`, `thm:log5W`, `thm:log5A`, `lem:monoT`, `lem:contT`, `lem:contA`,
`lem:firstcontact`, `thm:KEP2`, `thm:KEP3`, `thm:finmod`), against Paper 45 (`main.tex`, theorem counter per section:
Thm 8.4 = `thm:EF`, Thm 11.3 = `thm:sufficiency`, 10.4 = `rem:collapses`), and against Paper 48 (`thm:M`,
`tab:falsifiers`, `W1`).*

## 0. Verdict

**NOT CLEAN.** The logical skeleton is sound:
- $(\star_{\rm cell})\Rightarrow$ CL $\Leftrightarrow$ RH $\Leftrightarrow$ D;
- the witness chain §2.3–2.4 holds;
- Lemmas 3.0–3.4 hold;
- the cell identity holds;
- the conclusion "row D OPEN, the only gap is $(\star_{\rm cell})$" survives.

Several labels are still wrong:
- one is a **substantive mathematical error** (D1: Lemma 4.10 / Cor 4.10a);
- three are **miscitations** (D2–D4);
- the rest are missing hypotheses or unproved sentences sitting inside PROVED items (D5–D11).

Once the exact fixes below are applied, the only unproved step of the chain is the boxed $(\star_{\rm cell})$. Items
(I1), (I1-T) and 4.9 are subsidiary routes to it and are already labelled ARGUED.

## 1. Items checked and confirmed

| item | check |
|---|---|
| Thm 1.3 | `lem:roughEF` needs real $F$, (a) the form domain and (b) $\sum\lvert\Phi_F(\rho)\Phi_F(1-\rho)\rvert<\infty$. (b) follows from Lemma 3.0 applied to $f(z)$ and $f(-z)$, plus Cauchy–Schwarz. Polarisation to complex $F$ is correct: the cross term $\sum_\rho[\widehat F_2(t)\widehat F_1(-t)-\widehat F_1(t)\widehat F_2(-t)]$ is odd under $\rho\mapsto1-\rho$ and absolutely convergent, so it vanishes. |
| 2.1 | Matches `thm:log5W` ($10^{-18}$, even part; $10^{-16}$, odd part) and `thm:log5A` ($2.5\cdot10^{-12}$). Both are certified computations (record). |
| 2.2 | `lem:monoT` and `lem:contT` read and correct. Attainment holds by compactness in the proof of `thm:O`; Bombieri Thms 3 and 5 are cited in the same way in Paper 46, l. 224–225. |
| 2.3 | $T_c>\tfrac12\log5$; $\lambda^{\rm W}_{T_c}=0$, attained; $E_c$ finite-dimensional. $T_*\ge T_c$ holds because $\lambda^{\rm W}\le\lambda^{\rm A}$. All correct. |
| 2.4(i)–(iii) | Agree with R163_501 (Thm B, R(a)–(c),(e), R(d′), FC0(ii), FC(i)–(ii), G), with $w_x=d_x/\lvert\widehat F'\rvert^2$. Q0 (R163_502) re-checked: $W$ is $\mathcal D$-bounded, the seminorm is Cauchy, point evaluations are continuous, and the limit is in $\ell^2$. Adding $\mathbb CF$ is harmless, since $W(F,\cdot)=0$ and $\widehat F|_X=0$. But see D5. |
| Lemma 3.0 | Subharmonic mean on $D(t_\rho,1)$, $\lvert y\rvert\le3/2$ there, $K\ll(1+u^2)^{-1}$, Titchmarsh 9.6(A). Correct; see D11(a). |
| Lemma 3.1 | Hadamard pairing, $b=0$ from parity, $\widehat F\widehat F^\#=G^2$ in both parities, quartet sum $=4\,\mathrm{Re}\,G(t)^2$. Correct. |
| Lemma 3.2 | Poisson majorant for the Cartwright class plus Jensen's inequality. Correct as a citation. Section numbers in Koosis and Levin were not verified here; R163_402 cites Levin Lecture 17 for the factorisation. |
| Lemma 3.3 | Correct; see D11(b) for wording. |
| Lemma 3.4 | (a)–(d) correct. (b): the condition is $\lvert\Theta\rvert\in(\pi/4,3\pi/4)$, and both directions check. (c): the limit $-G''(x_0)/(2G'(x_0))$ is correct. (d): Abel summation, constant $\kappa/(2g^2)$. (e): Taylor expansion at a node, with $\mathcal E$ bounded as stated. $M_2\le T^2e^{Tr}\lVert G\rVert_\infty$ is Bernstein on $\mathbb R$ plus Phragmén–Lindelöf off it. |
| Prop 4.0 | (⇐): the simple-zero proportion (Conrey 1989, $>2/5$ simple zeros on the line) gives $\gg R\log R$ distinct ordinates, against Jensen's $O(R)$. Correct. (⇒): FC0(ii) + R(c). Correct. |
| 4.1, 4.3 | Correct. |
| 4.2 | de la Vallée Poussin (Titchmarsh 3.8); Selberg's density theorem (Titchmarsh 9.19(C)); Thm Δ re-derived (constants 32 and 4); Platt–Trudgian 2021 to $3\cdot10^{12}$; $13.4$. All correct; see D11(c). |
| 4.6 | The kernel equation is correct, by Cauchy–Schwarz for nonnegative forms. See D3. |
| 4.7 | The cell identity is exact and converges absolutely. Both bounds follow from Lemma 3.4(e). See D7 and D11(e). |
| Rem 4.8a | Correct as logic. If ¬RH, quartets exist, every ordinate lies in some cell, the other cells are $\ge0$ and the sum is $0$. So "$(\star_{\rm cell})$ at every witness" $\Leftrightarrow$ RH. See D8. |
| §5 | The conditional deduction is correct; see D7 and D11(d). |
| Lemma 4.10, threshold part | $\inf<0\iff S(T,\delta)>\pi\rho$ re-derived: Poisson summation is alias-free for $2T<2\pi\rho$; $G(-i\delta)=A+iB$; Cauchy–Schwarz; the extremal is $b=\sinh\delta u$. $S=\sinh(2\delta T)/(2\delta)-T$. Correct. |

## 2. Defects, each with its exact fix

### D1 (substantive). Lemma 4.10 asymptotics and Cor 4.10a are false as stated

**The error.** Lemma 4.10 states $T^{*3}=\tfrac34L\,\delta^{-2}(1+o(1))$, with $L:=\log(\gamma/2\pi)$, and states that
it is self-consistent iff $\delta\gtrsim2.45/L$. Cor 4.10a then uses $T^{*3}>3L>\tfrac{\pi^2}6L$.

**Why it fails.**
- The cubic law needs $\delta T^*\to0$. But inside the self-consistent regime,
  $\delta T^*=(\tfrac34\delta L)^{1/3}\ge(\tfrac34\cdot2.45)^{1/3}\approx1.22$. So the error $O(\delta^2T^{*2})$ is
  never small there, and "$(1+o(1))$" is false. R163_402 Cor 5 honestly writes $1+O(\delta^2T^2)$; R163_490 §1 and
  R163_401 dropped that qualifier.
- Since $\sinh y-y\ge y^3/6$, we have $S(T)\ge\tfrac23\delta^2T^3$. So the exact contact satisfies
  $T^*\le(\tfrac34L/\delta^2)^{1/3}$. The cubic value is an **upper** bound, and Cor 4.10a uses it in the wrong
  direction.
- **Counterexample.** Fix $\delta\in(0,\tfrac12)$ and let $L\to\infty$. Then $\sinh(2\delta T^*)\sim\delta L$, so
  $T^*\sim\log(2\delta L)/(2\delta)$ and $T^{*3}=O(\log^3L)=o(L)$. Hence $T^{*3}<\tfrac{\pi^2}6L$ for all large $L$.
  Numerically:
  - $\delta=0.49$, $L=100$: $T^*=4.77$, $T^{*3}=109<164.5=\tfrac{\pi^2}6L$;
  - $\delta=0.3$, $L=1000$: $T^{*3}=1224<1645$;
  - already at $L=26.9$ (height $3\cdot10^{12}$), $\delta=0.49$: $T^{*3}=45.9<80.7=3L$.
- **The exact self-consistency threshold** is $T^*<\pi\rho=L/2\iff S(L/2)>L/2\iff\sinh(\delta L)>2\delta L\iff\delta L>y_0$,
  where $y_0=2.1773\ldots$ is the positive root of $\sinh y=2y$. The value $2.45$ is wrong.

**Fix for Lemma 4.10, second sentence.** Replace it with:

> "Hence $T^*$ is the root of $\sinh(2\delta T)-2\delta T=\delta L$. It satisfies $T^*\le(\tfrac34L/\delta^2)^{1/3}$,
> with equality asymptotically only as $\delta T^*\to0$, and $T^*\sim\log(2\delta L)/(2\delta)$ as $\delta L\to\infty$.
> It is self-consistent ($T^*<\pi\rho$) iff $\delta L>y_0=2.1773\ldots$ ($\sinh y_0=2y_0$)."

**Fix for Cor 4.10a.** Delete "Since $\delta<\tfrac12$, $T^{*3}=\ldots>3\log>\tfrac{\pi^2}6\log$: the contact always lies
outside the range …". Replace it with:

> "The refutation of (I0) does not depend on where $T^*$ lies relative to the range of (I0). The model witness exists for
> every $\delta\in(y_0/L,\tfrac12)$ and $(\star_{\rm cell})$ fails in its cell. For fixed $\delta$ and large $L$ the
> contact lies **inside** that range ($T^{*3}=O(\log^3L)$), where (I0) predicted success. So (I0) is refuted a
> fortiori. (I1-T) holds at the contact ($T^*<\pi\rho$), so (I1-T) is necessary but not sufficient."

**Fix for R163_490.** In §1 (bullet $T^{*3}$, threshold $2.45$) and §3 (bullet "Moreover $T^{*3}>3\log$…"), add an
erratum that points to this item.

**What survives.** The conclusions REFUTED (I0), "(I1-T) not sufficient" and "(α) empty in the model" all survive,
with the corrected reason.

### D2 (miscitation). Theorem 1.2 (D ⟺ RH)

Paper 45 Thm 11.3 (`thm:sufficiency`) proves only one direction: ¬RH ⇒ there are primitive $C_c^\infty$ tests with a
negative zero sum. Thm 8.4 identifies that zero sum with $W_T$ for smooth tests. The direction RH ⇒ $W_T\ge0$ **on
$\mathcal D_T$** (Definition 1.1 uses the form domain, not $C_c^\infty$) needs (1.1) for rough tests.

**Fix.**

> "PROVED-CITED. (⇒ D implies RH): $C_c^\infty(I_T)\subset\mathcal D_T$, then Paper 45 Thm 11.3 with Thm 8.4.
> (⇐): under RH, Thm 1.3 (Paper 46 `lem:roughEF`, Lemma 3.0) gives $W_T(F)=\sum_\gamma\lvert\widehat F(\gamma)\rvert^2\ge0$
> on $\mathcal D_T$. See also Bombieri 2000, Thm 1."

Because (⇐) uses Thm 1.3, move Thm 1.2 after Thm 1.3, or add a forward reference.

**Inherited citation error.** R163_501 (§0 bottom line, §3.2, §5) cites "P45 Thm 10.4" for ¬RH ⇒ $\lambda^{\rm W}_T<0$.
In Paper 45, 10.4 is `rem:collapses`. Replace it with "P45 Thm 11.3".

### D3 (miscitation). §4.6

- "By Selberg's uniqueness (R162_2301 Lemma S…)" is unnecessary. Uniqueness of $a$ with $a*1=\log$ on $n<e^{2T}$ is
  Möbius inversion, as R163_490 §1 already noted.
- "(Paper 46, `thm:finmod`, record)" is a **wrong reference**. `thm:finmod` concerns deletion and amplification
  thresholds, not the statement that data agreeing below $e^{2T}$ give the same $W_T$.

**Fix.** Replace the paragraph with:

> "By `eq:symbol` the comb of $W_T$ involves only $n\in\mathcal N_T$, so any coefficient vector agreeing with
> $(\Lambda(n))_{n<e^{2T}}$ gives the same $W_T$. The vector is determined by $a*1=\log$ on $n<e^{2T}$ (Möbius
> inversion)."

### D4 (miscitation, inside a conditional remark). §4.5

"This is the determinate Kreĭn extension at $\lambda=0$ (Paper 46, `thm:KEP3`)." `thm:KEP3` states:
- (a) $\lambda^{\rm W}>0\Rightarrow$ indeterminate $\Rightarrow\lambda^{\rm W}\ge0$, "except on $\{\lambda^{\rm W}=0\}$";
- (b) RH ⟺ indeterminacy for all $T$.

It asserts nothing about determinacy at $\lambda=0$. The only determinacy theorem in Paper 46 is `thm:finDet` (finite
zero sets).

**Fix.**

> "It is a positive solution of KEP($T_c$) (`thm:KEP2` gives the converse direction); whether it is the unique one is
> not claimed."

### D5 (missing hypothesis). 2.4(iii), §4.5 (Q0): simple nodes

The weights $w_x=W(H_x)/\lvert\widehat F'(x)\rvert^2$ and the diagonal quadrature need simple nodes. R163_501 §4(d)
says "at simple zeros"; R163_502 assumes simple nodes for Q1 and Q2. Neither R163_501, R163_502 nor R163_401 proves that
witness nodes are simple.

**Fix.** Append to 2.4(iii):

> "(stated for simple nodes; at a node of multiplicity $k$ add $\widehat F/(z-x)^j$, $j\le k$; the quadrature then has a
> $k\times k$ block at $x$ involving $\widehat G^{(i)}(x)$, and is no longer diagonal)."

Make the same addition in §4.5. §4.4 and §4.7 already assume a simple node, or are trivially true when
$G'(x_j)=0$.

### D6 (unproved text inside a PROVED item). §4.4

Two problems.
- "which is **positive**" holds only under a smallness condition. Write $G(t)/(t-x_0)=G'(x_0)(1+u)$ with
  $\lvert u\rvert\le M_2r/(2\lvert G'(x_0)\rvert)$. Then $\mathrm{Re}(1+u)^2>0$ is guaranteed when
  $\lvert u\rvert<\sqrt2-1$.
- The paragraph "**Consequence.** … no inequality on the weights $w_x$, including … 2.4(iv), can yield the contradiction
  alone" is a meta-claim with no proof.

**Fix.**
- Insert "provided $M_2r<2(\sqrt2-1)\lvert G'(x_0)\rvert$".
- Relabel the Consequence paragraph as "Remark (HEURISTIC; cf. R160_X_C1 Thm Q, W3)".

### D7 (labels). Rem 4.7a and (I1); §5 "i.e. (I1)"

- Rem 4.7a's "generically $M_2\asymp T^2\lVert G\rVert$, $\epsilon_j\gtrsim\pi/2$" is a heuristic. It sits under a
  PROVED heading and in a ledger row marked PROVED.
- When $\epsilon_j\ge1$ the side condition of (I1), $(1+\eta)(1-\epsilon_j)_+^2>1+\cdots$, cannot hold. So (I1) is
  generically **void as formulated**, not merely unproved.
- §5 says "Assume $(\star_{\rm cell})$, i.e. (I1)". But (I1) together with (I2) implies $(\star_{\rm cell})$; the two
  are not equivalent.

**Fix.**
- Label Rem 4.7a HEURISTIC in the text, in the status table and in §7.
- Add to the (I1) row: "generically void at cell scale (Rem 4.7a); $(\star_{\rm cell})$ must be attacked in the exact
  form $P_j=\sum_{C_j}G(\gamma)^2$".
- In §5, replace "i.e. (I1) for every cell…" with "(for instance via (I1)+(I2), Rem 4.7a notwithstanding)".
- In the §7 row "4.8 $(\star_{\rm cell})$, via (I1)", replace "via" with "possible route:".

### D8 (citation scope). Rem 4.8a

The sentence "$\lambda^{\rm A}_T\le\exp(-e^{(2-\varepsilon)T})$ nearby" sits inside an item labelled PROVED. Paper 48
`thm:M`(b) holds only for $T\ge T_0(\varepsilon)$, and Paper 48 says it is proved "in the record … not yet part of a
refereed paper". Nothing makes it "nearby" a witness at an unspecified $T_c$.

**Fix.** Keep PROVED for the circularity statement only. Rewrite the margin sentence as:

> "at the witness the bottom is exactly $0$, so no fixed margin $\eta$ exists at $T_c$ (PROVED); for $T\ge T_0(\varepsilon)$,
> moreover, $\lambda^{\rm A}_T\le\exp(-e^{(2-\varepsilon)T})$ (Paper 48 `thm:M`(b), PROVED-CITED, record)."

Make the same change in §4.9.

### D9 (labels). §6, "PROVED by inspection"

- The table contains record and numerical claims: $s_2^c\approx0.99977$ (uncertified), the deletion contact interval
  $[0.4608,0.60]$, the $\Lambda\chi_2$ value $T_c\le0.38$, and the DH zero $0.8085+85.699i$ (cited).
- The $M_m$ row derives its conclusion "By §4.9", which is ARGUED.

**Fix.**
- Label §6 "PROVED-CITED (record, Paper 48 `tab:falsifiers`); numerical entries uncertified as marked".
- Replace "By §4.9, its contact must sit where (I1-T) fails" with:

  > "$M_m$ has a witness (Paper 48 `tab:falsifiers`); by the argument of Rem 4.8a, $(\star_{\rm cell})$ fails in some
  > cell of that witness."

The conclusion of the row is unchanged and now rests on an identity rather than on a heuristic.

### D10 (overstatement). Rem 2.5a and the status table

"FC(iii) FALSE as stated" overstates R163_501 §3.4. That section shows the claim is unproved and fails *if*
$\lambda^{\rm A}$ vanishes on an interval, which is "not excluded". It does not show that this happens.

**Fix.** Replace "FALSE as stated" with "UNPROVED as stated (fails if $\lambda^{\rm A}$ vanishes on an interval
$[T_1,T_*]$, which is not excluded; repaired at $T_\flat$)". Apply the same change to R163_501 §0, row FC(iii).

### D11 (minor precision)

- **(a) Lemma 3.0.** "$0\le\delta\le\tfrac12$" → "$\lvert\delta_\rho\rvert<\tfrac12$". The sum runs over all $\rho$,
  and $1-\rho$ has $\delta<0$. The proof already covers $\lvert y\rvert\le3/2$.
- **(b) Lemma 3.3.** "$m$ copies of $x=0$; $\arctan(\delta/0):=\pi/2$" → "$m$ copies of $x=0$; when $x=\gamma$, set
  $\arctan(\delta/0):=\pi/2$". The convention concerns $x=\gamma$, not $x=0$.
- **(c) §4.2.** "$N(\sigma,R)=o(R)$ (Bohr–Landau; …)" → "(Carlson 1920; Ingham; Selberg, Titchmarsh 9.19(C))".
  Bohr–Landau give $O(R)$.
- **(d) Prop 4.0(⇐) and §5 item 3.** State the general fact used: "under RH, $W_T(F)=0$ with $F\in\mathcal D_T$
  arbitrary (complex) implies $F=0$". The proof given already covers this; the hypotheses real, parity-definite and
  real-rooted are not used, and $\ker W_T=0$ needs the general form.
- **(e) §4.7.** Define $M_2$ in $\epsilon_j$ as $\sup_{\lvert z-x_j\rvert\le h_j+\frac12}\lvert G''\rvert$.
- **(f) Definition 1.1.** "on $\mathcal P_T$" → "on $\mathcal P_T\cap\mathcal D_T$".

## 3. Is the boxed gap the only unproved step?

After D1–D11, yes. Every item in the chain $(\star_{\rm cell})\Rightarrow$ CL $\Leftrightarrow$ RH $\Leftrightarrow$ D
is PROVED, or PROVED-CITED with an exact and correct reference, except $(\star_{\rm cell})$ itself. The items (I0),
(I1), (I1-T), 4.9, Rem 4.7a and the band reading in §4.5 are labelled HEURISTIC, ARGUED or conditional, and none of
them carries the chain.

The record inputs used without re-audit are:
- the Paper 46 certificate at $\tfrac12\log5$;
- R162_2202 (node identity; unused);
- R162_1701 (unused);
- Paper 48 `thm:M`(b);
- the falsifier records of Paper 48 `tab:falsifiers`.

Only the first carries weight. It is a certified computation.

**Final verdict: NOT CLEAN.**
- Remaining defects: D1 (substantive: Lemma 4.10 asymptotics, Cor 4.10a), D2–D4 (miscitations), D5–D11 (hypotheses
  and labels).
- None of them reaches the conclusion: row D OPEN, with $(\star_{\rm cell})$ as the sole gap.
- After the listed edits the memo is CLEAN in that sense.
- No label of record moves.
