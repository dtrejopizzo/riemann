# B126.003 — primitive extraction cannot be monoidal

Status: `PROVED` (refutation of a requirement).
Full statement: Paper 44 §5.3, Thm. 5.4, Cor. 5.5.

Three places in the corpus record the same open item — P123.037 §5,
P123.038 §5, and §6.6 of the closure plan: primitive extraction "has not been
shown to commute monoidally with multiplication of labels".

It cannot, and the proof is one line:

    Λ(6) = 0,   Λ(2) + Λ(3) = log 6 ≠ 0.

So no functor on the label monoid with an additive degree can have
`deg Prim_n = Λ(n)`.  The requirement was a mis-specification.

The corrected structure, which holds:

1. the realization `Γ : (N,×) → (G,⋆)`, `n ↦ E_{a_S(n)}`, **is** strong
   monoidal, and its degree `log n` **is** additive (Paper 44 Thm. 4.3);
2. primitive extraction is the Möbius operation of the divisor **poset**, not
   of the monoid: the total cofiber of the P123.037 cube categorifies
   `Σ_{J⊆P(n)}(−1)^{|J|}f(n/∏_J p) = Σ_{d|n}μ(d)f(n/d)`, and at `f = log` this
   is `Λ = μ ∗ log`;
3. the two are compatible exactly through the ghost relation
   `log n = Σ_{d|n} Λ(d)`, i.e. `deg Γ_n = Σ_{d|n} deg Prim_d`.

Related: P123.082 gives `Hom(Γ_d,Γ_n)=0` for distinct classes, so the divisor
arrows have no realization as morphisms of correspondences.  They do not need
one — the cube lives on the shadow target, on the index complexes `Q_{S,d} →
Q_{S,n}` of P123.038 §3, where P123.037 §1 proves the arrows compose
literally.
