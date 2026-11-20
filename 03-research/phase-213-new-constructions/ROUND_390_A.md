# Two crossings in the order of the primes and the distance between them

**Status: PROVED, with independent review of the orientation, the ties and the conditional scale.**

Fix the band v=log(x/y²)∈[E/2−1/2−1,E/2−1/2+1] of 386. Enumerate the primes of the band in increasing order. For each prime p, evaluate W(p) and C(p) of 386 immediately after the jump. Let i_W be the first index with W(p)≥0 and i_C the first with C(p)≤0. Then both exist for x sufficiently large. Write N=i_C−i_W and

    D_x=2J sqrt(x) exp(E/4−1/4)/log x.

If |N|→∞ one has S(x)=(1+o(1))N D_x. At every sufficiently large x, |S(x)−N D_x|≤o(1)|N|D_x+O(D_x). In particular RH is equivalent to the order i_C≤i_W eventually. The count uses positions in the list of primes and does not approximate distances between consecutive primes by their mean.

**Proof.** At the ends of the band, W has opposite signs and absolute value ∼2Jx/L² by 386, while |S|=o(x/L²) by 377. Hence C=S−W also changes sign, in the opposite direction. If the value at the upper end of the threshold is attained on a plateau, the previous prime of the band already attains it. The jumps of W are positive by 387 and those of C are their negatives. At the prime of each crossing, W stays within at most one jump of its target level (0 for i_W and S for i_C). In the whole band that jump is O(D_x); by the profile of 386 and S=o(x/L²), the two primes satisfy v=E/2−1/2+o(1). By monotonicity of v in p the same holds between them. Thus **each** intermediate jump equals (1+o(1))D_x by 387, uniformly. Subtracting W at the two indices gives the estimate, including negative N and the two endpoint overshoots. If N<0 then S<0, and if N>0 then S>0, by the definition of first crossings. In a tie |S|=O(D_x).

**Reading of the criterion.** Under RH one has S<0 eventually by 368, and hence i_C≤i_W. Conversely, if i_C≤i_W eventually, the only possible positive excess is in ties and is O(D_x)=o(√x) by 387. This excludes an exterior zero by 372. More quantitatively, if Θ>1/2, the formula and 372 give for each sign e the equality

    limsup log(1+max(eN,0))/log x = Θ−1/2,

since D_x=x^(1/2+o(1)) and the rounding errors only cost O(1) in jump units. Under RH the equivalents of 367–368 even give −N→∞: log(|S|/√x)=(1+log 2+o(1))L/log z by the real saddle (see also [the calibration for fixed powers](SADDLE_FIXED_POWER_CALIBRATION.md)). Consequently log(−N) has the same equivalent. This conditional scale is subpolynomial but exceeds every power of log x.

**Review record.** The signs at the ends have size≫D_x, so both crossings lie within the list and their previous states are also available. Write W(i_W)=r_W and W(i_C)=S+r_C, with0≤r_W,r_C≤O(D_x). Subtraction gives S=W(i_C)−W(i_W)+r_W−r_C and fixes the sign of the distance N without inverting it. If i_C<i_W, then S≤W(i_C)<0; if i_C>i_W, then S>W(i_W)≥0. Only in a tie can either sign occur, and |S|≤O(D_x). The equivalence of the eventual order admits precisely that margin, which is o(√x) and excludes the positive excursions of372 under an alternative to RH. The two crossing primes are located at v=E/2−1/2+o(1), and every intermediate prime shares that localization by monotonicity of v; hence summing a variable number of jumps preserves the uniform relative error. Under RH, log(D_x/√x)=O(h), negligible relative to L/log z; dividing the saddle of368 by D_x and using |N|→∞ justifies the scale of log(−N), not only a power bound.

The levels are defined via the separate arithmetic sums. The identity W+C=S makes the two crossings dependent; monotonicity alone does not decide their order. An arithmetic comparison between their indices is missing.
