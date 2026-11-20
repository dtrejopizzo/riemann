# AUDIT_013 — Escalas universales del mapa Mellin–Gauss011

2026-10-19. Revisor independiente. Leído LINK_013_NO_FIXED_SCALE y cotejados P47 lem:testfam, thm:margin CON SU PRUEBA y cor:margin1.
**Veredicto: PROVED la exclusión de toda escala universal c>0 para U011, con el input CITED de la cota del paper sobre esa familia explícita. No exclusión de c(T), otros mapas o D.**

## 1. Corpus y cambio de clase

Consultados índice/grid/crucigrama, familias de margen y entradas011–012. La razón nueva es válida:012 trató una escala en una ventana;013 evalúa el MISMO mapa en los tests concretos responsables del margen cuando T→∞. No se intenta repetir la igualdad descartada ni se transforma un ínfimo pequeño en información sobre cualquier vector. El cálculo de M(F_T) es indispensable y se ha efectuado.

La cota CITED de P47 usa sus datos certificados Z1/Z2 y la fórmula explícita. Aquí sólo falsifica una dominación del auxiliar; no es una fuente de signo positivo de D ni se introduce equivalencia externa alguna.

## 2. Perfil h y Riemann impropia

La identidad h=2y^(1/4)[z_cm(y)−Σ(d^(−1/2)−d^(−1))m(d²y)] es exacta: la contribución de c cancela mediante Σv(d)/d=z_c. Las series convergen por las cotas ya probadas, sin separar un vector polar divergente.

Con N=y^(−1/2) y g(r)=r^(−1/2)m(r²), se verifica exactamente

    N^(−1/2)Σd^(−1/2)m((d/N)²)=(1/N)Σg(d/N).

La dominación g≤min(r^(−1/2),r^(−3/2)) controla las sumas cerca de cero y en infinito por2√ε+o(1) y2/√R+o(1). En un intervalo [ε,R] la suma usual converge por continuidad. No se invoca incorrectamente una Riemann ordinaria sobre un extremo singular.

La integral de g es κ/2 por y=r², con factor1/2 correcto. El término d^(−1) es O(1+logN) antes del factor N^(−1/2); su cola se acota mediante m((d/N)²)≤N/d. El término z_cm también desaparece. Así h(−∞)=−κ. La representación original con τ prueba h(+∞)=0 por decaimiento gaussiano; convergencia local uniforme da continuidad. Junto con los límites, h es acotado y h_ev→−κ/2 en ambos extremos.

## 3. Spline, derivadas y masa que escapa

Para cada j fijo, la fórmula Plancherel tiene prefactor k^(2j+1). En |v|≤1, |sincv|≤exp(−v²/7) produce integral O(k^(−j−1/2)), por lo que el producto es O(k^(j+1/2)). Los intervalos [1,2] y [2,∞) dan contribuciones exponencialmente pequeñas para k grande usando sin1<1 y v^(−2k). Con exponente k y sin peso se obtiene ||ω_k||∞=O(√k). Los argumentos y órdenes están correctos.

Para k~T,

    ||G_T^(j)||₂=O(T^(3/4−j/2)).

Cauchy–Schwarz en soporte de longitud2T da los dos órdenes L¹ T^(1/4) y T^(−3/4), y ||F_T||²=O(T^(3/2)). No se deriva un perfil h cuya integrabilidad de derivadas no se haya probado.

G_T/T es probabilidad y su masa en |x|≤R es O_R(T^(−1/2)). Aunque G_T se concentra en x/T cerca de cero, en la coordenada física x su anchura crece: la masa escapa de cada compacto fijo. Con h acotado y h_ev→−κ/2 esto prueba ∫G_Th/T→−κ/2. No hace falta un límite puntual de G_T.

## 4. Respuesta del mapa y dominio

P(D) coincide término por término con el polinomio de P47. El término −γ₁²G_T/4 da el principal positivo de M; las dos derivadas contribuyen o(T). Así

    M(F_T)/T→γ₁²κ/8,
    liminf ||U_TF_T||²/T²≥γ₁⁴κ³/64>0.

El signo y todas las potencias de κ son correctos.

Para invocar las propiedades del test basta fijar T≥1: k=ceil(21T/e)≥8, G tiene derivadas suficientes y F está en H¹ con soporte y momentos exigidos. Se comunicó explicitar ese umbral en§3, pues para T muy pequeño k<5 no se aplicaría el lema. Esto no limita el teorema asintótico: T_c se puede aumentar a1.

Paridad y cancelación de ambos momentos exponenciales proceden del polinomio P(±1/2)=0 y de las derivadas nulas al borde. Por tanto Q_T=a_T en estos tests sin término polar omitido.

## 5. Cota para la familia REAL de P47

El paso6 de la prueba de thm:margin acota la SUMA ABSOLUTA de contribuciones de ceros para el F de lem:testfam. Luego también acota |a_T(F)|, no sólo un ínfimo. El paso7 divide por el límite inferior de ||F||². Cor:margin1 optimiza justamente k=ceil(21T/e). Por tanto es válido transportar de esa prueba, como input CITED,

    |Q_T(F_T)|/||F_T||²≤4·10⁹ T exp(−15.449T).

No se obtiene esta afirmación sólo del enunciado λ_A≤…; la comprobación de la prueba evita esa inferencia inválida. No se reauditan aquí los certificados externos Z1/Z2 del paper.

Con ||F_T||²=O(T^(3/2)) y la respuesta de U≥const·T² resulta

    |Q_T(F_T)|/||U_TF_T||²
      =O(T^(1/2)exp(−15.449T))→0.

Es válido usar valor absoluto gracias al paso6; no se presupone Q_T≥0.

## 6. Cuantificadores y core

La convergencia de M/T y todas las cotas son para TODO T suficientemente grande, no únicamente una sucesión, porque k~T y las estimaciones son uniformes para k grande. Por tanto cada c>0 fija falla en todas las ventanas T≥T_c sobre la familia dada.

Para cada T con violación estricta, aproximar F_T en H¹ por funciones pares C_c∞ y corregir su momento cosh mantiene la desigualdad por continuidad de Q_T en H¹ y de U_T en L². No se necesita una aproximación uniforme simultánea en todas las ventanas.

Una dominación hipotética con c(T)>0 obligaría a c(T)≤O(T^(1/2)exp(−15.449T)) en estos tests. Esa condición necesaria no prueba existencia ni imposibilidad de tales escalas. Tampoco descarta mapas distintos o un enlace que cambie realmente de clase.

**Resultado final:** toda escala universal positiva de U011 descartada, con fuente CITED claramente delimitada. −R y sus identidades siguen válidos. D íntegro permanece OPEN y activo; este resultado sólo cierra esa familia de dominaciones del mapa concreto.
