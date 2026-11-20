# Umbral exacto de masa absoluta a segundo orden

**Estado: PROVED, con revisión independiente de la pérdida de fase, los intervalos cortos y la optimización deβ.**

Sea A(Y)=Σ g(log(x/n)) sobre productos libres de cuadrados de primos en (z,Y], z=L², b=log z. Para Y=(4+κ/b)z, con κ real fijo, bajo RH,

    log(A(Y)/|S|)=[κ/4−2(1+log 2)log 4+o(1)] L/b².

Así, para κ estrictamente mayor que la constante de 394 hay masa suficiente en cada escala, por un factor que tiende a infinito. El signo de los productos permanece decisivo. El equivalente para A que usamos es incondicional.

**Silla del producto positivo.** Poner H(s)=Ls+(s−1/2)²/2+Σ_{z<p≤Y}log(1+p^(−s)). La raíz real β de H'=0 satisface β=1/2+(log 2+o(1))/b por PNT en el intervalo y convexidad estricta. En efecto Σ log p/(1+p^s)∼2(√4−1)e^(−c)L para s=1/2+c/b. En un entorno de radio O(1/b) de β se tienen H''≍Lb y |H'''|≪Lb² (también sobre la vertical para la tercera derivada), por las series de los factores y log p∼b. Se obtiene

    A(Y)∼exp(H(β))/sqrt(2πH''(β)).

Para verificarlo, invertir el producto finito directamente en β. Para a_p=p^(−β), la pérdida log(1+a_p)−log|1+a_p exp(−it log p)| es ≥c a_p(1−cos(t log p)), por el cuadrado del módulo. En |t|≤1/(2b) esto da pérdida ≫Lb t². En 1/(2b)≤|t|≤2√L aplicar la estimación por subintervalos primos de 367 a [2z,3z], donde a_p≍1/L. En la variable log p, un subconjunto de longitud total ≫1 tiene 1−cos(t log p)≫min(t²,1); se puede seleccionar en intervalos de longitud ≫1/(1+|t|). En p esos tramos tienen longitud ≫z^(3/4), suficiente para el PNT corto usado en 367. Se obtiene pérdida ≫L/b³. Para |t|>2√L basta la cota por el propio producto positivo en β y la cola gaussiana. Finalmente t=w/√H'' da el equivalente por Taylor y dominación gaussiana, pues Lb²/(Lb)^(3/2)→0. El argumento usa fase de Fourier sólo para contar A en la misma escala, sin cambiar el signo de los coeficientes de A.

**Coste de optimizar la silla.** Sea α la silla exacta de 394. Se cumple H'(α)=O(L/b). Para verlo, comparar las sumas log p·p^(−α) en (z,Y] y hasta z: las potencias superiores de ambos productos cuestan O(b²), y para las primeras potencias el PNT da las integrales de t^(−α)dt con error o(L/b). Al escalar por 4, el multiplicador es 4^(1−α)=2+O(1/b); mover Y en O(z/b) aporta O(L/b). Usar la ecuación exacta de α da la estimación. La convexidad y H''≍Lb entre α y β implican |β−α|≪1/b² y H(β)=H(α)+O(L/b³). Este error desaparece en la escala L/b².

En H(α) reemplazar los logaritmos por las primeras potencias cuesta O(b²), tanto para el producto positivo como para el inverso hasta z de 368: α≥1/2 eventualmente y Σ_{n≤Y}1/n=O(b). Los prefactores de ambas sillas cuestan O(log L) en logaritmo. Por ello la diferencia logarítmica es justamente I(Y)−2I(z)+o(L/b²) de 394, esta vez en ambos sentidos. En el valor crítico exacto de κ el equivalente no decide.

**Registro de revisión.** El intervalo[2z,3z] está contenido en(z,Y] para todoκ fijo y x grande. En el tramo de frecuencias |t|≤2sqrt L, las piezas de fase favorable tienen longitud en p al menos c z^(3/4); si alguna es demasiado larga para el enunciado citado de PNT corto se subdivide, conservando el piso de fase. Quedan longitudes entre una potencia mayor que17/30 y una menor que1, dentro del alcance del corolario1.3 de Guth–Maynard usado en367. Su masa total ponderada es≳L/b y el peor factor min(t²,1) es≳1/b², dando la pérdida L/b³. Cerca de0 el piso Lb t² permite dominación gaussiana sin constantes auxiliares de zeta; fuera de2sqrt L se usa directamente |∏(1+p^(−β−it))|≤∏(1+p^(−β)). Así el equivalente deA es incondicional.

Las sillas α,β ya están ambas en1/2+(log2+o(1))/b, por lo que H''≍Lb en todo el segmento que las une. El error H'(α)=O(L/b) da por valor medio |β−α|=O(b^(−2)); integrar de nuevo la derivada da |H(β)−H(α)|=O(L/b³), aunque H(β)≤H(α) por convexidad. Este coste es de orden inferior al término L/b² comparado en394. El resultado por encima de la constante crítica afirma que la masa totalA supera |S|; no prueba que exista un peso terminal firmado que realiceS ni determina su signo. No se afirma uniformidad enκ creciente.
