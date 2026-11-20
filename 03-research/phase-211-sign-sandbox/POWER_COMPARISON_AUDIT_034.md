# POWER COMPARISON AUDIT 034

Estado: DIVISOR_COMPARISON034 y WEIGHTED_COEFFICIENT034 APROBADOS. Papers intactos.

## 1. Corpus y diferencia

Se conservan los antecedentes033: brackets de Neumann y Abel eran criterios con comparadores abiertos.032 certificó sólo un punto de cancelación crítica; no autorizaba una campaña de órdenes. La nueva obligación es demostrar un comparador realmente positivo o una desigualdad cuantitativa adicional, distinguiendo estos resultados de una identidad o condición equivalente al objetivo.

## 2. Comparador uniforme completo — APROBADO

Revisados `POWER_DIVISOR_COMPARISON_034.md` y `tools/power_divisor_comparison_034_verify.py`; ejecución independiente PASS. La región N≥3,u≥31.5,u²≥225N/4 está contenida en REGION033: la diferencia se acota por46u²/225−u/3+3/2>0 en todo u declarado. Así TODOS los contactos son favorables y cada S_K impar es positivo; no se abandona una cola de signo desconocido.

ARCH-GENERAL029 con k1, ψ(N−1/2)≤logN yψ(3/2)=2−γ−2log2 da exactamente log(15/2)−log(4π)+1−γ/2−4/25>.035. El costo inverso se usa en el rango donde es finito; no se extrapola a k0. El bound universal polar p0<27/28 procede de Jensen gamma y Bernoulli, y2N/(4u²−1)≤3/337 para N≥3 deja pérdida<.009. Los signos se conservan.

El comparador REAL B_N+S_K es por tanto>.026>.025 para CADA K impar, y FULL033 implica W/norma²>1/40 uniformemente. La contracción aritmética es válida, pero no es necesaria para esta magnitud: aquí ARCH−|POLAR| ya es positivo y el peine es favorable. No se atribuye a Neumann una reparación del régimen de ARCH negativo o de la cancelación crítica211.

Esta es nueva cobertura de W: k1 y u²≥225N/4, que en u31.5 añade simultáneamente N6..17 a los órdenes conocidos, sin certificados individuales. No se extiende a toda fila, k0, k≥2 o ventana T sin prueba adicional.

Adición §7 DIVISOR_COMPARISON034 APROBADA y verificador reproducido PASS: para k≥2, el cambioψ(5/2)−ψ(3/2)=2/3 y el menor momento inverso ganan exactamente11/25 sobre el lower de k1, dando ARCH>.475. CENTERED eta4 tiene exponente<.9 porque48N≤(64/75)u² y u²>720; por tanto R<2.5. El peine COMPLETO se controla en valor absoluto por2R·.062<.31, sin signo favorable supuesto. La cota polar porp0[2N/(4u²−1)]^k conserva pares favorables y deja impares<.009. W>.156>.15 para TODAS k≥2 en la región. Junto con k1, el teorema cubre todo k≥1 con margen1/40.

Combinación de fuentes previas, sin recertificar: POWER_ARITHMETIC_BLOCK_007 da W>norma²/10000 en TODO V12 a tasa FIJA31.5; incluye g_N,k0 para N≤12. POWER_SIGNED_TRANSFER_014 da W>norma²/1000 en espacios de ocho polos arbitrarios≥31.5, incluidos repetidos; cubre g_N,k0 para N≤8 y toda tasa declarada. Por ello, junto con las nuevas columnas y filas previas, quedan filas1..12 completas a tasa31.5 y filas1..8 completas para todas u≥31.5. En N13..17 fijo queda k0 pendiente. No se infiere k0 variable para N9..12 del certificado fijo V12.


## 3. Oscilación de T_m — revisión hostil APROBADA

Revisado `POWER_WEIGHTED_COEFFICIENT_034.md` íntegro. No requiere un verificador numérico. La normalización E(v)=2L_power(v+1/2) es correcta: conserva ARCH, peine y polar4v/(v²−1/4). La representación cosh positiva de CONE001 tiene caída doblemente exponencial, defineTheta par analítica en compactos yTheta(v)>0 para todo v real. Así E=2Theta′/Theta es holomorfa en un entorno de CADA punto real y es impar; no se supone ninguna propiedad global fuera de esos entornos.

El generador correcto es F=ΣT_mz^(m−1), con una sola división por z respecto033. E−vE′ tiene cero de orden al menos3 en v0, de modo que la singularidad aparente de F en z1 es removible y F es par alrededor1. Las cotas reales deψ,ψ′ y la suma prima dan E=O(log|v|),vE′=O(1) en ambos semiejes por paridad, y F(z)→0 en el eje real positivo. F(0)=T1 es la forma REAL gammaN2 normalizada, ya>1/8.

El lema elemental de Pringsheim está probado correctamente: si el radio R fuera finito, la prolongación holomorfa en el disco(R,ε) permite Taylor en a=R−ε/4 con radio al menos3ε/4. Elegir h=ε/2 mantiene convergencia absoluta. La positividad de la cola, tras restar un polinomio, permite Tonelli y obliga a convergencia de la serie original en a+h>R, contradicción. No se presumió convergencia en1 antes de aplicar el lema.

Bajo la hipótesis eventualT_m≥0, F sería entera. Una derivada impar de orden q mayor que los índices excepcionales se anula en1 por paridad, pero su serie entera tiene todos los términos restantes no negativos; fuerza a que todos esos coeficientes sean0. F sería polinomio, y su decaimiento real lo haría nulo, contradiciendo T1>0. Aplicar lo mismo a−F excluye eventual no positividad. Queda probado que T_m toma valores estrictamente positivos y negativos en índices arbitrariamente grandes, sin evaluar una campaña de índices.

El resultado refuta el criterio suficiente de033 T_m≥0 universal, incluso salvo finitas excepciones. No refuta las combinaciones gamma de Abel ni W; sus pesos reales pueden compensar signos. Se usa únicamente la integral positiva REAL, continuación analítica local y series de coeficientes, sin argumento de ceros ni equivalencias externas. El lema clásico no es novedad; la afirmación nueva es sobre esta sucesión aritmética específica.

## 4. Cierre

La ronda sí aporta nueva región W uniforme y cobertura fija derivada, con todas sus restricciones. A la vez decide una premisa suficiente abierta033 mediante un teorema analítico, sin convertir esa refutación en imposibilidad global. Los casos de comparación que requieren cancelación crítica permanecen abiertos fuera del único punto032 certificado. No hay ventana nueva T ni edición de papers. Root coincide independientemente en las revisiones conceptuales y de constantes.
