# Supresión bilateral de escalas en el resto factorial

Con las convenciones de 129 poner D=floor(M^(33/16)), V=M^(1/32)=X^(1/128). Se puede reemplazar el núcleo K por otro explícito K* tal que

    A(M)=∫_{V<v≤16X/D}(W−K*) dE − (7/3)M² + o(M²).

La parte v≤V se paga incluso en valor absoluto respecto de dψ+b(v)dv. Las dos cotas de escala se cumplen simultáneamente para la misma fórmula. La reparación no requiere ninguna estimación cancelatoria para μ.

**Dos coeficientes de corrección.** Conservar c_d=μ(d) hasta D. Poner S=Σ_{d≤D}μ(d), H=Σ_{d≤D}μ(d)/d y añadir c_{2D}=S−4DH y c_{4D}=4DH−2S. Entonces Σc_d=Σc_d/d=0 y Σ|c_d|≪D log(2D). Definir K* como K con estos coeficientes. Las dos dilataciones nuevas se anulan por encima de 16X/D, donde K=W. En la integral factorial completa se aplica 129 a los dos nuevos índices: la prueba allí da por índice grande Oε(M^(−2/25+ε) log²M + D/M⁴), también hasta 4D porque sus cotas de denominador admiten factores constantes. Multiplicar por O(D log D) sigue dando o(M²). Por tanto ∫K* dE=o(M²).

**Extremo inferior.** Para todo v≥1 se obtiene exactamente

    K*(v)=Σ_d c_d (1/M) Σ_{M<m≤2M} (1/2−{m⁴/(dv)}).

Los índices d≤M cuestan O(M) en módulo. Para M<d≤4D y v∈[1,V] basta ahora tratar el promedio completo de longitud M: ya no aparece el peso logarítmico de Stirling. Para h≤M^(1/8) aproximar h/(dv) por p/q mediante Dirichlet con Q=floor(M³), en términos reducidos, |q h/(dv)−p|≤1/Q y q≤Q. El numerador es positivo pues h/(dv)≫M^(−33/16−1/32)>1/Q para M grande. Así q≥dv/(2h)≫M^(7/8). En Weyl cuártico el paréntesis 1/q+1/M+q/M⁴ es O(M^(−7/8)); Erdős–Turán da para la media del diente de sierra Oε(M^(−7/64+ε)log M+M^(−1/8)). Esto es uniforme incluso en v real y en los átomos donde la parte fraccionaria se anula.

Por Chebyshev, la masa de dψ+b(v)dv hasta V es O(V); ambas medidas se anulan debajo de 1 (a_->1). Como |W|≤1, el coste absoluto inferior queda acotado por

    Oε(V (1+M+D log²M M^(−7/64+ε))) = o(M²),

ya que 1/32+1/16−7/64=−1/64. Esto prueba la fórmula mediante 129. No implica una cota para la zona central: allí ha cambiado el peso, incluidas las dos dilataciones correctoras.

**Cotejo.** R162_801 ya contiene la identidad factorial exacta y su lectura por Stirling. 047 usa regularización del peso y localiza otra cuadratura con sumas internas de Möbius. Aquí se mantienen las muestras crudas de 127; la cancelación exacta de dos sumas de coeficientes permite retirar los átomos de argumento pequeño y la densidad de ese mismo intervalo en norma absoluta. El objetivo pendiente sigue siendo acotar superiormente el resto central de esta representación.
