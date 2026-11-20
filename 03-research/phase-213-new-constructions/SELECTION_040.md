# Minoración divisorial del peso de 039

Escribir w(t)=min(t,t⁻²). Entonces Q(x)=x⁻¹ᐟ²ΣΛ(n)w(n/x). La operación propuesta es minorar w por Df(t)=Σ_{m≥1}f(mt). Con convergencia absoluta la identidad Σ_{d|k}Λ(d)=log k cambia el emparejamiento con Df en una sola suma contra log k. Cotejo: N_BUILD022_MATRIX_IDENTITY_FOR_X_M, 212-58/76 y G1_B9_R2 §5 ya usan la transformación divisorial. Aquí se comprueba la posibilidad de que un minorante fijo pague el término principal completo de 039.

**Un perfil no negativo no sirve.** Si f≥0 y Df(t)≤w(t) en todo t>0, para y>0 y todo entero k se tiene f(y)≤Df(y/k)≤y/k. Por tanto f es idénticamente cero. Basta incluso exigir el minorante en las muestras n/x con n=2 y x=j⁴ para excluir todo f continuo no negativo fijo: elegir m_j el entero más próximo a yj⁴/2. Se tiene f(2m_j/j⁴)≤Df(2/j⁴)≤2/j⁴ y pasar al límite da f(y)=0. Así no es necesario presuponer la comparación entre las muestras de interés para este descarte.

**Perfil firmado compacto.** Supóngase f continuo real soportado en [α,b]⊂(0,∞), de integral cero y Df≤w en toda la semirrecta. Integrando desde ε>0,
    
    ∫_ε^∞ Df(t)dt = ∫ f(u) H_floor(u/ε) du → ∫ log(u) f(u)du,

donde H_n es la suma armónica. El límite sigue del desarrollo H_n=log n+γ_E+O(1/n) uniforme en el soporte tras sustraer la constante usando ∫f=0. La parte positiva de Df es integrable por el minorante, luego también la negativa por el límite finito. Como Df=0 más allá de b, el déficit integral es al menos ∫_b^∞w>0. En particular ninguna elección fija de este tipo alcanza la masa 3/2.

El déficit también se ve directamente en los verdaderos pesos primos, sin suponer un teorema de cuadratura para Df cerca de cero. Fijar B>max(b,1). Sólo los contactos con Bx<n≤2Bx aportan al coste de la minoración al menos

    x^(−1/2) Σ_{Bx<n≤2Bx} Λ(n) w(n/x) ≥ [ψ(2Bx)−ψ(Bx)]/(4B²√x) ∼ √x/(4B).

El coste total puede ser mayor. Esta pérdida de orden √x impide obtener la precisión aditiva O(1) de Q a partir del minorante solo. Dejar crecer el soporte con x o evaluar aparte el resto cambia esa conclusión.

**Inverso exacto.** Para t>0, f(t)=Σ_{m≥1}μ(m)w(mt) satisface Df=w por inversión de Möbius. Las sumas dobles convergen absolutamente para t fijo: salvo finitos productos la mayorante es t⁻²Σ_{m,k}(mk)⁻². Para t≥1 el inverso vale t⁻²/ζ(2); para t=1/2 vale 4/ζ(2)−7/2<0. El traslado exacto reintroduce pesos de Möbius firmados. El índice ya recoge esa familia de inversiones; no se abre una ruta de signo a partir del cambio de coeficientes.

**Decisión.** Descartado el minorante fijo no negativo (incluso si se exige sólo en las muestras originales), y el minorante firmado de soporte fijo que pretenda suministrar la cota sin estimar el resto. No se deduce un impedimento para otras identidades de divisores. La desigualdad uniforme de 039 permanece abierta.
