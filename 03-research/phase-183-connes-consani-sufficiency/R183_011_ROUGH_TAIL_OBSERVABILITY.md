# R183.011 — Bilateral observability of the exterior leak

> **CORRECTION R183.012.** The support lemma (2.4) remains proved for the
> formal comb of translations. Identification (3.2) with the semilocal
> scattering and every operator consequence based on it are
> withdrawn: `E_S^{-1}` was not built on the physical Hilbert space.

## 0. Result

R183's search collides with phase 116 at a precise point. That phase already built the Julia Euler--Gamma systems and reduced a first failure to a clamped source \(\phi\ne0\) whose current

\[
 g=\mathcal A_\infty L^2E_T\phi                     \tag{0.1}
\]

vanishes on \(I_T=(-T,T)\). The new information from R183 is that, for \(S(q)\) and \(q=e^{2T}\), the causal and reflected co-Poisson combs separately observe the two tails of \(g\). This is proved only via support and unique factorization.

Closing D is now equivalent to a restricted bilateral observability: no Euler--Gamma current produced by a clamped source can be simultaneously invisible to the two Poisson-related observations.

## 1. Honest collision with phase 116

Phase 116 proves:

1. the positive reference column via Julia defects;
2. the Gamma ODE system and the Euler resolvents;
3. certified positivity in the initial window;
4. the reduction of every first failure to
   \[
   P_{I_T}\mathcal A_\infty L^2E_T\phi=0,
   \qquad \phi\in H_0^2(I_T).                       \tag{1.1}
   \]

What is open there is uniqueness \(\phi=0\). Hence a new graph
projection or a new sum of Julia dilations would repeat the corpus. The
only new admissible use of R183.004 is to apply the Poisson--Möbius
pair directly to the leak \(g\) of (1.1).

## 2. Exact separation of the tails

Let

\[
 P=1_{(-T,T)},\qquad
 Q_+=1_{[T,\infty)},\qquad Q_-=1_{(-\infty,-T]}.     \tag{2.1}
\]

If \(Pg=0\), write \(g=g_-+g_+\), with \(g_\pm=Q_\pm g\). For the rough monoid \(M_S\), define

\[
 V_S=\sum_{\substack{m\in M_S\\m>1}}m^{-1/2}D_m,
 \qquad (D_mf)(t)=f(t+\log m).                      \tag{2.2}
\]

The exact gap is

\[
                    \log m\ge2T.                   \tag{2.3}
\]

### Lemma 2. `PROVED`

On the locally finite core,

\[
 \boxed{PV_Sg=PV_Sg_+,\qquad
        PI V_S I g=PI V_S I g_-.}                   \tag{2.4}
\]

**Proof.** If \(t\in(-T,T)\) and \(m>1\), then
\(t+\log m>T\), except at a null endpoint. Hence \(D_mg_-(t)=0\), which
proves the first equality. Applying the same statement after the
reflection \(I f(t)=f(-t)\) proves the second. \(\square\)

Hence the observations

\[
 \mathcal O_+g:=PV_SQ_+g,
 \qquad
 \mathcal O_-g:=PI V_SI Q_-g                        \tag{2.5}
\]

do not mix the tails.

## 3. Möbius whitening

Let

\[
 M_S=\sum_{m\in M_S}{\mu(m)\over\sqrt m}D_m,
 \qquad M_SE_S=1,\quad E_S=1+V_S.                 \tag{3.1}
\]

R183.004's factorization is

\[
                    u_S=(IM_SI)E_S.                 \tag{3.2}
\]

At finite cutoff, \(M_S\) causally eliminates the paths of \(E_S\) without mixing their orientations. Hence (2.5) is the unwhitened version of two ports of the same scattering unitary. Poisson's reflection fixes the correspondence between their coefficients; it does not allow choosing the tails independently.

This is more than R170.878's Möbius identity: there, the exterior vector remained arbitrary. Here \(g\) belongs to the specific range

\[
 \mathscr G_T=
 \{\mathcal A_\infty L^2E_T\phi:\phi\in H_0^2(I_T)\}. \tag{3.3}
\]

## 4. What the support does not prove

Equalities (2.4) do not imply that \(\mathcal O_+\) or \(\mathcal O_-\) are injective on arbitrary tails. The observed intervals are

\[
                 (\log m-T,\log m+T),\qquad m\in M_S. \tag{4.1}
\]

They may overlap, and the weighted sums may cancel. R183.005 computes exactly those interferences via

\[
 c_h\!\left(\log{n\over m}\right).                 \tag{4.2}
\]

Hence the inference

\[
 \mathcal O_+g=0\Longrightarrow g_+=0               \tag{4.3}
\]

is false without additional hypotheses, or at the very least does not follow from the gap alone. The restriction \(g\in\mathscr G_T\) is essential.

## 5. Observability theorem that would close D

**Bilateral Rough Observability (BRO, OPEN, conditional on the vanishing
observation).** For \(q=e^{2T}\), let
\(S=S(q)\). If

\[
 \phi\in H_0^2(I_T),\qquad
 g=\mathcal A_\infty L^2E_T\phi,\qquad Pg=0,        \tag{5.1}
\]

and the two observations are related by Poisson's factorization
(3.2), then

\[
 \mathcal O_+g=0=\mathcal O_-g
 \quad\Longrightarrow\quad g=0
 \quad\Longrightarrow\quad\phi=0.                 \tag{5.2}
\]

A sufficient quantitative version is

\[
 \|g_-\|^2+\|g_+\|^2
 \le C_T\bigl(\|\mathcal O_-g\|^2+
               \|\mathcal O_+g\|^2\bigr),          \tag{5.3}
\]

for \(g\in\mathscr G_T\), with any \(C_T<\infty\). To exclude the
equality mode, injectivity alone suffices; to directly obtain the
contraction with budget one, the sharp version compatible with
D.247 is needed.

The first-loss theorem only delivers \(Pg=0\); it does not deliver
\(\mathcal O_\pm g=0\). Hence BRO does not yet exclude a first
contact. An additional bridge is needed:

\[
 Pg=0,\quad g\in\mathscr G_T
 \quad\Longrightarrow\quad
 \mathcal O_+g=\mathcal B_+(\phi),\qquad
 \mathcal O_-g=\mathcal B_-(\phi),                 \tag{5.4}
\]

where the boundary terms \(\mathcal B_\pm\) vanish by the clamped/Tate
conditions. Phase 116's differentiated Poisson identity,

\[
 Z\partial f+\mathscr JZ\partial\mathcal Ff
 =(C+\mathscr JC\mathscr J)Zf,                     \tag{5.5}
\]

relates the orientations, but the corpus proves that its physical Gram
matrix remains open. It has not been proved that its boundary side is zero.

## 6. Next admissible computation

Range \(\mathscr G_T\) is not arbitrary. Its transform is

\[
 \widehat g(\tau)
 =a_\infty(\tau)(\tau^2+\tfrac14)^2\widehat\phi(\tau), \tag{6.1}
\]

with \(\widehat\phi\) entire of type \(T\). The next step is to compute
\(\mathcal O_\pm g\) in this representation and determine its kernel within
the clamped Paley--Wiener space. It is not allowed to replace it by all of
\(L^2\), because observability fails there.

## 7. Logical status

* Collision with phase 116's Julia construction: **CONFIRMED**.
* Exact tail separation (2.4): **PROVED**.
* Common Poisson--Möbius factorization (3.2): **WITHDRAWN** as an
  operator identity; only the formal computation on a core remains.
* Injectivity on arbitrary tails: **NO-GO / not implied**.
* Observability on the clamped range \(\mathscr G_T\): **OPEN**.
* "First failure \(\Rightarrow\mathcal O_\pm g=0\)": **UNPROVED**; it is
  phase 116(99)'s open physical bridge.
* BRO plus the null bridge \(\Rightarrow\) absence of first failure:
  **PROVED CONDITIONALLY**.
* Row D: **OPEN**.
