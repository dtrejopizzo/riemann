# Recovery of the full energy by two remote correctors

**Cross-check.** 012-B evaluates the return of a tail to a head of zero inverse moment. P46 lem:polarelim and rem:polarelim-full make the polar terms explicit. The cross-check with P45, P46, R160 and the moment correctors of 211/212 distinguished the scope of a test-by-test approximation. The operation is to compensate both moments at opposite ends and retain the crossing of the correctors with each other. The global sufficiency of the primitive sector was already established in the corpus.

**Statement.** Let F be a smooth compactly supported complex test in the logarithmic variable t. Write A(F)=∫exp(t/2)F(t)dt, B(F)=∫exp(−t/2)F(t)dt, and a for the pole-free energy with all contacts visible in the support. There are smooth compactly supported tests F_s with moments A=B=0 such that ||F_s−F||₂→0 and

    a(F_s) → W(F)=a(F)+2 Re(conjugate(B(F)) A(F)).

The windows of the approximants may grow. The indicated convergence concerns the L² distance and the energy values. Continuity of the full energy in L² is not presupposed.

**Computation of a remote crossing.** Let L=Ul and R=Ur be two smooth compactly supported profiles in the logarithmic variable, Uf(t)=exp(t/2)f(exp t). For a distance s→∞ only one of the two directions of contact between L and V_s R can contribute. In the polarized energy, with the antilinear-on-the-left convention, the archimedean crossing is O(1) by Cauchy–Schwarz with weight |m|. For the comb, multiplying the crossing by exp(−s/2) and putting K=exp(s), the expression being subtracted is

    K⁻¹ Σ_n Λ(n) φ(n/K),    φ(v)=∫conjugate(l(x)) r(vx)dx.

Indeed the physical profile of V_s R is K^(−1/2)r(x/K). The correlation gives a factor √n that cancels the denominator of the weight. The sum is for a single direction in the polarized form, with factor two when taking the full real crossing. The function φ is smooth with compact support in (0,∞). PNT in quadrature form and Fubini give ∫φ=conjugate(B(L))A(R). Hence

    exp(−s/2) a(L,V_s R) → −conjugate(B(L)) A(R).

**Two correctors.** Choose smooth profiles P,Q with A(P)=−A(F), B(P)=0 and B(Q)=−B(F), A(Q)=0. They exist because the two functionals are independent on smooth compactly supported tests (two distinct translations of a positive bump give an invertible moment matrix). Take

    F_s=F+exp(−s/2)(V_s P+V_(−s) Q).

The laws A(V_s P)=exp(s/2)A(P) and B(V_s P)=exp(−s/2)B(P) give exactly the two zero moments. The L² distance tends to zero by the isometry of translation, and the two added self-energies are O(exp(−s)). In spatial order Q,F,P, the mixed contributions to the limit are minus twice the real part of the sum

    conjugate(B(Q)) A(F) + conjugate(B(F)) A(P) + conjugate(B(Q)) A(P).

For the last term, translate jointly by s and apply the previous computation with distance 2s: exp(−s) is precisely the critical factor. Substituting the moments of P,Q, the sum equals −conjugate(B(F))A(F). This proves the formula.

**Consequence.** On the union of windows, the infimum of W(F)/||F||² over nonzero smooth compactly supported tests coincides with that of a over primitive smooth compactly supported tests with the same normalization. One direction follows by inclusion and the other by the previous approximation. A test with W(F)<0 would produce primitive tests of negative energy. The argument fixes how an energy value is transported and leaves pending the global inequality that would sign it. PROVED after independent mathematical audit.
