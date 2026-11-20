# Ronda 6 — Reparto local dependiente de la ventana en T = 0.5925 (NUMÉRICO)

Todo lo que sigue es NUMÉRICO salvo donde se indica. Valida un punto; no prueba nada. Script:
`verify_window_split.py` (argumentos: T, modos N, celdas NC, iteraciones del control, nodos por celda).

## 1. Montaje

T = 0.5925, primos 2 y 3 (únicos contactos: log 4 > 2T). Base s_k(t) = T^{−1/2} sin(kω(t + T)), ω = π/(2T),
k ≤ N, proyectada sobre P_T (dos condiciones de momento). Con ε_F(u) = c_F(0) − c_F(u) = ½‖F − F_u‖²,

    Arch(F) = C_0‖F‖² + ∫_0^∞ ε_F K du = ∫ W(t)F(t)² dt + ¼ ∬_{I_T×I_T} K(|t − s|)(F(t) − F(s))² dt ds,
    W(t) = C_0 + ½[(π − G(T − t)) + (π − G(T + t))],   G(u) = log tanh(u/4) + 2 arctan e^{u/2},

(PROVED, cuenta directa: ¼∬_{ℝ²} = ¼∬_{I×I} + ½∫F²·∫_{s∉I}K), Π_p(F) = v_p c_F(log p), a_T = Arch − Π_2 − Π_3.
La matriz de Arch se construyó de las dos maneras; con 2400 nodos difieren en 2.8·10⁻⁵ por entrada.
Fondo de a_T sobre P_T en el modelo: 1.32·10⁻⁴ (N = 20), 1.26·10⁻⁴ (N = 30), 1.25·10⁻⁴ (N = 40).
Fondo de Arch − Π_2: −0.029.

## 2. Clases de reparto

Se maximiza τ con r_2 − Π_2 ⪰ τ y Arch − r_2 − Π_3 ⪰ τ sobre P_T. Techo: τ ≤ ½ λ_min(a_T|P_T).

- LK (fase 159, G2_B8_R5): r_2 = c_2‖F‖² + ∫_0^{2T} ϑ(u)K ε_F du, 0 ≤ ϑ ≤ 1.
- P: r_2 = ∫W_2(t)F² + ϑ·¼∬K(ΔF)², ϑ constante, W_2 libre.
- M: r_2 = ∫W_2(t)F² + ¼∬ϑ(|t − s|)K(ΔF)², W_2 libre.
- DIR: r_2 = ∫W_2(t)F² + ¼∬θ(t, s)K(|t − s|)(F(t) − F(s))² dt ds, 0 ≤ θ = θ(s, t) ≤ 1, W_2 libre.
  θ y W_2 constantes a trozos sobre NC celdas iguales.

## 3. Resultados

N = 20, NC = 12:

| clase | τ |
|---|---|
| LK | −1.56·10⁻³ |
| P | −3.30·10⁻² |
| M | −1.60·10⁻⁴ |
| DIR | +6.5665·10⁻⁵ (igual al techo) |

DIR según la resolución (techo entre paréntesis):

| N | NC | τ |
|---|---|---|
| 20 | 2 | −8.4·10⁻² |
| 20 | 4 | −2.7·10⁻² |
| 20 | 6 | −3.4·10⁻³ |
| 20 | 8 | −2.3·10⁻³ |
| 20 | 12, 16 | +6.5665·10⁻⁵ (6.5665·10⁻⁵) |
| 30 | 12 | −7.2·10⁻⁵ |
| 30 | 16, 20, 24 | +6.2925·10⁻⁵ (6.2925·10⁻⁵) |
| 40 | 12 | −1.3·10⁻⁴ |
| 40 | 20, 24 | +6.253·10⁻⁵ (6.2530·10⁻⁵) |

LK con las mismas mallas: −1.56·10⁻³ (N = 20), −2.73·10⁻³ (N = 30), −3.03·10⁻³ (N = 40).

## 4. Lectura

1. En la clase DIR el reparto existe y alcanza el techo en cuanto NC ≳ N/2 (una celda por longitud de onda
   del modo más alto), en los tres tamaños probados. Con menos celdas falla.
2. Las clases intermedias fallan: no basta un potencial dependiente de la posición (P), ni repartir el
   núcleo según la distancia (M). Hace falta que la parte del núcleo dependa de las dos posiciones.
3. La solución hallada no toca ninguna cota (0 de 78 parámetros en 0 o 1 con N = 20, NC = 12) y no es
   única. Su forma no tiene significado.
4. Que se alcance exactamente el techo con solución interior indica que, resuelta la malla, la clase DIR
   certifica siempre que a_T ⪰ 0 en el modelo. De ser así en el continuo, «existe un reparto DIR» es una
   reformulación del objetivo en esta ventana y no un objeto con signo (patrón de reformulación). No está
   probado en ninguna dirección.
5. En términos de formas: q_p = r_p − Π_p tiene medida de salto θ_pK + (v_p/2)δ(|t − s| − log p) ≥ 0 y un
   potencial; el reparto es una partición de la medida de salto y del potencial de a_T entre los primos.

## 5. Dualidad (ARGUED; cuenta sin segundo lector)

Repitiendo el argumento de minimax de G2_B8_R5 Teorema D con la clase DIR: como W_2 es libre, el supremo
sobre W_2 es finito sólo si los dos estados tienen la misma densidad puntual ρ_{σ_2}(t) = ρ_{σ_3}(t)
(ρ_σ = Σ w_i|F_i|²), y el supremo sobre θ cobra el máximo puntual en (t, s) de D_p(t, s) = Σ w_i|F_i(t) −
F_i(s)|². La obstrucción a un reparto DIR sería un par de estados de igual densidad con

    ∫Wρ + ¼∬K max(D_2, D_3) − Π_2(σ_2) − Π_3(σ_3) < 0.

El par de prueba de G2_B8_R5 §4 tiene densidades distintas y no es admisible. Para estados puros de igual
densidad en un espacio de polinomios trigonométricos, F_3 = ±F_2 y el valor es a_T(F_2) ≥ 0; una
obstrucción sólo puede venir de mezclas.

## 6. Qué falta para que esto sea algo

- Una fórmula para θ_p(t, s) y W_p(t) que no se obtenga resolviendo el problema (sin ella es circular:
  `RULES_AVOID.md` J3).
- El continuo: N → ∞ con θ medible arbitraria.
- Tres o más primos (T > ½ log 5) y T grande.
- Controles: por construcción la clase no puede distinguir cΛ; certifica exactamente cuando el fondo es ≥ 0.

## 7. Segunda tanda, con cuadratura de alta precisión (NUMÉRICO)

Script: `verify_window_split_canonical.py` (T, N, NC, c, modo ∈ {exist, box, canon}; variables de entorno
BYN = 1: una pieza por potencia de primo; NOPOW = 1: se borran las potencias p^k, k ≥ 2; TH_LO, TH_HI: cotas
de θ en el modo box). Todos los integrandos son analíticos en su dominio (autocorrelación con límites
exactos; celdas diagonales partidas en triángulos; el potencial total se obtiene por resta), de modo que
la cuadratura de Gauss converge espectralmente. Fondo de a_T sobre P_T en T = 0.5925: 1.318997·10⁻⁴
(N = 20), 1.264204·10⁻⁴ (N = 30), 1.256310·10⁻⁴ (N = 40).

### 7.1 El reparto más suave se estabiliza

Entre los repartos DIR con q_2, q_3 ⪰ τ_0 (τ_0 = la cuarta parte del fondo) se minimiza
R = ∬|∂θ|² + ∫(W_2 − W/2)² (discretizado). Diferencia máxima de θ_2 promediada sobre una malla común 6×6
entre resoluciones sucesivas (N, NC): (20,12)→(20,24): 0.075; →(30,18): 0.031; →(30,24): 0.016;
→(40,24): 0.009. R_θ = 1.47, 1.21, 1.64, 1.76, 1.85. Ningún parámetro en cota.

θ_2 sobre la malla 6×6 (N = 40, NC = 24):

    0.57 0.40 0.39 0.45 0.52 0.58
    0.40 0.30 0.47 0.61 0.60 0.52
    0.39 0.47 0.62 0.68 0.61 0.45
    0.45 0.61 0.68 0.62 0.47 0.39
    0.52 0.60 0.61 0.47 0.30 0.40
    0.58 0.52 0.45 0.39 0.40 0.57

Rasgos: (a) la media por distancia |t − s| es plana (0.48–0.51 hasta |t − s| ≈ 0.8, sube a 0.65 en 2T);
(b) la media por centro (t + s)/2 va de 0.68 en los bordes a 0.32 a dos tercios del camino y 0.62 en el
centro; (c) valores singulares de θ_2 − media: 1.90, 1.87, 0.93, 0.23, 0.20, 0.05: rango efectivo tres;
(d) W_2 − W/2 ≈ +0.41 en las dos franjas a dos tercios del camino y ≈ 0 en el resto, estable en las cinco
resoluciones.

### 7.2 La clase no distingue el peso en T = 0.5925

Con cΛ (N = 30, NC = 20): c = 0.80, fondo 1.88·10⁻², τ = techo; c = 0.95, fondo 5.97·10⁻³, τ = techo;
c = 1.01, 1.03, 1.10: fondo negativo, τ = fondo/2.

### 7.3 La clase DIR tiene umbral propio, cerca de T = log 2

N = 30, NC = 20, dos optimizadores (uno convexo):

| T | fondo de a_T | τ (θ ∈ [0, 1]) |
|---|---|---|
| 0.62 | 2.28·10⁻⁵ | techo |
| 0.65 | 2.77·10⁻⁶ | techo |
| 0.67 | 7.35·10⁻⁷ | techo |
| 0.69 | 1.62·10⁻⁷ | techo |
| 0.70 | 7.37·10⁻⁸ | −7.3·10⁻⁴ |
| 0.71 | 3.22·10⁻⁸ | −8.1·10⁻³ |
| 0.72 | 1.29·10⁻⁸ | −2.6·10⁻² |
| 0.75 | 1.04·10⁻⁹ | −8.6·10⁻² |
| 0.80 | 9.2·10⁻¹² | −1.3·10⁻¹ |

Luego la clase DIR con partes no negativas no equivale al objetivo: certifica hasta un umbral
T_DIR ∈ [0.69, 0.70) y deja de hacerlo con la forma todavía positiva. log 2 = 0.6931 es donde entra n = 4
y donde cabe en la ventana una cadena de tres puntos t − log 2, t, t + log 2.

Controles sobre la causa: (i) una pieza por potencia de primo (2, 3, 4) no lo repara (τ = −6.5·10⁻⁴ en
0.70; −5.7·10⁻² en 0.75); (ii) borrando el término de n = 4, en T = 0.70 la forma sigue positiva
(8.9·10⁻⁸) y el reparto sigue fallando (−6.9·10⁻⁴): el término de n = 4 no es la causa; (iii) con partes
del núcleo con signo, θ ∈ [−1, 2], el reparto vuelve a existir cerca del techo (T = 0.70: 3.68·10⁻⁸;
T = 0.75: 3.6·10⁻¹⁰ frente a 5.2·10⁻¹⁰), y con θ ∈ [−0.2, 1.2] existe en 0.70 y falla en 0.75. Lo que
se pierde en T ≈ log 2 es la no negatividad de la parte del núcleo de cada primo.

Control lateral: borrando n = 4, el fondo pasa a −1.55·10⁻³ en T = 0.72 y −5.3·10⁻² en T = 0.75.

### 7.4 Límites

Para T ≳ 0.85 el fondo del modelo (≈ 10⁻¹⁴) está al nivel del redondeo; sólo se distingue «falla por
mucho» de «compatible con cero». No se ha probado nada: ni la existencia del reparto en el continuo para
T < log 2, ni la no existencia para T > log 2, ni la identificación del umbral con log 2.

## 8. Dónde se pierde la no negatividad pasado log 2 (NUMÉRICO)

Modo `sdp` de `verify_window_split_canonical.py` (programa semidefinido; requiere cvxpy y clarabel).
`N = 30`, `NC = 20`, primos 2 y 3.

### 8.1 Tercer optimizador para el umbral

Máximo `τ` con `0 ≤ θ ≤ 1`: `T = 0.69`: `8.0834·10⁻⁸` (techo `8.0833·10⁻⁸`); `T = 0.70`: `−6.91·10⁻⁴`;
`T = 0.72`: `−2.553·10⁻²`; `T = 0.75`: `−8.582·10⁻²`. Coincide con los dos optimizadores de la sección 7.

### 8.2 Préstamo mínimo

Se escribe `θ = u − n₂ + n₃` con `0 ≤ u ≤ 1`, `n₂, n₃ ≥ 0`, y se minimiza la fracción de área
`∬ (n₂ + n₃) / (2T)²` con ambas piezas `≥ −10⁻⁶` (margen relajado: con margen igual a medio techo el
solver no converge).

| `T` | préstamo | parte `θ < 0` | parte `θ > 1` |
|---|---|---|---|
| 0.69 | 0 | 0 | 0 |
| 0.70 | `4.7·10⁻³` | `4.7·10⁻³` | 0 |
| 0.72 | `5.2·10⁻²` | `2.1·10⁻²` | `3.2·10⁻²` |
| 0.75 | `1.24·10⁻¹` | `5.7·10⁻²` | `6.6·10⁻²` |

### 8.3 Localización

El préstamo es ralo: ocupa unas pocas celdas, simétricas bajo `(t,s) → (−s,−t)`.

- `T = 0.70`: una sola celda y su espejo, `t ≈ −0.455`, `s ≈ 0.315`, `|t−s| ≈ 0.77`, `θ ≈ −0.47`.
- `T = 0.72`: `θ < 0` en tres celdas con `|t−s| ≈ 0.79` y `t ∈ [−0.47, −0.32]`; `θ > 1` (hasta `3.85`)
  en el par formado por el borde `t ≈ −T` y `s ≈ 0.32–0.40`, `|t−s| ≈ 1.01–1.08`, y su espejo.
- `T = 0.75`: el mismo dibujo (`θ < 0` a distancia `0.75–0.83`, `θ > 1` desde el borde a distancia
  `1.05–1.13`), más una segunda capa: `θ < 0` desde el borde a distancia `0.60–0.68` y `θ > 1` a
  distancia `0.45`.

Lectura, con la resolución de celda `h ≈ 0.07`: las distancias están entre los contactos y no sobre
ellos de modo nítido (`log 2 = 0.693`, `log(9/4) = 0.811`, `log 3 = 1.099`); la malla no permite
identificarlas. La predicción «partes negativas en los puntos centrales con vecino a distancia `log 2`
a ambos lados» no se confirma en esa forma simple: en el arranque (`T = 0.70`) el préstamo aparece a
distancia `≈ 0.77`, no a `log 2`, y lejos del centro.

Reserva: minimizar una norma `L¹` favorece soluciones ralas por sí mismo; la ralidad es en parte
efecto del criterio. Las posiciones no son únicas por construcción y falta la malla fina
(`N = 40`, `NC = 30` no terminó en el tiempo asignado).

### 8.4 Malla fina (`N = 40`, `NC = 30`, `h ≈ 0.048`)

Máximo `τ` con `0 ≤ θ ≤ 1`: `T = 0.70`: `−7.84·10⁻⁴`; `T = 0.72`: `−2.662·10⁻²`.
Préstamo mínimo: `T = 0.70`: `5.3·10⁻³`; `T = 0.72`: `4.7·10⁻²` (malla gruesa: `4.7·10⁻³`, `5.2·10⁻²`).

Celdas con exceso (mitad `t + s ≤ 0`; el resto por espejo):

- `T = 0.70`: `(−0.677, 0.303)`, distancia `0.980`, exceso `+0.85`; `(−0.443, 0.350)`, distancia `0.793`,
  exceso `−0.34`.
- `T = 0.72`: `(−0.696, 0.312)`, distancia `1.008`, exceso `+4.04`; `(−0.456, 0.312)`, distancia `0.768`,
  exceso `−2.88`; `(−0.408, 0.408)`, distancia `0.816`, exceso `−5.00` (cota impuesta `5`);
  `(−0.696, −0.072)`, distancia `0.624`, exceso `−0.88`.

Lectura:

- Persisten al refinar dos distancias: `≈ 0.77–0.82` con `θ < 0` y `≈ 0.98–1.01` con `θ > 1` desde el
  borde. La segunda excluye `log 3 = 1.099` (la celda cubre `±0.048`). La primera es compatible con
  `log(9/4) = 0.811` sin identificarla.
- El total del préstamo es estable entre mallas; las celdas concretas no, y un valor toca la cota. El
  mínimo de área se concentra al refinar: como criterio está mal planteado para leer una forma límite.
- La localización del préstamo no entrega una regla. El objeto bien definido para `T > log 2` es el
  dual del problema con `0 ≤ θ ≤ 1` (el par de estados obstructores), que es único en lo esencial y no
  depende de un criterio de selección.

## 9. El par obstructor pasado log 2 (NUMÉRICO)

Modo `dual` del script: variables duales `Y₂, Y₃ ⪰ 0` de las dos restricciones del programa «máximo `τ`
con `0 ≤ θ ≤ 1`».

### 9.1 Verificación de la dualidad de la sección 5

En todos los casos `tr Y₂ = tr Y₃ = ½`, las densidades por celda coinciden (`≤ 1.4·10⁻¹⁶`) y

`−tr(Y₂Π₂) + tr(Y₃(Arch − Π₃)) + Σ_celdas max(D, 0) = τ`,  `D = ` energía de par de `Y₂` menos la de `Y₃`,

reproduce el valor primal en todas las cifras (`T = 0.70`: `−6.911123·10⁻⁴`). La dualidad queda
comprobada en la discretización; sigue sin prueba en el continuo.

### 9.2 Forma de los estados

Rango efectivo 4–5 cada uno. `T = 0.70`, `N = 30`: autovalores de `Y₂`: `0.276, 0.185, 0.025, 0.010`;
de `Y₃`: `0.257, 0.170, 0.047, 0.026`. Las dos autofunciones principales (una par con tres lóbulos,
una impar) casi coinciden entre `Y₂` e `Y₃`. Densidad común con máximos en `t ≈ ±0.30` y mínimos en
`0` y `±0.47`. En `T = 0.75`, `Y₂` es casi de rango uno (`0.469`) e `Y₃` de rango dos (`0.311, 0.180`).

### 9.3 Reparto óptimo: todo o nada, por bandas de distancia

`θ₂ = 1` donde `D > 0`, `θ₂ = 0` donde `D < 0`. El signo de `D(t,s)` depende casi sólo de `|t − s|`:

| banda de `|t − s|` | `θ₂` | contacto dentro de la banda |
|---|---|---|
| `≈ 0.15–0.55` | 1 | ninguno |
| `≈ 0.63–0.85` (máximo de `|D|` en `0.70–0.75`) | 0 | `log 2 = 0.693` |
| `≈ 0.93–1.17` (máximo en `1.03–1.10`) | 1 | `log 3 = 1.099` |
| `≳ 1.2` (máximo en `1.3–1.4`) | 0 | `log 4 = 1.386` |

Estable en `T = 0.70, 0.72, 0.75` y en las dos mallas (`h ≈ 0.07` y `h ≈ 0.05`). En las distancias de
transición hay celdas de ambos signos (los bordes de banda se curvan hacia los extremos de la ventana)
y cerca de la diagonal `D ≈ 0`.

Valores del déficit: `T = 0.70`: `−6.91·10⁻⁴` (`N=30`), `−7.84·10⁻⁴` (`N=40`); `T = 0.75`: `−8.58·10⁻²`,
`−8.30·10⁻²`. No convergidos a más de una cifra.

### 9.4 Lectura (sin prueba)

Cada primo cede el núcleo en las distancias de sus propios contactos. Heurística: el núcleo en la
distancia `u` controla `∫(F(t) − F(t+u))²`, que es pequeño exactamente cuando `c_F(u)` es grande; para
acotar `v_p c_F(log p)` ese control no sirve, y sí sirve el de las otras distancias.

No explica por sí solo el umbral en `log 2`. Pasado el umbral, el óptimo se parece a un reparto que
sólo ve la distancia (clase M de la sección 2); la libertad de posición que alcanzaba el techo por
debajo de `log 2` no aparece en el par obstructor.

## 10. Ensayos de reapertura tras `REVIEW_006.md` (NUMÉRICO)

Modos `mclass` y `transfer` del script. `N = 30`, `NC = 20` salvo indicación.

### 10.1 Clase M en `T = 0.5925`

`θ = φ(|t − s|)` con `0 ≤ φ ≤ 1` y `W₂(t)` libre: `τ = −6.04·10⁻⁴` (`N = 30`), `−5.75·10⁻⁴` (`N = 40`,
`NC = 30`); techo `6.3·10⁻⁵`. El valor `−1.6·10⁻⁴` de la sección 3 (`N = 20`) no estaba convergido. La clase M
falla; alcanzar el techo por debajo del umbral exige `θ` de dos posiciones.

### 10.2 Transferencia mínima entre las dos piezas

Se añade una forma `X` cualquiera: `q₂ + X ⪰ −10⁻⁶`, `q₃ − X ⪰ −10⁻⁶`, con `q_p` en la clase DIR, y se
minimiza la norma nuclear de `X`.

| `T` | norma nuclear | autovalores de `X` |
|---|---|---|
| 0.695 | `1·10⁻¹⁴` | — (el reparto existe) |
| 0.70 | `2.14·10⁻²` (`N = 40`: `2.73·10⁻²`) | uno positivo; el resto `≤ 10⁻¹¹` |
| 0.71 | `1.21·10⁻¹` | uno positivo; el resto `≤ 10⁻¹⁰` |
| 0.72 | `2.39·10⁻¹` (`N = 40`: `2.46·10⁻¹`) | uno positivo; el resto `≤ 10⁻⁸` |
| 0.75 | `5.33·10⁻¹` | dos positivos: `0.449`, `0.084` |

- El umbral de la clase DIR está entre `0.695` y `0.70`: por encima de `log 2 = 0.6931`, no en él.
- `X = λ ℓ ⊗ ℓ` con `ℓ` par. En el óptimo `q₃ ⪰ 0` y `q₂` tiene un único autovalor negativo
  (`−1.8·10⁻²` en `0.70`, `−0.20` en `0.72`; dos en `0.75`: `−0.39`, `−0.059`); `ℓ` es esa dirección
  (solapamiento `0.92–0.95`).
- Forma de `ℓ` estable en `T` y en la malla: positiva en el centro, negativa en torno a `±0.4`, grande
  junto a los bordes. Solapamiento con la proyección de `cos(2πt/log 2)` sobre `P_T`: `0.91–0.93`; el
  mejor coseno tiene periodo `0.707–0.736`, creciente con `T`. Solapamiento con el autovector más bajo
  de `a|P_T`: `0.60–0.62`; con el tercero: `0.35–0.42`. Ninguna candidata la identifica.
- Reserva: la norma nuclear favorece rango bajo por sí misma. Con `ℓ` libre el formato es el reparto con
  signo (vacío). No hay fórmula para `ℓ`, y el número de cuadrados crece con `T`.

### 10.3 Dependencia del peso en estas ventanas

Fondo de `a_T` sobre `P_T` con `cΛ` (primos 2, 3 y el término de 4):

| `c` | `T = 0.70` | `T = 0.75` |
|---|---|---|
| 0.98 | `−1.5·10⁻³` | `−2.9·10⁻³` |
| 0.995 | `−1.5·10⁻⁴` | `−6.6·10⁻⁴` |
| 0.999 | `+4.5·10⁻⁵` | `−1.2·10⁻⁴` |
| 1 | `+7.4·10⁻⁸` | `+1.0·10⁻⁹` |
| 1.001 | `−2.6·10⁻⁴` | `−4.7·10⁻⁴` |
| 1.005 | `−1.7·10⁻³` | `−2.5·10⁻³` |
| 1.02 | `−9.7·10⁻³` | `−1.2·10⁻²` |

El fondo de `Arch` solo es `−0.154` (`T = 0.70`). En estas ventanas la forma es positiva sólo en un
intervalo de `c` de anchura `≲ 10⁻³` alrededor de 1. La afirmación «genérico en `c`» de la sección 7.2
vale en `T = 0.5925` (donde `Arch ⪰ 0` sobre `P_T`) y no aquí: todo certificado exacto en `T ≥ 0.70`
distingue `c = 1` con esa precisión. Resolución `N = 30`; sin control de convergencia en `c`.

### 10.4 Precisiones tras el cotejo (`ANNEX_COTEJO_NULLDIR.md`)

- La sección 10.3 no aporta nada nuevo: la ventana bilateral estrecha en `c`, la escalera de autovalores
  diminutos, la concavidad en `c` y la derivada `−Π(F*)` están en la fase 211 (`ROUND_003_A.md`,
  `ROUND_002_D.md`, `ROUND_002_E.md`, `ROUND_021_A.md`) y en el Paper 47. El ancho de la ventana en `c` es
  el margen salvo constantes.
- No hay contacto exacto por ambos lados: `Π(F*) > 0`, luego el máximo en `c` se alcanza en `c* < 1`
  estricto y 1 es interior al intervalo de positividad.
- «`Arch ⪰ 0` sobre `P_T` en `T = 0.5925`» es NUMÉRICO: ese valor cae en el intervalo `[0.58, 0.60]` que el
  umbral probado no decide.
