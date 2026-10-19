# R170_858 — The minimal residue is a Ward resolvent sandwich

> **Correction R170_859 (Kato gauge).** The sandwich defined here is
> exact after fixing a C1 trivialization of the primitive space,
> but it is not canonical by itself. Under an infinitesimal gauge
> change it changes by the same amount as `(q,chi_f)`. The combination
> `(q,chi_f)-S_RW(f)` is indeed gauge-invariant and constitutes the
> intrinsic residue. R170_859 proves this claim and replaces the reading
> of "unique transfer function" with a class of exterior connection.

## 0. Result

This record expands the transverse coordinate isolated in R170_857 without
attributing to it a sign that does not exist. Under the REG/C1 hypotheses of
that record, let

\[
 Z=1_{\{0\}}(H),\qquad Q_K=I-Z,\qquad
 R=Q_K(H|_{Q_K\mathfrak P})^{-1}Q_K,
 \qquad C=Q_K\dot H Z .                                    \tag{0.1}
\]

For the contact vector `f` and the exterior observer
`eta=L_0^*q`, the only new term from R170_857 is

\[
 \boxed{\mathfrak S_{\rm RW}(f)
 :=(Q_K\eta,RCf).}                                         \tag{0.2}
\]

Defining

\[
 \boxed{Y:=RQ_K\eta,}                                      \tag{0.3}
\]

the exact equality is obtained

\[
 \boxed{\mathfrak S_{\rm RW}(f)=(Y,\dot Hf).}              \tag{0.4}
\]

The right-hand side admits the finite PC extraction of R170_856, but this
does not turn it into a diagonal. It produces the same physical dual test
`B_mu^*Y`, the combined port and the Tate/primitive connection. In
particular, the linear divisor identity cancels before the resolvent
and does not evaluate (0.2).

Thus, in the fixed gauge, the residue of R170_853 is represented by
a single zero-energy transfer function. The canonical quantity is
its combination with the connection of R170_857, as R170_859 makes precise.
Proving the scalar identity of §5 would close the Tate defect. It is not
proved here; VIR--LB and D remain open.

## 1. Types and conventions

Use `P=P_T` for the physical window, `Q_e=I-P`, and `Pi` for the primitive
projection inside the window. The letters `Z,Q_K` are reserved for the
spectral projections of (0.1). This separation avoids confusing three
different complements.

Let

\[
 \mathscr L_0=Q_eA\iota_0:\mathfrak P\longrightarrow Q_eL^2,
 \qquad q=Q_eS^*Ph,\qquad \eta=\mathscr L_0^*q.             \tag{1.1}
\]

Since `R=RQ_K=Q_KR` is self-adjoint positive on `Q_K`, (0.4) follows from

\[
 (Q_K\eta,RCf)=(RQ_K\eta,Cf)=(Y,Q_K\dot Hf)=(Y,\dot Hf).   \tag{1.2}
\]

The last equality uses `Y in Q_K mathfrak P`. It uses no sign, no PC, nor
an extension of the inverse of `H` to the radical.

## 2. Spectral expansion

Let `(phi_j)` be an orthonormal basis of eigenfunctions of `H` in `Q_K`, with
`H phi_j=lambda_j phi_j`, `lambda_j>0`. Then

\[
 \boxed{
 \mathfrak S_{\rm RW}(f)
 =\sum_{\lambda_j>0}
 { (\eta,\phi_j)(\phi_j,\dot Hf)\over\lambda_j}.}           \tag{2.1}
\]

The series is understood via the functional calculus of the reduced resolvent;
for data in the corresponding domain it converges in the sense of the
Hilbert product. The factors of each numerator are cross-correlations.
The positivity of `R` only signs `(u,Ru)`, not `(eta,RCf)`.

Left minimality proves `Z dot H Z<=0`; that block does not appear
in (2.1). Indeed, `RZ=0`. For this reason neither Hellmann--Feynman nor
radical semidefiniteness give a sign term by term or after summing.

## 3. PC extraction of the sandwich

In the fixed gauge of R170_857, write the speed of the form as

\[
 (Y,\dot Hf)
 =(Y,P\dot AF)+\mathfrak T_{\rm conn}(Y,f),                 \tag{3.1}
\]

where `T_conn` gathers exactly the derivatives of the primitive
projection, of the transport `iota_s`, and of the Tate port. This
definition is an identity; the connection is not assumed to vanish.

R170_856(7.2)--(7.3) gives, with

\[
 B_\mu=(PSP)^{-1}=PM_\mu P,\qquad
 \mathcal C_{PC}=S\dot A-\dot SA,
\]

the formula

\[
 P\dot Af=B_\mu P\mathcal C_{PC}f
             +\mathcal P^{\rm comb}(f),                   \tag{3.2}
\]

\[
 \mathcal P^{\rm comb}(f)
 =B_\mu P\dot SAf-B_\mu PSQ_e\dot Af.                    \tag{3.3}
\]

Therefore

\[
\boxed{
\begin{aligned}
 \mathfrak S_{\rm RW}(f)
 ={}&(B_\mu^*Y,P\mathcal C_{PC}f)\\
    &+(Y,\mathcal P^{\rm comb}(f))
      +\mathfrak T_{\rm conn}(Y,f).
\end{aligned}}                                             \tag{3.4}
\]

This is the requested finite arithmetic expansion. The first term is
expanded literally via R170_856(3.5):

\[
\begin{aligned}
 \mathcal C_{PC}={}&S\dot{\mathcal M}-\dot S\mathcal M
 -\dot L^*E\mathscr F-L^*E_-\mathscr F-L^*E\dot{\mathscr F}\\
 &-J\mathcal A^{\rm raw}\mathscr F-JK\dot{\mathscr F}
   -JH\dot{\mathscr F}-\mathcal A^{\rm raw}.              \tag{3.5}
\end{aligned}
\]

Thus (3.4) simultaneously preserves the archimedean multiplier, the
exact values of `Lambda`, the comb of all integers through
`B_mu`, the incomplete hyperbola `H`, the reflected orientation, and the
exterior/Tate ports. There is no `K2` remainder: R170_856 proves its
complete cancellation.

## 4. Why linear Ward does not evaluate (3.4)

The identity `Lambda*1=log` acts inside `mathcal C_PC`. In the full
PC, the jets of `K` and `K2` cancel between the Poisson--X block
and the two hyperbolic branches. Applying `B_mu` afterward preserves this
cancellation. Hence an exterior derivative of coefficients of the
R162_305 type only proves again the previous operator identity
prior to pairing.

The resolvent `R` depends on the full operator `H`, not coefficient by
coefficient. In (2.1), changing one arithmetic entry changes at once
`lambda_j`, `phi_j`, and both factors of the numerator. There is no
legitimate rule that passes `Lambda*1=log` through `R` as if it were
a causal convolution.

In particular, (3.4) is exactly the response form of MET--WARD:

* `B_mu^*Y` is the physical test produced by the extraction;
* the known Wronskian sign corresponds to a different Hankel test;
* `P_comb` and `T_conn` are the ports that prevent identifying them.

The expansion is more explicit than MET--WARD, but it is not a proof of
that law.

## 5. Remaining minimal scalar law

R170_857(5.5) states

\[
 g\Delta^{\rm Tate}
 =\mathfrak W_K(f)+(q,\chi_f)-\mathfrak S_{\rm RW}(f).      \tag{5.1}
\]

Using (3.4), the vanishing of the defect is equivalent to the single
identity

\[
\boxed{
\begin{aligned}
 \mathfrak W_K(f)+(q,\chi_f)
 ={}&(B_\mu^*Y,P\mathcal C_{PC}f)\\
    &+(Y,\mathcal P^{\rm comb}(f))
      +\mathfrak T_{\rm conn}(Y,f).
\end{aligned}}                                             \tag{5.2}
\]

We will call (5.2) **RES--WARD**. It is a rank-one equality for the
selected first-contact vector. It is strictly weaker than
annihilating the exterior vector `z_f` or proving a reciprocity in all
directions. It is also stronger than linear PC: PC only rewrites its
right-hand side.

## 6. Finite falsifier

The lack of sign is not an estimation defect. Consider

\[
 H=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
 Z=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 R=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
 V_c=\begin{pmatrix}-1&c\\c&0\end{pmatrix}.              \tag{6.1}
\]

For `s<0` small enough, `H+sV_c>=0`, and
`ZV_cZ=-Z<=0` for every real `c`. Take `f=e_1` and `eta=e_2`. Then

\[
 (Q_K\eta,RQ_KV_cf)=c.                                    \tag{6.2}
\]

The sandwich can take any value while the following remain fixed:

* positivity before contact;
* the radical and its metric;
* the full sign of `ZVZ`;
* the positive resolvent.

For this reason any proof of RES--WARD must use an additional relation that
ties the observer `eta` to the arithmetic transverse block. It cannot come
from minimality and spectral positivity alone.

## 7. Audit and next piece

1. **Linear PC:** (3.5) is used without inferring a sign; repeating it does
   not prove (5.2).
2. **Selberg:** `K2` is not separated; its independent physical
   contribution was refuted in R170_856.
3. **Squares:** (2.1) is not replaced by a norm; doing so loses the
   orientation or generates a comb ratio.
4. **W12/Kato:** (2.1) is the same class of cross current as the
   resolvent/cofactor chains already audited. The novelty is having
   identified its coordinate and all its ports within PC.
5. **Exact arithmetic:** it is present in (3.4)--(3.5), but a law making it
   commute with the reduced response has not yet been proved.

The next admissible piece must relate `eta=L_0^*q` to
`C=Q_K dot H Z` before taking the resolvent, so that the cross product
of (2.1) becomes an exact derivative or a boundary current with
orientation. Another coefficient identity inside `C_PC`
would repeat the cancellation of §4.

## 8. Status

```text
transverse sandwich S_RW=(Q eta,R C f)                   DEFINED
representation S_RW=(Y,dot H f)                          PROVED
spectral expansion (2.1)                                 PROVED
PC extraction with port and connection, (3.4)            PROVED
preservation of Lambda, Mobius, H, reflection and Tate    PROVED by R170_856
sandwich as a gauge-invariant quantity                    REFUTED R170_859
combination (q,chi)-S_RW gauge-invariant                  PROVED R170_859
linear Ward evaluates the sandwich                       REFUTED
minimality signs the sandwich                            REFUTED by (6.1)-(6.2)
RES--WARD, equation (5.2)                                OPEN
exterior law / VIR--LB / D                               OPEN
```
