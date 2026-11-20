# En qué frecuencias del parámetro de tasa vive una posible violación del signo

Usar b_N de 207, prolongado para 0<u≤1/2 mediante la misma suma espectral (ninguna afirmación sobre el dominio original de la forma es necesaria allí). Escribir w_ρ=|γ|−i sgn(γ)δ, con z=ρ−1/2=δ+iγ, y Θ=max_ρ |arg w_ρ|. Así tan Θ=max |δ/γ|. El promedio firmado contra cualquier frecuencia FIJA de log u decae como O_t(N^(−1/2)), independientemente de RH. Más precisamente, si RH falla, la energía a escala exponencial se concentra en las dos bandas |t|/(2N)≈tan Θ. Esto determina qué oscilaciones del parámetro hay que conservar antes de intentar una estimación de la energía.

**Factorización.** Para s=−3/2+it y N≥1 se cumple

    ∫₀^∞ u^(s−1)b_N(u)du = K_N(s) Z(s),
    K_N(s)=4^N Γ(N+s/2)Γ(N−s/2)/(2Γ(2N)),
    Z(s)=Σ_ρ w_ρ^s.

Las potencias usan la rama principal. Para w positivo real el integral de u^(s−1)[4u²w²/(u²+w²)²]^N es w^s K_N(s) por sustitución beta. Ambos lados son holomorfos para Re w>0, por dominación local en compactos, y por tanto coinciden allí. Para el intercambio de la suma con el integral usar |u²+w²|≥cos(Θ)(u²+|w|²). Tras escalar por |w| se obtiene para N fijo una constante por |w|^(−3/2); Z3 hace sumable la serie. En particular |Z(s)|≤C exp(Θ|t|). La desigualdad |K_N(s)|≤K_N(−3/2)=O(N^(−1/2)) sale del integral beta real y Stirling. Así toda banda |t|≤o(N) tiene energía a lo sumo exp(o(N)), también si algún cero sale de la línea.

**Dónde se alcanza el exponente.** Por Plancherel en log u la energía I_N=∫₀^∞ |b_N(u)|²du/u⁴ es (2π)⁻¹∫|K_N(s)Z(s)|²dt. Su raíz de orden 2N tiende a R=sec²Θ. En u≥3 el techo y el piso son los de 210 para b_N: en el caso fuera de línea el cuarteto extremo da el piso en un intervalo de ancho comparable a 1/N. Bajo RH el primer cero da el piso en un intervalo de ancho comparable a 1/√N por el perfil de 209 (o directamente por positividad de todos los sumandos). En 0<u<3, |h_u|<1 por 207 y la primera altura; Σ|h_u|≤Cu² por Z3 y |γ|>14. Esto da contribución acotada incluso con u⁻⁴. En el infinito la cota Cu log(2u) R^(N−1) de 210 asegura la integrabilidad.

Para y=|t|/(2N), Stirling uniforme en el semiplano Re z≥N−3/4 da

    |K_N(s) Z(s)| ≤ C N^(−1/2) (1+y²)^(−1/2) exp(N f(y)),
    f(y)=log(1+y²)−2y arctan y+2Θy.

En efecto los factores Γ(N(1±iy)±3/4) admiten la expansión uniforme de Stirling en el sector |arg z|≤π/2; los desplazamientos reales opuestos se cancelan en las potencias del módulo. El máximo único de f está en y=tan Θ, ya que f'=2(Θ−arctan y), y vale log R. Para ε>0 la parte |y−tan Θ|≥ε tiene supremo de f estrictamente menor: f tiende a −∞ en el infinito. Integrar la cota cuadrática usando ∫(1+y²)⁻¹dy<∞ muestra una brecha exponencial respecto de I_N, incluso bajo RH. En particular, bajo fallo de RH la energía restringida a | |t|/(2N)−tan Θ |<ε conserva el límite raíz R. No se requiere una hipótesis sobre separación de las ordenadas o ausencia de cancelación en Z(s): el piso lo da 210 antes de transformar.

**Uso y frontera.** 210 evita cancelación integrando el cuadrado en u. Aquí se calcula por qué medir sólo unos pocos momentos firmados de u, aun de frecuencia creciente o(N), perdería todo el crecimiento exponencial. La serie Z(s) se construye con los mismos ceros y su tipo Θ sólo da el techo anterior. Este cambio de variable no prueba Θ=0. El resultado es sobre la prolongación espectral de b_N; no se identifica la transformada de la suma prima truncada con K_N Z.

**Transferencia al observable aritmético finito.** Definir B_N(t)=∫₃ᴺ A_N(u)u^(−5/2+it)du con A_N de 210. Aunque no hay igualdad puntual con la factorización, sí hay una comparación L² uniforme:

    ||2B_N + K_N Z||_(L²(dt)) = O(1).

Por Plancherel basta estimar b_N+2·1_[3,N] A_N en L²(du/u⁴). En [3,N] usar el error absoluto Cu log(2u) de 210. En u<3 ya se dio la cota Cu². Para u>N≥4, 208 da |h_u(z)|≤M_(1/2)(u)≤exp(C/u²) para todo cero. La suma de primeros módulos de 210 da |b_N(u)|≤Cu log(2u) exp(CN/u²), con cuadrado integrable contra u⁻⁴ uniformemente en N sobre esa cola. Esto prueba la comparación.

Por tanto, si Θ>0, en el complemento de cada banda | |t|/(2N)−tan Θ |<ε, la energía de B_N tiene limsup de raíz 2N a lo sumo max(1,exp(sup_complemento f))<R. En la banda conserva exactamente la tasa R por 210. Ésta sí es una afirmación sobre primos finitos. En particular la raíz de la energía aritmética sobre |t|=o(N) tiene limsup ≤1 sin hipótesis, también si falla RH. Bajo RH la comparación O(1) no transfiere automáticamente la brecha exponencial del complemento espectral.
