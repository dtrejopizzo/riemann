# La fase del corte determinista al mover la escala: ambos signos en cada bloque

**Estado: PROVED, con revisión independiente de la ley de fase móvil y de los saltos en ambos bordes.**

Fijar κ real. Sea C_κ(x) el pulso finito sin peso fraccional con z=L², b=log z, Y=(4+κ/b)z. Para cada L₀ grande, b₀=2log L₀ y 0≤u≤3b₀, el equivalente incondicional de 398 toma la forma

    C_κ(exp(L₀+u))/A_osc(L₀+u)
      = cos(Ψ₀+πu/b₀)+o(1)

uniformemente en u. Aquí Ψ₀ es la fase inicial de 398 y A_osc=2exp(Re G(s_*))/√(2π|G''(s_*)|)>0 es su amplitud local. En particular en CADA bloque de escalas [X,X(log X)^6] hay valores positivos y negativos de módulo al menos (1−o(1)) veces la amplitud correspondiente. En este bloque se varía x y se conserva la regla de corte; en 398 se mantenía fijo x y se variaba el corte.

**Movimiento entre saltos.** Usar la rama de G de 398 y la silla superior simple. Con el conjunto de primos fijo, la diferenciación de G(s_*) respecto de L da exactamente s_* ya que G'=0. Luego dΨ/dL=Im s_*=π/b+O(1/b²) uniformemente. En el bloque b=b₀+O(b₀/L₀), y el error integrado es o(1).

**Saltos de la fase.** Cada primo admitido por Y o retirado por z produce un cambio O(1/(L₀ b₀)) en Ψ. Para justificarlo interpolar su peso en [0,1] con L congelado. La derivada es la parte imaginaria de −p^(−s_*)/(1−λp^(−s_*)). En cualquiera de los dos bordes log p=b+O(1), p^(−Re s_*)≍1/L y |Im s_* log p−π|=O(1/b). La construcción local de 398 vale durante la interpolación también en el borde inferior: se modifica un solo factor de peso O(1/L) y quedan intactos los bloques interiores, la media límite y las cotas de derivadas. Al empalmar se recupera la rama por las mismas series convergentes; un salto simultáneo se divide en los dos pasos. Esto controla la fase real desenrollada.

Las funciones z(L),Y(L) son crecientes eventualmente, con derivadas O(L₀) en el bloque. Cada una barre un intervalo de longitud O(L₀ b₀). El número total de primos allí es o(L₀ b₀) incondicionalmente y sin PNT corto: para cada primorial fijo P el número de enteros coprimos a P en cualquier intervalo de longitud H es ≤H φ(P)/P+O(P); añadir los divisores primos de P y luego dejar P crecer. Así la suma de todos los saltos en módulo es o(1), uniformemente en bloques y subbloques. Junto con la derivada resulta la ley de fase propuesta. El error aditivo uniforme en el coseno viene de 398. Un intervalo angular de largo 3π contiene tanto un máximo como un mínimo; evaluar en los correspondientes u de la fase lineal da ambas excursiones aun cuando el pulso tenga discontinuidades.

**Registro de revisión.** Entre saltos G sólo depende explícitamente deL por Ls, así que la derivada total de su valor crítico es exactamente s_*; el movimiento de b no introduce un término adicional. En el borde inferior se elimina un factor y en el superior se añade: las orientaciones pueden tratarse por separado y el coste absoluto de fase es O(1/(L₀b₀)) en ambos, al interpolar el factor. Si ocurren simultáneamente se realizan dos pasos y las ramas por series vuelven al producto canónico. Las modificaciones de un factor no afectan a los bloques interiores ni a la construcción uniforme de398.

Para cada primorial fijoP, el número de primos en cualquiera de los intervalos barridos es≤C L₀b₀φ(P)/P+O(P)+ω(P). Dividir por L₀b₀, pasar L₀→∞ y después P→∞ prueba el o(L₀b₀) uniforme, sin dejar crecerP antes del límite ni usar un PNT de intervalos de longitud raíz. La suma absoluta de saltos es por tanto o(1). La integral del error O(b^(−2)) a lo largo de3b₀ es O(1/b₀), y reemplazar b por b₀ cuesta o(1). Esto controla la fase desenrollada también en los puntos de discontinuidad. Evaluar en los puntos donde la fase lineal vale0 oπ módulo2π usa el error aditivo uniforme del coseno y no requiere que el pulso sea continuo al variarx.

**Obstrucción.** Ninguna elección de κ constante en esta familia produce signo negativo eventual del producto finito. Si RH vale, el pulso completo S sí es negativo eventualmente por 368, de modo que un corte determinista de esta forma no puede reproducirlo en todas las escalas. Esto concierne al signo o a la igualdad exacta: el propio pulso finito siempre admite un techo de exponente 1/2+o(1) por 393, y sigue pendiente una cota del error que se comete al sustituir S.
