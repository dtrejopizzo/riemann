# An explicit formula for the trace on semilocal idele class groups

The paper evaluates the functional `T` of [Paper 43](../43-row-a-torsion-theory/) on the radial
functions `Γ_h(w) = h(−log|w|_S)`, using the radial family of
[Paper 44](../44-row-b-arithmetic-family/). For the limit `T_lim` of `T` over `S` it proves

    T_lim(Γ_h) = Φ_h(0) + Φ_h(1) − Σ_ρ Φ_h(ρ),      Φ_h(s) = ∫ h(t) e^{(s−1/2)t} dt,

where `ρ` runs over the zeros of the completed zeta function. This is Weil's explicit formula; a
proof in this normalization is included. The paper also

- gives the corresponding identity for the Hermitian form, for complex test functions, and shows
  that the formula fixes the constant at the identity;
- writes `T_lim(Γ_h)`, for even `h`, as a contour integral against an explicit function and as a
  sum of residues;
- recalls, with a proof in this notation, the known form of Weil's criterion (Yoshida;
  Connes–Consani): if the completed zeta function has a zero off the critical line, there are real
  primitive test functions, even and odd, on which the form is positive; such functions cannot
  have small support;
- proves that the form is nondegenerate on radial functions for each finite `S`;
- describes the radical of the form in the limit over `S` and proves that it is zero. The key
  statement, that no nonzero `Φ_h` vanishes at all zeros, is known (Yoshida); what is proved here
  is the reduction to it in the presence of the polar term.

Nothing in the paper depends on the Riemann hypothesis, and nothing in it gives information on
the location of the zeros.

- Source: [`main.tex`](main.tex)
- PDF: [`explicit-formula-trace-idele-class-group.pdf`](explicit-formula-trace-idele-class-group.pdf) (23 pages)
