"""
E32: ceros on-line de Davenport-Heilbronn, independientes (para validar el engine-DH).
f(s)=(sec th/2)(e^{-i th}L(s,chi)+e^{i th}L(s,chibar)), chi mod 5, chi(2)=i.
L(s,chi)=5^{-s} sum_{a=1}^4 chi(a) zeta(s,a/5)  (Hurwitz).
En s=1/2+it, f es real (x fase). Hallar cambios de signo = ceros on-line.
Tambien: localizar el cero off-line famoso (~0.808+85.7i) para ver si esta en rango.
"""
import mpmath as mp
mp.mp.dps = 30
k = (mp.sqrt(10-2*mp.sqrt(5)) - 2)/(mp.sqrt(5)-1)
theta = mp.atan(k)
chi = {1:mp.mpc(1,0), 2:mp.mpc(0,1), 3:mp.mpc(0,-1), 4:mp.mpc(-1,0)}
def Lchi(s, conj=False):
    tot = mp.mpc(0)
    for a in range(1,5):
        c = mp.conj(chi[a]) if conj else chi[a]
        tot += c*mp.zeta(s, mp.mpf(a)/5)
    return 5**(-s)*tot
def f(s):
    sec = 1/mp.cos(theta)
    return (sec/2)*(mp.e**(-1j*theta)*Lchi(s,False) + mp.e**(1j*theta)*Lchi(s,True))

# f en la linea: deberia ser real (x fase global). Tomamos parte real tras quitar fase.
def fline(t):
    val = f(mp.mpf('0.5')+1j*t)
    return val
# chequear realidad: arg const?
print("chequeo f(1/2+it):")
for t in [5,10,15,20]:
    v = fline(t); print(f"  t={t}: f={mp.nstr(v,6)}  |arg|={mp.nstr(mp.arg(v),4)}")

# La Z-funcion real: Z(t)=f(1/2+it)/phase. Por EF, e^{i*phi(t)} f es real. Usar Re tras rotar
# Aqui: hallar ceros de |f| (minimos a 0) o cambios de signo de una componente real.
# Como Lambda_f(1/2+it) es real (doc196), trabajamos con g(t)=Re(e^{-i a} f) con a=arg f en un t0 generico.
# Mas simple: ceros de f = ceros de |f|. Buscar minimos profundos de |f(1/2+it)|.
print("\nbuscando ceros on-line (min de |f(1/2+it)|) en t in [0,40]:")
ts = [mp.mpf(j)/10 for j in range(1,400)]
av = [abs(fline(t)) for t in ts]
zeros=[]
for i in range(1,len(av)-1):
    if av[i]<av[i-1] and av[i]<av[i+1] and av[i]<0.05:
        # refinar
        t0=ts[i]
        tr = mp.findroot(lambda t: mp.re(fline(t)/ (fline(t0)/abs(fline(t0)))), t0)
        zeros.append(tr)
print("  ceros on-line:", [mp.nstr(z,7) for z in zeros[:20]])

# cero off-line famoso de DH (Spira): ~ 0.808517 + 85.699i ; y mirror. Verificar f~0 ahi.
print("\ncero off-line (Spira) ~0.8085+85.699i:")
for s0 in [mp.mpc('0.808517','85.6993')]:
    print(f"  f({mp.nstr(s0,8)}) = {mp.nstr(f(s0),5)}")
