# 115.10 — Por qué todos los rayos tienen la misma forma

Observación sobre `115_09_fig_primos_polar.png`: cada rayo nace en el origen,
se estira, y sobre el final se dobla un poco — y **todos se doblan igual**.

Es correcto, y es exacto.  Script: `115_10_por_que_se_curvan_los_rayos.py`,
salida en `115_10_resultados.txt`, figura `115_10_fig_rayos.png`.

## El número que gobierna el dibujo

```
113 · 2π = 709.999939706…
710      = 710
δ        = 710 − 113·2π = +6.0289 × 10⁻⁵ rad
```

Avanzar p en 710 unidades gira el punto exactamente δ radianes.  **δ no
depende del rayo.**  Por eso los 280 rayos no son parecidos: son el mismo
arco, rotado.

Cada rayo es un arco de **espiral de Arquímedes**

> r = 710 (θ − θ_a) / δ

con paso 710/δ = 1.18 × 10⁷ — enorme, por eso a simple vista parece recto.

## Verificación, sin ajustar nada

Predicción: para todo primo p, con a = p mod 710,

> Δθ(p) = δ · (p − a) / 710

Medido sobre los 100 000 primos del dibujo:

* desvío máximo: **3.9 × 10⁻¹¹ rad**
* ancho de un rayo: 2π/710 = 8.85 × 10⁻³ rad — 2.3 × 10⁸ veces mayor

No se parecen: coinciden a precisión de máquina (panel B).

## Cuánto se doblan

Al borde del dibujo (p = 1 299 709):

* giro acumulado = **0.110363 rad = 6.323°**
* eso son **12.47 anchos de rayo**, y en el mismo sentido para los 280

Eso es exactamente el "todos tienen la misma onda y al final se doblan".

## Por qué el dibujo cambia según el radio

Cada convergente de 2π genera su propia familia de rayos, y cada familia se
desarma cuando la deriva acumulada llega a un ancho de rayo, en r = 2π/|δ|:

| familia | δ (rad/paso) | se desarma en r ≈ |
|---|---|---|
| 6/1 | −2.83 × 10⁻¹ | 22 |
| 19/3 | +1.50 × 10⁻¹ | 42 |
| 25/4 | −1.33 × 10⁻¹ | 47 |
| 44/7 | +1.77 × 10⁻² | 355 |
| 333/53 | −8.82 × 10⁻³ | 712 |
| **710/113** | **+6.03 × 10⁻⁵** | **104 218** |

El dibujo llega a r = 1 299 709.  De ahí la estructura anidada: cerca del
centro mandan las familias 6 y 44, que se desarman enseguida; afuera manda la
de 710; y pasando r ≈ 10⁵ la de 710 también empieza a doblarse
visiblemente — que es justo donde el ojo ve que "se caen".

## Lo único que el dibujo dice de los primos

Todo lo anterior es sobre 2π, no sobre primos: con **todos los enteros** el
dibujo tendría los mismos 710 rayos, sólo que más densos.

Los primos hacen exactamente una cosa: 710 = 2·5·71, y un primo no puede
compartir factor con 710 salvo siendo 2, 5 o 71.  Entonces de las 710 clases
sólo se ocupan **φ(710) = 280** (más los tres primos excepcionales, 283
medidas).  Las 430 restantes quedan vacías.

Y que las 280 brillen parejo — 100 000/280 = 357 primos por rayo, medido — es
**el teorema de Dirichlet** sobre primos en progresiones aritméticas.

Ésa es toda la aritmética del dibujo: **qué rayos faltan, y que los que quedan
pesan igual.**  La forma de cada rayo es geometría de 2π.

## Clasificación

* Congruencia de los 280 rayos: **PROBADA Y VERIFICADA**, desvío 3.9 × 10⁻¹¹ rad.
* Curvatura = arco de espiral de Arquímedes de paso 710/δ: **DERIVADA**, sin
  parámetros libres.
* Estructura anidada por radio: **EXPLICADA** por los radios de coherencia
  2π/|δ| de cada convergente.
* Contenido aritmético: **280 de 710 clases + equidistribución de Dirichlet**.
  Nada más.
* Relación con φ: **NINGUNA** — ver `115_08`.
