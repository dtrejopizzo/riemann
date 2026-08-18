# 107.41 -- Paper B consistency audit for the joint Gamma--polar factor

## 1. Purpose

This note adds a narrow but reproducible audit artifact for the
archimedean factor jointly used by `107_05` and `107_09`.

The target is the explicit identity

\[
 A_\infty(s)
 =\frac12 s(s-1)\pi^{-s/2}\Gamma(s/2)
 =\sqrt\pi\,(2\pi)^{-s/2}
 \frac{\det((s-\tfrac12)I-N_{\mathrm{triv}})}
      {\det_\zeta(N_\Gamma+s-\tfrac12)}.
 \tag{1.1}
\]

This does **not** audit the whole fixed-point geometry of `107_09`.  It
audits the explicit coupled Gamma--pole factor at the formula level.

## 2. Verifier

The verifier is `107_41_joint_gamma_polar_factor_consistency.py`.
It is self-contained and uses a Lanczos approximation for the complex
Gamma function.

It evaluates the two explicit sides of (1.1) at high precision on a
small sample of representative points:

1. real points \(s=2\) and \(s=3/2\);
2. an off-axis complex point \(s=2+3i\);
3. two critical-line points \(s=\tfrac12+14.1347\,i\) and
   \(s=\tfrac12+85.7\,i\).

For each sample, it checks numerically that

\[
 |A_{\infty,\mathrm{closed}}(s)-A_{\infty,\mathrm{ratio}}(s)|<10^{-12}.
 \tag{2.1}
\]

## 3. Audit outcome

Running the verifier on Friday, July 31, 2026 produced:

```text
All joint Gamma--polar factor consistency checks passed.
```

So the workspace now contains a reproducible audit artifact for the
explicit joint Gamma--pole factor itself.

## 4. What this proves and what it does not

This note proves something useful but narrow.

It proves:

1. the explicit archimedean factor imported by `107_09` is numerically
   self-consistent at representative real and complex sample points;
2. the Gamma and pole factors are coupled in one explicit expression,
   rather than being audited here as unrelated scalars.

It does **not** prove:

1. the full common-phase fixed-point geometry of `107_09`;
2. the one-step joint production of the prime, Gamma, and polar sectors
   from a single flow correspondence;
3. any arithmetic surface realization over \(\mathrm{Spec}\,\mathbf
   Z\).

So the correct reading is:

\[
 \text{joint Gamma--pole factor identity exact-audited},
 \qquad
 \text{joint prime--Gamma--polar fixed-point page still formalized}.
 \tag{4.1}
\]
