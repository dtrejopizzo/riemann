# POWER — Intersección Cauchy de coeficientes, diseño109

Estado: CONSTRUCTOR TERMINADO exit2/INCONCLUSO por presupuesto REST. Origen PASS16/16. Sin reproducción independiente de109. No se modifican107 ni108.

## 1. Diferencia y antecedente

Se conserva la consulta las reglas del proyecto, ROUTES-TRIED-INDEX/README, R162_2300_MASTER_GRID y CROSSWORD-TO-D del objeto mixto104–108.107 terminó INCONCLUSIVE al evaluar entradas separadas.108 preservó lambda formando primero el determinante polinómico, pero constructor y reproducción terminaron INCONCLUSIVE tras15 evaluaciones,4 celdas aceptadas, cobertura141/8192; celda fallida[141/8192,1129/65536], profundidad10. La rama restante no se ejecutó. Es un fallo de encierro y no un signo negativo.

109 añade información analítica YA PROBADA sobre coeficientes, sin nuevos puntos ni parámetros theta. La corrida repetirá el builder107 intacto para recuperar sus coeficientes; esa repetición todavía no se ha ejecutado. No se afirma que el exceso de anchura tenga una causa única ni se garantiza PASS. El cambio es intersectar las bolas de coeficientes base con sus cotas Cauchy antes de derivar y multiplicar.

## 2. Cotas y operación exacta

Las funciones completas son holomorfas en un entorno de |lambda|<=1/2 y satisfacen, por107,

 |phi(lambda)|<2^40, |J(lambda)|<2^42, |K(lambda)|<2^42.

Por Cauchy, sus coeficientes verdaderos verifican para todo k>=0

 |phi_k|<=2^(40+k), |J_k|<=2^(42+k), |K_k|<=2^(42+k).

Después de construir las bolas de coeficientes BASE de grado512 por el builder107, incluyendo errores de modos, momentos103 y a, intersectar cada una con el intervalo real simétrico correspondiente. La intersección contiene el coeficiente verdadero porque AMBOS encierros lo contienen. No escoger un punto ni un valor central en lugar de la intersección. Si la intersección es vacía, abortar con estado BUG/INCONCLUSIVE, nunca continuar ni ajustar una cota.

Reconstruir todas las derivadas desde estas bases intersectadas. Construir Q=-phi-2lambda phi' y sus derivadas desde la misma phi intersectada. No se intersectan arbitrariamente resultados intermedios con una cota no probada. Los coeficientes de J y K pueden intersectarse por separado: no se exige ni se supone correlación entre sus errores.

## 3. Presupuesto y corrección sin cambios

Reutilizar108: determinante completo de24 permutaciones como polinomio intervalar, todos los grados hasta2048, traslado Taylor al centro racional de cada celda y pérdida sum_(j>=1)|b_j|h^j. Conservar la corrección independiente2^-200 del determinante debida a las colas de funciones. La intersección sólo estrecha encierros de los mismos coeficientes verdaderos; no altera esa prueba.

Conservar todas las precisiones, modos, caps, dominios, particiones iniciales, profundidad10, máximo8192 evaluaciones por rama y criterio de aceptación107/108. El resto Gauss107 queda intacto y sólo se ejecuta si el origen pasa. No se cambian parámetros ni se eligen según signos observados. El nuevo wrapper comprueba hashes de fuentes reutilizadas antes de calcular.

## 4. Pendientes y alcance

Pendiente auditoría matemática y literal independiente antes de ejecutar109. Root implementa el wrapper; no se modifica código107/108. Un resultado INCONCLUSIVE sigue siendo legítimo. Esta operación no prueba signo por sí misma, no añade cobertura W ni altera la obligación mixta. Su objeto específico es aprovechar un encierro Cauchy uniforme de coeficientes que107/108 aún no imponían a la representación intervalar.

## 5. Estado histórico durante la ejecución, antes del resultado final

Tras aprobación matemática yliteral independientes antesdatos, root inició el constructor52183. Log:`tools/power_mixed_four_cauchy_109_root.log`; driverhash c3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba. Origen Cauchy completo PASS16/16 enlambda[0,1/4]. La ramaREST sigue activa con subdivisión ypresupuestosfijos107. NO hay FULLPASS ni reproducción independiente anunciados.

Los impresos Arb de hojasREST pueden mostrar formas decimales groseras[+/−...] pese al predicado binario value>0; la prueba de aceptación es el predicado intervalar, no inferir ceros del formato decimal. No se modifican códigos/parámetros yno se lanza réplica antes del resultado constructor. Este estado es provisional, sin registro de signo global en índices hasta exit real.

## 6. Resultado final constructor109

Root52183 terminó exit2/INCONCLUSIVE por presupuesto fijo de8192 evaluaciones REST, con4113 hojas aceptadas. El origen pasó16/16celdaslambda[0,1/4]. La siguiente celda REST pendiente era[2645/512,1323/256], profundidad6; no se evaluó tras agotarse el presupuesto. No fue una celda de signo negativo ni una parada por profundidad.

Auditoría del LOG, sin nueva corrida: las4113 hojas aceptadas son contiguas y cubren exactamente REST[1/2,2645/512], longitud2389/512. El resto de[1/2,64] no quedó certificado por esta corrida. El log está en`tools/power_mixed_four_cauchy_109_root.log`, conhashdriver c3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba yhashes107/108intactos. NO se afirma reproducción independiente109.

Resultado final INCONCLUSO, sinFULLPASS,Cheb4global,Ufinito,W/T/allorders niobstrucciónmatemática. La condiciónprevia110(109sinFULLPASS) se cumple, pero otro literal debe auditarse antes de ejecutar esa representación. No se modifican parámetros109ni se reinicia esa corrida.
