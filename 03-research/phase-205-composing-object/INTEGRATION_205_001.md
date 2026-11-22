# INTEGRATION_205_001 — Paper 46 editor, phase 205

 Backup: `04-papers/46-row-d-dual-certificates/main_pre_205.tex`.
Compilation: pdflatex ×2, 0 errors, 0 undefined references, 190 → 191 pages.
Check script: `INTEGRATION_205_001_check.py` (mpmath, 30 digits).

## 1. Verification

**P2a / CALIB_R5 §1 (PROVED, rederived).**
- With y = x + T and sin a·sin b = ½[cos(a−b) − cos(a+b)]:
  ∫_0^{L} sin(ay)sin(b(y+u))dy = ½[(sin((a−b)L − bu) + sin bu)/(a−b) − (sin((a+b)L + bu) − sin bu)/(a+b)], with L = 2T − u.
  Matches CALIB_R5.
- With 2T(ω_k ∓ ω_l) = π(k ∓ l), the boundary term equals sin(π(k∓l) − ω_k u) = −s·sin ω_k u, with s = (−1)^{k+l}.
  This gives the form of SKELETON_001 §3 for G_kl and G_kk. ✓
- Independent quadrature at T = ½log15 over 5 triples (k,l,u), including k even and k = l: differences ≤ 5e−32. ✓
- **New fact, PROVED.**
  - G_lk = s·G_kl: the block is symmetric within each parity and antisymmetric between parities, so the sectors decouple.
  - Summing over n, with D_T(ω) = Σ v_n sin(ω log n) and C_T(ω) = Σ v_n(1 − log n/2T)cos(ω log n):
    - Π_kk = C_T(ω_k) + D_T(ω_k)/(2Tω_k);
    - Π_kl = (1/2T)[−(D_T(ω_k) − D_T(ω_l))/(ω_k − ω_l) + (D_T(ω_k) + D_T(ω_l))/(ω_k + ω_l)].
  - Checked against quadrature at (1,3), (3,5), (2,4), (1,1), (5,5): error ≤ 6e−31.
  - This is the **exact** Toeplitz−Hankel reading: the Toeplitz part is the divided difference of D_T and the Hankel
    part is (D_k + D_l)/(ω_k + ω_l), with the phases sin(ω log n) intact.
  - Correction to CALIB_R5: there it is said that the Toeplitz part "depends only on the difference." That is
    inaccurate, because the numerators depend on each frequency. The exact statement is the divided-difference formula.

**c_k (PROVED).**
- ∫cosh(x/2)cos(ωx) = 2ω cosh(T/2)sin(ωT)/(¼ + ω²), using cos ω_kT = 0.
- sin ω_kT = (−1)^{(k−1)/2}, which cancels the sign of e_k. Hence c_k > 0.
- ‖χ_ev‖² = T + sinh T.
- Checked by quadrature for k = 1, 3, 7. ✓

**(R1) extended (PROVED, AUDIT §P3).**
- e^{|s|/2} = 2cosh(s/2) − e^{−|s|/2}.
- ∫c_F·2cosh(u/2) = AB̄ + BĀ (proof of lem:polarelim) and ∫c_F e^{−|u|/2} = 𝔢(F). Hence 2∫_0^{2T}Re c_F e^{u/2} = 2Re(AB̄) − 𝔢.
- With eq:form, σ_T = m − Σv_n cos and 𝔞^♯ = 𝔪 + 𝔢, one obtains in 𝒟_T:
  - 𝔞_T = 𝔞^♯ − 𝓕_T − 2Re(AB̄);
  - equivalently, W_T = 𝔞^♯ − 𝓕_T.
- For real even F: A = B = ⟨F,χ_ev⟩ = ℓ_ev (def. of ℓ_par, l.4208). ✓
- Verified against eq:W, eq:form, def. of 𝔢 and 𝓕_T (subsec:polarfree), prop:sharp(i)(ii) and v_n = 2Λ(n)/√n.

## 2. Changes in main.tex (numbering of the new file)

- **l.462–488**, new `lem:combsine` (proved), after the proof of lem:archcount.
  - Content: e_k, G_kk, G_kl, parity symmetry, Π_kk and Π_kl in terms of D_T and C_T, and the Toeplitz/Hankel reading.
  - The proof is elementary and includes the quadrature check.
- **l.4426–4446**, after cor:H1minus:
  - `rem:chiev-sine`: c_k > 0, Σc_k² = T + sinh T and the tail c_k ≍ e^{T/2}T^{−½}ω_k^{−1}.
  - `rem:finitesign` (numerical), with the CALIB_R5 facts for ζ:
    - n₋(𝔪) = N(T);
    - the cancellation occurs within the first N sines;
    - the residual eigenvector is the polar direction, with cos ≥ 0.9999;
    - the smallest eigenvalues are −1.81, −5.77 and −23.8;
    - eigenvalues ~1e−15 are not counted.
  - In the same remark: for Epstein, the extra directions appear only with k > N(T); for a_P there is no cancellation
    and the mechanism B_P is PROVED (TOOLS_204U_001).
- **l.7325–7337**, `rem:polarelim-full` after the proof of lem:polarelim: (R1), and prop:sharp(ii) extended to 𝒟_T as
  W_T = 𝔞^♯ − 𝓕_T, with the rank-one term −2ℓ_ev² in the even sector.
- **Not integrated:**
  - the upper bound of A∞ and t₀′ = 6.12587 (pending constants);
  - E_G/β_T, 𝔅_T and L205.★, per AUDIT.

## 3. Labels
- lem:combsine, rem:chiev-sine and rem:polarelim-full: PROVED.
- rem:finitesign: NUMERICAL.
- No status changes in row D or L′♯ (they remain OPEN).
