# R170_811 — Proposal for a uniform arithmetic law to close D

Proposal for falsification and audit; it is not a
theorem and does not prove RH.

**Audit update:** definition (1) contains an adjoint
mismatch at the Tate port and the indicated regularization is
redundant under the Paper 47 definitions. See
[R170_812](R170_812_FIDC_AUDIT.md). The revised definition is in
[R170_813](R170_813_FIDC_REVISED.md); neither sign has been proved.
This original proposal is kept for traceability.

## 0. Decision

A single new law is proposed: an **oriented divisor–collar incidence
flow law** (FIDC). Its support is the finite Poisson–Chebyshev
identity of Paper 47,

    S_N A_M 𝓕 = {X,E_N} − L_M*E_N − JH_{M,N} − H_{M,N}𝓕,       (PC)

with

    h_{M,N}(k)=Σ_{dm=k, d≤M, m≤N} Λ(d) ≥ 0,
    H_{M,N}=Σ_{k>N}h_{M,N}(k)k^(−1/2)τ_{log k}       (M≥N).

The proposed novelty is not (PC), which is proved, but a sign for its
**linear exterior flux**, preserving orientation, both collars, and the
Tate term. The norm of (PC) is not taken: that would lose the sign
under `A_M↦−A_M`.

## 1. Object and exact interface

Fix `T>0`, `X_T=e^(2T)` and a real vector `F`, extended by zero outside
`I_T=(-T,T)`. Let `𝓕,J,S_N,L_M,A_M,E_N,H_{M,N}` be the Paper 47
operators, *A sum--product identity* section. Fix `δ>0` and

    a_j=2j+1/2,
    (R_LF)_j=√a_j exp(−a_j(T+δ))∫_{−T}^T exp(−a_jt)F(t)dt,
    1≤j≤L.

Let `S_L=R_L*R_L+JR_L*R_LJ`. To avoid the boundary being a hidden
convention, we define the oriented pairing by regularization: if `χ_ε`
equals one on `I_T`, is supported on `I_{T+ε}`, and converges to the
indicator of `I_T`, we set

    𝔉_{M,N,L}^{ε}(F)
      = Re ⟨ {X,E_N}F−L_M*E_NF−JH_{M,N}F−H_{M,N}𝓕F,
              χ_ε S_LF ⟩
        − Re ⟨ S_N r_F, 𝓕(χ_ε S_LF) ⟩.                    (1)

Here `r_F` is the unique Tate vector satisfying

    𝔞_T(F,G)=⟨r_F,G⟩                                      (2)

when `F` is in the primitive radical; outside the radical (1) is not
part of the law. The second term is the crossed Tate port. In the
expansion of (1), the parts of the translations that leave `I_T` are
kept as the exact collars `𝓔_N` of Paper 47; they are not replaced by
full moments. The **FIDC flux** is

    𝔉_{M,N,L}(F)=lim_{ε↓0}𝔉_{M,N,L}^{ε}(F),               (3)

if the limit exists. A first task for tomorrow is to prove that (3)
exists and write it only in terms of integrals over finite intervals.
This is a pending analytic definition, not a fact assumed silently.

The arithmetic interface of (1) is finite: integers `n≤N`, divisors
`d≤M`, the exact weights `Λ(d)`, and the relation `dm=k`. For each `N`,
the interior coefficients cancel by

    Σ_{d|k}Λ(d)=log k,                                    (4)

and only the incomplete hyperbola `k>N` remains. This fails immediately
if a von Mangoldt weight is changed.

## 2. The proposed law (CONJECTURE)

**FIDC.** There exists a universal choice of scales

    N(T)=⌈e^(2T)⌉,          M(T)=N(T)^2,                  (5)

and, for each `T`, a finite integer `L=L(T)` such that `R_L` is
injective on `ker H_T`, with the following property. If `T` is the
first primitive contact, `H_T≥0`, and `0≠F∈ker H_T` has definite
parity, then

    𝔉_{M(T),N(T),L}(F)
       ≥ (1−q_0) ||R_LF||²,
    q_0=log(2)/4+1/16 < 0.236.                            (FIDC+)

On the other hand, the incoming orientation of (PC), the minimality of
the first contact, and the weak equation (2) must give

    𝔉_{M(T),N(T),L}(F) ≤ 0.                              (FIDC−)

`(FIDC+)` and `(FIDC−)` are the two faces of **one single flux law**:
the divisor hyperbola pushes outward at least the energy that the
Euler channel can give back, while the first contact admits no
positive outgoing flux. The number `1−q_0` is not guessed: it is the
proved reserve of the Gamma–Euler channel,

    R_L*(I−D_{N,L})R_L ≥ (1−q_0)R_L*R_L.                 (6)

The conjectural part is that the complete oriented expansion of (PC),
with the collars and Tate, realizes that reserve with the sign of
`(FIDC+)`, and that the one-sided variation of the first contact
realizes `(FIDC−)`.

The quantifiers are essential. The claim is not for every `F`, nor for
every positive eigenvector: only for a radical vector at the first
failure scale. Paper 47 proves that an analogous sign for every
eigenvector would be false. `L(T)` may grow; a uniform gap in `T` is
not postulated.

## 3. Why this might close D

Conditionally on (3), `(FIDC+)` and `(FIDC−)` being proved:

1. For a nonzero first contact,

       0 ≥ 𝔉 ≥ (1−q_0)||R_LF||² ≥ 0.

   Since `1−q_0>0`, it follows that `R_LF=0`.

2. The choice of `L` injective on the radical implies `F=0`, a
   contradiction. The existence of some `L(T)<∞` is already proved in
   Paper 47 by the finiteness of `ker H_T` and the fidelity of all
   Gamma moments.

3. There is no primitive first contact. By the Paper 47 first-contact
   reduction, `𝔞_T≥0` on the primitive space for every `T`.

4. The bridge between the primitive form and the full row D must then
   be cited exactly in the applicable version of the manuscript. If the
   first contact of the complete form is used instead, (1) must be
   redone for the kernel of the polar Schur complement. Paper 47 warns
   that the complete null vector need not be primitive. **This bridge
   is a separate pending item**; FIDC, as formulated, closes the
   primitive annihilation problem, it does not resolve it by decree.

5. In the R169 architecture, the same mechanism applies to the short
   sum: the sieve of Eratosthenes exactly reconstructs every integer
   and prime of `[X,Y]` from the primes `<X` when `Y<X²`; (4) makes the
   tail a deterministic incidence image, not an independent family. The
   sign would then be required for every `γ∈Γ_S(F)`, not for a `γ_q`
   supposedly chosen by the window.

Step 5 explains the conceptual compatibility with the D decorrelator,
but the numerical bound `Re 𝒮<B` still needs to be derived from FIDC.
Until that translation is written with constants, the prime-sum version
of R167 should not be claimed closed.

## 4. What is proved and what is not

**Proved in the corpus:**

- (PC), the positivity `h_{M,N}(k)≥0`, and the exact cancellation (4);
- the exact collar identity `RB_N=D_NR−𝓔_N`, including the exterior
  primes;
- (6) with the explicit value `q_0`;
- fidelity of the infinite family of Gamma moments and existence of a
  finite `L(T)` injective on each radical;
- primitive first contact and the weak equation with its Tate vector;
- when `Y<X²`, Eratosthenes determines the tail from the primes `<X`.

**Conjectural:** existence of the limit (3) for the minimal-energy
datum; its expansion without omitted boundary terms; `(FIDC+)`;
`(FIDC−)`; an effective rule for `L(T)`; and the quantitative
translation to `Re 𝒮<B`.

FIDC is not presented as a reformulation of `W≥0`, nor as the Schur
complement `C−A*B^(−1)A≥0`. It is a more structured and potentially
false sufficient condition, expressed via incidences `dm=k`. Nor do we
know it to be strictly weaker than RH: if it held under the above
quantifiers, it would close the first-contact reduction and would have
that global strength.

## 5. Arithmetic mechanism being exploited

The incidence matrix `d·m=k` has two simultaneous features:

1. **Saturated zone.** For `k≤N≤M`, all divisor edges are present and
   (4) exactly cancels `K_N`. No average error or sieve bound remains.
2. **Positive boundary.** For `k>N`, the incomplete edges carry weights
   `Λ(d)≥0`; their physical direction is exterior because `log k`
   exceeds the cutoff. Poisson–Tate supplies the orientation that a
   square does not see.

The conjecture claims that, at the first contact, that positive
boundary pays the reserve `(I−D_N)` after coherently summing the paths
and the collars. This is precisely the comparison that is not in the
corpus. No prime independence, Bombieri–Vinogradov at a selected
frequency, or window-based selection of `γ_q` is invoked.

## 6. Falsifiers and checks for tomorrow

1. **Symbolic boundary check.** Expand (1) for `F` smooth and compactly
   supported in `I_T`; verify term by term that both collars, the polar
   continuum, and the crossed Tate term appear. A term with no
   counterpart or with `χ_ε` dependence refutes this formulation.

2. **Sign reversal.** Replace `A_M` by `−A_M`. The flux must change
   orientation. If the final expression is invariant, the forbidden
   square was reintroduced and FIDC is rejected.

3. **Eigenvectors with `λ>0`.** Evaluate the flux on the Paper 47
   Galerkin data. `(FIDC+)` must not automatically extend to them; the
   identity `Q_{N,L}=-2Σ(d_{m,N}+λ)|(R_LF)_m|²` provides the sign test.

4. **Certified windows.** At `T=½log3`, `0.58`, `0.62`, `0.65`, and
   `log2`, use the archived Galerkin data to compute both sides of
   `(FIDC+)` on the lowest mode or a near-null vector. The law applies
   only to the contact, but a stable violation when approaching `λ=0`
   would be strong evidence against it.

5. **Perturbation of a weight.** Change `Λ(p)` to `Λ(p)+η`. The exact
   defect

       η · #{m: pm=k},

   must appear in the interior zone, before any limit. If the formula
   does not detect the perturbation, it is not really using (4) in the
   sign step.

6. **DMV/Beurling and `M_m`.** Run the expansion with its own integer
   comb. FIDC must fail at `(FIDC+)`, `(FIDC−)`, or at the exact
   saturation by ordinary integers. If it only uses `Λ≥0`, Poisson, and
   a functional equation, it is refuted by those models.

7. **Eratosthenes v2.** For a small scale with `Y<X²`, reconstruct
   `[X,Y]` by sieving with primes `<X` and compare the `h_{M,N}`
   coefficients bit by bit. No random or free variables should be
   introduced for the tail primes.

8. **Frequency set v2.** In the translation to R167, sample the whole
   union `Γ_S(F)`, not a single `γ_q`. An argument requiring `γ_q` to be
   a function of the window is discarded.

9. **Precision W2.** Measure the residue of the expansion against the
   doubly exponential margin of Theorem M. Any `O(N^(−c))` estimate
   without exact cancellation is insufficient. The goal is a sign
   identity with zero residue or a remainder relative to `||R_LF||²`.

10. **Comparison with R170_809.** Discretize the same datum in the
    decomposition `Vx+y`. FIDC must control the exact response
    `A*B^(−1)A`, or avoid it by annihilation; replacing it with
    `A*A/g_M` reproduces the rational loss of R170_810 and refutes the
    closure.

## 7. Provisional verdict

FIDC is a coherent, falsifiable candidate, not a proof. It has three
advantages over earlier attempts: it uses the exact structure of the
integers at the place where the sign is required, it preserves the
collars and the Gamma–Euler reserve, and it is restricted to the first
contact, where a sign can be compatible with the spectral identity. Its
weak point is localized: the sign of the exterior flux has not yet been
derived from minimality and Poisson–Tate. That is the decisive
calculation for tomorrow.
