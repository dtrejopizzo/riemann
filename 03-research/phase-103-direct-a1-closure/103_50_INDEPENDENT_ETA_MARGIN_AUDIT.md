# Independent audit of the eta finite-margin closure

## Verdict

The algebraic formulas for the normalized eta generator, the logarithm
recurrence, and the prime/archimedean reconstruction are correct.  An
initial audit suggestion to install \(q_0=1\) before the triangular
recurrence was itself incorrect and has been reverted.

The previously reported 129 outputs still require a reproducible rerun and
independent containment audit before being called certificates.  This audit
does not infer RH from a finite range.

## Checks

Write

\[
q(t)=t\zeta(1+t)=1+\sum_{n\ge1}(-1)^n\gamma_n\frac{t^{n+1}}{n!}.
\]

The divisor is

\[
d(t)=\frac{1-2^{-t}}t=\sum_{r\ge0}\frac{(-1)^r(\log2)^{r+1}}{(r+1)!}t^r.
\]

Thus the initialization `p=a`, followed by `p=-p*a`, used in the
code has the right signs and indices.  Solving \(d(t)q(t)=\eta(1+t)\) is
triangular.  Let \(q_K=\eta_K/d\), where \(\eta_K\) is the finite Hasse
sum.  The tail theorem controls \(q-q_K\), including every coefficient of
the quotient.  Therefore the recurrence must first compute the genuine
\(q_K\), with \((q_K)_0=(\eta_K)_0/d_0\).  Replacing that number by 1
*inside* the equation for degree one makes a hybrid series which is not
\(\eta_K/d\), and to which the quoted tail bound does not apply.

It is valid to replace only the returned constant coefficient by the exact
identity \(q_0=1\), after the recurrence: the error bound already encloses
each nonconstant coefficient \(q_n-(q_K)_n\), and the logarithm recurrence
uses the exact constant coefficient only at its later stage.

For the Hasse tail, `103_44` supplies an error at normalized coefficient
degree \(n\) proportional to \(2^{n-K}\).  `q_coeffs` uses
\((27+9\log(K+1))2^{n-K}/(K+1)\), with an outward integer ceiling.  This is
the correct level at which to add the error: no factorial belongs there.
The later conversion to Stieltjes constants, when used, multiplies by
\(n!\).

The recurrence in `fixed_margin_eta_21_149.py`,

\[
p_n=q_n-\frac1n\sum_{k=1}^{n-1}kp_kq_{n-k},
\]

is the coefficient recurrence for \(\log q\).  Its prime expression and
the archimedean expression match the finite `217` identities.  The fixed
interval multiplication and division by positive integers are outward.  The
positive-interval division used for \(d_0=\log2\) takes extrema over all
four endpoint quotients, also outward.

## Subsequent status

After this algebra audit, complete runs at \((K,T)=(830,800)\) and
\((850,820)\) each produced 129 positive interval lower endpoints, with
identical twelve-place endpoint prefixes.  A separate overlap run on
\(9\le n\le20\) matched the earlier Euler--Maclaurin certificate exactly at
the emitted precision.  These executions and their hashes are recorded in
`103_51_FINITE_STRONG_MARGIN_21_149_CERTIFICATE.md`.

That closes the finite range through 149.  It remains only a finite input
to the conditional phase-103 chain; it is not a proof of RH.
