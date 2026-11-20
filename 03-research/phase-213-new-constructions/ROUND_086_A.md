# La suma de recíprocos es exactamente la semilongitud de la ventana límite

Fijar S>0. Denotar por b(V,S) el ínfimo de W(g)/||g||² sobre todas las longitudes L>0 y todos los tests no nulos de 085 con v_j≥V y Σ 1/v_j≤S. No se restringe la dimensión, el numerador ni la multiplicidad. Entonces, incondicionalmente,

    lim_{V→∞} b(V,S)=λ_W(S),

donde el miembro derecho es el mínimo de la forma completa en el intervalo de longitud 2S. En particular, subir las tasas dejando libre la dimensión a presupuesto fijo no hace desaparecer la dificultad de esa ventana.

**Localización inferior, incluso para cortes arbitrariamente lejanos.** Normalizar ||f||=1. Dado H>2S, elegir η∈(0,1) con H>2S/(1−η²) y poner σ=ηV>1. La estimación de 085 da ||exp(σt)f||≤exp(2σ S/(1−η²)). Así, para cualquier L>H, k=f 1_(H,L] satisface
     
    ||exp(t)k||≤δ=exp(H−σ[H−2S/(1−η²)]).

También ||exp(t)f||≤exp(2S/(1−V^(−2))) para V>1. Si L≤H basta la monotonía del dominio. Para L>H escribir g=h+k, con h=f 1_[0,H]. Las normas de g y h tienden uniformemente a 1 pues la misma estimación de cola vale con L infinito. El término arquimediano de k es ≥m(0)||k||². El cruce de h y k cuesta ≤5||h||||k|| antes del factor 2: el núcleo exterior es −K(v+w)/2, con K(u)≤3/u por la fórmula de 077 (separar u≤1 y u≥1), y la norma del operador de Carleman es ≤π por su integral de dilataciones. Esto permite comparar las energías sin exigir que la derivada de la cola sea pequeña.

Para u≥0 el cambio en la autocorrelación al pasar de h a g es la integral con el tiempo mayor en (H,L], acotada por exp(−u)||exp(t)k||·||g||. Pagar todo el peine cuesta ≤2δΣ(log n)n^(−3/2)<12δ. Cada momento polar de la cola cuesta ≤δ por Cauchy contra exp(−t/2); los momentos de h y g son ≤||exp(t)f|| por la misma razón. El cambio polar cuesta ≤4δ||exp(t)f||. Por tanto W(g)≥λ_W(H/2)||h||²−O_S(δ+δ²). Tomar V→∞ y después H↓2S, usando la continuidad de P47. Esto prueba el liminf también si λ_W(H/2) es negativa.

**Recuperación del intervalo entero.** Usar n veces el polo v=n/S. El producto interior B_n(s)=[(1−sS/n)/(1+sS/n)]^n converge puntualmente en el eje imaginario a exp(−2Ss) y tiene módulo 1 allí. En Fourier físico, sus multiplicadores unitarios y sus adjuntos convergen fuertemente a la traslación por 2S y su inversa, respectivamente, en cada H^q(ℝ), por dominación. Elegir 0<q<1/2 y denotar por P_+ la proyección por soporte en tiempos positivos, acotada en H^q por la desigualdad de Hardy usada en 077. Sobre funciones causales, el operador
    
    Q_n=I−B_n P_+ B_n^*

es la proyección ortogonal L² al complemento de B_n H² en el espacio de Hardy causal. Su imagen es el espacio de numeradores de grado <n sobre (s+n/S)^n: por ejemplo, la descomposición ortogonal de los productos de Blaschke en n factores da precisamente la base de Malmquist de 084. Aquí B_n y su adjunto en la fórmula son multiplicadores del espacio completo antes de aplicar P_+. El límite fuerte en H^q, sobre entradas causales, es la restricción a [0,2S]. Para cualquier test suave compacto dentro de ese intervalo, Q_n f converge por tanto a f en H^q. Recortar otra vez a [0,2S] preserva la convergencia por el multiplicador de intervalo en H^q. Los coeficientes pueden tomarse reales para entradas reales. En soporte fijo esta convergencia implica la de la norma de forma por log(2+|ξ|)≪_q(1+ξ²)^q y acotación de peine y polar. Los tests suaves interiores son un núcleo de forma (P47, dilatación hacia dentro y alisado). Así b(V,S)≤λ_W(S) para cada V, tomando n arbitrariamente grande con n/S≥V. Se cierra la igualdad. La aproximación de un retardo por factores racionales y la proyección de Hardy son clásicas; importa aquí que se recupera la energía de la forma completa en una ventana de tamaño EXACTAMENTE 2S.

**Un sector ampliado con constantes.** Si S≤3/4 y V≥10000, hay en todas las longitudes W(g)≥(10^(−18)/2)||g||². Tomar H=log 5, donde P47, thm:log5W, da λ_W(H/2)≥10^(−18). Para L≤H se aplica directamente. En el otro caso elegir η=1/8: H−(3/2)/(1−1/64)>0.08, σ≥1250 y δ≤5 exp(−100). Además ||exp(t)f||<5 y m(0)>−6. Así la pérdida en W es ≤42δ+6δ² y ||h||²≥1−δ² (aplicar el control a toda la cola). Estas cifras implican el margen indicado pues ||g||≤1. La comparación con 085 cambia dos parámetros: el presupuesto crece de 1/512 a 3/4 y se exige una tasa mínima más alta; el margen demostrado es menor.

**Cotejo y límite.** 002/014 usan densidad de modelos racionales para el puente global; 085 controla el orden mediante el presupuesto recíproco. Aquí las dos direcciones identifican el valor variacional límite con presupuesto fijo y polos que escapan a infinito, incluso optimizando sobre L. El resultado transporta márgenes de ventanas conocidas y muestra exactamente qué positividad sería necesaria para extenderlos a presupuestos mayores. No prueba que λ_W(S) sea positiva para todo S.

Antecedente puntual: POWER_CONFLUENT_BRIDGE_014 §6 ya da la distancia de una exponencial al modelo móvil y el criterio n/v→∞ para densidad en toda la semirrecta. A cociente finito S esa distancia ya refleja la cola tras 2S. La identificación variacional aquí incluye el recorte físico, todos los tests del dominio por densidad y, en el liminf, configuraciones arbitrarias de polos y longitudes.
