# L2_BUILD_002 — Variational form and refinement tower of S_{T,k}

Setting: thm:coer-schur, def:coer-V, lem:coer-decomp of Paper 46. Fix T and k with c := c(T,k) > 0.
V := V_k ∩ D_T. Corpus check: rem:coer-honest gives the sup-formula for 𝔞_T(Ke); "some
(equivalently every) k ≥ k_0" is stated in §open; no nested/quotient (Crabtree–Haynsworth) form of
S_{T,k} across k was found (grep crabtree / quotient formula / Schur tower in phase-16x–18x and
Paper 46).

## 1. Minimum principle (PROVED)

**Proposition 1.** For e ∈ E_k: s_{T,k}(e) = min_{v∈V} 𝔞_T(e+v), attained exactly at v = −Ke.

*Proof.* By eq:coer-schur, 𝔞_T(e+v) = 𝔞_T(v+Ke) + s_{T,k}(e) and 𝔞_T(v+Ke) ≥ c‖v+Ke‖² ≥ 0, with
equality iff v = −Ke. ∎

Consequence: S_{T,k} is the matrix of the *relative minimum energy* of 𝔞_T over the affine fibres
e + V; λ_S = min over unit e of the minimum energy in the fibre. (Upper bounds by Galerkin, lower
bounds need duality — as in rem:coer-honest(2); nothing new about certification.)

## 2. Nesting (PROVED)

**Lemma 2.** E_k ⊂ E_{2k}, V_{2k} ⊂ V_k, and V_k = V_{2k} ⊕ W with W := E_{2k} ⊖ E_k (L²-orthogonal).

*Proof.* Block B_j of the k-partition is the union (up to a point) of blocks B'_{2j−1}, B'_{2j} of the
2k-partition, so e_j^± = e'^±_{2j−1} + e'^±_{2j}, and the global Tate conditions A = B = 0 are the
same; hence E_k ⊂ E_{2k}. The 2k Tate conditions per half-block imply the k per block: V_{2k} ⊂ V_k.
P_T = V_k ⊕ E_k = V_{2k} ⊕ E_{2k} (orthogonal) gives V_k = P_T ⊖ E_k = V_{2k} ⊕ (E_{2k} ⊖ E_k). ∎

## 3. The tower identity (PROVED)

**Theorem 3.** Let c(T,k) > 0. Then c(T,2k) ≥ c(T,k) > 0, and for every e ∈ E_k
  s_{T,k}(e) = min_{w∈W} s_{T,2k}(e + w),
and s_{T,2k}(w) ≥ c(T,k)‖w‖² on W. In matrix form, in an orthonormal basis of E_{2k} adapted to
E_k ⊕ W,
  S_{T,k} = S_{EE} − S_{EW} S_{WW}^{−1} S_{WE},  S_{WW} ⪰ c(T,k)·I,
i.e. S_{T,k} is the Schur complement of S_{T,2k} onto E_k.

*Proof.* c(T,2k) ≥ c(T,k) since V_{2k} ⊂ V_k. By Proposition 1 and Lemma 2 (and D_T-membership of
E_{2k}, lem:coer-decomp(iv)),
s_{T,k}(e) = min_{v∈V_k∩D_T} 𝔞(e+v) = min_{w∈W} min_{v'∈V_{2k}∩D_T} 𝔞(e+w+v') = min_{w∈W} s_{T,2k}(e+w),
applying Proposition 1 at level 2k to e + w ∈ E_{2k}. For w ∈ W ⊂ V_k:
s_{T,2k}(w) = 𝔞(w − K'w) with w − K'w ∈ V_k, so s_{T,2k}(w) ≥ c(T,k)‖w − K'w‖² = c(T,k)(‖w‖² + ‖K'w‖²)
≥ c(T,k)‖w‖² (W ⊥ V_{2k}). The finite-dimensional minimum of a quadratic form coercive in w is
the Schur complement. ∎

**Corollary 4.** (a) sign S_{T,k} = sign S_{T,2k} (inertia additivity, Haynsworth: In S_{T,2k} =
In S_{WW} + In S_{T,k}, and S_{WW} ≻ 0). Thus n_−(S_{T,k}) is independent of k ≥ k_0: the number of
negative directions of 𝔞_T on P_T is carried, without loss, by the coarsest admissible E_k.
(b) If λ_S(k) > 0 then λ_S(2k) ≤ λ_S(k): the Rayleigh quotient of s_{T,2k} at e + w_e (w_e the
minimizer) is s_{T,k}(e)/(‖e‖² + ‖w_e‖²) ≤ s_{T,k}(e)/‖e‖².
(c) The extra rows from refining are always "cheap": they are absorbed with constant c(T,k).

Labels: Prop 1, Lemma 2, Thm 3, Cor 4(a),(c) PROVED. Cor 4(b) PROVED for λ_S(k) > 0 only.
No sign certified; no negative value produced.

## 4. What this buys for (L2) and the next construction

(L2) at T is the sign of the smallest admissible Schur matrix S_{T,k_0(T)}. The tower makes the
problem *coarse-grained*: one may always go DOWN to the smallest k with c(T,k) > 0. The bottleneck
is therefore c(T,k) itself: the smaller the k at which the archimedean+prime form is coercive on
V_k, the smaller the matrix. At the limit case k = 1, E_1 = {0} and c(T,1) > 0 IS λ_A(T) > 0.
So (L2) is equivalent to the statement "c(T,k) > 0 can be pushed down to k = 1"; each halving
step k → k/2 (when 2 | k) is the sign of one Schur complement with a coercive W-block —
namely S_{T,k/2} = Schur complement of S_{T,k}. This is a *multiscale (renormalization) scheme*:

  (RG_k) if S_{T,k} ≻ 0 and c(T,k) > 0 then c(T,k/2) > 0 iff the W-block of 𝔞_T at scale k/2
  is coercive. Precisely (PROVED, same argument as Theorem 3 with V_{k/2} = V_k ⊕ W',
  W' := E_k ⊖ E_{k/2}): c(T,k/2) > 0 ⟺ S_{T,k}|_{W'} ≻ 0 (given c(T,k) > 0).

Next construction (L2_BUILD_003, OPEN): an explicit inequality between c(T,k/2) and
(c(T,k), λ_min of S_{T,k}|_W), i.e. a *one-step coercivity transfer* c(T,k/2) ≥ Φ(c(T,k), S_{T,k}|_W)
with Φ positive whenever its inputs are, computed from the two-block coupling of adjacent half
blocks (the coupling form of rem:coer-nogo restricted to the 2-dimensional Tate pairs, NOT the
full Hilbert-norm π/2, which rem:coer-nogo(b) shows is far from the minimizers). Iterated
log₂ k_0(T) ≈ T + A_T/ln2 times this would give c(T,1) = λ_A > 0.

## 5. Self-review

1. *Correctness.* Prop 1 is eq:coer-schur rewritten — correct, and essentially already implicit in
   rem:coer-honest(2) (sup-form). Lemma 2: e^{t/2}1_{B_j} is literally the sum of the two half-block
   functions — correct; requires equal blocks to be nested, true for k → 2k. Theorem 3: the
   coercivity bound on W uses W ⊂ V_k and W ⊥ V_{2k}; correct. Haynsworth inertia additivity is
   CITED (standard).
2. *Novelty.* The tower/Schur-complement-of-Schur-complement identity is the quotient formula; its
   statement for S_{T,k} is new in the corpus but mathematically routine. Cor 4(a) re-proves
   "some ⟺ every k" with inertia, slightly stronger (n_− independent of k).
3. *Is RG_k an escape or a restatement?* As stated, RG_k is a restatement: c(T,1) > 0 ⟺ λ_A > 0.
   The content would be in Φ. Danger: if Φ is built from norms of the coupling it falls into
   thm:posext/lem:half (fixed-frame norm loss) and rem:coer-nogo(a) (two-block coupling norm
   exactly π/2 on Tate-orthogonal pairs). Escape condition for 003: Φ must use the *minimizer
   geometry* of S_{T,k}|_W (the w_e of Theorem 3), not an operator norm. Whether such Φ exists is
   OPEN. Each step k → k/2 is a finite Schur complement with a coercive block, so W-det
   (determinant inheritance) applies to determinant criteria for it: Φ must not be a det/trace
   functional either.
4. *Barriers for 002 itself.* 002 decides nothing, so no barrier is violated; it lies outside
   W-loc/W-fam/W-pat (uses the full form on all of ℝ at one window), and outside finmod/cor:void
   only in the trivial sense that it uses no property of Λ at all — it is a structural identity
   valid for any weights. Any sign must come from 003's Φ fed with actual prime data.
5. *Verdict.* PROVED, routine, correct. Real value: fixes the shape of the next construction
   (multiscale coercivity transfer) and its escape condition.
