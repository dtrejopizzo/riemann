# Estado041 — Beneficio integrado real en una banda energética móvil

Estado: PROVED y auditado. Sustituye STATE040 como resumen de trabajo. Goal activo, signo global OPEN, papers intactos.

## Resultado sobre una integral aritmética completa

POWER_ENERGY_BAND_041 prueba para TODOS N>=2^80, u=63/2:

    2 int_(exp(T))^(exp(T+L)) h_N(x) B(x) dx < −C_N/25600,
    T=2(N−1)v/(u²−v²), v=1/2+N^(-2), L=sqrt(N)/100,
    C_N=exp(T/2)[rho_N(T)/2−rho_N′(T)]>0.

h_N es el inverso Möbius COMPLETO y B(x)=log(floor(x)!)−xH_floor(x)+floor(x) es el peso REAL con todos sus saltos. La banda se desplaza y crece con N; no se evaluó una lista de órdenes ni se truncó la aritmética.

En la identidad W/norma²=ARCH_sharp−F_N, F_N=2int_1^infinito h_N B, esta banda aporta un beneficio mayor que C_N/25600. El signo de F_N completo y el de W siguen abiertos: falta comparar el complemento, y no se suman beneficios de representaciones distintas sin sus términos de borde.

## Qué cambia respecto de los signos puntuales040

La expansión Fourier040 es uniforme en la traslación. Su factor delta−D se integra sobre un intervalo FINITO, conservando exactamente los bordes. Una caída demostrada del perfil gamma da un beneficio de borde; después se acotan el resto Fourier y la corrección de B. El error es pequeño respecto a C_N, la misma escala de la contribución, y por eso decide el signo de esta integral real.

No se intercambia una integral global con la suma crítica sum|mu(n)|/n, que diverge. Tampoco se pretende que un error pequeño respecto a C_N sea suficiente para decidir W total, cuyo residuo puede ser mucho menor.

Frente030/031, el resultado es una banda MOVIL en la región energética y usa el factor firmado del inverso infinito antes del módulo. No es otra integración por partes sin desigualdad ni un nuevo punto positivo de un núcleo.

## Corrección periódica con bordes controlados

El mismo memo demuestra para TODO x>=1:

    B(x)=−gamma x−B1({x})logx+kappa+E(x),
    kappa=(log(2pi)−1)/2, −1/x<E(x)<1/(2x).

Se incluyen pruebas elementales de los restos de Stirling y de los números armónicos. La parte periódica conserva los saltos logm en enteros, mientras E es continua allí. Una primitiva periódica continua Q2, de norma1/16, produce un bound integrado explícito con bordes, variación de h(x)logx y int|h|/x. Es una herramienta auxiliar sin signo propio; BAND ya se prueba con una cota más gruesa suficiente.

## Evidencia y obligación restante

POWER_ENERGY_AUDIT_041 aprueba BAND y la expansión periódica. Root revisó ambos; el verificador exacto de constantes de BAND fue reproducido por root y auditor: PASS. La expansión periódica tiene prueba analítica autónoma. Papers sin modificaciones.

No hay nueva fila W, combinación arbitraria ni ventana T del Paper47. La cobertura positiva de W permanece la de035 y resultados anteriores. El avance de esta ronda es un beneficio firmado integrado y cuantificado, cuya compensación con el complemento todavía debe resolverse.
