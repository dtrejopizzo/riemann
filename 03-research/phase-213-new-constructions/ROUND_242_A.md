# Scattered good samples in the block of two counts suffice

Take S and W from 240–241. For large t fix h=exp(−(log t)²), N=ceil(t²), δ=h/N and n=ceil(t/(log t)²). At the N nodes k=0,...,N−1 measure

    V_k=exp(−t/2)|S(t+(k+1)δ)−exp(δ)S(t+kδ)|.

If V_(n) is the n-th smallest value (including ties), then

    lim log(1+V_(n))/t = B.

In particular if B>0 and 0<ε<B, in each sufficiently distant block at most n−1 nodes satisfy V_k≤exp((B−ε)t). The placement of those nodes is free. The physical block measures approximately X exp(−(log log X)²) with X=exp(t); the support of each weight W keeps its fixed logarithmic width.

**Maximum of the block.** The first difference eliminates the main term exactly. The argument of 241 for the maximum applies with this step: log(1/δ)=O(log²t)=o(t), G=t(log t)³, Gδ=o(1) and M log(1/δ)=o(t) for the M≤t^(q+o(1)) of the filter, q<1. Moreover M<N. For any fixed zero β₀>1/2 one can choose σ strictly between both. The first-difference multiplier of the chosen mode is comparable to δ and keeps its exponent. The same separation of zeros and powers as in 241 proves log(1+max V_k)/t→B, even for this shorter choice of h.

**From n nodes to the maximum.** Interpolate the real function without modulus g(v)=S(t+v+δ)−exp(δ)S(t+v) at the n nodes of smallest modulus. On [0,h] each elementary Lagrange numerator has modulus ≤h, and each separation between nodes is ≥δ. Hence the absolute value of the interpolant is ≤n N^(n−1)exp(t/2)V_(n), where log(n N^(n−1))=o(t). For the derivative of order n of the count it suffices to differentiate the first n boxes of W and reserve another box for the sup norm. Since 1/a_j≤Cj², this costs exp(O(n log(n+2))). The primes involved satisfy p≤exp(t+1) for large t and the sum of their weights log p is ≤exp(t+O(log t)). The real interpolation remainder is thus ≤exp(t+O(n log(n+2)+log t))h^n/n!≤exp(o(t)), uniformly on the block. After dividing by exp(t/2), the maximum costs at most exp(o(t))V_(n)+exp(−t/2+o(t)). The reverse inequality V_(n)≤max V_k concludes.

**What was gained and what is missing.** To establish B=0 it suffices to exhibit along a subsequence of blocks any n nodes of size V_k≤exp(o(t)). Their fraction n/N tends to zero. Interpolation gives stability with respect to the choice of positions and the result of 241 only controlled the maximum. The existence of those n good nodes in arbitrarily distant blocks has not been proved. The crossings of 237 are for another sum and do not provide that count.
