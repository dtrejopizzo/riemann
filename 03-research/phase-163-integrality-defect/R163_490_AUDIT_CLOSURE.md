# R163_490 — Audit of R163_401 (D-closure candidate) and R163_402 (light cone)

*Referee report. Pure reading; no numerics run; nothing else edited. Checked against Paper 48
(`04-papers/48-row-d-route-map/main.tex`): codes F1–F4, M, E1, W3, Table `tab:falsifiers`, Condition S1–S12.*

## 0. Verdict on §4 of R163_401

**GAP, and the gap is circular.** The proof stops at $(\star_{\rm cell})$ (equivalently (I1), with its necessary part
(I1-T)), which is not proved. Applied to the witness, $(\star_{\rm cell})$ is equivalent to "no witness", so it is
equivalent to RH (E1). The heuristic given for (I1), the counting (I0), is **false in the lattice model of R163_402
Theorem 4**: there, for every $\delta<\tfrac12$, the witness sits outside the regime where (I0) supports (I1), and
$(\star_{\rm cell})$ fails in the cell of the quartet (§3 below). Regime (α) of §4.9 is therefore empty in that model.
It is not merely "unproved".

The memo's own summary (row D OPEN, CL ⟺ RH, a conditional deduction only) is **confirmed**. Several PROVED labels need
fixes (§2). One claimed separation is wrong: (I2) does **not** separate the sign step from Davenport–Heilbronn (§4).

## 1. Line-by-line: steps that check out

- **Lemma 3.0 (absolute convergence).** Correct. The disc $D(t_\rho,1)$ has $|y|\le3/2$, which gives the factor
  $e^{3T}$. $K(u)\ll(1+u^2)^{-1}$ holds. Titchmarsh 9.6(A) gives the sum over $\rho$.
- **Lemma 3.1.** Correct, including the odd case: $\widehat F^\#(z)=\widehat F(-z)$ for real $F$, so
  $\widehat F\widehat F^\#=G^2$ in both parities. Hadamard pairing, $b=0$ and the quartet sum $4\,\mathrm{Re}\,G(t)^2$
  are all fine.
- **Lemma 3.3 (phase).** Correct. Pairing $\pm x$ gives $2\delta\gamma/(x^2-\gamma^2)$, which is summable. The sign
  convention agrees with R163_402 Lemma 1(2).
- **Lemma 3.4 (a)–(d).** Correct. In (d), the Stieltjes boundary term vanishes because no node lies at distance $<g$.
- **Prop 4.0 (⇐).** Correct, and it holds for every complex $F$. It gives $\ker W_T=0$ under RH.
- **4.1 balance.** Correct. It needs Selberg's positive proportion: Hardy–Littlewood's $\gg R$ would not beat the
  $O(R)$ zeros allowed by Jensen.
- **4.3.** Correct.
- **4.6.** Correct but trivial: uniqueness of $a$ with $a*1=\log$ is Möbius inversion, and Selberg's identity is not
  needed.
- **R163_402 Lemma 1, Cor. 2, Cor. 3, Thm 4, Cor. 5.** All re-derived and correct:
  - Poisson aliasing vanishes since $2T<2\pi\rho$;
  - $S=\sinh(2\delta T)/(2\delta)-T$;
  - the extremal is $b=\sinh\delta u$;
  - $T^{*3}=\tfrac34\log(\gamma/2\pi)/\delta^2$;
  - the self-consistency threshold is $\delta>2.45/\log(\gamma/2\pi)$.
  *(Erratum, R163_590 D1: the cubic value is only an upper bound, $T^*\le(\tfrac34L/\delta^2)^{1/3}$ with $L=\log(\gamma/2\pi)$, since $\sinh y-y\ge y^3/6$; it is not asymptotic in the self-consistent regime, where $\delta T^*\gtrsim1.2$. For fixed $\delta$ and $L\to\infty$, $T^*\sim\log(2\delta L)/(2\delta)$, so $T^{*3}=O(\log^3L)=o(L)$. The exact self-consistency threshold is $\delta L>y_0=2.1773\ldots$, $\sinh y_0=2y_0$, not $2.45$. See R163_401 Lemma 4.10 and Cor 4.10a.)*

  §2's density-limited branch and §3 are correctly labelled HEURISTIC/UNCERTIFIED.

## 2. Fixes required (labels and errors)

1. **Lemma 3.4(e).** The disc $|z-x_0|\le r$ reaches $|y|=r\ge\delta$, so the bound must be
   $M_2\le T^2e^{Tr}\|G\|_\infty$, not $e^{T\delta}$.
2. **§4.7 is vacuous at cell scale.** The bound $P_j\ge G'(x_j)^2\sum(\gamma-x_j)^2(1-\epsilon_j)^2$ is valid only
   with $(1-\epsilon_j)_+$.
   - Bernstein gives $|G'|\lesssim T\|G\|$ and generically $M_2\asymp T^2\|G\|$ locally. With $h_j\asymp\pi/T$ this
     makes $\epsilon_j=M_2h_j/(2|G'(x_j)|)\gtrsim\pi/2>1$ for typical cells.
   - The Lorentzian linearisation is valid only on scale $r\ll1/T$, not on a cell of length $\pi/T$.
   - So the lower bound on $P_j$ is generically empty. The heuristic (I0) ($P_j\approx\bar n_jh_j^2G'^2/12$) uses the
     linearisation outside its range.
   - Fix: keep $P_j=\sum_{C_j}G(\gamma)^2$ exactly and do not linearise.
3. **Prop 4.0 (⇒) is labelled PROVED, but it rests on 2.4(ii).** 2.4(ii) is the real-rooted witness of R160_X_C1
   Thm R, a record result that has not been re-audited. Relabel as PROVED-CITED (conditional on record).
   - On the Blaschke step: flipping a zero $w\mapsto\bar w$ leaves $\widehat F\widehat F^\#$ unchanged. So (1.1)
     preserves $W$, even though $A(F)$ and $B(F)$ individually change. This part is sound.
   - The flip does **not** make zeros real. The real-rootedness rests entirely on the eigenspace/parity-crossing
     argument, which is load-bearing and unaudited.
4. **§4.4, odd case.** $\widehat F'(x)^2=-G'(x)^2$, so $w_x=W(H_x)/\widehat F'(x)^2$ would be $\le0$. The definition
   must be $w_x=W(H_x)/|\widehat F'(x)|^2$. "Up to sign convention" is not acceptable in a PROVED step.
5. **§4.2.** $\sum_{\gamma\le R}\delta^2\ll R(\log\log R)^2/\log R$ is cited to R163_115 (record). The standard
   result is Selberg's $\sum_{\beta>1/2}(\beta-\tfrac12)\ll R\log\log R$. Either re-prove the stronger bound or
   replace it; it is not load-bearing. Minor: $\tfrac12\log(3\cdot10^{12}/2\pi)\approx13.4$, not $13.1$.
6. **§4.8, "$n^{\rm off}_j$ is small by the density bounds".** Density bounds are averages. Any cell that contains a
   quartet has $n^{\rm off}_j\ge1$, so nothing makes it small. This is the same non-localisation as (I1-a).

## 3. §4.8–4.9: circularity and a counterexample to the heuristic

- **Circularity (E1).** Under ¬RH the witness gives the exact identity $\sum_j(P_j-N_j)=0$ (§4.7 is an identity, not
  an estimate). So "$(\star_{\rm cell})$ at the witness" is literally the negation of the existence of the witness. By
  Prop 4.0, it is RH. The memo presents $(\star_{\rm cell})$ as "the one non-restating inequality", but it is not
  non-restating unless it is proved for a class of $G$ strictly larger than witnesses, using data that $M_m$ lacks.
  No such class is named.
- **Counterexample to the (I0) heuristic (lattice model, R163_402 Thm 4).** Take on-line ordinates on an exact lattice
  of density $\rho$ and one quartet with $\delta<\tfrac12$.
  - In the large-δ branch the inf of the form is $0$ at $T^*$, attained by $b=\sinh\delta u$. This is a witness
    whose node sits at the cone vertex, as Lemma 3.4 predicts.
  - All other cells have $P_j\ge0$, so in the quartet's cell $P_0-N_0=-\sum_{j\ne0}P_j\le0$, and $(\star_{\rm cell})$
    fails.
  - Moreover $T^{*3}=\tfrac34\log(\gamma/2\pi)/\delta^2>3\log(\gamma/2\pi)>\tfrac{\pi^2}6\log(\gamma/2\pi)$. So the
    contact always lies outside the range $T^3\ll\tfrac{\pi^2}{6}\log$ in which §4.8 (I0) claims that (I1) holds "by a
    large factor".
    *(Erratum to this bullet, R163_590 D1: the cubic value is only an upper bound, $T^*\le(\tfrac34L/\delta^2)^{1/3}$ with $L=\log(\gamma/2\pi)$, since $\sinh y-y\ge y^3/6$; it is not asymptotic in the self-consistent regime, where $\delta T^*\gtrsim1.2$. For fixed $\delta$ and $L\to\infty$, $T^*\sim\log(2\delta L)/(2\delta)$, so $T^{*3}=O(\log^3L)=o(L)$. The exact self-consistency threshold is $\delta L>y_0=2.1773\ldots$, $\sinh y_0=2y_0$, not $2.45$. The conclusion survives with the reason corrected: for fixed $\delta$ and large $L$ the contact lies *inside* the range of (I0), which is refuted a fortiori. See R163_401 Lemma 4.10 and Cor 4.10a.)*
  - This happens although (I1-T) holds there ($T^*<\pi\rho$). Hence **(I1-T) is necessary but not sufficient**, and
    regime (α) of §4.9 is empty in the model.
  - The density-limited branch (R163_402 §2–3, heuristic and uncertified) puts small-δ contacts *above* the Landau
    ceiling, where (I1-T) fails outright. This agrees with regime (β).
- **Theorem M.** (I1) with a fixed $\eta>0$ is a per-window margin. At a true witness no margin exists: the bottom is
  $0$, and nearby $\lambda^{\rm A}_T\le\exp(-e^{(2-\varepsilon)T})$. Any proof of $(\star_{\rm cell})$ through
  estimates with slack $\eta$ is code M. Only an exact (identity-level) mechanism could work, and none is offered.
- **Hidden positivity.** None was found beyond $W_T\ge0$ at $T_c$, which is legitimate. §4.5's quadrature is
  conditional on (Q) (OPEN) and is not used in the sign step.

## 4. Falsifier battery (Paper 48 minimal battery)

| model | finding |
|---|---|
| **Davenport–Heilbronn** | **The memo's claim of separation by (I2) is wrong.** DH has off-line zeros with $\tfrac12<\beta<1$, for example $\rho\approx0.8085+85.699i$ (Spira 1994; Balanzario–Sánchez-Ortiz 2007), so $\delta\approx0.31<\tfrac12$. In a cell containing such a quartet, every line of §§3–4.8 holds verbatim for DH: the zero-side identity, the cone, the cell identity, and (I2) itself. Whether $(\star_{\rm cell})$ holds there is the same open question. So the sign step is not separated from DH (F3:DH, W3); the zeros in $\sigma>1$ are irrelevant to such cells. |
| Epstein ($h>1$) | Same objection: Epstein functions also have off-line zeros in $\tfrac12<\sigma<1$, so (I2) does not separate them. T2: the chain uses no axiom beyond A1–A6 at the sign step. |
| Beurling–DMV, $\zeta_\theta$ | They are excluded only because there is no Weil form centred at $\tfrac12$, i.e. by the functional equation and not by integrality. The memo admits this. S4 is violated. |
| two-atom Type I curve | It lies below ½log5, outside CL's range. The sign step is zero-side, so S8 is not triggered. Correct. |
| deletion, κ-models | (1.1) fails for them, so they are irrelevant. Correct. The regularised-jet invariance (S7) is respected, because the chain sees $\Lambda$ only through (1.1). |
| $M_m$ | Decisive and correctly identified. $M_m$ satisfies every hypothesis used up to (I1), including $\delta<\tfrac12$ and $\gamma_q$ beyond any verification height, and it has a witness. So $(\star_{\rm cell})$ is false for $M_m$, and no proof can use only the on-line zeros, the off-line positions and δ. |

## 5. Bottom line

- §§1–3 are sound with fix 1. §4.1–4.7 are sound with fixes 2–6; §4.7 is vacuous as an estimate.
- §4 does not close CL. The missing step is **$(\star_{\rm cell})$/(I1)** at the witness, and it is RH-equivalent there
  (E1).
- Its supporting heuristic (I0) is refuted in the lattice model, where the contact always lies at
  $T^3>3\log(\gamma/2\pi)$. *(Erratum, R163_590 D1: the location claim is false; the refutation of (I0) survives, see the erratum in §3.)*
- The δ<½ input does not separate DH or Epstein. The Euler product and integrality still do not enter the sign step
  (S4, as the memo's Remark 4.8 concedes).
- Row D: **OPEN**. No label moves. R163_402: correct as labelled. Its Theorem 4 is the most useful new rigorous item:
  an exact threshold in the lattice model, and the counter-model to (I0).
