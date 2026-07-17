"""
L_DH (Davenport-Heilbronn) function — verified definition. Definition: Let chi be the primitive Dirichlet character mod 5 of order 4: chi(1)=1, chi(2)=i, chi(3)=-i, chi(4)=-1, chi(5)=0 Let xi = (sqrt(10 - 2*sqrt(5)) - 2) / (sqrt(5) - 1) ≈ 0.28407904... Let A = (1 - i*xi)/2, B = (1 + i*xi)/2 (= conj(A)) L_DH(s) = A * L(s, chi) + B * L(s, chi_bar) Properties verified at mpmath dps=30/50: - Real on real axis (L_DH(real) is purely real). - Functional equation: xi_DH(s) = xi_DH(1-s) where xi_DH(s) = (5/pi)^(s/2) * Gamma((s+1)/2) * L_DH(s) (Odd character, so gamma factor uses (s+1)/2.) - Has off-critical-line zero near s ≈ 0.808517 + 85.699348i (Spira 1994). - First on-critical-line zero at t ≈ 5.094159844571... Z-function analogue (for finding critical-line zeros via sign changes): theta_DH(t) = (t/2)*log(5/pi) + Im[loggamma(3/4 + i*t/2)] Z_DH(t) = Re[exp(i*theta_DH(t)) * L_DH(1/2 + i*t)]
""" import mpmath mpmath.mp.dps = 50 # Constants (computed at high precision)
_SQRT5 = mpmath.sqrt(5)
XI_DH = (mpmath.sqrt(10 - 2*_SQRT5) - 2) / (_SQRT5 - 1)
_I = mpmath.mpc(0, 1)
_A = (1 - _I*XI_DH)/2
_B = (1 + _I*XI_DH)/2 # Character lists for mpmath.dirichlet (period 5, starting at chi(0)):
CHI_LIST = [mpmath.mpc(0), mpmath.mpc(1), _I, -_I, mpmath.mpc(-1)]
CHI_BAR_LIST = [mpmath.mpc(0), mpmath.mpc(1), -_I, _I, mpmath.mpc(-1)] def L_DH(s): """Davenport-Heilbronn L-function.""" return _A * mpmath.dirichlet(s, CHI_LIST) + _B * mpmath.dirichlet(s, CHI_BAR_LIST) def theta_DH(t): t = mpmath.mpf(t) return (t/2)*mpmath.log(5/mpmath.pi) + mpmath.im( mpmath.loggamma(mpmath.mpc(mpmath.mpf("0.75"), t/2)) ) def Z_DH(t): """Real-valued Hardy-Z analogue of L_DH on the critical line.""" t = mpmath.mpf(t) s = mpmath.mpc(mpmath.mpf("0.5"), t) return mpmath.re(mpmath.exp(_I * theta_DH(t)) * L_DH(s))
