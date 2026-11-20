# Radio del certificado y desplazamiento de una lista finita

Fijar T>0, distintas frecuencias reales γ_j con multiplicidades m_j>0 simétricas, y desplazamientos 0≤δ_j≤Δ=max δ_j, también simétricos. El dato local es
    g(u)=Σ_j m_j exp(iγ_j u)cosh(δ_j u).
Para Δ pequeño y L grande, el ínfimo de la masa negativa de los certificados con perfil w plano en [−2T,2T] y soporte [−L,L] satisface
    c(Z,T)(L^(−2)+Δ²) ≤ inf ν⁻(ℝ) ≤ C(T)(Σ_j m_j)(L^(−2)+Δ²),
con transformada de ν igual a wg. Para el inferior se fijan las multiplicidades y las frecuencias; las constantes son uniformes al variar todos los desplazamientos. También admite que se desdoblen multiplicidades en varios términos de masa entera en la misma frecuencia. El caso Δ=0 es 170. En particular el costo de un cuarteto aislado a distancia δ es comparable a L^(−2)+δ².

**Curvatura común.** Con a y P de 170, sea H(t)=|P(exp(it))|² en el eje real, continuado como polinomio trigonométrico entero mediante P(exp(it)) y su factor conjugado reflejado. En cada θ_j=aγ_j hay una raíz doble con H''(θ_j)>0, porque la raíz de P es simple. Para toda extensión firmada admisible, por sus momentos en la ventana,
    ∫H(aτ)dν(τ)=Σ_j m_j Re H(θ_j+i aδ_j)
                 =−(a²/2)Σ_j m_j δ_j² H''(θ_j)+O_Z(Σ_j m_j δ_j⁴).
El error es uniforme en la caja de desplazamientos pequeños; el dato simétrico elimina la parte impar. Como H≥0 en el eje real, esto implica ν⁻(ℝ)≥c_Z Σ m_jδ_j² y en particular ≥c Δ². El mismo signo de las curvaturas impide que varios desplazamientos se oculten unos a otros en esta prueba finita.

**Recuperación del costo del radio.** Sea g₀ el mismo dato sin desplazamientos y χ una función suave par de soporte fijo, igual a uno en la ventana. Corregir la transformada por χ(g₀−g) tiene norma L¹ en la variable espectral O_(Z,T)(Δ²), por Taylor y dos integraciones por partes en soporte fijo. Se obtiene una extensión de g₀, todavía de radio L. El inferior general de 170 da ν⁻≥c₁ L^(−2)−C₁Δ². Combinar con ν⁻≥c₂Δ² prueba el inferior conjunto incluso cuando las dos escalas son comparables.

**Superior válido para toda la lista.** Usar la autocorrelación b y el corte χ de 170. Sea h(u)=b(u/L)/cosh(Δu) y poner w=h+χ(1−h). Para cada |d|≤Δ el cociente cosh(du)/cosh(Δu) es positivo definido. Para Δ>0 y |d|<Δ, su transformada inversa es la parte real de una constante positiva por sech(π(τ+id)/(2Δ)), aplicando la transformada de sech a los factores exp(±du). Esa parte real es positiva por cos(πd/(2Δ))>0. En el borde el cociente es uno; para Δ=0 se aplica 170 directamente. Por productos y traslaciones hg tiene medida no negativa. En soporte fijo, χ(1−h) y sus dos primeras derivadas son O_T(L^(−2)+Δ²). Multiplicar antes de trasladar por cosh(δ_j u) conserva esta cota para Δ acotado. Por tanto la norma L¹ de toda la corrección es ≤C(T)Σ m_j (L^(−2)+Δ²), independientemente de la altura o separación de las frecuencias. Esto da el superior.

**Cotejo.** R7-01 ya estudió la curvatura negativa cuadrática de un cuarteto fuera de línea, y la ruta G7E ya contiene la herramienta de Poisson en una banda. Aquí se combinan con la tasa de finZ de 170 para el problema variacional de masa negativa, con un perfil común para desplazamientos distintos y constantes uniformes en el radio y los desplazamientos. Las frecuencias se fijan antes del límite. El inferior pierde control con la separación y el superior crece con la masa total; ninguno permite pasar sin más al espectro infinito del paper 47.
