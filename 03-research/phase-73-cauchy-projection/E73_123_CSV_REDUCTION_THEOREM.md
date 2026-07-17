# E73.123 - CSV Reduction Theorem for the Asymptotic Standard Box

Date: 2026-07-12.

This note records the first clean asymptotic reduction after E73.122.

## 1. Definitions

For a standard natural-height box `B(L)` define:

```text
C_k(L) = |C_x(-gamma_k)|,
F_k(B,L) = W_k^+(B,L) dist(-gamma_k,Div(P_x)),
T_k(B,L) = W_k^+(B,L) C_k(L).
```

The verified box quantities are:

```text
S_FAR^+(B,L) = sum of the top-three possible F_k(B,L),
MAIN^+(B,L)  = L^5 sum of the top-three possible T_k(B,L),
OUT^+(B,L)   = sum outside the compatible top-three FAR triple.
```

The local factors satisfy

```text
LOCK^+(B,L) <= A_LOCK^+(B,L) S_FAR^+(B,L) NLC^+(B,L),
TAIL^+(B,L) <= A_TAIL^+(B,L) S_FAR^+(B,L) Gloc^+(B,L),
```

with `A_LOCK^+(B,L) <= C_A e^{alpha1 L}` and
`A_TAIL^+(B,L) <= C_T e^{alpha1 L} L^2/M(L)^2`.

In the Phase 73 standard boxes `alpha1=0.25` is fixed.

## 2. CSV hypothesis

The Cauchy small-value hypothesis is:

```text
CSV_r:
max_{gamma in local natural-height rows} |C_x(-gamma)| <= C_C L^-r.
```

E73.122 measures `r ~= 17` on the tested boxes.

## 3. Elementary envelope hypotheses

Assume:

```text
FAR_a:
S_FAR^+(B,L) <= C_F L^a.

NLC_b:
NLC^+(B,L) <= C_N L^-b.

GLOC_c:
Gloc^+(B,L) <= C_G L^-c.

MAIN_m:
sum_{k in possible top-three} W_k^+(B,L) <= C_W L^m.
```

In the current data:

```text
a ~= 6,
b ~= 16,
c ~= 15,
m roughly <= 6 plus the Cauchy small value.
```

## 4. Reduction

If

```text
a-b <= -5,
a-c+2-2m_M <= -5,
m-r+5 <= 0,
```

where `M(L) >= c_M L^{m_M}`, then

```text
LOCK^+(B,L) <= C_LOCK L^-5,
TAIL^+(B,L) <= C_TAIL L^-5,
MAIN^+(B,L) <= C_MAIN.
```

Proof:

`LOCK` follows directly:

```text
LOCK^+ <= C_A C_F C_N L^{a-b}.
```

`TAIL` follows from `M(L) >= c_M L^{m_M}`:

```text
TAIL^+
 <= C_T C_F C_G c_M^{-2} L^{a-c+2-2m_M}.
```

For `MAIN`, use `CSV_r`:

```text
MAIN^+
 = L^5 sum_{top3} W_k^+ |C_x(-gamma_k)|
 <= C_W C_C L^{m-r+5}.
```

Thus if `m-r+5 <= 0`, `MAIN` is bounded uniformly; if the constant is
`<1`, the `MAIN` gate is certified. `□`

## 5. OUT condition

`OUT` is separate because it depends on the uniqueness of the compatible
FAR triple:

```text
UNIQ-FAR:
|T_3(B,L)| = 1
```

and the row envelope outside that triple:

```text
OUT_o:
sum_{k notin S_3(B,L)} W_k^+(B,L)|C_x(-gamma_k)| <= C_O L^-9.
```

E73.122 shows that `UNIQ-FAR` holds for the wide boxes at `lambda>=24`
and that `OUT` is already about `L^-13`.  The lambda=20 failure is exactly
the finite transition where `|T_3|=2`, handled by the manifest cover.

## 6. Concrete exponent target

The observed target sufficient for the standard boxes is:

```text
CSV_17,
FAR_6,
NLC_16,
GLOC_15,
MAIN_m with m<=12,
OUT_13 after UNIQ-FAR.
```

Then:

```text
LOCK exponent <= 6-16 = -10,
TAIL exponent <= 6-15+2-2 = -9      if M(L) ~ L,
MAIN exponent <= 12-17+5 = 0.
```

The measured `MAIN` constants are below `0.26` for lambda=24,28 and below
`0.01` at lambda=32 in E73.122, so the uniform constant target `C_MAIN<1`
has room.

This reduction isolates the only genuinely arithmetic input:

```text
prove CSV_17, or a weaker CSV_r paired with a sharper MAIN_m.
```

