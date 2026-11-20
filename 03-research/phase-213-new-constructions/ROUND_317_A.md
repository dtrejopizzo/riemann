# Corte en la raíz por dos convoluciones sucesivas de orden uno

Sea c_t=b_t*1 y C_t(v)=Σ_(m≤v)c_t(m); conservar B_t para el sumatorio de b_t. Para cualquier D=x^o(1), q=⌊D⌋+1, hay pesos firmados explícitos g(n) tales que

    C_t(x)+Σ_(D<n≤√x)g(n) C_t(x/n) = O_ε(x^(1/2+ε))

uniformemente para 0≤t≤2. El techo integrado unilateral de 292 para B_t vale como criterio equivalente al signo también con C_t. Por tanto en este criterio de un solo saldo las dilataciones conservadas tienen argumentos entre √x y x/D. Para el saldo original B_t se obtiene el mismo recorte usando dos tipos de saldos intermedios, B_t y C_t. No se usa una estimación del problema del divisor.

**Qué cuenta C.** Sus factores locales son c_t(p)=1−2u_p y c_t(p^e)=(1−u_p)²=cos²(t log p) para todo e≥2. En particular,

    c₀(n)=(−3)^(#{p≡2 mod 3: p divide n exactamente una vez}).

Esto incluye el primo 2. La serie de C es G_t²L(s−it,χ)L(s+it,χ)/ζ(s) por 292. Bajo RH la misma prueba Mellin de 292 con una sola potencia del recíproco da |C_t(x)|≪_ε x^(1/2+ε) uniformemente en [1,2]. Ante un cero exterior, el numerador sigue siendo no nulo para casi toda frecuencia y se puede localizar un promedio positivo suave que conserve ese polo. No hay polos reales en s>1/2. El argumento unilateral de Landau de 292 prueba la recíproca con el promedio de las partes positivas de C_t. Esta equivalencia es para la familia en frecuencia; no se atribuye a la fila explícita t=0 por sí sola.

**Criba de orden uno.** Escribir a=(μ 1_[1,D])*(δ₁−qδ_q) como sucesión de Dirichlet y g=1*a. Entonces g(1)=1, g(n)=0 en 2≤n≤D y Σ|a(d)|≤(1+q)D. Para cualquier v,

    |Σ_(n≤v)g(n)| = |Σ_(d≤D)μ(d)(⌊v/d⌋−q⌊v/(qd)⌋)| ≤ qD.

En efecto, cada diferencia de pisos es un residuo entre 0 y q−1. Este techo independiente de v sustituye el error de potencia de 316. Si F es el sumatorio de b_t o c_t y f sus coeficientes, ambos satisfacen |f(m)|≪_ε m^ε por los valores locales. Para X≤x y V=√x, el intercambio exacto de 311 da

    |Σ_(X/V<n≤X)g(n)F(X/n)| ≤ 2qD Σ_(m≤V)|f(m)| ≪_ε x^(1/2+ε).

Las pérdidas subpotenciales en D,q pueden absorberse en cualquier ε. Aplicamos esto sólo para X=x o x/d con d≤qD, así que X/V>D para x grande.

**Cierre de las dos identidades.** Definir I_F(X)=Σ_(D<n≤X/V)g(n)F(X/n). Sea U el sumatorio de los coeficientes de D_t(s)ζ(s)², con techo de raíz uniforme por 309. Como g*c_t=a*(1*c_t), la media completa de C en X es Σ_d a(d)U(X/d), de tamaño O_ε(x^(1/2+ε)). Retirar la cola prueba C_t(X)+I_C(X)=O_ε(x^(1/2+ε)), también en los X=x/d requeridos. Para B, la misma convolución exacta da la media Σ_d a(d) C_t(x/d). Sustituir las identidades de C en esos puntos, absorbiendo Σ|a(d)|=x^o(1), da

    B_t(x)+I_B(x)+Σ_d a(d) I_C(x/d)=O_ε(x^(1/2+ε)).

Todos los sumatorios dentro de las dos I se evalúan en argumentos ≥√x y <x/D. El criterio de un tipo requiere un piso integrado para I_C; el de dos tipos requiere ese piso para la combinación escrita. Ninguno de esos pisos se deduce de acotar los residuos de las divisiones.

**Cotejo con el corpus.** La ronda 049 ya confinó dos factores cerca de la raíz en una suma suavizada distinta, usando inversión finita sobre filas de divisibilidad y control de cuadratura. La inversión finita también es clásica aquí. La ganancia específica respecto de 316 es la cota elemental y uniforme para la cola de los sumatorios ordinarios de 292 mediante el saldo intermedio c_t, con identidad punto a punto en x, sin signo nuevo para el tramo que queda.
