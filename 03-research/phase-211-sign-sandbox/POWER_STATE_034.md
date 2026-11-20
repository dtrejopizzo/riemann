# Estado034 — Filas completas hasta12 a tasa fija y oscilación del criterio de Abel

Estado: dos resultados PROVED y auditados. Sustituye STATE033. Goal activo, signo global OPEN, papers intactos.

## Nueva región uniforme de positividad de W completo

POWER_DIVISOR_COMPARISON_034 demuestra para TODOS enteros N>=3,k>=1 y tasas u>=63/2 con u²>=225N/4:

    W[f_(N,k,u)] > ||f_(N,k,u)||²/40,
    F_(N,k,u)(s)=s^k/(s+u)^(N+k).

Para k>=2 el margen es mayor que3/20. En k1 se conserva el peine favorable019 y se prueba ARCH−|polar|>.026; cada comparador inferior impar033 es positivo. Desde k2, el incremento beta de ARCH permite pagar un bound absoluto de TODO el peine mediante los dos pesos opuestos029. No se extrapola el signo del peine de k1 a otras columnas.

La prueba es analítica uniforme, no un barrido de N,k,u. La contracción033 no es la responsable de compensar un ARCH negativo en esta región: aquí ARCH−|polar| ya es positivo. El caso211 de032 conserva su prueba separada con cancelación mucho más fina.

## Cobertura exacta al combinar fuentes anteriores

A tasa FIJA u0=63/2, la condición nueva alcanza TODOS N<=17 y k>=1. Para k0,N<=12, el dato g_N=y^(N−1)e^-u0y/(N−1)! pertenece al bloque V12 probado en ARITHMETIC_BLOCK007. Por tanto quedan completas TODAS las filas N1..12 para TODO k>=0 a u0. Para N13..17 queda pendiente sólo k0.

Para TODAS las tasas u>=u0, k0,N<=8 pertenece al espacio de ocho polos repetidos de SIGNED_TRANSFER014; junto a la nueva región quedan completas las filas N1..8 para TODO k>=0 y TODO u>=u0. No se extiende el certificado fijo V12 a tasas variables en N9..12.

Estos enunciados se refieren a los átomos escalares indicados. No certifican arbitrarias combinaciones lineales de todos los nuevos átomos ni una ventana T. Los bloques de formas cuadráticas ya probados007/014 mantienen su alcance propio.

## Criterio de Abel033 refutado uniformemente

POWER_WEIGHTED_COEFFICIENT_034 demuestra que la sucesión real T_m de033 tiene términos estrictamente positivos y negativos en índices arbitrariamente grandes. No sólo falla la premisa T_m>=0 para todo m: tampoco basta exceptuar un número finito de índices.

La demostración no calcula nuevos m. Usa la representación real cosh positiva ya auditada001 para prolongar el funcional exponencial E(v) de forma real-analítica y obtener su paridad. El generador F(z)=sum T_m z^(m−1) es simétrico alrededor de1 y decae cuando z real tiende a infinito. Un lema elemental de series positivas, demostrado en el texto, muestra que coeficientes eventualmente de un signo obligarían a que la serie fuera entera. Una derivada impar en1 por encima de las excepciones forzaría entonces una cola nula, convirtiendo F en un polinomio; el decaimiento contradice F(0)=T1>1/8.

Ésta es una refutación del criterio suficiente específico, no un contraejemplo a W. La mezcla gamma exacta de033 sigue válida: sus pesos pueden compensar los signos de T_m. No se declara imposible controlar esas combinaciones por otro mecanismo.

## Evidencia y obligación restante

POWER_COMPARISON_AUDIT_034 aprueba ambos memos, la extensión a k>=2 y las inclusiones de espacios007/014. Root revisó ambas pruebas y reprodujo el verificador racional de la región: PASS. La oscilación se demuestra analíticamente, sin certificado numérico de índices ni hipótesis no probadas sobre la serie en1.

A u31.5, fuera del cono k>=10000N² y del átomo211,k1 ya decidido, resta k0 paraN>=13 y, desdeN18, las columnas inferiores al cono no cubiertas. No hay cierre del signo global ni nueva ventana T certificada. La continuación debe conservar la compensación aritmética de los pesos reales; no reintentar positividad componente a componente de T_m, ahora refutada.
