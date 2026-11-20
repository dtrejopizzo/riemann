# Signo negativo de la media cribada en intervalos relativos decrecientes

Fijar D≥2 y A>0. Sea φ suave, no negativa, de integral uno y soporte compacto en (0,1). Para casi todo t fijo en [1,2], L=log x y δ=L^(−A), el saldo cribado exacto de 310 satisface

    ∫₀¹ φ(u) S_D(x(1+δu),t) du  ∼  −c_(D,t) √x/L^(3/2),    c_(D,t)>0.

En particular en cada intervalo [x,x+x/(log x)^A], para x suficientemente grande, hay una escala donde S_D es negativo de módulo ≫_(D,t)√x/L^(3/2). No se requiere RH ni hay uniformidad afirmada para D creciente. Se estima el signo de la media con sus dilataciones, no el signo puntual de B_t.

**Positividad del factor de criba en la semirrecta.** La serie de coeficientes cuyo sumatorio es S_D es E(s)=D_t(s)ζ(s)² h_D(s), en notación de 306 y 310. Para s real positivo el polinomio h_D(s) es estrictamente positivo. Tomar variables de Bernoulli independientes X_p, p≤D, de probabilidades q_p=p^(−s)(2−p^(−s)). Por la fórmula de mcm de 310,

    h_D(s)=E[(Σ_(d≤D) μ(d)∏_(p|d)X_p)²].

Cuando todas las variables valen cero, el cuadrado vale uno y el suceso tiene probabilidad positiva. Esto evita una posible anulación o inversión de signo por la criba.

**Tres puntos de ramificación.** Aplicar la extracción de segundo grado de 307. La multiplicación por ζ(s)² ya ha quitado el denominador de primer grado, y los factores L(s±it,χ) son enteros. Los factores no enteros restantes son ζ(2s)^(−1/2) y [ζ(2s−2it)ζ(2s+2it)]^(−3/4). En s₀=1/2, E(s)=(s−s₀)^(1/2)(K+O(s−s₀)), con K>0 para las frecuencias consideradas. En efecto, a la derecha sobre la recta real los factores conjugados se agrupan en módulos positivos; se excluyen los t donde L(1/2+it,χ) o algún numerador local finito se anula. Sólo pueden intervenir p≤4 en esa última exclusión. Las demás unidades son no nulas en s₀ y h_D(s₀)>0. En s±=1/2±it la expansión es (s−s±)^(3/4) por un factor analítico, posiblemente nulo. El resto de Euler con los primos pequeños ajustados es holomorfo y acotado en las franjas cerradas usadas de Re s>1/3.

**Inversión con la ventana decreciente.** En Mellin el núcleo que multiplica E(s)x^s es

    Wδ(s)=s^(−1)∫ φ(u)(1+δu)^s du.

La inversión desde Re s=2 sigue por Perron suavizado. En una franja acotada y para |Im s|≥1, integrar por partes N veces da |Wδ(s)|≪_N (1+|Im s|)^(−1)(1+δ|Im s|)^(−N). En entornos fijos de los tres puntos la función y sus primeras derivadas están acotadas uniformemente, y Wδ(1/2)→2. Desplazar inicialmente a 1/2+1/L, sin cruzar singularidades. Allí E(s) crece a lo sumo como L^C(2+|Im s|)^C, por los factores extraídos, los límites absolutos para los recíprocos de ζ a la derecha de 1 y el crecimiento polinómico de las L. Tomar T=L^B, B>A+2 fijo y N suficientemente grande para que la cola sea O(√x/L³).

En |Im s|≤T desplazar a 1/2−c/log(T+3), con cortes horizontales a la izquierda de los tres puntos. La región clásica libre de ceros de ζ, con c reducido, permite las tres ramas. En las partes exteriores a vecindades de los puntos, los factores y recíprocos son a lo sumo polinómicos en T (para las potencias reales basta acotar sus módulos); cerca de los puntos se usan las expansiones locales. La ganancia exp(−cL/log(T+3)) absorbe las potencias de T en el borde izquierdo; en los bordes horizontales basta aumentar N. En cada corte la discontinuidad de (s−s_j)^ν integrada contra x^s aporta x^(s_j)L^(−1−ν)/Γ(−ν) por unidad de coeficiente constante: parametrizar s=s_j−v y usar ∫₀^∞ exp(−Lv)v^ν dv=Γ(1+ν)L^(−1−ν) y la reflexión de Γ. El error del factor analítico lineal cuesta una potencia adicional de L, uniformemente en δ. Por tanto los puntos no reales cuestan O(√x/L^(7/4)), mientras el real da K Wδ(1/2)√x/[Γ(−1/2)L^(3/2)]. Como Γ(−1/2)=−2√π, queda c_(D,t)=K/√π.

**Implicación para la ruta.** Este signo demuestra cancelación aritmética en la media positiva de dilataciones con criba fija, incluso al localizar la escala en intervalos relativos cada vez menores. Extraer sólo la muestra n=1 exige controlar el resto de las dilataciones y la dependencia en D; el cálculo de la rama real no resuelve esas dos cuestiones.
