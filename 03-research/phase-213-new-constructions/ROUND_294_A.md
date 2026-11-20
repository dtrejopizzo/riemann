# Signo del bloque con un primo mayor que la raíz y cancelación con el complemento

Para la autoconvolución b_t de 292 definir B_t(s)=Σ b_t(n)n^(−s) en Re s>1 y por prolongación cerca de 1. Para 1/2≤α<1 fijo, uniformemente en 1≤t≤2, se obtiene incondicionalmente

    Σ_(n≤x; P⁺(n)>x^α) b_t(n) = −2 B_t''(1) x/log³x + O_α(x/log⁴x),
    Σ_(n≤x; P⁺(n)≤x^α) b_t(n) = +2 B_t''(1) x/log³x + O_α(x/log⁴x),

con P⁺(1)=1 y min_t B_t''(1)>0. El término principal no depende del corte α dentro de este rango fijo. El obstáculo para el techo de raíz es la diferencia entre dos contribuciones firmadas grandes incluso después de agrupar cada una.

**Momentos con signo.** De 292,

    B_t(s)=G_t(s)² L(s−it,χ)L(s+it,χ)/ζ(s)².

Los coeficientes de G_t² convergen absolutamente con peso n^(−σ) en cada σ>1/2 uniformemente en t: los factores locales de la corrección cuadrada son (1+(cos θ_p−1)z)²(1−χ(p)p^(it)z)(1−χ(p)p^(−it)z)/(1−z)², con z=p^(−s), salvo el factor finito en 3 que se ajusta por la extensión. El término lineal se cancela para p≠3 y la cola local absoluta cuesta O_σ(p^(−2σ)). La serie de B_t es por tanto una convolución de esa corrección, dos copias de μ y las sucesiones χ(n)n^(±it). Para todo R>0,

    Σ_(n≤z)b_t(n) ≪_R z/log^R(2z).

En efecto, μ satisface el techo para todo R por el PNT cuantitativo, y las dos sucesiones periódicas torcidas tienen sumas parciales O(log(2z)) por partes. La fórmula de la hipérbola con corte √z conserva los ahorros logarítmicos arbitrarios para sus convoluciones finitas: cada suma corta en módulos con peso 1/n cuesta una potencia fija de log z por mayoración divisorial. Para la corrección final dividir su convolución en d≤√z y d>√z; la cola armónica absoluta gana una potencia por convergencia en σ=3/4 y basta la mayoración divisorial del otro factor. Todas estas cotas son uniformes en t.

Por sumación parcial los momentos Σ b_t(m)(log m)^j/m convergen a (−1)^j B_t^(j)(1) con cola O_(j,R)(log(2M)^(−R)) después de M. Los dos primeros momentos son cero, y B_t''(1)=2G_t(1)² |L(1+it,χ)|²>0. Los factores locales en 1 son reales positivos para la corrección cuadrada; sólo podría anularse el de p=2 si u_2=2, excluido por 1≤t≤2. La cola converge uniformemente y L no tiene ceros en Re s=1. Por compacidad el piso es uniforme.

**Sumar el primo grande.** Existe un único primo p>x^α en los enteros del primer bloque, siempre con exponente uno. Escribir n=mp, m≤x^(1−α); luego b_t(n)=−2b_t(m)u_p. En los primos el PNT con resto clásico, en las dos clases módulo 3 y por partes contra p^(it), da Σ_(p≤z)u_p=li(z)+O_R(z/log^R(2z)) uniformemente. Al sustituir esta suma en los dos extremos de (x^α,x/m], los errores cuestan O_R(x/log^R x) reduciendo el exponente previamente si hace falta, pues Σ_(m≤x)|b_t(m)|/m≪log^C(2x) por los factores locales. El extremo inferior incluye li(x^α)Σ_(m≤x^(1−α)) b_t(m), despreciable a cualquier orden logarítmico para α fijo. Queda −2Σ_m b_t(m)li(x/m).

**Cálculo del primer término.** Poner L=log x, M=exp(√L). Para M<m≤x^(1−α) la cota de sumas parciales y la derivada de li(x/m), de módulo x/(m² log(x/m)), dan un coste O_R(x/L^R), eligiendo suficientemente alto el ahorro inicial. Para m≤M usar la expansión de li:
    
    li(x/m)=(x/m) Σ_(k=1)^8 (k−1)!/(L−log m)^k + O(x/(m L⁹)).

La suma armónica absoluta de |b_t| hasta M es O((log(2M))^4), por el factor local (1+2/p)². En cada denominador desarrollar en log(m)/L hasta grado 16. El error sumado es O(x/L⁴), ya que |log(m)/L|≤L^(−1/2). Sustituir por los momentos completos cuesta O_R(x/L^R). Sólo el par k=1, grado 2 contribuye en orden L^(−3); los grados 0 y 1 se anulan exactamente y los momentos fijos siguientes son acotados. El coeficiente resultante es B_t''(1). Esto prueba el primer equivalente y la cota para el sumatorio completo da la segunda fórmula.

**Límite para la ruta.** Borrar el bloque del primo grande por ser negativo deja un complemento positivo de orden x/log³x. Integrar en frecuencia tampoco elimina ese término, pues el coeficiente tiene un piso positivo en todo [1,2]. A precisión logarítmica se identifica explícitamente qué se compensa; queda abierta la cota a precisión de raíz para el saldo. A diferencia de 293 no se estima aquí la masa de cada paridad por separado: se evalúa el saldo aritmético dentro de cada bloque.
