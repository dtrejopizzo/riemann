# Eta sum interchange: exact finite reduction

For a Hasse truncation \(k<K\), interchange of the two finite sums gives

\[
[t^m]\eta_K(1+t)=\frac{(-1)^m}{m!}
\sum_{j=0}^{K-1}\frac{W_j\log^m(j+1)}{j+1},
\]

\[
W_j=(-1)^j\sum_{k=j}^{K-1}{k\choose j}2^{-k-1}.
\]
\]

`tools/eta_fixed_generator.py` computes the weights exactly as signed
integers over the common denominator \(2^K\).  It therefore changes the
transcendental work from a nested Hasse evaluation to \(K\) rational-log
intervals and their powers through order 149.

The file is an implementation scaffold, not a certificate yet: its formal
division by \(d(t)=(1-2^{-t})/t\) deliberately stops before an outward
fixed-point reciprocal is installed.  Consequently no containment test and
no new \(\gamma_j\) enclosure is claimed.  The tail theorem in `103_44`
remains valid and supplies the missing analytic error once that finite
division is completed.
