# Estado028 — Cuarta y quinta filas completas positivas de W

Estado: ROW4 y ROW5 PROVED y auditados. Sustituye STATE027 como resumen vigente. Signo global OPEN; goal activo; papers intactos. Ambas construcciones cerradas y revisadas.

## Nueva cobertura de la forma completa

POWER_ROW_FOUR_028 demuestra

    W[f_(4,k)] > ||f_(4,k)||²/50,
    F_(4,k)(s)=s^k/(s+u)^(4+k), TODOS k>=0 y TODOS u>=63/2.

Se incluyen TODO el peine aritmético y el término polar. No es positividad de un núcleo auxiliar ni una muestra de exponentes. La prueba combina ARCH/norma²>11/400, peine en magnitud<3/500 y pérdida polar<1/1000 para k impares; en k pares el polar es positivo. El margen resultante41/2000 supera1/50.

## Qué cambió respecto de las filas anteriores

La fórmula exacta ARCH40=d−ud'+(2u²/5)d''−(u³/15)d''' mantiene el pequeño margen positivo que se perdería con cotas más gruesas. Las monotonías de ARCH en u y en k reducen todos los parámetros a u=63/2,k0. Las tres series de polygamma se acotan con resto integral racional.

El peso eta12 en WR4 reduce el coste del peine completo frente a eta15 usado018; la positividad de los coeficientes de su serie demuestra uniformidad en u. El signo alternado real del polar evita restar el término favorable de k0. No se supone monotonía de W bajo movimiento de polos.

La recurrencia completa implica además positividad estricta de la tercera diferencia de la fila inicial para TODOS k. No implica diferencias de cualquier orden.

## Evidencia y límite

POWER_ROWS_AUDIT_028 aprueba ROW4 y ROW5; root leyó ambas pruebas y reprodujo los dos verificadores Fraction: PASS. La uniformidad proviene de argumentos analíticos, no de un barrido. Se conserva la auditoría027 del balance exterior y la mezcla gamma, sin atribuirles signo del interior.

La cobertura ahora incluye filas N1,2,3,4,5 para todo k y u>=31.5; también permanece el cono k>=10000N² a u31.5, ocho polos arbitrarios y bloque fijo12. En la tabla suficiente a u31.5 resta N>=6 debajo del cono. El puente017 exige todos N,k; una fila nueva no certifica una ventana T ni resuelve el signo global.

## Quinta fila y patrón de separación

POWER_ROW_SPLIT_028 demuestra W[f_(5,k,u)]>norma²/25 para TODOS k>=0,u>=63/2. Para k>=1 da el margen más fuerte4/5. ARCH50(u0)<−1/10, así que exigir ARCH positivo desde k0 habría perdido esta fila real.

En k0 y u entre u0 y2u0 se combinan extremos opuestos: ARCH>−.13 y polar>.23. Para u>=2u0, ARCH>.5 y el polar sigue favorable. En k>=1, covarianza y escala dan ARCH>.9; el polar impar pierde menos de.002. El peine COMPLETO pierde menos de.06 en todos los parámetros, por WR5 con eta12. Esas cotas prueban la fila sin asumir monotonía de AP ni de W.

El criterio reutilizable del memo separa la obligación k0 de la órbita k>=1. La identidad A_(N,1)=A_(N,0)+u∂_u A_(N,0) explica la mejora; las premisas del criterio no están probadas para todo N. La cuarta diferencia de la fila1 es ahora estrictamente positiva, sin concluir completa monotonía.

La continuación029 busca un patrón uniforme mediante control de autocorrelación con pesos opuestos y parámetros N/u², previa comparación con el no-go de pesos a u fijo016. No se sustituye el objetivo de todos N a tasa fija por un resultado con tasa creciente.
