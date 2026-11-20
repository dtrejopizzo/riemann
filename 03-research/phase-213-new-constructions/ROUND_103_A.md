# The cubes decide the contact at the covering threshold for squares

With the notation of 102, under RH let A=sup_T(−J(T)) and λ*=1−A/2. The set of λ∈[0,1] with U_λ(x)≤x eventually is exactly the CLOSED interval [0,λ*]. At the endpoint itself,

    x−U_(λ*)(x) ≥ 3x^(1/3)−O(x^(1/4)).

It is not claimed that the coefficient 3 is the exact lower limit of the normalized margin: that would require controlling how fast −J approaches its supremum.

Indeed, by 092 under RH S(y)=y+O(√y), since J is bounded. On the other hand, the integrated weight of all prime powers is Σ_{k≥1}k S(x^(1/k)) and by the integrated explicit formula of 092 equals x−√x J((log x)/2)+O(log x). The block k≥4 is O(x^(1/4)): separate k=4, and for 5≤k≤log x/log 2 use S(y)≪y and the bound O(x^(1/5)log²x). Extracting squares and cubes leaves, uniformly for 0≤λ≤1,

    U_λ(x)−x = √x[−J((log x)/2)−2(1−λ)] − 3x^(1/3) + O(x^(1/4)).

At λ* the bracket is always ≤0, including the contacts and arbitrarily close approximations. The cubic term has fixed sign and dominates the whole error. By monotonicity in λ the rest of the closed interval follows; for λ>λ* the recurrence of 102 applies. Without RH no λ works by 092. In particular the ceiling for the explicit value λ=1−D/2 is equivalent to the global sign, because under RH A≤D. This resolves the endpoint left open by the first-order estimate of 102. It does not determine A nor global positivity.
