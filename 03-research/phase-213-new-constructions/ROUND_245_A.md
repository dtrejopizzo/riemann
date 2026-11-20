# Dos incrementos de un promedio positivo con datos de primos anteriores

Para t grande y cada racional fijo 0<c<1/4 usar n=floor(ct), δ=exp(−log²t)/t² y, con S de 240, calcular

    J(v)=(3/2)^n ∫₀^∞ S(t+v−z) exp(−z) z^(n−1)/(n−1)! dz,
    F(v)=J(v+δ)−exp(δ)J(v).

Los parámetros t,n,δ se congelan en las tres evaluaciones necesarias v=0,δ,2δ de J. Cada J es una suma finita de contribuciones positivas de primos p≤exp(t+2δ+1/10), pues el soporte de W está en [0,1/10]. No hace falta elegir parámetros según ceros para definir la familia.

**Criterio.** El signo global equivale a que para cada tal c existan inicios t→∞ con ambos |F(0)|, |F(δ)|≤exp(t/2+o(t)). Las subsucesiones pueden depender de c. Si falla RH existe incluso un intervalo abierto de pendientes para las que todos los bloques suficientemente lejanos incumplen la cota.

**Transformación exacta.** Aplicar la expansión de 240 a S(u), incluyendo su media H(1)exp(u). El resto es O(exp(u/2)poly(1+u)) para u≥0. Para u<0 definir el resto por la identidad: es O(1) porque S(u) es acotada y la serie de ceros converge absolutamente con |exp(ρu)|≤1. En el promedio los u≥0 cuestan O(exp(t/2)poly(t)) usando la transformada gamma en 1/2; los u<0 cuestan O((3/2)^n), menor que exp(t/2). Integrar cada modo está justificado por convergencia absoluta para t fijo. El principal desaparece en F y el modo ρ en J se multiplica por [3/(2(1+ρ))]^n. En RH todos los modos quedan acotados en suma por C exp(t/2), pues |1+ρ|≥3/2. Esto prueba la condición en todo inicio bajo RH.

**Máximo alcanzado después de promediar.** La tasa de cada modo en J es
     
    b_c(ρ)=Re ρ+c log(3/(2|1+ρ|)).

Dado un cero con Re ρ>1/2, para c positivo pequeño su tasa supera 1/2. En un intervalo compacto de esas pendientes, sólo un conjunto finito puede competir, ya que b_c tiende uniformemente a menos infinito con la altura. Dos rectas de tasas idénticas exigirían iguales Re ρ e |1+ρ|, luego las raíces serían iguales o conjugadas. Excluir los finitos empates del conjunto competidor deja un subintervalo con par conjugado único y cualquier racional de él sirve. Para c fijo allí, sea D>1/2 la tasa ganadora, con brecha η>0 a las restantes tasas y a 1/2. El redondeo de n cuesta a lo sumo un factor O(1+|ρ|) en cada término. Los momentos de H sumables de 240 dan una cola total O(exp((D−η)t)), reduciendo η para absorber el polinomio del resto. Esto también vale en ambas primeras diferencias.

**Dos lecturas.** Para el cero ganador ρ=β+iγ, la contribución del par a F(v) es 2 Re(Z exp(ρv)), con |Z| comparable a δ exp(Dt): el coeficiente incluye H(ρ) no nulo, multiplicidad y exp(ρδ)−exp(δ). Para todo complejo Z, max(|Re Z|, |Re(Z exp(iγδ))|)≥|Z| |sin(γδ)|/2 (usar la identidad para el seno de la diferencia de fases). Como γ es fijo y distinto de cero, al menos una lectura tiene módulo ≥C δ² exp(Dt), que domina el error exponencial. Esto prueba la recíproca aun si la desviación máxima de los ceros originales nunca se alcanza.

**Antecedentes y obligación.** La selección por tasas ya estaba en 143 y 206. La novedad interna frente a esos pasos es la condición de dos incrementos adyacentes de una sola suma positiva sobre primos, por pendiente, con corte superior finito y sólo existencia en una subsucesión. El resultado cambia S por J; no produce dos nodos del conteo sin promediar de 244. El dato pendiente es una propiedad aritmética de J: obtener dos incrementos pequeños consecutivos por cada c. La positividad de los pesos de J no fija el signo ni el tamaño de sus incrementos.

**En las pendientes que detectan el fallo, una lectura aislada sí se anula.** En cada tramo ct∈[n,n+1) el argumento del coeficiente dominante de F(0) es γt más una constante dependiente de n y un término o(1) uniforme: (exp(ρδ)−exp(δ))/δ→ρ−1. La longitud 1/c>4, y |γ|>14 por la primera ordenada verificada. En el interior caben fases lineales de coseno +1 y −1. Allí el término dominante supera el error con signos opuestos. Por continuidad en el tramo, F(0)=0 en algún inicio para cada n grande. En esos mismos inicios la segunda lectura excede el umbral por el resultado anterior. Esto comprueba que exigir ambas lecturas tiene contenido incluso tras el promedio.
