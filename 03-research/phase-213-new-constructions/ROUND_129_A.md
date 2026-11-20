# El resto factorial centrado desciende por debajo de la raíz

En el promedio de 127 poner X=M⁴ y D=floor(M^(2+1/16)). Existe una densidad explícita fija b(v), igual a uno para v mayor que una constante, tal que para dE=dψ−b(v)dv y

    K(v)=M⁻¹ Σ_{M<m≤2M} Σ_{d≤D} μ(d) floor(m⁴/(dv)),

se tiene ∫K dE=o(M²) incondicionalmente. Para v>16X/D se tiene K(v)=W(v) de 128 por inversión finita. Así el defecto de la media de ψ sobre su término principal queda, con error o(√X), en la integral de (W−K)dE sobre v≤16X/D=O(X^(31/64)). La restricción es sobre el argumento de los átomos: el núcleo del resto puede ser grande y firmado.

**Calibración de los dos términos.** Denotar por γ la constante de Euler, escoger t>0 por cosh t=log(2π)/exp(γ)>1 y tomar a±=exp(γ±t). Definir b(v) como la media de los dos indicadores de [a±,∞). Para y≥3 suficientemente grande, con n=floor(y/a),
    
    ∫_a^∞ floor(y/v)dv=y H_n−an
      =y log y + (γ−log a−1)y + a/2 + O_a(1/y).

Esto sigue de H_n=log n+γ+1/(2n)+O(n⁻²); se cancelan los términos que contienen {y/a} a orden constante. Por divisores, ∫floor(y/v)dψ(v)=log(floor(y)!). Por Stirling y por la elección de las medias de log a y de a, la diferencia exacta tiene la expansión uniforme

    ∫floor(y/v)dE(v)=(1/2−{y})log y+O(1/y).

En particular el término constante independiente del redondeo se cancela antes de sumar en d. Usar solamente un corte a=exp γ dejaría una constante por término.

**Control cuártico.** Para d≤M se paga O(M log M) en total por la expansión. Para M<d≤D controlar el promedio ponderado de 1/2−{m⁴/d} en los prefijos M<m≤U≤2M. Para cada h≤floor(M^(1/8)), el denominador reducido de h/d cumple M^(7/8)≤q≤M^(33/16). En prefijos de longitud L≥M^(23/25), la desigualdad clásica de Weyl para el polinomio cuártico acota su suma exponencial por

    Oε(L^(1+ε)(1/q+1/L+q/L⁴)^(1/8)) ≪ε M^(1−7/64+ε).

Para prefijos más cortos usar la longitud. Erdős–Turán y la desigualdad de discrepancia para la función de variación acotada 1/2−{u} dan una suma en cualquier prefijo O(M^(23/25)+M^(7/8)+M^(1−7/64+ε)log M). Por Abel, introducir log(m⁴/d) cuesta O(log M). Tras dividir por M y sumar hasta D, resulta o(M²), ya que 2/25>1/16. Los restos de Stirling cuestan O(D²/M⁴)=O(M^(1/8)). Se usó |μ(d)|≤1, sin cancelación entre denominadores.

**Obligación aritmética resultante.** Puesto que ∫W b(v)dv=M⁻¹Σ m⁴−O(1) y la aportación media de las potencias propias es (7/3+o(1))M² por 127, se tiene

    M⁻¹Σ (θ(m⁴)−m⁴) = ∫_{v≤16X/D}(W−K)dE − (7/3)M² + o(M²).

Una cota superior de constante estrictamente menor que 7/3 para el limsup de esta integral dividida por M² bastaría para el signo. Se desconoce. La estimación de 128 sobre la pérdida bruta en una banda no acota esta integral centrada.

**Antecedentes.** 128 da la identidad factorial en una banda, 045 usa inversión divisorial y centrado, y 049–053 tratan errores de cuadratura aritméticos. El paso específico es cancelar simultáneamente los términos lineal y constante del coste factorial y pagar el diente de sierra de Stirling mediante la equidistribución cuártica, uniformemente más allá de d=√X. La prueba usa Weyl y Erdős–Turán como insumos clásicos.
