#!/usr/bin/env python3
"""R187 — falsificador M_m (m = 1) con el MISMO código que la campaña (r187_campaign.py), CONSTRAINTS §3.3 / §6 paso 5.

M_1 = ξ × factor racional con un cuarteto de ceros 1/2 ± delta ± i gamma_1 fuera de la recta (R163_801 Thm 5).
Lado de primos de M_1 = el de ζ + densidad beta_1(u) = 4 cos(gamma_1 u) cosh(delta u) 1_{|u|<2T}  (no atómica):
    a^M_T(F) = a_T(F) + ∫_{-2T}^{2T} c_F(u) beta_1(u) du      (= suma del cuarteto Φ_F(ρ)Φ_F(1-ρ), lem:roughEF)
    sigma^M_T(tau) = sigma_T(tau) + bhat(tau),  bhat(tau) = ∫_{-2T}^{2T} beta_1(u) cos(tau u) du  (forma cerrada).
Todo lo demás (Galerkin, P_T, Neg/Pos, haz, K_delta, paridad, pico, escalera) es el código de la campaña sin cambios.
Uso: python3 r187_mm.py --delta 0.1 --T t1 t2 ...   (escribe DATA_MM_FALSIFIER.csv y windows_mm/)
"""
import sys, os, math, argparse, inspect, csv, fcntl
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import r187_campaign as r
from flint import arb, arb_mat

GAM1 = 14.134725141734693

def bhat_np(T, tau, delta):
    a = 2.0 * T; out = np.zeros_like(np.asarray(tau, dtype=float))
    for w in (GAM1 + tau, GAM1 - tau):
        out = out + 4.0 * (delta * math.sinh(delta * a) * np.cos(w * a) + w * math.cosh(delta * a) * np.sin(w * a)) / (delta ** 2 + w ** 2)
    return out

def bhat_arb(T, tau, delta):
    a = r.aex(2.0 * T); d = r.aex(delta); g = r.aex(GAM1); out = arb(0)
    for w in (g + tau, g - tau):
        out += 4 * (d * (d * a).sinh() * (w * a).cos() + w * (d * a).cosh() * (w * a).sin()) / (d * d + w * w)
    return out

def install(delta):
    r.DELTA_MM = delta
    s0np, s0arb = r.sigma_np, r.sigma_arb
    r.sigma_np = lambda T, tau, cont: s0np(T, tau, cont) + bhat_np(T, tau, delta)
    r.sigma_arb = lambda T, tau, cont: s0arb(T, tau, cont) + bhat_arb(T, tau, delta)
    src = inspect.getsource(r.build_form)
    assert 'A0 += (I - Cmat(u)) * (K(u) * ws)' in src
    src = src.replace('A0 += (I - Cmat(u)) * (K(u) * ws)',
                      'A0 += (I - Cmat(u)) * (K(u) * ws); Q += Cmat(u) * (8 * (GAM_A * u).cos() * (DEL_A * u).cosh() * ws)')
    src = src.replace('ug, uw = gauss_arb(n_u); A0 = arb_mat(M, M)', 'ug, uw = gauss_arb(n_u); A0 = arb_mat(M, M); Q = arb_mat(M, M)')
    src = src.replace('return A0 + Pr, A0, Pr, ta, tb', 'Pr = Pr + Q\n    return A0 + Pr, A0, Pr, ta, tb')
    ns = dict(r.__dict__); ns['GAM_A'] = r.aex(GAM1); ns['DEL_A'] = r.aex(delta)
    exec(src, ns); r.build_form = ns['build_form']
    r.WINDIR = os.path.join(HERE, 'windows_mm')

def selfcheck(delta):
    # cuadratura numérica de bhat frente a la forma cerrada
    from scipy.integrate import quad
    T, tau = 0.7, 20.3
    num = quad(lambda u: 4 * math.cos(GAM1 * u) * math.cosh(delta * u) * math.cos(tau * u), -2 * T, 2 * T, limit=400)[0]
    cf = bhat_np(T, np.array([tau]), delta)[0]
    assert abs(num - cf) < 1e-9 * (1 + abs(cf)), (num, cf)
    print(f"selfcheck bhat: cuadratura {num:.12f} = cerrada {cf:.12f}", flush=True)

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--delta', type=float, default=0.1); ap.add_argument('--T', type=float, nargs='+', required=True)
    ap.add_argument('--csv', default=os.path.join(HERE, 'DATA_MM_FALSIFIER.csv')); a = ap.parse_args()
    selfcheck(a.delta); install(a.delta)
    for T in a.T:
        row = r.run_window(T, f'MM_delta={a.delta}')
        row = dict(model=f'M_1(gamma1,delta={a.delta})', delta=a.delta, **row)
        r.append_row(a.csv, row)
        print('FILA', row['T'], row['lamA_float'], row['converged'], 'nneg', row['nneg'], 'K2/3/4/e', row['K_1em2'], row['K_1em3'], row['K_1em4'], row['K_e'], 'N(T*)', row['N_Tstar'], 'par', row['hstar_parity'], 'pico', row['hstar_peak'], 'N_Sh', row['N_Sh'], flush=True)
