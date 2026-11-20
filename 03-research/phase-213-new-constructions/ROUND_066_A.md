# Dos cortes de signo opuesto para el total de semiprimos

Frente a las subfamilias de 061 y las filas de 065, aquí se incluyen TODOS los productos de dos primos distintos bajo un corte macroscópico. Sea x=L² y sea A(c,x) la suma del representante filtrado de 063 sobre p<q, pq≤cx, contando una pendiente por producto (para las cuatro, multiplicar por cuatro). Para todo c>0 fijo,
    
    A(c,x)/(x log log x / log x) → I(c) = ∫₀ᶜ J(1/√v) dv.

Hay cortes fijos c₊, c₋ para los que I(c₊)>0>I(c₋). En particular incluso una cota unilateral O(√x) falla en algún prefijo completo, también sobre x=j⁴.

**Conteo.** El número B(y) de pq≤y con p<q es asintótico a y log log y/log y. En efecto, sumar π(y/p)−π(p) para p≤√y. La resta es O(y/log²y). Para cualquier ε fijo entre 0 y 1/2 la parte p>y^ε es O_ε(y/log y) por Chebyshev y sumación parcial. Para p≤y^ε el PNT uniforme en y/p y la suma recíproca de primos (asintótica a log log y por PNT y sumación parcial) encierran el coeficiente principal entre 1 y 1/(1−ε); hacer ε↓0. Así, normalizando por B(x), las masas de los puntos pq/x convergen sobre intervalos compactos de (0,∞) a longitud. Por aproximación escalonada vale también para el peso continuo J(1/√v).

**Máscara y borde inferior.** Escribir T=√(x/pq). En δx≤pq≤cx, T≤1/√δ; sustituir la máscara de 060/063 por J(T) cuesta O_δ(p⁻²+q⁻²) por pareja, aplicando |J(z)|≪z² y sumando las dos series geométricas. El signo exterior μ(pq) es positivo. El coste agregado es O_{δ,c}(x/log x), pues p≤√(cx), π(cx/p)≪_c x/(p log x) y Σp⁻³ converge. Para pq≤δx usar |J(z)|≪z^(1/2) en toda la semirrecta. La serie completa en potencias de p y q tiene módulo ≪T^(1/2), con constante uniforme por p,q≥2. Debajo de √x la suma es O(x^(5/8)) contando todos los enteros. Por encima, en cada bloque y/2<pq≤y, B(y)≪ y log log x/log x; el coste dividido por B(x) es O((y/x)^(3/4)). La suma diádica hasta δx da O(δ^(3/4)). Tomando primero x→∞ y después δ↓0 resulta el límite.

**Los dos signos.** Escribir w(v)=J(1/√v). Los momentos de órdenes cero y uno de 063 dan ∫w=∫w log v=0 al cambiar variables. Así I(c)=−∫_c^∞ w, e integración por partes da ∫₀^∞ I(c) dc/c=−∫w(v) log v dv=0. Los bordes I(c)log c se anulan por el decaimiento de 063 en ambos extremos. I no es idéntica a cero pues I'=w y J no es nula. Por continuidad I toma ambos signos.

El resultado descarta extender 065 a todos los cortes pq≤cx mediante una cota uniforme del saldo de semiprimos por separado. El contraejemplo corresponde al prefijo del representante filtrado. La representación global incluye tanto el resto de productos como la cola en pq; la propia identidad ∫w=0 cancela el coeficiente principal al completar el integral. La asintótica para c fijo no estima el resto de esa cancelación a escala √x.
