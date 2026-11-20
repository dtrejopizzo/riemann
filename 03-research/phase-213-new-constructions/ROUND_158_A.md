# La resta del peso elemental conserva el error crítico por unidad de inclinación

Con E_d,J_d,G,b de 157 y E_0(u)=G(u)+1/2, existen c,C,u₀>0 absolutos tales que

    c d u ≤ E_d(u)−E_0(u) ≤ C d u   para 0≤u≤u₀, 0<d≤1/4.

Por tanto, al aproximar las sumas interiores en la diferencia A_d−A_0 de 155 por sus respectivas integrales y constantes, el error del prefijo r≤Y es positivo y de orden d Y³/x² para Y grande y Y≤x√(u₀/π), uniformemente incluso si d depende de x. La tolerancia O(d√x) de 155 se alcanza exactamente en orden de magnitud en Y=x^(5/6). Hacer d pequeño no compra rango a esa tolerancia.

**Prueba uniforme.** Sea h=d/2. Por Poisson G es suave hasta cero, con G'(0)=0 y derivadas de orden positivo que se anulan allí. En t grande G'(t)=O(t^(−3/2)). La fórmula de mezcla de 157 da

    (J'_d(u)−G'(u))/h =
       [(1/Γ(1+h)−1)/h] G'(u)
       + [1/Γ(1+h)] · {∫₀¹ [G'(u+t)−G'(u)] t^(h−1)dt
                          + ∫₁^∞ G'(u+t)t^(h−1)dt}.

El miembro derecho se extiende continuamente al rectángulo 0≤u≤1, 0≤h≤1/8: G'' está acotada en [0,2], de modo que la diferencia en la primera integral es O(t), y en la segunda hay una mayorante integrable uniforme. El cociente con gamma tiene singularidad removible en h=0. Para u=0 el resultado es ∫₀^∞ G'(t)t^(h−1)dt/Γ(1+h), estrictamente positivo para cada h por 157. La compacidad en h da un mínimo positivo. Por continuidad conjunta los valores siguen separados de cero para 0≤u≤u₀ y están acotados por arriba. Integrar en u desde cero demuestra la cota, pues E_d(0)=E_0(0)=0. La estimación del prefijo sigue de Σ_{r≤Y}r²b(r)≍Y³ en 157.

**Escala del peso elemental solo.** Para Y=k x/√log x con k>0 fijo, el error sin inclinación satisface

    Σ_{r≤Y} b(r) E_0(π(r/x)²) = x^(1−π/k²+o(1)).

Por la serie dual, en r≤Y se tiene E_0(π(r/x)²)=(x/r)Σ_{n≥1}exp(−πn²(x/r)²). Su valor en Y es x^(−π/k²+o(1)), y es creciente en r. Esto y la masa O(Y) dan la cota superior. Para el límite inferior usar [(1−η)Y,Y] de masa ≍_η Y y evaluar el primer término en (1−η)Y. Tomar primero x→∞ y luego η→0 prueba el exponente. Así el peso sin inclinación permite prefijos de orden x/√log x (con k<√(2π)) a coste O(√x), pero la resta normalizada (E_d−E_0)/d conserva un término cuadrático en r/x. Esta diferencia explica por qué transferir directamente la precisión del peso elemental a la inclinación pierde rango.

**Decisión.** 157 trataba d fijo y el error sin restar; sus constantes no resolvían esta pregunta conjunta en d y x. El resultado descarta una posible cancelación dentro del prefijo de la diferencia centrada. La contribución del resto de índices y su interacción con el centrado global siguen abiertas. La escala crítica aquí es la de la estimación uniforme de 155; su recíproca para un d fijo no presupone uniformidad adicional.
