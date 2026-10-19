# R170_884 — Audit of the finite cutoff and the continuous polar term

## 0. Structural correction

The causal port of R170_853 contains the finite comb `S_N`. The condition
`N>=e^(2T)` stabilizes `PS_NP`, but does not stabilize `QS_N^*P`. Setting

\[
 U_N:=S-S_N,
\]

one has

\[
 (PS_N^*P)^{-1}=PM^*P,
 \qquad q_N=QS_N^*PM^*Pb,                                 \tag{0.1}
\]

and the exact exterior loop is

\[
\boxed{q_N=-QS^*QM^*Pb-QU_N^*PM^*Pb.}                    \tag{0.2}
\]

The second term cannot be discarded by interior stabilization.

## 1. Physical incidence

The correct pointwise expansion is

\[
 q_N(t)=\sum_k {b(t-\log k)\over\sqrt k}\,
       \mathfrak m_{N;T,t}(k),                            \tag{1.1}
\]

\[
 \mathfrak m_{N;T,t}(k)=
 \sum_{\substack{n\mid k\\n\le N\\|t-\log n|\le T}}
       \mu(k/n).                                         \tag{1.2}
\]

Its first two moments are

\[
 \int\mathfrak m_{N;T,t}(k)dt
 =2T\sum_{\substack{n\mid k\\n\le N}}\mu(k/n),          \tag{1.3}
\]

\[
 \int t\mathfrak m_{N;T,t}(k)dt
 =2T\sum_{\substack{n\mid k\\n\le N}}
       \mu(k/n)\log n.                                   \tag{1.4}
\]

For `k<=N` these are `2T delta_(k,1)` and `2T Lambda(k)`. For `k>N`
the exact tails over divisors `n>N` remain. Hence R170_880--881 are
correct lemmas for the full incidence, but they do not eliminate the tail of the
physical predictor.

## 2. Finite logarithmic Ward law

The frozen derivative satisfies

\[
 \dot q_N^{,0}=Q\partial_t\sum_k {b(\cdot-\log k)\over\sqrt k}
                    \mathfrak l_{N;T,t}(k),               \tag{2.1}
\]

\[
 \mathfrak l_{N;T,t}(k)=
 \sum_{\substack{n\mid k\\n\le N\\|t-\log n|\le T}}
       \mu(k/n)\log n
 =\Lambda(k)+\mathfrak e_{N;T,t}(k),                     \tag{2.2}
\]

\[
\boxed{
 \mathfrak e_{N;T,t}(k)=
 -\sum_{\substack{n\mid k\\n>N\ \text{or}\ |t-\log n|>T}}
       \mu(k/n)\log n.}                                  \tag{2.3}
\]

Integration by parts is understood with the distributional derivative of
the extension by zero. With classical exterior derivatives one must add
the traces at `+-T`.

## 3. The polar term has a different arithmetic type

On the core,

\[
 C_N=\int_0^N x^{-1/2}\tau_{\log x}\,dx,
 \qquad
 \dot C_N=-\int_0^N x^{-1/2}\log x\,\partial_t\tau_{\log x}\,dx.\tag{3.1}
\]

Pairing with `h=PM^*Pb`,

\[
 (h,P\mathcal P_{C,A_M}F)
 =(C_N^*h,\dot A_MF)-(\dot C_N^*h,A_MF).                  \tag{3.2}
\]

The expansion of `C_N^*h` integrates a continuous variable `y` and uses
coefficients

\[
 \mathfrak c_{N;T,t}(y)=
 \sum_{\substack{m\ge1\\y/m\le N\\|t-\log(y/m)|\le T}}
       {\mu(m)\over m}.                                  \tag{3.3}
\]

The logarithmic version replaces the summand with
`mu(m) log(y/m)/m`. These are not the discrete routes `n|k` of (2.3). Hence the
polar term does not cancel `mathfrak e_(N;T,t)(k)` coefficient by coefficient.

## 4. Corrected minimal residue

Write `L=MK`, `R_M=L-L_M`. After extracting the finite prime channel, the
residue contains at least

\[
\boxed{
\begin{aligned}
 \mathfrak R_{\rm min}(F)={}&
 -\int \mathcal E_{N,T}b\,z_F'
 -\int R_M^*b\,z_F'
 -\int q_N\,\dot z_F^{,0}\\
 &+(C_N^*h,\dot A_MF)-(\dot C_N^*h,A_MF),
\end{aligned}}                                           \tag{4.1}
\]

in addition to the occurrences of `R_M` inside `z_F` and
`dot z_F^0`. The tails `U_N` and `R_M` are distinct and both must
be kept.

The next admissible piece must be an exact Euler--Maclaurin
identity inside the full pairing of (4.1), able to transport the
discrete comb to the polar continuum with its boundary terms. An
additional local identity on the collar would repeat the previous
no-gos.

## 5. Status

```text
correction of the predictor S -> S_N                       PROVED
finite incidence and tail n>N                               PROVED
finite logarithmic Ward law                                  PROVED
continuous type of the polar term                             PROVED
coefficient-by-coefficient polar/discrete cancellation        REFUTED
minimal residue (4.1)                                         LOCATED
paired Euler--Maclaurin identity                               OPEN
sign via minimality / VIR--LB / D                              OPEN
```
