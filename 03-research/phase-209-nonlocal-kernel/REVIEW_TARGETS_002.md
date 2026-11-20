# REVIEW_TARGETS_002 — Qué contaría como un positivo en la continuación O1

2026-10-18. Revisor hostil. OPEN; no candidato ni nuevo NO-GO.

## 1. Corpus y oportunidad realmente disponible

Consultados índice README y 06_OPEN_RESIDUES (R1, R4, R7–R9 y W₂), P1_BBSTAR_001 §§1–5, D_CONSTRUCTION_001 (resumen, defecto de rango y Lema 𝔇-Sch), R11_2_ORIGIN_001 (polar), CELL_001/AUDIT_207 y controles de esta fase. Revisión adicional de R152_001 para evitar presentar como nuevo un operador de transferencia ya examinado. No se reabre ninguno de esos métodos.

**Hallazgo:** el corpus no contiene un lema positivo aritmética+FE listo para extraer por cambiar de representación. P1 no-BB* remite a crecimiento de secciones h⁰/𝔇-Sch, cuyo objeto sigue sin construirse. El defecto de rango de D_CONSTRUCTION no ofrece un positivo pequeño conocido: su dependencia de relaciones algebraicas entre log p es una dificultad propia; el memo observa que bajo Schanuel ese defecto desaparecería. No tomarlo como atajo constructivo.

La oportunidad concreta de O1 es otra: **el primer enlace parcial que sobreviva al cálculo exacto de una correlación entre alturas distintas y cuyo signo dependa de una restricción aritmética explícita**. No necesita ya pagar todo Q_T. Pero debe contener un término identificado de Q_T o de su déficit, con orientación de desigualdad útil. Un kernel positivo desconectado, aunque nuevo por fórmula, no cumple este objetivo.

Esto especifica un ensayo comprobable; no afirma que tengamos hoy su fórmula ni que su demostración sea accesible. No recomiendo sustituir la ausencia de candidato por otra lista de barreras.

## 2. Forma mínima del resultado positivo solicitado

El constructor debería entregar simultáneamente estos datos:

1. Un dominio efectivo explícito 𝒱_b, construido antes de usar el signo, y una forma B_b(F,G) de dos alturas con dominio, pesos y regularización. Si 𝒱_b es no lineal, especificar qué afirmación de positividad se pretende; no atribuirle automáticamente codimensión.
2. Una identidad exacta que use la FE sobre ese dominio. Invariancia J*BJ=B por promedio de una forma positiva no cuenta como acoplamiento aritmético demostrado.
3. Una desigualdad no trivial B_Λ(F,F)≥0 demostrada sin Q_T≥0. Tiene que intervenir una restricción verificable que no satisfaga el dato de primo eliminado pertinente, o un enlace específico que deje de valer para él.
4. Un enlace parcial de signo orientado: identificar qué contribución del nodo controla B, qué términos quedan y cuáles tienen signo probado. No es obligatorio cerrar el nodo para registrar el lema; sí obligatorio exhibir para qué sirve.

Si sólo se obtiene (1) y (2), etiquetar identidad estructural, no positivo. Si sólo se obtiene (3) para cualquier b, etiquetar norma/positividad genérica y reservar todo posible contenido para (4). Si (4) exige el signo desconocido del resto, declarar ese resto por separado: no adjudicarle positividad por nomenclatura.

## 3. Prueba temprana de especificidad

Usar b=Λ y b^(p), con alguna potencia p^k interior que tenga peso efectivo no nulo en el ensayo. El defecto Σ_{d|n}b^(p)(d)=log n−v_p(n)log p identifica un fallo exacto disponible, pero C-data ya explica que añadir esa identidad como ecuación entre datos no mueve por sí solo la forma.

**Pregunta concreta al candidato:** ¿en qué paso de la prueba de la desigualdad entra esa identidad de manera que intervenga una variable de la forma o del certificado? Si no hay tal paso, no atribuirle el signo. No basta que el kernel lleve Λ en sus coeficientes ni que cambiar p cambie sus entradas.

No pedir negatividad bajo todo borrado. No usar p exterior como falsificación de una afirmación local. No equiparar «no separa por el signo propio» con «ningún enlace específico puede funcionar»: ese salto sería incorrecto.

## 4. Qué no sería una continuación constructiva

- Reemplazar J+C compacto por I+J, proyecciones de J o promedios positivos: signo genérico ya identificado.
- Gram, Schur finito, Cholesky o un menor 2×2 tomado como ruta nueva sin una relación aritmética realmente nueva: rutas ya registradas.
- Volver a Gonek con peso indefinido o ignorando el resto y la escala.
- Usar un conteo h⁰ formal y atribuirle RR, dualidad o crecimiento sin construir el espacio y probar esas propiedades.
- Dar un signo que desaparece en el ortogonal polar: el objetivo vive precisamente allí.
- Clasificar una propuesta como def:PD y considerarla por eso imposible: una construcción explícita de certificado seguiría siendo un resultado; lo que falta es construirla y probarla.

## 5. Decisión de revisión

**Oportunidad: OPEN, específica y falsable en §§1–3; no positivo probado todavía.** No identifico en los residuos examinados una desigualdad positiva independiente ya disponible que satisfaga esas condiciones. Esta conclusión es sobre lo encontrado en el corpus, no una imposibilidad matemática ni motivo para cerrar O1. La siguiente revisión debe centrarse en las fórmulas de CONSTRUCTOR_002, evitando fabricar una fuente de signo a partir de una norma genérica.
