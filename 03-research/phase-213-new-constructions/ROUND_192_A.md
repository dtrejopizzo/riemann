# Positividad estricta hasta T=68/25

Para 0<T≤68/25 y todo f del dominio del paper 47, W_T(f)≥exp(−22000000001)||f||₂². La altura de ceros verificados sigue siendo G=3·10¹². Se añade el tramo (2.68,2.72].

**Filtro interior con banda de transición.** Fijar H=G/2, b=29, v=τ/H y

    u(τ)=1−sinc(v)² [cosh(b√(1−v²))/cosh b]².

La serie par del coseno hiperbólico elimina la elección de raíz compleja. Para v=x+iy, |Re√(1−v²)|²=(|1−v²|+1−x²+y²)/2≤1+y². Junto con la representación integral de sinc esto da crecimiento a lo sumo constante por exp(2(b+1)|Im τ|/H) para u. Sobre la recta 0≤u≤1. Para el polinomio exterior h de 190, de grado m/2, h(u)f̂ es entera de tipo ≤T+m(b+1)/H y de clase L² en la recta. El teorema de Paley–Wiener conserva el soporte requerido. El multiplicador es par, por lo que ambos momentos polares se multiplican por el mismo valor real.

**Tres regiones y polo.** Si r=R/H y |v|≤r<1, entonces

    u≤v²/3+2b v²/(1+√(1−r²)) ≤ a=r²[1/3+2b/(1+√(1−r²))].

En efecto 1−sinc(v)²≤v²/3, y log cosh es 1-Lipschitz, así que el déficit del segundo factor cuadrado es ≤2b(1−√(1−v²)). Para 2r≤|v|≤1 ambos factores sin cuadrar son positivos decrecientes en |v|, y Arb verifica u(2R)>7a/2 (argumento en unidades de τ). Desde |v|=1 el factor hiperbólico se convierte en coseno y 1−u≤sech²(b)/v². En particular sigue u≥7a/2. En el polo v=i/(2H), con y=1/(2H), se tiene sinh(y)/y≤exp(y²), y log cosh(b√(1+y²))−log cosh b≤by²/2. Por ello |u(i/2)|≤exp((b+2)y²)−1≤(b+2)/(2H²). El último paso usa (b+2)y²<1.

**Certificación de la forma.** Usar T=68/25, U=2749/1000, R=315000000, m=1390000000 y N=10¹⁰. Se obtiene T+m(b+1)/H=2.7478<U y 2U=5.498<5.5. El peso escalonado de 191, recalculado en esta ventana, verifica en enteros las 2048 filas para ||C||≤17.62. El margen arquimediano fuera de R supera 1/10; el piso global supera −24. Aplicar ahora la prueba de 190 con el a indicado. En unidades de B=D_{m/2}(2/a−1)^(−2), la ganancia después de reservar la densidad alta es ≥η exp(m arcosh 6)/80−24; el costo polar es ≤4 exp(T) exp(m arcosh(1+(b+2)/(H²a))). El certificado comprueba la absorción y B>exp(−22000000000).

Para |τ|≥H, la máscara exterior satisface 1−P≤2m sech²(b)(H/|τ|)² por la derivada de 190. Esta potencia cuadrática basta para la corrección alta: log(3+t)/t² decrece para t≥H, y al inicio 2m sech²(b) por 10⁹log(3+G) es <1/1000. El costo bajo es ≤2π exp(−22000000002)||f||². La reserva 1/(80π) y el signo no negativo de los átomos retenidos completan la prueba como en 190; se aplica inclusión de soportes. El filtro exterior sigue siendo el de Chebyshev de 190; el ahorro de soporte proviene de la función interior, que suprime la cola desde G/2 mediante sech² b.

**Reproducción.** Ejecutar python3 verify_192.py con python-flint. El resultado es interno al proyecto y conserva los insumos espectrales y de extensión de 175–179.
