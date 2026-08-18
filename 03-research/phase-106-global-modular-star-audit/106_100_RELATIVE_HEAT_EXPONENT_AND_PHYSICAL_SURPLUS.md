# 106.100 — A global relative-heat exponent for the physical surplus

## 1. Purpose and result

The heat-core theorem proves form-core exhaustion but does not determine the
sign of the completed form.  This note constructs a global trace-class heat
observable even though neither of the two heat semigroups is assumed to be
trace class.  Its exponential decay rate detects the missing spectral floor
exactly.

Let

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp,
 \qquad A=L|_{\mathscr C},
 \qquad S=A+\frac12 I,
 \tag{1}
\]

where \(L\geq0\) is the self-adjoint operator associated with the complete
ordinary-prime--Gamma energy.  Thus the desired physical surplus is

\[
 \boxed{A\geq\frac12 I.}                              \tag{2}
\]

There is a positive injective trace-class operator \(V\) on \(\mathscr C\)
for which

\[
 \Theta_V(t)=\mathrm{Tr}
 \bigl(e^{-tS}-e^{-t(S+V)}\bigr),\qquad t>0,          \tag{3}
\]

is well defined, nonnegative, and satisfies

\[
 \boxed{
 A\geq\frac12 I
 \quad\Longleftrightarrow\quad
 \limsup_{t\to\infty}\frac1t\log\Theta_V(t)\leq-1.}
 \tag{4}
\]

The construction is unconditional.  The implication from the right side of
(4) to the physical surplus uses the already proved essential threshold
\(\sigma_{\rm ess}(A)\subset[1/2,\infty)\).  Formula (4) is therefore a
faithful heat detector, not a proof of the remaining exponent bound.

## 2. A trace-class boost inside the heat core

The heat-core theorem supplies a Hilbert-dense sequence in \(\mathscr C\)
whose members are smooth vectors for \(S\).  Applying Gram--Schmidt to
successive finite spans gives an orthonormal basis \((u_j)_{j\geq1}\) with
every \(u_j\) in the heat core.  Define

\[
 \boxed{V=\sum_{j\geq1}2^{-j}|u_j\rangle\langle u_j|.} \tag{5}
\]

Then \(V\geq0\), \(\ker V=\{0\}\), and

\[
 \|V\|_1=\mathrm{Tr}\,V=1.                    \tag{6}
\]

The particular weights \(2^{-j}\) are immaterial; any strictly positive
summable sequence gives the same exponent criterion.

## 3. Exact relative-heat identity

For \(s\in[0,1]\), put \(S_s=S+sV\).  Since \(V\) is trace class and
bounded, the Duhamel derivative in trace norm gives

\[
 \frac{d}{ds}e^{-tS_s}
 =-\int_0^t e^{-(t-r)S_s}V e^{-rS_s}\,dr.           \tag{7}
\]

Cyclicity of the trace yields

\[
 \frac{d}{ds}\mathrm{Tr}_{\rm rel}e^{-tS_s}
 =-t\mathrm{Tr}(V e^{-tS_s}).               \tag{8}
\]

Here only the difference of two heat operators is traced; (7) proves that
this difference is trace class.  Integrating (8) in \(s\) proves

\[
\boxed{
 \begin{aligned}
 \Theta_V(t)
 &=t\int_0^1\mathrm{Tr}(V e^{-tS_s})\,ds\\
 &=t\int_0^1
 \bigl\|e^{-tS_s/2}V^{1/2}\bigr\|_{\mathfrak S_2}^2\,ds
 \geq0.
 \end{aligned}}                                      \tag{9}
\]

This identity is global and does not require compact resolvent.  In the
quadratic form of \(S_s\), all physical sources remain coupled:

\[
\begin{aligned}
 \langle f,S_sf\rangle={}&
 \mathscr E_\Gamma(f)
 +\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
   \int_{\mathbb R}K(x)K(x-\log n)
      |f(x)-f(x-\log n)|^2\,dx\\
 &+\frac12\|f\|_{\mu_K}^2+s\langle f,Vf\rangle.
\end{aligned}                                        \tag{10}
\]

No zero sum or zero-location assumption is inserted in (9)--(10).

## 4. The unconditional and target decay rates

Unconditionally \(A\geq0\), hence \(S_s\geq\frac12I\).  Therefore

\[
 \boxed{0\leq\Theta_V(t)
 \leq t\|V\|_1e^{-t/2}.}                            \tag{11}
\]

If (2) holds, then \(S_s\geq I\), and the same calculation improves (11)
to

\[
 \boxed{0\leq\Theta_V(t)
 \leq t\|V\|_1e^{-t}.}                              \tag{12}
\]

This proves the forward implication in (4).

## 5. A subthreshold state fixes the exact slower exponent

Assume that

\[
 \alpha=\inf\sigma(A)<\frac12.                      \tag{13}
\]

The essential-threshold theorem makes \(\alpha\) an isolated eigenvalue of
finite multiplicity.  Let \(P_\alpha\) be its spectral projection.  Since
\(V\) is injective and \(P_\alpha\mathscr C\) is finite dimensional,

\[
 v_\alpha:=\lambda_{\min}
 \bigl(P_\alpha V P_\alpha|_{P_\alpha\mathscr C}\bigr)>0.
 \tag{14}
\]

Choose a circle separating \(\alpha\) from the rest of \(\sigma(A)\).
Bounded analytic perturbation theory for \(A+sV\) then gives constants
\(s_0,c_1,c_2>0\) such that, for \(0\leq s\leq s_0\), its perturbed ground
cluster \(P_s\) satisfies

\[
 \sup\sigma\!\left((A+sV)|_{P_s\mathscr C}\right)
 \leq\alpha+c_1s,
 \qquad
 \mathrm{Tr}(V P_s)\geq c_2.                \tag{15}
\]

The contribution of this cluster to (9), integrated over
\(0\leq s\leq\min(s_0,t^{-1})\), gives

\[
 \Theta_V(t)
 \geq c_2t e^{-t(\alpha+1/2)}
       \int_0^{\min(s_0,t^{-1})}e^{-c_1ts}\,ds
 \geq c_3e^{-t(\alpha+1/2)}                         \tag{16}
\]

for all sufficiently large \(t\).  On the other hand,
\(\inf\sigma(S_s)\geq\alpha+1/2\), so (9) gives

\[
 \Theta_V(t)\leq t\|V\|_1e^{-t(\alpha+1/2)}.        \tag{17}
\]

Equations (16)--(17) prove the exact logarithmic rate

\[
 \boxed{
 \lim_{t\to\infty}\frac1t\log\Theta_V(t)
 =-\left(\alpha+\frac12\right)>-1.}                 \tag{18}
\]

This proves the reverse implication in (4).

## 6. Differential form of the remaining estimate

Put

\[
 a_s(t)=\mathrm{Tr}(V e^{-tS_s}),
 \qquad A_V(t)=\int_0^1a_s(t)\,ds,
 \qquad \Theta_V(t)=tA_V(t).                       \tag{19}
\]

Differentiating under the trace gives the exact heat-weighted Rayleigh
quotient

\[
 \boxed{
 -\frac{d}{dt}\log\frac{\Theta_V(t)}t
 =\frac{\displaystyle\int_0^1
       \mathrm{Tr}(V S_s e^{-tS_s})\,ds}
      {\displaystyle\int_0^1
       \mathrm{Tr}(V e^{-tS_s})\,ds}.}       \tag{20}
\]

Both traces have positive Hilbert--Schmidt realizations.  For example,

\[
 \mathrm{Tr}(V S_s e^{-tS_s})
 =\bigl\|S_s^{1/2}e^{-tS_s/2}V^{1/2}
   \bigr\|_{\mathfrak S_2}^2.                     \tag{21}
\]

Subtracting the target value \(1\) from (20) leaves the numerator

\[
 \int_0^1
  \mathrm{Tr}\,\!\left[
  V^{1/2}(A-\tfrac12I+sV)e^{-tS_s}V^{1/2}
  \right]ds.                                      \tag{22}
\]

Thus the heat calculation keeps the signed physical form inside one
positive density matrix, but it does not change its sign.  On a
subthreshold eigenstate the expression in (22) is eventually negative and
has the exact exponent found in (18).

The auxiliary boost can in fact be removed from the leading exponent with
an explicit error.  Define the positive trace-class density

\[
 \Gamma_{s,t}=e^{-tS_s/2}V e^{-tS_s/2},             \tag{22a}
\]

and put

\[
 \begin{aligned}
 E_V(t)&=\int_0^1\mathrm{Tr}(L\Gamma_{s,t})\,ds,\\
 B_V(t)&=\int_0^1s\mathrm{Tr}(V\Gamma_{s,t})\,ds.
 \end{aligned}                                      \tag{22b}
\]

Then (20) becomes

\[
 \boxed{
 -\frac{d}{dt}\log\Theta_V(t)
 =-\frac1t+\frac12+\frac{E_V(t)}{A_V(t)}
                    +\frac{B_V(t)}{A_V(t)}.}        \tag{22c}
\]

The energy in (22b) has the literal source expansion, justified by
Tonelli's theorem for positive forms:

\[
\boxed{
 \begin{aligned}
 E_V(t)={}&\int_0^1\int_0^\infty
 \frac{e^{-u/2}}{1-e^{-2u}}
 \mathcal J_u[\Gamma_{s,t}]\,du\,ds\\
 &+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   \int_0^1\mathcal J_{\log n}[\Gamma_{s,t}]\,ds.
 \end{aligned}}                                      \tag{22d}
\]

Here, for a positive trace-class operator
\(\Gamma=\sum_j\gamma_j|f_j\rangle\langle f_j|\), the notation is

\[
 \mathcal J_u[\Gamma]=\sum_j\gamma_j\mathcal J_u(f_j,f_j),
 \qquad
 \mathscr E_\Gamma[\Gamma]
 =\sum_j\gamma_j\mathscr E_\Gamma(f_j,f_j).        \tag{22e}
\]

These values are independent of the spectral decomposition of \(\Gamma\)
because they are traces of the associated closed positive forms.

To estimate \(B_V\), set
\(g_s(t)=\mathrm{Tr}(V e^{-tS_s})\).
Duhamel's formula gives

\[
 -\partial_s g_s(t)=\int_0^t
 \mathrm{Tr}\,\!\left(
 V e^{-(t-r)S_s}V e^{-rS_s}\right)dr.
\]

The spectral theorem for \(S_s\) writes the contribution of spectral
coordinates \(\lambda,\mu\) to this integral as

\[
 |V_{\lambda\mu}|^2e^{-t(\lambda+\mu)/2}
 \int_0^t e^{(r-t/2)(\lambda-\mu)}\,dr.
\]

The last integral is at least \(t\), since
\(\sinh y/y\geq1\).  Integration against the positive two-variable
spectral measure therefore gives

\[
 -\partial_s g_s(t)
 \geq t\mathrm{Tr}(V\Gamma_{s,t}).
\]

Integration by parts in \(s\) now yields

\[
 0\leq B_V(t)
 \leq\frac1t\int_0^1-s\partial_s g_s(t)\,ds
 =\frac{A_V(t)-g_1(t)}t
 \leq\frac{A_V(t)}t.
\]

Consequently the exact source-only sandwich is

\[
 \boxed{
 \frac12+\frac{E_V(t)}{A_V(t)}-\frac1t
 \leq-\partial_t\log\Theta_V(t)
 \leq\frac12+\frac{E_V(t)}{A_V(t)}.}               \tag{22f}
\]

The positive measure

\[
 d\nu_V(\lambda)
 =\int_0^1\mathrm{Tr}
 \bigl(V^{1/2}E_{S_s}(d\lambda)V^{1/2}\bigr)\,ds
\]

has Laplace transform \(A_V(t)\).  The logarithmic derivative of a
Laplace transform decreases to the infimum of the support of its measure.
Because \(s=0\) lies in the closure of the mixture and \(V\) is injective, that
infimum is \(\alpha+1/2\), where \(\alpha=\inf\sigma(A)\).  Combining
this fact with (22c) and \(B_V/A_V=O(t^{-1})\) gives

\[
 \boxed{
 \lim_{t\to\infty}\frac{E_V(t)}{A_V(t)}
 =\inf\sigma(A).}                                  \tag{22g}
\]

Consequently the source-rate criterion is exact:

\[
 \boxed{
 A\geq\frac12I
 \quad\Longleftrightarrow\quad
 \lim_{t\to\infty}\frac{E_V(t)}{A_V(t)}\geq\frac12.}
 \tag{22h}
\]

The right side of (22h) is therefore not a weaker consequence of heat
positivity.  It is the physical surplus evaluated in a canonical family
of positive heat states.

The target rate may equivalently be stated as the existence, for every
\(\varepsilon>0\), of \(T_\varepsilon\) and \(C_\varepsilon\) such that

\[
 \Theta_V(t)\leq C_\varepsilon e^{-(1-\varepsilon)t}
 \qquad(t\geq T_\varepsilon).                       \tag{23}
\]

A sufficient infinitesimal version is

\[
 \frac{d}{dt}\log\Theta_V(t)\leq-1+o(1).           \tag{24}
\]

Using (9), proving (24) from the literal source would require a lower
bound for \(S_s\) in the \(V^{1/2}e^{-tS_s}V^{1/2}\)-weighted state.  If a
subthreshold eigenvector exists, (18) shows that the same weighted state
concentrates on it and makes (24) false by a fixed amount.  Thus neither
the positivity in (9) nor trace-class summability supplies part of the
missing exponent improvement.

### All-order heat moments do not shift the support

Every raw heat moment is nonnegative:

\[
 M_k(t):=(-1)^kA_V^{(k)}(t)
 =\int_0^1\mathrm{Tr}
   (V S_s^k e^{-tS_s})\,ds\geq0,
 \qquad k\geq0.                                    \tag{24a}
\]

This is only the Stieltjes moment condition for support in
\([0,\infty)\).  A subthreshold eigenvalue \(\alpha<1/2\) passes every
one of these inequalities and gives

\[
 \frac{M_k(t)}{A_V(t)}\longrightarrow
 \left(\alpha+\frac12\right)^k>0.                  \tag{24b}
\]

Support in \([1,\infty)\) would instead follow from complete monotonicity
of the shifted transform \(e^tA_V(t)\).  Already its first derivative is

\[
 -\frac{d}{dt}\{e^tA_V(t)\}
 =e^t\{M_1(t)-A_V(t)\}.                            \tag{24c}
\]

Thus the first shifted localizing moment is the missing physical surplus.
The scalar positivity of every generalized von Mangoldt coefficient does
not imply (24c): powers of the physical generator contain the ordered
theta-sandwiched words of 106.99, whose primitive comparison becomes
indefinite at order three.

## 7. Relation to the finite heat route

The finite heat-cofactor program of Phase 101 already constructed exact
finite spectral-shift formulas and proved all separate prime and mesh tail
bounds.  Its remaining coupled trace comparison implies \(\Omega_7\), and
finite derivative truncations do not determine it.  The observable (3) is
different in that it is a global relative trace built directly from the
closed ordinary-prime--Gamma operator.  It removes global trace-class
existence as an issue, but its decisive exponent (4) is precisely the same
physical surplus.

## 8. Status

Proved in this note:

* existence of a positive injective heat-core trace-class boost;
* the exact relative-heat identity (9);
* the unconditional rate (11);
* the exact equivalence (4), including the subthreshold asymptotic (18);
* the boost-free source sandwich (22f) and source-rate criterion (22h);
* the failure of raw all-order heat moments to move the spectral support.

Not proved in this note:

\[
 \Theta_V(t)\leq e^{-(1-o(1))t},                    \tag{25}
\]

or equivalently the physical surplus \(A\geq1/2\).  Any proof of (25) must
use a signed joint estimate for the literal ordinary-prime, Gamma and polar
terms; heat positivity alone gives only the exponent \(-1/2\).
