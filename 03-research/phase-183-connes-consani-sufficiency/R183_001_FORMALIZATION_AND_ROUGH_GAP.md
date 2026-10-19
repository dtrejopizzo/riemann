# Phase 183 — Connes--Consani semilocal sufficiency

## 0. Goal and first-round verdict

We study Connes--Consani's Conjecture 4.1, *The Scaling Hamiltonian*
(arXiv:1910.14368): for

\[
 S(q)=\{\infty\}\cup\{p:p<q\},                           \tag{0.1}
\]

the semilocal framework should suffice to prove Weil for tests supported on
\((q^{-1/2},q^{1/2})\).

The published text says "the framework suffices"; it does not specify an
operator or an auxiliary inequality whose proof is weaker than Weil's. This
file formalizes the conjecture as a sign compression, proves the exact
arithmetic gap explaining choice (0.1), and locates the open step.

Results:

* the rough-integer gap is `PROVED`;
* the resulting semilocal triangularity is `PROVED`;
* that triangularity explains the exact elimination of inactive places, but
  does not by itself sign the compressed operator: `PROVED`;
* the formalized sufficiency for every \(q\) is equivalent to row D:
  `PROVED`;
* a prespectral factorization of the compression remains `OPEN`.

RH is not claimed.

## 1. Logarithmic normalization

Set

\[
 T={1\over2}\log q,
 \qquad I_T=(-T,T).                                      \tag{1.1}
\]

Connes--Consani's multiplicative interval becomes \(I_T\). Let
\(M_S\) be the monoid of positive integers coprime to every finite prime
of \(S(q)\). In other words, every prime factor of an element
\(m\in M_S\) is greater than or equal to \(q\).

### Theorem 1 (exact rough gap). `PROVED`

\[
 \boxed{m\in M_S,\ m>1\quad\Longrightarrow\quad
        m\ge q\quad\Longrightarrow\quad\log m\ge2T.}    \tag{1.2}
\]

**Proof.** If \(m>1\), it has a prime divisor \(r\). By definition of
\(M_S\), \(r\not<q\), so \(r\ge q\). Hence \(m\ge r\ge q\). `QED`

This proof simultaneously uses that the primes are those of \(\mathbb Z\),
unique factorization, and that **every** prime less than \(q\) is
incorporated into \(S(q)\).

## 2. Triangularity of the co-Poisson operator

In the coordinate \(y=\log x\), conjugate a function \(f(x)\) via
\(g(y)=e^{y/2}f(e^y)\). Connes--Consani's semilocal map

\[
 \mathcal E_Sf(x)=|x|^{1/2}\sum_{m\in M_S}f(mx)           \tag{2.1}
\]

formally takes the form

\[
 \widetilde{\mathcal E}_Sg(y)
 =\sum_{m\in M_S}m^{-1/2}g(y+\log m)
 =g(y)+V_Sg(y).                                          \tag{2.2}
\]

Let \(P_T\) be multiplication by \(1_{I_T}\).

### Theorem 2 (window triangularity). `PROVED`

On the core of compactly supported functions in \(I_T\),

\[
 \boxed{P_TV_SP_T=0,\qquad
 P_T\widetilde{\mathcal E}_SP_T=P_T.}                   \tag{2.3}
\]

**Proof.** For \(m>1\), the support of
\(g(\,\cdot+\log m)\) is contained in
\((-T-\log m,T-\log m)\). By (1.2), its right endpoint is at most
\(-T\). It does not intersect \(I_T\), except possibly at the endpoint, which has
measure zero. Summing the terms gives (2.3). `QED`

The statement is about support and does not depend on an asymptotic estimate.

## 3. What the gap does and does not obtain

The gap explains exactly why a test with propagation smaller than
\(\log q\) only sees the places \(p<q\). It is the operator version of Fact 4.2
of the article: a compact test's explicit formula involves finitely many
places.

It does not imply that the remaining terms have a sign. The semilocal
scattering unitary \(u_S\) incorporates Poisson via

\[
 \mathcal E_S\mathcal F_S=J\mathcal E_S,                 \tag{3.1}
\]

but Connes--Consani prove that none of the local quotients \(u_v^*\)
is inner. By their Lemma 3.3, the quantized logarithm

\[
 A_S={1\over2}u_S^{-1}[F,u_S]                            \tag{3.2}
\]

has no global sign. Moreover, already for \(S=\{\infty\}\), its
multiplier is proportional to the derivative of the Riemann--Siegel phase
and changes sign. The support compression is essential.

The inference

\[
 P_TV_SP_T=0\quad\Longrightarrow\quad
 P_{\mathcal P_T}A_SP_{\mathcal P_T}\preceq0            \tag{3.3}
\]

is not an algebraic consequence: the left side only controls the
rough synthesis map; the right side also contains Fourier/Poisson, Gamma, the
two Tate modes, and the return from the exterior.

## 4. Mathematical formulation of "suffices"

Let \(\mathcal P_T\subset L^2(I_T)\) be the subspace defined by

\[
 \int_{I_T}F(t)e^{t/2}\,dt=0,
 \qquad
 \int_{I_T}F(t)e^{-t/2}\,dt=0.                           \tag{4.1}
\]

The semilocal form, with the principal-value normalizations fixed by
Poisson, is identified via the trace formula with Paper 47's Weil form
\(\mathfrak a_T\). Hence the verifiable version of
Conjecture 4.1 is

\[
 \boxed{
 \langle F,A_{S(q),T}F\rangle\le0
 \quad(F\in\mathcal P_T),
 }                                                        \tag{CC-T}
\]

with the sign flipped if the convention \(W_T=-A_{S,T}\) is used.

### Theorem 3 (logical strength). `PROVED`

For each \(T\), `(CC-T)` is Weil's inequality in the corresponding window.
The family `(CC-T)` for every \(q>1\), equivalently for every \(T>0\), is
equivalent to row D and to RH.

**Proof.** The semilocal trace exactly sums the places that can
contribute to the support. Theorem 1 eliminates all the rest. The two
conditions (4.1) are precisely the conditions \(h^0=h^2=0\) that
Connes--Consani impose before stating the conjecture. The explicit formula
then identifies the trace with \(\mathfrak a_T(F,F)\), including Gamma,
primes, and poles. Varying \(q=e^{2T}\) sweeps every window. Weil's criterion
concludes. `QED`

This does not invalidate the route. It says that the content must be a
factorization of `(CC-T)` obtained from the semilocal operators, not the
mere trace identity.

## 5. The exact operator door

Before formulating it, a particularly close false proof must be excluded.

### Lemma 4 (the automatic negative corner is in the wrong space).
`PROVED`

For every unitary \(u\) and every orthogonal projection \(P\), with
\(F_P=2P-I\),

\[
 A={1\over2}u^*[F_P,u]=u^*Pu-P,                           \tag{5.1}
\]

and hence

\[
 \boxed{PAP=-Pu^*(I-P)uP\preceq0.}                       \tag{5.2}
\]

**Proof.** Expand the commutator and use \(P^2=P\):
\(u^*[P,u]=u^*Pu-P\). Compressing,
\(Pu^*PuP-P=Pu^*(P-I)uP\). `QED`

In *The Scaling Hamiltonian*, \(P\) is the half-line cutoff of the
quantized calculus. The support hypothesis on \(h_1\) belongs to the
convolution algebra of the scaling group. It does not imply

\[
 \operatorname{Ran}\widehat h_1\subseteq\operatorname{Ran}P. \tag{5.3}
\]

In fact, \(\widehat h_1\) is multiplication by the transform of \(h_1\)
in the dual representation and typically has dense range. Replacing the
cutoff \(P\) by the support projection \(P_T\) changes \([F_P,u]\) and it
ceases to be the operator of the trace formula. Hence (5.2) does not prove
the conjecture.

The real door is to transport the **cone of multipliers**
\(\widehat h_1\widehat h_1^*\) to the corner (5.2) via Poisson and the
rough gap, exactly preserving the trace.

Let \(K_T:\mathcal P_T\to\mathcal H_{S(q)}\) be the map inserting the test into
the semilocal space, before the explicit formula. The construction that
would close the conjecture is an operator, defined from Poisson and the
quotient \(X_S=\mathbb A_S/\mathbb Q_S^*\), such that

\[
 \boxed{
 -K_T^*A_SK_T=Z_{q,T}^*Z_{q,T}.                          \tag{CC-SQ}
 }                                                        
\]

It is not admissible to take \(Z_{q,T}=(-K_T^*A_SK_T)^{1/2}\), because that
assumes the sign. It must be built before knowing the spectrum, via:

1. the decomposition \(\widetilde{\mathcal E}_S=I+V_S\);
2. the exact gap \(P_TV_SP_T=0\);
3. the oriented Poisson identity
   \(\mathcal E_S\mathcal F_S=J\mathcal E_S\);
4. the two Tate modes' short;
5. a flow conservation keeping the exterior return and the
   Gamma channel together.

This list coincides, under the D.260--D.262 dictionary, with R182.201's
nonlocal joint factor `NGF`. The Connes--Consani route supplies the
space and the scattering unitary that were missing there; it still does not
supply the square (CC-SQ).

## 6. Next admitted computation

Write \(u_S\) with respect to the logarithmic decomposition

\[
 L^2(\mathbb R)
 =L^2(( -\infty,-T])\oplus L^2(I_T)oplus L^2([T,\infty)) \tag{6.1}
\]

and compute every block of

\[
 u_S^{-1}[2P-1,u_S]                                      \tag{6.2}
\]

using (2.3) **before** forming the Schur complement. Success requires that,
after removing the two Tate modes, the central block be the negative of a
Gram matrix of the two exterior channels jointly. If a Schur residual
appears, it must be literally identified with R182.201's joint
Chebyshev--Gamma column, not bounded separately.

## 7. Status

```text
gap m>1 => m>=q in M_S                             PROVED
triangularity P_T(E_S-I)P_T=0                       PROVED
places p>=q do not contribute to the test            PROVED/CITED
local quantized logarithm has a global sign          REFUTED (CC)
triangularity alone signs the compression             REFUTED
corner PAP is negative                                PROVED
support of h places Ran(hat h) inside P                FALSE
formalization (CC-T)                                  PROVED
(CC-T) for every q is equivalent to D/RH               PROVED
semilocal source factor (CC-SQ)                        OPEN
row D                                                  OPEN
```
