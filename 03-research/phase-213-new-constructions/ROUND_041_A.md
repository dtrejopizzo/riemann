# Pérdida óptima de un minorante divisorial positivo a escala variable

En 040 se descartó el perfil fijo. Aquí los coeficientes b_n≥0 pueden elegirse de nuevo para cada x>1. En n=1 se puede fijar b₁=0. Sea w(t)=min(t,t^(−2)), como en 040. Para un tope entero N en el soporte, maximizar

    x^(−1/2) Σ_{n≤N} b_n log n

bajo las restricciones Σ_{n≤N:p^e|n}b_n ≤ w(p^e/x) para cada primo p y e≥1. Sólo se necesitan restricciones donde Λ no se anula. Por la identidad de divisores, cada familia admisible minora Q(x) de 039. Llamar M_N(x) al máximo.

**Solución exacta.** Poner d_{p,e}=min_{1≤i≤e} w(p^i/x). Entonces

    M_N(x)=x^(−1/2) Σ_{p^e≤N} (log p)d_{p,e}.

En efecto las masas acumuladas por los múltiplos de p^e son decrecientes en e, así que d_{p,e} las domina término a término. La descomposición de log n da la cota superior. Para alcanzarla, en cada cadena truncar d a cero desde la primera potencia mayor que N y poner b_{p^e}=d_{p,e}−d_{p,e+1} con esos valores truncados. En los demás enteros poner cero. Telescopar satura todas las cotas simultáneamente. Con soporte infinito la misma construcción alcanza el límite M∞, por monotonía y convergencia de la suma dominada por Q(x). Entre sucesiones de soporte finito sin tope prefijado ese límite es un supremo.

**Cuánto cuestan las restricciones.** El primer nivel e=1 conserva íntegro el peso de cada primo admitido. Para los cuadrados d_{p,2}=min(p/x,x²/p⁴). Separando en p=x^(3/5), la cota de Chebyshev θ(t)=O(t) y sumación parcial dan

    x^(−1/2) Σ_p log(p) d_{p,2} = O(x^(−3/10)).

En efecto los dos tramos quedan acotados por constantes por x^(−3/2)(x^(3/5))² y x^(3/2)(x^(3/5))^(−3). Para e≥3 la contribución retenida, al ser a lo sumo la plena, es O(x^(−1/6)) por 039. Estas cotas valen para todo N. De 039, el peso pleno de los cuadrados tiende a 2/3; por ello

    Q(x)−M∞(x) = 2/3 + o(1).

**Tope finito.** Si N≥x y N→∞, los primos mayores que N quedan íntegramente en la rama decreciente del peso. Por los cálculos anteriores,

    Q(x)−M_N(x) = 2/3 + o(1) + x^(3/2) Σ_{p>N} (log p)/p²,

con el primer o(1) uniforme en N≥x. Por el teorema de los números primos y sumación parcial, la cola es asintótica a 1/N. Así, para cualquier λ>0 fijo, N∼λx^(3/2) da pérdida 2/3+1/λ+o(1). En general, para mantener acotada la pérdida es necesario y suficiente que N≥c x^(3/2) eventualmente para algún c>0. Si N<x a lo largo de una subsucesión, ya la cola de primos >x cuesta orden √x; para N≥x rige la fórmula anterior.

La precisión aditiva O(1) requerida en 039 sí es alcanzable por una minoración positiva si se permite elegirla a cada escala. La construcción exacta depende de los primos y conserva su suma del primer nivel. Lo pendiente es una cota inferior de M_N(x) por (3/2)√x−O(1) con N del tamaño indicado; calcular la pérdida no suministra esa cota. La operación divisorial ya figuraba en 040 y N_BUILD022. El cotejo no localizó este problema de optimización por cadenas con esta función de peso.

## ¿Se pueden sustituir los coeficientes en primos por productos de dos primos?

Imponer ahora b_p=0 para cada primo p. Denotar el nuevo máximo finito por M_N^comp. Para mantener Q(x)−M_N^comp(x)=O(1) es necesario y suficiente que N≥c x^(9/4) eventualmente, para algún c>0. Para la suficiencia basta usar productos de dos primos distintos. La afirmación trata del soporte de los coeficientes; su elección todavía utiliza las capacidades de los primos individuales.

**Necesidad.** De no existir tal c, hay una subsucesión con N=o(x^(9/4)). Fijar δ>0, P=δ x^(3/2) y considerar los primos en (P,2P]. Un entero compuesto ≤N que contenga uno de esos primos p contiene exactamente uno y con exponente uno, pues P²>N para x grande. Su cofactor tiene algún divisor primo q≤N/P. Por tanto la suma de masas asignadas a los primos de esa banda es a lo sumo

    Σ_{q primo≤N/P} w(q/x) = o(√x/log x).

En efecto y=N/P=o(x^(3/4)); si y≤x^(2/3) basta la suma de todos los enteros dividida por x. Para y>x^(2/3) se usa Σ_{q≤y}q≪y²/log y. Multiplicar por log(2P)/√x da o(1) de contribución a la banda. Su capacidad completa ponderada, en cambio, es x^(3/2)Σ_{P<p≤2P}log(p)/p²∼1/(2δ) por el teorema de los números primos. El déficit en cada fila es no negativo, así que el liminf de la pérdida en esa subsucesión es al menos 1/(2δ) para cada δ fijo. Una pérdida acotada es imposible.

**Suficiencia.** Basta construir para N=⌊c x^(9/4)⌋, pues aumentar N conserva factibilidad. Elegir X=λ x^(3/2), con λ>0 suficientemente pequeña en función de c. Se van a saturar las capacidades de primer nivel d_p=w(p/x) para *todos* los primos p≤X. Los primos p de √N<p≤X se recorren de mayor a menor. Asignar su masa d_p a productos pq, repartiéndola entre primos q≤y=min(x,N/p) con capacidad disponible. Esos socios son menores que √N y los conjuntos permitidos crecen durante el recorrido. Basta verificar en cada paso que la demanda acumulada hasta el p actual no excede la capacidad total de sus socios.

La demanda es a lo sumo C x²/(p log p) por la cota de Chebyshev y sumación parcial. La capacidad disponible *antes de empezar todo el recorrido* en q≤y es al menos c₁ y²/(x log y), por la cantidad de primos en (y/2,y]. Aquí y crece uniformemente. Si y=x, la demanda es o(x/log x) porque p>√N. Si y=N/p<x, la razón demanda/capacidad es a lo sumo C′ x³ p/N² ≤ C′ x³ X/N², que es menor que uno al elegir λ suficientemente pequeña. Así se completa el reparto sin exceder capacidades.

Quedan las demandas residuales de los primos ≤√N. Su suma L es ≫x/log x: sólo en [x/2,x] había ese orden de masa y el recorrido anterior consumió O(x²/(√N log N))=o(x/log x). Cada demanda residual es ≤1. Para x grande ninguna supera L/2. Dividir un círculo de longitud L en arcos consecutivos con esas longitudes; emparejar cada punto con el punto opuesto. Casi ningún par tiene los dos extremos en el mismo arco. La longitud emparejada entre dos arcos da un coeficiente no negativo b_pq (contar cada par una sola vez), con suma en cada primo exactamente su demanda residual. Los productos son ≤N. Este segundo reparto usa socios distintos y no activa restricciones para p². Así se alcanza como valor exactamente la contribución de los primos ≤X. Su pérdida frente a Q tiende a 2/3+1/λ por 039 y el cálculo de cola anterior. Esto es una cota superior del déficit óptimo para este soporte restringido; no identifica su constante óptima.

En particular, en la escala de soporte x^(3/2) de la primera parte, los compuestos por sí solos no pueden certificar la cota inferior buscada. Al permitir la escala x^(9/4) se puede reproducir la suma sobre primos, pero su estimación uniforme sigue siendo necesaria.
