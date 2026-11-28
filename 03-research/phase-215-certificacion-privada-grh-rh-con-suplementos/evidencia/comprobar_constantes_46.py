"""Chequeos de consistencia a 80 decimales. NO son aritmética de intervalos."""
import mpmath as m
m.mp.dps=80
T=m.log(5)/2
c=240*T
A=2*m.log(2)/m.sqrt(2)+2*m.log(3)/m.sqrt(3)+m.log(2)
symbol=m.re(m.digamma(m.mpf(1)/4+120j))-m.log(m.pi)
for name,value in [('T',T),('c',c),('A',A),('m240',symbol),
                   ('s_infty_max',symbol-A),('omega_minus_min',2*A)]:
    print(name,m.nstr(value,45))
for k in [280,330]:
    term=lambda j:c**(2*j+1)/(2**(j+1)*m.gamma(j+m.mpf('1.5'))/m.sqrt(m.pi))**2
    # 500 positive summands: numerical approximation, not an upper enclosure.
    approx=2/m.pi*m.fsum(term(j) for j in range(k,k+500))
    print('Lambda_star',k,m.nstr(approx,45))
print('Z3 derived gap at21',m.nstr(m.mpf('.45166')*21-m.mpf(7)/8-m.mpf('1.588')-m.mpf('.137')*m.log(21)-m.mpf('.443')*m.log(m.log(21)),30))
