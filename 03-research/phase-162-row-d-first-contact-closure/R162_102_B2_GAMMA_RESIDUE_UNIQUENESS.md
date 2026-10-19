# R162_102 — B2: Gamma-residue uniqueness of the homogeneous mode

Note, round 1, mechanism B2.

**Status: NO-GO (as an independent closing mechanism).** Three statements are proved below. (1) Germ-level
uniqueness holds and needs no arithmetic: it is equivalent to Gate 1 and gives no leverage on it. (2) A
nonzero interior homogeneous mode exists in the Davenport–Heilbronn model. (3) The whole B2 chain uses no
Euler product, so Λ*1=log can enter only through the unproved (PC)→scattering passage (L161.8), which is
already the terminal gate.

Sources: R161_017 (defect identity (2.3), interior value (4.3)), R161_019 (pole lattice, moment
completeness Thm 3.1), R161_025 (residue (0.1), faithful energy Thm 3.1), Paper 47 §sec:firstcontact,
phase 121 (README l.59; OPTION_MATRIX rows "Tate-port opposite parity", "equality-state annular
transport").

## 0. Two different "homogeneous" statements

These two statements are often run together, and they must be kept apart.

* **(H-germ)** The global meromorphic germ vanishes: W^0_ε ≡ 0, where
  W^0_ε(s) = d_Γ(s)K_F(s−½) − Q_+ − Q_− − Θ_+ − Θ_− (R161_017 (4.2)).
* **(H-int)** Only the interior restriction vanishes: (W^0_ε)^∨|_{(−T,T)} = r_ε = 0. Equivalently
  (D_Γ−B_+−B_−)F = 0 on I_T (R161_017 (5.3)). This is the phase-121 "homogeneous zero mode": a
  primitive F with 𝔞_T(F,G)=0 for **all** G in the full form domain, not only primitive G.

(H-germ) implies (H-int), because the Θ_± are supported in the exterior and so do not change the
interior restriction. The converse does not hold.

## 1. Germ level: uniqueness is trivial, and the vanishing is equivalent to Gate 1

**Proposition 1.1 (PROVED).** Let F∈L²(I_T), and let W^0_ε be built from F by the canonical,
F-linear construction of R161_017 §§3–4. The following are equivalent:
(a) W^0_ε ≡ 0; (b) K_F(a_m)=0 for all m≥1, a_m=2m+½, i.e. R_L F=0; (c) D_T^pole(F)=0; (d) F=0.

*Proof.* (a)⇒(b): by R161_025 (1.4), Res_{s=2m+1}W^0_ε = K_F(a_m). This uses Res d_Γ = 1 and the
holomorphy of Q_±, Θ_± at s=2m+1. (b)⇔(c)⇔(d): R161_019 Thm 3.1 and R161_025 Thm 3.1.
(d)⇒(a): Q_± and Θ_± are linear in F. ∎

**Corollary 1.2.** For every first-contact vector (which is nonzero by definition), W^0_ε ≢ 0, and it
has a genuine pole at some s=2m+1. The question "must W^0_ε vanish for a first-contact vector?" is
therefore exactly the question "does a first-contact vector exist?", which is Gate 1 itself.

This is the "equivalence" branch of the task, and it is stronger than stated. Homogeneous uniqueness
at the germ level is a *theorem*, and it holds for every F. It carries no information, because it
never uses first contact, λ=0, T_*, orientation, or Λ. The non-trivial content lies entirely in
*producing* W^0_ε=0 from (PC). That is the physical scattering theorem of R161_017 §6 / L161.8, which
the linear limit cannot supply (R161_018, F4).

In particular, the remark in R161_019 §5 ("no separate homogeneous zero mode after the product-range
condition is retained") is correct but empty. The product range excludes the homogeneous germ only
because it excludes every nonzero germ.

## 2. Interior level: a genuine nonzero homogeneous mode in a model

**Proposition 2.1 (PROVED modulo the standard facts listed).** Take L = the Davenport–Heilbronn
function. It has a degree-1 functional equation with Gamma factor Γ((s+κ)/2), it is entire, it has
no Euler product, and it has zeros off the critical line. Build its truncated Weil form 𝔞^{DH}_T
(archimedean multiplier from its Gamma factor, and comb coefficients c(n) of −L'/L). Then there are
T_*<∞ and a nonzero parity F∈L²(I_{T_*}) with 𝔞^{DH}_{T_*}≥0 and 𝔞^{DH}_{T_*}(F,G)=0 for all G. In
other words, (H-int) has a nonzero solution.

*Proof.*
1. L is entire, so the explicit formula has no polar term. The Tate space is therefore absent, the
   primitive and complete forms coincide, and every radical vector is automatically interior
   homogeneous (r≡0).
2. By Weil's criterion, which uses only the explicit formula and so holds for DH, an off-line zero
   gives a test on which the form is negative. Density of compactly supported tests then gives
   λ^{DH}(T_0)<0 for some finite T_0.
3. λ^{DH}(T)→+∞ as T→0. On I_T the comb is empty for 2T<log 2. The multiplier behaves like
   log(2+|τ|), and its compression to I_T has bottom ≥ log(1/T)−O(1).
4. The proof of Paper 47 lem:contT uses only the archimedean and comb bounds of lem:mbounds, and
   these hold for any finite coefficient list. It therefore gives continuity. Monotonicity also
   holds, by zero-extension.
5. Compact resolvent holds as in thm:O.

Take T_* = inf{T: λ^{DH}(T)<0}. Then λ^{DH}(T_*)=0 is attained. The kernel is J-invariant, so it
contains a parity vector. ∎

**Consequence.** Uniqueness of the interior homogeneous mode is false once the Euler product is
dropped, even with the functional equation, the Gamma factor, and the full Gamma-pole lattice kept.
By Prop. 1.1, which applies verbatim with the lattice a_m=2m+½+κ, this DH mode also has
R_L F ≠ 0 and W^0 ≢ 0. So a proof of either (H-int)-uniqueness or W^0=0 must use (a) the pole of ζ
at s=1 (the Tate space), or (b) the Euler product, at the step that forces vanishing.

For ζ itself, (H-int)-uniqueness remains open, as recorded in phase 121. It is also strictly weaker
than Gate 1. An (H-int) mode is a radical vector with r=0, so excluding (H-int) modes removes only the
r=0 part of the radical. Gate 1 must also handle radical vectors with r≠0 in the Tate space.

## 3. Where Λ*1=log can and cannot enter

**Proposition 3.1 (PROVED; structural).** Three identities are formal consequences of
L(s)=χ(s)L(1−s) and the choice of Gamma factor alone:
* the scattering defect identity G_++χG_− = L(s)·W_ε (R161_017 (2.3));
* the interior identification (4.3);
* the residue formula R161_025 (0.1), with ζ(2m+1) replaced by L(2m+1).

The completeness theorem (R161_019 Thm 3.1) is pure analysis. None of these uses the Euler product
or Λ*1=log.

*Proof.* Inspect the derivations. (2.1)–(2.4) differentiate the functional equation. Division by L is
licit in any zero-free right half-plane, and every absolutely convergent Dirichlet series with
L(σ)→1 has one. ∎

Hence, in the task's hint, the ζ in "G_+ + χG_− = ζ[…]" is multiplicative only as the functional
equation's L(s), and this holds for DH and Epstein just as for ζ. The Euler product does not act
through that factor. The only place in the B2 chain where Λ*1=log is used is Paper 47
thm:PCfinite (hyperbola cancellation at k≤N). That feeds the unproved (PC)→scattering passage.

## 4. Falsifier tests

* **F1 (spectral).** Props. 1.1 and 3.1 are equivalences or identities valid for every F, so they
  prove no falsehood. For the same reason they cannot close Gate 1. B2 gives no statement that
  distinguishes λ=0 from λ>0. Any "W^0=0" derived without λ=0 and minimality would contradict
  Prop. 1.1 on eigenvectors with λ>0. **Passes, and inert.**
* **F2 (orientation).** B2 gives no quadratic estimate. R161_025 §2 already shows that the two
  oriented residues cancel in the completed current, so extracting one orientation is exactly the
  missing input. **Not addressed; the gap is the same.**
* **F3 (arithmetic).** DH (Prop. 2.1) exhibits an actual first-contact / interior-homogeneous vector
  with W^0≢0. This shows that "first contact ⇒ W^0=0" is false without the Euler product.
  - **Epstein.** The pole at s=1 is present and the Gamma factor is Γ(s), so the lattice is
    s=1,2,3,… and is still complete. The same argument applies once the continuity of λ_A from
    R162_001 is transplanted, and it is local-analytic. So Epstein first-contact vectors exist when
    the form has off-line zeros.
  - **Modified coefficients a≠Λ** (thm:finmod). Those models also carry negative directions. Their
    first-contact vectors have W^0≢0 by Prop. 1.1.

  Every step of B2 proper holds in all three models. **B2 fails F3 in the strong sense:** it has no
  step that could distinguish ζ, so it cannot be the vanishing step.
* **F4 (linear limit).** Consistent with R161_018. B2 needs W^0=0 as a *germ*, and the linear limit
  gives only the tautological completed commutator.

## 5. What survives

* Prop. 1.1 is the clean reformulation Gate 1 ⟺ "(PC-ren) forces the Gamma-residue germ of
  W^0_ε to vanish at one orientation". This is L161.8 with the residue normalization made exact.
* The DH model gives a concrete, well-posed falsifier for any future (H-int) argument. Such an
  argument must use the pole/Tate space or the Euler product at the step that forces vanishing.
* Open for ζ: (H-int)-uniqueness, which is weaker than Gate 1. Gate 1 itself also remains open.

**Status: NO-GO for B2 as a closing mechanism.** Germ-level uniqueness is PROVED (trivial and
Euler-free). Interior-level uniqueness is FALSE in the DH model and OPEN for ζ. The vanishing of
W^0_ε at first contact is EQUIVALENT to Gate 1.
