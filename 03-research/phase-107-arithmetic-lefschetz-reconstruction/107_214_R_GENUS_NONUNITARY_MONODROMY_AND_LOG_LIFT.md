# 107.214 -- The nonunitary R-genus requires a logarithmic lift

## 1. The line-bundle anomaly

For a flat equivariant line of character \(\zeta\), Tang's definition
of the Bismut equivariant \(R\)-genus reduces in degree zero to

\[
 R(\zeta)=D(\zeta)-D(\zeta^{-1}),
 \qquad
 D(z)=\left.{\partial\over\partial\nu}
 \operatorname{Li}_{\nu}(z)\right|_{\nu=0}.
 \tag{1.1}
\]

For unitary \(\zeta\ne1\), this is the published arithmetic
fixed-point anomaly.  Phase 107 needs \(\zeta=q=p^{-s}\), with
\(0<q<1\) for real \(s>0\).  Then \(q^{-1}>1\) lies on the branch cut
of the polylogarithm.

## 2. Exact discontinuity

For \(x>1\), the standard polylogarithm continuation satisfies

\[
 \operatorname{Li}_{\nu}(x+i0)
 -\operatorname{Li}_{\nu}(x-i0)
 =
 {2\pi i(\log x)^{\nu-1}\over\Gamma(\nu)}.
 \tag{2.1}
\]

Since

\[
 {1\over\Gamma(\nu)}=\nu+O(\nu^2),
 \qquad
 (\log x)^{\nu-1}={1\over\log x}+O(\nu),
 \]

differentiating (2.1) at \(\nu=0\) gives

\[
 D(x+i0)-D(x-i0)={2\pi i\over\log x}.
 \tag{2.2}
\]

Consequently the two boundary continuations of (1.1) at
\(q=p^{-s}\) differ by the nonzero quantity

\[
 \operatorname{Disc}R(p^{-s})
 =\pm {2\pi i\over s\log p}.
 \tag{2.3}
\]

The sign depends only on the convention for upper versus lower
continuation and is irrelevant to nonvanishing.

### Theorem 2.1 (unlifted continuation no-go)

There is no single-valued holomorphic extension of the published
unitary line \(R\)-genus to the full punctured character disk
\(0<|q|<1\) that depends only on \(q\) and agrees with (1.1).

The obstruction is the monodromy (2.3), not a missing choice of
numerical normalization.

## 3. Arithmetic weighting exposes the pole lift

Multiplying (2.3) by the arithmetic degree of the prime support gives

\[
 \log p\cdot\operatorname{Disc}R(p^{-s})
 =\pm {2\pi i\over s}.
 \tag{3.1}
\]

The prime dependence cancels exactly.  Thus the logarithmic lift

\[
 \ell_{p,s}=s\log p,\qquad q=e^{-\ell_{p,s}},
 \tag{3.2}
\]

contains strictly more information than the multiplicative character
\(q\).  On the universal cover parametrized by \(\ell\), a branch can
be fixed before evaluation.

Equation (3.1) does not yet identify the anomaly with the pole term of
the completed zeta determinant: summing the same monodromy over all
primes would diverge.  It proves instead that any successful global
formula must combine the lifted local anomalies with the generic-point
or white-light subtraction before taking a prime sum.

## 4. Consequences for the architecture

107_213 left open a nonunitary extension of the
Koehler--Roessler/Tang anomaly.  The present theorem closes the naive
version:

\[
 \text{unitary }R_g(\chi)
 \longrightarrow
 \text{single-valued function of }\chi=p^{-s}
 \quad\text{is impossible}.
\]

The surviving target is a log-lifted relative \(R\)-genus on the
covering parameter \(s\log p\), together with a global subtraction that
cancels its prime-independent pole monodromy.  This is compatible with
Meyer's use of the additive logarithmic scaling representation, but it
is not supplied by the published arithmetic fixed-point theorem.

## 5. Exact scope

This result does not reject:

1. a chosen lifted branch on the \(s\)-plane;
2. a real-part continuation for real \(s\), where the two boundary
   values are conjugate;
3. a relative anomaly in which generic and prime terms cancel;
4. a nuclear-space continuation after that cancellation.

It rejects forgetting the logarithmic lift before defining the
arithmetic direct image.

## 6. Falsifier

107_214_r_genus_nonunitary_monodromy_and_log_lift.py independently
differentiates the polylogarithm order across the cut for actual prime
characters, checks (2.2), and verifies the prime cancellation (3.1).

