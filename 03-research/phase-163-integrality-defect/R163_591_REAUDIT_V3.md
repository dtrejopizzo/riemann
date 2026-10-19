# R163_591 —  re-audit of R163_401 v3 against R163_590

*Referee report. This was pure reading: no , no commits, no numerics beyond a hand check of
$y_0$. Only this file was written. I compared R163_401 (v3) against R163_590 D1–D11, and checked the errata in
R163_490, R163_402 and R163_501.*

## 0. Verdict

**NOT CLEAN (editorial only).**

- All of D1–D11 are applied, and applied correctly.
- The new block-node item 2.4(iii′) is mathematically correct.
- No new mathematical defect was found.
- Four wording defects remain (N1–N4). The main one, N2, is a set of leftover sentences that still name (I1) or (I1-T)
  as "the exact gap". This contradicts the boxed gap $(\star_{\rm cell})$, Rem 4.7a and Cor 4.10a.
- None of the four reaches the conclusion: row D is OPEN, and $(\star_{\rm cell})$ is the only gap.

## 1. Fix-by-fix check

| fix | where | check |
|---|---|---|
| D1 | Lemma 4.10, l. 532–540 | Correct. See the derivation below. |
| D1 | Cor 4.10a, l. 542–548 | Correct. The refutation of (I0) is now independent of where $T^*$ lies. For fixed $\delta$, $T^{*3}=O(\log^3L)$ falls inside the range of (I0). $P_0-N_0\le0$ follows from the exact sum. |
| D1 | errata | R163_490 l. 40, 86 and 114, and R163_402 l. 60, are present and consistent. |
| D2 | Thm 1.2, l. 104–107 | Both directions are cited as specified, with a forward reference. The table and ledger are updated. The R163_501 "Thm 10.4" citation is gone (grep finds no hits). |
| D3 | §4.6, l. 442–444 | Verbatim fix. `thm:finmod` and Lemma S are gone. |
| D4 | §4.5, l. 426 | Applied, but see N1. |
| D5 | 2.4(iii), 2.4(iii′), §4.5 | Applied, and the block version was added. Checked in §2 below. |
| D6 | §4.4 | Applied. See the check below. |
| D7 | Rem 4.7a, (I1) row, §5, §7 | Applied. Rem 4.7a is HEURISTIC in the text, the table and the ledger. The (I1) row now says "generically void". §5 reads "for instance via (I1)+(I2)". §7 reads "possible route:". |
| D8 | Rem 4.8a, §4.9 | Applied, with $T\ge T_0(\varepsilon)$, PROVED-CITED, record. |
| D9 | §6 heading, $M_m$ row | Applied. The $M_m$ row now rests on Rem 4.8a. |
| D10 | Rem 2.5a, table, R163_501 §0 | Applied as "UNPROVED as stated …". |
| D11(a)–(f) | l. 216, 267, 373, 346–348 and 585–587, 458, 102 | All applied. |

**D1 derivation.**
- $S>\pi\rho=L/2$ holds iff $\sinh(2\delta T)-2\delta T>\delta L$.
- $\sinh y-y\ge y^3/6$ gives $S\ge\tfrac23\delta^2T^3$, so $T^{*3}\le\tfrac34L/\delta^2$.
- $e^{2\delta T}/2\sim\delta L$ gives $T^*\sim\log(2\delta L)/(2\delta)$.
- $S'=\cosh(2\delta T)-1>0$, so $S$ is increasing. Hence $T^*<L/2$ iff $S(L/2)>L/2$ iff $\sinh\delta L>2\delta L$.
- Hand check of the root: $\sinh2.1773=4.354$ and $2y_0=4.355$.

**D6 check.** $\lvert u\rvert\le M_2r/(2\lvert G'\rvert)<\sqrt2-1$. Since $1-2u-u^2>0$ iff $u<\sqrt2-1$, this gives
$\mathrm{Re}(1+u)^2>0$. The Consequence paragraph is now a HEURISTIC remark.

## 2. 2.4(iii′) in detail

**Cross-node W-orthogonality: correct.**
- Take $x\ne y$ real. Then $((z-y)^j)^\#=(z-y)^j$, so
  $\widehat H_{x,i}\widehat H_{y,j}^\#=\widehat F\widehat F^\#/((z-x)^i(z-y)^j)=\widehat F\,\widehat K^\#$.
- $\widehat K$ is entire because $i\le k_x$ and $j\le k_y$. $\widehat K\in PW_T$ with faster decay, so $K\in\mathcal D_T$.
- The form depends only on the product $\Phi\Psi^\#$:
  - by (1.1), which converges absolutely;
  - or by `eq:form`, since $A(F)\overline{B(G)}=(\widehat F\widehat G^\#)(-i/2)$, $B(F)\overline{A(G)}=(\widehat F\widehat G^\#)(i/2)$,
    and $\widehat F\overline{\widehat G}=\widehat F\widehat G^\#$ on $\mathbb R$.
- Hence the entry equals $W(K,F)$, which is $0$ because $F\in\ker W_{T_c}$ (§4.6).

**Blocks: correct.**
- *Hankel.* Each entry depends only on $\widehat F\widehat F^\#/(z-x)^{i+j}$, so only on $i+j$.
- *Zeros.* The entry is $0$ when $i+j\le k_x$, since $\widehat K_{i+j}$ is then entire and in $\mathcal D_T$.
- *Positive semidefinite.* $B_x$ is a Gram matrix of $W_{T_c}\ge0$.
- *Consequence (not a defect).* A PSD matrix whose diagonal entries $(i,i)$ with $2i\le k_x$ are zero must have those
  rows equal to $0$. So for $k_x\ge2$, $H_{x,1}\in E_c$, and $\operatorname{rank}B_x\le\lceil k_x/2\rceil$. This is
  consistent, because $\dim E_c<\infty$. The memo could record it, but nothing is wrong.

**Quadrature: correct.**
- The principal part of $\widehat G/\widehat F$ at $x$ is $\sum_ja_{x,j}(z-x)^{-j}$.
- For $m<k_x$, the coefficient of $(z-x)^m$ in $\widehat G/u_x$ is $a_{x,k_x-m}$.
- The map from $(\widehat G^{(i)}(x))_{i<k}$ to these coefficients is triangular and invertible, since $u_x(x)\ne0$.
- Therefore $\widetilde B_x=M^*B_xM\succeq0$.
- For $k=1$ this reduces to $w_x\lvert\widehat G(x)\rvert^2$.

**Extension to $\overline N^{\mathcal D}$.** The memo calls this "verbatim Q0". That is acceptable:
- derivative evaluations are bounded on $PW_T$;
- the infinite sum is a sum of PSD blocks, so the Fatou/Cauchy argument of R163_502 carries over.

It is not written out. It is a minor point, already covered by the citation.

## 3. Remaining defects (exact fixes)

**N1 (§4.5, l. 426).** "It is a positive solution of KEP($T_c$)" grammatically refers to the Weil distribution. That
distribution has negative atoms, and the intended referent is $\nu_X$.
Fix: "The measure $\nu_X$ is a positive solution…".

**N2 (leftover gap-location claims).** These sentences still name (I1) or (I1-T) as the precise gap:
- the summary, l. 63–65 ("§4.9 identifies the inequality (I1) that would supply it");
- Remark 4.8, l. 571–572 ("violates S4 exactly at (I1). This is the precise location of the gap");
- the §6 verdict, l. 619–620 ("incomplete exactly at (I1)");
- the closing status, l. 658–659 ("identification of (I1-T) … as the exact missing inequality").

They contradict three other parts of the memo:
- Rem 4.7a: (I1) is generically void;
- Cor 4.10a: (I1-T) is necessary but not sufficient;
- the boxed gap, which is $(\star_{\rm cell})$.

Fix: replace each of them with "$(\star_{\rm cell})$, in the exact form $P_j=\sum_{C_j}G(\gamma)^2$; (I1) is one route,
void at cell scale; (I1-T) is necessary, not sufficient".

**N3 (l. 63).** "§6.6" does not exist. Fix: "§6, row $M_m$".

**N4 (l. 8).** The text says "three labels" but lists four. Fix: "four".

## 4. Conclusion

All the mathematics of v3 holds as labelled. The memo becomes CLEAN once the four text edits N1–N4 are made. No label
of record moves. Row D is OPEN, and the sole gap is $(\star_{\rm cell})$.
