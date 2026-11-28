# Dictamen de la revisión matemática

> **REGISTRO HISTÓRICO DE LA PRIMERA TANDA.** Sus pendientes y dictámenes globales no representan el estado vigente. La segunda auditoría resolvió numerosos puntos y demostró un fallo de caracteres en la prueba de53. Consultar [estado actualizado](../auditoria-profunda/ESTADO.md), [error53](../auditoria-profunda/ERROR-53-CARACTERES.md) y los certificados de46 enlazados desde README. Se conserva el texto inferior para trazabilidad; no debe citarse como conclusión final actual.


Fecha: 28 de noviembre de 2026. Copia local del repositorio en el commit `97fb4e78d5a858baa926829a42336ae3b914e59a`; hashes individuales en `evidencia/fuentes.json`. Se excluyeron de la lectura los papers 47 y 48. Se trabajó sobre LaTeX y los registros indicados, no sobre una versión remota que pudiera cambiar durante la revisión.

**La revisión no certifica la demostración de GRH/RH de la serie. Tampoco produjo un contraejemplo confirmado a sus teoremas principales.** Hay argumentos concretos comprobados y pasos centrales que permanecen **(c), no verificados**, con sus localizadores y la comprobación necesaria para resolverlos. La mayor parte de esos pasos tiene una prueba escrita en el manuscrito: el límite es de esta auditoría, no una afirmación de que el autor haya omitido toda prueba.

Los dictámenes siguen el esquema solicitado:

- **(a) correcto como está escrito**, en el alcance que se especifica. Cuando se verifica una implicación a partir de lemas, se dice expresamente que no se certificaron todos sus antecedentes.
- **(b) incorrecto**, con primer fallo demostrado. No se obtuvo un (b) defendible para los teoremas principales. Se identifican separadamente precisiones de datos o formulación.
- **(c) no verificado**, indicando el paso exacto y lo que falta comprobar. No equivale a «falso», ni a «correcto por no haber encontrado un error».

## Resultados centrales

| Bloque | Resultado de esta revisión |
|---|---|
| 46, equivalencia entre positividad en todas las ventanas y RH | **(a)**. Se comprobaron fórmula explícita, dominio de forma y construcción del test primitivo negativo en 45. |
| 46, cotas hasta `(log 5)/2` | **(c)**. La reducción a inercia es comprobable; faltan certificados ejecutables y matrices para validar los números reportados. |
| 46, ventana `2.8022` | **(c)**. Z2 y la cota publicada Z3 se cotejaron; el filtro y las 17 verificaciones no se reproducen. Z1 no se certificó independientemente. |
| 43 | **(c)** global. Descomposición del grupo, símbolo radial y estabilización comprobados; cálculo completo de Hochschild, firma y completación no certificados. |
| 44 | **(a)** para los dos teoremas principales de composición/contacto examinados, con su rango; no aprobación automática de todos los resultados secundarios. |
| 45 | **(a)** para comparación con fórmula explícita, normalización radial y criterio primitivo. Esos resultados tienen antecedentes clásicos. |
| 50 | **(a)** para el teorema algebraico con sus hipótesis y sus inputs internos; **(c)** para certificar íntegramente su aplicación a todos los datos automórficos posteriores. |
| 49 | **(c)** para seesaw global, constante exacta en todos los conjugados y divisibilidad completa. Hay pasos parciales comprobados. |
| 51–52 | **(c)** para segundo momento, estimaciones locales y multiplicidades completos. Se verificaron varias constantes, reducciones y cierres de rango. |
| 53–54 | **(c)** para exchange, cadena automórfica, fórmula de un lift y test de valoración mínima completos. Álgebra de inyectividad y de compresión de determinantes comprobada. |
| 55 | **(c)** para existencia global de twists, Ribet/Selmer y clases impares completos. La irreducibilidad sí está explicitada; dualidad y suma de pérdidas se comprobaron en las reducciones indicadas. |
| 56 | **(c)** para los teoremas integrales completos. Se verificaron sustituciones y NM en la aplicación; NM no es condición necesaria para toda anulación, y el texto no formula tal equivalencia. |
| Uniones | Entradas centrales de la tabla de 46 cotejadas con grados de cobertura explícitos; **(c)** para certificar todas las importaciones transitivas y sus aplicaciones. |
| Novedad y conexiones | Identificados antecedentes y una conexión cuantitativa propuesta; no se certifica prioridad global ni nacimiento de un campo nuevo. |

## Observaciones que permiten mejorar el manuscrito

1. **Paper 46, línea 1766:** `omega_-` debe ser al menos `2A=5.88394705…` para el corte especificado. `5.8839` puede ser un resumen decimal, pero no una cota superior literal. El certificado debe conservar valores exactos o redondeos dirigidos. Las cotas de las dos colas son numéricamente consistentes; esto no certifica la inercia.
2. **Paper 51, línea 3961:** la absorción `f·2^(3−k)≤b^-10` necesita una relación entre k y `log b`, además de las cotas listadas localmente. La relación viene de los datos admisibles; conviene incluirla al aislar el lema. No se encontró una contradicción en la aplicación vigente.
3. **Paper 50:** su conclusión es de colongitud truncada, con término excepcional `θj`. Presentarla como una cota uniforme de todos los divisores elementales perdería una parte esencial del enunciado.
4. **Paper 56:** «para todo ℓ» no elimina las condiciones sobre pesos, ventanas y distribución de letras. NM es una condición suficiente del argumento genérico, no una caracterización necesaria de anulación. El reporte ofrece un ejemplo de rango positivo que distingue ambos conceptos.

También se descartaron objeciones que serían injustas con esta versión: la irreducibilidad residual de 55 sí está escrita; 51 sí trata la extensión de la comparación a lugares inertes y cierra el rango de corangos; la constante corregida `3x^35` de 54 sí llega a 46; y la diferencia entre los retículos de 49 y 51 sí tiene un transporte propuesto.

## Lectura de la conexión propuesta

La idea que merece aislarse es convertir divisibilidad de coeficientes theta en una cota unilateral sobre primos, comparando el tamaño de muchas formas con un límite inferior de su covolumen. El segundo momento garantiza el rango casi total; los períodos CM, los twists y los grupos de Selmer deben hacer compatibles las dos cuentas.

La serie reconoce que la ruta automórfica y su matemática se atribuyen a Levent Alpoge, mientras que la organización en tres teoremas y su presentación en esta serie son del autor de los manuscritos. Los nombres de especialistas proporcionados por el usuario se usaron para definir las tareas de los agentes; ninguno de esos investigadores participó ni avaló esta revisión.

Una línea de investigación describible sería **métodos de pendientes para retículos automorfos y divisibilidad theta**. Es una propuesta de programa, no una declaración de nueva disciplina. El capítulo de conexiones da resultados intermedios concretos que podrían validarse y desarrollarse sin depender de RH.

## Método y alcance material

Trabajaron el agente principal y tres agentes especializados: theta/Hecke/covolumen; segundo momento/traza y conexiones; Selmer/Hodge integral. Hubo relecturas cruzadas de los dictámenes positivos y de los ejemplos. La revisión no reproduce un arbitraje exhaustivo línea por línea de todos los manuscritos ni la construcción formal Lean completa.

El inventario contiene 14 fuentes, 1910 etiquetas compartidas y 3526 referencias internas explícitas con las claves reconocidas por el script. Esos números incluyen repeticiones y el volumen 58; **no son un número de teoremas verificados**. Las tablas de los capítulos explican exactamente qué fue cotejado. Las referencias que no se individualizan quedan (c).

No se ejecutaron los certificados de las ventanas finitas porque no se localizaron en los artefactos examinados. Los chequeos propios de constantes usan precisión múltiple sin intervalos y están identificados como consistencia, no como certificación. No se volvió a compilar el archivo Lean de gran escala. Los papers y el archivo sin seguimiento `06-alpoge-verification/README-mio.md` permanecieron intactos.

## Prioridades para cerrar la revisión

La certificación global exige resolver varios trabajos independientes, no sólo corregir los dos detalles editoriales: aportar las inercias reproducibles de 46; completar la auditoría de períodos y divisibilidad de 49; certificar los sistemas locales y el término principal uniforme de 51–52; comprobar exchange y test forms de 53–54; cerrar Selmer y clases impares de 55; y verificar los lemas integrales centrales de 56. Los capítulos señalan sus etiquetas precisas. Sólo después puede una comparación semántica completa de las uniones sustentar un dictamen sobre la cadena entera.
