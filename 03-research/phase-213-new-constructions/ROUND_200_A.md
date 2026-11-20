# A block of arbitrary dimension with four free rates

Let L₄,c₄ be a length and margin valid in 199. There exists ε>0 such that, ordering the rates 1/2<v₁≤…≤v_n and counting multiplicities, it suffices that

    Σ_{j=5}^n 1/v_j ≤ ε

to obtain W(F)≥(c₄/4)||F||². Here F consists of any form datum g on [−L₄,0] and any causal rational function with denominator ∏(s+v_j) and numerator of degree less than n. The bound admits four free rates and arbitrarily large n. Repeated poles are interpreted in the confluent sense. The sufficient budget is not evaluated numerically.

**Dimension-independent concentration lemma.** If a fast block has budget B=Σ 1/v>0, put σ=1/(2B). For each pole σ/v≤1/2. By Hardy reflection in 213-085,

    ||exp(σy)h||₂ ≤ exp(2σB/(1−1/4))||h||₂ = exp(4/3)||h||₂.

Thus every unit h has ||h||₁≤exp(4/3)√B. For B→0 its Fourier mass on each fixed interval tends to zero uniformly. The global floor of the archimedean symbol and its growth to infinity imply that the infimum of the archimedean term over such h tends to infinity. For every fixed weight b, eventually σ>b and the weighted norm of h with exp(by) is uniformly bounded. In particular the prime and polar pieces of W(h) are bounded in absolute value by a constant using b=1. The fast bottom of W tends to infinity, independently of the number of poles.

**Keeping the window of 199.** If no ε worked, there would be listings with budget after the fourth rate tending to zero and norm-one data with W(F)<c₄/4. Cases with up to four poles already satisfy 199. Extract a subsequence in which each of the first four rates has a finite or infinite limit. Poles with finite limit stay in a fixed box [1/2,V], and all others form a fast block with total budget B→0: to the truncated sum only up to four reciprocals tending to zero are added. Eventually the two groups are disjoint and partial fractions decompose the whole tail as s+h. An exact collision is kept whole in its group. The initial unit norm does not require the partial fractions to have bounded coefficients.

One has W(g+s)≥c₄||g+s||² by 199. For some fixed C along the subsequence, |W(g+s,h)|≤C||g+s||·||h||. Indeed, g and s have disjoint supports; for g against h, Carleman and the weighted bound of 198 apply (the interval is fixed). For s against h the divided-difference basis of up to four rates in a compact box is used: the archimedean term of s acting as an operator is bounded on L², and its non-archimedean crossing, after combining ζ'/ζ and the pole, has density O(exp(C' y)) with the three required derivatives, as in 198–199. In that estimate only ||exp((C'+1)y)h||₂=O(||h||₂) is required, which has just been proved with a constant independent of the fast dimension. By Young, if the fast floor is at least 2C²/c₄+c₄/2, one obtains

    W(F) ≥ (c₄/2)(||g+s||²+||h||²) ≥ (c₄/4)||F||².

The contradiction proves uniform existence. Once the statement is proved on L₄, every smaller length enters by extension of the datum by zero to the left.

**Consequence for the sign.** A negative rational test in this class would need more than ε of reciprocal budget after removing its four slowest rates. For five poles without compact datum, for example, there is an absolute threshold for the largest rate above which all numerators have strict sign, with the other four rates arbitrary. The sign of five arbitrary rates is not concluded, nor that of the dense regime of the bridge. 213-085 already covered all orders with TOTAL budget ≤1/512; here the four free rates are allowed to consume a much larger budget and an arbitrary compact datum is kept. No improvement of the value 1/512 is claimed when no rates are excluded.
