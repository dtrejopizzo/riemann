# POWER_CUMULATIVE_INVERSE_022 — Primitiva compensada y balance celular con B

Estado: **PROVED** identidades de primitivas, masa aritmética y criterio celular cuantitativo; **PROVED** un punto positivo del kernel compensado donde h es negativo. **FALSIFIED** la hipótesis compensada universal K_N>=0 por el test completo N129 de POWER_CUMULATIVE_TEST_023.md; el criterio sigue válido como implicación. Emparejamiento firmado global **OPEN**. Papers intactos.

## 1. Corpus y diferencia precisa

Leídos las reglas del proyecto, SIGNED_MEAN019§§2–6 (PAIR), INVERSE_KERNEL020 (LOCAL/OUTER), STATE020 y el certificado completo INVERSE_INTERIOR022. Consultados el índice (Euler/Möbius, momentos e inversos), grid maestro y CROSSWORD-TO-D.md (sumación por divisores y rondas019/020). La identidad mu*1 y la integración por partes son clásicas; no se presentan como herramientas nuevas.

La diferencia es un criterio explícito MÁS DÉBIL que h>=0 que utiliza las pendientes y saltos del MISMO B, tolera crecimiento local de la primitiva de cola y produce una cota cuantitativa firmada. Su constante se combina con una masa discreta exactamente1 derivada de mu*1. No se repite PAIR como supuesto de signo y no se infiere una desigualdad global desde un único punto. El contraejemplo completo h128(1)<0 ya pertenece al otro constructor022 y se cita sin duplicarlo.

## 2. Primitiva completa, uniforme y masa entera exacta

Con u=63/2 y rho_N=C_N/C_N(0), ponga

    w_N(x)=x^(−1/2)rho_N(logx)=x^(−32)P_N(logx),
    H_N=−w_N',
    h_N(x)=sum_(m>=1)mu(m)mH_N(mx),
    J_N(x)=int_x^infty h_N(y)dy.

Aquí P_N tiene coeficientes positivos, P_N(0)=1, grado N−1; la recurrencia racional es la de020/022. Integración término a término da la fórmula COMPLETA

    J_N(x)=sum_(m>=1)mu(m)w_N(mx).                           (J)

Para cada N fijo, las series de (J), h y sus derivadas necesarias convergen absolutamente y uniformemente en x>=1: expandir P_N(logm+logx) reduce a términos m^(−32)(logm)^j por x^(−32)(logx)^l, estos últimos uniformemente acotados. La misma observación prueba J_N(x)=O_N(x^(−32)(1+logx)^(N−1)) y los límites en infinito usados abajo. No se trata de una primitiva formal de una serie condicional.

La identidad de divisores aporta una masa discreta EXACTA, con todos sus signos:

    sum_(n>=1)J_N(n)
      =sum_(n,m>=1)mu(m)w_N(mn)
      =sum_(r>=1)w_N(r)sum_(m|r)mu(m)=w_N(1)=1.            (MASS)

Fubini es absoluto: la suma de módulos está acotada por sum_r d(r)w_N(r), convergente ya con d(r)<=r. MASS no prueba que cada J_N(n) sea positivo.

## 3. El criterio compensado que tolera h negativo

Defina

    K_N(x)=J_N(x)+x h_N(x)=J_N(x)−xJ_N'(x).                 (K)

**Teorema celular.** Si K_N(x)>=0 para TODO x>=1, entonces J_N>=0 y

    F_N=2int_1^infty h_N(x)B(x)dx
        <=−2(3/4−log2)[1−J_N(1)]<=0.                     (CELL)

La hipótesis K>=0 es estrictamente más permisiva que exigir h>=0: admite h<0 mientras su magnitud sea <=J/x. Aquí se afirma una implicación, no que la hipótesis global esté probada.

Prueba. Por (K), (J_N(x)/x)'=−K_N(x)/x²<=0. El cociente tiende a0 en infinito, por lo que J_N(x)>=0. Para n>=2 y n−1<=x<=n,

    J_N(x)>=xJ_N(n)/n,
    int_(n−1)^n J_N(x)dx>=[1−1/(2n)]J_N(n).               (CELL-AVG)

B(1)=0; B tiene pendiente−H_(n−1) en(n−1,n) y salto logn en n. Integrar por partes, conservando los saltos, da

    F_N/2=int_1^infty J_N dB
      =sum_(n>=2){logn J_N(n)−H_(n−1)int_(n−1)^n J_N(x)dx}.

El borde J_N B se anula en infinito y ambas contribuciones convergen absolutamente. Por CELL-AVG, cada celda es <=J_N(n)[logn−H_(n−1)(1−1/(2n))]. Ahora

    H_(n−1)−logn>=1−log2,
    H_(n−1)/(2n)<=1/4.

La primera desigualdad crece desde n2 por comparación integral; la segunda se sigue de H_(n−1)<=n/2 por inducción. Así cada corchete es <=log2−3/4<0. Sumar y aplicar MASS prueba CELL. En particular la masa discreta no negativa implica J_N(1)<=1. QED.

Esto no es la identidad PAIR reetiquetada: K>=0 es una desigualdad puntual verificable suficiente, permite h negativo y entrega la constante explícita y la masa1. Tampoco CELL por sí sola prueba W>=0: aún debe compensar el déficit arquimediano sharp de019/020.

## 4. Kernel aritmético nuevo y región exterior

La función cuyo signo queda pendiente tiene una expresión concreta con el mismo inverso completo:

    K_N(x)=x^(−32)sum_(m>=1)mu(m)m^(−32)D_N(logx+logm),
    D_N(t)=33P_N(t)−P_N'(t).                              (KD)

Todos los coeficientes de D_N son estrictamente positivos: la recurrencia020 da (j+1)p_(j+1)<=u p_j, y33−u=3/2>0. No se deduce de esto positividad del inverso Möbius.

El argumento exterior020 se aplica también a D_N: si logx>=(N−1)/30, el cociente D_N(logx+logm)/D_N(logx)<=m^30. Por sum_(m>=2)m^(−2)<=3/4,

    K_N(x)>=x^(−32)D_N(logx)/4>0                          (OUT-K)

en esa región. OUT-K es una aplicación del lema ya probado020, no una nueva prueba de cancelación interior. Para un N al que se quiera aplicar CELL falta controlar K en el intervalo finito declarado. La versión universal para todos N es falsa por POWER_CUMULATIVE_TEST_023.md: −1/250<K_129(1)<−1/251. OUT-K sigue válido y no borra esa región negativa interior.

## 5. Punto hostil128: compensación real, sin extrapolación

INVERSE_INTERIOR022 prueba −2/3<h_128(1)<−33/50. Por continuidad, la primitiva desde1, int_1^x h_128, es NEGATIVA cerca de1; queda refutada su positividad universal. J_128 tampoco es monótona decreciente allí porque J_128'(1)=−h_128(1)>0.

Usando EXACTAMENTE el mismo corte64, los coeficientes P128 y las integrales de cola022, el verificador adjunto prueba sobre la suma COMPLETA

    .665<J_128(1)<.666,
    .003<K_128(1)=J_128(1)+h_128(1)<.004.                   (POINT)

La cola de J se acota con sum p_j I_j; la de K con sum(p_j+a_j)I_j, donde a_j son los coeficientes de A=32P−P'. Ambas son menores que10^(−10). Los valores orientativos son J128(1)≈.66561185155114 y K128(1)≈.003266751102; no participan en la prueba.

POINT muestra que el criterio compensado puede sobrevivir en el punto real donde falla h>=0 y donde J crece. No prueba K>=0 en una vecindad uniforme, en toda la semirrecta ni para otros N; por continuidad sí hay una vecindad de ese punto para N128 donde K>0. No se añade un certificado W ni una nueva región de tabla.

## 6. Residuo preciso

La hipótesis universal K_N>=0 queda refutada por023; el criterio CELL no se convierte en prueba de PAIR para todos N. El nuevo objetivo posible es una versión integrada de CELL-AVG o el presupuesto firmado de§7, conservando los mismos saltos. No basta J>=0 sin controlar promedios celulares; no se reemplaza h por su módulo ni se borran contribuciones adversas. La masa exacta1 puede servir para cuantificar un resultado de signo si se obtiene esa compensación global, pero no la suministra automáticamente.

Verificador: tools/power_cumulative_inverse_022_verify.py; Fraction/intervalos racionales, un solo punto y colas COMPLETAS. Reutiliza y reproduce el certificado interior022 antes de probar POINT. Sin campaña de N ni modificación de papers.


## 7. Kernel celular positivo y presupuesto de la parte negativa de K

La negatividad completa de K129(1) no se descarta ni se absorbe en una hipótesis. Sin N restringido ni condición de signo, la identidad diferencial de§3 da

    J_N(x)=x int_x^infty K_N(t)/t² dt.

Sustituirla en la integral de Stieltjes de§3, por Fubini absoluto, prueba

    F_N=−2 int_1^infty K_N(t) C_B(t)dt,
    C_B(t)=−t^(−2) int_1^t x dB(x).                       (CB-ID)

La identidad sola no resuelve el signo. Lo cuantitativo adicional es el siguiente lema sobre el MISMO B:

    C_B(t)>0 para t>1;
    C_B(t)=(1−t^(−2))/2 para1<=t<2;
    C_B(t)>=(3/4−log2)/2 para t>=2.                      (CB-POS)

Prueba. Escriba S(t)=int_1^t x dB(x). En una celda completa,

    S(n)−S(n−1)=nlogn−H_(n−1)(n−1/2)<=−a n,
    a=3/4−log2>0,

por la desigualdad numérica probada en§3. Así S(n)<=−a sum_(j=2)^n j y −S(n)/n²>=a/2 para n>=2. Entre n y n+1,

    C_B(t)=H_n/2+[C_B(n)−H_n/2]n²/t²,

una combinación convexa de C_B(n) y H_n/2, ambos >=a/2. En la primera celda dB=−dx y S(t)=−(t²−1)/2, dando la fórmula y la positividad. Los saltos de B se conservan, incluido el que reduce C_B en2. QED.

La masa aritmética también se transforma SIN sustituir K por su módulo:

    int_1^infty K_N(t) floor(t)[floor(t)+1]/(2t²)dt=1.       (K-MASS)

Se obtiene sustituyendo J en MASS y usando sum_(n<=t)n=floor(t)[floor(t)+1]/2. Fubini es absoluto por el decaimiento polinomial-logarítmico demostrado en§2. K-MASS no elimina las regiones negativas de K.

El presupuesto firmado exacto es ahora

    F_N=−2int K_N^+ C_B +2int K_N^- C_B.                  (BUDGET)

No se afirma que escribir BUDGET aporte por sí solo una desigualdad global. CB-POS sí cuantifica dónde pesa una lesión: para0<delta<=1,

    2int_1^(1+delta) K_N^-(t)C_B(t)dt
      <=delta² sup_[1,1+delta] K_N^- .                    (BOUNDARY)

En efecto C_B(t)<=(t−1) en la primera celda. La negatividad inicial de K129 aporta realmente un término adverso, pero su peso se anula linealmente en1 y el bound de esa región es cuadrático en su longitud. No se ha estimado aquí esa longitud ni la magnitud del presupuesto adverso total; por tanto tampoco se afirma que lo favorable lo compense. OUT-K conserva positividad exterior.

Se distingue así el resultado probado (kernel positivo explícito, cota uniforme exterior, amortiguación en borde y masa exacta) de la obligación abierta (control cuantitativo de BUDGET para el kernel real, suficiente además para compensar ARCH_sharp). No se reinicia la hipótesis K>=0 universal ya refutada.
