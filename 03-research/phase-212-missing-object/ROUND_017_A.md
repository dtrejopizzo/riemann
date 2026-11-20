# Ronda 17, memo A: el muro de log 2, el muro del reparto DIR y el reparto de los átomos

Notación de `ROUND_006_WINDOW_SPLIT_NUMERIC.md` §§2, 7–10 y `ROUND_015_D.md`: `q₂, q₃` piezas DIR sobre `P_T`,
`a = q₂ + q₃`, `L_u(F) = ∫_{J_u} F(t)F(t+u) dt` (`J_u = [−T, T−u]`), `Π_p = Σ_k v_{p^k} L_{k log p}`.
Cómputos de §§3–4: script temporal `r17_lattice.py` en el directorio de trabajo temporal (reutiliza, sin
modificarlo, el montaje de `verify_window_split_canonical.py`; Clarabel, estado `optimal_inaccurate`, suelo de
precisión `≈ 10⁻⁹`); no forma parte del corpus.

## 0. Filtro de cuatro puntos

1. **Antecedentes leídos en primaria.** Fase 153 `README.md`, `R153_000_BLUEPRINT.md` §§1–2, `R153_001_ROUND1.md`
   §1.2, `R153_005_CLOSING_DECISION.md`; Paper 47 `main.tex` thm:A (l. 444), cor:mono, `subsec:schur` (prop:schur,
   thm:w11), thm:index (l. 2518), thm:log5A (l. 4680); Paper 42 `main.tex` thm:certifiedendpoints (l. 4164);
   `G2_B8_R5.md` (fase 159) resumen y Teorema D; en la fase 212: `ROUND_006` §§4–10, `ROUND_007_A` §§1–4,
   `ROUND_013_A`, `ROUND_015_B` §4, `ROUND_015_D`, `RULES_AVOID.md` O, Q, Y, Z.
2. **Lo nuevo.** (a) Corrección de la premisa (1) del encargo: el corpus no tiene ninguna prueba de mecanismo más
   allá de `T*`; el «Teorema A» es una identidad de conjugación o una reescritura, y `log 2` es el punto donde se
   corrió un certificado de ordenador (§1, lectura PROVED). (b) El muro DIR no es un evento de cadena y no depende de la
   resolución: `T_DIR ∈ (0.696, 0.698)` en dos mallas, con y sin `n = 4` (§2, NUMÉRICO). (c) La clase «reparto
   posicional de los átomos» (pieza de un primo con soporte arbitrario en su retículo `ℤ log p`) alcanza el techo
   en `0.70–0.75` con fracciones de átomo no negativas. Basta un solo retardo, `log 2` o `log 3`, y no hace falta
   `2 log 2` (§3, NUMÉRICO). (d) Lectura: esa clase disuelve la etiqueta de primo y su versión bilateral es
   trivialmente exacta (§3, PROVED). No es una ley estructural.
3. **Por qué no repite.** (a)–(c) no figuran en el corpus. El grep de «átomo/atom» junto a «pieza/split/reparto» en las
   fases 159, 211 y 212 da sólo usos léxicos. `ROUND_006` §4.5 nombra la medida de salto con átomos, pero no
   la reparte. El reparto con signo del núcleo suave (`ROUND_006` §7.3(iii), O3) es otra libertad. Pero (c) no
   aporta mecanismo de signo. Es una ampliación de clase que confirma el patrón J3/O3 (la clase certifica cuando el
   fondo es `≥ 0`), y así se registra.
4. **Enlace con la positividad global.** Ninguno. Ver §5.

## 1. El «Teorema A» y el muro de log 2 (pregunta 1)

**Lectura (PROVED como lectura de las fuentes).** Hay dos teoremas con ese nombre y ninguno es un mecanismo de signo:

- **Fase 153, Teorema A** (`R153_001` §1.2): `A_T^{(a)} = E_{−a}A_TE_a + E_aA_TE_{−a}`, es decir
  `⟨A_T^{(a)}F,F⟩ = 2[⟨A_Tu,u⟩ − ⟨A_Tw,w⟩]` con `u = cosh(at)F` y `w = sinh(at)F`. Es una polarización de dos
  líneas sobre la forma del falsificador `Ξ_a`, y la propia auditoría (`R153_002` fila 3) la llama así. No
  descompone `a_T` ni da su signo. El signo en `log 2` que usa la fase 153 es el de **Paper 42
  thm:certifiedendpoints**: un certificado en aritmética de intervalos (Arb, malla de dimensión 760, Feshbach dirigido,
  márgenes `6.5·10⁻⁴` par y `1.2·10⁻⁴` impar en `½log 3`). Su blueprint (`R153_000` l. 6, 19) lo dice: «archimedean
  domination (Yoshida Lemma 2 quantified)».
- **Paper 47 thm:A** («the form as a Lévy energy»): `a_T(F) = C₀‖F‖² + Lev(c_F) − Σ v_n c_F(log n)`. Es la fórmula de
  la forma, no una desigualdad. La positividad hasta `½log 5` es thm:log5A, también por certificado (ball
  arithmetic, prop:lowercert). En `log 2`, thm:w11 da sólo el valor de una dirección (la mitad fácil de prop:schur).

**Consecuencias.**
- No hay «decomposición de `a_T` con desigualdad que da el signo» que leer. Los valores exactos de `v₂, v₃` y de
  `C₀ = −γ − 3log 2 − π/2 − log π` entran sólo como entradas numéricas encerradas. `log 2` no es el punto donde
  falla un paso: es una de las ventanas donde se corrió el certificado de Paper 42. Elegirlo es natural, porque
  allí el conjunto de contactos sigue siendo `{2, 3}` y `log 4 = 2T` todavía no entra.
- El único hecho estructural en `log 2` es arquimediano: `n_odd(Arch|P_T) = 0` para `T ≤ log 2` (thm:index(i), con
  `log 2 ≤ T*_odd`). Es una cota inferior de un umbral **certificado en esa ventana**, no un evento en `log 2`.
- **El Teorema A no pertenece a la clase DIR**, porque no es un reparto. **`T_DIR ≥ log 2` no está probado** por nada
  del corpus: es NUMÉRICO (`ROUND_006` §7.3 y §2 abajo). El hecho (1) del encargo es falso tal como está enunciado.
  Los dos muros no son «dos muros de mecanismo a 0.005»: uno es una ventana de certificado y el otro un umbral numérico
  de una clase.

## 2. El primer cuadrado cruzado y la hipótesis de cadena (pregunta 2)

**Condición exacta en `T_DIR` (ARGUED en el continuo, PROVED en Galerkin por dualidad SDP con Slater; reúne
`ROUND_007_A` §3.1 y `ROUND_015_D` §2).** Sea `τ*(T)` el valor DIR y `λ(T)/2` el techo. Entonces `T_DIR = inf{T :
τ*(T) < λ(T)/2}`, y por el dual de `ROUND_007_A` §3.1 se tiene `τ*(T) = λ(T)/2` mientras el ínfimo del funcional dual

`Φ(Y₂,Y₃) = ∫Wρ + ¼∬K[ρ(t)+ρ(s) − 2min(Y₂,Y₃)] − tr(Y₂Π₂) − tr(Y₃Π₃)`

se alcance en el par diagonal `Y₂ = Y₃ = ½ e⊗e` (`e` el fondo de `a|P_T`). `T_DIR` es el primer `T` en que existe un
par con `Y₂ ≠ Y₃`, igual densidad, `tr Y₂ + tr Y₃ = 1` y `Φ < λ/2`. Con holgura complementaria, en ese `T` aparece un
dual no diagonal con `Y₂q₂ = 0` y `Y₃q₃ = 0`, y `θ₂ = 𝟙{Y₃ > Y₂}`. Por el Lema R, en el lado primal esto equivale a
`ν₋(q₂) + ν₋(q₃) = 1` en el reparto óptimo, es decir a que `μ(T) → 0⁺` en el haz `a w = μ q₃ w` (con
`q₃ ⪰ 0`, `μ < 0` cuando `q₂` tiene un autovalor negativo). Observación de primer orden (PROVED, cuenta directa): una
perturbación `Y₂,₃ = ½e⊗e ± Z` con `diag Z = 0` y ambos `⪰ 0` obliga, a primer orden, a `Z = e⊗h + h⊗e`
con `e h ≡ 0`, es decir `Z = 0` donde `e ≠ 0`. Por eso el nacimiento del par no diagonal es de **segundo orden**, y eso
cuadra con el arranque cuadrático `τ* ≈ −(6.7(T − 0.696))²` medido en `ROUND_015_D` §1. No obtengo una forma cerrada
de la condición.

**Hipótesis de cadena (prueba NUMÉRICA en contra).** La cadena `t, t + log 2, t + 2log 2` cabe en `I_T` si y sólo si
`2T ≥ 2log 2`, o sea exactamente en `T = log 2`, el mismo evento en que entra el contacto 4. Datos (`N, NC`; techo entre
paréntesis):

| `T` | `(30,20)` | `(40,30)` | `(30,20)` sin `n = 4` |
|---|---|---|---|
| 0.694 | techo (`5.73·10⁻⁸`) | techo (`5.41·10⁻⁸`) | techo |
| 0.696 | techo (`5.00·10⁻⁸`) | techo (`4.59·10⁻⁸`) | techo |
| 0.698 | — | `−1.45·10⁻⁴` | — |
| 0.700 | `−6.91·10⁻⁴` | `−7.84·10⁻⁴` (`ROUND_006` §8.4) | `−6.9·10⁻⁴` (`ROUND_006` §7.3) |

- El muro está en `(0.696, 0.698)` en las dos mallas. No baja hacia `log 2` al refinar. El retraso `0.003–0.005` es
  estable y no es un artefacto de discretización (NUMÉRICO, dos resoluciones).
- La cadena doble ya cabe en `0.694` y `0.696`, con o sin `n = 4`, y el reparto alcanza el techo. Por tanto
  «la ventana contiene `t, t + log 2, t + 2log 2`» no es la causa. A lo sumo es una condición necesaria con un margen
  que nada predice.
- Lo que refutó `ROUND_007_A` Teor. 2.1: la clase 𝒢. Son los certificados que **acotan cada contacto por un potencial
  `V_p ≥ 0`** (Schur/estado fundamental, con cadenas de cualquier longitud y cualquier `θ_p`, `W_p`), y mueren en
  `T*_{∞,P} ≤ 0.60` por el índice arquimediano. Ese teorema no dice nada sobre la causa del muro DIR. La lectura
  «periodicidad `log 2` a lo largo de cadenas» de `ROUND_007_A` §4 ya notaba que la zona central mide `2(T − log 2)`
  (`0.013` en `0.70`), y la dejaba como ARGUED sin explicación del umbral. Los datos de arriba y §3 la debilitan más:
  el remedio no necesita el retardo `2log 2` y funciona también con un retardo de 3 solo.

## 3. Pieza con soporte arbitrario en su retículo (pregunta 3)

**Clase.** A DIR se añade una transferencia atómica posicional `X = Σ_{u∈𝒰} Σ_i g_{u,i} L_u^{(i)}`, donde
`L_u^{(i)}(F) = ∫_{celda i ∩ J_u} F(t)F(t+u)dt`. Se toma `q₂ + X` y `q₃ − X`. Para `u = log 2`, la pieza 2 conserva
el átomo `−(v₂ − g(t))` y la pieza 3 recibe `−g(t)`. Las fracciones de átomo son no negativas si
`0 ≤ g ≤ v₂ = 0.980`. Para `u = log 3`, la condición es `−v₃ ≤ g ≤ 0` con `v₃ = 1.268`. Esto es exactamente
«la pieza de cada primo es cualquier forma con soporte en su retículo `{0, ±log p, ±2log p}`»: como en `Arch` no hay
átomos, todo lo que una pieza añade en esos retardos lo resta la otra.

**Resultados (NUMÉRICO, `N = 30`, `NC = 20`, máximo `τ`).**

| `T` | DIR | `log 2` solo, `g ∈ [0, v₂]` | `log 2, 2log 2`, `|g| ≤ 50` | `log 3` solo, `g ∈ [−v₃, 0]` | techo |
|---|---|---|---|---|---|
| 0.70 | `−6.9·10⁻⁴` | `3.683·10⁻⁸` | `3.683·10⁻⁸` | `3.683·10⁻⁸` | `3.683·10⁻⁸` |
| 0.72 | `−2.6·10⁻²` | `6.460·10⁻⁹` | `6.460·10⁻⁹` | `6.460·10⁻⁹` | `6.459·10⁻⁹` |
| 0.75 | `−8.6·10⁻²` | `5.18·10⁻¹⁰` | `5.15·10⁻¹⁰` | `5.18·10⁻¹⁰` | `5.18·10⁻¹⁰` |
| 0.80 | `−1.3·10⁻¹` | `−1.6·10⁻⁹` | `4.7·10⁻¹⁰` | `1.0·10⁻⁹` | `4.6·10⁻¹²` |

En `0.80` el techo está por debajo del suelo del solver: «compatible con el techo», sin decidir. En `T = 0.69`,
DIR y la clase ampliada coinciden en el techo.

**Forma de los `g` (NUMÉRICO).**
- `log 2` solo: `g ≈ 0.57–0.73` en `0.70`, `0.74–0.83` en `0.72`, `0.78–0.91` en `0.75`, `0.78–0.93` en `0.80`.
  La pieza 3 se queda con el **60–95 %** del átomo de 2.
- `log 3` solo: `g ≈ −0.94` a `−1.20`. La pieza 2 se queda con el **75–95 %** del átomo de 3.

Las cotas no se tocan. Con `|g| ≤ 50` y los dos retardos de 2 aparecen `|g| = 18` en `0.70`: no hay unicidad.

**Lectura.**
- *(PROVED, trivial.)* Si se permiten los dos retículos con fracciones `≥ 0`, el reparto `q₂ = q₃ = a/2`
  (`θ = ½`, `W₂ = W/2`, `g_{log 2} = v₂/2`, `g_{log 4} = v₄/2`, `g_{log 3} = −v₃/2`) es admisible y alcanza el techo
  `λ/2` para todo `T`. La clase bilateral es la forma misma (J3).
- *(NUMÉRICO.)* La versión unilateral (un solo retículo) no es trivial, pero alcanza el techo en todo el rango
  medible. Lo hace vaciando la etiqueta: la «pieza del primo 3» termina llevando la mayor parte del contacto de 2
  (o al revés).
- La extensión que pide el encargo **no** es una cadena de longitud 2 de 2. Un solo retardo basta, y el de `log 3`
  basta tanto como el de `log 2`. La falla de DIR viene de exigir que **cada átomo quede entero en una sola pieza**.
  En cuanto un átomo puede repartirse con un peso posicional, el reparto vuelve al techo. La transferencia de rango uno
  `λℓ⊗ℓ` de `ROUND_015_D` se sustituye por una transferencia concentrada en el retardo de un contacto.

**¿Cerrada en el corpus?** La clase M (`ROUND_006` §10.1), el Teorema D de la fase 159 y Q1 reparten el núcleo
suave o acotan contactos por potenciales. Ninguno reparte el átomo con peso posicional, y tampoco «per-prime
positivity» de la fase 6 S2.1 (una pieza por primo, átomo entero). Lo nuevo es sólo la medición. Por el punto
anterior, la clase cae en el patrón J3/O3: certifica cuando el fondo es `≥ 0` y no aporta regla. **No hay ley
estructural** del tipo «exacta mientras…». Lo único estructural es la frontera de DIR, «átomo indivisible», y su muro
`T_DIR ≈ 0.697` no tiene evento aritmético asociado (§2).

## 4. Hasta `½log 5`

En `(0.75, 0.8047)` el techo (`≤ 5·10⁻¹⁰`) cae al nivel del solver. «Exacta hasta `½log 5`» no es decidible con
esta herramienta: es OPEN y, por §3, no tiene interés como ley. No se corrió con tres primos.

## 5. Filtro aplicado a lo que sobrevive, y Lema T

- Sobrevive sólo: (a) la corrección de la premisa (lectura); (b) el muro DIR, estable en `(0.696, 0.698)` y no
  causado por cadenas ni por `n = 4` (NUMÉRICO); (c) el reparto posicional de átomos, exacto en lo medible
  (NUMÉRICO) y trivial en su versión bilateral (PROVED).
- **Enlace global, honesto.** Un reparto exacto para todo `T` sería una identidad «`a_T` = suma de piezas `⪰ 0`».
  Pero cada pieza `⪰ 0` es una afirmación del mismo tipo que la original, sin fórmula propia (J3). Ninguna de las
  clases medidas da `θ_p`, `W_p` ni `g` sin resolver el problema.
- **Lema T.** Para un reparto, el paso que debería fallar en los controles es la **existencia** del reparto. Con
  `cΛ` (`c = 2`), con el borrado de una potencia de primo o con Beurling, el reparto deja de existir sólo porque la
  forma deja de ser `⪰ 0`. `ROUND_006` §7.2 y §10.3 muestran que la clase sigue al fondo de `a_T` y no a `c = 1`.
  Esto es exactamente la ruptura automática R3-i. No es un paso nombrado que use una relación aritmética falsa en los
  controles. **No es un paso legítimo para el Lema T.**

## 6. Etiquetas

| # | Afirmación | Etiqueta |
|---|---|---|
| 1 | Fase 153 Teor. A = conjugación para `Ξ_a`; P47 thm:A = fórmula de Lévy; `log 2` = ventana de certificado (P42) | PROVED (lectura) |
| 2 | Ninguna prueba de mecanismo más allá de `T*` en el corpus; `T_DIR ≥ log 2` no probado | PROVED (lectura) / NUMÉRICO |
| 3 | Caracterización dual de `T_DIR` (salida del par diagonal) | PROVED en Galerkin, ARGUED en el continuo |
| 4 | El par no diagonal nace a segundo orden (`diag Z = 0` mata el primer orden) | PROVED (cuenta) |
| 5 | `T_DIR ∈ (0.696, 0.698)` en dos mallas, también sin `n = 4`; no es evento de cadena | NUMÉRICO |
| 6 | Reparto posicional de un átomo (`log 2` o `log 3`, fracciones `≥ 0`) alcanza el techo en `0.70–0.75` | NUMÉRICO |
| 7 | Versión bilateral trivialmente exacta (`a/2`) | PROVED |
| 8 | Ley estructural «exacta hasta `½log 5`» | OPEN, sin interés por 7 |
| 9 | Existencia del reparto como paso de Lema T | NO-GO de selección (R3-i automático) |

**Re-derivar:** 4 (diagonal `Y₂ = Y₃ = ½e⊗e` con `diag Z = 0`) y 7. **Siguiente operación explícita:** ninguna
desde los repartos. El único hecho rígido es que el átomo indivisible deja de bastar en `≈ 0.697` y no en
`log 2`. Una candidata real tendría que dar el `g(t)` de §3 (unilateral, `log 3`) por una fórmula propia que se
rompa en `c = 2`, y no la tengo.
