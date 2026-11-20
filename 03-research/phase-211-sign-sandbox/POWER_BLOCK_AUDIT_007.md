# POWER_BLOCK_AUDIT_007 — Auditoría de signo en el bloque completo Laguerre12

Estado: PROVED. Revisión independiente de POWER_ARITHMETIC_BLOCK_007.md y tools/power_arithmetic_block_007_verify.py; ejecución del script con salida PASS. Papers intactos.

## 1. Fórmulas y factores del contacto

La norma de coordenadas en la base Laguerre es la norma L². Las bandas arquimediana y polar coinciden con las fórmulas auditadas en rondas004–006. La autocorrelación de un vector real suma cada pareja triangular una sola vez, mientras una matriz simétrica cuenta dos veces cada pareja fuera de diagonal. Esto explica exactamente a0(n)=-2Lambda(n)n^-32 y ak(n)=-Lambda(n)n^-32 qk(63logn), k>=1. El script usa esos dos factores diferentes tanto para el contacto2 como para los majorantes de cola. No presupone positividad de una matriz individual de contacto.

## 2. Euler–Maclaurin y las bandas intervalares

Las sumas finitas para S_p llegan de16 a255, y la cola comienza en256. Para p2..12, las cotas dadas por T_p y T_p menos el término cúbico son correctas con las direcciones declaradas. Una justificación directa de su resto de signo es escribir la cola como integral Laplace de e^(-Mt)/(1-e^-t). Las desigualdades globales

    1/t+1/2+t/12-t³/720 < 1/(1-e^-t) < 1/t+1/2+t/12

se obtienen expandiendo los denominadores positivos de la fracción parcial de coth(t/2), con un resto positivo después de cada truncación. Integrar contra t^(p-1)e^(-Mt)/Gamma(p) produce exactamente los factoriales ascendentes p y p(p+1)(p+2) usados. Es válida para todo p>1, no sólo para un régimen asintótico.

El intervalo de gamma en M256 tiene los signos correctos: se retienen hasta -1/(120M^4), y el resto está entre0 y1/(252M^6). Machin con treinta términos alternados y las series atanh de log tienen colas correctas. Los intervalos se forman íntegramente con Fraction y no hay redondeo flotante oculto. El signo de cada coeficiente al combinar bandas y polygamma está correctamente conservado.

Para qk(63log2), se usan intervalos de potencias positivas de log2 y multiplicación intervalar completa; las sumas con coeficientes alternados toman los extremos pertinentes. El contacto2 incluye su factor Lambda(2)=log2 mediante una multiplicación intervalar separada.

## 3. Centro racional y matriz de doce dimensiones

Cada centro es el punto medio racional intervalar redondeado hacia abajo a denominador10^12. El error de cada banda se toma como máximo de sus distancias a ambos extremos: el desplazamiento del redondeo está incluido. La suma de error por fila usa todas las bandas Toeplitz y el máximo sobre las doce filas; su valor está certificado <10^-8.

La eliminación LDL exacta del centro menos1/1250 veces la identidad tiene doce pivotes positivos. El bucle que actualiza todo el cuadrado restante es seguro: ninguna entrada de la columna o fila del pivote k se modifica mientras i,j>k. Las entradas simétricas se recalculan por separado desde el mismo valor inicial y los mismos factores inalterados. Así ARCH+POLAR+contacto2>(1/1250-10^-8)I.

## 4. Cola completa en norma de operador

La prueba de signos de qk(x+40) se ejecuta para todos k0..11, incluido k0, cuyo único coeficiente es1. La propiedad (-1)^k a_kj>=0 implica que, para x>=40, la suma de valores absolutos de sus monomios trasladados coincide con |qk(x)|. Por ello no se pierde su cancelación anterior al desplazamiento y no se asigna signo matricial favorable a la cola.

Para t=logx>log3>1, la derivada logarítmica de f_j es menor que1+693/23-32<0 para j<=11, de modo que la suma desde3 está acotada por el primer término más la integral. La sustitución t=log3+z deja los coeficientes de (a+z)[63(a+z)-40]^j. La fórmula de R_jr usada por el script es exactamente su expansión binomial, y todos esos coeficientes son no negativos y crecientes en a>40/63. Reemplazar log3 por11/10 preserva el majorante. Cada integral de z^r e^-31z es r!/31^(r+1), explicando el factor3^-31.

Se usa Lambda(n)<=logn para TODOS los enteros n>=3: el majorante incluye potencias de2 y cualquier contacto más allá de1024 sin truncar. La suma de bandas absolutas t_k produce un máximo de fila <3/5000. Para la matriz simétrica esto controla la norma de operador de TODA la cola, independientemente de sus signos y términos cruzados. La convergencia absoluta de esas sumas también queda demostrada por el majorante.

## 5. Conclusión y alcance

Restar la norma de la cola da estrictamente

    W|V12 > (1/1250-10^-8-3/5000)I > (1/10000)I.

Este resultado comprende todos los vectores del bloque y todos los contactos. El test de WITNESS006 pertenece al bloque y tiene ARCH+POLAR negativa; el avance sí verifica compensación aritmética dentro de una región previamente indefinida. No se deduce positividad al añadir modos, en otros conjuntos arbitrarios de doce tasas ni sobre todo el dominio de ventana. El siguiente paso requiere un principio o un certificado adicional.
