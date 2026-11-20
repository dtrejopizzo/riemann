# POWER_AUDIT_006 — Revisión independiente del test reparado por el contacto 2

Estado: PROVED y reejecutado. Papers intactos. Audita POWER_ARITHMETIC_WITNESS_006.md y tools/power_arithmetic_witness_006_verify.py.

## 1. Certificación aritmética y de matrices

El verificador Fraction se ejecutó independientemente con salida PASS. La norma N=99993678, la reducción de bandas Toeplitz y los coeficientes T_r son correctos: el factor 2 de los pares de bandas cancela el factor 1/2 de b_k, y la sustitución psi^(r)(16)=(-1)^(r+1)r!sum m^(-r-1) cancela el factorial restante. Se comprobó que cada coeficiente de signo negativo usa la cola superior en el extremo inferior y viceversa. Los momentos polares producen 126AB con las sumas racionales declaradas. La certificación da estrictamente

    -2/125 < (Arch+Polar)/N < -1/100.

Las cotas de d, logaritmos y gamma son las mismas ya auditadas en la ronda005; las colas de cada derivada de psi se acotan por las integrales desde256 y255, con orientación correcta.

## 2. Autocorrelación verificada por un cálculo independiente

Además de ejecutar la fórmula del constructor, se expandió directamente el polinomio P(x)=sum v_j L_j(x) en monomios y se calculó

    Q(t)=integral_0^infinito exp(-x)P(x)P(x+t)dx.

Si P(x)=sum p_a x^a, cada coeficiente se obtiene como

    [t^k]Q=sum_{a=0}^{11}sum_{b=k}^{11} p_a p_b binom(b,k)(a+b-k)!.

La integración exacta mediante Fraction/factoriales reproduce los doce coeficientes del memo, sin usar la identidad de Laguerre desplazada como premisa. Esto confirma la orientación de los términos cruzados y la ausencia de un factor dos faltante. Al escalar x=63y queda exactamente c_h(t)=e^(-31.5t)Q(63t).

El desplazamiento Q(x+40) tiene doce coeficientes estrictamente negativos, verificados de nuevo por el script. Por tanto Q<0 y Q'<0 en [40,infinito). Como 63log2>42, cada contacto primo-potencia real aporta signo positivo:

    -2Lambda(n)n^-32 Q(63log n)>0.

No se asigna signo estricto a enteros con Lambda(n)=0.

## 3. Reparación inferior sin estimar cola

Las desigualdades -Q creciente y log2>2/3 justifican con su signo exacto

    -2log2*2^-32 Q(63log2)/N >-(4/3)2^-32 Q(42)/N>1/25.

Todos los demás términos del peine son no negativos. Su serie converge absolutamente porque Q es un polinomio de grado once y el peso es n^-32. En consecuencia

    W[h]/N>1/25-2/125=3/125>1/50.

La cola no se omite como error pequeño: se conserva como suma de términos de signo favorable, lo cual basta para esta cota inferior. No se deduce que retirar el contacto2 haga negativa la suma de los restantes; haría falta una cota superior adicional.

## 4. Novedad y alcance

Se obtiene un caso exterior explícito en el que ARCH+POLAR es negativa y el contacto2 aislado compensa el déficit. Los antecedentes de necesidad aritmética general y de otros usos de Laguerre están detallados en POWER_AUDIT_005§7. La novedad concreta queda en el vector racional, la autocorrelación de signo comprobable y la reparación exacta del test presente; no es un certificado para todo el bloque de orden doce ni para el signo de todas las ventanas.

## 5. Ampliación revisada: eliminar solamente el contacto2 cambia el signo

El constructor añadió después de §§1–4 una cota superior de la cola. Revisada y reejecutada: APROBADA, sustituye la limitación anterior sobre no disponer de esa cota. Para r<=12, log3>1 garantiza que f_r(x)=(log x)^r x^-32 decrece en x>=3. Su suma se controla por f_r(3)+integral_3^infinito f_r(x)dx. La sustitución t=log x y la expansión binomial dan exactamente la fórmula de §4 del memo principal; usar log3<11/10 tiene el signo correcto porque todos sus coeficientes son positivos.

El script añadido certifica 1<log3<11/10 con J/E en r=1/2 y verifica, después de sumar los doce valores absolutos de coeficientes de Q, que la contribución TOTAL de n>=3 es menor que N/500. Por tanto

    W_sin_contacto2[h]/N < -1/100+1/500=-1/125.

Este paso sí permite ahora afirmar el cambio de signo al retirar exclusivamente n=2, manteniendo todos los n>=3, incluidas las potencias de2. La afirmación previa de §§3–4 era deliberadamente condicionada a no tener cota superior; esta ampliación aporta exactamente la pieza faltante. El resultado sigue referido al test exterior explícito, no a todas las direcciones ni a otra clase de portadores.
