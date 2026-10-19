# 104_56 — Density- and block-relaxed Li criterion

**Role.** Audit the proposal to replace "for all \(n\ge150\)" with
a condition outside an exceptional set. The result does not prove A1
nor RH. It does rigorously weaken the quantifier needed for a proof:

* if RH is false, the indices at which the quartic margin fails contain
  a **syndetic** set;
* hence it suffices to prove the margin on consecutive blocks of unbounded
  length, or outside a set of zero upper logarithmic density;
* there is no universal positive-density constant derivable from the
  Bombieri–Lagarias axioms. The dominant phases can make that
  density arbitrarily small.

The last point corrects the initial proposal of a fixed constant
\(\delta _0>0\).

---

## 1. What Bombieri–Lagarias, Theorem 1(c), exactly says

Let \(R\) be a multiset satisfying the Bombieri–Lagarias summability
hypotheses and set

\[
 u_\rho:=\left(1-{1\over\rho}\right)^{-1}
 ={\rho\over\rho-1}.
\tag{1}
\]

Theorem 1 of Bombieri–Lagarias, *Complements to Li's criterion for the
Riemann hypothesis*, J. Number Theory **77** (1999), 274--287, states the
equivalence between

\[
 \Re\rho\le {1\over2}\quad(\rho\in R)
\tag{2}
\]

and the following one-sided subexponential bound: for each
\(\varepsilon>0\) there is \(c(\varepsilon)>0\) such that

\[
 \sum_{\rho\in R}\Re(1-u_\rho^n)
 \ge-c(\varepsilon)e^{\varepsilon n}
 \qquad(n\ge1).
\tag{3}
\]

Their Corollary 1 applies this to a multiset stable under conjugation and
\(\rho\mapsto1-\rho\). In that situation

\[
 \lambda_{-n}=\lambda_n,
\qquad
 \lambda_{-n}:=\sum_\rho^*(1-u_\rho^n).
\tag{4}
\]

The paper proves that, if (2) fails, the term in (3) is negative and of
exponential size **infinitely often**. The published statement does not
claim natural density, logarithmic density, or a universal constant. The
phrase "sometimes exponentially large" from Lagarias 2007 should be read
with this scope.

The Bombieri–Lagarias proof, however, contains more structure than its
statement makes explicit. The next section extracts that consequence.

---

## 2. Dominant exterior modes

Suppose RH is false. Then there is some \(u_\rho\) with
\(|u_\rho|>1\). Since

\[
 |u_\rho|^2-1={2\Re\rho-1\over|\rho-1|^2}
\tag{5}
\]

and the right-hand side tends to zero as \(|\rho|\to\infty\), there is a
maximum

\[
 R:=\max_\rho|u_\rho|>1.
\tag{6}
\]

Only finitely many zeros attain it. Write, with multiplicity,

\[
 u_1=Re^{i\phi _1},\ldots,u_K=Re^{i\phi _K}.
\tag{7}
\]

Stability under conjugation makes

\[
 S(n):=\sum_{j=1}^K\cos(n\phi_j)
\tag{8}
\]

real. The argument on pages 3--4 of Bombieri–Lagarias gives a
\(1<R_1<R\) such that

\[
 \boxed{
 \lambda_n=-R^nS(n)
 +O(n^2R_1^n+n^2).}
\tag{9}
\]

Indeed, the other exterior modes have modulus at most \(R_1\), the
elements with \(|\rho|\le n\) are \(O(n^2)\) under their hypothesis (ii), and
the tail \(|\rho|>n\) is \(O(n^2)\). Equation (4) turns their computation with
exponent \(-n\) into (9). This orientation matters: the dominant
modes are \(u_\rho=\rho/(\rho-1)\) corresponding to zeros to the
**right** of \(1/2\), not \(1-1/\rho\).

For Lagarias's incomplete coefficient the same dominant part is obtained.
Once \(n>\max_j|\Im\rho_j|^2\), all the modes (7) are included in
\(\lambda_n(\sqrt n)\). Riemann–von Mangoldt and the gap
\(R_1<R\) give

\[
 \boxed{
 \lambda_n(\sqrt n)=-R^nS(n)+
 O\!\left(\sqrt n\log n\,(1+R_1^n)\right).}
\tag{10}
\]

So (9) and (10) simultaneously carry the same exponential sign on
any set where \(S(n)\) is bounded away from zero.

---

## 3. The correct strengthening: a syndetic set of excursions

Let

\[
 \alpha=(\phi_1,\ldots,\phi_K)\in\mathbb T^K,
 \qquad
 H=\overline{\{n\alpha:n\in\mathbb Z\}}.
\tag{11}
\]

\(H\) is a compact monothetic group and translation by \(\alpha\) is
minimal and uniquely ergodic on \(H\). Let

\[
 F(x_1,\ldots,x_K)=\sum_{j=1}^K\cos x_j.
\tag{12}
\]

Since \(F(0)=K\), one can choose

\[
 {K\over2}<\eta<K
\tag{13}
\]

so that the Haar measure \(\mu_H\) satisfies
\(\mu_H(F=\eta)=0\). This is possible because a probability
distribution has at most a countable set of atoms. The open set

\[
 U_\eta:=\{x\in H:F(x)>\eta\}
\tag{14}
\]

contains a nonempty neighborhood of the origin and hence

\[
 d:=\mu_H(U_\eta)>0.
\tag{15}
\]

By equidistribution on the compact group, the set of returns

\[
 D_\eta:=\{n\ge1:n\alpha\in U_\eta\}
\tag{16}
\]

has natural density \(d\). It is moreover **syndetic**. To see this, the
translations \(U_\eta-j\alpha\), \(j\ge0\), cover \(H\) by minimality;
compactness gives a finite subcover. Hence there is \(L<\infty\)
such that every interval of \(L\) integers contains a member of
\(D_\eta\).

On \(D_\eta\), \(S(n)>\eta\). From (9)--(10), for every \(n\) sufficiently
large in \(D_\eta\),

\[
 \boxed{
 \lambda_n\le-{\eta\over2}R^n,
 \qquad
 \lambda_n(\sqrt n)\le-{\eta\over2}R^n.}
\tag{17}
\]

We have proved:

**Theorem 3.1 (dense excursions if RH fails).** If RH is false, the
sets

\[
 \{n:\lambda_n<0\},\qquad
 \{n:4\lambda_n\le A_n\}
\tag{18}
\]

contain, up to a finite prefix, the same syndetic set of positive
natural density. The second claim uses only
\(A_n=O(n\log n)\), which is negligible against (17).

The same theorem holds for any margin
\(\lambda_n\ge cA_n\) with fixed \(c>0\), and also for a
subexponential additive perturbation smaller than \(R^n\).

---

## 4. Two RH criteria with a relaxed quantifier

Define the upper logarithmic density

\[
 \overline\delta_{\log}(E)
 :=\limsup_{X\to\infty}{1\over\log X}
   \sum_{\substack{n\le X\\n\in E}}{1\over n}.
\tag{19}
\]

**Corollary 4.1 (zero-density exception).** The following statements
are equivalent:

1. RH;
2. there exists \(E\subset\mathbb N\) with
   \(\overline\delta_{\log}(E)=0\) such that, for every \(n\) sufficiently
   large outside \(E\),

   \[
   4\lambda_n>A_n;
   \tag{20}
   \]

3. (20) holds outside a set whose upper natural density is zero.

**Proof.** Under RH, Lagarias's asymptotic theorem gives
\(\lambda_n=A_n+O(\sqrt n\log n)\), while
\(A_n\sim\tfrac12n\log n\). Hence (20) eventually holds with
\(E=\varnothing\). Conversely, if RH fails, (18) contains a set
of natural density \(d>0\). By partial summation that set also
has logarithmic density \(d\), and it must be contained in any
exception to (20), contradicting (19). \(\square\)

The logarithmic version is the wider of the two relaxations: an exception
can have large local blocks and still have zero logarithmic density.

**Corollary 4.2 (block criterion).** RH is equivalent to the existence of
consecutive blocks of unbounded lengths in which

\[
 4\lambda_n>A_n
\tag{21}
\]

for every index of the block.

**Proof.** RH gives (21) on an entire half-line. If RH fails, the set of
failures contains, after a prefix, a syndetic set; hence the
length of a block of successes is uniformly bounded. \(\square\)

This corollary completely removes the obligation to control every degree:
an averaging method would suffice if it produced good blocks of increasing
length, not just many scattered good indices.

---

## 5. Why no universal \(\delta_0\) exists from the BL axioms

The density \(d\) of (15) depends on the dominant phases. It cannot
be replaced by a universal positive constant using only summability,
conjugation, and functional symmetry.

Fix integers \(K\ge2\), \(q>2K\), set
\(\theta=2\pi/q\), and choose

\[
 1<R<\sec\theta.
\tag{22}
\]

Consider the exterior modes

\[
 Re^{\pm ik\theta}\qquad(1\le k<K),
\tag{23}
\]

each with multiplicity \(K-k\), and complete each point via
conjugation and \(u\mapsto u^{-1}\). The points
\(\rho=u/(u-1)\) satisfy

\[
 {1\over2}<\Re\rho<1.
\tag{24}
\]

The first inequality is equivalent to \(|u|>1\); the second follows from
\(R\cos(k\theta)<1\), guaranteed by (22) and
\(k\theta\in[\theta,\pi)\).
This is thus a finite admissible multiset with the symmetries of a
functional equation and zeros off the line.

Its dominant sum is

\[
 \begin{aligned}
 S_K(n)
 &=2\sum_{k=1}^{K-1}(K-k)
       \cos\!\left({2\pi kn\over q}\right)\\
 &=K\left\{\mathsf F_K\!\left({2\pi n\over q}\right)-1\right\},
 \end{aligned}
\tag{25}
\]

where

\[
 \mathsf F_K(x)={1\over K}
 \left({\sin(Kx/2)\over\sin(x/2)}\right)^2
\tag{26}
\]

is the Fejér kernel. If \(S_K(n)\ge0\), then

\[
 \left|\sin{\pi n\over q}\right|\le {1\over\sqrt K}.
\tag{27}
\]

Hence the proportion of classes mod \(q\) where the dominant term
can be negative is at most

\[
 \boxed{
 {2\over\pi}\arcsin{1\over\sqrt K}+{1\over q}.}
\tag{28}
\]

This quantity tends to zero by first letting \(K\to\infty\) and then
\(q/K\to\infty\). In the remaining classes \(S_K(n)<0\), and the Li
coefficient is eventually positive. Thus the density of negative
excursions can be made arbitrarily small within the abstract
Bombieri–Lagarias class.

This does not construct an Euler product equal to \(\zeta\), nor does it
prove that the dominant phases of \(\zeta\) have that geometry. It proves
exactly that a universal \(\delta_0\) does not follow from the BL theorem
nor from the symmetries. For hypothetical non-RH zeta some
\(d_\zeta>0\) exists, but it depends on unknown zeros. The robust and
usable formulation is therefore "zero-density exception" or "blocks of
unbounded length."

---

## 6. Relation to earlier stop-gates

* `104_17` showed that radial Abel–Fejér can be positive even when
  individual coefficients are exponentially negative. The block
  criterion does not contradict that no-go: it requires signed Tauberian
  information capable of manufacturing whole intervals, not just a
  positive average.
* `104_33` and `104_41` localized the defect in the sum of exterior
  residues. The phases \(\phi_j\) of this document are precisely the
  maximal-modulus modes of that sum. No new mechanism for bounding it
  appears.
* The relaxation does open methods that were previously logically
  insufficient: an average estimate can close RH if it implies good
  blocks of increasing size or an exceptional set of zero logarithmic
  density.

---

## 7. Reproducible verification

`tools/density_relaxed_li_criterion_check.py` verifies:

1. the exact orientation \(u=\rho/(\rho-1)\) on a rational quadruple;
2. the finite Fejér identity (25);
3. the counting bound (28) for a periodic family;
4. that its density can drop below one percent while the set of
   returns remains syndetic.

The tool verifies finite algebra and periodic counts; the compact-group
steps and the error terms of (9)--(10) are proved in the text, not
certified by floating point.

---

## 8. Verdict

\[
\boxed{
\begin{gathered}
 \mathrm{RH\ false}
 \Longrightarrow
 \{n:4\lambda_n\le A_n\}
 \text{ contains a syndetic set of positive density},\\[2mm]
 \mathrm{RH}
 \Longleftrightarrow
 \text{the quartic margin holds on blocks of unbounded length},\\[2mm]
 \mathrm{RH}
 \Longleftrightarrow
 \text{the quartic margin holds outside an exception of zero
 logarithmic density}.
\end{gathered}}
\tag{29}
\]

The proposal to relax the quantifier is valid and considerably stronger
than expected. The version with a universal constant
\(\delta_0>0\) is not justified and is false within the abstract BL
class. Nothing in (29) yet proves a single one of the good blocks
required for the real zeta; that is the new quantitative target.
