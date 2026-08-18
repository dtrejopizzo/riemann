# 107.183 -- Gamma and pole completion of the boundary Green channel

## 1. Completed source

Use the standard completed zeta function

\[
 \xi(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

Its negative logarithmic derivative is

\[
 \mathscr G_{\rm comp}(s)
 =-{\xi'(s)\over\xi(s)}.
 \tag{1.1}
\]

Expanding the factors gives

\[
 \mathscr G_{\rm comp}(s)=
 -{\zeta'(s)\over\zeta(s)}
 -{1\over s}-{1\over s-1}
 +{1\over2}\log\pi
 -{1\over2}\psi(s/2),
 \tag{1.2}
\]

where \(\psi=\Gamma'/\Gamma\).

The first term is exactly the finite-prime boundary channel constructed
in `107_182`.  The remaining terms are the forced Gamma and pole
contributions.  No normalization remains free.

## 2. Functional symmetry

The functional equation \(\xi(s)=\xi(1-s)\) implies

\[
 \mathscr G_{\rm comp}(1-s)=-\mathscr G_{\rm comp}(s).
 \tag{2.1}
\]

Thus the completed channel is odd about the critical center.  The
apparent singularities at \(s=0,1\) in (1.2) cancel against the Gamma
and zeta terms because \(\xi(0)=\xi(1)\neq0\).  Its poles are the zeros
of \(\xi\), with residues equal to minus their multiplicities.

Equation (2.1) supplies the exact balancing absent from the finite Euler
channel alone.  It is the spectral counterpart of centering the graph
classes in Paper 0.

## 3. Global status

The scalar Green channel is now meromorphically completed:

\[
 \boxed{
 \text{prime inverse-Euler classes}
 +\text{Gamma/pole source}
 =-\xi'/\xi.}
\]

This is a genuine source-derived global object and its construction
still fails for Davenport--Heilbronn because the finite Euler summand is
missing there.

What remains is geometric rather than analytic:

1. pair (1.1) with compactly supported Mellin tests and identify the
   resulting distribution with a Green current on the absolute space;
2. construct its algebraic/vertical companion and primitive projection;
3. prove that the resulting quadratic pairing is the Weil form;
4. place that pairing in the evaluated Hodge cone calibrated in
   `107_181`.

No assertion about the location of the poles of (1.1) is made here.

## 4. Mellin interface

For a test function with Mellin transform \(\widehat f(s)\), the natural
completed boundary functional is the contour pairing

\[
 \mathcal G(f;c)
 ={1\over2\pi i}\int_{\Re s=c}
 \widehat f(s)\mathscr G_{\rm comp}(s)\,ds,
 \qquad c>1.
 \tag{4.1}
\]

Moving the contour uses (2.1) and picks up the zero residues.  Formula
(4.1), not pointwise evaluation at a zero, is the correct input for the
future divisor/Green-current realization.

## 5. Falsifier

The verifier independently evaluates (1.1) and (1.2) at real and complex
points, checks (2.1) on both sides of the critical line, and checks
cancellation near \(s=0,1\).  Fixed precision and tolerances are chosen
before evaluation.  Any normalization or sign mismatch returns
`VERDICT: NO`.
