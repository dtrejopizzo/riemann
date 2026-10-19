# R162_1202 — Round 12: odd-degree and self-referential functionals of the first-contact vector — **NO-GO (PROVED), plus a correction to the R162_1101 residual**

Round 12. Inputs: README (F1–F4, rounds 1–11), R162_590, R162_1101 (Thms 2.1, 2.2, 5.1,
residual), R162_903 (Thm 5.1, tensor lift), R162_205/206 (exterior correlation, one-dimensional linear content), R162_402
(port, (1.1)), R162_405/408 (collar), R162_1004 (tensor power). Pure mathematics; no numerics.

Conventions. H = H_{T_*} is self-adjoint on P = L²(I_{T_*}) (parity sector) with H ≥ 0, and F is in N = ker H, F ≠ 0
(first contact, λ_A(T_*) = 0, T_* minimal). Q(h) = ⟨h,Hh⟩ and B(g,h) = ⟨g,Hh⟩. e_m ∈ P is the Gamma-lattice vector,
so that K_F(a_m) = ⟨F,e_m⟩ (plus the Q_+ history term, as in R162_1101 Thm 5.1(i)). Gate 1 is ℓ_m(F) := ⟨F,e_m⟩ = 0
for m ≤ L. The additive self-convolution is F*F. In log coordinates, Mellin convolution is additive convolution, so both
readings in the task are covered by one symbol. Its support is I_{2T_*}, and its compression is P_T(F*F).

**Status.** I built and tested four families of odd-degree or self-referential functionals: (i) nonlinear variations of
λ through F, (ii) polynomial identities that follow from HF = 0, (iii) cubic Weil tests such as W[c_F * F] and
⟨F*F,HF⟩, and (iv) ports with F-dependent entire multipliers. None closes Gate 1. Labels:
- Thm A (flatness at contact: Q(F+h) = Q(h), so every odd-order variation of λ at F vanishes identically) PROVED.
- Thm B (parity obstruction: odd degree gives no sign, and odd degree with a normalisation is even degree) PROVED.
- Thm C (polynomial collapse: any identity ℓ_m·q ≡ ⟨HF, 𝔅(F)⟩ with q(F) ≠ 0 implies e_m ∈ ran H, i.e. the Sonin range
  statement (4.2) of R162_011; the degree plays no role) PROVED. **New.**
- Thm D (cubic Weil tests are exterior correlations with self-referential exterior vectors; they are odd in F and have
  no sign) PROVED.
- Prop E (the convolution-power port has residue ∝ K_F(a_m)³; F-dependent entire multipliers keep the pole on atom 0)
  PROVED.
- Prop H (the atom localisation in R162_1101 Thm 2.2 depends on the representation; the invariant is the residue
  *value*; the residual is restated) PROVED. **Correction to R162_1101 §7.**
Gate 1 OPEN. No label moves.

## 0. Corpus check

I grepped "cubic", "third variation", "odd degree", "self-convol", "convolution square" and "F*F" in phases 155–162.
The phase-155 hits concern kernel convolutions in the LP and decay scripts; none is a functional of the contact vector.
Related work already in the corpus: R162_903 Thm 5.1 (even degree 2d means quadratic on N^{⊗d}); R162_1004 (ζ^d
carries weights dΛ and the same T_*); R162_405–408 (right minimality, the collar); R162_205 (exterior correlation,
linear and sign-flipping). No prior file treats odd degree, the Rayleigh quotient along nonlinear curves, or
polynomial-ideal consequences of HF = 0.

## 1. Failing lines, stated first

Theorems A–C use exactly three inputs: H_{T_*} ≥ 0, HF = 0, and polynomial algebra in F. Theorem D adds the
explicit-formula form of W, and Proposition E adds the port of R162_402. Each model below has first contacts at its
own T_*, where the same three inputs hold.

| model | own first contact | inputs of A–C | inputs of D–E | where it fails |
|---|---|---|---|---|
| DH | yes, with R_LF ≠ 0 (R162_102) | hold | hold with −L'/L | any Gate-1 conclusion from A–E would be false for DH; A–E give only the range restatement, which is consistent |
| deletion Λ1_{n≥5}, κ | yes, T_W ≤ 0.4608 (R162_703, 702) | hold | hold; the weights enter only through H (linear) | the same |
| Λχ₂ | yes (R162_502 B3) | hold | hold; the lattice moves to the trivial zeros of L(s,χ) | the same |
| Beurling DMV | yes (off-line zeros) | hold | hold; atom 0 = identity | the same |
| ζ | — | hold | hold | reduces to e_m ∈ ran H (Thm C), i.e. to Gate 1 |

In every model, the tools of this memo reach one of two ends: (a) the positivity H ≥ 0 applied to some vector, or
(b) the range statement e_m ∈ ran H. Neither end separates ζ from DH.

## 2. Nonlinear variations of λ at the contact

**Theorem A (flatness).** (a) For every h ∈ P, Q(F+h) = Q(h).
(b) Let F_ε be any curve in P with F_0 = F, and put h(ε) = F_ε − F. Then λ-type quantities along the curve are
Q(F_ε) = Q(h(ε)) ≥ 0. Every odd-order Taylor coefficient of ε ↦ Q(F_ε) is a sum of terms B(h_i,h_j) with
i + j odd. These terms are bounded by Cauchy–Schwarz through the even-order terms Q(h_i), and they never contain F.
(c) Along great circles γ(ε) = cos ε·F + sin ε·G, with G ⊥ F and ‖F‖ = ‖G‖ = 1, the Rayleigh quotient is exactly
sin²ε·Q(G). All odd derivatives vanish, and the Morse index at F is 0 with nullity dim N.
(d) Take the curve F + εF*F. It is admissible for the minimality of λ at T_* only after compression,
F + ε P_T(F*F). The second-order condition is then Q(P_T(F*F)) ≥ 0, which is H ≥ 0 at one vector. On the
uncompressed curve inside L²(I_{2T_*}), the first variation is 2B_{2T_*}(F, F*F) = 2E(F,(F*F)_out) (see Thm D). No
minimality is available there, because T_* is the *first* contact and λ_A carries no sign past it.

*Proof.* (a) Q(F+h) = Q(F) + 2⟨h,HF⟩ + Q(h), and HF = 0. (b) Expand h(ε) = Σ ε^i h_i and use (a). For the
Cauchy–Schwarz bound, H ≥ 0 gives |B(g,h)|² ≤ Q(g)Q(h). (c) Q(γ) = cos²ε·Q(F) + 2 sinε cosε·B(F,G) + sin²ε·Q(G),
and the first two terms vanish. (d) Supports: F*F is supported in I_{2T_*}. The Rayleigh minimality holds only on P. ∎

**Reading.** At a zero of a nonnegative quadratic form, the form is flat in the direction of F: F drops out of every
variation. "Second variation along F ↦ F + εF*F" is H ≥ 0 at the vector P_T(F*F). That inequality is true in every
model at its own first contact. It carries no arithmetic information and no information about F beyond the choice of
vector. This is F1 in its sharpest form: minimality contributes nothing beyond HF = 0 and H ≥ 0.

## 3. Parity of degree

**Theorem B.** Let C be a real, continuous, homogeneous functional of odd degree on P.
(a) If C(F) ≥ 0 for every first-contact vector, then C = 0 on N. The reason is that −F is also a first-contact
vector and C(−F) = −C(F).
(b) Suppose the orientation is fixed by an F-free linear normalisation ν(F) > 0, for example ν = ⟨·,ψ_{T_*}⟩ or an
endpoint value. Then a conclusion "C(F) ≥ 0 when ν(F) > 0" is the even-degree conclusion ν(F)·C(F) ≥ 0. If C is built
from 𝒜_T, X̂, A^∞ and Tate data, the product νC falls under the tensor lift (R162_903 Thm 5.1) with one factor
replaced by the F-free vector.
*Proof.* (a) is immediate. (b) ν·C is homogeneous of even degree, and a product with an F-free linear form is a
mixed tensor pairing, which the lift covers (R162_903 §5, "symmetric mixed tensors"). ∎

**Degree in F versus degree in A_M.** F2 concerns the orientation A_M → −A_M of (PC), not the sign of F. A cubic in F
of the form ⟨HF, 𝔅(F,F)⟩ or B(g(F),h(F)) is *linear* in H, hence linear in A_M. It is therefore odd in A_M, but it
lies in the one-dimensional linear content of (PC) (R162_206), where R162_205 applies: the term is linear,
sign-flipping, and zero at Λ. A use of degree ≥ 3 in A_M needs products H·H. Every such product that touches F
vanishes, since HF = 0. The products that do not touch F are spectral data of H on non-kernel vectors. Those hold for
all F, so they fail F1. Odd degree in F therefore escapes the even-degree tensor lift (Thm 5.1 of R162_903) only
formally. It does not escape F2.

## 4. Polynomial consequences of λ = 0 (the decisive statement)

Call a continuous polynomial functional P *contact-derivable* if P(G) = ⟨HG, 𝔅(G)⟩ for all G ∈ P, for some continuous
polynomial map 𝔅: P → P. Such a P vanishes on N. The natural cubic candidates have this form: ⟨HF, F*F⟩ compressed,
⟨H'F, F·F⟩ with H' = ∂_T H evaluated at contact after the collar correction, and the second variation of λ along
F + εF*F.

**Theorem C (polynomial collapse).** Let dim N = 1 (primitive parity) and N = span F. Suppose there are a
contact-derivable P of any degree and a continuous polynomial q with q(F) ≠ 0 such that ℓ_m(G)·q(G) = P(G) for all G.
Then ℓ_m(F) = 0 and
    e_m = H 𝔅(F) / q(F) ∈ ran H.
Hence e_m ∈ ran H, which is the Sonin range statement (4.2) of R162_011: exactly what a linear test needs
(R162_1101 Thm 5.1(i)). The same holds with ℓ_m·q replaced by any polynomial whose restriction to the line F + εf
has an ε¹ coefficient of the form ℓ_m(f)·c + (terms vanishing at F).
*Proof.* Order ε⁰ at G = F: ℓ_m(F)q(F) = P(F) = 0, and q(F) ≠ 0. Order ε¹ at G = F + εf: the left side gives
ℓ_m(f)q(F) + ℓ_m(F)·Dq(F)f = ℓ_m(f)q(F). The right side gives ⟨εHf, 𝔅(F)⟩ + ⟨HF, ·⟩ = ε⟨f, H𝔅(F)⟩. Since f is
arbitrary, ⟨f,e_m⟩q(F) = ⟨f,H𝔅(F)⟩ for all f. ∎

**Reading.** From the equation HF = 0, every polynomial route of any degree, odd or even, to ℓ_m(F) = 0 contains its
own linear part. That linear part is the range statement. This is the algebraic form of "the vanishing ideal of N is
generated by linear forms": {⟨·,u⟩ : u ⊥ N} generates I(N), so the degree-1 part of I(N) decides membership of ℓ_m.
A self-referential kernel ψ_F = 𝔅(F) does appear, as the "kernel depending on F" asked for in R162_1101. Theorem C
shows that it must satisfy Hψ_F ∝ e_m. So the self-reference is used only at the single point F, and the question
stays linear.

## 5. Cubic Weil tests and the convolution-power port

**Theorem D (cubic tests = self-referential exterior correlations).** Let φ = c_F * F = F̃ * (F*F). φ has degree 3 and
support I_{3T_*}. Then
    W[φ] = B_{3T_*}(F, F*F) = ⟨P_T(F*F), HF⟩ + E(F, (F*F)_out) = E(F, (F*F)_out),
where E is the exterior correlation of R162_205 and (F*F)_out = (1−P_T)(F*F). The explicit-formula side is
Σ_ρ F̂(t_ρ)²F̂*(t_ρ). E is odd in F and linear in the exterior vector. Under η → −η it changes sign (R162_205). By
Thm B it has no sign. The vanishing E(F,G) = 0 for *all* exterior G is extendability, which R162_408 (NE) excludes
unless ξ_G = 0. For the single vector G = (F*F)_out, no equation of the contact forces vanishing.
*Proof.* Bilinearity of the window form, supp F ⊂ I_{T_*}, and HF = 0. The autocorrelation of a convolution is the
convolution of the autocorrelations. The explicit formula is applied to the test φ termwise. ∎

**Proposition E (convolution powers in the port).** For φ = F^{*j} * F̃^{*k}, K_φ(z) = K_F(z)^j K_F(−z)^k. With
primitive parity, K_F(−z) = ±K_F(z), so K_φ(a_m) = ±K_F(a_m)^{j+k}. The port of φ, −(ζ'/ζ)K_φ − Q_+^φ, has residue
∝ K_F(a_m)^{j+k} at s = −2m. So cubic port regularity is equivalent to Gate 1: it is the cube, no weaker and no
stronger. The kernel of the representation is K_{c_F}(z)^{…}·ζ(s)^{-1}N_s. The F-dependent factor is entire in s, so
by R162_1101 Thm 2.2 the polar part is again (entire multiplier) × δ_0^{(2m)}, supported on atom 0.
*Proof.* The Laplace transform turns convolution into a product, and parity gives the sign. Thm 2.2 applies to
ζ(s)^{-1}N_s, and multiplying by a function that is regular at −2m preserves the support of the polar coefficient. ∎

"The port of F evaluated with F itself as the test" means ∫ H_+(z)K_F(−z)dz along the critical line. That integral is
W[c_F] = Q(F) = 0, the contact equation itself (quadratic). Evaluating the port at an F-dependent point z(F) gives a
non-polynomial functional whose s-dependence still comes through ζ^{-1}·(entire). The pole therefore still sits on
atom 0.

## 6. Correction: atom localisation depends on the representation

**Proposition H.** Let w be finitely supported with Σ_d Λ(d)w(d) = 0, for example w(2) = log 3, w(3) = −log 2. Let
g^w_s be the kernel with u_{g^w_s}(d) = w(d)/(s+2m) (Thm 1.1 of R162_1101; g^w_s = (s+2m)^{-1}Σ_e ŵ-lift, a finite
combination of ν_e − Leb). Then g_s + K-multiple·g^w_s represents the same pairing with Φ_Λ. Its pole at s = −2m is
supported on the 2- and 3-torsion atoms as well as on 0. The residue value is unchanged.
*Proof.* ⟨Φ_Λ, g^w_s⟩ = (s+2m)^{-1}Σ Λ(d)w(d) = 0 identically. ν_2 and ν_3 charge 1/2, 1/3 and 2/3. ∎

So "the pole reads only atom 0" is a property of the *canonical* kernel g_s. It is not an invariant of the pairing. A
kernel "whose pole at −2m is not supported at 0" exists trivially. The null kernel even uses Λ-specific data: the
choice of w depends on log 2 and log 3. It still moves nothing. The invariant datum is the residue value −εK_F(a_m)
(R162_402). **Restated residual:** a closing argument needs a *second, independent evaluation* of that residue, one
that does not pass through ζ'/ζ·K_F, and that evaluation must return 0. Thm C shows that any polynomial second
evaluation built on HF = 0 is the range statement. Thm A shows that minimality contributes only H ≥ 0 at vectors.

## 7. F1–F4

- **F1.** A, B and D hold for all F, and C uses λ = 0 exactly through HF = 0. By Thm A the minimality of T_* adds
  nothing non-perturbative on the window. Passed only by restatement (C gives the range statement, E1).
- **F2.** Odd degree in F is linear in A_M (§3) and lies in the linear (PC) content of R162_205/206. Not passed.
- **F3.** A–C use only H ≥ 0 and HF = 0, which hold at the first contacts of DH, deletion/κ, Λχ₂ and Beurling (§1).
  D–E transport verbatim with the model's −L'/L. Prop H's null kernel is Λ-specific but invisible. Not passed.
- **F4.** No graph limit is taken, so F4 does not apply. The only limit object is the linear part in Thm C, which is
  the R161_018 situation.

## 8. Verdict

**NO-GO (PROVED).** At a first contact, the Weil form is flat along F (Thm A). Every nonlinear or self-referential
variation of λ, including F ↦ F + εF*F, gives only H ≥ 0 at some vector, and all odd-order terms vanish. A functional
of odd degree cannot carry a sign, because F and −F are both contact vectors, and fixing an orientation makes it
even (Thm B). From HF = 0, every polynomial identity of any degree that yields ℓ_m(F) = 0 contains the linear identity
e_m ∈ ran H (Thm C). Degree is therefore irrelevant, and the question collapses to the Sonin range (4.2). Cubic Weil
tests are self-referential exterior correlations, which are linear in (PC) and unsigned (Thm D). Convolution powers
turn Gate 1 into its own cube (Prop E). Separately, the "atom 0" localisation of R162_1101 is not an invariant: the
residual should be read as the need for an independent second evaluation of the residue −εK_F(a_m) (Prop H).

Add to R162_590 §1c: "odd-degree / self-referential functionals (nonlinear variation of λ, polynomial consequences
of HF = 0, cubic Weil tests, convolution-power ports) — R162_1202 — flatness at contact; odd degree gives no sign;
polynomial collapse to e_m ∈ ran H in any degree; cubic = exterior correlation; atom-0 localisation depends on the
representation | F1 (restatement), F2, F3".

Files edited: this file only.
