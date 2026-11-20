"""Cover the gap in 112 using squares and cubes on multiplicative cells."""
from bisect import bisect_right
from math import isqrt
from flint import arb, ctx

ctx.prec = 100
h = arb(11)/25
stop = 10**10
upper = 2*stop
prime_limit = isqrt(upper)
prime = bytearray([1])*(prime_limit+1)
prime[:2] = bytes(2)
for p in range(2, isqrt(prime_limit)+1):
    if prime[p]:
        prime[p*p::p] = bytes((prime_limit-p*p)//p+1)
powers = sorted((p**k,p) for p in range(2,prime_limit+1) if prime[p]
                for k in (2,3) if p**k<=upper)
nodes = [n for n,p in powers]
mass, reciprocal = [arb(0)], [arb(0)]
for n,p in powers:
    d = arb(p).log()
    mass.append(mass[-1]+d)
    reciprocal.append(reciprocal[-1]+d/n)

a = ((h-(arb(1001)/1000).log())/2).exp()
v = 4*((h/2).cosh()-1)
assert a*a < 2
x = 999983
cells = 0
minimum = 1.
while x < stop:
    y = arb(x).sqrt()
    i = bisect_right(nodes,int((x/(a*a)).floor().unique_fmpz()))
    j = bisect_right(nodes,x)
    k = bisect_right(nodes,int((x*a*a).floor().unique_fmpz()))
    value = (a*(mass[j]-mass[i])/y-y*(reciprocal[j]-reciprocal[i])/a
             +a*y*(reciprocal[k]-reciprocal[j])-(mass[k]-mass[j])/(a*y))/(2*v)
    minimum = min(minimum,float(value))
    assert value > arb('.497'), (x,value)
    x = min(stop,x+x//1000)
    cells += 1
print(cells, 'cells; certified >0.497; minimum midpoint', minimum)
