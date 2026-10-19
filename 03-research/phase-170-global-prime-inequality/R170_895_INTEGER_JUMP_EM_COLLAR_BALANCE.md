# R170_895 — EM collar balance with integer jumps

## 0. Exact law, doubly reviewed

Couple the continuous cutoff to the window via

\[
 N(T)=e^{2T},\qquad T_n={1\over2}\log n,
\]

and define the exterior anchor

\[
 a_T:=Q_TZ_{N(T)}^*h_T,\qquad Z_N=S_N-C_N.                \tag{0.1}
\]

Then `a_T` satisfies, as an identity of measures in `T`,

\[
\boxed{
\begin{aligned}
 D_Ta_T={}&-\dot P_TZ_N^*h_T\\
 &+Q_T\sum_{n\ge1}{\tau_{-\log n}h_T\over\sqrt n}
       \delta_{T_n}\\
 &-2\sqrt N\,Q_T\tau_{-\log N}h_T\,dT
 +Q_TZ_N^*D_Th_T.
\end{aligned}}                                           \tag{0.2}
\]

The four terms are, in order:

1. the collar of the moving window;
2. births at the exact integers;
3. the continuous Euler--Maclaurin density;
4. the connection of the causal dual.

The equation is a forced balance, not an already closed conservation
law.

## 1. Derivative of the cutoff

As a measure in `N`,

\[
 d_NS_N=\sum_{n\ge1}{\tau_{\log n}\over\sqrt n}\delta_n,
 \qquad
 d_NC_N={\tau_{\log N}\over\sqrt N}dN.                  \tag{1.1}
\]

Hence

\[
\boxed{
 d_NZ_N=
 \sum_{n\ge1}{\tau_{\log n}\over\sqrt n}\delta_n
 -{\tau_{\log N}\over\sqrt N}dN.}                      \tag{1.2}
\]

The change `N=e^(2T)` preserves the mass of each atom and transforms the
continuous part via `dN=2N dT`:

\[
 D_TZ_{N(T)}=
 \sum_{n\ge1}{\tau_{\log n}\over\sqrt n}\delta_{T_n}
 -2\sqrt N\,\tau_{\log N}dT.                            \tag{1.3}
\]

Differentiating (0.1), using `dot Q=-dot P`, and taking adjoints proves
(0.2).

The continuous density of (1.3) is the same face `t+log N` that appears in
`dot C_N`. When (0.2) is inserted into the polar ledger it must be counted
only once.

## 2. Connection of h

Fiber by fiber, for `N>=e^(2T)`,

\[
 h_T=(P_TS_N^*P_T)^{-1}b_T=P_TM^*P_Tb_T.                 \tag{2.1}
\]

Hence, in the ambient trivialization,

\[
\boxed{
 D_Th_T=\dot P_TM^*P_Tb_T
 +P_TM^*\dot P_Tb_T
 +P_TM^*P_TD_Tb_T.}                                     \tag{2.2}
\]

In another trivialization, all derivatives must be replaced by the
metric connection of R170_887.

The derivative of the window is the trace operator

\[
 \dot P_Tf=f(T)\delta_T+f(-T)\delta_{-T}.                \tag{2.3}
\]

Thus the first and fourth terms of (0.2) literally preserve the
motion of the collar.

## 3. Exterior jumps

At a threshold `T=T_n`, the new translate connects boundary to boundary
inside the compression, so `P_TS_N^*P_T` does not jump in `L2`. The
exterior anchor does jump:

\[
\boxed{
 [a_T]_{T_n}
 =Q_{T_n}{\tau_{-\log n}h_{T_n}\over\sqrt n}.}           \tag{3.1}
\]

This explains why a classical derivative within each chamber loses
the arithmetic of the births, even though the interior operator is already
stabilized.

## 4. Insertion of Möbius and Mangoldt

Multiplying (1.2) by the Möbius comb produces

\[
\boxed{
\begin{aligned}
 (d_NZ_N)M={}&
 \sum_{n,m\ge1}{\mu(m)\over\sqrt{nm}}
       \tau_{\log(nm)}\delta_n\\
 &-\sum_{m\ge1}{\mu(m)\over\sqrt{mN}}
       \tau_{\log(mN)}dN.
\end{aligned}}                                           \tag{4.1}
\]

Prepending the prime comb `L`, the auxiliary fiber `r=dm` contains
coefficients

\[
 (\Lambda*\mu)(r)=\sum_{dm=r}\Lambda(d)\mu(m),           \tag{4.2}
\]

still accompanied by the birth route `n`, so that the total
translation is in `nr`. They do not reduce by themselves to `Lambda(r)`.
The identity
`mu*log=Lambda` only acts when the full logarithmic block is
present; the cutoff leaves signed incidence terminals.

## 5. Remaining obligation

A conservation of the anchor would require jointly annihilating the
right-hand side of (0.2): jumps, continuous density, `dot P_T`, and
`D_Th_T`. PC can re-express its prime insertion via (4.2), but it does not
by itself cancel the moving face nor the collar.

The next admissible law must be an identity of measures in `T`, not an
equality within a single chamber. It must convert the
`Lambda`--Möbius terminals of (4.2) and the continuous density into the two
collar traces, while preserving the connection of `h_T`.

```text
cutoff measure d_N Z_N                                       PROVED
coupled T,N balance, equation (0.2)                           PROVED
exterior jumps at every integer                                PROVED
exact Möbius insertion                                          PROVED
Lambda(d)mu(m) fibers                                           PROVED
automatic algebraic conservation                                REFUTED
measure law cancelling the balance                               OPEN
polar normalization / VIR--LB / D                                OPEN
```
