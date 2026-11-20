# Muestreo uniforme de la paridad impar de 088

Para cualquier paso h>0, fijar a≥1/2, 0<b<1/2 y γ=mπ/h>a+b con m natural. Considerar el modelo de la fórmula espectral finita con z=±b±iγ (cuatro elecciones), sin atribuir esos puntos a ζ. Cumple las simetrías y la sumabilidad usadas en el cálculo de 088. En T=nh el par con parte real positiva contribuye a J(T) exactamente

    2 exp(2bT) ((a+b)²−γ²)/((a+b)²+γ²)².

El otro par cuesta O(exp(−2bT)). La diagonal normalizada converge a una constante por b<a. Por tanto la energía impar normalizada 2D_T−2C_T tiende a +∞ sobre la rejilla. En T=nh+π/(2γ) cambia el signo de las dos fases y la misma energía tiende a −∞. Añadir cualquier familia sobre el eje crítico con suma de (1+γ²)⁻¹ finita altera J y las diagonales normalizadas en O(1) (para ordenadas acotadas lejos de cero). Así incluir los ceros críticos ya verificados no repara la inferencia formal.

**Decisión.** Descartar la inferencia de positividad continua a partir de la paridad impar observada en una rejilla fija usando sólo simetrías y sumabilidad. 088 usa un polo fuera del eje real en la transformada continua; en las muestras su fase es uno. Este modelo no proporciona ceros de ζ ni refuta una desigualdad aritmética en las ventanas nh. El fallo de Nyquist de fase 186 (R186_117) corresponde al símbolo de ventana, mientras aquí se muestrea la ventana misma.

**Afinación auditada.** En realidad la contribución impar del cuarteto es estrictamente positiva en TODOS los nh con n≥1. Poner A=a+b, B=a−b, U=sinh(AT)/(A²+γ²), V=sinh(BT)/(B²+γ²). En la rejilla la transformada bilateral de sinh(at) en z=b+iγ es, salvo signo, AU−BV−iγ(U+V), por integración directa. Por imparidad y conjugación la suma del cuarteto en Weil es −4 veces la parte real del cuadrado de esa transformada. Es positiva porque |AU−BV|<γ(U+V). La afirmación se refiere a la paridad impar individual.
