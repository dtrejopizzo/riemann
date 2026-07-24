# Índice de cobertura y control de tamaño

## Cobertura del corpus

| Sector | Inventario contrastado | Evidencia de lectura |
|---|---:|---|
| Paper 36 | 8.806 líneas; 54.962 palabras | [`PAPER36_AUDIT.md`](PAPER36_AUDIT.md) y [`fragments/PAPER36_LOGIC_AUDIT.md`](fragments/PAPER36_LOGIC_AUDIT.md) |
| RH1–RH3 | 266 directorios de tarea | [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md) y [`fragments/RH1_RH3_AUDIT.md`](fragments/RH1_RH3_AUDIT.md) |
| RH4–RH6 | 211 directorios de tarea | [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md) y [`fragments/RH4_RH6_AUDIT.md`](fragments/RH4_RH6_AUDIT.md) |
| RH7–RH9 | 149 directorios de tarea | [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md) y [`fragments/RH7_RH9_AUDIT.md`](fragments/RH7_RH9_AUDIT.md) |
| Fases 000–025 | Todos los directorios existentes del intervalo | [`fragments/PHASES_000_025_AUDIT.md`](fragments/PHASES_000_025_AUDIT.md) |
| Fases 026–050 | Todos los directorios existentes del intervalo, incluidas las dos ramas 044 | [`fragments/PHASES_026_050_AUDIT.md`](fragments/PHASES_026_050_AUDIT.md) |
| Fases 051–075 | Todos los directorios existentes del intervalo | [`fragments/PHASES_051_075_AUDIT.md`](fragments/PHASES_051_075_AUDIT.md) |
| Fases 076–089 | Todos los directorios; 512 Markdown contrastados | [`fragments/PHASES_076_089_AUDIT.md`](fragments/PHASES_076_089_AUDIT.md) |
| Fases 090–101 | Todos los directorios existentes del intervalo | [`fragments/PHASES_090_101_AUDIT.md`](fragments/PHASES_090_101_AUDIT.md) |

Los nueve programas contienen 626 directorios `task`, continuos desde `task1` hasta el máximo de cada programa: 89, 94, 83, 83, 60, 68, 43, 27 y 79. El árbol de fases contiene 101 directorios. Los rótulos 001 y 002 no existen y el 044 aparece en dos rutas; la cobertura conserva esas anomalías en vez de inventar continuidad.

El control nominal de archivos con `CLOSURE`, `cierre` o `final` no encontró ningún candidato fuera de los intervalos auditados. Los binarios, imágenes, cachés y salidas masivas no fueron tratados como demostraciones; se contrastaron cuando un texto apoyaba en ellos una afirmación material.

## Mapa del dossier

| Documento | Función |
|---|---|
| [`README.md`](README.md) | Entrada, dictamen y orden de lectura. |
| [`00_SCOPE_AND_METHOD.md`](00_SCOPE_AND_METHOD.md) | Corpus, etiquetas, H0 y precedencia. |
| [`MASTER_CONTEXT.md`](MASTER_CONTEXT.md) | Contexto autocontenido del programa completo. |
| [`PAPER36_AUDIT.md`](PAPER36_AUDIT.md) | Columna Step 1–15, H0–H8 y cadena Ω. |
| [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md) | Síntesis de los nueve programas. |
| [`PHASES_AUDIT.md`](PHASES_AUDIT.md) | Genealogía matemática de todas las fases. |
| [`NO_GO_AND_RETRACTIONS.md`](NO_GO_AND_RETRACTIONS.md) | Clases cerradas, circularidades y retiros. |
| [`LIVE_FRONTIER_AND_RESTART_PLAN.md`](LIVE_FRONTIER_AND_RESTART_PLAN.md) | Frente real, puertas y orden de trabajo. |
| [`fragments/CROSS_PROGRAM_SYNTHESIS.md`](fragments/CROSS_PROGRAM_SYNTHESIS.md) | Contraste transversal independiente. |
| [`fragments/COVERAGE_VALIDATION.md`](fragments/COVERAGE_VALIDATION.md) | Validación mecánica de inventario y enlaces. |

Los restantes fragmentos son las auditorías de bloque listadas en la tabla de cobertura. Una discrepancia no se resuelve por el nombre del archivo: prevalece la corrección que exhiba el paso matemático y sus hipótesis.

## Control de tamaño

El dossier completo contiene veinte Markdown, menos de 50.000 palabras y menos de 350.000 bytes. Incluso usando la cota deliberadamente conservadora de un token por byte, el contexto queda por debajo de 350.000 tokens y lejos del límite de un millón.

La cota por bytes evita depender de un tokenizador concreto y sobreestima fuertemente el tamaño real. Por tanto el dossier completo puede cargarse como contexto único dentro del presupuesto solicitado.

## Controles de integridad

- Todos los directorios de fase existentes pertenecen a un intervalo auditado.
- Todos los directorios de tarea RH pertenecen a una auditoría de bloque.
- Los destinos de los enlaces Markdown locales fueron verificados.
- Se separaron resultados demostrados, condicionales, numéricos, refutados, abiertos y de fuerza-RH.
- Los rótulos `QED`, `closure` o `theorem` no se aceptaron como evidencia sin auditar hipótesis y cuantificadores.
- La revisión de novedad bibliográfica queda como puerta separada; este índice certifica cobertura interna, no prioridad externa.
