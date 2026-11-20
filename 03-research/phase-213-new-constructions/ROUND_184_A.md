# Almost total alignment on a multiplicative interval of primes

Under the critical hypothesis of 183, for each fixed D≥8 and T→∞, put N=exp(2T−2D). There is τ with |τ−Γ|≤exp(4T) such that

    |Σ_{N≤p≤eN}(log p) p^{iτ}| / Σ_{N≤p≤eN}log p ≥ 1−C/D²−o_D(1).

C is absolute. The interval, of ratio e, lies inside the arithmetic support. The threshold approaches one by taking first T large and then D large. The antecedent 181 uses a superlevel set for a global comb; 183 localizes the mass of the profile. Here an almost maximal normalized alignment on a single interval is deduced, at an effective frequency of the profile.

**Facing windows.** With w and f=M_Γ h of 183, write b=exp(T/2)f/w. Define L(y)=b(−T+D+y), R(y)=b(T−D+y), extended by zero. For y in compact subsets of (−D,D), the measures |L(y)|²dy, |R(y)|²dy tend vaguely to dy/2: at each end the depth is D±y and the factor exp(T)/w² cancels exp(−(D±y)). Let χ be a smooth real nonzero function supported in (−1/4,1/4) and put χ_D(y)=χ(y/D). For U=χ_D L and V=χ_D R the squared norms both tend to D∫χ²/2.

Write d_p=log(p/N) and E the average with weights log p over [N,eN], of total asymptotic mass (e−1)N by PNT. In the nonnegative deficit of 183 keep only the jumps from −T+D+y to T−D+y+d_p with |y|≤D/2. After the change to b the coefficient of each jump is exp(−2T)w(t)w(t+log p)(log p)/√p. On these strips w(t)w(t+log p)=(1+o_D(1))√p uniformly. Hence

    E∫_{|y|≤D/2}|L(y)−R(y+d_p)|²dy=o_D(1).

The cost of truncating the translation, in averaged squared norm, is at most ||χ'||∞²/D² times the mass of R on |y|≤D/4+2, which is O(D) in the limit (for D=8 use a compact set inside (−D,D)). It follows, by the triangle inequality, that E||U−V(·+d_p)||²≤C/D+o_D(1). The polarization identity gives a real mean correlation ≥(1−C/D²−o_D(1))||U|| ||V||.

**Effective frequency.** By Plancherel this correlation is an integral of the transform of U against that of V with multiplier E exp(iτ d_p), up to conjugation depending on convention. After demodulating by Γ, both truncations have variation O_D(exp T): the multiplier χ_D exp(T/2)/w and its variation are bounded by constants depending on D, and ||h||∞≤Var(h). Their Fourier energy outside |τ−Γ|≤exp(4T) is O_D(exp(−2T)). Cauchy–Schwarz inside and outside the band gives the statement. Passing from d_p to log p only changes a common phase.

The result requires a real frequency that may depend on D and on the profile. To exclude saturation along this route one would need a uniform separation from one able to beat C/D² at some D, including the exceptional frequencies. That separation is not proved here.

**Independent audit.** The extraction by Plancherel, the coefficient of the deficit, the relative loss O(D⁻²) and the order of limits were verified. P47 prop:wit-coh already deduces weighted coherence from a negative datum. The additional statement here is the threshold close to one on a localized prime interval under critical saturation.
