"""Independent interval checks of the scalar inequalities in ROUND_175_A.md."""
from flint import arb, ctx

ctx.prec = 160
T = arb(26) / 25
R = 5000
G = 3 * 10**12
H = 2 * 10**10
m = 2 * 10**7
N = 10**10
omega = 2 * R
n = 64 * (1 + 10400)
pi = arb.pi()
one = arb(1)
a = arb(8 * R**2) / (3 * H**2)

def check(name, predicate):
    if not predicate:
        raise ArithmeticError(name)
    print("PASS", name)

prime_sum = sum(2 * arb(p).log() / arb(q).sqrt()
                for p, q in [(2, 2), (3, 3), (2, 4), (5, 5), (7, 7), (2, 8)])
z = arb(21) / 10
transition = arb(53) / 50
tail = 4 * (-z / 2).exp() / (1 - (-2 * z).exp())
polar_variation = 4 * (2 * transition.cosh() - 1)
polar_mass = 8 * transition.sinh()
check("prime and archimedean bounds", prime_sum < arb(6343)/1000 and tail < arb(143)/100)
check("polar bounds", polar_variation < 9 and polar_mass < arb(102)/10)
m_lower = (R/(2*pi)).log() - one/R - one/(2*R**2)
check("positive high density", (m_lower-prime_sum-(tail+polar_variation)/R)/(2*pi) > one/20)
check("lower density", (-arb(5373)/1000-prime_sum-tail-polar_mass)/(2*pi) > -4)
check("support guard", arb(16*m)/H < z-2*T)
check("interpolation remainder",
      (omega/pi).log()/2 + n*(3*one.exp()*omega*T/n).log() < -(4*T.sqrt()).log())
loss = 1800*(1+T*R)
check("Fourier leakage", 2*n*arb(256).log()+arb(64).log() < loss)
check("archimedean margin", a.log() > -32 and m*arb(2).log()-loss > 10)
check("far tail polynomial envelope", arb(10**9).log() + arb(3+G).log().log()
      - N*arb(100).log() < -700000002)
check("high-frequency absorption", m*(arb(2*H)/G)**16 * 10**9 * arb(3+G).log() < one/1000)
check("surviving form margin", 2*pi*(1-(-arb(2)).exp()) > (-one).exp())

T = arb(6)/5
R = 50000
m = 180000000
H = 150000000000
k = 16
omega = 2*R
n = 64*120001
z = arb(246)/100
edge = arb(5)/4
a = arb(k*R**2)/(3*H**2)
prime_sum += 2*arb(3).log()/3 + 2*arb(11).log()/arb(11).sqrt()
tail = 4*(-z/2).exp()/(1-(-2*z).exp())
polar_variation = 4*(2*edge.cosh()-1)
polar_mass = 8*edge.sinh()
check("6/5 prime and archimedean bounds", prime_sum < arb(853)/100 and tail < arb(12)/10)
check("6/5 polar bounds", polar_variation < 12 and polar_mass < 13)
m_lower = (R/(2*pi)).log()-one/R-one/(2*R**2)
check("6/5 density high", (m_lower-prime_sum-(tail+polar_variation)/R)/(2*pi) > one/20)
check("6/5 density low", (-arb(5373)/1000-prime_sum-tail-polar_mass)/(2*pi) > -5)
check("6/5 support", arb(2*k*m)/H < z-2*T)
check("6/5 interpolation", (omega/pi).log()/2+n*(3*one.exp()*omega*T/n).log() < -(4*T.sqrt()).log())
loss = 1800*(1+T*R)
check("6/5 leakage", 2*n*arb(256).log()+arb(64).log() < loss)
check("6/5 mask", (1-one/400)**(k-1) > arb(4)/5 and a.log() > -32)
check("6/5 margin", m*arb(2).log()-loss > 10 and 32*m < 6000000000)
check("6/5 low correction", arb(10**9).log()+arb(3+G).log().log()-N*arb(100).log() < -6000000002)
check("6/5 high correction", m*(arb(2*H)/G)**(2*k)*10**9*arb(3+G).log() < one/1000)
