# Ventana de búsqueda en número de primos alrededor de una amplitud calculable

**Estado: PROVED, con revisión independiente de las constantes, la normalización y el primer acierto.**

Sean α,K de 368 en el corte z=L², b=log z y T₀=exp(K(α))/(|ζ(1/2)|√(2πK''(α))). Este número positivo usa ζ en un punto real y el producto hasta z, sin conocer S. Enumerar en orden creciente los primos terminales de la franja κ₀−1≤b(Y/z−4)≤κ₀+1 de 398; recorrer cada primo con el peso λ de 0 a 1 y usar como coordenada r el número de pasos de peso acumulados (cada primo tiene longitud uno). Definir

    A₀(r)=2 exp(Re G(s_*))/√(2π Lb).

Hay un único r₀ con A₀(r₀)=T₀. Bajo RH, si r_* es la coordenada del primer peso que reproduce S, entonces para cada ε>0 fijo, eventualmente,

    r₀−ε L ≤ r_* ≤ r₀+[8/(2−log 4)+ε] Lb.

Esto acota una parte de la adaptación en número de primos; no se convierte la anchura en longitud usando un promedio de huecos primos.

**Calibración sin consultar S.** Las comparaciones de 394–395 con T₀ son incondicionales: RH sólo se usó para sustituir T₀ por |S|. La corrección al logaritmo de la amplitud firmada cuesta O(L/b³) por 398. En cada extremo de la franja, log(A₀/T₀) tiene signo opuesto y módulo ≍L/b² (tomar el primo interior más cercano no altera el resultado, por el PNT con resto como en 398, o empezar con el conjunto de primos ya presente en el extremo real). En la franja la derivada exacta de G(s_*) con respecto a λ es −p^(−s_*)/(1−λp^(−s_*)); su parte real satisface

    ∂_r log A₀=(1+o(1))/(4L),

porque Re s_*=1/2+(log 2+o(1))/b y p/z→4. Su parte imaginaria, por 398, es

    ∂_r Im G(s_*)=−[π(2−log 4)+o(1)]/(4Lb).

Ambas estimaciones son uniformes y empalman al pasar al siguiente primo. La primera asegura unicidad de r₀ y deja ≫L²/b² pasos entre r₀ y cada extremo. El prefactor de 398 difiere de A₀ por 1+o(1): G''(s_*)/(Lb)→1 por la ecuación de la silla positiva, log p=b+O(1) y 398.

**Alcance del primer acierto.** Bajo RH, |S|/T₀→1. Para todo r≤r₀−εL en la franja, la envolvente continua A₀(r)≤T₀ exp(−ε/4+o(1)) no alcanza |S| ni con el error uniforme de 398. Antes de la franja la exclusión es la de 394, válida para todos los pesos. Para la otra dirección empezar en r₀+L√b: la envolvente ya supera T₀ por un factor que tiende a infinito. Una vuelta completa de fase necesita (8/(2−log 4)+o(1))Lb pasos. En el recorrido se alcanzan fases de ambos signos del coseno con módulo uno, por continuidad, contando si hace falta un o(Lb) adicional. Allí los saldos finitos encierran S; por interpolación se lo alcanza en el intervalo anunciado. Los redondeos de un primo son O(1).

**Registro de revisión.** En el factor terminal p^(−s_*)=−a exp(−iδ), con a=(1+o(1))/(4L) y δ=[π(2−log4)+o(1)]/b. La parte real de a exp(−iδ)/(1+λa exp(−iδ)) es a(1+o(1)); su parte imaginaria es−a sinδ/(|1+λa exp(−iδ)|²). Así se obtienen las dos tasas con factor1/4 y, para una vuelta de2π, exactamente8Lb/(2−log4). Los empalmes son continuos y las tasas uniformes, incluidos los pesos0 y1. La ecuación positiva y log p/b→1 dan G''(s_*)/(Lb)→1; por eso A₀ y la amplitud compleja de398 difieren sólo en1+o(1), sin perder un factor2 ni una raíz de2π.

Los márgenes r₀−r_inicial y r_final−r₀ son≳L²/b², que dominan tantoLsqrt b comoLb. Por tanto la vuelta de fase usada para el techo cabe en la franja. Antes de r₀−εL se utiliza la monotonía deA₀ para reducir la estimación a un intervalo de longitudεL; no se acumula un error relativo no uniforme sobre toda la lista. La exclusión de394 antes de la franja vale para cualquier peso, y bajoRH |S|/T₀→1. Esto localiza al primer acierto global y no sólo a alguno de los aciertos del bloque. Las afirmaciones sobre r₀, sus márgenes y las tasas son incondicionales; tanto excluir valores anteriores por comparación conT₀ como afirmar que los extremos encierranS en esta ventana usanRH.

La construcción de r₀ y la amplificación de ambos signos son incondicionales. La localización de r_* usa RH. El problema pendiente es comparar el saldo completo con el rango de valores de estos productos sin usar el equivalente para S de 368.
