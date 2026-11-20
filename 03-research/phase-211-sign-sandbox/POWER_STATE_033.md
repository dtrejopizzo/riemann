# Estado033 — Cotas aritméticas relativas y agrupación finita de coeficientes

Estado: resultados parciales PROVED y auditados; condiciones finales OPEN. Sustituye STATE032. Goal activo; papers intactos.

## Peine completo con resto relativo firmado

POWER_PRIME_BALANCE_033 demuestra para u>=63/2 y3<=N<=2u²/9−u/3+3/2 que el kernel positivo de contactos k1 satisface w(mq)<=m^-2w(q) para q>=5,m>=1. El operador de dilataciones Df(q)=sum_(m>=2)f(mq) contrae esta clase real por rho=2389/3600<2/3.

Restando correctamente los divisores pequeños2,3,4 de logn se obtiene un funcional L sobre enteros y la identidad L(f)=A((I+D)f), donde A es la cola aritmética real q>=5. Para K impar, el prefijo S_K=sum_(j=0)^K(−1)^j L(D^jw) cumple

    0<S_K<=A(w)<=S_K/(1−rho^(K+1)).

También A(w)>=3600L(w)/5989. Son cotas firmadas y uniformes, no prefijos arbitrarios de Möbius supuestos positivos. El error es relativo al peine o a su prefijo, NO al residuo pequeño de W. Añadir ARCH, polar y contactos2,3,4 da un comparador completo, pero su signo positivo en un rango nuevo aún no está demostrado.

## Mezcla finita que conserva la forma

POWER_COEFFICIENT_BALANCE_033 representa exactamente la autocorrelación gamma como mezcla finita de perfiles Erlang S_j=e^-ut sum_(r<=j)(ut)^r/r!, con pesos w_Nj=a_Nj−a_N,j+1>=0. La funcional lineal conserva todos los contactos y el polar.

La premisa de que cada componente tenga funcional positivo es falsa: para el único corte22 se prueba −.01<L[S22]<−.006. Su transformada de Fourier toma un valor negativo, por lo que S22 NO es una autocorrelación admisible; no es un contraejemplo a W. La pérdida de ese componente individual en la mezcla real está acotada por .22/(N−1), sin controlar por ello todos los demás.

Una segunda agrupación de Abel da coeficientes no negativos para T_m=sum_(j=1)^m jL[S_j]. Probar TODOS T_m>=0 sería suficiente para la fila k0, pero sigue OPEN. No sería por sí solo un cierre de todos k ni del Paper47. La identidad generadora se conserva como descripción del requisito, no como prueba de signo.

## Evidencia y alcance

POWER_BALANCE_AUDIT_033 aprueba ambos memos. Root revisó las identidades, fronteras de divisores, signos de restos y alcances, y reprodujo ambos verificadores exactos: PASS. No se certificaron nuevos N ni una campaña de cortes.

No hay ampliación de cobertura W/T en033. Permanecen las filas1..5, el cono017, el único átomo211,1 decidido032, y las regiones029 de tasas crecientes con sus límites. El promedio firmado031 y el criterio nuevo de coeficientes siguen sin resolver la obligación global.

La próxima construcción debe demostrar una comparación positiva completa con estos restos o controlar las compensaciones de T_m; convergencia de una aproximación y positividad de sus piezas no equivalen al signo total.
