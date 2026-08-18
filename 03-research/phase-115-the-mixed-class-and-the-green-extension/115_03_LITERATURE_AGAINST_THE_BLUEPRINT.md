# 115.03 — The literature, read against the blueprint

Search run 2026-08-08 against the four load paths of `115_02`, not as a general
survey.  Local sources in `00-references/` were read where available; the rest
from arXiv abstracts and introductions.

## Headline

**No one in the current literature is building the geometric route.**  Every
active programme found is analytic or spectral:

| work | date | approach |
|---|---|---|
| Connes–Consani–Moscovici, *Zeta Spectral Triples* (2511.22755) | Nov 2025 | spectral realization; rank-one perturbations of the scaling operator on \([\lambda^{-1},\lambda]\).  No intersection form, signature, Riemann–Roch, effective cone or section functor. |
| Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time* (2602.04022) | Feb 2026 | survey + new material; the proposed strategy is *"convergence of zeros from finite to infinite Euler products"* — spectral |
| Connes–Consani, *On the Absolute Geometry of \(\operatorname{Spec}\mathbf Z\)* (2606.06604) | Jun 2026 | \(\mathbb F_1\)-structures via perfectoids, untilts, Fargues–Fontaine.  Not the square. |
| Connes–Consani, *On the Jacobian of \(\overline{\operatorname{Spec}\mathbb Z}\)* (2602.15941) | Feb 2026 | Picard group / Jacobian of the arithmetic **curve**; dimension one |
| Suzuki, *Weil's quadratic form via the screw function* (2606.09096) | Jun 2026 | screw functions, de Branges spaces, Hilbert–Pólya |

So the architecture of `115_02` is not duplicated.  That is a real fact — but
read it correctly: it may be that nobody is doing it because everyone judges it
harder, not because nobody thought of it.  `main.tex` itself records that
Connes–Consani declare Riemann–Roch on the square open.

## Calibration first: what was already known in 1992

Suzuki's introduction records, and it matters for how row (d)'s results are
described:

> **Yoshida (1992)** established that RH is equivalent to positive
> definiteness of \(Q_W\) on \(C_c^\infty(-a,a)\) for every \(a>0\), and proved
> that it *is* positive for sufficiently small \(a>0\) (Yoshida, Lemma 2).

So the localized equivalence and the existence of an initial positive interval
are 34 years old.  `thm:certifiedendpoints` (\(0<T\le\log2\), full Hilbert
space, interval-certified) is a **quantitative refinement** of Yoshida, not a
new kind of statement.  Worth saying plainly in the paper.

---

## Load 2 — the negatives: the screw function is the function-level version

Suzuki's \(g\) (his (1.3), expanded near the origin in his (2.2)) is

\[
 g(t)=\tfrac12|t|\log|t|+A|t|
 +\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}\bigl(|t|-\log n\bigr)+r(t),
 \qquad A=\tfrac12(\log2\pi-\psi(2))=0.707546\ldots
\]

with \(r\) even, \(C^2\), \(r(t)=O(t^2)\).  That is our contact-plus-archimedean
split again — but as a **continuous function**, not a distribution.

And the defining property (Krein–Langer): \(g\) is a screw function iff

\[
 g(t-u)-g(t)-g(-u)+g(0)\ \ge 0 ,
\]

**iff RH holds.**  Two observations for the blueprint:

* that is a **two-point kernel positivity** — structurally the Green-kernel
  condition of D.261, in a different language;
* the second difference **annihilates affine parts of \(g\)**.  Our two degree
  conditions annihilate the degree.  These are the same operation: the
  \(|t|\)-linear terms in \(g\) (both \(A|t|\) and the \(|t|-\log n\) pieces)
  are precisely the degree-like part.

## Loads 1–3 — three things Suzuki has that this programme does not

1. **Theorem 1.1.**  \(A_a\) is the **Friedrichs extension of \(B_a=D^*G_aD\)**,
   where \(G_a=P_aGP_a\) is the integral operator with the continuous kernel
   \(g(x-y)\) and \(D=i\,d/dx\) with Dirichlet conditions.  So the localized
   Weil operator has a closed form with a *continuous* kernel.  Section 8
   reduces \(Q_W^a(v)=\langle A_av,v\rangle\) to \(\langle G_au,u\rangle\) —
   "treatable within the theory of integral operators with continuous kernels".
   Compare our own `115_04` result from the previous session, which reached a
   quadrature-free closed form for the same operator by a different route.

2. **Theorem 1.3 — \(\lambda_a\) is continuous in \(a\), proved
   unconditionally.**  The propagation programme of `ROW_D_EXECUTION_PLAN`
   Phase 8 needs exactly "birth continuity" and does not have it.  Suzuki
   proves it, and notes that Bombieri's corresponding continuity claim
   ([1, Theorem 5]) "calls for a more careful analysis".

3. **Theorem 1.4 — the small-\(a\) asymptotic**, unconditional:
   \[
    \lambda_a=\log\tfrac1a+\mu_1-\log(2\pi)+\psi(2)-1+O(a),
   \]
   with \(\lambda_a\) simple and the eigenfunction even.  Consistent with the
   diagnostic measurements of the previous session
   (\(\lambda_{\min}\) decreasing in \(T\); \(1.09\cdot10^{-7}\) at
   \(T=\log2\)), though those are at \(a\) far from the asymptotic regime.

   Caveat on comparison: Suzuki works on \(L^2_0(-a,a)=\{\widehat u(0)=0\}\),
   **one** condition, whereas \(\mathcal P_T\) imposes **two**.  The two are
   related through his \(D=i\,d/dx\) (a derivative of compactly supported data
   automatically integrates to zero), but the identification has not been
   checked here and should not be assumed.

## Load 4 — the section functor: the best candidate found

> **Wei He, *Numerical cohomology for arithmetic surfaces and applications*,
> arXiv:2512.01811 (Dec 2025).**  Local source in
> `00-references/papers-nuevos/D/`.

He constructs **numerical cohomology \(h^0,h^1,h^2\) for arithmetic surfaces**
and derives an **absolute arithmetic Riemann–Roch formula**.  That is the shape
`thm:mixedsectionforcing` asks for.  Structure:

* \(h^0_{\mathcal O}(\mathcal F)=\log\sum_{x\in H^0}e^{-\pi\|x\|^2}\) — the
  **theta invariant** (Gauss mass), traced to Artin–Hasse–Tate and Quillen;
* Riemann–Roch for arithmetic curves is stated as **equivalent to Poisson
  summation**;
* \(h^0_{\mathcal X}(\mathcal L):=h^0_{\mathcal O}(f_*\mathcal L)\),
  \(h^2_{\mathcal X}(\mathcal L):=h^0_{\mathcal X}(\omega_{\mathcal X}\otimes
  \mathcal L^\vee)\) — **Serre duality by construction**;
* \(h^1\) via the Leray spectral sequence and relative Serre duality.

Why this is the right candidate rather than another Arakelov result:

* **axiom 3** of `thm:mixedsectionforcing` (\(h^2(D)=h^0(-D)\)) is built in;
* **axiom 4** is the Riemann–Roch formula itself;
* **the engine is Poisson summation** — the same engine as row (c), where
  Meyer's construction *is* Poisson summation (`eq:Hcap`,
  \(Zf=\mathscr JZ\mathcal Ff\)).  These are not merely compatible; they run on
  the same mechanism.
* the quantities are **numerical**, defined by a theta series rather than by a
  section space.  `thm:mixedsectionforcing` only needs numbers.  A numerical
  invariant is far more transportable than an candid cohomology.

**The gap, stated candidly.**  Wei He works on classical Arakelov arithmetic
surfaces \(f:\mathcal X\to\operatorname{Spec}\mathcal O\) with Hermitian line
bundles.  \(\mathscr Y_{\mathbb S}\) is not one of those, and `main.tex`'s own
Hodge-route audit says exactly why: the spherical ringed square is not a
regular proper arithmetic variety in the sense those theorems assume.  So this
is the same category gap as Faltings–Hriljac–Moriwaki and Yuan–Zhang.

What is different is the *kind* of object being transported.  Those are
signature theorems whose hypotheses cannot be constructed here.  This is a
recipe for numerical invariants from a theta series — and row (a) supplies a
metric, a determinant and an effective cone, which is what a theta series
needs.

## Consequences for the blueprint

* **Load 4 gets a concrete first target**: can \(h^0_{\mathcal O}\)'s theta
  series be written from row (a)'s data — the based normed determinant lines
  \(\lambda_{\rm int}\) and the effective cone of
  `prop:externaleffectivity` — rather than from a section space?  If yes,
  axioms 1 and 3 come along for free and only axiom 2 is left.
* **Load 2/3 get a translation**: the screw condition is the Green-kernel
  positivity in continuous-function form, and its second difference is our
  degree-killing.  Anything we prove about \(\mathcal G_N\) should be checked
  against \(g\), where it becomes a statement about a concrete continuous
  function.
* **The programme should import Suzuki's Theorem 1.3** rather than re-derive
  birth continuity.

## Classification

* No current geometric/RR programme in the literature: **ESTABLISHED** by the
  search above, with the caveat that absence of evidence is not proof.
* Yoshida 1992 already has the localized equivalence and small-\(a\)
  positivity: **RECORDED** (via Suzuki's introduction; the primary source was
  not read here).
* Suzuki Thms 1.1, 1.3, 1.4 as stated: **RECORDED** from the paper.
* Screw condition \(\leftrightarrow\) Green-kernel positivity, second
  difference \(\leftrightarrow\) degree-killing: **OBSERVATION**, no map
  constructed.
* Wei He's numerical cohomology as a Load-4 candidate: **CANDIDATE**; the
  category transport is **UNRESOLVED** and is the same gap as the classical
  Hodge-index theorems.
* Row D: **OPEN**.

## Sources

Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096 ·
Suzuki, *On the Hilbert space derived from the Weil distribution*,
arXiv:2301.00421 · Connes–Consani–Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755 · Connes, *The Riemann Hypothesis: Past, Present and a Letter
Through Time*, arXiv:2602.04022 · Connes–Consani, *On the Absolute Geometry of
Spec Z*, arXiv:2606.06604 · Connes–Consani, *On the Jacobian of
Spec Z-bar*, arXiv:2602.15941 · Wei He, *Numerical cohomology for arithmetic
surfaces and applications*, arXiv:2512.01811 · Yoshida (1992), via Suzuki [17].
