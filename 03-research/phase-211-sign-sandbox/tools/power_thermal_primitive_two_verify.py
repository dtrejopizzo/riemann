"""Fixed certificate: the complete thermal primitive 2x2 block and its split.

192 bits; 960 panels on [1,16]; Taylor degree 40; thermal modes 1,2.
The parameters use four theta modes with a positive infinite tail.  All
omitted modes and the infinite temporal tail are bounded analytically.
No parameter search, adaptive quadrature, or floating-point sign tests.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from flint import arb, arb_series, ctx

BITS, PANELS, DEGREE, PARAM_MODES, MODES = 192, 960, 40, 4, 2
ctx.prec = BITS
ctx.cap = DEGREE + 1


def ball(q):
    q = F(q)
    return arb(q.numerator) / q.denominator


def error(q):
    return arb(0, ball(q).upper())


def positive_tail(q):
    return arb(ball(q / 2), ball(q / 2).upper())


pi = arb.pi()
assert pi > 3 and pi < ball(F(22, 7))
assert arb(3).exp() > 20
log2 = arb(2).log()
assert log2 > ball(F(2, 3)) and log2 < ball(F(7, 10))
C = F(101, 100)
# Successive terms n^d exp(-3n^2), n>=2 and d<=11.
assert F(3, 2)**11 / 20**5 < F(1, 1000)
assert 1 / (1 - F(1, 1000)) < C

# S_j is a FULL sum, enclosed by four exact modes and a positive tail.
S = {}
for j in (2, 4, 6, 8):
    prefix = sum(((-pi*n*n).exp() / n**j
                  for n in range(1, PARAM_MODES + 1)), arb(0))
    tail = C * F(1, 5**j * 20**25)
    S[j] = prefix + positive_tail(tail)
mu = [ball(1), ball(2), ball(6), ball(24)]
mu = [mu[j] * S[2*j+2] / pi**(j+2) for j in range(4)]
den = mu[2]*mu[0] - mu[1]**2
assert den > 0
b = mu[1]/mu[0]
alpha = (mu[3]*mu[0]-mu[2]*mu[1])/den
beta = (mu[3]*mu[1]-mu[2]**2)/den
assert b > ball(F(63, 100)) and b < ball(F(2, 3))
assert alpha > ball(F(19, 10)) and alpha < ball(F(48, 25))
assert beta > ball(F(3, 5)) and beta < ball(F(31, 50))
# R_i=(t-1)q_i.  For t>=1, |R|<=t^3, |R'|<=3t^2,
# |R''|<=6t, |R'''|<=6.  The q2 lower bound is >-1.
assert ball(F(3, 5))-ball(F(48, 25))**2/4 > -1
assert ball(F(48, 25))*2 < 4

# Common real-axis modal bounds for i=1,2:
# |F_i,n| <=39 n^4 t^(21/4) exp(-pi n^2 t).
# |Z_i,1| <=45 t^(21/4) exp(-pi t).
# |Z_i,n| <=73 n^10 log(n)t^(21/4) exp(-pi n^2t), n>=2.
assert pi*(2*pi+6) < 39
assert F(38, 27)/F(512, 3) + F(65, 32) < 3
assert F(25, 12)/F(512, 3) + F(195, 32) < 7
assert 6*pi + ball(F(7, 2)) < 23
assert 23*pi < 73
assert pi*(3*pi+ball(F(14, 3))) < 45


def T(d, n):
    return C * F(n**d, 20**(n*n))


# Every omitted pair has n^2+m^2>=10.  The B tail uses t^(19/2)
# and denominator pi(n^2+m^2)-19/2>20.  The log tail uses log(t)<=t,
# t^(21/2), and denominator >19.  Both include the measure dt/(2t).
assert 3*10-F(19, 2) > 20
assert 3*10-F(21, 2) > 19
s4 = F(1, 20) + T(4, 2)
RB = F(39, 40)*(73*s4*T(11, 3)
                    +45*T(4, 3)/20+73*T(4, 3)*T(11, 2))
RL = F(1521, 19)*T(4, 3)*s4
assert RB == F(510613632029241, 409600000000000000000)
assert RL == F(623421823401, 972800000000000000000)
assert RB < F(1, 500000) and RL < F(1, 10**9)
assert RB+RL < F(1, 400000)

# Infinite temporal tail of the retained modes beyond t=16.
# Sum |F|<=663 t^(21/4)e^(-pi t), sum |Z|<=149549 t^(21/4)e^(-pi t).
# log(t)<=t; integral_16^inf t^r e^-6t <=16^r e^-96/(6-r/16).
assert 39*(1+2**4) == 663
assert 45+73*2**11 == 149549
assert 6-F(21, 32) > 5
TEMP_B = F(663*149549*16**10, 2*5*20**32)
TEMP_L = F(663**2*16**11, 2*5*20**32)
assert TEMP_B+TEMP_L < F(1, 10**20)

# Complex bounds on radius-1/8 disks centered in [1,16].  Here |z|<17,
# Re z>7/8; |z-1|<18 and |4z-1|<69.  Branches log(z), z^(3/2)
# are holomorphic throughout these disks.  exp(-pi n^2 z) has modulus<1.
assert 18**3+2*18**2+18 < 10**4
assert 3*18**2+4*18+1 < 2000
assert 6*18+4 < 200
assert 69**3+2*69**2+69 < 4*10**5
assert 3*69**2+4*69+1 < 15000
HB = (2*4*4*17+3)*10**4+2*17*2000
LB = F(2000, 3)+F(200, 18)+F(6, 81)+8*(10**4+4*10**5)
LPB = F(200, 3)+F(6, 18)+8*(2000+4*15000)
assert HB < 10**7 and LB < 4*10**6 and LPB < 5*10**5
JB = (2*4*4*17+3)*(4*10**6)+2*17*(5*10**5)
assert JB < 3*10**9
# |z|^(5/4)<17^2, including each of the two modes.
assert 2*4*4*17**2*10**7 < 2*10**11
assert 2*4*17**2*(3*10**9) < 10**13
# |log z|<4 (log17<3 and |arg z|<1); |1/(2z)|<1.
assert arb(3).exp() > 17
assert F(1, 2)*F(8, 7) < 1
# This also bounds the direction F1+F2, Z1+Z2, with its extra factor4.
M = 10**30
assert 4*(4*(2*10**11)**2+2*10**11*10**13) < M
HALF = F(1, 128)
RADIUS = F(1, 8)
RATIO = HALF/RADIUS
assert RATIO == F(1, 16) and F(15, PANELS) == 2*HALF
REM_TAYLOR = 15*M*RATIO**(DEGREE+1)/(1-RATIO)
assert REM_TAYLOR < F(1, 10**18)


def fields(t):
    x = t-1
    y = 4*t-1
    # These are EXACT polynomial derivatives.  arb_series.derivative()
    # reduces the order of a truncated series, even for a polynomial; do
    # not use it here, since every subsequent jet must retain order 41.
    polys = [
        (x*(x-b), 2*x-b, arb(2), arb(0), y*(y-b), 2*y-b),
        (x*(x*x-alpha*x+beta), 3*x*x-2*alpha*x+beta,
         6*x-2*alpha, arb(6), y*(y*y-alpha*y+beta),
         3*y*y-2*alpha*y+beta),
    ]
    fs, zs = [], []
    for R, r1, r2, r3, R4, r14 in polys:
        ff = arb_series([0], prec=DEGREE+1)
        zz = arb_series([0], prec=DEGREE+1)
        for n in (1, 2):
            nn = n*n
            ex = (-pi*nn*t).exp()
            H = (2*pi*nn*t-3)*R-2*t*r1
            L = -r1/pi-r2/(2*pi*pi*nn)-r3/(3*pi**3*nn*nn)
            Lprime = -r2/pi-r3/(2*pi*pi*nn)
            if n == 2:
                # The only nonzero divisor is m=2.  Evaluate R(4t)
                # algebraically, preserving the full polynomial.
                L += 2*nn*log2*(R-R4)
                Lprime += 2*nn*log2*(r1-4*r14)
            J = (2*pi*nn*t-3)*L-2*t*Lprime
            ff += nn*ex*H
            zz += ex*J
        assert ff.prec == DEGREE+1 and zz.prec == DEGREE+1
        fs.append(ff)
        zs.append(zz)
    return fs, zs


def integrate_polynomial(series):
    # Exact integral of the retained Taylor polynomial on [-HALF,HALF].
    assert series.prec == DEGREE+1
    return sum((series[k]*ball(2*HALF**(k+1)/F(k+1))
                for k in range(0, DEGREE+1, 2)), arb(0))


print('Fixed certificate: bits=192 panels=960 degree=40 interval=[1,16]', flush=True)
print('Parameters b, alpha, beta:', b, alpha, beta, flush=True)
print('PASS analytic parameter, modal, temporal and Cauchy error gates', flush=True)
totals = [arb(0) for _ in range(4)]
for panel in range(PANELS):
    center = F(1)+F(2*panel+1, 128)
    t = arb_series([ball(center), 1], prec=DEGREE+1)
    fs, zs = fields(t)
    logt = t.log()
    weight = pi*pi/2*(ball(F(3, 2))*logt).exp()
    integrands = []
    for i, j in ((0, 0), (0, 1), (1, 1)):
        integrands.append(weight*(logt*fs[i]*fs[j]
                              +(fs[i]*zs[j]+fs[j]*zs[i])/2))
    integrands.append(weight*(fs[0]+fs[1])*(zs[0]+zs[1]))
    assert all(s.prec == DEGREE+1 for s in integrands)
    for j in range(4):
        totals[j] += integrate_polynomial(integrands[j])
    if (panel+1) % 240 == 0:
        print('PASS finite integration panels:', panel+1, flush=True)

# Inflation is BEFORE every sign gate.  Parameter uncertainty is already in
# every coefficient.  Symmetric cross entries use the exact average above.
EQ = RB+RL+TEMP_B+TEMP_L+REM_TAYLOR
EB_DIRECTION = 4*RB+4*TEMP_B+REM_TAYLOR
q11, q12, q22 = [totals[j]+error(EQ) for j in range(3)]
qb_direction = totals[3]+error(EB_DIRECTION)
assert q11 > ball(F(179, 100000)), ('Q11', q11)
assert q22 > ball(F(17, 10000)), ('Q22', q22)
assert q12.abs_upper() < ball(F(79, 50000)), ('Q12', q12)
DET_GATE = F(179, 100000)*F(17, 10000)-F(79, 50000)**2
assert DET_GATE == F(2733, 5000000000) and DET_GATE > 0
assert qb_direction < -ball(F(1, 20000)), ('QB direction', qb_direction)
print('FULL Q11:', q11, flush=True)
print('FULL Q12 (symmetric cross):', q12, flush=True)
print('FULL Q22:', q22, flush=True)
print('FULL QB(P1+P2):', qb_direction, flush=True)
print('Certified determinant lower:', ball(DET_GATE), flush=True)
print('Errors per Q entry:', ball(EQ), flush=True)
print('Error QB direction:', ball(EB_DIRECTION), flush=True)
print('SHA256:', sha256(Path(__file__).read_bytes()).hexdigest(), flush=True)
print('FULL PASS: complete primitive 2x2 SPD; QB(P1+P2)<-1/20000', flush=True)
print('Scope: this fixed block only; no core, recurrence or global sign.', flush=True)
