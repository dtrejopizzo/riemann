# 115.08 — El número áureo en σ: auditoría, y qué sí dice el dato

`115_04` produce la constante universal σ = e^{-(log 2)²}.  Su valor,
0.6185031378…, se parece a 1/φ = 0.6180339887….  Esta nota audita esa
semejanza con mediciones, no con impresiones.  Script:
`115_08_golden_ratio_audit.py`; salida completa en `115_08_resultados.txt`.
Los dos dibujos de los paneles F y G, sueltos y en grande, en `115_09_*`; la
anatomía de los rayos, en `115_10_*`.

**Corrección de paso.**  `115_04` escribía σ = 0.618505…; el valor correcto
es **0.618503**137801575983…  Corregido en el texto.

## Resultado

σ ≠ 1/φ, y la diferencia no es de precisión sino estructural.

| | valor |
|---|---|
| σ = e^{-(log 2)²} | 0.618503137801576 |
| 1/φ | 0.618033988749895 |
| separación relativa | 7.59 × 10⁻⁴ (0.076 %) |

σ = 1/φ equivaldría a (log 2)² = log φ, es decir 0.480453014 = 0.481211825.
Son números distintos: coinciden en 3 cifras significativas y difieren en la 4ª.

## Las tres mediciones (`fig1`)

**A — de dónde sale el 2.**  El 2 de (log 2)² no es una constante universal:
viene de que `cor:cotangentRRdimension` cuenta **dígitos binarios**,
r(m) ≈ log m / log 2.  Con un código en base b la construcción da
σ_b = e^{-(log b)²}.  El valor áureo se alcanza en b\* = e^{√(log φ)} =
**2.0010946**, no en b = 2.  La "aparición" del áureo es exactamente el hecho
numérico log 2 ≈ √(log φ), y nada más.

**B — calibración de la casi-coincidencia.**  A 7.6 × 10⁻⁴ de σ ya caen 3
constantes de un catálogo de 2 201 combinaciones simples de π, e, φ, √2, ln 2,
γ, ζ(3), y 5 de un catálogo de 4 115 cuadráticos (p+q√d)/s de altura ≤ 12.
Más aún: **e^{-γ/ζ(3)} = 0.618665854 está 3 veces más cerca de σ que 1/φ**.
A esta precisión el áureo no es un vecino distinguido; es uno entre ocho, y
gana sólo porque es el que uno ya conocía.

**C — el test que decide.**  El teorema de `115_04` es
h⁰_t − h²_t = N_t·log(1/σ), y su contenido es que eso sea (log 2)²N_t = t²ab
**sin factor espurio**.  Con σ = 1/φ el cociente log φ/(log 2)² = 1.001579…,
o sea un factor espurio del 0.158 % en cada t; como N_t ~ t²ab/(log 2)², el
error absoluto crece como t² y diverge.  El covolumen no deja elegir: σ está
forzado por `eq:finiteRRmetric`, y lo que fuerza no es φ.

## ¿Y en los primos o en los ceros? (`fig2`)

**D2 es el panel importante, y por un rato parece darle la razón a la
hipótesis áurea.**  Sobre **100 118 ceros** de ζ hasta altura γ = 75 000,
calculados por Riemann–Siegel con corrección C₀, por segmentos donde
N = ⌊√(t/2π)⌋ es constante (controles: 100 118 encontrados contra
N(T) = 100 117.7 teórico; error 1 × 10⁻⁴ contra `mpmath` en γ₁₀₀ y γ₁₀₀₀).
El estadístico r — razón de espaciados consecutivos, independiente del
desplegado — da

* medido, toda la muestra: **0.6109 ± 0.0007**
* GUE asintótico: 0.5996 → a 15.8 σ
* 1/φ: 0.6180 → a 9.9 σ

Con la muestra chica (22 491 ceros hasta γ = 20 000) el mismo cálculo daba
0.6133 ± 0.0015, a 3.2 σ de 1/φ y 9.2 σ de GUE: ahí el áureo parecía ganar.
Con 100 000 ceros esa ventaja desaparece — el valor global no es ninguna de
las dos constantes, porque **depende de la altura**.

Partiendo la muestra en 12 franjas y graficando ⟨r⟩ contra 1/log(γ/2π) — la
escala natural de las correcciones aritméticas de altura finita
(Bogomolny–Keating) — el valor **baja monótonamente** y el ajuste lineal
extrapola a altura infinita en

> ⟨r⟩_∞ = **0.5965 ± 0.0026** → GUE a 1.2 σ, **1/φ excluido a 8.2 σ**.

Control con término cuadrático en 1/L, por si hubiera curvatura:
⟨r⟩_∞ = 0.5992 ± 0.0273, χ²/dof 0.15 (lineal) contra 0.16 (cuadrático) — el
ajuste lineal alcanza y el resultado no se mueve.

El exceso sobre GUE se va como 1/log(altura).  φ no es un límite: es un valor
de paso que la muestra cruza alrededor de γ ~ 10³.

**E — φ contra los primos.**  Suma de Weyl |N⁻¹ Σ_{p≤p_N} e(αp)| sobre 148 933
primos: α = φ da 0.00118, α = √2 da 0.00143, ambos siguiendo N^{-1/2} (ruido
puro).  Una resonancia real se ve así: α = 1/2 da 0.99999.  φ es genérico
frente a los primos.

**F, G, H — los dibujos.**  Los primos en polar (p, p rad) **sí** forman brazos
y rayos, y el girasol (√n, n·2π/φ²) **también** (13, 21, 34).  Es el mismo
mecanismo — fracciones continuas — con dos números distintos: los brazos de
los primos los cuentan los denominadores de 2π (6, 44, 710), los del girasol
los de φ (Fibonacci).  El panel H mide la causa: q²|α − p/q| baja a 0.007 en
710/113 para 2π, mientras que φ está pegado al piso de Hurwitz 1/√5 = 0.447
por ser el peor aproximable que existe.  Los primos hablan de 2π; φ aparece
donde uno lo pone.

## Clasificación

* σ ≈ 1/φ: **CASI-COINCIDENCIA**, 0.076 %, con al menos 7 competidores igual
  de cercanos y uno (e^{-γ/ζ(3)}) más cercano.  **No hay identidad.**
* σ = 1/φ como hipótesis: **REFUTADA** — rompe la igualdad exacta de `115_04`
  con un factor espurio del 0.158 %.
* φ en la estadística de espaciados de ceros: **REFUTADA** a 8.2 σ tras
  extrapolar la altura, sobre 100 118 ceros hasta γ = 75 000.  El acuerdo
  aparente a γ ≲ 10⁴ es la corrección aritmética de altura finita, y se
  desarma sola al agrandar la muestra.
* φ en la distribución de primos: **NEGATIVO** — genérico en sumas de Weyl.
* Lo que sí queda: el 2 de (log 2)² es el **2 del código binario**.  Si alguna
  vez hay que entender de dónde viene esa constante, la pregunta correcta es
  por qué la codificación de `perfectCotangentObject` es binaria, no por qué
  σ se parece a 1/φ.
