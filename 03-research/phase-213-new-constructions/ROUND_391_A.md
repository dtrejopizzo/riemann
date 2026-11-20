# Segundo cruce de la unión y un corte finito por debajo de la raíz

**Estado: PROVED, con revisión independiente del marcado doble, el perfil y la interpolación exacta.**

Con los z,E,J,L de 384 sea y=exp(L/u) con u en un compacto interior de (2,3). Entonces el saldo W de todos los enteros que tienen algún primo >y satisface uniformemente

    W(y)=(JxE/L²)[log(u−1)−1/(u−1)+o(1)].

El perfil cambia de signo en u₀=1+w donde w log w=1 (u₀≈2.7632). Es el negativo de la derivada, con el factor de escala apropiado, de la densidad de Buchstab en el tramo (2,3). La consecuencia para la suma aritmética exacta usa los momentos de la criba congelada de 384.

**Inclusión y exclusión.** Sean T₁ y T₂ los saldos marcados con j y binom(j,2), respectivamente, cuando hay j primos grandes. Los enteros con j≥3 cuestan O(x exp(−cL²)), incluso con marcas polinomiales en log n, pues y³ supera x por una potencia fija. Así W=T₁−T₂ con ese error. Como en 385, T₁∼JxE/L² por el momento congelado, válido aquí ya que log y y L−log y son comparables a L. En T₂ se extraen dos primos y permanece el signo positivo del marcado doble, multiplicado por el saldo del cofactor f de 384. Permitir p=q o un primo marcado que divida el cofactor cuesta O(x L³/y) para n≤x² por g(log(x/n))≪x/n, el factor cuadrado >y² y la suma armónica de los restantes factores. Para n>x² basta la cola gaussiana con O(log² n) multiplicidad.

Reemplazar ambas medidas primas por dt/log t como en 380, ahora con f en el integrando: |f(v)|+|f'(v)|≪exp v permite integración por partes en [y,x²] a coste O(x L³ exp(−c√L)) tras sumar o integrar el otro factor. Extender los límites superiores sólo afecta la cola gaussiana de argumento negativo. Por ello

    T₂=x ∫ exp(−v) f(v) H₂(L−v) dv + o(x/L²),
    H₂(D)=log((D−b)/b)/D para D>2b, cero por debajo; b=log y.

Para |v|≤L^(1/10), el intervalo entre L y L−v queda a distancia ≫L del quiebre 2b, y H₂''=O(L^(−3)) allí. Fuera de ese tramo se aplican la cola negativa y la cota de 384 para f en v≥L^(1/10); H₂ es O(1/L) globalmente. El término constante de Taylor integra a cero y el lineal a JE H₂'(L). El resto cuesta O(L^(−2.7)) tras integrar, como en 384. Así T₂=JxE[L/(L−b)−log((L−b)/b)]/L²+o(xE/L²), y restar da la fórmula.

**Reducción exacta con un solo peso fraccional.** Escoger dos extremos fijos de u a ambos lados de u₀ dentro de (2,3). Los dos estados contiguos del primer cruce de W en la lista de primos encierran cero. El salto está acotado por O(x/p), luego es o(xE/L²) en toda esa banda. El perfil uniforme fuerza log p/L→1/u₀. Si W toma el valor cero basta ese corte. En caso contrario sea λ∈(0,1) tal que (1−λ)W(p−)+λW(p)=0. La misma combinación convexa de C(p−) y C(p) vale S exactamente. En la representación de Mellin su producto es

    (1−λ p^(−s)) ∏_{z<q<p}(1−q^(−s)).

El mayor primo aquí es x^(1/u₀+o(1)), con 1/u₀≈0.362. A diferencia del corte próximo a √x, el coste trivial de redondear λ puede superar la raíz. La igualdad requiere conservar el peso; calcularlo exige los dos saldos aritméticos W. La localización asintótica del cruce no determina ese peso. Sigue faltando un techo de signo para el nuevo producto.

**Registro de revisión.** El marcado T₂ lleva binom(j,2), por lo que la extracción de dos primos se divide por2 y usa exactamente la densidad H₂ de380. El término lineal H₂(L−v)=H₂(L)−vH₂'(L)+… integra a+JEH₂'(L), pues el momento primero congelado es−JE. La derivada es H₂'(L)=[L/(L−b)−log((L−b)/b)]/L²; restarla de T₁ da log(u−1)−1/(u−1), con el signo anunciado. Para Buchstab, uω(u)=1+log(u−1) en(2,3), luego el perfil es exactamente−u²ω'(u). El quiebre D=2b queda a distancia≍L del punto de Taylor para u en un compacto interior, y las cotas de f de384 justifican uniformemente completar los dos momentos. Los términos con marcas repetidas cuestan xL³/y y la cola de tres primos tiene y³≥x^(1+c) con c>0 uniforme en ese compacto.

La selección sólo necesita que los estados extremos tengan signos opuestos y que cada salto sea o(xE/L²); no se supone monotonía de W en esta nueva banda. En el orden creciente de los primos los signos extremos van aquí de positivo a negativo. La localización log p/L→1/u₀ sigue de la unicidad del cero del perfil y su uniformidad, también para el estado izquierdo del salto. Finalmente C(p−) tiene producto A(s)=∏_{z<q<p}(1−q^(−s)), mientras C(p) tiene(1−p^(−s))A(s). La combinación con los mismos pesos1−λ,λ es por tanto exactamente(1−λp^(−s))A(s), sin invertir el peso terminal. Su integral vale S por W interpolado igual a0; no se reemplaza λ por una fórmula asintótica ni por un extremo.
