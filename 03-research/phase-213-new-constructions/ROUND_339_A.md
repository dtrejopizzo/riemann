# A shared logarithmic phase survives the square of the block

For 0<δ<1/4 and h=X^(−δ), the bound of 338 for two copies does not follow from squarefree support, bounded real coefficients and a power saving in the sums of each copy over **all** subintervals (relative to the length of the full block). There are identical copies satisfying those properties whose second moment in 338 is ≫(hX)². The criterion asks for O_ε(hX·X^ε).

**Construction.** Y=√X, I=[1.05Y,1.1Y], t=c/h with c>0 fixed and small enough that the Fourier transform of η does not vanish at c. Put b(n)=μ²(n) sign cos(t log(n/Y)) on I and zero outside, with sign +1 at the zeros of the cosine. This interval fits in the block of 338 for large X. For any subinterval J of I,

    |Σ_{n∈J} b(n)| ≪ Y/t + (1+t)√Y.

Indeed the count up to v of squarefree integers is v/ζ(2)+O(√v). The sign function has O(1+t) jumps, so replacing the count by its integral costs O((1+t)√Y). In the integral change to u=log(v/Y); the periodic sign has mean zero and primitive O(1/t), and the variation of the weight Ye^u is O(Y). Both terms of the bound give a power saving relative to Y for each fixed δ in the indicated range.

**Measuring the resonance.** On [X,2X] the product of two members of I only activates the first comb at k=1. All pulses W_x(de) are entirely inside that window for large X, since de/X lies between 1.05² and 1.1². Let B(x)=Σ b(d)b(e) W_x(de). Integrating against exp(−it log(x/X)) in dx/x one obtains exactly

    h hatη(c) [Σ_{n∈I} b(n)(n/Y)^(−it)]².

The real part of the sum in brackets is Σ μ²(n)|cos(t log(n/Y))| ≫ Y. To see this, the error in passing to the integral is O((1+t)√Y)=o(Y) by total variation; the function |cos| has mean 2/π and the averaging error in the integral is O(Y/t). By Cauchy–Schwarz, ∫_[X,2X]|B|²dx/x ≫ h²Y⁴. Thus there is a macroscopic imbalance even with savings in all the ordinary intervals of the two copies.

**What it excludes.** A uniform proof for block coefficients treatable only through those limits of partial sums would give a false estimate. The example selects its coefficients according to X; it is not a fixed multiplicative function and does not claim resonance of this size for μ. It makes explicit the frequency t of order 1/h that the two copies can reinforce simultaneously. The arithmetic block antecedent is 338; the phase ingredient n^(it) is the usual Mellin one.
