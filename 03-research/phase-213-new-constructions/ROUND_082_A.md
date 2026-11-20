# Energía necesaria para que sobreviva el coste exponencial del peine

Escribir W=Arch+D_T, donde D_T=polar−C_T y C_T es el peine positivo de 081. Para T suficientemente grande, con constantes absolutas c,C>0, todo test del dominio de forma verifica
     
    |D_T[F]| ≤ C e^T [ exp(−c√T)||F||² + (Arch[F]−m(0)||F||²)/√T ].

En particular para ||F||=1 y |D_T[F]|≥δ e^T, δ>0 fijo, el exceso arquimediano es al menos c_δ√T para T grande. Además ||D_T||∼e^T como operador acotado en la ventana, pero en el plano de los dos momentos polares su norma como aplicación hacia todo L² es O(exp(T−c√T)).

**Estimación sobre el mismo test.** En la forma cuadrática se puede truncar el núcleo de convolución polar 2cosh(u/2) a |u|≤2T, por el soporte de la autocorrelación. Su símbolo menos el del peine es
     
    b_T(ξ)=4∫₀^{2T} cosh(u/2)cos(ξu)du − 2Σ_{n≤e^(2T)} Λ(n)n^(−1/2)cos(ξ log n).

El contacto en el extremo tiene autocorrelación nula, así que es lícito incluirlo. Sustituir dψ(t) por dt en la suma deja en el símbolo la integral de 2 exp(−u/2)cos(ξu), acotada uniformemente. Para el error, integrar por partes contra ψ(t)−t=O(t exp(−c√log t)) para t≥2. La derivada del peso t^(−1/2)cos(ξ log t) cuesta O((1+|ξ|)t^(−3/2)); separando la integral en t≤exp(T) y t>exp(T), e incluyendo el extremo, resulta O((1+|ξ|)exp(T−c₁√T)). La cota absoluta trivial del símbolo es O(exp T) en toda la recta por 081 y la masa total de los coeficientes (para el símbolo se usa la masa, no la norma comprimida).

Elegir R=exp(c₁√T/2). En |ξ|≤R el símbolo tiene tamaño O(exp(T−c₁√T/2)). En |ξ|>R, Plancherel y monotonía dan masa espectral ≤(Arch[F]−m(0)||F||²)/(m(R)−m(0)); el denominador es comparable a √T. Integrar el símbolo da la desigualdad. Esta estimación conserva el término polar en la cancelación de densidad.

**En qué subespacio reside el coste principal.** Sea P la proyección al plano de c(t)=cosh(t/2) y s(t)=sinh(t/2) restringidos al intervalo. Por la fórmula de filas de 081 y el PNT cuantitativo,
     
    C_T c=e^T c+O(exp(T−c₁√T)c),
    C_T s=−e^T s+O(exp(T−c₁√T)c)

puntualmente casi por todas partes (en estas dos igualdades c sin argumento dentro del error designa el perfil). Para la segunda identidad restar las filas correspondientes a exp(t/2) y exp(−t/2). En las dos se usa Chebyshev en los extremos X_±<exp(T/2), que aportan un error relativo O(exp(−T/2)) respecto a e^T cosh(t/2), como en 081. Las normas de c y s son comparables al crecer T. Los autovalores del operador polar en esos vectores son 2T+2sinh T y 2T−2sinh T, respectivamente. Por tanto ||D_T P||≪exp(T−c₂√T). Por autoadjunción también se controla el bloque cruzado a ese plano. En el complemento la compresión es exactamente la de −C_T y tiene norma ||C_T|| por 081. Resulta ||D_T||=||C_T||+O(exp(T−c₂√T))∼exp T. Esto se refiere al operador acotado D_T, sin el multiplicador arquimediano.

**Cotejo y escala pendiente.** P47 prop:wit-cheb ya centra el peine mediante PNT en tests con control de derivada. P211-006 y 081 ya identifican las modulaciones y el test cosh. Aquí se usa el corte de Fourier para obtener una condición energética para todos los tests del dominio y el cálculo de las dos filas para controlar conjuntamente el plano polar y su cruce. El resultado excluye un exceso no arquimediano de orden e^T en tests normalizados con exceso arquimediano o(√T). No demuestra W≥0: la cota superior para |D_T| sigue siendo muchísimo mayor que la energía arquimediana en las escalas relevantes. No produce una ventana adicional.
