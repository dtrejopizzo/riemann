# Alcance y método de la revisión

## Corpus incluido

La revisión cubre tres capas.

| Capa | Tamaño inspeccionado | Protocolo |
|---|---:|---|
| Paper 36 | `main.tex`: 8.806 líneas, 54.962 palabras | Lectura completa y segunda auditoría lógica independiente. |
| RH1–RH9 | 5.867 archivos; 743 Markdown; 629 `README`/`OVERVIEW` | Lectura de todas las respuestas de trayectoria y contraste con datos, código o tablas cuando sostienen una afirmación material. |
| Fases | 101 directorios; 4.052 archivos; 2.228 Markdown; 12 TeX; 1.067 sondas Python | Lectura por bloques de todos los documentos matemáticos y cierres; inspección de sondas cuando certifican signos, identidades o falsadores. |

Los directorios de fase representan los rótulos 0 y 3–101; no existen 1–2 y hay dos directorios con rótulo 44. Esta irregularidad se conserva como parte del registro y no se rellena artificialmente.

Los PDF, imágenes, binarios, cachés y salidas masivas no se interpretaron como pruebas. Se usaron sólo para verificar que un texto no estuviera atribuyendo a una figura o ejecución una conclusión más fuerte que sus datos.

## Unidad de auditoría

Cada afirmación se separó en seis campos:

\[
(\text{objeto},\ \text{hipótesis},\ \text{cuantificadores},\ \text{conclusión},\ \text{evidencia},\ \text{dependencias}).
\]

La etiqueta se asigna a esa sextupla, no al título del archivo ni al nombre `theorem`, `closure`, `QED`, `wall` o `no-go`. El procedimiento evita que una identidad correcta de dimensión finita absorba por asociación un límite no demostrado.

Para todo puente finito–infinito se auditó por separado el orden lógico

\[
\forall N\ \exists X_N
\qquad\text{frente a}\qquad
\exists X\ \forall N,
\]

la dependencia de constantes y la preservación de soporte, conjugación, multiplicidad lineal y signo. La mayoría de las falsas clausuras del corpus ocurre al intercambiar esos cuantificadores o al perder una de esas cuatro informaciones.

## Prueba adversarial H0

Toda ruta que pretenda cerrar \(\Omega_7\) debe exhibir su paso portador de dificultad. Se aplica el siguiente control:

1. sustituir el divisor real por un modelo con un cuarteto fuera de línea;
2. mantener, tanto como sea posible, conductor, simetrías, coeficientes y normalización;
3. localizar la primera afirmación que deja de ser verdadera;
4. exigir una demostración aritmética de esa afirmación que no use el divisor buscado;
5. clasificarla como **FUERZA-RH** si, mediante las transferencias existentes, ya prohíbe el cuarteto.

Si una construcción también funciona sobre el control fuera de línea, es infraestructura o una identidad build-neutral. Si sólo falla después de haber insertado positividad de Weil, real-rootedness, un divisor real o una métrica adaptada a las raíces, es circular. El único candidato legítimo es una propiedad aritmética que falle en el control y cuya prueba no presuponga ese fallo.

## Precedencia documental

Se aplica el orden

\[
\text{corrección con demostración}
\;>\;
\text{ledger final}
\;>\;
\text{cierre explícito}
\;>\;
\text{borrador o resumen}
\;>\;
\text{salida numérica aislada}.
\]

Un rótulo anterior de cierre queda retirado si un documento posterior identifica una hipótesis abierta o un contraejemplo. Si dos versiones discrepan y ninguna resuelve la discrepancia, el estado conservador es **CONDICIONAL** o **ABIERTO**.

## Límites de esta revisión

La revisión determina consistencia interna, alcance de pruebas y duplicaciones dentro del repositorio. No certifica por sí sola prioridad bibliográfica. Antes de declarar una idea novedosa, el reinicio exige una búsqueda separada en fuentes primarias y una comparación por enunciado, hipótesis y mecanismo, no por vocabulario.

El dossier se mantiene deliberadamente muy por debajo de un millón de tokens. La medición exacta y el inventario final quedan en `COVERAGE_INDEX.md`.
