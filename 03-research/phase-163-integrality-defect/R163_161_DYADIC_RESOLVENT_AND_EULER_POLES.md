# R163_161 — Dyadic resolvent, homogeneous term and local Euler poles

**Status:** exact identity for smooth primitive sources. It is not a sign law nor does it close D.

Let `F∈C_c^∞([-T,T])` with `K_F(0)=K_F(1)=0`, where

```
K_F(s)=∫_ℝ F(u)e^((s−1/2)u)du.
```

Define `G=VJF`, with `(Vh)(u)=e^(−u/2)∫_{−∞}^u e^(t/2)h(t)dt`, `J F(u)=F(−u)`. Then `G` has compact support because `K_F(0)=0`, and

```
(∂+1/2)G=JF,
K_G(s)=K_F(1−s)/(1−s).                              (1)
```

The apparent singularity at `s=1` is removable. In particular,

```
K_G(0)=K_F(1)=0,
K_G(1)=K_F'(0).                                     (2)
```

`G`'s second Tate moment does **not** vanish from `F`'s primitivity. This is the exterior term preventing radicality from being applied directly to `G`.

Set `ℓ=log 2`, `U=√2 τ_{−ℓ}`, where `τ_a h(u)=h(u+a)`. The sums

```
D_+G=Σ_{r≥0}U^rG,
D_-G=−Σ_{r≥1}U^(−r)G,
H_G=Σ_{r∈ℤ}U^rG=D_+G−D_-G                         (3)
```

are locally finite in `D'(ℝ)`; `D_-G` moreover converges in `L²`. They satisfy

```
(I−U)D_+G=(I−U)D_-G=G,
UH_G=H_G.                                              (4)
```

Since `||U^(−1)||=1/√2<1`, `D_-G` is the **unique** `L²` solution of `(I−U)D=G`: `I−U`'s multiplier never vanishes on the real axis. So `D_+G∈L²` if and only if `H_G=0`. The homogeneous term has the form

```
H_G(u)=e^(u/2)P_G(u),       P_G(u+ℓ)=P_G(u),          (5)
```

and its Fourier coefficients, for `ω_k=2πk/ℓ`, are exactly

```
P̂_G(k)=K_F(1+iω_k)/[ℓ(1+iω_k)].                      (6)
```

Indeed, multiplying each summand of `H_G` by `e^(−u/2)` produces the `ℓ`-periodization of `e^(−u/2)G(u)`; integrating over one period gives `K_G(−iω_k)/ℓ`, and (1) gives (6). The constant mode vanishes by `K_F(1)=0`, but the modes `k≠0` are not forced to vanish. The **frequencies** `ω_k` are those of the poles of the local Euler factor `(1−2^(−s))^(−1)`; `K_F`'s arguments `1+iω_k` are shifted by the reflection in (1), they are not those poles themselves.

Finally, with `k_F(v)=⟨𝓕F,τ_v JF⟩`, `R163_160`'s kernel satisfies

```
I_F(y)=⟨𝓕F,τ_(log y)G⟩,
Σ_{r≥0} y_r^(−1/2) I_F(y_r)
 =2^(θ/2)⟨𝓕F,τ_(−θℓ)D_+G⟩,  y_r=2^(−θ−r).           (7)
```

The second pair is understood as a sum of pairings, not as an `L²` inner product when `H_G≠0`; it converges by `𝓕F`'s right super-exponential tail. So `R163_160`'s subprincipal signature is an **unstable** solution of a scaling equation. Replacing it with the stable resolvent `D_-G` discards homogeneous term (5), i.e. the modes on the local-Euler-frequency lattice (6).

## Exact pairing with the Fourier channel

Write `h=𝓕F` and `K_h(s)=∫h(u)e^((s−1/2)u)du`. The homogeneous term's pairing is absolutely defined, and `P_G`'s Fourier series gives

```
⟨h,H_G⟩
 = 1/ℓ Σ_{k∈ℤ} [overline{K_F(1+iω_k)}/(1−iω_k)]
                    K_h(1−iω_k).                    (8)
```

The sum converges absolutely: `G` is smooth and compactly supported, so its periodic coefficients decay rapidly; `e^(u/2)h(u)` and all its derivatives are integrable, by the `e^(u/2)` left tail and the super-exponential right tail. The `k=0` term is zero by `K_F(1)=0`.

The Mellin–Fourier identity replaces `K_h(1−iω_k)` with a Gamma factor times `K_F(iω_k)` (for `k≠0`; at zero a limit is taken). It does **not** turn it into `K_F(1+iω_k)` or its conjugate. Even after using the functional equation, (8) is a crossing between two Mellin lines, not a sum of squared moduli. So (8) has no sign derivable from Parseval or from Fourier reflection alone; any sign on the radical must come from an additional first-contact identity and from the exterior physical terms.

## Exact insertion of first contact

If, moreover, `F` belongs to the primitive radical in window `[-T,T]`, the compressed equation only says that, for certain scalars `a_F,b_F`,

```
1_[−T,T] A_loc F = a_F e^(u/2)+b_F e^(−u/2)           (9)
```

in the convention where the two Tate moments are projected. Since `G` is compact on that window, (2) gives exactly

```
⟨A_loc F,G⟩=a_F overline{K_F'(0)}.                   (10)
```

If `H_T`'s convention already subtracts both Tate moments, (10)'s right side is simply the corresponding Tate concomitant. None of the values `K_F(1+iω_k)` with `k≠0` appear in (10). So transferring the contact equation to (8)'s modes requires an **additional exterior identity**; (9) does not annihilate them, and replacing (10) with zero without controlling `a_F` would be incorrect. This finding does not rule out a global exterior comparison producing the sign; it only pins down what must be proved in that comparison.

Obtaining a first-contact sign would require proving, from the full physical identity — including Tate, exterior, and the other primes — a law controlling **those homogeneous modes** on the radical. Neither (4) nor primitivity does this: (4) holds for every `F`, and (2) shows the Tate moment is still present. `H_G`'s vanishing is not asserted here; imposing it would be another gate, not a consequence of this note.
