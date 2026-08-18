# 106.74 — Baker separation in the physical prime filter bank

## Purpose and verdict

The moving-bank observation suggests a precise high-frequency attack: use
the phases (t\log p) of small literal prime channels to dominate the
rapidly decaying archimedean cross terms.  The calculation gives a genuine
fixed-cluster theorem, but not a cofinal gap.

1. Baker's theorem gives polynomial anti-resonance for pure prime phases.
2. The physical theta quotient is stronger: one prime atom has a strictly
   positive floor on a single carrier, and on every fixed finite cluster
   translated to arbitrary carrier frequency.
3. That floor depends on the cluster.  When its dimension moves, the
   conditioning can collapse.  In the large-prime rank-one regime at least
   as many prime channels as exposed directions are required, and their
   strengths decay superexponentially.

Thus “more modes require more primes” is correct, but adding those primes
proves approximation, not the missing normalized sign.

## 1. Semantic audit

This route has close predecessors which must not be counted again.

* Phase 45, Proposition 5.6, proves polynomial Baker repulsion between
  (2\pi\mathbb Z/\log p) and (2\pi\mathbb Z/\log q).
* Phase 47, Document 148, proves that this helps only under an effective
  frequency cutoff.  Kronecker near-collisions at unbounded frequency make
  the unweighted global frame floor zero.
* Phase 50 shows that rational independence gives phase transversality but
  supplies no map from that fact to Weil inertia.

What is new below is the insertion of that question into the literal
theta-weighted atom of 106.31 and the rank-one asymptotic of 106.73.

## 2. What Baker proves

Write

\[
 \|y\|_{2\pi}=\min_{k\in\mathbb Z}|y-2\pi k|.
\]

### Lemma 1 — Scalar anti-resonance

There are effective constants (C,\kappa>0) such that

\[
 \boxed{|1-e^{it\log2}|^2+|1-e^{it\log3}|^2
 \ge C(1+|t|)^{-2\kappa}}                         \tag{1}
\]

for every real (t).

#### Proof

Let (k,l) be nearest integers to (t\log2/(2\pi)) and
(t\log3/(2\pi)), and set

\[
 \epsilon=\max(\|t\log2\|_{2\pi},\|t\log3\|_{2\pi}).
\]

Eliminating (t) gives

\[
 |k\log3-l\log2|
 \le {\log2+\log3\over2\pi}\epsilon.             \tag{2}
\]

The linear form is nonzero unless (k=l=0), by unique factorization.
Baker's theorem gives

\[
 |k\log3-l\log2|\ge C_1(1+|t|)^{-\kappa}.        \tag{3}
\]

Finally (|1-e^{iy}|\ge2\|y\|_{2\pi}/\pi).  Decrease
(C) to cover bounded (t). \(square\)

For two mode columns one must quotient out a common phase.  Two prime rows
are insufficient: the columns at (2,3) are proportional whenever
((t-s)\log(3/2)\in2\pi\mathbb Z).  Three primes remove that alias.

### Lemma 2 — Three-prime separation of two columns

Put (v(t)=(2^{it},3^{it},5^{it})^{\mathsf T}).  There are effective
(C,\kappa>0) such that

\[
 \boxed{\inf_{|\zeta|=1}\|v(t)-\zeta v(s)\|^2
 \ge C(1+|t-s|)^{-2\kappa}.}                      \tag{4}
\]

Equivalently, the smaller eigenvalue of
([v(s),v(t)]^*[v(s),v(t)]) has this lower bound.

#### Proof

Set (delta=t-s).  Small projective distance forces both
(e^{i\delta\log(3/2)}) and (e^{i\delta\log(5/2)}) close to (1).
Nearest integers (k,l) then make

\[
 k\log(5/2)-l\log(3/2)                            \tag{5}
\]

small.  The algebraic numbers (5/2) and (3/2) are multiplicatively
independent, so Baker gives the polynomial lower bound.  For three unit
complex numbers (z_j),

\[
 3-|\sum z_j|
 ={\sum_{i<j}|z_i-z_j|^2\over3+|\sum z_j|}
 \ge {1\over6}\sum_{i<j}|z_i-z_j|^2,             \tag{6}
\]

which converts it to the Gram bound. \(square\)

This is a two-column theorem.  Baker does not control a general sampling
determinant whose nodes are Riemann frequencies rather than logarithms of
algebraic numbers.

## 3. The physical envelope removes scalar resonance

Let

\[
 b(x)=\mathrm{sech}(x/2),\qquad
 a_u(x)=K(x)K(x-u),qquad u>0,
\]

and

\[
 D_u=\int a_u(x)b(x)^2dx,qquad
 C_u=\int a_u(x)b(x)b(x-u)dx.                     \tag{7}
\]

Reflection (x\mapsto u-x) gives
(int a_ub(x-u)^2=D_u), and

\[
 \boxed{2(D_u-C_u)=\int a_u|b(x)-b(x-u)|^2dx>0.} \tag{8}
\]

Strictness uses (a_u>0) and the fact that (b) is not (u)-periodic.

### Theorem 3 — Exact one-atom carrier floor

For (q_t(x)=b(x)e^{itx}),

\[
 \boxed{\mathcal J_u(q_t)=2D_u-2C_u\cos(tu)
 \ge2(D_u-C_u)>0}                                 \tag{9}
\]

for every real (t).

#### Proof

The exact factorization

\[
 q_t(x)-q_t(x-u)
 =e^{itx}\{b(x)-e^{-itu}b(x-u)\}                 \tag{10}
\]

followed by expansion and (7) proves (9). \(square\)

For the even mode (chi_t=b\cos(tx)), polarization yields

\[
 \mathcal J_u(\chi_t)=D_u-C_u\cos(tu)+R_u(t),     \tag{11}
\]

where (R_u) is a Fourier transform at (2t) of a smooth function with
all derivatives integrable.  Hence

\[
 |R_u(t)|\le C_{u,N}(1+|t|)^{-N}                 \tag{12}
\]

for every (N).  A single literal atom therefore controls every
sufficiently high individual real mode.  Baker is not needed for this
physical scalar statement.

## 4. Fixed translated clusters

Fix distinct real offsets (	au_1,\ldots,\tau_d), put

\[
 P_c(x)=\sum_{j=1}^dc_je^{i\tau_jx},\qquad
 q_{T,c}(x)=b(x)e^{iTx}P_c(x).                    \tag{13}
\]

### Theorem 4 — Fixed-cluster one-prime frame

For every (u>0) there is
(c(u;\tau_1,\ldots,\tau_d)>0) such that

\[
 \boxed{\mathcal J_u(q_{T,c})
 \ge c(u;\tau_1,\ldots,\tau_d)\|q_{T,c}\|_{\mu_K}^2} \tag{14}
\]

for every real (T) and every (c\in\mathbb C^d).

#### Proof

The norm is independent of (T).  After removing the unit carrier, the
atom depends on (T) only through (z=e^{-iTu}\in\mathbb T):

\[
 \int a_u|bP_c-zb(\cdot-u)P_c(\cdot-u)|^2.        \tag{15}
\]

Minimize (15) on the compact set

\[
 \{|z|=1,\ \|bP_c\|_{\mu_K}=1\}.                 \tag{16}
\]

If the minimum were zero, (q=bP_c) would satisfy
(q(x)=zq(x-u)), hence (|q|) would be (u)-periodic.  But (P_c) is
bounded and (b(x)\to0) at both ends, so (q\to0).  A periodic function
with that limit is zero, contradicting (16). \(square\)

This is the real gain over the old unweighted Phase-47 frame.  It is
uniform in the common carrier, but its constant depends on the entire
offset list and its dimension.

## 5. Why more modes still require more primes

The large-prime theorem 106.73 gives, on a (d)-mode block,

\[
 P_p=\beta_pv_pv_p^*+\mathcal E_p,qquad
 \beta_p\asymp(\log p)p^2e^{-2\pi p}.             \tag{17}
\]

Therefore fewer than (d) leading rank-one channels leave a nonzero
coefficient vector orthogonal to every (v_p).  In this regime,

\[
 \boxed{d\text{ independent exposed directions require at least }d
 \text{ new prime channels}.}                     \tag{18}
\]

With (d) channels the determinant is

\[
 \det(V^*WV)=\left(\prod_{i=1}^d\beta_{p_i}\right)|\det V|^2. \tag{19}
\]

Baker controls the pairwise alias in Lemma 2, but not the higher
determinant in (19).  Coherent cancellation among three or more columns is
not a linear form in logarithms.  Moreover, resolving frequencies up to
(Z) in the asymptotic formula requires (p\gg Z^2), where

\[
 \beta_p\le e^{-cZ^2}                              \tag{20}
\]

up to polynomial factors.  A polynomial Baker bound cannot cancel that
attenuation without a matching theorem for the complete deficit and the
mode-Gram conditioning.

## 6. Sharp verdict for the moving schedule

Theta weighting changes the finite-dimensional verdict: a fixed cluster
translated to infinity has a genuine one-prime gap (14), whereas the old
unweighted frame had only Diophantine transversality.  It does not change
the cofinal verdict.

The unresolved spectrum below (1/2) is already compact and centrally
localized by 106.47; high-frequency Gamma coercivity has removed the
essential tail.  What remains is the moving normalized contraction

\[
 \Theta_M(\varepsilon)
 =\|C_M^-(A_M^*A_M+\varepsilon I)^{-1/2}\|^2.      \tag{21}
\]

Theorems 3--4 do not bound (21) uniformly as (M\to\infty).  The cutoff
must grow with the mode space, but the literal missing theorem is still a
comparison between the shrinking deficit, the conditioning of (N_M),
and the accumulated prime channels.  Baker alone supplies none of those
three comparisons.

### Established here

* effective scalar and two-column phase bounds, (1) and (4);
* the exact physical one-atom carrier floor (9);
* the uniform fixed-cluster frame (14);
* the rank necessity (18) for asymptotic large-prime sensors.

### Not established

* a lower bound for arbitrary high-dimensional sampling determinants on
  the Riemann divisor;
* uniform control of the moving mode Gram;
* the cofinal contraction (21).

The Baker/filter-bank idea is therefore a completed high-carrier gate, not
the global sign theorem.
