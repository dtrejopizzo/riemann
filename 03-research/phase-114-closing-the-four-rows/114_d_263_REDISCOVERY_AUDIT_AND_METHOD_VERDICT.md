# D.263 — Rediscovery audit: the campaign re-proved two obstructions already in the paper

## Verdict

The local-construction campaign D.191--D.262 terminated on two obstructions.
Both were already proved in `04-papers/42-arithmetic-lefschetz-programme`,
at the level of the form \(B_{\rm nuc}\) itself, before the campaign began.

This is not a defect of the individual notes, each of which is correct.  It
is a defect of the **unit of work**: the campaign's unit was a candidate
*local* construction, so each refutation had to be re-derived once per
candidate, in the candidate's own coordinates.  The paper's unit was the
form, so one theorem covered the whole family at once.

The two rediscoveries are recorded below with exact correspondences, so that
the same ground is not covered a third time.

## 0. Chronology

`main.tex` and its four row files were last modified **2026-08-06 15:02**.
The notes discussed below were written **2026-08-08, 07:56--08:40**.  The
paper is untracked in git, so no commit history is available; the filesystem
timestamps are the evidence, and they are unambiguous for this claim.  No
file in `04-papers/42-*` was modified by this campaign.

## 1. Rediscovery A — infinite rank is not removed by two Tate equations

### Paper (before the campaign)

`thm:infiniterankcontact`: the convolution map \(T_W:a\mapsto W*a\) has
infinite algebraic rank, hence \(B_{\rm nuc}\) cannot factor through any
finite-dimensional space.  The proof is arithmetic: a finite-dimensional
translation-invariant space of distributions is annihilated by some \(P(D)\)
and therefore consists of exponential polynomials, which are smooth; this
contradicts the prime atoms at \(t=\pm k\log p\) supplied by
`eq:rowcidentity`.

`cor:primitiveinfiniterank`: the restriction to \(\mathcal T^0\), of
codimension at most two, still has infinite rank.

`ROW_D_MASTER_GOAL.md`, *Rejected closure claims*, item 4, states the same
prohibition in one line: *"two Tate jets controlling an infinite boundary
block"*.

### Campaign

| Note | Statement | Object |
|---|---|---|
| D.195--D.196 | boundary state space is two full \(L^2\) modules, inertia \((\infty,\infty)\) | per-prime two-chart colligation |
| D.197 | explicit two-cell counterexample to the local isometric boundary relation | periodic boundary graph |
| D.258 (2.1) | \(\operatorname{rank}\mathcal C_{S,T}=\infty\) | coherent dual-central port |
| D.259 (2.1) | Tate primitivity does not annihilate the coherent port | same |

### Relation

D.258's proof is *softer* than the paper's and proves *less*: it uses only
that \(\mathcal P_T\) has codimension two in \(L^2(I_T)\) and that
\(M_{\eta_S}\), \(\mathcal F\), \(J_T\) are injective.  No arithmetic input
appears — as D.258 itself notes, "replacing \(\eta_S\) by any nonzero
multiplier which is nonvanishing almost everywhere gives the same
conclusion".  The paper's theorem uses the prime atoms and applies to
\(B_{\rm nuc}\) directly.

Shared structural content, in both directions:

> a codimension-two condition cannot make an infinite-rank object
> finite rank.

The campaign instantiated this once per candidate port.  The paper had
proved it once for the form.

## 2. Rediscovery B — the archimedean multiplier is indefinite

This correspondence is verbatim, not merely structural.

### Paper (before the campaign)

`eq:archmultiplier` defines
\[
 m_\infty(\tau)=\log\pi-\operatorname{Re}\psi(\tfrac14+i\tfrac\tau2),
\]
and the text following `eq:archenergy` proves

* \(m_\infty(0)=\log\pi-\psi(1/4)>0\);
* \(\psi(z)=\log z+O(z^{-1})\) gives \(m_\infty(\tau)\to-\infty\);
* "Thus \(G_\infty\) is indefinite";
* "Hence the local energy does not close row~(d); a non-circular proof must
  derive the exact domination from a new mixed Riemann--Roch/effectivity
  theory."

The constant itself already appears a third time, as \(m_0=\log\pi+\gamma+
\frac\pi2+3\log2\) in `row-d-local-analysis.tex`
`eq:localizedprimitiveoperator`.

### Campaign

D.262 §3 proves (3.1) \(m_\infty(0)=\log\pi-\psi(1/4)=\log\pi+\gamma+
\frac\pi2+3\log2>0\); (3.2) the digamma asymptotic; (3.3)
\(m_\infty(\tau)=\log(2\pi/|\tau|)+O(\tau^{-2})\to-\infty\); and concludes
that the local Blaschke colligations of D.249 cannot be assigned independent
positive Douglas budgets.

### Relation

Same function, same two values, same conclusion, two days later.  The
marginal new content of D.262 §3 is the verification that orthogonal support
compression and the rank-two Tate short do not repair the sign for the
specific D.249 network.  That increment is genuine but small, and it was
predictable from `cor:primitiveinfiniterank` (a rank-two correction cannot
change an infinite-rank verdict) — i.e. from Rediscovery A.

## 3. Why it happened

The campaign and the paper differ in method, not in rigour.

**Paper (rows a, b, c).**  Prove a no-go about the naive object; then build,
once, the forced replacement in an infinite but tame category, and import an
external theorem to carry the analysis:

| Row | No-go proved first | Forced replacement | Imported engine |
|---|---|---|---|
| (a) | `thm:rawsmashnogo` (exponential growth), `thm:finiteNSnogo` (finite rank cannot carry \(\Lambda(mn)\)) | intrinsic periodic cohomology; nuclear Dirichlet algebra | Connes--Consani |
| (b) | — (contact must come from \(F_n\), not an appended module) | derived Witt contact \(K_n^W\) | Haran |
| (c) | naive \(\sum\Lambda(n)n^{-s}\) diverges off \(\Re s>1\) | operator identity \(Z\partial(Z^{-1})\) in a nuclear multiplier algebra | Meyer |

No row proceeds by enumerating finite local candidates.

**Campaign (row d).**  Enumerate local finite candidates; refute each.  Since
`thm:infiniterankcontact` forbids *every* finite-rank factorization of
\(B_{\rm nuc}\), and \(\mathcal T^0\) is only codimension two, each candidate
was condemned before it was built.  Roughly seventy notes recovered that
verdict candidate by candidate.

**Counterfactual.**  From D.214 (defect-difference identity) and D.260
(identification of the coherent channel with the Mellin--Stieltjes transform
of \(d\Psi-dx\)), the joint regularized residual D.262(4.2)--(4.4) is
reachable directly.  D.241--D.259 lie off that path.

## 4. What survives, and is load-bearing

Recorded so the closure is not read as an erasure.

* **D.200** — correction of a real gap in the D.172/D.181 three-block
  Feshbach template (dropped safe-block/tail coupling), with a scalar
  counterexample proving the omission is not cosmetic.  A bug fix, not a
  reformulation.
* **D.210, D.211, D.214** — exact operator Green identity, reference-spectral
  reduction, defect-difference identity.  These carry the current
  formulation.
* **D.260** — the unpaid channel *is* the Mellin--Stieltjes transform of
  \(dA\), \(A(x)=\Psi(x)-x+1\).  This is an identification of the object with
  something that has a name outside this programme.  It is the handoff.
* **D.261, D.262(4.2)--(4.4)** — the exact joint Green energy and the
  regularized residual identity with its monotone \(\varepsilon\downarrow0\)
  limit.
* **D.244** — exact inertia \((1,|S|-1)\) for the finite prime tangent form.
  Unconditional, self-contained, and *not* usable for row D (D.258--D.259).
  Worth extracting separately.

Retained as a catalogue of refuted mechanisms, explicitly marked as
instances of `thm:infiniterankcontact` or of the indefiniteness of
\(G_\infty\), not as independent walls: D.191--D.197, D.234, D.241, D.243,
D.250, D.252, D.255, D.258--D.259.

## 5. Method rule adopted going forward

> Before constructing any candidate for row D, state which theorem of
> `main.tex` §`sec:rowdgate` forbids the naive version of that candidate, and
> what feature of the candidate escapes it.  A candidate that cannot answer
> this is not built.

Corollary, from `thm:infiniterankcontact`: **no finite-rank, per-prime, or
separately-budgeted local construction will be attempted again.**

## 6. Classification

* Rediscovery A (infinite rank vs. two Tate equations): **CONFIRMED,
  STRUCTURAL**.
* Rediscovery B (indefinite archimedean multiplier): **CONFIRMED, VERBATIM**.
* Paper modified by the campaign: **NO** (§0).
* Load-bearing survivors: **D.200, D.210, D.211, D.214, D.260, D.261,
  D.262(4.2)--(4.4)**; independent side result **D.244**.
* The open theorem, unchanged: construct \(\mathscr Z_{N,\varepsilon}\) with
  \(\mathscr R_{N,\varepsilon}=\mathscr Z_{N,\varepsilon}^*
  \mathscr Z_{N,\varepsilon}\), without pseudoinverses and without assuming
  RH.
* Row D: **OPEN**.
