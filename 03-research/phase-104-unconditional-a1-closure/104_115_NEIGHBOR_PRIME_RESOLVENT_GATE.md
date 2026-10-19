# 104_115 — Global resolvent gate and pivot to neighboring prime towers

## Result

The proposed scalar certificate was audited

\[
 \left\|(-S_\varepsilon)^{1/2}g_n+
 {\eta_n\over2}(-S_\varepsilon)^{-1/2}C_\varepsilon g_n
 \right\|_{\pi_\varepsilon}^{2},
 \qquad C_\varepsilon=i[X,S_\varepsilon].                 \tag{1}
\]

The global generator of exchanges between all towers does not define a
Markov operator in the Abel regime (\varepsilon\downarrow0). Even if
truncated, the cross term of (1) is identically zero for the real
Laguerre vector, and the Poisson equation does not in general satisfy the
compatibility condition with the layered kernel. Hence (1) cannot be the
A1 certificate as originally stated.

The pivot to exchanges between consecutive primes does produce a
well-defined self-adjoint generator. After projecting out the constants
of each layer, the Poisson equation is solved and the resolvent term is
positive. A complex twist recovers a phase term, but it changes sign with
the Laguerre degree. The correct successor is not another scalar
certificate: it must be a lift of at least two components coupling
adjacent Laguerre degrees via a local current between towers.

This document proves the gate and builds the local operator. It does not
prove A1 or RH.

---

## 1. The global generator does not exist near Abel

Write

\[
 \nu=(\nu_p)_p,\qquad m(\nu)=\prod_pp^{\nu_p},\qquad
 X(\nu)=\log m(\nu),
\]

and

\[
 \pi_\varepsilon(\nu)
 ={m(\nu)^{-1-\varepsilon}\over\zeta(1+\varepsilon)}.
                                                               \tag{2}
\]

The proposed generator moves one unit from tower (q) to tower (p), with
rate

\[
 r_{q\to p}(\nu)
 =\mathbf1_{\nu_q>0}\sqrt{\log p\log q}
   \left({q\over p}\right)^{(1+\varepsilon)/2}.              \tag{3}
\]

The rates satisfy formal detailed balance. Indeed, if

\[
 \nu'=\nu+e_p-e_q,
\]

then

\[
 {\pi_\varepsilon(\nu')\over\pi_\varepsilon(\nu)}
 =\left({q\over p}\right)^{1+\varepsilon},
\]

and hence

\[
 \pi_\varepsilon(\nu)r_{q\to p}(\nu)
 =\pi_\varepsilon(\nu')r_{p\to q}(\nu').                   \tag{4}
\]

But from state (\nu=e_q), the total outgoing rate is dominated, up to a
constant depending on (q), by

\[
 \sum_p {\sqrt{\log p}\over p^{(1+\varepsilon)/2}}.          \tag{5}
\]

The sum over primes in (5) diverges when
((1+\varepsilon)/2\le1), that is, for every
(0<\varepsilon\le1). This contains the entire regime needed to
take (\varepsilon\downarrow0). So the global generator has no finite
outgoing rate, and (1) is not defined.

## 2. Two independent algebraic obstructions

Suppose momentarily that the set of primes has been truncated, so that
(S_\varepsilon) is a real self-adjoint matrix on
(L^2(\pi_\varepsilon)). Let (X) be multiplication by (\log m) and

\[
 C_\varepsilon=i[X,S_\varepsilon].                         \tag{6}
\]

Then (C_\varepsilon) is self-adjoint. For every real vector (g),

\[
\begin{aligned}
 \langle C_\varepsilon g,g\rangle
 &=i\{\langle XS_\varepsilon g,g\rangle
       -\langle S_\varepsilon Xg,g\rangle\}\\
 &=i\{\langle S_\varepsilon g,Xg\rangle
       -\langle Xg,S_\varepsilon g\rangle\}=0.             \tag{7}
\end{aligned}
\]

In particular, for

\[
 g_n(\nu)=L_{n-1}^{(1)}(X(\nu)),                            \tag{8}
\]

the supposed interaction term (I_2) vanishes exactly. The norm in (1)
contains only two positive terms and retains none of the signed
orientation that was supposed to control (B_n).

There is also a large kernel. The exchanges preserve

\[
 \Omega(\nu)=\sum_p\nu_p,
\]

so that every function constant on a layer (\{\Omega=k\}) belongs to the
kernel of (S_\varepsilon). If (\mathbf1_k) is the constant on that layer,

\[
 \langle\mathbf1_k,C_\varepsilon g\rangle
 =-i\langle S_\varepsilon X\mathbf1_k,g\rangle,             \tag{9}
\]

which is in general nonzero. Hence

\[
 -S_\varepsilon h=C_\varepsilon g                           \tag{10}
\]

does not satisfy the Fredholm condition. The correct equation should be

\[
 -S_\varepsilon h=(I-\Pi)C_\varepsilon g,                  \tag{11}
\]

where (\Pi) projects onto the constants of each layer. The (I_3) of the
original proposal was likewise undefined without this projection.

## 3. Generator localized on neighboring towers

Enumerate the primes (p_1<p_2<\cdots), set

\[
 d_j=\log {p_{j+1}\over p_j},\qquad a_j=d_j^{-2},           \tag{12}
\]

and allow only the moves
(p_j\leftrightarrow p_{j+1}). The rates are

\[
\begin{aligned}
 r_{j\to j+1}(\nu)
 &=\mathbf1_{\nu_{p_j}>0}\,a_j
   \left({p_j\over p_{j+1}}\right)^{(1+\varepsilon)/2},\\
 r_{j+1\to j}(\nu)
 &=\mathbf1_{\nu_{p_{j+1}}>0}\,a_j
   \left({p_{j+1}\over p_j}\right)^{(1+\varepsilon)/2}.
                                                               \tag{13}
\end{aligned}
\]

Each state has at most (2\Omega(\nu)) distinct moves; its total rate is
finite. The same computation as in (4) proves detailed balance. The
factor (d_j^{-2}) is the natural diffusive normalization in the variable
(X=\log m): it exactly compensates the square of the jump between
nearby towers.

In every finite truncation of a layer, (S_\varepsilon^{\rm nb}) is
self-adjoint, irreducible, and has only the constants as kernel. The
projected equation

\[
 -S_\varepsilon^{\rm nb}h
 =(I-\Pi)C_\varepsilon^{\rm nb}g                            \tag{14}
\]

has a unique solution under the normalization (\Pi h=0), and

\[
 \langle h,(I-\Pi)C_\varepsilon^{\rm nb}g\rangle
 =\langle h,-S_\varepsilon^{\rm nb}h\rangle\ge0.           \tag{15}
\]

Thus the resolvent term is repaired, with no need to assume a uniform
spectral gap when the truncations are removed.

## 4. What a phase twist recovers and what it does not

Let (c_{xy}=\pi(x)r(x,y)=c_{yx}) be the conductance of an unoriented edge
and (d_{xy}=X(y)-X(x)). For

\[
 g_\tau(x)=e^{i\tau X(x)}F(X(x)),\qquad F\ \hbox{real},     \tag{16}
\]

the form of the commutator is

\[
 \boxed{
 \langle Cg_\tau,g_\tau\rangle
 =2\sum_{\{x,y\}}c_{xy}d_{xy}
   \sin(\tau d_{xy})F(X(x))F(X(y)).}                      \tag{17}
\]

The phase reappears, but the product of Laguerre functions in (17)
changes sign as it crosses its zeros. Hence closeness of towers does not
imply a uniform sign. Connecting only edges within the same lobe would
make the product positive, but it would separate precisely the boundaries
between lobes, where the sought cancellation lives.

The finite verification `tools/neighbor_prime_resolvent_check.py`, on the
layer (\Omega=1), confirms:

* detailed balance and self-adjointness with errors smaller than (3\cdot10^{-15});
* (\langle Cg_n,g_n\rangle=0) for the real vector;
* nonzero incompatibility of the Poisson equation without projecting;
* residual smaller than (3\cdot10^{-12}) in the projected equation;
* positivity of (15);
* sign change of the phase term: with 48 primes,
  (\varepsilon=1/2) and (\tau=1/5), it is approximately
  (+0.2111) at (n=24), (-0.3859) at (n=32), and
  (-0.7145) at (n=48).

## 5. Exact successor

The failure of (7) is intrinsic to a scalar certificate. The minimal form
that can have real interaction is a two-component lift. Set, for
example,

\[
 G_n=
 \begin{pmatrix}
 L_{n-1}^{(1)}(X)\\
 L_{n-2}^{(2)}(X)
 \end{pmatrix},                                          \tag{18}
\]

using that

\[
 {d\over dX}L_{n-1}^{(1)}(X)=-L_{n-2}^{(2)}(X).           \tag{19}
\]

The new target is to build a local current (J_\varepsilon),
antisymmetric and with (J_\varepsilon\mathbf1=0), on cycles of three
consecutive towers, and to prove an identity of the form

\[
 {3\over4}A_n-\delta_n-B_{n,\varepsilon}
 =\left\langle G_n,
 \begin{pmatrix}
 -S_\varepsilon^{\rm nb}&\eta_nJ_\varepsilon\\
 -\eta_nJ_\varepsilon&-S_\varepsilon^{\rm nb}
 \end{pmatrix}G_n\right\rangle
 +\mathcal R_{n,\varepsilon}.                            \tag{20}
\]

Here the real cross term does appear,

\[
 2\eta_n\left\langle
 L_{n-1}^{(1)}(X),J_\varepsilon L_{n-2}^{(2)}(X)
 \right\rangle,                                         \tag{21}
\]

which can preserve the orientation of the Laguerre recurrence. Cycles of
length three are necessary: a chain of neighbors is a tree and has no
nontrivial local current that is simultaneously antisymmetric,
conservative, and vanishing on constants.

The blocking step of (20) is no longer inverting a global generator. It
is a second-order Mecke identity relating the three-tower current to the
real linear term (B_{n,\varepsilon}), followed by a Schur bound for the
matrix in (20). This is the next falsifiable attack; (1) is withdrawn.

The script `tools/neighbor_prime_two_component_check.py` builds this
current on the finite layer (\Omega=1). It verifies (J^*=-J),
(J\mathbf1=0), and computes the exact Schur constant

\[
 \eta_{\max}
 =\left\|(-S)^{-1/2}J(-S)^{-1/2}\right\|^{-1}.             \tag{22}
\]

For 48 primes and (\varepsilon=1/2) it obtains
(\eta_{\max}\simeq0.7194) and a non-negative block form at all the
degrees tested. The cross term of adjacent degrees is positive for
(4\le n\le48) in that truncation. In larger truncations both signs are
observed when (\varepsilon) is still far from zero, while trials close
to the Abel regime become positive again. This is only a diagnostic: as
(\varepsilon) decreases, a growing fraction of the stationary measure
falls outside any fixed truncation. It is not used as a lemma.

## Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 neighbor_prime_resolvent_check.py
python3 neighbor_prime_two_component_check.py
```
</content>
