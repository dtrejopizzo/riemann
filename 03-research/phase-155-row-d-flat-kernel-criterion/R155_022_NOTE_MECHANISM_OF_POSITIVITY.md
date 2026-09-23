# R155_022 — Note: the mechanism of positivity, zero side and prime side (2026-09-22)

Owner's questions: "what turns real zeros into positivity? test the first 10 zeros of a 3-digit prime and of a
12-digit prime; then generalise D to infinity, verify positivity and extract the why in each case."
Scripts: `scripts/reverse/mechanism/`. Everything from tables of zeros is DIAGNOSTIC; the structural statements
are PROVED where marked (they are standard).

## 1. "Zeros of a prime" = zeros of L(s, (·/q)), q prime ≡ 1 (mod 4)

q = 101: first ten zeros on Re s = ½ (AFE with complex incomplete gamma; independent mpmath check to 9 digits):
1.164269322, 2.999351933, 5.503954505, 6.269516873, 7.506059910, 9.280980161, 10.124137411, 10.989791807,
12.420396616, 13.445433311.
q = 100000000057 (12 digits): §5 below (944 070 terms per evaluation).

## 2. The mechanism on the zero side (PROVED, one line)
For h = F⋆F̃, ĥ(t) = F̂(t)·conj F̂(t̄). If t is real, t̄ = t and ĥ(t) = |F̂(t)|² ≥ 0. Positivity of W(h) = Σ_ρ ĥ(t_ρ) is
exactly the statement t_ρ = t̄_ρ for every zero. Off the line a zero comes in a quadruple {γ±iδ, −γ±iδ} contributing
2Re[F̂(γ−iδ)conj F̂(γ+iδ)], not a square. Demonstration with the ten zeros of q = 101 and F(u) = u e^{−u²/18}e^{−iγ₁u}:
all on the line W = +4.4e−9; γ₁ moved off by δ = 0.02, 0.05, 0.1, 0.2: W = −3.68, −23.4, −100.2, −525.2.
So the "pattern in the zeros" that yields positivity is t = t̄, i.e. RH itself; no finite sample can show more.

## 3. The visible pattern (DIAGNOSTIC): GUE repulsion
Unfolded nearest-neighbour spacings of the first 10⁵ zeros of ζ vs Wigner's GUE surmise: agreement column by
column (e.g. spacing 0.1: 0.031 vs 0.032; 0.9: 1.002 vs 0.936; 1.9: 0.106 vs 0.118); fraction of spacings < 0.2:
0.0061 vs GUE 0.0086 vs Poisson 0.18. This is the fingerprint of a self-adjoint spectrum (Hilbert–Pólya): the
mechanism it points to is self-adjointness of an operator built from the primes — rows A/B (carrier), row C (trace
formula), row D (self-adjointness = positivity of the prime-side form). Statistics of a finite sample cannot prove it.

## 4. The prime side: D at infinity, verified on test functions, and the why
W(F) = pole + gamma + prime with pole = 2M₊M₋ = 2∫h cosh(u/2), gamma = (1/2π)∫m|F̂|², prime = −Σ v_n h(log n)
(phase-118 normalisation; cross-checked against 2Σ_{γ≤1419}|F̂(γ)|² to 6 digits at U = 0.30, 0.55, 0.70).
12 random C_c^∞ F per support U, ‖F‖ = 1 (`why.out`):

| U | min W | pole (mean) | gamma (mean) | prime range | worst W/pole |
|---|---|---|---|---|---|
| 0.30 | +3.3e−2 | +0.650 | −0.512 | 0 | 3.7 % |
| 0.40 | +4.7e−3 | +0.638 | −0.531 | ±6e−4 | 0.4 % |
| 0.50 | +6.9e−4 | +0.825 | −0.834 | −0.04..+0.13 | 0.06 % |
| 0.55 | +4.4e−3 | +0.432 | −0.468 | −0.03..+0.16 | 0.3 % |
| 0.60 | +9.1e−4 | +0.825 | −0.826 | −0.20..+0.29 | 0.07 % |
| 0.65 | +1.7e−4 | +0.372 | −0.417 | −0.21..+0.38 | 0.01 % |
| 0.70 | +4.1e−4 | +0.712 | −0.741 | −0.22..+0.33 | 0.02 % |

Reading:
(a) pole and gamma cancel to a few percent at every support; the primes enter as a perturbation of that residue
and by U ≈ 0.6 they are as large as either archimedean term; W survives at 10⁻⁴, i.e. three terms of size 0.5
cancel to four digits. Positivity is never visible term by term on the prime side.
(b) The average of the prime comb is the pole density (PNT: Σ_{log n≤x} v_n ≈ 4e^{x/2}, density 2e^{u/2} ≈
2cosh(u/2)); hence W(h) = archimedean part + ∫h d(2cosh(u/2)du − Σv_nδ_{log n}): positivity is the statement that the
FLUCTUATIONS of the primes about their mean, dominated by the Gamma kernel, form a positive-definite measure
(Weil's criterion; PROVED as a reformulation).
(c) Two regimes (PROVED / OPEN): for |τ| ≳ 2πe^{A_T} the archimedean m(τ) ≥ log(τ/2π) − 1/τ − 1/2τ² beats the
bounded comb (|comb| ≤ A_T): positivity there is a theorem for every window (Paper 47 Lemma 4.1, Prop env). For
low frequencies it is a finite problem per window: certified for 2T ≤ log 3 (Theorem C, margin 8.86e−5), open beyond.
(d) What a proof of D must produce: a manifestly positive form of the prime side (sum of squares / Cholesky /
dual certificate), which is what Paper 47's certificates are. The zero side gives it for free (|F̂(γ)|²); the prime
side has to earn it, and the cancellation in the table is the measure of how much.

## 5. The 12-digit prime
q = 100000000057, first ten zeros of L(s,(·/q)) on Re s = ½ (3732 s single process, 944 070 terms per evaluation):
0.372605226, 0.562898567, 0.787047838, 1.092549818, 1.226301287, 1.626158296, 1.925580479, 2.111589295,
2.434595705, 2.689324452. Riemann–von Mangoldt count up to γ₁₀: 10.06 (q = 101: 9.96) — no zero missed.
Density ≈ 4 per unit vs ≈ 0.7 for q = 101: a 12-digit conductor packs its first ten zeros below t = 2.7.
Same mechanism: with F = u e^{−u²/1250}e^{−iγ₁u} (F̂ of width 1/25, sharper than the spacing 0.19) W = +1.0e−2 on the
line; γ₁ moved off by δ = 0.005, 0.02, 0.05 gives W = −7.8e4, −1.6e6, −3.7e7 (the scale is set by ‖F‖², not by q).
(A first attempt with F̂ of width 1/3 did not flip the sign because it averaged over three neighbouring zeros —
the test must resolve individual zeros; recorded to keep the method honest.) What the 3-digit and 12-digit primes share is not a pattern in the positions (density differs by 6×)
but t = t̄ for every zero.

Labels: §2, §4(b),(c) PROVED (standard); §1, §3, §4 table DIAGNOSTIC. No label of record changes. No sign for ζ
beyond log 2 is claimed. Endpoint unchanged.
