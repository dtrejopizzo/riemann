# The principal character at fixed frequency oscillates too much; it can be removed from the full average

In 290 take 1≤κ≤N^(1/4) and odd P comparable to κ+1 and at least κ. Thus the average of all characters reproduces μ exactly. There are two compatible facts: for the trivial character the summands at fixed frequency exceed the square-root budget with both signs; after integration that character can be suppressed and the rest renormalized, with square-root error on any interval.

**Obstruction at fixed frequency.** For the trivial character, in the Fourier representation of 288 the real summand is

    a_t(n)=μ²(n) ∏_(p|n)(cos(t log p)−1),     A_t(x)=Σ_(n≤x) a_t(n).

It is obtained by factoring the centered ordinary square prime by prime and dividing by 2^ω(n). For any t∈[1,2] one has A_t(x)=Ω₊(x/√log x) and Ω₋(x/√log x), where each sign has its own subsequence. Even the integrals in t of the positive part and of the negative part in magnitude have, separately, that limsup lower bound in order.

In Re s>1 compare the Euler product of F_t(s)=Σ a_t(n)n^(−s) with

    ζ(s−it)^(1/2) ζ(s+it)^(1/2) / ζ(s).

The degree-one terms coincide, so the correcting factor has an absolutely convergent tail and does not vanish near Re s=1, uniformly for t∈[1,2]; the finite factors are checked directly. At s=1+it only p=2 could give zero in 1+(cos(t log p)−1)p^(−s); it would require both cos(t log 2)=−1 and exp(−it log 2)=1, impossible. The branches are taken from Re s>1; only their moduli are needed. By the simple pole at 1, the absence of zeros of ζ on Re s=1 and compactness,

    |F_t(1+ε+it)| ≫ ε^(−1/2),      |F_t(1+ε)| ≪ ε,

with uniform constants. By partial summation F_t(s)/s is the integral of A_t(exp u) exp(−su) for u≥0. The first estimate implies that the integral of the absolute value with weight exp(−(1+ε)u) is ≫ε^(−1/2). The second bounds the signed integral with the same weight by O(ε). Hence both parts in magnitude have mass ≫ε^(−1/2). Since ∫₁^∞ exp(−εu)du/√u≤√(π/ε), one obtains the announced Ω for each sign; integrating first in t and applying Tonelli gives the integrated version. This rules out bounding the summands one by one by the square root, even at ordinary low frequencies; it uses no hypothesis on zeros in the open strip.

**Removing already integrated characters.** Let R_χ(n) be the real part of the filter with one character of 290, integrated with Wδ (that is, against its Fourier density). Its diagonal term after complementing equals μ(n). The other character factors have modulus one. The proof of 289, which already summed the moduli before grouping, therefore gives uniformly

    Σ_(n≤N)|R_χ(n)−μ(n)| ≪ κ√N log(2κ)/(log(2N))^(3/4).

Let k=2(P−1). On removing any set E of e<k characters, the difference between the renormalized average of the remaining k−e and μ is exactly −Σ_(χ∈E)(R_χ−μ)/(k−e). In particular one can remove the two characters that are trivial on the units (and differ only in the parity of v_P), with total error O(√N log(2κ)/(log(2N))^(3/4)) when P≥3 and P≍κ+1. This bound holds for every sum over subintervals. The remaining average need no longer majorize pointwise; the accumulated absolute error suffices for the one-sided criterion of 287.

**What remains.** The oscillations of A_t make it unfeasible to seek a uniform square-root bound term by term before integration. The trivial character and its variant in the valuation are no longer needed in the global estimate. The signed bound for the integrated average of the characters nontrivial on the units remains open. The Euler product of each keeps the common factor of the reciprocal of ζ in the first-degree term.
