# Propuesta: casos de mezclas con cancelación

Estado: OPEN, apoyada en un caso PROVED. Tres revisiones independientes y coordinación. Papers intactos.

## Resultado

POWER_CONE_001 demuestra positividad exterior en cada plano de dos potencias X^{-a},X^{-b}, a,b>=32, con coeficientes reales arbitrarios. No demuestra positividad en su envolvente ni admisibilidad PW_N. Prueba revisada independientemente.

## Novedad

No hallamos el lema específico a>=32 en búsquedas dirigidas del corpus, índice, grid y crucigrama. La familia general Pick y la eliminación matricial tienen antecedentes: NO se afirma una vía global nunca intentada. Algunos índices de semillas están desactualizados respecto de fases posteriores. La diferencia concreta es el caso positivo con constante explícita y el falsificador del paso de diagonales a mezclas.

## Siguiente experimento matemático

Definir u_i=a_i-1/2, K_ij=(L(a_i)+L(a_j))/(u_i+u_j), r_ij=K_ij/sqrt(K_ii K_jj), con L real explícita en POWER_CONE_001. El objetivo primero es demostrar o refutar, para a_i=A+(i-1)h, A>=32,h>0,

    (r_23-r_12 r_13)^2 <= (1-r_12^2)(1-r_13^2).   (P3)

Es exactamente el determinante de tres puntos. Investigar h pequeño mediante derivadas de L, luego h=A y después h general. Buscar restos de signo en las series reales de digamma y Σ Lambda(n)n^{-a}, conservando cancelaciones. Si falla, extraer vector negativo: sólo sería contraejemplo exterior; verificar admisibilidad antes de atribuir consecuencias al paper.

Si se prueba, seguir con triples desiguales y cuatro generadores. La meta sería una regla uniforme que controle los residuos tras eliminar un generador. La eliminación es conocida; la desigualdad aritmética que preservaría el signo NO está construida. No extrapolar casos finitos a todos los órdenes.

Segundo requisito independiente: puente hacia las colas admisibles PW_N módulo gauge en NORMA DE LA FORMA. Densidad L² sola no basta. Sin todos los órdenes y ese puente no hay cierre.

## Falsificadores y decisión

H(u)=3+cosh u es positiva, par y logconvexa, pero el kernel en log2,2log2 tiene valor -129/(34 log2) sobre (42,-41). Esto refuta el argumento genérico theta, no el dato aritmético.

NEAR_CASES_RESULTS_2026_11_04 documenta una mejora auxiliar nearfree y refuta monotonía al agregar contactos y la supuesta contribución favorable automática del ciclo (2,2,4). No refuta el signo total.

Recomiendo la escalera de potencias como experimento nuevo en su detalle porque ya produce un teorema y una obstrucción exacta. No hay evidencia suficiente para llamarla mecanismo de cierre; el signo global sigue abierto.
