# D.216 — Referee-proposal triage and the next admissible porting target

## Verdict

Five independent reports on paper 42 were compared with the exact operator
reductions D.190--D.214.  None supplies a proof of row D.  Two proposed
``closures'' are circular, two are research programmes rather than
constructions, and three suggestions survive as useful structural filters.

The smallest current theorem is still

\[
 q_N^*D_N^\dagger q_N\leq \mathcal M_N,
 \qquad
 \mathcal M_N=I-y_N^*y_N-h_N^*D_Nh_N
       +2\mathrm{Re}(h_N^*q_N),               \tag{0.1}
\]

including the supported-range condition
\(q_NE_N\subset\mathrm{Dom}\,D_N^{\dagger/2}\).  Here \(q_N\) is
the complete Tate-centred Poisson--prime--Gamma column of D.175, not its
Witt majorant or its two moments.  Equation (0.1) is equivalent to the
sharp birth capacity, by D.214.

The next admissible proof must factor the *difference*

\[
 \mathcal R_N:=\mathcal M_N-q_N^*D_N^\dagger q_N     \tag{0.2}
\]

by source-defined operators, or establish (0.1) by an equally sharp
identity.  It may not define effectivity, a contraction, or a section
space by requiring (0.1) itself.

## 1. Epistemic classification of the reports

| Proposal | Classification | Audit |
|---|---|---|
| Define mixed sections as vectors with a dissipated return load | **CIRCULAR / DISCARDED** | The defining condition requires finiteness of \(D_N^{\dagger/2}q_N\), which is the missing range assertion.  The claimed RR asymptotic is then asserted, not derived. |
| Define \(h^1\) from the capacity residual | **CIRCULAR / DISCARDED** | Nonnegativity of that residual is row D.  It cannot be used to prove its own nonnegativity. |
| Adjoin a mixed nuclear module by a homotopy pushout | **FORMAL CONSTRUCTION ONLY** | A pushout may exist, but it does not imply that its determinant equals \(B_{\rm nuc}\), that its cone is effective, or that mixed RR/duality holds. |
| Mixed periodic Riemann--Roch or theta effectivity | **OPEN GEOMETRIC PROGRAMME** | This could close D only if constructed independently.  It is not the active analytic route and cannot use threshold positivity in its proof. |
| Two-projection/Julia--Halmos identity | **AUDITED; NO CLOSURE** | D.190--D.194 and D.214 show that the available defect factorization is equivalent to the original sharp gate. |
| Local Poisson/Hankel contraction from the two Tate jets | **IMPOSSIBLE LOCALLY** | D.195--D.197 prove the boundary block is infinite-dimensional and retains infinite positive and negative inertia. |
| Exact critical identity or sum of squares | **ADMISSIBLE TARGET** | It could produce constant one without a lossy estimate, provided it is derived before the sign. |
| Poisson/Gamma input distinguishing the rational adelic system | **ADMISSIBLE REQUIREMENT** | The complete centred column must be used.  PNT-strength estimates of isolated Witt words are insufficient by D.189 and the counterfactual harness. |
| Sonin/prolate/semilocal dilation | **CANDIDATE, NOT A RESULT** | It becomes relevant only after an explicit intertwiner is exhibited whose defect is exactly (0.2). |
| Finish selected endpoints by Arb | **INTERVAL-CERTIFICATE PROGRAMME** | This can close a finite remainder and validate the propagation machinery, but cannot replace a uniform large-birth theorem. |

## 2. Claims in the reports which are not imported

### 2.1 Alleged uniform saturation

One report sketches that the sharp capacity must approach one.  The sketch
uses spectral packets near critical zeros and an unproved quantitative
passage from window Rayleigh quotients to the normalized birth capacities.
It is therefore **HEURISTIC / OPEN**, not a theorem available to D.

We retain only the safe methodological rule: do not demand a uniform
strict gap unless it is independently proved.  The exact target remains
the non-strict constant one.

### 2.2 Alleged Beurling transplantation barrier

The reports cite generalized-prime systems with strong PNT properties and
off-line zeros.  Turning this into a theorem about the precise D.190
operator would require constructing the corresponding Gamma, functional
equation, Tate compression, and localized capacity, and then proving the
transplantation.  That has not been done here.

Accordingly:

* the existing counterfactual harness is a **FALSIFIER OF RELEVANCE**;
* a candidate lemma which survives it cannot close D by itself;
* failure on the surrogate is useful evidence that the centred arithmetic
  channel was retained;
* neither outcome is a proof of the candidate lemma for \(\mathbb Q\).

## 3. Exact porting target

For each genuine prime-power birth \(q_j=p^k\), after the D.211
reference-high block has been shorted by the D.210 Green identity, define
the finite reference-low defect \(D_j\), the complete centred column
\(q_j\), and the born budget \(\mathcal M_j\) with the normalizations of
D.170/D.175/D.214.

The large-birth theorem to prove is:

> **Source-defined sharp return theorem.**  There is \(j_0\) such that for
> every \(j\ge j_0\), \(q_jE_j\) lies in the form domain of
> \(D_j^{\dagger/2}\) and
> \[
>   \mathcal M_j-q_j^*D_j^\dagger q_j\ge0.
> \]
> The factorization is constructed from the exact Poisson support maps,
> the complete Gamma kernel, all prime-power contacts and the Tate
> compression, without a spectral sign assumption.

An acceptable stronger form is an identity

\[
 \mathcal R_j=Z_j^*Z_j+R_j,
 \qquad R_j\ge0,                                    \tag{3.1}
\]

with all domains and limits proved.  An acceptable weaker form is the
small-defect layer estimate of D.212/D.213 with constants that fit the
*actual* operator budget \(\mathcal M_j\), not an unnamed
\(O(\log q_j)\) allowance.

## 4. Parallel finite work

The endpoint certificates remain logically separate:

1. reconstruct frozen frames from high-precision directed centres;
2. impose the two Tate equations in Arb;
3. recompute Gamma and delicate contacts natively;
4. certify the finite Schur complement;
5. retain the D.210 operator Green for the intermediate-to-infinite
   complement;
6. publish every generator, precision, outward rounding rule and hash.

Each completed endpoint is classified **CERTIFIED BY INTERVALS**.  Only a
uniform theorem plus a finite certified remainder can close row D.

## 5. Equality

If (0.2) is factored as in (3.1), equality is

\[
 Z_je=0,\qquad R_j^{1/2}e=0.                         \tag{5.1}
\]

This kernel must be tracked during the construction.  It may not be
declared to consist of Tate modes merely because two Tate equations were
imposed: D.190 proves the uncompressed boundary channel has infinite rank.

## 6. Current status

* Reduction to (0.1): **PROVED EQUIVALENCE**.
* Range equivalences and harmonic cancellation: **PROVED** (D.214).
* High-reference tail coercivity: **PROVED** (D.211).
* Exact operator Green identity: **PROVED** (D.210).
* Strong defect-layer/return criterion: **PROVED SUFFICIENT REDUCTION**
  (D.212--D.213).
* Uniform source-defined estimate (0.1): **OPEN**.
* Finite endpoint completion: **IN PROGRESS, INTERVAL ROUTE**.
* Global propagation, equality, row D: **OPEN**.

