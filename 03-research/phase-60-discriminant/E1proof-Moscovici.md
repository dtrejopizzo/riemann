# E1 — Real-rootedness of ξ̂_{λ,N}: own proof or mandatory citation?
## Re-examination (de Branges / Hermite–Biehler lens)
**Rule:** cold. A forced proof is worse than an admitted gap. RH is NOT claimed.
**Object:** E1 = «for all λ,N, ξ̂_{λ,N}(s)=sin(Ls/2)·Σ_{|k|≤N} ξ_k/(s−d_k) has only
real zeros», where ξ is the ground state of the Weil form QW. It holds empirically even
for Davenport–Heilbronn (RH-false). **Verdict:** **MANDATORY CITATION** (CCM Thm 1.1(iii)). The attempted rescue via «quadratic
resolvent» **does not apply to the correct object**, and the de Branges construction, although it exists in
the abstract, **is equivalent to the self-adjoint realization itself** — not a shortcut. Details below. --- ## 1. The decisive question: linear or quadratic? (task §1) The rescue hypothesis was: maybe the correct CCM object is the **diagonal resolvent**
``` m(s) = ⟨ξ,(s−D)^{-1}ξ⟩ = Σ_k ξ_k²/(s−d_k) (SQUARED residues),
```
which is **automatically Herglotz** (residues ξ_k²≥0 ⟹ Im m<0 in the upper half-plane
⟹ only real zeros, Nevanlinna). If ξ̂ came from m, E1 would close in one line. **This is FALSE, and terminally so. Two things must be separated:** ### 1.1 The eigenvalue equation DOES have squares — but it is not ξ̂
The true secular equation of the **rank-1 perturbation** (H1_PROOF.md §7, pole term
P=|φ⟩⟨φ|) is
``` 1 + Σ_k |⟨φ,ψ_k⟩|²/(λ_k − μ) = 0,
```
yes, with **squared** residues |⟨φ,ψ_k⟩|²>0 — and that is why it gives a clean interlacing μ₀∈(λ₀,λ₁).
But that is the equation that locates **the eigenvalue μ₀ of the operator**, NOT the band-limited
function ξ̂ whose zeros are the γ_ρ (the zeros of ζ). They are two distinct resolvents: | object | residues | role | real-rooted |
|---|---|---|---|
| `1+Σ|⟨φ,ψ_k⟩|²/(λ_k−μ)` | squared | locates μ₀ (eigenvalue) | yes, trivially (Herglotz) |
| `f(s)=Σ ξ_k/(s−d_k)` | **linear** | secular: its zeros = γ_ρ | **is E1, the non-trivial one** | ### 1.2 ξ̂ is unambiguously the LINEAR resolvent (no typo/gauge)
Prop. \ref{prop:bandlimited} of `rh-proof.tex` fixes it unambiguously:
``` ξ̂_{λ,N} = Σ_k ξ_k · sinc_k (cardinal interpolation of the ξ_k SAMPLES on the grid d_k).
```
This is linear in ξ_k by construction: ξ̂ interpolates the **values** ξ_k, not their squares.
It is the image of the eigenvector under the Paley–Wiener isomorphism (ℓ²(Nyquist grid)→PW_Ω),
a **linear isometry**. Replacing ξ_k↦ξ_k² would destroy that structure: the resulting function
would no longer be the transform of the ground state, would not satisfy the Weil identity
⟨ξ,QWξ⟩=Σ_ρ ξ̂(γ_ρ)conj(ξ̂(conj γ_ρ)) (§1 of the master document), and its zeros would **not** be
the zeros of ζ. It is not a gauge: it is a different object, with a different zero-function. ### 1.3 Elementary proof that m and f are DISTINCT zero-functions
Counterexample from the program, ξ=(−1,2,−1), d=(−1,0,1) (hand computation, Python blocked): - **Linear** f = −1/(s+1)+2/s−1/(s−1). Numerator = −s(s−1) + 2(s²−1) − s(s+1) = (−s²+s) + (2s²−2) + (−s²−s) = **−2** (constant). ⟹ **ZERO real zeros** (in fact zero zeros). [matches the program's `−2/(s³−s)`]
- **Quadratic** m = 1/(s+1)+4/s+1/(s−1). Numerator = s(s−1) + 4(s²−1) + s(s+1) = (s²−s)+(4s²−4)+(s²+s) = **6s²−4**. ⟹ zeros at s=±√(2/3)=±0.816, **real** (as Herglotz requires). **Conclusion §1.** The quadratic resolvent m is trivially real-rooted, **but its zeros
(±0.816) are not those of ξ̂ (none)**. Replacing f by m is not fixing a typo: it changes the
zero-function and breaks the Weil identity. ξ̂ is genuinely the **linear** resolvent.
The squared-Herglotz route **does not close E1**. ∎(§1) > Severe corollary: the temptation «residues²⟹Herglotz⟹RH» is exactly the kind of shortcut that
> must be rejected. The correct square (the quadratic form ⟨ξ,QWξ⟩=Σ_ρ|ξ̂(γ_ρ)|²) **does**
> exist and **is** indeed ≥0 — but **only under RH** (γ_ρ real). That is where the RH kernel lives (IV.2),
> not a proof of E1. The square that would help is baked in with RH; the free square (m)
> is the wrong object. --- ## 2. The explicit de Branges attempt (task §2) Since f is genuinely linear, one must check whether ξ̂ is the B part (or A) of an E=A−iB of
Hermite–Biehler type, which would give real zeros via de Branges interlacing. ### 2.1 What ξ̂ DOES satisfy (favorable constraints)
ξ̂ is: entire, **of exact exponential type Ω=logλ** (Paley–Wiener), **real on ℝ**, **even**
(ι-symmetry of the ground state), and in L²(ℝ) (Plancherel–Pólya, ‖ξ̂‖²=π logλ). These are
precisely the conditions needed to *aspire* to membership in a de Branges space H(E) with E
of real, even structure. So far, promising. ### 2.2 The canonical construction and why it is circular
For a real entire function g of exponential type τ in L²(ℝ), the canonical candidate is
``` E(s) = g(s) − i·g̃(s), g̃ = Hilbert transform (harmonic conjugate) of g,
```
and g=B=−Im E|_ℝ. The **Hermite–Biehler inequality** |E(s̄)|<|E(s)| for Im s>0
**is equivalent** (de Branges, Theorems 12–13; classical Hermite–Biehler) to: > the zeros of A=Re E and of B=g are **all real and interlace**, with Wronskian
> A'B−AB' of **constant sign** on ℝ. In other words: **building E HB ⟺ already knowing that the zeros of ξ̂ are real and simple**. The
HB inequality is not a hypothesis separately verifiable from the information the
program has in isolation (positive PF envelope); **it is logically equivalent to the conclusion
E1**. There is no gain: exhibiting E with HB *is* proving E1. ### 2.3 The concrete obstacle that prevents verifying HB by hand: phase mismatch
Why can one not certify |E(s̄)|<|E(s)| directly? Because the only sign input
available is **PF in function-space**: ψ₀ is nodeless in L²([λ⁻¹,λ]) (H1, §6). But the
**coefficients ξ_k** are the coordinates of ψ₀ in the **sinc/Nyquist basis**, linked to ψ₀ by
the PW isometry — which **does not preserve coordinate positivity**. The real ground state has
``` ξ_k ≈ u_k·cos(ω* k + φ), u_k>0 (positive PF envelope), ω*≈0.966π (boundary carrier).
```
- Demodulating by the exact Nyquist carrier, ξ_k=(−1)^k η_k, would make η_k of near-constant sign, but **reintroduces (−1)^k in the residues** of f ⟹ not Herglotz.
- Since ω*≈0.966π **≠** π, there is no demodulation that makes the *raw* residues of constant sign: **neither ξ_k>0 nor (−1)^k ξ_k>0**. For E=A−iB, this means: A and B are ξ̂ and its Hilbert conjugate, and controlling the
**sign-constant Wronskian A'B−AB'** (the operative HB condition) requires precisely
the interlacing of the zeros of A and B — which is the self-adjoint spectral property. PF delivers
positivity in the wrong coordinate (envelope, not residues), so that **the sign of the
Wronskian cannot be deduced from the isolated PF information**. That is the exact technical wall. ### 2.4 Why the self-adjoint realization DOES give HB — but that IS CCM 1.1(iii)
If f(s)=Σ ξ_k/(s−d_k) is the **Weyl–Titchmarsh m-function of a self-adjoint
Jacobi/Sturm–Liouville operator** (not necessarily with positive weights), then f is
Nevanlinna/Herglotz by spectral construction, its zeros and poles interlace, and the associated
E is HB **automatically** — even with coefficients of variable sign (this is why
it works for Davenport–Heilbronn, where Λ≥0 fails: self-adjointness does not use positivity).
**But «the secular roots = real spectrum of the self-adjoint realization of CCM» is
literally the statement of CCM Thm 1.1(iii).** Reconstructing that realization (exhibiting the Jacobi
operator of which f is the m-function, or the H(E) of which ξ̂ is a member) **is re-proving 1.1(iii)**, not a
pending lemma of entire-function sugar. **Conclusion §2.** E exists in the abstract (any g∈LP of finite type lives in some H(E)),
but exhibiting it with HB **verified** is equivalent to E1, and the available PF input does not
certify it, because of the phase mismatch ω*≠π. The de Branges construction **is not self-contained**;
it collapses to the self-adjoint realization = CCM 1.1(iii). ∎(§2) --- ## 3. Brutally honest verdict (task §3) **E1 is a MANDATORY CITATION of CCM Thm 1.1(iii).** Precisely: 1. **Sub-case closed (Lemma M1, own, without citing CCM):** if all residues ξ_k>0, f is Herglotz ⟹ only real zeros with strict interlacing. Elementary, solid. **Does NOT cover the real ground state** (carrier ω*≈0.966π). 2. **Rescue via quadratic resolvent: REFUTED.** Σξ_k²/(s−d_k) is Herglotz and real-rooted, but it is a **different object** whose zeros are not those of ξ̂ (proved elementarily in §1.3); ξ̂ is genuinely the **linear** resolvent Σξ_k sinc_k fixed by Paley–Wiener and by the Weil identity. There is no typo nor gauge. 3. **Rescue via explicit de Branges: NOT a shortcut.** The canonical E=A−iB exists, but the HB inequality |E(s̄)|<|E(s)| is **logically equivalent** to E1, and its verification requires the sign of the Wronskian A'B−AB', which the PF positivity (envelope, function basis) **does not** deliver in the residue basis because of the phase mismatch ω*≠π. The only route is the m-function of a self-adjoint operator = **CCM Thm 1.1(iii)**. **Precise obstruction (one-liner):** *The real-rootedness of ξ̂ is the claim that the
linear secular f(s)=Σξ_k/(s−d_k) is a self-adjoint Nevanlinna m-function; the only
proved positivity (PF, positive envelope u_k>0) lives in the function basis and, via the boundary
carrier ω*≈0.966π≠π, does NOT translate into positivity of the raw residues ξ_k nor into a
constant-sign Wronskian. Therefore E1 admits no proof at the elementary Herglotz/HB level;
it is a mandatory citation of the self-adjoint realization CCM 1.1(iii).* **Inherited status:** E3 (Hurwitz) and N5c remain «modulo E1». The label of the master document
(🔧, mandatory citation) **confirmed and reinforced**: it is not «a repair closable with more
entire-function work». **Honesty:** E1 is **RH-neutral** (it holds for DH). Using E1 as a CCM black box to
conclude RH **is not circular** — the RH burden is not in E1 but in the convergence (IV.2).
Citing CCM 1.1(iii) here is legitimate; presenting it as a closable gap would be self-deception. *— H..*
