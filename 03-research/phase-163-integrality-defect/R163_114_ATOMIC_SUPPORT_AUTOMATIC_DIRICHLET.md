# R163_114 — Integer support ⇒ automatic Dirichlet series ⇒ RH

**Status:** conditional theorem proved and audited in its distributional steps. **Does not close Row D**, because the support hypothesis for the effective current is not proved. Improves `R163_113`: there is no need to postulate that the current is a measure nor its Laplace convergence; both properties follow from the support and the zero count.

**Later update (`R163_116`):** the implication `supp(q_E)⊂L ⇒ E=1` now has a shorter proof: `L∩(0,log 2)=∅`, and `R163_116`'s no-gap lemma with variable displacements gives `E=1` directly. This note's arguments about atomicity and coefficient growth are additional information, not needed for that implication.

**Second proof (`R163_117`):** for this specific gap `(0,log2)`, even the explicit negative test and the rigorous verification of the absence of off-line zeros up to height `3·10¹²` suffice; `R163_115`'s global weighted-mass bound `o(T)` is not needed. Both proofs remain conditional on obtaining the gap from arithmetic.

## Theorem

Let `E` be the canonical product of `R163_001` built from all of ζ's effective off-line quartets, and let

```
q_E(u)=Σ_j 4e^{u/2}[cosh(δ_j u)−1]cos(γ_j u)/u        (1)
```

be the distributional current defined there on `u>0`, with multiplicities. Write

```
L={log n : n∈ℕ, n≥2},       P={k log p : p prime, k≥1}⊂L.
```

If `supp(q_E)⊂L` as a distribution on `(0,∞)`, then `q_E` is automatically an **atomic measure**

```
q_E=Σ_{n≥2} a_n δ_{log n},     |a_n|≪n²,                (2)
```

and for `Re s>3` its Laplace transform converges absolutely and satisfies

```
log E(s)^{-1}=Σ_{n≥2}a_n n^{-s}.                      (3)
```

Consequently `E≡1`, by Hamburger, and there are no off-line quartets. Conversely, if RH holds, `q_E=0`, so the support is contained even in `P`. Hence, for this **specific effective exchange**, support on the ordinary lattice `L` — with no requirement of support on prime powers, sign, or weights — is already equivalent to RH; it is not presented as a weaker step.

## 1. Local order bound and exclusion of delta derivatives

Let

```
A_δ(u)=4e^{u/2}[cosh(δu)−1]/u.
```

For `0≤δ≤1/2`, `u` in a compact subset of `(0,∞)` and any fixed `m`, the derivatives `A_δ^{(m)}(u)` are uniformly bounded in `δ`. The count `N_ζ(T)=O(T log T)` implies

```
Σ_j γ_j^{-2}<∞.                                      (4)
```

Integrating twice by parts against `cos(γ_j u)` shows that, for every test `φ` supported on a fixed compact subset of `(0,∞)`,

```
|⟨q_E,φ⟩| ≤ C Σ_{m=0}² ∫|φ^{(m)}(u)|du.             (5)
```

In particular, `q_E` has local order at most 2.

Fix `u₀>0`, a fixed test `ψ∈C_c^∞(−1,1)` and `φ_h(u)=ψ((u−u₀)/h)` as `h→0+`. One gets a bound **better than order 2**:

```
|⟨q_E,φ_h⟩| ≪_{u₀,ψ} log(2/h).                         (6)
```

Indeed, for `γ_j≤1/h`, each integral of (1) against `φ_h` is `O(h)` and there are `O(h^{-1}log(2/h))` zeros. For `γ_j>1/h`, change `u=u₀+hv` and integrate by parts three times in `v` to get `O(h(γ_j h)^{-3})`, uniformly in `δ_j`. By partial summation and `N_ζ(T)=O(Tlog T)`, the tail is also `O(log(2/h))`. This proves (6).

If `supp(q_E)⊂L`, every point `u₀∈L` is locally isolated. A finite-order distribution supported at `u₀` is a finite combination `Σ_{m=0}² b_m δ_{u₀}^{(m)}`. Testing it against `φ_h`, a coefficient `b_m` with `m≥1` would produce a term of order `h^{-m}` for a suitable choice of `ψ`'s jet at 0, contradicting (6). So only `b_0δ_{u₀}` can remain. Since `L` is locally finite, `q_E` is a locally finite atomic measure on `(0,∞)`.

**The endpoint `u=0`.** Sum (1) has a canonical extension to smooth tests supported on `[0,∞)`: two integrations by parts now give a boundary term `O(γ_j^{-2})`, since `A_δ(0)=0` and `A_δ′(0)=2δ²`; (4) ensures convergence. This extension does not freely add a contact term. Moreover, for a scaled test `φ_h(u)=ψ(u/h)` supported on `[0,h]`,

```
|⟨q_E,φ_h⟩|≪ h log(2/h)→0.                         (6a)
```

For `γ≤1/h`, each term is `O(h²)` because `A_δ(u)=O(u)` near zero; the number of terms is `O(h^{-1}log(2/h))`. For `γ>1/h`, two integrations by parts, including the boundary at zero, bound each term by `O(γ^{-2})`, and `Σ_{γ>1/h}γ^{-2}=O(h log(2/h))`. A combination of `δ_0` and its derivatives cannot satisfy (6a) for every test `ψ`, unless all its coefficients are zero. So the canonical extension has no contact term at the origin. This is needed to identify its Laplace transform with the series in (2), with no extra polynomial in `s`.

## 2. Polynomial growth of the masses

For any `n≥2`, take `u_n=log n`, `h_n=1/(4n)` and a test `ψ` as above with `ψ(0)=1`. The interval `|u-u_n|<h_n` contains no `log m` for any integer `m≠n`; by (2),

```
a_n=⟨q_E, ψ((u-u_n)/h_n)⟩.
```

Now use (4) and the integration by parts of (5), **without** fixing the compact set. For `u≥log2/2` and `m=0,1,2`,

```
|A_δ^{(m)}(u)| ≪ e^u                           (0≤δ≤1/2).
```

The `L¹` norm of the second derivative of `A_δ(u)ψ((u-u_n)/h_n)` is `O(e^{u_n}h_n^{-1})=O(n²)`, uniformly in `δ`. Summed against `Σγ_j^{-2}`, it gives `|a_n|≪n²`. Hence,

```
Σ_{n≥2}|a_n|n^{-σ}<∞                       (σ>3).    (7)
```

## 3. Laplace identity and conditional closure

The canonical extension of (1), viewed as an order-2, exponentially-growing distribution, admits a Laplace transform for `Re s>1`. To justify the non-compact test `e^{-su}`, cut at `u=R`; the integration-by-parts bound and `|A_δ^{(m)}(u)|≪e^u` give a tail `O_s(e^{-(Re s-1)R})`, after summing (4). At the origin the integration-by-parts boundary term is retained, finite by (4), and (6a) shows no extra contact remains. `R163_001`'s Frullani identity, summed with that same domination, gives

```
⟨q_E,e^{-su}⟩=Σ_j log E_{δ_j,γ_j}(s)^{-1}
             =log E(s)^{-1}                         (Re s>1),
```

with the branch tending to zero as `s→+∞`. If, moreover, the support is `P`, the same transform is the atomic series (7) for `Re s>3`, which proves (3).

Then `F=ζ/E` is an ordinary Dirichlet series absolutely convergent for `Re s>3`. It has the same conductor-1 functional equation as ζ, only the possible pole at `s=1`, finite order, and initial coefficient 1. [Hamburger's formulation for series convergent in some sufficiently far right half-plane, cited by Bombieri–Ghosh](https://www.mathnet.ru/php/getFT.phtml?jrnid=rm&paperid=9410&what=fullteng) gives `F=ζ`. Hence `E≡1` and no quartet was exchanged. □

## 4. Logical audit and falsifiers

- The hypothesis, even in its weaker form `supp(q_E)⊂L`, does **not** follow from ζ's Euler product: that controls `log ζ`, not `log E^{-1}`. Proving it for the effective exchange has the full strength of RH by this theorem.
- `R163_108` shows an artificial infinite exchange can indeed have its current on `P`; it does not contradict the theorem because its zeros do not cancel zeros of ζ and `ζ/E` has poles off `s=1`, violating Hamburger.
- Epstein and Davenport–Heilbronn do not simultaneously have ζ's exact Euler product and its conductor-1 functional equation; Beurling–DMV lacks the ordinary lattice `log ℕ` and the same Hamburger theorem. None falsifies the implication.
- The proof uses no positivity of `ζ/E` nor a disguised equivalent inequality. Its new content is that **mere distributional support** on `P` suffices: the absence of atomic derivatives and Dirichlet convergence follow from `N_ζ(T)=O(TlogT)`.

**Construction gate:** obtain from Poisson–Tate, `(PC-ren)` and exact arithmetic an independent reason for the effective exchange's current to have no component outside `L`. There would no longer be a need to classify the prime powers or their weights. That reason has not been obtained. Row D remains open.
