# Estado030 — Compensación de un bloque interior a tasa fija

Estado: resultados parciales PROVED y auditados. Sustituye STATE029. Goal activo, signo global OPEN, papers intactos.

## Bloque aritmético real, uniforme en órdenes grandes

POWER_INTERIOR_SCALE_030 transforma exactamente la representación conjunta, mediante inversión de divisores, en

    W[g_N]/norma² = int_1^infinito G_N(x) H(x)dx,
    G_N=x^-1/2[(3/2)rho_N(logx)−rho_N'(logx)]>0,
    H(x)=1+[log((x+1)/(x−1))−gamma−log(4pi)−1
                            −2sum_(q<=x)qLambda(q)]/x².

Se cancelan las singularidades logarítmicas en enteros mayores que1, conservando los saltos aritméticos reales. La identidad sola no da signo.

A u=63/2 FIJO se demuestra, para TODOS N>=2^20,

    int_1^(9/4) G_N(x)H(x)dx >1/100.

El bloque contiene el contacto2 adverso. La comparación local con G_*=(3/2)x^-1/2 tiene error<=7M2/4, M2=u²/(2N−3). La integral principal se calcula exactamente, incluye Lambda(2), y supera1/50; el error integrado es<1/200. No se evalúa una campaña de órdenes. El resto desde9/4 hasta infinito sigue sin control de signo: no se afirma positividad de W total.

También se demuestra que las primitivas ordinaria y ponderada por x² de H hasta5/2 son negativas. La monotonía real de G_N a órdenes grandes no basta para el criterio de primitivas positivas. El bloque favorable se prueba usando su magnitud real, no suponiendo esa premisa falsa.

## Comparación gamma–gaussiana con coste explícito

POWER_GAMMA_BALANCE_030 demuestra para TODOS N>=2 a tasa fija

    0<A_sharp(EV)−ARCH_sharp[g_N]/norma²
      <=.5[psi(N−.5)−log(N−1.5)]<1/[2(N−1.5)].

El peso de resto L_N es el de la ley inversa gamma real. Su momento int L_N/a² se calcula exactamente, y K_sharp<=1/t controla la curvatura negativa. Es una estimación constructiva O(1/N), válida incluso en N2 sin varianza finita de V.

La comparación de las formas COMPLETAS sin coste es falsa en la ley real N2: Wgamma/norma²<.85 y G_W(EV)>.875, de modo que el gap integrado es<−1/40. Esto no significa W negativo: esa fila ya tiene positividad probada. Falta compensar la fluctuación aritmética firmada junto a la pérdida sharp; la comparación gaussiana sola no la decide.

## Evidencia y obligación restante

POWER_INTERIOR_AUDIT_030 aprueba ambos memos, incluidos inversión/Fubini, primitiva exacta J, contacto2, límites uniformes y comparación gaussiana. Root leyó las pruebas y reprodujo los dos verificadores exactos: PASS. Las demostraciones proporcionan la uniformidad en N; los scripts certifican constantes.

No hay nueva cobertura de W total ni ventana T. A u31.5 permanecen filas N1..5 para todo k y cono k>=10000N²; resta N>=6 debajo del cono. Las regiones029 de tasas crecientes siguen válidas con su límite de puente explícito. No se puede sumar una cola de otra representación sin contabilidad de sus fronteras.

La siguiente obligación es controlar el resto del emparejamiento G_N H a tasa fija o la diferencia aritmética en la comparación gamma–gaussiana. El bloque integrado favorable y el coste sharp son herramientas concretas; ninguno sustituye esa obligación.
