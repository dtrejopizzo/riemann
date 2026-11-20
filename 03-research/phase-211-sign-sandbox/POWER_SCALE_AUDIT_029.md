# POWER SCALE AUDIT 029

Estado: ROW_PATTERN029, BOUNDARY_WEDGE029 y SCALE_BRIDGE_LIMIT029 APROBADOS. Papers intactos.

## 1. Región k≥1, u²≥256N — APROBADA

Revisados `POWER_ROW_PATTERN_029.md` y `tools/power_row_pattern_029_verify.py`; ejecución independiente PASS. La fórmula de Euler con B2 periódico da un error tras logz−1/(2z) de módulo≤1/(4t²). Aplicada en5/4+it y trasladada hasta1/4+it, produce exactamente9/(8t²). La integral beta tiene los momentos logarítmico e inverso declarados; el inverso es finito desde k1. Las monotonías del bound con k y ψ(N−1/2)≤logN dan ARCH>.9 para todos N≥2,k≥1,u²≥256N.

Cauchy–Schwarz con ambos pesos tiene el factor e^−ηt y las dos normas opuestas correctas. WRN admite η negativo. Los cocientes de B_l y del coeficiente binomial difieren en (N−1)l≥0; la suma de series y la simplificación algebraica producen CENTERED con coste[(u²−η²)/(u²−4η²)]^(N−1/2). eta4 y u²≥256N hacen ese coste menor que exp(3/14)<14/11, uniformemente en N. El bound del peine<.16 incluye toda la suma real deΛ.

El polar beta, Jensen para la razón gamma, Bernoulli y el cociente2N/(4u²−1)≤4/2047 controlan todos los polares adversos por.001; los pares son favorables. Así W/norma²>739/1000>.7 es una desigualdad de la forma REAL completa en toda la región. GAIN es correcta pero no se usa como signo automático.

La distinción respecto JOINT_SCALE016 es mantener N/u² acotado y cancelar el coste lineal de pesos mediante ambos signos. No contradice el obstáculo a u fijo,N/u² creciente. No se cubre k0 por un momento inverso divergente.

## 2. Límite del puente de tasas crecientes — APROBADO

Revisado `POWER_SCALE_BRIDGE_LIMIT_029.md`. La densidad espectral está normalizada. Su máximo enτ²/u²=k/N decrece con k: la comparación de punto medio convexa da ψ′(x)≤1/(x−1/2), cuya integral proporciona la derivada logarítmica estrictamente negativa declarada. El límite k0 y Jensen para la razón gamma dan HEIGHT<sqrtN/(u sqrtπ).

Por ello toda mezcla positiva normalizada del dominio u≥C√N tiene altura≤1/(C√π). En I=[−C/8,C/8] su masa es<1/4. Un átomo objetivo fijo u0 con2M−3>256u0²/C² tiene masa>3/4 en I por Chebyshev. La distancia L1 es por tanto>.5. El argumento usa un intervalo, no un valor puntual; también excluye conos no normalizados cuya masa tienda a1.

Ésta es una obstrucción a reemplazar automáticamente el cono positivo del puente017 por esta región restringida. No excluye otros puentes, identidades con estructura adicional o controles directos. La nueva región no certifica ventana T ni signo global.


## 3. Región incluida k0, u≥64√N — APROBADA

Revisados `POWER_BOUNDARY_WEDGE_029.md` y `tools/power_boundary_wedge_029_verify.py`; ejecución independiente PASS. La comparación de coeficientes usa exactamente(N−1)(l−1)≥0 y vale también N1. La expansión WRN requiere a>0 yη²/a²<1, válidos para ambos signos del peso cuandoη<u/2. El producto bilateral y eta15 dan coste≤exp(675/4096)<6/5 uniformemente; el bound de todo el peine<1/5000 conservaΛ real.

El lower global deψ trasladado desde5/4 tiene el recíproco exacto1/(τ²+1/4). La densidad k0 tiene máximo Gamma(N)/[u√π Gamma(N−1/2)]; Jensen y la integral del recíproco2π producen Erecip<4√N/u. El momento logarítmico beta, ψ(1/2)>−2 yψ(N−1/2)≤logN dan Elog|τ|>log(u/√N)−1, también N1. Los extremos elementales de log(32/π) y las constantes certificadas dejan ARCH>.45. La monotonía de ARCH en k extiende ese bound sin momento inverso singular.

El polar base satisface la cota Bernoulli uniforme p0<1/4. Como a≥4095N, p1<1/(4·8190); el cociente de magnitudes decrece con k y su extremo N1 también es menor que1. Todos los polares adversos quedan controlados por.001, conservando los pares positivos. Así W/norma²>.45−.0002−.001>.4 para TODOS N≥1,k≥0,u≥64√N. Es signo de la forma real completa, no una extrapolación de las constantes de N pequeños.

## 4. Cierre de alcance

La región k≥1 tiene margen>.7 bajo u²≥256N; la región con borde k0 tiene margen>.4 bajo u²≥4096N. Se trata de teoremas uniformes en todos los órdenes, no campañas de certificados. A tasa31.5 la primera sólo cubre N≤3 ya conocidos y la segunda no añade órdenes; no cambia el resto de la tabla fija. La obstrucción del cono de densidades impide trasladar automáticamente el puente positivo017 a estas regiones, sin excluir otros mecanismos. No hay nueva ventana T ni signo global del Paper47. Root coincide en las revisiones independientes de los tres memos.
