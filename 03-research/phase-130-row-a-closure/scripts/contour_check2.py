import mpmath as mp
mp.mp.dps=25
p=3; L=mp.log(p); a=mp.mpf(3); t0=mp.mpf('1.3')
f=lambda t: mp.exp(-a*(t-t0)**2)
fhat=lambda tau: mp.sqrt(mp.pi/a)*mp.exp(-1j*tau*t0)*mp.exp(-tau**2/(4*a))   # closed form
def Wp_c(t):
    z=mp.power(p,-0.5-1j*t); w=mp.power(p,-0.5+1j*t); return L*(z/(1-z)+w/(1-w))
direct=L*sum(mp.power(p,-abs(m)/mp.mpf(2))*f(m*L) for m in range(-12,13) if m!=0)
axis=mp.quad(lambda s: fhat(s)*Wp_c(s), mp.linspace(-60,60,61))/(2*mp.pi)
K=400; res=sum(fhat(0.5j+2*mp.pi*k/L) for k in range(-K,K+1))
poisson=L*sum(f(m*L)*mp.power(p,m/mp.mpf(2)) for m in range(-12,13))
h=mp.mpf(1)
contour=mp.quad(lambda s: fhat(s+1j*h)*Wp_c(s+1j*h), mp.linspace(-60,60,61))/(2*mp.pi)
print("W_p direct      =", mp.nstr(direct,15))
print("axis integral   =", mp.nstr(axis,15))
print("residue sum     =", mp.nstr(res,15))
print("Poisson         =", mp.nstr(poisson,15))
print("contour (h=1)   =", mp.nstr(contour,15))
print("res + contour   =", mp.nstr(res+contour,15))
