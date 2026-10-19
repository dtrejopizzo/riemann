# R163_132 — Falsifier of the entropic lift's two account books

**Status:** NO-GO for deducing closure from the mere coexistence of the contact selector and the ordinary torsional cocycle. It does not rule out a genuine mixed `(PC-ren)` identity.

## Two independent weights

Let `a` be a real weight with a finite comb on a window `I_T`, and write `A_a=M−C_a`, with the same Gamma part as ζ. Suppose the compressed primitive operator `H_{T,a}` has a contact `0≠F∈ker H_{T,a}`. Build `c_{A_a}`, `w_{A_a}`, `h_{A_a}` by the same formulas as `R163_127`, and `b_{a,F}=−εh_{A_a}`. **Separately**, we keep the torsional distribution `Φ_Λ` of the ordinary weight `Λ`, even though `a≠Λ`.

The proofs of `R163_127`–`131` use of the weight `a` only that its comb is finite and vanishes in the far exterior. Hence:

```
 b_{a,F}(0)=∫b_{a,F}=0,    b_{a,F}≠0,
 b̂_{a,F}(k)=Σ_{m≥1}K_m(F)²/[ζ(2m+1)k^(2m+1)]>0
                                      (k>e^(4T)).             (1)
```

The `Φ_Λ` cocycle, for its part, holds **for any admissible test**, not only for those built with `A_Λ` (`R162_1101 §3.3`). So, for every ordinary prime `p`,

```
 ⟨Φ_Λ,e^{b_{a,F}(p·)}−e^{b_{a,F}}⟩
   =(log p)[1−∫e^{b_{a,F}}]<0.                 (2)
```

`R163_130`'s positive non-linear tail and `R163_131`'s quartic expansion likewise survive unchanged. This builds a **two-ledger** model: first contact belongs to `a`, while the exact arithmetic identity `Λ*1=log` belongs to `Φ_Λ`. The combination of (1) and (2) does not detect that `a≠Λ`.

## Concrete falsifier and scope

There is an unconditional example of a **non-trivial primitive kernel** with `a≠Λ`: fix a window `T₀` where ζ's primitive form is strictly positive (e.g. `T₀<0.8` within the certified range). On a parity sector, `R162_103` Lemmas 2.1–2.2 give continuity of the minimal eigenvalue `g_par(κ,T₀)` and `g_par(κ,T₀)→−∞` as `κ→∞`, for the model `a_κ=κΛ` on the visible contacts and `a_κ=Λ` outside. By the intermediate value theorem there is `κ₀>1` with `g_par(κ₀,T₀)=0` and a non-zero primitive vector `F` in its kernel. Choosing `a=a_{κ₀}` satisfies (1)–(2). **We do not claim `T₀` is the model's first global contact window**; that requirement plays no role in either identity. Consequently, no contradiction can follow from them alone, nor from their asymptotic or quartic version: they hold simultaneously in a falsifier with a non-trivial radical.

The coupling failure is exact. For a general weight `a`, its own distribution `Φ_a` no longer satisfies the ordinary cocycle: the defect `D_{a,p}=ℒ_pΦ_a−Φ_a−(log p)(δ_0−Leb)` of `R162_1101 §3.2` appears. Replacing `Φ_a` with `Φ_Λ` erases that defect, but then the distribution no longer knows which weight created the contact. A proof of D must make **the same weight `a` appear on both sides of a signed physical identity**, so that `D_{a,p}` is zero *because* `a=Λ`, not because `Φ_Λ` was inserted externally.

**Operational conclusion:** route `R163_127`–`131` should not keep expanding via tests of the isolated cocycle. Its faithful Gamma datum and its contact selector can be input pieces; the new step will have to tie `(PC-ren)`'s comb to the compressed operator's comb before applying Jensen or taking a square. Without that link, the `κ` models pass every visible equation and Row D remains open.
