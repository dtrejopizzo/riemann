# Two copies of the same Möbius block in the local mean

For large X, δ=1/j with j≥3, h=X^(−δ), fix 0<ε<1/2−δ. Put D=⌈2√X⌉, L=X^(1−δ−ε)/D and M(d)=μ(d)1_{L<d≤D}. Define W_x(v)=η(log(x/v)/h). Uniformly in X≤x≤2X,

    S_h(x)−2S_h(x/2)
      = −Σ_{k≤2X/L²} Σ_{d,e} M(d)M(e)[W_x(kde)−2W_x(2kde)] + O_B(X^(−B))

for any fixed B. One can also cut k at O(X^(δ+ε)) if one imposes de>X^(1−δ−ε). The formula with the longer cut keeps an exact convolution square M*M, without a pair-dependent cut.

**Identity and error.** For U(d)=μ(d)1_{d≤D}, the convolution μ−2U+U*U*1 is (1*U−e₁)^( *2 )*μ. The defect in parentheses vanishes up to D, hence the whole residue vanishes up to D². The terms 2U disappear in both samples because n lies in (xe^(−h)/2,x] and exceeds D. For each l=de≤X^(1−δ−ε), the two combs of multiples of l and 2l have the same integral contribution after the factor two. In the real variable k, the pulse W_x(lk) has length comparable to J=hx/l and L¹ norm of the derivative of order N bounded by C_N J^(1−N), by the chain rule on its support. Poisson summation and N>1 give error O_N(J^(1−N)) for the comb; the same argument holds at step 2l. Here J≥X^ε. There are O(D²)=O(X) pairs. Choosing N according to ε,B allows erasing any subset of those complete pairs, including all those with min(d,e)≤L. By support k≤2X/L² in the remaining rectangle. If all the small pairs are erased, the cut for k improves to the indicated one.

**Equivalence.** The mean square of this block in dx/x satisfies the criterion of 337 with ceiling X^(1+ε')h for each ε'>0 and j≥3 if and only if RH holds. Indeed the Dirichlet transform for S_h(x)−2S_h(x/2) is F(s)(1−2^(1−s)); its coefficients are bounded by 3. The extra factor preserves each pole with 1/2<Re s<1 since its zeros have real part one; ζ has no zeros on Re s=1. Under RH the factor is bounded in each strip considered. The dual argument with the weight φ and the error O(Xh^K) of 337 therefore applies unchanged, and the uniform error O_B(X^(−B)) passes to the local norm.

**Comparison with the antecedent.** 049 already obtained factors near √X via corrections in progressions for a pointwise deficit. Its exterior weight a(k)+c(k) is different from the interior μ(m). Here the same real sequence M intervenes twice and the norm is the mean of 337. The symmetric convolution allows writing an ordinary square of Dirichlet polynomials, which may have complex phase. Eliminating short factors is an application of truncated inversion and Poisson; the bound for the mean of the symmetric block remains open.
