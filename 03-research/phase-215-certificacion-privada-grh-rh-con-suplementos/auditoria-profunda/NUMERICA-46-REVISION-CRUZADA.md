# Revisión cruzada independiente del certificado en T₅

Se revisaron `reconstruir_matriz_46.py`, `verificar_inercias_46.py` y `verificar_restos_46.py`, cotejándolos con P46:1630–1782. Los valores de corte T se toman fijados; esta auditoría trata las cotas certificadas y no busca otros cortes.

## Normalización y cajas

La matriz integra en [0,240] con factor2T/π. La aplicación del nodo es `τ=panel/2+(node+1)/4`; por ello el peso lleva1/4, y480 paneles cubren exactamente el intervalo. Se consultó la documentación de la instalación de python-flint: `legendre_p_root(46,k,weight=True)` devuelve los46 ceros, en orden decreciente, con los pesos de Gauss para(−1,1). El orden no afecta la suma.

La escala `sqrt(2n+1)(−1)^floor(n/2)` reproduce el signo `(-1)^((l−i)/2)` cuando i,l tienen la misma paridad. Las matrices165×140 corresponden a grados<330 contra grados<280, por separado en cada paridad. Los resets de Bessel reemplazan dos valores consecutivos por evaluaciones Arb y conservan la recurrencia; ningún nodo es0, de modo que las divisiones por x son legítimas. La suma y el producto de matrices son de bolas, y la serialización210 dígitos retiene un radio explícito.

El vectorχ usa `i_n(T/2)=sqrt(π/(2x)) I_(n+1/2)(x)`, x=T/2. Sus normas totales son exactamente `sinhT+T` en par y `sinhT−T` en impar. Los índices del sumatorio140:165 son precisamente el tramo280≤grado<330. Las cajas de las colas de Gram son `tail²` y las de los términos cruzados `tail·||χ_tail||`, por Cauchy–Schwarz. La sustitución exclusiva de la entrada final por `c−upper(||P_Yχ||²/q_Y)` produce efectivamente R'≤R; no se interpreta una resta entrada por entrada arbitraria como orden de formas.

Una precisión expositiva: P46:1765 escribe `c_*=193.13`, que es un redondeo hacia abajo de240T=193.132549… . No debe utilizarse193.13 como cota superior en las colas. Los scripts usan240T como bola y sus predicados conservan las cotas4.5e−20 y3.9e−70.

## Resto analítico

La identidad integral de j_n y `∫_{−1}^1 P_n²=2/(2n+1)` dan
`sqrt(2n+1)|j_n(z)|≤exp|Imz|` por Cauchy–Schwarz. Esta versión normalizada es la que controla las entradas de matriz sin introducir factores crecientes en n.

Para un panel de longitud1/2 yρ=3.2 la semialtura es `(ρ−ρ^-1)/8=.3609375`, menor que la distancia1/2 a los polos de digamma. En la recurrencia a w+8 queda Re(w)>0 y Re(w+8)>8. Las cotas de los ocho inversos, la parte digamma desplazada, logπ y los cosenos dan |g|<34. El producto Bessel normalizado es<2, así que M=70 es válido.

Gauss46 es exacta hasta grado91. Los coeficientes de Chebyshev satisfacen |a_k|≤2Mρ^-k, la diferencia entre integral y cuadratura de T_k tiene módulo≤4 y es0 para k impar. Por tanto el resto por panel estándar es≤`8Mρ^-92/(1−ρ^-2)`. Multiplicar por480,1/4 y2T/π da un resto<2e−42 por entrada. Esto no reproduce la cifra más fina1.5e−43 del manuscrito; sí certifica la caja conservadora2e−42 efectivamente añadida por el script.

Ejecutado `verificar_restos_46.py`: resto1.28151474598754e−42, Λ280≤4.40516113423683e−20, Λ330≤3.86274619398775e−70. Todos los predicados Arb pasan.

## Inercia: primera ejecución y obligación pendiente

La primera ejecución independiente de `verificar_inercias_46.py` pasó los dos casos primitivos y el caso completo impar. El caso completo par, μ=1e−18,c=−1/2, no quedó certificado: en el complemento de Schur del bloque fijo la eliminación intervalar llegó al pivote83 con bola[±2.48]. Esto es **(c) para esa implementación**, no un contraejemplo al signo de la forma. Los demás pivotes mínimos fueron0.00846658,0.02026832 y8.14424e−14.

Se notificó el resultado al frente principal; éste está reconstruyendo un precondicionamiento por LDL de puntos medios seguido de una comprobación Arb de la forma congruente. No debe comunicarse éxito de los cuatro certificados basándose en la primera ejecución. La revisión posterior de esa reparación se añadirá aquí cuando exista evidencia ejecutada.

## Cierre posterior: cuatro inercias certificadas

Se leyó y ejecutó independientemente la versión corregida con `preconditioned_positive`. Los cuatro casos pasan. En el completo par se certifica primero la invertibilidad de la congruencia Householder mediante `||HᵀH−I||∞<1`; el bloque binario tiene determinante<0. La eliminación intervalar directa sigue agotándose en índice83, pero ya no se usa como certificado.

El nuevo precondicionamiento toma entradas **puntuales** de una factorización aproximada: L es unitriangular con entradas diádicas exactas y D tiene diagonales puntuales estrictamente positivas. No se presupone que M=LDLᵀ exactamente. Se define la matriz invertible `P=D^-1/2 L^-1`, se calcula una bola para `PMPᵀ` usando M completo con sus radios y se comprueba diagonal dominante positiva por Gershgorin. Esta prueba es válida para la matriz exacta encerrada; su independencia respecto de la exactitud de la factorización aproximada evita el problema de dependencia intervalar.

La ejecución cruzada obtuvo, en el completo par:

- determinante binario≈−0.0425472158049231;
- mínimo pivote de la factorización aproximada≈0.000447307564344;
- margen de Gershgorin certificado>0.999999999999999999999969;
- `ok:true` en los cuatro casos.

**Dictamen final de esta reconstrucción: (a)** para las cotas solicitadas en T₅ y su extensión a ventanas menores mediante la monotonía declarada. El resto2e−42, las colas y las normalizaciones fueron comprobados arriba. El certificado reconstruido usa precondicionamiento y Gershgorin para el caso par completo: no debe describirse como una reproducción literal exitosa de la eliminación Cholesky intervalar simple. La cifra más fina de resto1.5e−43 y las columnas «fails at» de la tabla no se certifican por este trabajo; no son necesarias para las cotas inferiores que sí quedaron demostradas.
