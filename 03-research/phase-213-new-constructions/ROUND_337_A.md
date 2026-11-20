# Detección de la abscisa por una media local sin los pesos de Taylor

Fijar el mismo η suave de 325, con soporte compacto en (0,1) e integral no nula. Para X real, 0<δ<1 y h=X^(−δ), poner

    S_h(x)=Σ μ(n)η(log(x/n)/h),     L_δ(X)=∫_[X,2X] |S_h(x)|² dx/x,
    λ(δ)=limsup_(X→∞) log L_δ(X)/log X.

Entonces lim_(δ→0+) λ(δ)=2Θ. Además RH equivale a la cota L_δ(X)≪_(δ,ε) X^(1+ε)h para todo ε>0 y δ=1/j, j≥2. En cada bloque h es constante. El objetivo equivale así a una media cuadrática de tamaño Xh, salvo X^ε, sobre los centros de intervalos de longitud comparable a Xh. No intervienen órdenes de derivación m ni un máximo sobre centros excepcionales.

**Techo.** El transformado de Mellin de S_h es F(s)k_h(s), con F=1/ζ y k_h(s)=h∫η(v)e^(−shv)dv. Para cada σ>Θ, en la recta Re s=σ se tiene |F(s)|≪_σ(2+|Im s|)^C por 325. En cualquier franja vertical fija, |k_h(s)|≪_N h(1+h|Im s|)^(−N) por integración por partes. La inversión en una recta de abscisa >1 se desplaza hasta σ por estas mismas cotas uniformes en la franja. Plancherel en log x da

    L_δ(X) ≪ X^(2σ) ∫ |F(σ+it)k_h(σ+it)|²dt ≪ X^(2σ) h^(1−2C).

Por tanto limsup_(δ→0)λ(δ)≤2σ. Bajo RH se puede tomar σ arbitrariamente próximo a 1/2 y C arbitrariamente pequeño, como en 326, lo que implica el techo X^(1+ε)h.

**Detección inversa.** Para φ suave de soporte compacto en (0,log 2), la integración de S_h contra ψ(log(x/X)) y división por h reemplaza el peso en n por T_hψ(u)=∫η(v)ψ(u+hv)dv, u=log(n/X). Para cada entero K fijo hay ψ_h con el mismo control de soporte que φ, norma L² uniformemente acotada y T_hψ_h=φ+O(h^K) uniformemente. En efecto usar ψ_h=P(h∂)φ, donde P es el inverso formal hasta grado K−1 de Σ_{k<K}(∫v^kη(v)dv)z^k/k!. El término constante es invertible y Taylor con resto acotado justifica el error. Para h pequeño ambos pesos se anulan fuera de un compacto fijo, por lo que la suma de errores cuesta O(Xh^K). Cauchy–Schwarz da

    |Σ μ(n)φ(log(n/X))| ≪_φ,K L_δ(X)^(1/2)/h + Xh^K.

En particular Θ≤λ(δ)/2+δ: si el miembro derecho fuera menor que Θ, escoger una abscisa positiva entre ambos. Una partición suave de la recta logarítmica por trasladados de una φ de este tipo (paso fijo menor que log 2, normalizar una campana solapada por la suma periódica) descompone la serie de F en bloques X geométricos. Para s en un compacto a la derecha de esa abscisa aplicar la última desigualdad a φ(u)e^(−su) y multiplicar por X^(−Re s). Las constantes de las derivadas son uniformes allí. Elegir K con 1−Kδ menor que la abscisa elegida. La suma de bloques converge normalmente, coincide con F en Re s>1 y contradice un polo a la derecha de la abscisa elegida. Esto prueba el piso y, junto al techo, el límite. Bajo la cota propuesta λ(δ)≤1−δ, luego Θ≤(1+δ)/2 para δ=1/j; hacer j→∞.

**Alcance.** Es una reducción para μ en media dyádica. El índice ya recoge varianzas de primos y promedios en intervalos cortos, y 327–329 usan medias de μ con ahorro de logaritmos. Aquí se demuestra la implicación inversa para intervalos de longitud X^(1−δ) con el mismo suavizado fijo, incluyendo el error de deshacer el promedio. Falta demostrar incondicionalmente el techo de tamaño Xh.
