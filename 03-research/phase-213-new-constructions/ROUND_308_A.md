# Cruces efectivos más allá de la cuarta potencia por un factor doblemente logarítmico

Para casi todo t∈[1,2] existe C_t>0 y una sucesión x→∞ con cortes

    √x ≤ y ≤ x/[C_t (log x)^4 (log log x)^2],
    |R_t(x,y)| ≪_t √x.

Es una afirmación de existencia **sin RH** en una sucesión de escalas. No se afirma para la fila excepcional t=0. Prueba que la franja de oscilación de 307 llega más allá de la cuarta potencia pura, aunque permanece por debajo de cualquier potencia fija 4+ε en el extremo superior de y aquí prescrito.

**Corte de comparación.** Parametrizar x por z→∞ mediante L=log x=z^(1/4)/(d(log z)^a), d>0 fijo, 0<a≤1/2. Es creciente eventualmente y z∼4^(4a)d⁴ L⁴(log L)^(4a). En el corte de comparación x/z poner F=−LR_t(x,x/z)/(2x). El desarrollo de 306 hasta tres términos da

    F=H₀+d z^(−1/4)(log z)^a H₁+d² z^(−1/2)(log z)^(2a) H₂
        + O(z^(−3/4)(1+log z)^C).

H₂(z)=D_t''(1)+O_N((log z)^(−N)) para todo N: usar la cota de 294 para las colas de los momentos hasta grado dos y para B_t(z)P₂(log z)/z. Los momentos de grados cero y uno se anulan. El Mellin del término H₂ menos su constante, incluido su peso, está absolutamente acotado hasta la frontera Re s=−1/2. La parte constante aporta d²D_t''(1)Γ(1+2a)(s+1/2)^(−1−2a), salvo modificación entera por el extremo inferior.

**El término de primer orden.** Sea M el Mellin de H₁ dado en 306. El peso adicional (log z)^a tiene Mellin aplicado a H₁ igual a

    [a/Γ(1−a)] ∫₀^∞ [M(s)−M(s+u)] du/u^(1+a).

La identidad se obtiene integrando 1−exp(−u log z), inicialmente en convergencia absoluta. La integral da continuación holomorfa cerca de cada punto cuyo rayo horizontal a la derecha esté libre de singularidades de M, dentro de su dominio meromorfo. En u pequeño la diferencia es O(u) localmente uniforme; para u grande M(s+u) está uniformemente acotada por la representación convergente. La traslación z^(−1/4) evalúa esta expresión en s+1/4. Sobre el rayo real desde −1/4 no hay singularidad, incluido el origen por el cero doble de D_t en 1.

**Oscilación.** Tomar el cero crítico y la frecuencia genérica de 307. Si D_t tiene polos estrictamente a la derecha de ρ a su misma altura, elegir el de mayor parte real; de lo contrario usar ρ. En el punto desplazado por −1, el término H₀ conserva el polo y el rayo de H₁ queda libre por la elección anterior. Para el punto interior basta Landau como en 307. Para el punto de frontera, el término H₂ es acotado al aproximarse a esa altura no real desde la derecha, por la separación de su constante. Sobre el eje real el Mellin completo en −1/2+h crece a lo sumo como d²D_t''(1)Γ(1+2a)h^(−1−2a)+O(1). El polo complejo tiene orden 2r≥2 y coeficiente principal A≠0 independiente de d. Al comparar el Mellin de una supuesta mayorante o minorante eventual c z^(−1/2)log z exactamente como en 307, se obtienen ambas oscilaciones de magnitud ≫z^(−1/2)log z. Esto vale para todo d fijo si a<1/2; en a=1/2 elegir d suficientemente pequeño para que d²D_t''(1)<|A|/2, y después c<|A|/2. En el caso de polo interior cualquier d sirve. La regularidad en la recta real abierta hasta la frontera, necesaria para Landau, sigue de los mismos tres términos.

**Del signo a un corte equilibrado.** En a=1/2 se obtienen x arbitrariamente grandes donde el bloque en x/z es positivo; en √x es negativo por 294. Entre los dos extremos, un salto tiene módulo 2u_p |B_t(x/p)|≪√x por la cota incondicional de 294, pues x/p≤√x. El primer cruce proporciona el corte del enunciado; tomar, por ejemplo, C_t=8d⁴ en la equivalencia asintótica para z. La detección por 306 exige superar una potencia fija 4+ε; el factor ganado aquí no alcanza esa escala. La nueva conclusión usa oscilación de frontera y no estima el bloque complementario.
