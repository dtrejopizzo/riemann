# La cancelación de incrementos alarga las ventanas de coste pequeño

Sea Ω(X)=(log X/log log X)^(1/3). Para alguna constante fija κ>0, poner L=X^(2/3)exp(κΩ(X)). Se obtienen dos techos incondicionales:

* En la subsucesión de enteros n de 237, con X=n, X⁻²∫_X^(X+L) F(x)² dx→0 para el MISMO coseno de 236.
* Para TODOS los X suficientemente grandes, el mínimo cuadrático local de 231 en [X,X+L] también tiende a cero. En este enunciado basta incluso la recta de pendiente uno e intercepto cero para el conteo desde X.

El factor que alarga L supera toda potencia fija de log X pero es X^o(1). La ganancia proviene de cancelar el principal de los incrementos del conteo; la regla de 237 basada sólo en contar enteros no da estos techos.

**Estimación importada y uniformidad.** Sea E(z)=θ(z)−z. Para X^(5/8)≤v≤X/2, uniformemente en y∈[1,2],

    |E(y(X+v))−E(yX)| ≪ v exp(−c Ω(X))

con alguna c>0. Se usa Thorner–Zaman, sección 1.2, consecuencia de su teorema 1.1 para intervalos de Hoheisel. En su notación tomar módulo 2, clase 1, extremo superior z=y(X+v), longitud yv y A=1. Para ε=1/48 se tiene 7/12+ε<5/8, por lo que yv≥z^(7/12+ε)log z eventualmente. Todos los primos del intervalo son impares. Las cantidades Ω(z) y Ω(X) son comparables y se puede reducir c. Para 0≤v<X^(5/8) el conteo de enteros da O((v+1)log X). [Thorner y Zaman, sección 1.2](https://arxiv.org/pdf/2108.10878).

**Dónde se cancela el término principal.** Con f(y)=cos(2πy) y el convenio de extremo izquierdo abierto, ∫₁² f(y)dy=0 y f(1)=f(2)=1 dan por partes

    F(x)=E(2x)−E(x)−∫₁² f'(y)E(xy)dy.

Al restar el valor en X del valor en X+v se obtienen sólo incrementos del mismo E, incluidos ambos bordes. La constante de integración cuesta a lo sumo 2+∫|f'|. Para 0≤v≤L se deduce

    |F(X+v)−F(X)| ≪ X^(5/8)log X + L exp(−c Ω(X)).

En X=n con |F(n)|≪log n de 237 se puede usar el mismo techo para |F(n+v)|. Multiplicar su cuadrado por L/X² cuesta
O(X^(−1/12+o(1))+exp((3κ−2c)Ω(X))). Elegir por ejemplo κ=c/3 da convergencia a cero. En el segundo enunciado el residuo de la recta propuesta es directamente E(X+v)−E(X). Le vale la misma estimación para todo X sin elegir un cruce, y la minimización sólo puede mejorarla.

**Interpretación.** La longitud relativa L/X=X^(−1/3+o(1)) no satisface la hipótesis log(1/h)=o(log log X) de 231 y 236. El techo para estas longitudes ya vale en ambas alternativas para RH, por lo que no resuelve la obligación de las ventanas detectoras. No se da un valor numérico para κ ni una mejora fija del exponente 2/3.
