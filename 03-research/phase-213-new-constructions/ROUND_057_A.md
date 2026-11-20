# Cancelación de la diagonal por cocientes racionales en la forma de 056

Sea P entero libre de cuadrados y sumar la forma simétrica de 056 sobre los pares, incluida la diagonal, tales que sf(dm)|P. Con las convenciones de 056, para 0<δ<4 fijo, P≤(log x)^(4−δ) y cualquier A fijo positivo, el valor es

    C_diag L ∏_{p|P}(1−2√p/(p+1)) + O_{A,δ}(L/(log x)^A).

Aquí C_diag>0. Por tanto la parte de este bloque con d≠m tiene el mismo término principal con el producto menos uno. Si P recorre primoriales crecientes dentro de ese rango, su contribución fuera de la diagonal es −C_diag L+o(L). No hay restricciones de coprimalidad sobre el índice w.

**Valor de cada cociente.** Escribir d=at,m=bt con gcd(a,b)=1 y t=gcd(d,m). Si ambos valores de μ son no nulos, r=ab es libre de cuadrados, sf(dm)=r y μ(d)μ(m)=μ(r)μ²(t)1_{(t,r)=1}. En la variable u=t√r/L, al retirar los cortes U y d,m>D, la media de los dos logaritmos vale exactamente log u. El núcleo restante es F(u)=Σ_w β(w)V(u²w/4), común a todos los cocientes.

**Uniformidad de ese retiro.** Si falla uno de los límites inferiores o un U difiere de uno en el soporte de V, entonces u≤C√P/(log x)²≤C(log x)^(−δ/2). Para U esto se sigue de dw≤C L√P/u en el soporte, y análogamente para mw. Para los límites inferiores usar min(d,m)≥Lu/√P. En este intervalo la suma en w, para cada uno de los dos cortes por separado o sin corte, es O_N(u^N) para todo N fijo. La prueba diádica de 056 se aplica con w de tamaño comparable a u⁻²: en w=ij las derivadas del corte U(di j) o U(mi j) en el factor largo cuestan su escala inversa, uniformemente en d,m. Los logaritmos discretos cuestan a lo sumo O(log x). Hay como máximo 3^ω(P)≤P² cocientes y O(L) muestras t por cociente. Elegir N grande según δ,A prueba el error indicado.

La función f(u)=log(u)F(u) tiene soporte superior compacto y se extiende por cero con variación acotada en el origen: al aplicar u∂_u a V(u²w/4) la prueba de decaimiento rápido da las mismas cotas. El conteo elemental
     
    Σ_{t≤T,(t,r)=1} μ²(t) = (T/ζ(2))∏_{p|r} p/(p+1) + O(τ(r)√T)

se obtiene por la expansión μ²(t)=Σ_{k²|t}μ(k) y el conteo de coprimos por inclusión-exclusión. Así la sumación parcial de f(t√r/L) da para el cociente a/b el término C_diag L μ(r)/√r por ∏_{p|r}p/(p+1), con error O(τ(r)√L). La suma de esos errores cuesta √L veces una potencia fija de log x. Para cada p|P se puede omitir p, incluirlo en a o incluirlo en b. Multiplicar las tres contribuciones da el producto del enunciado. Sus factores están en (0,1), y el producto tiende a cero en primoriales crecientes por divergencia de Σ_p 1/√p.

**Signo de la constante.** Escribir η(s)=(1−2^(1−s))ζ(s), y V̂(s)=∫V(t)t^(s−1)dt. La transformada de Mellin de F en z es 2^(z−1)V̂(z/2)η(z/2)², por sustitución donde la serie converge absolutamente (Re z>2) y luego por continuación hasta z=1. El decaimiento demostrado para F y su soporte superior justifican la derivación en z=1. Por 044 el sombrero W(t)=t⁻¹W(1/t); así Ŵ' en 1/2 es cero. La ley de 047 tiene media 1/2, de modo que V̂'(1/2)=V̂(1/2)/2. La constante de 056 es por ello

    C_diag = V̂(1/2)η(1/2)² [log 2 + 1/4 + η'(1/2)/η(1/2)] / ζ(2).

Para s>0, η(s) es la esperanza de 1/(1+exp(−T)) con T de ley gamma de forma s y tasa uno, por la integral de la serie alternada. Su derivada es la covarianza de esa función con log T, estrictamente positiva porque ambas crecen estrictamente. Esto prueba el signo sin estimación numérica.

**Límite de la extrapolación.** Ya en los cocientes p/1 con p primo, la suma de los módulos de las constantes individuales diverge como serie: sus términos son C_diag√p/(p+1). En consecuencia la expansión por cocientes no admite una mayorante sumable de los módulos de sus contribuciones normalizadas, uniforme al pasar al límite en x. La agrupación del producto anterior es esencial. Falta controlar las parejas con sf(dm) que no divide P. La evaluación extiende la diagonal de 056; usa herramientas clásicas de densidad y productos de Euler.
