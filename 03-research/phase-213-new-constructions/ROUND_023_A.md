# Coste de tomar valores absolutos entre dos bandas

Cotejo previo independiente con BUILD084 (18), 213-022, el descarte de la familia lacunaria en el índice y 212 ROUND095_A. Aquí se examina exclusivamente la dominación término a término que permitiría sumar los presupuestos de 022. El ejemplo usa la matriz física completa y vectores con ambos momentos nulos en cada banda.

Tomar las bandas enteras [12,24), [12R,24R), R entero grande. En la primera elegir un vector unitario u soportado en 12,13,14 y ortogonal a 1 y l_j=log(1+1/j). Se tiene |u₁₂|>0 porque l₁₃≠l₁₄. En la segunda dividir en los tres intervalos consecutivos de longitud 4R. Para los valores constantes de w en ellos elegir un vector fijo de tres coeficientes ortogonal a (1,1,1) y a (log(16/12),log(20/16),log(24/20)). El telescopaje de l_j da exactamente ambos momentos. Normalizar en norma euclidiana sobre las celdas: en el primer intervalo |w_j|=c/√R, c>0 independiente de R, porque los últimos dos logaritmos difieren.

Para R<n≤(6/5)R las n celdas j=12n,...,13n−1 están enteramente en [12R,16R). En cada una la entrada aritmética de la fila 12 incluye Λ(n)/n; el término arquimediano fuera de diagonal tiene el mismo signo en M. Al sumar, aun cuando distintos n visiten una celda, sus pesos se añaden. Por consiguiente

    Σ_{i,j}|u_i M_ij w_j| ≥ c|u₁₂| R^(−1/2) Σ_{R<n≤6R/5} Λ(n) ≫ √R,

por el teorema de los números primos. Cada norma es uno. Los presupuestos D de 022 de estas dos bandas son O(1) y O(log R); el crecimiento obtenido excede incluso su suma. Por tanto no existe constante uniforme para pagar el cruce absoluto por la suma de los presupuestos cuadráticos locales D₁||u||²+D₂||w||², aun imponiendo los dos momentos por separado.

La desigualdad inferior se refiere a la suma de módulos de los sumandos, antes de toda cancelación. Deja abierta una estimación del cruce firmado y una estimación específica para los residuos aritméticos adaptativos de 022. PROVED tras auditoría matemática independiente.
