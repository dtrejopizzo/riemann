# Una falla exige excursiones simultáneas de θ y de Mertens

Escribir Θ=sup Reρ y M₀(z)=Σ_{d≤z}μ(d). Si Θ>1/2, existen sucesiones v_j,d_j→∞ tales que

    log d_j / log v_j → 2,
    log |θ(v_j)−v_j| / log v_j → Θ,
    log |M₀(d_j)| / log d_j → Θ.

Los máximos pueden ocurrir en distintos puntos de las dos bandas. La relación es logarítmica; no se afirma d_j/v_j²→1 ni una relación entre signos. Se obtiene una cota de tamaño para el resto en función del producto de dos discrepancias locales de los datos aritméticos verdaderos.

**Retirar los correctores.** En 131 tomar r≥2 y cambiar w_n por w*=(T₂−I)(T₂−2I)w_n, donde T₂w(t)=w(t/2)/2. El promedio es firmado. Su momento de orden s se multiplica por (2^s−1)(2^s−2); conserva los polos no triviales que detectaba w_n pues 0<Reρ<1. Sus momentos de órdenes 0 y 1 se anulan. Mantiene la imparidad y el soporte Fourier en [−B_n,B_n]. En consecuencia F(y)=∫w*(t)floor(yt)dt vale exactamente cero para y>B_n/(2π). Además F, yF' y (y∂_y)²F están acotadas. Para y acotado usar F(y)=Σ_{k≥1}W(k/y), con W(s)=∫_s^∞ w*(t)dt; las dos derivadas se suman absolutamente por el decaimiento de w* y de su primera derivada. En y grande la función es cero.

En la fórmula de 131 se toma ahora K(v)=Σ_{d≤D}μ(d)F(X/(dv)), sin correctores, D=floor(X^(2/3)). La estimación factorial sigue por linealidad de las tres dilataciones o por la misma prueba de Stirling. Se mantienen los dos extremos: F da el corte inferior, la inversión en d y el decaimiento absoluto de w* dan el superior. Escribiendo Y=X^(1/3), U=Y X^δ, queda el promedio de ψ(Xt)−Xt igual a ∫_(cY,U](W(v/X)−K(v))dE+o(√X), donde c>0 es fija suficientemente pequeña. Las constantes pueden depender de los pesos fijos. En esta banda K(v) sólo usa d≥l=κX/U, con κ>0 fija suficientemente pequeña.

**Cota bilateral de tamaño.** Sean A=1+sup_{l≤u≤z≤D}|Σ_{u<d≤z}μ(d)| y P=1+sup_{cY≤v≤U}|ψ(v)−v|. Se puede reducir κ para que los posibles términos del extremo izquierdo queden incluidos. Por Abel en d, |K|+|vK'|≪ A(1+log X), usando las dos derivadas logarítmicas anteriores para integrar la variación de cada peso. W y su derivada logarítmica están acotadas. En la banda b=1 para X grande. Una integración por partes contra d(ψ(v)−v), incluidos los términos de borde, da

    |∫_(cY,U](W(v/X)−K(v))dE| ≪ A P (1+log X)².

**Obtención de la simultaneidad.** Incondicionalmente |ψ(t)−t|+|M₀(t)|≪ε t^(Θ+ε). Para Θ=1 bastan Chebyshev y el conteo trivial. Para Θ<1, la primera cota es la fórmula explícita de 121. Para la segunda, en cada semiplano Re s≥Θ+η y alturas grandes se tiene 1/ζ(s)≪ε,η |Im s|^ε. En efecto en discos centrados en 2+it contenidos con margen en la región sin ceros, Borel–Carathéodory da |log ζ|≪log |t| por el crecimiento polinómico de ζ. En un disco menor dentro de Re s>1 se tiene O(1) por la serie. Tres círculos da en cada radio intermedio O((log |t|)^a) con a<1. Perron truncado en semienteros a altura x² y traslado a Θ+η dan la cota anunciada al elegir η y el exponente de altura suficientemente pequeños.

Para δ,ε>0 pequeños elegir un cero con parte real >Θ−ε/2 y luego n fijo que lo detecte, por 131. El promedio firmado discrepa en módulo por más de X^(Θ−ε) a escalas arbitrariamente grandes: un techo eventual de ese orden daría convergencia absoluta de su Mellin a la derecha de Θ−ε y contradiría ese polo. Tomar ε<Θ−1/2 para descartar el error o(√X). En esas escalas A P ≫ X^(Θ−ε)/log²X. Por los techos generales anteriores A≪X^((2/3)(Θ+ε)) y P≪X^((1/3+δ)(Θ+ε)). Por tanto A≥X^((2/3)Θ−O(ε+δ)) y P≥X^((1/3)Θ−O(ε+δ)) en las mismas escalas. Una suma local de Möbius grande implica que al menos uno de sus extremos tiene |M₀| grande. Para δ,ε suficientemente pequeños, el término de potencias propias O(U^(1/2)log² U) es despreciable en el pico de ψ, de modo que se obtiene el de θ. Haciendo δ,ε→0 y tomando X arbitrariamente grande en cada paso, los dos puntos elegidos satisfacen log v/log X→1/3 y log d/log X→2/3 y las dos tasas del enunciado.

**Alcance.** Las cotas generales de los dos factores permiten exactamente el exponente Θ al estrechar las bandas; falta una mejora conjunta. 130 ya anulaba dos momentos en los coeficientes; aquí se anulan en el promedio y desaparece la dependencia del momento armónico global de μ. 131 ya detectaba polos en la banda prima. La afirmación adicional se refiere a las dos sumas aritméticas y a la relación entre las escalas de sus excursiones, no sólo al soporte de un núcleo.
