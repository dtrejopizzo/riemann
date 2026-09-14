#!/usr/bin/env python3
"""
R145 / D.41 certification script.

Computes, for explicit curves C/F_q:
  (1) point counts N_m = #C(F_{q^m}) by brute force (m=1) and by the Weil numbers;
  (2) the model constant  s_C(gamma,theta) = sup_{n in Z} |cos(gamma n log q + theta)| / cosh(n log q /2),
      note n = 0 IS in the sample set, so s_C >= |cos theta| and s_C(.,0) = 1;
  (3) the threshold d_0 = 1/(1 - s_C^2) of the D.31.10-type witness, and a certified witness;
  (4) the canonical-kernel coefficients k_n of Lambda_C(z) = z^{-g} prod (z - u_i)
      (the model's Polya kernel) and the sign test "K_C >= 0?";
  (5) the Gram check  I_inf^C(delta_a, delta_b) = gamma_a . gamma_b = q^{-|a-b|/2} N_{|a-b|}
      (with N_0 := 2-2g), i.e. the dictionary  I_inf^C(E,F) = + (D_E . D_F);
  (6) the two support functions in the direction theta at a zero:
        pointwise (Frobenius-graph) cone   ->  1/2 * s_C
        positive / effective cone          ->  1/2
  (7) the preimage of the ruling class F_1 = {P} x C and the test class F_0;
  (8) [ROUND 2, finding F1] the theta-OPTIMISED constant s_C^* = min_theta s_C(gamma_1,theta),
      its closed form, the exact tie pattern, d_0^* and the minimal witness degree.

Usage:  python3 sC_and_points.py [--fast]
No external data.  mpmath used if available, else float (margins are wide).
"""
import sys, math, itertools

FAST = "--fast" in sys.argv
NMAX = 12 if FAST else 60          # range of n in the sup defining s_C
MARGIN_DIGITS = 12

# ---------------------------------------------------------------- point counts
def ec_points_F2(a1,a2,a3,a4,a6):
    """#E(F_2) for y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6 over F_2 (affine + 1)."""
    n = 1                                            # point at infinity
    for x in (0,1):
        for y in (0,1):
            lhs = (y*y + a1*x*y + a3*y) % 2
            rhs = (x**3 + a2*x*x + a4*x + a6) % 2
            if lhs == rhs: n += 1
    return n

def ec_points_F3(a2,a4,a6):
    """#E(F_3) for y^2 = x^3 + a2 x^2 + a4 x + a6 over F_3."""
    n = 1
    for x in range(3):
        rhs = (x**3 + a2*x*x + a4*x + a6) % 3
        for y in range(3):
            if (y*y) % 3 == rhs: n += 1
    return n

def smooth_F2(a1,a2,a3,a4,a6):
    # discriminant of a general Weierstrass equation, reduced mod 2
    b2 = a1*a1 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    disc = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    return disc % 2 != 0

def smooth_F3(a2,a4,a6):
    b2 = 4*a2; b4 = 2*a4; b6 = 4*a6; b8 = 4*a2*a6 - a4*a4
    disc = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    return disc % 3 != 0

# ---------------------------------------------------------------- model pieces
def weil_angles(q, a, g=1):
    """genus 1: alpha = (a +- i sqrt(4q-a^2))/2, u = alpha/sqrt(q) = e^{i theta}."""
    assert a*a <= 4*q
    th = math.acos(a/(2*math.sqrt(q)))
    return [th, -th]                                   # arg(u_i)

def N_m(q, a, m):
    """#C(F_{q^m}) for genus 1 with trace a;  N_0 := 2 - 2g = 0."""
    if m == 0: return 2 - 2*1
    th = math.acos(a/(2*math.sqrt(q)))
    S = 2*(q**(m/2))*math.cos(m*th)                    # alpha^m + alphabar^m
    return q**m + 1 - S

def s_C(q, theta_u, theta, nmax=NMAX):
    """sup_{n in Z} |cos(n*theta_u + theta)| / cosh(n log q / 2).  n=0 included."""
    L = math.log(q); best = 0.0; argbest = 0
    for n in range(-nmax, nmax+1):
        v = abs(math.cos(n*theta_u + theta)) / math.cosh(n*L/2)
        if v > best: best, argbest = v, n
    return best, argbest

def lambda_coeffs(q, a):
    """genus 1: Lambda_C(z) = z + k0 + 1/z with k0 = -(u+ubar) = -a/sqrt(q).
       Returns dict n -> k_n."""
    return {-1: 1.0, 0: -a/math.sqrt(q), 1: 1.0}

# ---------------------------------------------------------------- linear algebra on V_C (g=1)
def ev(q, theta_u, n):
    """(Phi(1), Phi(0), Re Phi(rho), Im Phi(rho)) of the point mass delta_n."""
    return (q**(n/2), q**(-n/2), math.cos(n*theta_u), math.sin(n*theta_u))

def solve4(rows, rhs):
    """tiny Gaussian elimination, 4x4."""
    M = [list(r)+[b] for r,b in zip(rows,rhs)]
    k = len(M)
    for i in range(k):
        p = max(range(i,k), key=lambda r: abs(M[r][i]))
        if abs(M[p][i]) < 1e-13: return None
        M[i],M[p] = M[p],M[i]
        piv = M[i][i]
        M[i] = [v/piv for v in M[i]]
        for r in range(k):
            if r!=i and M[r][i]!=0:
                f = M[r][i]; M[r] = [v-f*w for v,w in zip(M[r],M[i])]
    return [M[i][k] for i in range(k)]

def I_inf(E, F):
    """I_inf^C on coordinates (a,b,x,y):  a_E b_F + b_E a_F - 2(x_E x_F + y_E y_F)."""
    return E[0]*F[1] + E[1]*F[0] - 2*(E[2]*F[2] + E[3]*F[3])

# ================================================================= run
print("="*78)
print("R145 D.41 — function-field model of the row-D frame:  s_C, point counts,")
print("            the dictionary Gram, and the D.31.10-type witness")
print("            mode:", "FAST" if FAST else "FULL", " n-range +-%d" % NMAX)
print("="*78)

# ---- (1) explicit curves over F_2 and F_3, by brute force
print("\n[1] Explicit curves, point counts by brute force (N_1) and trace a = q+1-N_1")
curves = []
seen = set()
for a1,a2,a3,a4,a6 in itertools.product((0,1),repeat=5):
    if not smooth_F2(a1,a2,a3,a4,a6): continue
    N1 = ec_points_F2(a1,a2,a3,a4,a6); a = 3 - N1
    key = ("F2", a)
    if key in seen: continue
    seen.add(key); curves.append((2, a, N1, "E/F_2: y^2+%dxy+%dy = x^3+%dx^2+%dx+%d"%(a1,a3,a2,a4,a6)))
for a2,a4,a6 in itertools.product((0,1,2),repeat=3):
    if not smooth_F3(a2,a4,a6): continue
    N1 = ec_points_F3(a2,a4,a6); a = 4 - N1
    key = ("F3", a)
    if key in seen: continue
    seen.add(key); curves.append((3, a, N1, "E/F_3: y^2 = x^3+%dx^2+%dx+%d"%(a2,a4,a6)))
for q,a,N1,lbl in sorted(curves, key=lambda t:(t[0],t[1])):
    print("   %-42s q=%d N_1=%d a=%+d  h=P(1)=%d" % (lbl, q, N1, a, 1-a+q))
print("    -> %d isogeny classes in all (%d over F_2, %d over F_3)."
      % (len(curves), sum(1 for c in curves if c[0]==2), sum(1 for c in curves if c[0]==3)))

# ---- pick the curve of record: ordinary, over F_2, a = -1
Q, A = 2, -1
lbl = [c for c in curves if c[0]==Q and c[1]==A][0][3]
print("\n    CURVE OF RECORD: %s   (q=%d, g=1, a=%+d, N_1=%d, h=%d, ordinary)"
      % (lbl, Q, A, Q+1-A, 1-A+Q))
th = weil_angles(Q, A)[0]
print("    Weil numbers: alpha = (%+d +- i sqrt(%d))/2, |alpha| = sqrt(q);  u = alpha/sqrt(q),"
      % (A, 4*Q-A*A))
print("    theta_u = arg(u) = %.*f rad ;  gamma_1 = theta_u/log q = %.*f"
      % (MARGIN_DIGITS, th, MARGIN_DIGITS, th/math.log(Q)))
print("    N_m (m=0..6):", [round(N_m(Q,A,m),9) for m in range(7)])

# ---- (2) s_C
print("\n[2] The model constant s_C(gamma_1, theta)")
for tname, tval in (("theta = 0", 0.0), ("theta = pi/2", math.pi/2), ("theta = pi/4", math.pi/4)):
    v, n = s_C(Q, th, tval)
    print("    s_C(%-12s) = %.*f      (sup attained at n = %d)" % (tname, MARGIN_DIGITS, v, n))
sC, nstar = s_C(Q, th, math.pi/2)
# max over theta
best = 0.0; bt = 0.0
K = 200 if FAST else 4000
for i in range(K+1):
    t = math.pi*i/K
    v,_ = s_C(Q, th, t, nmax=min(NMAX,20))
    if v > best: best, bt = v, t
print("    max_theta s_C = %.*f at theta = %.6f   (= 1, attained at theta in pi Z, n = 0)"
      % (MARGIN_DIGITS, best, bt))
print("    ARITHMETIC COMPARISON (imported, R142_001 Prop D.31.5): s_1 = 0.99846016271880910923")
print("    MODEL:  s_C(gamma_1, pi/2) = %.*f   ->  the gap 1 - s_C = %.*f is %.1fx the arithmetic one"
      % (MARGIN_DIGITS, sC, MARGIN_DIGITS, 1-sC, (1-sC)/(1-0.99846016271880910923)))

# ---- (3) witness
print("\n[3] The D.31.10-type witness  E = t F_0 + d kappa_C   (chi = 0)")
d0 = 1.0/(1.0 - sC*sC)
print("    threshold d_0 = 1/(1 - s_C^2) = %.*f      (arithmetic: 324.9598266...)" % (MARGIN_DIGITS, d0))
d = math.ceil(d0) + 1
lo = 0.5*sC*d
hi = math.sqrt(d*(d-1))/2
print("    take d = %d :  admissible window for t = |Im Phi_E(rho_1)| is (%.*f, %.*f), width %.*f"
      % (d, MARGIN_DIGITS, lo, MARGIN_DIGITS, hi, MARGIN_DIGITS, hi-lo))
t = 0.5*(lo+hi)
E = (d/2, d/2, 0.0, t)          # (a,b,x,y) of t*F_0 + d*kappa_C with F_0 = (0,0,0,1)
deg = E[0]+E[1]; II = I_inf(E,E); R = 0.5*II - 0.25*deg
print("    t = %.*f :  deg E = %.*f, I_inf(E,E) = %.*f, R(E) = %.*f  > 0 ? %s"
      % (MARGIN_DIGITS,t, MARGIN_DIGITS,deg, MARGIN_DIGITS,II, MARGIN_DIGITS,R, R>0))
print("    |Re(e^{i pi/2} Phi_E(rho_1))| = %.*f   vs   (1/2) s_C deg E = %.*f   -> VIOLATED ? %s"
      % (MARGIN_DIGITS,t, MARGIN_DIGITS,0.5*sC*deg, t > 0.5*sC*deg))
print("    old (non-sharp) bound (1/2) deg E = %.*f   -> satisfied ? %s"
      % (MARGIN_DIGITS,0.5*deg, t <= 0.5*deg))
print("    margin against the violated bound: %.3e" % (t - 0.5*sC*deg))

# ---- (4) the canonical kernel
print("\n[4] The model canonical class K_C:  Phi_{K_C}(s) = Lambda_C(z), z = q^{s-1/2}")
for q_,a_,N1_,lb in sorted(curves, key=lambda t:(t[0],t[1])):
    k = lambda_coeffs(q_,a_); h = 1-a_+q_
    degK = sum(k[n]*2*math.cosh(n*math.log(q_)/2) for n in k)
    pos = all(v >= 0 for v in k.values())
    print("    q=%d a=%+d : k_{-1},k_0,k_1 = %+.6f %+.6f %+.6f   K_C>=0? %-5s  deg K_C = %.6f  (= 2h q^{-g/2} = %.6f)"
          % (q_,a_,k[-1],k[0],k[1], pos, degK, 2*h/math.sqrt(q_)))
print("    -> K_C >= 0 holds iff a <= 0, i.e. iff N_1 >= q+1.  REFUTES the blueprint's guess that")
print("       nonnegativity of the coefficients of Z_C forces K_C >= 0: it is the NUMERATOR P(T),")
print("       not Z_C, whose Fourier coefficients are K_C.")

# ---- (5) the dictionary Gram
print("\n[5] Dictionary check:  I_inf^C(delta_a, delta_b) =? gamma_a . gamma_b = q^{-|a-b|/2} N_{|a-b|}")
ok = True; worst = 0.0
for a_ in range(-4,5):
    for b_ in range(-4,5):
        lhs = I_inf(ev(Q,th,a_), ev(Q,th,b_))
        rhs = Q**(-abs(a_-b_)/2) * N_m(Q,A,abs(a_-b_))
        worst = max(worst, abs(lhs-rhs))
        ok = ok and abs(lhs-rhs) < 1e-9
print("    all |a|,|b| <= 4 :  max |LHS - RHS| = %.3e   ->  %s" % (worst, "MATCH" if ok else "FAIL"))
print("    sign: I_inf^C(E,F) = + (D_E . D_F)  with D_E = sum_n E(n) q^{-|n|/2} Gamma_{q^n}")
print("          (the blueprint's proposed  I_inf^C = -(D_E . D_F)  is REFUTED)")
print("    fibre pairings:  D_E . F_1 = Phi_E(0),  D_E . F_2 = Phi_E(1),  deg E = D_E . (F_1+F_2)")
for n_ in range(-2,3):
    e = ev(Q,th,n_)
    print("       gamma_%+d :  . F_1 = %.6f = q^{-n/2},  . F_2 = %.6f = q^{n/2},  self = %.6f (= Gamma^2 q^{-|n|} = 0 for g=1)"
          % (n_, e[1], e[0], I_inf(e,e)))

# ---- (6) support functions
print("\n[6] Section cone vs pointwise cone: the support function in the direction y at rho_1")
print("    sup over the POINTWISE (Frobenius-graph) cone   sup_n |Im Phi(rho)| / deg  = (1/2) s_C = %.*f"
      % (MARGIN_DIGITS, 0.5*sC))
print("    sup over the POSITIVE cone {I(D,D) >= 0, deg > 0}                          = 1/2 = %.*f"
      % (MARGIN_DIGITS, 0.5))
print("    [g=1 ONLY.  C x C = E x E is an ABELIAN surface: every effective divisor is nef, so")
print("     D.D >= 0 on Eff, and Hodge index then gives |y| <= sqrt(ab) <= deg/2 -- the UPPER bound.")
print("     The lower bound is Hartshorne V.1.8 (D^2>0, D.H>0 => nD effective), so Effbar = Posbar.")
print("     The value 1/2 is a SUPREMUM over big classes; it is not attained by an integral")
print("     effective divisor.  For g >= 2 there are negative curves (Delta^2 = 2-2g) and the")
print("     upper bound is OPEN -- see R145_003 finding F2.]")
print("    ratio = s_C = %.*f   <  1.   MODEL DEFICIT PRESENT, and larger than the arithmetic one."
      % (MARGIN_DIGITS, sC))

# ---- (7) the ruling class and the test class as elements of D^W_C
print("\n[7] Explicit preimages in D^W_C (finitely supported, support {-1,0,1,2})")
sup = [-1,0,1,2]
rows = [[ev(Q,th,n)[k] for n in sup] for k in range(4)]
for name, target in (("F_1 = {P} x C  -> (a,b,x,y) = (1,0,0,0)", [1.0,0.0,0.0,0.0]),
                     ("F_2 = C x {P}  -> (a,b,x,y) = (0,1,0,0)", [0.0,1.0,0.0,0.0]),
                     ("F_0 (test)     -> (a,b,x,y) = (0,0,0,1)", [0.0,0.0,0.0,1.0]),
                     ("kappa_C        -> (a,b,x,y) = (.5,.5,0,0)", [0.5,0.5,0.0,0.0])):
    sol = solve4(rows, target)
    chk = [sum(sol[i]*ev(Q,th,sup[i])[k] for i in range(4)) for k in range(4)]
    print("    %-44s E = %s" % (name, ", ".join("E(%+d)=%+.6f"%(sup[i],sol[i]) for i in range(4))))
    print("        %-40s   check ev = (%.2e off), pointwise >= 0 ? %s"
          % ("", max(abs(c-t2) for c,t2 in zip(chk,target)), all(v>=-1e-12 for v in sol)))
print("    -> the ruling classes F_1, F_2 ARE in the image of the dictionary and are effective on")
print("       C x C, but their preimages are NOT pointwise nonnegative.  That single class is the")
print("       whole gap:  E >= 0, E != 0  forces Phi_E(0) > 0 AND Phi_E(1) > 0, while F_1 has")
print("       Phi(0) = F_1.F_1 = 0.")

# ---- (8) [ROUND 2, F1] the theta-optimised constant
print("\n[8] [round 2, finding F1]  s_C is theta-DEPENDENT; the model's sharp constant")
def sC_of(theta, nmax=NMAX):
    return max(abs(math.cos(n*th + theta))/math.cosh(n*math.log(Q)/2) for n in range(-nmax,nmax+1))
lo_, hi_ = 0.0, math.pi
for _ in range(40 if FAST else 60):
    xs = [lo_ + (hi_-lo_)*i/200 for i in range(201)]
    vs = [sC_of(x, min(NMAX,40)) for x in xs]
    i  = min(range(201), key=lambda k: vs[k])
    lo_, hi_ = xs[max(0,i-1)], xs[min(200,i+1)]
tstar = 0.5*(lo_+hi_); sstar = sC_of(tstar)
cf = math.sqrt((4*Q-A*A)/((4*Q-A*A) + (Q+1+A)**2))
print("    theta*        = %.*f   (tan theta* = %.*f = (q+1+a)/sqrt(4q-a^2) = 2/sqrt7 = %.*f)"
      % (MARGIN_DIGITS, tstar, MARGIN_DIGITS, math.tan(tstar), MARGIN_DIGITS, 2/math.sqrt(7)))
print("    s_C^*         = %.*f   closed form sqrt((4q-a^2)/((4q-a^2)+(q+1+a)^2)) = %.*f"
      % (MARGIN_DIGITS, sstar, MARGIN_DIGITS, cf))
print("    sqrt(7/11)    = %.*f   |difference| = %.3e" % (MARGIN_DIGITS, math.sqrt(7/11), abs(sstar-math.sqrt(7/11))))
print("    tie pattern at theta* (the sup is attained at EVERY n printed with a '*'):")
for n in range(-4,5):
    v = abs(math.cos(n*th+tstar))/math.cosh(n*math.log(Q)/2)
    print("       n=%+d  %.*f %s" % (n, MARGIN_DIGITS, v, "*" if abs(v-sstar)<1e-9 else ""))
print("    -> EXACT TRIPLE TIE at n = -2, 0, +1 (verified in closed form in R145_003 Prop. D.41.12'):")
print("       n=0 : |cos theta*| = sqrt(7/11);  n=1 : |cos(theta_u+theta*)|/cosh(L/2) = sqrt(7/11);")
print("       n=-2: |cos(2 theta_u - theta*)|/cosh(L) = (5 sqrt7 / (4 sqrt11)) / (5/4) = sqrt(7/11).")
d0s = 1.0/(1.0 - sstar*sstar)
print("    d_0^* = 1/(1-(s_C^*)^2) = %.*f   (= 11/4 EXACTLY);  arithmetic optimum d_0 = 324.9598266..."
      % (MARGIN_DIGITS, d0s))
print("    minimal integer witness degrees:")
for name, sval in (("theta = pi/2  (arithmetic's choice)", sC), ("theta = theta* (model optimum)", sstar)):
    dmin = None
    for dd in range(1, 40):
        if 0.5*sval*dd < math.sqrt(dd*(dd-1))/2: dmin = dd; break
    lo2, hi2 = 0.5*sval*dmin, math.sqrt(dmin*(dmin-1))/2
    print("       %-36s s = %.9f  d_min = %d  window (%.9f, %.9f)  margin %.3e"
          % (name, sval, dmin, lo2, hi2, hi2-lo2))
print("    MISMATCH 11: arithmetically theta = pi/2 IS the optimum (min_theta s(gamma_1,theta) = s_1);")
print("                 on the lattice it is NOT, because n = 0 is a sample point.  A discreteness effect.")
print("    deficit of record: 1 - s_C^* = %.*f  =  %.1fx the arithmetic 1 - s_1 = 1.5398e-03"
      % (MARGIN_DIGITS, 1-sstar, (1-sstar)/(1-0.99846016271880910923)))

print("\nDone.")
