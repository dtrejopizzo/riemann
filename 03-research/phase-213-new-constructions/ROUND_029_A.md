# The plateau line as a global criterion

**Cross-check.** P45 thm:sufficiency and P46 thm:parityschur distinguish global parity from that of a fixed window. P46 thm:oneprofile fixes a profile and requires all translation matrices. Here the profile varies, but a single plateau is evaluated per pair of data and the signed exponential defect of 027 may be discarded. The additional step relative to 027 is to build a violation of the line from any negative direction using the remote crossing of 028. It is not claimed that the line inequality is proved.

Fix any width threshold R≥0 and any ratio L≥1, finite. Take all real even smooth compactly supported primitive profiles F of mass M=∫F≠0 and all D>max(R,L·diam supp F). Write H_D=1_[−D/2,D/2]*F, b=m^sharp(0), C_F as in 027 and Φ(H_D) for the arithmetic fluctuation of P46 prop:sharp. The global sign is equivalent to

    Φ(H_D) ≤ b M² D + C_F     for all such pairs (F,D).

By homogeneity one can fix M=1. F is not prescribed to be positive. Each H_D is even and primitive, with a central plateau of height M. On a common window P46 gives a(H_D)=a^sharp(H_D)−Φ(H_D). The translation that centres the box does not change these forms. By 027 the difference between the line and a^sharp is

    S_D(F)=Σ_{k≥1} exp(−2a_kD) |∫F(t)exp(2a_kt)dt|²/(2a_k²),   a_k=k+1/4.

Thus line−Φ=a(H_D)+S_D(F). Positivity implies the inequality.

Conversely, if there is a negative test, 028 gives a real odd primitive smooth compactly supported G with q=a(G)<0. For that G there are D_j→∞ with a(G,V_{D_j}G)→0. Let F₀=G', even, of zero mass, with zero moments by parts. Its plateau is exactly G(t+D/2)−G(t−D/2); along D_j its energy tends to 2q. The identity of 027 is valid for F₀ since its derivation does not divide by M. In particular S_D(F₀)→0: for support within [−w/2,w/2], each summand is bounded by ||F₀||₁² exp(−2a_k(D−w))/(2a_k²). Consequently for large j line−Φ, evaluated at F₀, is strictly negative, even after discarding the whole defect.

Choose a smooth even bump ψ of positive integral and K=(1/4−∂²)ψ. It is primitive and has mass (∫ψ)/4. Fix j sufficiently large to exceed R and L times the diameter of an interval containing both supports. For D=D_j and F=F₀+εK, a(H_D) is a quadratic polynomial in ε. S_D(F) is also continuous in ε by the previous summable majorization on the common support. For nonzero ε sufficiently small the strict violation persists and M≠0. Normalizing the mass preserves the sign of the difference. This proves the converse. The perturbation may depend on D_j: the proof does not produce a single profile of nonzero mass with violations at unbounded widths.

By the same argument, positivity on all the indicated plateaus suffices for the global sign. The version with the line requires only the weaker majorant; the open obligation is to prove it uniformly in the allowed profile. PROVED after independent mathematical audit.
