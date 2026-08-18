"""
Por que 'construir el operador' es exactamente RH, mostrado con dos operadores.

(A) El operador de Hilbert-Polya VACUO:  H = diag(gamma_1, ..., gamma_N).
    Es autoadjunto y sus autovalores SON los ceros... pero se construyo
    A PARTIR de los ceros. No prueba nada. Es circular. Hilbert-Polya pide
    lo contrario: derivar los ceros de una estructura independiente.

(B) Una matriz GUE aleatoria, desdoblada a la densidad N(T).
    Sus autovalores tienen la MISMA estadistica que los ceros (repulsion,
    rigidez, rampa+meseta) pero NO SON los ceros. Muestra que la estadistica
    NO determina el operador: infinitas matrices comparten la fenomenologia.

Moraleja: exactitud => circular;  estadistica => no-unica.
El unico camino valido -derivar los gamma EXACTOS desde la aritmetica y probar
autoadjuncion- es el problema abierto.
"""
import math
import numpy as np

g = np.loadtxt("zeros_10000.txt")
N = 12

# ---------- (A) operador vacuo diag(gamma) ----------
H_A = np.diag(g[:N])
autov_A = np.linalg.eigvalsh(H_A)
print("(A) H = diag(gamma):  autoadjunto, autovalores = ceros EXACTOS")
print("    autovalores:", np.round(autov_A, 4))
print("    ceros reales:", np.round(g[:N], 4))
print("    -> coincide perfecto PORQUE lo construimos con los ceros. CIRCULAR.\n")

# ---------- (B) matriz GUE con la misma densidad ----------
rng = np.random.default_rng(1)
M = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N))) / math.sqrt(2)
M = (M + M.conj().T) / 2          # matriz hermitica (GUE)
ev = np.sort(np.linalg.eigvalsh(M))
# reescalar a la ventana de los primeros N ceros (misma densidad media)
ev_scaled = (ev - ev.min())/(ev.max()-ev.min())*(g[N-1]-g[0]) + g[0]
print("(B) matriz GUE reescalada:  autoadjunta, estadistica correcta")
print("    autovalores:", np.round(ev_scaled, 4))
print("    ceros reales:", np.round(g[:N], 4))
print("    -> MISMA estadistica, autovalores DISTINTOS. La estadistica no basta.\n")

print("CONCLUSION:")
print("  exactitud sin circularidad + autoadjuncion probada = RH.  Abierto.")
