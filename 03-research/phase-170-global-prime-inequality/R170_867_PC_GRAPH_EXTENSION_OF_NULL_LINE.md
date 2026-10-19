# R170_867 — PC extension of the null line: graph theorem

> **Closure R170_868.** This record identifies as necessary a
> component that does not factor through `D_N`. R170_868 proves that such a
> component is impossible if it remains linear, uses only `(a,c)`, and by itself
> annihilates the line `(Lambda,1)`: every row with those properties automatically
> factors. The only linear way out is to enlarge the domain with a
> physical boundary coordinate and jointly cancel arithmetic and port.

## 0. Result

The null line `R(Lambda,1)` of R170_866 can be extended canonically
to the finite PC identity. For general coefficients `(a,c)`, the residual of
using only the hyperbolic tail is exactly a linear map of the interior
defect

\[
 \mathscr D_N(a,c)={(a*\mathbf1)-c\log\over\sqrt\cdot}.    \tag{0.1}
\]

Consequently, the full positive extension has the form

\[
 \widetilde{\mathscr D}_N
 =\binom{I}{\mathcal T_{PC}}\mathscr D_N,                  \tag{0.2}
\]

and its Laplacian is

\[
 \boxed{
 \widetilde{\mathscr L}_N
 =\mathscr D_N^*(I+\mathcal T_{PC}^*\mathcal T_{PC})
  \mathscr D_N.}                                          \tag{0.3}

Hence

\[
 \ker\widetilde{\mathscr L}_N
 =\ker\mathscr L_N=\mathbb R(\Lambda,1).                 \tag{0.4}

The extension preserves arithmetic rigidity, but it is only the graph of the
divisor defect with a different positive metric. It does not produce the
exterior--Tate port nor recover the first oriented jet. Any
extension factoring through `mathscr D_N` belongs to this same class and
cannot close Ward--PC.

## 1. Homogeneous PC for `(a,c)`

Define

\[
 L_a:=\sum_{d\le M}{a(d)\over\sqrt d}\tau_{\log d},
 \qquad
 A_{a,c}:=c\mathcal M-(L_a+L_a^*),                         \tag{1.1}
\]

\[
 K_c:=cK_N,\qquad
 H_{a,c}:=L_aS_N-K_c.                                     \tag{1.2}
\]

The algebraic proof of PC is linear simultaneously in `L` and in the
channel `mathcal M,K,{X,E}`. Hence, on the core,

\[
\boxed{
 S_NA_{a,c}\mathscr F
 =c\{X,E_N\}-L_a^*E_N
  -JH_{a,c}-H_{a,c}\mathscr F.}                           \tag{1.3}
\]

For `(a,c)=(Lambda,1)` one recovers Paper 47. Positivity of
`a` is not used.

## 2. Interior and tail

Decompose

\[
H_{a,c}=H_{a,c}^{\le N}+H_{a,c}^{>N}.                    \tag{2.1}
\]

On a fiber `k<=N<=M`, every divisor appears and

\[
 H_{a,c}^{\le N}
 =\sum_{k\le N}
 { (a*\mathbf1)(k)-c\log k\over\sqrt k}\tau_{\log k}.    \tag{2.2}

Introduce, for `v=(v_k)_{k<=N}`,

\[
V_N(v):=\sum_{k\le N}v_k\tau_{\log k}.                   \tag{2.3}

With the convention of R170_866, (2.2) says

\[
 \boxed{H_{a,c}^{\le N}=V_N(\mathscr D_N(a,c)).}          \tag{2.4}

## 3. Residual when keeping only the tail

Replace `H_{a,c}` by `H_{a,c}^{>N}` on the right-hand side of (1.3) and
bring every term to one side. By (1.3), the residual is

\[
\boxed{
 \mathcal R_{PC}(a,c)
 =-JH_{a,c}^{\le N}-H_{a,c}^{\le N}\mathscr F.}           \tag{3.1}

Using (2.4), define

\[
 \mathcal T_{PC}(v)
 :=-JV_N(v)-V_N(v)\mathscr F.                              \tag{3.2}

Then

\[
 \boxed{\mathcal R_{PC}(a,c)
       =\mathcal T_{PC}\mathscr D_N(a,c).}                 \tag{3.3}

Depending on whether one works before or after multiplying PC by `mathscr F`
on the right, the Fourier factors of (3.1)--(3.2) change position. The
invariant statement is the factorization (3.3): the interior residual is
a linear function of the defect `a*1-c log`.

## 4. Graph Laplacian

On a finite Hilbert space for coefficients and an output space
where `T_PC` is bounded on the core under consideration, define

\[
 \widetilde{\mathscr D}_N(a,c)
 :=\bigl(\mathscr D_N(a,c),\mathcal R_{PC}(a,c)\bigr).     \tag{4.1}

Equation (3.3) proves (0.2), and then

\[
\begin{aligned}
 \|\widetilde{\mathscr D}_N(a,c)\|^2
 ={}&\|\mathscr D_N(a,c)\|^2\\
 &+\|\mathcal T_{PC}\mathscr D_N(a,c)\|^2.              \tag{4.2}
\end{aligned}

This proves (0.3). Since the first summand of (4.2) vanishes only on
`R(Lambda,1)`, it also proves (0.4).

The PC extension neither increases nor decreases the arithmetic null
dimension. It only changes the metric in the normal space via
`I+T_PC^*T_PC`.

## 5. Universal theorem for factored extensions

**Proposition 5.1.** Let `Q` be any linear operator defined on the
output of `mathscr D_N`. For

\[
 \mathscr D_N^Q:=\binom{I}{Q}\mathscr D_N,                \tag{5.1}
\]

one has

\[
 (\mathscr D_N^Q)^*\mathscr D_N^Q
 =\mathscr D_N^*(I+Q^*Q)\mathscr D_N,                     \tag{5.2}
\]

and

\[
 \ker\mathscr D_N^Q=\mathbb R(\Lambda,1).                \tag{5.3}

**Proof.** (5.2) is block multiplication. Since the first component
of `mathscr D_N^Q` is `mathscr D_N`, their kernels coincide. QED.

Thus adding tails, reflections, or tests that are linear functions of the
interior defect preserves the null line, but does not introduce any new
condition on it.

## 6. First jet

In the two-scale deformation of R170_866,

\[
\mathscr D_N(1,1)(\Lambda,1)=0.                           \tag{6.1}

Hence, for any regular graph extension `Q(r,q)`,

\[
\partial_-\left[Q(r,q)\mathscr D_N(r,q)ight]_{1,1}
 =Q(1,1)\,\partial_-\mathscr D_N(1,1).                    \tag{6.2}

The jet is transported linearly, but the positive energy of the graph
starts over again at order two. No term `partial_-Q` survives
because it multiplies the null value (6.1).

In particular, adding PC via (0.2) does not manufacture the mixed linear block of
R170_862. To obtain it one needs a boundary component that does not
factor through `mathscr D_N`, even though its value at `(Lambda,1)` is tied to
the null line by a new law.

## 7. Falsifiers and scope

The null line still distinguishes `Lambda` from finite modifications. But
the operation `Q` in Proposition 5.1 may be chosen for any system;
the positivity of the graph adds no selectivity. Therefore:

* the specific arithmetic lives entirely in `ker mathscr D_N`;
* PC transports that nullity to the interior residual;
* the exterior sign does not appear as long as every new block factors through
  the same defect.

This explains why linear PC, even mounted on the correct null line,
does not close D.

## 8. Status

```text
homogeneous PC in (a,c), equation (1.3)                   PROVED
H_int = V_N D_N(a,c)                                      PROVED
residual PC with tail alone = T_PC D_N                    PROVED
positive PC extension preserves ker=R(Lambda,1)           PROVED
every factored extension is a change of normal metric     PROVED
factored extension produces first-order mixed block        REFUTED
non-factored boundary component                           NECESSARY / OPEN
exterior law / VIR--LB / D                                OPEN
```
