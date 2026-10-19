# 104_96 — Dyadic visual diagnostic of the discrete Cramér energy

**Result (diagnostic, not a proof of RH).** For the literal ordinary
weights, set

\[
 b_n={\Lambda(n)-1\over\log n},\qquad
 B_m=\sum_{2\le n\le m}b_n,
 \tag{1}
\]

and use the exact energy from `104_93`,

\[
 \mathcal E(N)=\sum_{m=2}^{N}{B_m^2\over m(m+1)}.
 \tag{2}
\]

The new checker computes (1)--(2) up to \(N=10^7\), without approximating
\(\Lambda\): it uses the combinatorial identity

\[
 {\Lambda(p^k)\over\log(p^k)}={1\over k}
 \tag{3}
\]

on all prime powers. Only \(1/\log n\) and the final accumulation
are numerical.

If

\[
 \Delta_j:=\mathcal E(2^j)-\mathcal E(2^{j-1}),
 \tag{4}
\]

the data give

\[
 0.0519113<j^2\Delta_j<0.0981871
 \qquad(9\le j\le23).
 \tag{5}
\]

This suggests the concrete target

\[
 \boxed{\Delta_j\le {1\over8j^2}\quad(j\ge9).}
 \tag{C}
\]

It is not an empty fit: the power \(j^{-2}\) is the critical scale that
separates a summable energy from the contribution of an off-axis zero, and the
rational constant \(1/8\) leaves an observed margin of more than \(21\%\).
If (C) were proved for all blocks, then

\[
 \sup_N\mathcal E(N)
 \le \mathcal E(2^8)+{1\over8}\sum_{j\ge9}{1\over j^2}<\infty,
 \tag{6}
\]

and `104_93` would give RH. But (C) is strictly more pointwise than mere
convergence of the energy; RH has not been used here to prove that
constant. `104_97` shows that the mere localization of a spectrum on
the critical line does not impose (1/8), without thereby asserting that (C) fails
for the ordinary zeta. The finite range (5) is evidence, not an asymptotic
certificate.

The same computation **refutes** two natural shortcuts:

* \(j^2\Delta_j\) is not monotone;
* the stronger bound \(\Delta_j\le1/(20j^2)\) already fails in the
  computed range.

Hence there is no monotonicity-based extrapolation hidden in (C).

---

## 1. Exact arithmetic coordinate

Identity (3) rewrites the primitive as

\[
 B_m=\pi(m)-\sum_{n=2}^{m}{1\over\log n}
       +\sum_{k\ge2}{1\over k}\pi(m^{1/k}),
 \tag{7}
\]

which matches the split proved in `104_94`. The program sieves
the primes, inserts each prime with weight one and inserts each proper power
\(p^k\) with weight \(1/k\). A second trial-division routine
independently reconstructs the table up to \(10^4\) and requires
entrywise equality before producing the plot.

The global values obtained are

\[
\begin{array}{c|c}
N&10^7\\ \hline
\#\{p^k\le N\}&665134\\
B_N&-90.8934853592657\\
\mathcal E(N)&0.117735413945729
\end{array}
\tag{8}
\]

Over the whole prefix,

\[
 \min B_m=-98.4290621774\quad(m=9993078),
 \qquad
 \max B_m=96.2514194808\quad(m=7105253).
 \tag{9}
\]

Some relevant blocks are

\[
\begin{array}{c|c|c}
j&\Delta_j&j^2\Delta_j\\ \hline
9 &9.78943751\cdot10^{-4}&0.0792944439\\
10&9.81870687\cdot10^{-4}&0.0981870687\\
13&3.35784779\cdot10^{-4}&0.0567476276\\
17&1.79624130\cdot10^{-4}&0.0519113735\\
19&2.61153355\cdot10^{-4}&0.0942763610\\
23&1.35757677\cdot10^{-4}&0.0718158110
\end{array}
\tag{10}
\]

The increases from \(j=9\) to \(10\), from \(13\) to
\(14\), and from \(18\) to \(19\) are finite counterexamples to the
proposed monotonicity.

## 2. Critical and off-axis controls

To check that the visualization distinguishes the correct scale, we
prescribe exactly the control primitive

\[
 B_m^{(\beta,\gamma)}
 ={m^\beta\cos(\gamma\log m)\over\log m},
 \qquad \gamma=7,
 \tag{11}
\]

and define its increment by
\(b_m^{(\beta,\gamma)}=B_m^{(\beta,\gamma)}-
B_{m-1}^{(\beta,\gamma)}\). Hence there is no reconstruction nor a
fit: (11) is the exact primitive that enters (2).

A sum--integral comparison, followed by \(t=\log x\), gives

\[
\begin{aligned}
 \Delta_j^{(\beta,\gamma)}
 &\asymp
 \int_{2^{j-1}}^{2^j}
 {x^{2\beta-2}\cos^2(\gamma\log x)\over\log^2x}\,dx\\
 &\asymp {2^{(2\beta-1)j}\over j^2}.
\end{aligned}
\tag{12}
\]

For \(\beta=1/2\), \(j^2\Delta_j\) stays at constant scale. For the
off-axis control \(\beta=0.65\), it grows at scale
\(2^{0.3j}\). In the last five blocks of the plot, the critical
control gives

\[
 0.6422\le j^2\Delta_j^{(1/2,7)}\le0.9025,
 \tag{13}
\]

while the off-axis one gives

\[
 37.26\le j^2\Delta_j^{(0.65,7)}\le80.84.
 \tag{14}
\]

Dividing (14) by \(2^{0.3j}\), the values stay between \(0.58\) and
\(0.81\), as predicted by (12). This is the visual control of the
quantitative obstruction \(2\beta-1\) from `104_93`; it does not assert that (11) is an
alternative zeta function.

## 3. Stability audit

The published run performs three distinct checks:

1. prime-power table against independent factorization up to
   \(10^4\);
2. `float64` accumulation against `longdouble` up to \(10^6\);
3. repetition of the prefix with different block cuts.

In the second check one obtained

\[
 |B_{10^6}^{(64)}-B_{10^6}^{(LD)}|=6.148\cdot10^{-13},
 \qquad
 |\mathcal E_{10^6}^{(64)}-\mathcal E_{10^6}^{(LD)}|
 =3.064\cdot10^{-15}.
 \tag{15}
\]

These figures audit floating-point stability; they do not turn (5) into
certified interval arithmetic. The margin of (C) is, however, more
than twelve orders of magnitude larger than the observed energy discrepancy.

## 4. What it shows and what it does not

The figure cleanly separates three behaviors:

```text
ordinary Lambda, measured range:      j^2 Delta_j ~ 0.05--0.10
critical control beta=1/2:            j^2 Delta_j ~ constant
off-axis control beta=0.65:           j^2 Delta_j ~ 2^(0.3j)
```

Inequality (C) is now a concrete one-sided target, expressed only
with the real ordinary weights. It is also an RH-strength statement:
no finite data, nor the plot, nor the numerical stability proves it
for all \(j\). The contribution of this document is to visually locate the
summable scale, to record a candidate falsifiable constant and to rule out the
monotonicity that would have allowed an illegitimate extrapolation.

In particular, this document **does not prove** (C), Deep-\(\Lambda\), A1 nor
RH.

## 5. Reproduction

From `tools/`:

```bash
python3 discrete_cramer_energy_visual.py --limit 10000000 \
  --chunk 500000 --audit-limit 1000000
```

Files produced:

* `discrete_cramer_energy_dyadic.csv`;
* `discrete_cramer_energy_visual.svg`;
* `discrete_cramer_energy_visual.png` (reproducible conversion of the SVG).
