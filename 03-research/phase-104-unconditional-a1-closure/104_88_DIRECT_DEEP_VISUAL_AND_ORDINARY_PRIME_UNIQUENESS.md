# 104_88 — Direct diagnostic of Deep-\(\Lambda\) and uniqueness of ordinary primes

**Result.** The Deep-\(\Lambda\) limit visually and exactly distinguishes the
on-line and off-line controls of `104_81`. For the ordinary zeta, the
two-radius diagnostic extraction gives

\[
 \lambda_n+\log(n+1)>0\qquad(1\le n\le2000),             \tag{1}
\]

with maximum discrepancy \(4.2\cdot10^{-5}\) between the radii used. Hence
the deep indicator is zero on that finite range. The exact exterior
quartet, by contrast, produces a density growing toward \(1/8\); at
\(X=2,560,000\) it is approximately \(0.0338716\).

The visualization is in
`deep_lambda_visual_diagnostic.svg` and
`deep_lambda_visual_diagnostic.png`. It is a double-precision diagnostic,
not certified nor an extrapolation to \(X\to\infty\).

There is also an important logical distinction. There is no **second**
meromorphic model that has exactly the ordinary weights \(\Lambda(m)\), the
same normalization, and zeros distinct from those of \(\zeta\). The
logarithmic derivative determines the function by analytic uniqueness.
Hence:

* building a counterexample that literally preserves all the ordinary
  \(\Lambda(m)\) is equivalent to finding an exterior zero of \(\zeta\)
  itself;
* proving that such a counterexample does not exist is equivalent to
  proving RH;
* the Euler controls of `104_81` are valid falsifiers of mechanisms, but
  necessarily change some prime multiplicity.

A zero of \(\zeta\) does not "correspond to" an individual prime. It is a
global singularity of the analytic continuation determined jointly by all
the primes. Membership or not on the critical line cannot be refuted by
assigning the zero to an isolated Euler factor.

This document does not prove the Deep-\(\Lambda\) limit or RH. It proves
that the program of searching for a distinct counterexample with the
exact same weights cannot decide them, and it graphically exhibits the
uniform signature that must still be excluded.

---

## 1. The observable represented

For a real sequence \(\ell=(\ell_n)\), set

\[
 \mathcal D_X(\ell)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf 1_{\{\ell_n+\log(n+1)\le-e^{\sqrt X}\}}.       \tag{2}
\]

`104_75` and `104_81` prove

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad
 \mathcal D_X(\lambda)\longrightarrow0.                 \tag{3}
\]

The plot compares three objects:

1. \(x_n=\lambda_n+\log(n+1)\) for the ordinary zeta on
   \(1\le n\le2000\), extracted by the Cauchy integral of `zeta_tools`;
2. the critical quartet, for which \(\mathcal D_X=0\) exactly;
3. the exterior quartet of radius \(201/200\), for which
   \(\mathcal D_X\to1/8\) exactly.

For the third object,

\[
 \ell_n^{(R)}=4-2(R^n+R^{-n})\cos(\pi n/2).              \tag{4}
\]

Only the class \(4\mid n\) is negative. The program evaluates the event in
logarithmic domain, without forming \(R^n\), and sums exactly the harmonic
weights of that class after its first crossing.

The essential visual difference is this: a finite observation of value
zero only says that the crossing has not yet appeared. For a radius \(R\)
close to one, the approximate condition

\[
 n\log R\gtrsim\sqrt X                               \tag{5}
\]

may begin well after the range in which the ordinary coefficients were
computed. That is why (1) has no asymptotic force.

The red convergence in the figure is necessarily slow. If
\(a=\log R\), the first bad class satisfies
\(n_*(X)=\sqrt X/a+O(1)\), and the exact harmonic sum gives

\[
 \mathcal D_X(\ell^{(R)})
 ={\,{1\over8}\log X+{1\over4}\log a+O(1)\,
   \over \log X+\gamma+o(1)}.                            \tag{5a}
\]

Hence a raw curve can look small over an enormous range even when its
limit is \(1/8\). The accelerated quantity

\[
 \widetilde{\mathcal D}_X
 =\mathcal D_X{\log X+\gamma\over\log X}
  -{\log a\over4\log X}                                 \tag{5b}
\]

tends to \(1/8\). In the exterior Euler control of 104_81, \(1/4\) appears
analogously. This acceleration serves to validate the geometry of the
falsifiers; it does not apply to the ordinary zeta without first knowing
an exterior mode. The dashed orange curve in the figure represents
precisely (5b): at the last point shown it equals
\(0.125007267602\), while the raw density is still
\(0.0338715807899\). This confirms that the apparent red delay is the
explicit term \(1/\log X\), not evidence of a zero limit.

## 2. Uniqueness theorem for ordinary weights

**Theorem 2.1.** Let \(\Omega\) be a connected domain containing the half-plane
\(\Re s>1\). Let \(F\) and \(\zeta\) be meromorphic on \(\Omega\), and suppose
that, on \(\Re s>1\),

\[
 -{F'(s)\over F(s)}
 =\sum_{m\ge2}{\Lambda(m)\over m^s}
 =-{\zeta'(s)\over\zeta(s)}.                            \tag{6}
\]

If \(F(s_0)=\zeta(s_0)\ne0\) at some point \(\Re s_0>1\), then

\[
 \boxed{F\equiv\zeta\quad\hbox{on }\Omega.}            \tag{7}
\]

**Proof.** Away from poles and zeros, (6) gives

\[
 {d\over ds}\log{F(s)\over\zeta(s)}=0.                 \tag{8}
\]

Hence \(F/\zeta\) is constant on the half-plane \(\Re s>1\). The
normalization at \(s_0\) makes that constant equal to one. The meromorphic
identity extends to all of \(\Omega\) by the identity theorem.
\(\square\)

The theorem uses the full sequence of weights, not merely positivity, PNT,
or support on prime powers. It explains why control models can share broad
Euler properties but not the exact sequence
\(\Lambda(m)\): if they did share it, they would not be distinct models.

## 3. What a valid counterexample would be

A counterexample to RH compatible with the ordinary primes is simply a
complex number

\[
 \rho=\beta+i\gamma,\qquad \zeta(\rho)=0,\qquad
 \beta\ne{1\over2}.                                    \tag{9}
\]

It needs no prime label and admits none. If \(\beta>1/2\), the
corresponding interior pole of `104_80` produces, after gathering the
dominant modes, constants \(c>0\), \(R>1\), and a syndetic set of degrees
on which

\[
 \lambda_n\le-cR^n.                                    \tag{10}
\]

Inequality (10) forces a positive logarithmic mass in (2). Proving that
this mass tends to zero for the ordinary weights excludes (9), but that is
exactly the pending implication of (3), not a consequence of uniqueness
(7).

## 4. Reproduction

From `tools/`:

```bash
python3 deep_lambda_visual_diagnostic.py
```

The script generates the SVG. The PNG copy is obtained mechanically with
ImageMagick. The extraction of \(\lambda_n\) uses two radii and shows their
discrepancy; this internal stability does not turn the values into
certified intervals.
