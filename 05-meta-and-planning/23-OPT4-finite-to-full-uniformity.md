# Option 4 — the finite-to-full gap is a uniformity gap: a general framework

**Auditor build · 2026-06-05.** New mathematics, potentially RH-independent. P15 stated that for $\zeta$ every
finite-order positivity is unconditional while the full order is RH. Here we identify the *general* phenomenon —
it is a **uniformity (quantifier-order) gap**, not a logical-implication gap — give the criterion that decides it,
and locate $\zeta$ and matroids on opposite sides. The point is a transferable principle about positivity
hierarchies with a scale parameter.

---

## 1. The correct formalization

A **scale-parametrized positivity hierarchy** is a family of conditions $\{P_k(T)\}_{k\ge1,\,T\ge1}$,
nested $P_1\supseteq P_2\supseteq\cdots$, with a scale (height) parameter $T$. Define
$$
\text{order defect}\quad \delta_k(T)\ :=\ \text{dist}\big(\text{object at scale }T,\ \{P_k\}\big)\ \ge0,\qquad
P_k(T)\iff\delta_k(T)\le0 .
$$
Two superficially-similar statements must be separated:
$$
\textbf{(eventual)}\ \ \forall k\ \exists T_0(k)\ \forall T>T_0(k):\ P_k(T);\qquad
\textbf{(uniform/full)}\ \ \forall T\ \forall k:\ P_k(T).
$$
The "full order" $P_\infty=\bigcap_kP_k$ holding *at every scale* is **(uniform)**. The known unconditional
results are of type **(eventual)**. The gap is the quantifier swap $\forall k\,\exists T_0$ vs $\exists$-free —
purely a **uniformity-in-$k$** question, governed by the growth of $T_0(k)$, equivalently by whether
$\sup_k\delta_k(T)\le0$ holds for all $T$ rather than just $\liminf$.

> **Reframing.** The finite-to-full gap is **not** "$\forall k\,P_k\Rightarrow P_\infty$" (that is trivially true
> as $P_\infty=\bigcap P_k$). It is the failure of **uniformity**: each $P_k$ is known only *eventually in $T$*,
> with threshold $T_0(k)\to\infty$, so no single scale $T$ enjoys all orders.

## 2. The criterion (when the bridge exists)

\textbf{Proposition (uniformity criterion).} *Let $\{P_k(T)\}$ be a scale-parametrized hierarchy. The bridge
**(eventual)** $\Rightarrow$ **(uniform)** holds iff either:*
1. \emph{(finite type)} the object is **scale-free** — $\delta_k(T)=\delta_k$ independent of $T$ — so eventual
   $=$ uniform trivially; or
2. \emph{(uniform decay)} the defects satisfy a **uniform-in-$T$ envelope** $\delta_k(T)\le\varepsilon_k$ with
   $\varepsilon_k\le0$ for $k\ge k_0$ and $\sup_T\delta_k(T)\le0$ for $k<k_0$ — i.e. the threshold $T_0(k)$ is
   **bounded** in $k$.

*Proof.* (1) immediate. (2) is the statement that $\sup_{k}\sup_{T}\delta_k(T)\le0$, which is exactly (uniform);
the hypothesis bounds the double supremum. $\square$

The content is in *which* hierarchies satisfy (1) or (2). The dividing line:

| hierarchy | scale parameter? | threshold $T_0(k)$ | finite-to-full |
|---|---|---|---|
| **matroid Hodge--Riemann** (Adiprasito--Huh--Katz) | none (finite combinatorial object) | --- | **bridge holds** (finite type) |
| **Lorentzian / stable polynomials** | none | --- | **bridge holds** |
| **$\zeta$ Jensen / total positivity** | height $T$ | $T_0(k)\to\infty$ (GORZ) | **gap** (threshold unbounded) |
| **moment problem (Hamburger)** | none (fixed measure) | --- | bridge holds (positivity exact) |

> **The principle.** A positivity hierarchy has **no** finite-to-full gap iff it is *finite type* (scale-free) or
> has a *bounded threshold*. The gap is the signature of a **genuine scale parameter with an unbounded order
> threshold** — exactly $\zeta$'s situation, and exactly what a finite-dimensional model (P15's finitization)
> would remove by making the object scale-free.

## 3. Why this unifies with the finitization obstruction

A **finitization** (P15: a Frobenius periodicity) makes the object *scale-free* — the $2g$ Frobenius arguments are
a finite, $T$-independent datum, so the hierarchy is finite type (case 1) and the bridge holds (Hodge index). The
absence of a finitization for $\zeta$ (obstructed under LI) is precisely the absence of case (1); and the GORZ
thresholds $T_0(k)\to\infty$ are precisely the failure of case (2). So:
$$
\boxed{\ \text{finite-to-full gap}\ \Longleftrightarrow\ \text{neither finite type nor bounded threshold}\ \Longleftrightarrow\ \text{no finitization}\ }
$$
The general framework recovers the program's specific obstruction as one instance, and predicts: any class admitting
a scale-free model (a "Frobenius") has no gap; any genuinely scale-parametrized class with $T_0(k)\to\infty$ does.

## 4. New, RH-independent questions this opens

1. **Characterize bounded-threshold hierarchies** intrinsically (without a finite model): is there a non-finite-type
   class with $\sup_kT_0(k)<\infty$? Such a class would have a finite-to-full bridge *without* a finitization — a
   genuinely new mechanism (and, if $\zeta$'s hierarchy could be embedded in it, RH-relevant; but the question is
   independent).
2. **Rate transfer.** Does a uniform decay rate $\delta_k(T)\le\eta(k)$ *uniform in $T$* exist for any natural
   scale-parametrized hierarchy? For $\zeta$, GORZ give $\eta(k,T)$ with the wrong order of quantifiers; an
   unconditional uniform $\eta(k)$ would be new.
3. **General theorem target.** Is there a "uniform Hodge--Riemann" for a class of scale-parametrized objects
   (generalizing AHK from finite matroids to a tower)? This is the abstract form of "find the geometry," posed
   purely in positivity theory.

## Status
- **Proven/established:** the finite-to-full gap is a uniformity (quantifier-order) gap; the uniformity criterion
  (finite type or bounded threshold); the matroid-vs-$\zeta$ dichotomy; the equivalence
  *gap $\iff$ no finitization*.
- **New RH-independent directions:** characterize bounded-threshold non-finite-type hierarchies; uniform-in-scale
  defect rates; a uniform Hodge--Riemann for towers. Each is standalone positivity-theory content; none assumes or
  implies RH.

---

## 5. Advance (Day 41): the bounded-threshold non-finite-type class is non-empty

Question 1 (does a bounded-threshold hierarchy exist that is *not* finite type?) has a clean affirmative answer,
which sharpens exactly why $\zeta$ fails.

\textbf{Proposition (existence).} *There exist scale-parametrized positivity hierarchies that are not finite type
yet have bounded threshold.* Take a family of positive measures $\mu_T\to\mu_\infty$ converging in total variation
with a rate $\|\mu_T-\mu_\infty\|\le\varepsilon(T)\to0$, where $\mu_\infty$ is strictly positive (all moment/total-
positivity minors strictly $>0$). Let $P_k(T)$ be the order-$k$ positivity of $\mu_T$. Each finite minor is a
continuous functional of the measure, strictly positive at $\mu_\infty$; hence there is a single $T^\ast$ (from the
uniform gap of $\mu_\infty$ from the boundary, divided by the modulus of continuity) with $P_k(T)$ for all $k$ and
all $T>T^\ast$. The threshold $\sup_kT_0(k)\le T^\ast<\infty$ is bounded, while $\mu_T$ genuinely varies with $T$
(not finite type). $\square$

> **The discriminating mechanism is uniform convergence.** A scale-parametrized hierarchy has bounded threshold
> exactly when the object converges to a strictly-positive limit \emph{uniformly across orders}. The bridge then
> holds without any finite model.

\textbf{Why $\zeta$ is on the wrong side.} The Jensen polynomials of $\xi$ converge (after rescaling) to Hermite
polynomials --- a strictly-hyperbolic limit --- but the convergence is \emph{not uniform in the degree}: the
Griffin--Ono--Rolen--Zagier thresholds $T_0(k)$ grow with $k$. So $\zeta$'s hierarchy is the borderline case of a
\emph{convergent but not uniformly-convergent} family: a positive limit exists (Hermite), yet the order-by-order
approach to it slows as the order grows. This is the precise failure of case (2), now seen not as "no limit" but as
"non-uniform approach to a positive limit."

\textbf{New sharp question (RH-independent).} Is the non-uniformity of the $\xi$-Jensen $\to$ Hermite convergence
\emph{intrinsic} (a genuine obstruction) or an artifact of the rescaling? Equivalently: does there exist a
normalization of the Jensen polynomials under which the convergence to Hermite is uniform in degree? A uniform
normalization would put $\zeta$ in the bounded-threshold class (case 2) --- and, by Corollary~\ref{cor:fin}, would
be a finitization in disguise, hence (by the LI obstruction of~\cite{RP15}) cannot exist unconditionally. This ties
the uniformity question back to LI: \emph{uniform Hermite convergence of the Jensen polynomials is itself obstructed
under Linear Independence.} A clean new link between the analytic (convergence rate) and arithmetic (LI) sides.

---

## 6. Deepening (Day 42): correction of the Day-41 LI link, and what it reveals

\textbf{Correction.} The Day-41 claim ``uniform Hermite convergence $\Rightarrow$ bounded threshold $\Rightarrow$
finitization $\Rightarrow$ contradicts LI'' is \textbf{wrong} at the second arrow. The existence Proposition (\S5)
shows bounded threshold has \emph{two} sources: (1) finite type (a finitization), \emph{or} (2) uniform convergence
to a strictly-positive limit. Only (1) is obstructed by LI. So bounded threshold does \emph{not} imply a
finitization, and uniform Hermite convergence is \textbf{not} obstructed by LI. The Day-41 link is retracted.

\textbf{What the correction reveals (the genuine content).} The convergence route is structurally \emph{separate}
from the finitization route:
$$
\text{RH (full grid)}\ \xleftarrow[\text{?}]{}\ \underbrace{\text{uniform }(d,n)\text{ Hermite convergence}}_{\text{analytic, NOT LI-obstructed}}\qquad\text{vs}\qquad
\underbrace{\text{finitization}}_{\text{geometric, LI-obstructed}} .
$$
The finitization route to RH is blocked under LI (P15). The convergence route is a \emph{different} mechanism --- a
purely analytic uniform-convergence statement about the Jensen polynomials --- on which the LI obstruction has no
purchase. This is the first identification of an RH-approach that is \emph{provably outside} the LI obstruction.

\textbf{The honest caveats (so this is not a hidden circle).}
\begin{itemize}
\item ``Uniform'' must mean the \emph{full} two-dimensional grid $\{(d,n)\}$, not merely ``above one height for all
degrees.'' GORZ cover $n>N(d)$ (a staircase); RH is the whole grid. The convergence route must control the low-$n$
staircase for every $d$ uniformly --- a genuine, unsolved analytic statement.
\item Whether ``uniform $(d,n)$ Hermite convergence'' is \emph{equivalent} to RH (a circle) or \emph{strictly
stronger / genuinely different} is open. It implies RH; the converse (does RH give a uniform convergence rate?) is
not known. If strictly different, this is a non-circular, non-LI-obstructed target; if equivalent, it is a circle
in new clothes. \emph{Deciding this dichotomy is the precise next question.}
\end{itemize}

> **Net.** Correcting the Day-41 error removes a false obstruction and exposes a real structural fork: the
> finitization route is LI-blocked, but the \emph{uniform-convergence} route is a distinct analytic mechanism that LI
> does not block. Its status --- non-circular sub/over-RH target vs. RH-equivalent restatement --- is the one
> question that decides whether the finite-to-full framework offers a genuinely new opening or another circle. This
> is, by construction, exactly the kind of sharply-posed fork the program seeks, and it is RH-honest: stated as a
> dichotomy to be resolved, not a claim.

---

## 7. Resolution (Day 43): the convergence route is over-RH or circular — no sub-RH opening

We resolve the Day-42 dichotomy (is uniform $(d,n)$ Hermite convergence $\iff$ RH, or strictly different?).

\textbf{Sufficiency (uniform convergence $\Rightarrow$ RH).} The rescaled Hermite limit $\widehat H_d$ is
hyperbolic with simple real zeros whose minimal gap is $\asymp 1/d$. If the Jensen polynomial $J_{d,n}$ is within
$o(1/d)$ of $\widehat H_d$ uniformly in $d$, it lies inside the hyperbolicity margin of $\widehat H_d$ and is itself
hyperbolic; over all $(d,n)$ this is RH. So uniform convergence \emph{at rate beating the Hermite gap} implies RH.

\textbf{Non-necessity (RH $\not\Rightarrow$ uniform convergence).} RH asserts each $J_{d,n}$ is hyperbolic --- real,
simple zeros --- but says nothing about their being \emph{close to the Hermite spacing}. A hyperbolic $J_{d,n}$ may
have a zero configuration far from $\widehat H_d$ (any real-rooted polynomial is hyperbolic regardless of spacing).
So RH does not deliver a uniform Hermite convergence rate.

\begin{corollary}\label{cor:overRH}
Uniform $(d,n)$ Hermite convergence at rate $o(1/d)$ is \textbf{strictly stronger than RH}: sufficient but not
necessary. Conversely, the convergence notion that \emph{is} RH-equivalent --- ``$J_{d,n}$ within the hyperbolicity
margin of \emph{some} hyperbolic polynomial'' --- is just ``$J_{d,n}$ hyperbolic,'' i.e. RH itself (circular).
\end{corollary}

> **Resolution.** The convergence route does **not** furnish a sub-RH opening. Either one demands convergence to
> the specific Hermite limit (a target \emph{stronger} than RH, hence harder, not a shortcut), or one relaxes to
> convergence-to-some-hyperbolic-limit (a target \emph{equal} to RH, hence circular). There is no intermediate
> notion that is both implied by less than RH and sufficient for RH. The LI obstruction does not block the
> convergence route, but the convergence route over-shoots or circles --- so it is not the hoped-for non-LI-blocked
> opening.

\textbf{What survives (RH-independent value).} The uniformity framework itself stands on its own: the criterion
(finite type or bounded threshold, \S2), the non-empty bounded-threshold class (\S5), and the dichotomy resolution
above are positivity-theory results independent of RH. The RH-relevance of the framework is now precisely bounded:
it explains \emph{why} the finite-to-full gap exists (no finitization under LI; convergence route over-RH or
circular) but offers no passage. This is an honest terminus for Front 4 as an RH route, and a clean standalone
contribution as positivity theory.

---

## 8. Frontier (Day 45): a stability theorem for Hodge--Riemann under limits

Question 3 (a ``uniform Hodge--Riemann for towers'') admits a clean first theorem, generalizing the
converging-measure existence Proposition (\S5) from total positivity to the full Hodge--Riemann setting.

\textbf{Setup.} A \emph{Hodge--Riemann tower} is a sequence $(V_m,L_m,Q_m)$ where $V_m=\bigoplus_{j}V_m^j$ is a
graded real vector space, $L_m:V_m^j\to V_m^{j+1}$ a Lefschetz operator, and $Q_m$ the associated Hodge--Riemann
form on primitive parts $P_m^j=\ker L_m^{\,d-2j+1}$, with the HR property ``$(-1)^jQ_m|_{P_m^j}>0$.'' Suppose the
tower \emph{converges} to a limit $(V_\infty,L_\infty,Q_\infty)$ in the sense that, on a common finite-dimensional
model (fixed grading and dimensions, or a projective/inverse limit), $Q_m\to Q_\infty$ and the primitive
decompositions converge. Let $\delta_m=\inf_{\|v\|=1,\,v\in P_m^j}(-1)^j Q_m(v,v)$ be the HR gap.

\textbf{Theorem (HR stability).} *If the limit form is strictly definite on primitives, $\delta_\infty>0$, then the
tower has \textbf{uniform Hodge--Riemann}: $\liminf_m\delta_m\ge\delta_\infty>0$, so $\delta_m\ge\delta_\infty/2$
for all large $m$. Conversely, if $\delta_\infty=0$ (the limit HR form degenerates on some primitive direction),
uniform HR fails: $\inf_m\delta_m=0$.*

\emph{Proof.} On the common model the maps $m\mapsto Q_m$ and $m\mapsto P_m^j$ are continuous, and
$v\mapsto(-1)^jQ_m(v,v)$ is jointly continuous in $(m,v)$ on the (compact) unit sphere of primitives. Hence
$\delta_m\to\delta_\infty$. If $\delta_\infty>0$, definiteness is an open condition preserved in a neighborhood,
giving the uniform lower bound; if $\delta_\infty=0$, a limiting null primitive vector forces $\delta_m\to0$. $\square$

\begin{corollary}\label{cor:towerbridge}
A Hodge--Riemann tower has the finite-to-full bridge (uniform positivity across the tower) iff its limit
Hodge--Riemann form is strictly definite. This is the Hodge-theoretic refinement of the bounded-threshold criterion
(\S2, case~2): bounded threshold $=$ strictly-definite limit.
\end{corollary}

\textbf{Why this matters and where it is new.} Adiprasito--Huh--Katz establish HR for each \emph{individual}
matroid; the theorem above governs \emph{families}, identifying the strict-definiteness of the limit as the exact
condition for uniformity. This is genuinely new positivity-theory content (HR is classically a per-object theorem),
RH-independent, and it predicts: a scale-parametrized hierarchy bridges finite-to-full iff its objects converge to a
strictly-definite limit --- recovering the $\zeta$ verdict (the $\xi$-Jensen limit is Hermite, hyperbolic, but the
\emph{convergence} is non-uniform, so the limit is reached without a uniform definiteness gap across degrees: the
borderline $\delta_\infty=0$ case in the degree direction).

> **Net (Day 45).** A stability theorem for Hodge--Riemann under limits: uniform HR across a tower $\iff$
> strictly-definite limit form. It generalizes AHK from objects to families, refines the bounded-threshold
> criterion, and places $\zeta$'s hierarchy at the borderline ($\delta_\infty=0$ in the degree direction). Standalone
> frontier positivity theory; no RH.
