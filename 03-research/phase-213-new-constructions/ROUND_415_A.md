# Qué detectan las derivadas del déficit integrado

**Estado: PROVED, con revisión independiente de la inversión de Laplace, el coeficiente oscilatorio y el límite gamma.**

Para el D de 412 sea F(s)=D(√s)/√s. Si se ha verificado la recta crítica hasta altura H≥2, entonces para todo s>0

    (−1)^n F^(n)(s) ≥ 0 si (n+1) 2 arctan(1/(2H)) ≤ π/2.

Con H=3·10¹² esto incluye todos los órdenes enteros de 0 a 4.7·10¹². Si existe un cero exterior, la desigualdad falla en algún s positivo para cada n suficientemente grande.

**Demostración.** Para cada cero superior, contado con multiplicidad, poner d=|Re ρ−1/2|. Integrando dos veces la identidad de 414 se obtiene F(s)=4Σ∫₀ᵈ(d−u) Re[1/(s+(γ+iu)²)]du. El argumento del denominador es a lo sumo 2 arctan(u/γ); al derivar n veces, su recíproco queda elevado a n+1 y multiplicado por (−1)^n n!. La convergencia local de las series derivadas sigue de Σγ⁻²<∞.

La densidad inversa de Laplace es

    K(t)=4Σ∫₀ᵈ(d−u) exp(−(γ²−u²)t) cos(2γut)du.

Es continua para t>0 por convergencia local uniforme. La integral de la serie de valores absolutos es finita por Σ d²/(γ²−1/4)<∞, justificando el intercambio de integrales. Si existe un cero exterior, tomar el mínimo A de γ²−d² entre ellos. Lo alcanzan finitos ceros y hay un salto positivo hasta los restantes, por finitud local. Su contribución restante es O(exp(−(A+ε)t)) para t≥1, sumando primero a t=1.

Para cada minimizador sustituir v=t(d−u). Tras multiplicar por t² exp(At), su contribución es
4 Re[exp(−2iγdt)/(2d−2iγ)²]+o(1), por convergencia dominada con mayorante 4v exp(−dv). A fijo, la frecuencia 2γd determina γ y d porque (γ+id)²=A+2iγd. Las multiplicidades se suman. El polinomio trigonométrico resultante tiene media cero y media cuadrática positiva. Como es acotado, la media inferior de su valor absoluto es positiva; ambas partes de signo tienen por ello media inferior positiva. Así K toma valores estrictos de ambos signos a tiempos arbitrariamente tardíos.

Fijar t₀ con K(t₀)<0. La derivada de orden n con signo alternado, en s=(n+1)/t₀, tiene el signo de la integral de K contra la densidad gamma proporcional a tⁿ exp(−st). Estas densidades tienen media t₀ y varianza t₀²/(n+1). Fuera de cualquier entorno fijo de t₀ su supremo tiende a cero por unimodalidad y Stirling; allí basta la norma L¹ de K. Por continuidad la integral converge a K(t₀).

**Registro de revisión.** La identidad de412 da J_R''(u)/R=4Re[1/(R²+(γ+iu)²)], confirmando el factor4 enF y enK. El argumento del denominador a s>0 no supera2arctan(u/γ); por eso la condición sobre n+1, y no sobre n, garantiza el signo. La normaL¹ deK es finita por el mayorante2Σd²/(γ²−1/4), mientras su continuidad sólo se necesita para t>0; no se presupone K acotada en0.

En el mínimo A, el cambio v=t(d−u) da exactamente t²exp(At)K_ρ(t)=4Re[exp(−2iγdt)∫₀^(td) v exp(−2dv+v²/t+2iγv)dv]. La dominación porv exp(−dv) conduce a1/(2d−2iγ)², con el signo y coeficiente anunciados. Los ceros reflejados con el mismoγ y|δ| suman sus multiplicidades; no cancelan esta frecuencia. Distintos minimizadores con igualA tienen distinta2γd salvo esa duplicación, pues la raíz cuadrada deA+2iγd fijaγ,d>0. La media cuadrática positiva y la media cero dan valores positivos y negativos separados de0 para el polinomio en tiempos arbitrariamente tardíos, suficientes para absorber el restoo(1) y los exponentes posteriores.

Al normalizar tⁿexp(−s_nt), s_n=(n+1)/t₀, se obtiene la densidad gamma de forma n+1, media t₀ y varianza t₀²/(n+1). Por Stirling su supremo fuera de un entorno fijo de t₀ tiende a0; multiplicarlo por la normaL¹ deK controla incluso la zona próxima a0. En el entorno se usa continuidad. Así el promedio gamma converge aK(t₀)<0 para todos los n suficientemente grandes, y no sólo a lo largo de una subsucesión. Esto prueba exactamente el fallo eventual de cada orden alto si existe un cero exterior, sin contradecir el rango finito garantizado porH.

**Alcance.** La fase 101 ya registra criterios abstractos de monotonía completa. Aquí se identifica el término oscilatorio que impide extrapolar los órdenes finitos para el déficit específico de 412. La monotonía completa de F equivale a RH, ya que bajo RH F es idénticamente cero. Queda abierta una cota independiente sobre la contribución de las ordenadas. La positividad de todas las diferencias diádicas iteradas no se deduce de 414.
