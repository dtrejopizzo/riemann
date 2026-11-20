"""Lower bound for the square-prime term on whole cells of sqrt(x)."""
from bisect import bisect_right
from math import isqrt
from flint import arb, ctx

ctx.prec = 100
h = arb(11)/25
step = 5
start, stop = 100000, 1000000
a = ((h-2*(1+arb(step)/start).log())/2).exp()
v = 4*((h/2).cosh()-1)
bound = 1300000
assert a*stop < bound
prime = bytearray([1])*(bound+1)
prime[:2] = bytes(2)
for n in range(2, isqrt(bound)+1):
    if prime[n]:
        prime[n*n::n] = bytes((bound-n*n)//n+1)
ps = [n for n in range(2,bound+1) if prime[n]]
mass, square = [arb(0)], [arb(0)]
for p in ps:
    d = arb(p).log()
    mass.append(mass[-1]+d)
    square.append(square[-1]+d/(p*p))
minimum = 1.
for y in range(start,stop,step):
    i = bisect_right(ps,int((y/a).floor().unique_fmpz()))
    j = bisect_right(ps,y)
    k = bisect_right(ps,int((a*y).floor().unique_fmpz()))
    value = (a*(mass[j]-mass[i])/y-y*(square[j]-square[i])/a
             +a*y*(square[k]-square[j])-(mass[k]-mass[j])/(a*y))/(2*v)
    minimum = min(minimum,float(value))
    assert value > arb('.497'), (y,value)
print('certified > 0.497 on', (stop-start)//step, 'cells; minimum midpoint',minimum)
