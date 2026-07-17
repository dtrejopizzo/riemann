"""
W-1 (plan WALL-FROM-2.3.F): el muro <=> eps_0(lambda) >= 0 sobre el ground state PF u_0.
eps_0(lambda) -> 0 (marginalidad, Teorema 12.2 PROBADO). Si ademas eps_0(lambda) es MONOTONA
decreciente y > 0, entonces eps_0 >= 0 para todo lambda => RH.

GATE: computar eps_0(lambda) a alta precision desde los builds cacheados; testear
  (1) signo: eps_0 > 0 para todo lambda?   (2) monotonia: eps_0 decreciente?
  (3) que tan suave/estructurada es la tendencia (para buscar la energia libre Phi).
Falsador DH (su eps_0 debe ser < 0 = imbalance O(1)).

Nota honestidad: eps_0 ~ e^{-cL} ~ 1e-21; con dps=40 y cancelacion O(1)->1e-21 quedan ~19 digitos
de eps_0, suficiente para signo y monotonia. La pregunta del muro es si eps_0 toca 0 por ARRIBA.
"""
import sys, mpmath as mp
from engine_cache import get_matrices

mp.mp.dps = 50


def eps0(lam, N, kind='zeta'):
    Larch, Lpr, A, L, idx = get_matrices(lam, N, kind, dps=50)
    E, _ = mp.eigsy(A)
    ev = sorted(float(E[i]) for i in range(A.rows))
    return ev[0], L, ev[1]


if __name__ == '__main__':
    grid = [(7.0, 14), (9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("W-1 GATE — eps_0(lambda): signo + monotonia (muro <=> eps_0>=0)")
    print(f"{'lam':>5} {'L':>6} {'eps_0':>16} {'eps_0*e^{L/2}':>16} {'signo':>7} {'mono?':>7}")
    prev = None; allpos = True; mono = True
    rows = []
    for lam, N in grid:
        e0, L, e1 = eps0(lam, N, 'zeta')
        import math
        scaled = e0 * math.exp(L / 2)  # quitar el decaimiento e^{-cL} aprox para ver la tendencia
        sg = '+' if e0 > 0 else '-'
        if e0 <= 0:
            allpos = False
        mo = ''
        if prev is not None:
            mo = 'baja' if e0 < prev else 'SUBE'
            if e0 >= prev:
                mono = False
        rows.append((lam, L, e0, scaled))
        print(f"{lam:>5} {L:>6.3f} {e0:>16.3e} {scaled:>16.4f} {sg:>7} {mo:>7}")
        prev = e0
    print(f"\n  eps_0 > 0 para todo lambda: {allpos}   |   eps_0 monotona decreciente: {mono}")
    # tendencia de eps_0 * e^{L/2} (deberia tender a una constante si eps_0 ~ C e^{-L/2})
    sc = [r[3] for r in rows]
    print(f"  eps_0*e^{{L/2}} = {[round(x,3) for x in sc]}  (¿tiende a constante => ley limpia?)")
    print("\nFALSADOR DH (eps_0 debe ser < 0):")
    e0d, Ld, _ = eps0(7.0, 14, 'DH')
    print(f"  DH lam=7: eps_0 = {e0d:.4e}  signo {'+' if e0d>0 else '-'}  "
          f"=> {'FALSADO OK (negativo)' if e0d < 0 else 'INESPERADO'}")
