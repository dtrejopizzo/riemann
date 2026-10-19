# R163_143 — Two ports on the same weight: lattice–Euler coincidence only for `b(n)=1`

**Status:** exact identities for the selector, jets and Gamma residues, for a class of weights including ζ and the finite `κ` modifications. This is a genuine arithmetic comparison of the two channels; it does not give a `(PC-ren)` inequality nor close Row D.

## 1. Definitions

We use `a`, `Z_a=Σb_a(n)n^(−s)`, `μ_a*b_a=δ_1`, `A_a` and `w_{a,F}(n)` from `R163_142`. We assume the following series and rearrangements converge absolutely near `s=0`, and that `Z_a` continues with a simple pole at `s=1` of residue `ρ_a>0`; these conditions hold for `a=Λ` and for the finitely-modified `a_κ` models. We define two ports:

```
 B_a^lat(s)=−εΣ_{n≥1}w_{a,F}(n)
                   Σ_{d|n}μ_a(d)(n/d)^(−s),

 B_a^Eul(s)=−εΣ_{n≥1}w_{a,F}(n)
                   Σ_{d|n}μ_a(d)b_a(n/d)(n/d)^(−s). (1)
```

`B_a^lat` is exactly the Dirichlet series of `R163_142`'s lift's Fourier coefficients: the quotient `n/d` runs over the circle's torsion indices **with multiplicity 1**. `B_a^Eul` inserts the multiplicity `b_a(n/d)` of the **same Euler product** defining the physical operator. Consequently,

```
 B_a^Eul(s)−B_a^lat(s)
   =−εΣ_n w_{a,F}(n)Σ_{d|n}μ_a(d)
                   [b_a(n/d)−1](n/d)^(−s).      (2)
```

For ζ, `b_Λ(n)=1` term by term, so the two ports coincide **as functions**, not just in a few jets. This is the exact lattice–Euler equality missing for Epstein/Beurling and broken in `κ`.

As a **universal identity in the test sequence `w`**, the ports' coincidence at `s=0` is likewise equivalent to `b_a≡1`: its difference coefficients are `μ_a*(b_a−1)`, and convolving by the inverse `b_a` shows they can all vanish only if `b_a−1=0`. For an individual `F` there may indeed be accidental cancellations; that false version is not used.

## 2. Selector and first jet

Dirichlet inversion `μ_a*b_a=δ_1` gives

```
 B_a^Eul(0)=−εw_{a,F}(1)=−ε⟨F,H_{T,a}F⟩,
 B_a^lat(0)=−εΣ_n(μ_a*1)(n)w_{a,F}(n).       (3)
```

For the first jet, the derivative `−log(n/d)` and the Dirichlet-series derivative identity

```
 a=μ_a*(b_a·log)                              (4)
```

produce

```
 (B_a^Eul)'(0)=εΣ_n a(n)w_{a,F}(n),
 (B_a^lat)'(0)=εΣ_n(μ_a*log)(n)w_{a,F}(n).    (5)
```

So the Euler port has contact and the correct physical weight **for every `a`**; by itself it is F3-blind. The lattice port keeps the torsion's ordinary multiplicities and matches the other port only when `b_a=1`. For ζ, (3)–(5) simultaneously recover `R163_134 (4)` and `R163_135 (2)`; for `κ` they separate the two operations that `R163_132` had conflated.

## 3. Residues of the exterior tail

Let `s_m=2m+1`, `m≥1`, and choose `N₀>e^{4T}`. For `n>N₀`, `w_{a,F}(n)=−εΣ_mK_m(F)²n^(−s_m)`. For each fixed `m`, initially in a half-plane of convergence, the full series factor:

```
 Σ_{n≥1}n^(−s_m)Σ_{d|n}μ_a(d)(n/d)^(−s)
       =ζ(s+s_m)/Z_a(s_m),

 Σ_{n≥1}n^(−s_m)Σ_{d|n}μ_a(d)b_a(n/d)(n/d)^(−s)
       =Z_a(s+s_m)/Z_a(s_m).                (6)
```

Subtracting the `n≤N₀` terms only modifies each expression by an entire function of `s`. The sum over `m` of these **tails** converges normally away from its poles: the moments grow at most like `e^{2s_mT}`, while `n>N₀>e^{4T}` gives a geometric ratio; for `a_κ` the local coefficient series have subpolynomial growth. So both ports continue meromorphically near each `s=−2m`, and their residues are

```
 Res_{s=−2m}B_a^lat(s)=K_m(F)²/Z_a(2m+1),
 Res_{s=−2m}B_a^Eul(s)=ρ_a K_m(F)²/Z_a(2m+1). (7)
```

For ζ, `ρ_Λ=1` and `b_Λ=1`: the ports and residues coincide. For the `κ` model, `Z_{a_κ}(s)=ζ(s)e^{δH(s)}` with `δ=κ−1` and `H(s)=2^(−s)+3^(−s)+½·4^(−s)`, so

```
 ρ_{a_κ}=e^{δH(1)}=e^{23δ/24},
 Res(B_{a_κ}^Eul−B_{a_κ}^lat)_{s=−2m}
    =[e^{δH(1)}−1] K_m(F)²/Z_{a_κ}(2m+1). (8)
```

The defect has a strict sign for `δ≠0` and `K_m(F)≠0`, with the sign of `δ`; it is a quantitative falsifier at the **same Gamma pole**, not only at a low jet.

## 4. Scope and gate

The coincidence `B_Λ^lat=B_Λ^Eul` combines, in a single equality, integer-indexed torsion, `b_Λ(n)≡1` and ordinary Euler. The lattice port delivers the contact selector; the Euler port delivers the correct physical weight in the first jet; (7) joins them with the Gamma squares. There is still no Poisson–Tate law comparing their values/residues with opposite sign **after compressing**. Postulating that their coincidence forces `K_m(F)=0` would be false: for ζ the ports coincide for every `F`, not only on the radical.

Continuing this mechanism must use `(PC-ren)` to produce a *third* relation, depending on the equality state `H_{T,Λ}F=0`, between the common port and the polar/exterior collars. That relation would have to acquire defect (2) or (8) as `a` varies; without it, it would again pass the `κ` models. It is not claimed that such a relation exists or is proved here.
