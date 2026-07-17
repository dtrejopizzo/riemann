# E72.181 -- Chebyshev absolute-value schedule for adaptive SRP

**Date:** 2026-07-09.
**Role:** replace the conservative Bernstein schedule of E72.180 by a sharper explicit Chebyshev
schedule.

## 0. Exact Chebyshev expansion

On `[-1,1]`:

```text
|u| = 2/pi + (4/pi) sum_{k>=1} (-1)^(k+1) T_{2k}(u)/(4k^2-1).
```

Let:

```text
q_N(u)=2/pi + (4/pi) sum_{k=1}^N (-1)^(k+1) T_{2k}(u)/(4k^2-1).
```

Then:

```text
deg(q_N)=2N.
```

The absolute tail is telescopic:

```text
sum_{k>N} 1/(4k^2-1)
= 1/(2(2N+1)).
```

Therefore:

```text
sup_{|u|<=1}|q_N(u)-|u||
 <= (4/pi) sum_{k>N} 1/(4k^2-1)
 = 2/(pi(2N+1)).                                  (Cheb-tail)
```

This is explicit and sharper than the Bernstein `D^{-1/2}` schedule.

## 1. SRP error

As in E72.180:

```text
f_a(t)=(1-a/2)t-(a/2)|t|.
```

For interval `[-M,M]`, define:

```text
g_{a,N,M}(t)=(1-a/2)t-(aM/2)q_N(t/M).
```

Then:

```text
sup_{|t|<=M}|g_{a,N,M}(t)-f_a(t)|
 <= (aM/pi)/(2N+1).
```

For Phase 72:

```text
(a_0,M_0)=(0.70,0.90),
(a_1,M_1)=(0.60,0.60),
```

so:

```text
eps_0(N)+eps_1(N)
 <= (0.70*0.90 + 0.60*0.60)/(pi(2N+1))
 = 0.99/(pi(2N+1)).                               (eps-Cheb)
```

If `D=2N`, this is:

```text
eps_0+eps_1 <= 0.99/(pi(D+1)).
```

## 2. Degree schedule

To guarantee:

```text
sqrt(d_x)(eps_0+eps_1) <= m_*,
```

it is sufficient to choose even degree `D_x=2N_x` with:

```text
D_x + 1 >= 0.99 sqrt(d_x)/(pi m_*).               (Cheb-schedule)
```

Thus:

```text
D_x = O(sqrt(d_x)).
```

The maximum mixed cycle length in the adaptive SRP identity is:

```text
2D_x = O(sqrt(d_x)).
```

This supersedes the Bernstein schedule of E72.180, which gave `D_x=O(d_x)`.

## 3. Diagnostic output

The companion script:

```text
E72_181_chebyshev_abs_schedule_probe.py
```

uses the explicit coefficients above and the theoretical tail bound:

```text
E72.181 explicit Chebyshev |t| schedule probe
degree D=2N; theoretical eps_sum <= 0.495*2/(pi(2N+1))
prepared lambda=12 dim=32 op0=0.439 op1=0.445
prepared lambda=14 dim=36 op0=0.429 op1=0.445
prepared lambda=16 dim=40 op0=0.399 op1=0.437
prepared lambda=18 dim=44 op0=0.362 op1=0.313
prepared lambda=20 dim=48 op0=0.356 op1=0.449
prepared lambda=22 dim=52 op0=0.326 op1=0.500
prepared lambda=24 dim=56 op0=0.349 op1=0.508
prepared lambda=26 dim=60 op0=0.335 op1=0.369
prepared lambda=28 dim=64 op0=0.346 op1=0.482
   D   epsSum  maxBound worstLam  per-window
  28 1.087e-02    0.985       12 12:0.985 14:0.953 16:0.935 18:0.908 20:0.921 22:0.939 24:0.929 26:0.769 28:0.831
  40 7.686e-03    0.965       12 12:0.965 14:0.933 16:0.913 18:0.886 20:0.898 22:0.916 24:0.904 26:0.746 28:0.807
  56 5.529e-03    0.952       12 12:0.952 14:0.920 16:0.899 18:0.871 20:0.882 22:0.900 24:0.887 26:0.728 28:0.789
  80 3.890e-03    0.943       12 12:0.943 14:0.909 16:0.888 18:0.859 20:0.870 22:0.888 24:0.875 26:0.715 28:0.775
 112 2.789e-03    0.936       12 12:0.936 14:0.902 16:0.881 18:0.852 20:0.863 22:0.880 24:0.866 26:0.706 28:0.766
 160 1.957e-03    0.931       12 12:0.931 14:0.897 16:0.876 18:0.846 20:0.857 22:0.874 24:0.860 26:0.700 28:0.759
```

## 4. Updated open theorem

The adaptive SRP theorem can now use the explicit Chebyshev schedule:

```text
||K_0||<=0.90,
||K_1||<=0.60,
D_x+1 >= 0.99 sqrt(d_x)/(pi m_*),
Tr(G_{x,D_x}^2) < (1-m_*)^2.
```

Here:

```text
G_{x,D_x}=g_{0,N_x,M_0}(K_0)+g_{1,N_x,M_1}(K_1),
D_x=2N_x.
```

This remains a finite explicit mixed-cycle inequality, with cycle length `O(sqrt(d_x))`.
