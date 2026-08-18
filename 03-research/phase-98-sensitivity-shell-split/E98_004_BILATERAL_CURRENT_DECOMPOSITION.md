# E98.004 - Bilateral current decomposition

## 1. Internal contribution

With `K_N=S_t^bil(s;s_*)`, define

```text
INT_(L,N,t)(s;s_*)
 =-Tr([Z_N,K_N]Z^(-1)X)
  -Tr((Z^*)^(-1)[K_N,Z_N^*]X).                       (1.1)
```

## 2. Shell contribution

Using the four crossing terms of E98.002, define

```text
SHELL_(L,N,t)(s;s_*)
 =-Tr((Q_NZP_NK_N-K_NP_NZQ_N)Z^(-1)X)

  -Tr((Z^*)^(-1)
    (K_NP_NZ^*Q_N-Q_NZ^*P_NK_N)X).                  (2.1)
```

## 3. Exact sum

E97.003 and E98.002 give

```text
BJ_t(s;s_*)=INT_(L,N,t)(s;s_*)
             +SHELL_(L,N,t)(s;s_*).                  (3.1)
```

No remainder occurs in (3.1).

## 4. Status

```text
proved:
  exact internal plus Fourier-shell decomposition of the full bordered
  deformation current.
```

