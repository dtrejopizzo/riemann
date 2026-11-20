# Contracción en rectángulos de altura verificada mediante pesos explícitos de Taylor

Sea G=3·10¹² la altura verificada que usa el dato Z2 del paper 47. Para cada ε>0 con ε<1/2 hay una misma construcción de pesos (independiente de ε) con banda polilogarítmica tal que

    sup_(1/2+ε≤Re s≤1, |Im s|≤G−2) |H_X(s)| ≪_ε (log X)^(−c_ε),    c_ε>0.

El filtro de observación de 320 también conserva esta cota. Las constantes pueden depender de G. No se proporciona un umbral numérico práctico para X. El argumento usa la verificación de ceros ya disponible; no extiende esa verificación ni la ventana de soporte T. A diferencia del supremo a todas las alturas de 322, aquí la distancia a la recta 1/2 puede ser cualquier ε fijo y la altura está limitada.

**Polinomio fijado sin conocer las ordenadas.** Poner L=log X, m=⌊log L⌋, D=m, B=⌈exp(20m)⌉. Con f=1/ζ desarrollar f(s+1) hacia s mediante el polinomio Σ_(j=0)^m (−1)^j f^(j)(s+1)/j!. Como Re(s+1)>1, el coeficiente de n^(−s) en esta expresión es exactamente

    μ(n) e^(−u) Σ_(j=0)^m u^j/j!,    u=log n.

Para cada s del rectángulo, el disco de centro s+1 y radio 1+η, con 0<η<min(ε/2,1/4), está a la derecha de 1/2 y a altura menor que G. Por Z2 no hay ceros allí; el polo en 1 es removible para f. La unión de los discos es compacta. Por Cauchy el error al evaluar el desarrollo en s es O_ε((1+η)^(−m)), uniforme. Lo mismo vale en una vecindad del rectángulo reduciendo η. Más generalmente basta esta condición de discos, sin hipótesis a alturas mayores.

**Brecha, soporte y masa armónica.** Reemplazar el peso por μ(n) para n≤m, y por cero para n>B. Para los primeros, la cola de Poisson de orden mayor que m con media ≤log m es ≤(e log m/(m+1))^(m+1) por Chernoff, por lo que el coste es superexponencialmente pequeño en m. En los últimos, la probabilidad de orden ≤m es ≤4^m exp(−3u/4) por Markov aplicado a 4^(−Y) para Y de Poisson de media u. La cola absoluta en Re s≥1/2 es por tanto O(4^m B^(−1/4)). Llamar A₀(s) al polinomio así obtenido; por el cálculo anterior A₀(1) es exponencialmente pequeño ya que f(1)=0. En el índice 2m sumar a su coeficiente −2m A₀(1). El nuevo polinomio A cumple A(1)=0 y las tres modificaciones mantienen un error O_ε(exp(−c_ε m)) en el rectángulo y en una vecindad fija del punto 1. La cota de Cauchy en esa vecindad controla también la derivada del error; por tanto ζ(s)A(s)−1 satisface el mismo tipo de cota incluso cerca del polo removido en el producto.

**Paso a las dilataciones reales.** Con a los coeficientes de A, g=1*a, N=C₀ B L² y el corte ψ de 320, poner H_X(s)=Σ_(D<n<2N) g(n)(1−ψ(n/N))n^(−s). Hay brecha hasta D, Σ|a(d)|=O(B) y Σa(d)/d=0. Las estimaciones de 320 dan el mismo criterio unilateral para el saldo aritmético: sustituir 2D por B en la derivación de Poisson de orden ⌈L⌉, pues B es polilogarítmico y N/B=C₀L². Para el símbolo, el muestreo centrado de ψ(v/N)v^(−s) en 321 da 1+H_X=ζA+O_K(L^(−K)) en el rectángulo: para orden fijo j el resto es ≪_(G,j) N^(1−σ)(B/N)^j, y j se puede tomar suficientemente grande pues B≤2L²⁰. Esto concluye la cota. El factor positivo de observación en 322 tiene módulo ≤exp(1) en toda la región.

**Dónde deja de informar el resultado.** Bajo RH el mismo polinomio funciona en cada rectángulo compacto interior de cualquier altura fija por la prueba de discos. Un cero exterior fijo ρ, de existir por encima de la verificación, fuerza H_X(ρ)→−1 por Poisson, cualquiera sea el valor de A(ρ). De ahí que el control en todos los rectángulos a cualquier altura sea ya equivalente a RH. La mejora es una localización efectiva del mecanismo de aproximación en altura y el retorno a una banda polilogarítmica; no es una nueva región libre de ceros ni un control uniforme cuando la altura crece con X.
