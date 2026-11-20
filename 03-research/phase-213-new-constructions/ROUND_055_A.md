# Qué detectan las clases de residuos en el criterio de 054

Usar L=√x, y=4x, K=C₀L(log x)² y los pesos de 054. Denotar por R(q) el peso de la fila antes de multiplicar por Λ(q), incluyendo la restricción q>L:

    R(q)=1_{q>L} Σ_{v,m≥1} α(v) U(qv) μ(m) V(qvm/y).

Aquí q puede ser cualquier entero. Para cada 0<η<1/2 fijo, con C₀ suficientemente grande fijado de una vez,

    sup_{d≤x^(1/2−η)} Σ_{r mod d} | Σ_{q≡r mod d} R(q) | = o(1).

En particular se puede sustituir Λ(q) por Λ(q)−1 en el criterio inferior de 054. También se puede restar cualquier perfil periódico de módulo en ese rango y norma suprema acotada. La afirmación concierne a los pesos de prueba R, no a la distribución de primos en progresiones.

**Paso a modelos periódicos.** Sea f real, d-periódica, |f|≤1. En la suma completa sin U y con todos los q, α*μ está soportada en j=1,2,4 con masas c_j=1,−4,4, respectivamente. Resulta Σ_q f(q)Σ_j c_j V(jq/y). Las partes integrales de la media de f se anulan por Σc_j/j=0. El resto tiene tamaño O_N(y(d/y)^N): en cada progresión sumar el peso suave por Poisson, con N≥2 integraciones por partes. Para una función suave apoyada en una banda de anchura comparable a Q y derivadas de orden n acotadas por C_n Q^(−n), el error por progresión cuando d≤Q es O_N((Q/d)(d/Q)^N), uniforme en el residuo. Al sumar los d residuos queda O_N(Q(d/Q)^N).

Las filas con q≤L y U cuestan en conjunto O(y log x exp(−c√(K/(4L))))=o(1). En efecto, sus sumas plenas son cero; las cuadraturas de sus partes altas tienen densidad combinada cero por 054. Esta cota sólo usa |f(q)|≤1. Se toma C₀ suficientemente grande para que el exponente absorba y log x.

**Parte alta de la media constante.** Escribir ε(n)=(−1)^(n+1). La convolución de divisores satisface 1*α=ε*ε: ambas son la convolución de dos funciones constantes con los tres átomos c_j, pues ε=1*(δ₁−2δ₂). Así, para el modelo constante, la parte con 1−U se expresa exactamente como

    Σ_{a,b,m} ε(a)ε(b)μ(m)[1−U(ab)]V(abm/y).

Usar una partición diádica suave en a,b, con tamaños Q,R, respectivamente. En una caja no vacía QR≳K, m≪y/(QR), y al menos uno de Q,R es ≳√K. En la variable mayor la alternancia tiene media cero y la estimación de progresiones da la ganancia O_N(max(Q,R)^(−N)) respecto del conteo trivial. Las derivadas del corte cuestan O_n(Q^(−n)) o O_n(R^(−n)) en la correspondiente variable, por ser un corte fijo en log(ab/K); se cumple lo mismo para el peso V en el soporte de sus derivadas. Sumando en las demás variables y en las O(log²y) cajas resulta O_N(y K^(−N/2) log²y).

**Parte alta del perfil de media cero.** Descontar la media de f e incorporar la estimación precedente. En la suma alta original tomar cajas q≈Q,v≈R. Tanto f(q) centrada como α(v) tienen media cero, con períodos d y 4. La mayor escala medida en períodos es al menos una constante por √(K/d), pues QR≳K. Aplicar la estimación de progresiones en la variable que alcanza esa escala. La uniformidad respecto de los residuos evita que aparezca un factor adicional d. El conteo restante da

    O_N(y (d/K)^(N/2) log²y).

Para d≤x^(1/2−η), elegir N>2/η. Todas las cotas son uniformes en f y d. Restando la parte alta y las filas pequeñas de la suma completa se obtiene Σ f(q)R(q)=o(1). Elegir f en cada clase como el signo de su suma prueba el enunciado.

**Alcance.** El corte alto del modelo constante explota la factorización en dos variables alternadas; centrar el peso primo antes del corte no bastaba para justificar el resultado. La cota vale para la suma completa de 054. Imponer después una restricción sobre qvm puede romper la factorización. La estimación inferior uniforme de Σ(Λ(q)−1)R(q) sigue abierta.

**Rango casi de raíz.** La misma conclusión vale uniformemente para d≤c₀ L/(log x)² con c₀>0 fijo suficientemente pequeño. Para controlar los órdenes de derivación usar la partición telescópica χ(log u−i)−χ(log u−i−1), i entero, en cada variable positiva. Hay O(log²y) cajas activas en las sumas enteras. En una variable z de escala Q, las derivadas ordinarias de orden N del peso de caja tienen norma L¹ ≤Q^(1−N) C^(N+1)(N!)²: en log z los factores son traslaciones de los pesos fijos de 047 y sus productos conservan la cota por Leibniz, y la conversión a derivadas ordinarias es la demostrada en 047. Por tanto al elegir el orden en la variable larga, la contribución alta por caja es ≤Cy exp(−c√max(Q/d,R)), por el mismo cálculo de optimización de 047. En total cuesta O(y log²y exp(−c(K/d)^(1/4))). Para d≤c₀L/(log x)² el exponente supera 2log x si c₀ es suficientemente pequeño. La media constante y las filas pequeñas ya están controladas; la suma completa de f periódica también se estima con un orden fijo grande pues d/y es de orden a lo sumo x^(−1/2). Este argumento usa un solo módulo cada vez, con uniformidad en su elección. El antecedente CORRECTION_RESIDUE_BALANCE_031 de fase 211 describe el fallo de inferir cancelación para pesos arbitrarios sólo por balance en una clase completa. Aquí el control cuantitativo proviene de la regularidad del peso y de la segunda variable de media cero.
