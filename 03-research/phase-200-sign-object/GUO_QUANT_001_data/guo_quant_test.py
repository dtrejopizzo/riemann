# GUO_QUANT_001 §3 (NUMÉRICO): J = g*(T) del extremal de Mori μ=15 y cociente W*/(J²Σ_{γ>0}|ρ|^{-2}).
import json, mpmath as mp, re, sys
mp.mp.dps = 60
D = '/home/trabajo/Documentos/research/riemann/03-research/phase-199-frontier-pattern/proof-L-sharp/MORI15_EXTREMAL_001_data/'
mid = lambda s: mp.mpf(re.sub(r'^\[|\s*\+/-.*$|\]$', '', str(s)).strip() or '0')
eig = json.load(open(D+'p0_eig.json')); pcs = json.load(open(D+'p0_pieces.json')); pro = json.load(open(D+'p0_prolate_M28.json'))
v = [mp.mpf(x) for x in eig['vectors'][0]]
L = mp.log(15)/2
# base par: φ_j, j = 0,2,4,... ; φ_j(L) = sqrt((2j+1)/(2L))
J = mp.fsum(vk*mp.sqrt((4*k+1)/(2*L)) for k, vk in enumerate(v))
g0 = mp.fsum(vk*mp.sqrt((4*k+1)/(2*L))*mp.legendre(2*k, 0) for k, vk in enumerate(v))
Q = mid(pcs['Q=v(A+J)v'])
S = 2 + mp.euler - mp.log(4*mp.pi)          # Σ_ρ 1/(ρ(1-ρ)) (todos los ρ)
Shalf = S/2                                  # Σ_{γ>0}|ρ|^{-2} bajo línea crítica = 0.0230957...
print('J (recomputado)      =', mp.nstr(J, 20)); print('J (p0_prolate_M28)   =', pro['g(T)'])
print('g(0) recomputado     =', mp.nstr(g0, 15), ' archivo:', pro['g(0)'])
print('Σ_{γ>0}|ρ|^-2        =', mp.nstr(Shalf, 20))
print('Q (Mori, compr.)     =', mp.nstr(Q, 20))
r = Q/(J**2*Shalf); print('Q/(J²·Σ)             =', mp.nstr(r, 20))
for tail in (mp.mpf('1e-71'), mp.mpf('2e-71')):
    print('  con cola Ω +%s:   ' % mp.nstr(tail,2), mp.nstr((Q+tail)/(J**2*Shalf), 10))
# modelo de salto puro: F(t) ≈ 2J sin(Tt)/t ⇒ Σ_{γ>0} 2|F(γ)|² ; promedio sin²=1/2 ⇒ ≈ 4J²Σγ^{-2}
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
mp.mp.dps = 20
s = mp.mpf(0); s2 = mp.mpf(0)
for n in range(1, N+1):
    gm = mp.im(mp.zetazero(n)); s += 2*(2*mp.sin(L*gm)/gm)**2; s2 += 1/(mp.mpf(1)/4+gm**2)
tailjump = 4*mp.quad(lambda t: mp.log(t/(2*mp.pi))/(2*mp.pi)/t**2, [gm, mp.inf])  # ⟨sin²⟩=1/2
print('N zeros =', N, ' Σ_{γ≤γ_N}|ρ|^-2 =', mp.nstr(s2, 10), ' (límite', mp.nstr(Shalf,10), ')')
print('modelo salto: Σ 2|2 sin(Tγ)/γ|² (N) + cola =', mp.nstr(s+tailjump, 10), ' /Σ|ρ|^-2 =', mp.nstr((s+tailjump)/Shalf, 8))
# sector impar (base φ_j, j = 1,3,5,...)
mp.mp.dps = 50
e1 = json.load(open(D+'p1_eig.json')); p1 = json.load(open(D+'p1_pieces.json'))
v1 = [mp.mpf(x) for x in e1['vectors'][0]]
J1 = mp.fsum(vk*mp.sqrt((4*k+3)/(2*L)) for k, vk in enumerate(v1)); Q1 = mid(p1['Q=v(A+J)v'])
print('impar: J =', mp.nstr(J1, 15), ' Q =', mp.nstr(Q1, 15), ' Q/(J²Σ) =', mp.nstr(Q1/(J1**2*Shalf), 12))
