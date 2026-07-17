#!/usr/bin/env python
"""
Generate the first 5000 critical-line zeros of the Davenport-Heilbronn L-function.
Adapted: configurable WORK_DIR via env; time-budget guard for graceful partial save.
"""
import os, sys, time, json, re
import numpy as np
import mpmath
import cypari2 WORK_DIR = os.environ.get('LDH_WORK_DIR', os.path.dirname(os.path.abspath(__file__)))
os.chdir(WORK_DIR)
CKPT_DIR = os.path.join(WORK_DIR, 'checkpoints_ldh')
os.makedirs(CKPT_DIR, exist_ok=True)
LOG_PATH = os.path.join(WORK_DIR, 'run_log_resume.txt') TIME_BUDGET = float(os.environ.get('LDH_TIME_BUDGET', '10800')) # seconds; default 3h def log(msg): line = f"[{time.strftime('%H:%M:%S')}] {msg}" print(line, flush=True) with open(LOG_PATH, 'a') as f: f.write(line + '\n') log(f"Starting L_DH zero generation; WORK_DIR={WORK_DIR}; TIME_BUDGET={TIME_BUDGET:.0f}s") mpmath.mp.dps = 50
pari = cypari2.Pari()
pari.allocatemem(1024*1024*1024) T_MAX = 5200
DPS_PARI = 80 pari(f"default(realprecision, {DPS_PARI})")
pari("gz5 = znstar(5, 1)")
pari("Lchi = lfuncreate([gz5, [1]])")
pari("Lchibar = lfuncreate([gz5, [3]])")
log(f"Building lfuninit at dps={DPS_PARI}, T_max={T_MAX} ...")
t0 = time.time()
pari(f"Lchi_hi = lfuninit(Lchi, [{T_MAX}])")
pari(f"Lchibar_hi = lfuninit(Lchibar, [{T_MAX}])")
log(f"lfuninit done in {time.time()-t0:.1f}s") sqrt5 = mpmath.sqrt(5)
xi_dh = (mpmath.sqrt(10 - 2*sqrt5) - 2) / (sqrt5 - 1)
I = mpmath.mpc(0, 1)
A_const = (1 - I*xi_dh)/2
B_const = (1 + I*xi_dh)/2 def theta_dh(t): t = mpmath.mpf(t) return (t/2)*mpmath.log(5/mpmath.pi) + mpmath.im(mpmath.loggamma(mpmath.mpc(mpmath.mpf("0.75"), t/2))) def fix_pari_str(s): s = re.sub(r'\s+', '', str(s).strip()) s = s.replace('E', 'e') return s def Z(t): t = mpmath.mpf(t) s_str = f"(0.5) + ({mpmath.nstr(t, 70, strip_zeros=False)})*I" pari(f"v1 = lfun(Lchi_hi, {s_str})") pari(f"v2 = lfun(Lchibar_hi, {s_str})") Lc = mpmath.mpc(mpmath.mpf(fix_pari_str(pari("real(v1)"))), mpmath.mpf(fix_pari_str(pari("imag(v1)")))) Lcb = mpmath.mpc(mpmath.mpf(fix_pari_str(pari("real(v2)"))), mpmath.mpf(fix_pari_str(pari("imag(v2)")))) Ldh = A_const*Lc + B_const*Lcb return mpmath.re(mpmath.exp(I*theta_dh(t)) * Ldh) def sgn(x): return 1 if x > 0 else (-1 if x < 0 else 0) # Resume
zeros = []
t_start = mpmath.mpf("1.0")
ckpts = sorted([f for f in os.listdir(CKPT_DIR) if f.startswith('ldh_ckpt_') and f.endswith('.npy')])
if ckpts: last = ckpts[-1] label = last.replace('ldh_ckpt_','').replace('.npy','') meta_path = os.path.join(CKPT_DIR, f'ldh_ckpt_{label}_meta.json') if os.path.exists(meta_path): arr = np.load(os.path.join(CKPT_DIR, last), allow_pickle=True) zeros = [mpmath.mpf(str(s)) for s in arr] with open(meta_path) as f: meta = json.load(f) t_start = mpmath.mpf(meta['t_last']) log(f"Resumed from {last}: {len(zeros)} zeros, t_last={float(t_start):.4f}") h = mpmath.mpf("0.1")
N_TARGET = 5000
t = t_start
z_prev = Z(t)
s_prev = sgn(z_prev)
n_evals = 1
last_ckpt = (len(zeros) // 250) * 250 start = time.time()
last_report_time = start
budget_save_done = False def save_partial(reason): if not zeros: return arr = np.array([mpmath.nstr(z, 50, strip_zeros=False) for z in zeros], dtype=object) out_path = os.path.join(WORK_DIR, f'ldh_zeros_partial_dps50.npy') np.save(out_path, arr, allow_pickle=True) meta = {'n_zeros': len(zeros), 't_last': mpmath.nstr(t, 30), 'reason': reason, 'elapsed_s': time.time()-start} with open(os.path.join(WORK_DIR, 'ldh_zeros_partial_meta.json'), 'w') as f: json.dump(meta, f, indent=2) log(f"Partial save: {len(zeros)} zeros to {out_path} ({reason})") try: while len(zeros) < N_TARGET: # Time budget guard if time.time() - start > TIME_BUDGET: log(f"TIME BUDGET EXCEEDED at {len(zeros)} zeros, t={float(t):.2f}") save_partial("time_budget") budget_save_done = True break t_next = t + h z_next = Z(t_next) n_evals += 1 s_next = sgn(z_next) if s_next != s_prev and s_prev != 0: try: root = mpmath.findroot(Z, (t, t_next), solver='anderson') except Exception as e: log(f"Anderson failed at [{float(t)},{float(t_next)}]: {e}; trying illinois") try: root = mpmath.findroot(Z, (t, t_next), solver='illinois') except Exception as e2: log(f"Illinois failed: {e2}; trying bisect") root = mpmath.findroot(Z, (t, t_next), solver='bisect') n_evals += 12 if zeros and root <= zeros[-1]: log(f"WARNING: non-monotonic root {float(root)} <= prev {float(zeros[-1])}; skipping") else: zeros.append(root) if len(zeros) // 250 > last_ckpt // 250: last_ckpt = (len(zeros) // 250) * 250 label = f"{last_ckpt:05d}" arr = np.array([mpmath.nstr(z, 50, strip_zeros=False) for z in zeros], dtype=object) np.save(os.path.join(CKPT_DIR, f'ldh_ckpt_{label}.npy'), arr, allow_pickle=True) meta = {'n_zeros': len(zeros), 't_last': mpmath.nstr(t_next, 30), 'n_evals': n_evals} with open(os.path.join(CKPT_DIR, f'ldh_ckpt_{label}_meta.json'), 'w') as f: json.dump(meta, f) elapsed = time.time() - start rate = len(zeros) / elapsed if elapsed > 0 else 0 log(f"Checkpoint {label}: {len(zeros)} zeros, t={float(t_next):.2f}, " f"elapsed={elapsed/60:.1f}min, rate={rate:.2f} z/s, n_evals={n_evals}") t = t_next s_prev = s_next z_prev = z_next if time.time() - last_report_time > 60: last_report_time = time.time() elapsed = time.time() - start log(f"PROGRESS: {len(zeros)} zeros, t={float(t):.2f}, elapsed={elapsed/60:.1f}min")
except KeyboardInterrupt: log("Interrupted by user; saving partial") save_partial("keyboard_interrupt") budget_save_done = True if len(zeros) >= N_TARGET: log(f"DONE. Found {len(zeros)} zeros in {(time.time()-start)/60:.1f} minutes") sorted_ok = all(zeros[i] < zeros[i+1] for i in range(len(zeros)-1)) log(f"Strictly monotonic: {sorted_ok}") log(f"Total zeros: {len(zeros)}") log(f"First zero: {mpmath.nstr(zeros[0], 50)}") log(f"Last zero: {mpmath.nstr(zeros[-1], 50)}") arr = np.array([mpmath.nstr(z, 50, strip_zeros=False) for z in zeros], dtype=object) np.save(os.path.join(WORK_DIR, 'ldh_zeros_5000_dps50.npy'), arr, allow_pickle=True) log("Saved to ldh_zeros_5000_dps50.npy")
elif not budget_save_done: save_partial("loop_exit")
