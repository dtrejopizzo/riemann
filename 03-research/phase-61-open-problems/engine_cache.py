"""
Cache compartido para la Fase 2.3.F-CLOSE-II (N1 Lanczos, N2 trazas, N3 Liouville-Green).

build(lam,N,kind) es caro (cuadraturas mpmath dps>=40 por entrada + criba de primos hasta lam^2).
Las entradas de ARCH/PRIME son O(1) pero los autovalores eps_k ~ e^{-cL} ~ 1e-20 salen por
cancelacion masiva (ARCH=PRIME a >16 digitos). => hay que cachear las matrices a PRECISION PLENA
(50 digitos), NO en float (float destruiria el residuo e^{-cL}).

API:
  get_matrices(lam, N, kind, dps=40) -> (Larch, Lpr, A, L, idx)   [mpmath, full precision, cacheado]
  doob_spectrum(lam, N, kind, dps=40, nlow=8) -> dict con eps[], ratios[], V (mp), L, idx, Larch, Lpr
Reusa el engine de E70_doob_parter.py SIN reescribirlo.
"""
import os, json, mpmath as mp

CACHE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".cache_23F")
os.makedirs(CACHE_DIR, exist_ok=True)

# importar el engine de E70 (parts_entry, build, recon_grid, q_func) sin ejecutar su bloque final
_E70 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "E70_doob_parter.py")
exec(open(_E70).read().split('# ---- ejecutar')[0])  # define q_func, parts_entry, build, recon_grid, extract_C

_DIG = 50  # digitos guardados por entrada (suficiente para resolver el residuo 1e-20 desde O(1))


def _mat_to_strs(M):
    n = M.rows
    return [[mp.nstr(M[i, j], _DIG) for j in range(n)] for i in range(n)]


def _strs_to_mat(rows):
    n = len(rows)
    M = mp.zeros(n)
    for i in range(n):
        for j in range(n):
            M[i, j] = mp.mpf(rows[i][j])
    return M


def get_matrices(lam, N, kind='zeta', dps=40):
    """Devuelve (Larch, Lpr, A, L, idx) con cache en disco a precision plena."""
    mp.mp.dps = max(dps, _DIG)
    key = f"build_lam{float(lam):.4f}_N{int(N)}_{kind}.json"
    path = os.path.join(CACHE_DIR, key)
    if os.path.exists(path):
        with open(path) as fh:
            d = json.load(fh)
        mp.mp.dps = dps
        Larch = _strs_to_mat(d['Larch']); Lpr = _strs_to_mat(d['Lpr'])
        return Larch, Lpr, Larch - Lpr, d['L'], d['idx']
    # construir
    A, Larch, Lpr, L, idx = build(lam, N, kind)
    with open(path, 'w') as fh:
        json.dump({'Larch': _mat_to_strs(Larch), 'Lpr': _mat_to_strs(Lpr),
                   'L': float(L), 'idx': list(idx), 'lam': float(lam), 'N': int(N), 'kind': kind}, fh)
    mp.mp.dps = dps
    return Larch, Lpr, A, L, idx


def doob_spectrum(lam, N, kind='zeta', dps=40, nlow=8):
    """Espectro de Weil + datos para Doob. eps ordenados; V autovectores (mp); ratios eps_k/eps_0."""
    mp.mp.dps = dps
    Larch, Lpr, A, L, idx = get_matrices(lam, N, kind, dps)
    dim = len(idx)
    E, V = mp.eigsy(A)
    order = sorted(range(dim), key=lambda j: E[j])
    eps = [E[order[k]] for k in range(dim)]
    ratios = [eps[k] / eps[0] for k in range(min(nlow, dim))]
    return {'eps': eps, 'ratios': ratios, 'V': V, 'order': order,
            'L': L, 'idx': idx, 'Larch': Larch, 'Lpr': Lpr, 'dim': dim}


if __name__ == '__main__':
    # smoke test: reproducir ratios de E70 a lam=7
    d = doob_spectrum(7.0, 14, 'zeta')
    print("lam=7 ratios eps_k/eps_0:", [round(float(r), 4) for r in d['ratios'][:6]],
          " target (k+1)^2 = 1,4,9,16,25,36")
