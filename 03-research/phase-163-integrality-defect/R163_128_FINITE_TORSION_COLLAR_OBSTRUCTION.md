# R163_128 — Finite Fourier obstruction forced by a first contact

**Status:** exact consequence of the crossed lift `R163_127`; does not close Row D. It turns the Gamma–Euler tail's faithfulness into a **finite** sign test that any non-zero radical must violate. The opposite inequality is still not derived from `(PC-ren)`/Poisson–Tate.

## Theorem

Let `T>0` and `0≠F∈ker H_T` be a real primitive vector of parity `ε`. Let `h_A` be `R163_127`'s lift and set `b_F=−ε h_A`. Choose an integer `K>e^(4T)`. Then

```
∫_𝕋 b_F=b_F(0)=0,
\widehat b_F(k)=Σ_{m≥1} K_m(F)²/[ζ(2m+1)k^(2m+1)]>0
                                                  (k>K),     (1)
Σ_{1≤k≤K}\widehat b_F(k)
 =−Σ_{m≥1} K_m(F)²/ζ(2m+1)
       ·Σ_{k>K} k^(−2m−1) <0.                    (2)
```

In particular, **some mode `1≤k≤K` has a negative coefficient**. There cannot be a non-zero contact whose crossed lift is positive-definite at every mode.

## Proof

The first line is `R163_127 (6)` on the radical and the normalization `\widehat h_A(0)=0`. The high-frequency formula is `R163_127 (4a)` multiplied by `−ε`; completeness of the Gamma moments makes the positivity strict if `F≠0`. The series `Σ_{k≥1}|\widehat b_F(k)|` converges. Hence

```
0=b_F(0)−∫b_F=2Σ_{k≥1}\widehat b_F(k).
```

Splitting off the tail `k>K` and using (1) proves (2), with absolute rearrangement. □

## Mathematical reading of the gate

The exterior half of the problem **already has a fixed sign**. If a first contact existed, its compensation would have to live in the `K` low modes. So it would suffice to have an arithmetic-geometric inequality

```
Σ_{1≤k≤K}\widehat b_F(k) ≥ 0                  (G_K)
```

proved **independently** for every vector in ζ's radical, with `K>e^(4T)`. (2) would exclude that radical. `(G_K)` carries the full strength of RH over the contacts and must not be assumed or derived merely from `H_TF=0`. The usefulness of the form is to localize the single site of compensation within a finite Fourier collar; proving it would require the polar/exterior corrections and the Poisson orientation, not just a square of `(PC-ren)`.

"Finite" here counts **modes `k`**, not prime data: by `R163_127`'s (5), each low coefficient `\widehat b_F(k)` still sums `w_A(kj)` for infinitely many `j`. So this reduction does not contradict the finite-arithmetic-jet NO-GO `R163_119`, nor does it authorize replacing the global Euler product with the first `K` primes.

## Adversarial tests

- For an eigenvector with `H_TF=λF`, `λ>0`, the total balance is `Σ_{k≥1}\widehat b_F(k)=−ελ||F||²`, not zero. Identity (2) is specific to the contact.
- Deletion/κ systems with a non-zero first contact must likewise exhibit a negative low mode if their crossed lift is constructed. So `(G_K)` **cannot** be deduced from the geometry of a non-negative compressed operator nor from the positivity of the Gamma kernel: it must use the ordinary values of `Λ`.
- The periodic model `R163_108` and `R163_103`'s discrete Beurling systems do not simultaneously satisfy the ordinary integer lattice and ζ's Gamma/Poisson construction. They do not supply `(G_K)` by analogy.

**Decision:** explore `(G_K)` only if it can be written as a verifiable consequence of `(PC-ren)` plus a signed polarity term. Without that derivation, (2) is an exact localization of the difficulty, not a proof of D.

An amplification `k↦p^r k` by itself does not remove the negative collar: the cocycle gives `⟨Φ_Λ,b_F(p^r·)−b_F⟩=r(log p)[b_F(0)−∫b_F]=0` at the contact. The growing positive contribution of the high modes is exactly cancelled by the low modes' contribution, also multiplied by `r log p`. Breaking that balance requires an additional physical inequality; iterating the cocycle without one only rewrites (2).
