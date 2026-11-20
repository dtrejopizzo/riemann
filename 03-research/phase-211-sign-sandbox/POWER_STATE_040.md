# Estado040 — Signos opuestos en el centro y cola positiva a distancia constante

Estado: PROVED y auditado. Sustituye STATE039 como resumen de trabajo. Goal activo, signo global OPEN, papers intactos.

## Patrón uniforme del inverso aritmético completo

POWER_CRITICAL_BALANCE_040 prueba para TODOS N>=2^80, u=63/2, v=1/2+N^(-2), t_v=2(N−1)v/(u²−v²):

    h_N(exp(t_v))/H_N(exp(t_v)) < −1/N,
    K_N(exp(t_v))/G_N(exp(t_v)) > 1/N.

Los denominadores H_N y G_N son positivos. Son signos opuestos de dos núcleos aritméticos COMPLETOS en el MISMO centro t_v=(N−1)/992+O(1/N), no prefijos de sus sumas ni evaluaciones de W. La negatividad de h no es un contraejemplo al signo de W.

Se prueba además, para los mismos N, una cola entera:

    h_N(exp(t))>0 y K_N(exp(t))>0
    para TODO t>=(N−1)/992+5.

El comienzo certificado queda a distancia CONSTANTE del centro; mejora el desplazamiento O(sqrtN) de039, aunque con el rango N>=2^80 declarado. No identifica la transición exacta ni demuestra unicidad de una transición. La coordenada t=logx del núcleo no es la ventana T del Paper47.

## Insight y control del error

Se separa el factor elemental del producto infinito antes de estimarlo. La identidad con la parte fraccionaria da, para Re z>=0 y |z|<=1/8,

    1/zeta(1+z)=z−gamma z²+R3(z), |R3(z)|<=9|z|³.

Al invertir Fourier con z=delta−i xi, el cociente completo se expresa mediante delta−f′(0)−gamma[delta²−2delta f′(0)+f″(0)], con resto explícito menor que1/(10000N) en el régimen central. Se mantiene delta>0 y la convergencia absoluta del producto infinito. No se usa una serie formal ni una interpretación probabilística de pesos firmados.

Una nueva cota elemental, −2q′(t)/t<q″(t)<0, se demuestra a partir de los coeficientes positivos de P_N y Riccati. Proporciona límites efectivos para f′, f″ y una cota inferior q′>50/N. Así el error es realmente menor que el margen de signo de ambos inversos. Para la cola, delta entre2000/N y1000/sqrtN da positividad por el mismo resto y enlaza con039; el desplazamiento del primer centro es menor que5.

La novedad frente039 es controlar la escala1/N del inverso cerca del centro y extender la cola hasta distancia constante. El factor local sustituye el centrado con momentos que se deterioraban cuando delta bajaba a esa escala.

## Evidencia y obligación restante

POWER_CRITICAL_AUDIT_040 aprueba expansión, curvatura, patrón central y corte constante. Root revisó todas las pruebas; hubo revisión independiente adicional de la curvatura. El verificador exacto ampliado fue reproducido por root y auditor: PASS. No se recorrieron N, primos o casos numéricos W.

Falta controlar la contribución interior integrada y su balance con ARCH_sharp para decidir W. Los signos de estos núcleos, incluso completos, no son automáticamente el signo de la forma. No hay nueva fila W, combinación arbitraria ni ampliación de T. Se conserva la cobertura035 y resultados previos: filas1..17, todo k>=0 a u31.5, regiones adicionales y átomo211,1. El objetivo global permanece abierto.
