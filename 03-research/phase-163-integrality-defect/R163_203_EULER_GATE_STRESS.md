# R163_203 — Euler gate: stress test on the two-atom Type I curve, Beurling-like atom, deletion; quantitative (U)

Round 31.
Grid cell: row 4 (Euler gate), col B. Wall evaded: none. The gate is circular (W1), as  R163_290 also finds.
Scripts: `scripts/r163_203_euler_gate_stress.py` (contacts and modes; uses `phase-162/.../scripts/c3/t1601_nodal_rerun.py`,
Legendre K=30 even basis, fixed tail sign R162_1590), `scripts/r163_203_stab.py` (stability constant).
Every number in §2 and §4 is **UNCERTIFIED float**. The statements in §1 and §3 are proved.

## Status

- (1) **Do the modes vanish on the two-atom contact? NO. Not deciding.** No nonzero F can have all its modes vanish, by (U) (§1),
  so the question only re-asks whether F = 0. The modes at the contact are O(1) (§2).
- (2) **Beurling-like atom (x = 1.6, s = 1.412, T_c = 0.7333).** The contact exists, and its modes at 2, 3 and 1.6 are O(1).
  (U) itself is **integrality-blind**: it holds for any two incommensurable periods a, b with a + b > 2T (§3). The real-p
  falsifier therefore cannot fail at the (U) step. It has to fail at (G), and nothing in hand does that.
- (3) **Quantitative (U): PARTIAL (the "if" direction is a sketch, the "only if" is proved).** There is an exact formula for the constant, as a minimum over finite orbit
  graphs, and it vanishes exactly at 2T = log 6. Its values are float (§3).
- **Non-circular signal (review's request): none found.** Along the row s₃ = 0, s₂ ∈ [0.999, 1.0005], the modes at the contact
  vary smoothly and linearly. Their slope is about 1 in units of ‖g‖ per unit s₂. Nothing marks the Type I point
  s₂ = 0.99977 or the arithmetic point s₂ = 1. The difference across the 2.3e-4 gap is ~1e-4 relative, the same size as the
  drift between any two nearby rows. **NO-GO** for a mode–contact relation that is visible at the level of mode sizes.

## 1. Why (G) is circular

Put g = e^{u/2}F on [−T,T] and ℓ_p = log p. Fourier series on a period give

  Σ_k |K_F(1+2πik/ℓ_p)|² = ℓ_p ‖P_{ℓ_p} g‖²_{L²[0,ℓ_p)},   where (P_ℓ g)(u) = Σ_m g(u+mℓ).

If 2T < ℓ_2 + ℓ_3 = log 6, then P_2 g = P_3 g = 0 forces g = 0 (§3). Since every first contact has T_* < ½log 6 in the cases
tested here, "all modes vanish" is equivalent to F = 0. (G) is therefore the conclusion restated.

## 2. Mode sizes at the contacts (UNCERTIFIED float, K=30)

The table lists |K_F(1+2πik/ℓ)|/‖g‖ for k = 1, 2, 3. The k = 0 entry is ~1e-14 in every row (primitivity).
E_p = ‖P_p g‖²/‖g‖².

| case | T | p=2: k=1,2,3 | E_2 | p=3: k=1,2,3 | E_3 |
|---|---|---|---|---|---|
| Type I (s₂=0.99977, s₃=0) | 0.59321 | .665 .105 .025 | 1.312 | .628 .368 .127 | 0.997 |
| row s₂=0.9990 | 0.59452 | .666 .106 .026 | 1.314 | .627 .369 .127 | 0.997 |
| row s₂=1.0000 (Type II) | 0.59279 | .665 .105 .025 | 1.311 | .628 .368 .127 | 0.998 |
| row s₂=1.0005 | 0.59186 | .665 .105 .025 | 1.310 | .629 .368 .126 | 0.998 |
| deletion (0,0) | 0.59582 | .470 .085 .017 | 0.669 | .775 .075 .047 | 1.127 |
| ζ n≤3 (1,1), near-null (λ=1.4e-7, no contact) | 0.69 | .628 .047 .003 | 1.145 | .683 .302 .063 | 1.022 |
| Beurling x=1.6, s=1.412 | 0.73330 | .209 .063 .061 | 0.157 | .108 .679 .177 | 0.944 |

For the Beurling row, the modes at x = 1.6 itself are k=1,2,3: .819 .046 .029, with E = 2.87.

Reading: on the decisive curve, E_2 + E_3 ≈ 2.3. The proved floor at that T is λ_min = 0.382 (§3). So the contact vector is
nowhere near the mode-null directions, and ζ's near-null vector is not either. The modes do not tell the Type I contact
apart from the Type II contacts next to it, from ζ's near-kernel, or from the deletion contact, beyond smooth O(1) changes.

## 3. Quantitative (U)

**Proposition.** Let a, b > 0 with a/b ∉ ℚ, and let M_T = P_a*P_a + P_b*P_b on L²[−T,T]. Then

  ‖g‖² ≤ λ(T)⁻¹ ( a⁻¹ Σ_k |ĝ_a(k)|² + b⁻¹ Σ_k |ĝ_b(k)|² ),

where λ(T) = inf over u₀ of the smallest eigenvalue of the finite matrix M(u₀). Here M(u₀)_{(i,j),(i',j')} = [i=i'] + [j=j'] on
the coset points u₀ + ia + jb lying in [−T,T]. Moreover λ(T) > 0 if and only if 2T < a + b.

**Proof.**
- M_T decomposes over cosets of aℤ + bℤ, which gives the finite matrices M(u₀).
- M(u₀) = BBᵀ, where B is the point/class incidence matrix of the bipartite graph H whose nodes are the a-classes and the
  b-classes and whose edges are the points. So M(u₀)x = 0 exactly when x is a signed cycle of H.
- A cycle in H needs four points u, u+ia, u+ia+jb, u+jb inside the window, which requires |i|a + |j|b ≤ 2T. (A longer
  cycle contains such a rectangle after a staircase reduction. This step is only SKETCHED; the exact orbit enumeration below agrees with it.) So for 2T < a + b, H is a forest and M(u₀) ≻ 0.
- Only finitely many orbit types occur, so the infimum is attained.
- For 2T ≥ a + b, the rectangle u, u+a, u+b, u+a+b with signs (+,−,−,+) lies in the kernel. ∎

Values, computed by exact enumeration of orbit types between the breakpoints s·T − ia − jb (float eigenvalues):

| T | λ(T) for {2,3} | λ(T) for {1.6,3} |
|---|---|---|
| 0.593 | 0.38197 (= 2 − 2cos(π/5)) | 0.268 |
| 0.733 | 0.19806 (= 2 − 2cos(π/7)) | 0.0402 |
| 0.8047 | 0.0722 | 0 (log 4.8 < 2T) |
| 0.85–0.8955 | 0.0238 | 0 |

λ(T) = 0 for {2,3} only when 2T ≥ log 6, that is T ≥ 0.89588. At the target T_* ≈ 0.8047 the stability constant is
1/λ ≈ 13.8.

**Finite-k version.** For g ∈ H¹₀ we have Σ_{|k|>K} |ĝ_p(k)|² ≤ (ℓ_p/2πK)² ℓ_p ⌈2T/ℓ_p⌉ ‖g′‖². This gives

  ‖g‖² ≤ λ(T)⁻¹ [ Σ_p ℓ_p⁻¹ Σ_{|k|≤K} |K_F(1+2πik/ℓ_p)|² + Σ_p ⌈2T/ℓ_p⌉ (ℓ_p/2πK)² ‖g′‖² ].

The Beurling–Malliavin density threshold Σ log p > 2T is attained here by an elementary finite-graph argument. No
arithmetic enters: real periods behave identically.

## 4. Falsifier lines

| test | what happens |
|---|---|
| Two-atom Type I curve | The contact is genuine and its modes are O(1). Consistent with (U), so the test is circular, not discriminating. |
| Beurling-like (x = 1.6) | (U) holds for {1.6, 3} when T < 0.784. The contact modes are O(1). Integrality is not used. |
| Deletion | Modes O(1). |
| ζ near-null | Modes O(1). Positivity is not visible in mode size. |

Λχ₂, Z_K and Epstein/DH were not computed. By §3, (U) holds for them whenever their window prime periods satisfy
Σ ℓ > 2T, independent of their weights.

## 5. Residual

The gate can only make sense as a dynamical statement relating the modes to κ (Lemma 3 of R162_2101: Type I ⟺ κ = 0),
for example ⟨modes, Gamma-weighted K_h(1−iω_k)⟩ (R163_161 eq. 8) tied to κ. Testing that requires the exterior pairing (8),
which was not computed here. This is O163.203a.
