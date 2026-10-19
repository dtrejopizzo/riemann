# 104_105 — Adversarial audit of Deep-Λ and of the discrete energy

**Verdict.** The two audited equivalences hold up:

\[
 \mathrm{RH}\iff
 {1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf 1_{\{\lambda_n+\log(n+1)\le-e^{\sqrt X}\}}
 \longrightarrow0,                                      \tag{D}
\]

and, with

\[
 b_n={\Lambda(n)-1\over\log n},\qquad
 B_m=\sum_{2\le n\le m}b_n,
\]

\[
 \mathrm{RH}\iff
 \sup_N\sum_{m=2}^N{B_m^2\over m(m+1)}<\infty
 \iff
 \sum_{m=2}^N{B_m^2\over m(m+1)}=N^{o(1)}.              \tag{E}
\]

No circular implication, orientation flip of the exterior modes, or loss
in the Abel summation was found. These are criteria equivalent to RH, not
estimates already proved for the primes. This audit does not prove the
limit in (D), the bound in (E), A1, or RH.

---

## 1. Exterior-mode convention

Set

\[
 z_\rho=1-{1\over\rho}={\rho-1\over\rho},\qquad
 u_\rho=z_\rho^{-1}={\rho\over\rho-1}.
\]

The orientation used in `104_56` is correct, since

\[
 |u_\rho|^2-1
 ={|\rho|^2-|\rho-1|^2\over|\rho-1|^2}
 ={2\Re\rho-1\over|\rho-1|^2}.                         \tag{1}
\]

Thus a zero to the right of the line produces \(|u_\rho|>1\). The
apparent discrepancy with the usual definition
\(\lambda_n=\sum_\rho^*(1-z_\rho^n)\) disappears upon applying the
symmetry \(\rho\mapsto1-\bar\rho\):

\[
 z_{1-\bar\rho}=\overline{u_\rho}.                     \tag{2}
\]

Reindexing the zero multiset and using that \(\lambda_n\) is real turns
the sum into the version with \(u_\rho^n\). Hence the dominant modes of a
hypothetical violation are precisely the ones on the right, not their
contractive inverses.

If RH fails, \(|u_\rho|\to1\) as \(|\Im\rho|\) grows, so the
maximum \(R>1\) is attained on a finite set. Separating those modes gives,
with positive multiplicities,

\[
 \lambda_n=-R^nS(n)+O(n^2R_1^n+n^2),\qquad
 S(n)=\sum_{j=1}^K\cos(n\phi_j),\quad 1<R_1<R.           \tag{3}
\]

This is exactly the sign that Deep-Λ requires: near the origin of the
torus, \(S(n)>0\) and \(\lambda_n\) is exponentially negative.

## 2. Density and syndeticity

Let \(H=\overline{\{n\alpha:n\in\mathbb Z\}}\), with
\(\alpha=(\phi_1,\ldots,\phi_K)\). Rotation by \(\alpha\) is minimal and
uniquely ergodic on the compact monothetic group \(H\). Since
\(S(0)=K\), there is a regular level \(\eta\in(K/2,K)\) for which

\[
 U=\{x\in H:\textstyle\sum_j\cos x_j>\eta\}
\]

has Haar-measure-zero boundary and measure \(d>0\). Consequently,

\[
 D=\{n\ge1:n\alpha\in U\}                               \tag{4}
\]

has natural density \(d\). It is also syndetic: the translates
\(U-j\alpha\), \(j\ge0\), cover \(H\), and a finite subcover gives a
uniform bound on the gaps of (4). By (3), apart from a prefix,

\[
 \lambda_n\le-cR^n\qquad(n\in D).                       \tag{5}
\]

The natural density transfers without loss to logarithmic density. If
\(D(x)=dx+o(x)\), partial summation gives

\[
 \sum_{\substack{n\le X\\n\in D}}{1\over n}
 ={D(X)\over X}+\int_1^X{D(t)\over t^2}\,dt
 =d\log X+o(\log X).                                    \tag{6}
\]

No universal density constant is used: \(d\) may depend on the
hypothetical exterior configuration.

## 3. Implications of the deep observable

Under RH, \(\lambda_n\ge0\); hence the indicator in (D) is identically
zero.

If RH fails, fix \(K>1/\log R\). For
\(n\in D\cap[K\sqrt X,X]\), (5) gives, from some point \(X\) on,

\[
 \lambda_n+\log(n+1)\le-e^{\sqrt X}.                   \tag{7}
\]

Using (6),

\[
 {1\over H_X}
 \sum_{\substack{K\sqrt X\le n\le X\\n\in D}}{1\over n}
 \longrightarrow {d\over2}>0.                          \tag{8}
\]

So the limit in (D) cannot be zero. This also audits the two points that
could have hidden a loss: discarding \(n<K\sqrt X\) costs exactly half
the logarithmic mass, not all of it, and the constant factor \(c\)
in (5) is absorbed by the strict inequality
\(K\log R>1\).

The diagonal translation of `104_75` does not alter the criterion either.
The uniform bound of `104_69`,

\[
 \sup_{n\le X}|\lambda_{n,e^{-X/100}}-\lambda_n|=o(1),   \tag{9}
\]

is negligible compared with \(e^{\sqrt X}\). No continuity of a hard
indicator is used: inclusions with shifted thresholds, or directly the
growing distance of the deep threshold, justify the step.

## 4. Finite energy identities

With \(B(x)=B_m\) on \([m,m+1)\), the exact telescoping is

\[
 \mathcal E(N)=\int_2^{N+1}{B(x)^2\over x^2}\,dx
 =\sum_{r,s\le N}b_rb_s
 \left({1\over\max(r,s)}-{1\over N+1}\right).           \tag{10}
\]

The boundary term \(-B_N^2/(N+1)\) is present. The attached checker
verifies (10) in rational arithmetic for arbitrary signed data.

For \(\Re s>1\),

\[
 G(s)=\sum_{n\ge2}b_nn^{-s}
      =\log\zeta(s)-C(s),\qquad
 C(s)=\sum_{n\ge2}{n^{-s}\over\log n},                 \tag{11}
\]

and \(C'(s)=1-\zeta(s)\). Hence

\[
 G'(s)={\zeta'(s)\over\zeta(s)}+\zeta(s)-1.             \tag{12}
\]

Abel summation has no omitted term:

\[
 G(s)=s\int_2^\infty B(x)x^{-s-1}\,dx.                 \tag{13}
\]

In particular, if a sequence is truncated after \(M\), the constant value
\(B_M\) on \([M,\infty)\) supplies exactly the boundary term
\(B_M(M+1)^{-s}\) that completes the identity. This is also verified
rationally in the checker.

## 5. From subpolynomial energy to RH

Suppose \(\mathcal E(N)=N^{o(1)}\). For every \(\delta>0\), summation by
parts against the positive increments of \(\mathcal E\) gives

\[
 \int_2^\infty B(x)^2x^{-2-\delta}\,dx<\infty.           \tag{14}
\]

If \(\sigma>1/2\), choose \(0<\delta<2\sigma-1\). Then
Cauchy–Schwarz applied to (13) gives

\[
 \int_2^\infty|B(x)|x^{-\sigma-1}\,dx<\infty.           \tag{15}
\]

The choice can be made uniformly on compact sets, so that (13) extends
\(G\) holomorphically to \(\Re s>1/2\). If there were a zero
\(\rho\) of multiplicity \(m\) there, the right-hand side of (12) would
have residue \(m\) at \(\rho\), while \(G'\) and \(\zeta-1\) would be
holomorphic. The meromorphic identity, extended from \(\Re s>1\), forbids
this. The functional equation then excludes the symmetric zeros on the
left.

This argument does not presuppose a global branch of \(\log\zeta\): after
differentiating, (12) is a single-valued meromorphic identity.

## 6. From RH to finite energy

The only deep external input in this direction is correctly labeled
**conditional on RH**: Cramér's mean-square bound

\[
 \int_Y^{2Y}|\psi(x)-x|^2\,dx\ll Y^2.                   \tag{16}
\]

It is not used unconditionally. It is a classical theorem under RH;
modern explicit results even prove an absolute constant for the ratio
over \(Y^2\).

The Stieltjes identity

\[
 J(x)-\mathrm{Li}_2(x)
 ={\psi(x)-x\over\log x}
 +\int_2^x{\psi(t)-t\over t\log^2t}\,dt+{2\over\log2}  \tag{17}
\]

together with (16) gives an \(O(1/j^2)\) contribution to the first term
in the block \(x\asymp2^j\), and the integral term is
\(O(\sqrt x/\log^2x)+O(1)\). Both squares, divided by \(x^2\), are
integrable. Finally,

\[
 0\le\sum_{n=2}^m{1\over\log n}-\int_2^m{dt\over\log t}
 \le {1\over\log2}                                      \tag{18}
\]

shows that replacing the continuous comparator with the discrete one only
adds a bounded function. This proves \(\sup_N\mathcal E(N)<\infty\).

## 7. Audit result

1. The convention \(u_\rho=\rho/(\rho-1)\) has the correct orientation.
2. The negative excursions form a set of positive natural density that is
   syndetic; no universal density is assumed.
3. The threshold \(-e^{\sqrt X}\) retains a positive logarithmic mass
   under non-RH.
4. The Abel identity and the moving boundary term of the energy are
   exact.
5. \(\mathcal E(N)=N^{o(1)}\) really does exclude every zero with
   \(\Re\rho>1/2\); RH really does imply finite energy via (16).

Therefore neither of the two targets becomes easier through a
formulation error. Proving either of the pending arithmetic limits for
the ordinary Mangoldt weights would prove RH.

---

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 deep_energy_equivalence_audit_check.py
```

The checker certifies only the finite algebraic identities and the
rational orientation of the exterior mode. The asymptotic and analytic
steps are proved above; the program does not claim to certify them in
floating point.
</content>
