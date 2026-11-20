# Diferencias de filas con un extremo común

Para una fila binomial de extremo superior n, escribir Y_k(n) para su masa en potencias propias (265), e incluir Y_0=0. Aquí se permite trasladar el extremo n. La distribución se toma primero en densidad natural para cada familia finita de longitudes. Se obtiene una cota para combinaciones firmadas cuyo coste depende de la separación entre longitudes.

**Ley límite.** Para cada primo p tomar un entero p-ádico U_p uniforme, independientemente de los demás. Para q=p^a definir C_k(q)=1 si U_p mod q < k mod q, y cero en otro caso. Esta fórmula es el acarreo por resta de k. Definir Y_k=Σ_{p,a≥2} log(p) C_k(p^a). Para k fijo la suma es finita casi seguramente porque Σ min(1,k/p^a) converge. La ley conjunta es la de las filas en densidad natural: truncando q≤M se aplica el teorema chino. Para M mayor que todas las longitudes, el coste de omitir una potencia en n≤X es, en proporción, a lo sumo k_max Σ_{M<q≤X}(1/q+1/X), salvo los primeros k_max enteros. El número de potencias propias hasta X es O(√X log X), por lo que la cola desaparece en el límite iterado. Esta aproximación vale incluso para probabilidades de conjuntos arbitrarios de valores del vector, pues el vector truncado coincide fuera del evento excepcional.

**Cancelación exacta.** Poner μ_k=Σ log(p){k/p^a} y Z_k=Y_k−μ_k. Para cada q, el acarreo cuenta múltiplos en (n−k,n] menos ⌊k/q⌋. Restar dos intervalos con extremo común y centrar da exactamente Z_{k+h}(U)−Z_k(U)=Z_h(U−k), donde se traslada cada coordenada en −k. Por invariancia de la ley, si V(h)=Var Z_h, la covarianza de dos filas es (V(k)+V(l)−V(|k−l|))/2.

**Tamaño de la diferencia.** Cuando h→∞,
   
    V(h) ~ κ √h log h,     κ=ζ(3/2)/(2π).

En los cuadrados solos la independencia entre primos da la suma de (log p)² φ(h/p²), con φ(u)={u}(1−{u}). En el tramo δ√h≤p≤A√h el teorema de los números primos, por sumación parcial, da tras normalizar por √h log h el límite (1/2)∫_δ^A φ(1/y²)dy. Las colas normalizadas tienen limsup O(δ+1/A) por θ(t)≪t y φ(u)≤min(1,u). Para evaluar la integral usar φ(u)=Σ_{m≥1}(1−cos(2πmu))/(πm)² y u=1/y². Tonelli e integración por partes dan ∫₀^∞(1−cos(2πmu))u^(−3/2)du=2π√m (integral de Fresnel). Así se obtiene κ.

Dentro de cada primo los niveles altos pueden depender unos de otros. La norma cuadrática del bloque centrado a≥3 es ≤log(p)Σ_{a≥3}min(1,√h/p^(a/2)). Para p≤h^(1/3) esto es O(log(2h)) por la cola geométrica. Por encima es O(log(p)√h/p^(3/2)). Sumando cuadrados sobre primos independientes, aun mayorando por todos los enteros, la varianza de esos bloques juntos es O(h^(1/3)log²(2h)). La desigualdad triangular en L² permite reincorporarlos sin afectar el equivalente.

**Combinaciones firmadas.** Para longitudes k_i en un intervalo entero de diámetro d≥1 y coeficientes reales b_i de suma cero, restar a cada fila la de longitud mínima. Resulta

    ||Σ b_i Z_{k_i}||₂ ≪ (Σ |b_i|) d^(1/4) √log(2d).

La constante es independiente de la posición del intervalo y del número de filas. Por Chebyshev, si el lado derecho es o(√x), la proporción límite de traslaciones con error centrado superior a ε√x tiende a cero para todo ε>0 al crecer x. Se usa el centrado exacto y se toma primero la densidad para cada x. Para el ajuste de 262 se exige un extremo dentro de un rango finito y la reproducción simultánea de átomos prefijados. La densidad obtenida aquí no garantiza una traslación con esas propiedades. El signo global sigue abierto.

**Qué sobrevive si se fijan átomos.** En una progresión n≡r (mod M), las coordenadas de los primos que no dividen M siguen siendo independientes y uniformes por el mismo argumento de truncación (para M fijo, la cota de cola en densidad relativa sólo pierde un factor M). Si se reserva por separado toda la contribución de p|M, la varianza del incremento restante es a lo sumo V(h), exactamente por aditividad de varianzas entre primos. Por tanto la cota de combinaciones firmadas vale para el residuo incluso después de fijar cualquier número finito de congruencias compatibles, con la misma constante. Esto precisa el coste pendiente: en las filas del ajuste, para imponer un valor prescrito en q=p^a mediante congruencias hay que incluir ese primo en el bloque reservado. Al imponer todos los átomos, la estimación aleatoria ya no controla el bloque donde se decide el ajuste.
