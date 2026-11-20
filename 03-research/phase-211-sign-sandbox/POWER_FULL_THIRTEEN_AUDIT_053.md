# POWER_FULL_THIRTEEN_AUDIT_053

Estado: **APROBADO** el certificado y demostración completos de POWER_FULL_THIRTEEN_053. Se obtiene W>norma²/4000 para todos los trece polos reales>=63/2, multiplicidades permitidas, con numerador real propio. Papers intactos.

Antecedentes cotejados: índice/grid/crucigrama, COMMON_TRANSFER010, FULLTEL014, MULTI015, FULL_TWELVE050 y CONFLUENT_THIRTEEN052. El corte J=96 y su auditoría anteceden al segmento exhaustivo. La diferencia es una ganancia COMPLETA sobre catorce polos con numerador cero, no positividad por codimensión ni extrapolación automática del bloque confluente.

## Certificado racional y redondeo

Leídos íntegros el memo y tools/power_full_thirteen_053_verify.py. Reproducción independiente con python3, sin modificar parámetros: **exit0; logaritmos/pi,108 bandas, error de filas previo, los95 LDL de índices1,...,95 y las conclusiones finales PASS**. No quedan índices del segmento sin comprobar.

La optimización de lograw conserva los mismos512 términos y precisión10^−260: cada potencia y suma se evalúa en intervalos racionales con redondeo hacia fuera. El resto universal2(1/2)^1025/[1025(1−1/4)] domina el omitido porque el argumento exacto está entre0 y1/2. Esto evita denominadores enormes sin cambiar el enunciado, margen, precisión, corte o condición de éxito. Pi por Machin y logpi por monotonía de los extremos conservan sus recintos.

Revisado Euler–Maclaurin12 para Hurwitz: después del términoB24, el resto periódico se acota por |B24|(p)_23/[24!CUT^(p+23)]. Se obtiene al integrar el valor absoluto de la derivada24 usando |B24({x})|<=|B24|. Los coeficientes exactos de cada banda multiplican los extremos racionales ANTES del redondeo. Los restos de gamma y las bandas polares mantienen las normalizaciones auditadas. El control real de propagación no descansa sólo en una estimación previa de derivadas: el programa comprueba el error total de operador<10^−12 antes de cualquier LDL.

Vandermonde comprime exactamente C_jᵀTC_j a trece bandas; el índice máximo requerido es12+95=107, cubierto por108 bandas. La Gram comprimida es binom(2j,j+r), y el factor4^−j omitido es común a forma y norma. El error se paga contra epsilon C_jᵀC_j, evitando un pago incorrecto contra la identidad de coordenadas. Los95 LDL13 exactos verifican margen1/500 en todos los numeradores, incluidos sus términos cruzados.

## Órbita, mezcla y peine completo

CENTERED_MOMENT053 ya demuestra E23>norma²/10 para TODOS j>=96 y TODOS F0∈V13. Junto al segmento certificado queda E23>norma²/500 para toda j>=1. Cada numeradorD de grado<=13 conD(0)=0 es sP, gradoP<13, y su base confluente de catorce polos es QF0. MULTI015 con catorce factores mezcla exactamente los índices ya positivos. Norma, ARCH, ambos contactos y polar usan los mismos pesos no negativos; para tasas finitas las series son absolutamente convergentes. No se itera una hipótesis restringida sobre una base intermedia desconocida.

La traza ponderada uniforme010 es B_T14=947334302964<973312². El exponente total de la cola es65/4; conservar n^−1/4<=5/7 para n>=4 es válido porque(7/5)^4<4. La comparación suma-integral con log4<7/5 produce el racionalL4 del memo, menor que1/1000. Incluye TODOS los enteros desde4 y todas sus potencias primas. Así W>norma²/1000 sobre todos los catorce polos con numerador cero.

Finalmente, las correcciones FULLTEL para trece polos pertenecen precisamente a esa clase de catorce polos. La identidad conserva simultáneamente norma, polar y todos los contactos con coeficientes no negativos. La base052 tiene margen1/4000 y cada corrección un margen mayor1/1000; restar1/4000 veces la identidad de norma prueba el margen declarado sin deterioro bajo movimientos de tasas. Coincidencias y multiplicidades no requieren límites ni división por diferencias de polos.

No se demuestra dimensión arbitraria ni catorce polos generales, y el resultado por sí solo no certifica una nueva ventana temporal del Paper47.
