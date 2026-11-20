# Las dos lecturas tienen signo y término principal en un intervalo de pendientes

Para J,F,δ de 245 y cada pendiente fija 9/500≤c<1/4 se cumple, en TODO inicio t→∞,

    F(0) ∼ F(δ) ∼ H(1/2) δ exp(t/2)/4 > 0.

Se usa la verificación de ceros hasta G=3·10¹² (Z2 del corpus). Bajo RH la misma ley vale para cada 0<c<1/4. En particular RH equivale también a que para cada racional 0<c<9/500 la PRIMERA lectura sea eventualmente no negativa en todos los inicios. Aquí el cuantificador en los inicios es más fuerte que en la condición de dos lecturas de 245.

**Separación de cuadrados.** Para u≥0 escribir S como suma de von Mangoldt suavizada menos cuadrados de primos y potencias de orden ≥3. Estas últimas cuestan O((1+u)^C exp(u/3)) por conteo elemental (hay O(1+u) exponentes). Para calcular los cuadrados aplicar la misma fórmula explícita suavizada a la mitad del argumento u y al peso W(2v), con transformada H(s/2)/2. Al reemplazar primos por von Mangoldt en ese cálculo el error cuesta O((1+u)^C exp(u/4)). Con el resto arquimediano de la fórmula compacta de 239 resulta

    S(u)=H(1)exp(u)−Σ H(ρ)exp(ρu)−H(1/2)exp(u/2)/2
         + (1/2)Σ H(ρ/2)exp(ρu/2)+O((1+u)^C exp(u/3)).

Las sumas incluyen multiplicidades y admiten momentos absolutos de todo orden. Para u<0 definir el resto por diferencia; es acotado como en 245. No se usa RH para esta expansión.

**Brecha.** Tras el promedio, la tasa de exp(su) es Re s−c log(|1+s|/(3/2)). Para s=ρ/2 es ≤1/2−c log(7/(3/2)) por |Imρ|>14. Para s=ρ en la franja verificada es ≤1/2−c log(14/(3/2)). Para los restantes ceros es ≤1−c log(2·10¹²)<1/2 si c≥9/500, dado que log(2·10¹²)>28. El resto de u≥0, integrado como en 245, tiene tasa a lo sumo 1/3+c log(9/8)<1/2, aparte de factores polinómicos. El resto de u<0 cuesta a lo sumo (3/2)^n. Así existe η>0 que deja todo ese error en O(exp((1/2−η)t)); el redondeo de n sólo cuesta un factor polinómico en |s| dentro de las sumas. Bajo RH todos los ceros están sujetos a la cota de la franja verificada, a cualquier altura.

**Signo.** El principal en exp(u) se cancela y la normalización del promedio conserva exactamente exp(u/2). Para v=0,δ queda

    F(v)=H(1/2)exp((t+v)/2)(exp(δ)−exp(δ/2))/2 + O(exp((1/2−η)t)).

El primer término es positivo y su equivalente domina el error porque log(1/δ)=o(t). Si RH falla, 245 selecciona una pendiente racional arbitrariamente pequeña evitando empates (empezar con cualquier intervalo suficientemente próximo a cero y de extremo izquierdo positivo). En ella el par dominante da lecturas F(0) de ambos signos en cada tramo de n fijo suficientemente grande. Esto prueba la recíproca de signo eventual.

**Alcance.** Se prueba incondicionalmente la estimación aritmética pendiente de 245 en parte de su rango, con signo, constante y todos los inicios. 9/500 es una cota suficiente redondeada, no un umbral óptimo. La entrada de verificación finita sólo protege pendientes separadas de cero. El argumento del sesgo por cuadrados ya aparece en 237 para otro peso; aquí se aísla como término principal después del promedio gamma y de las diferencias.
