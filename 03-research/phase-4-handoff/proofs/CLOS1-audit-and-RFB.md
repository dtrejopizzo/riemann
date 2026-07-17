# Day 8 — Audit of CLOS.1, and the (RFB) attack as a Carleson problem

Two tasks in parallel (per referee): (A) audit CLOS.1 before it becomes foundation — three weak points
flagged; (B) attack (RFB), with the warning that it is a **Carleson/interpolation** condition, not raw
density. **Tags:** ✅ rigorous · ⬜ open · ⚠️ corrected.

---

# Part A — Audit of CLOS.1 (three weak points)

### A.1 Does $\sum_\gamma|\langle g,K_\gamma\rangle|^2$ equal the closure of the *original* core form? ⚠️
**Weak point (referee #1).** CLOS.1 proves the *sum-of-evaluations* form $\mathfrak t_+$ is closed (Kato).
That is **not** the same as proving it equals $\overline{\mathfrak t_+|_{\mathcal D}}$, the closure of the
form coming from the Weil core. **Status now:** what is rigorous is only
$$
\mathfrak t_+|_{\mathcal D}\ \text{is closable}\quad(\text{closed extension }\mathfrak t_+\text{ exists}),\qquad \overline{\mathfrak t_+|_{\mathcal D}}\subseteq\mathfrak t_+ .
$$
Equality $\iff$ $\mathcal D$ is a form-core. The earlier "closure $=\mathfrak t_+$" was an **overclaim,
retracted** (and corrected in `closure-in-HEgamma.md`).

### A.2 The form-core question — the most delicate point ⬜
**Need:** $\overline{\mathcal D}^{\,\|\cdot\|_{\mathfrak t_+}}=D(\mathfrak t_+)$, with
$\|g\|^2_{\mathfrak t_+}=\|g\|^2_{H(E)}+\sum_\gamma|\widehat g(\gamma)|^2$. If this fails, Kato still gives a
closed $\mathfrak t_+$, but the operator obtained **from the core** $\overline{\mathfrak t_+|_{\mathcal D}}$
is a *proper restriction* — a **different operator** with possibly different spectrum. Historically this is
exactly where spectral programs die. **What we can say now:**
- ✅ A non-negative self-adjoint operator $\overline{T_+}\ge0$ exists (closability, A.1).
- ⬜ Whether $\overline{T_+}$ is the "maximal" $T_+$ (zeros-indexed) is the form-core question — **OPEN**.
- **Sufficient condition to pursue:** $\mathcal D$ is a form-core iff Hermite–Gauss localizers are dense in
  $D(\mathfrak t_+)$ in the graph norm. Plausible because $\{K_\gamma\}$ and the Hermite basis are both
  natural for the $\tfrac1{2\pi}\log$-density geometry, but **must be proved, not assumed.**

### A.3 What in CLOS.1/CLOS.2 survives the audit ✅
- **CLOS.1 (corrected):** $\mathfrak t_+|_{\mathcal D}$ closable; $\overline{T_+}\ge0$ exists. ✅
- **CLOS.2 (corrected):** under RH, $\mathfrak t|_{\mathcal D}=\mathfrak t_+|_{\mathcal D}$ closable; a
  bounded-below (by $0$) self-adjoint realization **from the core** exists in $H(E_\gamma)$. ✅ *This much
  needs no form-core claim* — closability of the restriction is automatic.
- **Downgraded:** identifying $\operatorname{spec}(\overline{T_+})$ with the zeros / the maximal operator
  (needs A.2).

> **Net of Part A.** The *existence* of a legitimate closed Weil form and bounded-below operator from the
> core in $H(E_\gamma)$ **survives** (RH-world). The *identification* of its spectrum with the zeta zeros
> is the open form-core question A.2 — now the second load-bearing item (with EF-id's closure). CLOS.1 is
> **not** yet a green box; it is "✅ existence / ⬜ identification."

---

# Part B — (RFB) is a Carleson condition; first real bounds

Recall the target (closes B-2): $\;|\mathfrak t_-(g)|\le a\,\mathfrak t_+(g)+C\|g\|^2$, $a<1$.

### B.1 Reduction to a positive Carleson bound ✅
Since $|\mathrm{Re}[z^2]|\le|z|^2$,
$$
|\mathfrak t_-(g)|=\Big|\sum_{\text{off-line}}4\,\mathrm{Re}[\widehat g(t-ib)^2]\Big|\ \le\ 4\sum_{\text{off-line}}|\widehat g(t-ib)|^2 .
$$
So (RFB) follows from
$$
\boxed{\ 4\sum_{\text{off-line }\rho}|\widehat g(t-ib)|^2\ \le\ a\,\mathfrak t_+(g)+C\|g\|^2_{H(E)}\ }\tag{RFB$'$}
$$
i.e. the **off-line-zero measure** $\mu_{\mathrm{off}}:=4\sum_{\text{off-line}}\delta_{\,t-ib}$ (points in
the open strip, at the off-line ordinates) must be a **Carleson measure for $H(E_\gamma)$**, with constant
controlled (relatively) by the on-line evaluation form. **This is the referee's point made precise:
(RFB) $=$ a Carleson/embedding condition, NOT a raw density count.**

### B.2 A clean sufficient condition (Hilbert–Schmidt / trace) ✅
By the reproducing property, $|\widehat g(w)|^2=|\langle g,K_w\rangle|^2\le K(w,w)\,\|g\|^2_{H(E)}$. Hence
$$
4\sum_{\text{off-line}}|\widehat g(t-ib)|^2\ \le\ \Big[\,4\!\!\sum_{\text{off-line}}\!\!K(t-ib,\,t-ib)\Big]\,\|g\|^2_{H(E)} .
$$
$$
\boxed{\ \text{If }\ S_{\mathrm{off}}:=\sum_{\text{off-line }\rho}K_{H(E_\gamma)}(t-ib,\,t-ib)<\infty\ \Longrightarrow\ \mathfrak t_-\ \text{is BOUNDED}\ \Longrightarrow\ \text{(RFB) with }a=0.\ }
$$
Then $\mathfrak t=\mathfrak t_++\mathfrak t_-$ is a **bounded perturbation** of the closed $\mathfrak t_+$:
closed and semibounded by $-\tfrac14 S_{\mathrm{off}}$. **B-2 settled**, and — since the bottom can then be
$<0$ when off-line zeros exist — this is exactly the **"B-2 true, RH false" separation** §3.3 wanted.

### B.3 When does $S_{\mathrm{off}}<\infty$? — density vs the dangerous edge ⬜
The diagonal kernel $K(w,w)$ of the Gamma-factor de Branges space grows (i) with $|t|$ like the
$\tfrac1{2\pi}\log$ density, and (ii) **blows up as $w$ nears the strip edge** $|\Im w|\to\tfrac12$, i.e. as
$\beta\to0$ or $1$. An off-line zero $\rho=\beta+it$ sits at depth $|b|=|\beta-\tfrac12|<\tfrac12$. So:
- **Shallow off-line zeros** ($\beta$ near $\tfrac12$, $b\to0$): $K$ moderate, but possibly *many* — controlled
  by zero density **near the line**.
- **Deep off-line zeros** ($\beta$ near $0$ or $1$, $|b|\to\tfrac12$): $K$ **blows up**, but these are the
  *rarest* — zero-density bounds $N(\sigma,T)$ are strongest (smallest) for $\sigma$ near $1$.
$$
S_{\mathrm{off}}=\sum_{\text{off-line}}K(t-ib,t-ib)\ \asymp\ \int\!\!\int K(t-ib,t-ib)\,dN(\beta,t),\qquad dN=\text{off-line zero-counting measure}.
$$
So $S_{\mathrm{off}}<\infty$ is a **weighted zero-density integral** — convergent iff the off-line zeros are
sparse enough that their count, *weighted by the edge-blowup of $K$*, integrates. This is the precise
content, and it is genuinely a **Carleson/density** statement, finer than a bare count (the referee's #3).

### B.4 Honest limits of B.2 (when $a=0$ is too much to hope for) ⬜
If $S_{\mathrm{off}}=\infty$ (e.g. RH fails so badly that off-line zeros are too dense or too deep), the
crude norm bound dies and one must use the *relative* term: control each off-line evaluation
$\widehat g(t-ib)$ by **nearby on-line evaluations** $\widehat g(\gamma)$, $\gamma\approx t$ real — a genuine
**interpolation** estimate (off-axis value from on-axis samples), exploiting that an off-line zero at
$t-ib$ has on-line zeros at real ordinates clustering near $t$. This is the $a>0$ regime, and it is where
the fine geometry (Carleson boxes, the actual fluctuation $S(T)$ of zeros, not just the smooth density)
enters. **So the honest statement is the referee's:**
$$
\boxed{\ \text{B-2}\ \Longleftarrow\ \text{($\mu_{\mathrm{off}}$ is Carleson for }H(E_\gamma)\text{)}\ \Longleftarrow\ \text{a zero-density / zero-free-region input;}\quad\text{B-2}\neq\text{raw density.}\ }
$$

### B.5 Status of (RFB)
| Step | Statement | Status |
|---|---|---|
| B.1 | (RFB) $\Leftarrow$ (RFB$'$): $\mu_{\mathrm{off}}$ Carleson for $H(E_\gamma)$ (relatively) | ✅ reduction |
| B.2 | $S_{\mathrm{off}}=\sum K(t-ib,t-ib)<\infty\Rightarrow\mathfrak t_-$ bounded $\Rightarrow$ (RFB), $a=0$, **B-2 done** | ✅ sufficient condition |
| B.3 | $S_{\mathrm{off}}<\infty$ $=$ weighted zero-density integral (edge-blowup of $K$ × off-line count) | ⬜ open (density input) |
| B.4 | if $S_{\mathrm{off}}=\infty$: need relative/interpolation ($a>0$) — Carleson-box fine geometry | ⬜ open (harder) |

---

## Net (Day 8)
- **Part A:** CLOS.1 audited; the "closure $=\mathfrak t_+$" overclaim **retracted**. What survives:
  existence of a bounded-below closed Weil operator **from the core** in $H(E_\gamma)$ (RH-world).
  **Open and now load-bearing:** the **form-core** question A.2 (is $\overline{\mathfrak t_+|_{\mathcal D}}$
  the maximal $T_+$?). CLOS.1 is "✅ existence / ⬜ identification," not a green box.
- **Part B:** (RFB) restated correctly as a **Carleson condition** for the off-line-zero measure on
  $H(E_\gamma)$ (referee #3 was right). A clean **sufficient** condition — $S_{\mathrm{off}}=\sum K(t-ib,t-ib)<\infty$,
  a kernel-weighted zero-density integral — would give $\mathfrak t_-$ **bounded** and settle B-2 with the
  desired RH-false separation. The dangerous zeros are the *deep* ones (near the strip edge), which are
  also the *rarest* — a genuine tension to be resolved by a zero-density/zero-free-region input.
- **Corrected logical order (referee).** "Does the Weil form close & control in $H(E_\gamma)$?" (CLOS +
  RFB + form-core) is now **logically prior** to the 0A2 faithful-compression question. 0A2 regains
  meaning only once $\overline{T_+}$ is shown to be the right operator.

**Next:** (1) the **form-core** A.2 (Hermite density in graph norm) — audit before building; (2) make B.3
quantitative: pick a zero-density bound, estimate $S_{\mathrm{off}}$, find the weakest input giving
convergence; (3) Bombieri's normalization — his semiboundedness analysis should be exactly B.1–B.4.
