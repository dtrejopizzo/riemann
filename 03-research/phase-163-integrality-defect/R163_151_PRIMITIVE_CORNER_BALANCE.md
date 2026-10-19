# R163_151 — Corner balance of the two prime channels on the primitive space

## Setup

`R163_150` computes the anomaly of `S_N^ren L_M^*` when changing `M=N` to `M=⌊αN⌋`, `α>1`. Here we also compute `S_N^ren L_M` and pair both with a physical autocorrelation. To connect the result with `(PC-ren)` one must apply that identity to `Fcal F`, as in `R161_005`, and **not** simply replace `F` with `Fcal F` in the autocorrelation computations. The final section carries out that audit.

Let `Δ_{α,N}L=L_{⌊αN⌋}−L_N` and `P_M=L_M+L_M^*`. For `φ∈C_c^∞(ℝ)`, let `ν^+_{α,N}` be the kernel of `S_N^ren Δ_{α,N}L` and `ν^-_{α,N}` that of `S_N^ren Δ_{α,N}L^*`.

## Theorem 1 — The forward channel is purely polar on a fixed window

For every compactly supported `φ` and `N` large enough,

```
⟨ν^+_{α,N},φ⟩
 =−[Σ_{N<n≤⌊αN⌋}Λ(n)/n] ∫_ℝ e^(v/2)φ(v)dv.       (1)
```

Consequently, by the prime number theorem,

```
lim_{N→∞}⟨ν^+_{α,N},φ⟩
 =−log(α) ∫_ℝ e^(v/2)φ(v)dv.                         (2)
```

*Proof.* The discrete summand `S_N ΔL` only has translations `log(kn)>log N`, outside `supp φ` for large `N`. For the continuous `C_N ΔL`, changing `v=log(xn)` gives the weight `Λ(n)e^(v/2)/n` and the condition `e^v≤Nn`, automatically true on a compact set when `n>N`. The minus sign is that of `S_N^ren=S_N−C_N`. The convergence `Σ_{N<n≤αN}Λ(n)/n→logα` follows from `ψ(x)∼x` via partial summation. ∎

## Theorem 2 — Primitive physical balance

Let `F∈C_c^∞(ℝ)`, `c_F(v)=⟨F,τ_vF⟩=∫_ℝ overline{F(t)}F(t+v)dt` (linear inner product in the second entry), and suppose the two Tate moments

```
∫_ℝ e^(t/2)F(t)dt=∫_ℝ e^(−t/2)F(t)dt=0.           (3)
```

Then channel (2) vanishes **exactly at every sufficiently large cutoff**, because

```
∫_ℝ e^(v/2)c_F(v)dv
 = [∫e^(u/2)F(u)du][∫e^(−t/2)overline{F(t)}dt]=0.     (4)
```

Since `A_M=M_Γ−P_M` and `M_Γ` does not depend on the prime cutoff, `R163_150` gives

```
lim_{N→∞} ⟨F,S_N^ren(A_{⌊αN⌋}−A_N)F⟩
 =−(1/2)∫_1^α y^(−1/2)c_F(−log y)dy.                (5)
```

For every `F≠0`, (5)'s real part is strictly negative when `α>1` is close enough to 1, since `c_F(0)=||F||²`. So the Tate moments remove the forward edge, but **not** the reflected channel's half-step. No act of primitivization alone makes the physical product `S_N^ren A_M` path-independent.

In particular, the right derivative at `α=1` of the limit in (5) is `−||F||²/2`. This local coefficient is universal: it uses neither `Λ*1=log`, the functional equation, nor first contact. A proof obtaining its sign and calling it "the Weil sign" would only be measuring the relative choice of cutoffs.

### Saturation: exact return to phase 114's continuous model

If `supp F⊂[-T,T]` and `α≥e^(2T)`, (5)'s integral no longer changes with `α`. Let

```
Q_0(F)=∫∫ e^(|t-s|/2)F(t)overline{F(s)}dt ds,
u(t)=∫ e^(|t-s|/2)F(s)ds.
```

By symmetry of the autocorrelation, (5)'s limit's real part is `−Q_0(F)/4`. The two Tate moments make `u=0` outside `[-T,T]`; since `(d²/dt²−1/4)u=F`, integration by parts gives

```
Re lim_{N→∞}⟨F,S_N^ren(A_{⌊αN⌋}−A_N)F⟩
 = (1/4)∫_ℝ (|u'(t)|²+|u(t)|²/4)dt >0            (F≠0). (5a)
```

This identity **is not a new arithmetic sign**. It is exactly the continuous `Q_0` of `phase-114/114_d_14_RANK_TWO_BOUNDARY_CORRECTION_GATE.md`, obtained here as the limit of the cutoff anomaly. `114_d_11_CONTINUOUS_REMAINDER_FALSIFIER.md` already warns that the arithmetic remainder relative to `Q_0` admits no reliable separate inequality. So (5a) does not close D: any gain must occur in the coupling with that remainder, not in the Green square alone.

**Sign-change corollary.** For every primitive `F≠0`, (5)'s real part is negative if `α>1` is close enough to 1, but positive for every `α≥e^(2T)` by (5a). By continuity there is at least one intermediate ratio `α_F∈(1,e^(2T))` where it equals zero. Choosing that ratio depending on the state to manufacture an "annihilation" of `(PC-ren)` has no arithmetic content: it also occurs for any prime weight with the same leading anomaly, including `Z_K`.

Moreover, if `supp F⊂[-T,T]` and `N>e^(2T)`, we have exactly `⟨F,(A_{⌊αN⌋}−A_N)F⟩=0`: every new prime translation has length `log n>2T`. The comparison with (5) proves that **compressing first and then applying Müntz does not commute with the moving limit**, even within the primitive space. The difference does not require `F` to be a contact state; so it likewise does not by itself supply the specific first-contact sign.

*Proof.* (4) follows from `u=t+v` and Fubini, valid by compact support. Identities (1) and (4) annihilate the forward variation. The reflected channel's variation is `R163_150`'s (1), with a minus sign in `A_M`. Continuity of `c_F` gives the last claim. ∎

## Falsifier and scope

In `R163_147`'s `Z_K` model, replacing `Λ` with `a_K` does not change limits (2) or (5): the extra powers of 2 in `(N,αN]` contribute `O_{K,α}(N^(−1))` to both. So the corner balance is a **physical-limit faithfulness condition**, not a property distinguishing ζ or proving the Weil sign.

## Audit of the final Fourier step in `(PC-ren)`

Let `R_{M,N}^ren` be `(PC-ren)`'s right side and write `S=S_N^ren`, `E=E_N^ren`, `ΔL=L_{⌊αN⌋}−L_N`, `ΔA=−ΔL−ΔL^*`. Since `Fcal²=I`, the exact identity at finite cutoffs gives

```
⟨F,(R_{⌊αN⌋,N}^ren−R_{N,N}^ren)Fcal F⟩
 =⟨F,S ΔA F⟩.                                          (6)
```

Formula (5) computes (6)'s limit on the primitive space. There is no issue here with the tails of `Fcal F` on (6)'s **left side**: the Fourier transform cancels before the pairing. But `(PC-ren)`'s expanded right side supplies no independent sign. Indeed, `ΔH=ΔL S`, `E Fcal F=SF−JSFcal F` and `JΔL=ΔL^*J`; so

```
−ΔL^*E Fcal F−JΔL S Fcal F=−ΔL^*SF,                (7)
```

and the third term is `−ΔL S F`. Their sum is exactly `SΔA F`, since the finite translations commute. So (5)'s negative half-step **survives in the full identity but is an algebraic recombination of already-known terms**. It is not `R161_021`'s new oriented identity, and, since it also holds for `Z_K`, it cannot close D.

Closing D would require one of two things, neither proved here: (i) choosing and justifying a canonical cutoff regime whose compression and Tate corrections produce exactly `R161_021`'s defect, with an additional law using contact; or (ii) deriving from `(PC-ren)` a relation **not reducible to (7)** that cancels or controls (5) after separating the orientations. Identifying (5)'s universal sign with the scattering sign would be circular. Row D remains open.
