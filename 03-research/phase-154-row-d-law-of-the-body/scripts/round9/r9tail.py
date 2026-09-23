"""R154 round 9 -- smooth (Laplace/Laguerre) columns for the outside-window measure nu,
and Lemma T (tail by construction).

Column (even, supported in |u| >= 2T, finite total variation):

    d nu_{s,k}(u) = (|u| - 2T)^k e^{-s(|u|-2T)} 1_{|u| >= 2T} du / 2      (on all of R)

With the phase-154 convention  nuhat(tau) = int_R cos(tau u) d nu(u)  (so that an atom pair
a(delta_{u0}+delta_{-u0}) gives 2a cos(u0 tau)):

    nuhat_{s,k}(tau) = Re[ e^{2 i T tau} * k! / (s - i tau)^{k+1} ],
    |nuhat_{s,k}(tau)| <= k! / (s^2 + tau^2)^{(k+1)/2}          (EXACT, for every tau)

Total variation of nu_{s,k} = k!/s^{k+1}.

LEMMA T (proved in R154_025 sec.2).  Let
    f(tau) = m(tau) - sum_n v_n cos(tau log n) + nuhat(tau) + b0 g0h + b1 g1h,
    nu = sum_k c_k nu_{s_k,p_k}  +  sum_j a_j (delta_{u_j} + delta_{-u_j}),  u_j >= 2T.
Then for tau >= tau1 >= 2,
    f(tau) >= L(tau) := log(tau/2) - log pi - 1/(12.5 tau^2) - Sv
                        - sum_k |c_k| p_k!/(s_k^2+tau^2)^{(p_k+1)/2}
                        - 2 sum_j |a_j| - |b0| k0(tau) - |b1| k1(tau),
and L is nondecreasing on [2,oo).  Hence  L(tau1) >= c  implies  f >= c on [tau1,oo).
No lattice, no period, no flat floor rho: ONE linear row closes the whole tail.
"""
import math
import numpy as np


def nuhat_col(tau, T, s, k=0):
    tau = np.asarray(tau, dtype=float)
    z = s - 1j*tau
    return np.real(np.exp(2j*T*tau) * math.factorial(k) / z**(k+1))


def nuhat_col_p(tau, T, s, k=0):
    """d/dtau"""
    tau = np.asarray(tau, dtype=float)
    z = s - 1j*tau
    fk = math.factorial(k)
    return np.real(2j*T*np.exp(2j*T*tau)*fk/z**(k+1)
                   + np.exp(2j*T*tau)*fk*(k+1)*1j/z**(k+2))


def tailcap(tau, s, k=0):
    """the exact modulus bound k!/(s^2+tau^2)^((k+1)/2)"""
    return math.factorial(k) / (np.asarray(tau, float)**2 + s*s)**((k+1)/2.0)


def L_floor(tau, T, Sv):
    """log(tau/2) - log pi - 1/(12.5 tau^2) - Sv   (the monotone archimedean floor)"""
    return np.log(np.asarray(tau, float)/2.0) - math.log(math.pi) \
        - 1.0/(12.5*np.asarray(tau, float)**2) - Sv
