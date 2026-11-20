# El coste de reproducir la banda con una suma divisorial

En 044 el inverso del sombrero W tenía esquinas arbitrariamente cerca de cero. Eso descartaba un perfil fijo con pérdida acotada en los primos. Aquí se permite **cambiar el soporte y el perfil** a cada escala. Escribimos Df(t)=Σ_{m≥1}f(mt); W es el sombrero normalizado de las escalas pares en 044. Las dos conclusiones siguientes aclaran si con la identidad de divisores se puede conservar la banda y hacer cuadratura del nuevo perfil.

**Construcción exacta en todo el tramo muestreado.** Para cada x=j⁴ con j par, existe f continuo firmado de soporte compacto en (0,∞) con Df≤W en toda la semirrecta y Df(t)=W(t) para todo t≥1/x. Sea g(t)=Σ μ(m)W(mt), suma localmente finita con Dg=W. Tomar δ=1/(8x), multiplicar g por un corte continuo que vale cero bajo δ/2 y uno desde δ; llamar f₀ al producto. Tomar un sombrero continuo auxiliar 0≤h≤1 soportado en [δ/2,4δ], igual a uno en [δ,3δ]. Para t<δ hay al menos δ/t múltiplos mt en [δ,3δ]; además Df₀(t)≤16‖f₀‖∞/t. Así

    f=f₀−(16‖f₀‖∞/δ)h

da Df≤0 cuando t<δ, Df≤W para t≥δ y Df=W para t>4δ. En particular sirve simultáneamente para todos los enteros n/x. La igualdad ΣΛ(n)W(n/x)=Σ f(k/x)log k resultante usa inversión exacta en las muestras. Su signo exige controlar la suma firmada de la derecha.

**Obstrucción al balance.** Para cualquier función continua f no nula de soporte compacto alejado de cero, Df≤W globalmente implica ∫f<0. Vale para cualquier banda W continua no negativa de soporte compacto alejado de cero, independientemente de la escala.

En efecto tDf(t)→∫f por sumas de Riemann y por ello ∫f≤0. Si se tuviera igualdad, regularizar f mediante convolución con una identidad aproximada positiva en log t: g(t)=∫f(te^v)φ(v)dv. Para un núcleo suficientemente estrecho g≠0. Es suave, de soporte compacto alejado de cero, con ∫g=0, y Dg≤U, donde U es la misma regularización de W y tiene soporte [a,b]⊂(0,∞) en el sentido de inclusión.

Extendiendo g de manera par a G en la recta, Poisson da Dg(t)=t⁻¹Σ_{n≥1}Ĝ(n/t); los términos en el origen desaparecen por G(0)=∫G=0. Con la convención de Fourier exp(−2πiξs), para cada entero k≥1,

    ∫ Dg(t)t^(−2k−1)dt = ζ(2k+1) ∫₀^∞ v^(2k)Ĝ(v)dv = 0,

porque G^(2k)(0)=0. El cambio de orden es absoluto por el decrecimiento rápido de Ĝ y la convergencia de Σn^(−2k−1); todas las integrales en t son en (0,∞).

Si Dg fuese estrictamente negativa en algún punto de (0,a), sería ≤−η en un intervalo [l,h] con h<a. La magnitud de esa contribución al momento sería ≥η(h−l)h^(−2k−1), mientras que toda la contribución positiva es ≤a^(−2k−1)∫U. Para k grande se contradice el momento nulo. Así Dg=0 bajo a. También se anula sobre el extremo superior del soporte de g y más allá. En el compacto restante se anulan todos los momentos de la medida Dg(t)t⁻³dt en la variable t⁻², usando k=1,2,... . La aproximación polinómica implica Dg=0. La inversión finita en cada t>0 da g=0, contradicción.

**Alcance para el signo.** El balance ∫f=0 es la cancelación que elimina el término x log x·∫f de la integral de f(t/x)log t. Está prohibido exactamente para cada minorante global no trivial de esta clase. El argumento no da una cota inferior uniforme para |∫f_x|. Tampoco controla los errores de cuadratura cuando f_x varía. La desigualdad local de 044 continúa abierta.

Antecedentes dirigidos: selección 040 para la condición de balance y la pérdida de cola; 044 para la banda, el inverso y la pérdida del perfil fijo; SPEC_SIGN_OBJECT_003 de fase 200 para los momentos en los ceros triviales. Aquí la inferencia adicional es que el solo signo fuera de una banda, combinado con todos los momentos y el balance, fuerza la nulidad. La construcción desplaza la corrección a escalas inferiores a la primera muestra.

## El balance puede aproximarse con igualdad en las muestras

Fijar el sombrero W de 044. Para cualquier umbral τ>0 y cualquier tolerancia ε>0 existe un minorante compacto continuo f como el anterior con Df=W en [τ,∞), −ε<∫f<0 y |∫f(t)log t dt−∫W|<ε. Más generalmente se puede aproximar simultáneamente cualquier lista finita de momentos logarítmicos del inverso exacto. No hay por tanto una pérdida fija en el balance, incluso después de imponer todas las muestras de una escala.

**Estimaciones del inverso.** Se usa el teorema cuantitativo clásico de los números primos para Möbius, M(y)=Σ_{m≤y}μ(m)=O_A(y/(log y)^A) para cada A fijo. Es una entrada analítica incondicional. Escribir L=log(1/t) para t pequeño. La sumación parcial para una función U de variación acotada soportada en [1/16,16] da Σμ(m)U(mt)=O_{A,U}(t⁻¹L^(−A)): en el intervalo de suma m es comparable a 1/t, y la variación de U(mt) es a lo sumo la de U. Aplicar esto a W y a uW'(u), ambas de variación acotada por tramos con variación total finita. El inverso g de la construcción anterior es localmente Lipschitz; se obtiene |g(t)|≤C_A t⁻¹L^(−A) y |g'(t)|≤C_A t⁻²L^(−A) casi en todas partes. En consecuencia g es integrable con cualquier peso (1+|log t|)^k.

Para s>1 la inversión absolutamente convergente da ∫g(t)t^(s−1)dt=(∫W(t)t^(s−1)dt)/ζ(s). Tomando el límite y su primera derivada en s=1 por convergencia dominada y usando el residuo uno de ζ, se obtiene ∫g=0 y ∫g(t)log t dt=∫W(t)dt.

**Corrección con masa pequeña.** Repetir la construcción de 045 con δ↓0 y corte lineal en [δ/2,δ]. Para cada A, |∫f₀|=O_A(log(1/δ)^(−A)) por ∫g=0 y la cota de cola (usar un exponente mayor en g). Además Var(f₀)=O_A(δ⁻¹log(1/δ)^(−A)) por la cota de la derivada y la variación en el corte. Para t<δ, la comparación de cada rectángulo de ancho t con su integral da

    t Df₀(t) ≤ ∫f₀ + t Var(f₀) ≤ ηδ,
    ηδ=max(0,∫f₀)+δ Var(f₀).

Basta restar (ηδ/δ)h, con h el mismo sombrero auxiliar de 045. El nuevo f satisface Df≤W y Df=W para t>4δ. La masa absoluta de la corrección es O(ηδ). Para cada k fijo, ∫|f−g|(1+|log t|)^k tiende a cero más rápido que cualquier potencia inversa de log(1/δ), sumando la cola de g y la corrección soportada a escala δ. Elegir 4δ<τ y luego reducir δ hasta alcanzar la tolerancia. El signo estricto de ∫f sigue del lema anterior tomando τ por debajo del extremo superior de la banda en la construcción para garantizar f≠0.

**Lo que queda por estimar.** Para x fijo, elegir τ≤1/x y 4δ<τ. Tanto f como g coinciden en cada k/x y la suma contra log k es idéntica. Sin embargo, la integral de g(t/x)log t es exactamente x∫W. Así el único término por estimar en esta comparación es la diferencia entre la suma discreta contra log k y esa integral. Para la banda de escalas pares hace falta que la suma supere la integral menos O(√x). La aproximación de los momentos por sí sola no acota esa diferencia.

La misma prueba cubre j impar usando el sombrero W_j(t)=√x w_j(xt) de 044. El extremo inferior está en [1/81,1/16] y el superior en 16. En las dos ramas las fórmulas de 044 dan combinaciones de t y t⁻² con coeficientes uniformemente acotados (el cociente j/floor(j/2) está entre 2 y 3). Así W_j y tW_j' tienen variaciones uniformemente acotadas, incluidos los saltos de la derivada. Todas las cotas de aproximación anteriores pueden tomarse uniformes en j.

Para precisar el resto, escribir g_j para el inverso de W_j. Integrando por partes en las celdas de k/x se obtiene exactamente

    x∫W_j − Σ_k g_j(k/x) log k
      = x∫₀^{1/x} g_j(t) log(xt)dt
        − ∫_{1/x}^∞ {xt}[g_j'(t)log(xt)+g_j(t)/t]dt.

El valor de log(xt) en el extremo inferior es cero. El antecedente de este tipo de fórmula de parte fraccionaria está en fase 188, N_BUILD_005 §4 y N_BUILD_006 §§1–2. La desigualdad de 044 pide una cota superior uniforme O(√x) para el lado derecho antes de normalizar. Las estimaciones absolutas de Möbius usadas para los momentos sólo dan O_A(x/(log x)^A) para cada A fijo: en la segunda integral se separa t≤1/√x, donde se extrae la potencia inversa de log x, del resto, que cuesta O(√x log x). Falta cancelación en este resto de cuadratura.
