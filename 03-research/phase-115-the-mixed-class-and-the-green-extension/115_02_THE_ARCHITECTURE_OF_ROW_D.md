# 115.02 — The architecture of row (d)

Rows (a), (b), (c) are built.  They are load-bearing floors: they supply
certain materials and they forbid certain moves.  This note derives what
row (d) is then *allowed* to be — not as a wish list, but as a set of design
decisions each forced by something already standing.

Nothing here is a proof of row (d).  It is the blueprint the proof has to fit.

---

## 0. The brief

\[
 B_{\rm nuc}(f,f)\le0\qquad(f\in\mathcal T^0),
 \qquad
 \mathcal T^0=\{\widehat f(0)=\widehat f(1)=0\}.
\]

By `thm:mixedsectionforcing` it suffices to produce \(h^0,h^1,h^2\) on the
mixed classes satisfying four numerical axioms.  By `main.tex` §1 nothing else
is admissible: *"Row (d) must come from a Riemann–Roch theorem on the square,
or not at all."*

---

## 1. What the lower floors supply

| from | material | reference |
|---|---|---|
| (a) | a stable symmetric monoidal category with duals, \(\operatorname{Perf}_{IDN}\) | `eq:PerfDN` |
| (a) | invertible divisor lines, tensor law, principal descent | `prop:divisorlines` |
| (a) | an effective cone \(\to\mathbb R_{\ge0}^2\) | `prop:externaleffectivity` |
| (a) | intrinsic cohomology with **quadratic growth** \(\dim\sim t^2ab\) | `cor:cotangentRRdimension` |
| (a) | a coefficient-one determinant \(\lambda_{\rm int}\), exponent \(B_{\rm int}\) | `prop:continuousRRdet` |
| (a) | derived prime contact \(C_p\), torsion determinant \(\log p\) | `prop:derivedPrimeContact` |
| (a) | **the Green rank cut** \(M(G)=\ell\ell^{\!\top}-\operatorname{diag}(\ell)\) | `eq:greenline`, `115_01` |
| (a) | ruling plane with \(H\!\cdot\!H=2\), signature \((1,1)\) | `eq:rulingquotient` |
| (b) | a faithful multiplicative family, \(\Gamma_m\circ\Gamma_n\simeq\Gamma_{mn}\) | `thm:rowbcompose` |
| (b) | contact weights \(\Lambda(n)\), self-dual \(\Lambda(n)/\sqrt n\) | `eq:centralLocalCoefficient` |
| (c) | the complete trace \(I_\Delta^{\rm nuc}\), hence \(B_{\rm nuc}\) | `thm:rowc` |
| (c) | the splitting \(B_{\rm nuc}=K+G_\infty\) | `thm:forcedgreen` |
| (c) | the archimedean multiplier \(m_\infty\), one zero at \(\tau^*\approx2\pi\) | `eq:archmultiplier` |

## 2. What the lower floors forbid

These are the walls that cannot be moved.

| forbidden | by |
|---|---|
| any factorization through a finite-dimensional space | `thm:infiniterankcontact` |
| one positive line per prime (the self-contact shape) | `thm:finitecontactobstruction` |
| making the archimedean term more negative | `thm:forcedgreen` — \(G_\infty\) is **pinned**, zero freedom |
| defining anything from zeros, the sign, or a positive part | `ss:constraint` |
| an equivalence derived from the explicit formula | `main.tex` §1 |
| separate positive budgets per local channel | D.262 §3 |
| defining the contraction by a pseudoinverse | `ROW_D_MASTER_GOAL` |
| building \(h^0\) inside \(\mathcal D\) | `113_11` Thm 3.3 (obstruction O1) |
| finite-rank, per-prime, or local constructions generally | D.263 §5 |

## 3. The one remaining freedom

Everything above is pinned except one thing.  Of the coefficient algebra
`main.tex` says explicitly:

> three module generators suffice after the infinitely many labels are moved
> into the scalar nuclear algebra.  **No universality or uniqueness of this
> extension of scalars is asserted.**

\(\mathcal C_{\mathbb R}\) was *chosen*, not forced.  So:

> **Design rule.**  If the construction needs more room, it gets it in the
> **coefficients**, never in the geometry (pinned by row (a)) and never in the
> forms (pinned by rows (b) and (c)).

## 4. The blueprint

Seven decisions, each with what forces it.

**D1 — row (d) is an object, not an estimate.**
Forced by `thm:mixedsectionforcing` (four axioms suffice) and `main.tex` §1
(nothing else admissible).  What is missing is a perfect complex whose
determinant is \(B_{\rm nuc}\), so that its signature becomes computable the
way \(B_{\rm int}\)'s is.

**D2 — it lives in \(\operatorname{Perf}_{IDN}\), not in \(\mathcal D\).**
Forced by `113_11`: obstruction O1 is a category error *inside* \(\mathcal D\),
where divisors and sections are the same type, so the divisor map is linear
instead of scaling-invariant.  Row (a) does not have that defect —
\(\mathcal L(D,E)\) and \(\mathbf H^{\rm int}\) are different objects.
`113_11` leaves this open explicitly (condition R10).

**D3 — the degree map is the pair of Tate evaluations.**
\(\deg(f)=(\widehat f(1),\widehat f(0))\), and the mixed class splits as
\(D_f=\widehat f(1)F_1+\widehat f(0)F_2+M_f\) — which is `eq:requiredprimitiveclass`
verbatim.  Forced by the chain: row (a)'s two degrees \(d_1,d_2\) \(\leftrightarrow\)
row (c)'s polar characters \(x^0,x^1\) \(\leftrightarrow\) the two rulings
\(\leftrightarrow\) the two Tate conditions.  On \(\mathcal T^0\), \(D_f=M_f\).

**D4 — the polarization is \(H=F_1+F_2\), \(H\!\cdot\!H=2\).**
Supplied by row (a); measured independently from primes in `113_09` Thm 4.1.

**D5 — the form carries three blocks with distinct jobs.**
This is the structural core, and it is forced by an inertia fact: a cross form
\(\begin{pmatrix}0&M\\M^{\!\top}&0\end{pmatrix}\) has inertia
\((\operatorname{rank}M,\operatorname{rank}M,\cdot)\) — always neutral.  So the
negatives row (d) needs cannot come from the contact.

```text
ruling block     cross, rank 2      -> the ONE positive: H
contact block    cross per prime    -> hyperbolic pairs, neutral (r,r)
Green cut        ell ell^T - diag   -> rank r -> 1, so only H stays positive
archimedean      diagonal multiplier -> the infinitely many negatives (tail of m_inf)
```

**D6 — \(h^0\) is a cohomology dimension, not a section set.**
Forced by `113_11` Thm 3.3: any \(h^0\) defined by section sets
\(\{g\in\operatorname{rad}:f+g\ge0\}\) is scale-invariant, so \(h^0(nD)=h^0(D)\)
and the growth argument has nothing to grow.  Row (a)'s
\(\mathbf H^{\rm int}_t\) does grow, quadratically.

**D7 — axiom 4 is inherited, not proved again.**
`cor:cotangentRRdimension` gives \(t^2ab=\frac12t^2q(D,D)\) on the ruled cone,
which is exactly `eq:mixedRRminimum`.  The task is to *extend* it to the mixed
classes, not to establish it.

---

## 5. The four load paths

| # | load | carried by | status |
|---|---|---|---|
| 1 | exactly one positive direction, and it is \(H\) | row (a)'s ruling plane after the rank cut | **PROVED** in row (a): \((1,1,2r-2)\), and \((0,1,\cdot)\) on \(H^\perp\) |
| 2 | infinitely many negative directions | the tail of \(m_\infty\), \(|\tau|>2\pi\) | **PROVED** (digamma asymptotics) |
| 3 | the contact's \(r\) positives are cut away | the Green term \(\ell\ell^{\!\top}-\operatorname{diag}(\ell)\) | **PROVED for primes**; **OPEN for prime powers** |
| 4 | \(h^0,h^1,h^2\) with the four axioms | intrinsic periodic cohomology | axiom 4 **PROVED** on the ruled cone; 1–3 **OPEN** |

### The residual budget, and a measured asymmetry

After load 3 does its work, the positives that remain are those of
\(G_\infty\) on the band \(|\tau|<2\pi\), where \(m_\infty>0\).  That band is
finite-dimensional on a window of length \(2T\).

Diagnostic measurement (`phase-114` session, floating point):
\(\operatorname{ind}_-(\Gamma)\) on \(\mathcal P_T\) reads
\(1,1,2,3,5,7,10\) for \(T=0.69,\,0.80,\,0.90,\,1.24,\,1.70,\,2.30,\,3.00\) —
growing roughly like \(3.3\,T\).  Over the same range \(r\) reads
\(2,2,3,5,10,25,78\), i.e. exponentially in \(T\).

> **The rank cut converts an exponentially growing positive index into a
> linearly growing one.**  That asymmetry is the reason the architecture is
> worth building: the hard part (all the primes) is handled structurally, and
> what is left is a budget growing like \(T\).

Marked diagnostic, not proved: these are floating-point counts, and per D.198
anything rigorous must be redone in interval arithmetic.

---

## 6. The single unproven joint

Load 3, extended from primes to prime powers.

Row (a)'s cut works because \(\ell\ell^{\!\top}\) is the outer square of the
**degree vector**.  On prime powers the analogue \(v_n=\Lambda(n)/\sqrt n\) is
**not summable**: \(\sum_{n\le N}\Lambda(n)/\sqrt n=2\sqrt N+\dots\).

The programme's own machinery already removes exactly that divergence — the
continuous synthesis is subtracted by the two Tate conditions, leaving D.260's
centred measure \(dA=d\Psi-dx\).  So three separate entries in the ledger are
one object:

```text
row (a)'s degree vector ell          the rank-one cut
the two Tate conditions / rulings    what makes its extension finite
D.260's dPsi - dx                    the extended vector itself
```

**Working hypothesis.**  \(d\Psi-dx\) is the centred degree vector of the mixed
classes, and row (d)'s Green term is its outer square minus the local contact.

**Falsifier.**  The resulting term must reproduce \(G_\infty\) — which row (c)
pins *exactly*, with no freedom (`thm:forcedgreen`), as the multiplier
\(m_\infty(\tau)=\log\pi-\operatorname{Re}\psi(\frac14+i\frac\tau2)\).  One side
is forced by row (c), the other constructed from row (a), and they were built
independently.  If they disagree, the hypothesis is dead.

---

## 7. Acceptance tests for anything built against this blueprint

1. **Non-circularity.**  No zero of \(\xi\), no Li coefficient, no sign, no
   positive part (`ss:constraint`).
2. **Arithmetic discrimination.**  Must fail on the off-line Beurling
   surrogate.  A mechanism that also works there cannot close row (d).
3. **Shape.**  The contact must enter in the **cross** form.  The self form is
   `thm:finitecontactobstruction`.
4. **No pseudoinverse.**  Neither \(\Theta_E\) nor \(\mathscr Z_{N,\varepsilon}\)
   may be defined through the inverse whose positivity is the conclusion.
5. **Subspace hygiene.**  \(\mathcal T^0\) is codimension **two**; \(H^\perp\) is
   codimension **one**.  Row (a) gives \(=0\) on the first and \((0,1,\cdot)\) on
   the second.  Confusing them is the error logged in `115_01`.
6. **Method rule (D.263).**  State which theorem of `main.tex` §`sec:rowdgate`
   forbids the naive version of the candidate, and what feature escapes it.

---

## 8. Classification

* §1, §2 inventories: **RECORDED** from the paper.
* §3 (coefficients are the only free parameter): **RECORDED** — `main.tex`
  asserts non-uniqueness explicitly.
* D1–D7: **DERIVED** from the cited results; these are design consequences,
  not theorems about row (d).
* Loads 1, 2: **PROVED**.  Load 3 for primes: **PROVED**.  Load 3 for prime
  powers, load 4 axioms 1–3: **OPEN**.
* The linear-vs-exponential asymmetry: **MEASURED, DIAGNOSTIC**.
* The centred-degree hypothesis: **HYPOTHESIS**, with a sharp falsifier.
* Row D: **OPEN**.
