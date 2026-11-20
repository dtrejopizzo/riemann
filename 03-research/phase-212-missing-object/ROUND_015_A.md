# Ronda 15, memo A — Transporte de retardos no afín: cotejo y cierre por repetición

Encargo: ver si un transporte de retardos que no es afín en el retardo (una reindexación de contactos que depende de la
factorización) lleva el canal de productos (retardos `log(pq)`, donde vive `Λ·log + Λ∗Λ = μ∗log²`) al canal de
cocientes (retardos `log(p/q)`, donde vive `‖LF‖²`). Se pedían tres realizaciones: (i) reindexación aditiva `(k,h)`,
`m − kn = h`; (ii) multiplicadores de Mellin compuestos con el truncamiento y con `𝓕`; (iii) sumas de Ramanujan,
gran criba y criba Λ² de Selberg.

Lectura en primaria: ROUND_014_A §§0–3 (Lemas P, U, Q); RULES_AVOID §L (L2, L4) y las líneas 37, 57 y 84–89;
`phase-188-closing-D/L2_BUILD_030_NEAR_AS_SHIFTED_CONVOLUTION.md` §§1–2; `N_BUILD_003_LAG_RESTRICTED_SIEVE_NOGO.md`
(cotejo y Teorema 1); `phase-167-witness-weighted-sieve/README.md` y `R167_103` §0;
ROUTES-TRIED-INDEX/README, entradas INV_C_001, INV_H_001 y SPEC_SIGN_OBJECT_008; índice de
`POWER_GRAM_SLICES_OBSTRUCTION.md` §§17.1–17.2. No releí enteros R162_1102 ni la fase 200, así que esa parte del
cotejo es indirecta (a través del índice).

## 0. Filtro de cuatro puntos

1. **Antecedente más cercano, uno por realización.**
   - (i) `L2_BUILD_030` §1(c) ya escribe el término cercano exactamente como suma sobre desplazamientos aditivos `h`,
     `Σ_{m−kn=h} s_m s_k v_n c₀(log(m/(kn)))`, con `c₀(−log(1−h/m))`. Además, §2 identifica su estructura de signo. La
     reindexación por `(k,h)` en lugar de `n` es esa misma fórmula. La variante «Farey/coprimos» de la masa de fibras
     sobre `log ℚ` está cerrada en INV_C_001 («no information for the sign», residuo CLOSED). La selección
     `(m,n) → (m+n, m−n)` está rechazada en las reglas del proyecto y en GRAM §§17.1–17.2.
   - (ii) ROUND_014_A, Lema U y su relación con R1. Los multiplicadores de función del generador de dilataciones
     conmutan con las traslaciones en `log n`. Compuestos con `J`, `𝓕` y el truncamiento dan operadores de la clase
     `𝒯` (ARGUED para `𝓕` en 014_A) o el concomitante de borde `⟨g,[P,S]w⟩` (R161_035, 057–065: sin signo).
   - (iii) Ramanujan/`c_q`: INV_H_001, clase `𝒞_H` NO-GO («finite Ramanujan = regrouped Möbius», con la indicación
     explícita «do not retry Ramanujan … as an identity»). Gran criba: SPEC_SIGN_OBJECT_008 V3 (= R162_1102, Thm O/O′),
     que sólo da cota superior y vale para todo peine. A esto se suma ROUND_014_A, Lema Q(a): `TT*` es diagonal en `n`.
     Pesos de Selberg/Barban–Vehov/GPY/`Λ_R`: RULES_AVOID L2 (fase 200 Q1–Q3, R162_1003 §4). Mayorantes de criba
     restringidas a retardos: N_BUILD_003. Criba ponderada por testigo: fase 167, Teorema B′ y Teorema S (cribas
     válidas en sistemas de Beurling discretos).
2. **Objeto nuevo.** No encontré ninguno. Las tres realizaciones coinciden, salvo por la notación, con objetos ya
   escritos en el corpus.
3. **Por qué esquivaría la dificultad.** No aplica. Lo único que no está escrito literalmente es una observación sobre
   la criba Λ² (§1), y esa observación es otro cierre, no una vía.
4. **Enlace global.** Ninguno.

**La idea es una repetición y se detiene aquí.** No hice derivaciones, cómputos ni certificados.

## 1. Por qué el cuadrado de Selberg no conecta (observación de clase)

**Clase `𝒮_Λ²`.** Son las expresiones `Σ_n x_n Q_n(F, λ)` en las que `Q_n ≥ 0` es un cuadrado o una suma de cuadrados
cuyos coeficientes no dependen de `Λ` (por ejemplo `Q_n = (Σ_{d|n} λ_d)²·|ψ_n(F)|²`) y `x_n` es afín en `Λ` con
`x_n ≥ 0` cuando `Λ ≥ 0`.

**Observación.** Ningún certificado del tipo «`a_T(F) = Arch-parte Λ-libre − Σ_n x_n Q_n + (resto ≥ 0)`» con términos
de `𝒮_Λ²` usa una relación que falle en los tres controles a la vez. Por lo tanto, por el Lema T (ROUND_013_C), no
puede certificar `a_T ≥ 0`.

*Prueba.* La no negatividad de `Σ x_n Q_n` sólo usa `x_n ≥ 0`, y esto vale para `cΛ` con `c = 2`, para `Λ` con una
potencia de primo suprimida y para un peso de Beurling no negativo. El cuadrado `(Σ_{d|n}λ_d)²` no ve `Λ`: sus
coeficientes son los `λ_d`, fijados de antemano. Lo único que el cuadrado de Selberg «sabe» de los primos es que
`Σ_{d|p} λ_d = λ_1 = 1` para `p > D`, y eso es una propiedad del soporte de `λ`, válida para cualquier sucesión
`x_n ≥ 0` sostenida en enteros sin factores pequeños. La información aritmética de la criba sale de evaluar
`Σ_n x_n (Σ_{d|n} λ_d)²` con `x_n ≡ 1`, a través de la regularidad `|r_d| ≤ 1` del conteo de múltiplos en intervalos
(R167_103 §0, ítem 1). Esa regularidad se transfiere a los sistemas de Beurling discretos (fase 167, Teorema S), así
que tampoco falla en el tercer control. ∎

**Etiqueta.** PROVED como consecuencia directa del Lema T y del Teorema S, en la clase declarada. No es un enunciado
sobre cribas no lineales en `Λ`. Una criba cuyos pesos `λ_d` dependan de los valores exactos de `Λ` no está cubierta,
pero ese caso cae en RULES_AVOID L2/L4 (Möbius truncado, reparto del símbolo).

**Respuesta a la pregunta del encargo.** El cuadrado de Selberg es no lineal en los pesos de criba, no en `Λ`.
La no linealidad que exige OBJECT_SPEC es en los valores exactos de `Λ`. Lo que el cuadrado aporta sobre primos es una
cota superior Λ-libre del tipo `Σ_{p≤x} 1 ≤ (2+o(1))x/log x`, y esa cota vale para `cΛ` con `c ≤ 2` y para Beurling.
Pertenece a la clase `C_BT` de Paper 47 (cor:void, thm:finmod), que se cierra por supresión (N_BUILD_003, cotejo).
No digo nada sobre paridad: no tengo un enunciado probado de esa índole dentro de esta clase, y no lo uso.

## 2. Búsqueda de una idea cercana distinta

Revisé dos candidatas más:
- Un núcleo en la red `(k,h)` cuya dependencia en `h` no sea suave, por ejemplo con pesos que dependan de
  `gcd(h,k)`.
- Cortar las sumas desplazadas `Σ_{m−kn=h} Λ(n)` por clases de `h`.

Las dos son funciones de `h` multiplicadas sobre la fórmula de `L2_BUILD_030` §1(c). Son lineales en `Λ`, y su
aritmética la difiere ese memo a la pista (N), que INV_J_001 cierra en J2: la positividad de Gram/Bochner es genérica
en el peine. Ninguna aporta una operación de signo. No tengo una idea defendible distinta que proponer dentro de este
encargo.

## 3. Para el revisor

- Volver a derivar §1. El punto delicado es si el Teorema S (fase 167) cubre la positividad usada. Basta con que se
  use sólo `x_n ≥ 0`, y eso es inmediato.
- Confirmar que `L2_BUILD_030` §1(c) coincide con la realización (i), con `h = m − kn` y retardo `−log(1 − h/m)`.

**Próxima operación explícita (OPEN, no construida).** Haría falta una identidad en la que los pesos del cuadrado
`λ_d` se definan por los propios valores de `Λ`, por ejemplo `λ_d` igual a la solución de un problema extremal cuyo
dato es `Λ` restringido a la ventana, de modo que el cuadrado sea no lineal en `Λ`. Antes de construir nada debe
cotejarse contra RULES_AVOID L2/L4 y contra ROUND_014_A, Lema P(b). Si `λ` depende de `Λ` sólo a través de un cociente
afín, la identidad cae de nuevo en la polarización del Lema P.
