# Loss of the Poisson majorant under cell dilation

Antecedents 212-59, 212-75 and 212-76. The additional operation consists in sweeping the radial measure of the Hankel block H to the circle while keeping the comb exactly. The independent cross-check enabled checking the resulting sufficient condition. We use the full matrix M=K−H/2 of 212-59. If P(z)=Σα_j z^j, then H[P]=∫₀^∞ w(x)|P(exp(−x))|² dx, with w(x)=((1−exp(−x))/x)². We write M[P] for the full energy of the cells.

Let J[P] be the same integral with |P(r)|² replaced by the mean of |P(z)|² with respect to the Poisson probability of r=exp(−x) on the circle. J−H is the integral of the variance by the Poisson formula. The proposed sufficient criterion would be K≥J/2. We show that for any fixed nonzero primitive cell profile its normalized defect tends to minus infinity under integer replication.

For the integer q≥1 the replica has polynomial P_q(z)=(1+⋯+z^(q−1))P(z^q). It corresponds to f_q(u)=f(u/q). In logarithmic variable it is a translation of F multiplied by √q. It preserves the vanishing moments and M[P_q]=q M[P], with ||P_q||²=q||P||² in the coefficient norm. Moreover, when evaluating at exp(−x) the geometric factor cancels exactly the geometric denominator of w: w(x)|P_q(exp(−x))|²=q² w(qx)|P(exp(−qx))|². Thus H[P_q]=qH[P] and K[P_q]=qK[P].

With dz the uniform angular probability, J[P_q]=∫|P_q(z)|² S(z) dz, where S(z)=∫₀^∞ w(x)(1−exp(−2x))/|z−exp(−x)|² dx by Tonelli. The mass of S is finite by integrability of w. As z→1 the lower limit of S is infinite by Fatou: at z=1 the integrand is w(x)(1+exp(−x))/(1−exp(−x)), equivalent to 2/x at zero.

The measures |P_q|² dz/q have mass ||P||² by orthogonality. Outside any fixed arc around 1, |P_q(z)|≤2 sup|P|/|1−z|, so the exterior mass tends to zero. For each positive L we choose an arc where S≥L. It follows that liminf J[P_q]/q≥L||P||² for all L, and hence J[P_q]/q→∞. Conclusion: (K[P_q]−J[P_q]/2)/||P_q||²→−∞. The test f_3 of BUILD_084 allows realizing the obstruction starting from a strictly positive physical energy.

Scope: paying the whole swept majorant with K is discarded. The variance recovered in the exact identity is essential at this scale. The sign of M on the full carrier remains open. Status PROVED for this obstruction. The independent review checked the scales, the variance and the concentration even when P(1)=0.
