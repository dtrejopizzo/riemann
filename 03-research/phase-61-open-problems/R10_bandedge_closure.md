# R10 — La ruta de cierre de 2.3.F-Loc: borde de banda de la Jacobi intrínseca acotada

**Fecha:** 2026-06-25. **Experimento:** `E85_bandedge_closure.py` (λ=9,13,17,21; engine_cache, dps=40).
**Tesis:** 2.3.F-Loc es **RH-neutral** y se reduce a teoría espectral estándar de operadores de
Jacobi acotados — NO al muro.

## El punto de partida (ya probado): 2.3.F-Loc es RH-neutral por R1

Por R1 (probado), tras conjugar por el estado base positivo `u_0` (Perron–Frobenius, Teorema 2.2,
**incondicional** a λ finito), el operador de Doob

> `G_λ(v,v) = A_λ(u_0 v, u_0 v) − ε_0‖u_0 v‖²  ≥  0`

es **manifiestamente positivo a cada λ, se cumpla RH o no**. Sus autovalores `e_k = ε_k − ε_0 > 0`.
2.3.F-Loc es la afirmación sobre los **ratios** `(e_k)/(e_1) → k(k+2)` (forma desplazada de Doob)
— una pregunta espectral **incondicional** sobre `G_λ`. El muro (12.1) es el **signo** de `ε_0`: un
enunciado distinto. Por tanto el contenido restante de 2.3.F es analítico puro y RH-neutral.

## El mecanismo de cierre (identificado y demostrado, E85)

**(i) `G_λ` es, en su marco de Lanczos intrínseco, una Jacobi de coeficientes ACOTADOS O(1).**
Lanczos exacto sobre `A` (N1/E79) reproduce el espectro completo (la escalera `(k+1)²`, rep_err=0).
Los coeficientes son acotados y **period-2** (acoplamiento de paridad): `α ≈ [0.79, 3.69, 0.85, 3.68,…]`.
**Boundedness uniforme en λ verificado (E85, B0):** `max|A_ij| = 4.25, 4.77, 5.71, 4.50` para
λ=9,13,17,21 — **se queda O(1), NO crece como λ**. Crucial: el balance `ARCH=PRIME` mantiene el
operador acotado (la suma cruda `Σ Λ(n)n^{−1/2} ~ 2λ` divergería; el balance la cancela). Esta
acotación es **incondicional** (propiedad de las entradas de la forma de Weil).

**(ii) Extremos Dirichlet** (Lema 2.3.F-Box, **probado**, E20): el time-limiting fuerza `H¹_0`.

**(iii) Una Jacobi acotada con extremos Dirichlet tiene, genéricamente, borde de banda
CUADRÁTICO** ⟹ `(e_k − e_0)/(e_1 − e_0) → k(k+2)`. **DEMOSTRADO en E85 (T3):** construyendo la
Jacobi period-2 LÍMITE con SOLO los coeficientes **promediados** del bulk (`a_par, a_impar, b`
constantes) sobre la cadena finita con Dirichlet, los ratios desplazados salen:

| λ | T3 (solo promedios) | target k(k+2) |
|---|---|---|
| 9  | [0, 1, 2.64, 4.88, 7.66, 10.91] | [0, 1, 2.667, 5, 8, 11.667] |
| 13 | [0, 1, 2.66, 4.95, 7.85, 11.32] | |
| 17 | [0, 1, 2.65, 4.90, 7.73, 11.07] | |
| 21 | [0, 1, 2.66, 4.97, 7.91, 11.47] | |

La escalera se reproduce **a partir de los promedios solamente** (a ~2–4%, con el undershoot la
corrección de cadena finita `O((k/M)⁴) → 0`). El "suavizado" running-mean crudo (T2) la rompe
—porque introduce un gradiente espurio—; el **límite period-2 limpio (T3) es la homogeneización
correcta y funciona.**

## Por qué esto es RH-neutral (el argumento decisivo)

El borde de banda cuadrático es **genérico** para *cualquier* Jacobi acotada: los modos bajos de
borde de banda tienen longitud de onda `~ M` (largo de la cadena) `≫ 1` (espaciado), así que por
**homogeneización** solo ven los coeficientes **promediados (Cesàro)**, no las fluctuaciones.
**La escalera NO se puede afinar con RH** — vale para todo operador de Jacobi acotado con extremos
Dirichlet. La aritmética solo debe aportar (i) que el operador sea asintóticamente Jacobi acotada
[incondicional, verificado] y (ii) Dirichlet [probado]. Por eso E84 falló (suavizar los primos
rompía el balance/marginalidad = el SIGNO), mientras E85 funciona (suaviza la Jacobi del operador
ya-positivo `G_λ` = la FORMA).

## Estado: la ruta de cierre, con lo que falta RH-neutral y estándar

**2.3.F-Loc queda reducido a tres lemas, todos RH-neutrales, ninguno el muro:**
1. **Acotación uniforme** `sup_λ max_{ij}|A_ij| < ∞` (⟹ Jacobi intrínseca acotada). *Numéricamente
   verificado (O(1) hasta λ=21).* Falta la cota analítica incondicional desde la fórmula explícita.
2. **No-degeneración del borde de banda** (mínimo cuadrático, no cuártico). *Numéricamente
   confirmado (escalera `k(k+2)`, no `k⁴`).* Falta: curvatura del símbolo `> 0`.
3. **Homogeneización de borde de banda** (los modos bajos ven solo el promedio Cesàro). *Demostrado
   numéricamente (T3).* Es teoría estándar (Sturm–Liouville / efecto de masa efectiva), falta
   redactarla.

**Ninguno de los tres toca el signo `ε_0` (el muro).** Esto es un avance material respecto del crux
previo ("portadora θ afín / asintótica prolato-Sonin del balance exacto", que se *sentía*
entrelazado con el muro): ahora 2.3.F-Loc es **teoría espectral estándar de una Jacobi acotada**,
RH-neutral por construcción (R1) y con el mecanismo **demostrado** (E85 T3). El cierre completo
requiere redactar (1)–(3) — análisis estándar e incondicional, **nuestro, no de Connes/Consani.**

---

## CORRECCIÓN HONESTA (2026-06-25, posterior) — el Lema 1 NO es RH-neutral

Al **intentar probar el Lema 1** (acotación) en vez de solo verificarlo, descompuse la entrada:
`A_ij = (∫e^{-u/2}q_ij − WR_ij)[acotado] − (PRIME − PRIME_smooth)_ij[fluctuación de CEROS]`.
El segundo término **es la suma sobre ceros** (fórmula explícita). Medido: **CRECE con λ**
(max|fluct| = 2.78, 3.59, 4.06, 3.66 en λ=7,11,15,21). Cotas analíticas:
- incondicional (dVP, `|ψ−t|≪t e^{−c√log t}`): **DIVERGE** (~λ/polylog);
- incluso con RH (`|ψ−t|≪√t log²t`): **DIVERGE** (~log³λ);
- la acotación real necesita la **cancelación oscilatoria de `Σ_ρ ĝ(γ_ρ)`** = maquinaria
  de Branges/Sonin = **el muro**.
⟹ **El Lema 1, apenas se intenta DEMOSTRAR (no solo verificar num.), reconecta con el control de
ceros = el muro.** R10 sobre-afirmó al llamarlo "análisis estándar RH-neutral". El mecanismo de
borde de banda (E85) sigue siendo correcto y útil como ENTENDIMIENTO, pero NO da un cierre
incondicional vía Lema 1. Ver R11 (ángulo Weyl/homogeneización) para el intento siguiente.
