# 111.00 — Phase 111 plan: does $I_\partial$ converge on Schwartz-class data?

## 0. The single question

Requirement d1 (Riemann–Roch via $h^0$, via linear equivalence, via a principal
subspace $\mathcal P\subseteq\operatorname{rad}I_\partial$) needs the corner
pairing

$$I_\partial(D_f,D_g)=\mathfrak T(f\star\widetilde g),\qquad
\mathfrak T(h)=\lim_{\Lambda\to\infty}\Big(\mathrm{Tr}(\theta(h)R_\Lambda)-2h(1)\log\Lambda\Big)$$

to make sense on a class of test data rich enough to contain nonzero
$\xi$-divisible functions ($\widehat f=\xi\widehat g$). Phase 110 proved this
class cannot be the compactly-supported class (ADM): $\xi$ has infinite
exponential type on $\mathbb R$, every nonzero compactly-supported transform
has finite type, and division forces the class to $\{0\}$. Phase 110 also
exhibited a candidate Schwartz-class (non-compact) witness, $g(r)=e^{-(\log
r)^2}$, $\widehat g(w)=\sqrt\pi\,e^{w^2/4}$.

Phase 111 asks whether $I_\partial$ itself — not just the algebra of
$\xi$-divisibility — survives the relaxation from compact support to
Schwartz class. This is the last gap in d1's chain.

## 1. Working conventions (fixed here, used throughout 111_01–111_03)

Write $x=\log r$, $\tilde f(x):=f(e^x)$. Mellin transform convention (matching
110\_02, which computed $\widehat g(w)=\int\tilde g(x)e^{-wx}dx$ and verified
$\widehat g(w)=\sqrt\pi e^{w^2/4}$ for $\tilde g(x)=e^{-x^2}$ under this
convention):
$$\widehat f(w):=\int_{-\infty}^\infty \tilde f(x)\,e^{-wx}\,dx.$$
$\xi(w):=\tfrac12 w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w)$, entire, $\xi(w)=\xi(1-w)$
(functional equation, cited, standard).

**Schwartz class** $\mathcal S(\mathbb R)$: smooth $\tilde f$ with
$\sup_x|x^k\tilde f^{(j)}(x)|<\infty$ for all $j,k\ge0$ — decay faster than
every polynomial. This is the *only* thing "Schwartz-class test data" is
entitled to mean without smuggling in an assumption; **it does not by itself
imply exponential decay** (Remark 111.0.1 below). Where extra exponential
decay is needed we name it explicitly as membership in
$$\mathcal S_\eta:=\Big\{\tilde f\in\mathcal S(\mathbb R):\ \forall N\ \exists
C_N,\ |\tilde f(x)|\le C_N(1+|x|)^{-N}e^{-\eta|x|}\ \ \forall x\Big\},\qquad
\eta>0,$$
and $\mathcal S_{>1}:=\bigcup_{\eta>1}\mathcal S_\eta$.

> **Remark 111.0.1 (the class "Schwartz" is not self-evidently the right
> one).** $\tilde f(x)=e^{-\sqrt{|x|}}$ is Schwartz (every derivative, times
> every power of $x$, is bounded — an elementary check) yet
> $\tilde f(x)e^{\sigma x}\to\infty$ as $x\to-\infty$ for **every** $\sigma>0$: it
> has no exponential decay rate at all, so $\widehat f(\sigma)$ diverges for
> every $\sigma\ne0$. Bare "Schwartz-class" therefore does **not**
> automatically deliver even the polar terms of Task 1. This is a real
> distinction the phase must track, not a technicality to wave past — see
> §3 below.

## 2. Pre-registration: what would refute the Schwartz route

Per the anti-circularity rule, these are written **before** the convergence
computations of 111\_01–111\_03, and each is a genuinely possible outcome
that the computations below could have produced instead of the one they did.

**Refutation R1 (polar terms admit no exponential-decay margin).** If it
turned out that *no* subclass of Schwartz functions with exponential decay
of any fixed rate $\eta$ could contain a $\xi$-divisible pair — i.e. if
achieving $\widehat f=\xi\widehat g$ forced $\tilde f$ or $\tilde g$ out of
every $\mathcal S_\eta$ the same way Theorem 110.2.4 forced it out of compact
support — the Schwartz route would die by the same mechanism that killed the
compact-support route. This is checked directly in 111\_03 by computing the
decay of the *inverse* transform of $\xi(w)\widehat g(w)$, not merely
asserting it.

**Refutation R2 (identity value forced to zero, incompatibly with $\xi$).**
If convergence of $\mathfrak T$ forced $h(1)=0$ for every admissible $h$ (the
literal analogue of phase 108's $\varphi_0=0$ constraint), and if this were
incompatible with $\widehat f=\xi\widehat g$ for nonzero $g$ — e.g. if it
forced $\widehat g(1)=0$ *and* that constraint could not be met without also
forcing $\widehat g\equiv0$ on the class where the rest of the machinery
converges — d1 would die by a second, independent mechanism. This is checked
in 111\_02: is $h(1)=0$ actually forced, and if so, is it satisfiable?

**Refutation R3 (the trace's own divergence is not what the counterterm
kills, off compact support).** The defining limit $\mathfrak T(h)$ is a
regularized trace with counterterm $2h(1)\log\Lambda$, fixed in *form*. If
the actual divergence of $\mathrm{Tr}(\theta(h)R_\Lambda)$ for
non-compactly-supported Schwartz $h$ contains pieces the fixed counterterm
cannot see (because they come from the tail of $h$ rather than its value at
the identity), the limit could fail to exist even when the Weil-formula
right-hand side is manifestly finite. This is the one piece of the
computation this phase **cannot** settle outright, because the operator
definitions of $\theta,R_\Lambda,\mathrm{Tr}$ are not among the two files
this phase is permitted to read; it is isolated as an explicit, named,
flagged assumption in 111\_01 §3, and its failure is registered here, in
advance, as the single largest way this phase's positive conclusion could be
wrong.

**If none of R1–R3 held even in principle** — i.e. if every possible
numerical/analytic outcome had been read as confirming convergence — the
test would be circular and worthless. They are not vacuous: R1 was modeled
on the exact mechanism (type mismatch) that closed the compact-support case
in Phase 110, so it had a live prior; R2 is modeled on the exact mechanism
that closed the local Tate integral in Phase 108, so it too had a live
prior; R3 is simply not something this phase's tools can rule out from
first principles, so it is quarantined rather than argued away.

## 3. What "convergence on Schwartz-class data" will be allowed to mean

Given Remark 111.0.1, an unqualified claim "$I_\partial$ converges on
Schwartz data" is not a claim that can be true for the *entire* space
$\mathcal S(\mathbb R)$ (the $e^{-\sqrt{|x|}}$ example already refutes that
reading trivially, and cheaply — so cheaply that asserting the full space
converges would itself be a red flag). The only non-vacuous question is
whether a genuine, non-compactly-supported subclass exists on which (a)
every piece converges and (b) the subclass contains nonzero $\xi$-divisible
elements. That is exactly Tasks 1–3, and the class produced,
$\mathcal S_{>1}$, is defined by a decay-rate threshold derived from where the
integrals in Task 1 actually start converging — not defined after the fact
to contain the answer. §4 of 111\_03 checks nonemptiness and
$\xi$-divisible membership explicitly, per the rule that a restricted class
must be shown nonempty and shown to intersect the target class, not assumed
to.

## 4. Deliverables

* `111_01_CONVERGENCE_OF_THE_THREE_PIECES.md` / `.py` — Task 1: polar terms,
  zero sum, defining trace.
* `111_02_THE_IDENTITY_CONSTRAINT.md` / `.py` — Task 2: is $h(1)=0$ forced?
* `111_03_COMPATIBILITY_AND_VERDICT.md` / `.py` — Task 3 (does the
  convergence class meet the $\xi$-divisible class) and Task 4 (verdict).
* `111_99_PHASE_111_SUMMARY.md` / verifier — aggregate.

## 5. Scope note

Nothing in this phase bears on RH. $\xi$'s growth asymptotic (Phase 110) is
unconditional; the zero-density estimate $N(T)\sim(T/2\pi)\log T$
(Riemann–von Mangoldt) is unconditional and quoted, not used to locate any
zero off the critical line or to assume one on it. No definition below uses
a zero of $\xi$, a Li coefficient, or a positive-definite Weil-type form;
zeros appear only inside theorems, as the source rule permits.
