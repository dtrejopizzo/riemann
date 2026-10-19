# Doc 131 -- Phase 44: Hodge-Witt and visible inertia

**Program:** Riemann Hypothesis -- creative break after Phase 43.  
**Status:** starting document. Does not prove RH. Defines a new framework, proves internal lemmas, and fixes bridges/wishes with explicit status.

---

## 0. Contract for the new stage

Mathematical freedom lives in the definition. Discipline lives in the theorem.

We will use four mandatory labels:

- **[NEW-DEFINITION]** total freedom: an object, a category, an algebra, a geometry is defined.
- **[THEOREM]** proved within the declared framework.
- **[BRIDGE]** connection with zeta/RH, with its real status.
- **[WISH]** unproved goal. A wish is not a shame; it is the declared engine.

Golden rule of Phase 44: no result will be called "toward RH" if it only repackages Weil positivity, uniform continuity, Hadamard, Connes-Consani, Deninger, de Branges, Lee-Yang, Li, Jensen, Nyman-Beurling, or a known equivalence. If the bridge is conditional, it is stated as conditional.

---

## 1. Operational diagnosis: which hypothesis must be broken

Phases 0--43 left a very precise map. The wall is not lack of data; it is the lack of an object that reads **inertia** without putting it in as input.

Design table:

| No-go / wall | Hypothesis feeding it | Proposed break |
|---|---|---|
| MW-1, Weil positivity is equivalent to RH | the final object is a scalar positivity | change the codomain to a Witt/inertia class; positivity will be a consequence, not a definition |
| MW-2, propagation from Re(s)>1 | one tries to push arithmetic information from a boundary into the strip | build a two-boundary object, where primes and the archimedean place are simultaneous boundaries |
| MW-3, infinite Hasse-Minkowski | local positivity implies global positivity | do not require local positivity; require a boundary law in the Witt group |
| MW-4, wrong sign | unconditional tools give lower bounds | look for a mechanism of **exclusion of negative inertia**, not a lower bound on the value |
| MW-7 / Hadamard | verifiable properties do not see zero positions | require test NC4: under `not RH`, the object exists and fails visibly |
| Phase 43 / Deninger | the polarization uses the analogue of Hasse | require a pre-RH polarization: defined before knowing where the zeros are |

**Decision of Phase 44.** We abandon as primary object the inequality `Q >= 0`. The new primary object is a **defect class in a Witt group**, because inertia is what every program needed and none could read without circularity.

---

## 2. The new algebra: Hodge-Witt objects with visible failure

### 2.1. Finite Hodge-Witt object

**[NEW-DEFINITION]** A **finite Hodge-Witt object** is a quintuple

`X = (V, q, L, F, B)`

where:

1. `V` is a real vector space of finite dimension.
2. `q: V x V -> R` is a non-degenerate symmetric bilinear form.
3. `L: V -> V` is an abstract Lefschetz operator.
4. `F` is a finite increasing filtration, called the arithmetic filtration.
5. `B` is a boundary datum: a formal decomposition `B = B_infty - sum_p B_p`, not necessarily locally positive.

The **inertia defect** of `X` is

`Def(X) = [q|P(X)] in W(R)`,

where `P(X)` is the primitive subspace defined by `L` and `W(R)` is the real Witt group. We identify `W(R) ~= Z` via the signature.

### 2.2. Visible polarization

**[NEW-DEFINITION]** A family `X_theta` of Hodge-Witt objects, parametrized by deformations `theta` of the zeros, has **visible polarization** if:

1. `X_theta` exists for on-line and off-line deformations.
2. The definition of `(V,q,L,F,B)` does not use as input the conclusion "all the zeros are on the line".
3. If an off-line packet `rho = 1/2 + b + i gamma` appears, with `b != 0`, then there exists a primitive vector `v_rho in P(X_theta)` such that `q(v_rho,v_rho) < 0`.
4. The failure is not "the space stops existing"; the failure is a visible negative vector.

This is the NC4 test turned into a design axiom.

### 2.3. Boundary bridge

**[NEW-DEFINITION]** A Hodge-Witt family has an **explicit boundary law** if there exists a formal identity

`partial Def(X) = B_infty - sum_p B_p`

in an abelian group of boundaries `A`, compatible with finite truncations and stable under adding hyperbolic summands.

The important word is **formal**: local positivity of `B_p` is not required. Phase 6 already showed that this fails.

---

## 3. Internal theorems: small, hard, and useful

### Theorem 1 -- Blindness of scalar values

**[THEOREM]** No invariant that factors only through the trace of a real symmetric form can decide the negative index.

**Proof.** In `R^2`, the forms

`q_0 = diag(1,1)` and `q_1 = diag(3,-1)`

have the same trace, `tr(q_0)=tr(q_1)=2`. But `neg.ind(q_0)=0` and `neg.ind(q_1)=1`. Therefore any invariant that sees only the trace takes the same value on both and cannot decide the negative index. QED.

**Reading.** This is the algebraic skeleton of P43: the value/trace is autonomous; the inertia is not.

### Theorem 2 -- The Witt class does read inertia

**[THEOREM]** Let `q` be a non-degenerate symmetric form over a real space of fixed dimension `n`. Its Witt class, together with `n`, determines its negative index.

**Proof.** By Sylvester's law of inertia, `q` is congruent to `diag(1,...,1,-1,...,-1)` with `p` positive signs and `m` negative signs. The real Witt class is the signature `sig(q)=p-m`. Since `n=p+m`, we obtain

`m = (n - sig(q))/2`.

Hence `neg.ind(q)=m` is determined by `([q],n)`. QED.

**Reading.** Inertia is not read in trace-type scalar values, but it is read in the correct codomain: `W(R)`.

### Theorem 3 -- Necessity of visible failure

**[THEOREM]** In this framework, a polarization that fails to be defined for every off-line deformation cannot be a non-circular proof of RH.

**Proof.** By definition, a visible polarization requires existence both on-line and off-line and fails via a visible negative vector. If the structure only exists in the on-line world, then its existence already contains the conclusion one wanted to prove: it does not separate "RH implies structure" from "structure implies RH". Therefore it fails the visible-polarization criterion. QED.

**Reading.** This formalizes the lesson of Phase 43: it is not enough to say "if the space is Kähler-Riemann then there is positivity"; one must build the space before knowing RH.

### Theorem 4 -- Hodge-Witt bridge conditional on RH

**[THEOREM / CONDITIONAL BRIDGE]** Suppose there exists a visible Hodge-Witt family `X_zeta` associated with the zeta function, with these properties:

1. `X_zeta` is defined without assuming RH.
2. Hodge-Witt positivity holds for every primitive vector: `q(v,v) >= 0` for `v in P(X_zeta)`.
3. Every off-line packet produces a visible negative primitive vector, as in 2.2(3).

Then RH is true.

**Proof.** If `not RH`, there exists an off-line packet. By visibility, there is a primitive vector `v_rho` with `q(v_rho,v_rho)<0`. This contradicts the primitive positivity of (2). Hence there are no off-line packets. QED.

**Status.** The theorem is correct, but the bridge is conditional. What is not proved is the existence of `X_zeta` with a zero-independent definition and external primitive positivity. This is exactly the hard point.

---

## 4. The new conjecture, formulated without a false victory

### Conjecture 131.A -- Pre-RH Hodge-Witt polarization

**[WISH]** There exists a Hodge-Witt family `X_zeta` associated with `Spec Z` such that:

1. It is built from the bare space: flow, primes, archimedean boundary, arithmetic filtration.
2. It does not use the localization of the zeros to define `q`, `L`, the transverse metric, or the measure.
3. Its defect `Def(X_zeta)` is defined in `W(R)` before imposing RH.
4. Under `not RH`, the object does not collapse: a visible negative class appears.
5. The explicit boundary law recovers Weil's explicit formula as a scalar shadow.

**[BRIDGE]** If, in addition, primitive Hodge-Witt positivity is proved for an external geometric reason, then Theorem 4 gives RH.

**[Frank WISH]** The difficulty is not writing the conjecture. The difficulty is building a polarization that does not copy the pattern of Deninger-elliptic, where the metric uses Hasse as input.

---

## 5. Three lines of work, ordered by risk

### Route I -- Toy model of an off-line packet

**Goal.** Build `X(b,gamma)` for a single off-line quadruple and verify that the negative vector appears in `W(R)` at the correct scale.

**Expected output.**

- [THEOREM] Local formula: `Def(X(b,gamma)) = -2` or an equivalent class per conjugate packet.
- [BRIDGE] Compare with Phase 26/96: localization of the negative index in `K_off`.
- [FALSIFIER] If the defect depends on data absorbable as in Doc 98, the route dies early.

### Route II -- Bare Morishita + non-metric polarization

**Goal.** Take the bare space of Morishita (flow + orbits + profinite transversal) and look for a polarization in `W(R)` that does not require classical leafwise Kähler structure.

The idea is not to require complex leaves. Require a **Witt polarization over the boundary complex**:

`C^0(F) -> C^1(F) -> C^2(F)`

with a symmetric form in reduced cohomology. This breaks the "the leaves must be Kähler" hypothesis of the Deninger no-go.

**[NEW-DEFINITION]** A **profinite-Witt polarization** is a symmetric form in the cohomology of a complex of filtered profinite spaces that:

1. is stable under refinement of the filtration;
2. has an explicit boundary law;
3. admits a visible-failure test under off-line packets.

**[WISH]** Prove a Hodge-type index theorem for this polarization, not from Kähler-ness but from exactness/profiniteness/filtration.

### Route III -- Category of boundaries and arithmetic exact triangle

**Goal.** Build a triangulated category `D_Ari` with a formal triangle

`Finite primes -> Archimedean boundary -> Zero cohomology ->`

and a functorial symmetric form on the cohomology term.

**[BRIDGE]** The explicit formula would be the trace of the boundary of this triangle. RH would not be a positivity of the trace; it would be the vanishing of the negative part of the Witt class of the middle term.

**[WISH]** Find the axiom that forces `Def(X_zeta)=0` without turning it into RH by definition.

---

## 6. Mandatory falsifiers

A healthy Phase 44 must be able to die. These are the falsifiers:

1. **Falsifier F1 -- absorption.** If the leading off-line defect is absorbable into the closure of the admissible class, as happened with `g*` in Doc 98, route I does not work.
2. **Falsifier F2 -- Hasse metric.** If the profinite-Witt polarization can only be defined by imposing the analogue of `|xi|^2=q`, we fall back into Phase 43: circularity via inertia.
3. **Falsifier F3 -- trace only.** If the new object only produces numbers `T_lambda` or equivalent scalar values, it falls by Theorem 1.
4. **Falsifier F4 -- local positivity.** If it requires `B_p >= 0` per prime, it falls by Phase 6.
5. **Falsifier F5 -- uniform limit.** If the last step is `sup_X |lambda_min(Q_X)-lambda_min(Q_infty)| -> 0`, without additional structure, it falls by MW-6.

---

## 7. First concrete problems

### Problem 131.1 -- Witt computation of the quadruple

Explicitly build the minimal symmetric form for an off-line packet

`rho, 1-rho, conjugates`

and compute its class in `W(R)`. Compare with the sign of the second variation already documented in Phase 28 and with the Pontryagin index of Phase 26.

### Problem 131.2 -- NC4 for candidate polarizations

Every new polarization must pass the test:

- exists under `not RH`;
- does not use zero-localization as input;
- produces a visible negative vector if `b != 0`;
- is not limited to saying "the metric does not exist".

### Problem 131.3 -- Profinite boundary

Define a complex of boundaries over the profinite transversal of Morishita that has nontrivial cohomology and a natural symmetric form. The goal is to replace "Kähler leaves" with "profinite boundaries with Witt duality".

### Problem 131.4 -- Scalar shadow

Prove that the trace/scalar shadow of `Def(X_zeta)` recovers the known explicit formula. If it does not recover the explicit formula, the object does not touch zeta. If it only recovers the explicit formula and nothing of inertia, it is useless.

---

## 8. Starting verdict

**[THEOREM]** Theorems 1--4 are valid within the defined framework.

**[BRIDGE]** The bridge to RH is conditional on a new construction: a pre-RH Hodge-Witt polarization with visible failure. This does not yet exist.

**[WISH]** Build that polarization. If it exists, it changes the game because it reads inertia before positivity. If it does not exist, Phase 44 will still have proved something: that even the Witt codomain falls under the master quantifier.

**Guiding sentence.** We are not looking for another positive form. We are looking for the object prior to positivity, the one that keeps existing when RH fails and shows us where it bleeds.
