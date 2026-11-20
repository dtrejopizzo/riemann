# Un peso fijo con sólo O((log x)²) muestras exteriores pendientes

En 046 la variación de la derivada del peso imponía el umbral x^(1/4) a la estimación absoluta. Cambiamos el peso mediante un promedio compacto de dilataciones, comprobando que conserva la implicación al signo. Antecedentes: promedios de traslaciones en selección 027, transferencia analítica en 038, banda en 044 y cuadratura en 045–046. El paso de suficiencia usa Landau y Weil; no constituye un mecanismo elemental nuevo para firmar el resto.

**Un solo promedio para todas las escalas.** Sea ν la ley de la suma de variables independientes uniformes en [0,l_n], con l_n=1/(n(n+1)), n≥1. La suma está en [0,1]. La transformada P(z)=∫exp(zv)dν(v) es el producto de (exp(l_n z)−1)/(l_n z). Los factores difieren de uno en O_R(l_n) en |z|≤R. Así P no tiene ceros para Re z>0. La densidad de ν es suave: en la transformada de Fourier los primeros N factores dan O_N((1+|ξ|)^(−N)) para cada N y los restantes tienen módulo a lo sumo uno.

Tomar el peso normalizado W de 044 para j par y usar ese mismo peso a toda escala real. Definir

    V(t)=∫ exp(−v/2) W(t exp(−v)) dν(v),
    D(r)=exp(−r/2)[exp(r)∫V−Σ_n Λ(n)V(n exp(−r))].

V es positivo en el interior de su soporte [a,B]=[1/16,16e]. Para h=log16, b=3/2 y c=1/(2cosh(bh)), por la identidad de 044 D es el promedio en v del valor en r+v de (I−c shift_{−h}−c shift_{h})E, escribiendo E en coordenada logarítmica.

**Por qué basta una cota superior en j⁴.** Bajo el signo, E está acotada en la semirrecta por 038–039, luego D también. Recíprocamente D''(r)=O(exp(r/2)) para r grande por derivación de la suma de soporte local, regularidad de V y la cota de Chebyshev Σ_{n≤X}Λ(n)=O(X). En las celdas entre r_j=4log j y r_{j+1} la interpolación lineal tiene error O(j²/j²)=O(1). Basta D(r_j)≤C para que D quede acotada superiormente.

En r grande E(r)=3k(r)+O(1) por 039. La misma cota superior se transfiere al promedio de las tres traslaciones de k. Su Laplace unilateral, salvo términos enteros de los tramos finitos y un factor constante si se conserva el 3, es la transformada de k en 038 por

    P(z)[1−cosh(hz)/cosh(bh)].

Esto se obtiene primero en Re z>1/2 trasladando el límite inferior de cada integral, con traslaciones uniformemente acotadas. El factor no se anula en 0<Re z≤1/2: para el corchete las únicas partes reales posibles de un cero son ±b. La transformada es regular en el semieje real positivo por 038. Landau aplicado a una constante menos el promedio, eventualmente no negativo, excluye polos en Re z>0 como en 038. Todo cero de ξ con Re s>1/2 produciría un polo superviviente en z=s−1/2; 038 y Weil dan el signo.

**Control de derivadas.** En variable logarítmica, el peso exp(y/2)V(exp y) es la convolución de exp(y/2)W(exp y) con ν. Derivar q de los factores uniformes cuesta en norma de variación como máximo ∏_{n≤q}(2/l_n)=2^q q!(q+1)!. Así la norma suprema de la derivada q de V(exp y) en su soporte es ≤C^(q+1)(q!)², por Leibniz y el factor exp(−y/2). La función χ(y)=ν((−∞,y]) también cumple esa cota: es la convolución del escalón acotado con ν. Vale cero hasta 0 y uno desde 1.

Sea g(t)=Σ μ(m)V(mt). Aplican 045 y sus momentos, pues V es suave y de soporte compacto alejado de cero. En particular ∫g=0, ∫g log=∫V y Σg(k/x)=V(1/x)=0 para x grande. Con Δ como en 046, el déficit sin normalizar es Δ[g(u/x)log(u/K)].

**Cuadratura superior.** Definir H₊(u)=g(u/x)χ(log(u/K))log(u/K). Su término m, sin μ, es F_z(mu/x) con z=mK/x y F_z(s)=V(s)χ(log(s/z))log(s/z). Sólo interviene z≤B. En variable log s, por Leibniz las derivadas de orden q tienen norma suprema ≤C^(q+1)(q!)²(1+log(B/z)); donde la función o sus derivadas son no nulas se tiene s≥z. Pasar a derivadas ordinarias conserva este orden: s^q ∂_s^q es el producto de operadores (∂_{log s}−i), 0≤i<q. El coeficiente de orden l en valor absoluto es ≤binom(q,q−l) q!/l!, acotando cada producto de q−l índices por el producto de los q−l mayores enteros entre 1 y q. Al sumar contra (l!)² se obtiene a lo sumo 2^q(q!)². El soporte s≥a absorbe s^(−q) y el ancho fijo permite pasar a norma L¹.

Por Poisson e integración por partes q≥2 veces, |ΔF|≤2ζ(q)(2π)^(−q)‖F^(q)‖₁ para F suave compacta en la semirrecta, extendida por cero. En cada dilatación el factor es (m/x)^(q−1). Para M=Bx/K≥1, Σ_{m≤M}m^(q−1)(1+log(M/m))≤C M^q uniformemente en q≥2, usando m^(q−1)≤M^(q−2)m. En conjunto,

    |ΔH₊| ≤ x C₀^(q+1)(q!)² K^(−q).

Elegir q=floor(c√K) con c suficientemente pequeño y usar q!≤q^q. Resulta |ΔH₊|≤C x exp(−c'√K). Por tanto una constante fija A suficientemente grande y K=A(log x)² dan |ΔH₊|=O(√x).

**Obligación firmada.** En x=j⁴, poner H₋(u)=g(u/x)[1−χ(log(u/K))]log(u/K). La positividad global equivale a ΔH₋≤C√x eventualmente, porque la parte superior cumple la cota bilateral y la normalización de D es x^(−1/2). La suma exterior sólo contiene k<eK. Quedan la integral cerca de cero y las sumas interiores de Möbius en g; su coste y su signo no están controlados por contar muestras. Todos los pesos y constantes del corte son independientes de j.

**Afinación del corte.** Para cada δ>0 fijo se puede elegir en su lugar l_n=cδ/[n(log(n+1))^(1+δ)], normalizando la suma a uno. La misma construcción da, hasta C^(q+1), la cota q! L(q)^q para las derivadas, con L(q)=max(1,(log(q+2))^(1+δ)). Esta clase de cotas se conserva por Leibniz (usar L(l)≤L(q)) y por la conversión a derivadas ordinarias anterior, cuya suma ahora cuesta como máximo 2^q q! L(q)^q. En la cota de cuadratura se sustituye (q!)² por q! L(q)^q. Con q=ceil(log x), K=Aδ log x (log log x)^(1+δ) y Aδ suficientemente grande se obtiene otra vez O(√x). El peso es fijo una vez elegido δ. No se toma δ=0: las longitudes propuestas en ese caso no son sumables.

La construcción de funciones de Gevrey por convolución infinita de uniformes ya figura en fase 159, G2_B6_R2, lemas W/E, y G2_P3_R2 en su auditoría. La aplicación conjunta a la conservación de polos de la banda y al corte de la cuadratura es el contenido específico aquí.
