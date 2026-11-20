# Los cubos deciden el contacto en el umbral de cobertura de cuadrados

Con la notación de 102, bajo RH sea A=sup_T(−J(T)) y λ*=1−A/2. El conjunto de λ∈[0,1] con U_λ(x)≤x eventualmente es exactamente el intervalo CERRADO [0,λ*]. En el extremo mismo,

    x−U_(λ*)(x) ≥ 3x^(1/3)−O(x^(1/4)).

No se afirma que el coeficiente 3 sea el límite inferior exacto del margen normalizado: eso exigiría controlar con qué rapidez se acerca −J a su supremo.

En efecto, por 092 bajo RH S(y)=y+O(√y), ya que J es acotada. Por otro lado, el peso integrado de todas las potencias primas es Σ_{k≥1}k S(x^(1/k)) y por la fórmula explícita integrada de 092 vale x−√x J((log x)/2)+O(log x). El bloque k≥4 es O(x^(1/4)): separar k=4, y para 5≤k≤log x/log 2 usar S(y)≪y y la cota O(x^(1/5)log²x). Extrayendo cuadrados y cubos queda, uniformemente para 0≤λ≤1,

    U_λ(x)−x = √x[−J((log x)/2)−2(1−λ)] − 3x^(1/3) + O(x^(1/4)).

En λ* el corchete es siempre ≤0, incluidos los contactos y las aproximaciones arbitrariamente cercanas. El término cúbico tiene signo fijo y domina todo el error. Por monotonía en λ se obtiene el resto del intervalo cerrado; para λ>λ* se aplica la recurrencia de 102. Sin RH ningún λ sirve por 092. En particular el techo para el valor explícito λ=1−D/2 equivale al signo global, porque bajo RH A≤D. Esto resuelve el extremo dejado abierto por la estimación de primer orden de 102. No determina A ni la positividad global.
