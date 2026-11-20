# Las dos frecuencias dominantes del mayorante en la silla positiva

**Estado: PROVED, con revisión independiente de la normalización, la varianza y la exclusión uniforme de frecuencias lejanas.**

Sean β y H la silla y exponente positivos de 395, Y=(4+κ/b)z a κ fijo. Denotar por B el mayorante obtenido al integrar en β el módulo del integrando firmado, incluyendo 1/(2π). Entonces, incondicionalmente,

    log(B/A)=−(π² V/2+o(1))L/b³,
    V=4−2(log 4)²>0.

Poner μ=2log 4−2, t₀=π/(b+μ). Para cada ε>0 fijo, la parte de B fuera de los dos intervalos |t∓t₀|<ε/b² es ≤B exp(−c_ε L/b³). Esto localiza el mayorante; en la integral firmada los dos intervalos son conjugados y aún puede haber oscilación dentro de ellos.

**Medida de los logaritmos.** Para a_p=p^(−β), M=Σa_p∼L/b por la ecuación de silla (log p=b+O(1); los cuadrados cuestan O(1)). Con pesos a_p/M, los valores v_p=log(p/z) convergen en distribución sobre [0,log 4] a la densidad exp(v/2)/2 por el PNT y β→1/2. La integral de la densidad es uno; su media y su varianza son μ y V por integración. Soporte acotado da convergencia de ambos momentos.

**Pérdida próxima a una fase impar.** Para |t|≤K/b con K fijo considerar

    D(t)=Σ log((1+a_p)/|1−a_p exp(−it log p)|).

Uniformemente D(t)=Σ a_p(1+cos(t log p))+O(Σa_p²), con Σa_p²=O(1), despreciable ante M/b². Si tb=ℓπ+h/b para ℓ impar fijo y h acotado, Taylor da

    b²D(t)/M = [(h+ℓπ μ)²+(ℓπ)² V]/2 + o(1).

Si b dist(tb,π+2πℤ)→∞ con |tb|≤K, entonces b²D(t)/M→∞: las perturbaciones tv_p son O_K(1/b) y 1+cos se acota inferiormente por una constante por la distancia angular al impar más próximo al cuadrado. Por compacidad secuencial, el mínimo normalizado en este tramo es π²V/2+o(1) para K>π. Sólo ℓ=±1 e h→−ℓπμ lo alcanzan; fuera de las dos bandas indicadas hay un margen fijo (dependiente de ε).

**Excluir frecuencias lejanas e integrar.** Para K/b≤|t|≤2√L, la estimación de fase en 396 da D(t)≫(L/b)min(t²,1), con constante absoluta independiente de K. Elegir K fijo suficientemente grande para superar el mínimo normalizado por un margen. Más allá de 2√L basta la cola gaussiana. Estos techos pierden a lo sumo O(log L) en logaritmo al integrar y normalizar por A∼exp(H(β))/√(2πH''(β)). Para el piso de B usar |t−t₀|≤b^(−3): en toda esa banda h=−πμ+o(1), se conserva el mínimo hasta o(1) y el logaritmo del ancho es despreciable. Esto da el equivalente y el ahorro exponencial exterior. Un peso terminal en [0,1] cambia los logaritmos de los productos en O(1/L) en la vertical, así que las afirmaciones persisten.

**Registro de revisión.** Para q=log4, la densidad exp(v/2)/2 en[0,q] integra a1; sus momentos son2q−2 y2q²−8q+8. Al restar el cuadrado de la media se obtiene exactamente V=4−2q²>0, siendo también positivo por no degeneración de la densidad. La ecuación de silla da M∼L/b, por lo que M/b²∼L/b³ sin un factor2 adicional. En tb=ℓπ+h/b, la desviación angular es(h+ℓπv_p)/b+O(b^(−2)), que fija la constanteπ²V/2 y los centros±π/(b+μ) a error o(b^(−2)). El error uniforme O(Σa_p²)=O(1) es o(M/b²).

Para K/b≤|t|≤1, el lema de396 da D(t)≥cK²L/b³; para1≤|t|≤2sqrt L da D(t)≥cL/b, con la misma constante absoluta. Así se puede fijar K grande una sola vez para separar todas esas frecuencias del mínimo; no se extrapola el Taylor de fase a frecuencias crecientes. En el tramo compacto restante, la extracción de subsucesiones distingue h acotado de b·dist(tb,π+2πℤ)→∞ y da el margen uniforme fuera de las bandas de radioε/b². La banda inferior de anchura b^(−3) y los prefactores sólo cuestan O(log L), menor que L/b³; esto permite convertir los márgenes del exponente en la concentración relativa aB. Ponderar el último factor altera su logaritmo de módulo en O(1/L) uniformemente en t, pues su radio es O(1/L)<1, por lo que tampoco crea una frecuencia adicional de magnitud comparable.

La constante es del mayorante en esta vertical. Obtener la fase del pulso exige estudiar la suma de las dos integrales complejas y compararla con el error exterior antes de atribuirle un signo.
