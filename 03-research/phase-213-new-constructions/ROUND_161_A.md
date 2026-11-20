# Dos contribuciones de signo determinado en la banda de 160

Con K,B,P,W,d=1/4 de 160, la parte de las potencias no primas en la suma filtrada vale, incondicionalmente,

    Σ_{p,k≥2} (log p) K(x/p^k)
       = [B(1/2)/2]√x + [B(1/3)/3]x^(1/3) + o(x^(1/3)).

Ambos coeficientes son estrictamente negativos. La misma expansión vale al restringir a la banda q>x/(K₀ log⁶x) de 160, pues su error o(1) se probó en módulo total. A diferencia de estimar los cuadrados por el teorema de los números primos, aquí la precisión del término de raíz cuadrada basta para distinguir el término cúbico.

**Parte par completa.** En Re s>1 el Mellin de la suma sobre p y k par es B(s)(−ζ'/ζ)(2s)=−P(s)W(s)ζ(s+d)ζ'(2s). Por tanto en cada cero de ζ(2s) la singularidad ya está eliminada. En 1/2 sólo queda un polo simple (el polo doble de ζ' se encuentra con el cero de P), de residuo B(1/2)/2. No quedan polos en 0 ni en 1−d. En cualquier tira vertical fija las derivadas de zeta tienen crecimiento polinómico por Cauchy y la ecuación funcional, mientras PW decrece más rápidamente que cualquier potencia en altura. Desplazar a Re s=−N para N fijo da el principal de raíz con error O_N(x^(−N)), sin hipótesis sobre los ceros. El signo resulta de B(1/2)=P'(1/2)W(1/2)ζ(1/2+d)/2, con P'(1/2)>0 y ζ(3/4)<0.

**Parte impar.** Sea X=x^(1/3). Por el teorema de los números primos la medida X^(−1)Σ log p δ_(p/X) converge a Lebesgue en intervalos compactos de (0,∞). El perfil t↦K(t^(−3)) es continuo, tiene extremo superior de soporte finito por 160 y se prolonga por cero en el origen. Chebyshev controla uniformemente el extremo pequeño. Así el coeficiente de X es ∫K(t^(−3))dt=B(1/3)/3 por Mellin; la transformada de K converge para todo s por los dos extremos de 160. En s=1/3 el polinomio P es negativo, W es positivo y ambos factores zeta reales son negativos, luego B(1/3)<0. Para k≥5 sólo cuentan p^k≤exp(A)x y K está uniformemente acotada. El exponente 5 cuesta O(x^(1/5)) por Chebyshev; la suma de los impares k≥7 cuesta O(x^(1/7)log x), al haber O(log x) exponentes. Esto prueba la expansión.

**Qué queda para el signo.** En el techo original de orden √x de 160 basta trabajar con los primos simples, cuyos excesos siguen sin cota demostrada a esa escala. 107 y 152–154 ya separaban potencias y 154 daba la identidad puntual de los cuadrados. La precisión O_N(x^(−N)) para la parte par en este filtro permite declarar el signo de la siguiente corrección sin presuponer una tasa para el error del teorema de los números primos. La expansión no prueba el signo de la suma sobre primos.
