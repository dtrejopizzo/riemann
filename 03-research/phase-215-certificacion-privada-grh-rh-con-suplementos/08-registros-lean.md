# Alcance de los registros Lean

**Dictamen (c): esta revisión no certifica la formalización completa ni la correspondencia entre ella y los papers.** Los registros locales son evidencia documental de una compilación reportada, no una compilación repetida durante esta auditoría.

Se leyeron `06-alpoge-verification/README.md`, `scripts/AxiomCheck.lean`, `source-metadata/Statements.lean`, `source-metadata/MainTheorems.lean` y `results/axioms.log`. El archivo `README-mio.md`, que aparecía sin seguimiento de Git al empezar, no fue modificado ni utilizado.

El log contiene `riemannHypothesis : RiemannHypothesis` y reporta únicamente `propext`, `Classical.choice` y `Quot.sound` para cinco teoremas principales. El script de chequeo efectivamente pide `#print axioms` sobre esos nombres. `Statements.lean` expresa ceros de zeta excluyendo enteros negativos pares, un semiplano sin ceros para caracteres de Dirichlet salvo el polo, y ceros de L en la franja abierta. Esas fórmulas tienen el alcance que sus nombres sugieren al nivel de las expresiones visibles.

Esto no establece todavía:

1. Que las definiciones transitivas de zeta, L y `RiemannHypothesis` del entorno compilado sean exactamente las esperadas; `Statements.lean` importa Mathlib y no contiene todo ese entorno.
2. Que el log corresponda a la totalidad del árbol fuente y a los binarios cuya cadena de confianza se pretende verificar.
3. Que cada enunciado humano de 49–56 sea traducción fiel de una declaración formal, con las mismas constantes e hipótesis.
4. Que una prueba formal del resultado final valide automáticamente una prueba en prosa diferente del mismo resultado.

El README describe un archivo de aproximadamente 175.000 módulos y una compilación de gran escala. No se descargó ni reconstruyó ese archivo en esta tarea. Tampoco se ejecutaron `lake build` o un kernel independiente. Por ello no se informa «Lean verificado» como resultado de este trabajo.

La siguiente comprobación útil sería un mapa bidireccional entre los enunciados centrales de cada paper y declaraciones Lean exactas, incluyendo sus definiciones y el árbol transitivo de dependencias. Esta tarea es distinta de revisar los logs y distinta de auditar las pruebas humanas, que fue el encargo principal.
