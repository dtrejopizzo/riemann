# Un promedio positivo suprime todos los residuos en una ventana explícita

**Estado: PROVED, con revisión independiente de la normalización theta, la ventana y la conclusión a corte congelado.**

Congelar z=L², x=exp L, y poner S_z(u)=S^*(exp u;z). Sea Φ el núcleo theta bilateral de ξ, normalizado por ∫Φ(v)exp((s−1/2)v)dv=ξ(s). Entonces, incondicionalmente, con B=(log L)/2,

    ∫_{−B}^B Φ(v)exp(−v/2) S_z(L+v) dv ∼ −ξ(1/2) T₀(x).

En particular en cada intervalo [x/√log x,x√log x] hay una escala t con S^*(t;z)≤−c T₀(x)L^(−1/4), con c absoluto positivo. El corte en esa conclusión es el z del centro. 365 anulaba sistemas finitos de frecuencias con medidas discretas dependientes del sistema. Aquí el núcleo clásico es fijo, el integrando aritmético es el pulso de 368 y se cuantifican tanto la ventana como el piso. No se atribuye novedad a la representación theta de ξ.

**Núcleo y signo.** Para v≥0 usar Φ(v)=Σ_n (4π² n⁴ exp(9v/2)−6π n² exp(5v/2))exp(−πn² exp(2v)), n≥1; extender por paridad. Todos sus términos son positivos en v≥0. La inversión theta da la misma serie bilateral (para v<0 entendida sumando antes de integrar). La integral de Mellin término a término en Re s>1 se justifica en esa banda para las dos sumas separadas por la convergencia de ζ(Re s); el cambio r=πn²exp(2v) da ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2. El núcleo tiene cola O(exp(5|v|−πexp(2|v|))). La expresión para ξ se prolonga por analiticidad.

**Promedio completo.** En la inversión gaussiana inicial sobre 1+1/L se puede integrar en v por convergencia absoluta. El factor restante tras promediar es F(s)ξ(s)=s(s−1)π^(−s/2)Γ(s/2)/2, regular en toda la banda α≤Re s≤1+1/L y negativo en s=1/2. Ahora se traslada el contorno entero a α sin residuos. El factor gamma por Stirling tiene crecimiento a lo sumo polinómico en esa banda, y es regular cerca de la silla. La dominación local y la pérdida de fase de 367, junto con la cola gaussiana, dan el equivalente exp(K(α))ξ(1/2)/(ζ(1/2)√(2πK''(α)))=−ξ(1/2)T₀. Así se anulan también los residuos de orden superior, por cancelación exacta antes de desplazar el contorno.

**Ventana efectiva.** Uniformemente en z, |S_z(L+v)|≪x exp v por el conteo diádico en la gaussiana. Tras normalizar por exp(−v/2), el coste de |v|>B es ≤x exp(−πL+O(log L)), despreciable ante T₀. En [−B,B] la medida positiva Φ(v)dv tiene masa ≤ξ(1/2). Algún v satisface exp(−v/2)S_z(L+v)≤−(1−o(1))T₀ y exp(v/2)≥L^(−1/4), lo que da el piso. El promedio pierde sensibilidad a los ceros precisamente porque el multiplicador se anula en todos ellos. Recuperar el signo en el centro, o con corte móvil igual al de cada escala, sigue abierto.

**Registro de revisión.** Poner θ(t)=1+2Σ_{n≥1}exp(−πn²t). La serie del núcleo es2t^(9/4)θ''(t)+3t^(5/4)θ'(t), t=exp(2v); derivar θ(t)=t^(−1/2)θ(1/t) muestra que esta expresión es invariante bajo t↦1/t, justificando la extensión par y la misma serie en v negativo. Con r=πn²exp(2v), su Mellin bilateral para Re s>1 resulta exactamente π^(−s/2)ζ(s)[2Γ(s/2+2)−3Γ(s/2+1)]=ξ(s). No falta un factor2: la integral positiva sobre v≥0 sería la mitad de la bilateral al usar cosh. En particular ∫Φ=ξ(1/2)>0.

El multiplicador restante Fξ es regular en toda la franja desplazada y negativo en la silla; su factor gamma no introduce polos allí. La cancelación de los ceros se realiza analíticamente antes de mover el contorno, incluidos los órdenes múltiples. En la cola |v|>B, exp(2B)=L y el coste absoluto es x exp(−πL+O(log L)), usando el techo uniformeCe^(L+v); no se usa un techo de raíz paraS. Finalmente dividir el promedio negativo por la masa positiva de la ventana y usar exp(v/2)≥L^(−1/4) da la afirmación puntual con el mismoz congelado, sin sustituirlo por(log t)².
