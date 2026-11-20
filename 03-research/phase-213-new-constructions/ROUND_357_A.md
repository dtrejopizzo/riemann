# Basta estimar cofactores sin primos pequeños, con un solo corte prescrito

Para X≥e fijar y(X)=4^⌊log₂(log X)⌋, de modo que (log X)²/4<y(X)≤(log X)². Sea R_{z,h}(x) la suma P_h de 353 reteniendo sólo pares pm en los que todos los primos de m son mayores que z (se admite m=1). El primo exterior p no tiene restricción. Entonces

    RH ⇔ para cada ε>0, ‖R_{y(X),h}‖_X ≪_ε √(hX) X^ε,
          para todo X≥e y 0<h≤1.

Aquí la norma usa todo el bloque [X,2X] con el corte congelado en y(X). En contraste con 356, el criterio sólo pide estimar cofactores que no tengan **ningún** primo pequeño. Es una reconstrucción por convolución; no afirma que el conjunto retirado tenga masa pequeña. El factor log(2X) de 353 se puede absorber en X^ε.

**Identidades exactas.** Para f(x) escribir T_d f(x)=f(x/d). La factorización de los factores primos del cofactor da, para z≥w,

    R_z = Σ_{d con primos en (w,z]} T_d R_w,
    P = Σ_{d z-liso} μ(d) T_d R_z.

En la primera igualdad los coeficientes son +1, con todas las potencias permitidas. En la segunda sólo contribuyen d libres de cuadrados. Ambos sumatorios admiten d=1 y h permanece fijo en cada dilatación. Se verifican en el semiplano de convergencia absoluta multiplicando los factores de 1/ζ y conservando el factor común de los primos simples; también son identidades de coeficientes por inversión. Sólo importan d≤2X en un bloque X.

**Coste de una expansión.** Para z≤(log X)², la suma de los módulos de coeficientes con peso d^(−1/2) en cualquiera de las dos expansiones es ≤∏_{p≤z}(1−p^(−1/2))^(−1)=X^o(1). En efecto su logaritmo cuesta O(√z/log(2z)+log log(3z)) por Chebyshev y sumación parcial. El peso d^(−1/2) es exacto al trasladar la norma normalizada por √(hX) al bloque X/d. En todo bloque 1/2≤Y≤X^κ hay además un techo trivial uniforme para cualquier corte: cada coeficiente por entero tiene módulo ≤log(2+2Y), hay O(1+Y) enteros y cada pulso tiene norma ≤√h. El coste normalizado es O((1+√Y)log(2+2Y)).

**Dirección directa.** Bajo RH usar 353 y la primera expansión con w<2 (por ejemplo w=1, R_w=P). La cota de 353 en los hijos X/d≥2, el techo trivial en los menores y el coste X^o(1) dan la cota postulada, empezando con una pérdida de exponente menor que ε.

**Reconstrucción con el único corte disponible.** Para la dirección inversa partir de la segunda expansión con z=y(X). En un hijo de escala Y, si Y≤X^κ usar la cota trivial. Si el corte heredado z coincide con y(Y), aplicar la hipótesis. Si z>y(Y), usar la primera expansión con w=y(Y) y repetir en los hijos, sin aumentar el corte. Entre escalas X^κ e X hay a lo sumo 2+⌈log₂(1/κ)⌉ valores distintos de y. En cada nodo que requiere expansión el corte baja estrictamente, incluso para el término d=1. Así la profundidad está acotada independientemente de X para κ fijo. A cada nivel la suma de costes normalizados es a lo sumo la del nivel anterior multiplicada por X^o(1); las ramas detenidas pueden arrastrarse con coste uno. Con κ pequeño respecto de ε, la cota trivial en hojas pequeñas y la hipótesis con exponente ε/3 en las otras hojas dan finalmente ‖P_h‖_X≪_ε √(hX) X^ε. 353 implica RH.

**Límite.** 309 ya usa el coste de productos de Euler pequeños a escala log². Aquí la reconstrucción resuelve el desajuste del corte al cambiar X por X/d: basta un solo corte por escala, sin hipótesis uniforme en todos los cortes inferiores que incluiría el problema original. Queda demostrar la estimación firmada para estos cofactores cribados.
