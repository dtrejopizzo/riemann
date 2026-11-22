# Phase 182 — rectangular Gram tunnel

## 0. Verdict corrected after corpus audit

Exactly two already-validated mechanisms are selected:

1. **positivity:** a Gram matrix, which preserves every correlation;
2. **orientation:** the affine logarithmic channel
   \([X,V_p]=(\log p)V_p\), whose physical coefficients are
   \(2\Lambda(n)n^{-1/2}\).

The correct fusion is not the square of the oriented channel. It is a
**rectangular** factorization with the oriented channel in one corner. This
architecture algebraically avoids R181's quotient comb. Below we prove the
closure lemma and also the exact circularity test. Closing
D reduces to building a single common arithmetic factor before
recombining the fibers \(dm=k\).

**Internal priority correction.** The null-corner lemma is not new in the
corpus: it is the static form of the *bordered null anchor law* of R170_862
§§2--4. The prime-local rectangular coligation is also not new: D.244--D.247
already build its conservative part. D.256--D.262 further prove that
transporting it to support/Gamma leaves an infinite-dimensional coherent
channel and reduce the problem to a joint square of the centered Chebyshev
measure and the Gamma measure. Hence the first version of this file
exaggerated the architecture's novelty; that claim is withdrawn.

The fusion lemma is `PROVED/CITED`. The local fiberwise realization proposed
in §5 is `NO-GO` after R182_201. The only part still open is a **joint,
nonlocal** factorization prior to the pseudo-inverse. D is not claimed.

## 1. The null corner

Let \(\mathcal P,\mathcal E,\mathcal K\) be Hilbert spaces and

\[
 A:\mathcal P\longrightarrow\mathcal K,
 \qquad B:\mathcal E\longrightarrow\mathcal K .          \tag{1.1}
\]

The Gram form of the row operator \((A\ B)\) is

\[
 \mathbb M(A,B)=
 \begin{pmatrix}
 A^*A&A^*B\\
 B^*A&B^*B
 \end{pmatrix}
 =
 \binom{A^*}{B^*}(A\ B)\succeq0.                         \tag{1.2}
\]

### Theorem 1 (rectangular tunnel lemma). `PROVED`

If

\[
 H=A^*A,\qquad R=B^*A,                                   \tag{1.3}
\]

then

\[
 \boxed{\ker H\subseteq\ker R.}                         \tag{1.4}
\]

In particular, if \(F\) is a first-contact vector,
\(H_{T_*}F=0\), and \(R=R_L\), then \(R_LF=0\).

**Proof.** From \(H=A^*A\) one obtains
\(\langle F,HF\rangle=\|AF\|^2\). If \(HF=0\), then \(AF=0\), and
by (1.3), \(RF=B^*AF=0\). `QED`

The same proof holds for a scalar port
\(\beta(F)=\langle b,AF\rangle\): simply take
\(\mathcal E=\mathbb C\) and \(Bz=zb\).

## 2. Why this fusion preserves both halves

Positivity comes from (1.2) before observing the spectrum. The orientation
is not diagonalized: it lives in the corner \(B^*A\), which changes when
\(B\)'s orientation changes. Hence the sign loss of a scalar covariance
does not appear.

Nor is \(B_c^2\) formed inside the physical block. Correlations between
different channels may appear in \(B^*B\), but that term is confined to
the auxiliary space \(\mathcal E\). The block acting on
\(\mathcal P\) is exactly \(A^*A=H\). This avoids R181's mechanism:
the terms \(\log(m/n)\) do not contaminate \(H\).

This is the essential difference from \(\|(X+iB_c)F\|^2\): there, the same
oriented operator occupies both sides of the product and forces
\(B_c^2\); here, the two sides of the product are different operators.

## 3. Exact circularity test

### Theorem 2 (energy factorization criterion). `PROVED`

Let \(H\succeq0\) be bounded in finite dimension and let
\(R:\mathcal P\to\mathcal E\). The following are equivalent:

1. there exists \(B\) such that \(R=B^*H^{1/2}\);
2. there exists \(C\succeq0\) such that
   \(\begin{psmallmatrix}H&R^*\\R&C\end{psmallmatrix}\succeq0\);
3. \(\ker H\subseteq\ker R\).

In infinite dimension, (1) with bounded \(B\) is equivalent to the
inequality \(R^*R\preceq cH\) for some \(c<\infty\); the kernel inclusion
alone is necessary, but may not suffice for boundedness.

**Finite proof.** (1) implies (2) by taking \(C=B^*B\), and (2) implies (3)
via Cauchy--Schwarz for the semidefinite form: a zero diagonal entry
annihilates its whole row. If (3) holds, define
\(B^*=RH^{\dagger/2}\) on \(\operatorname{ran}H\) and zero on its
orthogonal complement. Then \(B^*H^{1/2}=R\). `QED`

Hence it does not count to choose \(A=H^{1/2}\) and then solve for \(B\):
that construction exists precisely when \(R_LF=0\) is already known on the
radical. The only admissible version must produce \(A\) and \(B\) jointly
from the arithmetic, before knowing \(\ker H_T\).

## 4. The missing assembly law

For each finite cutoff \(N\), let

\[
 \mathscr H_N=\{(d,m):dm\le N\}                         \tag{4.1}
\]

be the factorization hyperbola, without yet recombining \((d,m)\) into
\(k=dm\). The sought construction consists of:

\[
 A_{N,T}:\mathcal P_T\to\mathcal K_N,
 \qquad
 B_{N,L}:\mathbb C^L\to\mathcal K_N,                    \tag{4.2}
\]

defined locally on \(\mathscr H_N\), and of a closed limit
\(A_T,B_L\), with these exact identities:

\[
 \boxed{A_T^*A_T=H_T,}                                  \tag{RT1}
\]

\[
 \boxed{B_L^*A_T=R_L.}                                  \tag{RT2}
\]

`RT1` must result from the Poisson--Tate assembly, including Gamma and
poles. `RT2` must result from the orientation of the divisor edges and from

\[
 \Lambda*1=\log,                                        \tag{RT3}
\]

not from a posterior definition via \(R_L\). The sum over a product
fiber must be carried out only after forming the rectangular corner.
This is the condition that prevents quotient fibers from appearing.

If `RT1--RT3` are proved before the spectrum, Theorem 1 gives

\[
 H_{T_*}F=0\Longrightarrow R_LF=0,                       \tag{4.3}
\]

and the already-proved fidelity of \(R_L\) on the radical excludes first
contact. Then Paper 46 delivers \(W_T\ge0\) for every \(T\).

## 5. First local ansatz and its consistency condition — `NO-GO`

Let \(e_{d,m}\) be an orthogonal basis of \(\mathcal K_N\). A non-circular
ansatz has the form

\[
 (A_{N,T}F)_{d,m}=a_{d,m}(F),\qquad
 (B_{N,L}z)_{d,m}=\sum_{j\le L}z_j b^{(j)}_{d,m}.         \tag{5.1}
\]

Then

\[
 \langle z,B_{N,L}^*A_{N,T}F\rangle
 =\sum_{dm\le N}\overline{\sum_jz_jb^{(j)}_{d,m}}
                    a_{d,m}(F).                          \tag{5.2}
\]

There are no cell pairs \((d,m),(d',m')\) in (5.2); in particular no
frequencies \(dm/(d'm')\). The minimal arithmetic condition is that, when
summed over each fiber \(dm=k\), (5.2) gives exactly the Gamma moment of
\(R_LF\), while

\[
 \sum_{dm\le N}|a_{d,m}(F)|^2                          \tag{5.3}
\]

assembles into Weil's full form. Identity `RT3` fixes the oriented sum
of the coefficients of (5.2), but by itself does not fix the quadratic moduli
of (5.3). The new, concrete condition is thus a
**product-fiber Euler--Poisson isometry**:

\[
 \boxed{
 \sum_{dm\le N}|a_{d,m}(F)|^2
 =\mathfrak a_{T,N}(F,F)+\operatorname{boundary}_{N,T}(F),
 }                                                        \tag{EPG}
\]

with a boundary term converging exactly to Gamma plus poles, and with
the same \(a_{d,m}\) appearing linearly in (5.2).

The subsequent audit found that the conservative part of this geometry
is already in D.244--D.247. Moreover, D.258--D.259 and R182_201 prove that
imposing **fiber-by-fiber** orthogonality cannot produce the global null
anchor: the coherent channel realized on \(L^2\) has infinite rank, while the two
Tate conditions have codimension two. Hence `EPG` in this local form is
`NO-GO`.

The surviving version replaces (5.3) by a single joint square of the
full column

\[
 \mathfrak q_N=q_{N,\infty}
   -\int_{[1,N]}\mathcal K_N(x)\,d(\Psi(x)-x+1),          \tag{5.4}
\]

after support and Tate, but before the pseudo-inverse. This is exactly
the object typed in D.262(4.1)--(4.5), not a sum of local squares.

## 6. Falsifier proofs

1. **Davenport--Heilbronn:** has no positive Euler coefficients
   satisfying `RT3`; the map \(B\) cannot be defined with the required
   anchor.
2. **P_171:** has factorization and integrality, but not the ordinary
   Poisson--Tate assembly of `RT1/EPG`; the \(A\) side fails.
3. **Finite modifications of \(\Lambda\):** break `RT3` with the exact
   column \(\log k\); `RT2` fails.
4. **Inserted-zero models:** preserve the physical block on one window,
   but do not simultaneously build the global prespectral factors
   `RT1--RT2`.

These separations are typed; they still do not prove that `EPG` exists for
\(\mathbb Z\).

## 7. What was obtained and what remains

```text
full Gram preserves positivity                              PROVED
rectangular corner preserves orientation                     PROVED
null corner forces R_L F=0                                   PROVED
the rectangular architecture avoids the quotient comb         PROVED
factoring a posteriori via H^(1/2) is circular                PROVED
Lambda*1=log fixes the oriented sum of fibers                   PROVED-CITED
null corner / rectangular coligation are new                    RETRACTED
local fiberwise Euler--Poisson isometry (EPG)                   NO-GO
joint nonlocal square prior to the pseudo-inverse                OPEN
row D                                                            OPEN
```

The next mathematical operation is not to look for another detector nor
another fiberwise factorization. It is to build, from the source, without
\(D_N^{\dagger/2}\), an operator \(\mathscr Z_{N,\varepsilon}\) for which

\[
 \mathcal M_N-
 \mathfrak q_N^*(D_N+\varepsilon I)^{-1}\mathfrak q_N
 =\mathscr Z_{N,\varepsilon}^*\mathscr Z_{N,\varepsilon}.
\]

It must preserve the cross term between \(d\Psi-dx\) and Gamma. Separating
them into two positive budgets returns to D.262 §3's `NO-GO`.
