# Estado revisado — cuatro generadores y compensación aritmética

Estado: resultados particulares PROVED, signo general OPEN. Goal activo; papers intactos.

## Ronda anterior y progreso de ésta

La ronda004 resolvió todas las ternas a_i>=32 y el puente de aproximación. Esta ronda aporta pruebas verificadas que distinguen tres mecanismos.

1. POWER_CONFLUENT_FOUR_005: sobre exp(-31.5y) por polinomios de grado<=3, ARCH tiene una dirección negativa certificada, pero ARCH+POLAR>49/200 y la forma completa W>1/5 de la norma. No es cuatro tasas arbitrarias.
2. POWER_POLAR_MOVEMENT_005: en esa misma confluencia, para cualquier numerador racional de grado<4, la derivada del Rayleigh de ARCH+POLAR al aumentar un polo es >1/420. Identidad SOS racional y LDL exacto, auditados en POWER_AUDIT_005. Es transporte LOCAL, no global ni signo del término primo.
3. POWER_ARITHMETIC_WITNESS_006: vector Laguerre de dimensión12 con ARCH+POLAR normalizada entre -2/125 y -1/100. Su autocorrelación es exp(-31.5t)Q(63t); todos los coeficientes de Q(x+40) son negativos. Todos los contactos aritméticos ayudan; el de2 aislado repara el déficit. W>norm²/50. Retirar únicamente n=2 (conservando4,8,...) da W<−norm²/125, por cola racional restante<norm²/500. Revisado de modo independiente en POWER_AUDIT_006, incluida expansión directa de autocorrelación sin depender de la identidad Laguerre.

Los tres verificadores exactos fueron reejecutados por coordinación con PASS. No se infiere de estos casos positividad de matrices de orden arbitrario.

## Patrón probado y límite

Tres generadores: domina ARCH. Cuatro confluyentes: se necesita conservar el polar positivo. El test explícito de doce necesita el contacto aritmético2. Esta sucesión muestra compensaciones distintas: no justifica una regla única de inducción. La monotonía de ARCH por covarianza está probada; la extensión a ARCH+POLAR sólo es local en el caso4 y falsa sin restricción de tasas (contraejemplo u1→2).

## Próxima obligación

Controlar la compensación conjunta en una familia densa, no sumar familias positivas por separado. En paralelo se audita un falsificador a la monotonía ARCH+POLAR en orden grande incluso con tasas31.5, usando y^(n−1)exp(-uy); no es todavía resultado de registro aquí. El signo general permanece OPEN y no hay impedimento externo.

## Actualización007 auditada

El falsificador anunciado arriba ya está PROVED en POWER_HIGH_ORDER_PM_NOGO_007, auditado en POWER_AUDIT_007. Afecta la monotonía universal de todos los Rayleigh AP con numerador fijo, no el mínimo espectral ni el signo. No se intentará cerrar todos los órdenes extrapolando la monotonía local4. El trabajo se orienta a la cancelación aritmética conjunta.
