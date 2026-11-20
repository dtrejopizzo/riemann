# Cómo el corte amplifica la oscilación forzada de la ventana triangular

Para un corte z mantenido fijo al crecer x, sea Q_w(x;z) el observable de 360. Fijar un cero ρ=1/2+iγ de multiplicidad m≥1, γ>0. Para ambas elecciones del signo vale incondicionalmente

    limsup_{x→∞} (±Q_w(x;z))/(√x (log x)^m)
        ≥ m |W(ρ)| |E_z(ρ)| / |ζ^(m)(ρ)|,
    E_z(s)=∏_{p≤z}(1−p^(−s))^(−1).

El factor del corte puede ser exponencialmente grande en √z/log z: los límites superior e inferior de log|E_z(ρ)| dividido por √z/log z, cuando z→∞, son respectivamente 1/|1−ρ| y −1/|1−ρ|. Lo que cambia de forma demostrada es la contribución de ese cero al piso de oscilación; no se acota por arriba la oscilación total.

**Órdenes de los polos.** Para Re s>1 la transformada del observable es

    W(s) E_z(s) / ζ(s) · [−ζ'(s)/ζ(s) − Σ_{k≥2,p}(log p)p^(−ks)
                                      − Σ_{p≤z}(log p)p^(−s)].

En el término de potencias superiores, sumar y restar −ζ'(2s)/ζ(2s) deja una función holomorfa en Re s>1/3 por convergencia absoluta de las potencias restantes. La transformada es regular sobre el eje real en σ>1/2, incluido 1 por cancelación con el cero de 1/ζ. En 1/2 presenta a lo sumo un polo simple. En ρ, ζ(2ρ) es finita y no nula en la recta 1 y W(ρ)≠0. El polo tiene orden m+1 con coeficiente principal −m·m! W(ρ)E_z(ρ)/ζ^(m)(ρ).

**Comparación de Landau.** Si uno de los dos limsup fuera menor que el piso indicado, elegir una constante positiva C estrictamente entre ambos (o entre cero y el piso si el limsup no es positivo). La función C√x(log x)^m∓Q_w(x;z) es eventualmente no negativa. Su transformada de Mellin converge absolutamente en σ>1/2 por el principio de Landau, ya que su continuación no presenta singularidades reales en ese intervalo. Descartar un tramo inicial sólo cambia una función entera. Para la cola no negativa, el módulo de su transformada a σ+iγ es a lo sumo su valor a σ. Multiplicar por (σ−1/2)^(m+1) y hacer σ↓1/2: el lado real tiende a C m!, pues el polo real del observable tiene orden ≤1. En el lado torcido sobrevive el módulo del coeficiente principal en ρ, contradicción. El argumento no presupone RH.

**Amplificación con el corte.** Por desarrollo del logaritmo, log|E_z(ρ)|=Re Σ_{p≤z}p^(−ρ)+O(log log(3z)), al sumar los términos de orden ≥2 en módulo. Por el teorema de los números primos y sumación parcial, para ρ fijo la suma es z^(1−ρ)/((1−ρ)log z)+o(√z/log z). En efecto integrar t^(−ρ)/log t da ese principal y la sustitución del recuento de primos por li(t) cuesta o(√z/log z). El argumento de z^(−iγ)/(1−ρ) recorre ambas fases extremas indefinidamente. Esto prueba los límites.

**Decisión.** La meta con x^ε de 360 es compatible con este piso. Un techo C√x log x con C absoluto para todos los cortes fijos sería falso: si m>1 ya falla a un corte, y si m=1 fallan las constantes uniformes por la amplificación. Los límites son primero en x, luego en z; no dan por sustitución una sucesión con z≈log²x. Antecedentes del principio de oscilación en 058 y 126. La dependencia explícita del factor de Euler pertenece al observable doblemente cribado de 360.
