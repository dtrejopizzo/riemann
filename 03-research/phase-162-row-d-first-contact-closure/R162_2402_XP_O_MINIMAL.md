# R162_2402 — Cell 5H: ×p rigidity and o-minimality (Pila–Wilkie) against the first-contact data — **NO-GO (PROVED, scoped)**

Note, single pass, pure mathematics, no numerics. Cell **5H** (integrality of ℤ × geometric/dynamical
objects). Nearest routes: R157_002 #27–#29 (EXCL arg.), R160_M12_R1 Prop 4.1 (PROVED scoped), R162_1001 Thms 3.1/5.1
(with the R162_1190 fixes). Walls named: **W8** (finZ / rationality), **W10** (no MW-5 object), **W3** (class blindness).
Conventions: R162_1001 (X = e^{2T}, c_F, w_F, h_F, Φ_a, ν_d); first-contact witness F ∈ ker H_{T_c}, F̂ entire of exponential
type T_c, real-rooted, nodes 𝒩_F = {x : F̂(x) = 0} (Gauss nodes of R162_2202/2301). "Definable" means definable with
parameters in some o-minimal expansion of (ℝ,<,+,·), in particular ℝ_{an,exp}.

## 0. Corpus check and why R157_002 excluded the route

- R157_002 #28 excluded model theory "by argument" on two grounds: (i) Λ is not definable (it would define the primes, an
  infinite discrete set); (ii) bounded-parameter families see finitely many Λ(n), so prop:uniform(b)/prop:finsupp apply.
  #27/#29: "Pila–Wilkie counts positions". The exclusion was scoped to Λ as a *function* and to T-uniformity; it never
  considered the *torsion* structure (R162_1001 did not exist) nor sets built from the first-contact witness.
- R160_M12_R1 Prop 4.1 (PROVED scoped): σ_T not definable for T ≥ ½log 2; bounded pieces are ℝ_an-definable and add nothing
  beyond real-analyticity; the family over T is not definable.
- Grep "o-minimal|Pila|Wilkie|model theory" over the whole tree: the only substantive hits are the two above plus
  R152_001 §4 and the closure-plan count (0 uses). Nothing on nodes, torsion points or the cocycle (3.1).
- New here: the node set, the Kronecker node image, the torsion distribution Φ_Λ, and the Pila–Zannier scheme
  (upper bound H^ε on the transcendental part vs lower bound H^δ from the arithmetic), each tested.

## 1. Falsifier lines, stated first

| model | line | where |
|---|---|---|
| two-atom Type I curve a = s₂w₂δ_{log2}+s₃w₃δ_{log3} (R162_2001, T_c ∈ [0.553,0.607] < log 2) | its Φ_a has **finitely many** torsion atoms (2- and 3-torsion), Φ_Λ has infinitely many; yet every definable functional of the window data at T_c < log 2 takes the same value for ζ and for (s₂,s₃)=(1,1), since X = e^{2T_c} < 4 and the two coefficient systems agree on n ≤ 3. The count difference is invisible to F. | Thm C, §4 |
| Λχ₂ (every nontrivial χ) | Φ_{Λχ} has the same torsion support as Φ_Λ (all d, via prime powers); (3.1) fails at every p with χ(p) ≠ 1 (R162_1190 fix). Node-side statements of Thms A, B hold verbatim. Counting arguments see the support, not the cocycle. | Thms A, B |
| DH, deletion Λ1_{n≥5}, κ/finmod | Thms A, B hold verbatim (they use only that F̂ is entire, real-rooted, and log p/log q ∉ ℚ). | Thms A, B |
| Beurling DMV (𝒩_B ⊄ ℤ) | Φ undefined on ℝ/ℤ, but Thm B needs only ℚ-independence of the logs of generators, which holds generically; the node statements pass. | Thm B |

So the only line on which ζ is separated from a falsifier is the torsion *support* of Φ_a (∞ vs finite atoms for the
two-atom curve); §4 shows this separation cannot be read by a definable set built from F at finite T_c.

## 2. Definability of the first-contact data

**Theorem A (definability dichotomy).** Let F be a first-contact witness (any model in the table; only "F̂ entire,
nonzero, with infinitely many real zeros" is used).
(a) 𝒩_F is not definable in any o-minimal structure; nor is the graph of F̂|_ℝ, nor of F̂ on any unbounded interval.
(b) For every prime p, S_p := {(x, p^{ix}) : x ∈ 𝒩_F} ⊂ ℝ × S¹ is not definable, and neither is the map x ↦ p^{ix} on
    any unbounded interval. The family (S_p)_p is not a definable family.
(c) For every bounded box B, 𝒩_F ∩ B is finite and F̂|_B, (x ↦ p^{ix})|_B are ℝ_an-definable. Any definable set 𝒮 built
    from F therefore uses F̂ only on a bounded set and the coefficient data only through finitely many real parameters
    (Λ(n), log n)_{n ≤ N}.
(d) Any family of definable sets indexed by d ∈ ℕ whose d-th member is 0-dimensional with ≥ d points is not a definable
    family. In particular no definable family carries the d-torsion atoms of Φ_Λ for all d.
*Proof.* (a) 𝒩_F is infinite (F̂ has exponential type T_c > 0 and is real-rooted with order-1 growth, so by
Hadamard/Lindelöf it has ≍ T_c R zeros in [−R,R]) and discrete; a definable subset of ℝ is a finite union of points and
intervals. The graph of F̂ on an unbounded interval would make its zero set definable. (b) Projection of S_p is 𝒩_F;
x ↦ cos(x log p) on an unbounded interval has infinitely many isolated zeros. A definable family has uniformly bounded
number of connected components in its fibres (uniform finiteness, van den Dries Ch. 3), while #(S_p ∩ ([−R,R]×S¹))
is unbounded in R. (c) Restricted analytic functions are ℝ_an-definable by definition. (d) Uniform finiteness. ∎

This is R157_002 #28 and M12 Prop 4.1, extended from Λ and σ_T to the witness and its nodes. Consequence: the node
set, which R162_2202 identifies as the carrier of the first-contact information, is exactly the part that o-minimality
cannot see globally; on every bounded box it is a finite set, on which Pila–Wilkie is empty (below).

## 3. Torsion avoidance and the algebraic part

**Theorem B (Kronecker node image is never torsion).** Let S be a set of ≥ 2 primes and κ_S(x) = (x log p/2π)_{p∈S} mod 1.
For every x ≠ 0, κ_S(x) is not a torsion point of (ℝ/ℤ)^S. For |S| = 1 the torsion preimage {x : x log p ∈ 2πℚ} is the
rational line 2πℚ/log p, a semialgebraic (linear) set with parameter log p.
*Proof.* If x log p = 2πr and x log q = 2πs with r,s ∈ ℚ, x ≠ 0, then log p/log q = r/s ∈ ℚ, i.e. p^b = q^a with
a,b ≥ 1, contradicting unique factorisation. ∎

So "torsion points on the node image" is empty for every F in every model with ℚ-independent logs of primes (ζ, Λχ₂,
DH, deletion, the two-atom curve — log 2/log 3 ∉ ℚ). No counting is possible, and the emptiness is class-blind (W3).

**Proposition B′ (the carriers of the cocycle are algebraic).** The torsion structure used by (3.1) lives on ℝ/ℤ with
uniformisation θ ↦ e(θ) and the maps ×p, all of which are (semi)algebraic after uniformisation: the preimage of the
d-torsion is (1/d)ℤ, contained in the algebraic set ℝ (a line). For any definable 𝒮 ⊂ ℝ^m containing the rational points
(r/d, …) of the torsion lattice, the Pila–Wilkie count N(𝒮^{tr}, H) ≤ C_ε H^ε constrains only 𝒮^{tr} = 𝒮 minus its
algebraic part; points of the form (θ, ℓ(θ)) with ℓ semialgebraic lie in 𝒮^{alg}.
*Proof.* Definition of the algebraic part (union of connected positive-dimensional semialgebraic subsets) and
Pila–Wilkie (Duke 2006, CITED). ∎

Hence the "H^ε vs H^δ" contradiction can only arise on a genuinely transcendental definable set whose rational points
are *forced*. In the Pila–Zannier scheme (Manin–Mumford) the forcing comes from a variety V ⊂ 𝔾_m^n defined over ℚ̄ and
Galois orbits of torsion points (≫ d^δ conjugates, all on V). Two inputs are indispensable: (Z1) V algebraic over ℚ̄,
(Z2) a Galois-stable lower bound.

## 4. Collapse: nothing forces rational points on a transcendental set built from F

**Theorem C (vacuity of the counting against first-contact data).** Let 𝒮 be definable, built from the first-contact
data (F, T_c, nodes, window coefficients). Then:
(a) (Only bounded data.) By Thm A(c), 𝒮 depends on F̂|_B for a bounded B and on finitely many coefficients; by R162_1001
    Thm 5.1 every pairing with Φ_Λ reduces to the finite list (log k, Λ(k))_{k ≤ X^{O(1)}}.
(b) (No forced rational points.) The equations satisfied by F (H_{T_c}F = 0, λ = 0) are linear in F with transcendental
    coefficients (digamma values, w_n = 2Λ(n)/√n); none produces a rational or bounded-degree algebraic value of F̂,
    F̂′, c_F or h_F at a rational argument. The only integral data, the index set ℕ and the atoms r/d of Φ_Λ, lie on
    algebraic carriers (Prop B′). So the set of points that λ = 0 forces into 𝒮(ℚ) is contained in 𝒮^{alg}.
(c) (Uniform bound is already trivial.) For h_F (trigonometric polynomial of degree ≤ X, R162_1001 Prop 3.2) and any
    c ∈ ℝ, #{r/d : h_F(r/d) = c} ≤ 2X unless h_F ≡ c. The o-minimal uniform bound adds nothing to the degree bound, and
    it is identical for ζ and for any model with the same coefficients on n ≤ X.
(d) (Two-atom falsifier.) For T_c < log 2 every such 𝒮 is the same set for ζ and for the two-atom model at
    (s₂,s₃) = (1,1), whose Φ_a has only 2- and 3-torsion atoms. Any contradiction derived from 𝒮 would therefore also
    hold for a model with finitely many torsion atoms, where no H^δ lower bound exists; so no contradiction is derivable.
*Proof.* (a) Thm A(c) and R162_1001 Thm 5.1. (b) Prop B′ plus Thm B: the rational points that arise are either
torsion abscissae r/d (algebraic line) or none; no value equation with rational right-hand side appears among the
defining relations of F. (c) A nonzero trigonometric polynomial of degree ≤ X has ≤ 2X zeros on ℝ/ℤ. (d) Window
coincidence: for n ≤ 3 the coefficients coincide; X = e^{2T_c} < 4 (R162_2001 §0, T_c ∈ [0.553, 0.607]). ∎

Reading: Pila–Wilkie needs (Z1)+(Z2). The first-contact data supply a transcendental analytic object (F̂) with no
algebraic structure over ℚ̄, and the arithmetic (Φ_Λ, cocycle, Euler) is carried by algebraic sets. The two never meet
on a transcendental definable set. An object satisfying (Z1) and attached to F non-trivially would be an algebraic
(motivic) carrier of the first contact — this is exactly **W10** (MW-5 object absent). Reading the torsion support of
Φ_Λ (∞ atoms) instead of finitely many log k requires data beyond X, i.e. T → ∞, which is **W8/finZ** and Theorem M.

## 5. F1, F2, M

- **F1.** Thms A, B, B′ do not use λ = 0; Thm C uses it only as the linear equation H_{T_c}F = 0, which an eigenvector
  with λ > 0 replaces by (H − λ)F = 0 with the same definability and the same (absent) rationality. Minimality of T_c is
  not used. **Not passed** (no route to use it: nothing counts).
- **F2.** Every set in §§2–4 depends on F through |F̂|, the nodes (invariant under F ↦ −F) or c_F; Φ_Λ is F-independent;
  the (PC) orientation A_M ↦ −A_M leaves nodes and c_F unchanged. **Not passed.**
- **M (Theorem M / margins).** The mechanism has no quantitative step, so M does not bite directly; but any attempt to
  make the torsion count unbounded passes through T → ∞ (Thm A(d), C(d)), where M applies.
- F3 is passed only at the object level (Φ_Λ's support vs two-atom), and fails at the use step (Thm C(d)).

## 6. Verdict and residual

**NO-GO (PROVED, scoped to sets definable in an o-minimal expansion built from finite-T first-contact data).**
(i) Nodes, node Kronecker images and ×p over all p are not definable (Thm A); (ii) node images are never torsion for two
primes (Thm B); (iii) the torsion/cocycle structure lives on algebraic carriers, so Pila–Wilkie puts it in the algebraic
part (Prop B′); (iv) no rational point is forced on a transcendental set, and the two-atom falsifier kills any count
derived from window data at T_c < log 2 (Thm C). The R157_002 exclusion stands, now with proofs and extended to the
witness; its reason is the same (bounded parameters, no definable Λ) plus the new one (no ℚ̄-algebraic V: Z1).

**Residual (named, not a live route).** A Pila–Zannier argument would need an algebraic variety V over ℚ̄, attached
non-trivially to the first contact, whose Galois orbits are forced by Euler/ℤ — this is W10 in another language. Mark
the 5H residual "o-minimality / Pila–Wilkie" as DEAD (killer W10+W8, F1, F2), keeping "rigidity of ×p measures" dead via
R162_1001 Thm 2.1–2.2 and M12 Thm 3.6. No label moves; Gate 1 stays OPEN.

References (CITED): J. Pila, A. J. Wilkie, Duke Math. J. 133 (2006); J. Pila, U. Zannier, Rend. Lincei 19 (2008);
L. van den Dries, *Tame topology and o-minimal structures* (1998); van den Dries–Macintyre–Marker, Ann. Math. 140 (1994)
(ℝ_{an,exp} o-minimal).
