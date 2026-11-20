# Estado017 — puente escalar suficiente y positividad conjunta

Estado: resultados parciales PROVED con revisión independiente; signo global OPEN. Goal activo. Papers intactos. Sustituye STATE016 como resumen vigente.

## Qué se necesita ahora para cerrar el signo

POWER_SCALAR_BRIDGE_017 demuestra que basta probar W[h_(N,k)]>=0 para TODOS los enteros N>=1,k>=0, con H_(N,k)=s^k/(s+u)^(N+k) y una tasa fija u=63/2. Esta tabla escalar controla todos los términos cruzados de los bloques completos: la densidad de cualquier numerador es un peso base por un polinomio R(q)>=0 en[0,1]. R+epsilon tiene una expansión Bernstein exacta de grado elevado con coeficientes positivos. La identidad racional de densidades conserva el polar al evaluar x=-1/4, además de cada contacto y su suma completa. Pasar epsilon a0 prueba la suficiencia. El puente fuerte014 conecta entonces con los datos del Paper47.

No se infiere positividad de una envolvente lineal desde una unión de tests. La representación es cónica en densidades e incluye todos los cruces. La elevación de grado es elemental y efectiva; el grado puede crecer al disminuir epsilon. Prueba revisada por mapa y signo.

## Regiones de la tabla ya controladas

POWER_INTERIOR_017: para N=1, TODOS k>=0 y TODAS u>=63/2, W>4norma²/3. No queda umbral inicial desconocido en esta fila. Nuevo control uniforme por coeficientes binomiales de la norma ponderada, monotonía sólo arquimediana, polar completo y peine infinito acotados. Verificador racional reproducido PASS. Su §7 da una cota efectiva por cada fila N, uniforme en todos k, sin afirmar signo de todas las filas.

POWER_QUADRATIC_017: para cada c>0, W>0 para P1 en TODOS k>=cN² cuando N>=N0(c), con N0 explícitamente acotable. La herramienta desplaza la DENSIDAD racional completa a Imz=1 y prueba una cota L1 uniforme. Produce |correlación(t)|<=C(c)e^(-|t|) y controla TODO el peine. Evita la separación de pesos temporales falsificada016. También prueba una aproximación del peine completo por una serie gaussiana modulada absolutamente convergente; no presupone signo de esa serie. Revisado independientemente por root y signo; auditoría consolidada en POWER_INTERIOR_AUDIT_017.

POWER_QUADRATIC_EXPLICIT_017 prueba W>49norma²/50 para TODOS N>=2,k>=10000N², a tasa31.5, mediante desplazamiento15 de la densidad. La autocorrelación está acotada por5e^(-15|t|), de modo que peine y polar cuestan menos de1/1000 cada uno y ARCH>99/100. Root revisó la prueba completa y reprodujo el verificador racional PASS. Mapa y signo también aprobaron la extensión: POWER_INTERIOR_AUDIT_017 §9 y POWER_QUADRATIC_EXPLICIT_AUDIT_017. Es un cono explícito sin umbral dimensional desconocido.

## Resultados anteriores vigentes

Ocho polos arbitrarios>=31.5: W>norma²/1000. Bloque fijo de dimensión12: certificado separado. Todos los bloques de una tasa bastan por continuidad fuerte, sin margen uniforme. Teorema015 de cola para cada dimensión fija válido. Las obstrucciones016 a densidad de colas y uniformización de pesos temporales permanecen: el argumento nuevo conserva el producto de factores de la densidad antes de tomar el valor absoluto.

## Límite y obligación restante

La tabla completa todavía NO está probada. Faltan sus regiones inferiores y las interacciones aritméticas en el régimen donde ambos índices crecen sin entrar en el cono positivo controlado. Una fila infinita o un cono no sustituyen toda la tabla. No hay contraejemplo a W.

Ninguno de estos resultados certifica por sí solo una nueva ventana T>log(5)/2: son teoremas sobre familias de tests. La suficiencia global aparece sólo si se completa la tabla escalar o se encuentra otro argumento que cubra todos los datos. No confundir exponentes, índices o dimensión con el ancho T.
