# El coste exacto fuera de la diagonal, incluso con peso igual al mcd

Sea P_off(κ) la suma con valores absolutos término a término de 326 sobre n≠d, multiplicando cada término por (n,d)^κ. Para h=exp(−am), a>0 fijo y 0≤κ≤1 se tiene

    lim P_off(κ)^(1/(2m)) = 2 exp(−a/2)       si a≤2,
                           = a exp(1−a)      si a≥2.

En particular, para a≥log 4 el techo uno fuera de diagonal se conserva incondicionalmente hasta κ=1. Para a<log 4 persiste la tasa absoluta excesiva aun en κ=0.

**Techo.** En el bloque X≤n<2X de 331, para dos múltiplos distintos de g se cumple g≤|n−d|≤C hX. Por tanto sólo hay bloques X≥1/(Ch). Mayorar el peso por la suma de g^κ sobre los divisores comunes y aplicar el conteo por g de 331. La suma Σ_{g≤ChX}g^(κ−2) cuesta O(log(2X)) incluso en el extremo κ=1. Tras AM–GM y simetría el techo es una constante por

    h/(m!)² Σ_{X diádico ≥1/(Ch)} (log(2X))^(2m+1)/X.

Por la comparación integral de 331 esto cuesta a lo sumo una constante por h/(m!)² veces la integral de u^(2m+1)exp(−u) desde am−O(1) hasta infinito. Para a≤2 usar la integral completa (2m+1)!. Para a>2 la derivada logarítmica del integrando es (2m+1)/u−1 y en todo el tramo es ≤−c_a para m grande. La integral cuesta a lo sumo el valor inicial dividido por c_a. Stirling da los dos techos indicados.

**Piso.** Con t=max(2,a) tomar X=⌈exp(tm+√m)⌉ y H=⌊c₀hX⌋ como en 332. Tanto X como H crecen aun en t=a. El conteo de 332 da ≫ XH pares coprimos con ambos factores libres de cuadrados y K≥1/2. Todos tienen peso de mcd uno. Con l_m(n)≥(log X)^m/((m!)(3X)^(3/2)) en el bloque, la raíz inferior es al menos t exp(1−(a+t)/2), que coincide con ambos techos.

**Cancelación firmada en el régimen pendiente.** Para 0≤κ<1, la mejora de 333 también admite la potencia q^κ fuera de diagonal:
    
    Σ_q q^κ |S_q| ≪_(a,b,A,κ) h binom(2m,m) m^(−A)

en todo el rango de 333. En efecto, en la inversión de pesos usar |c_g|≤g^κτ(g). La cola de 331 cuesta en unidades de h binom(2m,m) a lo sumo O_κ(G^(κ−1)log(2G)); se obtiene por sumación parcial. Tomar G=m^B con B>(A+1)/(1−κ). En la parte corta se suman a lo sumo G^(1+κ)(1+log G) unidades del error uniforme de 333; elegir el exponente de ahorro por encima de A+B(1+κ)+2. Este último argumento no da el extremo κ=1. Para a<log 4 falta convertir el ahorro de potencias en una mejora exponencial.
