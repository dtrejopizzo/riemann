# D.182 — What the closed endpoint gives to the first propagation cell

## Verdict

D.181 supplies the previously missing positive old-core seed at

\[
 T_5=\frac12\log5.
\]

It therefore removes the endpoint itself from the propagation problem and
turns the next obligation into one explicit, source-defined capacity
estimate for the opening \(5\)-contact.  It does **not** by itself propagate
positivity to \(T_6=\frac12\log6\).  The obstruction is not the contact at
\(6\), whose von Mangoldt weight is zero; it is the nonzero \(5\)-contact
whose overlap opens on \((T_5,T_6]\).

## 1. Quantitative seed now available

The final directed congruence of D.181 has minimum Gershgorin lower endpoint

\[
 m_G=0.7940881020622326.
\]

For the frozen congruence matrix \(P\),
\(\|P\|_2=599703.282114629\ldots\).  Hence the five-dimensional Feshbach
matrix has the explicit lower bound

\[
 K_{\rm final}-0.218^{-1}H_X
 \ge {m_G\over\|P\|_2^2}I
 >2.20798\,10^{-12}I.                                \tag{1.1}
\]

Together with the \(0.218\) complement bound, this is a genuine coercive
seed for the complete operator at \(T_5\).  Before D.181 only a finite
section was known, so the old block in the threshold capacity could not be
inverted as an operator.

## 2. Exact first update

Put \(a_5=\log5\) and \(w_5=\log5/\sqrt5\).  D.121 gives, on the primitive
space,

\[
 H_{5,T}=H_{4,T}-w_5P_T(S_{a_5}+S_{-a_5})P_T.       \tag{2.1}
\]

At \(T=T_5\) the translated supports meet only in a null set, so the second
term in (2.1) has zero quadratic form.  This explains why D.181 is the
correct birth certificate.  For \(T=T_5+\delta\), however, two boundary
overlaps of total length \(4\delta\) open.  Their operator norm does not tend
to zero merely because their measure does: boundary-concentrated unit
vectors prevent an \(L^2\) operator-norm continuity argument.  Thus (1.1)
cannot legitimately be divided by a naive Lipschitz constant.

Numerically the cell widths are

\[
 T_6-T_5=0.0911607783969773\ldots,
 \qquad T_7-T_5=0.1682361183106065\ldots.             \tag{2.2}
\]

Reaching either endpoint requires an annular capacity estimate, not just
the strict value at birth.

## 3. Sharpened remaining theorem

Transport the D.181 positive core into the enlarged primitive space and
split it from the born boundary annulus.  The first-cell operator has block
form

\[
 \begin{pmatrix}A_5(\delta)&B_5(\delta)\\
 B_5(\delta)^*&D_5(\delta)\end{pmatrix}.
\]

The endpoint certificate makes \(A_5(0)\) strictly invertible and supplies
an explicit starting margin.  Propagation is therefore reduced to

\[
 \boxed{D_5(\delta)-B_5(\delta)^*A_5(\delta)^{-1}
 B_5(\delta)\ge0
 \quad(0\le\delta\le\tfrac12\log(6/5)).}             \tag{3.1}
\]

By D.175--D.179, \(B_5\) is not an arbitrary boundary load: it is the
off-diagonal compression of the same completed Gamma/prime-power symbol as
the old defect and carries the vanishing phase factor at birth.  Thus the
Hadamard counter-scaling for an independently chosen load does not apply.
The unresolved part of (3.1) is precisely the Toeplitz--Hankel divisibility
of that actual cross under the changing Tate projection.

## Conclusion

The closed endpoint materially improves propagation: the old-core
invertibility and its complete-operator Feshbach margin are now proved, so
the first cell no longer contains an endpoint gap.  What remains is one
well-typed compression theorem, (3.1), for the opening \(5\)-contact.  No
claim that the whole cell is closed follows from D.181 alone.
