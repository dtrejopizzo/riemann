# R170_835 — Source–innovation–port quadratic map and exact residual

Continuation of R170_834. Status: the unique finite
map provided by the existing operators is built and its metric is
computed exactly. That map reaches the exponential columns of R170_829,
not the canonical Hardy port produced by the source. It is proved that a
universal factorization of the canonical port by a finite number of Gamma
moments is impossible. Over the finite radical the factorization exists
algebraically, but it uses the inverse of the restricted observation and
does not constitute an arithmetic law nor a uniform construction. The
residual between the three objects is completely localized.

## 0. Verdict

Fix a hypothetical first-contact window, a parity sector

\[
 Z_\varepsilon=\{F\in\ker H_T:JF=\varepsilon F\},
 \qquad \varepsilon\in\{+1,-1\},
 \tag{0.1}
\]

and a finite number of moments for which \(R_L|_{Z_\varepsilon}\) is
injective. Let

\[
 D=D_{N,L},\qquad
 \mathcal J_+=(I-D)^{1/2}R_L,\qquad
 \mathcal J_-=(I-D)^{1/2}R_LJ .
 \tag{0.2}
\]

On \(Z_\varepsilon\), both orientations have the same energy and

\[
 {1\over2}\bigl(\mathcal J_+^*\mathcal J_+
                  +\mathcal J_-^*\mathcal J_-\bigr)
 =D_\Delta:=R_L^*(I-D)R_L .
 \tag{0.3}
\]

This note proves four statements.

1. The exterior candidate of R170_829 does factor canonically through the
   innovations (0.2). Its slope Gram matrix is a squared Cauchy matrix,
   computed in (3.7). Hence its difference from \(D_\Delta\) is an
   explicit finite matrix, (3.9).
2. That candidate is not the canonical Hardy port of R161_015. In fact
   there is no universal operator on the ambient space that reconstructs
   its product germ, on a carrier preserving the critical jet, from
   \(R_LF\) with \(L<\infty\). The obstruction is seen by evaluating at a
   critical zero: it would force an oscillatory exponential to be
   expressed as a finite combination of the real Gamma exponentials.
3. Since \(R_L|_{Z_\varepsilon}\) is injective, over the radical there
   exists a unique a posteriori factor. Its metric defect is exactly
   \[
    \mathcal S_{\rm can}-D_\Delta,
   \]
   where \(\mathcal S_{\rm can}\) is minus the causal slope of the Hardy
   norm. Building that factor through PC, without inverting the
   observation of the radical, is precisely the open theorem.
4. The identity \(\Lambda*1=\log\) enters, in a load-bearing way, only in
   the finite PC carrier of §2. It does not enter the column Gram of §3.
   That is why the column map passes the positive-weight systems that
   have first contacts and cannot close D. The missing minimal datum is a
   mixed quadratic law identifying the finite PC carrier with the
   **inverse orientation** of the Hardy slope and with \(D_\Delta\) in the
   same equality.

No new sign, vanishing of the radical, nor D is proved.

## 1. Non-duplication check and scope corrections

The following construction does not re-present as new the pieces already
closed in the corpus.

- R161_015 fixes the Hardy gauge
  \(\Theta_T(s)=e^{-T(s-1)}/s\) and proves
  \[
   N_T'(0+)=-2\int_T^\infty(t-T)|g_+(t)|^2dt .
   \tag{1.1}
  \]
- R161_016 proves that a contraction with the direct orientation only
  recovers the automatic sign of (1.1). The closure needs the input and
  output exchanged before taking the metric.
- R161_017–019 compute the scattering defect and the rigidity of the
  Gamma pole lattice. R161_018 formulates the quadratic goal before the
  linear limit. Its linear no-go was corrected in R161_075 according to
  the carrier; it was then reinstated in R162_2302 for the weak carrier:
  there the linear limit is zero for every primitive source and does not
  distinguish the first contact.
- R161_052–065 already try coligations, boundary powers, and
  concomitants. Corrections R161_056 and R161_065 show, respectively,
  that the unitary phase has the mean tangent, not the critical
  difference, and that the proposed concomitant recomposes the exterior
  commutator already audited.
- R161_068 builds the Gamma–Euler observation with weights
  \(-\zeta'/\zeta(2m+1)\). R161_070–072 give the finite detector, the
  collar, and the exact balance; the latter works for arbitrary positive
  weights and recombines into the original equation. R161_073–074 give
  the stabilized inversion and its residual certificate. R162_2502 proves
  that an abstract positive comparison of that detector with \(H_T\) is
  equivalent to excluding the kernel, and that its diagonal part suffers
  the positivity lock. In particular, the \(K_\delta\) suggested in
  R161_068 was never built: its global adjoints mixed carriers, and
  R161_070 replaced it with the correctly typed compressed collar.
- Paper 46 proves finite PC, the collar
  \(R_LB_N=D_{N,L}R_L-\mathcal E_{N,L}\), the strict positivity of
  \(D_\Delta\), and the balance on the radical.
- R170_823–830 preserve PC, the two orientations, and the multiscale
  flux, but do not produce a sign. R170_831 computes the Green response
  of the exterior columns. R170_834 proves that the Hardy port of a
  source is canonical, while its use as an extension of the Tate vector
  on arbitrary columns is not.

The new piece of this note is the exact Gram of the column map, the
rank obstruction to identifying it with the source port, and the
decomposition of the source–column–detector residual.

## 2. The finite quadratic carrier where \(\Lambda*1=\log\) enters

Keep \(M,N\) finite. Use the notation of Paper 46:

\[
\begin{aligned}
 S_N&=\sum_{n\le N}n^{-1/2}\tau_{\log n},&
 K_N&=\sum_{n\le N}(\log n)n^{-1/2}\tau_{\log n},\\
 L_M&=\sum_{d\le M}\Lambda(d)d^{-1/2}\tau_{\log d},&
 H_{M,N}&=L_MS_N-K_N,\\
 E_N&=S_N\mathscr F-JS_N,&
 A_M&=m(D)-(L_M+L_M^*).
\end{aligned}
\tag{2.1}
\]

On the regular kernel we have

\[
 S_NA_M\mathscr F
 =\{X,E_N\}-L_M^*E_N-JH_{M,N}-H_{M,N}\mathscr F .
 \tag{2.2}
\]

If \(M\ge N\), then

\[
 H_{M,N}=\sum_{k>N}{h_{M,N}(k)\over\sqrt k}\tau_{\log k},
 \qquad
 h_{M,N}(k)=\sum_{\substack{dm=k\\d\le M,\ m\le N}}\Lambda(d).
 \tag{2.3}
\]

The absence of coefficients for \(k\le N\) does not come from positivity:
it uses exactly

\[
 \sum_{d\mid k}\Lambda(d)=\log k.
 \tag{2.4}
\]

### 2.1. The two PC innovations produced by the source

Let \(P=P_T\), \(Q=I-P\), and for a first-contact source write

\[
 A_MF=r_F+\ell_F,
 \qquad r_F=PA_MF\in\operatorname{span}\{e^{-t/2},e^{t/2}\},
 \qquad \ell_F=QA_MF .
 \tag{2.5}
\]

Include the polar renormalization in \(S_N^{\rm ren}\) and in the
right-hand side \(\mathscr R_{M,N}^{\rm ren}\) of (2.2). R161_005–006
prove

\[
 P\mathscr R_{M,N}^{\rm ren}\mathscr FF
 -PS_N^{\rm ren}r_F
 =PS_N^{\rm ren}\ell_F
 =\Delta_{N,T}^{R}\ell_F-e^{-t/2}a_-(\ell_F),
 \tag{2.6}
\]

where

\[
 a_-(\ell_F)=\int_{-\infty}^{-T}e^{y/2}\ell_F(y)\,dy .
 \tag{2.7}
\]

Reflecting the same identity gives directly

\[
 PS_{N,-}^{\rm ren}\ell_F
 =\Delta_{N,T}^{L}\ell_F-e^{t/2}a_+(\ell_F),
 \qquad S_{N,-}^{\rm ren}=JS_N^{\rm ren}J .
 \tag{2.8}
\]

Hence the finite, correctly centered innovations are

\[
 \boxed{
 \mathcal I_{M,N}F=
 \bigl(\Delta_{N,T}^{R}\ell_F,
       \Delta_{N,T}^{L}\ell_F\bigr).}
 \tag{2.9}
\]

Formulas (2.6)–(2.9) retain:

- both orientations;
- the polar continuum, because \(S_N^{\rm ren}\) is used;
- the two Tate scalars \(a_\mp(\ell_F)\);
- the hyperbolic divisor \(H_{M,N}\), and hence (2.4).

They do not yet contain a signed metric on (2.9). Taking
\(\|\mathcal I_{M,N}F\|^2\) loses the orientation of \(A_M\), exactly as
in R161_002 and Paper 46.

### 2.2. Defect under coefficient substitution

Replace \(\Lambda(d)\) by \(a(d)\) and set

\[
 \delta_a(k)=\sum_{d\mid k}a(d)-\log k.
 \tag{2.10}
\]

For \(k\le N\le M\), the interior coefficient of \(H^a_{M,N}\) is exactly
\(\delta_a(k)\). Thus, in (2.2), the two oriented terms contribute the
explicit defect

\[
 -J\!\sum_{k\le N}{\delta_a(k)\over\sqrt k}\tau_{\log k}
 -\left(\sum_{k\le N}{\delta_a(k)\over\sqrt k}\tau_{\log k}\right)
  \mathscr F,
 \tag{2.11}
\]

in addition to the obvious changes in \(L_M^*E_N\) and in the tail
\(k>N\). For \(a=\Lambda\), (2.11) vanishes exactly. This is the line
through which the geometry of the integer divisors enters the map. The
diagonal detector of the next section does not contain (2.11).

## 3. Finite map from Gamma–Euler innovations to exterior columns

Set, as in R170_829–834,

\[
 a_m=2m+\tfrac12,\qquad
 b_m=\sqrt{a_m}\,e^{-a_m(T+\delta_0)},\qquad 1\le m\le L,
 \tag{3.1}
\]

with \(\delta_0>0\) fixed. For \(c\in\mathbb C^L\), define

\[
 (\iota_+c)(t)={\bf1}_{t>T}\sum_{m\le L}b_mc_me^{-a_mt},
 \qquad \iota_-=J\iota_+ .
 \tag{3.2}
\]

The source–innovation map is (0.2). The innovation–column map was already
implicit in R170_829 and is now written with its correct type:

\[
 \boxed{
 \mathcal K_+=\iota_+(I-D)^{1/2},\qquad
 \mathcal K_-=\iota_-(I-D)^{1/2}.}
 \tag{3.3}
\]

Indeed,

\[
 \mathcal K_+\mathcal J_+F
 =\iota_+(I-D)R_LF,
 \tag{3.4}
\]

which is exactly \(Y_+F\) of R170_829; the reflected formula gives the
other orientation. No extension of the Tate vector has been chosen: (3.3)
is only the exterior Gamma block.

### 3.1. Slope Gram matrix

Let the positive forms be

\[
 W_+=2(X-T)\quad\hbox{on }L^2(T,\infty),
 \qquad
 W_-=2(-X-T)\quad\hbox{on }L^2(-\infty,-T).
 \tag{3.5}
\]

An elementary computation gives

\[
 2\int_T^\infty(t-T)e^{-(a_m+a_n)t}\,dt
 ={2e^{-(a_m+a_n)T}\over(a_m+a_n)^2}.
 \tag{3.6}
\]

Hence

\[
 \boxed{
 G^{\rm col}_{mn}
 ={2b_mb_ne^{-(a_m+a_n)T}\over(a_m+a_n)^2},
 \qquad
 \mathcal K_+^*W_+\mathcal K_+
 =(I-D)^{1/2}G^{\rm col}(I-D)^{1/2}.}
 \tag{3.7}
\]

Reflection produces the same matrix. In particular, the bilateral Gram
with the sum of orientations used in R170_834 is

\[
 \mathcal S_{\rm col}
 =
 R_L^*(I-D)G^{\rm col}(I-D)R_L
 +J R_L^*(I-D)G^{\rm col}(I-D)R_LJ
 .
 \tag{3.8}
\]

Everything in (3.8) is finite and explicit. On \(Z_\varepsilon\), each
orientation has detector \(D_\Delta\), and the average of both does too,
by (0.3). Since the obligation of R170_834 sums the two responses but
contains a single copy of \(D_\Delta\), the metric residual with that
same convention is

\[
 \boxed{
 \begin{aligned}
 \mathcal R_{\rm col}
  &: =\mathcal S_{\rm col}-D_\Delta\\
  &=\sum_{\sigma=\pm}
  \mathcal J_\sigma^*
  \left[(I-D)^{1/2}G^{\rm col}(I-D)^{1/2}-{1\over2}I\right]
  \mathcal J_\sigma
  \quad\hbox{on }Z_\varepsilon .
 \end{aligned}}
 \tag{3.9}
\]

This is an identity, not an estimate. The corpus does not prove a sign
for the central matrix of (3.9). More importantly: even a favorable sign
in (3.9) would refer to the columns (3.2), not to the Hardy product port.

### 3.2. Relation to the Green matrix of R170_834

Denote by \(M_{\rm H}\) the matrix (5.3) of R170_834, restricted to
\(Z_\varepsilon\):

\[
 M_{\rm H}
 =\operatorname{Herm}\!\left[
  (\Gamma_{+,M}-\Theta_+^{\rm H})C_+
 +(\Gamma_{-,M}-\Theta_-^{\rm H})C_-
 \right].
 \tag{3.10}
\]

Define

\[
 \mathcal R_{\rm H}=M_{\rm H}-D_\Delta .
 \tag{3.11}
\]

The response \(\Gamma_{\pm,M}\) and the polar block
\(\Theta_\pm^{\rm H}\) compute \(M_{\rm H}\); the Gram (3.8) computes the
norm slope of the same columns. By simple addition and subtraction,

\[
 \boxed{
 \mathcal R_{\rm H}
 =(M_{\rm H}-\mathcal S_{\rm col})+\mathcal R_{\rm col}.}
 \tag{3.12}
\]

Thus the residual of R170_834 already splits into two finite blocks:

1. Green response minus column metric;
2. column metric minus Gamma–Euler detector.

Both are computable with the existing formulas. Neither identifies the
column with the port produced by the source.

## 4. The Hardy port produced by the source

Denote by

\[
 \mathcal G_+:Z_\varepsilon\longrightarrow L^2(T,\infty),
 \qquad
 \mathcal G_-:Z_\varepsilon\longrightarrow L^2(-\infty,-T)
 \tag{4.1}
\]

the canonical ports of R161_009 and R161_015, including the polar
corrections determined by the source. They are linear maps. If
\(g_+(F)=\mathcal G_+F\), then

\[
 N_{+,F}(\eta)
 =\|e^{-\eta(X-T)}g_+(F)\|^2,
 \qquad
 -N_{+,F}'(0+)=\langle g_+(F),W_+g_+(F)\rangle .
 \tag{4.2}
\]

The left orientation gives the reflected formula. Define the bilateral
slope form

\[
 \boxed{
 \mathcal S_{\rm can}
 =
 \mathcal G_+^*W_+\mathcal G_+
 +\mathcal G_-^*W_-\mathcal G_-\succeq0.}
 \tag{4.3}
\]

In a parity sector, each term of (4.3) is the positive form
\(E_T^{\rm PC}\) of R161_015; their sum is the bilateral convention of
this note.

### 4.1. No universal factorization by finite moments exists

For this statement use the product germ of R161_007,
\[
 \mathbf G_+^{\rm prod}(F)(z)
 =-\zeta'(\tfrac12+z)K_F(z)
  -\zeta(\tfrac12+z)Q_{+,T}(z).
 \tag{4.4}
\]
It is defined on the ambient space of sources. The port
\(\mathcal G_+F\) of (4.1) is its corrected Hardy realization when \(F\)
is a first-contact vector; the polar correction does not alter its values
at the nontrivial zeros.

**Proposition 4.1 (finite-rank obstruction; PROVED).** For no
\(L<\infty\) is there a linear operator \(\mathcal K\), independent of
the source, that factors the product germ on a carrier preserving the
critical-jet evaluation,

\[
 \mathbf G_+^{\rm prod}(F)=\mathcal K R_LF
 \tag{4.5}
\]

as an identity over the ambient space of smooth compactly supported
sources. In particular there is no such universal operator identity from
which the factorization over every possible radical could be obtained by
restriction.

**Proof.** Let \(\rho=\tfrac12+i\gamma\) be a simple critical zero.
R161_007 gives

\[
 \mathbf G_+^{\rm prod}(F)(i\gamma)
 =-\zeta'(\rho)K_F(i\gamma).
 \tag{4.6}
\]

If (4.5) held on a jet-preserving carrier, the functional
\(F\mapsto K_F(i\gamma)\) would belong to the span of
\(F\mapsto K_F(a_m)\), \(m\le L\). By duality of
\(C_c^\infty(-T,T)\), there would exist constants \(c_m\) such that

\[
 e^{-i\gamma t}=\sum_{m\le L}c_me^{-a_mt}
 \quad\hbox{for almost every }t\in(-T,T).
 \tag{4.7}
\]

Both sides are entire in \(t\), so (4.7) would hold on all of
\(\mathbb C\). Exponentials of distinct exponents are linearly
independent; since \(i\gamma\notin\{a_1,\ldots,a_L\}\), this is
impossible. ∎

The proof uses the product jet (4.6), whose arithmetic origin is
precisely \(\Lambda*1=\log\). The Tate/polar correction cannot repair the
factorization because it vanishes at every nontrivial zero.

### 4.2. Factorization restricted to the radical

Since \(R_L|_{Z_\varepsilon}\) is injective, a unique factor does exist
over the finite image

\[
 \mathscr R_{N,L}:=\operatorname{Ran}
 \left(\mathcal J_+|_{Z_\varepsilon}\right)
 \tag{4.8}
\]

given by

\[
 \boxed{
 \mathcal K_{\rm can}^{Z}(\mathcal J_+F)
 :=\mathcal G_+F.}
 \tag{4.9}
\]

The left orientation is defined analogously. This formula is not a PC
construction: it uses \((\mathcal J_+|_{Z_\varepsilon})^{-1}\), depends on
the unknown radical, and does not give a canonical extension to
\(\mathbb C^L\). It is the exact analogue, at the level of ports, of the
stabilized inversion of R161_073. R162_2502 explains why turning such a
factorization into a uniform comparison already has the strength of Gate
1.

Nevertheless, (4.9) gives a useful metric identity. In bilateral
notation, define

\[
 \mathcal J_{\rm bi}F
 =(\mathcal J_+F,\mathcal J_-F),\qquad
 W_{\rm bi}=W_+\oplus W_-,
 \qquad
 \mathcal G_{\rm bi}F
 =(\mathcal G_+F,\mathcal G_-F),
 \tag{4.10}
\]

and let \(\mathcal K_{\rm can}^Z\) act diagonally on the two
orientations. Then

\[
 \boxed{
 \mathcal S_{\rm can}
 =\mathcal J_{\rm bi}^*
   (\mathcal K_{\rm can}^{Z})^*W_{\rm bi}
   \mathcal K_{\rm can}^{Z}\mathcal J_{\rm bi}.}
 \tag{4.11}
\]

Hence the source–detector residual is exactly

\[
 \boxed{
 \mathcal R_{\rm src}
 :=\mathcal S_{\rm can}-D_\Delta
 =\mathcal J_{\rm bi}^*
  \left[(\mathcal K_{\rm can}^{Z})^*W_{\rm bi}
        \mathcal K_{\rm can}^{Z}-{1\over2}I\right]
  \mathcal J_{\rm bi}.}
 \tag{4.12}
\]

This identity does not assign a sign to the bracket. It names it without
losing the interference between channels.

## 5. Exact decomposition of the residual and orientation of the closure

The three metrics are related by

\[
 \boxed{
 \mathcal S_{\rm can}-D_\Delta
 =\underbrace{(\mathcal S_{\rm can}-\mathcal S_{\rm col})}
              _{\mathcal R_{\rm range}}
 +\underbrace{(\mathcal S_{\rm col}-D_\Delta)}
              _{\mathcal R_{\rm col}}.}
 \tag{5.1}
\]

The second term is computed in (3.9). The first is the rank defect that
R170_834 localized qualitatively: it identifies the Gamma tail built from
columns with the product port built from the source. Proposition 4.1
proves that \(\mathcal R_{\rm range}=0\) cannot come from a universal
factorization identity, extended to the ambient space on a
jet-preserving carrier, for any finite \(L\). Its eventual vanishing or
control only over a first-contact radical would be a new law.

The sign of the arrow must also be preserved. Set
\(N_T^{\rm bi}=N_{+,T}+N_{-,T}\). Its causal slope is

\[
 (N_T^{\rm bi})'(0+;F)
 =-\langle F,\mathcal S_{\rm can}F\rangle.
 \tag{5.2}
\]

A direct identification of metrics only reproves
\(-(N_T^{\rm bi})'(0+)\ge0\). If the inverse theorem requested in R161_016
is realized through the specific detector \(D_\Delta\), its first-order
version must give

\[
 (N_T^{\rm bi})'(0+;F)=\langle F,D_\Delta F\rangle,
 \quad\hbox{that is,}\quad
 \boxed{\langle F,(\mathcal S_{\rm can}+D_\Delta)F\rangle=0}
 \quad\hbox{on a first-contact vector.}
 \tag{5.3}
\]

Since both forms in (5.3) are nonnegative and \(D_\Delta\) is positive
definite on the detected radical, (5.3) immediately forces \(F=0\). This
shows two things at once:

- an ordinary Hilbertian innovation–port map cannot by itself produce the
  inverse sign;
- the missing content must be a two-orientation flux identity, with a
  signed boundary term, not another single-tail norm.

The relation with R170_834 can be written without hiding the defect.
With

\[
 \mathcal R_{\rm H}=M_{\rm H}-D_\Delta,
 \qquad
 \mathcal R_{\rm or}=M_{\rm H}+\mathcal S_{\rm can},
 \tag{5.4}
\]

we have the identity

\[
 \boxed{
 \mathcal R_{\rm or}-\mathcal R_{\rm H}
 =\mathcal S_{\rm can}+D_\Delta.}
 \tag{5.5}
\]

Thus, the inverse law is equivalent to the same finite quadratic carrier
producing the two residuals of (5.4). Proving separately
\(M_{\rm H}=-\mathcal S_{\rm can}\) and
\(M_{\rm H}=D_\Delta\) would be a
stronger version of the same closure. Neither of these equalities is in
the corpus.

## 6. Minimal additional datum

The available operators give two exact arrows from the source: write
\(\mathcal J_{N,L}:=\mathcal J_{\rm bi}\) for short.

\[
 F\longmapsto\mathcal I_{M,N}F,
 \qquad
 F\longmapsto\mathcal J_{N,L}F
       \longmapsto\iota_\pm(I-D)R_LF.
 \tag{6.1}
\]

And they separately give the canonical port

\[
 F\longmapsto(\mathcal G_+F,\mathcal G_-F).
 \tag{6.2}
\]

They do not give a source-independent arrow from (6.1) to (6.2). The
minimal missing datum is not another detector nor another Tate
extension. It is a finite, oriented sesquilinear form

\[
 \mathfrak B_{M,N,L}^{\varepsilon}(F,G),
 \tag{6.3}
\]

derived from the mixed polarization of the two PC equations —
difference \(E_N\) in one slot and complementary sum in the other, as
R161_056–057 require — with these two simultaneous readings:

1. **Euler–Gamma reading:** after inserting the exact collar, its leading
   term is
   \(\langle\mathcal J_{N,L}F,\mathcal J_{N,L}G\rangle\), with
   \(D_\Delta\) and both orientations counted once.
2. **Inverse Hardy reading:** after the polar/crossed-Tate correction
   produced by the same source, its leading term is
   \(-\langle W_{\rm bi}^{1/2}\mathcal G_{\rm bi} F,
            W_{\rm bi}^{1/2}\mathcal G_{\rm bi} G\rangle\).
3. **Same residual:** the Poisson, hyperbola, collar, polar, and Tate
   terms that are not leading must be literally the same in both readings
   before any limit. Subtracting, (5.3) remains.
4. **Load-bearing arithmetic:** the step identifying the two residuals
   must use the vanishing of (2.11), not only the positivity of
   \(D_{N,L}\).

Without the third condition, two formulas with different errors are
obtained and there is no comparison. Without the fourth, the construction
works for the positive-weight systems of R161_072 and R162_2502 and is
false as a closure law.

## 7. Falsifiers

### 7.1. Positive weights, elimination, and Type I

Formulas (0.2), (3.3), (3.7), and (3.9) remain valid when \(\Lambda(n)\)
is replaced by weights \(w_n\ge0\). It suffices to replace \(D\) by

\[
 d_m^w=\sum_n w_nn^{-(a_m+1/2)}.
 \tag{7.1}
\]

In particular they survive for a single translation, for
\(\Lambda\mathbf1_{n\ge5}\), and for the Type I families that have first
contacts. Hence the column map and any sign deduced only from its Gram
fail the weight falsifier. What those models do not preserve is
\(\delta_a(k)=0\) for all \(k\le N\) in (2.10).

### 7.2. Davenport–Heilbronn, Epstein, and Beurling

A functional equation and Gamma poles allow analogues of ports and
observations for Davenport–Heilbronn or Epstein; they do not provide the
finite product (2.3) with the integer comb and the coefficients of
\(\Lambda\). In Beurling systems one may have
\(\Lambda_B*1_B=\log_B\), but the additive comb and its transform are not
the comb of \(\mathbb Z\). A valid law must use (2.2) and the exact
vanishing (2.11) simultaneously, not only one of these two facts.

### 7.3. Sign reversal

\(D_\Delta\), \(G^{\rm col}\), and the port norms do not change under a
formal reversal of the sign of the Weil operator. The mixed
polarization of \(E_N\) with the complementary sum does change its
orientation. This confirms that (6.3) must be mixed; a diagonal square
cannot satisfy (5.3).

### 7.4. Positive eigenvectors and minimality

Nothing in §§2–5 yet uses that the window is the **first** contact. The
same matrices can be evaluated on an eigenvector with positive
eigenvalue. Paper 46 and R161_081 show there

\[
 Q_{N,L}(F)=-2\sum_{m\le L}(d_{m,N}+\lambda)|(R_LF)_m|^2<0.
 \tag{7.2}
\]

Hence a sign law deduced from (3.9) without a window variation would also
be false. Form (6.3) must contain the boundary-motion term or an
equivalent consequence of the minimality of \(T\).

### 7.5. Weak linear limit

R162_2302 proves that the renormalized linear limit vanishes for every
primitive source in the weak carrier. Passing to that limit before
forming (6.3) eliminates precisely the finite residue containing (2.11).
That is why the required law must be proved at finite \(M,N,L\) and only
then admit a limit with metric control.

## 8. Ledger

```text
finite PC carrier with polar, Tate, and two orientations      PROVED
exact entry of Lambda*1=log into the support of H_M,N         PROVED
Gamma–Euler innovation map -> columns iota_±                  PROVED
column slope Gram matrix                                      PROVED / EXPLICIT
residual R_col versus D_Delta                                 PROVED / EXPLICIT
decomposition R_H=(M_H-S_col)+R_col                            PROVED
universal factorization by R_L on jet carrier, finite L       FALSE
factorization restricted to the radical                       EXISTS A POSTERIORI
construction of that factorization from PC                    OPEN
identification columns = source port                          UNIVERSALLY FALSE / OPEN ON Z
inverse law S_can + D_Delta = 0 at first contact               OPEN / CLOSURE
finite mixed form B_(M,N,L)^epsilon of §6                      NOT BUILT
non-perturbative use of first-contact minimality               ABSENT
uniformity in T                                                ABSENT
D and the global inequality                                    OPEN
```

The next admissible piece is now precisely typed: build the mixed form
(6.3) from the two orientations of PC, and prove that its two expansions
have **the same residual**. Another column norm, another Gamma detector,
or a new choice of Tate port cannot fill that gap.
