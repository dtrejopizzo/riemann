# Estado revisado — caso de tres potencias resuelto

Estado: PROVED caso de tres; OPEN signo a todos los órdenes. Goal activo. Papers intactos.

## Teorema nuevo

Para cualesquiera a_1,a_2,a_3>=32 y coeficientes reales c_i, sea rho=Σc_i X^{-a_i}, f(y)=Σc_i zeta(a_i)exp(-(a_i-1/2)y), y>0. Entonces

    Q[rho] >= (1/20)||f||².

Si la función no es nula, el signo es estrictamente positivo. No se requiere separación ni cota superior de exponentes. Por tanto P3 para A>=32,h>0 queda resuelto, también para triples desiguales. Los límites confluyentes de multiplicidad total tres quedan cubiertos.

Fuentes: POWER_POLE_MOVEMENT_004 (prueba), POWER_CONFLUENT_004 (certificado racional), POWER_AUDIT_004 (revisión independiente). Anula la anterior condición de rango alto para triples; no cambia alcance del teorema general de orden n con umbral creciente.

## Insight y prueba

Las transformadas son P(iτ)/∏(u_j+iτ). Al subir individualmente los polos u_j, la densidad se multiplica por un factor creciente de |τ|. El multiplicador arquimediano también crece en |τ|. La identidad de covarianza prueba que cada cociente Rayleigh aumenta, y por minmax lo hacen todos los autovalores comprimidos. Esto reduce el mínimo arquimediano a polos confluyentes en u=31.5.

En la base Laguerre de dimensión tres, la matriz arquimediana es Toeplitz3 explícita y se certifica >1/10 con sumas racionales. La norma ponderada ||exp(uy/2)f||²<=1302||f||² controla el peine (<.003) y sólo la parte negativa del polar (<.042). La suma conserva más de1/20 de margen.

## Lo que no se ha resuelto

La familia fija32+k, de todos los órdenes, sigue sin signo demostrado. El puente de esa familia al signo de ventanas sí está probado. No extrapolar triples ni los seis tamaños ya certificados a todos los tamaños.

En dimensión cuatro, un diagnóstico concreto del confluente en31.5 da fondo arquimediano negativo (~−.17005), mientras arquimediano+polar es positivo (~.32259). Estos números son diagnósticos, no certificados. Motivan el siguiente paso: conservar la contribución positiva del polar y revisar si el movimiento de polos sigue teniendo el signo adecuado para esa suma. NO se presupone tal monotonía.
