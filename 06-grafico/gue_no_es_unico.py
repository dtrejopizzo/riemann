"""
GUE no es 'la respuesta': es una CLASE de universalidad, no un operador.

Generamos 3 matrices GUE independientes. Las 3 tienen la MISMA estadistica
(la de los ceros), pero sus autovalores son TODOS DISTINTOS entre si y
distintos de los ceros. 'GUE' nombra una distribucion con infinitos miembros;
los ceros son UN miembro determinista, elegido por la aritmetica (los primos).

'Afinar el mecanismo' para pasar de la clase GUE al miembro exacto = inyectar
los primos = construir el operador aritmetico = RH. No es una perilla; es la
montania entera.
"""
import math
import numpy as np

g = np.loadtxt("zeros_10000.txt")
N = 10

def gue_spectrum(seed, N):
    rng = np.random.default_rng(seed)
    M = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N)))/math.sqrt(2)
    M = (M + M.conj().T)/2
    ev = np.sort(np.linalg.eigvalsh(M))
    return (ev - ev.min())/(ev.max()-ev.min())*(g[N-1]-g[0]) + g[0]

print("Ceros de Riemann (fijos, deterministas):")
print("  ", np.round(g[:N], 3), "\n")

for s in [1, 2, 3]:
    ev = gue_spectrum(s, N)
    print(f"GUE draw #{s} (misma estadistica, mismo rango):")
    print("  ", np.round(ev, 3))
print()
print("Las 3 tiradas GUE: estadistica identica, autovalores TODOS distintos.")
print("Ninguna reproduce los ceros. GUE = distribucion, no operador.")
print()
print("Lo que SELECCIONA el miembro correcto de la clase = los primos.")
print("Ese selector es el operador aritmetico que falta. Ahi esta TODO el problema.")
