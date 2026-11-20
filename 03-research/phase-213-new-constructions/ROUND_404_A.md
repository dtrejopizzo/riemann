# Una parte de la suma de residuos ya cumple un ahorro exponencial

**Estado: PROVED, con revisión independiente de la comparación de contornos y la orientación parabólica.**

Sean α,K,T₀ de 403, b=log z, z=L². Existen η,c₁>0 absolutos y bordes seguros σ₀=α+δ (0≤δ≤1/L), H∈[2√L,2√L+1], tales que en la suma rectangular R de 403 basta retener los ceros ρ=β+iγ con

    β−γ²/(2L)>σ₀+η/b.

Si R_par es la suma retenida con residuos completos, se tiene |R−R_par|≪T₀ exp(−c₁ L/b). Esto estima el saldo agregado de los residuos retirados, sin estimar cada multiplicidad por separado. En particular S=R_par−(1+o(1))T₀. Las exclusiones parabólicas de 364–366 tenían parámetro de difusión fijo; aquí el pulso tiene varianza uno y la parábola depende de L.

**Ahorro uniforme del producto en las alas.** Para 1≤|t|≤H y α≤σ≤1+1/L hay c₂>0 con

    log|E_z(σ+it)| ≤ log E_z(α)−c₂ L/b.

Si σ≤α+1/b, los primos de [z/2,z] tienen p^(−σ)≍p^(−α); en una proporción fija de la banda la fase está separada de 2πℤ por 367, usando intervalos cortos hasta altura H. Esto da pérdida ≫L/b respecto al producto real E_z(σ)≤E_z(α); los términos de potencias mayores añaden pérdidas no negativas. Si σ≥α+1/b, ya el decaimiento del producto real cuesta ≫L/b por los mismos primos, pues 1−p^(−1/b) está separado de cero. Elegir 0<η<c₂/4.

**Comparación de contornos.** Conservar sin cambios el segmento σ₀+it para |t|≤1. En cada extremo conectar horizontalmente con la nueva curva de abscisa

    s_R(t)=min(1+1/L, σ₀+η/b+t²/(2L)),    1≤|t|≤H.

No hay ceros no triviales a alturas |γ|≤2 (también basta la verificación finita utilizada en 367). Para escoger δ, excluir bandas de radio 4L^(−2) tanto en torno a β−α como a β−α−η/b−γ²/(2L) para todos los ceros hasta H+2 (usar de antemano 2√L+4). La longitud perdida es o(1/L) por el conteo de 403. En la parte curva no saturada la pendiente es O(L^(−1/2)); esa exclusión da distancia euclídea ≫L^(−2) a los ceros, incluso mirando alturas vecinas. En la parte saturada la separación horizontal ya es ≥1/L. Elegir H seguro como en 403. Por tanto 1/ζ cuesta a lo sumo exp(O(log² L)) sobre ambos recorridos.

En las alas de la nueva curva el coste (s_R(t)−α)L−t²/2 es ≤δL+ηL/b, también cuando está saturada. En el conector horizontal a |t|=1 vale la misma cota. El ahorro del producto domina ese coste, la longitud O(√L), el prefactor gaussiano real y la cota de 1/ζ. Toda la integral en estas piezas cuesta ≪T₀ exp(−c₁L/b), reduciendo c₁ para absorber el prefactor √K''. Lo mismo vale en las alas rectas originales y en la tapa a H por el argumento de 403. Al restar los dos recorridos se cancela exactamente el tramo central común. El teorema de los residuos da la cota anunciada para su diferencia, y la saturación a la derecha de uno no elimina ningún polo que cumpla la desigualdad indicada.

**Registro de revisión.** Las dos familias de exclusiones paraδ consumen O(sqrt L log L·L^(−2))=o(1/L) incluso contando multiplicidades. En un punto de la curva no saturada con |t−γ|<L^(−2), su pendiente O(L^(−1/2)) cambia la abscisa en o(L^(−2)); el margen4L^(−2) a la alturaγ deja por tanto distancia euclídea≫L^(−2). Si |t−γ|≥L^(−2) la distancia ya es suficiente, y al saturar en1+1/L la separación horizontal es≥1/L. Esto justifica el techo deF sólo en el recorrido, no en el interior con polos.

La nueva curva queda a la derecha de la vertical vieja. Los residuos que quedan a su derecha cumplen β>σ₀+η/b+γ²/(2L), exactamente la desigualdad retenida; cuando la curva satura, ambos criterios excluyen todos los polos porque β<1. Al restar recorridos, el tramo |t|≤1 se cancela de manera idéntica, sin aproximar dos términos de tamañoT₀. Sólo permanecen alas, conectores y tapas, todos con ahorro exp(−cL/b). De ahí el techo agregado paraR−R_par, válido para residuos completos sin estimar cada uno. Las orientaciones del teorema de residuos dan R−R_par como diferencia de esas integrales, cuyo módulo se acota independientemente del signo.

**Alcance.** Todo cero fijo con β>1/2 acabaría entrando en la región retenida cuando L crece, pues α→1/2 y γ²/L→0. Así el ahorro no excluye un cero exterior; identifica qué agregado ya es despreciable frente al fondo negativo a cada escala.
