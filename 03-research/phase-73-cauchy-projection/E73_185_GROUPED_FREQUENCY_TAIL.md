# E73.185 - Grouped-frequency WR tail bound

Date: 2026-07-14.

## 1. Purpose

E73.184 gives a valid order-`K` WR tail certificate, but its derivative
envelope is conservative because it expands

```text
F^(s)=(e^(y/2)B)^(s)
```

by the binomial formula and takes absolute values before combining terms.
This note keeps each frequency together before taking absolute values.

## 2. Direct frequency derivative

For the finite packet

```text
B(y)=sum_omega c_omega e^(i omega y)
    + y sum_omega l_omega e^(i omega y),
```

write

```text
lambda_omega=1/2+i omega.
```

For `s>=1`,

```text
F^(s)(y)
= sum_omega e^(lambda_omega y)
   [ c_omega lambda_omega^s
     + s l_omega lambda_omega^(s-1)
     + y l_omega lambda_omega^s ].
```

Therefore

```text
M_s^grp
<= e^(L/2) sum_omega
   ( |c_omega lambda_omega^s+s l_omega lambda_omega^(s-1)|
     + L|l_omega lambda_omega^s| ).
```

This is still a rigorous coefficient-absolute bound, but it preserves the
cancellation between the constant and linear pieces at the same frequency.

## 3. Tail certificate

The order-`K` tail bound becomes

```text
|Tail_{R,K}|
<= M_{K+1}^grp sum_{r>=R}(2r+1)^(-(K+2)).
```

The odd tail sum is the same polygamma expression from E73.184.

## 4. Status

```text
proved:   grouped-frequency derivative bound;
verified: it bounds observed tails in tested rows;
measured: it improves the binomial envelope, but not enough alone to close
          SCRCE at the final residual scale.
```

The next sharpening is no longer local to `WR`: it must use the signed
model-prime principal residual itself, because the archimedean tail is now
a certified finite component.
