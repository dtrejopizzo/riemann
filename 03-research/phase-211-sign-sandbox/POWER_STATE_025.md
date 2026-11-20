# Estado025 — Balance aritmético integrado completo en el caso hostil129

Estado: PROVED resultados parciales auditados; signo global de W OPEN. Goal activo. Papers intactos. Sustituye STATE023 como resumen vigente e incorpora024/025.

## Avance firmado completo

POWER_INVERSE_LOGCONCAVITY_025 demuestra ERR129<−33/50 para u31.5, con TODOS los enteros de la inversión Möbius y TODA la semirrecta. Se trata del mismo N129 donde K129(1)<0 fue certificado023. La positividad puntual falla, pero no impide este control integrado.

La cadena probada tiene tres pasos independientes:

1. POWER_CELL_TEST_024 certifica la primera celda completa: S129(2)>33/100, con cola Möbius<10^-10 y antiderivado polinómico exacto. También certifica integral_1^2 K C_B>31/100 y una masa ponderada positiva. Son representaciones distintas del mismo balance y NO se suman entre sí.
2. Los cocientes de coeficientes (j+1)c_(j+1)/c_j de D_N=33P_N−P_N' decrecen para TODOS N. Covarianza elemental implica que D_N'/D_N decrece. Un único chequeo racional D129'(2/3)<30D129(2/3) controla todos los desplazamientos logm y la suma Möbius COMPLETA: K129(x)>0 para x>=2.
3. La primitiva J129/x decrece en esa semirrecta y es positiva. Todas las celdas n>=3 tienen S129(n)>0, analíticamente, sin enumeración. ERR=−2sumS y el primer paso dan ERR129<−.66.

Root leyó las pruebas, verificó independientemente los cocientes y ejecutó los certificados Fraction. POWER_CELL_AUDIT_024 y POWER_INVERSE_LOGCONCAVITY_AUDIT_025 aprueban la cadena completa. No se usó cuadratura flotante para estos resultados.

## Lema uniforme y alcance

POWER_CELL_BALANCE_024 proporciona un presupuesto celular que tolera K negativo: S_n=b_nJ(n)+(H_(n−1)/2)integral_cell[1−(n−1)²/t²]K(t)dt, b_n>=.75−log2. De él deriva S_n>=b_nJ(n)−H_(n−1)sup_cellK^-/(2n). Es una cota efectiva, no la afirmación de que su término favorable domine para todos N,n.

La logconcavidad025 vale para TODOS N y puede reutilizarse para reducir una semirrecta a un chequeo de cociente. El chequeo t0=2/3 y el balance completo sólo están certificados para N129; no se extrapolan a toda la tabla.

## Límite exacto frente al objetivo

W[g129]/||g129||²=ARCH_sharp[g129]/||g129||²−ERR129. Falta comparar cuantitativamente el déficit arquimediano con el beneficio demostrado: ERR<−.66 no se declara suficiente. Esta ronda no añade un signo de W ni una ventana nueva T.

La cobertura previa de W permanece: filas N1,2,3 para todo k, cono k>=10000N², ocho polos arbitrarios y bloque fijo12. El puente escalar017 exige completar TODOS N,k. Los contraejemplos auxiliares022/023 permanecen válidos; se superó su hipótesis puntual en este caso mediante integración, sin borrar las regiones adversas.

## Continuación

Buscar un balance conjunto con ARCH_sharp que conserve cancelaciones y una extensión analítica del mecanismo integrado a órdenes variables. No convertir el resultado ERR en positividad de W, no relanzar K>=0 universal ya refutado y no sustituir el paso universal por una campaña de certificados aislados. Goal activo, sin cierre global ni bloqueo externo.
