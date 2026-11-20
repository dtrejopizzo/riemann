# POWER_INVERSE_COEFFICIENT_AUDIT_054

Estado: **APROBADO** el lema COEFF/EVAL de POWER_INVERSE_COEFFICIENT_054, tras lectura íntegra de la fuente. No se afirma nuevo signo de W ni un corte completo. Papers intactos.

## Antecedentes y diferencia

Se cotejaron índice/grid/crucigrama y HIGHPASS015, JOINT_SCALE016, QUADRATIC_EXPLICIT017 y los momentos049/053.015 ya prueba eventualidad uniforme en los numeradores a dimensión fija mediante convergencia de Gram y Riemann–Lebesgue, sin una dependencia efectiva del condicionamiento en dimensión.016 impide una constante temporal ponderada independiente de n, pero no constantes explícitas que crezcan con n.017 trata densidades monomiales. El objeto nuevo aquí es un polinomio en frecuencia inversa cuyo control de coeficientes depende explícitamente sólo de n y vale para todos j>=n. No se registra otra prueba cualitativa de RL como avance.

## Normalización y prueba del bound

Para a=u sqrt(j), R(y)=y^(n−1)P(ia/y) es un polinomio de grado<=n−1, y su cambio de coeficientes es invertible para cada j. El cambio tau=a/y en ambas semirrectas tiene jacobiano absoluto a/y². Sustituyendo la potencia del denominador resulta exactamente

    ||Q^jF0||²=a^(1−2n)/(2pi) ∫|R(y)|²(1+y²/j)^−(n+j)dy.

No falta un factor2 porque la última integral cubre toda la recta. La integrabilidad se mantiene en cero y en infinito para todo n>=1,j>=n.

En[-1,1], log(1+y²/j)<=y²/j y (n+j)/j<=2, de modo que el peso es>=exp(−2). La recurrencia de Legendre implica por inducción que la suma de módulos de sus coeficientes es<=3^k. Su ortogonalidad da por Cauchy

    (sum|coef R|)²
      <= exp(2) D ·sum_(k<n)(2k+1)9^k/2
      <= exp(2)D n²9^(n−1).

Como exp(2)<9, la constante declarada C_n=9n²9^n es sobrada y válida también en n=1. La demostración cubre coeficientes complejos y por tanto TODOS los numeradores, no sólo sus diagonales o un numerador fijo al variar j. No requiere un eigenvalor límite no cuantificado.

La evaluación compleja satisface |R(z)|<=(sum|coef R|)max(1,|z|^(n−1)); aplicarla a z y−z prueba las dos cotas EVAL con exactamente la misma normaD y constanteC_n. No aparece una pérdida cuadrática adicional deC_n.

## Signo y límites

Para P real se verifica R(y)R(−y)=(−1)^(n−1)|R(y)|² en la recta real. La fuente conserva explícitamente ese factor en DENSITY; su identidad analítica es correcta. Los majorantes absolutos sobre un contorno no eliminan la obligación de integrar la densidad completa con su denominador.

COEFF/EVAL no demuestra aún una cola aritmética summable ni un corteK(n) para W. Un bound IBP de correlación proporcional a1/t por sí solo no suma el peine infinito. El extremo monomialN'=1 de una futura reducción no puede importarse de una prueba que sólo cubreN'>=2. La sección5 del memo mantiene estas obligaciones separadas y OPEN. No se modifica la cobertura de signo previamente certificada.
