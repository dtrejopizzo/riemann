# Ronda 15 — D. Umbral del reparto DIR, vector de transferencia y cuenta de cuadrados faltantes

Objeto: el reparto por primo de dos posiciones (clase DIR) de `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §§7–10,
con primos 2 y 3 (el término de `n = 4` va en la pieza de 2). Notación: `q₂, q₃` piezas sobre `P_T`
(discretizadas, `N = 30` modos, `NC = 20` celdas salvo indicación), `a = q₂ + q₃`.

## 0. Filtro de cuatro puntos

1. **Antecedente más cercano, leído en primaria.** `phase-159-row-d-two-front-construction/G2_B8_R5.md` §2,
   Teorema D (dualidad de Sion para el reparto de núcleo por distancia `θ_p(u)`; dual = familia de estados con
   el máximo puntual de los déficits; umbral `T_loc ≤ 0.5925`). En la fase 212: `ROUND_006` §§7.3, 9, 10.2
   (umbral DIR en `(0.695, 0.70)`, par obstructor, transferencia de rango uno) y `RULES_AVOID.md` O1–O4, P1, Q2.
   Fase 156 `R156_001_CONVERSE.md` Prop. 2.1 (capacidad polar `2×2`): es otra cosa (frontera `e^{±t/2}` de
   `P_T`, no transferencia entre primos); no se reutiliza.
2. **Afirmaciones nuevas.** (a) Lema de rango mínimo exacto de la transferencia (§2, PROVED, álgebra lineal).
   (b) Descarte de la causa «entra el contacto 4» y de la ley «cuadrados faltantes = contactos en la ventana»
   (§§1, 4, NUMÉRICO). (c) Caracterización del vector `ℓ` por un haz generalizado (§3, construcción PROVED,
   identificación con el óptimo NUMÉRICO).
3. **Por qué no repite.** La caracterización dual del umbral (§1) **sí es repetición**: es el Teorema D de la
   fase 159 con `θ` dependiente de la posición y potenciales libres; lo digo y no lo cuento como avance. (a) y (b)
   no figuran en el corpus (grep «rango mínimo», «transferencia», «cuadrados faltantes» en 03-research y el índice:
   sólo `ROUND_006` §10.2, que mide pero no tiene lema ni contraste de la ley).
4. **Conexión con la positividad global.** Ninguna directa. Todo lo de esta nota es ciego a `Λ` (el lema de §2
   vale para cualquier par de formas con suma `≻ 0`; con `cΛ`, `c = 2`, la suma deja de ser `≻ 0` y el lema no
   aplica, que es la ruptura automática de R3-i, no una ruptura del signo). Es diagnóstico de la clase DIR, no un
   mecanismo de signo. No pasa la puerta como construcción; se entrega como tarea de identificación asignada.

## 1. El umbral (tarea 1)

**Caracterización (repetición del Teorema D, PROVED en la discretización por dualidad cónica con Slater; ARGUED en
el continuo por el mismo argumento de Sion).** `T_DIR = sup{T : Ψ_T ≥ 0}`, con

`Ψ_T = inf { −tr(σ₂Π₂) − tr(σ₃Π₃) + ∫W ρ + ¼∬ K(|t−s|) max(E_{σ₂}, E_{σ₃})(t,s) }`,

ínfimo sobre pares de estados `σ₂, σ₃ ⪰ 0` en `P_T`, `tr σ₂ + tr σ₃ = 1`, **con igual densidad puntual**
`ρ_{σ₂} = ρ_{σ₃} = ρ` (la libertad de `W_p(t)` fuerza la igualdad), `E_σ(t,s)` la energía de par y `Π_p` la
parte de contactos del primo `p` (`Π₂` incluye `v₄ c_F(log 4)`). El máximo puntual es la holgura complementaria:
`θ₂ = 1` donde `E_{σ₂} > E_{σ₃}`. Esto es la ecuación exacta pedida («`Ψ_T = 0`»); no tiene forma cerrada en `T`
y no la obtengo.

**El umbral no es la entrada del contacto 4 (NUMÉRICO, datos existentes y nuevos).**
- Control ya registrado (`ROUND_006` §7.3 (ii)): borrando el término de `n = 4`, en `T = 0.70` la forma sigue
  positiva y el reparto sigue fallando (`−6.9·10⁻⁴` frente a `−6.9·10⁻⁴` con el término). La pieza de 2 no
  falla por tener que absorber `−v₄ c_F(log 4)`.
- Nuevo: `T = 0.697` tiene transferencia nula (norma nuclear `6.6·10⁻¹⁴`, el reparto existe).
- Inicio: norma nuclear `0.0214, 0.121, 0.239` en `0.70, 0.71, 0.72`, aproximadamente lineal, se anula por
  extrapolación en `≈ 0.698`; el déficit primal `−6.9·10⁻⁴, −8.1·10⁻³, −2.6·10⁻²` se ajusta a
  `−(6.7(T − 0.696))²` (arranque cuadrático). Luego `T_DIR ∈ (0.697, 0.699)`, retraso `≈ 0.004–0.006` sobre
  `log 2`, sin evento geométrico asociado (`2T_DIR ≈ 1.396`, no es `log` de un racional simple con contactos
  ≤ 4; no lo identifico). Lectura honesta: coincidencia cercana, no causa. Resolución única en `0.697`.

## 2. Lema de rango mínimo (PROVED)

**Lema R.** Sean `q₂, q₃` simétricas reales con `a = q₂ + q₃ ≻ 0`. Entonces

`min { rango X : q₂ + X ⪰ 0, q₃ − X ⪰ 0 } = ν₋(q₂) + ν₋(q₃)`,

y el mínimo se alcanza con `X = X₊ − X₋`, `X₊ ⪰ 0` de rango `ν₋(q₂)`, `X₋ ⪰ 0` de rango `ν₋(q₃)`.

*Prueba.* Sea `B = a^{−1/2} q₂ a^{−1/2}`; entonces `a^{−1/2} q₃ a^{−1/2} = I − B` y, por Sylvester,
`ν₋(B) = ν₋(q₂)`, `ν₋(I − B) = ν₋(q₃)`. Con `Y = a^{−1/2} X a^{−1/2}` (mismo rango) las condiciones son
`0 ⪯ B + Y ⪯ I`. *Cota inferior:* `B + Y₊ ⪰ B + Y ⪰ 0`, y sumar una forma `⪰ 0` de rango `r` baja el número de
autovalores negativos a lo sumo en `r` (entrelazamiento de Weyl); luego `rango Y₊ ≥ ν₋(B)`; igual,
`I − B + Y₋ ⪰ 0` da `rango Y₋ ≥ ν₋(I − B)`; y `rango Y = rango Y₊ + rango Y₋`. *Alcance:* en la base propia de
`B` (autovalores `β_i`) tomar `y_i = −β_i` si `β_i < 0`, `y_i = 1 − β_i` si `β_i > 1`, `0` si no. ∎

**Corolario (rango uno, PROVED).** Si `q₃ ≻ 0` y `q₂` tiene un único autovalor negativo, una transferencia
`X = λ ℓℓᵀ` existe si y sólo si `ℓᵀ(q₂⁻¹ + q₃⁻¹)ℓ ≤ 0` (con `q₂` invertible), y `q₂⁻¹ + q₃⁻¹ = q₂⁻¹ a q₃⁻¹`
tiene exactamente un autovalor negativo. *Prueba.* Por Schur, `q₂ + λℓℓᵀ ⪰ 0 ⇔ λ ≥ −1/(ℓᵀq₂⁻¹ℓ)` con
`ℓᵀq₂⁻¹ℓ < 0`, y `q₃ − λℓℓᵀ ⪰ 0 ⇔ λ ≤ 1/(ℓᵀq₃⁻¹ℓ)`; compatibles si y sólo si la suma es `≤ 0`. Inercia:
`q₃^{1/2}(q₂⁻¹ + q₃⁻¹)q₃^{1/2} = (C − I)⁻¹ + I`, `C = q₃^{−1/2} a q₃^{−1/2} ≻ 0`; el único autovalor
`c − 1 ∈ (−1, 0)` da `1/(c − 1) + 1 < 0`. ∎

**Consecuencia.** «Número de cuadrados faltantes» tiene definición exacta:
`n_miss(T) = min_{(θ,W) ∈ DIR} [ν₋(q₂) + ν₋(q₃)]`. La norma nuclear de `ROUND_006` §10.2 da sólo cotas
superiores de `n_miss`; `n_miss ≥ 1` para `T > T_DIR` por definición del umbral.

## 3. El vector `ℓ` (tarea 2)

- **Construcción (PROVED, del Lema R):** con `q₃ ≻ 0`, `ν₋(q₂) = 1`, la dirección `ℓ = q₃w ∝ a w`, `w` el
  vector generalizado más bajo del haz `a w = μ q₃ w` (`μ < 1`), da una transferencia admisible.
- **Identificación (NUMÉRICO,** con las piezas óptimas guardadas, desplazadas `+2·10⁻⁶` por el piso del solver):
  solapamiento de `ℓ` (óptimo nuclear) con `a w`: `0.9979, 0.99994, 0.99998` en `T = 0.70, 0.71, 0.72`; con el
  vector negativo de `q₂⁻¹ + q₃⁻¹`: igual a cuatro cifras; con el autovector negativo de `q₂`: `0.925–0.935`.
  `μ = 4.9·10⁻⁴, 8.9·10⁻⁵, 4.7·10⁻⁵`. Las dos caracterizaciones no son algebraicamente idénticas; coinciden por
  el mal condicionamiento de `q₃` (piso de autovalores).
- **Formas cerradas:** proyección de `cos(2πt/log 2)`: `0.911, 0.919, 0.922`; añadir `cos(4πt/log 2)` o
  `cos(2πt/log 3)` no mejora (`≤ 0.927`); `cos(2πt/log(3/2))` sube a `0.95–0.96`, y cuatro cosenos a `0.98–0.99`
  (ganancia esperable de grados de libertad). **No hay fórmula cerrada**; la caracterización exacta disponible es
  la del haz `(a, q₃)`, que depende del reparto óptimo, no de un dato aritmético. OPEN.

## 4. Significado y la ley de conteo (tarea 3)

**Enunciado exacto (PROVED en la discretización, dado el reparto numérico):** para `T ∈ [0.70, 0.72]`,
`a_T = (q₂ + λℓ⊗ℓ) + (q₃ − λℓ⊗ℓ)`, ambos `⪰ 0`; el término cruzado es un único cuadrado `λ⟨ℓ,F⟩²` que pasa
de la pieza de 3 a la de 2. No encuentro expresión aritmética de `ℓ` vía `log 3 − log 2 = log(3/2)` o `2 log 2 − log 3 = log 4 − log 3 = log(4/3)`:
la única señal es el `0.95` con `cos(2πt/log(3/2))`, insuficiente.

**Conteo (NUMÉRICO, `N = 30`, `NC = 20`; desde `0.73` estado `optimal_inaccurate`):**

| `T` | autovalores de `X` (módulo) | rango (cota sup. de `n_miss`) |
|---|---|---|
| 0.697 | `< 10⁻¹³` | 0 |
| 0.70–0.72 | uno positivo | 1 |
| 0.73 | `0.327, 0.027` | 2 |
| 0.74 | `0.387, 0.061` | 2 |
| 0.75 | `0.449, 0.084` | 2 |
| 0.77 | `+0.448, +0.140, −0.093, −0.003` | ≤ 4 (aparece parte negativa: la pieza de 3 también pide) |
| 0.80 | `+0.567, +0.228, −0.069, −0.048` | ≤ 4 |

El segundo cuadrado nace en `≈ 0.722` (extrapolación lineal del segundo autovalor). Entre `0.70` y `0.80` el
conjunto de contactos es fijo (`2, 3, 4`; el 5 entra en `½ log 5 = 0.8047`, y ahí el código pasa a tres primos y
los modos `transfer`/`dual` no corren; `½ log 6` tampoco es alcanzable, y el fondo de `a_T` está ya en `10⁻¹²`).
**La ley «cuadrados faltantes = contactos (o casi coincidencias) en la ventana» queda refutada en esta clase**:
la cuenta crece 0 → 1 → 2 → (≤4) sin que entre ningún contacto. `T ≈ 0.722 ≈ ½ log(3√2)` es numerología sin
mecanismo; no la propongo. Control: sin el término de `n = 4` en `0.72` el programa es infactible (la forma ya es
negativa, `−1.55·10⁻³`), coherente con `ROUND_006` §7.3.

## 5. Etiquetas y lo que un revisor debe rehacer

- PROVED: Lema R y su corolario (§2); construcción de `ℓ` por el haz (§3).
- Repetición declarada: caracterización dual del umbral = Teorema D de `G2_B8_R5.md` con `θ(t,s)`, `W_p(t)`.
- NUMÉRICO: `T_DIR ∈ (0.697, 0.699)`; no causado por el contacto 4; `n_miss = 1` en `[0.70, 0.72]`; segundo
  cuadrado en `≈ 0.722`; refutación de la ley de conteo; ausencia de forma cerrada para `ℓ`.
- Re-derivar: la cota inferior del Lema R (entrelazamiento) y la inercia del corolario.
- Siguiente operación concreta: calcular `n_miss(T)` como invariante (minimizar `ν₋(q₂)+ν₋(q₃)` sobre DIR, no la
  norma nuclear) y comprobar si es monótono en `T`; si lo es, `T ↦ n_miss(T)` es la escalera que una clase con
  acoplamiento entre primos debe pagar con exactamente esa cantidad de cuadrados cruzados. Ninguna conexión con el
  signo global está establecida.

Scripts: `r15_ell.py` y registros `r15_tr_*.log` en el directorio temporal; no forman parte del corpus.
