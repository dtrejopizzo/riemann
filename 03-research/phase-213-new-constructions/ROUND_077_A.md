# Regularidad de los minimizadores y módulo de potencia para el fondo completo

Para cualquier compacto J⊂(0,∞), cualquier 0<s<1/2 y todo minimizador completo normalizado F en I_T=[−T,T], T∈J, su extensión por cero cumple ||F||_{H^s(ℝ)}≤C(J,s). En particular, para cada 0<α<1,
    
    |λ_W(T')−λ_W(T)| ≤ C(J,α)|T'−T|^α,     T,T'∈J.

El lema contT del paper 47 obtiene un módulo logarítmico controlando el dominio de forma entero. Aquí basta controlar los minimizadores de los dos extremos y la ecuación fuera del intervalo aporta la regularidad adicional. Se trabaja con la forma completa, sin imponer los momentos primitivos.

**Ecuación a ambos lados del borde.** Sea P la multiplicación por 1_{I_T}, m(D) el multiplicador arquimediano de P47. Dentro del intervalo, el mínimo satisface m(D)F=λ_W F menos las contribuciones de las traslaciones primas y del operador polar acotado de rango finito, por la ecuación débil frente a tests compactos en el interior. Estas contribuciones, restringidas con P y extendidas por cero, son operadores uniformemente acotados en L² y en H^s para T∈J. En efecto las traslaciones son isometrías y hay una lista finita común; los perfiles polares son exponenciales suaves en un compacto común restringidas con P. Se usa el teorema clásico de multiplicadores de Sobolev: la indicatriz de una semirrecta actúa acotadamente en H^s(ℝ) para |s|<1/2 (equivalentemente la desigualdad de Hardy fraccionaria en la recta). Para intervalos se restan dos semirrectas, con cotas independientes de sus extremos. λ_W está acotada en J por contT y los mínimos existen por compacidad.

Fuera, el núcleo de Lévy de P47 da
     
    m(D)F(x)=−(1/2)∫_{I_T} K(|x−y|)F(y)dy,   K(u)=2e^(−u/2)/(1−e^(−2u)).

La identidad exterior se prueba frente a tests separados del intervalo usando la fórmula de Lévy; sólo interviene el término cruzado. Para la derecha trasladar al borde y reflejar la variable interior. Las dos distancias al borde son positivas y el núcleo pasa a ser K(v+w). Lo mismo vale en el otro extremo. Se demuestra que este operador de cruce prolongado por cero está acotado en H^s y L². Descomponer K(u)=e^(−u)/u+R(u). R y su primera derivada son acotadas hasta cero por Taylor y decrecen exponencialmente en infinito. El núcleo R(v+w) y su primera derivada en v son Hilbert–Schmidt en las semirrectas, por integración de u|R^{(i)}(u)|². La salida queda en H¹ de la semirrecta; reflejar para extenderla y aplicar la indicatriz da la cota en H^s.

Para el término singular multiplicar en cada lado por e^(−v) o e^(−w) (usar extensiones Lipschitz acotadas). El operador restante es el de Carleman. Para f apoyada en la semirrecta positiva su salida extendida por cero es
    
    ∫₀^∞ f(tv) dt/(1+t),    v∈ℝ.

La norma L² de la dilatación es t^(−1/2)||f||₂ y la seminorma homogénea H^s es t^(s−1/2)||f||_{Ḣ^s}. Ambos factores son integrables contra dt/(1+t) para 0≤s<1/2. Traslaciones, reflexiones y las restricciones iniciales no alteran la uniformidad.

Juntando interior y exterior se obtiene m(D)F=B_T F en la recta, con B_T acotado en ambos espacios, uniformemente en T∈J. Para definir B_T sobre entradas arbitrarias, proyectar primero por P; construir las dos salidas anteriores y sumar. No se ha supuesto de antemano regularidad Sobolev de F: la identidad se verifica inicialmente en L² en los tres abiertos. La diferencia distribucional está soportada en los dos extremos y pertenece a H^(−ε) para todo ε>0, pues m tiene crecimiento logarítmico. Ninguna combinación no nula de deltas y sus derivadas pertenece a H^(−ε) para ε<1/2. Esto elimina las posibles contribuciones de borde.

**Ganancia de regularidad.** Sea Q la proyección de Fourier sobre |ξ|>N y A el multiplicador Q/m, definido por cero en |ξ|≤N. Como m(ξ)→+∞ se elige N fijo en J tal que ||AB_T||<1/2 tanto en L² como en H^s. La ecuación es F=(1−Q)F+AB_T F. El primer término tiene norma H^s ≤(1+N²)^(s/2) y la serie de Neumann converge en ambos espacios al mismo F por unicidad en L². Esto prueba el enunciado de regularidad incluso a través de los contactos primos.

**Del minimizador al fondo.** Dilatar un minimizador unitario de T a T'=rT. En la prueba de contT el cambio de la parte arquimediana y el del término polar son O_J(|r−1|) para r próximo a 1. Para el peine, |e^{iu}−1|≤2|u|^(2s) da un error O_{J,s}(|r−1|^(2s)||F||²_{H^s}) en la lista común de traslaciones, incluidas las que entran en el borde. Por el principio variacional esto acota λ_W(T')−λ_W(T). Invertir T,T' con el otro minimizador da la estimación bilateral; los pares alejados se cubren por acotación de λ_W. Tomar s=α/2.

**Aplicación y frontera.** Si se dispone de λ_W(T₀)≥g>0 y una cota numérica C para este compacto y exponente, basta C|T−T₀|^α<g para transportar el signo estricto. No se ha calculado C ni una ventana adicional. El certificado de 026 a 1.035 trata el fondo primitivo. El índice ya registra reproducción externa completa en log(11)/2; una prolongación cualitativa por continuidad no es novedad. La aportación aquí es el módulo para el fondo, sin extenderlo al dominio de forma entero. Las constantes dependen de J y no hay de este argumento margen positivo uniforme al crecer T.

**Antecedente directo y atribución.** P121_DYADIC_RADICAL_BOOTSTRAP.md ya desarrolla la transmisión de Carleman y la inversión de altas frecuencias para obtener H^s, s<1/2, en ventanas finitas. 106_123_BOUNDED_PRIME_GENERATOR_AND_SECOND_LOG_BOOTSTRAP.md ya trata el segundo momento logarítmico. La parte de regularidad de esta nota adapta esas pruebas al mínimo de la forma completa, con el término polar, y hace uniformes las constantes al variar T en un compacto. El resultado a retener es su aplicación bilateral al módulo del fondo del paper 47; no se propone la regularidad de los modos ni el método de Carleman como mecanismos inéditos.
