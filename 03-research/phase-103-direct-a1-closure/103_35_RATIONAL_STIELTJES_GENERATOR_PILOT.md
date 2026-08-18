# Exact-rational Stieltjes generator: pilot certificate

`tools/stieltjes_em_interval_pilot.py` is a self-contained extension of the
constant-generation side missing from `217`.  It uses `Fraction` throughout;
no floating-point value participates in a decision.

For \(f_j(x)=\log^j(x)/x\), it applies

\[
 \gamma_j=A_j(N)-\frac12f_j(N)-
 \sum_{r=1}^R\frac{B_{2r}}{(2r)!}f_j^{(2r-1)}(N)+R_{j,N},
\]

and generates \(f_j^{(q)}=x^{-q-1}P_{j,q}(\log x)\) exactly from
\(P_{j,q+1}=P'_{j,q}-(q+1)P_{j,q}\).  The certified remainder used by the
program is

\[
 |R_{j,N}|\le\frac4{6^{2R}}
 \int_N^\infty x^{-2R-1}
 \sum_l|[t^l]P_{j,2R}|\log^l x\,dx,
\]

where the last integral is evaluated by its finite exact antiderivative.
This follows from the periodic-Bernoulli Euler--Maclaurin remainder and
\(|B_{2R}(x)|/(2R)!\le4/6^{2R}\).  Every logarithm is enclosed by the
rational `artanh` series; \(\zeta(k)\) uses rational partial sums and
integral tails.

With the deliberately modest parameters \(N=64,R=16\), the generator
produced, for example,

\[
 \gamma_8\in[-0.000352123353803040,-0.000352123353803039],
\]

and its generated inputs, propagated through the unchanged `217` algebra,
certify

\[
 \lambda_9-\tfrac12A_9\in[1.62075622,1.62075623],
\]

\[
 \lambda_{10}-\tfrac12A_{10}\in[1.80157152,1.80157153].

These are rigorous pilot certificates, not floating-point diagnostics.

The shared exact tables are now cached.  To avoid denominator growth in the
final recurrence, `tools/fixed_margin_9_20.py` quantizes each generated
Fraction interval outward once at scale \(10^{70}\), and then uses only
integer floor/ceiling rounding.  Its executed batch certifies

\[
\lambda_n-\tfrac12A_n>0\qquad(9\le n\le20).
\]

The lower endpoints, truncated downward to 12 decimals, are

\[
1.620756227586,1.801571523444,1.999901807021,2.217326783781,
2.454980687481,2.713643545635,2.993808896556,3.295734955124,
3.619484042361,3.964953610633,4.331901184343,4.719964842446.
\]

Each fixed-point operation contains its Fraction counterpart by construction;
the first four results also agree with independently executed Fraction
propagation.  No range beyond 20 has been executed or certified.  Scaling to
149 still needs an explicit propagated-width choice of \(N,R,K\) and a
serialized interval table.
