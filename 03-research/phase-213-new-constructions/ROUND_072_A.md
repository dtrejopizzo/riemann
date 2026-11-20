# Signed compensation between two complementary sectors of complete rows

Let U be from 069 and v₀>0 such that k₀(v)=0 for v<v₀, with k₀=U₁ as in 070. Fix the cutoff Y=√(x/v₀). Split the whole sum into V, rows of reduced numerator divisible by some prime q>Y, and W, all the others. For large real x,
    
    V(x)=−D x/(log x)³+O(x/(log x)⁴),
    W(x)= D x/(log x)³+O(x/(log x)⁴),      D=Û''(1)>0.

Both sectors contain the complete denominators, with all the multiplicities of 069. The balance of each whole sector is determined. The construction of one-sign subfamilies in 071 did not determine those balances, and its friable cutoff was different.

**Physical identity.** Expand the row of 069 in powers of the local inverses, as in 070. Each term evaluates k₀ at x/(mn), with rad(n)|m (that is, all primes of n divide m) and the outer factor μ(m). In particular m≤x/v₀. If q>Y divides m, it is unique and q does not divide n in any nonzero term, since q²>x/v₀. Writing m=qb, one gets exactly −U_b(x/q). Conversely in the sum of rows at scale x/q every nonzero row satisfies b≤x/(qv₀)<q, so that there is no residual restriction on b. Hence
    
    V(x)=−Σ_{q>Y prime} U(x/q).

The extreme cases with q²=x/v₀ stay in W by definition.

**Moments of the complete profile.** One has U(u)=O(u exp(−c√log u)) for large u. For S this was proved in 063 by quantitative PNT. In the average over k⁶ of 069 it is preserved: for k≤u^(1/12) the argument is ≥√u, and for the rest use |S(z)|≪z together with Σ_{k>u^(1/12)} k^(−6)≪u^(−5/12). The finite differences preserve the estimate. In particular all absolute moments of U(u)du/u² with powers of log u converge; U vanishes below v₀. The transform of 067, with the additional factors of 069, is
    
    Û(s)=2 M_G(2s) ζ(4s)ζ(6s)(1−4^(1/3−s))(1−4^(1/4−s)) / [ζ(s)²ζ(2s)].

At s=1 it has a zero of order exactly two by M_G(2)>0 from 062 and the remaining positive factors. By dominated convergence from the right, the logarithmic moments of degrees zero and one are zero, and that of degree two is D=Û''(1)>0.

**Prime sum.** On a block of ratio two of q between Y and x/v₀, the sup norm and the total variation of U(x/q) are O(x/q_initial) by the bounds on the first logarithmic derivative from 069. By partial summation and the quantitative PNT the error of replacing the sum by the integral with density 1/log q is O(x exp(−c'√log x) log x) in total. Changing u=x/q in the integral gives
    
    x ∫_{v₀}^{x/Y} U(u) du / [u²(log x−log u)].

On that interval the denominator is comparable to log x. The geometric expansion up to the quadratic term has remainder ≤C |log u|³/(log x)⁴. The three moments can be completed to infinity with error O_N((log x)^(−N)) before multiplying by x, by the proven decay and x/Y comparable to √x. What remains is D x/(log x)³ with the minus sign in V. The unconditional bound above for U=V+W gives the asymptotic for W.

**Limit of the result.** A cancellation between signed sectors of all orders at the same scale has been verified. The exact equality reduces the global comparison to W(x)−Σ_{q>Y}U(x/q); its two terms are individually of size larger than the root. The control O(x/log⁴x) does not decide the precision O(√x). The decomposition by large prime and the density expansion are classical; the identity with U itself and the orientation of the sectors come from the rows of 069 and the positive moment of 062.
