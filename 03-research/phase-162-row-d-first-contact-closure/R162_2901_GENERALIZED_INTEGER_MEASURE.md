# R162_2901 — O2801.1: generalized-integer measure dN₀ of ζ₀ = ζ/R — **NO-GO (PROVED): positivity is never forced; in the strict deletion class dΠ₀ ≥ 0 fails for every m ≥ 1 (Thm A, this is the 2β* oscillation law, i.e. E1 content), and one symmetric factor more gives a genuine positive Beurling system (dΠ₀ ≥ 0, dN₀ ≥ 0, FE, all zeros in the strip on the line) (Thm B). O2801.1 closes negatively and folds into O2601.1 (integrality).**

Pure math, no numerics. Cell 4F. Residual O2801.1 of R162_2801 §5. Gate 1 OPEN; no sign claimed.
Corpus check: R162_2801 (§0 setup, Lemmas 1–3), R162_2802 (exp_* ledger, the deletion ledger ">=0 rational"), R162_2601 (Λ̃, Thm T),
R162_2501 (Prop 1, 2β* law, M_m), grid §4 Beurling DMV. 00-references/beurling-dmv: BDV 2004.11501 §1 (DMV restated,
CITED secondary). No earlier file computes dΠ₀/dN₀ for ζ/R, and none looks at extra symmetric factors with a real pole.

## 0. Setup and notation
H(m): ξ has exactly m ≥ 1 off-line quartets Q_j={ρ_j,ρ̄_j,1−ρ_j,1−ρ̄_j}, ρ_j=½+β_j+iγ_j, 0<β_j<½, β* = max β_j.
γ_j ≠ 0 always (ζ(σ)<0 on (0,1), PROVED classical), so Q_j has four distinct points and no real points.
A = ∪Q_j (the 4m points a), B = 4m chosen points b on Re s=½, stable under b↦b̄ and b↦1−b. P=∏_A(s−a), P₀=∏_B(s−b),
R=P/P₀, ζ₀=ζ/R = ζ·P₀/P. Variable u = log x ≥ 0; a Beurling system is (dΠ, dN) on [0,∞) (x ≥ 1) with
ζ_B(s)=∫e^{−su}dN(u), log ζ_B = ∫e^{−su}dΠ(u), dN = exp_*(dΠ) = Σ_k dΠ^{*k}/k! (additive convolution in u).
"Genuine" = dΠ ≥ 0 supported in (0,∞); then dN ≥ 0 automatically (exp_* of a positive measure is positive).

## 1. Falsifier lines first
- **deletion** is the object itself (ζ₀). Anything proved about ζ₀ must be a property of *the deleted data*, not of ζ.
- **M_m** (2501): ζ×rational with m' off-line quartets and same FE/log-derivative structure — any sign statement about
  "ζ × symmetric rational" must be equally true for M_m, which has off-line zeros; so positivity of a ζ×rational system
  cannot itself say anything about where ζ's zeros are (checked in Thm B: it doesn't).
- **Λ̃** (2601/2802): F̃ = exp(Σ Λ̃/log · n^{−s}) has ≥0 non-integer coefficients and exactly the m off-line zeros;
  positivity of an integer-type measure is compatible with off-line zeros.
- **DMV** (CITED secondary, BDV §1): genuine Beurling systems with N(x)=ρx+O(x^θ) and zeros off the line exist.
  Conversely genuine Beurling systems satisfying RH exist (BDV title result). So "positive + FE-free" separates nothing;
  the only question is whether the *specific form* ζ·(rational) forces a sign violation. Thm B: it does not.

## 2. Explicit measures (PROVED)
**Prop 1 (dΠ₀).** For Re s>1, by Frullani, log((s−b)/(s−a)) = ∫_0^∞ (e^{au}−e^{bu}) e^{−su} du/u
(valid for Re s > Re a, Re b; pair a↔b arbitrarily). Hence
  dΠ₀ = Σ_n (Λ(n)/log n) δ_{log n} + π₀(u) du,  π₀(u) = λ(u)/u,  λ(u) := Σ_A e^{au} − Σ_B e^{bu}.
Explicitly λ(u) = e^{u/2} [ Σ_j 4cosh(β_j u)cos(γ_j u) − Σ_{B} e^{i Im b·u} ] (real). ∎
**Prop 2 (dN₀).** If A has simple points (generic; else use higher-order partial fractions), 1/R = P₀/P = 1 + Σ_A c_a/(s−a)
with Σ_A c_a = 0 (deg P = deg P₀ = 4m and deg(P₀−P) ≤ 4m−2, since Σa = Σb = 2m by the symmetries). Then
  dN₀ = Σ_n δ_{log n} + h(u) du,  h(u) = Σ_A c_a e^{au} Σ_{n≤e^u} n^{−a}.
Using ζ(a)=0 and Euler–Maclaurin, Σ_{n≤x} n^{−a} = x^{1−a}/(1−a) + (½−{x})x^{−a} + O_a(x^{−Re a−1}), so
  h(u)/x = (1/R(1) − 1) + (½−{x})x^{−1}Σc_a + O(x^{−2}) = (1/R(1) − 1) + O(x^{−2}),  x=e^u,
using Σ_A c_a/(1−a) = 1/R(1) − 1 and Σ c_a = 0. Total N₀(x) = x/R(1) + O(1) type, consistent with Res_{s=1}ζ₀ = 1/R(1). ∎
Remark. The off-line zeros are *invisible* in dN₀ at leading order (they cancel through ζ(a)=0); they are visible in dΠ₀.
This is the multiplicative/additive asymmetry of 2802 (Λ side sees zeros, integer side is Lindelöf-type).

## 3. Theorem A (strict deletion class: dΠ₀ ≥ 0 fails, PROVED)
For every m ≥ 1 and every admissible B, π₀ takes negative values on a set of u of positive lower density; hence ζ₀
is not a genuine Beurling system.
Proof. The a.c. part of a positive measure is positive, and the atoms of dΠ₀ are singular, so dΠ₀ ≥ 0 ⟺ λ ≥ 0 a.e.
Write λ(u) = e^{(½+β*)u}[g(u) + o(1)], g(u) = 2Σ_{β_j=β*} cos(γ_j u) (all B-terms and lower quartets are
O(e^{(½+β')u}), β'<β*). g is a nonzero trig polynomial with nonzero frequencies, Bohr mean 0, so g < −ε on a relatively
dense family of intervals of fixed length (a nonnegative a.p. function of mean 0 is ≡ 0). ∎
*Content check:* this is literally the statement that ψ₀ − (atoms) oscillates at size x^{½+β*}, i.e. Prop 1 of 2501 /
Landau oscillation — the deleted zeros re-enter as a signed density. No information about ζ beyond H(m) is used.
dN₀ in the strict class: Prop 2 gives h/x → 1/R(1) − 1, which is > 0 for suitable B (|Im b| large makes P₀(1) large),
so dN₀ ≥ 0 for large x is achievable; small x is a finite-parameter question left open and irrelevant (Thm B).

## 4. Theorem B (positivity is achievable; PROVED, conditional only on H(m) for the existence of ζ₀)
Let S₁(s) = (s−½)²/(s(s−1)) (degree 0, S₁(1−s)=S₁(s)). Then log S₁ = ∫_0^∞ (e^{u/2}−1)² e^{−su} du/u (Frullani), density ≥ 0.
Put ζ₀^K := ζ · S₁^K · P₀/P. There is K = K(A,B) < ∞ such that:
 (i) dΠ₀^K = Σ(Λ/log n)δ_{log n} + [K(e^{u/2}−1)² + λ(u)] du/u ≥ 0, supported in (0,∞);
 (ii) dN₀^K = exp_*(dΠ₀^K) ≥ 0: (dΠ₀^K, dN₀^K) is a genuine Beurling system;
 (iii) π^{−s/2}Γ(s/2)ζ₀^K satisfies ζ's functional equation (symmetric rational factor);
 (iv) every zero of ζ₀^K in 0<Re s<1 lies on Re s=½ (ζ's on-line zeros, B, and s=½ of order 2K); poles at s=1 (order K+1) and s=0.
Proof of (i). λ(0)=0; λ′(0)=ΣA−ΣB=0 (both 2m by symmetry), so |λ(u)| ≤ C u² near 0, and |λ(u)| ≤ 8m e^{(½+β*)u}.
(e^{u/2}−1)² ~ u²/4 at 0 and ~ e^u at ∞ with β*<½, so sup_u |λ(u)|/(e^{u/2}−1)² =: K₀ < ∞; take K ≥ K₀. (ii) exp_* of a
positive measure; convergence for Re s>1 since every exponent has real part < 1 except the K+1 pole at 1. ∎
Consequence: under H(m) there is a genuine Beurling system, with ζ's own prime atoms, ζ's FE, all strip zeros on the line,
differing from ζ by a symmetric rational factor. The same K-trick with B:=∅, A:=∅ gives the unconditional system
ζ·S₁^K. So "ζ × rational" does **not** force a sign violation once one is allowed a higher pole at 1; and with the pole
order fixed (strict class) the violation of Thm A is the deleted zeros themselves.

## 5. Logic check (item (3) of the brief) and what would give C_B
- No contradiction can arise from ζ₀: it is auxiliary, and nothing forces dΠ₀ ≥ 0. Thm A is "deleted zeros produce a
  signed density" (tautological); Thm B shows the sign can always be repaired by a symmetric factor that does not touch ζ.
- To get C_B one would need a theorem of the form: *a genuine Beurling system whose prime measure is (atoms on {log n})
  + (finite exponential-polynomial)/u, with ζ's FE, simple pole at 1 and all zeros real, has zero continuous part.*
  Thm A proves exactly this in the strict class — but its hypothesis "dΠ₀ ≥ 0" is never supplied by ζ; demanding it is
  demanding that the removed zeros' density be ≥ 0, which is false iff m ≥ 1, i.e. it is H(m) ⇒ ¬H(m) only after assuming
  what is to be proved. Forcing positivity would need an input on ζ's primes of size x^{½+β*} (E1/W1).
- Pole-order constraint as the "forcing" property: vacuous, since the simple pole at 1 is part of the hypothesis of the
  strict class and Thm A already shows its failure is the explicit-formula oscillation; no new constraint on m.
- Remaining separator between ζ₀^K and ζ: dN₀^K has a nonzero a.c. part (non-integrality), cf. 2801 Lemma 2. That is
  O2601.1 (individual Euler/integrality property), not a positivity property.

## Verdict
**NO-GO (PROVED).** Props 1–2 (explicit dΠ₀, dN₀; off-line zeros cancel in dN₀ at leading order via ζ(a)=0) PROVED-TOOL.
Thm A: strict class dΠ₀ ≥ 0 fails ∀m≥1 — equals the 2β* oscillation law (E1/W6 content, no new information).
Thm B: with S₁^K, positivity of dΠ₀ and dN₀ + FE + all zeros on the line holds — positivity is never forced.
O2801.1 closed negative; the only surviving discriminator is integrality/atomicity of dN (O2601.1). check wanted
on: Prop 2 constant (Σc_a=0 ⇒ ½−{x} term vanishes), Thm B K₀<∞ near u=0 (needs λ′(0)=0).
