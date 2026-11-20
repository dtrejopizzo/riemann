# POWER ARCH CELL AUDIT 026

Estado: ARCH_CELL026 y UNIFORM_CUTOFF026 APROBADOS. Papers intactos.

Antecedentes revisados: CELL_BALANCE024 y su auditoría, CELL_TEST024, INVERSE_LOGCONCAVITY025 y su auditoría. La logconcavidad específica ya permite un corte completo y ERR129<−.66; no es por sí sola un signo de W. La nueva obligación cuantitativa es conservar ARCH_sharp en el balance real, o extender el corte con un teorema uniforme de parámetros. Una cota inferior insuficiente no es W negativo. Una identidad de agrupación sin desigualdad adicional no completa ese balance.

## ARCH_CELL026 — APROBADO

Revisados `POWER_ARCH_CELL_026.md` y `tools/power_arch_cell_026_verify.py`; ejecución independiente PASS. La recurrencia ψ(5/4+iτ/2)=ψ(1/4+iτ/2)+1/(1/4+iτ/2) incorpora exactamente el símbolo polar sharp. Para g129, la varianza V=u²/[4(2N−3)] y las tres traslaciones hasta17/4 son correctas; Euler/Jensen dan ARCH_sharp<−.81. Por tanto el comparador ARCH_sharp+.66 es negativo por más de.15. Esto demuestra insuficiencia de esa garantía de ERR, no W<0.

La identidad w(x)=ΣJ(nx) sigue de μ*1 con suma absoluta. Sustituir J=x∫K/t² da los pesos D=T(t)/t² y E_x=T(t/x)/t² y el factor x^(3/2) en rho. La representación de ψ produce k(x)=x^−7/2/(1−x^−2), con el factor2 declarado. Así JOINT conserva todas las normalizaciones y saltos.

El intercambio agrupado es válido: cerca de x1, la parte suave de T(t)−x^(3/2)T(t/x) es O(x−1) en norma integrada contra |K|/t²; los cruces de escalones n≤t<nx también suman O(x−1) por el decaimiento y acotación suave de K. Esto cancela la singularidad de k. En infinito el mayorante es integrable. Las singularidades logarítmicas en t entero tienen medida cero y son localmente integrables; no se separan los dos términos divergentes del corchete.

En1<t<2, I′=−1/(t²−1) y la diferencia de valores ψ dan la fórmula FIRST. El evaluador racional certifica Omega(3/2)<−.1. Se refuta positividad puntual universal de este peso conjunto. No se permite elegir un K arbitrario como si proviniera de una autocorrelación gamma: el ejemplo de soporte compacto violaría rho≤1. No se infiere signo de W ni imposibilidad de otras agrupaciones.


## UNIFORM_CUTOFF026 — APROBADO

Revisados `POWER_UNIFORM_CUTOFF_026.md` y `tools/power_uniform_cutoff_026_verify.py`; ejecución independiente PASS. El corte Jensen es válido para d≥2: f(j)=(d−j)/(2d−j−1) es decreciente y cóncava, r_j≤63(1+10/d)f(j), y la media del índice es tL<d. La comparación con L30 da exactamente t_J=d(d+220)/(330d+6300). El caso30t≥d también está tratado, sin salir del dominio de f.

La ecuación diferencial de rho y la Riccati de q son correctas. q>0 procede del kernel de calor; la expansión polinómica en infinito da q′=d/t²+O(t^−3)>0. En el nivel q′0, q″<0 impide volver a valores positivos; en el nivel q′M_d, q″=2qM_d+q²/t>0 impide retornar desde arriba al límite0. Estas barreras excluyen también contactos y dan0<q′<M_d en todo t>0. No se presupone la desigualdad que se pretende probar.

De Riccati se obtiene la cota inferior de q. La identidad D′/D=u−q+q′/(3/2+q), el umbral Q²=9/4+M_d y la resolución t_R=2dQ/(u²−Q²) son correctos. Para d≥2 el denominador es positivo. El caso d1 se separa correctamente con el polinomio afín y su umbral1/30−1/693. Así ambos cortes son teoremas uniformes, no extrapolaciones entre certificados puntuales.

La expresión de t_R en x=2d−1 y el polinomio del signo de su derivada tienen denominadores positivos. La expansión en x=5+y es positiva; las dos comparaciones racionales d2,d128 y el caso afín prueban el rango2≤N≤129. El script sólo verifica estas constantes; el argumento analítico proporciona la uniformidad.

Integrar el bound de logderivada controla la suma COMPLETA de Möbius por Σm^−2≤3/4, y por tanto K>0 en toda la cola declarada. La representación de J da la integral gamma inferior positiva; LOCAL da CELLTAIL. La reducción del número de celdas interiores es correcta y no aporta su signo. El orden129 reproduce ERR025, sin contarlo como nueva cobertura.

## Cierre de alcance

La ronda añade dos cortes uniformes y un kernel conjunto exacto que sigue siendo firmado. El comparador ARCH+.66 insuficiente y Omega(3/2)<0 no son W<0. Las colas positivas no prueban los promedios interiores restantes ni el signo de todos los órdenes. No hay una ventana nueva T certificada ni modificación de papers.
