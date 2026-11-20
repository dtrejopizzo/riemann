# Retirar las potencias primas pequeñas con sus dos sumas interiores completas

Fijar d=1/4, W de 159 y P(s)=s(s−1)(s−1+d)(s−1/2). Definir w_* aplicando P(−t d/dt) al perfil w de 159. Tiene soporte compacto en [exp(−A),exp(A)] y puede cambiar de signo. Para y>0 poner
    K(y)=Σ_{m,n≥1} m^(−d) w_*(mn²/y).
La condición Σ_q Λ(q)K(x/q)≤O(√x) eventualmente equivale al signo. En esa condición se pueden borrar todos los q≤x/(K₀(log x)^6), con error total absoluto o(1) para K₀ suficientemente grande. El descarte incluye los principales y la constante de las dos sumas, sin estimación de cancelación en Λ.

**Descarte.** Por Mellin, K es la inversa de B(s)=P(s)W(s)ζ(s+d)ζ(2s). B es entera: los únicos polos posibles están en 0, 1−d y 1/2. En Re s=−L con L=N+1/4, N≥2, y s=−L+it,
    |P(s)W(s)| ≤ exp(C L−c√|t|)(1+L+|t|)^3.
En efecto cada factor del producto de uniformes antes del divisor s cuesta ≤exp(L/j²)min(1,j²/|s|) por la fórmula con sinh y la representación integral. Cada j≤√|t|/2 da un ahorro ≥4 en el denominador del mayorante. En la misma recta las ecuaciones funcionales dan
    |ζ(s+d)ζ(2s)| ≤ C^(L+1)(1+L+|t|)^(3L+C).
Para verlo, en cada ecuación usar Stirling en el semiplano derecho para Γ(1−z) y |sin(πz/2)|≤exp(π|Im z|/2). La diferencia entre estos exponentes angulares cuesta O(1+|Re z|), por v arctan(u/v)≤u; el factor ζ(1−z) está absolutamente acotado. Desplazar el contorno para L fijo (el decaimiento en t vence toda potencia). La integral en módulo es ≤y^(−L) C^(L+1)(1+L)^(6L+C'): separar |t|≤L y el resto, y usar el momento gamma de exp(−c√|t|). Escoger L de orden ε y^(1/6) con ε pequeño da |K(y)|≤C exp(−c' y^(1/6)) para y≥1. La cota de Chebyshev Σ_{q≤x}Λ(q)=O(x) demuestra el descarte. En el extremo opuesto K(y)=0 para y<exp(−A), de modo que la suma restante es finita.

**Detección.** La transformada de la suma original es B(s)(−ζ'/ζ)(s). P(1)=0 elimina el polo principal de la derivada logarítmica; los otros polos reales ya se retiraron de B. Bajo RH se puede desplazar hasta Re s=1/4, sumando residuos críticos de tamaño total O(√x) por el decaimiento vertical y el conteo de ceros. Si hay ceros a la derecha, elegir el más a la derecha a una misma altura. Allí ζ(s+d), ζ(2s), W(s) y P(s) son distintos de cero, así que queda un polo simple. Landau como en 155 excluye tal polo si se demuestra el techo unilateral. El argumento opera sobre el peso filtrado directamente, sin derivar una desigualdad.

**Cotejo.** 047 ya localizaba criterios usando promedios Gevrey y Landau. Aquí se estima la fibra doble específica mn² de 155; la diferencia con 159 es que en el tramo retirado ya no queda un término principal ponderado por Λ. Lo que subsiste es otra desigualdad centrada sobre potencias primas en una banda multiplicativa. Seguir estrechando esa banda sin controlar su signo repetiría la estrategia de localización del corpus. No se obtiene una nueva ventana.
