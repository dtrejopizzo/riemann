# D.198 — The apparent `T=log(6)/2` negative mode is a Schur artifact

## Verdict

The two negative midpoint eigenvalues reported by the nested directed Schur
calculation are not certified eigenvalues of the complete primitive form.
The interval inversions used to eliminate the shell and safe blocks lose all
useful radius information.  In particular, for the first reported vector the
saved data give

\[
 \max_i\mathrm{rad}\,w_i=271.91,\qquad
 \max_{ij}\mathrm{rad}(K_{\rm final})_{ij}=255.10,
\]

and the interval called `rayleigh` is

\[
 [-265.8051548,,265.8051539].                         \tag{0.1}
\]

It contains zero by a wide margin.  The two Tate residuals are likewise
stored only as intervals of radius about `1.55`.  Therefore neither
primitivity nor a negative Rayleigh quotient was certified.  The final
negative-sign assertion in `114_d_185_log6_nested200_directed_schur.py`
fails after the artifact is written.

An independent evaluation of the midpoint polynomial, bypassing every
Schur inverse, gives instead

\[
 \boxed{-B_{\rm nuc}(F,F)=4.40495\,10^{-9}>0}.          \tag{0.2}
\]

This audit includes the complete Gamma form, the scalar finite-part
constant, and the contacts at `2,3,4,5`.  Thus the apparent negative mode is
not a counterexample to the endpoint inequality.  Equation (0.2) is a sign
statement about the fixed midpoint polynomial, not yet a proof of positivity
on the whole primitive Hilbert space.

No paper file is modified.

## 1. Evaluation independent of the Schur hierarchy

Let

\[
 T={1\over2}\log6,
 \qquad
 F(t)=\sum_{j=0}^{199}w_j
 \sqrt{{2j+1\over2T}}P_j(t/T),\quad |t|\le T,          \tag{1.1}
\]

and extend `F` by zero.  The direct evaluator uses only (1.1).  It computes

\[
 \begin{aligned}
 \|F\|^2&=1.55353680167947,\\
 M_+(F)&= 2.6846324\,10^{-10},\\
 M_-(F)&=-2.6846317\,10^{-10}.                         \tag{1.2}
 \end{aligned}
\]

The small nonzero values in (1.2) are the residuals of taking the midpoint
of a very wide interval vector; they are not used as exact primitive
equations.

For `n=2,3,4,5` put `a_n=log n`.  Direct Gauss integration of the physical
overlaps gives

\[
 -2\sum_{n=2}^5{\Lambda(n)\over\sqrt n}
    \mathrm{Re}\,\int F(t)\overline{F(t+a_n)}dt
 =-0.899445505251153.                                  \tag{1.3}
\]

The scalar Gamma constant contributes

\[
 -m_0\|F\|^2=-8.34588464713932,\qquad
 m_0=\log\pi-\psi(1/4).                                \tag{1.4}
\]

Finally the positive zero-extension Gamma energy is evaluated from

\[
 \int_0^\infty {e^{-r/2}\over1-e^{-2r}}
       \|\widetilde F-S_r\widetilde F\|^2dr
 =9.24533015679543.                                    \tag{1.5}
\]

Four independent outer Gauss orders `320,480,640,800` have spread
`1.76e-13`.  Adding (1.3)--(1.5) proves the numerical enclosure displayed
in (0.2) at a margin more than four orders of magnitude larger than the
observed quadrature spread.  Direct multiplication by the separately saved
complete Legendre matrix gives `4.40488e-9`, providing a second assembly
check.

The second reported midpoint mode also has positive direct value about
`1.5e-12`; its former interval Rayleigh quotient has radius `2.29e-5`, so it
too carries no certified negative sign.

## 2. Why the midpoint eigenvalue is irrelevant

For an interval matrix `K=[K_c\mathbin\pm K_r]`, an eigenvalue of `K_c` is
not an enclosure of an eigenvalue of `K`.  The nested calculation formed
several inverses of almost singular Gram matrices.  Its midpoint final block
has eigenvalues beginning with

\[
 -7.0599\,10^{-7},\qquad -1.1344\,10^{-12},             \tag{2.1}
\]

but some entry radii of that same block are larger than `255`.  Consequently
(2.1) has no directed meaning.  The correct directed scalar test is
`w^*Aw`; the saved ball for it is (0.1), not a negative interval.

This also explains why increasing the working precision did not repair the
calculation: the imported binary frame and repeated dependent interval
inversions, rather than the exact Gamma matrix, dominate the radii.

## 3. Correct pivot

The next endpoint calculation must avoid nested inverses in a nonorthogonal
frame.  It will:

1. impose the two Tate equations before reduction;
2. whiten the primitive basis in the ambient `L^2` Gram;
3. split low and shell coordinates only after whitening;
4. perform one directed congruence (or a pivoted `LDL^*` test) on the exact
   complete matrix;
5. retain exact Arb contact entries rather than serializing them through
   binary64 before the final sign test.

The independent command

```text
python3 114_d_198_t6_independent_scalar_audit.py \
  /tmp/t6_negative_candidate.npz --column 0 --certify-artifact
```

repeats (1.2)--(1.5) and rejects the claimed negative certificate.
