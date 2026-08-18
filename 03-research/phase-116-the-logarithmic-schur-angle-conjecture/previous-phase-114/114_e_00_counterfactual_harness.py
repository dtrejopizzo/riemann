#!/usr/bin/env python3
"""E.00 — Arnes contrafactual reusable.

Instrumenta el principio P3 del paper 41 (`41/main.tex:1259-1262`):

    "si un argumento propuesto sigue siendo valido verbatim en un sistema con un
     cero fuera de linea, ya esta refutado."

Base: 113_14 Thm 3.3 da un generador de testigos en forma cerrada -- todo cero fuera
de linea produce, por una formula de una linea, un dato de Schwartz real con
s(f,f) = 4m|a_1|^2 > 0.  Este archivo lo extrae a una interfaz reusable.

USO
---
    from importlib import import_module
    H = import_module("114_e_00_counterfactual_harness")

    def mi_lema(w):
        "devuelve True si el lema afirma positividad en el mundo w"
        ...
        return alguna_condicion

    H.audit(mi_lema, "prop:shiftchaincoercivity")

VEREDICTOS
----------
  BLIND            el predicado nunca consulto los datos espectrales del mundo.
                   No puede ser portante para row (d): vale igual con RH y sin RH.
  NON-DISCRIMINATING  los consulto, pero da el mismo valor en ambos mundos.
  DISCRIMINATING   da valores distintos.  Toca el mecanismo decisivo.

Un veredicto BLIND o NON-DISCRIMINATING no dice que el lema sea falso ni inutil --
dice que por si solo no puede cerrar row (d), y conviene saberlo el dia que se enuncia.

Solo requiere mpmath.  No certifica nada: es un falsificador.
"""
import mpmath as mp

mp.mp.dps = 30

__all__ = ["World", "on_line_world", "off_line_world", "audit", "witness", "s_form"]


# --------------------------------------------------------------------------- mundos
class World:
    """Un modelo espectral.  Registra cada acceso a los datos de ceros.

    zeros: lista de (rho, multiplicidad).  El mundo es cerrado bajo la orbita
    rho -> conj rho -> 1-conj rho -> 1-rho, como exige la ecuacion funcional.
    """

    def __init__(self, zeros, name, rh_holds):
        self._zeros = list(zeros)
        self.name = name
        self.rh_holds = rh_holds
        self.accesses = 0

    @property
    def zeros(self):
        self.accesses += 1
        return self._zeros

    def reset(self):
        self.accesses = 0

    def mirror(self, rho):
        """rho' = 1 - conj rho.  Bajo RH coincide con rho."""
        return 1 - mp.conj(rho)

    def s_form(self, fhat):
        """s(f,f) = - sum_rho m_rho f^(rho) conj(f^(rho'))   sobre D^o.

        fhat: callable s -> C.  Signo: A_T representa -B_nuc, luego
        <A_T F, F> = + sum_rho m_rho f^(rho) conj(f^(rho')).
        Aca devolvemos s(f,f) = -esa suma, la convencion de 113_12.
        """
        tot = mp.mpf(0)
        for (rho, m) in self.zeros:
            tot += m * fhat(rho) * mp.conj(fhat(self.mirror(rho)))
        return -tot

    def __repr__(self):
        return f"<World {self.name!r} RH={self.rh_holds} nz={len(self._zeros)}>"


# primeras alturas de ceros de zeta (Odlyzko); suficientes para un modelo finito
GAMMAS = [mp.mpf(g) for g in [
    "14.134725141734693", "21.022039638771555", "25.010857580145688",
    "30.424876125859513", "32.935061587739189", "37.586178158825671",
    "40.918719012147495", "43.327073280914999",
]]


def on_line_world(n=6, name="on-line (RH cierta)"):
    """Ceros en la linea critica, en pares conjugados."""
    zs = []
    for g in GAMMAS[:n]:
        zs.append((mp.mpc(mp.mpf("0.5"), g), 1))
        zs.append((mp.mpc(mp.mpf("0.5"), -g), 1))
    return World(zs, name, rh_holds=True)


def off_line_world(n=6, sigma="0.8", name="off-line (RH falsa)"):
    """Igual, pero el PRIMER cero se corre fuera de la linea, generando el
    cuadruple {sigma+it, sigma-it, 1-sigma+it, 1-sigma-it} de 113_14 C2."""
    w = on_line_world(n, name)
    g0 = GAMMAS[0]
    s0 = mp.mpf(sigma)
    w._zeros = w._zeros[2:]                       # quitar el par on-line
    for rho in [mp.mpc(s0, g0), mp.mpc(s0, -g0),
                mp.mpc(1 - s0, g0), mp.mpc(1 - s0, -g0)]:
        w._zeros.append((rho, 1))
    w.rh_holds = False
    return w


# --------------------------------------------------------------------- testigo 113_14
def witness(rho0, m=1, Gauss=True):
    """113_14 Thm 3.3 caso 1: el testigo real en D^o con s(f,f) = 4m|a_1|^2 > 0.

    Devuelve (fhat, quadruple, prediccion).  rho0 debe estar fuera de la linea y
    no ser real.  Sobre un Xi surrogate Xi_S = D4 * G con G(s) = exp((s-1/2)^2).
    """
    q1 = mp.mpc(rho0)
    QUAD = [q1, mp.conj(q1), 1 - mp.conj(q1), 1 - q1]
    G = lambda s: mp.e ** ((mp.mpc(s) - mp.mpf("0.5")) ** 2)
    gg = lambda s: mp.mpc(s) * (mp.mpc(s) - 1) * G(s)     # = s(s-1) Xi_S / D4

    A1 = gg(q1)
    u0 = q1 - mp.mpf("0.5")
    if abs(mp.im(u0 ** 2)) < mp.mpf("1e-25"):
        raise ValueError("rho0 esta en la linea critica: Im(u_0^2)=0, no hay rotacion")
    z = mp.mpc(0, 1) / A1
    c2 = mp.im(z) / mp.im(u0 ** 2)
    c0 = mp.re(z) - c2 * mp.re(u0 ** 2)
    P = lambda s: c0 + c2 * (mp.mpc(s) - mp.mpf("0.5")) ** 2
    fhat = lambda s: P(s) * gg(s)
    return fhat, QUAD, 4 * m


def s_form(fhat, quad, m=1):
    """s(f,f) sobre el cuadruple, con el emparejamiento espejo rho <-> rho'."""
    MIR = [2, 3, 0, 1]
    a = [fhat(q) for q in quad]
    return -m * sum(a[j] * mp.conj(a[MIR[j]]) for j in range(4))


# --------------------------------------------------------------------------- auditoria
def audit(predicate, label, worlds=None, verbose=True):
    """Evalua `predicate(world) -> bool` en un mundo con RH y otro sin RH.

    Devuelve (veredicto, valor_on, valor_off, accesos_on, accesos_off).
    """
    if worlds is None:
        worlds = (on_line_world(), off_line_world())
    w_on, w_off = worlds
    w_on.reset(); w_off.reset()
    v_on = bool(predicate(w_on))
    v_off = bool(predicate(w_off))
    a_on, a_off = w_on.accesses, w_off.accesses

    if a_on == 0 and a_off == 0:
        verdict = "BLIND"
        note = "nunca consulto los ceros; no puede ser portante para row (d)"
    elif v_on == v_off:
        verdict = "NON-DISCRIMINATING"
        note = f"consulto los ceros ({a_on} accesos) pero da {v_on} en ambos mundos"
    else:
        verdict = "DISCRIMINATING"
        note = f"RH-mundo: {v_on}   no-RH-mundo: {v_off}  -- toca el mecanismo"

    if verbose:
        print(f"  [{verdict:<19}] {label}")
        print(f"      {note}")
    return verdict, v_on, v_off, a_on, a_off


# ------------------------------------------------------------------------------ self-test
if __name__ == "__main__":
    print("E.00 — arnes contrafactual: self-test\n")

    # 1. el testigo de 113_14 se reproduce
    print("1. Testigo cerrado de 113_14 Thm 3.3")
    fhat, QUAD, pred = witness(mp.mpc("0.8", 6))
    val = s_form(fhat, QUAD)
    assert abs(mp.im(val)) < mp.mpf("1e-18"), "s(f,f) deberia ser real"
    assert mp.re(val) > 0 and abs(mp.re(val) - pred) < mp.mpf("1e-15"), \
        f"s(f,f)={mp.re(val)} != {pred}"
    assert abs(fhat(0)) < mp.mpf("1e-25") and abs(fhat(1)) < mp.mpf("1e-25"), \
        "el testigo debe estar en D^o"
    print(f"   ok  s(f,f) = {mp.nstr(mp.re(val), 15)}  (predicho 4m = {pred}) > 0")
    print(f"   ok  f^(0) = f^(1) = 0, el testigo esta en D^o")

    # sobre la linea critica el generador debe NEGARSE a producir testigo
    try:
        witness(mp.mpc("0.5", 14))
        raise AssertionError("deberia haber fallado sobre la linea critica")
    except ValueError:
        print("   ok  sobre Re s = 1/2 no hay testigo (Im(u_0^2)=0) — eso ES RH")

    # 2. auditoria de los tres lemas de row (d)
    print("\n2. Auditoria de los enunciados actuales de row (d)")

    def shift_chain_coercivity(w):
        """prop:shiftchaincoercivity — R_T >= alpha_N I.
        Depende solo de Lambda(n) y de la geometria de cadenas."""
        import numpy as np
        from sympy import factorint
        N, T2 = 200, mp.log(200)
        alpha = 0.0
        for n in range(2, N):
            f = factorint(n)
            if len(f) != 1:
                continue
            w_n = float(mp.log(next(iter(f)))) / float(mp.sqrt(n))
            m = int(mp.ceil(T2 / mp.log(n)))
            alpha += w_n * (1 - float(mp.cos(mp.pi / (m + 1))))
        return alpha > 0

    def uniform_witt_moments(w):
        """prop:uniformWittmoments — sumabilidad de todas las profundidades.
        Tambien puramente aritmetico."""
        return True

    def weil_positivity(w):
        """La afirmacion de row (d) misma: s(f,f) <= 0 en D^o.
        Se testea con el testigo del propio mundo."""
        offline = [r for (r, _) in w.zeros if abs(mp.re(r) - mp.mpf("0.5")) > mp.mpf("1e-9")
                   and abs(mp.im(r)) > mp.mpf("1e-9")]
        if not offline:
            return True                      # sin cero fuera de linea, no hay testigo
        fh, quad, _ = witness(offline[0])
        return mp.re(s_form(fh, quad)) <= 0

    audit(shift_chain_coercivity, "prop:shiftchaincoercivity  (R_T >= alpha_N I)")
    audit(uniform_witt_moments, "prop:uniformWittmoments")
    audit(weil_positivity, "row (d) mismo:  s(f,f) <= 0 en D^o")

    print("\nLECTURA")
    print("  Los dos primeros salen BLIND: son enunciados sobre Lambda(n) y la")
    print("  geometria de canales, sin ningun cero. Coincide con la propia")
    print("  evaluacion del paper (row-d-local-analysis.tex:464-474): controlan la")
    print("  referencia pero no prueban la dominacion aguda.")
    print("  El tercero sale DISCRIMINATING, como debe: es row (d).")
    print("\n  El arnes esta calibrado. Usarlo sobre cada lema de D2 el dia que se enuncia.")
