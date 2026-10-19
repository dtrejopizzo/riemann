# Doc 163 — Destructor of secondary homotopic inertia

**Phase 52. Adversarial mandate: KILL.**

## Claim under attack

> *m* (number of zeros of ζ off the critical line; RH ⟺ m=0; 2m = negative
> index of the Weil form Q) is a **secondary homotopic invariant**
> —arithmetic e-invariant, Toda bracket ⟨f,g,h⟩, or k-invariant— definable
> **without** the form Q, **RH-free**, and delivering 2m as output.

**Motivation of the construction (to be defeated):** the PRIMARY invariant (the
Witt class in L⁰) is blind to m because K_off is Witt-trivial (D132). What is blind to the
primary is a candidate to live on a secondary floor. And secondaries in the style of
Adams's e-invariant (Adams, *On the groups J(X) IV*, Topology 1966) are
"metric-free" —read from the stable homotopy structure, not from a
quadratic form.

**Thesis of the destructor:** the three routes to death are, at bottom, **a single
obstruction seen three times**, and that obstruction is already proved in the program
(D156, D161). I proceed route by route and then give the verdict.

---

## Preliminary: honest anatomy of a secondary invariant

To avoid attacking a ghost, I fix what a secondary IS, in any of its three
incarnations. The three share an identical architecture:

- **Toda bracket ⟨f,g,h⟩** (Toda, *Composition methods in homotopy groups of
  spheres*, 1962): defined when g∘f ≃ 0 and h∘g ≃ 0. The value is
  H̄∘(g∘f-nullhtpy) − (h∘g-nullhtpy)∘F̄, living in a quotient
  [ΣA,D]/(indeterminacy). **Requires TWO nullhomotopies** (the two null primary
  relations) and the secondary is the "difference between the two fillings."
- **Adams e-invariant** (Adams J(X) IV; APS II §4, Atiyah–Patodi–Singer,
  *Spectral asymmetry and Riemannian geometry II/III*, 1975–76): for
  f: S^{2n-1}→S^q stable with vanishing d-invariant (primary Chern), e(f)∈ℚ/ℤ is
  defined by choosing a manifold/cobordism W with ∂W realizing f and reading
  ⟨ch∪Todd, [W,∂W]⟩ mod ℤ. **Requires a FILLING W (a null cobordism of the
  primary) and a genus (ch·Td) integrated over it.**
- **Postnikov k-invariant**: the obstruction in H^{n+1}(X;π_n) to deforming the
  section over the (n-1)-skeleton; it lives over the kernel of the lower-order
  invariant.

**Common structural fact (key to the attack):** a secondary invariant is
*an integral of a filling of the primary*. Its well-definedness requires (a) that the
primary vanish (we are over its kernel) and (b) choosing a filling/nullhomotopy;
the indeterminacy is killed by the image of the lower-order primary. **Where
a "metric-free secondary" is claimed, one may ask: what is the filling and
with what is it integrated?** There Q will either be, or nothing will.

---

## Route 1 — The secondary reintroduces the form Q

**Question:** is the nullhomotopy/filling defining the arithmetic e-invariant
exactly the Weil form (or the ζ partition)?

### Death argument (CLOSED)

I identify the primary and the secondary with the program's objects, with no
ambiguity:

- **Primary = Witt class of K_off in L⁰(ℝ) (or W(ℝ)=ℤ via signature).**
  D132 proved: K_off is **Witt-trivial**. This means the off-line form is
  *metabolic/hyperbolic* in the Witt sense: it possesses a **Lagrangian**
  (isotropic subspace of half dimension). In L-theory (Ranicki, *Algebraic
  L-theory and topological manifolds*, 1992, Ch. 1–3) the class is zero PRECISELY
  because that Lagrangian L with L=L^⊥ exists.

- **The filling of the secondary IS the choice of that Lagrangian.** Here lies the
  trap. The well-definedness of any secondary over the kernel of the Witt primary
  requires fixing the witness of the primary nullity. The witness of "Witt-trivial"
  is NOT a free datum: it is the Lagrangian L, and a Lagrangian of a nondegenerate
  symmetric form **is a datum that only exists relative to the form**. One cannot
  name L "without Q": L=L^⊥ is an equation IN Q. (Ranicki, ibid., §1.6: the Witt
  class is the cobordism of forms; the cobordism is exhibited by a *formation*
  (L, Q|L), which contains Q.)

  Formally: the analogous Toda bracket is ⟨ι, Q_off, π⟩ where the null
  intermediate relation "Q_off ≃ 0 in Witt" is realized by the nullhomotopy =
  contraction along the Lagrangian. **That nullhomotopy transports Q.**

- **Identification with D161 (NEW, and this is the decisive blow).** In the KK/dual
  weight language of D161: the "orientation that turns the phase class into inertia
  signature" is modular (the dual weight), not topological. Translation into
  secondary language: the filling of the e-invariant = the **noncommutative-Poincaré
  orientation** = the dual weight = the datum D161 proved has ζ as its partition
  function. The secondary does not dodge this; it inherits it, because the
  nullhomotopy of the primary IS the orientation D161 already identified with ζ(β).

**Conclusion Route 1: KILLS.** The filling (Lagrangian / orientation) defining the
secondary is the form Q disguised as "witness of Witt-triviality."
Q re-enters through the back door —EXACTLY the pattern of Phase 51 Doc 161
(the canonical metric was ζ in disguise via the dual weight) and of Phase 43 (the
polarization metric carries the Frobenius eigenvalues). The "metric-free secondary"
is the metric disguised as nullhomotopy.

[Minor residual GAP] I do not rule out a secondary whose filling is NOT the Witt
Lagrangian but a nullhomotopy of *another* primary (e.g. the d-invariant / Chern
of a stable map, not the Witt class). That is captured by Routes 2 and 3.

---

## Route 2 — Witt-triviality propagates to the secondary

**Question:** if K_off is trivial at the primary level, is there a reason for the
secondary to also kill it? Does the secondary capture m, or does it lose it for the
same reason as the primary?

### Death argument (CLOSED, with an important nuance)

Here one must be fair: the e-invariant exists **precisely
to detect what the primary does not see**. The d-invariant (integer Chern) does not see
torsion; the e-invariant in ℚ/ℤ does. So "primary trivial ⟹ secondary
trivial" is FALSE in general (that is Adams's whole point). I cannot kill by
automatic propagation. I have to look at the ARITHMETIC of m.

**The decisive datum: 2m = κ is EVEN and an INTEGER.** (D132: κ=2m even; D156: κ=2m =
spectral flow = Maslov = APS-eta, **the same integer**.) Now I confront this with
where each invariant lives:

- **An Adams e-invariant lives in ℚ/ℤ.** It detects torsion / the *fractional*
  part of a genus. It captures what is invisible to the integer because the
  integer has already been "modded away." But **m is already an integer**, and in fact 2m is the
  spectral flow —which is the integer PRIMARY invariant of inertia (π₁(Fred^sa)=ℤ,
  Atiyah–Patodi–Singer III §7; Phillips, *Self-adjoint Fredholm operators and
  spectral flow*, 1996). The spectral flow IS κ=2m (D156). **So the "natural
  primary of inertia" already captures m completely, with no residue in ℚ/ℤ.**

- **Inverted question (and answered):** *"if the spectral flow
  already IS the primary and captures κ, what secondary floor remains?"* — **None with
  content.** The ℚ/ℤ part of the e-invariant is exactly the part the integer
  spectral flow does **NOT** see. But m=½κ is already entirely in the integer
  spectral flow. Therefore the projection of κ to the secondary receiver ℚ/ℤ is
  **2m mod ℤ = 0** (m integer). **The secondary in ℚ/ℤ annihilates m by
  construction of the receiver.** Not because of Witt-triviality of the primary, but because the
  natural receiver of the secondary is a group where integers are zero.

- **And a secondary with a NON-ℚ/ℤ receiver?** (e.g. a Toda bracket with value
  in a finite stable homotopy group π^s_k, or a k-invariant in
  H^{n+1}(·;ℤ).) Here Witt-triviality DOES propagate, directly via D132:
  K_off Witt-trivial = Lagrangian exists = the formation is *split*. A
  split formation has **a Toda bracket with total indeterminacy** (the
  middle nullhomotopy is canonical via the Lagrangian, so ⟨f,Q_off,h⟩
  contains zero / is indeterminate). In Ranicki's language: the cobordism
  of the split formation is also trivial at the level of cobordism of
  cobordisms (L-theory is 4-periodic and the relative groups of a null class
  with canonical filling vanish). **Witt-trivial + canonical filling ⟹ secondary
  indeterminate/trivial.**

**Conclusion Route 2: KILLS, by receiver dichotomy.**
- If the receiver is ℚ/ℤ (Adams style): m integer ⟹ projection = 0. The secondary
  loses m by *arithmetic of the receiver*, not by the metric. **NEW node**
  (different from D156/D161: here ζ does not even enter; it dies earlier, by parity).
- If the receiver is integer-valued (spectral-flow style / k-invariant in ℤ): then the
  secondary **is** the inertia primary (κ already integer), there is no floor below,
  and D132's Witt-triviality turns the formation split ⟹ total indeterminacy.

The argument is caught between two receivers: the "honestly secondary"
one (ℚ/ℤ) cannot carry an integer, and the one "that carries the integer" is not secondary but
the primary spectral flow that D156 already showed requires Fredholmness = m<∞ = RH
through the back door.

---

## Route 3 — The carrier spectrum re-inherits {log k} ⟹ ζ partition

**Question:** is the stable homotopy spectrum / the stable map from which the
e-invariant is taken built, at bottom, from the prime operator (spectrum {log k})?
Is there a carrier WITHOUT the flow of the primes, or is it inevitable?

### Death argument (CLOSED under a named hypothesis; otherwise [GAP])

The Phase 49/51 no-go says: any object whose spectrum is {log k} has
partition function ζ (D161 §161.5: Z(β)=Σk^{-β}=ζ(β), identical to Bost–Connes).
The arithmetic e-invariant, in order to *compute 2m from the primes*, needs a
carrier whose arithmetic information is the primes. There are exactly two
possibilities:

**(3a) The carrier IS the flow of the primes.** The arithmetic e-invariant would be
computed via a Chern character / Todd genus of an object (stable map,
or D of the spectral triple) whose spectral zeta is ζ. This is forced if one wants the secondary to "come from the
primes" to be RH-free while still *speaking of the zeros of ζ*. But then:

- The Todd genus / ch·Td defining the e-invariant (APS II §4) is integrated
  against the **spectral density of the carrier**, and that density is exactly the
  one producing ζ(β) (D161). The "Euler bridge {log k}→{γ_ρ}" reappears: going from the
  partition ζ(β) to the γ_ρ is analytic continuation to the zeros. **ζ re-enters
  as the carrier's partition function** —SAME node as D161 (orientation/
  normalization), not new.

**(3b) The carrier is NOT the flow of the primes** (spectrum ≠ {log k}, partition
≠ ζ). Then the carrier knows nothing about the γ_ρ nor about m. The e-invariant would be
RH-free but **empty with respect to m**: it computes a homotopy number of an object
with no proven relation to the zeros. To connect it to m one would need an
identification "this e-invariant = 2m," and that identification is exactly the
[central GAP] inherited from D156 §4.5 / D161 §boundary: *a spectral triple whose D is NOT
the flow of the primes but whose Chern = κ = 2m*. **That object is the program's
nonexistent grail, not something the e-invariant hands over for free.**

**Conclusion Route 3: KILLS by dichotomy (the same D156 trifurcation),
except for a named GAP.**
- Branch (3a): carrier = primes ⟹ partition = ζ ⟹ NOT RH-free. ζ at the
  ORIENTATION/NORMALIZATION node (known, = D161).
- Branch (3b): carrier ≠ primes ⟹ RH-free but the bridge "e = 2m" is
  precisely the nonexistent Connes/Deninger object [central GAP, = D156 §4.5].

The e-invariant opens no new escape at branch (3b): it *relocates* it from the
level "metric" (D161) to the level "homotopic identification," but the content of the GAP
is identical —building a genuine arithmetic carrier without its spectral zeta
being ζ. **The secondary does not touch a new node of ζ; it touches the SAME node of D161
(the carrier's partition) or falls into the SAME GAP of D156 (nonexistent object).**

---

## Verdict

**All three routes KILL**, and —the central finding— **they kill via a single
obstruction seen at three levels**, which is the same D156 trifurcation translated
to the secondary floor:

| Route | Death mechanism | ζ node | New? |
|-----|--------------------|-----------|---------|
| 1 (filling = form) | the nullhomotopy/Lagrangian defining the secondary IS Q (orientation = dual weight) | ORIENTATION | known (= D161) |
| 2 (Witt propagates) | receiver dichotomy: ℚ/ℤ annihilates integer m (2m mod ℤ=0); ℤ ⟹ it is the primary spectral flow, not secondary | — (dies before ζ, by parity) | **NEW** |
| 3 (carrier {log k}) | carrier=primes ⟹ ζ partition; carrier≠primes ⟹ grail-GAP | ORIENTATION or existence-GAP | known (= D161/D156) |

The construction does not survive. **The deep reason:** a secondary invariant is
an *integral of a filling of the primary*; the relevant primary (Witt) is trivial
by D132 *via a Lagrangian that is a datum of Q*, so the filling reintroduces
Q (Route 1); and the honest receiver of a secondary (ℚ/ℤ) cannot house the
integer m (Route 2). The "primary's blindness to m" that motivated the construction is
real but **sterile**: the primary is blind to m not because m lives in an accessible
secondary floor, but because m is the *signature*, which no
Witt/stable-homotopic invariant reads without reintroducing the form or the prime-carrier.

### What would have to be true for it to survive (complement to the 3 attacks)

Although my verdict is death, I honestly record the logical escape —it is the
same grail from D156/D161, now with a precise added homotopic condition:

1. **(against Route 1)** There exists a nullhomotopy of the inertia primary that
   is **not** the Lagrangian of Q nor the modular orientation —a
   *purely homotopic* filling (e.g. a contraction in a stable spectrum) whose
   well-definedness invokes no quadratic form nor the dual weight. One would have
   to prove that the indeterminacy of the associated Toda bracket is killed
   **without** using Q.
2. **(against Route 2)** The secondary has a receiver that **distinguishes 2m from 0
   modulo the indeterminacy** and is neither ℚ/ℤ (which kills integers) nor ℤ (which
   collapses it to the primary spectral flow). Logical candidate: a
   stable homotopy group π^s_* with *suitable* torsion such that the image of 2m is nonzero and
   distinguishes m —but NO known example pairs π^s_* with a zero count
   [strong literature GAP].
3. **(against Route 3)** There exists a stable/arithmetic spectral-triple carrier
   whose D does **not** have spectrum {log k} (hence partition ≠ ζ) and whose e-invariant
   (ch·Td mod ℤ) **equals 2m** by a theorem. This is exactly the
   [central GAP D156 §4.5] = the nonexistent Connes/Deninger object. Phase 52's
   contribution is to narrow it: "Chern=κ" alone no longer suffices; now it is also
   required that the invariant be of order ≥2 (secondary) with a non-Q filling. **It is HARDER,
   not easier.**

The three conditions must hold **simultaneously** (a non-Q filling over a
non-prime carrier with a receiver that distinguishes the integer). I know of no
candidate in the literature meeting even two of them.

---

## Final message

**ALL THREE KILL.** The cleanest and the only one with a genuinely new flavor is
**Route 2 (receiver dichotomy)**: the honest e-invariant lives in ℚ/ℤ and *m is an
integer* (2m=κ even, D132), so 2m mod ℤ = 0 —the secondary annihilates m by
**arithmetic of the receiver**, before ζ has a chance to appear. Routes 1
and 3 lead back to the already-known node (ζ in the ORIENTATION/partition of the carrier,
= D161) or to the existence grail-GAP (= D156). **The secondary does NOT touch ζ at a new
node:** either it dies earlier (Route 2, by parity), or it dies at the
ORIENTATION node of D161 (Routes 1 and 3a), or it falls into the EXISTENCE GAP of D156 (Route 3b).

**Three labeled findings:**

- **[FINDING 163.1 — the filling IS the form]** The nullhomotopy giving well-definedness
  to any secondary over the Witt kernel is the *Lagrangian*
  witnessing the Witt-triviality of K_off (D132); a Lagrangian L=L^⊥ is a
  datum of Q by definition. Identified with D161's "orientation = dual weight":
  the secondary inherits ζ via the SAME link as the canonical metric. *Q re-enters
  as witness of its own triviality.*

- **[FINDING 163.2 — parity kills the receiver]** (NEW, not in D156/D161.)
  Since κ=2m is even and an integer, its image in the natural receiver of the e-invariant
  (ℚ/ℤ) is 0. The "Adams-style" secondary cannot transport m due to the
  very structure of its value group, independently of ζ and of the metric.
  The only receiver carrying the integer is ℤ, where the "secondary" collapses to the
  primary spectral flow —which D156 already showed requires Fredholmness = m<∞ = RH.

- **[FINDING 163.3 — the secondary narrows, not opens, the grail-GAP]** The
  secondary homotopic route is a *translation* of D156's trifurcation, not an
  escape: it translates the requirement "Chern=κ without carrying ζ" into "e-invariant=2m with
  a non-Q filling over a non-prime carrier and a receiver that distinguishes the integer." This
  ADDS conditions to the nonexistent grail; it makes it strictly harder. It is
  consistency, not progress: the Phase 43 wall still stands, now also
  against secondary homotopic inertia.

**Discipline:** no theorem "RH ⟺ X" produced; no numerics; the logical
escape (section "what would have to be true") is recorded as an honest [GAP],
not as a hope. Verdict: the Phase 52 claim is **destroyed** except for
the already-known Connes/Deninger grail, now with three additional locks.
