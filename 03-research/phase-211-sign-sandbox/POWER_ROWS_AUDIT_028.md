# POWER ROWS AUDIT 028

Estado: ROW_FOUR028 y ROW_SPLIT028 (N5) APROBADOS. Papers intactos.

## Fila N4 completa — APROBADA

Revisados `POWER_ROW_FOUR_028.md` y `tools/power_row_four_028_verify.py`; ejecución independiente PASS. La norma base5/(32u^7) y la recurrencia de integrales producen A4=d−ud′+(2u²/5)d″−(u³/15)d‴. Las series poligamma dan exactamente los tres términos negativos con factores u/2,u²/5,u³/20. El resto integral sobre la cola desde116 está correctamente acotado por la integral desde115. El extremo racional A4(u0)>11/400 está certificado.

Las dos monotonías ARCH son legítimas: la ley en ξ=τ/u es independiente de u y m(uξ) crece con u; aumentar k repondera por ξ²/(1+ξ²), creciente con |ξ|. Así el extremo u0,k0 extiende el bound a todo u≥31.5,k≥0. Esto no usa movimiento de polos de la forma completa.

WR4 eta12 conserva eta<u/2. Su serie generadora tiene coeficientes positivos y ambos argumentos decrecen con u; R4<400 en el extremo controla todos los parámetros. El bound del peine incluye toda la suma de von Mangoldt, con el factor2sqrt R<40 y la integral decreciente de(log x)x^−12. La sustitución2^−1/2<5/7 y el extremo log2<.7 dan pérdida<.006.

La norma beta y el polar alternado son correctos. La cota c_k≥2^−k y binom(k+3,3)≤4^k da la razón geométrica8q_u; p40 y q_u decrecen con u. Para k pares el polar no se resta; para k impares su pérdida es<.001. El balance REAL completo es por tanto mayor que41/2000>1/50, uniformemente en todos k,u declarados.

La diferencia respecto018 es la evaluación exacta de ARCH4 y el peso eta12 que deja un margen positivo; las recurrencias solas no implican este resultado. La fila completa sí añade signo real de W y tercera diferencia estricta de la fila1, pero no completa la tabla ni certifica una ventana nueva T.


## Fila N5 completa — APROBADA

Revisados `POWER_ROW_SPLIT_028.md` y `tools/power_row_split_028_verify.py`; ejecución independiente PASS. Los coeficientes Laguerre de k0 y k1 y sus normas70 y28 son correctos. Las bandas Toeplitz arquimedianas conservan los factores1/2 y1/r!. Las series poligamma usan256 sumandos y dos extremos integrales válidos; ψ(127/4) se reconstruye desdeψ(3/4)=−γ+π/2−3log2 mediante31 pasos. Los tres extremos racionales de ARCH están certificados.

Las monotonías legítimas de ARCH en k y u cubren todos los parámetros infinitos. El polar beta tiene la normalización declarada, signo (−1)^k y cociente (k+N)/[(k+1/2)(4u²−1)]. Para N5,k≥1 ese cociente es≤4/(4u0²−1)<1. El extremo p51(u0)<.002 domina todos los polares adversos. p50 decrece con u; por tanto usar ARCH(u0)>−.13 y polar(63)>.23 en [u0,63] es válido sin suponer monotonía AP. Para u≥63, ARCH>.5 y el polar k0 sigue favorable.

WR5 eta12 es válido para todo u≥u0 y k≥0. Su serie generadora tiene coeficientes positivos; la monotonía de R5 se justifica por esa serie, no por el numerador cerrado de signos mezclados. R5<2500 da2sqrt R5<100. El bound completo de peine medianteΛ(q)≤q, q^−11.5≤q^−11 y la integral desde2 es menor que.06. No falta ninguna potencia prima.

El balance real completo da W>norma²/25 para todo k≥0,u≥31.5 y W>4norma²/5 para k≥1. La identidad A_(N,1)=A_(N,0)+u∂_uA_(N,0) se deriva de la recurrencia de resolventes y la norma beta, sin límite asintótico ni extrapolación en N.

La diferencia específica de N5 es conservar el polar positivo del borde k0, usar extremos opuestos en un intervalo y empezar la covarianza en k1. El criterio reutilizable de§7 es sólo suficiente bajo sus hipótesis, no un teorema de todas las filas.

## Cierre de alcance

Se añaden dos filas infinitas REALES de W con u uniforme, y por la recurrencia completa la tercera y cuarta diferencias estrictas correspondientes de la fila1. No se deduce completa monotonía de todo orden, todas las matrices ni nueva ventana T. La tabla suficiente completa sigue abierta. Root coincide independientemente en las revisiones de ambas filas.
