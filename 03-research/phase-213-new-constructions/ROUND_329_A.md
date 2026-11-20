# Saving of every power in the central Möbius energy

With the notation of 325–328, for each fixed a in (0,log 4] and fixed real b, take h=exp(−am)m^b. Then, for **each fixed A>0**,

    E_m[h] = Δ_m + O_(a,b,A,η)( h binom(2m,m) m^(−A) ).

In particular E_m[4^(−m)m^b]∼Δ_m for every fixed b, and for every 0<a<log 4 the quotient E_m(a)/P_m(a) is O_(a,A,η)(m^(−A)) to any fixed order. The restriction b<1/50 of 328 came from the estimate used, not from the weight of the problem.

**Which external estimate enters.** In the introduction of *Higher uniformity of arithmetic functions in short intervals II*, Matomäki, Radziwiłł, Shao, Tao and Teräväinen state the maximal bound in almost all intervals of length H≥Y^(1/6+ε) and expressly specify its version for μ. For each A, the sum of μ over any subinterval of (y,y+H] costs O(H log^(−A)Y) except on a set of y of measure O_(ε,A)(Y log^(−A)Y) in the dyadic block. We only use contiguous subintervals, contained in the maximum over progressions. This is the scalar estimate of the introduction, not the threshold 1/3 for general nilsequences. [Statement (1.5) and paragraph on Möbius in the arXiv version](https://arxiv.org/html/2411.05770v1) · [Published version, formula (1.6)](https://doi.org/10.1007/s00222-026-01408-6)

**The actual length exceeds the threshold.** Take as central zone 1.8m≤log x≤2.2m. In a dyadic block [Y,2Y] meeting it put H=ceil(4hY), constant on the block. Uniformly there,

    (log H)/(log Y) ≥ 1−(log 4)/1.8−o(1) > 0.22.

Hence, for example, the margin 1/6+1/30 fits. Also H/Y→0 and, for each fixed positive a, H≤Y^(1−ε') for some ε'>0. Adjust ε to the smaller of the margins if needed. Every nonzero sample of the smoothing in 327 lies in (x−H,x]. Applying the theorem with y=x−H covers the shifted range with a bounded number of dyadic blocks. Exceptionality is still measured with respect to x because the shift H is constant.

On the support, the weight η(log(x/n)/h) l_m(n)/l_m(x) has total variation O_η(1): the variation of η is fixed by monotonicity of the change of variable and the logarithmic derivative of l_m with respect to log n is m/log n−3/2, bounded. By partial summation the maximal bound of the input passes to the weight. On normalizing by hx, the weighted local sum costs O_A(m^(−A)) outside the exceptional set, and O(1) on the whole block. Hence its mean square costs O_A(m^(−A)), including the exceptional points. The constants are uniform over the central blocks for large m.

**Integration and limits.** Repeat the Gram integral of 327 with the weight h x l_m(x)² dx; its ratio variation within each central block is bounded. The central contribution is O_A(h binom(2m,m)m^(−A)). The diagonal contained in that zone is exponentially small relative to 1/√m, since it is concentrated at log n near m. Outside the central zone the absolute mass of distinct pairs costs O(h binom(2m,m) exp(−c m)), by the gamma tail of the neighbour weight of 328. This also covers the two edges widened by h. Since h binom(2m,m) is at least a fixed power of m below 1/√m throughout the stated range, the central diagonal is absorbed into the error. The formula is obtained. For a<log 4 the diagonal is moreover exponentially smaller than P_m(a), and 327 gives the announced quotient.

There is no control of the constants when A grows with m. In particular, these estimates do not give a fixed reduction of the exponential rate at a=1/j. That reduction is what the global criterion demands; it remains open.
