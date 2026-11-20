# Un intervalo de grados certificado dentro de un criterio que detecta todos los ceros

Fijar c=1.25·10^(−25), W=cT y Y normal centrada de varianza W. Para polinomios reales normalizados por E[P(Y/√W)²]=1, formar la cuadrática

    Q_T(P)=E[P(Y/√W)² U(T+Y)],    U(t)=exp(−t/2)L(exp t).

Sin RH, uniformemente en TODOS los polinomios de grado ≤floor(cT), se tiene Q_T(P)=1/ζ(1/2)+O(exp(−10^(−24)T)). En particular toda la matriz de esta cuadrática es negativa definida para T suficientemente grande, con margen uniforme. A su vez, el signo global equivale al techo subexponencial de la parte positiva del mayor cociente, para cada pendiente fija de grado κ>0 (grado ≤κT). Si existe un cero fuera de línea, alguna pendiente fija admite cocientes positivos exponenciales en toda escala suficientemente grande.

**Intervalo certificado.** En la base de Hermite probabilista ortonormal la derivada baja el grado y tiene norma ≤√d en grado ≤d. Trasladar por h complejo es exponenciar h∂, de norma ≤exp(|h|√d) desde ese espacio a sí mismo. El multiplicador en el contorno de 145 es

    E[P(Y/√W)² e^{sY}]=exp(Ws²/2) E[P(Z+s√W)²],    Z normal estándar.

La igualdad se obtiene para s real por cambio de media y luego por continuación entera. La cota en módulo para el integrando, sin R(s), tiene tasa por T a lo sumo σ+c(σ²−τ²)/2+2c|s| si d≤cT. En la línea derecha σ=.54, por encima de altura 2.99·10¹² la tasa es <−.01; lo mismo en los horizontales del rectángulo de 145. En el lado izquierdo σ=−1/4 es <−.24, incluso al maximizar en τ. En los ceros incluidos σ=0 y |τ|>14, la tasa es ≤c(−14²/2+28)=−70c. Rodear cada uno por un pequeño círculo fijo y disjunto donde la tasa siga siendo <−2·10^(−24); esto permite multiplicidades cualesquiera con constantes independientes de P,d,T. El residuo real en cero es a=1/ζ(1/2) por normalización. Se concluye la estimación uniforme por el mismo contorno finito. La verificación de altura utilizada es Z2 de P47.

**Por qué las pendientes mayores importan.** Bajo RH, |U(t)|≪ε exp(εt) para t≥0 y U=0 para t<0. La traslación anterior en s=ε da |Q_T(P)|≪ε exp(T[ε+cε²/2+2ε√(cκ)]) cuando d≤κT. Para cada κ esto da tasa exponencial superior cero usando log(1+|Q|).

Si hay un polo z=b+iγ con b>0, modular la gaussiana por exp(−iτY), con τ fijo cercano a γ. En el rectángulo finito de 142 el multiplicador es exp(Ts+W(s−iτ)²/2); centrando la frecuencia se obtiene un máximo de tasa estrictamente positivo. Elegir τ genérico en el abierto para tener un máximo único: para polos de igual ordenada la tasa crece con b en la franja usada, y para ordenadas distintas sólo hay un empate por pareja. Los contornos se eligen después de τ, incluyendo los maximizadores y a distancia de los polos. El borde izquierdo es negativo y las colas derechas se hacen despreciables a altura finita suficientemente grande. El coeficiente líder para un polo múltiple contiene (1+c(z−iτ))^(m−1)≠0. Por ello el módulo de E[U(T+Y)exp(−iτY)] supera exp(ηT) para algún η>0 en todo T grande. Escoger una fase según T y usar que E U(T+Y)→a: el peso 1+cos(τY+fase)=2cos²((τY+fase)/2) da una cuadrática positiva de tamaño exponencial.

Aproximar ese coseno por su Taylor en y=0 hasta d=floor(κT), guardando la fase en los coeficientes. El error puntual real es ≤(|τy|/2)^(d+1)/(d+1)!. Para n=d+1, la norma L² de este error en la medida exp(y/2)φ_W(y)dy es ≤exp(W/16)[C|τ|(W+√(Wn))/n]^n por inclinación de la normal, la cota de momentos gaussianos y Stirling. Lo mismo sin inclinación. Con κ suficientemente grande según τ,c el error es O(exp(−2T)) en ambas normas. Por Cauchy–Schwarz y |U(T+y)|≤exp((T+y)/2), reemplazar el coseno por el polinomio cuesta o(1) en la cuadrática, también teniendo en cuenta que la norma del coseno en la medida inclinada es ≤exp(W/16). La norma gaussiana ordinaria del polinomio es acotada y es no nulo por la señal positiva. Tras normalizar se conserva una tasa positiva. Esto prueba la equivalencia, sin reclamar que todos los grados tengan signo negativo bajo RH.

**Por qué no bastaba aproximar directamente el peso corto.** En L² de la normal estándar, la raíz del cociente de las densidades gaussianas corta y ancha es g(t)=q^(1/4)exp(−(q−1)t²/4), q=W/V, V=j log(j+2) de 144. Su coeficiente de grado 2k es

    q^(1/4)((q+1)/2)^(−1/2) [−(q−1)/(q+1)]^k √((2k)!)/(2^k k!).

Se obtiene integrando la generatriz exp(tz−z²/2). Para d=O(T) el primer coeficiente par omitido tiene módulo ≥exp(−O(V+log T)); es una cota inferior para el error L². No justifica una precisión exp(−δT) con δ>0 fijo para trasladar el signo por la cota elemental de U. La modulación de frecuencia fija es la que hace funcionar la demostración anterior.

**Cotejo y alcance.** 115/122 ya detectan polos por modulación o por espacios crecientes para la forma de Weil. 145 certificaba la constante (P=1) de la media de Liouville. Aquí se verifica a la vez la cota uniforme en un intervalo lineal de grados para esta cuadrática aritmética y la detección por alguna pendiente mayor si el signo falla. La parte pendiente es un techo subexponencial para todas las pendientes fijas; la certificación de este intervalo no lo demuestra.
