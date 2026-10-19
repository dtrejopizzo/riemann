# R170_882 — Log-weighted Möbius Ward law at the boundary

> **Version corrected for finite cutoff.** PC contains `S_N`, not the full
> comb. Every admissible route carries `n<=N`; the defect contains
> routes outside the window **or** with `n>N`. The full Mangoldt channel
> also leaves the prime tail `R_M^*`. The polar term lives on continuous
> routes and does not cancel this defect coefficient by coefficient.

## 0. Result

The frozen derivative of the causal predictor of R170_853 directly contains
`Lambda`, not only after taking a global moment.

Let

\[
 \mathfrak l_{N;T,t}(k)
 :=\sum_{\substack{n\mid k\\n\le N\\|t-\log n|\le T}}
       \mu(k/n)\log n.                                    \tag{0.1}
\]

Then, in the distributional sense on the right boundary,

\[
\boxed{
 \dot q_N^{\,0}
 =Q\partial_t\sum_{k\ge1}{b(\,\cdot-\log k)\over\sqrt k}
       \mathfrak l_{N;T,t}(k).}                           \tag{0.2}
\]

The full sum over divisors satisfies

\[
\boxed{
 \sum_{n\mid k}\mu(k/n)\log n=\Lambda(k).}               \tag{0.3}
\]

Hence

\[
 \mathfrak l_{N;T,t}(k)=\Lambda(k)+\mathfrak e_{N;T,t}(k),\tag{0.4}
\]

with exact exterior defect

\[
\boxed{
 \mathfrak e_{N;T,t}(k)
 =-\sum_{\substack{n\mid k\\
          n>N\ \text{or}\ |t-\log n|>T}}
       \mu(k/n)\log n.}                                   \tag{0.5}
\]

This is a local Ward law in `(t,k)`: the Mangoldt force is the value with no
boundary, and every residue is supported on routes whose intermediate
divisor crosses the window.

## 1. Derivation of `dot q`

Set `H=Ph`, extended by zero. On the scale of the integer leg,

\[
 S_N(q)^*H(t)=\sum_{n\le N}{1\over\sqrt n}
                  H(t-\log n/q).                          \tag{1.1}
\]

Keeping `H` fixed,

\[
 \left.\partial_qS_N(q)^*H(t)\right|_{q=1}
 =\partial_t\sum_{n\le N}{\log n\over\sqrt n}
                  H(t-\log n).                            \tag{1.2}
\]

The derivative is distributional: it includes the jumps of the
extension by zero at `+-T`. This keeps exactly the atoms that would be
lost by differentiating only inside the window.

Inside `H`, use

\[
 h(u)=\sum_{m\ge1}{\mu(m)\over\sqrt m}b(u-\log m).         \tag{1.3}
\]

Inserting (1.3) into (1.2), grouping `k=nm`, and keeping the condition
`t-log n in I_T`, proves (0.2).

## 2. Mangoldt and the route defect

Equation (0.3) is `mu*log=Lambda`. Subtracting from it the restricted
sum of (0.1) proves (0.4)--(0.5). There is no asymptotic step nor
recombination of one positive term with another discarded term.

Define

\[
 \mathcal L_{N,T}b(t)
 :=\sum_k{k^{-1/2}}b(t-\log k)\mathfrak l_{N;T,t}(k),      \tag{2.1}
\]

\[
 \mathcal E_{N,T}b(t)
 :=\sum_k{k^{-1/2}}b(t-\log k)\mathfrak e_{N;T,t}(k).      \tag{2.2}
\]

Then

\[
\boxed{
 \dot q_N^{\,0}
 =Q\partial_t\left(
   \sum_k{\Lambda(k)\over\sqrt k}b(\,\cdot-\log k)
   +\mathcal E_{N,T}b\right).}                            \tag{2.3}
\]

The first term is the exact derived prime comb. The second keeps
the excluded intermediate divisors.

## 3. Insertion into the exterior Wronskian

Let

\[
 q_N=Q\sum_k{k^{-1/2}}b(\,\cdot-\log k)
                         \mathfrak m_{N;T,t}(k)             \tag{3.1}
\]

be the law of R170_879. Extend `z_F` by zero across the window. For
smooth core data, or by distributional duality on the whole line,

\[
\begin{aligned}
 (\dot q^{\,0},z_F)
 ={}&-\sum_k{\Lambda(k)\over\sqrt k}
       \int b(t-\log k)\,z_F'(t)\,dt\\
 &-\int \mathcal E_{N,T}b(t)z_F'(t)\,dt.                 \tag{3.2}
\end{aligned}
\]

Consequently

\[
\boxed{
\begin{aligned}
 \mathfrak W_{\rm ext}(F)
 ={}&-\sum_k{\Lambda(k)\over\sqrt k}
       \int b(t-\log k)z_F'(t)\,dt\\
 &-\int \mathcal E_{N,T}b(t)z_F'(t)\,dt
  -\int q_N(t)\dot z_F^{\,0}(t)\,dt .                    \tag{3.3}
\end{aligned}}
\]

Real parts are taken in the complex case. Since `z_F=Qz_F`, the `Q` of
(2.3) can be moved onto the test before integrating by parts. The
endpoint atoms are contained in the distributional derivatives of
the extensions by zero; (3.2) is their joint integration by parts,
not an omission.

## 4. New minimal door

The first line of (3.3) carries the exact Mangoldt coefficient. Its
collar against `b` and `z_F'` must still be identified with the prime
channel of the virial in the PC order; the coefficient equality alone does not prove that
identification. The last two terms form the excluded-routes residue

\[
\boxed{
 \mathfrak R_{\rm route}(F)
 :=-\int \mathcal E_{N,T}b\,z_F'
    -\int R_M^*b\,z_F'
    -\int q_N\,\dot z_F^{\,0}.}                           \tag{4.1}
\]

After that collar identification, to close the exterior defect it would
suffice to show, with the polar continuum and the Gamma connection of
R170_856, that

\[
 \mathfrak R_{\rm route}(F)
 +\mathfrak P_{\rm pol}(F)
 +\Theta_{\Gamma}(F)=0                                    \tag{4.2}
\]

at first contact, or the inequality compatible with VIR--LB.

Here `Theta_Gamma` denotes exactly the Gamma terms of that ledger;
it is not defined from (4.2), nor assumed to have the required value.

Equation (4.2) is narrower than a general exterior reciprocity: its
first summand is written exclusively via excluded divisors of ordinary
integers. But it is not proved. In particular,
`m_T,t(k)` and `e_T,t(k)` change sign, so it cannot be obtained by
term-by-term positivity.

## 5. Audit against no-go

* It does not use Selberg nor `Lambda log+Lambda*Lambda`.
* It does not square PC nor eliminate the orientation.
* It does not assume `z_F=0`.
* It keeps `R_M` inside `z_F` and the explicit contribution `R_M^*b`.
* It separately keeps the comb tail `U_N=S-S_N` inside `q_N`.
* It uses `mu*log=Lambda` before recombining and keeps the exact set
  of excluded divisors.
* It is uniform in `T`; the window only selects the routes of (0.1).

## 6. Status

```text
log-weighted divisor sum in dot q                           PROVED
full value = Lambda(k)                                      PROVED
defect as excluded intermediate routes                       PROVED
distributional decomposition of dot q                        PROVED
Wronskian = Mangoldt channel + route residue                  PROVED ON THE CORE
coefficient-by-coefficient cancellation with the polar term    REFUTED BY TYPE
Mangoldt collar of (3.3) = prime channel of the virial          OPEN
route + polar + Gamma cancellation, equation (4.2)              OPEN
VIR--LB / D                                                      OPEN
```
