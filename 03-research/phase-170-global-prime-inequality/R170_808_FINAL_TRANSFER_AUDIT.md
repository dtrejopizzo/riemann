# R170_808 — Final audit of the transport and indispensable reserve

Audit following the R170_806 construction; see
also the independent verification R170_807. No global positivity is
obtained, and the Three Gates induction is not accepted.

## Audited identity

In Paper 46 notation, K(v)=2 exp(−v/2)/(1−exp(−2v)).
For L=2T, U F(x)=√L F(L(x−1/2)), we set

    q_L(v)=L K(Lv)−1/v,       q_L(0)=L/2,
    H_L(x,y)=q_L(|x−y|)/2,
    a_L=γ_E+log(2πL).

The archimedean term is exactly b−a_L I−H_L. We checked:

1. The factor 1/2 of the H_L kernel and the diagonal value L/4 of
   R170_806.
2. The constant via lim(z→0)[∫_z^∞ K(v)dv+log z]=log4+π/2,
   together with m(0)=−γ_E−π/2−3log2−logπ.
3. The prime distances log n/L and their coefficients Λ(n)/√n.
4. The factor √L in each polar vector: the complete term preserves
   2|⟨f,c_L⟩|²−2|⟨f,s_L⟩|².
5. The matching of the energy domains, since H_L and the shift are
   bounded for each fixed L. No uniform bound in L is claimed for
   their norms.

The identity uses exclusively the kernel formula already present in
Paper 46. The validity of this transport does not depend on the global
closure claimed by the Three Gates manuscript.

## Independent diagnostic via autocorrelation

`python3 verify_archimedean_transfer.py` directly compares

    m(0)||f||² + ∫_0^1 L K(Lv)(||f||²−Re c_f(v))dv
                    + ||f||² ∫_L^∞ K(v)dv

with b[f]−a_L||f||²−∫_0^1 q_L(v) Re c_f(v)dv. The first expression does
not use the transfer. The matrix of b is integrated analytically over
normalized indicators; the other integrals are evaluated by quadrature
at 45 digits, subdividing at the autocorrelation nodes.

Eight cases, two data (one complex), and L=0.5, approximately log5, 4,
12, gave absolute errors smaller than 9·10⁻⁴⁴. This checks
normalizations and signs in examples; it does not replace the proof
nor certify positivity.

## Additional result: the entire reserve cannot be spent

The R170_806 warning admits a precise statement. Let S be the windows
of R170_805 and R_S=r−P_S≥0. Define the relaxation that discards R_S:

    W_rel[f]=l₀[f]+P_S[f]−a_L||f||²−⟨H_Lf,f⟩−⟨J_Lf,f⟩
                  +2|⟨f,c_L⟩|²−2|⟨f,s_L⟩|².

Suppose S^c contains an open interval. If

    L > L_* := exp(log2+1/2−γ_E)/(2π) ≈ 0.29465634,

then

    inf {W_rel[f] : f|S=0, f of finite energy} = −∞.       (A)

**Proof.** Choose an interval J contained in S^c of length less than
log2/L. Take an orthonormal sequence f_j supported on J with finite
energy; the normalized sines of J extended by zero work. Every prime
shift has length at least log2/L, so ⟨J_L f_j,f_j⟩=0 exactly. Also
P_S[f_j]=0.

The sequence converges weakly to zero. Since H_L is compact, its
quadratic value tends to zero. The same happens with the two polar
terms and with |∫f_j|², which come from finite-rank operators. With
β=log2+1/2, we get

    W_rel[f_j] → β−a_L < 0.

Hence there exists a j with negative value. Multiplying that f_j by an
arbitrarily large constant keeps f|S=0 and proves (A).

At L=log5 the limit is approximately −1.69783. This is not a value of
W_T, nor does it contradict its certificate: it corresponds to a
relaxation that removed the positive reserve R_S. No limit was swapped
with an assumed positivity of the original operator.

## Decision for the construction

The exact transport (1)–(3) of R170_806 is accepted. That concrete
identification step of the archimedean block with b and its explicit
remainder is thereby resolved. The identification of every intermediate
Three Gates model, and its induction, is not resolved.

Minimizing W_rel as if it preserved a positive complement is not
accepted: (A) shows an obstruction even with prescribed datum zero. The
next step must retain enough R_S in the eliminated block and control
the arithmetic coupling in its inverse metric. The window budget alone
does not provide that control. This is a proved restriction on the
construction, not a claim that other routes are impossible.
