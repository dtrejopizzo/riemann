# R163_001 — Canonical infinite exchange and proof defect

**Status:** algebraic identities and local convergence proved; arithmetic vanishing property **open**. RH is not asserted.

## 1. Exchange at the same height

Let there be a quartet of zeros of ζ off the line

`ρ = 1/2 ± δ ± iγ`, with `0 < δ < 1/2` and `γ > 0`, counted with multiplicity. We write `w=s−1/2` and define

```
E_{δ,γ}(s) = [((w−δ)^2+γ²)((w+δ)^2+γ²)]/(w²+γ²)².
```

The numerator has the original four zeros and the denominator has two double zeros at `1/2 ± iγ`. Moreover `E(1−s)=E(s)` and `E(conj s)=conj E(s)`. The quotient `Z₀=ζ/E` removes the original quartet and introduces points on the line, subject to whatever multiplicity cancellations may occur there. It is not assumed that `Z₀` is a positive Beurling system.

For all quartets, `E=∏_j E_{δ_j,γ_j}`. On a compact set avoiding the factors' poles, `E_j−1=O_K(γ_j^{-2})`, uniformly in `0<δ_j<1/2`. The classical count `N(T)=O(T log T)` implies `Σ_j γ_j^{-2}<∞` after separating out the small heights. So the product converges normally as a local meromorphic product. The construction does not require the extra hypothesis `N(σ,T)=o(N(T))`; that hypothesis belongs to other density problems, not to this convergence.

An exact check at the center:

```
log E(1/2) = 2 Σ_j log(1+δ_j²/γ_j²) ≥ 0,
```

with equality exactly when there are no exchanged quartets. The sum converges. It is a faithful detector, but it is written **directly as a sum over zeros**; so it does not satisfy Paper 48's arithmetic specification.

## 2. Oriented current in the variable u=log x

For `Re s>1`, Frullani for each factor gives

```
log E_j(s)^{-1} = ∫₀^∞ e^{-su} q_j(u) du,
q_j(u) = 4 e^{u/2}[cosh(δ_j u)−1] cos(γ_j u)/u.
```

For a test `φ∈C_c^∞(0,∞)`, two integrations by parts against `cos(γ_j u)` give `|⟨q_j,φ⟩|≤C_φ γ_j^{-2}`. Hence `q_E=Σ_j q_j` defines a distribution on `(0,∞)`. The Laplace identity for the infinite object should initially be read **factor by factor**, or with a convergence scheme that justifies exchanging sum and integral; local distributional convergence alone does not guarantee global integrability.

In the Euler product's zone of convergence, `dΠ_ζ=Σ_{p,k≥1}(1/k)δ_{k log p}`. Formally, and exactly in finite truncations,

```
dΠ_{Z₀} = dΠ_ζ + q_E,
dN_{Z₀} = ν_N * exp_*(q_E),     ν_N=Σ_{n≥1}δ_{log n},
exp_*(q_E) = dN_{Z₀} * Σ_{n≥1} μ(n)δ_{log n}.
```

The last equality is Möbius inversion in the convolution algebra. For infinitely many quartets, the `exp_*` expressions require choosing a space of distributions/measures and proving convergence; they do not yet constitute a positivity theorem.

## 3. Constructed defect and the exact limit of its reach

Fix a countable dense family `(φ_k)` of real tests in `C_c^∞(0,∞)` and define

```
D_test(E) = Σ_{k≥1} 2^{-k} min(1, |⟨q_E,φ_k⟩|).
```

It is non-negative. If `D_test(E)=0`, then `q_E=0` as a distribution on `(0,∞)`. **Later update:** `R163_116` proves directly that this implies `E≡1` for the effective exchange; there is no need to go through a global Laplace identity nor to add `log E(1/2)` to the defect. That addition remains a manifest alternative detector, but is not needed for faithfulness.

Each summand is continuous under distributional convergence of `q_E`; Fatou gives lower semicontinuity of `D_test` **in that topology**. For a concrete sequence of Hadamard products one must also check that their currents converge distributionally; the mere phrase "Hadamard convergence" does not by itself fix a sufficient topology.

`R163_118` further proves `E(σ)=1+o(1/σ)` on the right real axis. The caution about the global Laplace step remains valid as a separate issue, but no longer affects the defect's faithfulness.

This defect plays the role of a *topological prototype*, not the O2601.1∞ specification: it uses the zeros in its definition and there is no theorem making `D_test(E)=0` follow from the exact values `Λ(n)` of ζ. Property 2 is precisely the remaining problem, not a consequence of the prototype.

The later audit `R163_113` clarifies a further limit: proving that the full current `q_E` of the **effective** exchange admits an ordinary, absolutely convergent Euler series in **some** right half-plane already implies `E=1` by the original Hamburger formulation cited by Bombieri–Ghosh. Neither that support nor a global Laplace representation should be inferred from the local distributional convergence proved above.

## 4. Falsification tests and status

- Epstein and Davenport–Heilbronn show that a functional equation, atomicity or integrality without Euler is not enough.
- Beurling–DMV shows that a generalized Euler product and positivity without the exact integer lattice is not enough either.
- A valid argument must simultaneously use the datum `b(n)≡1` in `exp_*(Λ/log)` and the support/exact prime values; it is not enough to write both identities on separate lines.

The exchange and `D_test` are formulation tools. **They do not close Gate 1, O2601.1 or Row D.**
