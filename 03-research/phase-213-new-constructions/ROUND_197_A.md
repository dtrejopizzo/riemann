# Cancelación exacta en la tasa crítica de la cola y una ventana común para toda tasa

Sea el espacio de 196: dato arbitrario en [0,L] seguido por una cola z exp(−v(y−L)) con v>1/2. Existe L₀>0 común a TODAS las tasas y un margen positivo común en norma L² para 0<L≤L₀. En el extremo v↓1/2 los coeficientes completos de esta forma tienen límite finito. La afirmación de signo para v=1/2 se refiere sólo a ese límite regularizado; los momentos originales divergen por separado.

**Cruce a distancia x=L−y.** Para la cola sin normalizar y casi todo x en (0,L) el funcional de cruce es integración contra

    k_v(x)=−(1/2)∫₀^∞ K(x+r)exp(−vr)dr
            +exp(x/2)/(v−1/2)+exp(−x/2)/(v+1/2)
            +exp(vx)[ζ'/ζ(v+1/2)+Σ_{n<exp x} Λ(n)n^(−v−1/2)].

El núcleo K de 077 da el cruce arquimediano; los dos momentos se integran directamente. Un contacto primo atraviesa el corte exactamente para log n≥x y en el otro extremo evalúa exp(−v(log n−x)). Restar el prefijo de la serie de Dirichlet completa da la última línea. Las convenciones en los contactos no influyen en L². La diagonal sin normalizar es d_v=(ξ'/ξ)(v+1/2)/v por POWER_CONE_001.

**Extremo crítico.** Por ζ'/ζ(1+h)=−1/h+γ+O(h), los términos singulares dejan −x exp(x/2). En el término arquimediano integrar con t=x+r y z=exp(−t); se obtiene −exp(x/2) artanh(exp(−x)). Así

    k_*(x)=exp(x/2)[γ−x+Σ_{n<exp x}Λ(n)/n−artanh(exp(−x))]+exp(−x/2),
    d_*=2+γ−log(4π)>0.04.

La constante diagonal sale de la misma expansión, ψ(1/2)=−γ−2log2 y la fórmula de 001. En cada x-intervalo acotado la parte singular ya combinada converge uniformemente, salvo el prefijo con saltos fijos que también converge en norma suprema esencial. La integral arquimediana está dominada por C_L(1+|log x|) para v≥1/2; por convergencia dominada k_v→k_* en L²(0,L). En particular se puede usar esta expresión en el complemento de Schur sin restar dos cantidades numéricas divergentes.

**Ejemplo explícito cerca del extremo.** Para L=10⁻⁴ no hay primo interno; |k_*|≤3+0.51 log(3/x), usando (1+exp(−x))/(1−exp(−x))≤3/x. Al integrar el cuadrado de este mayorante se obtiene <0.009 (los dos primeros momentos de log(L/x) en medida uniforme son 1 y 2). El piso compacto supera 2: en la representación de Lévy del arquimediano el déficit de correlación es no negativo, y para t≥L la correlación se anula. Como m(0)>−6, K(t)≥1/t−1/2 para 0<t≤1, resulta A≥[−6+log(1/L)−1/2]||g||². El término polar cuesta ≤2L exp(L/2)||g||², y el peine se anula. Por tanto d_*−||k_*||²/2>0.035; por continuidad hay signo estricto en esta misma ventana para todas las tasas suficientemente próximas a 1/2 desde arriba. No se fija el tamaño del entorno.

**Una longitud común sin restricción de tasa.** Trabajar en coordenadas medidas desde el corte. Por 196 en una ventana inicial de longitud fija certificada hay margen uniforme para v≥V₀ suficientemente grande, usando cola de norma uno. Reducir L sólo restringe los datos a la izquierda del corte. Para v∈[1/2,V₀], normalizar multiplicando k_v por √(2v) y d_v por 2v. La diagonal normalizada tiene mínimo positivo en ese compacto: 001 da positividad por el núcleo theta en v>1/2 y el valor crítico es positivo. Por la cancelación anterior, el cruce normalizado es dominado uniformemente cerca de x=0 por C(V₀)(1+|log x|). Su norma L²(0,L) tiende uniformemente a cero. Escoger L₀≤10⁻⁴ de modo que el cuadrado de esa norma sea menor que la mitad del mínimo diagonal. La cota compacta ≥2 y Young dan una coercividad común para la combinación completa, por ortogonalidad de soportes de los dos datos. Esto cubre también la zona de tasas intermedias; L₀ no se calcula.

**Alcance.** 001 contiene la diagonal por derivada logarítmica y 196 el criterio de Schur a tasa fija. La información adicional es el vector de cruce regularizado, con su cancelación polo por polo, y un intervalo común para una cola arbitraria entre todas las tasas v>1/2. No se afirma positividad de una superposición de colas de tasas distintas ni para longitud compacta 5.53 a todas las tasas.
