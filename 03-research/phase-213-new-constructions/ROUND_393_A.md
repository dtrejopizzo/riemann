# Qué tamaño de primo bastaría y qué tamaño es inevitable

**Estado: PROVED, con revisión independiente de la constante4, la consecuencia incondicional y la barrera de exponente.**

Sea p_*(x) el menor primo terminal que admite la representación exacta de 392, incluidos los pesos terminales 0 y 1. Es finito eventualmente por 392. Se tienen dos cotas de distinta naturaleza:

* Si p_*(x)≤(log x)^(2+o(1)) eventualmente, entonces RH.
* Bajo RH, liminf p_*(x)/(log x)²≥4.

En particular, pretender una localización uniforme p_*≤(4−δ)(log x)² con δ>0 fijo sería contradictorio: implicaría RH por la primera afirmación y luego violaría la segunda. El resultado no asegura existencia al llegar a la constante 4.

**Mayorante que no necesita conocer el peso.** Para un corte terminal Y, cualquier peso terminal entre cero y uno, y σ real en un compacto fijo, la masa en módulo es ≤ C x^σ ∏_{z<q≤Y}(1+q^(−σ)), pues g(u)≤C exp(σu). Es un mayorante sobre los enteros, diferente de tomar módulos en el contorno de 388. Si Y≤L^(A+o(1)), A≥2 fijo y L=log x, elegir 1−1/A<σ<1. El logaritmo del producto es O(Y^(1−σ))=o(L), por suma incluso sobre enteros. En el corte mínimo el pulso completo tiene entonces exponente superior ≤1−1/A al dejar bajar σ. Para A=2, 372 excluye cualquier cero exterior. Más generalmente, si Θ>1/2, 372 implica limsup log(p_*)/log L≥1/(1−Θ), interpretado como infinito para Θ=1: todo A estrictamente menor que esa barrera da contradicción con el exponente Θ (para A<2 basta p_*≥z).

**Constante en el extremo de raíz.** Fijar 1<K<4 y Y=Kz, z=L², b=log z. Permitir todos los primos de (z,Y] en el mayorante. Para σ=1/2+c/b con c constante,

    Σ_{z<q≤Kz} q^(−σ)=(2(√K−1)e^(−c)+o(1)) L/b.

Esto sigue por sumación parcial del PNT en [z,Kz], usando q^(−c/b)=e^(−c)(1+o(1)) uniformemente. Por tanto el logaritmo de la cota para cualquier producto terminal en ese intervalo es a lo sumo

    L/2 + [c+2(√K−1)e^(−c)+o(1)]L/b.

Minimizar en c da c=log(2(√K−1)) y coeficiente 1+log(2(√K−1)). Por 368 y la calibración de la silla bajo RH, el logaritmo de |S| es L/2+[1+log 2+o(1)]L/b. El término gaussiano y el prefactor de la silla cuestan o(L/b) en logaritmo. Para K<4 el primer coeficiente es estrictamente menor, por lo que ningún peso en [0,1] ni corte ≤Kz puede reproducir S eventualmente bajo RH. Tomar K↑4.

**Registro de revisión.** La cota por módulos vale también para los pesos terminales0 y1, ya que todos los coeficientes del producto tienen módulo≤1 y se domina por permitir todos los primos hastaY. Para cada A fijo y cada σ>1−1/A, el exponente A(1−σ)<1 absorbe el o(1) en Y≤L^(A+o(1)); dejar σ bajar después justifica el techo de exponente1−1/A. Si el limsup del exponente de p_* fuese menor que1/(1−Θ), se escogería un A fijo estrictamente intermedio y se contradiría372. Para Θ=1 se descarta de esta manera cada A finito.

En el cálculo de la constante, el parámetro óptimo c=log(2(sqrt K−1)) puede ser negativo: está permitido, pues σ=1/2+c/b permanece en un compacto fijo y la cota gaussiana g(u)≤C exp(σu) no exige σ≥1/2. El error del PNT en[z,Kz] es uniforme para ese c fijo y el logaritmo de la constante gaussiana es O(1)=o(L/b). El contraste exacto de coeficientes es log(sqrt K−1)<0 para K<4. Esto prueba el liminf≥4 sólo bajoRH. La imposibilidad de un techo eventual(4−δ)L² sí es incondicional por combinar las dos implicaciones; no se convierte sin hipótesis en un piso punto a punto ni en un liminf≥4. La igualdad conS y la restricción del peso a[0,1] son esenciales para este argumento.

La oportunidad que permanece es encontrar un corte terminal de exponente 2+o(1). La escala x^o(1) obtenida en 392 es mucho mayor en general. El umbral necesario 4 se refiere a igualdad exacta con S bajo RH, no al signo de un sumando aislado.
