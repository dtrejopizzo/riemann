# POWER_R12_ENDPOINT_048 — Primer extremo del transporte aritmético restringido

Estado: certificado racional del extremo confluyente; revisión independiente APROBADA en POWER_R12_AUDIT_048.md y verificador reproducido por root. OPEN R12 uniforme para todas las tasas. Papers intactos.

## Antecedentes y diferencia

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, R162_2300_MASTER_GRID, CROSSWORD-TO-D y PRIME_TRANSFER014, SIGNED_TRANSFER014 y ARITHMETIC_BLOCK007. No se encontró un cierre posterior explícito de R12. El falsificador universal014 usa orden enorme; no pertenece a V12. Aquí se conserva exactamente la base positiva V12 y se comprueba únicamente el primer extremo natural v=u, sin barrer tasas ni órdenes.

## Forma y restricción exactas

Sea u=63/2, y sea e_j la base ortonormal causal con transformadas

    E_j(s)=sqrt(2u)(s−u)^j/(s+u)^(j+1), 0≤j≤12.

Se mantiene E2=ARCH+POLAR−sqrt(2)log(2)c(log2), sin omitir el polar ni sustituir el contacto por una norma. Para F0 en V12, G(s)=sF0(s)/(s+u) pertenece a V13 y G(0)=0. Recíprocamente cada G en V13 con G(0)=0 tiene esa representación con F0 en V12. La restricción en coordenadas reales z es sum_j(−1)^j z_j=0.

El verificador tools/power_r12_endpoint_048_verify.py reproduce las cotas racionales auditadas007, extendidas una banda: ARCH mediante sumas de potencias desde16 con cola Euler y resto explícito; polar exacto; contacto2 mediante log2 encerrado por atanh. Las bandas son Toeplitz. El centro racional usa denominador10^15 y el error de norma por suma de filas es menor que10^−10.

La congruencia de trece a doce dimensiones tiene columnas C_i=e_i−(−1)^i e_12, 0≤i≤11. El LDL racional comprueba positividad de

    Cᵀ[T_centro−(1/50+10^−10)I]C.

Por tanto, sin diagonalización numérica,

    E2[G] > (1/50)||G||²,   G∈V13, G(0)=0, G≠0.       (ENDPOINT)

No se ha incluido la cola de primos restantes en esta afirmación: R12 fue planteado precisamente para E2. Tampoco se importa la cota de esa cola sobre V12 hacia V13.

## Consecuencia local y obligación pendiente

Para cualquier c<1/50, en particular c=1/2500 (también inferior a la coercividad base certificada007), ENDPOINT demuestra R12 en v=u. Además existe ε>0 tal que R12 vale simultáneamente para todos F0∈V12 y u≤v≤u+ε. En efecto, en una base fija de V12, las matrices de E2[sF0/(s+v)]−c||sF0/(s+v)||² son continuas en v. La integral arquimediana se domina uniformemente cerca de u por una función integrable con factor log(2+|τ|); los términos polar y contacto son continuos por sus integrales racionales causales. La matriz en u es definida positiva; su menor autovalor conserva signo en un entorno. No se da aquí un radio efectivo.

Esta consecuencia local no prueba R12 para todo v≥u. La monotonía de ARCH bajo movimiento de polos no ordena el símbolo oscilatorio del contacto2 ni su cambio polar. Tampoco autoriza sucesivos movimientos: después del primero la base ya no es V12 confluyente. La obligación uniforme original sigue OPEN. El resultado nuevo es el certificado de la corrección restringida en el extremo, con margen, y la exclusión de un falsificador en ese extremo; no un cierre del transporte o del signo completo.

## Complemento: el polar de la órbita highpass tiene un resto efectivo

La expansión geométrica pertinente ya fue probada en GEOMETRIC_TRANSFER015; no se presenta aquí como nueva. Para usarla sobre V12 falta un corte efectivo J después del cual ARCH sobre Q^jV12 domine el contacto2 y el polar, y certificados de todos los índices anteriores. ENDPOINT sólo cubre j=1.

Sí se puede cuantificar sencillamente la desaparición del polar, sin recurrir a una estimación de peor orden. Sea Q(s)=s/(s+u). En la base e_0,...,e_11, la compresión de q=|Q(iτ)|² es tridiagonal con diagonal1/2 y adyacentes1/4: con z=(iτ−u)/(iτ+u), q=(2+z+z̄)/4 y la medida espectral de e_0 es la medida uniforme del círculo. Para un vector real o complejo a, cambiar signos alternados da la energía de diferencias con dos extremos cero. Por telescopado y Cauchy,

    <qF,F> ≥ ||F||²/(4·12²)=||F||²/576.

Para M_j=||Q^jF||², Cauchy da M_(j+1)M_(j−1)≥M_j²; así M_j≥576^−j M_0. Por otra parte Q(−1/2)Q(1/2)=−1/3968, y por tanto

    Polar[Q^jF]=(−1/3968)^j Polar[F],
    |Polar[Q^jF]|/M_j ≤ (9/62)^j |Polar[F]|/M_0.

Un límite explícito uniforme para el último cociente es la norma de la matriz polar12 exacta de007; puede usarse su suma de valores absolutos. Esto paga el resto polar de una eventual prueba por corte J. No da por sí solo un corte arquimediano efectivo ni el signo de los bloques intermedios; no se ha ejecutado una campaña de esos bloques.
