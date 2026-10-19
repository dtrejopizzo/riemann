# Paper 21 — An exact information barrier in the ω-class: the unique RH-sensitive window and the impossibility of algebraic cancellation

The paper studies the arithmetic functions q^{ω(n)}, q = k² > 0, whose Dirichlet series factor as ζ(s)^q G_q(s). Because the zeros of ζ appear as zeros, not poles, the partial sums M_k(N) are monotone and carry no oscillatory terms. The paper proves that the only zero-sensitive observable in this class is the convergence rate of the normalized shifted correlation C_k(h,N)/M_k(N)² to an explicit Euler product, gives an explicit error formula with a strictly positive arithmetic coefficient, and shows that no positive combination of ω-class correlations can cancel the zero contribution. Nothing depends on or proves RH.

## Main results
- (L1): G_q holomorphic and non-vanishing in Re s > ½ (Selberg–Delange, CITED). PROVED.
- Monotonicity of M_k(N), no N^{ρ−1} terms. PROVED.
- `thm:LD` (T2): Poisson large-deviation rate for ω(n); no zero enters at any finite order. PROVED.
- `prop:limit`: C_k(h,N)/M_k(N)² → r_q(h), an explicit Euler product. PROVED.
- `thm:error` (T4): explicit error formula with coefficient A_q(h) > 0. PROVED.
- `thm:rh` (T4.1): RH ⟺ the convergence rate is O(N^{−1/2+ε}) for all h, q. PROVED (equivalence).
- `thm:impossible` (T5): impossibility of algebraic cancellation, A_{q₁…q_r}(h₁…h_r) > 0. PROVED.
- `prop:ratio`: M_k/M_1^{k²} = C_q + O(1/log N). PROVED.
- `thm:barrier` (Information barrier): the ω-class has exactly one zero-sensitive window. PROVED; NO-GO for the ω-class as a route.

## Files
- `main.tex`, `main.pdf` — source and compiled paper.
