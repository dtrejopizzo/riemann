# Intervalos largos de exceso y muestreo en una sucesión de bandas

Sea E la discrepancia prima de 109 y Θ=sup Reρ. Si Θ>1/2, para cualesquiera ε>0, 0<δ<1 y 1/2<α<Θ, toda banda [X,X^(1+ε)] suficientemente grande contiene un intervalo [y,y+y^(1−δ)] donde E(t)>t^α en todo punto. También contiene otro intervalo de ese tipo con E(t)<−t^α. No se exige un cero de parte real Θ.

**Existencia de picos.** Escribir Z(x)=−Σρ x^ρ V(ρ). Por 112, E(x)=Z(x)+O(√x): la contribución de cuadrados es O(√x) por Chebyshev en soporte fijo, las potencias superiores son O(x^(1/3)log²x) y las triviales son o(1). Para J(v)=exp(−v/2)Z(exp v) se cumplen las hipótesis de 115, pues V no se anula en la franja abierta y es O((1+|γ|)⁻²). Para cualquier α'<Θ con α'>1/2 se puede elegir d entre α'−1/2 y Θ−1/2. Aplicar 115 con media (1+ε/2)log X y semianchura relativa suficientemente pequeña para permanecer estrictamente dentro de la banda y para que d/(1+semianchura)>α'−1/2. Así existen puntos y de cada signo con ±Z(y)>y^α', separados de los extremos de la banda por un factor que crece con X.

**Variación entre puntos.** Para 0<u≤1/2,
    
    |Z(y(1+u))−Z(y)| ≪ y^Θ u log²(2/u).

En efecto |(1+u)^ρ−1|≪min(1,u(1+|γ|)), por integración en el logaritmo y por la cota trivial. En |γ|≤1/u sumar (1+|γ|)⁻¹ con el conteo N(T)≪T log(2T), y por encima sumar γ⁻². En particular para 0≤u≤y^(−δ) la pérdida es O(y^(Θ−δ)log²y), por la misma división a altura y^δ. Tomar α' estrictamente entre max(α,Θ−δ) y Θ. Esta pérdida y O(√y) quedan absorbidos por y^α', incluso comparando t^α para todo t del intervalo. Esto prueba ambas afirmaciones.

**Criterio por muestras.** Basta que haya ε,δ>0 fijos (δ<1), una sucesión X_j→∞ y en cada [X_j,X_j^(1+ε)] una malla que incluya los dos extremos y tenga pasos consecutivos de longitud ≤C t^(1−δ) desde su extremo izquierdo t, con E≤C'√t en todas sus muestras. Bajo RH esto vale por 109. Si falla RH, aplicar el teorema con δ/2: el intervalo positivo tiene longitud y^(1−δ/2), mayor que cualquier hueco que lo contenga. Incluye una muestra cuyo exceso supera C'√t. Por ejemplo sirve cualquier malla de potencias enteras n^k, para cada entero fijo k≥1 (recortar a las bandas o escoger extremos en la malla). La prueba no identifica una malla donde la cota aritmética ya se conozca.

**Cotejo.** 039/044 usan cuartas potencias, 090 usa una familia no magra de pasos para tests distintos y 115 produce puntos en bandas de potencias. Aquí la variación controlada por la abscisa real Θ convierte los picos cercanos al exponente supremo en intervalos de longitud y^(1−δ); sería insuficiente una estimación de variación que usara siempre el exponente 1. El intervalo sigue teniendo longitud relativa tendiente a cero.
