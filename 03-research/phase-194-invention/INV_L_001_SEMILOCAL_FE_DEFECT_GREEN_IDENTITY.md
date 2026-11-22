# INV_L_001 — Clause (5): the semilocal FE-defect, the Green identity and the local reflected poles (track L)

Track L.
Notation: Paper 46 (eq:symbol, eq:form, A(F)=Φ_F(1), B(F)=Φ_F(0), Φ_F(s)=∫F(t)e^{(s−½)t}dt, 𝒫_T, N=e^{2T}); O_6 = prop:shape-eulerdel
(a_P); K1/J4 from INV_K_001/INV_J_001. Γ_R(s)=π^{−s/2}Γ(s/2). For a finite set S of primes: ζ_S=Π_{p∈S}(1−p^{−s})^{−1},
ξ_S=Γ_R ζ_S, u_S=log|ξ_S|, and the **semilocal FE-defect** d_S(s):=u_S(s)−u_S(1−s̄).

## 0. Index / corpus check (new reasons)
- Semilocal phase identity σ_T ≡ Θ_∞′−ΣΘ_p′ (local γ-factor phases): = R160_C8 / R160_C8_R1 (ε-phase, DEAD F3) and the phase-183/R186
  semilocal Sonin chain (PROVED, no sign). **Not reattempted**: §1 only records why it is O_6-stable (L1), then leaves it.
- Poisson on ℤ applied to the window test: = integer comb (INV_H H3, EI_002, CA_C_007 Epstein). **Not reattempted** (§2, one line).
- Jacobi theta with T_{p²} (R173_FINAL), theta kernels (F-θkern, 103_15–30): the window theta object of §2 is different (S-smooth
  theta, near-modularity on the window) but reduces to indexed pieces; recorded as such.
- σ-log-concavity of log|ξ| (NG-D1/D2): concerns the full ξ. **New reason for §3:** the object is the finite-S function d_S, which is
  not zero (no FE), has no zeros-of-ζ input, and whose Laplacian lives at the *local reflected poles* s=1+2πik/log p of the p-adic
  local factors (not at zeros of ζ, not at ζ(½+iτ)). No index entry uses Green's identity on the semilocal FE-defect.

## 1. Lemma L1 — local FE is O_6-stable (PROVED, elementary)
On window tests σ_T ≡ 2∂_σu_S(½+iτ) for every finite S ⊇ S_N:={p<N} (atoms p^k ≥ N are invisible against |F̂|², 𝒞_F⊂[−2T,2T];
Re(Γ_R′/Γ_R)(½+iτ)=m/2). Every local factor satisfies its own Tate local FE (|γ_v|=1 on the line), so any condition formed
place-by-place from {γ_v: v∈S} is closed under deleting places, hence holds for S∖{p<P}, i.e. for a_P. Conversely no finite S is
globally FE-compatible: d_S≢0 (d_S→−∞ at s=1, §3). So "which finite Euler products are FE-compatible" has the trivial answer
*all locally, none globally*: **NO-GO for clause (5) via local FE used place by place.** (New vs phase 183: there the question was a
semilocal positivity; here it is the FE-compatibility classification, which is trivial.)

## 2. Window theta (ARGUED, reduces to indexed pieces)
Θ_S(x)=Σ_{n∈ℤ, n S-smooth}e^{−πn²x}. Lemma L2 (PROVED): Θ_S(1/x)−√xΘ_S(x)=−Σ_{n≥N non-S-smooth}(…)=O(exp(−πN²e^{−|log x|}))
for S⊇S_N, i.e. near-modular on |log x|<4T−O(log T) because **every n<N is S_N-smooth** (additive interval ⊂ multiplicative monoid:
the semiring coincidence). For a_P (2∉S′) the defect contains −2(e^{−4π/x}−√x e^{−4πx}): O(1), not small. Beurling: generalized
integers are not a lattice, defect O(1). But L2 = (support identification "a=Λ on n<N") ⊕ (Poisson on ℤ); each is indexed
(𝒞_1 identification R163_1001 / thm:shape(C); CA_C_007), and passing to Λ needs ∂log, which fails near zeros (clause 6). ARGUED: no
deduction mechanism; not a sign carrier as stated.

## 3. Theorem L3 — Green–FE-defect identity (PROVED for F∈C_c^∞(I_T); NUMÉRICO check 6 digits)
For every finite S (window equality with 𝔞_T needs S⊇S_N), with G=|Φ_F|², ΔG=4|Φ_F′|², strip Ω={½<σ<2}:

  (1/2π)∫ 2∂_σu_S(½+iτ)|F̂(τ)|²dτ
   = (1/2π)[ 4∬_Ω d_S|Φ_F′|² dA − 2π(1+|S|)|Φ_F(1)|² − 2π Σ_{p∈S}Σ_{k≠0}|Φ_F(1+2πik/log p)|² − B_2(F) ],
  B_2(F)=∫_{σ=2}(d_S ∂_σG − G ∂_σd_S)dτ.

Proof. d_S=0 on σ=½ (1−s̄=s there), ∂_σd_S(½)=2∂_σu_S(½). In Ω, u_S(s) is harmonic; u_S(1−s̄) is harmonic except at the
reflected poles of Γ_R (s=1; next at s=3∉Ω) and of the local factors (1−p^{−w})^{−1}, Re w=0 ⇒ s=1+2πik/log p, each giving
Δd_S=+2πδ. Green's second identity on Ω (outward normal −∂_σ on σ=½), decay in τ from F smooth. ∎
Check: INV_L_001_green_check.py (T=0.6, S={2,3}, bump F): LHS −0.4794314, RHS −0.4794303.

Consequences.
(a) **P_T is exactly the condition killing the k=0 sources** (Γ and every local factor reflect a pole to s=1; A(F)=Φ_F(1)). B(F)
appears symmetrically from the strip (−1,½). This is a new reading of the Tate moments as Green residues of reflected poles.
(b) **The two-place object {∞,p}.** Each p∈S contributes −|Φ_F(1+2πik/log p)|², k≠0 — a p-adic analogue of the Tate moment, NOT
killed by P_T. By Parseval on the multiplicative lattice p^ℤ (log p·ℤ):
  Σ_{k∈ℤ}|Φ_F(1+2πik/log p)|² = (2π/log p)·∫_0^{log p}|Σ_j (F e^{·/2})(t+j log p)|²dt   (PROVED).
This couples Λ(p^k) (via the local factor at p) with the FE reflection s↦1−s̄, without passing through ζ(½+iτ) — clause (5)'s
literal requirement — and it sees small primes exactly (sources indexed by p, spacing 2π/log p).
(c) **O_6, quantitatively.** 𝔞[Λ]−𝔞[a_P] = (1/2π)[4∬Σ_{p<P}d_p|Φ′|² − 2πΣ_{p<P}Σ_k|Φ(1+2πik/log p)|² − B_2^{(p<P)}] with
d_p(s)=log|1−p^{s̄−1}|−log|1−p^{−s}|; equal to the deleted comb (consistency, tautological). a_P has *fewer* negative sources yet
fails WP_T at T≥0.60, so any sign must come from the area term. Free positivity found: Jensen gives τ-mean of d_p = (σ−1)_+log p ≥ 0
and of the archimedean part ≈(σ−½)log(|τ|/2π)>0 at large |τ|; pointwise d_p is indefinite (<0 where p^{−iτ}=1, −∞ at the sources).
(d) Clauses: (2) not a cone condition ✓; (6) built at log level, survives ∂log ✓; (5) literal ✓ (local reflected poles, not ζ(½+iτ));
**(1) fails as an identity**: it holds verbatim for Beurling primes q (sources at 1+2πik/log q); (4) likewise holds for every S.
The distinguishing content would have to be a *property* of d_{S_N} on Ω — candidate (Π_L): "4∬d_{S_N}|Φ′|² ≥ 2πΣ_{p<N,k≠0}|Φ(s_{p,k})|²
+ B_2 on P_T". (Π_L) is a restatement of λ_A ≥ 0 (REF-D) unless a reason specific to ℤ is supplied; the natural ℤ-specific input is
L2 (near-modularity of Θ_{S_N}), which would enter via the Mellin representation of ξ_{S_N} on Ω — not done.

## Status
PROVED: L1 (local FE O_6-stable; clause (5) cannot be met place by place), L2 (window near-modularity ⟺ S⊇S_N), L3 (Green–FE-defect
identity) with (a),(b) Parseval-on-p^ℤ. NUMÉRICO: L3 check. ARGUED: §2 reduction to indexed pieces. OPEN: (Π_L) via L2 — the only
live residue; it is a reformulation of D with a ℤ-specific handle (Θ_{S_N} near-modular on the window). No sign.
