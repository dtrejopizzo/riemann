# POWER_R12_AUDIT_048

Estado: **APROBADO** el extremo y complemento polar de POWER_R12_ENDPOINT_048; **OPEN** R12 uniforme. Papers intactos.

Se cotejaron PRIME_TRANSFER014, su auditoría, ARITHMETIC_BLOCK007, GEOMETRIC_TRANSFER015 y las referencias de índice/crucigrama. No se encontró un cierre posterior de la restricción R12. El falsificador universal de orden2^17 no pertenece a V12 y no refuta esta hipótesis restringida. La coercividad007 es E2>(1/1250−10^−8)norma²; para la forma completa resta además una cola de operador<3/5000, sólo certificada sobreV12.

La imagen de V12 por s/(s+u) es exactamente V13 con evaluación Laplace cero en0: el numerador tiene el factor s, y la división inversa lo cancela conservando el grado correcto. E_j(0)=sqrt(2u)(−1)^j/u, de modo que la restricción y las columnas C_i=e_i−(−1)^i e_12 son correctas. C no es ortonormal; el script conserva correctamente CᵀIC en la desigualdad de norma.

Revisado el script completo: intervalos racionales atanh/atan, gamma, sumas Euler para potencias hasta13, signos poligamma, bandas polar y contacto2, centro redondeado y majorante de error por filas. El LDL actualiza sólo el bloque posterior y conserva las columnas pivote durante cada paso; no introduce dependencias de entradas ya modificadas. Reproducción independiente con python3: **PASS**, doce pivotes estrictamente positivos. La comparación T_centro−(1/50+10^−10)I, junto al error de norma<10^−10, demuestra E2>norma²/50 sobre toda la restricción, con todos sus cruces. No es un diagnóstico de autovalores flotantes.

La continuidad matricial en v produce un intervalo local común para todos los vectores; no proporciona radio efectivo. El ejemplo editorial fue corregido a c=1/2500, compatible tanto con el extremo como con la coercividad base007. No se transporta la cola aritmética007 hacia V13 ni se obtiene todavía W completo. Tras mover un polo cambia el espacio base; una inducción exigiría hipótesis para esos espacios intermedios.

Complemento revisado: la compresión de q es la matriz tridiagonal con diagonal1/2 y adyacentes1/4. La energía de diferencias con extremos cero y Cauchy da M1>=M0/576. La logconvexidad de los momentos de la medida positiva q∈[0,1] implica M_j>=576^−j M0. La evaluación polar exacta multiplica por (−1/3968)^j; por ello su cociente normalizado se acota por (9/62)^j veces el cociente inicial. Es un resto polar efectivo válido. No da un corte J arquimediano, ni el signo de todos los bloques highpass, ni R12 para todo v.
