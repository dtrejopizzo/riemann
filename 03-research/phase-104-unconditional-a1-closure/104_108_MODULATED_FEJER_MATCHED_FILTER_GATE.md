# 104_108 — Modulated Fejér, matched filters, and the resonance gate

**Question.** The bad selector under non-RH is not arbitrary: it is a
Bohr set determined by the trigonometric polynomial of the dominant
modes. Does that structure allow replacing the full selector cube of
`104_106` with Fourier filters and transporting the phase bound of
`104_41`?

**Result.** Yes, there is a structural reduction of the tests. A
one-parameter family of modulated Fejér filters suffices. For \(N\ge L\),
\(a\ge4\), and every \(\phi\in\mathbb R\), one proves

\[
 \boxed{
 |\mathcal B^{\triangle}_{N,L,a}(\phi)|
 \le 3\pi {N\over L}+4.}                                \tag{1}
\]

This bound is uniform in the frequency and preserves the pole, all the
primes, and all the prime powers within the full phase.

Moreover, Parseval shows that controlling these filters uniformly in
\(\phi\) controls every degree of the block in quadratic norm. In
particular,

\[
 \mathrm {RH}\quad\Longleftrightarrow\quad
 \sup_\phi|\mathcal B^{\triangle}_{2L,L,1}(\phi)|
 \le e^{\sqrt L}\quad\hbox{eventually}.               \tag{2}
\]

But when \(a\) is lowered down to \(1\), a right zero produces exactly
one resonant filter. If \(w_\rho=re^{i\theta}\), choosing
\(\phi=-\theta\) picks out the positive factor
\(K_L(r^{-1})\ge r^{-L+1}/L^2\), and the residue keeps size
\(r^{-N-L+1}/L^2\). So (1) does not transport: the only missing term is
again the residue that (2) would exclude.

The gain relative to `104_106` is precise: to detect an exponential
coefficient one does not need to control all the selectors
\(a_j\in[0,1]\); a single continuous frequency suffices by Parseval.
This reduces the family of tests, but does not weaken the logical
difficulty: (2) is still equivalent to RH. The document does not prove
bound (2) at \(a=1\), nor A1, nor RH.

---

## 1. Internal non-duplication

`104_62`, §5.2, already proves that the optimal variational selector can
be concentrated on periodic classes and that geometric selectors do not
control that supremum. `104_58` and `104_65` prove that fixed local
windows and filters preserve the exterior modes. `104_107` obtains the
phase bound for the **unmodulated** Fejér filter.

So the general observation "periodic selectors are needed" is not
claimed as new. The new pieces of this document are exactly:

1. the modulation-uniform phase bound, (1);
2. the Parseval reduction from every degree to this one-parameter
   family, (11)–(12);
3. the modulated transport formula (15) and its exact resonance (16);
4. the falsifier for the full quartet, with no conjugate cancellation,
   (18)–(19).

---

## 2. The modulated filter

Set

\[
 \alpha_{L,k}={L-|k|\over L^2}\quad(|k|<L),
 \qquad
 H_L(x)=\sum_{|k|<L}\alpha_{L,k}e^{ikx}
 =\left({\sin(Lx/2)\over L\sin(x/2)}\right)^2.           \tag{3}
\]

For a real frequency \(\phi\), define

\[
 \begin{aligned}
 \mathcal B^{\triangle}_{N,L,a}(\phi)
   &:=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}
       \mathcal B_{N+k,a},\\
 V_{N,L,\phi}(t)
   &:=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}W_{N+k}(t).
 \end{aligned}                                           \tag{4}
\]

The weights are no longer real, but the phase identity of `104_41` is
linear and can be applied to the real and imaginary parts:

\[
 \mathcal B^{\triangle}_{N,L,a}(\phi)
 =-{1\over2\pi}\int_{\mathbb R}V_{N,L,\phi}(t)\,
 d\vartheta_a(t).                                        \tag{5}
\]

In the variable \(\theta\), where
\(W_n=2-e^{in\theta}-e^{-in\theta}\), the sum in (4) is

\[
 \boxed{
 V_{N,L,\phi}(\theta)
 =2H_L(\phi)
 -e^{iN\theta}H_L(\theta-\phi)
 -e^{-iN\theta}H_L(\theta+\phi).}                       \tag{6}
\]

In particular \(V_{N,L,\phi}(0)=0\), as required by the boundary
\(|t|\to\infty\).

---

## 3. Uniform bound on variation and phase

The integral of \(H_L\) over one period is \(2\pi/L\). The variation
bound proved in `104_107` implies

\[
 \mathrm{TV}_{[0,2\pi]}(H_L)
 \le {8\over3}\left(1-{1\over L^2}\right)<{8\over3}.   \tag{7}
\]

Differentiating (6), using \(H_L\ge0\), and extending each interval of
length \(\pi\) to a full period,

\[
 \begin{aligned}
 \int_0^\pi|V'_{N,L,\phi}(\theta)|\,d\theta
 &\le N\int_0^\pi
   \{H_L(\theta-\phi)+H_L(\theta+\phi)\}\,d\theta\\
 &\quad+\int_0^\pi
   \{|H_L'(\theta-\phi)|+|H_L'(\theta+\phi)|\}\,d\theta\\
 &\le {4\pi N\over L}+{16\over3}.                       \tag{8}
 \end{aligned}
\]

The two half-lines of \(t\) then give

\[
 \mathrm{TV}_{\mathbb R}(V_{N,L,\phi})
 \le {8\pi N\over L}+{32\over3}.                        \tag{9}
\]

For \(a\ge4\), `104_41` gives
\(|\vartheta_a(t)|<3\pi/4\). Integrating (5) by parts and using (9),

\[
 |\mathcal B^{\triangle}_{N,L,a}(\phi)|
 \le {1\over2\pi}{3\pi\over4}
       \mathrm{TV}_{\mathbb R}(V_{N,L,\phi})
 \le3\pi {N\over L}+4,                                  \tag{10}
\]

uniformly in \(\phi\). This proves (1). No modulus was taken inside
\(M_\Lambda\); the modulus appears only after integrating the full
phase.

---

## 4. Parseval replaces the selector cube

For any real sequence \(x_n\), orthogonality in \(\phi\) gives

\[
 \boxed{
 {1\over2\pi}\int_0^{2\pi}
 \left|\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}x_{N+k}\right|^2
 \,d\phi
 =\sum_{|k|<L}\alpha_{L,k}^2x_{N+k}^2.}                 \tag{11}
\]

Hence

\[
 \sup_\phi
 \left|\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}x_{N+k}\right|
 \ge\max_{|k|<L}\alpha_{L,k}|x_{N+k}|.                 \tag{12}
\]

This is the rigorous version of the Bohr/matched-filter intuition. There
is no need to approximate the discontinuous indicator of the Bohr set: if
an exterior mode creates an excursion at any degree of the block, some
frequency in (4) detects it automatically. (11) is an \(L^2\)-average
identity in \(\phi\); (12) passes from that average to the supremum.
Neither of the two states that a signed average produces a good block.
For that one still needs the positive part of `104_106`, (16).

Now take \(x_n=B_n=A_n-\lambda_n\), \(N=2L\). Under RH,
\(B_n=O(n\log n)\), so the supremum in (2) is \(O(L\log L)\). If RH is
false, `104_67` produces a syndetic set \(D_+\) and constants
\(c>0,R>1\) with \(\lambda_n\ge cR^n\) on \(D_+\). For every large \(L\)
there is \(d_L\in D_+\cap[2L,2L+G]\), where \(G\) is a fixed gap. Then

\[
 |B_{d_L}|\ge {c\over2}R^{d_L},
 \qquad
 \alpha_{L,d_L-2L}\ge {L-G\over L^2}.                  \tag{13}
\]

Equations (12)–(13) show that the supremum in (2) is
\(\gg R^{2L}/L\), and therefore exceeds \(e^{\sqrt L}\). This proves (2).

Equivalently, one may take \(x_n=\mathscr R_n\) from `104_106`:
the critical part is \(O(n\log n)\), so it does not change the
subexponential/exponential dichotomy.

Criterion (2) uses absolute value and is two-sided. Degree by degree it
is stronger than merely requiring the upper barrier of `104_67`, and the
Fourier supremum does not by itself construct a good block. Its
equivalence with RH comes from the **two-sided** excursions of
`104_67`: under non-RH, either sign produces an exponential coefficient
that (11)–(12) detect. Hence (2) is a structured re-expression of RH
strength, not a new logical weakening of the target.

---

## 5. Exact transport and resonance

Introduce the Laurent polynomial

\[
 K_L(z)=\sum_{|k|<L}\alpha_{L,k}z^k
 ={(1-z^L)(1-z^{-L})\over L^2(1-z)(1-z^{-1})}.           \tag{14}
\]

For a right zero \(\rho\), with \(w=w_\rho\), the identity

\[
 {\mathcal F_n(w)\over\rho(\rho-1)}=w^n+w^{-n}-2
\]

gives, with nothing omitted,

\[
\boxed{
 \begin{aligned}
 \mathscr R^{\triangle}_{N,L}(\phi)
 :=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}\mathscr R_{N+k}
 =\sum_{\Re\rho>1/2}m_\rho\{&
 w_\rho^N K_L(w_\rho e^{-i\phi})\\
 &+w_\rho^{-N}K_L(w_\rho^{-1}e^{-i\phi})
 -2H_L(\phi)\}.
 \end{aligned}}                                         \tag{15}
\]

Write \(w=re^{i\theta}\), \(0<r<1\). At the matched frequency
\(\phi=-\theta\),

\[
 w^{-1}e^{-i\phi}=r^{-1}>1,
\]

and all the terms of \(K_L(r^{-1})\) are positive. In particular,

\[
 \boxed{
 K_L(r^{-1})\ge {r^{-L+1}\over L^2},
 \qquad
 |w^{-N}K_L(w^{-1}e^{-i\phi})|
 \ge {r^{-N-L+1}\over L^2}.}                            \tag{16}
\]

The conjugate frequency matches the conjugate of the same zero. A
modulated filter detects, rather than cancels, the main exterior part.

The lack of angular selectivity outside the circle is also explicit. If
\(z=Re^{i\delta}\), \(R>1\), then the extreme term of \(K_L(z)\) has
size \(R^{L-1}/L^2\). A fixed misalignment in \(\delta\) only changes the
phase; it provides no exponential decay. Bohr localization lives in the
normalized trigonometric polynomial \(R^{-n}B_n\), while an unnormalized
average is dominated by the radial extreme of the block.

By (15), lowering \(a:4\to1\) in (10) crosses exactly the resonant
contribution (16). A continuation that preserved the polynomial bound
(10) would prove (2), and hence RH. There is no deduction of that
continuation from the phase at \(a\ge4\): it is the missing arithmetic
theorem.

---

## 6. Rational falsifier

Take

\[
 w={i\over2},\qquad \rho={4+2i\over5},\qquad
 \phi=-{\pi\over2}.
\]

Then \(e^{-i\phi}=i\) and

\[
 w^{-1}e^{-i\phi}=(-2i)i=2,
 \qquad
 K_L(2)\ge{2^{L-1}\over L^2}.                            \tag{17}
\]

To audit the full quartet, also sum the conjugate. If
\(4\mid N\), the joint contribution to (15) is exactly

\[
\begin{aligned}
 \mathscr R^{\triangle,\mathcal O}_{N,L}(-\pi/2)
 ={}&2^{-N}\{K_L(1/2)+K_L(-1/2)\}\\
 &+2^N\{K_L(2)+K_L(-2)\}-4H_L(\pi/2).                  \tag{18}
\end{aligned}
\]

Since \(0\le H_L(\pi/2)\le1\), and the largest even exponent less than
\(L\) gives in both parity cases

\[
 K_L(2)+K_L(-2)
 =2\sum_{\substack{|k|<L\\k\ {\rm even}}}\alpha_{L,k}2^k
 \ge {2^L\over L^2},
\]

one obtains the signed bound

\[
 \boxed{
 \mathscr R^{\triangle,\mathcal O}_{N,L}(-\pi/2)
 \ge {2^{N+L}\over L^2}-4.}                              \tag{19}
\]

In particular, with \(N=2L\) and \(L\) even, the full quartet produces
\(\ge2^{3L}/L^2-4\). There is no hidden cancellation when adding the
conjugate. The same quartet leaves the phase on the critical line
unchanged, as in `104_41`, and the conjugate frequency \(+\pi/2\) gives
the conjugate orientation. This passes the mandatory off-line falsifier.

The quartet does not have the Euler product of the ordinary primes. It
does not refute a specific bound on \(\Lambda(m)\); it refutes
transporting (10) without the residue sum (15).

---

## 7. Verdict

**Proved:** the modulated test identity (6), the uniform phase bound (1),
Parseval (11), the one-parameter criterion (2), the exact transport
(15), and the resonance (16).

**Gain:** the selector target of `104_106` is reduced to a continuous
single-frequency family. The uniform norm of matched filters is a
concrete subexponential condition, preserves the Li–Laguerre scaffolding,
and detects any exterior excursion by Parseval. It is a coordinate
reduction, not a proof nor a weakening of the target's RH strength.

**Ruled out:** that Bohr structure, a Fourier modulation, or the Fejér
average allow automatically carrying the phase bound from
\(a\ge4\) down to \(a=1\).

**Remains:** a \(\phi\)-uniform arithmetic bound for
\(\mathcal B^{\triangle}_{2L,L,1}(\phi)\), obtained from the literal
weights \(\Lambda(m)\), with growth \(e^{o(L)}\). By (2), such a bound
would prove RH.

**Not proved:** that bound at \(a=1\), A1, or RH.

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 modulated_fejer_matched_filter_check.py
```

The checker uses `Fraction` and Gaussian rationals. It verifies (6),
(11), (14)–(19) on exact finite families. The analytic variation bound
(8)–(10) is proved in the text and is not replaced by sampling.
</content>
