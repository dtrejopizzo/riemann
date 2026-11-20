# Estado de registro — compensación aritmética de un bloque completo

Estado: PROVED casos indicados; signo global OPEN. Goal activo. Ningún paper modificado.

## Progreso verificado de la ronda

POWER_ARITHMETIC_BLOCK_007 y POWER_BLOCK_AUDIT_007 prueban W[h]>||h||²/10000 sobre TODO V12=exp(-31.5y) por polinomios de grado<=11 (extensión cero a y<=0). Incluye todos los cruces y toda la cola prima; no es sólo el vector escogido en006. Certificado racional exacto reejecutado por constructor, coordinación y auditor: AP+contacto2>.0008 menos1e−8, cola en norma<.0006. El test006 pertenece a este bloque y tiene AP negativa; la prueba atraviesa una región donde la contribución aritmética es necesaria.

Resultados acumulados válidos: todas las ternas a_i>=32 con margen1/20 (004); confluencia4 con margen1/5 y transporte AP local de todos numeradores (005); escalera fija32..37 certificada (003); puente de aproximación en norma de forma (002). Nada de esto se extrapola a todos los órdenes.

## Dos patrones falsos descartados con pruebas

- POWER_HIGH_ORDER_PM_NOGO_007: a tasa31.5 y n=2^17, el Rayleigh AP de numerador1 decrece al aumentar cualquier polo. Refuta la monotonía numeratorfixed universal AP, no la monotonía de eigenvalores ni el signo.
- POWER_PRIME_PATTERN_FALSIFIER_008, auditado en POWER_AUDIT_008: en la misma familia confluente fija, el test f=(D²−1/4)[y^(n−1)e^-31.5y], n=2^17, tiene A=B=0, ARCH<−3.83||f||², y cada contacto primo-potencia<=1024 empeora el déficit. La cola posterior queda abierta; no se afirma signo negativo completo. Así el hecho de que2 repare el bloque12 NO constituye un patrón universal de primos reparadores.

## Requisitos pendientes, sin cambio de alcance

1. Cuatro exponentes arbitrarios>=32: sólo hay rango alto anterior y vecindad confluente/local; uniformidad no probada.
2. Todos los órdenes sobre familia densa: abierto. El puente sí está probado, pero los márgenes de bloques finitos no prueban uniformidad ni paso al límite sin signo de todos ellos.
3. Cierre del signo del Paper47: no obtenido. No editar papers ni declarar goal completo.

## Próximo problema útil

Buscar una identidad o desigualdad para la suma aritmética COMPLETA que conserve la autocorrelación de signos mixtos. No repetir monotonía AP en dimensión ni la inferencia desde contactos favorables de un vector. El test008 deja una obligación (TAIL) explícita pero no una solución: habrá que compararla con residuos ya registrados antes de proponer nueva construcción. El registro anterior sobre positividad bloque12 es progreso matemático real, no cierre.
