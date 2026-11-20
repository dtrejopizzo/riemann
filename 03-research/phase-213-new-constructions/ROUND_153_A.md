# Un techo de densidad para enteros cuya parte libre de cuadrados es prima

Sea S(x)=Σ_{p,n≥1} log p exp(−π(pn²/x)²), con p primo y n entero positivo. Cada entero contado tiene una única representación indicada. Con a=1/ζ(1/2) y c=ξ(1/2)>0, el signo global equivale al techo eventual

    S(x) ≤ ζ(2)x/2 + ca √x log x + O(√x).

Todos los pesos son positivos. El coeficiente secundario es negativo. La fórmula no establece incondicionalmente ese ahorro respecto de la densidad principal.

**Paso al peso positivo.** Escribir Q(T)=exp(−T/2)S(exp T)/c. Su transformada bilateral en Re z>1, z=1/2+s, vale
    G(z) D(z),   G(z)=π^(−z/2)Γ(z/2)ζ(2z)/(2c),   D(z)=Σ_p log p/p^z.
Esto se sigue de la integral de Mellin de la gaussiana por convergencia absoluta. Como B(z)=(z−1)G(z), se tiene P=(d/dT−1/2)Q con P de 152. La transformada de la derivada se justifica también diferenciando las gaussianas e integrando por partes en la tira inicial.

**Término de densidad.** Para y→∞ el teorema de los números primos da Σ_p log p exp(−π(p/y)²)~y/2 por integración por partes, con cota O(y) para todo y>0 por Chebyshev. Al tomar y=x/n² y sumar, la convergencia dominada por 1/n² da S(x)/x→ζ(2)/2. Así L=ζ(2)/(2c) es la constante de integración al resolver la ecuación para Q. Bajo RH, 151 da E(T)=O(1), luego 152 da P(T)=−aT/2+O(1). Integrar desde T hacia infinito da

    Q(T)−L exp(T/2)=−∫₀^∞ exp(−u/2)P(T+u)du=aT+O(1).

**Por qué basta el techo sin derivarlo.** En Re z>1/2, D(z)=−ζ'(z)/ζ(z)−Σ_{p,k≥2}(log p)p^(−kz), con la segunda serie holomorfa por convergencia normal. El polo en z=1 aporta L a la transformada. En cualquier cero ρ a la derecha de 1/2 queda un polo de residuo −mρ G(ρ)≠0. La parte T<0 de la transformada de Q es entera por el decaimiento gaussiano. Para Q−L exp(T/2) en T≥0 la sustracción elimina el polo en z=1. Si vale el techo anunciado, aT+C−Q(T)+L exp(T/2) es eventualmente no negativa. Su transformada unilateral es regular en el eje real s>0, por lo anterior y la ausencia de ceros reales de ζ en (1/2,1). Landau excluye cualquier singularidad en Re s>0. Esto fuerza RH y por el puente el signo del paper. De hecho también basta cualquier techo polinómico en T para el resto normalizado. El término secundario identifica la asintótica más precisa necesaria bajo RH.

**Recorte aritmético sin coste de escala.** En S(x) se pueden omitir todos los n>√x sin cambiar el criterio. Por el mayorante de Chebyshev O(x/n²) arriba, su contribución positiva total es O(√x). Los antecedentes 107 y 152 separaban potencias de primos. Aquí la integración elimina el cambio de signo del peso y la variable contada es el producto de un primo por un cuadrado. El techo de densidad en escala √x permanece abierto.
