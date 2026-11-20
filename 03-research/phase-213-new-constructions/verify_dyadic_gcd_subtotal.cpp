#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
int main() {
    constexpr int limit = 1 << 22, cutoff = 1600;
    std::vector<int> primes, lambda(limit+1), mu(limit+1), coefficient(limit+1);
    lambda[1] = mu[1] = 1;
    for (int i=2; i<=limit; ++i) {
        if (!lambda[i]) { primes.push_back(i); lambda[i]=-1; mu[i]=-1; }
        for (int p : primes) {
            if (p > limit/i) break;
            lambda[p*i] = -lambda[i];
            if (i%p == 0) break;
            mu[p*i] = -mu[i];
        }
    }
    for (int d=1; d<=cutoff; ++d)
        for (int j=1; j<=limit/d; ++j) coefficient[d*j] += mu[j];
    std::vector<int64_t> area(limit+1);
    for (int i=1; i<=limit; ++i) {
        area[i]=area[i-1]+int64_t(lambda[i-1])*lambda[i-1];
        lambda[i]+=lambda[i-1];
    }
    for (int x=1; x<=limit; x*=2) {
        __int128 numerator=0;
        for (int n=1; n<=x; ++n) {
            int q=x/n;
            numerator+= (__int128)coefficient[n]*(int64_t(n)*area[q]+int64_t(x%n)*lambda[q]*lambda[q]);
        }
        if (numerator != int64_t(numerator)) return 1;
        std::cout<<x<<" "<<int64_t(numerator)<<" "<<double(numerator)/x/x<<" "<<area[x]<<"\n";
    }
}
