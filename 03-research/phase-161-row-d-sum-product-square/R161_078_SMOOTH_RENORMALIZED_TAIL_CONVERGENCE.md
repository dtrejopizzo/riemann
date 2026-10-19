# R161_078 — Renormalized tail convergence on smooth primitive sources

## 1. Arithmetic input and scope

Use the unconditional estimate |psi(x)-x|<=C x exp(-c sqrt(log x)) for sufficiently large x. A primary source giving a stronger explicit bound, from which this weaker form follows by decreasing c, is Johnston–Yang, 'Some explicit estimates for the error term in the prime number theorem', https://arxiv.org/abs/2204.01980. This estimate is imported, not reproved here.

Fix f in C_c^infinity(-T,T) with integral exp(-u/2)f(u)du=0 and put h=A_loc f as in R161_076. Both primitive moments may be imposed, but this right-tail calculation needs the displayed one.

## 2. Smoothed right Euler tail

For t>T the backward shifts vanish and the right Euler current is

    l(t)=integral x^(-1/2) f(t-log x) d psi(x).

Only exp(t-T)<=x<=exp(t+T) occurs. Replacing d psi by dx gives exactly

    exp(t/2) integral exp(-u/2)f(u)du=0.

Write E(x)=psi(x)-x. Stieltjes integration by parts, with no boundary terms because f is compactly supported in the open interval, gives

    l(t)=-integral E(x) d_x[x^(-1/2)f(t-log x)]dx.

Since the derivative is x^(-3/2)[-f/2-f'], the imported bound gives

    |l(t)|+|l'(t)| <= C_f exp(t/2-c' sqrt(t))     (t large).  (2.1)

For l' use the same argument with f'; its weighted integral is one half of that of f and hence also zero. The bound involves f'' as well as f'. Constants depend on the fixed support window and source.

The Gamma multiplier is smooth on the real Fourier line with derivatives of at most polynomial growth, so it sends a Schwartz source to a Schwartz function. Thus its contribution g=mathcal M f has g and g' rapidly decreasing. For t>T, h=g-l.

## 3. Variation estimate and discrepancy limit

For |t|<=K set q_t(x)=x^(-1/2)h(t+log x). Direct differentiation gives

    q_t'(x)=x^(-3/2)[h'(t+log x)-h(t+log x)/2].

By (2.1), for large x uniformly on this fixed t-window,

    |q_t(x)| <= C_(f,K) exp(-c'' sqrt(log x)),
    |q_t'(x)| <= C_(f,K) x^(-1)exp(-c'' sqrt(log x))
                    +O_(f,K)(x^(-3/2)).                    (3.1)

In particular q_t tends to zero and its derivative is integrable in x uniformly in t. For integers B>A, comparison of q_t(n) with its integral over [n-1,n] proves

    |sum_(A<n<=B) q_t(n)-integral_A^B q_t(x)dx|
       <= integral_A^B |q_t'(x)|dx.                         (3.2)

The tail of the right side tends to zero, with bound of order

    C_(f,K)(1+sqrt(log A))exp(-c'' sqrt(log A))+O(A^(-1/2)).

Therefore sum_(n<=N)q_t(n)-integral_1^N q_t(x)dx converges uniformly for |t|<=K. This is a proved sum-minus-continuum limit on smooth primitive inputs, without assuming h in unweighted L2.

## 4. Matching the anchored continuum

Choose a finite anchor a and N sufficiently large for t+log N>a throughout the window. The change of variables y=t+log x gives

    C_(N,a)h(t)=integral_(exp(a-t))^N q_t(x)dx.

Hence replacing integral_1^N by C_(N,a) changes the discrepancy by an N-independent function on the window. It follows that the anchored renormalized expression S_N h-C_(N,a)h converges locally uniformly. Different choices of a differ by a negative Tate vector, as proved in R161_077; the projected limit is independent of a.

Combined with R161_077, this constructs an iterated projected limit: first M tends to infinity at fixed N, then N tends to infinity, for smooth compact primitive f. It does not identify arbitrary joint-cutoff limits.

## 5. Limits of the result

No vanishing of the resulting limit has been proved. Also the constants in (2.1) depend on derivatives of f. A first-contact vector is known only in a weaker Sobolev/form domain; smooth approximation does not transfer this convergence unless uniform estimates in that domain are supplied. The result therefore closes a smooth-source convergence step, not equality-state transport or D.

Status: locally uniform anchored discrepancy convergence for compact smooth primitive sources proved using the stated PNT estimate. Extension to radicals, value of the limit, and the required annihilation law remain open.
