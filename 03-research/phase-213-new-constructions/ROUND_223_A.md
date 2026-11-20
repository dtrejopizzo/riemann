# La constante de estabilidad de 222 es exacta para perturbaciones sobre los primos

Para cada A>0 existen pesos relativos positivos λ_p→1, sobre los mismos primos, tales que D(x)=Σ_(p≤x)(λ_p−1)log p satisface la hipótesis de 222 con ese A y

    limsup log(1+|C_k(λ)−C_k(1)|)/k = 4A^(3/2)/(9√3).

Puede conservarse exactamente la masa en cada bloque modificado. La conclusión es para la diferencia de las muestras. No afirma un comportamiento extremo de la muestra auténtica C_k(1).

**Escala que faltaba en 221.** Fijar z>0, N=k², L₀=z k^(3/2), X=exp(L₀), m(a)=log M_a(3) y elegir a por Nm'(a)=L₀. Existe para k grande y a=(9/2)z/√k+O(k^(−3/2)) por m(a)=a²/9+O(a⁴). Así

    Nm(a)−aL₀=−9z² k/4+O(1).

El perfil de 221 para a fijo no basta aquí. Para L=L₀+d con d en un compacto, s=−√k+ik e I_k de 218 se obtiene uniformemente

    L√N I_k(L)/(3^s exp(Nm(a)−aL))
       = Re[K_a exp(iNθ_a+ix_a d)/(a−ix_a)] + o(1).

Las constantes x_a,K_a,θ_a son las de 212 a tasa 3; x_a→3 y K_a converge a una constante no nula.

**Integrar primero en la tasa.** En el contorno a tasa 3 escribir u=3t. La integral de Fourier de I_k es 3^s/(2π) por el integral en τ de H₃(τ+ia)^N multiplicado por

    ∫₁^T t^s exp((iτ−a)Lt)dt.

El extremo T viene del corte original y u≤N. Uniformemente en d compacto, T≥2 eventualmente porque log X_N(6) tiene orden N. Cerca de los dos máximos ±x_a, |a−iτ| está separado de cero. Integrando dos veces por partes se obtiene el término exp((iτ−a)L)/[(a−iτ)L] con error en módulo ≤C exp(−aL)/L por

    O(k/L + k²/(aL²) + (1+k/L)exp(−aL)) = o(1)

como factor adicional. Para el resto usar |s(s−1)t^(s−2)|≤Ck² y ∫₁^∞ exp(−aLt)dt=exp(−aL)/(aL). La elección de dos integraciones evita una pérdida al acercarse a cero la altura del contorno. Fuera de vecindades fijas de ±3 usar directamente |integral interior|≤exp(−aL)/(aL). La integral allí de |H₃(τ+ia)|^N es exponencialmente menor que exp(Nm(a)) por separación uniforme, incluyendo la cola racional. Los errores integrados en los dos picos usan ∫|H₃|^N≤C exp(Nm(a))/√N.

**Uniformidad de la aproximación gaussiana.** Para 0≤a≤a₁ pequeño, los máximos siguen en dos vecindades disjuntas, con curvaturas reales negativas separadas de cero, por continuidad desde a=0. El logaritmo local tiene terceras derivadas acotadas en esas vecindades. En τ=x_a+w/√N el término lineal se cancela exactamente con iL₀(τ−x_a) por la elección de a. Tras extraer la fase central el integrando está dominado por C exp(−c w²); en compactos difiere en o(1) del perfil cuadrático con coeficiente h''(x_a+ia) y amplitud 1/(a−ix_a). Esto también vale uniformemente para d compacto. El otro pico es conjugado en el término principal; el prefactor complejo 3^s se extrajo antes. Queda probado el perfil relativo anterior, con control en la escala exponencial apropiada.

**Pesos sobre los primos.** Sobre un compacto fijo de d que contenga varios períodos, el perfil real principal tiene un intervalo donde supera c y otro donde es menor que −c, ambos de una misma longitud fija, para todo k grande. Esto sigue del módulo no nulo de K_a/(a−ix_a) y x_a→3. Aplicar pesos relativos adicionales +b y −b' en los dos intervalos, con

    b=X^(−1/2)exp(A L₀^(2/3)).

Escoger b' haciendo cero exactamente el cambio total de masa logarítmica. PNT da b'/b entre dos constantes positivas, uniformemente para estos intervalos móviles dentro del compacto. El cambio acumulado dentro del bloque está acotado por C√X exp(A L₀^(2/3)); se anula al salir. Los nuevos pesos son positivos para k grande. Al proyectar el cambio de C_k sobre la dirección 3^(ik), las dos contribuciones se suman con el mismo signo. La masa logarítmica en cada intervalo es comparable a X y allí p^(−1/2) es comparable a X^(−1/2). Por el perfil demostrado, la magnitud del cambio es al menos

    exp([A z^(2/3)−9 z²/4] k − o(k)).

Para construir un único sistema fijo de pesos, elegir los bloques sucesivamente por encima del corte máximo de todos los órdenes anteriores. La perturbación previa es finita en cada paso y su efecto tiende a cero con k por la envolvente de 211 y el peso de 217. Los bloques futuros no afectan a la muestra actual. La cota de D(x) vale globalmente por la masa cero y por log x=L₀+O(1) dentro de cada bloque. Elegir z=(4A/27)^(3/4) maximiza el exponente positivo y alcanza la cota superior de 222. Para A=0 la estabilidad ya se probó allí.

**Decisión.** La barrera de 222 es exacta aun imponiendo positividad, soporte en los primos reales y conservación de masa por bloques. Rebajar la constante o reemplazar el o((log x)^(2/3)) por O((log x)^(2/3)) en un teorema general de transferencia subexponencial requiere hipótesis adicionales.
