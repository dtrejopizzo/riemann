# AUDIT_007 — Contraction module of the canonical kernel

2026-10-18. Independent check. CONSTRUCTOR_007 read in full, including §8.
**Verdict: PROVED on the declared auxiliary domain. No link with Q_T nor closure of D.**

## 1. Corpus and new reason

Targeted query of index/grid/crossword for contractions, dilations, Frobenius, isometry and Hecke; reading of P44 (degree/half-density and Frobenius Gram), INV_B_002 and entries L2_016, INV_V_001/002, P1_BBSTAR and CELL_001. None of those routes is reopened as a sign proof.

The new reason of CONSTRUCTOR007 is sufficient to examine the auxiliary: norm −R fixed beforehand, exact action on it and Gaussian defect computed without an angle bound. It is not the transport of the window form by n↦n^k of L2_016 nor a new reading of the arithmetic degree of P44. Nor does the existence of this semigroup deliver the archimedean part missing in the previous constructions. The difference lies in the concrete object and its defect Π, not in renaming dilations as Frobenius.

## 2. Haar-centred domain and completion

𝒜₀ allows X₁ in order to impose E₁A=0. The formula for −R then reduces exactly to C_αE_s|A|²+Π_α(A). A constant observable in 𝒜₀ is zero, so the norm is positive definite.

The realisation in the Hilbert product and the closure of the image are correct. It is not necessary to prove beforehand that the map A↦E_yA is closable as an operator from the first factor separately. The compatible laws P_s on finitely many primes admit the usual realisation as a product of probabilities; they are not a normalised law on the integers for s<1.

Global continuity of E₁ in the K norm on a larger space is not assumed: only the already centred algebraic subspace is completed. This choice avoids an unproved domain condition.

## 3. Geometric memory and change of scale

D_nA=1_{n|N}A(N/n) implies D_nX_d=X_nd and composition D_mD_n=D_mn. Under P_t, conditioning the valuations on v_p≥v_p(n) leaves the differences with the same independent geometric law, even when n shares primes with the indices of A. Hence the two identities of Lemma1 are correct and D_n preserves the Haar centre.

In the Gaussian, the integer substitution N=nM gives exactly E_yD_nA=q_n(y)E_{n²y}A. No approximation of means nor stationary-phase argument intervenes.

With u=n²y and s=2α,

    Π(V_nA)=∫u^(α−1)τ(u)q_n(u/n²)|E_uA|²du.

The factors n^s and n^(−2α) cancel correctly. The arithmetic component is isometric and the difference of norms is exactly (1). Since q_n<1/n for n>1, the bound (2) has correct sign and constant.

The V_n are contractions on the algebraic core, so they extend to its completion. The semigroup equality passes by continuity. An invertible unitary action or an adjoint relation is not deduced automatically.

## 4. Gaussian adjoint

For G_nf(y)=n^(s/2)q_n(y)f(n²y), the change u=n²y in the inner product leaves n^(−s/2). Thus

    G_n*g(u)=n^(−s/2)g(u/n²),
    G_n*G_nf(u)=q_n(u/n²)f(u).

Both formulas are exact in L² with measure y^(α−1)τ(y)dy. The operator is bounded; the norm bound ≤1/√n comes from the supremum of the multiplier q_n. The telescoping composition of quotients of τ gives G_mG_n=G_mn.

The memo's caution is indispensable and correct: the closure of the image in the Hilbert product is proved invariant under the actions, not reducing. One cannot simply restrict the ambient adjoint to obtain V_n* on 𝓗_α.

## 5. Deletion and monoids

For removed p, D_pA=0 in the conditioned law. If A is NONZERO as an observable of that law, p^(−s)E_s^P|A|²>0 and the isometric identity for that same p fails. This does not break contractivity: the zero operator is also a contraction. The statement only identifies a degree identity that disappears.

The precision of §8 is correct: geometric memory and multiplicative scaling are properties of normed monoids, and q_n<1/n extends to real scales n>1 by concavity. The proof of the module by itself does not discriminate all Beurling systems nor produce full specificity. The interpretation as effective divisibility of integers, the identity with R and the single-profile FE are additional information whose action on Q_T must still be proved.

Do not use the deleted-prime test as proof of a complete battery of falsifiers nor turn the partial genericity into an absolute NO-GO for every link.

## 6. Verdict of scope

The contractive multiplicative representation, its two factors, Gaussian adjoint and positive defect are PROVED. α=1/4 gives normalisation V_n=n^(1/4)D_n and norm law n^(−1/2) in the first factor before normalising; this does not yet identify the comb coefficient of Q_T.

The FE inversion of Π is not proved as a closed unitary involution on 𝓗_α, nor as a conjugation to V_n*. No trace or character form over all tests of the node is built here. None is obtained merely from V_n being a contraction or from a formula looking like Frobenius.

**Auxiliary result approved. Full target D active.** Next concrete obligation: define the realisation/inversion and the form or trace link with domain and convergence, instead of replacing it by an abstract existence or a generic norm.
