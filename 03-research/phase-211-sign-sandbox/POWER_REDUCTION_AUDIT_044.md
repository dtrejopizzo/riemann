# POWER REDUCTION AUDIT 044

Estado: REFLECTION_TEST044 APROBADO; evaluación L55-B concluida sin nuevo lower construido. Papers intactos.

## 1. Corpus y restricciones

Consultados ROUTES-TRIED-INDEX/README yAUDIT_B, grid y crucigrama. L55-B sigue como candidato de par primal positivo en dato arquimediano desplazado, sujeto a W4; el gap-slice pequeño y la dualidad son antecedentes. La reducción de subfamilias debe preservar densidades y polar, sin invertir positivamente REC ni confundir una unión de conjuntos positivos con su suma.016/018/029/036 delimitan esas inferencias.

## 2. Reflexión del puente017 — APROBADA

Revisados `POWER_REFLECTION_TEST_044.md` y `tools/power_reflection_test_044_verify.py`; ejecución independiente PASS. La descomposición única R(q)=A(q(1−q))+(2q−1)B(q(1−q)) es correcta por simetría y divisibilidad. Sólo da una representación firmada; no elimina un sector del funcional.

Las funciones g_Q y g_L tienen norma uno y transformadas√(4u)s/(s+u)² y√(4u)u/(s+u)². Sus factores espectrales q y1−q se intercambian respecto a la medida común. Las combinaciones Laguerre dan gapARCH2b; el lower racional de trigamma prueba b>1. El polar evaluado en±1/2 da exactamente−2u(1+4u²)/(u²−1/4)²>−.5. Las autocorrelaciones e^−ua(1∓ua) son correctas y todo el peine diferencial es estrictamente positivo. Así W[g_Q]−W[g_L]>1.5 conserva TODAS las contribuciones reales.

El resultado refuta la simetría concreta que haría invisible el sector antisimétrico, no la positividad de W ni toda posible relación entre franjas. Ambos valores pertenecen a regiones ya positivas. No se ha probado una nueva subfamilia suficiente, nueva cobertura ni ventanaT; una reducción válida requiere un control desigual del sector restante.


## 3. L55-B: orientación revisada, sin resultado nuevo

La evaluación paralela no encontró un cierre posterior del candidato ni una construcción explícita de par primal. La transferencia condicional tiene orientación correcta: una representación positiva de TODAS las formas primitivas en un dato arquimediano desplazado, con slack r≤epsilon y mismatch primal de variación total≤eta en el intervalo relevante, daría lambda_A≥−epsilon−eta usando|c_F|≤norma². Con match exacto del peine, el piso sería−epsilon.

Esa medida representante no es el vector finito factible de la LP dual: los vectores de prueba y sus valores dan cotas superiores, no este lower. Tampoco basta que el mismatch sea una medida positiva, porque c_F puede tener signos. La representación positiva exacta del dato desplazado sería ya una extensión positiva de la forma; sigue faltando una construcción independiente que la demuestre.

No se registra la fórmula de transferencia como avance aritmético ni como W4 renombrado. El candidato L55-B permanece abierto, sin piso nuevo probado y sin artefacto ficticio de construcción. Esto no es un no-go global. La ronda sólo añade el chequeo real de reflexión del§2 y conserva sin cambios la coberturaW/T.
