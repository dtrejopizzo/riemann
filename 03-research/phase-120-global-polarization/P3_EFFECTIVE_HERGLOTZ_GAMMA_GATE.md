# Effective Herglotz--Gamma gate

Status: exact one-port positive-real formulation.  The finite-horizon
storage identity on the two-Tate domain remains open.

## 1. Arithmetic positive-real function

Use the right half-plane variable `s=-i tau`.  For every active prime set

    c_p(s)=p^(-1/2)exp(-s log p),
    theta=sum_p log p.                               (1)

For `Re(s)>0`, `|c_p(s)|<1`.  Define

    H_S(s)=1/theta sum_p (log p)
              (1+c_p(s))/(1-c_p(s)).                (2)

Each Cayley summand has positive real part, hence

    Re H_S(s)>0.                                    (3)

On the imaginary boundary `s=-i tau`,

    Re H_S(-i tau)
      =1/theta sum_p(log p)P_p(tau).                (4)

Let `R_S=sum_p(log p)(I-C_p)^(-1)`.  Since

    (1+c)/(1-c)=2/(1-c)-1,

the effective contraction of the parallel-sum theorem satisfies

    C_eff(s)=1-theta/R_S(s)
            =(H_S(s)-1)/(H_S(s)+1).                (5)

Thus `C_eff` is analytically Schur because it is the Cayley transform of
the independently positive-real function (2).  Formula (5) is a second,
direct proof of its contractivity.

Its normalized Poisson observation obeys

    |O_eff(-i tau)|^2=Re H_S(-i tau),               (6)

which is precisely the scalar boundary form of the operator identity

    theta O_eff^*O_eff
      =sum_p(log p)O_p^*O_p.                        (7)

## 2. Gamma is a positive-real impedance

Put `alpha_n=n+1/4` and define

    H_Gamma(s)=sum_(n>=0) alpha_n^(-1)
                         s/(s+2alpha_n).            (8)

The series converges locally uniformly on `Re(s)>0`, since its summands are
`O(alpha_n^(-2))`.  Moreover

    Re [s/(s+2alpha_n)]
      =[Re(s)(Re(s)+2alpha_n)+Im(s)^2]
        /|s+2alpha_n|^2 >=0.                        (9)

Hence `H_Gamma` is positive real.  On the imaginary boundary,

    Re H_Gamma(-i tau)
      =sum_(n>=0) alpha_n^(-1)
          tau^2/(tau^2+4alpha_n^2)
      =g_Gamma(tau).                               (10)

Thus the previously constructed Gamma oscillator reservoir is exactly a
parallel passive realization of (8).

## 3. The one-port global supply

Define the signed global impedance

    Z_T(s)=H_Gamma(s)+theta_T-m_0
              -theta_T H_(S_T)(s).                (11)

Equations (4) and (10) give the exact boundary identity

    Re Z_T(-i tau)=A_T(tau).                       (12)

Equivalently, introduce the two independently positive-real impedances

    Z_X,T=H_Gamma+theta_T,
    Z_Y,T=m_0+theta_T H_(S_T).                     (13)

Then

    Z_T=Z_X,T-Z_Y,T,                               (14)

and their canonical passive realizations have precisely the effective
columns

    X_eff=(W_Gamma,sqrt(theta_T)I),
    Y_eff=(sqrt(m_0)I,sqrt(theta_T)O_eff,T).         (15)

This proves that the global-square problem is now a comparison of two
one-port passive systems.  It is no longer a matrix completion with one
negative direction per active prime.

## 4. Why pointwise passivity is not the theorem

The signed impedance has a closed determinant expression.  The digamma
identity gives

    H_Gamma(s)=psi(1/4+s/2)-psi(1/4),               (16)

while (2) gives

    theta_T[1-H_(S_T)(s)]
      =-2 sum_(p in S_T)(log p)
          p^(-1/2-s)/(1-p^(-1/2-s)).                (17)

Since `m_0=log pi-psi(1/4)`, define

    D_T(s)=pi^(-s) Gamma(1/4+s/2)^2
              product_(p in S_T)
                (1-p^(-1/2-s))^(-2).               (18)

Direct differentiation proves

    Z_T(s)=partial_s log D_T(s).                    (19)

Thus the effective one-port network and the independently constructed
quarter determinant are the same analytic object before boundary
compression.  Formula (19) also fixes the storage connection uniquely: no
additive Green function or scalar impedance may be fitted later.

The signed impedance `Z_T` need not be positive real: its boundary real
part is the multiplier `A_T`, which changes sign before primitive support
compression.  Therefore taking the Cayley transform of (11) and declaring
it Schur would assume row (d).

The correct remaining object is a finite-horizon storage on the compact
potential domain

    F=L_0G,
    L_0=-partial_t^2+1/4,
    G in C_c^infinity((-T,T)).                      (20)

For the explicit realizations (2) and (8), construct a storage
`S_T(state)>=0`, before evaluating (12), such that the integrated supply
identity is

    <A_TL_0G,L_0G>
      =||D_T^bulk G||^2+S_T(out)-S_T(in).           (21)

The two compact-potential endpoints must give

    S_T(out)=S_T(in),                               (22)

leaving the desired square.  Equations (2), (5), and (8) now fix every
coefficient of the storage/Riccati equation; no prime-index matrix or
free defect unitary remains.

## 5. Classification

- arithmetic Herglotz mean (2)--(5): **PROVED**;
- Gamma positive-real impedance (8)--(10): **PROVED**;
- exact one-port signed supply (11)--(15): **PROVED**;
- determinant identity (16)--(19): **PROVED**;
- pointwise Schur shortcut: **REJECTED AS CIRCULAR**;
- source-constructed finite-horizon storage (21)--(22): **OPEN**;
- global square: **OPEN**.
