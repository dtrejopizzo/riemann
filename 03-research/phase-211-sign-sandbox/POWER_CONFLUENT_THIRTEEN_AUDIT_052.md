# POWER_CONFLUENT_THIRTEEN_AUDIT_052

Estado: **APROBADO** POWER_CONFLUENT_THIRTEEN_052, incluido su script y demostración algebraica. Papers intactos.

Se cotejaron los antecedentes de índice/grid/crucigrama sobre Schur, BLOCK007, ZERO13 de FULL_TWELVE050 y la discusión051. El caso nuevo está motivado por la única dirección que deja abierta ZERO13: se decide el bloque confluenteV13 completo, con sus cruces y toda la cola aritmética. No se atribuye signo al complemento mediante una identidad abstracta.

Leído íntegro power_confluent_thirteen_052_verify.py y reproducido independientemente con python3: **cinco mensajes PASS, exit0**. Las bandas intervalaresE2/E23 conservan las normalizaciones de007/048; los LDL13 verifican E2>3/10000 y E23>7/25000 contra la norma original ortonormal, pagando el error de operador<10^−10 contraI.

Para el Schur, h_j=(−1)^j tiene norma²13; C_i=e_i−(−1)^i e12 satisface Cᵀh=0 y tiene Gram no trivial. El código usa A=CᵀTC, g=CᵀTh, delta=hᵀTh y S=(delta−gᵀA^−1g)/13. El LDL resuelve exactamente el sistema sin invertir entradas intervalares. La comparación entre centrosT±epsilonI es válida porque el mínimo sobre el afín h+range(C) es monótono en el orden de formas. Esto incorpora correctamente la Gram y la variación simultánea de diagonal, acoplamiento e inversa. Las cotas certificadas son S_E2 en(.0004054,.0004055), S_E23 en(.0003834,.0003836), y S_W en(.0003,.0005).

Los componentes se evalúan con intervalos en el VECTOR FIJO x=h−CA_centro^−1g_centro: se calculan xᵀT_componente x/13. No son cocientes de Rayleigh por norma²x ni componentes del minimizador exacto desconocido. Esta normalización representa el coeficiente unitario del complemento h/sqrt13. En esa dirección central fija AP está en(.01839,.01841), el contacto2 en(−.018,−.01798), y el contacto3 es negativo. Por tanto el3 empeora aquí el pivote; no se afirma que rescate el signo ni que la aritmética sea monótona.

La cola desde4 amplía el argumento007 hasta banda12: signos de coeficientes trasladados por40 certificados exactamente, log4>4/3 para la monotonía y log4<7/5 para la comparación suma-integral con coeficientes positivos. El majorante de filas es<1/100000 y cubre TODOS los enteros desde4, sin truncar potencias primas ni presuponer sus signos. Por ello W>(7/25000−1/100000)norma²>norma²/4000 enV13 confluente. No se transporta esa cola a trece polos arbitrarios.

Leído finalmente el memo completo de seis secciones: explicita la normalización no unitaria de los componentes, separa el minimizador central del pivote exacto y distingue conservar3 para mejorar el presupuesto de afirmar un signo favorable de3. Su alcance confluente y la obligación adicional para trece polos arbitrarios son correctos. Las cifras decimales diagnósticas no se utilizan como prueba.
