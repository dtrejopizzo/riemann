# Pairing between distinct odd products in the full observable

For large X and Y=X^(1/3) there exist odd squarefree a<b in [Y,3Y] with μ(a)=−μ(b) and b−a≤Y^(1/4). Choose a single pair per X, independent of x. At all centers X≤x≤2X and with h=X^(−δ), fixed 0<δ≤1/16, select the products at and bt for t odd squarefree and (t,ab)=1. In the full observable C_h of 342 this family has absolute mass at least X^(2/3−δ−o(1)), but its joint signed contribution costs O_η(X^(5/12))=o(√(Xh)) uniformly. These are distinct integers even after gathering all representations of each product.

**Existence of the two factors.** In intervals (y,y+J] with Y≤y≤2Y and J=Y^(1/4), the mean over y of the number of odd squarefree integers is ≫J, by integration and their positive density in the long interval. Since the maximum is O(J), a positive proportion of centers has ≫J such integers. By the maximal bound over progressions of 329 and 333, outside a set of proportion o(1) the sum of μ over the progression of odd integers in the interval is o(J). The threshold 1/6+ε lies strictly below 1/4. Some center satisfies both conditions and contains both signs. [Short-interval input, §1.1](https://arxiv.org/html/2411.05770v1)

**Identity of signs and cost.** On odd integers, the full coefficient of C_h is μ(n). In each pair μ(at)=−μ(bt); the two classes of products are disjoint since if at=bu then b/(a,b)>1 divides t, contradicting coprimality. Within each class separately there are no repetitions either. Their signed sum equals

    μ(a) Σ_t μ(t)[W_x(at)−W_x(bt)]

with the previous restrictions. The difference of weights costs at most ‖η'‖∞ log(b/a)/h. Since log(b/a)≪Y^(−3/4)=X^(−1/4)≪h, the union of the two supports contains O(1+hX/Y) integers t. This yields O(X/Y · Y^(−3/4))=O(X^(5/12)). This step does not even require cancellation among the t.

**Removed mass.** It suffices to count products at with η bounded below on a subinterval. The range of t has length comparable to hX/Y. The count of 341 with Q=2ab has main density term c_Q=ζ(2)^(−1)∏_{p|Q}p/(p+1)≥X^(−o(1)) (for example c_Q≥ζ(2)^(−1)/τ(Q)). The error O(τ(Q)√(X/Y)) is X^(1/3+o(1)). The announced floor follows. For δ≤1/16 the mass exceeds √(Xh) by a power, while the balance stays strictly below.

**Limit.** 346 cancels representations of the same n. Here cancellation occurs in families of different n with the true coefficients of the full observable. A single pair of factors only covers O(hX/Y) samples per center. To sum many families one needs disjoint classes or an accounting of their intersections, besides controlling the accumulated balance and the uncovered products. The global sign is not inferred.
