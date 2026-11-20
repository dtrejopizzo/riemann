# Filas de numerador reducido hasta potencias menores que la raíz

En el representante de 060 cada pendiente a/b cuenta una vez, con a,b coprimos y r=ab libre de cuadrados. Construimos un criterio equivalente en que, para todo η fijo entre 0 y 1/2, se pueden retirar todas las filas con a≤x^(1/2−η), sumando el módulo del saldo de cada fila completa, a coste o(√x). El denominador recorre todo su rango. El umbral se aplica al numerador reducido, no a un índice previo a reducir el cociente.

**Representante.** Para D H(x)=H(x/4), tomar
     
    U(x)=(1−4^(1/3)D)(1−4^(1/4)D) Σ_{k≥1} S(x/k⁶).

La suma es localmente finita por el soporte inferior de S. El signo global equivale a U(j⁴)≤Cj² eventualmente. Bajo el signo, S satisface la cota bilateral raíz de 060 y Σk⁻³ converge. Para la vuelta, las dos derivadas logarítmicas de U y U mismo son O(x) por 060 y Σk⁻⁶<∞, de modo que la interpolación superior entre cuartas potencias de 060 conserva la escala raíz. En Mellin el multiplicador respecto de S es ζ(6s) (1−4^(1/3−s))(1−4^(1/4−s)). Es holomorfo y sin ceros en Re s>1/2. La transformada de U es regular en todo el eje real s>1/2 por 060; Landau sobre C√x−U(x) en una cola extiende la holomorfía a ese semiplano, exactamente como en 060. Dividir por el multiplicador conserva esta holomorfía, y el criterio de detección de polos de 060 da el signo. Este argumento verifica la vuelta unilateral sin suponer que la inversión por Möbius respete desigualdades.

**Fila completa.** Fijar un numerador libre de cuadrados m. Para cada producto libre de cuadrados r divisible por m hay exactamente un denominador admisible, b=r/m. Denotar por U_m la contribución así obtenida, con el mismo filtro de escala aplicado antes de sumar filas. Es una partición de las pendientes ordenadas: las distintas orientaciones de un mismo producto se cuentan con sus multiplicidades originales. Si F es la Mellin de una copia por producto de 068, la Mellin de U_m en Re s>1 es
     
    K(s) μ(m)m^(−s) ∏_{p|m} (1−p^(−s)+p^(−2s))^(−1),
    K(s)=F(s) ζ(6s) (1−4^(1/3−s))(1−4^(1/4−s)).

En cada primo obligado se reemplaza la opción local 1−u/(1+u²) por −u/(1+u²), con u=p^(−s). Su cociente da el factor escrito. Las permutaciones de sumas en este semiplano convergen absolutamente como en 067. En K la media en sextas potencias cancela el denominador ζ(6s) de 068. Las diferencias eliminan los polos en 1/3 y 1/4. El polo en 1/2 ya se cancelaba por el centrado. La fórmula de 068 muestra entonces que K es entera y decrece más que cualquier potencia en altura en cada franja vertical fija.

**Uniformidad.** Fijar 0<σ<1. En Re s≥σ los dos ceros de 1−u+u² tienen módulo uno; por factorización cada factor local inverso queda acotado por w_p=(1−p^(−σ))^(−2). Para todo m la inversión sobre Re s=σ da
    
    |U_m(x)| ≤ C_σ (x/m)^σ ∏_{p|m} w_p.

Además Σ_{m≤Y}∏_{p|m}w_p ≤ Y∏_p(1+(w_p−1)/p) ≪_σ Y: desarrollar el producto en divisores y usar w_p−1=O_σ(p^(−σ)). Sumación parcial da para M≥1
     
    Σ_{m≤M} |U_m(x)| ≪_σ x^σ M^(1−σ).

Para M=x^θ, 0≤θ<1/2 fijo, escoger 0<σ<(1/2−θ)/(1−θ); el exponente θ+(1−θ)σ es estrictamente menor que 1/2. El criterio equivalente se reduce por tanto a la cota superior para Σ_{m>x^θ} U_m(j⁴), con x=j⁴. En particular entran productos grandes e incluso filas con cualquier número admisible de primos en el denominador.

**Cotejo y límite.** 054–056 tratan índices antes de reducir y 059–060 productos reducidos pequeños. La fila de aquí atraviesa todos los productos múltiplos de m. El paso nuevo respecto de 068 es combinar la condición de divisibilidad exacta con un promedio que elimina su denominador ζ(6s) y dos diferencias que eliminan los residuos. La constante depende de σ; esta cota no alcanza θ=1/2. Por simetría vale el enunciado para columnas completas. Retirar simultáneamente filas y columnas exigiría controlar su intersección. El saldo complementario y la ventana siguen abiertos.
