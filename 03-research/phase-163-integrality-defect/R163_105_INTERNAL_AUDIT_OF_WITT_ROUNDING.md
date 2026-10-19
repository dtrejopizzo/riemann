# R163_105 — Internal audit of R163_103 (for the panel)

**Internal verdict:** no logical gap was found in `R163_103`'s proof; external review is requested before incorporating it into paper 48. No closure of D is asserted.

## Five places where it could fail, and their check

1. **Weights of `dΠ` vs. prime multiplicities.** The rounding is applied to `w_{p,m}=(1/m)Σ_{d|m}μ(d)p^{am/d}`, not to `p^{ma}/m`. The identity `Σ_{m|k}m w_{p,m}=p^{ak}` checks the local product at every order `k`. If `dΠ`'s weights were rounded instead, the second-power error would have size `p^{2a}` and could cancel the sought-for zeros. This danger is avoided by Witt inversion.

2. **Local uniformity of the random logarithm.** For `σ>(1−θ)/2`, `Σ q_j^{-2σ}<∞`. On compact rectangles the linear series `Σ ε_jq_j^{-s}` is a martingale with summable squared Bergman-norm increments; it converges almost surely in that norm and, by interior evaluation, locally uniformly. Orders `k≥2` converge absolutely. Hence the correcting factor is `exp` of a holomorphic function and never vanishes. Convergence at an isolated `s` is not enough: the proof explicitly uses spaces of analytic functions.

3. **All convolution orders.** The variable `K_j` includes *every* power `q_j^k`, and `K_J=*K_j` includes every product across indices. The recursion for `C_{r,J}` does not truncate at order 2; it uses the zero mean solely to cancel the linear term at each step. The remaining cost is quadratic, `O(b_x(q_j)^2)`, and the mean starts at `q_j²`. This is the new point relative to `R163_101`'s partial computation.

4. **Residue and the infinite limit.** For θ>0, `Σ q_j^{-1}<∞`, so `ρ_B=(1−θ)∏(1−q_j^{-1})^{-ε_j}` converges absolutely and positively. For each `x`, the factors with `q_j>x` do not change `N_B(x)`; Fatou retains the moment bound for `N_B(x)−ρ_Bx`. The randomness of the residue is not replaced by its expectation.

5. **Uniformity in x.** An isolated second moment would not be enough. `R163_103` obtains moments of every integer order `r≥2`. On the dyadic mesh of step `X^{θ+ε}`, there are `O(X^{1−θ−ε})` points; Markov with `rε>1−θ` makes the probabilities over scales `X=2^n` summable. Monotonicity of the positive count interpolates. At `θ=1/3`, the factor `(log x)^{C_r}` does not change the conclusion `O(x^{1/3+ε})`.

## Check against prior results

- `R163_101` had only controlled orders 1 and 2 and called `C_{1/3}` a conjecture. `R163_103` supplies the missing recursion; if the panel accepts it, that status should be updated. Paper 48 was **not** modified this round.
- `R163_102` Thm T is not contradicted: its transfer region depends on deletions relative to ζ, while the Witt system is built from the extended zeta `Z_θ` with a global redistribution.
- The Hilberdink/Neamah theorem on the two largest exponents `≥1/2` is not contradicted either: the created zeros have `β=(1+θ)/2>1/2`, and the integer-error exponent is smaller.

## Open questions

- Is there a topological subtlety in passing from the Bergman martingale to a single global meromorphic continuation that requires spelling out an overlapping exhaustion by rectangles? The standard construction handles it, but it should be written formally in a publication version.
- Does the Taylor inequality used hold for every integer `r≥2` with a constant independent of `A,Y`? Yes for real variables; the argument only uses it in the real count. A review should check the signs upon conditioning.
- Can the endpoint be strengthened to `O(x^{1/3}(log x)^C)` almost surely? That is not proved here; only `O_ε(x^{1/3+ε})` is obtained.

**Final scope:** a class countermodel above `1/3`, not a vanishing law for ζ's canonical exchange. The specific mechanism that would close D remains open.
