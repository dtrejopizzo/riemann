# Positividad simultánea de todos los momentos logarítmicos hasta s=9·10^24

Sea P(s)=Σ_p(log p)p^(−s), K(s)=2(s−1)/(s(s+1)(s+2)) y F=KP, como en 247. Con Z1–Z3 y 248, para todo entero n≥0 y todo real 1/2<s≤S=(3·10¹²)² se tiene (−1)^n F^(n)(s)>0. Para s>1 esto certifica sobre los primos genuinos el signo de la integral completa

    ∫₀^∞ C(exp t)t^n exp(−st)dt.

Para 1/2<s≤1 se habla de la continuación analítica. El enunciado no requiere convergencia de esas integrales allí. A diferencia de 245–246, son los momentos de un único baricentro fijo con independencia entre s y n.

**El ancla S.** Para G=3·10¹² y todo cero ρ se tiene |S−ρ|≥S−1/2. En la banda verificada lo da Z2; en la cola vale |S−ρ|²≥(S−1)²+G²>(S−1/2)². Esto explica por qué se puede obtener toda una familia infinita a partir de una verificación finita.

Cuando n≤30S, la integral en t≤46 es no negativa por 248 (en [1,3] para la variable x se ve directamente por el primo 2). En [34,35] aporta al menos 0.035·34^n exp(−35S). En t>46, |C(exp t)|≤2exp(t) por θ(x)≤2x. Usando log(t/46)≤(t−46)/46, esa cola cuesta a lo sumo 2·46^n exp(−46(S−1))/(S−1−n/46). La razón al piso positivo es menor que uno, pues 30 log(46/34)<10 y queda por lo menos exp(−S+46) antes del prefactor 2/[0.035(S−1−n/46)].

**Momentos altos.** Para n≥30S normalizar por (S−1/2)^(n+1)/n! y poner u=(n+1)/S. En la fórmula de 248 el término principal de cuadrados da 4/15. Un término x^z pasa al factor [(S−1/2)/(S−z)]^(n+1), también para exponentes complejos. Las sumas se pueden integrar término a término en S por convergencia absoluta. El error 50 para J_d de 248 vale incluso para y≥1: los techos allí dados suman a lo sumo 20+20·0.048+7 log(2π)+20 log 2<50. Por tanto:
 
* La suma de ceros de J_1 cuesta <0.095 por la distancia del ancla y el presupuesto 0.094+2.01·6.4·10^(−12) de 248.
* Para J_2, los ceros bajos de exponente ρ/2 tienen parte real 1/4, con coste ≤0.235 exp(−u/4); los altos cuestan ≤5·6.4·10^(−12). Los dos errores acotados cuestan ≤100 exp(−u/2).
* Para los exponentes primos impares retirados basta su techo unilateral de 248. El coste es ≤(2/3)[exp(−u/6)+exp(−3u/10)+(u/log 2) exp(−5u/14)]. En efecto, para z=1/3,1/5,1/7 el factor real se acota por exp(−(1/2−z)u); para el término log x aparece además (n+1)/(S−1/7)≤2u.

Para u≥30 todos estos techos decrecen y su suma es <0.102. El momento normalizado supera por tanto 0.16 para n≥30S.

**Propagación.** En el disco abierto |s−S|<S−1/2, la identidad P=−ζ'/ζ−Σ_{p,k≥2}(log p)p^(−ks) da continuación meromorfa; el doble sumatorio converge localmente en absoluto. No hay ceros de ζ dentro y K cancela el polo en 1. Por Taylor alrededor de S, cada derivada alternada en un real entre 1/2 y S es una suma con coeficientes positivos de las derivadas alternadas del ancla. Esto concluye todos los órdenes estrictamente.

**Relación precisa con el cierre.** Bastaría demostrar la misma positividad simultánea en anclas reales arbitrariamente grandes. En efecto, para s→∞ y n=floor(st₀) con t₀>0 fijo, la integral multiplicada por s^(n+1)/n! converge a C(exp t₀): el peso es una densidad gamma con media (n+1)/s→t₀ y varianza (n+1)/s²→0. La continuidad y el crecimiento |C(exp t)|≤2exp t permiten el paso al límite (el segundo momento exponencial está uniformemente acotado). Saldría C(x)≥0 en todo x y se aplica 247. Recíprocamente bajo RH el margen de 248 se prolonga a todo x≥10^20 usando la cota de todos los ceros sobre la línea de 247 en la misma fórmula explícita de 248: el término creciente 2.01·6.4·10^(−12)√x desaparece y la suma global |ρ|^(−2)<0.047 cubre toda la serie. La parte finita ya está certificada. Así la obligación de anclas no acotadas sí es equivalente al signo global.

**Cotejo.** 129–134 ya usaron inversión factorial y 247–248 ya obtuvieron el baricentro y la altura de control. La novedad de esta combinación es la prueba incondicional en TODOS los órdenes en una franja explícita de s. Se conserva la normalización logarítmica de los momentos. La barrera de esta prueba es la desigualdad de distancias para ceros de altura mayor que G cuando se desplaza el ancla hacia la derecha.
