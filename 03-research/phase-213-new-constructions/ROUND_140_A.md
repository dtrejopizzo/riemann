# Un peso positivo de Möbius calculable con tres sumas de Liouville

Poner A(z)=Σ_{k≥1}(−1)^(k+1)exp(−k²z) y W(z)=A(z)−A(4z). Para cada z>0 se tiene W(z)>0. A escala X≥2 hay una identidad exacta

    F(X)=Σ_r μ(r)W(r/X)
        =Σ_n λ(n)(1−3·1_{4|n}+2·1_{16|n})exp(−n/X).

Los múltiplos de 16 desaparecen; los múltiplos de 4 que no lo son de 16 tienen coeficiente −2λ(n). La identidad funciona con los signos verdaderos. En el lado de Möbius basta la banda X/(K log X)≤r≤K X log X, con error absoluto o(√X) y una constante fija K suficientemente grande.

**Demostración.** La identidad de Jacobi da A(z)=(1−θ₄(0,e^(−z)))/2. En el producto de θ₄ los factores (1−e^(−2jz))(1−e^(−(2j−1)z))² son positivos y crecientes en z; el producto es estrictamente creciente. De aquí el signo estricto de W. Al agrupar por n=rk² en la serie de A, la convolución de μ con el indicador de cuadrados es λ. Dar peso −1 a los k pares en vez de +1 resta 2·1_{4|n}λ(n/4). La segunda escala de A resta una copia a n múltiplo de 4. Usar λ(n/4)=λ(n) y, cuando corresponde, λ(n/16)=λ(n). Los cambios de orden son absolutos para X fijo.

Por alternancia A(z)≤e^(−z). Por Poisson para la gaussiana, θ₄(0,e^(−z))=√(π/z)Σ_{m∈ℤ}exp(−π²(m+1/2)²/z). Así W(z)≪z^(−1/2)exp(−π²/(16z)) para 0<z≤1. Las dos colas de la suma en r se pagan usando |μ(r)|≤1: la superior cuesta O(X exp(−K log X)), y la inferior O(X polylog(X) exp(−(π²/16)K log X)) por monotonía del mayorante para z pequeño. En particular sirve K=10 para X grande.

**Qué estimación cerraría el signo.** Basta un techo F(X)≪ε X^(1/2+ε) unilateral eventual para todo ε>0, equivalente al mismo techo en la banda recortada. En Re s>1 la Mellin bilateral en X con peso X^(−s−1) es Γ(s)η(2s)(1−4^(−s))/ζ(s), η(z)=(1−2^(1−z))ζ(z). Ningún factor del numerador se anula en Re s>1/2. El eje real allí es regular y el tramo X<1 es entero al transformar por el decaimiento exponencial. Landau da la suficiencia como en 139. Bajo RH la cota bilateral se deduce de M₀(t)≪ε t^(1/2+ε) por Abel; las derivadas de W en los dos extremos tienen el mismo decaimiento exponencial con factores de potencia, por las dos series anteriores.

**Qué aportó la segunda alternancia de 139 y por qué se usa aquí una sola.** El coeficiente doble ε*ε ya figura en 054/055 y su factor η² en 057. Para G(y)=Σ_{i,j}ε(i)ε(j)exp(−(yij)²), alternar la función positiva decreciente A(y²i²) da 0<G<1/2. Pero la diferencia G(y)−G(2y) no hereda un signo de ese argumento. Una sola alternancia proporciona simultáneamente el peso estrictamente positivo, la cancelación exacta de clases diádicas de λ y la localización por ambos lados sin hipótesis sobre μ. Las identidades theta, la transformada de η y el método de Landau son antecedentes, no una demostración de cancelación en la banda restante. Comparar también 047 y 131 para otras localizaciones.
