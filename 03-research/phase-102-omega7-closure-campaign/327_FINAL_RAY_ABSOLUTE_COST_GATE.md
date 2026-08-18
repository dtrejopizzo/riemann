# Final-ray absolute cost gate

## Purpose

`326_TAIL_LOBE_STEP_ENVELOPE_EFFECTIVE_REDUCTION.md` reduces every bounded
tail lobe in the `320` criterion to a finite prime-power computation.  The
only infinite piece left for a fixed \(n\) is the final ray after the last
zero of \(L_{n-1}^{(2)}\).

This note records a safe use of ordinary two-sided PNT/VK envelopes: they
may be used on that final ray as an explicit negative cost.  This does not
contradict `250`, because it is not being used to decide the whole signed
tail.  It only bounds the last infinite lobe after the bounded oriented
lobes have been certified arithmetically.

## Final ray notation

Let
\[
  K_n(u)=e^{-u}L_{n-1}^{(2)}(u),
  \qquad
  \mathcal E(u)=\psi(e^u)-e^u.
\]
Let \(\xi_{n,*}\) be the largest zero of \(L_{n-1}^{(2)}\) that is larger
than \(T_n\).  If there is no such zero, set \(\xi_{n,*}=T_n\).  The final
ray is
\[
  J_{n,\infty}=[\xi_{n,*},\infty).
\]
On this ray \(K_n\) has a fixed sign
\[
  \sigma_{n,\infty}=\operatorname{sgn}K_n(u)
  \qquad(u>\xi_{n,*}).
\]

The final-ray contribution to the tail functional is
\[
\boxed{
  I_{n,\infty}
  =
  \sigma_{n,\infty}
  \int_{\xi_{n,*}}^\infty \mathcal E(u)|K_n(u)|\,du .
}
\tag{1}
\]

## Absolute envelope as a valid final-ray lower bound

Assume a two-sided envelope on the final ray:
\[
\boxed{
  |\mathcal E(u)|\le W(u)
  \qquad(u\ge \xi_{n,*}),
}
\tag{2}
\]
where
\[
  \int_{\xi_{n,*}}^\infty W(u)|K_n(u)|\,du<\infty.
\]

Then, regardless of the sign \(\sigma_{n,\infty}\),
\[
\boxed{
  I_{n,\infty}
  \ge
  -\int_{\xi_{n,*}}^\infty W(u)|K_n(u)|\,du.
}
\tag{3}
\]

Indeed, if \(\sigma_{n,\infty}=+1\), then
\(\mathcal E(u)\ge-W(u)\).  If \(\sigma_{n,\infty}=-1\), then
\(-\mathcal E(u)\ge-W(u)\).  Multiplying by the positive weight \(|K_n|\)
and integrating gives (3).

## Insertion into the `322` certificate

Let \(\mathcal L_{n,\mathrm{bd}}^-\) be the certified lower contribution of
all bounded lobes, computed by the finite endpoint formulas of `326`.  Put
\[
\boxed{
  \mathcal R_{n,\infty}(W)
  =
  \int_{\xi_{n,*}}^\infty W(u)e^{-u}|L_{n-1}^{(2)}(u)|\,du.
}
\tag{4}
\]

Then the full tail lower bound is
\[
\boxed{
  I_n(T_n)
  \ge
  \mathcal L_{n,\mathrm{bd}}^- - \mathcal R_{n,\infty}(W).
}
\tag{5}
\]

Consequently compact A1 is certified at \(n\) if
\[
\boxed{
  \mathcal L_{n,\mathrm{bd}}^- - \mathcal R_{n,\infty}(W)
  \ge
  \left(d_n-\frac14\right)A_n.
}
\tag{6}
\]

Thus the final-ray theorem may be weakened to a computable absolute cost,
provided the bounded-lobe arithmetic surplus is large enough to absorb it.

## Why this does not revive the failed absolute route

If (2) is used on every lobe, then the lower bound becomes
\[
  -\int_{T_n}^{\infty}W(u)|K_n(u)|\,du,
\]
which is precisely the symmetric-envelope collapse of `250`.

The present gate is different.  The bounded lobes are evaluated with their
actual one-sided arithmetic extrema from `326`; the absolute envelope is
used only on the final ray, where finite prime-power enumeration is not
available.  Therefore (6) is a hybrid certificate:

1. finite, oriented arithmetic on bounded lobes;
2. analytic absolute cost only on the final ray;
3. a pointwise comparison against the exact A1 margin.

It may still fail in practice if the final-ray cost is too large, but it is
a logically valid sufficient criterion.

## Typical VK/PNT input

An explicit Vinogradov--Korobov type estimate of the form
\[
  |\psi(e^u)-e^u|
  \le
  C e^u \exp(-a u^\theta)
  \qquad(u\ge U_0)
\]
gives, for \(\xi_{n,*}\ge U_0\),
\[
  \mathcal R_{n,\infty}(W)
  \le
  C
  \int_{\xi_{n,*}}^\infty
  \exp(-a u^\theta)|L_{n-1}^{(2)}(u)|\,du.
\]
Since \(L_{n-1}^{(2)}\) is a polynomial of degree \(n-1\), this integral is
finite and can be enclosed by standard incomplete-gamma interval bounds
after expanding the polynomial.

If \(\xi_{n,*}<U_0\), the ray must be split at \(U_0\): the bounded segment
\([\xi_{n,*},U_0]\) is handled by finite step extrema as in `326`, and the
remaining ray by the VK envelope.

## Status

Closed as a sufficient final-ray cost gate for the oriented tail route.
A1 remains open until the bounded-lobe arithmetic lower bound and this
final-ray cost inequality are proved for every \(n\ge8\), or above an
effective threshold with a complete finite remainder.
