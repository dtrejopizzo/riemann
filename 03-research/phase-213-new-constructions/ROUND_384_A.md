# Inversión de signo del sector con un único primo macroscópico

**Estado: PROVED, con revisión independiente de los momentos congelados, la sustitución PNT y la inversión de signo.**

Sean z=L², L=log x, E=∏_{p≤z}(1−1/p)^−1 y J=exp(1/8). Para 1/2<θ<1 fijo, la contribución V_θ a S de 368 de los enteros con exactamente un primo mayor que x^θ satisface

    V_θ ∼ +J x E/L².

El signo es opuesto al obtenido en 379 para el umbral exp(L^a), a<1 fijo. No hay uniformidad al pasar de uno a otro régimen. 302 trata otro coeficiente y agrupación.

**Congelar la criba.** Sea f(u)=S^*(exp u;z) manteniendo z fijo a su valor en x. Se tiene |f(u)|+|f'(u)|≪exp u por el conteo gaussiano en bandas, y ambos decaen gaussianamente para u<−1 (en la suma n≥1). Salvo O_θ(x exp(−c_θ L²)), V_θ=−Σ_{p>x^θ}f(L−log p). Las duplicaciones o los múltiplos de p² en esta expansión tienen n≥x^(2θ), con multiplicidad O(log(2n)); se absorben por la cola gaussiana. Igualmente se puede cortar p en x². El PNT reemplaza esta suma por su integral con densidad dt/log t, con error O_θ(x L exp(−c_θ√L)): integración por partes, usando |π(t)−li(t)|≪t exp(−c_θ√L), y la cota para f y f' recién dada. Completando la cola t>x² se obtiene

    V_θ=−x ∫_{−∞}^((1−θ)L) exp(−u)f(u)/(L−u) du + o(x/L²).

**Dos momentos exactos.** Para u≥L^(1/10) se tiene |f(u)|≪exp(u−c u/log u) uniformemente. Es el contorno de 377 con escala exp u, altura 2√u y desplazamiento c₀/log u: aquí log z=2log L≤20log u, por lo que z^(c₀/log u) es acotada, log E_z(1−c₀/log u)≪log log z y el resto de sus estimaciones se aplica sin alteración. En particular se pueden completar los momentos de órdenes cero y uno por encima de (1−θ)L con error superpolinomial en L. Para z congelado, la transformada bilateral ∫ exp(−su) f(u)du, primero en s>1 real, es exp((s−1/2)²/2)E_z(s)/ζ(s). Su valor y su derivada por la derecha en 1 dan

    ∫ exp(−u) f(u) du=0,     ∫ u exp(−u) f(u) du=−JE.

El paso al límite se justifica por la cota precedente y la cola negativa. La identidad 1/(L−u)=1/L+u/L²+u²/[L²(L−u)] tiene resto integrado en módulo O_θ(L^(3/10)/L³): usar L−u≥θL, la cota absoluta elemental hasta u=L^(1/10) y la exponencial después. Así el primer término desaparece exactamente y el segundo, junto con el menos del primo marcado, da el signo positivo y el equivalente.

**Registro de revisión.** En la expansión por el primo marcado, todo término repetido o con dos marcas posibles tiene n≥x^(2θ), y el número de marcas está acotado por O_θ(log(2n)); la suma gaussiana de esa cola es O_θ(x exp(−c_θL²)). Para el PNT se integra la función suave f(L−log t), no una criba que varíe con t: z está congelado. Las cotas t|f(L−log t)|≤Cx y |f'|≤C exp u dan el coste xL exp(−c_θ sqrt L), incluidos ambos bordes del intervalo[x^θ,x²].

El contorno para u≥L^(1/10) es uniforme: log z≤20log u implica p^(c₀/log u)≤exp(20c₀) para p≤z, y log log z≤log log u+O(1). Así sus factores finitos son absorbidos por el ahorro u/log u, con constantes independientes de L y u en ese rango. Esta cota y la cola negativa gaussiana permiten diferenciar la transformada en s=1 por convergencia dominada. Puesto que (1/ζ)'(1)=1, el primer momento es −JE, no +JE. El resto del desarrollo del denominador tiene módulo O_θ(L^(−27/10)), y los momentos truncados difieren de los completos por menos que cualquier potencia negativa de L. El menos del primo marcado convierte por tanto el primer momento negativo en +JxE/L². No se afirma uniformidad cuando θ tiende a1/2 o a1.

Por 377, los enteros sin primo mayor que x^θ tienen saldo ∼−JxE/L² (dos o más son aquí despreciables). El resultado identifica cancelación entre dos sectores en cada escala grande; el signo de la suma completa requiere precisión mayor.
