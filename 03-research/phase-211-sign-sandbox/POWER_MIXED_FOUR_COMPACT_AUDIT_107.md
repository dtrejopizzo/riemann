# Auditoría107 — diseño compacto mixto

Estado: **DISEÑO Y LITERALES APROBADOS; ejecución fija INCONCLUSA reproducida independientemente.** Fuente:`POWER_MIXED_FOUR_COMPACT_DESIGN_107.md`. Consultas y diferencia respecto103–106 conservadas; papers intactos. No se garantiza PASS.

## Origen y pago explícito del resto

El nuevo disco lambda<=1/2 corresponde a|t|<3/4, con Rey>3/80. La suma absoluta Phi<2^40 y la cola m>=129<2^-583 son válidas; extraer coeficientes pares del parcial equivale a simetrizarlo, sin fingir paridad del parcial. Los errores de coeficientes se añaden antes de recurrencias. La fuente fija un único jet puntual para a con comprobación de compatibilidad098; I1/I3 permanecen cajas103 y todos sus errores se propagan.

Verificada la fórmula integral de K, incluido el factor(lambda²/2) integral s(1−s)²phi(s²lambda)ds. Produce|J|,|K|<2^42 en el disco. Las recurrencias J_k yK_k incluyen los factores correctos2k y2k(2k−1).

El pago pendiente de§8 se resuelve explícitamente: para N=513, suma n>=N de n4·2^-n es menor que3N4·2^-N, conN4<2^37. Enlambda<=1/4, derivados0..4 del resto deJ/K grado512 son menores que2^(42+8+39−513)=2^-424. ParaPhi el bound es2^-426. En Q=−phi−2lambda phi', Q^(j)=−(2j+1)phi^(j)−2lambda phi^(j+1), j<=3, la suma de costes es menor que8·2^-426<2^-423. Por tanto2^-400 porentrada cubre holgadamente todas estas colas analíticas. Es ADICIONAL al error de coeficientes de modos y de momentos, que la aritmética ya propaga. El determinante se forma enlambda yno se divide un jet incierto por t6.

## Rama restante

La forma A16 con potencia1/4 es exactamente la A16 de106 con potencia5/4 tras cancelar y+v=y(1+v/y); no cambia el objetivo. Cap4 de integrales ycap5 de logTheta pagan derivadas0..3. La columna constante permite el menor3x3 con signo positivo. Escalas Yc fijas no se derivan.

El semiancho inicial1/16 amplía la unión de discos temporales a3/32; al estar esta rama en[1/2,64], permanece dentro de S. Escalas Yc/Y y su cuadrado son menores que2, manteniendo el mayorante Gauss106. Error2^-81·32^j cubre Gauss2^-83·32^j y colas v/modos. La columnaX recibe su error local separado. Se pagan factoriales antes de determinante; bolas de nodos/pesos yredondeo son costes adicionales aritméticos.

## Cobertura y ejecución

Subdivisión determinista izquierda primero con profundidad y número máximo de evaluaciones fijados es legítima: sólo una cobertura completa por hojas con lower>0 certifica el intervalo. Agotar presupuesto daINCONCLUSO; una bola con upper<0 certifica sólo esa celda del objetivo mixto, no W negativo. El algoritmo debe conservar explícitamente las celdas pendientes para no confundir parada parcial con cobertura.

El diseño no es muestreo y no autoriza ajustes tras signos. Falta revisar el código literal, incluida theta origen completa, cuadratura y sus errores antes de formar matrices, y contabilidad exacta de hojas/presupuesto. No se ejecutó ninguna evaluación nueva en esta auditoría.

## Literales origen y REST/main

Leídos completos `tools/power_mixed_four_origin_branch_107.py` y `tools/power_mixed_four_compact_107_verify.py`. No se ejecutaron ni importaron sus funciones theta. Sólo se consultó el docstring local de arb.legendre_p_root, que confirma las bolas de nodos/pesos requeridas.

Origen: a porE regularizada, compatibilidad098 yprecisión correcta;128 modos/cap1025, extracción even512 ycola2^(k−583) ANTESrecurrencias. J/K sonpolinomios derivados; Q usa fórmula exacta, entrytail2^-400, determinantede24permutaciones. DFSleftfirst tiene límitesfijos ycontabilidadexactaFraction de cobertura1/4 antesPASS.

REST:64nodos por10segmentos conpesospositivosysumaqueencierra2. Ningún midpoint eliminaerrores de nodos/expescalars; cacheexp factoriza identidadesexactas. Cap5 deTheta anteslogder controlaXhasta3; cap4 de integrales yramapositivarealcorrectos. ErroresGauss/v/modos seañaden acoeficientesANTESfactoriales/determinante. La expansiónporcolconstante deja menor3x3con signo+. EscalasYc constantes sepropaganintervalarmente. La recursión sóloPASStrasresolverTODASlas hojas de508intervalosiniciales, no alagotarbudget.

Main requierePASSdeorigenantesREST; abortaNEGATIVEoINCONCLUSIVE sinpromovercobertura. Importarloscódigosnoevalúatheta. Ambosliterales aprobadosantescorrida; root coordinaunaprocesoúnico. No se garantiza resultado positivo ni se autoriza modificar parámetros trasdatos.

## Ejecución y reproducción sin modificaciones

Root5594 y mapa46719 terminaron exit2/INCONCLUSIVE. Mismos11 evaluaciones,0 hojas aceptadas, profundidad10 y celda lambda[0,1/65536], determinante[+/−2.94e−3]. REST no arrancó. Logs separados root/audit guardados. Hashes main2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054 yorigin15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553 verificados idénticos.

El código se comportó conforme al diseño: paró sin proclamar cobertura parcial. Un encierro que contiene0 no demuestra signo contrario. La matemática del diseño sigue siendo válida, pero el certificado NO decidió el signo. No se repite ajustando profundidad/precisión ni se infiere imposibilidad global. No hay nuevo resultado W ni obstrucción matemática.
