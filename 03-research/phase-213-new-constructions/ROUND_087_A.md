# Un solo listado de polos: comparación bilateral con la ventana efectiva

Sea v=(v₁,…,v_n) una lista finita, con repeticiones permitidas, S=Σ1/v_j en un compacto J⊂(0,∞), V=min v_j y ε=Σv_j^(−3). Sea R(v,L) el menor cociente de la forma completa sobre los numeradores de ese listado, recortados a longitud L y normalizados por la norma recortada. Uniformemente para V grande, se tiene, para todo 0<α<1 y 0<s<1/2,

    λ_W(S)−C_{J,α}(log V / V)^(2α/3)
       ≤ inf_{L>0} R(v,L) ≤ R(v,2S)
       ≤ λ_W(S)+C_{J,s} ε^(2s/3)(1+|log ε|).

En el corte 2S vale además R(v,2S)≥λ_W(S). Aquí ε≤S/V². Aunque 086 optimizaba también sobre los listados y recuperaba por polos repetidos, cada listado individual con las condiciones anteriores aproxima el mismo mínimo a su propio S. Por ejemplo el error es O_{J,β}(V^(−β)) para cualquier β<2/3, tanto al corte 2S como para el ínfimo sobre las longitudes. Las constantes no se han evaluado.

**Cota inferior para cualquier corte.** La reflexión de 085 da log ||exp(σt)f||≤Σ log((1+σ/v_j)/(1−σ/v_j)) para ||f||=1. Si σ≤V/2, la serie de artanh acota esta expresión por 2σS+Cσ³ S/V². Tomar σ=V^(2/3)(log V)^(1/3), H=2S+D(log V/V)^(2/3), con D>C sup J+3. El argumento de 086 da ||exp(t) f 1_{t>H}||≤exp(H−σ(H−2S)+Cσ³ S/V²)≤V^(−2) eventualmente. Para L≤H la inclusión de ventanas da R≥λ_W(H/2). Para L>H, el cruce arquimediano de Carleman, el peine completo y los momentos polares se pagan como en 086 con coste O_J(V^(−2)), también al normalizar. El módulo de potencia de 077 en un compacto ligeramente mayor que J da el lado inferior.

**Cota superior para el listado prescrito.** Tomar t como variable física y B(z)=∏(1−z/v_j)/(1+z/v_j). Sea E el multiplicador de retardo exp(−2Sz). Sobre el eje imaginario, la fase de B es −2Σ arctan(ξ/v_j). De |u−arctan u|≤|u|³/3 y el módulo unitario se obtiene exactamente el mayorante

    |B(iξ)−E(iξ)| ≤ min(2, (2/3) ε |ξ|³).

Para 0≤q≤s/2 esto da ||(B*−E*)F||_{H^q} ≤ C_s ε^((s−q)/3)||F||_{H^s}, donde los asteriscos denotan multiplicadores adjuntos sobre toda la recta. Elegir un minimizador normalizado de la ventana trasladada a [0,2S]; su extensión por cero tiene norma H^s acotada uniformemente en J por 077. Por soporte, P_+E*F=0, con P_+ la restricción a tiempos positivos. Como en 086, Q_B F=F−B P_+B*F pertenece al modelo racional del listado. Así para g=1_[0,2S] Q_B F el error e=F−g satisface la misma cota en H^q, hasta una constante uniforme. Se usa que las restricciones a semirrectas e intervalos son acotadas uniformemente para q∈[0,s/2], por interpolación entre L² y H^(s/2). En particular ||g||→1 uniformemente.

Sobre este soporte fijo, la parte acotada de W tiene norma O_J(1); el peso logarítmico arquimediano está dominado por C q^(−1)(1+ξ²)^q para q>0 pequeño. Elegir q=1/|log ε| para ε suficientemente pequeño. La ecuación propia de F cancela los términos lineales, de modo que
    
    W(g)/||g||²−λ_W(S)=[W(e)−λ_W(S)||e||²]/||g||²
                          ≪_{J,s} (1+|log ε|) ε^(2s/3).

El paso de fase cúbica se usa antes de la estimación de energía; un control meramente cualitativo de la densidad no da esta comparación finita.

**Límite del mayorante de fase.** Para n polos iguales v=n/S con S fijo, ε=S³/n². En ξ=ε^(−1/3) la diferencia de fases tiende a 2/3, pues el siguiente término en la expansión de arctan cuesta O(n^(−2/3)). Por continuidad en frecuencia esto da norma ≳ε^(s/3) para B−E de H^s a L². El cálculo muestra la escala donde deja de funcionar la aproximación uniforme del multiplicador; no demuestra optimalidad de la tasa de los mínimos ni de los errores tras proyectar.

**Cotejo.** POWER_CONFLUENT_BRIDGE_014 §6 tiene distancias exactas para tests exponenciales en el modelo repetido; 086 identifica el límite variacional; 077 suministra regularidad y continuidad en ventana. La contribución presente es la comparación con error para un listado prescrito, incluidos polos distintos o confluyentes y todos los términos aritméticos. No es una cota uniforme en S→∞ ni una prueba de signo para la ventana aproximada.
