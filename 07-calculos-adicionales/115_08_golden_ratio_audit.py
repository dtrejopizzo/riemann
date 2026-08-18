#!/usr/bin/env python3
"""
115.08 -- Auditoria del "numero aureo" en sigma = e^{-(log 2)^2}.

Pregunta:  sigma = 0.618503...  y  1/phi = 0.618034...
           Es una identidad oculta, o una casi-coincidencia?

Se contesta con tres mediciones (fig 1) y tres tests sobre datos
aritmeticos reales (fig 2).  Sin ajustes, sin factores libres.

Salidas:
  115_08_fig1_sigma_vs_phi.png
  115_08_fig2_phi_en_primos_y_ceros.png
  115_08_resultados.txt
"""

import itertools
import math
import os

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- paleta
C_BLUE, C_ORANGE, C_AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, INK3 = "#141413", "#3d3d3a", "#73726c"
SURFACE, GRIDC = "#fcfcfb", "#e3e2dd"

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "axes.edgecolor": GRIDC, "axes.labelcolor": INK2,
    "xtick.color": INK3, "ytick.color": INK3,
    "text.color": INK, "font.size": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "grid.color": GRIDC, "grid.linewidth": 0.6,
    "lines.linewidth": 2.0,
})

# ---------------------------------------------------------- constantes
LOG2 = math.log(2.0)
SIGMA = math.exp(-LOG2 ** 2)            # la constante de 115_04
PHI = (1.0 + math.sqrt(5.0)) / 2.0
INV_PHI = 1.0 / PHI
REL = abs(SIGMA - INV_PHI) / INV_PHI    # separacion relativa

out = []
def say(s=""):
    out.append(s)
    print(s)

say("=" * 68)
say("1. LOS DOS NUMEROS, AL MAXIMO DE DIGITOS")
say("=" * 68)
say(f"  log 2            = {LOG2:.17f}")
say(f"  (log 2)^2        = {LOG2**2:.17f}")
say(f"  sigma = e^-(l2)^2= {SIGMA:.17f}")
say(f"  1/phi            = {INV_PHI:.17f}")
say(f"  sigma - 1/phi    = {SIGMA - INV_PHI:.3e}")
say(f"  error relativo   = {REL:.4e}   ({100*REL:.4f} %)")
say()
say("  sigma = 1/phi  <=>  (log 2)^2 = log phi:")
say(f"     (log 2)^2 = {LOG2**2:.15f}")
say(f"     log phi   = {math.log(PHI):.15f}")
say(f"     difieren en {math.log(PHI)-LOG2**2:.3e}  -> NO son el mismo numero.")
say("  Coinciden en 3 cifras significativas; difieren en la 4a.")
say()

# ------------------------------------------------------------- PANEL A
# sigma_b = exp(-(log b)^2): de donde sale realmente el 2.
B_STAR = math.exp(math.sqrt(math.log(PHI)))   # base donde sigma_b = 1/phi
say("=" * 68)
say("2. DE DONDE SALE EL 2:  N_t cuenta DIGITOS EN BASE 2")
say("=" * 68)
say("  r(m) ~ log m / log b  con b la base del codigo digital.")
say("  Con base b generica:  sigma_b = exp(-(log b)^2).")
say(f"  sigma_2      = {SIGMA:.9f}")
say(f"  sigma_b=1/phi en b* = {B_STAR:.9f}   (no es 2, es 2.0011)")
say("  => el aureo no se alcanza en la base del codigo, sino")
say("     0.05% mas lejos.  La 'aparicion' es que log2 ~ sqrt(log phi).")
say()

# ------------------------------------------------------------- PANEL B
# Cuantas constantes simples caen igual de cerca de sigma?
def catalogo_famosas():
    base = {
        "2": 2.0, "3": 3.0, "5": 5.0, "7": 7.0,
        "pi": math.pi, "e": math.e, "gamma": 0.5772156649015329,
        "sqrt2": math.sqrt(2), "sqrt3": math.sqrt(3), "sqrt5": math.sqrt(5),
        "ln2": LOG2, "ln3": math.log(3), "phi": PHI,
        "zeta3": 1.2020569031595943, "G": 0.9159655941772190,
    }
    vals = {}
    it = list(base.items())
    for (na, a), (nb, b) in itertools.product(it, it):
        cands = [(f"{na}+{nb}", a + b), (f"{na}-{nb}", a - b),
                 (f"{na}*{nb}", a * b), (f"{na}/{nb}", a / b),
                 (f"sqrt({na}*{nb})", math.sqrt(a * b)),
                 (f"{na}^(1/{nb})", a ** (1.0 / b))]
        try:
            cands.append((f"exp(-{na}/{nb})", math.exp(-a / b)))
            cands.append((f"{na}^-{nb}", a ** (-b)))
        except OverflowError:
            pass
        for name, v in cands:
            if math.isfinite(v) and 0.0 < v < 10.0:
                vals[name] = v
                vals["1/" + name] = 1.0 / v
    return np.array(sorted(set(round(v, 12) for v in vals.values()))), vals


def catalogo_cuadraticos(hmax=12):
    """(p + q*sqrt(d))/s, altura pequena: los algebraicos 'bonitos' de grado<=2."""
    vals = []
    for d in (2, 3, 5, 6, 7, 10, 13):
        rd = math.sqrt(d)
        for p in range(-hmax, hmax + 1):
            for q in range(-hmax, hmax + 1):
                for s in range(1, hmax + 1):
                    v = (p + q * rd) / s
                    if 0.3 < v < 1.2:
                        vals.append(v)
    return np.array(sorted(set(np.round(vals, 12))))


fam_arr, fam_map = catalogo_famosas()
cua_arr = catalogo_cuadraticos()

rs = np.logspace(-6, -1.3, 260)
cnt_fam = np.array([np.sum(np.abs(fam_arr - SIGMA) / SIGMA < r) for r in rs])
cnt_cua = np.array([np.sum(np.abs(cua_arr - SIGMA) / SIGMA < r) for r in rs])
n_fam_at = int(np.sum(np.abs(fam_arr - SIGMA) / SIGMA < REL))
n_cua_at = int(np.sum(np.abs(cua_arr - SIGMA) / SIGMA < REL))

vecinos = sorted(
    [(abs(v - SIGMA) / SIGMA, n, v) for n, v in fam_map.items()
     if abs(v - SIGMA) / SIGMA < 3 * REL])[:10]

say("=" * 68)
say("3. CALIBRACION: CUAN RARO ES ESTAR A 0.076% DE UNA CONSTANTE?")
say("=" * 68)
say(f"  catalogo A ({len(fam_arr)} valores: combinaciones simples de pi,e,phi,")
say(f"    sqrt2,ln2,gamma,zeta3,...)  -> {n_fam_at} caen tan cerca de sigma como 1/phi")
say(f"  catalogo B ({len(cua_arr)} valores: (p+q*sqrt d)/s, altura<=12)")
say(f"    -> {n_cua_at} caen tan cerca de sigma como 1/phi")
say()
say("  Vecinos de sigma dentro de 3x esa distancia (catalogo A):")
for rel, n, v in vecinos:
    say(f"    {n:>18s} = {v:.9f}   rel {rel:.2e}")
say()
say("  Es decir: a esta precision el aureo no es un vecino distinguido.")
say("  Tiene competencia, y el ojo elige al que ya conocia.")
say()

# ------------------------------------------------------------- PANEL C
# Consecuencia dura: si sigma fuera 1/phi, el teorema de 115_04 falla.
say("=" * 68)
say("4. TEST DECISIVO: FORZAR sigma = 1/phi Y VER SI EL TEOREMA SOBREVIVE")
say("=" * 68)
say("  115_04:  h0_t - h2_t = N_t * log(1/sigma).")
say("  El teorema pide que eso sea (log2)^2 N_t = t^2 ab, SIN factor espurio.")
FACTOR = math.log(PHI) / LOG2 ** 2
say(f"  Con sigma = e^-(log2)^2 :  log(1/sigma)/(log2)^2 = 1.000000000  (exacto)")
say(f"  Con sigma = 1/phi       :  log(phi)  /(log2)^2 = {FACTOR:.9f}")
say(f"  -> factor espurio de {100*(FACTOR-1):.4f} % en cada t.")
say("  Como N_t ~ t^2 ab/(log2)^2, el error ABSOLUTO crece como t^2:")
ts = np.arange(1, 201)
ab = 1.0
N_t = ts.astype(float) ** 2 * ab / LOG2 ** 2
err_phi = N_t * abs(math.log(PHI) - LOG2 ** 2)
say(f"     t=10   -> discrepancia {err_phi[9]:.3f}")
say(f"     t=100  -> discrepancia {err_phi[99]:.3f}")
say(f"     t=200  -> discrepancia {err_phi[199]:.3f}   (y diverge)")
say("  El covolumen NO deja elegir: 1/phi rompe la igualdad exacta que")
say("  es todo el contenido de 115_04.  sigma esta forzado, y no es phi.")
say()

# ============================================================== FIGURA 1
fig1, axes = plt.subplots(1, 3, figsize=(13.6, 4.3))

# --- A ---
ax = axes[0]
bb = np.linspace(1.55, 2.75, 600)
ax.plot(bb, np.exp(-np.log(bb) ** 2), color=C_BLUE, zorder=3)
ax.axhline(INV_PHI, color=C_ORANGE, ls="--", lw=1.6, zorder=2)
ax.plot([2.0], [SIGMA], "o", ms=8, color=C_BLUE, mec=SURFACE, mew=2, zorder=5)
ax.plot([B_STAR], [INV_PHI], "o", ms=8, color=C_ORANGE, mec=SURFACE, mew=2, zorder=5)
ax.annotate(f"base 2 (el codigo binario)\n$\\sigma={SIGMA:.6f}$",
            xy=(2.0, SIGMA), xytext=(2.10, 0.74), color=C_BLUE, fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=C_BLUE, lw=1))
ax.annotate(f"$1/\\varphi={INV_PHI:.6f}$\nse alcanza en $b={B_STAR:.4f}$",
            xy=(2.35, INV_PHI), xytext=(2.30, 0.50), color=C_ORANGE, fontsize=8.5,
            arrowprops=dict(arrowstyle="-", color=C_ORANGE, lw=1))
# lupa: a esta escala los dos puntos son el mismo; hay que ampliar 500x
axi = ax.inset_axes([0.10, 0.08, 0.36, 0.30])
bz = np.linspace(1.9985, 2.0035, 200)
axi.plot(bz, np.exp(-np.log(bz) ** 2), color=C_BLUE, lw=1.6)
axi.axhline(INV_PHI, color=C_ORANGE, ls="--", lw=1.2)
axi.plot([2.0], [SIGMA], "o", ms=5, color=C_BLUE, mec=SURFACE, mew=1)
axi.plot([B_STAR], [INV_PHI], "o", ms=5, color=C_ORANGE, mec=SURFACE, mew=1)
axi.set_xticks([2.000, 2.002]); axi.set_yticks([])
axi.tick_params(labelsize=7)
axi.set_title("lupa $\\times$500", fontsize=7.5, color=INK3, pad=2)
for sp in axi.spines.values():
    sp.set_color(GRIDC)
axi.spines["top"].set_visible(True); axi.spines["right"].set_visible(True)
ax.set_xlabel("base $b$ del codigo digital")
ax.set_ylabel("$\\sigma_b=e^{-(\\log b)^2}$")
ax.set_title("A. El 2 viene de contar digitos binarios\nel aureo cae en b=2.0011, no en b=2",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- B ---
ax = axes[1]
ax.step(rs, cnt_fam, where="post", color=C_BLUE, label="constantes simples")
ax.step(rs, cnt_cua, where="post", color=C_AQUA, label="cuadraticos altura$\\leq$12")
ax.axvline(REL, color=C_ORANGE, lw=1.6, ls="--")
ax.annotate("$1/\\varphi$ esta\naca", xy=(REL, 24), xytext=(REL * 0.28, 26),
            color=C_ORANGE, fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=C_ORANGE, lw=1))
ax.plot([2.63e-4], [1], "o", ms=7, color=INK3, mec=SURFACE, mew=1.5, zorder=6)
ax.annotate("$e^{-\\gamma/\\zeta(3)}$ esta 3 veces\nMAS cerca que $1/\\varphi$",
            xy=(2.63e-4, 1), xytext=(1.6e-6, 5.0), color=INK3, fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=INK3, lw=1))
ax.text(4.5e-3, 7.5, "constantes simples", color=C_BLUE, fontsize=8.5, ha="right")
ax.text(4.5e-3, 33, "cuadraticos $(p+q\\sqrt{d})/s$", color=C_AQUA,
        fontsize=8.5, ha="right")
ax.set_xscale("log"); ax.set_xlim(1e-6, 5e-3); ax.set_ylim(0, 40)
ax.set_xlabel("distancia relativa a $\\sigma$")
ax.set_ylabel("cuantas constantes caen mas cerca de $\\sigma$")
ax.set_title(f"B. A esa distancia ya hay {n_fam_at+n_cua_at} candidatos\nel aureo no es el vecino distinguido",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- C ---
ax = axes[2]
ax.plot(ts, err_phi, color=C_ORANGE)
ax.plot(ts, np.zeros_like(ts, dtype=float), color=C_BLUE)
ax.set_ylim(-4, 70)
ax.text(ts[-1] * .98, 48, "con $\\sigma=1/\\varphi$: error $\\sim t^2$, diverge ",
        color=C_ORANGE, fontsize=8.5, va="top", ha="right")
ax.text(ts[-1] * .98, 2.0, "con $\\sigma=e^{-(\\log 2)^2}$: error CERO, exacto en todo $t$",
        color=C_BLUE, fontsize=8.5, va="bottom", ha="right")
ax.set_xlabel("escala $t$")
ax.set_ylabel("$|(h^0_t-h^2_t)-\\frac{t^2}{2}B_{int}|$")
ax.set_title("C. El aureo rompe el teorema\nfactor espurio 0.158%, error $\\sim t^2$",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

fig1.suptitle("$\\sigma=e^{-(\\log 2)^2}=0.618503\\ldots$  frente a  $1/\\varphi=0.618034\\ldots$   "
              "— coinciden en 3 cifras, difieren en la 4a",
              fontsize=11.5, color=INK, x=0.008, ha="left", y=0.995)
fig1.tight_layout(rect=[0, 0, 1, 0.94])
p1 = os.path.join(HERE, "115_08_fig1_sigma_vs_phi.png")
fig1.savefig(p1, dpi=170)
say(f"[fig] {p1}")

# ============================================================== FIGURA 2
say()
say("=" * 68)
say("5. Y EN LOS PRIMOS / LOS CEROS?  TRES TESTS SOBRE DATOS REALES")
say("=" * 68)

# ---- ceros de zeta (Riemann-Siegel con correccion C0, vectorizado) ----
TWOPI = 2 * math.pi


def rs_theta(t):
    return (t / 2) * np.log(t / TWOPI) - t / 2 - math.pi / 8 \
        + 1 / (48 * t) + 7 / (5760 * t ** 3)


def zeros_up_to(T_MAX, step=0.0015, t0=10.0):
    """Ceros de Z por segmentos donde N=floor(sqrt(t/2pi)) es constante.

    Cada segmento [2pi N^2, 2pi (N+1)^2) se vectoriza sin mascaras y se
    procesa aparte, asi la memoria queda acotada aunque T_MAX sea grande.
    """
    zs = []
    prev_t = prev_Z = None
    Nmax = int(math.floor(math.sqrt(T_MAX / TWOPI)))
    for Nseg in range(1, Nmax + 1):
        a = max(t0, TWOPI * Nseg ** 2)
        b = min(T_MAX, TWOPI * (Nseg + 1) ** 2)
        if b <= a:
            continue
        t = np.arange(a, b, step)
        if t.size < 2:
            continue
        th = rs_theta(t)
        Z = np.zeros_like(t)
        for n in range(1, Nseg + 1):               # suma principal, N constante
            Z += np.cos(th - t * math.log(n)) / math.sqrt(n)
        Z *= 2.0
        u = np.sqrt(t / TWOPI)
        p = u - Nseg
        C0 = np.cos(TWOPI * (p * p - p - 1 / 16.0)) / np.cos(TWOPI * p)
        C0 = np.where(np.isfinite(C0), C0, 0.0)    # 0/0 removible en p=1/4,3/4
        Z += (1.0 if Nseg % 2 == 1 else -1.0) * u ** (-0.5) * C0
        if prev_t is not None:                     # costura entre segmentos
            t = np.r_[prev_t, t]
            Z = np.r_[prev_Z, Z]
        k = np.nonzero(np.sign(Z[:-1]) != np.sign(Z[1:]))[0]
        zs.append(t[k] - Z[k] * (t[k + 1] - t[k]) / (Z[k + 1] - Z[k]))
        prev_t, prev_Z = t[-1], Z[-1]
    return np.concatenate(zs)


cache = os.path.join(HERE, "115_08_zeros.npy")
T_MAX = 75000.0
if os.path.exists(cache):
    gam = np.load(cache)
else:
    gam = zeros_up_to(T_MAX)
    np.save(cache, gam)

# control: contra la formula de Riemann-von Mangoldt y contra mpmath
NT = rs_theta(T_MAX) / math.pi + 1
say(f"  control ceros: encontrados {len(gam)}, N(T) teorico {NT:.1f}")
import mpmath
mpmath.mp.dps = 15
for j in (0, 9, 99, 999):
    if j < len(gam):
        ref = float(mpmath.im(mpmath.zetazero(j + 1)))
        say(f"    gamma_{j+1:<4d} calculado {gam[j]:.6f}  exacto {ref:.6f}"
            f"  err {abs(gam[j]-ref):.1e}")

d = np.diff(gam)
dens = np.log(gam[:-1] / (2 * math.pi)) / (2 * math.pi)   # von Mangoldt
s = d * dens                                              # espaciados normalizados
r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
r_mean, r_err = r.mean(), r.std() / math.sqrt(len(r))
R_GUE, R_POI = 0.5996, 0.3863
say(f"  ceros usados: {len(gam)} (hasta gamma={gam[-1]:.1f}); <s> = {s.mean():.4f}")
say()
say("  --- EL DATO QUE PARECE DARLE LA RAZON ---")
say(f"  estadistico r (razon de espaciados consecutivos), TODA la muestra:")
say(f"     medido  {r_mean:.4f} +/- {r_err:.4f}")
say(f"     GUE     {R_GUE:.4f}   <-- a {abs(r_mean-R_GUE)/r_err:.1f} sigmas")
say(f"     1/phi   {INV_PHI:.4f}   <-- a {abs(r_mean-INV_PHI)/r_err:.1f} sigmas (!)")
say(f"     Poisson {R_POI:.4f}")
say("  A esta altura el valor medido esta MAS CERCA de 1/phi que de GUE.")
say("  Si uno se detiene aca, 'aparece el aureo en los ceros'.  No hay que")
say("  detenerse: el estadistico r depende de la altura.")
say()

# deriva con la altura: las correcciones aritmeticas son O(1/log(gamma/2pi))
gm = gam[:-2]
B = 12
bins = np.array_split(np.arange(len(r)), B)
xb = np.array([1.0 / np.log(gm[i].mean() / TWOPI) for i in bins])
yb = np.array([r[i].mean() for i in bins])
eb = np.array([r[i].std() / math.sqrt(len(i)) for i in bins])
coef, cov = np.polyfit(xb, yb, 1, w=1.0 / eb, cov=True)
inter, inter_err = coef[1], math.sqrt(cov[1, 1])
say("  <r> por franja de altura (x = 1/log(gamma/2pi)):")
for i, x, y, e in zip(bins, xb, yb, eb):
    say(f"     gamma ~ {gm[i].mean():8.0f}   1/L={x:.4f}   <r>={y:.4f} +/- {e:.4f}")
say(f"  ajuste lineal, extrapolado a altura infinita (1/L -> 0):")
say(f"     <r>_inf = {inter:.4f} +/- {inter_err:.4f}")
say(f"     GUE     = {R_GUE:.4f}  -> compatible a {abs(inter-R_GUE)/inter_err:.1f} sigmas")
say(f"     1/phi   = {INV_PHI:.4f}  -> EXCLUIDO a {abs(inter-INV_PHI)/inter_err:.1f} sigmas")
coef2, cov2 = np.polyfit(xb, yb, 2, w=1.0 / eb, cov=True)
i2, i2e = coef2[2], math.sqrt(cov2[2, 2])
chi1 = float(np.sum(((yb - np.polyval(coef, xb)) / eb) ** 2)) / (len(xb) - 2)
chi2 = float(np.sum(((yb - np.polyval(coef2, xb)) / eb) ** 2)) / (len(xb) - 3)
say(f"  control con termino cuadratico en 1/L (por si hay curvatura):")
say(f"     <r>_inf = {i2:.4f} +/- {i2e:.4f}     chi2/dof: lineal {chi1:.2f}, cuadratico {chi2:.2f}")
say("  El exceso sobre GUE se va como 1/log(altura): es la correccion")
say("  aritmetica de altura finita (Bogomolny-Keating), no una constante.")
say("  phi no es un limite; es un valor de paso.")
say()

# ---- primos ----
def criba(n):
    sieve = np.ones(n // 2, dtype=bool)
    for i in range(3, int(n ** .5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = False
    p = 2 * np.nonzero(sieve)[0][1::] + 1
    return np.r_[2, p]

P = criba(2_000_000).astype(np.float64)
say(f"  primos usados: {len(P)} hasta {int(P[-1])}")

def weyl(alpha, P):
    ph = 2 * np.pi * alpha * P
    cs = np.cumsum(np.cos(ph)) ; sn = np.cumsum(np.sin(ph))
    n = np.arange(1, len(P) + 1)
    return np.sqrt(cs ** 2 + sn ** 2) / n

idx = np.unique(np.geomspace(10, len(P), 400).astype(int)) - 1
w_phi = weyl(PHI, P)[idx]
w_sq2 = weyl(math.sqrt(2), P)[idx]
w_hal = weyl(0.5, P)[idx]
say(f"  suma de Weyl |1/N sum e(alpha p)| en N={len(P)}:")
say(f"     alpha=phi    {w_phi[-1]:.5f}")
say(f"     alpha=sqrt2  {w_sq2[-1]:.5f}   <-- phi se comporta igual: generico")
say(f"     alpha=1/2    {w_hal[-1]:.5f}   <-- asi se ve una resonancia real")

fig2, axes = plt.subplots(2, 3, figsize=(16.5, 9.0))

# --- D: espaciados de ceros ---
ax = axes[0, 0]
ax.hist(s, bins=45, density=True, color=C_BLUE, alpha=.30, edgecolor=SURFACE, lw=.6)
xs = np.linspace(0, 3.2, 400)
ax.plot(xs, 32 / math.pi ** 2 * xs ** 2 * np.exp(-4 * xs ** 2 / math.pi),
        color=C_BLUE, label="GUE")
ax.plot(xs, np.exp(-xs), color=INK3, lw=1.4, ls=":", label="Poisson")
for v, lab in ((INV_PHI, "$1/\\varphi$"), (PHI, "$\\varphi$")):
    ax.axvline(v, color=C_ORANGE, ls="--", lw=1.3)
    ax.text(v, 0.93, lab, color=C_ORANGE, fontsize=10, ha="center",
            transform=ax.get_xaxis_transform())
ax.text(1.35, .82, "GUE", color=C_BLUE, fontsize=9)
ax.text(0.35, .55, "Poisson", color=INK3, fontsize=9)
ax.set_xlim(0, 3.2)
ax.set_xlabel("espaciado normalizado entre ceros")
ax.set_ylabel("densidad")
ax.set_title(f"D. {len(gam)} ceros de $\\zeta$: la ley es GUE\nen $\\varphi$ y $1/\\varphi$ no pasa nada",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- D2: la deriva del estadistico r  (el panel decisivo) ---
ax = axes[0, 1]
ax.errorbar(xb, yb, yerr=eb, fmt="o", ms=6, color=C_BLUE, ecolor=C_BLUE,
            elinewidth=1.4, capsize=3, mec=SURFACE, mew=1.2, zorder=4)
xf = np.linspace(0, xb.max() * 1.06, 50)
ax.plot(xf, np.polyval(coef, xf), color=C_BLUE, lw=1.6, ls="-", zorder=3)
ax.axhline(R_GUE, color=C_AQUA, lw=1.6)
ax.axhline(INV_PHI, color=C_ORANGE, lw=1.6, ls="--")
ax.errorbar([0], [inter], yerr=[inter_err], fmt="s", ms=8, color=C_BLUE,
            mec=SURFACE, mew=1.5, ecolor=C_BLUE, capsize=4, zorder=5)
ax.text(0.004, R_GUE - 0.0045, "  GUE  0.5996", color=C_AQUA, fontsize=8.5, va="top")
ax.text(0.004, INV_PHI - 0.0006, "  $1/\\varphi$  0.6180", color=C_ORANGE,
        fontsize=8.5, va="top")
ax.annotate(f"extrapolado a altura\ninfinita: {inter:.4f}$\\pm${inter_err:.4f}",
            xy=(0, inter), xytext=(0.052, 0.5960), color=C_BLUE, fontsize=8.5,
            arrowprops=dict(arrowstyle="->", color=C_BLUE, lw=1.2))
ax.set_xlim(-0.006, xb.max() * 1.06)
ax.set_xlabel("$1/\\log(\\gamma/2\\pi)$   (izquierda = mas alto en la recta critica)")
ax.set_ylabel("$\\langle r\\rangle$")
ax.set_title("D2. DECISIVO: el valor aureo se DERIVA\nsube con la altura y termina en GUE, no en $\\varphi$",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7)

# --- E: sumas de Weyl sobre primos ---
ax = axes[0, 2]
NN = idx + 1
ax.plot(NN, w_hal, color=C_ORANGE)
ax.plot(NN, w_phi, color=C_BLUE)
ax.plot(NN, w_sq2, color=C_AQUA)
ax.plot(NN, 1 / np.sqrt(NN), color=INK3, ls=":", lw=1.4)
ax.set_xscale("log"); ax.set_yscale("log")
ax.text(NN[-1], w_hal[-1] * 1.35, "$\\alpha=1/2$: resonancia real, no decae ",
        color=C_ORANGE, fontsize=8.5, ha="right", va="bottom")
ax.text(9e2, 0.055, "$N^{-1/2}$ = puro ruido", color=INK3, fontsize=8.5)
ax.text(1.1e1, 1.1e-3, "$\\alpha=\\varphi$ (azul) y $\\alpha=\\sqrt{2}$ (verde):\n"
        "se superponen, ambos genericos", color=C_BLUE, fontsize=8.5, va="bottom")
ax.set_xlabel("cantidad de primos $N$")
ax.set_ylabel("$|N^{-1}\\sum_{p\\leq p_N} e(\\alpha p)|$")
ax.set_title("E. $\\varphi$ contra los primos: indistinguible de $\\sqrt{2}$\nasi se veria si $\\varphi$ resonara: la curva naranja",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7, which="both")

# --- F: espiral polar de primos ---
ax = axes[1, 0]
Ps = P[P < 300000]
ax.scatter(Ps * np.cos(Ps), Ps * np.sin(Ps), s=.22, color=C_BLUE,
           alpha=.75, linewidths=0)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title(f"F. {len(Ps)} primos en polar $(p,\\ p\\ \\mathrm{{rad}})$: brazos y rayos\n"
             "los cuenta $6,\\ 44,\\ 710$ — denominadores de $2\\pi$",
             fontsize=9.5, color=INK, loc="left")

# --- G: girasol aureo ---
ax = axes[1, 1]
n = np.arange(1, 3001)
th = n * 2 * math.pi / PHI ** 2
ax.scatter(np.sqrt(n) * np.cos(th), np.sqrt(n) * np.sin(th), s=4.5,
           color=C_ORANGE, alpha=.9, linewidths=0)
ax.set_aspect("equal"); ax.axis("off")
ax.set_title("G. Girasol $(\\sqrt{n},\\ n\\cdot 2\\pi/\\varphi^2)$: mismo mecanismo\n"
             "los cuenta $13,\\ 21,\\ 34$ — denominadores de $\\varphi$",
             fontsize=9.5, color=INK, loc="left")


# --- H: por que las espirales de F son de 2pi y no de phi ---
def convergentes(alpha, n=10):
    a, x, res = [], alpha, []
    h1, h2, k1, k2 = 1, 0, 0, 1
    for _ in range(n):
        ai = math.floor(x)
        a.append(ai)
        h1, h2 = ai * h1 + h2, h1
        k1, k2 = ai * k1 + k2, k1
        res.append((h1, k1))
        f = x - ai
        if f < 1e-13:
            break
        x = 1.0 / f
    return res


ax = axes[1, 2]
for alpha, col in ((TWOPI, C_BLUE), (PHI, C_ORANGE)):
    cv = convergentes(alpha, 9)
    q = np.array([k for _, k in cv], dtype=float)
    q2err = np.array([k * k * abs(alpha - h / k) for h, k in cv])
    ax.plot(q, q2err, "o-", color=col, ms=5, mec=SURFACE, mew=1.2)
    for (h, k), y in zip(cv, q2err):
        if (alpha == TWOPI and k in (1, 7, 113)) or (alpha == PHI and k in (3, 21)):
            ax.annotate(f"{h}/{k}", (k, y), textcoords="offset points",
                        xytext=(3, 5), color=col, fontsize=7.5)
ax.axhline(1 / math.sqrt(5), color=INK3, ls=":", lw=1.4)
ax.set_ylim(4e-3, 4.0)
ax.text(1.6e2, 3.4, "$1/\\sqrt{5}$: el piso de Hurwitz.\n$\\varphi$ vive pegado a el:\n"
        "es el peor aproximable que existe", color=INK3, fontsize=8, va="top")
ax.text(1.6e0, 1.4e-2, "$2\\pi$ baja a $0.007$ en $710/113$:\n"
        "una resonancia 60 veces mas\nfuerte que cualquiera de $\\varphi$",
        color=C_BLUE, fontsize=8.5)
ax.text(1.15, 0.90, "$\\varphi$", color=C_ORANGE, fontsize=10)
ax.text(1.15, 0.115, "$2\\pi$", color=C_BLUE, fontsize=10)
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlabel("denominador $q$ del convergente")
ax.set_ylabel("$q^2\\,|\\alpha-p/q|$   (bajo = resonancia fuerte)")
ax.set_title("H. La causa de los dos dibujos, medida\n"
             "$\\varphi$ = resonancias minimas; $2\\pi$ = resonancias fuertes",
             fontsize=9.5, color=INK, loc="left")
ax.grid(True, alpha=.7, which="both")

fig2.suptitle("Buscando $\\varphi$ en los datos reales:  el unico rastro (D2) se disuelve "
              "con la altura;  los brazos de los primos los cuenta $2\\pi$, no $\\varphi$",
              fontsize=11.5, color=INK, x=0.008, ha="left", y=0.995)
fig2.tight_layout(rect=[0, 0, 1, 0.945])
p2 = os.path.join(HERE, "115_08_fig2_phi_en_primos_y_ceros.png")
fig2.savefig(p2, dpi=170)
say(f"[fig] {p2}")

with open(os.path.join(HERE, "115_08_resultados.txt"), "w") as f:
    f.write("\n".join(out) + "\n")
