# The scale reaching the Vinogradov–Korobov region

**Status: PROVED, with independent review of the deduction and of the two primary references.**

Corollary of 370 and its audit. Let L=log x, h=log L, b=log z and D=h^(5/3)(log h)^(1/3). For a sufficiently large absolute constant C, the equivalents and the signs S*<0, Q*>0 of 370 hold uniformly in CD≤b≤L^(3/4) for sufficiently large x.

There are only two uses of the old restriction b≥Ch². In the rectangle of height 2√L the available zero-free width is at least c h^(−2/3)(log h)^(−1/3). The saddle has d=1−α≤2h/b, by the same real partial summation as in 370. With C large a margin of at least half the strip remains. The bounds exp(O(h²)) for F,F' are maintained: on the disc centered at 1+1/h+it one can take outer radius 1/h plus three quarters of the available width and inner radius 1/h plus five eighths. The Borel–Carathéodory argument of 370 and Cauchy thus keep a margin, for |t|≥3; at bounded heights compactness and the regularity of F at 1 suffice. The value of log ζ at the center is controlled by the Euler series, since Re s=1+1/h. [Ford, theorem 1 and equation (1.1)](https://arxiv.org/html/1910.08205v5).

For the phase, apply the classical Vinogradov–Korobov remainder for θ on P≤y≤z, log P=b−1/d∼b. In AUDIT_370_PHASE the error relative to the mass M is bounded by

    O((1+2√L) exp(−c' b^(3/5)(log b)^(−1/5))).

The function in the exponent is increasing in this range. At b=CD its quotient by h tends to C^(3/5)(5/3)^(−1/5). Increasing C the error is O(exp(−h)), smaller than the minimal loss of order ξ^(−2), ξ=bd=O(h). This completes the oscillatory transfer. All the remaining Gaussian errors of 370 depend only on b/L≤L^(−1/4), on ξ→∞ and on the contour bounds already verified. Specifically the estimate for θ of [theorem 1.4, equation (1.8), of Johnston and Yang](https://arxiv.org/html/2204.01980v2) is used; its factor (log y)^(1.801) is absorbed by reducing the positive constant c' of the exponent.

The improvement comes from known external estimates applied to the observable of 368. For the target b=2h, the distance of the saddle to 1 tends to 1/2. No improvement of the constants in these two estimates bridges that difference of orders.

**Review record.** The following were independently verified: the fit d≤width/2, the nested Borel–Carathéodory radii, the substitution of the PNT remainder in AUDIT_370_PHASE and the limit of b^(3/5)(log b)^(−1/5)/h. The linked references contain respectively the region of order (log |t|)^(−2/3)(log log |t|)^(−1/3) and the required remainder for θ, with correct authors and statement numbers. The upper ceiling b≤L^(3/4) is not modified nor is the cut of 368 reached.
