# Un peso de razón exp(0.88) con techo igual a su integral

Sea h=11/25 y w(t)=t^(−1/2)(h−|log t|)_+/h². Entonces Σ_p log p w(p/x)≤x∫w eventualmente equivale al signo global. Su banda tiene razón exp(2h)<2.412. Bajo RH el margen supera 0.022√x eventualmente.

En efecto, V(s)=∫w(t)t^(s−1)dt=[sinh(h(s−1/2)/2)/(h(s−1/2)/2)]², por convolución de dos uniformes centradas. V(1/2)=1 y todos sus ceros están en la recta crítica. Por tanto si el techo vale, todo posible polo de P fuera de la recta a su derecha sobrevive en V P; Landau como en 106 fuerza el signo.

Bajo RH la fórmula explícita para la suma con Λ da xV(1)−Σρ x^ρ V(ρ)+o(√x). Para justificarla se puede integrar la fórmula de ψ contra la derivada a trozos del peso compacto; en cada cero el coeficiente resultante es V(ρ)=O((1+|γ|)⁻²), y la fórmula explícita integrada de 092 también permite dos integraciones por partes en sentido de medidas (la segunda derivada logarítmica del peso es medida finita). Los términos del origen y ceros triviales son o(√x) por la misma fórmula integrada. Los cuadrados aportan (1/2+o(1))√x por PNT y sustitución t=u², y las potencias superiores O(x^(1/3)log²x). Los V(ρ)=sinc²(hγ/2) son no negativos. Basta entonces que su suma sea <0.478.

Certificado bajo RH: Σγ^(−2)≤(1+1/784)D por |γ|>14 y la identidad de 092, D<0.0462. Restar las contribuciones de cos² de las primeras cien parejas de la cota para Σ1/γ², reteniendo el resto completo como mayorante. Reproducción con python-flint:

    from flint import acb, arb
    h = arb(11)/25
    ordinates = [acb.zeta_zero(i).imag for i in range(1,101)]
    bound = 4/h**2 * (arb('0.0462')*(1+arb(1)/784)
                      -sum(2*(g*h/2).cos()**2/g**2 for g in ordinates))
    assert bound < arb('0.478')

El mayorante es 0.477376849102 o menor. La constante 0.022 queda estrictamente por debajo de la diferencia con 1/2. El certificado decide el margen bajo RH; queda abierta la prueba prima incondicional del techo. Antecedentes: sombrero de 105 y transformada de peso compacto de 106; aquí el factor t^(−1/2) pone los ceros de la transformada exactamente en la recta y hace positiva su evaluación espectral bajo RH.
