# Fase 212 — Especificación del objeto a construir

Fusiona P47 prob:region y prop:spec, P48 req:spec (R1–R12), GRID §7 (S1–S12), CW §3.2 ((α)–(μ)) y
211/OBJECT_SPEC_001 (R1–R5), sin repetir. Notación de `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}.

## 1. Forma del objeto

Alcance: esta especificación define el programa de identidad (G), no una necesidad demostrada
para toda prueba posible de positividad global. La vía asintótica de P47 thm:wit-Tc(iv) y
ROUND_022_B, Lema 1, sigue admisible con sus cuantificadores completos; véase RULES_AVOID B2.
No se presenta esa vía ya registrada como una nueva construcción.

Un objeto 𝒪 = (ℋ_T, V_T, ρ_T)_{T>0} con:

- ℋ_T un espacio de Hilbert explícito y V_T : P_T ∩ 𝒟_T → ℋ_T lineal;
- ρ_T una forma sobre P_T **manifiestamente** no negativa (suma de cuadrados escrita, o medida positiva
  escrita);
- la identidad exacta **(G)** a_T(F) = ‖V_T F‖² + ρ_T(F) para todo F ∈ P_T ∩ 𝒟_T y todo T.

Se admite la variante por reducción exacta: (G) sobre el portador finito de (L2), sobre la matriz 𝔸_M
de (S), sobre la función 𝖡 de un perfil, o sobre la escalera de potencias, siempre que la reducción
usada sea una de las PROVED (README §3).

## 2. Cláusulas

O1. **Exactitud.** (G) es una igualdad. Ningún término se acota en valor absoluto, por norma, por
    Cauchy–Schwarz con pérdida ni por un resto o(·).
O2. **Dependencia exacta de Λ, con la no linealidad en el acoplamiento.** V_T usa los valores exactos
    Λ(n), n < N. La forma es afín en el peine, de modo que el grado en los pesos es invisible para
    ella, y toda relación polinómica sobre Λ en [2,N) se deduce de los átomos lineales
    Σ_{d|n}Λ(d) = log n (`ROUND_001_D.md` Lema A; la relación de grado dos es la regla de Leibniz
    sobre Λ∗1 = log, `ROUND_001_A.md` Lema B). La no linealidad que decide el signo tiene que estar en
    cómo V_T actúa sobre F (el cuadrado ‖V_T F‖²), no en productos de pesos. Un uso lineal en que F
    entra sólo por su autocorrelación es un certificado, cuyo contenido es λ^prim (P47 cor:shape (a)).
O3. **Las tres entradas juntas en una misma línea.** El producto de Euler sobre todos los primos, la
    ecuación funcional con Γ(s/2) a conductor 1 y la integralidad (coeficientes b ≡ 1 de la serie
    sobre ℕ, o Σ_{d|n}Λ(d) = log n) entran en la demostración de (G) en un mismo paso, no encadenadas
    (P48 req:spec R2–R3; P47 prop:shape-inputs).
O4. **Ruptura, no pérdida de margen.** Para cada falsificador de `RULES_AVOID.md` §E se señala la línea
    de la demostración de (G) que deja de ser cierta. En particular (G) es falsa para cΛ con c ≠ 1 por
    pequeño que sea |c − 1|, y para a_P con P > N (que coincide con Λ en casi toda propiedad de clase).
    Una ruptura formal aislada no basta para proponer una candidata: hay que demostrar la identidad
    completa y la no negatividad de su lado derecho para Λ. Una vez demostrado eso, el paso que falla
    en un falsificador puede ser la propia identidad de representación; no es necesario que también
    pierdan positividad la norma o el resto auxiliares. `REVIEW_003.md` R3-i describe la ruptura
    algebraica automática, pero no excluye una representación positiva exacta y específica de Λ.
    El Lema T de `ROUND_013_C.md` sólo transfiere la conclusión a un falsificador si sobreviven la
    identificación con la forma y todas las hipótesis que dan el signo.
O5. **Uniformidad en T.** La construcción es una sola, válida para todo T; no una familia de
    certificados cuya dimensión o precisión se recalcula por ventana (W-fam; P47 cor:shape (b)).
O6. **Ve las casi-coincidencias.** ‖V_T F‖² no se anula idénticamente sobre los vectores que ven
    m ≈ kn, m ≠ kn; allí está el signo (P47 prop:nearfree, rem:bar-arith).
O7. **Usa la fluctuación, no la densidad** (P47 thm:ceiling, prob:region (7)); **usa la parte positiva
    del símbolo en todo ℝ junto con el conjunto negativo** (prob:region (8)).
O8. **No es** un funcional del minimizador, un funcional acotado de los pesos, un criterio local, un
    determinante o momento del haz, ni una suma de cuadrados aritmética pura para T ≥ ½log3
    (P48 req:spec R7, R9, R10).
O9. **Acopla Λ(n), n < N, con la ecuación funcional por una vía distinta del factor común
    ζ(½+iτ)** (P47 prop:spec (5), OPEN: ningún objeto conocido). Las identidades de la franja cumplen
    la letra de esta cláusula pero son genéricas en el peine: no sirven solas.
O10. **Cruza la derivada logarítmica.** Las positividades de la serie de Dirichlet que pasan a su
     derivada logarítmica son sólo las infinitamente divisibles, cono homogéneo que cΛ conserva
     (P47 prop:spec (6)); el objeto debe trabajar del lado de Λ o cruzar por un mecanismo no homogéneo.
     La primera relación exacta no homogénea en (1, Λ) es de grado dos:
     Λ·log + Λ∗Λ = μ∗log² (P47 rem:spec-scope).

## 3. Dos restricciones probadas sobre (G) (ronda 1; `REVIEW_001_LC.md`)

Ninguna aporta signo; delimitan dónde no buscar.

R-comp (PROVED relativo a tres teoremas clásicos citados; `ROUND_001_L.md`, Teorema 3.1, Cor. 4.1).
En la escalera de potencias, si el núcleo objetivo menos ε veces un núcleo [M₀(u)+M₀(v)]/(u+v), con
M₀ real-positiva en Re u > 0 y real en (0,∞), es semidefinido positivo en todos los tamaños, entonces
M₀ no tiene término lineal y su medida de borde está dominada por (1/ε) veces la de M, que bajo esa
hipótesis es puramente atómica. La atomicidad es conclusión bajo la hipótesis, no un hecho
incondicional. La exclusión no es efectiva (no da bloque ni vector). No restringe espacios ℋ_T que no
provengan de un comparador de esta clase: fuera de ella no hay rigidez.

R-cont (PROVED relativo a 211 GRAM_SLICES §18.2 y a la holomorfía de z ↦ P_z; `ROUND_001_C.md`,
Lema 1, Teorema R). En una identidad única A_0 = Σ cuadrados + resto no negativo sobre el portador de
escalas enteras, cada cuadrado es continuo en la norma del grafo y sus coeficientes son valores
enteros de una función holomorfa de crecimiento polinómico en un semiplano. Ningún cuadrado no nulo
se anula sobre un conjunto de nodos o modos de suma recíproca divergente, ni es la torsión de un
funcional continuo por una función con conjunto de nivel divergente de complemento divergente
(caracteres, sumas de Ramanujan no constantes, μ, μ², Λ, indicadoras de residuos, múltiplos o gcd
fijo). Luego V_T usa observables globales, no de soporte finito ni seleccionados aritméticamente en
el nodo. Quedan admitidos: cuadrados continuos con índice o pesos aritméticos en la dilatación,
torsiones sin conjunto de nivel divergente, y objetos por ventana o sobre 𝔸_M.

## 4. Qué entrega una candidata antes de construir

(1) antecedente más cercano, con archivo y sección; (2) el objeto: ℋ_T, V_T, ρ_T escritos, o la parte
que falta por escribir señalada; (3) por qué el cambio evita la dificultad concreta del antecedente;
(4) la identidad que la conecta con (G) sobre el portador completo; (5) para cΛ y a_P, la línea que se
rompe. Una candidata que no puede escribir (2) y (5) no está lista para construcción.

## 5. Cláusulas añadidas por las rondas 6–17 (índice maestro `05-meta-and-planning/ROUTES-MASTER-INDEX.md`, III.0 §2; la lista completa de restricciones de todo el corpus está en su Parte II)

O11. **Los tres controles a la vez.** La relación exacta que da el signo falla simultáneamente en `cΛ`
     (`c = 2`), en el borrado de una potencia de primo y en un peso de tipo Beurling. Un signo obtenido de
     cuadrados ciegos más relaciones válidas en alguno de los tres prueba un enunciado falso (Lema T,
     `ROUND_013_C`; PROVED en la clase declarada).
O12. **Arch y el peso del mismo objeto.** Frente a `c = 2`, la parte arquimediana y el peso salen del
     mismo objeto en el mismo paso: un objeto que produce el peso `2Λ` con todas las relaciones exactas
     (anillo `ℤ×ℤ`) produce también Arch duplicada (`ROUND_016_B`). Frente al borrado, se usa la
     integralidad; frente a Beurling, el espaciado igual de los enteros. Precisa O3.
O13. **El vector tiene fórmula propia.** En `a_T = ‖V_T F‖² + ρ_T`, `V_T` se escribe sin invertir ni
     factorizar la forma. Si `V_T` puede contener `Λ` de modo arbitrario, la identidad existe si y sólo si
     `a_T ≥ 0` (`ROUND_014_A` Lema P(c)); si `V_T` es afín en el peso, el resto es ciego (polarización).
O14. **Un bloque de Gram o de Schur necesita una construcción y una identificación independientes del signo buscado.**
     No basta fabricar un bloque cuya positividad presuponga a_T≥0, ni exhibir un Gram positivo sin
     demostrar su identidad completa con a_T. Los lemas de `ROUND_013_B` no excluyen un Gram explícito
     con fórmula propia y una identificación aritmética específica demostrada para Λ. La equivalencia
     de Schur por sí sola no es una prueba de imposibilidad. Se conserva la exclusión de una suma de
     piezas por primo cada una con signo (falso para `Λ`
     pasado `T ≈ 0.697` en la clase de dos posiciones, NUMÉRICO; factores exponenciales por primo ciegos,
     `ROUND_014_B`).
O15. **La razón no es «la identidad se rompe fuera de `c = 1`».** El conjunto de `c` con positividad
     contiene un entorno de 1 del tamaño del margen (`ROUND_013_A`); el objeto tiene que explicar una
     coincidencia de ese orden entre Arch y la parte de primos, no una igualdad formal.
O16. **Acopla primos distintos a través de la estructura aditiva.** Lo que trata a cada primo por
     separado, es lineal en `F` y afín en el retardo, está cerrado o es ciego (lectura de conjunto de las
     rondas 13–16; precisa O6).
O17. **Una fuente de positividad auxiliar no sustituye su identificación con la forma completa.**
     El Lema K de `ROUND_013_C` prueba positividad de las Hessianas de las dos clases allí declaradas
     cuando sus medidas o pesos son positivos; no excluye una identidad aritmética específica que las
     identifique con a_T para Λ y falle para un falsificador. Por tanto no se prohíben universalmente
     las medidas positivas ni los pesos positivos como fuente del signo. Se exige construir y probar
     el enlace exacto, con el alcance global y la fórmula propia de las otras cláusulas. Las exclusiones
     relativas a tasas de generadores (`ROUND_016_A`) y monotonía completa arquimediana (`ROUND_016_C`)
     conservan las clases e hipótesis de sus enunciados; no se amplían a toda representación positiva.

## 6. Terreno sin objeto

La lista vigente está en el índice maestro `05-meta-and-planning/ROUTES-MASTER-INDEX.md` (Parte I, secciones B y B′) y en las secciones X–AB de `RULES_AVOID.md`.
