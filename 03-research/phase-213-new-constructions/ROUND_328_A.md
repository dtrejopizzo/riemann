# La diagonal domina incluso al ensanchar la ventana crítica

Con el núcleo de 325, denotar por E_m[h] la energía firmada a anchura h y por Δ_m su diagonal. Para todo 0≤b<1/50 fijo,

    h=4^(−m)m^b   ⇒   E_m[h] ∼ Δ_m ∼ 1/(2ζ(2)√(πm)).

En particular se resuelve el equivalente en el borde a=log 4 y persiste en ventanas más anchas por un factor que tiende a infinito. Para a fijo con 0<a<log 4 también se mejora la tasa de 327 a E_m(a)/P_m(a)≪_a m^(−1/50)log m. El exponente procede del teorema de intervalos cortos usado, sin pretensión de optimalidad.

**Estimación cuantitativa sin discretizar los extremos variables.** En la ventana crítica ensanchada fijar log 4<c<2<C y trabajar en bloques diádicos [Y,2Y] de la zona cm≤log x≤Cm. Para h=exp(−am) fijo en exponente basta en cambio a<c<2<C. En ambos casos H=⌊hY/m²⌋ crece exponencialmente y log H, log Y son comparables a m. Definir M_H(n)=H^(−1)Σ_(1≤j≤H) μ(n+j). Se tiene uniformemente

    (1/Y) Σ_(Y/2≤n≤3Y) |M_H(n)|² ≪ m^(−1/50)log m.

En efecto la media larga de μ en cada bloque es O_A(m^(−A)) por el PNT cuantitativo. Para λ entre m^(−1/100) y 1 el término aditivo O(log log H/log H) y los extremos de la suma corta cuestan o(λ). El teorema 1 de Matomäki–Radziwiłł, aplicado con su parámetro proporcional a λ, limita la proporción excepcional por O(λ^(−2)m^(−1/50)) más un término superpolinómicamente pequeño, pues H^(c'λ) crece al menos como exp(c''m^(99/100)). Integrar 2λ por esa proporción; por debajo de m^(−1/100) usar la cota uno. Un número acotado de bloques cubre el rango indicado. [Teorema 1, pp. 1015–1016](https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p06-p.pdf)

En la suma local con peso η(log(x/n)/h), sustituir μ(n) por M_H(n) cuesta O(H/(hY)) después de normalizar por hx. En efecto, al cambiar n por n+j la diferencia de los pesos es O(j/(hY)) y está soportada en O(hY) enteros, por suavidad y soporte compacto. Para los pesos nuevos, Cauchy–Schwarz mayoriza el cuadrado del promedio normalizado por O((hY)^(−1)Σ |M_H(n)|²), con n a distancia O(hY) de x. Al integrar en x∈[Y,2Y], cada n interviene en longitud O(hY). Esto transfiere la estimación cuantitativa sin pagar un factor por el número de posibles extremos. Sustituir l_m(n) por l_m(x) cuesta otro O(h) en el promedio normalizado, como en 327.

**Separación de los dos tamaños de enteros.** Por la identidad de Gram, el tramo central contribuye a E_m[h] a lo sumo O(m^(−1/50)log m · h binom(2m,m)). En el caso crítico ensanchado esto es O(m^(b−1/50)log m /√m)=o(Δ_m). La diagonal se concentra en log n próximo a m, mientras que el peso del recuento de pares distintos se concentra en log n próximo a 2m. Como c>log 4>1, la porción de la diagonal incluida en el tramo central de la integral de Gram es exponencialmente pequeña respecto de Δ_m (también desplazando el borde en h). Fuera de ese tramo, la masa absoluta de los pares distintos es exponencialmente pequeña respecto de h binom(2m,m): para cada n hay O(hn) vecinos distintos; usar la media de cuadrados de los dos pesos y la cola gamma de 327, con los extremos ampliados en h. Por no negatividad del núcleo esta cota sirve igualmente para porciones de la integral de Gram. Así, fuera del centro queda Δ_m+o(Δ_m). La suma de las dos regiones prueba el equivalente.

Para a fijo por debajo de log 4, Δ_m y las colas anteriores son despreciables respecto de P_m(a) incluso tras multiplicar por cualquier potencia fija de m; el techo central y 327 dan la tasa afirmada. Esta ganancia es polinómica en m. Para el criterio completo se necesita una ganancia exponencial en las ventanas a=1/j, por lo que el signo global continúa abierto.
