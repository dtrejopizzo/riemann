# POWER CRITICAL AUDIT 040

Estado: CRITICAL_BALANCE040 completo y verificador APROBADOS. Papers intactos.

## 1. Corpus y diferencia

Reconsultados índice, grid y crucigrama y los antecedentes020/038/039. El principal del producto Euler y las fórmulas floor son clásicos. La diferencia040 es una expansión con RESTO ABSOLUTO explícito antes de invertir Fourier, pequeña respecto de la escala1/N del inverso completo. No usa una serie formal ni los momentos divergentesA_sigma,B_sigma como si siguieran controlados cuando delta baja aN^−2.

## 2. Factor local e inversión completa — APROBADOS

Leído `POWER_CRITICAL_BALANCE_040.md` íntegro. La identidad floor para zeta(1+z) yH(0)=γ conserva los extremos. En Re z≥0, la comparación deI(z) conI(0) tiene módulo≤|z| yH−γ=−(I−I0)−zI(z), dando2|z|. Las cotas|H|≤17/8 y|zH|≤17/64 controlan el denominador geométrico. La expresión explícitaR3=−z²(H−γ)+z³H²/(1+zH) da el factor9 sin recurrir a una serie sin resto.

El producto inverso completo se mantiene en sigma1+delta>1, absolutamente convergente. La transformada uniforme039 y su normalización gamma original son aplicables. El multiplicadorz=delta−iξ invierte exactamenteδf−f′ yδ²f−2δf′+f″, con signos correctos.

En la banda|ξ|≤1/16,|z|≤1/8 y|z|³≤2(δ³+|ξ|³). Los momentos gaussianos producen288δ³ y9·10^6/N^(3/2). Fuera de la banda, el multiplicador total se domina por(4/δ)(1+ξ²); reservarN/4≥6 controla la integral y extraeexp(−N/10^6). Los cuatro monomios auxiliares suman108692<110000; los factores√N/2 y2π dejan el coeficiente110000√N/δ. No falta la cola ni se elimina la condiciónδ>0.

## 3. Curvatura y signos de escala1/N — APROBADOS

Con los pesos positivos deP, t²q′=EJ−VarJ<d. ParaS=q″+2q′/t, en todo ceroS′=2q′[q′−(2d+1)/t²]<0. La expansión algebraica deP daS>0 al infinito, por lo que no puede haber un valor no positivo anterior. Así−2q′/t<q″<0 y las dos cotas SLOPE son válidas.

La diferenciación directa de f da las fórmulas exactas de f′ y f″. En deltaN^−2, q<2, eta≤1/u² y t_v≥N/(2·992). El lower de f″ tiene3970/N=3968/N del término curvatura más2/N del término cuadrático. El lower específico de f′ parac1/2 usa1/(1+δ+epsilon)≥1−2/N. SLOPE da b>50/N con las cotas holgadas declaradas.

Para N≥2^80, multiplicar REMAINDER porN y usar el sexto término positivo de la exponencial demuestra error<10^−4/N. En c3/2, el margen(γ−1/2)b deja>3.5/N antes de errores; se conserva el costo negativoγδ². En c1/2, el upper tiene coeficiente de b menor que−.39, dejando margen negativo mucho mayor que1/N. Quedan aprobados h/H<−1/N yK/G>1/N en el centro inclinado indicado, sobre sus sumas COMPLETAS.

## 4. Alcance

Son signos opuestos reales del inverso completo cerca del centro energético, no W negativo ni positivo. El hombro039 y estas cotas no controlan la integral interior ni compensan ARCH_sharp por sí solos. No hay nueva fila o ventana T. Root coincide independientemente en todos los pasos analíticos; el verificador final se registra a continuación.


## 5. Corte a distancia constante — APROBADO

Leída§8 final y ejecutado independientemente `tools/power_critical_balance_040_verify.py`: PASS para núcleo y corolario. En TODOdelta∈[2000/N,1000/√N], las identidades exactas dan0<f′<b y f″<−b porquev<1,q<2; no se extrapolan sin justificación los bounds específicos de deltaN^−2. Con0<γ<1, el principal se acota porδ−b−δ².

El término cúbico es<.001δ; los otros dos errores son cada uno<10^−4/N. Para la cola, el boundδ^−1≤N/2000 y el sexto término de la exponencial producen exactamente55·6!·10^36/N^(7/2) tras multiplicar porN. Ademásδ²<.001δ. El lower resultante(.998)δ−(u²+.0002)/N es estrictamente positivo en todo el intervalo, con las constantes comprobadas racionalmente.

La monotonía v→t_v cubre todo el intervalo de centros y su extremo superior coincide con el comienzo del hombro039; por tanto se controla TODA la cola posterior. La diferencia exacta del primer centro respecto d/992 es dδ0(1985+δ0)/(992a_v)<5. Queda aprobado h_N(e^t)>0 yK_N(e^t)>0 para TODOt≥(N−1)/992+5 y TODOSN≥2^80. Es un corte suficiente, no una localización exacta de la transición.

El resultado mejora O(√N)039 a distancia constante para los mismos inversos completos. Los signos centrales opuestos y este corte no se convierten en un signo de la forma W, del emparejamiento interior ni de una ventana T. No hay edición de papers ni uso de argumentos de ceros/equivalencias.
