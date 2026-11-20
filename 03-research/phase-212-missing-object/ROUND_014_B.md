# Ronda 14, memo B: positividad de Schur–Schoenberg sobre el producto de Euler como fuente propia de un bloque no Gram

Resumen. La candidata es un núcleo 𝕂 sobre la ventana, positivo definido por ser producto de Hadamard (Schur)
de factores por primo, o exponencial de un generador condicionalmente negativo (Schoenberg), del que `a_T` se
recuperaría por una operación no lineal (generador en `t = 0`, derivada logarítmica, matriz de Loewner,
complemento de Schur contra el factor arquimediano). El cotejo encuentra la idea en el corpus: `ROUND_013_C`
O10, `INV_F_001` (Teor. F1–F2, Cor. F3, fila C5) y `RULES_AVOID` M3–M4. Además pruebo, en la clase declarada
abajo, que **toda positividad de producto de Schur sobre factores por primo sobrevive a los tres controles**
(Lema 2), y que la variante de Schoenberg «para todo t» es un reparto local por primo (Lema 1). Veredicto:
repetición y NO-GO de selección; M4 se mejora sólo parcialmente (§4).

Lectura en primaria: `RULES_AVOID` M, Q–W; `ROUND_013_B` (Lemas 1–3 y «Operación que reabriría la clase»);
`ROUND_013_C` §§2–3 (tabla O1–O14, Lemas T y K); `ROUND_009_G3` (lista P1–P12); `phase-194-invention/
INV_F_001_DLOG_WALL_CONES.md` §§1–4; índice de rutas, README, entradas «Total positivity / PF» e INV_F_001.
Grep en `03-research` de Schoenberg, Lévy–Khintchine, Loewner, Pólya frequency, «conditionally negative»:
los aciertos pertinentes son INV_F_001, la fila O10 de ROUND_013_C y los memos 104_21/AUDIT_A citados en el
índice (positividad total falla en PF₂ / PF₅). Los demás aciertos (fases 78, 163, 186, 206) usan las palabras
de paso; lectura por encabezado, ARGUED.

## 0. Filtro de cuatro puntos

1. **Antecedente más cercano.** `INV_F_001` §2 fila C5 y Teor. F2: «toda premisa cónica sobre log ζ o −ζ′/ζ
   vale para ζ^c», con la clase infinitamente divisible (Lévy–Khintchine/Schoenberg) entre las que cruzan ∂log;
   hipótesis a romper: H_cone (homogeneidad en log ζ). `ROUND_013_C` O10: «la exponencial (Schoenberg/Fock) de
   una forma es positiva ⟺ la forma es condicionalmente negativa: reformulación; el producto de Schur S∘W
   necesita W ⪰ 0». `RULES_AVOID` M3 (positividad total falla en orden 2) y M4.
2. **Lo nuevo propuesto.** Un 𝕂 producto de Hadamard sobre primos, del que `a_T` sale por una operación no
   lineal. Lo único no registrado en primaria es la forma matricial del argumento (Lemas 1–2), no un objeto.
3. **¿Evita la dificultad?** No. La dificultad del antecedente es H_cone: la premisa es invariante bajo
   `log ζ ↦ c log ζ`. En un semigrupo de Schoenberg el parámetro `t` multiplica el generador; si el generador
   contiene la parte prima, `t` es exactamente el control `c` (con el arquimediano escalado a la vez). Si sólo
   se usa un `t` fijo, el producto de Schur se conserva bajo potencias de Hadamard enteras, y `c = 2` es entera
   (Lema 2). En ninguno de los dos casos hay un paso firmado que falle en `c = 2`.
4. **Enlace global.** El único sería Schoenberg aplicado al generador `ψ = −a_T` (núcleo), lo que es la
   reformulación O10: «ψ condicionalmente negativo» es el enunciado de signo mismo. Además Schoenberg habla de
   codimensión uno (Σ c_i = 0, o ∫Fφ = 0 tras conjugar por diag φ), mientras que `P_T` tiene codimensión dos;
   el enunciado de codimensión uno es más fuerte que el buscado (ARGUED que no se necesita ni se dispone).

Respuesta a la pregunta hostil central: la positividad para todo `t > 0` no puede distinguir `t = 1` de
`t = 2`, porque es una propiedad del generador (cono), y la positividad a `t` fijo, si procede de un producto
de Schur, se hereda a las potencias enteras. El objeto es ciego a `c = 2` en ambas lecturas. Por la regla del
filtro, me detengo antes de construir y uso el resto para fijar el cierre de clase.

## 1. Clase declarada

Discretización: un conjunto finito de puntos `t_1, …, t_N` de la ventana (o cualquier familia finita de
pruebas), y matrices simétricas reales. Escribo `ψ = A − Σ_p P_p`, con `A` la matriz arquimediana y `P_p` la
contribución de las potencias del primo `p` (pesos `v_{p^k}`). Para un peso general `a` (cΛ, borrado,
Beurling) `P_p^a` es la matriz correspondiente; para `cΛ`, `P_p^{cΛ} = c P_p`. `J` es la matriz de unos,
`∘` el producto de Hadamard, `e^{∘M}` la exponencial entrada a entrada.

**Clase 𝔖.** Certificados en los que el signo se deduce de la positividad semidefinida de un núcleo
`𝕂 = 𝕂_∞ ∘ ∘_p 𝕂_p` obtenida por el teorema del producto de Schur a partir de `𝕂_∞ ⪰ 0` y `𝕂_p ⪰ 0`, donde
`𝕂_p` depende sólo de los pesos de las potencias de `p` y `𝕂_∞` no depende del peso.

## 2. Resultados

**Lema 1 (Schoenberg por factores = reparto local; PROVED).** Si para todo `t > 0` se tiene
`e^{∘(−tA)} ⪰ 0` y `e^{∘(tP_p)} ⪰ 0` para cada `p`, entonces `A` es condicionalmente negativa y cada `−P_p`
también; luego `ψ = A − Σ_p P_p` es condicionalmente negativa porque es una suma de tales matrices, y lo mismo
vale para `A − c Σ_p P_p` con todo `c ≥ 0`, para el borrado del factor entero de un primo `p` y para
cualquier sistema de Beurling cuyos factores cumplan la hipótesis. (El borrado de una sola potencia `p^k`
queda cubierto si el factor reducido sigue cumpliendo la hipótesis.)

*Prueba.* Schoenberg (CITED): `e^{∘(−tM)} ⪰ 0` para todo `t > 0` ⟺ `M` condicionalmente negativa. Las matrices
condicionalmente negativas forman un cono convexo. ∎

Consecuencia: la variante «para todo t» es un reparto por átomo con positividad local, es decir la familia
cerrada Q1/O1 («compensación sin positividad por átomo» en sentido inverso: aquí cada átomo tendría que ser
positivo por sí solo). Con la batería E (CITED: dirección negativa de `a_T(2Λ)`), la hipótesis por factores es
falsa para Λ: si valiera, valdría para `2Λ`.

**Lema 2 (producto de Schur a t fijo es ciego a c entero; PROVED).** En la clase 𝔖, si
`𝕂^Λ = 𝕂_∞ ∘ ∘_p 𝕂_p^Λ ⪰ 0` se deduce de `𝕂_∞, 𝕂_p^Λ ⪰ 0`, y los factores son exponenciales de los pesos,
`𝕂_p^{a} = e^{∘ P_p^a}`, entonces:
(i) `𝕂^{2Λ} = 𝕂_∞ ∘ ∘_p (𝕂_p^Λ ∘ 𝕂_p^Λ) ⪰ 0` (y para todo `c ∈ ℕ`);
(ii) borrar el factor de un primo (o una potencia, si el factor reducido sigue siendo ⪰ 0) da `⪰ 0`;
(iii) para Beurling, si cada factor es ⪰ 0, el producto es ⪰ 0.

*Prueba.* `e^{∘ 2P} = e^{∘P} ∘ e^{∘P}`, y el producto de Schur de semidefinidas es semidefinido (CITED,
Schur 1911). (ii) y (iii) son el mismo teorema con menos o con otros factores. ∎

Así, el lado firmado no deja de ser `≥ 0` en ningún control. Por el Lema T de `ROUND_013_C` (PROVED en su
clase), una deducción `𝕂^a ⪰ 0 ⇒ a_T^a ⪰ 0` uniforme en el peso probaría positividad en `c = 2`, contra la
batería E. Toda deducción no uniforme tiene que usar una identidad propia de Λ ((PC), `Λ∗1 = log`), y entonces
el signo sale del objeto ciego más una restricción sin signo: Lema T.

**Observación (exponencial del lado primo; CITED/ARGUED).** El producto de Euler es la exponencial en la
variable de frecuencia de `Σ Λ(n)/log n · n^{−s}`, es decir un producto de convolución en `log`, no la
exponencial de Hadamard en `(t,s)` del núcleo `Σ v_n δ(t−s∓log n)`, que no está definida para deltas. En la
variable `τ`, `exp(Σ b_n (cos(τ log n) − 1))` es definida positiva si `b_n ≥ 0` (Lévy–Khintchine): es la fila
C5 de `INV_F_001`, premisa cónica, cubierta por F2. La identificación «exp de la parte prima = producto de
Euler» del encargo vale sólo en este sentido de frecuencia.

**Loewner/Pick y positividad total (CITED, repetición).** Matrices de Loewner positivas ⟺ función operador
monótona ⟺ Pick: es el cono C6–C7 de `INV_F_001`, lado de ceros (REF-D, thm:Z, no se reintenta). Positividad
total / PF: M3 y el índice (falla en PF₂ para el núcleo pertinente, PF₅ para el de dBN).

## 3. Controles (R3-i)

- `c = 2`: los factores son `⪰ 0` y su producto también (Lema 2 (i)); lo que falla es la deducción o la
  igualdad, nunca un resto firmado.
- Borrado: Lema 2 (ii).
- Beurling: Lema 2 (iii); el producto de Euler formal de Beurling tiene factores del mismo tipo.

## 4. Estado de M4

- PROVED aquí: clase 𝔖 (producto de Schur con factores exponenciales por primo, a `t` fijo) y su variante de
  Schoenberg por factores para todo `t` son ciegas a `c = 2`, al borrado y a Beurling (Lemas 1–2).
- Sigue ARGUED: que sólo las clases infinitamente divisibles y de Pick crucen ∂log (la tabla de `INV_F_001`
  tiene once conos, no una clasificación).
- Queda sin cubrir por 𝔖 (OPEN, sin objeto): factores por primo **no** exponenciales en el peso (p. ej.
  `𝕂_p` con positividad sólo a exponente no entero, Hadamard fraccionario de FitzGerald–Horn), y positividad de
  Hadamard que acople primos distintos (no factorizada por primo), que es la única vía de romper H_cone. Ninguna
  tiene candidato escrito; la segunda tendría que pasar por la estructura aditiva (S2: «toda recursión debe
  acoplar la estructura aditiva»).

## 5. Veredicto

Repetición de O10 (`ROUND_013_C`) e `INV_F_001` F2/C5; NO-GO de selección. Lemas 1–2: PROVED (sobre
Schoenberg y Schur, CITED). Signo global de `a_T`: OPEN. Siguiente operación explícita, si alguna: un núcleo de
Hadamard ⪰ 0 cuyo factor no se separe por primos y que use `m ≈ kn` (colisiones aditivas) en la entrada
`(t,s)`, con un paso firmado que falle en `c = 2`; no la propongo porque no tengo su fórmula.
