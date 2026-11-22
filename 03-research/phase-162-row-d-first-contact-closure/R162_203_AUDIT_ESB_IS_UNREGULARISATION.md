# R162_203 — Audit of R162_201/202: ESB is the removal of the product regularisation

Status: **AUDIT. Both notes are correct as stated; ESB is not a weaker intermediate
statement. It is equivalent to the conclusion F=0 through an explicit identity.**

## 1. Checks passed

- R162_201 Thm 2.1: weak compactness in H²(C_+), continuity of point evaluation, Euler convergence in
  Re z>1/2, and the boundary growth bound |h(x+iy)|≤Cx^{-1/2}‖h‖ are used correctly; m−k≥1 beats
  x^{-1/2}. The last step needs (a) a positive proportion of simple zeros on the line (Levinson,
  Conrey), which gives ≫T log T simple ordinates up to T, and (b) Cartwright/Jensen: an entire K_F
  of exponential type has O(T) zeros in |z|≤T. Both are standard; cite them explicitly.
- R162_201 (3.2) and R162_202 Thm 3.1: correct. P_T U_{-a}|_{H_T}=S_a^*, C_log U_a=U_{-a}C_log
  (with the half-density built into U), unitarity of C_log, orthogonal split at T.

## 2. What ESB is, exactly

By R161_007 (1.2), the corrected port is the product regularisation

    G_{+,T}F = ζ(½+z) H_{+,T}F,     H_{+,T}F = −(ζ'/ζ)(½+z) K_F(z) − Q_{+,T}(z),  Q entire.   (2.1)

Theorem 2.1 of R162_201 shows ESB ⇒ ĝ/ζ(½+z) ∈ H²(C_+), i.e. by (2.1)

    ESB  ⇒  e^{Tz} H_{+,T}F ∈ H²(C_+).                                                   (2.2)

But H_{+,T}F has, at a zero ρ of multiplicity m, a pole with residue −m K_F(ρ−½), because Q is
entire. Hence e^{Tz}H_{+,T}F∈H² already says K_F vanishes at every zero, i.e. F=0. So:

**Proposition 2.1.** Within the first-contact class, ESB ⟹ [H_{+,T}F is pole-free] ⟺ F=0, and F=0 ⟹ ESB
trivially. ESB is therefore equivalent to the conclusion; the Euler stripping A_Y ĝ → ĝ/ζ undoes the
multiplication by ζ that produced G from H in R161_007.

This is the same structure as the return inequality (R162 README): not circular as a proof strategy,
but no weakening. Whatever proves ESB proves directly that the unregularised oriented current has no
critical poles.

## 3. The quantitative form of ESB

On the boundary, ‖A_P ĝ‖²_{H²} = (1/2π)∫ |ĝ(iτ)|² |ζ_P(½+iτ)|^{-2} dτ, ζ_P the partial Euler product
over p∈P. So

    ESB ⟺ sup_P ∫_R |ĝ(iτ)|² |ζ_P(½+iτ)|^{-2} dτ < ∞.                                        (3.1)

Heuristic scale: by Bohr's independence of (p^{-iτ})_p, the τ-mean of |1−p^{-1/2-iτ}|² is 1+1/p, so the
mean of |ζ_P|^{-2} grows like ∏_{p∈P}(1+1/p) ≍ log max P. ESB requires |ĝ|² to vanish at the zeros
strongly enough to beat a logarithmically growing negative moment of partial Euler products on the
critical line. This is the analytic content any PC-ren derivation must reproduce.

## 4. Consequence for the next step

The multiprime leakage identity (R162_202) is correct and keeps all divisor terms, but (5.2) there is
an exact rewriting of (3.1), so a PC-ren upper bound for (5.2) is equivalent to (3.1). The honest
target should be stated directly as:

> derive from first contact + PC-ren that the oriented current H_{+,T}F has zero residue at critical
> zeros, i.e. K_F(ρ−½)=0,

with (3.1) as one possible quantitative route. Test for any candidate derivation: it must fail if ζ_P
is replaced by the partial products of a finite modification a of Λ (thm:finmod of Paper 46), and it
must not apply to Davenport–Heilbronn (R162_102 Prop 2.1).

Status: R162_201 Thm 2.1 PROVED; R162_202 Thm 3.1 PROVED; ESB ⟺ F=0 within the first-contact class
(Prop 2.1); Gate 1 OPEN; row D OPEN.
