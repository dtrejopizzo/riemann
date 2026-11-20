# Ajuste en potencias primas: un escalar sustituye las ecuaciones compuestas

Fijar g,h de 257, N=⌊2x⌋ y los acarreos c_{n,k}(m) de 261, 2≤n≤N, 1≤k≤n/2. Sea W(x) el mínimo de Σ|a_{n,k}| que reproduce g(m/x) sólo en potencias primas. Sea W_c(x) el mismo mínimo imponiendo además

    Σ a_{n,k} e(n,k)=xh,
    e(n,k)=n log n−k log k−(n−k)log(n−k).

Esta condición iguala las masas continuas de los dos lados, por 258. Para x≥3, W_c siempre es finito. El signo global equivale a W_c(x)≪_ε x^(1/2+ε) para todo ε>0. Ya no se requiere exactitud en los enteros con varios divisores primos. Para W sin el escalar no se ha demostrado esa recíproca.

**Suficiencia.** Poner J(x)=Σ_m Λ(m)g(m/x). Toda representación en los átomos da exactamente J(x)=Σ a_{n,k}log binom(n,k). Por Stirling uniformemente |log binom(n,k)−e(n,k)|≪log(2N). Para un ajuste calibrado sigue |J(x)−xh|≪W_c(x)log(2N). Su Mellin en Re s>1 es H(s)(−ζ'/ζ)(s)−h/(s−1), integrando desde 1 (el soporte de g(m/x) queda en x≥1 para m≥2). Una cota de raíz con pérdida arbitraria continúa esa diferencia a Re s>1/2, imposible ante un cero a la derecha por H(ρ)≠0. El uso de todas las potencias primas en esta identidad es esencial.

**Necesidad y corrección explícita.** La combinación de los acarreos de binom(6,1), menos los de binom(3,1) y binom(2,1), es cero en todas las potencias primas, porque c_{j,1}(m)=1_(m|j) para m≥2. En cambio su masa continua es η=6 log 6−5 log 5−3 log 3≠0 (6^6≠5^5 3^3). Cualquier error escalar Δ se corrige exactamente con coste ≤3|Δ|/|η|. Bajo RH tomar el ajuste entero de 261, de coste O_ε(x^(1/2+ε)). El error de masa cuesta en valor absoluto O_ε(x^(1/2+ε)log(2N))+|J(x)−xh|, y el segundo término es O(√x) por la serie absolutamente convergente de 257 bajo RH. Absorber el logaritmo reduciendo ε. Sin RH el mismo procedimiento construye un ajuste finito partiendo de 261; su coste de raíz queda abierto.

**Dual sin calibración.** W es el supremo de Σ z_m g(m/x) sobre z reales en las potencias primas hasta N, con |H_z(n)−H_z(k)−H_z(n−k)|≤1, H_z(n)=Σ_m z_m⌊n/m⌋. Es dualidad lineal finita, con factibilidad por las columnas binom(m,1) que permiten corregir de mayor a menor exponente para cada primo. Los incrementos de H_z son una función aditiva en argumentos coprimos. Por el promedio cíclico de 261, si el defecto de aditividad de H_z está acotado por 1, entonces |H_z(n)−nH_z(N)/N|≤2. Recíprocamente aproximar H_z por una recta por el origen con error E acota el defecto por 3E. Esto permite investigar el ajuste atómico a través de sumas parciales de funciones aditivas.

**Casos finitos certificados.** Los siguientes intervalos encierran los óptimos SIN el escalar. Cada intervalo se redondeó hacia afuera a la milésima.

| x | Sólo potencias primas | Todos los enteros |
|---|---|---|
| 16 | [2.517, 2.518] | [4.477, 4.478] |
| 32 | [2.612, 2.613] | [5.740, 5.741] |
| 64 | [2.745, 2.746] | [7.597, 7.598] |

Ejecutar python3 verify_262.py. El solucionador sólo propone testigos. Para el piso se redondean los coeficientes duales y se divide por el máximo exacto de las restricciones y la escala. Para el techo se redondea el primal y se repara su residual r con binom(j,1): en potencias del mismo primo basta restar residuos sucesivos, con coste ≤2Σ|r_m|. Para todos los enteros se usa la inversión sobre múltiplos y el coste ≤Στ(m)|r_m|. Los pesos y presupuestos residuales se evalúan con bolas Arb. Se comprueba una brecha interna <0.0001 antes del redondeo de la tabla.

**Qué queda.** Los tres ejemplos comprueban que las ecuaciones compuestas encarecen genuinamente esos ajustes. El escalar de masa es una condición adicional: el ejemplo con 6 demuestra explícitamente que el ajuste atómico por sí solo no lo determina. No se deduce de la tabla que el coste calibrado crezca a escala de raíz. Para probarlo mediante la corrección propuesta aún hay que dominar el error de masa; pagarlo con una estimación condicional de J no da una prueba independiente.
