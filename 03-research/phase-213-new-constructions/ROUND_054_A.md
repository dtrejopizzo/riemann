# Segunda diferencia de escalas y eliminación de todas las filas pequeñas

048 usaba 2A(x)−A(2x). En 049 el corte de las filas exigía añadir coeficientes para equilibrar las densidades de sus progresiones. Aquí se usa la segunda diferencia de la misma dilatación. Su cero doble anula dos densidades, lo que permite cortar directamente en la potencia marcada q.

Escribir P(x)=Σ Λ(n)V(n/x), A(x)=x∫V−P(x), x=j⁴, L=√x, y=4x. Usar V,g,χ de la construcción de orden dos de 047, K=C₀ L(log x)² con C₀ fijo suficientemente grande y U(k)=1−χ(log(k/K)). Sea α(v)=1−4·1_{2|v}+4·1_{4|v}, que vale −3 en v≡2 módulo 4 y uno en las demás clases. Entonces el signo global equivale a que eventualmente

    Σ_{L<q<eK} Λ(q) Σ_{v≥1} α(v) U(qv) Σ_{m≥1} μ(m)V(qvm/y) ≥ −C√x.

Todos los índices son finitos por los soportes. En particular v≤eK/q=O((log x)²); los factores k=qv y m siguen en los rangos próximos a la raíz de 049. Aquí no se eligen compensaciones dependientes de los primos de una banda.

**Identidad y orientación.** Poner B(x)=4A(x)−4A(2x)+A(4x). Para x grande Σ α(k)log k g(k/y)=−B(x) por la identidad de divisores de 045 y por Σ g(dk/y)=V(d/y)=0 para d=1,2,4. La suma de los términos principales lineales también es cero. Con c₁=1,c₂=−4,c₄=4, tenemos

    α(k)log k = Σ_{q|k}Λ(q)α(k/q)+E(k),     E(k)=Σ_{d|k, d=1,2,4} c_d log d.

En efecto la suma en q es Σ_{d|k} c_d log(k/d) con los mismos tres índices d. Tanto Σ c_d/d como Σ c_d log d/d se anulan; así α y E tienen densidad media cero.

**Corte.** Reemplazar la suma plena α(k)log k por la suma con U introduce O(√x): aplicar en cada una de las tres progresiones la estimación superior de 047 al logaritmo (incluido log K), con escalas y/d,K/d y la misma función física en k. Las integrales suman cero por la primera identidad de densidad. Para E, la suma plena contra g ya es cero y el mismo argumento en la parte alta, sin logaritmo, tiene densidad cero por la segunda identidad. Su suma con U es por tanto O(√x).

En cada fila q≤L la suma plena en v de α(v)g(qv/y) es Σ_d c_d V(dq/y)=0 para x grande. En la parte alta las integrales se cancelan por la primera identidad de densidad y las tres cuadraturas cuestan O((y/q)exp(−c√(K/(4q)))). Sumar con Λ(q) cuesta a lo sumo Cy log x exp(−c√(K/(4L)))=O(√x) por Chebyshev y la elección de C₀. El criterio exhibido es, pues, −B(x) con error bilateral O(√x).

**Vuelta al signo.** Bajo el signo |A(x)|=O(√x) por 047. En sentido inverso, una cota inferior para la suma da B(x)≤C√x en j⁴. La combinación normalizada B(exp r)exp(−r/2) tiene segunda derivada O(exp(r/2)), por 047 aplicado a las tres traslaciones fijas. La interpolación en 4log j extiende la cota superior a toda la cola. Si 2f(x)−f(2x)≤C√x y f(x)=o(x), la iteración de 048 da f(x)≤C√x/[2(1−1/√2)]. Aplicarlo primero a f(x)=2A(x)−A(2x), después a f=A. Ambas hipótesis o(x) siguen del PNT con V fijo. Así 047 devuelve el signo global.

**Alcance.** La segunda diferencia de escalas y la inversión de divisores son herramientas conocidas. La cancelación simultánea de las dos densidades elimina las filas pequeñas de este criterio sin la corrección de 049. La desigualdad inferior sobre las filas restantes sigue abierta. La elección de C₀ se hace una vez, no varía con j.
