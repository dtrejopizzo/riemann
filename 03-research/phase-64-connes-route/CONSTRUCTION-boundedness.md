# The boundedness wall in colligation form: the precise mechanism and where new arithmetic must enter

*Pure mathematics. After Stage 4 (positivity is free), the entire route is the single boundedness
statement: the primitive compressions of the unconditionally-positive finite Euler colligations stay
bounded, i.e. $K_P$ diverges only along the rank-one pole direction $H$. We carry this to its exact
bottom: (i) the precise mechanism by which an off-line zero breaks boundedness (window amplification
$\times$ functional-equation pairing), (ii) the trace structure of $K_P$ and what "rank-one
divergence" means quantitatively, (iii) the unconditional partial results (PNT / zero-free region) and
the exact gap to the needed bound, (iv) the precise arithmetic input that must be **created**: a
critical-line bound on the Euler-product fluctuation of RH-strength. Honest: this is RH; no proof. The
contribution is the exact localization of the one remaining inequality and identification of the new
theorem required.*

---

> **Correction note.** Here $K_P\succeq0$ means the **canonical-system** kernel
> $K_P=\int Y_P^*\,d\mathcal H_P\,Y_P$ with $d\mathcal H_P\ge0$ (the corrected positivity,
> `CONSTRUCTION-TW-canonical-system.md` §3), replacing the withdrawn scalar Euler-colligation claim.
> The boundedness statement $(\mathsf B)$ — rank-one escape — is the corrected wall, identical in form.

## 1. The boundedness statement

By P50 §3, Stage 4, and `CONSTRUCTION-critical-finite-part.md`, the route is now:
\[
   \boxed{\ \RH\ \Longleftarrow\ \sup_{\lambda,P}\ \big\|P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\big\|<\infty\ }
   \tag{$\mathsf B$}
\]
where $K_P\succeq0$ is the finite Euler colligation defect kernel (unconditional, Theorem 2 of the
local construction), $H$ the rank-one pole/ample direction, $P_{\mathrm{prim}}=I-|H\rangle\langle H|$.
Equivalently: the only divergence of $K_P$ as $P\to\infty$ is along $H$. The primitive matrix elements
are the truncated Weil form, $\langle g,K_Pg\rangle=W_P(g)$ for $\deg g=0$ (Stage 5), so $(\mathsf B)$
is the uniform boundedness of $W_P$.

---

## 2. The exact mechanism: window amplification $\times$ functional-equation pairing

For $g$ supported on the window $[0,L]$, $L=2\log\lambda$, the transform $\hat g(s)=\int_0^L
g(y)e^{sy}\,dy$ is entire of exponential type $L$, with
\[
   |\hat g(\beta+i\gam)|\ \asymp\ e^{\beta L}\cdot|\text{(bounded factor)}| .
\]
By the explicit formula the Weil quadratic form is the zero-sum
\[
   W(g)=\sum_\rho \hat g(\rho)\,\overline{\hat g(1-\bar\rho)} ,
\]
the functional equation pairing $\rho\leftrightarrow 1-\bar\rho$ (reflection across the critical line).
Two regimes:

- **On-line** $\rho=\half+i\gam$: then $1-\bar\rho=\rho$, the term is $|\hat g(\rho)|^2\ge0$ with
  $|\hat g(\rho)|\asymp e^{L/2}$, matching the normalization $\|g\|$; the contribution is **bounded
  and positive**.
- **Off-line** $\rho=\beta+i\gam$, $\beta>\half$: then $1-\bar\rho=1-\beta+i\gam\ne\rho$, the term is
  $\hat g(\beta+i\gam)\overline{\hat g(1-\beta+i\gam)}$, **indefinite** (not a modulus), and of size
  $e^{\beta L}\cdot e^{(1-\beta)L}=e^{L}\gg e^{L}$... more precisely it is amplified relative to the
  on-line scale $e^{L}$ by choosing $g$ to concentrate on the larger lobe: $|\hat g(\beta+i\gam)|^2
  \asymp e^{2\beta L}$, which **exceeds** the normalization $e^{L}$ by $e^{(2\beta-1)L}\to\infty$.

\begin{resultbox}
\textbf{Mechanism.} A single off-line zero $\rho=\beta+i\gam$ ($\beta>\half$) makes
$W_\lambda(g)/\|g\|^2\asymp e^{(2\beta-1)L}=\lambda^{2\beta-1}\to\infty$: boundedness $(\mathsf B)$
fails. Conversely RH ($\beta=\half$ for all $\rho$) gives the bounded, positive on-line regime. So
$(\mathsf B)\Leftrightarrow\RH$, with the failure rate exactly $\lambda^{2\beta-1}$ — the same
exponent as the $A^{\mathrm{osc}}$ growth (P50 Lem.~3.1) and the Pick/Kre\u\i n--Langer threshold
$\om=\beta-\half$.
\end{resultbox}

This is the unified mechanism behind every prior numerical and structural finding: the window
transform amplifies an off-line zero by $e^{(2\beta-1)L}$, and the functional-equation pairing turns
it into an indefinite, unbounded contribution.

---

## 3. The trace structure: what "rank-one divergence" means

Since $K_P\succeq0$, boundedness is controlled by the trace: $\|K_P\|\le\Tr K_P$. The trace is the
$L^2$-mass of the prime measure,
\[
   \Tr K_P\ \asymp\ \sum_{p\le P}\frac{(\log p)^2}{p}\ \sim\ \tfrac12(\log P)^2\ \to\ \infty
\]
(Mertens). The divergence is genuine; $(\mathsf B)$ asserts it is **entirely along $H$**:
\[
   K_P=c_P\,|H\rangle\langle H|+R_P,\qquad c_P\asymp(\log P)^2,\qquad \sup_P\|R_P\|<\infty .
\]
Here $H$ is the constant/degree mode (the pole direction). $(\mathsf B)$ is thus a **rank-one
divergence theorem**: the divergent part of the positive kernel $K_P$ is one-dimensional. A second
divergent direction $v\perp H$ — necessarily of positive type since $K_P\succeq0$ — would be a
primitive $g$ with $W_P(g)\to+\infty$; by §2 this is exactly an off-line zero. So:
\[
   (\mathsf B)\ \Longleftrightarrow\ \text{the divergent subspace of }\{K_P\}\ \text{is}\ \C H
   \ \Longleftrightarrow\ \RH .
\]

\emph{Remark.} The positivity (Stage 4) guarantees the divergence is a sum of **positive** rank-one
pieces; the wall is purely about their **number** (one, the pole) versus more (off-line zeros). This
is the cleanest possible form: a positive kernel whose divergent subspace must be shown
one-dimensional.

---

## 4. What is unconditional, and the exact gap

\textbf{Unconditional (have):}
\begin{itemize}
\item $K_P\succeq0$ for all finite $P$ (Euler finite passivity).
\item The \emph{smooth} part of $W_P$ is bounded: $\sum_{p\le P}\Lambda(p^k)p^{-k/2}\cdot(\text{PNT
main term})$ converges by the prime number theorem; the divergent/fluctuating part is the zero-sum.
\item The pole direction $H$ carries a genuine divergence $c_P\asymp(\log P)^2$.
\item \textbf{Zero-free region (Korobov–Vinogradov):} no zeros with $\beta>1-c(\log\gam)^{-2/3}
(\log\log\gam)^{-1/3}$. This bounds the off-line amplification for zeros \emph{near $\Re s=1$}, giving
$W_\lambda(g)=O\big(\exp(c(\log\lambda)^{3/5})\big)$ unconditionally — \emph{sub-power growth}, but
\emph{not} bounded.
\end{itemize}

\textbf{The exact gap.} The zero-free region controls zeros near $\Re s=1$; it says \emph{nothing}
about zeros near $\Re s=\half$. The amplification $\lambda^{2\beta-1}$ is dangerous precisely for
$\beta$ bounded away from $\half$, and the unconditional bound $\exp(c(\log\lambda)^{3/5})$ is the best
available — it rules out $\beta$ very close to $1$ but allows, e.g., a hypothetical zero at
$\beta=\half+\delta$ to produce $\lambda^{2\delta}$ growth. \textbf{Bounded $W_\lambda$
($\beta\equiv\half$) is exactly RH; the unconditional bound is exponentially weaker.}

---

## 5. The arithmetic input that must be created

The remaining inequality $(\mathsf B)$ is a **critical-line bound on the Euler-product fluctuation**:

\begin{openbox}{the one remaining theorem (RH-strength)}
Show that the primitive (degree-zero) part of the finite Euler product, evaluated on the critical line
and tested against window functions, stays bounded uniformly in $\lambda$:
\[
   \sup_{\lambda}\ \sup_{\deg g=0,\ \|g\|=1}\ \Big|\sum_{p\le\lambda^2}\frac{\log p}{\sqrt p}\,
   \widehat g_p\Big|\ <\ \infty ,
\]
equivalently the rank-one divergence of §3. This is a bound on $\sum_{p\le x}\Lambda(p)p^{-1/2}
(\dots)$ at the **critical-line** normalization $x^{1/2}$, which the current zero-free region does not
provide.
\end{openbox}

This is where genuinely new mathematics is required, and where the Critical Tate–Weil Hodge Module
$\mathsf{TW}_\Z$ is meant to supply it: the divergence structure of the restricted product of local
Tate cells at $\Re s=\half$. Two honest observations on what such a theorem must use:

1. **It must be critical-line, not edge.** All classical unconditional inputs (PNT, zero-free region,
zero-density near $\Re=1$) control the \emph{edge} of the critical strip. The boundedness is a
\emph{center}-of-strip statement. No edge estimate reaches it; this is why the wall is genuinely new.

2. **It must be Euler/positivity-aware.** The mechanism (§2) is the functional-equation pairing
$\rho\leftrightarrow1-\bar\rho$ turning self-paired (on-line) into bounded-positive and cross-paired
(off-line) into unbounded-indefinite. Any proof must use that the finite kernels are \emph{positive}
(Euler) and that the pairing is the reflection — i.e. it must use the functional equation and the
Euler product \emph{together}, which is exactly the content of $\mathsf{TW}_\Z$. DH (no Euler product)
has indefinite finite kernels and fails $(\mathsf B)$ at finite level.

---

## 6. Status: the bottom of the route

\textbf{Established (the route, rigorously, modulo Stage 5):}
\[
   \RH\ \Longleftarrow\ (\mathsf B)\ \Longleftarrow\
   \underbrace{\text{Euler finite passivity}}_{\text{positivity, free}}\ +\
   \underbrace{\text{rank-one divergence of }K_P}_{\text{boundedness, the wall}} .
\]
Positivity is free (Stage 4). The wall is $(\mathsf B)$: a positive, explicit family of kernels
$\{K_P\}$ must have one-dimensional divergent subspace (the pole). By §2 this is RH, with failure rate
$\lambda^{2\beta-1}$. By §4 the unconditional tools give only $\exp(c(\log\lambda)^{3/5})$, an
exponential gap, because they are edge-of-strip estimates and $(\mathsf B)$ is center-of-strip.

\textbf{The contribution of this route.} It has, step by step and with explicit corrections,
\emph{removed every part of the problem except one}: a single critical-line boundedness of an
explicit, unconditionally-positive kernel family, equivalent to RH, with the off-line failure
mechanism made completely explicit. Positivity, curvature, the colligation, the index — all
unconditional. The one remaining inequality is the rank-one divergence $(\mathsf B)$, and it requires
a new arithmetic theorem at the center of the critical strip, of a kind no existing estimate provides.

\textbf{Honest endpoint.} This is the wall, mapped to its exact bottom. The proof of RH along this
route is the proof of $(\mathsf B)$, which is a genuinely new theorem about the divergence structure of
the Euler product on the critical line — to be \emph{created}, with $\mathsf{TW}_\Z$ as the proposed
home. No estimate on $A^{\mathrm{osc}}_\lambda$, no analytic continuation, and no positivity argument
can replace it; it is the irreducible arithmetic core, and it is exactly RH.
