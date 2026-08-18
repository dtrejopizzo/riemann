# 107.120 -- S3 attempt A4: Frobenius-trace gate

## 1. Purpose

`107_119` reaches visible \(S_3\) on the fixed real atlas with the
packet

\[
R_{A3}(row)=
(g,p,f_p,v_p(\Delta),c_p,\sigma_p),
\]

where \(\sigma_p\) is a manually exposed split/nonsplit flag.

This note replaces that manual flag by a more Frobenius-shaped signal.
The new candidate packet is

\[
R_{A4}(row)=
(g,p,f_p,v_p(\Delta),c_p,a_p^\flat),
\]

where \(a_p^\flat\) is defined on the present atlas by:

1. for elliptic rows, the actual local coefficient `E.ap(p)` returned
   by Sage;
2. for the genus-2 supersingular control row, the value \(0\), because
   the row is included only as an atlas constraint and not as the
   multiplicative split/nonsplit sector where the last obstruction lives.

The point is narrow but important:
if `A4` works on real data, then the visible \(S_3\) threshold can be
reached by a packet stated in Frobenius language rather than by an
externally named split flag.

## 2. Fixed atlas

The verifier fixes the same six real curves as `107_119` before
calculation:

1. `14a1` over \(\mathbf Q\), probed at \(p=2\);
2. `14a5` over \(\mathbf Q\), probed at \(p=7\);
3. `21a1` over \(\mathbf Q\), probed at \(p=7\);
4. `20a1` over \(\mathbf Q\), probed at \(p=2\);
5. `36a4` over \(\mathbf Q\), probed at \(p=2\);
6. the genus-2 curve
   \[
   C_{\mathrm{sup}}:\ y^2+y=x^5+x^2
   \]
   over \(\mathbf Q\), together with its supersingular control over
   \(\mathbf F_2\) and its PARI bad prime \(p=10037\).

## 3. Real Frobenius facts used

On the real elliptic rows of the atlas, Sage returns:

\[
\begin{array}{c|c|c}
\text{row} & \text{reduction type} & a_p \\
\hline
14a1@2 & I_6\ \text{nonsplit} & -1 \\
14a5@7 & I_2\ \text{split} & 1 \\
21a1@7 & I_2\ \text{nonsplit} & -1 \\
20a1@2 & IV^\ast & 0 \\
36a4@2 & IV^\ast & 0
\end{array}
\]

So on the multiplicative rows,

\[
a_p^\flat=\sigma_p,
\]

and on the additive rows both are \(0\).

This is the exact real mechanism by which `A4` replaces the manual
split-flag of `A3`.

## 4. Binary outcome

The verifier asks whether equal `A4` packets imply equal target states
on the fixed atlas, with the same target convention as before:

1. elliptic rows use
   \[
   T_E(row)=(\text{Kodaira symbol},c_p,\text{reduction label});
   \]
2. the genus-2 row uses the PARI local stable-reduction class at
   \(p=10037\).

Running the verifier on Saturday, August 1, 2026 returns

```text
VERDICT: YES
```

So the visible \(S_3\) threshold on the fixed atlas is also reached by
the Frobenius-shaped packet

\[
(g,p,f_p,v_p(\Delta),c_p,a_p^\flat).
\]

## 5. Meaning and limitation

This is progress toward the actual Phase 107 source language:
`a_p` is at least a Frobenius coefficient, not a manually named split
label.

But it still does **not** prove:

1. that the current source route of `107_04` already constructs
   \(a_p^\flat\);
2. that the finite determinant-line row of `107_04` contains enough
   information to recover this Frobenius coefficient without additional
   input;
3. any global realization theorem on arithmetic surfaces over
   \(\mathrm{Spec}\,\mathbf Z\).

So the correct reading is:

\[
\text{the visible S3 packet can be stated in Frobenius language,}
\]
\[
\text{but derivability of that packet from the current Paper A source row remains open.}
\]
