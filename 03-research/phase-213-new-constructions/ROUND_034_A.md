# Condición de borde de un extremizador negativo

En la normalización de 033, si Γ>0 existe un extremizador u de I(u)=1, y **todo** extremizador satisface

    liminf_{r↑1} (1−r)⁻¹∫ᵣ¹ x|u′(x)|² dx ≥ 1.

La constante es independiente del tamaño del defecto. Es un resultado condicional sobre el perfil óptimo. Antecedentes: monotonía variacional en BUILD083 y argumentos de borde de 212-36; P47 menciona cotas viriales. Aquí se usa la ley exacta de escalado en la norma degenerada de 033.

**Compacidad.** Representar B∞ por un operador autoadjunto A en el espacio de energía X₀ de 033. Para L fijo la demostración de Galerkin de 033 acota uniformemente en la bola la diferencia cuadrática entre B_L y su compresión finita en 6c_L/M. Para operadores autoadjuntos esa cota controla la norma del operador diferencia. Luego cada B_L representa un operador compacto. La estimación de diferencias de cortes de 032, transferida a X₀ en 033, da convergencia en norma hacia A. Si Γ>0, −Γ es un autovalor mínimo y lo alcanza un vector unitario.

**Compresión exacta.** Sea Y_r la imagen de la isometría de energía u(x)↦u(x/r) extendida por cero para x>r. El momento cero se conserva. Bajo U se obtiene una traslación por log r con amplitud √r; por ello B_L y luego B∞ se multiplican por r. El ínfimo del cociente de Rayleigh en Y_r es −rΓ. Estos subespacios cerrados crecen y su unión es densa por los aproximantes suaves compactos de media cero de 033.

**Coste de la capa exterior.** Para un extremizador normalizado, sea P la proyección de energía sobre Y_r. Poner m_r=∫₀ʳu−ru(r)=∫ᵣ¹xu′, por el momento cero y la traza en 1. Sobre (0,r) se tiene Pu=u−u(r)−2m_r(r−x)/r² y fuera vale cero. En efecto tiene media y traza en r nulas; el residuo es ortogonal a Y_r por integración por partes. La pertenencia del candidato a Y_r se obtiene por reescalado y la caracterización por energía finita y traza nula en r (en la variable logarítmica, truncar primero la derivada en la cola, continuar por constante y cortar esa constante sobre un intervalo de longitud creciente). Escribiendo d²=I(u−Pu) y E_r=∫ᵣ¹x|u′|², resulta

    d²=E_r+2|m_r|²/r²,       E_r≤d²≤E_r/r².

La última cota usa Cauchy–Schwarz contra x dx. Se tiene d>0 por la comparación de mínimos y d→0 por densidad. El residuo unitario e=(u−Pu)/d converge débilmente a cero por ortogonalidad a los subespacios crecientes. Por compacidad B∞(e)=o(1). Escribiendo R para el cociente de Rayleigh, la ecuación Au=−Γu da, cuando Pu≠0,

    (1−r)Γ ≤ R(Pu)+Γ = d²(Γ+B∞(e))/(1−d²).

Se deduce el liminf anunciado. Una contradicción exigiría otra propiedad del operador aritmético que impidiera tal energía en el borde. La suavidad por sí sola admite pendiente no nula en 1. PROVED (implicación condicional), auditoría matemática independiente.

## Ley exacta de borde y simplicidad del mínimo

Suponer Γ>0. Entonces el menor autovalor de la forma completa en la norma de 033 es simple. El extremizador real unitario se puede orientar de modo que u(x)/(1−x)→1 cuando x↑1. La afirmación se refiere al problema normalizado en X₀.

**Diferencia de dilataciones.** Escribir S_r para la isometría anterior y w=S_ru−u. Por la ecuación propia, la forma B∞+ΓI anula los cruces con u. Evaluándola sobre S_ru se obtiene exactamente

    B∞(w)+ΓI(w)=Γ(1−r).

En particular I(w)≥Γ(1−r)/(||A||+Γ). El vector w/√I(w) converge débilmente a cero: contra cada test suave compacto φ de media cero, el producto de energía con w es la integral de y u′(y) contra el conjugado de rφ′(ry)−φ′(y), de orden Oφ(1−r) por Cauchy–Schwarz. Pasar por densidad. La compacidad de A da B∞(w)=o(I(w)); por tanto I(w)/(1−r)→1. En (r,1) la contribución a I(w) vale E_r. La cota inferior de la sección previa obliga a E_r/(1−r)→1 y la contribución del intervalo (0,r) es o(1−r).

**La pendiente media determina el autoespacio.** Sea h=−log r y g(t) la derivada de u(exp(−t)) respecto de t. Se tiene h⁻¹∫₀ʰ|g|²→1. La contribución interior anterior equivale a D(h)=∫₀^∞|g(t+h)−g(t)|²dt=o(h). La varianza de g con medida dt/h en [0,h] es

    (2h²)⁻¹ ∫₀ʰ∫₀ʰ |g(s)−g(t)|² ds dt ≤ h⁻²∫₀ʰ D(s)ds = o(1).

Luego |ℓ_h(u)|²→I(u) para todo vector del autoespacio por homogeneidad, con ℓ_h(u)=u(exp(−h))/h. Para dos vectores ortonormales, polarizar exigiría ℓ_h(u)conj(ℓ_h(v))→0, aunque ambos módulos tienden a uno. Esto prueba simplicidad. La forma es real por la simetría del símbolo, luego se puede elegir un extremizador real. Su cociente ℓ_h es continuo para h>0 y su módulo tiende a uno; el signo es constante cerca de cero. Elegir orientación y usar h/(1−exp(−h))→1 prueba la ley de pendiente. No exige continuidad de u′ hasta el borde.

El resultado usa la estructura de compresión y compacidad; por sí solo admite un mínimo negativo simple. PROVED (implicación condicional), auditoría independiente.

Control del alcance: la forma modelo −||u||₂² en X₀ es compacta en I por 033, satisface el mismo escalado y tiene defecto estrictamente positivo. La ley de pendiente y la simplicidad también valen para ella. Por tanto un argumento de signo necesita una propiedad adicional específica de la forma aritmética. El fondo arquimediano simple de P47 corresponde a otro operador.

## Qué detectan los contactos aritméticos en un posible extremizador

Para n≥2 sea C_n el operador en X₀ que representa la forma (2/n) Re ∫conj(u(y))u(y/n)dy. Es acotado por la inclusión en L² y Cauchy–Schwarz. Para enteros distintos n y coeficientes reales a_n de soporte finito, toda combinación C=Σa_n C_n con algún a_n≠0 es inyectiva. Esto vale sin hipótesis sobre Γ. La inyectividad concierne a la acción del operador; un solo valor cuadrático puede valer cero.

En efecto, su símbolo logarítmico es q(t)=2Σa_n cos(t log n)/√n. Si Cu=0, probar la forma polarizada contra S_ru para todo 0<r≤1. Salvo un factor √r, se obtiene la transformada de Fourier de la función real integrable q(t)|widehat(Uu)(t)|² en un semieje. Por simetría hermitiana se anula en el otro, e inyectividad de Fourier implica q|widehat(Uu)|²=0 casi por doquier. Las frecuencias distintas hacen de q una función analítica no idénticamente nula (independencia de las exponenciales). Sus ceros son discretos, luego u=0.

**Consecuencia para el signo al variar pesos.** Si Γ>0, tomar el mínimo simple aislado λ=−Γ y un extremizador unitario u. Perturbar la forma como A+εC. El signo elegido para C sólo fija la orientación de ε. En cualquier dirección no nula en que λ′(0)=〈u,Cu〉 sea cero, se tiene estrictamente

    λ″(0)=−2〈Cu,(A−λ)⁻¹ en u⊥ aplicado a Cu〉 < 0.

En efecto el mínimo aislado simple admite una rama diferenciable dos veces para perturbaciones acotadas. Derivando la ecuación propia con derivada del vector en u⊥ se obtiene u′=−(A−λ)⁻¹Cu en ese subespacio cuando λ′=0. Diferenciar λ′ da la fórmula. El inverso reducido es positivo y Cu≠0. Por tanto en toda familia finita de pesos la Hessiana es negativa definida sobre el núcleo de la primera variación. No se necesita que ese núcleo tenga codimensión exactamente uno.

P47 rem:resweights y lem:degen ya estudian sensibilidad de pesos; aquí se excluyen direcciones planas hasta segundo orden en el portador de 033. Sólo la inyectividad es incondicional. El cálculo de curvatura presupone ya un mínimo negativo y no decide el signo para los pesos de von Mangoldt fijos. PROVED tras auditoría independiente.
