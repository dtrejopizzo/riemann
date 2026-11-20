# Recorte simultáneo de los argumentos grandes y pequeños en la media cribada

Fijar cualquier D=D(x)=x^o(1) con D≥2. Con los pesos w_D de 310, para 0≤t≤1 y x grande existe un V entre 2 y 4 tal que

    |Σ_(x/V<n≤x) w_D(n) B_t(x/n)| ≤ x^o(1).

Incluso se puede anular exactamente esta cola permitiendo un peso parcial en un solo extremo. Por tanto la media de 310 conserva el techo de raíz después de retirar esa cola. En t=0 puede elegirse V=V(x)→∞ sin exigir velocidad, manteniendo el mismo error. Al tomar además D→∞, fuera de la muestra principal B₀(x) sólo quedan argumentos en [V,x/D). El umbral creciente de este último enunciado se ha probado únicamente para la primera fila.

**Distribución de los pesos en intervalos proporcionales.** Sea W_D(v)=Σ_(n≤v)w_D(n). Congelar D al evaluar en varias escalas. Con h=h_D de 310, soportado en n≤D⁴, la fórmula elemental Σ_(n≤u)τ(n)=u(log u+2γ−1)+O(√u) da para v≥D⁴

    W_D(v)=v(A log v+E)+O(√v D^(1+o(1))),
    A=Σ h(n)/n,   E=(2γ−1)A−Σ h(n)log(n)/n.

Aquí y para D acotado el error se interpreta como O_ε(√v D^(1+ε)): la estimación de mcm de 310 es válida también en σ=1/2. Para cada D fijo A≥0 al pasar v→∞, por positividad de W_D. Por otra parte W_D(x)≫x/log x uniformemente para D=x^o(1) ya que w_D(p)=2 para todo primo p>D. La restricción W_D(√x)≥0, aplicada al mismo polinomio, da A log x≤2 W_D(x)/x+O(x^(−1/4+o(1))). Así, para cada intervalo compacto de c positivos,

    W_D(cx)/W_D(x)=c+O(1/log x)

uniformemente en c (con constante del compacto, y para x suficientemente grande según D(x)). Esto evita suponer que el segundo coeficiente E sea pequeño frente al primero.

**Selección del extremo.** Para V fijo el intercambio de las dos sumas da exactamente

    Σ_(n>x/V; n≤x)w_D(n) B_t(x/n)
        = Σ_(m≤V)b_t(m)[W_D(x/m)−W_D(x/V)].

Dividiendo por W_D(x), el miembro derecho es J_t(V)+O_V(1/log x), uniformemente en la frecuencia, donde J_t(V)=Σ_(m≤V)b_t(m)(1/m−1/V). En V=2 y 4 los perfiles son de signos opuestos con margen uniforme en [0,1] por 303. Los saltos al mover el extremo en ese intervalo cuestan como máximo O(max_(n≤x)τ(n)^3)=x^o(1) porque los argumentos de B están acotados y |Σ_(d|n,d≤D)μ(d)|≤τ(n). Escoger un extremo del salto que cambia el signo prueba el techo, o interpolar sólo su peso entre cero y el original para obtener cancelación exacta. En t=0, J₀(V)=−1+3/V entre 2 y 4; en particular el primer cruce allí está en V=3+O(1/log x) por la estimación uniforme en ese compacto.

**Extensión en t=0.** Por 304 hay intervalos fijos [A_j,B_j] con A_j→∞ y signos estrictamente opuestos del perfil en sus extremos. Para cada j los signos se trasladan a la cola cribada para x suficientemente grande. El salto está acotado por max_(v≤B_j)|B₀(v)| max_(n≤x)τ(n)^3. Retrasar el paso al intervalo j hasta que el primer factor sea ≤x^(1/j) y B_j D<x; esto da la diagonal requerida. En la media restante la positividad de los pesos no proporciona por sí misma el piso necesario para la suma de dilataciones intermedias. El recorte del bloque de primos de 303–304 y el recorte aquí establecido afectan a sumas diferentes: aquí se controla la cola de la media que ya tiene techo de raíz.
