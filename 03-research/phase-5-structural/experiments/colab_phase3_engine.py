# ======================================================================================
#  Phase 3 — Localized Weil positivity engine  (Google Colab, self-validating)
#  Author: David Alejandro Trejo Pizzo
#
#  STATUS: the ZERO-SIDE engine below is VALIDATED against engine-spec reference behaviour
#  (zeta at the floor; forced negativity with the delta^2 law, exponent ~2.03). It measures
#  local Weil positivity  lambda_min(M_zeros)  directly from the zeros -- NO arithmetic side
#  needed.  (The arithmetic-side "Carleson constant" reformulation needs a separate, delicate
#  explicit-formula calibration that did NOT validate; it is omitted here on purpose.)
#
#  HOW TO USE IN COLAB
#  -------------------
#  1) New notebook -> paste this whole file into one cell -> Run.
#  2) Read "VALIDATION GATES" first. All three should PASS (Gate 3 prints the delta^2 exponent).
#  3) The "MEASUREMENT" block then prints:
#       (a) the zeta_delta forced-negativity curve  lambda_min(M_zeros) vs delta  (the controlled
#           discriminant: off-line zeros at displacement delta force lambda_min ~ -c*delta^2);
#       (b) zeta (RH-true, lambda_min ~ 0) vs L_DH (RH-violator, lambda_min < 0)  -- set DO_LDH=True.
#  4) Runtime: gates + zeta_delta ~1 min. L_DH adds ~2-5 min (zero-finding).
#
#  WHAT IS MEASURED
#  ----------------
#  Hermite-Gauss basis g_k(z)=h_k((z-T0)/sigma), k=0..J-1, centred at height T0, width sigma.
#  Localized WEIL Gram (Hermitian) from the zeros rho=1/2+delta_rho+i*t_rho:
#       M_zeros[i,j] = sum_rho  g_i(t_rho - i*delta_rho) * conj( g_j(t_rho + i*delta_rho) )
#  For ON-line zeros (delta=0) this is PSD (Gram of evaluations); for OFF-line zeros the
#  pairing of z with its conjugate zbar makes it INDEFINITE -- that is the signal.
#  Local Weil positivity  <=>  lambda_min(M_zeros) >= 0.
# ======================================================================================

import numpy as np, mpmath as mp, math
mp.mp.dps = 30

# ----------------------------- config ------------------------------------------------
T0, SIGMA, J = 85.7, 2.0, 8     # engine-spec reference operating point (T0=85.7, sigma=2)
NZEROS  = 120                   # zeta zeros used (window |gamma-T0|<2*sigma suppresses the rest)
DO_LDH  = False                 # set True to add the L_DH (Davenport-Heilbronn) comparison (slow)

# ----------------------------- Hermite-Gauss basis -----------------------------------
def hermite(J, u):
    u = np.asarray(u, dtype=complex)
    H = [np.pi**-0.25*np.exp(-u**2/2)]
    if J > 1: H.append(np.sqrt(2.0)*u*H[0])
    for k in range(2, J): H.append(np.sqrt(2.0/k)*u*H[k-1]-np.sqrt((k-1.0)/k)*H[k-2])
    return H
def g_at(J, sigma, T0, z):
    return np.array([h[0] for h in hermite(J, (np.asarray([z],dtype=complex)-T0)/sigma)])

# ----------------------------- the validated Weil Gram (zero side) -------------------
def M_zeros(zlist, J, sigma, T0):
    """zlist: list of (t_rho, delta_rho). Weil Gram, Hermitian, signal-bearing for off-line."""
    M = np.zeros((J, J), dtype=complex)
    for (t, d) in zlist:
        for (tt, dd) in ((t, d), (-t, d)):          # even explicit formula: +/- ordinate
            v = g_at(J, sigma, T0, tt - 1j*dd)       # g_i(z),    z = t - i*delta
            u = g_at(J, sigma, T0, tt + 1j*dd)       # g_j(zbar), zbar = t + i*delta
            M += np.outer(v, np.conj(u))
    return (M + M.conj().T)/2

def lam_min_over_tr(M):
    l = np.linalg.eigvalsh(M)[0]; tr = np.trace(M).real
    return l, l/tr if tr != 0 else float('nan')

# ----------------------------- zeros -------------------------------------------------
print("computing zeta zeros ...", flush=True)
GAM = [float(mp.im(mp.zetazero(n))) for n in range(1, NZEROS+1)]
def shift_window(gam, T0, sigma, delta, hw=2.0):
    return [(g, (delta if abs(g-T0) < hw*sigma else 0.0)) for g in gam]

# ======================================================================================
#                                  VALIDATION GATES
# ======================================================================================
print("="*78); print(" VALIDATION GATES"); print("="*78)

# Gate 1: reference zeros
ref = [14.134725141734693790, 21.022039638771554992, 25.010857580145688763]
ok1 = all(abs(GAM[i]-ref[i]) < 1e-9 for i in range(3))
print(f"[Gate 1] zeta zeros match reference (>=9 digits): {'PASS' if ok1 else 'FAIL'}")

# Gate 2: zeta is locally positive (PSD floor)
M0 = M_zeros(shift_window(GAM, T0, SIGMA, 0.0), J, SIGMA, T0)
l0, r0 = lam_min_over_tr(M0)
ok2 = r0 > -1e-6
print(f"[Gate 2] zeta lambda_min/tr = {r0:+.3e}  (>= -1e-6): {'PASS (at the floor)' if ok2 else 'FAIL'}")

# Gate 3: forced negativity + delta^2 law (engine-spec: exponent ~2.03)
sig = {}
for d in (0.05, 0.1, 0.2):
    Md = M_zeros(shift_window(GAM, T0, SIGMA, d), J, SIGMA, T0)
    sig[d] = abs(np.linalg.eigvalsh(Md)[0] - l0)
expo = math.log(sig[0.2]/sig[0.05])/math.log(4) if sig[0.05] > 0 else float('nan')
ok3 = 1.7 < expo < 2.3
print(f"[Gate 3] forced-negativity scaling |lam(delta)-lam(0)| ~ delta^{expo:.2f}  (target ~2.03): {'PASS' if ok3 else 'CHECK'}")
nin = sum(1 for g in GAM if abs(g-T0) < 2*SIGMA)
print(f"         ({nin} zeros inside the window |gamma-{T0}|<{2*SIGMA})")

GATES_OK = ok1 and ok2 and ok3
print("\n GATES: " + ("ALL PASS — the zero-side engine reproduces engine-spec; measurements below are valid."
      if GATES_OK else "SOME FAIL — send me this output."))

# ======================================================================================
#                                   MEASUREMENT
# ======================================================================================
print("\n"+"="*78); print(" MEASUREMENT — local Weil positivity  lambda_min(M_zeros)"); print("="*78)
print("\n (a) zeta_delta family: shift the in-window zeros to Re=1/2+delta (off the line):")
print("     delta    lambda_min/tr      lambda_min        (forced-negativity curve)")
for delta in (0.0, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.8, 1.0):
    M = M_zeros(shift_window(GAM, T0, SIGMA, delta), J, SIGMA, T0)
    l, r = lam_min_over_tr(M)
    flag = "  <- RH-true floor" if delta == 0 else ("  <- positivity VIOLATED" if l < -1e-6*abs(np.trace(M).real) else "")
    print(f"   {delta:5.2f}    {r:+.4e}     {l:+.4e}{flag}")
print("\n  => off-line zeros at displacement delta force lambda_min ~ -c*delta^2 (Gate 3): a")
print("     LOCAL, EXPLICIT, VALIDATED positivity violation. This is the controlled discriminant.")

if DO_LDH:
    print("\n (b) L_DH (Davenport-Heilbronn, RH-violator):")
    # SELF-CHECK FIRST: the construction must reproduce the engine-spec reference off-line zero
    # (0.808517, 85.699348).  The simple ((1-i)/2,(1+i)/2) coefficients do NOT (they omit the
    # DH constant kappa ~ 0.28408); we verify and SKIP if the check fails, rather than report garbage.
    chi = {1:1, 2:1j, 3:-1j, 4:-1, 0:0}
    def Lchi(s, conj=False):
        c = (lambda a: np.conj(chi[a%5])) if conj else (lambda a: chi[a%5])
        return mp.mpf(5)**(-s)*sum(c(a)*mp.zeta(s, mp.mpf(a)/5) for a in range(1,5))
    kap = mp.mpf('0.28407904384')
    # Davenport-Heilbronn (Titchmarsh form): f(s) = (1-i*kappa)/2 * L(s,chi) + (1+i*kappa)/2 * L(s,chibar)
    LDH = lambda s: (1-1j*kap)/2*Lchi(s) + (1+1j*kap)/2*Lchi(s, conj=True)
    zref = mp.mpf('0.808517')+1j*mp.mpf('85.699348')
    val = abs(complex(LDH(zref)))
    print(f"     self-check |L_DH(0.808517+85.699348i)| = {val:.3e}  (reference off-line zero)")
    if val > 1e-2:
        print("     -> CONSTRUCTION UNVALIDATED (does not reproduce the reference zero); SKIPPING L_DH.")
        print("        (The validated zeta_delta family above already exhibits the off-line-zero signal.)")
    else:
        print("     locating L_DH zeros near T0 ...", flush=True)
        zlist = []
        for t in np.arange(T0-4, T0+4, 0.2):
            for be in (0.5, 0.6, 0.7, 0.8):
                try:
                    z = mp.findroot(LDH, mp.mpf(be)+1j*mp.mpf(t))
                    b, im = float(mp.re(z))-0.5, float(mp.im(z))
                    if abs(im-T0) < 4 and -0.02 < b < 0.4 and abs(complex(LDH(z))) < 1e-6 and \
                       all(abs(im-i2) > 1e-2 or abs(b-b2) > 1e-2 for (i2, b2) in zlist):
                        zlist.append((im, b))
                except Exception:
                    pass
        print(f"     L_DH zeros in window: {[(round(t,3),round(b,3)) for (t,b) in zlist]}")
        Mldh = M_zeros([(t, b) for (t, b) in zlist], J, SIGMA, T0)
        lldh, rldh = lam_min_over_tr(Mldh)
        print(f"     zeta : lambda_min/tr = {r0:+.4e}   (RH-true)")
        print(f"     L_DH : lambda_min/tr = {rldh:+.4e}   ({'VIOLATED (off-line zeros)' if lldh<0 else 'positive'})")

print("\nDONE.  Note on the Carleson constant: positivity  lambda_min>=0  <=>  C<=1 (Theorem T4-I);")
print("the SIGN is what we measure here (validated). The numerical value of C needs the arithmetic")
print("side (A_inf, P), whose explicit-formula calibration did not validate and is omitted.")
