# Audit : L70 (Liu, "Certified Weil Positivity Beyond the Unit Window")

Read-only audit. Paper 47 not edited.

## 1. Identification
- Title: "Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function".
- Author: Vincent Liu (AI-Native Mathematical Research Lab, Taiwan). Manuscript date 14 Sep 2026, alphaXiv posting 15 Sep 2026.
- Location: https://www.alphaxiv.org/abs/2609.weil-positivity-riemann-zeta-bounds (PDF read in full, 1392 text lines). No arXiv id found.
- Status: "preprint / manuscript under review" (Math. Comp. per the alphaXiv page). The paper itself says alphaXiv is not peer review and that "a public archival identifier and a finalized data/code license have not been supplied". The certificate is NOT publicly reproducible yet. The author declares AI tools (ChatGPT/Codex) as research support.
- Corpus: R186_027 (phase-186-toolbox, row 2) mentions it only for its method (block-Schur, Legendre, rank-two tail), not for its range. Master grid R162_2300 3A has the residual "S5 §5#14: web hit ... sin leer" (OPEN, "could move [compl] endpoint"). That residual is now resolved: it does move the endpoint, CITED.

## 2. Setting and normalization (Liu §2, eq. (1))
- D_L = C_c^∞((−L,L);ℂ), H_L = L²(−L,L). "Half-width L" = support of f in (−L,L), so supp h_f ⊂ (−2L,2L) and the sum runs over log n < 2L.
- Q(f) = P(f) + (1/2π)∫A(t)|F_f(t)|²dt − Σ c_n H_f(log n), c_n = 2Λ(n)/√n, A(t) = Re ψ(1/4+it/2) − log π, P(f) = 2Re(F_f(i/2)·conj F_f(−i/2)). This is the COMPLETE form (pole term kept, no Tate/pole-vanishing constraint), arbitrary complex tests.
- Thm A: Q ≥ 2^−151‖f‖² on D_1. Thm B: Q ≥ 2^−49162‖f‖² on D_{17/16} (log 8 < 17/8 < log 9; all of 2,3,4,5,7,8 kept). Rigor: interval enclosures + exact integer Gram residual certificates on two 224×224 integer matrices + analytic complement/tail bounds (block-Schur).
- Obstruction theorem: a specified tail-dropping lower comparison has negative high-frequency limit once L > ½log 8 (concerns the comparison, not Q).

Matching with Paper 47: N_T = {n: log n < 2T}, v_n = 2Λ(n)/√n (v_2 = 2log2/√2 matches c_2), F(±i/2) are the Tate moments A, B, so P = 2Re(A B̄) and Q = W_T = 𝔞_T + 2Re(A B̄) on L²(I_T), I_T = [−T,T]. Hence **L = T**. Liu states his normalization agrees with CC21 (149)–(154) and with Zhu; Paper 47 already identifies Zhu's half-width 0.8 with T = 0.8 (main.tex 142, 302–304, 4605, 4656). Liu: the 17/16 window has autocorrelation support 17/8 (L70's "≈ log 8.4" is correct: e^{2.125} ≈ 8.37).
- Domain: Liu's bound is on C_c^∞, Paper 47's λ^W_T is on L²(I_T) (form domain). C_c^∞ is a form core (Liu cites CC23/Suzuki; Paper 47 has its own closure lemmas), so the bound passes to the bottom. Minor check, not a gap.

## 3. Verdict
If Liu Thm B is correct: λ^W_T ≥ 2^−49162 for all 0 < T ≤ 17/16 (monotonicity, Paper 47 lem:monoT), and since λ^W_T ≤ λ^prim ≤ λ_A(T) (Paper 47 thm:A, rem:Kprim), also λ_A(T) > 0 on (0, 17/16]. 17/16 = 1.0625 > ½log5 = 0.8047; even Thm A (T = 1 > ½log 7 = 0.973) passes ½log5. **So Paper 47's "certified range up to ½log5" is superseded in range (not in constant) — label CITED (alphaXiv preprint, unrefereed, certificate not yet publicly archived).** Paper 47's own theorems (log5A/W) stay PROVED and keep much larger constants (2.5e-12, 1e-18 vs 2^−151 ≈ 3.5e-46).
Caveat: the constants 2^−151 and 2^−49162 come from a block-Schur with doubly exponential loss (consistent with Paper 47 prop:env / Zhu Thm 1.4); this is a range record, not a method toward all T. No effect on Gate/D mechanism; it changes the first-contact lower bound from ½log5 to 17/16 (CITED).

## 4. Paper 47 sentences that become outdated (main.tex line numbers)
Rule: keep every PROVED statement; add the cited extension; do not replace ½log5 in statements proved in-paper.

(a) l.141–142 intro: "...and was certified by Zhu for $T\le0.8$ \cite[Thm.~1.2]{Zhu2026}."
→ "...was certified by Zhu for $T\le0.8$ \cite[Thm.~1.2]{Zhu2026}, and, in a preprint under review, by Liu for $T\le17/16$ with $\lamW\ge2^{-49162}$ \cite[Thm.~B]{Liu2026} (CITED; not used in any proof here)."

(b) l.154–155: "The window $\frac12\log5$ is the last one with contact set $\{2,3,4\}$." — still true; append: "Liu \cite{Liu2026} reports a certified complete-form bound up to $T=17/16$, past the contacts $5,7,8$, with constant $2^{-49162}$."

(c) l.201–203 first contact: "there is a first window $T_*>\frac12\log5$" → "there is a first window $T_*>\frac12\log5$ (and $T_*>17/16$ if \cite[Thm.~B]{Liu2026} is granted)". Same pattern at l.222 ($T_c>\frac12\log5$) and abstract l.86.

(d) l.269–272 "What remains open": "Apart from the certified range, none of the results gives the sign of $\mathfrak a_T$ at a window $T>\frac12\log5$." → add: "Beyond $\frac12\log5$ the only certificate we know of is \cite{Liu2026} ($T\le17/16$, preprint under review); the open problem is unchanged for $T>17/16$." The open-problem quantifier "for every $T>\frac12\log5$" may stay (it is what this paper reduces), optionally "for every $T>17/16$ (by \cite{Liu2026}, CITED)".

(e) l.309: "...and the extension of the certified range to $\frac12\log5$." → "...and an independent certification up to $\frac12\log5$ with constants $2.5\cdot10^{-12}$ (primitive) and $10^{-18}$ (complete); a larger range, $T\le17/16$, with constant $2^{-49162}$, is claimed in \cite{Liu2026}." Also add Liu to the related-work paragraph l.302–305.

(f) l.4604–4605 §sec:log5: "...and it lies slightly beyond the range $T\le0.8$ of \cite[Thm.~1.2]{Zhu2026}." → append "; the range $T\le1$ and $T\le17/16$ is claimed, with much smaller constants $2^{-151}$ and $2^{-49162}$, in \cite[Thms.~A, B]{Liu2026}."

(g) l.4654–4664 rem:log5scope: "The gain over \cite[Thm.~1.2]{Zhu2026} is small, from $0.8$ to $0.80472$" → keep, add: "It is not the largest certified window: \cite{Liu2026} (preprint under review) claims $T\le17/16$. Our certificate is independent, uses a different section and gives constants larger by more than thirty orders of magnitude at $T\le\frac12\log5$." And "the first window with the new contact $5$ is not treated" → "...is not treated here (it is covered by \cite[Thm.~B]{Liu2026}, CITED)."

(h) l.3316–3318 rem (known proofs at individual windows): append "and \cite[Thm.~B]{Liu2026} for $T\le17/16$ (the complete form; preprint)."

(i) l.4700–4703 cor:beyond5: proof is internal and stays PROVED; add a remark: "Granting \cite[Thm.~B]{Liu2026}, $\lamW>0$ on $(0,17/16]$, which contains the contacts $5,7,8$; the corollary is the in-paper, unconditional statement."

(j) l.1081–1083 (cert at ½log3) and l.2274: no change needed.

New bibitem:
\bibitem{Liu2026} V.~Liu, \emph{Certified Weil positivity beyond the unit window: source-exact block-Schur and tail-compensation bounds for the Riemann zeta function}, preprint (alphaXiv, 15 Sep 2026), under review.

## 5. Records to update (not done here)
- Grid R162_2300 3A: close residual "S5 §5#14" → READ; complete-form endpoint 17/16 CITED (unrefereed).
- 05b L70: correct "COVERED (R186_027)" to "method covered in R186_027; range fact newly recorded here".
