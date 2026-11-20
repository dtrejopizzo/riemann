# Ley de masa necesaria para saturar el peine en la banda crítica

Sea C el peine positivo por entradas de 081. Si ||f_T||₂=1 y exp(−T)⟨f_T,Cf_T⟩→1, entonces, en cada mitad de la ventana, la medida |f_T(t)|²dt transportada por u=T−|t| converge débilmente en [0,∞) a (1/2)exp(−u)du. Esto restringe cualquier sucesión de perfiles de 181 con κ=1 y W(M_Γ h)≤o(exp T): el arquimediano es ≥exp T−O(1), el polar es o(1) por 181 y 081 acota el peine por (1+o(1))exp T. La modulación no cambia la densidad espacial.

**Concentración.** Para D fijo entre 0 y T, los desplazamientos log n>2T−D enlazan únicamente los dos intervalos extremos de longitud D. El bloque de izquierda a derecha truncado tiene norma ≤||C|| por dominación puntual sobre módulos por el peine completo. El resto tiene norma O(exp(T−D/2)) por Chebyshev y sumación parcial. Si l y r son las normas en esos intervalos, el cociente normalizado queda acotado por 2lr(1+o(1))+O(exp(−D/2)). Para un saturador, l²+r²≤1 y (l−r)²=l²+r²−2lr. Tomar primero T grande y después D grande da tightness en profundidad y masa asintótica 1/2 por mitad. Para κ fijo en (0,1), un valor W≤0 en la banda de 181 aún exige 2lr≥κ−O(exp(−D/2))−o(1).

**Transporte de la masa.** Poner w=2cosh(t/2), K(t,ds) el núcleo de C, P(t,ds)=exp(−T)K(t,ds)w(s)/w(t). Por 081, P1=1+o(1) uniformemente. En la medida simétrica dJ=exp(−T)w(t)w(s)dt K(t,ds), g=f_T/w satisface

    (1/2)∫|g(t)−g(s)|² dJ=∫|f_T|² P1−exp(−T)⟨f_T,Cf_T⟩=o(1).

Para todo test φ acotado por uno, ∫|f_T|²Pφ−∫|f_T|²φ=o(1) uniformemente. En efecto, por simetría se reemplaza |g(t)|² por |g(s)|² bajo la integral con φ(s) con error o(1) por Cauchy–Schwarz y ∫|g(t)|²dJ=O(1). Luego se usa P1=1+o(1).

**Fila límite.** Desde t=T−v con 0≤v≤D fijo, un salto hacia −T+u para a≤u≤b fijos exige que n esté entre Y exp(−b) y Y exp(−a), Y=exp(2T−v). En ese intervalo el peso de P por átomo es (1+o(1))Λ(n)/Y, uniformemente, sustituyendo w por sus exponenciales dominantes en cada extremo. El PNT da masa exp(−a)−exp(−b)+o(1) uniformemente en v. Desde t=−T+v la misma afirmación vale por reflexión. Desde el extremo del mismo lado que el destino, los desplazamientos a ese intervalo tienen longitud acotada y su masa normalizada es o(1). Las convenciones de extremos no afectan el límite. Integrar estas filas contra |f_T|² usando la tightness y la invariancia anteriores da la ley afirmada en cada intervalo acotado. La tightness permite pasar a convergencia débil de medidas finitas.

081 y 177 exhiben el peso w que alcanza asintóticamente la norma. Aquí la conclusión concierne a la densidad macroscópica de *todos* los saturadores, incluso complejos y sin regularidad. No se deduce proximidad en norma a w ni se excluyen oscilaciones finas de fase. La condición sobre saturadores tampoco decide el signo cuando κ<1.

**Revisión independiente.** Se cotejó concentración, invariancia y ley límite. El lema half del paper 47 ya estima una correlación por las normas en dos extremos. Aquí se necesita además la norma conjunta de 081, y después las filas límite para determinar la distribución dentro de cada extremo. El PNT en intervalos macroscópicos da convergencia débil de profundidades.
