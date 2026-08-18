# Contexto maestro del programa RH

Este directorio congela la revisión integral del programa antes de continuar con \(\Omega_7\). No es una fase nueva y no contiene una afirmación de prueba de RH. Su función es impedir tres errores de investigación: contar una equivalencia como avance, reutilizar una afirmación retirada y volver a recorrer una clase ya cerrada por un no-go.

El dictamen central es:

\[
\mathrm{ARP\!\!-P}\Longleftrightarrow\mathrm{RH}
\Longleftrightarrow
\bigl[J_N(z_0)\succeq0\ \forall N\bigr]
\Longleftrightarrow
\bigl[\lambda_n\ge0\ \forall n\bigr].
\]

Esta cadena es una localización correcta de la dificultad, no una reducción de su fuerza. \(\Omega_7\) continúa abierto. La auditoría también obliga a corregir una afirmación previa más fuerte: no todas las piezas auxiliares anunciadas como cerradas en paper 36 están demostradas con el alcance declarado. En particular, \(\Omega_4\) mezcla dos blanqueamientos con dominios distintos y \(\Omega_5\) demuestra continuidad por orden fijo, pero no positividad incondicional.

Hay además una corrección que cambia el reinicio. Del split exacto \(\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}\), Ω₇ equivale a

\[
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\qquad(n\ge1),
\]

no a \(|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}\). La dominación absoluta es una condición suficiente más fuerte y ni siquiera puede ser la equivalencia declarada en \(n=1\). Por eso el frente recomendado pasa a ser una desigualdad unilateral que preserve la cancelación firmada.

La auditoría corrige también la fórmula que debe iniciar ese frente: la integración por partes impresa cambia el signo y omite el borde \(-n\). Con \(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), la identidad válida es

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

Por tanto ninguna continuación debe reutilizar la versión anterior sin reparación.

## Orden de lectura

1. [`00_SCOPE_AND_METHOD.md`](00_SCOPE_AND_METHOD.md): corpus, protocolo y significado de las etiquetas.
2. `MASTER_CONTEXT.md`: síntesis autocontenida del camino completo y estado matemático actual.
3. `PAPER36_AUDIT.md`: columna lógica, resultados confirmados y reparaciones necesarias.
4. `RH1_RH9_AUDIT.md`: balance de los nueve programas exploratorios.
5. `PHASES_AUDIT.md`: recorrido de todas las fases, sin contar reparametrizaciones como cierres nuevos.
6. `NO_GO_AND_RETRACTIONS.md`: registro de rutas descartadas, alcance exacto y precedencia de correcciones.
7. `LIVE_FRONTIER_AND_RESTART_PLAN.md`: criterio de admisión y plan de reinicio centrado en el paso portador de fuerza-RH.
8. `COVERAGE_INDEX.md`: comprobación de cobertura y tamaño del contexto.

Los archivos en [`fragments/`](fragments/) conservan las auditorías de bloque que sostienen la síntesis. Son evidencia de trazabilidad; ante cualquier discrepancia, prevalece una corrección matemática posterior que exhiba el paso exacto.

## Etiquetas vinculantes

| Etiqueta | Significado |
|---|---|
| **DEMOSTRADO** | La conclusión sigue de las hipótesis escritas. El alcance puede ser finito o restringido. |
| **CONDICIONAL** | Falta probar al menos una hipótesis usada por la conclusión. |
| **NUMÉRICO** | Evidencia para cortes, datos y precisión fijados; no es un límite. |
| **REFUTADO** | El mecanismo concreto falla o contiene un error identificado. |
| **FUERZA-RH** | Probar el enunciado resolvería RH bajo transferencias ya establecidas. No puede usarse como lema auxiliar. |
| **ABIERTO** | El enunciado está bien tipado y aún no tiene demostración ni refutación. |

Una identidad finita demostrada no hereda automáticamente una conclusión cofinal. Una condición de fuerza-RH no es una brecha pequeña. Un no-go sólo cierra la clase de argumentos que sus hipótesis realmente cubren.
