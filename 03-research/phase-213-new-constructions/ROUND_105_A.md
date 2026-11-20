# A ceiling without tolerance on a band of ratio four

For large x, let w_x(p)=log(x/p) for x/2≤p≤x and log(4p/x) for x/4≤p<x/2, and zero outside. The global sign is equivalent to Σ_p w_x(p)log p≤x/4 eventually. The integral of the weight is exactly x/4. Under RH there is moreover a margin ≥0.034√x eventually. Localization by differences already appears in 044 with another weight and another tolerance.

**Quantitative direction.** With F=S−id of 104, the discrepancy is H(x)=F(x)−2F(x/2)+F(x/4), by pointwise cancellation of the lower weights. By 092 under RH F(x)=−√x[2+J((log x)/2)+o(1)] with |J|≤D<0.047. Thus

    H(x)/√x ≤ −2(1−1/√2)²+D(1+1/√2)²+o(1).

Using the value D=2+γ_E−log(4π)<0.0462, the magnitude of the margin exceeds 0.036 before the o(1), so the declared margin holds.

**Elementary recovery.** Extend S=0 for x<2 and F=S−x for x>0. At each fixed x one has F(x)=Σ_{j≥0}(j+1)H(x/2^j) by telescoping, since the tails decrease geometrically. If H≤0 from X₀≥2 on, the range x/2^j≥X₀ only helps the ceiling. For 2≤x/2^j<X₀ there remain O_(X₀)(1) values, of weight O(log x), and below 2 one has H(t)=−t/4. Hence F(x)≤O(log x), sufficient by 092 and the same one-sided argument of 088 (J stays bounded below). This recovers the sign without evaluating zeros to invert the cut.

**Scope.** With general ratio r>1 the same computation works if 2(1−1/√r)²>D(1+1/√r)², with support [x/r²,x]. At r=2, all the arithmetic sits in two adjacent intervals with symmetric logarithmic weights. In 044 the window in fourth powers has ratio 256 for even indices and the criterion admits a free constant after normalization. Here the ceiling is the integral itself; both it and the positive inverse come from the same second difference. The proof of the arithmetic ceiling remains open.
