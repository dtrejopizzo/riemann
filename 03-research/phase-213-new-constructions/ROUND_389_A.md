# Una banda horizontal que ningún contorno simple de módulos puede rodear

**Estado: PROVED, con revisión independiente de todas las abscisas, la reflexión y el coste geométrico de curvas.**

Sean D,z,y,L como en 388, b=log y∼L/2 y h=log L. Para todo t∈[0.95π/b,1.05π/b] y toda abscisa real σ se tiene uniformemente

    |x^s exp((s−1/2)²/2) D(s)| ≥ x exp(−O(h^12)),   s=σ+it.

Por tanto toda trayectoria rectificable por tramos que vaya de debajo a encima de esa banda paga ≥x exp(−O(h^12))/b en la integral del módulo. La vertical 1 da un coste ≤x^(1+o(1)) para el contorno completo. El óptimo en exponente sigue siendo uno incluso permitiendo curvas y abscisas negativas.

**Franja cerca de uno.** Para σ≥1 se usa |D|≥∏(1−1/p)≫1/b. Si 0≤1−σ=w/b con w≤10log h, entonces σ≥1/2 eventualmente y log|D|≥−2Σ p^(−σ)≥−O(h^11), pues p^(−σ)≤e^w/p y Σ_{p≤y}1/p=O(h). Además σL≥L−O(log h). El factor gaussiano en módulo siempre es ≥exp(−t²/2).

**Abscisas 1/8≤σ<1 con w>10log h.** Todos los factores con log p≥3b/4 tienen cos(t log p)≤−c. La parte b−b/(2w)≤log p≤b aporta a log|D| al menos c exp(w)/w. En efecto el peso de cada intervalo diádico de primos allí es ≫exp(w)/b por PNT y p^(1−σ)≥exp(w−1/2). Si b/(2w)<2 log 2 usar la subbanda final de ancho logarítmico 1/2, que cabe pues w≤7b/8, y aplicar el PNT con razón fija. Este argumento da ≫(1+b/w)exp(w)/b en ambos casos. El coste negativo restante es ≤C exp(3w/4) h, por Mertens y p^(−σ)≤z^(−1/8)=o(1) para estimar el logaritmo. El cociente por exp(w)/w es O(hw exp(−w/4))=o(1) uniformemente para w>10log h. El piso log|D|≫exp(w)/w absorbe la pérdida (1−σ)L=O(w).

**Abscisas entre cero y 1/8.** Aun cuando p^(−σ) esté cerca de uno, para p<y^(3/4) el módulo |1−p^(−σ)exp(−it log p)| es ≥c/b: minimizar en el radio real positivo da seno del ángulo hasta π/2 y uno desde allí en el arco considerado; t log p≫1/b. El coste negativo es O(y^(3/4)log b). Los primos en [y/2,y] aportan ≫y^(7/8)/b, pues log|1−p^(−s)|≫p^(−σ) en ese arco; todos los demás de la franja superior suman términos no negativos. El piso excede L.

**Abscisas negativas.** La identidad exacta |D(−u+it)|=exp(uΣ_{z<p≤y}log p)|D(u+it)| para u≥0 muestra que el módulo del integrando en −u dividido por el de +u es exp(u(Σlog p−2L+1)). El último 1 proviene de la gaussiana. Es ≥1 para x grande por el PNT. Finalmente la longitud de la porción de curva en la banda es al menos su altura, aun con retrocesos, de donde la afirmación.

**Registro de revisión.** Para σ≥1 la desigualdad factor a factor |1−p^(−σ−it)|≥1−1/p cubre también σ sin techo superior. En el tramo intermedio w>10log h, la razón O(hw exp(−w/4)) se maximiza en el extremo inferior para h grande y tiende a0; además exp(w)/w≫w, uniformemente, de modo que el piso absorbe (1−σ)L aun cuando σ esté lejos de1. La banda final de anchura1/2 cabe porque b/(2w)≥4/7 para σ≥1/8. Para0≤σ≤1/8, minimizar el módulo en cualquier radio positivo da al menos sin(t log p) si el ángulo está bajo π/2 y al menos1 cuando lo supera. En el arco inferior el ángulo está separado de0 por c/b, y en el superior todos los logaritmos de módulo son no negativos. Así el coste O(y^(3/4)log b) y el piso y^(7/8)/b son uniformes también en σ=0.

La identidad de reflexión usa |D(u−it)|=|D(u+it)| y el cociente de los factores gaussianos es exactamente exp(u); de ahí el término+1 y la comparación uniforme en todo u≥0. Finalmente, para una curva continua rectificable por tramos que atraviese ambas fronteras, ∫_banda|ds|≥∫_banda|dt|≥0.1π/b, incluso si hay retrocesos. Multiplicar por el piso puntual da el coste afirmado y su exponente1, ya que h^12=o(L). No se supone que la curva sea un gráfico en t ni que sus abscisas estén acotadas.

Alcance: el menorante se aplica al integrando intacto y a la integral de su módulo. No se aplica si primero se combinan contribuciones con sus fases o se resta un término cuya integral se conoce.
