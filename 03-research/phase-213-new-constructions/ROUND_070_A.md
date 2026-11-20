# Qué filas completas se pueden pagar según su cofactor de primos grandes

Usar exactamente las filas U_m de 069. Fijar B>1 y 0≤θ<1, y poner y=(log x)^B. Para m libre de cuadrados escribir t_y(m) para el producto de los primos de m mayores que y (producto vacío 1). Sea A(x) la suma de |U_m(x)| sobre todos los m con t_y(m)≤x^θ. Entonces

    limsup_{x=j⁴→∞} log(1+A(x))/log x = 1−(1−θ)/B.

La cota superior vale también para x continuo. Si B<2 y θ<1−B/2, el sector completo cuesta o(√x); tras retirarlo sólo quedan numeradores cuyo cofactor de primos grandes excede x^θ. Para θ>1−B/2 falla el control por módulos a escala raíz. El exponente crítico por sí solo no decide la igualdad.

**Cota superior.** Escribir m=s t con los primos de s a lo sumo y. En la cota de 069 a abscisa σ=1−1/B∈(0,1), la suma sobre t≤x^θ de su peso es O_σ(x^(θ(1−σ))) por la estimación media de allí. La suma sobre todos los s libres de cuadrados cuesta ∏_{p≤y}(1+p^(−σ)w_p), con w_p=(1−p^(−σ))^(−2). Su logaritmo es O_σ(1+y^(1−σ)/log y) por Chebyshev y sumación parcial. Como y^(1−σ)=log x, este factor es x^o(1). Multiplicando por x^σ resulta el exponente anunciado.

**Una familia donde se ve el tamaño real de las filas.** Sea k₀(v)=U_1(v) el núcleo físico de K de 069. Es continuo, no idénticamente cero por su transformada, y se anula en (0,v₀) para algún v₀>0 por el soporte inferior del representante y sus promedios. Elegir 0<A<C con |k₀|≥c₀>0 y de signo constante sobre [A,C]. Si x/m pertenece a ese intervalo y todos los primos de m exceden C/v₀, se tiene exactamente
    
    U_m(x)=μ(m) k₀(x/m).

En efecto, desarrollar las series de potencias de los factores locales (1−u+u²)^(−1) de 069 en Re s>1. Todos los términos salvo el constante evalúan k₀ en x/(mn)<v₀, porque n contiene algún primo de m. Esto evita inferir una cota inferior a partir del mayorante de Euler.

**Conteo a escala comparable a x.** Tomar X grande y Y=(log X)^B. Para θ>0 fijar 0<τ<θ; para θ=0 tomar τ=0. Formar m multiplicando k primos distintos en [Y/3,Y/2] y, cuando τ>0, otro primo en [X^τ,2X^τ]. Tomar k=(1−τ)log X/(B log log X)+O(1), entero. Todos los productos son distintos por factorización única. Uniformemente log m=(1+o(1))log X. Hay N≫Y/log Y primos disponibles en el primer intervalo por PNT y N/k→∞. Usando binom(N,k)≥(N/k)^k y contando los primos del segundo intervalo, el número de m es al menos
    
    X^(τ+(1−τ)(1−1/B)+o(1)).

En un intervalo para m de razón fija ρ>1, con ρ<C/A, hay ese mismo exponente de productos: partir su rango en O(log X) intervalos de razón ρ. Para el intervalo elegido [M,ρM], escoger x en un subintervalo interior de [AρM,CM] de longitud comparable a M. Contiene una cuarta potencia para X grande. Así x/m∈[A,C], log x∼log X, los primos pequeños elegidos son menores que (log x)^B y el primo adicional, si existe, es menor que x^θ. Se aplica la identidad de la fila anterior. Sumar los módulos, y hacer τ↑θ para θ>0, prueba la igualdad de exponentes. Ajustar k en una unidad permite obtener exclusivamente filas de cualquiera de los dos signos en la construcción, en sucesiones eventualmente distintas de x.

**Alcance.** El conteo de muchas elecciones de primos tiene antecedentes en 043. La cota para sus filas completas y la identidad que hace efectivo el contraejemplo usan específicamente el representante de 069. El resultado admite numeradores de tamaño comparable a x y todos los denominadores. La obstrucción inferior atañe a los módulos y a subfamilias seleccionadas de signo fijo; no establece el signo de la suma de las filas de toda la región ni del complemento.
