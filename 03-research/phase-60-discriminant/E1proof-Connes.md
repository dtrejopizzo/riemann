# Link E1 — lens (self-adjoint / spectral realization) **Task:** decide whether the
real-rootedness of `ξ̂_{λ,N}` closes by exhibiting the secular roots as the **spectrum of a
self-adjoint operator** (real spectrum ⟹ real-rootedness immediately), or whether it is a **mandatory citation of
CCM Thm 1.1(iii)**.
**Rule:** cold. A forced proof is worse than an admitted gap. RH is NOT claimed. --- ## 0. The object and the decisive question Secular: `f(s)=Σ_{|k|≤N} ξ_k/(s−d_k)`, `d_k=2πk/L`, `ξ` = ground eigenvector of the
Weil form `QW` (real, symmetric). `ξ̂_{λ,N}(s)=sin(Ls/2)·f(s)` is entire (the zeros of `sin` cancel
the poles `d_k`), real on ℝ, type `L/2`. Its zeros = roots of `f`. **E1:** are all the roots of `f` real, for all `λ,N` (including Davenport–Heilbronn)? **The question:** are the roots `ρ̂_n` the **spectrum of a self-adjoint operator `H`**?
If so, `σ(H)⊂ℝ` ⟹ real-rootedness for free. I examine the three requested routes. --- ## 1. Is the secular a self-adjoint resolvent with squared residues? — **NO** The hope (question 1) was that the correct object would be
``` m(s) = ⟨v,(s−D)^{-1}v⟩ = Σ_k v_k²/(s−d_k), D=diag(d_k),
```
the **Weyl m-function** of a self-adjoint operator `D` with cyclic vector `v`. Its residues
are **squares `v_k²≥0`** ⟹ `m` is Herglotz/Nevanlinna (`Im m<0` in `H`) ⟹ real zeros,
interlaced with the `d_k`. That **would close E1 today**. But: **Fact 1 (the residues are linear, not squared).** By construction (Prop 0.3, verified
in the master document), the residue of `f` at `d_k` is **exactly `ξ_k`** — the eigenvector
component, not its square. `ξ` is a real eigenvector **genuinely with sign changes**
(boundary carrier `ω*≈0.966π`, ~N sign changes). There is no hidden `v_k²`. **Fact 2 (the program's quadratic object is ANOTHER one, and its positivity IS RH).** The program does
have a quadratic form associated to `ξ`: the Weil identity (§1 of the master document)
``` ⟨ξ, QW ξ⟩ = Σ_ρ ξ̂(γ_ρ)·conj(ξ̂(conj γ_ρ)).
```
But this is a quadratic functional **in `g=ξ̂` evaluated at the zeros `γ_ρ` of ζ**, NOT the
resolvent `Σ v_k²/(s−d_k)` in the variable `s`. Its positivity (`Σ_ρ|g(γ_ρ)|²≥0` under RH) is
**RH-equivalent** (IV.2≡§V). The program's quadratic structure lives on the zero-side and is
the RH kernel; **it does not** descend to a Herglotz resolvent in `s` with residues `v_k²`. **Fact 3 (it is not a gauge).** Could `f` be a "gauge"/simplification of a quadratic `m`?
A de-modulation `ξ_k=(−1)^kη_k` with `η_k>0` (positive envelope, what H1/Perron–Frobenius
does give) **does not** turn the residues into squares: `f(s)=Σ(−1)^kη_k/(s−d_k)`, the alternating
sign **reappears** in the residues (phase mismatch of the, carrier `ω*≠π`). There is no
diagonal rescaling `ξ_k=v_k²` with `v_k` real when `ξ_k<0` for some `k`. And the real ground
state has `ξ_k<0` for a fraction of the `k`. > **Hard refutation, via the program's counterexample.** `ξ=(−1,2,−1)`, `d=(−1,0,1)`:
> `f(s)=−2/(s³−s)`. **Constant** numerator ⟹ `f=0` has **no** finite root at all. If `f`
> were `Σv_k²/(s−d_k)` (Herglotz) it would have exactly 2 real roots interlaced with
> `−1,0,1`. It does not. **The linear object is NOT a quadratic self-adjoint resolvent.** ∎ **Conclusion §1.** The quadratic-Herglotz route (Lemma M1) covers **only** `ξ_k>0` (or `(−1)^kξ_k>0`),
and the real ground state falls **outside** both. Question 1 is answered NEGATIVE: the
correct object of the program is genuinely linear with residues of variable sign. There is no quadratic
sugar to recover. --- ## 2. Explicit linear self-adjoint realization — **STRUCTURAL OBSTRUCTION** If the quadratic resolvent does not exist, question 2 asks for exhibiting a `(2N+1)`-dim (or
`(2N+2)`) self-adjoint operator `H` whose eigenvalues are the `ρ̂_n`, i.e. `det(s−H)=0 ⟺ f(s)=0`. ### 2.1 The canonical realization is the arrow matrix, and it is NOT symmetric
The standard identity: with `D=diag(d_k)`, `ξ=(ξ_k)`, `e=(1,…,1)^T`,
``` B = [[ D, ξ ], [ e^T, 0 ]] (of size (2N+2)),
```
has, by Schur complement, `det(sI−B) = det(sI−D)·(−e^T(sI−D)^{-1}ξ) = −det(sI−D)·f(s)`.
Hence **`σ(B)\{possible cancellations} = {roots of f}`**. But `B` is **NOT symmetric**: the bottom
row is `e^T` (ones) and the right column is `ξ` (eigenvector with signs); they coincide only if
`ξ_k≡1`. It is the "boundary" arrow-realization, already flagged as non-self-adjoint. ### 2.2 Self-adjointability test: is `B` similar to a real symmetric matrix?
A real matrix is similar to a symmetric one (real spectrum, diagonalizable) **only if its
spectrum is real**. But the spectrum of `B` **is NOT real in general**: > For `ξ=(−1,2,−1)`, `d=(−1,0,1)`: `f=−2/(s³−s)` has no roots; `B` (4×4) has eigenvalues
> that **are not** all real (there is pole-zero cancellation plus complex roots of the
> reduced block). A self-adjoint operator **cannot** have this spectrum. ∎ This is **decisive and mathematically terminal**: there exists a legitimate input `(ξ,d)` (with `ξ`
a real eigenvector of a symmetric matrix — in fact `(−1,2,−1)` is the ground state of the discrete
Laplacian `tridiag(−1,2,−1)` up to sign) for which the secular roots **are not real**.
Hence: **Theorem (E1-linear obstruction).** There is no **universal** construction (valid for
every `(ξ,d)` with `ξ` a real eigenvector of a symmetric matrix) that realizes the roots of `f` as the
spectrum of a self-adjoint operator. Real-rootedness, when it holds, **CANNOT** come from
a self-adjoint realization built functorially from the isolated data `(ξ_k,d_k)`.
It must use SPECIFIC information from the Weil ground state that `(−1,2,−1)` does not possess. ∎ ### 2.3 What specific information? — the boundary with CCM 1.1(iii)
The counterexample `(−1,2,−1)` comes from **any** symmetric matrix (Dirichlet
Laplacian), not from the Weil form. The program's real-rootedness holds for `QW` **and** for
`L_DH` (Davenport–Heilbronn), but **not** for `tridiag(−1,2,−1)`. What distinguishes `QW`/`L_DH`
from the Dirichlet Laplacian **is not** a sign property of `ξ` (ruled out: DH has signs,
PF fails and it is still real-rooted), **nor** total positivity (refuted, Gantmacher–Krein), **nor**
Herglotz (refuted, §1). It is the **Hermite–Biehler / de Branges** property of `ξ̂`: > `ξ̂ ∈ H(E)` for a structure function `E=A−iB` of HB type (`|E(z̄)|<|E(z)|`, `Im z>0`),
> equivalently `ξ̂` is the component `B` (or `A`) of a pair with real **interlaced** zeros,
> equivalently the secular roots are the **real spectrum of the self-adjoint realization of
> CCM** (multiplication-by-`s` compressed to the de Branges space, which IS self-adjoint because
> `H(E)` is built to be so). The subtle point: **a self-adjoint realization does exist — the compression of `M_s` on
`H(E)` — BUT its existence (that `E` be HB) is PRECISELY the statement of CCM 1.1(iii), not a
corollary of it.** `E` cannot be built from isolated `(ξ_k,d_k)`; `E` encodes the
complete Weil operator. Building `H` ⟺ proving that `E` is HB ⟺ CCM 1.1(iii). There is no shortcut
at the level of isolated information. The Laplacian `(−1,2,−1)` fails precisely because its `ξ̂`
**is not** in any `H(E)` with `E` of HB type (its `f` has numerator degree 0 < 2, violating
interlacing). **Conclusion §2.** The self-adjoint realization exists **conceptually** (compression of `M_s`
in the de Branges `H(E)` of CCM), but **constructing it = re-proving CCM 1.1(iii)**. The
elementary linear realization (arrow matrix) is structurally non-symmetric and **not symmetrizable** (non-real
spectrum for legitimate inputs). There is no universal `H = D + symmetric correction`. --- ## 3. Verdict (brutally honest) **E1 does NOT close in my lens.** Specifically: 1. **(question 1) NO** self-adjoint resolvent with squared residues exists. The residues are the linear `ξ_k` of variable sign (real ground state, carrier `ω*≈0.966π`). The program's only quadratic object (`Σ_ρ|g(γ_ρ)|²`) is RH-equivalent, not a Herglotz in `s`. The elementary Herglotz proof (Lemma M1) covers **only `ξ_k>0`** and remains confirmed and closed for that sub-case — but the real ground state falls outside it. 2. **(question 2) NO** linear self-adjoint realization is constructible from isolated `(ξ_k,d_k)`. The arrow matrix `[[D,ξ],[e^T,0]]` is non-symmetric and **not symmetrizable**: the counterexample `(−1,2,−1)→f=−2/(s³−s)` exhibits a legitimate input (real eigenvector of a symmetric matrix) whose secular roots **are not real**, impossible for a self-adjoint operator. Real-rootedness, therefore, **is not functorial** in the isolated data; it requires the specific Weil structure (which distinguishes `QW`/`L_DH` from the Dirichlet Laplacian). 3. **(question 3) I confirm the "mandatory citation".** The self-adjoint realization that would indeed give real-rootedness is the **compression of multiplication-by-`s` on the de Branges space `H(E)`** of CCM, with `E` of Hermite–Biehler type. Its existence (`E` HB ⟺ `ξ̂∈H(E)` ⟺ secular roots = real spectrum) is **exactly CCM Thm 1.1(iii)**, not an elementary corollary. Building `H` ≡ re-proving 1.1(iii). **E1 = mandatory citation of CCM Thm 1.1(iii).** **I agree, with the added edge of the spectral lens:** the obstruction is not
"missing work in entire-function theory"; it is that real-rootedness **is not encoded in the
isolated data `(ξ_k,d_k)`** — an arbitrary real eigenvector of a symmetric matrix
(`(−1,2,−1)`) reproduces them without being real-rooted. The burden is carried by the de Branges structure
of the Weil form, i.e. CCM 1.1(iii). There is no self-adjoint realization at the elementary level, and
proving it exists is proving the cited theorem. **Final label E1:** 🔧 → **mandatory citation of CCM Thm 1.1(iii)**. Sub-case `ξ_k>0` closed
(Herglotz, Lemma M1). General case (real ground state): mandatory citation, NOT closable as its own proof
with the isolated information. *— A. (in role), with H. and C..*
