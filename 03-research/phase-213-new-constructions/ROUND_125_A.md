# Las masas de los primos verdaderos entre cuartas potencias conservan la tasa

Para el bloque de 121 sustituir f(v)=c_F(log v)/√v por f(m⁴) en cada celda [m⁴,(m+1)⁴), tanto en la suma prima como en la integral. Se conserva la tasa Δ del exceso positivo para los espacios de 122. Por tanto basta la masa prima ponderada por log p en cada celda (para los dos bordes se usa su intersección con el bloque). A diferencia de 123 esto usa la fórmula explícita para los primos. El modelo de 124 explica por qué la positividad y las masas, sin la relación aritmética con los ceros, no daban la misma comparación. El signo requiere aún probar el techo subexponencial de la matriz redondeada.

**Estimación local.** Sea Θ=1/2+Δ. En una banda [R,2R] intersecada con el bloque, poner q(v)=f(v)−f(m⁴) dentro y cero fuera. Con F unitario y ||F'||≤B tenemos |q|≤A=C(1+B)R^(−3/4), J=ceil(C R^(1/4)) saltos incluidos extremos, derivada por tramos en y=log(v/R) acotada por C A J. Esto sigue de |c'|≤B. La variación total es O(AJ). Afirmamos

    |∫ q(v)(dψ(v)−dv)| ≪ (1+log R)^C R^Θ A √J + O(AJ(1+log R)^C).

Usar la fórmula explícita truncada de ψ a altura H comparable a R², con error uniforme O(log^C R) sobre [R,2R]. Es la versión clásica con término de cercanía a la potencia prima más próxima acotado por O(log R) (para los otros enteros se suma la serie armónica); se puede tomar una altura buena en [R²,2R²]. Cambiar la convención de medio salto cuesta O(log R). Integrando por partes contra q, el residuo cuesta O(AJ log^C R); esto incluye asignaciones de bordes, pues cada salto de ψ es ≤log(2R). La parte suave de la fórmula truncada da integrales R^ρ M(ρ), donde

    M(s)=∫ q(R exp y)exp(sy)dy.

**Suma hasta H.** Para −1≤σ≤2, w(y)=q(R exp y)exp(σy) tiene soporte de longitud acotada, amplitud O(A) y la misma cota de derivada por tramos. Por tanto para 0<h≤1,
    
    ||w(·+h)−w||₂² ≪ A² min(1,Jh).

En el conjunto que cruza saltos usar su longitud O(Jh); fuera usar la derivada y, para Jh≤1, (Jh)²≤Jh. En alturas L≤|t|≤2L, L≥2, Plancherel con h=1/L da ∫|M(σ+it)|²dt ≪ A² min(1,J/L), pues |exp(ith)−1| está separado de cero. Vale asimismo en la banda ensanchada una distancia 1/4 variando la constante. Por subarmonicidad de |M|² en discos de radio 1/4 alrededor de cada cero y multiplicidad local O(log(2L)), la suma de |M(ρ)|² en la banda es ≪ log(2L) A² min(1,J/L). Cauchy–Schwarz con O(L log(2L)) ceros da suma de módulos ≪ A log(2L)√J. Sumando las bandas hasta H se obtiene la afirmación local. El factor R^ρ se sacó antes del muestreo, lo que permite usar R^Θ sin ensanchar el exponente.

**Aplicación.** Cambiar de ψ a primos cuesta O(A√R log² R) por las potencias propias. La comparación aritmética de cuadráticas por banda queda así en O((1+B) log^C(2R) (1+R^(Δ−1/8))). Sumando diádicamente hasta X se obtiene en norma O((1+B)log^(C+1)(2X)(1+X^(Δ−1/8))). El factor 1+B es subpolinómico en X para los espacios de 122. Si Δ>0, la tasa del error es estrictamente inferior a Δ; si Δ=0, el error es subexponencial en T. La desigualdad variacional para el mayor autovalor y 121–122 prueban la conservación anunciada sin suponer RH. La dependencia de la cota intermedia en Θ no es una estimación numérica de su valor.

**Antecedentes y alcance.** 121 ya usa la fórmula explícita para descartar primos pequeños; 123 interpola con dos momentos; 124 conserva masas de una medida general. Aquí el ahorro 1/8 proviene de sumar las transformadas del error discontinuo sobre los ceros usando el número de saltos y Plancherel. No se ha obtenido una estimación del signo de la parte que queda.
