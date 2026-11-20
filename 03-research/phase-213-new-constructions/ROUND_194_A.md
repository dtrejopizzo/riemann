# De la ventana estricta a bloques de potencias de orden creciente y tasas desiguales

Poner T₀=553/200 y δ₀=exp(−85000000001), de 193. Considerar una sucesión de listas finitas de tasas v_j>0, con repeticiones permitidas; sean u=min v_j, V=max v_j y n su longitud. Si

    u→∞,    log V=o(u),    limsup Σ_j 1/v_j < T₀,

entonces en TODO el espacio causal de transformadas P(s)/∏(s+v_j), grado P<n, se tiene W(f)≥(δ₀−o(1))||f||₂² uniformemente en los numeradores, también complejos. Por ejemplo, para n polos iguales u≥cn con c>1/T₀ y n→∞ el bloque entero tiene signo estricto eventualmente. Para n polos cualesquiera en [cn,Kn] con K fijo y c>1/T₀ vale lo mismo. Es un enunciado asintótico; no se extrae un primer n práctico de δ₀.

**Control ponderado.** Usar la base ortonormal racional de POWER_THREE_002,

    F_j(s)=sqrt(2v_j)/(s+v_j) B_{j−1}(s),
    B_i(s)=∏_{l≤i}(s−v_l)/(s+v_l).

La triangularidad de denominadores y la ortogonalidad de Hardy por los factores de módulo uno dan todo el espacio, también con multiplicidades. Fijar S entre el limsup de la suma y T₀. Eventualmente n≤SV. En Re s=−λu, 0<λ<1 fijo, cualquier producto parcial B tiene módulo ≤M=exp(2λu S/(1−λ²)), pues log((1+x)/(1−x))≤2x/(1−λ²) para x=λu/v_j≤λ. Plancherel en la vertical da ||exp(λuy) f||₂≤poly(n,V) M para f unitario. En efecto la norma de (s+v_l)⁻¹ en dτ/(2π) es [2(v_l−λu)]⁻¹/².

La derivada en la semirrecta tiene la misma cota: sF_j(s)−sqrt(2v_j)=sqrt(2v_j)[−v_j B_{j−1}/(s+v_j)+(B_{j−1}−1)]. Telescopar el último término con B_l−B_{l−1}=−2v_l B_{l−1}/(s+v_l). Cada sumando admite la estimación anterior; Cauchy–Schwarz sobre los coeficientes unitarios introduce a lo sumo otro factor sqrt(n). Para λ=0 el argumento da normas H¹ sin peso a lo sumo polinomiales. Todos los factores polinomiales son exp(o(u)) bajo las hipótesis.

**Recorte en norma de la forma.** Elegir 2S<L<L'<2T₀ y luego λ pequeño de modo que 2S/(1−λ²)<L. Con η=1 fijo, en y≥L las normas L² de f y f' con peso exp(ηy) cuestan a lo sumo exp(−(λu−η)L) M exp(o(u))≤exp(−c'u) con c'>0 para tasas suficientemente grandes. Sea χ un corte suave igual a uno hasta L y cero desde L'. Por lo anterior, ||(1−χ)f||_{H_η}≤O(exp(−c'u)), reduciendo c' si hace falta. En y≤L' el peso es acotado y la norma sin peso es exp(o(u)), luego ||f||_{H_η}+||χf||_{H_η}≤exp(o(u)). La continuidad bilineal de la forma completa en POWER_CONFLUENT_BRIDGE_014 §3 implica |W(f)−W(χf)|=o(1) uniformemente. Tras trasladar el soporte [0,L'] a la ventana centrada, 193 da W(χf)≥δ₀||χf||₂². La forma es invariante por traslación, también el producto de los momentos polares. La extensión por cero del recorte con traza inicial arbitraria pertenece al dominio de forma por 014. Su norma L² tiende a uno, dando el enunciado.

**Qué aporta al puente.** 014 §§6–8 ya estableció la densidad fuerte para tasas confluentes móviles cuando n/u crece sin cota y la obstrucción de cortes aritméticos por debajo de 2n/u. POWER_THREE_002 ya obtiene margen fijo para tasas mínimas exponenciales en n. Aquí 193 se usa en sentido inverso, para demostrar signo de bloques completos desiguales con presupuesto de recíprocos y tasas incluso lineales en n. El margen es el pequeño margen de ventana. A tasa confluente, el régimen denso n/u→∞ queda fuera de la hipótesis. La positividad en esta colección no se extiende por el puente 014 a todas las ventanas.

**Comparación con 213-085 y auditoría.** 213-085 ya demuestra positividad para todo número de polos con Σ1/v≤1/512, margen 1/4 e incluso para recortes arbitrarios. Su reflexión de Hardy proporciona directamente ||e^(σy)f||₂≤∏(v_j+σ)/(v_j−σ)||f||₂, también para f' porque sF−f(0) pertenece al mismo espacio. Así se recupera la estimación ponderada anterior usando sólo la cota de derivada sin peso. La mejora de 194 es el presupuesto asintótico hasta cualquier S<2.765 para el dato entero bajo las condiciones de escala indicadas. La revisión independiente comprobó el caso desigual y esta comparación.

**Corrección de procedencia.** El cotejo posterior de 195 identifica 213-086 y 213-087 como antecedentes más fuertes: el piso de 194 se sigue de 087 pasando al límite en la longitud de recorte y aplicando la ventana 193. Es una aplicación del resultado previo.
