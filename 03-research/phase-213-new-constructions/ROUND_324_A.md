# Localización hasta la recta crítica sin suponer ceros simples

Poner m=⌊log log X⌋. En el rectángulo cerrado K dado por 1/2≤Re s≤1, |Im s|≤G−2 con G de 323, hay una modificación de sus pesos con el siguiente resultado. Sea Z el conjunto finito de ceros críticos hasta altura G−1 en módulo. Para todo entero k≥1,

    |H_X(s)| ≤ C_(k,G)(1+m dist(s,Z))^(−k) + O_G(exp(−c_G m)),   s∈K.

Los pesos son los mismos para todo k. En particular el módulo es <1/2 fuera de discos de radio C_G/m alrededor de los ceros, para X suficientemente grande, incluso sobre la recta crítica. Las constantes no están calculadas. En los propios ceros el multiplicador tiende a −1. Esto describe dónde se pierde la contracción del símbolo en la zona verificada, sin extender esa zona.

**Cambiar el orden de Taylor.** Elegir w suave no negativa de integral uno y soporte compacto en (1,2). Promediar los polinomios de Taylor de 323 de grados enteros j con pesos w(j/m)/Σ_j w(j/m). Mantener μ(n) en n≤m y borrar n>B=ceil(exp(40m)). Las cotas de Poisson de 323 siguen uniformes para m≤j≤2m: por ejemplo la cola de soporte es O(4^(2m)B^(−1/4)). Corregir la masa en 2m como en 323, que cuesta exponencialmente poco porque en un entorno de 1 la serie de Taylor converge geométricamente. El símbolo corto con N=C₀ B(log X)² aproxima este polinomio multiplicado por ζ, menos uno, con error exponencial en m (Poisson de orden fijo suficientemente alto, B=O((log X)^40)). En una vecindad de 1 se usa la cancelación del polo como en 323. En consecuencia continúa siendo aplicable el criterio aritmético de 320 con banda polilogarítmica.

**Separar las singularidades.** Lejos de vecindades fijas de los ceros, los discos centrados en s+1 de radio 1 no contienen ningún cero: están a la derecha de 1/2, con posible tangencia sólo en s si Re s=1/2. Por compacidad se puede aumentar ligeramente el radio, siempre dentro de la altura verificada. Cerca de cada cero ρ∈Z que toca la zona considerada, escribir f=1/ζ como su parte principal más una parte regular. La segunda admite el mismo aumento del radio, tras reducir la vecindad, pues en el disco de centro 1+ρ y radio 1 el único cero era ρ. El error de Taylor regular es exponencial, uniformemente en el grado j≥m. La finitud de Z permite reunir las constantes.

**Qué aporta el promedio de órdenes.** Escribir δ=s−ρ y r la multiplicidad. Para (s−ρ)^(−1) el resto exacto del desarrollo de grado j desde s+1 es δ^(−1)(1+δ)^(−j−1). Para un polo de orden l≤r se aplica (−∂δ)^(l−1)/(l−1)! a ese resto; derivar conmuta con el truncamiento pues la traslación es de longitud fija. Al multiplicar por ζ(s), cada término es una unidad analítica acotada por una constante, por δ^(r−l+a), por un polinomio en j de grado a, y por (1+δ)^(−j−1−a), con 0≤a≤l−1. Esta descripción incluye los coeficientes de la parte principal.

Con v=(1+δ)^(−1) se tiene |v|≤1 y |1−v| comparable a |δ| en la vecindad derecha. Para un polinomio fijo P_a de grado a, la suma normalizada de w(j/m)P_a(j)v^j cuesta O_(a,b)(m^a(1+m|δ|)^(−b)) para todo b fijo. La cota trivial trata m|δ|≤1. En el resto multiplicar por (1−v)^b y trasladar índices; la suma absoluta de las diferencias finitas de orden b de los coeficientes normalizados es O(m^(a−b)), por suavidad y soporte interior de w. Tomar b≥k+r absorbe las potencias de m|δ|. Esto prueba el techo también en el límite δ=0 por continuidad.

**Perfil comprobable.** Para z fijo con Re z≥0 y ρ en el rectángulo, al evaluar en s=ρ+z/m se obtiene

    H_X(ρ+z/m) → −∫₁² w(u) exp(−uz) Σ_(a=0)^(r−1) (uz)^a/a! du.

En la fórmula diferenciada sólo sobrevive el polo de orden r. Su coeficiente cancela el factor principal de ζ; el coeficiente de la derivada distribuida da 1/a! y el polinomio en j es mónico de grado a antes de ese factor. Pasar de j/m a la integral es una suma de Riemann. El signo menos procede de H≈ζ T−1. En z=0 el límite es −1, lo que impide una contracción uniforme dentro de distancias o(1/m). Ni la prueba ni el perfil presuponen simplicidad. No se han obtenido nuevas ordenadas de ceros ni una desigualdad de signo por encima de la altura verificada.
