# Frente vivo y plan de reinicio

## Regla rectora corregida

Ningún enunciado será descartado, rebajado o evitado por tener fuerza-RH. Si un enunciado verdadero es
equivalente a RH y aparece como obligación necesaria, entonces ése es precisamente el teorema que el
programa debe demostrar. La etiqueta **FUERZA-RH** es una marca de prioridad y carga matemática, no un
veto.

La única distinción que se conserva es lógica:

- un enunciado falso debe corregirse o reemplazarse;
- un enunciado de fuerza-RH debe atacarse hasta obtener una prueba;
- una equivalencia con RH puede usarse como conclusión o como cambio de coordenadas, pero no como
  hipótesis sin prueba independiente;
- una prueba independiente puede demostrar un criterio equivalente a RH desde datos Euler--Gamma,
  geométricos u operatoriales: hacerlo cuenta como demostrar RH y es el objetivo del proyecto.

Por tanto, expresiones como “esto contiene toda la fuerza de RH” no cierran una ruta. Identifican el
punto en el que debe crearse la matemática nueva.

## Lista canónica de obligaciones para cerrar \(\Omega_7\)

### Criterio de cierre

\(\Omega_7\) quedará cerrado únicamente cuando exista una demostración completa de

\[
   \lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}\ge0
   \qquad\text{para todo }n\ge1,
\]

con la parte prima definida mediante su continuación pareada, y cuando el teorema de Li permita concluir
RH sin ninguna hipótesis abierta intermedia. No alcanza una verificación finita, una identidad
condicional, una estimación numérica o una cadena que todavía contenga una obligación sin demostrar.

La lista se divide en un **tronco obligatorio**, que toda prueba debe cerrar, y dos **carriles de
construcción**. Basta completar íntegramente uno de los carriles; no es necesario cerrar LP+IDENT si el
ataque directo de Li produce la desigualdad global.

### Tronco obligatorio

1. **Fijar el blanco exacto. — CERRADO.**
   
   Demostrar y usar exclusivamente
   \[
      \Omega_7
      \Longleftrightarrow
      \lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}
      \quad(n\ge1).
   \]
   La cota absoluta de la parte prima es sólo una estrategia suficiente para ciertos índices, no el
   blanco lógico.

2. **Fijar la continuación aritmética. — CERRADO.**
   
   Mantener unidos el polo y la suma prima:
   \[
   \lambda_n^{\rm prime}
   =\lim_{\varepsilon\downarrow0}
   \left[
   \sum_{k=1}^n\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
   -\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
    L_{n-1}^{(1)}(\log m)
   \right].
   \]
   Ninguna prueba puede separar en el borde dos series divergentes y estimarlas por separado.

3. **Cerrar la identidad de integración por partes con su borde. — CERRADO.**
   
   Con
   \(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), usar
   \[
   \lambda_n^{\rm prime}
   =\lim_{\varepsilon\downarrow0}
   \left[-n+\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right]
   =\lim_{\varepsilon\downarrow0}
   \int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
   \]

4. **Separar rigurosamente el rango finito excepcional. — CERRADO.**
   
   Ya está demostrado que
   \[
      \lambda_n^{\rm arch}<0\iff1\le n\le7.
   \]
   Además, el certificado finito
   `fragments/OMEGA7_POINT4_FINITE_CERTIFICATE.md` demuestra con intervalos racionales que
   \[
      \lambda_n>0,\qquad 1\le n\le7,
   \]
   usando sólo el desarrollo de Laurent de \(\zeta\) en \(1\), la parte Euler--Gamma y aritmética
   racional de intervalos. Este bloque es finito y no contiene el problema asintótico.

5. **Probar la desigualdad firmada global. — ABIERTO / REDUCIDO A A1 / FUERZA-RH.**
   
   Para todo \(n\ge8\), demostrar
   \[
      \boxed{
      \lim_{\varepsilon\downarrow0}
      \int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
      \ge-\lambda_n^{\rm arch}}
   \]
   desde datos aritméticos. En phase 102 la cola uniforme A0 quedó cerrada, de modo que este punto se
   reduce al núcleo compacto firmado A1:
   \[
      -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
      \ge -{3\over4}\lambda_n^{\rm arch}
      \qquad(n\ge8).
   \]
   Su fuerza-RH no autoriza suspenderlo: obliga a encontrar una identidad, desigualdad unilateral,
   principio variacional o estructura geométrica que lo demuestre.

6. **Justificar uniformemente el límite de borde. — REDUCIDO.**
   
   La cola uniforme A0 da una cota independiente de \(\varepsilon\in[0,1]\). En el núcleo compacto
   \([1,e^{T_n}]\), \(f'_{n,\varepsilon}\to f'_{n,0}\) uniformemente. Por tanto el límite de borde queda
   reducido a A1 y ya no es una obstrucción separada.

7. **Controlar todas las escalas de \(n\). — REDUCIDO.**
   
   La prueba debe cubrir simultáneamente:
   
   - el rango finito posterior a \(I_-\);
   - la zona de transición del kernel Laguerre;
   - el régimen oscilatorio \(\log m\lesssim4n\);
   - la cola \(\log m\gtrsim4n\);
   - el límite \(n\to\infty\).
   
   A0 controla la cola \(u=\log y\ge T_n\) para cada \(n\ge8\). Las demás escalas permanecen dentro del
   núcleo compacto A1. Por tanto el control global de escalas se reduce a una sola desigualdad firmada
   uniforme en \(n\).

8. **Conservar el signo antes de estimar. — ABIERTO.**
   
   Debe construirse un pareamiento o una descomposición para la cual la excursión negativa sea visible
   sin aplicar
   \[
      \left|\int gh\right|\le\int|g||h|.
   \]
   El objeto buscado debe retener conjuntamente polo, Gamma, primos, conjugación y borde. La pérdida de
   signo por shells o por primos individuales no puede recuperarse después.

9. **Probar el mecanismo discriminante desde datos aritméticos. — FORMULADO / FUERZA-RH.**
   
   Sea cual sea la forma elegida en los puntos 5--8, sus hipótesis deben demostrarse para \(\zeta\)
   desde una construcción independiente. No basta definir una métrica, medida, corriente o
   factorización que exista exactamente cuando \(\lambda_n\ge0\). Si el mecanismo mismo equivale a RH,
   debe ser demostrado: no será descartado por esa equivalencia. Phase 102 formula el discriminante
   como la parte de A1 que debe fallar para un control tipado fuera de línea.

10. **Demostrar sensibilidad fuera de línea dentro de una clase tipada. — CONTROL DE VALIDEZ ABIERTO.**
    
    Construir una clase \(\mathcal C_{\rm Euler}\) con datos de Dirichlet, factor Gamma, ecuación
    funcional y continuación comunes. El nuevo mecanismo debe:
    
    - funcionar para los datos de \(\zeta\);
    - ser compatible con un control sobre la línea;
    - fallar estructuralmente para un miembro aritmético fuera de línea.
    
    Este punto no es una premisa lógica del criterio de Li y no debe insertarse artificialmente en la
    demostración. Es un control de validez del mecanismo: impide invertir el programa en una identidad
    incapaz de distinguir el fenómeno buscado.

11. **Cerrar el ensamblaje Li. — CERRADO CONDICIONALMENTE, dependiente de A1.**
    
    El ensamblaje está escrito en phase 102: el certificado \(1\le n\le7\), A0, el límite de borde y A1
    implican \(\lambda_n\ge0\) para todo \(n\); entonces Li da RH. El paso es condicional porque A1 sigue
    abierto.

### Carril A — construcción directa Euler--Gamma/Laguerre

Éste es el carril prioritario. Para completar el punto 5 debe cerrar, en este orden:

12. **Encontrar una unidad firmada elemental. — ABIERTO.**
    
    Identificar bloques de primos o intervalos de \(\log m\) cuyo aporte combinado con el polo y Gamma
    tenga una cota inferior, aunque cada término por separado cambie de signo.

    El triage actualizado está en `fragments/OMEGA7_CARRIL_A_FIRST_TARGET.md`: no se encontró una
    unidad local sana; la unidad canónica mínima es global, polo continuo contra todos los prime powers.
    Por eso el primer blanco técnico queda separado como A0, una cola uniforme incondicional, y A1, el
    núcleo firmado de fuerza-RH.

13. **Probar una ley de compensación global. — ABIERTO / FUERZA-RH.**
    
    Construir una involución, coborde, identidad funcional, desigualdad de energía o principio
    variacional que sume esas unidades antes de tomar magnitudes y produzca exactamente la cota del
    punto 5.

14. **Cerrar el error de truncación firmado. — CERRADO PARA LA COLA A0.**
    
    Para la truncación \(X=e^{T_n}\), A0 demuestra una cola absoluta menor que
    \({1\over4}\lambda_n^{\rm arch}\), uniforme en \(\varepsilon\). No cierra el núcleo A1.

15. **Cerrar la uniformidad \((n,\varepsilon,X)\). — REDUCIDO.**
    
    El orden queda fijado por \(n\), luego \(T_n\), luego \(\varepsilon\downarrow0\), con A0 controlando
    la cola. La uniformidad restante es exactamente la desigualdad A1 para todo \(n\ge8\).

16. **Convertir el mecanismo en el teorema global del punto 5. — ABIERTO.**
    
    El resultado final del carril no debe ser una nueva coordenada: debe entregar literalmente
    \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\) para todo \(n\ge8\).

#### Blanco global Toeplitz/Fejer agregado en phase 102

La puerta Toeplitz se refinó a su forma trigonométrica exacta:

\[
   \sum_{j,k=0}^{N}c_j\overline{c_k}\,m_{j-k}^{\rm EG}\ge0
   \qquad(N\ge0,\ c\in\mathbb C^{N+1}).
\]

Equivale a demostrar que el funcional de momentos Euler--Gamma es no negativo sobre todo cuadrado
trigonométrico
\[
   \left|\sum_{j=0}^{N}c_j\zeta^j\right|^2.
\]

Los núcleos de Fejer sin traslado y los cuadrados de Dirichlet con coeficientes fijos son pruebas
necesarias, pero no sustituyen a la positividad Toeplitz completa. En cambio, la positividad de todos
los promedios Fejer trasladados
\[
   \sum_{|k|<N}\left(1-\frac{|k|}{N}\right)m_k^{\rm EG}e^{ik\theta}\ge0
   \qquad(N\ge1,\ \theta\in\mathbb R)
\]
es equivalente a la positividad Toeplitz infinita por medidas de Cesaro positivas. El blanco válido es
esta positividad completa, o equivalentemente todos los cuadrados trigonométricos, junto con la
identificación no circular de las singularidades con el divisor transformado.

También quedó aislado un blanco de margen Schur--Toeplitz:
\[
   \lambda_n={1\over2}Q_n(1-z^n),\qquad
   Q_n(1-z^n)\ge\lambda_n^{\rm arch}\quad(n\ge8),
\]
o más fuerte \(\sigma_n\ge\lambda_n^{\rm arch}\). Junto con A0, ese margen implicaría A1.

La forma Abel/Poisson equivalente es:
\[
   \Re H_{\rm EG}(z)\ge0\qquad(|z|<1).
\]
Esta es la versión Carathéodory del mismo blanco: si se prueba para el objeto Euler--Gamma completado
y sus singularidades se identifican no circularmente con \(w_\rho=1-1/\rho\), entonces la medida de
Herglotz queda en \(\partial\mathbb D\), se obtiene RH y por Li se cierra \(\Omega_7\).
Para el ensamblaje compacto A1 se necesita además el margen Toeplitz
\(Q_n(1-z^n)\ge\lambda_n^{\rm arch}\) para \(n\ge8\).
Los documentos `165_POISSON_CARATHEODORY_POSITIVITY_GATE.md` y
`166_POISSON_CARATHEODORY_SUPPORT_GATE.md` registran, respectivamente, la
forma Abel/Poisson y el no-go de singularidades interiores.

Corrección esencial: el objeto no puede ser una medida finita ingenua que coloque masa unitaria en
todos los ceros. Una medida finita tiene momentos acotados, mientras que la fórmula de Li usa un
divisor infinito definido por emparejamiento y sustracción. Por tanto el primer blanco de esta ruta es
construir el objeto positivo Euler--Gamma renormalizado: medida finita con operador de recuperación,
corriente positiva substraída, o forma de Hilbert sobre polinomios que se anulan en el punto de
renormalización. Esta corrección quedó registrada en
`167_LI_MOMENT_RENORMALIZATION_OBSTRUCTION.md`.

El blanco renormalizado más concreto quedó escrito en
`168_RENORMALIZED_VANISHING_TEST_KERNEL_TARGET.md`: construir una forma positiva
\[
   \mathfrak Q_{\rm EG}:(z-1)\mathbb C[z]\times(z-1)\mathbb C[z]\to\mathbb C
\]
tal que
\[
   \mathfrak Q_{\rm EG}(1-z^n,1-z^n)=2\lambda_n,
\]
o con el margen más fuerte requerido por A1. En el modelo de línea crítica esta forma es
\(\sum_\rho |p(w_\rho)|^2\), que converge para \(p(1)=0\); la obligación abierta es construirla desde
Euler--Gamma sin asumir \(|w_\rho|=1\).

La normalización algebraica explícita de ese kernel es
\[
   K(j,k)=\lambda_j+\lambda_k-\lambda_{|j-k|}.
\]
Probar \(K\ge0\) para todos los bloques finitos daría Li por la diagonal \(K(n,n)=2\lambda_n\). Esta
ruta quedó registrada en `169_LI_SCHOENBERG_VANISHING_KERNEL.md`; sigue abierta porque la derivación
positiva usual usa \(\overline{w_\rho}=w_\rho^{-1}\), que es precisamente soporte crítico.

La revisión local del emparejamiento de la ecuación funcional quedó registrada en
`170_VANISHING_KERNEL_PAIRING_NO_GO.md`. En coordenada Li, la involución es
\[
   w\mapsto {1\over\overline w}.
\]
El emparejamiento cruzado que recupera exactamente Li sobre un par no fijo tiene matriz local
\[
   \begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
por lo que es indefinido fuera de \(|w|=1\). Por tanto la forma positiva buscada no puede ser ese
emparejamiento directo: debe aportar términos Euler--Gamma positivos nuevos, probar directamente la
positividad de Schoenberg, o demostrar primero el soporte crítico.

Además, `171_LOCAL_COUNTERTERM_RIGIDITY_NO_GO.md` descarta la reparación local más simple: en una
órbita no fija, los valores de \(1-z\) y \(1-z^2\) ya generan \(\mathbb C^2\). Cualquier contratérmino
positivo local que preserve todos los valores Li \(1-z^n\) debe anularse en una base y por tanto ser
cero. La misma rigidez por Cauchy--Schwarz descarta todo contratérmino positivo global invisible en
las diagonales \(Q(1-z^n)=2\lambda_n\). La reparación, si existe, debe construir una forma positiva
Li-normalizada desde el inicio, reorganizar signos globalmente, probar Schoenberg directamente o
probar primero soporte crítico.

La positividad de Schoenberg se redujo además a una puerta Toeplitz de incrementos en
`172_SCHOENBERG_INCREMENT_TOEPLITZ_GATE.md`. Definiendo
\[
   g_0=2\lambda_1,\qquad
   g_m=\lambda_{m+1}-2\lambda_m+\lambda_{m-1}\quad(m\ge1),
\]
se tiene
\[
   [\lambda_j+\lambda_k-\lambda_{|j-k|}]_{1\le j,k\le N}\ge0
   \Longleftrightarrow
   [g_{|j-k|}]_{1\le j,k\le N}\ge0
\]
para todo \(N\). El generador unilateral es
\[
   \mathcal G_+(z)=\lambda_1+{(1-z)^2\over z}\mathcal L(z).
\]
Este es ahora un blanco positivo-definido exacto para las segundas diferencias de Li.

La interpretación cero-lateral de esta puerta quedó en
`173_WEIGHTED_ZERO_DIVISOR_MEASURE_GATE.md`: si \(|w_\rho|=1\), entonces
\[
   g_m=\sum_\rho |1-w_\rho|^2w_\rho^m.
\]
El peso \(|1-w_\rho|^2\sim|\rho|^{-2}\) hace finita la masa del divisor y corrige la obstrucción de
medida finita. La obligación abierta es demostrar esa positividad de momentos ponderados desde el
objeto Euler--Gamma completado, sin asumir previamente soporte en \(\partial\mathbb D\).

La misma puerta tiene una forma de semiplano especialmente compacta, registrada en
`174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md`:
\[
   [g_{|j-k|}]\ge0\ \forall N
   \Longleftrightarrow
   \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2).
\]
Esto se debe a que
\[
   \mathcal G_+(z)=\lambda_1+{(1-z)^2\over z}\mathcal L(z)
   =
   \lambda_1+{\xi'\over\xi}\!\left({1\over1-z}\right),
\]
y la función de Carathéodory correspondiente es
\[
   2{\xi'\over\xi}\!\left({1\over1-z}\right).
\]
Probar esa positividad real excluiría polos interiores, por tanto ceros con \(\Re s>1/2\), y por la
ecuación funcional cerraría RH y \(\Omega_7\). Sigue siendo el teorema abierto de fuerza-RH.

`175_LOG_DERIVATIVE_RH_EQUIVALENCE.md` cierra el estado lógico de esa puerta: bajo RH, el producto de
Hadamard pareado da
\[
   {\xi'\over\xi}(s)=\sum_\rho {1\over s-\rho},
\]
y cada término tiene parte real positiva cuando \(\Re s>1/2\). Por tanto
\[
   RH\Longleftrightarrow \Re{\xi'\over\xi}(s)\ge0\quad(\Re s>1/2).
\]
La puerta de semiplano es una ruta válida de cierre, pero exactamente de fuerza RH.

La misma obligación se escribió como monotonicidad horizontal en
`176_HORIZONTAL_XI_MODULUS_MONOTONICITY_GATE.md`:
\[
   \partial_\sigma\log|\xi(\sigma+it)|\ge0\qquad(\sigma>1/2).
\]
En forma Euler--Gamma esto es
\[
  \Re{1\over s}+\Re{1\over s-1}-{1\over2}\log\pi
  +{1\over2}\Re\psi\!\left({s\over2}\right)
  +\Re{\zeta'\over\zeta}(s)\ge0.
\]
En \(\sigma>1\), el último término es
\[
  -\sum_{m\ge2}{\Lambda(m)\over m^\sigma}\cos(t\log m),
\]
lo que muestra de nuevo que la prueba debe conservar el pareamiento firmado global; ni la simetría
funcional ni la subarmonicidad ordinaria dan esta monotonía horizontal.

`177_UNCONDITIONAL_SIGMA_GT_1_POSITIVITY.md` separa la parte ya cerrada:
\[
   \Re{\xi'\over\xi}(s)>0\qquad(\Re s>1).
\]
Esto se prueba por el producto de Hadamard pareado, porque todos los ceros tienen \(\Re\rho<1\). Por
tanto el blanco abierto de esta ruta es exactamente extender esa positividad al strip
\[
   {1\over2}<\Re s\le1.
\]

`178_STRIP_POISSON_BOUNDARY_NO_GO.md` audita la idea de usar Poisson en la franja. Los signos de borde
son favorables: en \(\Re s=1/2\), \(\Re(\xi'/\xi)=0\) fuera de ceros por la ecuación funcional; en
\(\Re s=1\), la parte real es no negativa por el producto de Hadamard y \(0<\Re\rho<1\). Pero aplicar
Poisson dentro de la franja exige que \(\xi'/\xi\) no tenga polos interiores, es decir, exige ya la
ausencia de ceros con \(1/2<\Re\rho<1\). La inferencia de borde sin ese dato es circular.

`179_STRIP_GREEN_POLE_DEFECT_DECOMPOSITION.md` explicita el término perdido: un cero
\(\rho=\beta+i\gamma\), \(\beta>1/2\), aporta
\[
   m\,\Re{1\over s-\rho}
   =
   m{\sigma-\beta\over(\sigma-\beta)^2+(t-\gamma)^2},
\]
que es negativo para \(\sigma<\beta\) y explota a \(-\infty\) al acercarse al polo desde la izquierda.
Toda prueba por Green/Poisson debe eliminar o dominar esos defectos; ignorarlos es asumir RH.

`180_STRIP_POISSON_KERNEL_FORMULA.md` escribe la fórmula explícita:
\[
  P_L(x,y)=
  {1\over 2L}\,
  {\sin(\pi x/L)\over\cosh(\pi y/L)-\cos(\pi x/L)}.
\]
Con \(L=1/2\), los signos de borde implican positividad interior sólo si \(\xi'/\xi\) es holomorfa en
la franja. Esa hipótesis es la ausencia de ceros con \(1/2<\Re\rho<1\), por lo que la fórmula es una
representación condicional, no un cierre.

`181_GLOBAL_POSITIVITY_VS_COMPACT_A1_MARGIN.md` separa las cargas: una prueba global de
\(\Re(\xi'/\xi)\ge0\) cierra \(\Omega_7\) vía RH y Li, pero no entrega automáticamente el presupuesto
compacto A1. Para cerrar A1 dentro de la descomposición A0/A1 hace falta además
\[
   \lambda_n\ge {1\over2}\lambda_n^{\rm arch},
\]
una cola unilateral, o una prueba directa de \(C_n(T_n)\ge0\).

`189_GLOBAL_LOG_DERIVATIVE_TO_COMPACT_A1_AUDIT.md` fija la separación exacta. Por `150`,
\[
   C_n(T_n)=\lambda_n-R_n(T_n)-{1\over4}\lambda_n^{\rm arch}.
\]
La positividad global log-derivada daría \(\lambda_n\ge0\), mientras A0 sólo da
\[
   |R_n(T_n)|\le {1\over4}\lambda_n^{\rm arch}.
\]
Con esos dos datos se obtiene como mucho
\[
   C_n(T_n)\ge -{1\over2}\lambda_n^{\rm arch},
\]
no A1. La condición exacta que conecta la ruta global con A1 es
\[
   R_n(T_n)\le\lambda_n-{1\over4}\lambda_n^{\rm arch},
\]
o, de forma suficiente, el margen fuerte
\[
   \lambda_n\ge {1\over2}\lambda_n^{\rm arch}.
\]
Así, una prueba global cierra \(\Omega_7\), pero el cierre interno de A1 exige margen, cola unilateral
o prueba compacta directa.

`192_ONE_SIDED_TAIL_FROM_GLOBAL_POSITIVITY_AUDIT.md` refina la pregunta de cola unilateral. La
desigualdad
\[
   R_n(T_n)\le\lambda_n-{1\over4}\lambda_n^{\rm arch}
\]
es equivalente, por la identidad anterior, a \(C_n(T_n)\ge0\). La positividad global
Toeplitz/Schoenberg sólo entrega \(\lambda_n\ge0\); no compara el generador completo
\(\mathcal L\) con los generadores móviles de cola \(\mathcal R_{T_n}\). En forma de margen,
escribiendo
\[
   M_n=\lambda_n-{1\over2}\lambda_n^{\rm arch},\qquad
   R_n(T_n)={1\over4}\lambda_n^{\rm arch}-\delta_n,
\]
A1 es
\[
   M_n+\delta_n\ge0.
\]
La ruta global da \(M_n\ge-\frac12\lambda_n^{\rm arch}\), y A0 sólo da \(\delta_n\ge0\) en el lado
superior de la cola. Por tanto falta un margen fuerte, una correlación cola--margen, una comparación
Loewner/Schur o una prueba compacta directa.

`195_LOEWNER_SCHUR_TAIL_COMPARISON_GATE.md` escribe esa comparación como una condición exacta de
formas. Si \(\mathfrak Q^{\mathcal L}\), \(\mathfrak Q^{\mathcal A}\) y
\(\mathfrak Q^{\mathcal R,T}\) recuperan respectivamente \(\lambda_n\),
\(\lambda_n^{\rm arch}\) y \(R_n(T)\) en el test \(1-z^n\), entonces A1 en la diagonal móvil es
\[
  \left(\mathfrak Q^{\mathcal L}
  -{1\over4}\mathfrak Q^{\mathcal A}
  -\mathfrak Q^{\mathcal R,T_n}\right)(1-z^n,1-z^n)\ge0.
\]
Una versión más fuerte sería una desigualdad Loewner en un subespacio finito que contenga \(1-z^n\).
La positividad global sólo da \(\mathfrak Q^{\mathcal L}\succeq0\); no implica formalmente
\[
  \mathfrak Q^{\mathcal L}
  -{1\over4}\mathfrak Q^{\mathcal A}
  -\mathfrak Q^{\mathcal R,T_n}\succeq0.
\]
Por tanto el teorema nuevo requerido es una comparación Loewner/Schur de cola, no mera positividad
Toeplitz global.

`199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` refina esa puerta como margen de innovación. Para
\(p_n=1-z^n\), se elige un subespacio \(U_n\) y se exige primero positividad del bloque comparativo en
\(U_n\). El margen no circular es
\[
   \inf_{u\in U_n}
   \mathfrak Q^{\mathcal C,T_n}(p_n-u,p_n-u)\ge0.
\]
Entonces se deduce \(C_n(T_n)\ge0\). El orden inverso es circular: si se calcula el complemento de
Schur después de fijar la diagonal
\[
   \mathfrak Q^{\mathcal C,T_n}(p_n,p_n)=2C_n(T_n)
\]
y se usa su signo, sólo se reescribe A1. La positividad del bloque y el margen de innovación deben
probarse antes de usar la diagonal A1.

`182_HORIZONTAL_ZERO_BARRIER_NO_GO.md` agrega la forma local de barrera para la monotonía horizontal:
si \(\rho=\beta+i\gamma\), \(\beta>1/2\), es un cero de multiplicidad \(m\), entonces sobre
\(t=\gamma\)
\[
   \partial_\sigma\log|\xi(\sigma+i\gamma)|
   =
   {m\over\sigma-\beta}+O(1),
\]
que tiende a \(-\infty\) al acercarse desde la izquierda. Por tanto simetría, subarmonicidad,
promedios de borde o correcciones acotadas no pueden probar la monotonía horizontal; la prueba debe
excluir ese cero o neutralizarlo con un mecanismo singular Euler--Gamma no circular.

La ruta de inducción compacta quedó afinada en `183_EXACT_CUMULATIVE_FORCING_REPRESENTATION.md`.
Para cutoff fijo,
\[
  C_n(T)
  =
  C_8(T)
  +
  {n(n+1)-72\over16}\Delta_8(T)
  +
  {1\over2}\sum_{k=8}^{n-1}
  \left({n(n+1)\over k(k+1)}-1\right)F_k(T).
\]
Por tanto no hace falta \(F_k(T)\ge0\) término a término; hace falta la familia exacta de
desigualdades acumuladas y luego transferir de cutoff fijo a \(T_n\).

`184_MOVING_DIAGONAL_RECURRENCE_DEFECT.md` escribe la versión directamente sobre la diagonal A0
\(C_n^\ast=C_n(T_n)\). El forcing correcto es
\[
  F_n^{\rm diag}
  =
  F_n(T_n)
  +
  n\,\Phi_{n+1}(T_n,T_{n+1})
  -
  (n+1)\Phi_{n-1}(T_{n-1},T_n),
\]
donde
\[
  \Phi_k(S,U)=
  -\int_S^U E(e^u)e^{-u}L_{k-1}^{(2)}(u)\,du.
\]
La inducción A1 puede cerrarse con una cota acumulada para \(F_n^{\rm diag}\), no sólo para el forcing
de cutoff fijo.

`185_DIAGONAL_FORCING_SINGLE_KERNEL_FORM.md` comprime ese forcing diagonal en
\[
  F_n^{\rm diag}
  =
  1+{3\over4}D_n^{\rm arch}
  +
  \int_0^\infty E(e^u)e^{-u}\mathcal K_n(u)\,du,
\]
donde \(\mathcal K_n\) es un kernel de Laguerre por tramos que combina el momento \(uL_{n-1}^{(2)}\)
y los dos defectos de transferencia. El kernel sigue siendo firmado; el blanco es una cota inferior
acumulada, no positividad término a término.

`186_CUMULATIVE_DIAGONAL_FORCING_KERNEL.md` inserta esos kernels en los pesos acumulados:
\[
  \mathcal H_n(u)=\sum_{k=8}^{n-1}
  {1\over2}\left({n(n+1)\over k(k+1)}-1\right)\mathcal K_k(u).
\]
El blanco A1 inductivo se vuelve una sola desigualdad firmada sobre \([0,T_n]\), con términos
arquimedianos explícitos. El kernel acumulado sigue oscilando; no hay positividad formal.

`187_CUMULATIVE_DIAGONAL_BALANCE_FORM.md` integra una vez ese emparejamiento acumulado. La identidad
exacta contiene el balance \(B(U)=\int_0^U E(e^v)\,dv\), un kernel de Laguerre elevado por tramos y
una suma finita de saltos firmados en los cortes \(T_j\). Por tanto el balance acumulado no da una
prueba de positividad si se omiten esos saltos; la obligación correcta es la desigualdad completa con
término de borde, integral elevado y todos los saltos.

`190_DIAGONAL_BALANCE_FINITE_CERTIFICATE.md` expande esa desigualdad usando la fórmula aritmética
exacta de \(B\). El resultado es el certificado finito
\[
  \mathcal A_n+\Pi_n+\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n(m)\ge0.
\]
Los coeficientes \(\Xi_n(m)\), el bloque de polo \(\Pi_n\) y los saltos son firmados; por tanto el
certificado es el blanco exacto, no una prueba automática.

`188_DIAGONAL_CUMULATIVE_COERCIVITY_AUDIT.md` audita la posibilidad de coercividad diagonal. Si sólo
se sabe una envolvente simétrica \(|E(e^u)|\le R(u)\), entonces
\[
   \inf_{|G|\le R}\int_0^{T_n}G(u)e^{-u}\mathcal H_n(u)\,du
   =
   -\int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du.
\]
Por tanto las cotas de tamaño de PNT no producen una ganancia coerciva oculta: o bien esa cota absoluta
entra completa en el presupuesto base-arquimediano, o bien hace falta una desigualdad aritmética
unilateral que impida la alineación de \(E\) con el signo adverso de \(\mathcal H_n\).

`191_ABSOLUTE_DIAGONAL_BUDGET_SCALE_AUDIT.md` convierte esa alternativa absoluta en una condición de
escala explícita. Definiendo
\[
   W_n(R)=\int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du,
\]
la ruta absoluta cierra sólo si
\[
   \mathcal B_n\ge W_n(R)\qquad(n\ge9).
\]
Para perfiles relativos \(R(u)=e^u\varepsilon(u)\), esto es
\[
   \mathcal B_n\ge\int_0^{T_n}\varepsilon(u)|\mathcal H_n(u)|\,du.
\]
Una refutación de escala para una clase de envelopes debe probar una cota inferior uniforme para la
masa \(L^1\) ponderada de \(\mathcal H_n\) que supere \(\mathcal B_n\); la fase todavía no contiene esa
cota, así que el teorema necesario queda aislado.

`193_WEIGHTED_L1_KERNEL_CERTIFICATE.md` convierte esa masa en un certificado finito: se parte
\([0,T_n]\) por los cortes y por los ceros de la combinación polinómica \(\mathcal H_n\), de modo que
\(W_n(R)\) queda como suma de integrales con signo fijo. El blanco uniforme de la ruta absoluta es
\[
  \sup_{n\ge9}\left(W_n(R)-\mathcal B_n\right)\le0.
\]

`201_TERMINAL_LAGUERRE_LOAD_GATE.md` aísla la condición necesaria terminal de esa ruta. Como
\(\mathcal H_n=-L_{n-1}^{(2)}\) en \((T_{n-1},T_n)\), cualquier prueba absoluta debe cumplir primero
\[
  \mathcal B_n\ge
  \int_{T_{n-1}}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du.
\]
La carga terminal se escribe exactamente partiendo por los ceros de \(L_{n-1}^{(2)}\); para envelopes
constantes se reduce a valores de borde de \(L_n^{(1)}\).

`194_STRONG_MARGIN_GENERATOR_SECOND_PASS.md` reabre el margen fuerte con el generador exacto
\[
   \mathcal M_{\rm SM}(z)=\mathcal L(z)-{1\over2}\mathcal A(z).
\]
La condición suficiente para A1 vía A0 es
\[
   [z^n]\mathcal M_{\rm SM}\ge0\qquad(n\ge8),
\]
equivalentemente
\[
   Q_n(1-z^n)\ge\lambda_n^{\rm arch}
\]
en la energía Toeplitz. La positividad global Toeplitz/Schoenberg sólo da
\(Q_n(1-z^n)\ge0\), o \(\lambda_n\ge0\); falta una comparación cuantitativa con la escala
arquimediana. La positividad de kernels, por sí sola, no impone ese margen diagonal externo.

`198_STRONG_MARGIN_SECOND_DIFFERENCE_AUDIT.md` traduce el mismo margen a las segundas diferencias
Toeplitz \(g_m\):
\[
   2\lambda_n
   =
   n g_0+2\sum_{m=1}^{n-1}(n-m)g_m.
\]
Por tanto el margen fuerte equivale a
\[
   n g_0+2\sum_{m=1}^{n-1}(n-m)g_m
   \ge \lambda_n^{\rm arch}.
\]
Si \(g_m\) tiene medida positiva \(\nu_g\), esto es
\[
   \int_{\partial\mathbb D}|1+\zeta+\cdots+\zeta^{n-1}|^2\,d\nu_g(\zeta)
   \ge \lambda_n^{\rm arch}.
\]
La positividad Toeplitz de \(g\) sólo da que esta integral es no negativa; incluso con masa total fija
puede concentrarse en raíces no triviales de orden \(n\), donde el kernel de Dirichlet se anula. Por
tanto hace falta una cota inferior Fejer/Dirichlet cuantitativa para la medida de incrementos.

`200_FEJER_MASS_STRONG_MARGIN_GATE.md` convierte esa cota en una condición local suficiente: si
\[
  \nu_g(|\theta|\le1/n)\ge{\pi^2\over4}{\lambda_n^{\rm arch}\over n^2}
\]
para todo \(n\ge8\), entonces el margen fuerte sigue. El blanco exacto sigue siendo
\[
  n\int F_n\,d\nu_g\ge\lambda_n^{\rm arch}.
\]
La positividad o la masa total de \(\nu_g\) no bastan; hace falta masa cuantitativa vista por el kernel
de Fejer en cada escala.

`202_FEJER_DENSITY_SCALE_GATE.md` audita la escala de densidad: si
\(d\nu_g=h\,dm\) y \(h\) es acotada, entonces
\[
  n\int F_n\,d\nu_g=O(n),
\]
que no domina la escala arquimediana \(n\log n\). Por tanto una ruta Fejer exitosa necesita densidad
logarítmica o más singular cerca de \(\zeta=1\), un átomo/componente singular visible por Fejer, o una
prueba compacta firmada distinta.

`203_ATOM_AT_ONE_INCOMPATIBILITY_AUDIT.md` elimina el átomo en \(\zeta=1\) como atajo compatible con
la normalización real: si \(\nu_g\{1\}=a_0>0\), entonces aporta
\(\lambda_n^{atom}=a_0n^2/2\) y fuerza un término \(a_0z/(1-z)^3\) en \(\mathcal L(z)\). Pero el
generador Euler--Gamma satisface, sobre \(z\to1^-\),
\[
  \mathcal L(z)=O\!\left((1-z)^{-2}\log {1\over1-z}\right).
\]
La concentración Fejer viable debe ser logarítmica o singular continua compatible con esa escala, no
un átomo en \(1\).

`204_LOG_DENSITY_INCREMENT_GENERATOR_GATE.md` identifica esa escala compatible en el generador de
incrementos:
\[
  \mathcal G_+(z)=\lambda_1+{\xi'\over\xi}\!\left({1\over1-z}\right).
\]
Por tanto \(\mathcal G_+(r)=O(\log(1/(1-r)))\), exactamente la escala de una densidad logarítmica
cerca de \(\zeta=1\). Esto no prueba el margen: todavía falta construir una medida positiva y una cota
inferior logarítmica, o probar directamente \(n\int F_n\,d\nu_g\ge\lambda_n^{arch}\).

`205_FEJER_LOG_CONSTANT_AUDIT.md` fija las constantes de esa puerta. Se obtiene
\[
  \lambda_n^{\rm arch}\sim {1\over2}n\log n.
\]
Si una densidad positiva tuviera \(h(\theta)\sim a\log(e/|\theta|)\), entonces la parte real Abel
tendría coeficiente \(a/2\), mientras que el promedio de Fejer tendría coeficiente \(a\). La asíntota
radial Euler--Gamma tiene coeficiente \(1/2\), compatible en el modelo puro con \(a=1\), y el margen
Fejer exacto sólo necesita constante líder \(a\ge1/2\). Por tanto no hay obstrucción de constantes en
el modelo logarítmico ideal; lo que falta sigue siendo construir la medida positiva y demostrar una
cota inferior Fejer/logarítmica no circular.

`206_FEJER_ABEL_TAUBERIAN_GAP.md` cierra la falsa transferencia Abel--Fejer: en los ceros móviles
\(\theta=2\pi k/n\), \(F_n\) se anula mientras el kernel Abel en la escala \(r=1-1/n\) sigue siendo de
tamaño \(n\). Por tanto el crecimiento radial logarítmico no implica el margen Fejer sin una cota de
anti-concentración, una densidad inferior logarítmica o una estimación directa de
\(\int F_n\,d\nu_g\).

`207_A0_TERMINAL_CUTOFF_BRIDGE_AUDIT.md` audita la ruta absoluta terminal. El corte A0 para \(n-1\)
da, con \(\varepsilon(u)=A\exp(-\eta(u))\),
\[
  \mathcal T_n(\varepsilon)
  \le
  {n^2\over12(n-1)^2}B_{n-1}
  \log {1+T_n\over1+T_{n-1}}.
\]
Así, A0 ayuda en el intervalo terminal, pero sólo con una pérdida de razón de cortes; para cerrar esa
subruta hace falta probar esa comparación contra \(\mathcal B_n\) o imponer un surplus de una potencia
en el corte. El control no terminal de \(\mathcal H_n\) se separa después en `211` y se colapsa en
`219`.

`208_VK_CUTOFF_RATIO_TERMINAL_SCALE.md` evalúa esa pérdida para cortes canónicos de
Vinogradov--Korobov:
\[
  T_n={25\over9a^{5/3}}n^{5/3}(\log n)^2(1+o(1)),
  \qquad
  \log {1+T_n\over1+T_{n-1}}
  ={5\over3n}+{2\over n\log n}+o(1/n).
\]
Por tanto la carga terminal queda en escala \((5/72)\log n+O(1)\). Esto muestra que la razón de cortes
no es una obstrucción terminal fatal bajo cortes VK mínimos, pero no cierra A1: todavía faltan una cota
inferior efectiva para \(\mathcal B_n\), los casos iniciales, y el control no terminal que se aísla en
`211`.

`209_ARCHIMEDEAN_BUDGET_SIGN_AUDIT.md` muestra que el presupuesto arquimediano de recurrencia tampoco
da una reserva positiva gratuita:
\[
  D_n^{\rm arch}=-{1\over2}\log n+O(1),
  \qquad
  1+{3\over4}D_n^{\rm arch}=1-{3\over8}\log n+O(1).
\]
Por tanto los pesos positivos \(w_{n,k}\) no bastan para asegurar
\(\mathcal B_n>0\). La ruta absoluta necesita una cota inferior para el presupuesto completo,
incluyendo \(C_8^\ast\) y \(\Delta_8^\ast\), antes de poder usar el puente terminal.

`210_BASE_BUDGET_QUADRATIC_COEFFICIENT_GATE.md` reduce la escala grande de ese presupuesto a
\[
  \mathcal B_n=\Gamma_{\mathcal B}n^2+O(n\log n),
  \qquad
  \Gamma_{\mathcal B}
  =
  {\Delta_8^\ast\over16}
  +{1\over2}\sum_{k=8}^{\infty}
  {1+\frac34D_k^{\rm arch}\over k(k+1)}.
\]
Si \(\Gamma_{\mathcal B}>0\), la carga terminal \(O(\log n)\) de cortes VK queda absorbida para
\(n\) grande; si \(\Gamma_{\mathcal B}\le0\), esa absorción no sale del presupuesto base. En cualquier
caso falta evaluar ese coeficiente y cerrar los casos finitos.

`211_MIXED_INTERVAL_OFFDIAGONAL_LOAD_GATE.md` separa la obstrucción no terminal de la ruta absoluta.
En \((T_j,T_{j+1})\), \(\mathcal H_n\) contiene
\[
  u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u),
\]
con grados que llegan hasta \(n-2\). El decaimiento A0 disponible en la escala \(T_j\) no controla
automáticamente esos grados altos. Por tanto Theorem B necesita, además del terminal y del presupuesto,
una cota uniforme de carga mixta \(L^1\), un bound off-diagonal de Laguerre, o volver a una prueba
firmada.

`212_BASE_BUDGET_TELESCOPING_REDUCTION.md` resuelve la parte infinita de
\(\Gamma_{\mathcal B}\) por telescopía:
\[
  {D_k^{\rm arch}\over k(k+1)}
  =
  {\lambda_{k+1}^{\rm arch}-\lambda_k^{\rm arch}\over k+1}
  -
  {\lambda_k^{\rm arch}-\lambda_{k-1}^{\rm arch}\over k}.
\]
Por tanto
\[
  \Gamma_{\mathcal B}
  =
  {1+\Delta_8^\ast\over16}
  -{3\over64}(\lambda_8^{\rm arch}-\lambda_7^{\rm arch}),
\]
y
\[
  \Gamma_{\mathcal B}>0
  \Longleftrightarrow
  \Delta_8^\ast>-0.7175270082\ldots .
\]
La absorción terminal asintótica queda reducida a una cota finita/base para
\(\Delta_8^\ast\). En esta etapa cronológica todavía queda abierto el control no terminal de `211`,
que se cierra estructuralmente por telescopía en `219`.

`213_GAMMA_B_COMPACT_BASE_IDENTITY.md` sustituye la definición compacta de
\(\Delta_8^\ast\) y obtiene la identidad más fuerte
\[
  \Gamma_{\mathcal B}={I_7(T_7)-I_8(T_8)\over16}.
\]
Por tanto \(\Gamma_{\mathcal B}>0\) equivale exactamente a
\[
  I_7(T_7)>I_8(T_8).
\]
La parte infinita y la diferencia arquimediana se cancelan; queda una comparación aritmética compacta
finita dependiente de los cortes base. El certificado Li finito \(1\le n\le7\) no la implica
automáticamente, porque no es una comparación compacta con el momento \(n=8\).

`214_GAMMA_B_BASE_FINITE_CERTIFICATE.md` expande esa comparación como certificado finito de prime
powers. Para \(T_8\ge T_7\),
\[
\begin{aligned}
  16\Gamma_{\mathcal B}
  &=
  \sum_{m\le e^{T_7}}\Lambda(m)
  [\Phi_7(\log m,T_7)-\Phi_8(\log m,T_8)]\\
  &\quad
  -
  \sum_{e^{T_7}<m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
  -\Psi_7(T_7)+\Psi_8(T_8),
\end{aligned}
\]
con \(\Phi_7,\Phi_8,\Psi_7,\Psi_8\) expresiones elementales de extremos. Así el caso
\(\Gamma_{\mathcal B}>0\) queda convertido en una verificación finita una vez fijados \(T_7,T_8\).

`215_BASE_CUTOFF_NORMALIZATION_GAMMA_POSITIVITY.md` usa que \(T_7\) es auxiliar, ya que A0 empieza en
\(n=8\). Si se fija
\[
  0<T_7\le\min(\log2,1/130),
\]
entonces \(I_7(T_7)>-1\). Por otro lado, la condición base ya necesaria
\[
  C_8^\ast=C_8(T_8)\ge0
\]
implica \(I_8(T_8)<-29/4\), usando \(0<\lambda_8^{\rm arch}<1\). Por tanto
\[
  C_8^\ast\ge0\Longrightarrow \Gamma_{\mathcal B}>0
\]
bajo esa normalización. El signo terminal asintótico queda absorbido por el base case \(n=8\); en esta
etapa aún quedan abiertos el certificado base \(C_8^\ast\ge0\), los casos finitos efectivos y el
control no terminal que luego colapsa `219`.

`216_BASE_C8_COMPACT_CERTIFICATE.md` expande ese certificado base:
\[
  C_8^\ast\ge0
  \Longleftrightarrow
  \Psi_8(T_8)
  -
  \sum_{m\le e^{T_8}}\Lambda(m)\Phi_8(\log m,T_8)
  \ge
  8-{3\over4}A_8.
\]
También registra una alternativa finita suficiente:
\[
  \lambda_8\ge {1\over2}A_8,
\]
pues junto con A0 implica \(C_8^\ast\ge0\). El certificado Li finito previo no cubre esto, porque
cerraba \(1\le n\le7\), no el caso compacto \(n=8\).

`217_N8_BASE_MARGIN_CERTIFICATE.md` ejecuta esa alternativa finita. El verificador racional se
extendió a \(n=8\) agregando intervalos para \(\gamma_7\) y \(\zeta(8)\), y certifica
\[
  \lambda_8-{1\over2}\lambda_8^{\rm arch}
  >
  1.455305710633246144455217.
\]
Como A0 da \(|R_8(T_8)|\le\frac14\lambda_8^{\rm arch}\), la identidad
\[
  C_8(T_8)=\lambda_8-{1\over4}\lambda_8^{\rm arch}-R_8(T_8)
\]
implica \(C_8^\ast>0\). Junto con `215`, queda cerrado el signo de
\(\Gamma_{\mathcal B}\). Sigue abierta la cota efectiva terminal finita; las cargas mixtas crudas de
`211` se colapsan exactamente en `219`, y la ruta absoluta resultante queda descartada para
envolventes VK en `221`.

`218_MIXED_A0_DEGREE_MISMATCH_AUDIT.md` muestra que la ruta mixta no se cierra reciclando A0
localmente. En \((T_j,T_{j+1})\), A0 aporta \((1+u)^{-(j+1)}\), pero el término
\(L_{k-1}^{(2)}\) del sumando off-diagonal cuesta \((1+u)^{k-1}\). Queda el factor
\[
  (1+u)^{k-j-2},
\]
positivo para \(k\ge j+3\). Por tanto la forma cruda requiere un teorema Laguerre off-diagonal,
cancelación de la mezcla acumulada o una prueba firmada; no sale de A0 más la cota elemental. La
cancelación exacta se ejecuta en `219`.

`220_TERMINAL_EFFECTIVE_THRESHOLD_REDUCTION.md` separa el último trabajo puramente terminal. Define
\[
  \mathfrak D_n=\mathcal B_n-\Theta_n,\qquad
  \Theta_n={n^2\over12(n-1)^2}B_{n-1}\log{1+T_n\over1+T_{n-1}},
\]
de modo que el intervalo terminal queda controlado exactamente por \(\mathfrak D_n\ge0\). Como `217`
y `215` dan \(\Gamma_{\mathcal B}>25/64\), mientras que la carga terminal VK canónica es
\(O(\log n)\), la obstrucción terminal asintótica queda cerrada. Lo que falta es sólo el certificado
racional finito del umbral efectivo; esto no controla por sí solo la carga colapsada de `219`.

`219_MIXED_LAGUERRE_TELESCOPING_COLLAPSE.md` elimina la obstrucción mixta en su forma cruda. Al
aplicar
\[
  uL_{k-1}^{(2)}=(k+1)L_{k-1}^{(1)}-kL_k^{(1)}
\]
los pesos cumulativos telescopan y dan
\[
  \mathcal H_n(u)=-L_{n-1}^{(2)}(u)\qquad(T_8<u<T_n).
\]
Sólo sobreviven dos correcciones de grado fijo 7 en \((0,T_7)\) y \((T_7,T_8)\). Por tanto la ruta
absoluta ya no necesita un teorema para mezclas off-diagonal arbitrarias; necesita una cota \(L^1\)
ponderada para este Laguerre único colapsado, más las dos correcciones iniciales.

`221_SINGLE_LAGUERRE_BULK_L1_OBSTRUCTION.md` muestra que la ruta absoluta colapsada no funciona con
envolventes VK. En \(u\asymp n\), Plancherel--Rotach da masa absoluta Laguerre con factor \(e^{u/2}\),
mientras VK sólo decae subexponencialmente. La carga absoluta resulta exponencial y no puede ser
absorbida por \(\mathcal B_n=O(n^2)\). Por tanto A1 debe volver a una prueba firmada, cola unilateral,
margen fuerte, comparación Loewner--Schur o semiplano global.

`222_SIGNED_BALANCE_TELESCOPED_CERTIFICATE.md` empuja el telescopaje a la ruta firmada. En la
identidad integrada sólo quedan saltos en \(T_7\) y \(T_8\); todos los saltos \(T_9,\ldots,T_{n-1}\)
se anulan. El certificado firmado queda reducido a
\[
  \mathcal A_n+\Pi_n^{\rm tel}
  +\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n^{\rm tel}(m)\ge0.
\]
Este es ahora el objetivo firmado finito más pequeño para A1.

`223_SIGNED_BALANCE_B_ENVELOPE_NO_GO.md` muestra que tampoco alcanza una cota simétrica para
\(B(U)\). Esa información vuelve a producir una carga absoluta, ahora con \(L_{n-1}^{(3)}\), y el
bulk Laguerre vence de nuevo al decaimiento VK. Por tanto la ruta firmada necesita correlación
aritmética real de signos, no sólo tamaño PNT integrado.

`224_STRONG_MARGIN_RH_STRENGTH_AUDIT.md` registra que el margen fuerte no es una mejora elemental:
junto con el certificado finito \(1\le n\le7\), implica \(\lambda_n\ge0\) para todo \(n\), luego RH
por Li. Por tanto esa ruta sigue siendo válida, pero exige información de fuerza RH.

`225_A1_POST_ABSOLUTE_ROUTE_DECISION_LEDGER.md` fija la decisión actual: la ruta absoluta VK queda
descartada. Los gates base, terminal asintótico y estructura mixta están cerrados; lo que queda es
probar el certificado firmado telescopado de `222`, o una cola unilateral, margen fuerte,
Loewner--Schur no circular, o semiplano global.

`226_DIRECT_TELESCOPED_PRIME_COEFFICIENT_CERTIFICATE.md` elimina una capa más de la ruta firmada:
en vez de usar \(B(U)\), expande directamente \(\psi(e^u)\). El objetivo equivalente queda
\[
  \mathcal A_n-P_n+\sum_{m\le e^{T_n}}\Lambda(m)\Omega_n(m)\ge0,
\]
donde \(\Omega_n(m)\) es una fórmula de extremos en \(e^{-u}L_{n-1}^{(1)}\) más correcciones de grado
7. Esta es ahora la forma firmada finita más directa.

`227_SMALL_T7_PRIME_BLOCK_ELIMINATION.md` usa la normalización estricta
\(0<T_7<\log2\): no hay primo-potencias con \(\log m<T_7\). Por tanto la suma firmada directa tiene
sólo dos bloques aritméticos: \(T_7\le\log m<T_8\) y \(T_8\le\log m\). El primer intervalo sólo queda
en el término de polo \(P_n\).

`228_HIGH_BLOCK_LAGUERRE_CORRELATION_FORM.md` aísla el bloque alto:
\[
  \mathcal P_n^{\rm high}
  =
  e^{-T_n}L_{n-1}^{(1)}(T_n)\Psi_{[T_8,T_n]}
  -
  \sum_{e^{T_8}\le m\le e^{T_n}}
  {\Lambda(m)\over m}L_{n-1}^{(1)}(\log m).
\]
La dificultad final de ese bloque es una correlación firmada entre primo-potencias y oscilaciones de
Laguerre, no una cota de tamaño para \(\psi\).

`231_HIGH_BLOCK_PARTIAL_SUMMATION_FORM.md` aplica sumación parcial:
\[
  \mathcal C_n^{\rm high}
  =
  A_8(T_n)L_{n-1}^{(1)}(T_n)
  +\int_{T_8}^{T_n}A_8(u)L_{n-2}^{(2)}(u)\,du,
\]
donde \(A_8(u)=\sum_{e^{T_8}\le m\le e^u}\Lambda(m)/m\). La dificultad equivalente es controlar de
forma firmada el error \(E_8^\sharp(u)=A_8(u)-(u-T_8)\) contra \(L_{n-2}^{(2)}\).

`232_WEIGHTED_MERTENS_ENVELOPE_NO_GO.md` muestra que una cota simétrica para
\(E_8^\sharp\) tampoco alcanza: produce una carga absoluta contra \(L_{n-2}^{(2)}\), y el bulk
Laguerre vuelve a vencer al decaimiento VK. La forma de sumación parcial exige correlación firmada.

`233_SINGLE_TRANSFORM_FIXED_CUTOFF_GENERATOR.md` empaqueta el transformado único para corte fijo:
\[
  \mathcal S_T(z)=
  {z\over(1-z)^2}\sum_{m\le e^T}{\Lambda(m)\over m^{1/(1-z)}}.
\]
Para \(T\) fijo esto da una positividad ordinaria de coeficientes; A1 sigue necesitando positividad en
la diagonal móvil \(T=T_n\).

`235_MOVING_CUTOFF_DERIVATIVE_GATE.md` calcula el gate exacto para mover el corte:
\[
  C_n'(T)=-(\psi(e^T)-e^T)e^{-T}L_{n-1}^{(2)}(T)
\]
entre saltos, y los saltos de \(\psi\) se cancelan exactamente con los de \(S_n(T)\). Por tanto una
prueba a corte fijo sólo transfiere a \(T_n\) con un teorema firmado para esa integral.

`236_SINGLE_TRANSFORM_ZERO_SIDE_MARGIN_AUDIT.md` fija la separación zero-side: de
\[
  C_n(T_n)=\lambda_n-{1\over4}\lambda_n^{\rm arch}-R_n(T_n)
\]
se ve que Li/RH por sí solo no es el enunciado compacto A1. Una fórmula explícita por ceros aún debe
probar margen fuerte, cola unilateral o un margen compacto equivalente.

`237_CUTOFF_TRANSFER_TAIL_EQUIVALENCE.md` muestra que mover positividad desde un corte fijo o desde
el corte infinito a \(T_n\) es exactamente el problema de cola unilateral/correlación firmada:
\[
  R_n(T_n)\le\lambda_n-{1\over4}\lambda_n^{\rm arch}.
\]
Las estimaciones simétricas sólo sirven si además se prueba el margen fuerte.

`238_TAIL_MARGIN_COMPENSATION_FRONTIER.md` separa el margen fuerte y la cola:
\[
  C_n(T_n)=M_n+\delta_n,\qquad
  M_n=\lambda_n-\frac12\lambda_n^{\rm arch},\quad
  \delta_n=\frac14\lambda_n^{\rm arch}-R_n(T_n)\ge0.
\]
Por tanto A1 exige que la cola aporte exactamente el superávit necesario para cubrir cualquier
déficit de margen fuerte.

`239_MARGIN_TAIL_THRESHOLD_LADDER.md` calibra el intercambio cuantitativo:
si \(\lambda_n\ge\kappa_nA_n\) y \(R_n(T_n)\le\rho_nA_n\), entonces A1 equivale a
\[
  \kappa_n-\rho_n\ge {1\over4}.
\]
A0 tiene \(\rho_n=1/4\) y por eso exige \(\kappa_n\ge1/2\); Li positividad sola
\(\kappa_n=0\) exigiría \(R_n(T_n)\le-A_n/4\).

`240_DEFICIT_RATIO_TAIL_SURPLUS_GATE.md` normaliza el mismo gate:
\[
  d_n={(-M_n)_+\over A_n},\qquad
  s_n={\delta_n\over A_n}.
\]
Entonces A1 equivale exactamente a \(s_n\ge d_n\). Esto permite auditar cualquier prueba futura por
cuánto déficit de margen fuerte cubre la cola.

`241_TAIL_SURPLUS_GENERATOR_DIAGONAL_NO_GO.md` empaqueta la cola sobrante en
\[
  \Delta_T={1\over4}\mathcal A-\mathcal R_T.
\]
A0 da \([z^n]\Delta_{T_n}\ge0\), pero eso no basta: A1 requiere la comparación diagonal
\[
  [z^n]\Delta_{T_n}\ge-[z^n]\mathcal M,\qquad
  \mathcal M=\mathcal L-\frac12\mathcal A.
\]
El flujo exacto es
\[
  {d\over dT}[z^n]\Delta_T
  =
  -E(e^T)e^{-T}L_{n-1}^{(2)}(T),
\]
la misma transferencia firmada Chebyshev--Laguerre del gate de corte móvil.

`242_LOEWNER_CONE_MARGIN_TAIL_DECOMPOSITION.md` descompone la forma comparativa:
\[
  \mathfrak Q^{\mathcal C,T}
  =
  \mathfrak Q^{\mathcal M}
  +
  \mathfrak Q^{\Delta,T},
\]
donde \(\mathfrak Q^{\mathcal M}\) es margen fuerte y
\(\mathfrak Q^{\Delta,T}\) es superávit de cola. En \(p_n=1-z^n\),
\[
  {1\over2}\mathfrak Q^{\mathcal C,T_n}(p_n,p_n)=M_n+\delta_n=C_n(T_n).
\]
Por tanto una prueba Loewner no circular debe probar dominación del cono de margen
negativo por el cono de superávit, o innovación de Schur no negativa, antes de usar
la diagonal \(2C_n(T_n)\).

`243_LOEWNER_NEGATIVE_PART_COMPENSATION_REDUCTION.md` refina la ruta por parte negativa:
\[
  \mathfrak Q^{\mathcal M}
  =
  \mathfrak Q^{\mathcal M}_+
  -
  \mathfrak Q^{\mathcal M}_-.
\]
Un cierre suficiente sería
\[
  \mathfrak Q^{\Delta,T_n}\succeq\mathfrak Q^{\mathcal M}_-
\]
en un espacio finito que contenga \(1-z^n\); sobre la recta de test vuelve a
\(\delta_n\ge-M_n\).

`244_A0_TAIL_IMPROVEMENT_REQUIREMENT.md` fija la mejora cuantitativa exacta sobre A0:
\[
  \eta_n={1\over4}-{R_n(T_n)\over A_n},\qquad
  d_n=\max\left(0,{1\over2}-{\lambda_n\over A_n}\right).
\]
A0 sólo da \(\eta_n\ge0\); A1 equivale exactamente a
\[
  \eta_n\ge d_n.
\]
En forma de cola firmada, lo que falta es
\[
  \int_{T_n}^{\infty}
    E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du
  \ge
  \left(d_n-{1\over4}\right)A_n.
\]

`245_TERMINAL_THRESHOLD_DATA_DEPENDENCE_CERTIFICATE.md` separa el chequeo terminal finito
del punto A1: la positividad asintótica de \(\mathfrak D_n\) ya está cerrada, pero un
umbral numérico \(N_0\) exige fijar política de cortes, cotas de razón, cotas para
\(B_{n-1}\), intervalos base, intervalos arquimedianos finitos y la verificación
finita de \(\mathfrak D_n\ge0\). Esto no sustituye el teorema compacto firmado.

`246_GLOBAL_HALF_PLANE_COMPACT_A1_SEPARATION.md` separa dos cierres distintos. El
teorema global de semiplano
\[
  \Re{\xi'\over\xi}(s)\ge0\qquad(\Re s>1/2)
\]
cerraría \(\Omega_7\) por RH/Li, pero para A1 compacta sólo aporta
\[
  d_n\le {1\over2},
\]
mientras A0 aporta \(s_n\ge0\). La compacidad todavía exige
\[
  s_n\ge d_n.
\]
Por tanto, si se exige cerrar A1 internamente, el teorema global debe ir acompañado
del puente margen-cola o de una prueba compacta directa.

`247_QUARTER_MARGIN_NONPOSITIVE_TAIL_GATE.md` aísla un punto suficiente de la escalera:
\[
  \lambda_n\ge {1\over4}A_n,\qquad R_n(T_n)\le0.
\]
Equivale a \(d_n\le1/4\) y \(s_n\ge1/4\), luego cierra \(s_n\ge d_n\). Es más débil
que margen fuerte, pero sigue siendo de fuerza RH y exige signo de cola no provisto por A0.

`248_QUARTER_MARGIN_GENERATOR_RH_STRENGTH_AUDIT.md` define el generador de cuarto margen:
\[
  \mathcal Q_{1/4}=\mathcal L-{1\over4}\mathcal A,
  \qquad
  [z^n]\mathcal Q_{1/4}=\lambda_n-{1\over4}A_n.
\]
Si estos coeficientes son no negativos para \(n\ge8\), entonces con el certificado finito de índices
bajos se obtiene \(\lambda_n\ge0\) para todo \(n\), luego RH por Li. Por tanto el cuarto margen es una
ruta válida pero de fuerza RH.

`249_TAIL_SIGN_LAGUERRE_ZERO_PARTITION_GATE.md` escribe \(R_n(T_n)\le0\) como una
partición por ceros de \(L_{n-1}^{(2)}\) en la cola:
\[
  \sum_j\sigma_{n,j}\mathcal E_{n,j}\ge0.
\]
A0 sólo da la cota más débil \(\sum_j\sigma_{n,j}\mathcal E_{n,j}\ge-A_n/4\).
Así, la ruta de cola no positiva necesita una compensación firmada de lóbulos, no una envolvente
simétrica.

`250_NONPOSITIVE_TAIL_SYMMETRIC_ENVELOPE_NO_GO.md` demuestra que ese signo de cola
no puede salir de una envolvente simétrica \(|E(e^u)|\le W(u)\): el funcional de cola
es impar bajo \(E\mapsto-E\), mientras la envolvente no cambia. Se necesita información
aritmética firmada.

`251_RDI_LI_COEFFICIENT_EXTRACTION_GATE.md` fija el puente literal que permitiría
reingresar el carril RDI: convergencia local uniforme, en \(s=1/(1-z)\), de
\[
  zF_N'(z)\to {z\over(1-z)^2}{\xi'\over\xi}\!\left({1\over1-z}\right)
\]
con coeficientes aproximantes no negativos, o bien convergencia local uniforme de
aproximantes reales-raíces a la \(\Xi\) verdadera. Sin uno de estos puentes, RDI sigue
siendo infraestructura y no prueba Li.

`310_REAL_RAY_CONVERGENCE_NOT_LI_COEFFICIENT_NO_GO.md` muestra por qué no
basta converger en un rayo real: \(F_N(z)=z/(1+N^2z^2)\) converge
puntualmente a \(0\) sobre el eje real, pero su coeficiente lineal es
siempre \(1\).  Sin convergencia local uniforme compleja, Cauchy no permite
pasar a coeficientes Li.

`252_SCHUR_ZERO_COUPLING_DIAGONAL_COLLAPSE.md` cierra el caso degenerado de Schur:
si el acoplamiento comparativo \(b_n\) es cero, la innovación de Schur es exactamente
\[
  d_n=2C_n(T_n).
\]
Por tanto el caso de acoplamiento cero no produce margen nuevo; vuelve a la diagonal A1.

`253_DISK_HERGLOTZ_MEASURE_HALF_PLANE_GATE.md` reescribe el teorema global de semiplano como
una representación de Herglotz:
\[
  H_\xi(z)=2{\xi'\over\xi}\!\left({1\over1-z}\right)
  =
  \int_{\partial\mathbb D}{\zeta+z\over\zeta-z}\,d\nu_\xi(\zeta),
  \qquad \nu_\xi\ge0.
\]
Construida sin usar soporte de ceros, esta medida excluye polos interiores del disco, luego ceros
fuera de la línea crítica y cierra \(\Omega_7\) por RH/Li. Construirla desde los ceros en la línea
sería circular.

`290_RADIAL_ABEL_POSITIVITY_NOT_HERGLOTZ_NO_GO.md` elimina el atajo radial:
valores positivos o crecimiento logarítmico de \(H_\xi(r)\) para \(0<r<1\)
no implican \(\Re H_\xi(z)\ge0\) en todo el disco.  El ejemplo
\(H(z)=1+3z^2\) es positivo en el radio real positivo pero falla en el
radio imaginario y en un bloque Toeplitz.  Por tanto la ruta global exige
positividad angular de Herglotz/Toeplitz, no sólo datos Abel radiales.

`300_CENTERED_FEJER_TESTS_NOT_TOEPLITZ_NO_GO.md` elimina el atajo diagonal:
hay sucesiones hermíticas con todos los tests Fejer centrados positivos
pero con un bloque Toeplitz negativo.  Por tanto la positividad de
direcciones Li \(1-z^n\) no construye la medida de Herglotz; hacen falta
todos los tests trasladados/Toeplitz.

`324_FINITE_TOEPLITZ_BLOCKS_NOT_HERGLOTZ_GATE.md` elimina el atajo de
chequeos Toeplitz finitos: para cualquier \(N\), se pueden tener todos los
bloques \(T_L\), \(L\le N\), positivos y hacer negativo \(T_{N+1}\) con un
único modo grande en \(\pm(N+1)\).  Por tanto la ruta global necesita
positividad Toeplitz infinita, una medida de Herglotz positiva, o un límite
con convergencia real de coeficientes.

`275_PHASE_COMPLETION_CRITERION_A1_AND_GLOBAL.md` fija el criterio de cierre
de fase: una prueba global no circular de semiplano/Herglotz/RDI cierra
\(\Omega_7\) externamente, pero no prueba automáticamente A1 compacto. Como
el objetivo pedido incluye A1, la fase sólo queda completamente cerrada si
además se prueba
\[
  C_n(T_n)\ge0
  \quad\hbox{o equivalentemente}\quad
  s_n\ge d_n
  \qquad(n\ge8),
\]
o una de sus rutas equivalentes: margen fuerte, compensación de cola,
fase/lóbulos firmados, o comparación Loewner--Schur.

`276_LOEWNER_SUBSPACE_COFINALITY_GATE.md` fija la condición de cofinalidad
para pruebas Loewner--Schur: la positividad en un subespacio prueba A1 sólo
si ese subespacio contiene \(p_n=1-z^n\), o si
\[
  p_np_n^*
  \in
  \overline{\mathrm{cone}}\{v_\alpha v_\alpha^*\}
\]
para las direcciones testeadas.  Sin esta reconstrucción positiva, hay
formas hermíticas positivas en todos los tests pero negativas en la
diagonal A1.

`254_TAIL_SIGN_EXPLICIT_FORMULA_PHASE_GATE.md` traduce la cola firmada a una desigualdad
de fase por fórmula explícita:
\[
  I_n(T)
  =
  -2\Re\sum_{\Im\rho>0}{\Phi_{n,T}(\rho)\over\rho}
  -\mathcal T_{n,T}.
\]
Así \(R_n(T_n)\le0\) equivale a una cota unilateral sobre la fase de esa suma de ceros,
no a una estimación de módulo.

`274_TAIL_PHASE_LOBE_DUALITY_GATE.md` identifica esta desigualdad de fase
con la partición de lóbulos de `249`: si \(\Phi_{n,j}\) es la transformada
de un lóbulo absoluto, entonces
\[
  \Phi_{n,T}(\rho)=\sum_j\sigma_{n,j}\Phi_{n,j}(\rho).
\]
Sumar la fórmula explícita por lóbulos recupera exactamente la desigualdad
de fase.  Por tanto el carril de cola necesita correlación firmada de
lóbulos o control de fase de ceros; cotas absolutas de lóbulos y módulos de
ceros no bastan.

`280_TAIL_PHASE_LOBE_BALANCE_GATE.md` separa esa fase en lóbulos positivos
y negativos.  Si
\[
  q_{n,T}(\gamma)=
  \Re\left({\Phi_{n,T}(1/2+i\gamma)\over1/2+i\gamma}\right)
  =
  q^+_{n,T}(\gamma)-q^-_{n,T}(\gamma),
\]
y \(P^\pm_{n,T}=\int q^\pm_{n,T}\,d\mu_\zeta\), entonces
\[
  I_n(T)=2(P^-_{n,T}-P^+_{n,T})-\mathcal T_{n,T}.
\]
Por tanto la puerta completa de cola exige
\[
  P^-_{n,T_n}-P^+_{n,T_n}
  \ge
  {1\over2}
  \left(\mathcal T_{n,T_n}+\left(d_n-{1\over4}\right)A_n\right).
\]

`255_TAIL_MARGIN_CORRELATION_SLACK_FORM.md` introduce el slack de correlación \(h_n\):
\[
  R_n(T_n)\le {1\over4}A_n-h_n.
\]
A1 se obtiene exactamente cuando
\[
  h_n\ge(-M_n)_+.
\]
Normalizado, esto vuelve a \(s_n\ge d_n\), pero evita confundir el slack de correlación
con \(\delta_n\).

`256_POINTWISE_DUAL_CONE_AND_AVERAGE_GATE.md` fija la restricción dual para rutas
promediadas. A1 es equivalente a
\[
  \sum_{n\ge8}\mu_n C_n(T_n)\ge0
  \qquad(\mu_n\ge0,\ \mu\hbox{ de soporte finito}),
\]
y una positividad suavizada sólo cierra el problema si reconstruye positivamente cada masa
coordenada, o si aporta un teorema de extracción de coeficientes. Positividad Abel, Laplace,
Fejer, heat o promedio sin inversa positiva no es una prueba coeficiente-a-coeficiente.

`257_AVERAGED_SLACK_POINTWISE_NO_GO.md` aplica esa restricción al slack de cola:
promedios, subconjuntos de densidad uno, información cofinal o asintótica de
\(h_n-(-M_n)_+\) no bastan. Hay que demostrar
\[
  h_n\ge(-M_n)_+
\]
para cada \(n\ge8\), o dar un umbral efectivo y certificado finito de excepciones.

`277_FINITE_CERTIFICATE_EFFECTIVE_THRESHOLD_GATE.md` fija la misma regla
para los certificados aritméticos finitos: `148`, `190`, `230` y el resto
finito de `261` sólo prueban los índices efectivamente verificados.  Para
cerrar A1 completo hace falta un teorema uniforme para todos los \(n\ge8\),
o un umbral efectivo explícito \(N_\infty\) más verificación rigurosa de
todo \(8\le n<N_\infty\).

`278_COFINAL_SUBSEQUENCE_CERTIFICATE_NO_GO.md` elimina la variante
subsecuencial: certificar una familia cofinal, de densidad uno, o con
bloques arbitrariamente largos no prueba las coordenadas omitidas.  Cada
índice faltante debe venir de propagación, reconstrucción positiva, o del
mismo esquema de umbral efectivo más resto finito.

`258_CRITICAL_LINE_SUPPORT_TAIL_PHASE_NO_GO.md` fija la separación análoga
en el lado de ceros: aun suponiendo soporte sobre la línea crítica, la cola
compacta exige la cota orientada
\[
  2\Re\int_{\gamma>0}
  {\Phi_{n,T_n}(1/2+i\gamma)\over1/2+i\gamma}\,d\mu_\zeta(\gamma)
  \le -\mathcal T_{n,T_n}.
\]
El soporte da el dominio de integración, pero no el signo ni el tamaño de
ese momento incompleto de Laguerre.  Por tanto la ruta de cola todavía debe
probar esta desigualdad de fase o volver al gate equivalente \(s_n\ge d_n\).

`259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md` vuelve efectiva la ruta Fejer de
margen fuerte.  Si existe una medida positiva de incrementos \(\nu_g\) y se
prueba con constantes explícitas
\[
  \int F_n\,d\nu_g
  \ge
  \left({1\over2}+\eta\right)\log n-B_F,
\]
o una densidad logarítmica inferior con coeficiente \(a>1/2\), entonces
\[
  \lambda_n\ge {1\over2}A_n
\]
para todo \(n\) por encima de un umbral efectivo
\[
  N_\infty=
  \max\left(N_A,N_F,
  \left\lceil\exp\left({B_A+B_F\over\eta}\right)\right\rceil\right),
\]
y el resto es verificación finita.  Siguen abiertos la construcción no
circular de \(\nu_g\) y la cota inferior Fejer/logarítmica.

`260_EXACT_FEJER_LOG_KERNEL_CONSTANT.md` cierra la constante analítica de
esa ruta:
\[
  \int_{\partial\mathbb D}F_nL\,dm
  =
  H_{n-1}-{n-1\over n}
  \ge \log n-1.
\]
Por tanto en la alternativa de densidad logarítmica puede tomarse
\(B_L=1\), \(N_L=1\), y quedan sólo la medida positiva de incrementos y la
densidad inferior con coeficiente \(a>1/2\).

`261_FEJER_FINITE_REMAINDER_CERTIFICATE_SCHEMA.md` fija el remanente finito
de esa ruta.  Una vez conocido \(N_\infty\), para cada
\(8\le n<N_\infty\) hace falta un certificado intervalar punto a punto:
o bien
\[
  \lambda_n^- - {1\over2}A_n^+\ge0,
\]
o bien directamente
\[
  C_n(T_n)^-\ge0.
\]
Por `256` y `257`, un promedio o una afirmación asintótica no reemplaza
esta verificación finita.

`262_EXPLICIT_ARCHIMEDEAN_UPPER_FEJER_INPUT.md` cierra el input superior
arquimediano de ese umbral:
\[
  A_n=\lambda_n^{arch}\le {1\over2}n\log n+3n
  \qquad(n\ge2).
\]
Así en `259` puede tomarse \(B_A=3\), \(N_A=2\).

`263_LOCAL_LOG_DENSITY_TO_GLOBAL_FEJER_PATCH.md` repara el paso local-global:
si la densidad satisface \(h\ge aL-B_h\) sólo en \(|\theta|\le\theta_0\),
pero \(h\ge0\) globalmente y el remanente es positivo, entonces se obtiene
la cota Fejer global con
\[
  B_h^\ast=\max\{B_h,\ a(-\log(2\sin(\theta_0/2)))_+\}.
\]
Así basta una densidad logarítmica local con \(a>1/2\), siempre que exista
la descomposición positiva de la medida de incrementos.

`264_FEJER_ROUTE_EXPLICIT_THRESHOLD_LEDGER.md` combina las constantes:
\[
  N_\infty=
  \max\left(
    2,
    \left\lceil
    \exp\left({3+a+B_h^\ast\over a-1/2}\right)
    \right\rceil
  \right).
\]
Por encima de \(N_\infty\), margen fuerte más A0 implica A1.  Por debajo,
queda un certificado finito.  La obstrucción real es ahora construir
\(\nu_g\ge0\) y probar la densidad logarítmica local con \(a>1/2\).

`265_FEJER_LOG_DENSITY_ABEL_COEFFICIENT_BUDGET.md` añade el presupuesto
opuesto: como
\[
  \mathcal G_+(r)
  =
  \lambda_1+{\xi'\over\xi}\!\left({1\over1-r}\right)
  =
  {1\over2}\log {1\over1-r}+O(1),
\]
una cota inferior positiva \(h\ge aL-B_h\) fuerza \(a\le1\).  Así la única
ventana posible para cerrar por densidad Fejer es
\[
  {1\over2}<a\le1.
\]

`266_ABEL_TO_FEJER_DEFECT_GATE.md` aísla el defecto exacto en cualquier
transferencia Abel--Fejer.  Con
\[
  D_{n,\alpha}=(P_{1-1/n}-\alpha F_n)_+,
\]
se tiene
\[
  \int F_n\,d\nu
  \ge {1\over\alpha}
  \left(\int P_{1-1/n}\,d\nu-\int D_{n,\alpha}\,d\nu\right).
\]
En la normalización Euler--Gamma,
\(\int P_{1-1/n}\,d\nu_g=\log n+O(1)\).  Con \(\alpha=1\), bastaría un
defecto \(d\log n+O(1)\) con \(d<1/2\).  Esta es una puerta de
anti-concentración contra los ceros móviles de Fejer, no una prueba de A1.

`270_POISSON_TO_FEJER_POSITIVE_INVERSE_NO_GO.md` prueba que las cotas
radiales Abel/Poisson no tienen una inversa positiva hacia Fejer: \(F_N\)
se anula en las raíces \(N\)-ésimas no triviales, mientras todo kernel de
Poisson radial es estrictamente positivo allí.  Por tanto la ruta Fejer
requiere una cota Fejer directa, una densidad local, o anti-concentración
contra los ceros móviles de \(F_N\); el crecimiento Abel por sí solo no
alcanza.

`281_ABEL_SPIKE_FEJER_ZERO_MODEL_NO_GO.md` da un modelo positivo explícito:
una medida finita puede tener picos Poisson de tamaño \(\log N_j\) en
\(r_{N_j}=1-1/N_j\), mientras los tests Fejer correspondientes permanecen
acotados, colocando masa \((\log N_j)/N_j\) en raíces \(N_j\)-ésimas no
triviales donde \(F_{N_j}=0\).  Por tanto la escala radial correcta de
\(\mathcal G_+\) no fuerza margen Fejer ni densidad logarítmica local.

`271_POSITIVE_INCREMENT_FEJER_MASS_SEPARATION.md` fija la separación entre
positividad incremental global y A1 compacto.  Una medida positiva da
\[
  2\lambda_n=n\int F_n\,d\nu_g,
\]
y por tanto positividad Li si se construye de forma no circular.  Pero A1
requiere además
\[
  \int F_n\,d\nu_g\ge {A_n\over n}.
\]
La positividad, la masa total finita o el soporte lejos de \(\zeta=1\) no
producen esa masa Fejer de orden \(\log n\).  El carril compacto queda
exactamente en una densidad logarítmica inferior con \(1/2<a\le1\), o una
cota Fejer directa equivalente, más verificación finita.

`272_FEJER_MASS_LOCALIZATION_NECESSARY_GATE.md` fija una condición necesaria
de localización: como
\[
  F_n(e^{i\theta})\le \min\left(n,{\pi^2\over n\theta^2}\right),
\]
una cota \(\int F_n\,d\nu_g\ge\frac12\log n-O(1)\) fuerza masa logarítmica
localizada cerca de \(\zeta=1\).

`273_FEJER_LAYER_CAKE_DISTRIBUTION_GATE.md` reescribe la obligación Fejer
como distribución exacta de superniveles:
\[
  \int F_n\,d\nu_g
  =
  \int_0^n\nu_g\{F_n\ge t\}\,dt.
\]
Por tanto el margen fuerte compacto equivale a
\[
  \int_0^n\nu_g\{F_n\ge t\}\,dt\ge {A_n\over n}
  \qquad(n\ge8).
\]
La densidad local y el defecto Abel--Fejer son dos mecanismos suficientes
para esa misma cota de distribución.

El gate `277_FINITE_CERTIFICATE_EFFECTIVE_THRESHOLD_GATE.md` impide cerrar
esta ruta sólo con cálculos finitos dispersos: una vez probado el input
Fejer/log-density eventual, hay que publicar \(N_\infty\) y ejecutar el
certificado finito de `261` en todo el intervalo restante.

`234_WEIGHTED_MERTENS_CHEBYSHEV_ERROR_IDENTITY.md` identifica la discrepancia ponderada con el error
ordinario de Chebyshev:
\[
  E_8^\sharp(u)=
  e^{-u}E(e^u)-e^{-T_8}E(e^{T_8})
  +\int_{T_8}^{u}e^{-t}E(e^t)\,dt.
\]
Por tanto la frontera de sumación parcial es otra coordenada del mismo core firmado
Chebyshev--Laguerre, no una fuente independiente de positividad.

`229_SMALL_T7_DIRECT_COEFFICIENT_REDUCTION.md` combina `226`--`228`: el único transformado aritmético
móvil restante es
\[
  \sum_{m\le e^{T_n}}{\Lambda(m)\over m}L_{n-1}^{(1)}(\log m),
\]
más constantes finitas de la ventana base \(\log m<T_8\).

`230_SINGLE_TRANSFORM_A1_FRONTIER.md` elimina la última capa notacional: si
\[
  S_n(T)=\sum_{m\le e^T}{\Lambda(m)\over m}L_{n-1}^{(1)}(\log m),
\]
A1 equivale exactamente a
\[
  S_n(T_n)\le
  E(e^{T_n})e^{-T_n}L_{n-1}^{(1)}(T_n)
  +1-L_n^{(0)}(T_n)
  +{3\over4}\lambda_n^{\rm arch}-n.
\]

`196_A1_REMAINING_THEOREMS_CANONICAL_FORM.md` consolida los teoremas exactos que quedan vivos:
núcleo compacto directo/firmado, margen fuerte, cola unilateral, comparación Loewner--Schur, o el
teorema global de semiplano. La dominación absoluta \(L^1\) queda sólo como condición suficiente
formal fuera de la escala VK; con envolventes VK está descartada por `221`.

`197_CUMULATIVE_KERNEL_INTERVAL_FORM.md` da la fórmula exacta de \(\mathcal H_n\) por intervalos. En
el tramo terminal \((T_{n-1},T_n)\) se tiene \(\mathcal H_n=-L_{n-1}^{(2)}\); en los tramos previos
aparecen mezclas acumuladas de Laguerres. Por tanto la ruta absoluta debe dominar al menos la carga
\(\int_{T_{n-1}}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du\) y además controlar las mezclas anteriores;
el interlacing estándar de una sola familia Laguerre no basta sin un teorema adicional para esas
mezclas.

`199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` refina la comparación Loewner--Schur: una prueba válida
debe construir una forma comparativa
\(\mathfrak Q^{\mathcal L}-\frac14\mathfrak Q^{\mathcal A}-\mathfrak Q^{\mathcal R,T_n}\), probar
positividad en un bloque auxiliar y probar una innovación no negativa antes de usar que la diagonal es
\(2C_n(T_n)\). Calcular el complemento de Schur después de insertar el signo de A1 sería circular.

### Carril B — LP+IDENT/RDI, sólo si produce el signo de Li

Este carril es alternativo. Para completarlo deben cerrarse todos los puntos siguientes y, al final,
probarse su enlace explícito con el punto 5:

17. **BTG-DIV en la medida verdadera \(\mu_L\). — ABIERTO.**
18. **Interfaz LP libre de una elección circular de \(\mu_L\). — ABIERTO.**
19. **GAP-Z, incluida la contribución ZERO con cancelación firmada. — ABIERTO.**
20. **RDI-ANCHOR o una única formulación equivalente completamente escrita. — ABIERTO / FUERZA-RH.**
21. **RDP-SHELL con colas direccionales después del pareamiento firmado. — ABIERTO.**
22. **SAFE-PROLATE-BRIDGE sin asumir positividad de Weil. — ABIERTO / posible FUERZA-RH.**
23. **SAFE-LIMIT-POINT. — ABIERTO.**
24. **SR-SAFE. — ABIERTO.**
25. **Teorema de enlace RDI \(\Rightarrow\lambda_n\ge0\). — ABIERTO / FUERZA-RH.**
    
    No basta llegar a un objeto “seguro”: hay que demostrar, con normalizaciones y límites completos,
    que su seguridad implica la desigualdad unilateral de Li para cada índice.

    El triage corto está registrado en `fragments/OMEGA7_CARRIL_B_TRIAGE.md`. La conclusión actual es
    suspender este carril como prioridad: no hay todavía un puente literal RDI \(\Rightarrow\lambda_n\ge0\)
    ni RDI \(\Rightarrow\) realidad de ceros; BTG y GAP-Z permanecen como infraestructura abierta, no como
    mecanismo de signo.

### Controles transversales que deben acompañar cualquier carril

26. **Auditoría de no-go por clase, no como veto universal.** Cada no-go sólo elimina la clase que
    realmente cubre. Ningún no-go puede usarse para abandonar un enunciado por ser equivalente a RH.
27. **Comparación bibliográfica por mecanismo.** Determinar qué parte es conocida y aislar exactamente
    la identidad o desigualdad nueva que se debe probar.
28. **Prueba simbólica antes de inferencia numérica.** Los cálculos sirven para descubrir y falsar; el
    cierre requiere una demostración uniforme.
29. **Orden de límites explícito.** Todo teorema debe declarar dependencias en \(n,N,L,X,\varepsilon\)
    y el orden en que se eliminan los reguladores.
30. **Ledger de dependencias.** Cada obligación cerrada debe señalar el lema exacto que la demuestra y
    no puede depender directa o indirectamente de la misma conclusión salvo dentro de una equivalencia
    declarada cuyo sentido útil tenga prueba independiente.

## Decisión principal

No conviene continuar acumulando fórmulas alrededor de LP+IDENT. La revisión descubre además que el blanco primo usado para organizar parte de paper 36 era innecesariamente fuerte. Del split exacto

\[
\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}
\]

se obtiene

\[
\Omega_7
\quad\Longleftrightarrow\quad
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}
\quad\text{para todo }n,
\]

no una dominación en valor absoluto. El reinicio debe dar prioridad al lower bound **unilateral y firmado** de la parte prima. Cuando \(\lambda_n^{\rm arch}\ge0\), esto significa controlar su excursión negativa; cuando \(\lambda_n^{\rm arch}<0\), exige conservar una contribución prima positiva suficiente. Las paredes basadas en sumar magnitudes o dominar \(|\lambda_n^{\rm prime}|\) no cierran esta clase.

RDI-ANCHOR sigue siendo el candidato más claro dentro de la ruta LP+IDENT a portar la identificación aritmética que debe fallar fuera de línea. No está demostrado que sea el único paso de fuerza-RH, porque LP/BTG y GAP-Z tampoco están cerrados en el control correcto. Esa ruta queda como segundo carril, no como prerequisito de todo ataque a \(\Omega_7\).

La proposición “GAP-Z es infraestructura neutral” sería concluyente si se probara para una clase que incluye una construcción con divisor fuera de línea. Hoy sólo hay evidencia finita, y parte usa \(\mu_{\rm ref}\) en lugar del verdadero \(\mu_L\). Por eso no se debe invertir una campaña larga en GAP-Z, pero tampoco declararlo irrelevante.

El reinicio debe atacar primero el blanco mínimo de Li y, en paralelo limitado, decidir si LP/GAP-Z son infraestructura demostrable o cargas adicionales. Sólo si aparece un mecanismo genuino en la ruta RDI debe retomarse su cadena downstream.

## Estado mínimo de la ruta actual

La cadena suficiente es

\[
\begin{aligned}
&\mathrm{LP}+\mathrm{IDENT}+\mathrm{RDP\!-\!SHELL}
+(\mathrm{PROLATE}+\mathrm{WEIL\!-\!TAIL})\\
&\Longrightarrow
\mathrm{SAFE\!-\!LIMIT\!-\!POINT}
\Longrightarrow
\mathrm{SR\!-\!SAFE}
\Longrightarrow
\Omega_7.
\end{aligned}
\]

Su ledger corregido es:

| Obligación | Estado | Riesgo |
|---|---|---|
| BTG-DIV en el verdadero \(\mu_L\) | **ABIERTO** | La evidencia Outcome A usa una aproximación finita; LP neutral no está certificado. |
| Interfaz LP mu-libre | **ABIERTO** | Las cláusulas fijadas en \(\mu_L\) fueron declaradas inadmisibles, pero no se construyó el reemplazo. |
| GAP-Z | **ABIERTO** | MESH y BND están acotados; ZERO no. La suma absoluta de capas está bloqueada. |
| RDI-ANCHOR | **ABIERTO / candidato FUERZA-RH** | Convergencia y coherencia no identifican el límite Euler–Gamma. |
| RDP-SHELL y colas direccionales | **ABIERTO** | No se pueden estimar antes del pareamiento firmado. |
| SAFE-PROLATE-BRIDGE | **ABIERTO** | Alto riesgo de reintroducir positividad de Weil. |
| \(\Omega_7\) | **ABIERTO / FUERZA-RH** | Es RH por Li. |

El candidato original E79.6 —single-signedness de una nube finita— no es el blanco canónico. Fue debilitado por retracciones y fases posteriores. La versión actual debe formularse en una sola de estas coordenadas equivalentes:

\[
\mathrm{RDI\!-\!ANCHOR}
\sim
\mathrm{DIRECT\!-\!BORDERED\!-\!ANCHOR}
\sim
\mathrm{LOCAL\!-\!COVARIANT\!-\!IDENT}
\sim
\mathrm{STIELTJES\!-\!IDENT}.
\]

TRUE-DIVISOR-IDENT es más fuerte y no debe elegirse si basta una identificación segura de menor alcance.

## Etapa I — reparar el mapa para atacar RH

Esta etapa no necesita una fase nueva.

### I.1 Registro canónico de objetos

Fijar una sola definición para:

\[
\delta_N^{\rm ref},\quad
\delta_N^{\rm arch},\quad
\mu_L,\quad
\mu_{\rm ref},\quad
\mathrm{ZERO},\quad
C_{\rm core},\quad
\mathrm{RDI\!-\!ANCHOR},\quad
\mathcal C_{\rm Euler}.
\]

Cada definición debe contener dominio, normalización, orden de límites y dependencia de \(L,N,z\). Ningún teorema puede usar \(\delta_N\) o \(\mu\) sin superíndice o dominio.

### I.2 Errata matemática de paper 36 — COMPLETADA

Separar del frente de prueba las reparaciones:

- retirar la extensión compacta de H2;
- corregir H6, conservar \(|\kappa|\) y rotular la dominación de cola como abierta;
- reescribir \(\Omega_4\) con los dos blanqueamientos;
- rebajar \(\Omega_5\) a continuidad por \(N\) fijo;
- retirar la envolvente que aísla \(\sum_\rho(1-1/\rho)^n\);
- corregir el signo y el término de borde de la integración por partes Laguerre;
- restaurar \(\frac{\gamma-1}{2}n\) en la asintótica de envolvente y restringir la cota con \(\log n\) a \(n\ge2\);
- rebajar muestreo, saturación y cascada a resultados condicionales;
- corregir la aplicación de X3 a una clase de norma negativa.

Estas reparaciones ya están incorporadas en paper 36. No cierran \(\Omega_7\), pero dejan su frente
correctamente tipado y evitan apoyar la prueba nueva en lemas falsos.

### I.3 Registro de precedencia

Crear una tabla claim \(\to\) estado \(\to\) prueba \(\to\) corrección \(\to\) dependencias. El rótulo de cierre nunca será fuente de verdad. Esto evita que una fase posterior herede el QED retirado de fase 65, E78.154, el proxy de precisión insuficiente o la definición incorrecta de mean(d).

## Etapa II — ataque directo al blanco unilateral de Li

### II.1 Definición sin ambigüedad

Fijar la continuación aritmética mediante el límite pareado

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[
\sum_{k=1}^n
\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
-
\sum_{m\ge2}\frac{\Lambda(m)}{m^{1+\varepsilon}}
L_{n-1}^{(1)}(\log m)
\right]
\]

o con un símbolo de parte finita que declare exactamente el mismo procedimiento. La suma desnuda en el borde no puede manipularse como absolutamente convergente. Toda integración por partes debe mantener junta la cancelación que define el valor continuado.

Con \(f_{n,\varepsilon}(y)=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y)\), el término polar no es una abreviatura formal: satisface

\[
\sum_{k=1}^n\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
=
\int_0^\infty L_{n-1}^{(1)}(x)e^{-\varepsilon x}\,dx
=
\int_1^\infty f_{n,\varepsilon}(y)\,dy.
\]

Esta identidad es la que debe conservarse al pasar a Stieltjes e integrar por partes.

El objetivo exacto será

\[
\boxed{
\lambda_n^{\rm prime}+\lambda_n^{\rm arch}\ge0
\quad(n\ge1)
}
\]

Éste es el único blanco global. Para los índices con \(\lambda_n^{\rm arch}\ge0\), puede reescribirse como

\[
(\lambda_n^{\rm prime})_-
\le\lambda_n^{\rm arch}.
\]

Para este split se puede cerrar el signo de la parte arquimediana:

\[
I_-:=\{n\ge1:\lambda_n^{\rm arch}<0\}=\{1,2,\ldots,7\}.
\]

En efecto,

\[
\lambda_n^{\rm arch}
=1-\frac n2(\gamma+\log(4\pi))
+\sum_{\substack{r\ge1\\r\ {\rm impar}}}
\left[\left(1-\frac1r\right)^n-1+\frac nr\right].
\]

Si \(d_n=\lambda_{n+1}^{\rm arch}-\lambda_n^{\rm arch}\), entonces

\[
d_{n+1}-d_n
=\sum_{r\ {\rm impar}}\frac{(1-1/r)^n}{r^2}>0.
\]

Una evaluación con intervalos de la fórmula exacta da \(d_3\in(0.0062,0.0063)\), \(\lambda_1^{\rm arch}\in(-0.555,-0.554)\), \(\lambda_2^{\rm arch}\in(-0.875,-0.874)\), \(\lambda_7^{\rm arch}\in(-0.356,-0.355)\) y \(\lambda_8^{\rm arch}\in(0.020,0.022)\). Por convexidad discreta, la sucesión crece desde \(n=3\) y no vuelve a ser negativa después de \(n=8\). Para \(n=1,\ldots,7\) se debe certificar el lower bound original; allí una contribución prima positiva es necesaria.

### II.2 Descomposición por excursión negativa

Usar la representación que conserva el signo del kernel Laguerre antes de estimar. Con

\[
f_{n,\varepsilon}(y)
=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\]

la identidad corregida, con el borde inferior incluido, es

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty
(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
=
\lim_{\varepsilon\downarrow0}
\left[-n+
\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy\right].
\]

El blanco es

\[
\lim_{\varepsilon\downarrow0}
\int_1^\infty
(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
\ge-\lambda_n^{\rm arch}.
\]

En el complemento de \(I_-\), la misma desigualdad controla sólo la parte negativa. La integral de
\(|\psi-y+1|\,|f'_{n,\varepsilon}|\), la suma de normas por shell y los majorantes simétricos no son el
blanco mínimo y las estimaciones conocidas no alcanzan. Sin embargo, no quedan prohibidos: si se logra
demostrar una cota absoluta de fuerza-RH suficientemente fuerte, eso también cerrará \(\Omega_7\). La
prioridad unilateral sólo evita imponer dificultad adicional sin necesidad.

### II.3 Falsadores obligatorios

Antes de exigir un falsador aritmético debe definirse una clase \(\mathcal C_{\rm Euler}\) de objetos completados \(F\), cada uno con coeficientes de Dirichlet, factor Gamma, ecuación funcional, continuación y una regla común que produzca

\[
F\longmapsto
(\lambda_{n,F}^{\rm arch},\lambda_{n,F}^{\rm prime}).
\]

Sólo dentro de esa clase tiene sentido afirmar que un mismo lema vale para \(\zeta\) y falla fuera de línea. Un cuarteto insertado sin datos aritméticos compatibles prueba sensibilidad del lado de ceros, pero no falsifica deductivamente una desigualdad Euler–Gamma.

Una vez construida la clase, un lema candidato debe distinguir tres situaciones sin leer posiciones de ceros:

1. los datos aritméticos de \(\zeta\), donde entrega el lower bound;
2. un miembro de \(\mathcal C_{\rm Euler}\) con cuarteto fuera de línea, donde la excursión negativa crece geométricamente y el lema falla;
3. un control sobre la línea, donde no prohíbe las oscilaciones positivas ni la suma de cuadrados.

Si el lema vale también para el control fuera de línea, no puede cerrar \(\Omega_7\). Si su hipótesis
equivale a real-rootedness, esa hipótesis pasa a ser una nueva obligación de fuerza-RH: debe demostrarse
independientemente desde la estructura aritmética y no puede darse por supuesta.

### II.4 Puerta de salida

Este carril continúa sólo si produce uno de estos objetos:

- una identidad firmada nueva que entregue el lower bound exacto sin valores absolutos;
- una desigualdad unilateral estable bajo el límite del borde;
- un principio variacional aritmético cuya hipótesis sea verificable desde Euler–Gamma y falle estructuralmente fuera de línea.

Una cota numérica de envolvente, un exponente ajustado o positividad para índices finitos no justifican una fase nueva.

## Etapa III — prueba de atribución H0 para LP+IDENT

Antes de atacar el discriminante hay que decidir qué partes son realmente neutrales.

### III.1 Neutralidad de LP

Formular una clase abstracta \(\mathcal C_{\rm LP}\) que contenga tanto la construcción zeta como un control fuera de línea y que use sólo:

\[
H_L=D_L+B_L,\qquad
D_L(n)=\log(1+|n|)+O_L(1),\qquad
B_L\ \text{acotado},
\]

más hipótesis explícitas de compacidad y fuente.

El objetivo no es medir discos, sino demostrar o refutar:

\[
\mathcal C_{\rm LP}
\Longrightarrow
\|A_N(\mu_L)^{-1}b_N\|\longrightarrow\infty.
\]

Hay tres resultados posibles:

1. se prueba para toda \(\mathcal C_{\rm LP}\): LP queda neutral;
2. aparece un contraejemplo dentro de \(\mathcal C_{\rm LP}\): la formulación es falsa;
3. la prueba necesita una propiedad aritmética que separa el control: LP también porta dificultad y la atribución exclusiva a IDENT queda refutada.

No se acepta sustituir \(\mu_L\) por \(\mu_{\rm ref}\) en la conclusión.

### III.2 Neutralidad de GAP-Z

Partir únicamente de la identidad demostrada

\[
g_{N+2}-g_N
=
\mathrm{ZERO}+\mathrm{MESH}+\mathrm{BND},
\]

con las cotas conocidas para MESH y BND. El problema exacto es una cota firmada y localmente uniforme para ZERO.

Primero debe probarse una dicotomía:

\[
\begin{cases}
\mathrm{ZERO}\text{ se controla desde axiomas compartidos por ambos builds},&
\text{GAP-Z neutral};\\
\mathrm{ZERO}\text{ requiere una identidad Euler específica},&
\text{GAP-Z porta parte de la discriminación}.
\end{cases}
\]

Quedan prohibidos:

- sumar magnitudes de shells antes de cancelar;
- usar una firma que separa los builds como supuesto de convergencia;
- inferir una ley desde un exponente ajustado;
- transportar al límite una malla de \(N\) finitos.

Esta etapa debe ser de triage: si no aparece un teorema abstracto corto o un contraejemplo, GAP-Z se mantiene abierto y se suspende. No se abre otra cascada de proxies.

### III.3 Resultado de atribución

Sólo después de III.1–III.2, mediante un teorema build-neutral o un contraejemplo en las clases declaradas, se puede afirmar una de estas sentencias:

\[
\boxed{\text{toda la fuerza está en IDENT}}
\qquad\text{o}\qquad
\boxed{\text{la fuerza está repartida o la ruta contiene un error}}.
\]

H0 garantiza al menos un paso de fuerza-RH o falso. No garantiza exactamente uno mientras los demás pasos no estén demostrados.

## Etapa IV — fijar el único blanco RDI, si sobrevive la atribución

Si la atribución deja IDENT como separador, congelar todas sus coordenadas salvo una. La recomendación es usar el defecto covariante core porque:

- conserva el factor exterior correcto;
- evita dividir en la curva singular;
- mantiene la fuente Gamma–Euler completa;
- se formula en \(\Re s>1\), donde el lado primo converge absolutamente;
- admite un falsador fuera de línea dentro de una clase aritmética tipada.

Esta etapa no autoriza una nueva reformulación del ancla. Sólo continúa si ya existe una identidad o desigualdad que aporte una estimación ausente en las coordenadas anteriores. En ese caso, el enunciado mínimo debe tener esta forma lógica:

\[
\textbf{ARITHMETIC-CORE-IDENT:}\qquad
C_{{\rm core},L,N}(s)
\longrightarrow
0
\]

localmente en un conjunto seguro, con un orden de límites escrito y una derivada si la propagación la necesita. El nombre es provisional; el documento final debe escribir la fórmula completa, no esconderla bajo una sigla.

El teorema debe satisfacer cinco condiciones:

1. el lado izquierdo se calcula desde datos finitos CCM sin posiciones de ceros;
2. su anulación se deriva de una identidad Euler–Gamma en convergencia absoluta, no se postula;
3. la identidad conserva conjugación, soporte transversal y multiplicidad lineal;
4. el control aritmético fuera de línea de la clase declarada falla por un cálculo estructural, no por un umbral ajustado;
5. la prueba no usa positividad de Weil, real-rootedness, una métrica adaptada a raíces ni una suma absoluta de contribuciones primas.

Probar este enunciado tendrá fuerza-RH. La meta no es volverlo “técnico”, sino encontrar una razón aritmética nueva por la cual sea verdadero.

## Etapa V — búsqueda de mecanismo, no de coordenada

Tres clases candidatas actualmente identificadas, sin pretensión de exhaustividad, justifican trabajo nuevo.

### V.A Identidad global de cancelación

Buscar una involución, coborde o relación funcional sobre el conjunto completo de celdas primas que haga desaparecer el defecto después del pareamiento correcto:

\[
\sum_{p^k}\mathcal J_{p^k}(s)
\quad\text{se reorganiza globalmente antes de tomar}\quad |\cdot|.
\]

No sirve positividad por prima ni matching célula a célula. El mecanismo debe ser no local y retener los términos arquimedianos y de borde.

### V.B Transporte firmado fase→corriente

Construir un teorema que transforme información aritmética de fases en la corriente covariante sin pasar por promedio:

\[
\text{datos Euler}
\Longrightarrow
\text{cancelación firmada del core}
\Longrightarrow
\text{identificación segura}.
\]

Debe exceder las clases tauberianas/locales ya cerradas y distinguir \(\zeta\) del control fuera de línea dentro de una clase tipada.

### V.C Geometría externa

Sólo reabrir la ruta geométrica si se construye primero un objeto independiente con diagonal, polarización y lector espectral. No se permite definir la estrella, métrica o correspondencia desde el divisor de \(\Xi\). Sin objeto nuevo, volver a Hodge/Lefschetz sería repetir RH9 y las fases 39–45.

La prioridad recomendada es V.A, empezando por su versión directa unilateral de la Etapa II. Es la vía directa actualmente especificada que usa la estructura Euler–Gamma ya aislada sin pedir una geometría inexistente ni un promedio.

## Etapa VI — puerta de novedad bibliográfica

Antes de desarrollar un lema candidato:

1. escribir el enunciado sin terminología interna;
2. identificar sus ingredientes clásicos;
3. buscar en fuentes primarias por fórmula y mecanismo;
4. comparar hipótesis y conclusión, no sólo palabras clave;
5. registrar si es conocido, combinación conocida, variante real o nuevo.

Hasta pasar esta puerta, toda etiqueta “nueva matemática” queda como **NOVEDAD NO CERTIFICADA**.

## Etapa VII — falsación previa a una fase

No se abre otra fase hasta tener un candidato que pase:

| Prueba | Requisito |
|---|---|
| Off-line | Debe fallar en un control aritmético fuera de línea dentro de una clase tipada; un cuarteto plantado aislado sólo da falsación heurística. |
| On-line | Debe ser compatible con el control sobre la recta sin usar sus ceros. |
| Información | Debe preservar conjugación y multiplicidad lineal. |
| Límites | Debe declarar y justificar el orden \(N\), \(L\), borde. |
| No-go | No puede ser Gram tautológica, positividad finita, gap único, smoothing, pseudoinversa, un nivel de momentos o producto de trazas. |
| Independencia | Puede demostrar y usar una condición equivalente a RH, pero no asumirla: debe derivarla independientemente desde los datos permitidos. |
| Novedad | Debe superar la comparación bibliográfica por mecanismo. |

Si falla una puerta, se registra en este dossier; no se abre un nuevo directorio de fase. Una fase nueva sólo se justifica cuando aparece un nuevo grado de libertad matemático, no otro nombre para el ancla.

## Orden de esfuerzo recomendado

1. **Completado:** corregir el ledger, el blanco primo, paper 36 y la separación de objetos.
2. **Completado:** fijar la fórmula aritmética unilateral con todos sus términos de continuación y borde.
3. **Completado:** cerrar con intervalos racionales los siete índices del rango arquimediano excepcional.
4. Pasar la puerta bibliográfica para la fórmula y para cada mecanismo firmado propuesto.
5. Atacar A0, la cola uniforme Mellin--Laguerre, y después A1, el núcleo firmado global de los puntos
   12--13.
6. Probar simultáneamente el límite de borde, la cola firmada y la uniformidad en \(n\).
7. Si aparece una cota absoluta demostrable de fuerza-RH, perseguirla: aunque sea más fuerte que el
   blanco mínimo, cerraría igualmente \(\Omega_7\).
8. **Completado:** ejecutar un triage corto de LP/GAP-Z. Resultado: el carril B no aporta todavía un
   mecanismo de signo literal; queda suspendido salvo aparición de un puente RDI-to-Li o RDI-to-realidad.
9. Fijar una sola fórmula de RDI-ANCHOR/core si el carril B produce un enlace explícito con Li.
10. Volver a colas y puentes downstream únicamente como parte de una cadena completa hasta el punto 25.
11. Ensamblar los rangos finito e infinito y aplicar el criterio de Li.

Esta secuencia concentra el esfuerzo en el primer enunciado todavía abierto que puede entregar el signo
global. No excluye una ruta por ser más fuerte o equivalente a RH; exige que cada ruta llegue, mediante
una prueba, a la desigualdad final.

## Adenda phase 102 — puertas A1 actualmente normalizadas

La reducción A0/A1 ya está separada. A0 cierra la cola absoluta con datos PNT y cotas Laguerre; no
crea signo. El núcleo pendiente sigue siendo

\[
  -n+\int_1^{e^{T_n}}(\psi(y)-y)f'_{n,0}(y)\,dy
  +{3\over4}\lambda_n^{\rm arch}\ge0
  \qquad(n\ge8).
\]

Las puertas equivalentes o más fuertes que quedan permitidas son:

1. probar A1 directamente;
2. probar el margen fuerte
   \[
      \lambda_n\ge {1\over2}\lambda_n^{\rm arch}\qquad(n\ge8);
   \]
3. probar una cola unilateral que mejore A0 en signo;
4. construir la medida positiva de borde para \(\xi'/\xi\) en coordenada de línea;
5. construir un Hermite--Biehler Euler--Gamma independiente;
6. probar positividad Pick/Stieltjes infinita de la transformada generadora de Li;
7. probar una corriente bordered positiva no tautológica;
8. probar positividad del borde Mellin simetrizado;
9. probar positividad de coeficientes para la función generadora compacta con corte fijo junto con un
   manejo real de la dependencia \(T_n\), o construir directamente una transformada positiva de corte
   móvil.
10. probar positividad de coeficientes para el generador prime-pole exacto después del pareamiento con
    el polo;
11. probar la compensación alternante entre lóbulos de \(L_{n-1}^{(2)}\);
12. probar el lema coercivo de Schur Euler--Gamma;
13. probar el teorema completado de soporte de borde Pick/Stieltjes;
14. probar el balance dual firmado de lóbulos;
15. probar una desigualdad de la jerarquía elevada de balances \(B_r\) contra
    \(L_{n-1}^{(2+r)}\).
16. probar la desigualdad de jets finitos en \(s=1\) para la transformada
    truncada \(\mathcal B_{r,T_n}\).
17. probar una cota firmada uniforme para el certificado aritmético finito
    explícito de A1.
18. probar positividad de coeficientes sobre la diagonal móvil
    \([z^n]\mathcal C_{T_n}(z)\).
19. probar el margen fuerte o una cola unilateral en la convención exacta
    \(C_n(T)=\lambda_n-\frac14\lambda_n^{\rm arch}-R_n(T)\).
20. probar la transferencia firmada entre cortes
    \(C_n(T)-C_n(S)=-\int_S^T E(e^u)e^{-u}L_{n-1}^{(2)}(u)\,du\).
21. probar la forma dual acumulada de esa transferencia, con \(B_S\) y
    \(L_{n-1}^{(3)}\).
22. construir la raíz cuadrada positiva de Weil/autocorrelación para el test
    compacto A1.
23. probar las cotas firmadas de forzamiento en la recurrencia de Laguerre
    en \(n\) para \(C_n(T)\).
24. probar la cota firmada del forzamiento completo en la recurrencia de
    Laguerre, con la corrección arquimediana explícita.
25. probar la desigualdad acumulada diagonal en coordenadas de balance, con
    el kernel elevado y todos los saltos firmados en los cortes \(T_j\).
26. probar uniformemente el certificado finito diagonal
    \(\mathcal A_n+\Pi_n+\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n(m)\ge0\).
27. construir una forma positiva Euler--Gamma Li-normalizada sin añadir al
    pareamiento cruzado un contratérmino positivo invisible en todos los
    tests \(1-z^n\), opción eliminada por
    `171_LOCAL_COUNTERTERM_RIGIDITY_NO_GO.md`.

Los atajos descartados son: optimizar \(T_n\) usando sólo A0; usar una matriz finita positiva sin
identificación cofinal; usar positividad total finita; llamar medida de borde a la medida de Riesz sin
colapso de soporte; desplazar contornos Mellin sin un teorema de positividad; o deducir signo de un
complemento de Schur por álgebra formal; o inferir A1 desde positividad de coeficientes para un único
corte fijo sin resolver la dependencia \(T_n\).

El archivo `124_A1_GATE_IMPLICATION_GRAPH.md` registra el grafo actual de implicaciones,
`126_UNIVERSAL_CUTOFF_GATE_AUDIT.md` registra que A0 no suministra un \(T_\ast\) universal, y
`127_MOVING_CUTOFF_FLOW_NORMAL_FORM.md` identifica el flujo de borde que habría que controlar si se
persigue la puerta de corte móvil. El archivo `128_TAIL_AND_STRONG_MARGIN_GENERATORS.md` registra que
el margen fuerte sí es un problema de coeficientes de la transformada de Li modificada, mientras que
la cola sólo está justificada coeficiente a coeficiente o en dominio de Abel bajo A0/PNT.
`129_ABEL_LAPLACE_TAIL_DOMAIN_AUDIT.md` refina esto: en la variable \(w=z/(1-z)\), A0 produce una
transformada de Laplace firmada, no una transformada positiva. `130_FOURIER_BOCHNER_GATE_AUDIT.md`
registra además que la positividad Fourier ordinaria de \(\Xi\) no fuerza ceros reales; la ruta
Fourier sólo reentra mediante total positividad infinita, Pólya-frequency o Hermite--Biehler.
`131_JENSEN_COFINAL_GATE_AUDIT.md` registra la subpuerta Jensen: se necesita hiperbolicidad cofinal
con convergencia Laguerre--Pólya, no verificaciones finitas ni asintótica de grado fijo.
`132_HEAT_FLOW_NEWMAN_GATE_AUDIT.md` registra la subpuerta heat-flow: se necesita colocar el umbral de
realidad de ceros en \(t\le0\), no sólo realidad para tiempos positivos futuros.
`133_LI_DISK_SCHUR_GATE_AUDIT.md` registra la coordenada de disco \(w_\rho=1-1/\rho\): la puerta
Schur requiere construir soporte en \(\partial\mathbb D\), no definirlo desde el divisor.
`134_OFFLINE_GEOMETRIC_MODE_LEMMA.md` prueba que cualquier punto exterior \(|w|>1\) produce una
subsecuencia negativa geométrica en Li; esto fortalece el falsador, pero no excluye el punto exterior
para \(\zeta\). `135_ARCHIMEDEAN_GROWTH_BOUND.md` prueba además que
\(\lambda_n^{\rm arch}=O(n\log n)\), de modo que ese modo geométrico no puede absorberse en el
presupuesto arquimediano. `136_FINITE_EXTERIOR_SHELL_DOMINANCE.md` cierra el caso de un shell exterior
finito máximo y deja aislado el problema infinito de soporte del divisor.
`137_ISOLATED_EXTERIOR_RADIUS_REDUCTION.md` extiende esto a radios exteriores aislados; lo que queda
es soporte exterior no aislado, acumulación hacia \(\partial\mathbb D\) o cancelación pareada infinita.
`138_ZETA_EXTERIOR_RADIUS_MAXIMUM.md` cierra esa caveat en el lado de ceros para \(\zeta\): cualquier
cero off-line produce un shell exterior máximo finito. Esto recupera la implicación cero-side de Li,
pero no la positividad aritmética A1. `139_ZERO_SIDE_LI_CRITERION_CLOSURE.md` consolida esa conclusión:
el criterio de Li está cerrado del lado de ceros; lo pendiente es probar \(\lambda_n\ge0\) desde
Euler--Gamma, concentrado en A1 o en una puerta más fuerte. `140_EULER_GAMMA_LI_GENERATOR.md` fija el
generador aritmético exacto \(\mathcal L=\mathcal A+\mathcal P\), con la parte prima pareada al polo.
`141_PRIME_POLE_INTEGRAL_GENERATOR.md` reescribe \(\mathcal P\) como el integral exacto contra
\(\psi(y)-y\) y recupera coeficiente a coeficiente el núcleo Laguerre; por tanto la ruta generadora
no evita A1, sino que la identifica como su problema firmado compacto.
`142_A1_VARIATIONAL_ENERGY_FORM.md` pone A1 en forma de mínimo de Schur--Friedrichs y aísla el lema
coercivo Euler--Gamma que faltaría. `143_PRIME_POLE_PICK_STIELTJES_GATE.md` elimina la positividad
Pick/Stieltjes local del generador prime-pole y deja como puerta viva sólo el teorema completado de
soporte de borde positivo.
`144_LAGUERRE_CORE_SIGN_PARTITION.md` prueba además el colapso
\(L'_{n-1}^{(1)}-L_{n-1}^{(1)}=-L_{n-1}^{(2)}\), dejando A1 como una
desigualdad alternante sobre lóbulos canónicos de Laguerre.
`145_LAGUERRE_LOBE_DUAL_BALANCE.md` integra una vez el error de Chebyshev y obtiene el balance
acumulado exacto contra la variación de esos lóbulos. `146_RAISED_LAGUERRE_DUAL_HIERARCHY.md`
itera ese paso: cada integración sube el parámetro Laguerre y reemplaza el error por balances
acumulados \(B_r\) con fórmula aritmética exacta. `147_BALANCE_LAPLACE_JET_FORM.md` convierte esos
balances elevados en jets finitos de una transformada de Laplace truncada en \(s=1\).
`148_A1_FINITE_ARITHMETIC_CERTIFICATE_SCHEMA.md` expande esos jets como sumas finitas explícitas sobre
prime powers y bloques de borde. `149_MOVING_DIAGONAL_A1_GENERATOR.md` escribe la función generadora
de corte fijo \(\mathcal C_T\) y muestra que A1 exige positividad sobre la diagonal móvil \(T=T_n\),
no para un único corte fijo. `150_A1_TAIL_REMAINDER_GENERATOR_IDENTITY.md` fija además la identidad de
signos \(C_n(T)=\lambda_n-\frac14\lambda_n^{\rm arch}-R_n(T)\), que es la forma generadora exacta de
las puertas de margen fuerte y cola unilateral. `151_EXPLICIT_ARCHIMEDEAN_POSITIVE_LOWER_BOUND.md`
provee un \(B_n>0\) explícito con \(B_n\le\lambda_n^{\rm arch}\) para todo \(n\ge8\), cerrando el
input arquimediano de A0. `152_EXPLICIT_PNT_INPUT_ADAPTER.md` fija la forma exacta del PNT explícito
decayente que todavía se debe importar para A0 y registra que una cota relativa constante de Chebyshev
no alcanza para la cola. `153_CUTOFF_COMPARISON_AND_MONOTONICITY_GATE.md` fija la comparación exacta
entre cortes y muestra que mover positividad hasta \(T_n\) requiere una transferencia firmada, no
monotonía formal. `154_CUTOFF_TRANSFER_DUAL_BALANCE.md` integra esa transferencia una vez y la expresa
mediante balance acumulado local y el kernel elevado \(L_{n-1}^{(3)}\).
`155_A1_WEIL_SQUARE_ROOT_GATE.md` aísla la puerta Weil: la fórmula explícita lineal ya no basta; se
necesita una factorización positiva tipo autocorrelación del test compacto.
`156_A1_LAGUERRE_N_RECURRENCE_GATE.md` deriva una recurrencia exacta en \(n\) para \(C_n(T)\); una
inducción requeriría controlar firmadamente el forzamiento de esa recurrencia.
`157_ARCHIMEDEAN_FORCING_AUDIT.md` corrige la parte arquimediana de ese forzamiento: es explícita,
pero no una fuente automática de positividad, de modo que la obstrucción inductiva es el forzamiento
firmado completo. `158_A1_GATE_TRIAGE_AND_PRIORITY.md` separa reescrituras equivalentes de puertas
positivas reales y fija la prioridad: balance aritmético local/inducción o positividad global
Euler--Gamma. `159_INDUCTIVE_FORCING_CERTIFICATE_SCHEMA.md` expande el forzamiento inductivo como
certificado finito de prime powers más corrección arquimediana explícita.
`160_INDUCTIVE_FORCING_GENERATOR.md` empaqueta el mismo forzamiento como generador de corte fijo,
dejando la inducción como positividad de sumas de coeficientes más transferencia de corte.
`161_LI_TOEPLITZ_MOMENT_GATE.md` formula la ruta Schur como positividad Toeplitz infinita de momentos;
los chequeos finitos no bastan sin identificación cofinal no circular. Si no aparece
un teorema nuevo en una de las puertas registradas, el frente sigue abierto aunque todas sus
reformulaciones algebraicas estén normalizadas.
`291_ABEL_DEFECT_CONSTANT_THRESHOLD_LEDGER.md` añade una puerta Fejer ejecutable para el subcarril
Abel: si existe la medida incremental positiva \(\nu_g\) y se prueba
\[
  \int(P_{1-1/n}-\alpha F_n)_+\,d\nu_g\le d_\alpha\log n+B_D,
  \qquad d_\alpha<1-\alpha/2,
\]
junto con la cota Abel radial efectiva, entonces el margen fuerte queda cerrado para
\[
  n\ge N_\infty(\alpha)
  =
  \max\left(N_0,2,\left\lceil
  \exp\left({3+B_\alpha\over(q_\alpha-1/2)}\right)\right\rceil\right),
\]
y sólo queda el certificado finito de `261`.  Si el defecto tiene constante mayor o igual a
\(1-\alpha/2\), la transferencia Abel--Fejer no supera la constante arquimediana \(1/2\).
`292_POISSON_WEIGHTED_BAD_SET_ANTI_CONCENTRATION_GATE.md` localiza ese defecto en los conjuntos
\[
  B_{n,\tau}=\{F_n<\tau P_{1-1/n}\}.
\]
La desigualdad puntual
\[
  (P_{1-1/n}-\alpha F_n)_+
  \le
  P_n{\bf1}_{B_{n,\tau}}
  +(1-\alpha\tau)_+P_n{\bf1}_{B_{n,\tau}^c}
\]
reduce el input faltante a probar que la medida incremental positiva no carga esos bad sets con masa
Poisson de coeficiente logarítmico mayor que
\[
  b_\tau<1-\alpha/2-(1-\alpha\tau)_+.
\]
Ésta es la forma anti-concentración local del subcarril Abel.
`293_FEJER_POISSON_BAD_SET_GEOMETRY_GATE.md` calcula la geometría
determinista de esos conjuntos: para \(0<\tau\le1\), \(B_{n,\tau}\)
contiene ventanas de radio \(\sqrt{\tau}/(2n)\) alrededor de cada raíz
\(n\)-ésima no trivial.  Por tanto el input de `292` no es una pequeñez
geométrica automática; debe ser una anti-concentración aritmética de la
medida incremental verdadera.
`294_LOCAL_DENSITY_NOT_BAD_SET_ANTI_CONCENTRATION_NO_GO.md` separa la ruta
de densidad local de la ruta Abel-defecto: una cota logarítmica local cerca
de \(1\) puede coexistir con spikes positivos dispersos en ceros móviles de
Fejer, y esos spikes fuerzan coeficientes bad-set arbitrariamente grandes.
Por tanto `292` requiere información aritmética independiente.
`295_BOUNDED_DENSITY_BAD_SET_ZERO_COEFFICIENT_GATE.md` elimina una parte
inofensiva: si \(d\nu=h\,dm\) y \(0\le h\le H\), entonces
\[
  \int_{B_{n,\tau}}P_{1-1/n}\,d\nu\le H.
\]
La masa absolutamente continua acotada aporta coeficiente logarítmico cero;
la obstrucción Abel-defecto queda en la parte singular o de densidad no
acotada de la medida incremental.
`311_BAD_SET_CARLESON_WINDOW_SUFFICIENT_CONDITION.md` añade la dirección
suficiente local: \(B_{n,\tau}\) queda cubierto por ventanas de escala
\(1/n\) alrededor de todas las raíces \(n\)-ésimas, y si
\[
  \nu_g(I_{n,k}(\tau))\le { \rho_\tau\log n+B_\tau\over n}
\]
para todas esas ventanas con
\[
  C_\tau'\rho_\tau<1-{1\over2\tau},\qquad \tau>1/2,
\]
entonces se obtiene el bound de bad set de `292`, luego el umbral Abel de
`291`, y finalmente margen fuerte eventual más resto finito `261`.  El
input abierto pasa a ser una estimación Carleson aritmética para la medida
incremental real.
`296_WEIGHTED_CARLESON_BAD_SET_GATE.md` afina esa condición suficiente:
basta probar la suma ponderada
\[
  \sum_{k=0}^{n-1}{n\,\nu_g(I_{n,k}(\tau))\over1+\kappa(k)^2}
  \le \beta_\tau\log n+B_\tau,
\]
con \(C_\tau\beta_\tau<1-1/(2\tau)\).  Esta forma sigue el peso Poisson y
no exige controlar uniformemente ventanas lejanas de \(1\) más de lo
necesario.
`297_CENTRAL_FLOOR_WEIGHTED_BUDGET_GATE.md` combina ese target superior
con el piso central: si el coeficiente local logarítmico es \(a\), cualquier
prueba ponderada viable debe cumplir
\[
  aK(\tau)\le C_\tau\beta_\tau<1-{1\over2\tau}.
\]
Si el piso central ya supera el target derecho, esa elección de \(\tau\)
no puede cerrar el subcarril Abel-defecto.
`316_CENTRAL_FLOOR_COMPATIBILITY_WINDOW.md` muestra que ese presupuesto no
queda vacío sólo por la ventana central en el rango vivo \(a\le1\).  Para
\(\tau=3/2\), se prueba
\[
  K(3/2)<{2\over3}
  =
  1-{1\over2(3/2)}.
\]
Por tanto \(aK(3/2)\) queda estrictamente debajo del target para todo
\(a\le1\).  Así el piso central consume presupuesto pero no refuta por sí
solo la ruta Abel-defecto.
`314_BAD_SET_CENTRAL_WINDOW_LOG_MASS_FLOOR.md` añade el costo necesario
central de esa misma elección: como
\[
  {F_n(1)\over P_{1-1/n}(1)}\to {1\over2},
\]
toda \(\tau>1/2\) mete una ventana de escala \(1/n\) alrededor de \(1\) en
\(B_{n,\tau}\).  Si localmente \(h\ge aL-B\), esa ventana fuerza
\[
  b_\tau\ge a\,{2\over\pi}\arctan c_\tau
\]
para toda escala central \(c_\tau\) donde el cociente límite quede debajo
de \(\tau\).  Por tanto el subcarril Abel debe presupuestar una cuota
central además de controlar las ventanas de raíces no triviales.
`312_LOG_KERNEL_ABEL_DEFECT_MODEL_LEDGER.md` calibra el caso modelo opuesto:
para \(L=-\log|2\sin(\theta/2)|\),
\[
  \int(P_{1-1/n}-\alpha F_n)_+L\,dm
  =
  \kappa_\alpha\log n+o_\alpha(\log n),
\]
con \(\kappa_\alpha\) dado por una integral explícita en la variable de
escala \(u=n\theta\).  Por tanto el defecto del log-kernel puro es
computable; lo que sigue abierto es controlar el remanente Euler--Gamma
real cerca de los ceros móviles de Fejer.
`315_LOG_KERNEL_DEFECT_OPTIMIZATION_LEDGER.md` compara ese coeficiente con
el presupuesto \(1-\alpha/2\).  El modelo logarítmico puro deja margen
principal positivo; por ejemplo, cerca de \(\alpha=3/4\),
\[
  \kappa_\alpha\approx0.3520355633,\qquad
  1-\alpha/2-\kappa_\alpha\approx0.2729644367.
\]
Así, la ruta Abel--Fejer sigue viable en constantes: lo pendiente es
controlar el remanente en los bad sets.
`325_EG_REMAINDER_BAD_SET_CERTIFICATE_SCHEMA.md` empaqueta ese pendiente
como certificado efectivo: si
\[
  d\nu_g=aL\,dm+d\rho,
\]
hay que certificar el defecto del log-kernel con coeficiente
\(\kappa_\alpha^+\), y para \(\rho\) una cota directa de defecto o una cota
bad-set ponderada que dé \(e_\alpha\), con
\[
  a\kappa_\alpha^+ + e_\alpha<1-\alpha/2.
\]
Entonces `291` da el umbral explícito de margen fuerte y `261` el resto
finito.

`328_POISSON_LOWER_NOT_LOG_DOMINATION_NO_GO.md` separa crecimiento Abel de
dominación logarítmica: la masa puntual \(\delta_1\) tiene
\(\int P_{1-1/n}\,d\delta_1=2n-1\ge\log n\), pero no domina \(aL\,dm\) en
arcos alejados de \(1\) donde \(L>0\).  Por tanto la descomposición
\(d\nu_g=aL\,dm+d\rho\) debe probarse aparte o reemplazarse por una cota
directa del defecto total.

`313_DIRECT_A1_TERMWISE_SIGN_OBSTRUCTION.md` fija la auditoría directa:
en el bloque alto,
\[
  \Omega_n(m)=
  e^{-T_n}L_{n-1}^{(1)}(T_n)
  -
  e^{-\log m}L_{n-1}^{(1)}(\log m).
\]
Como \(e^{-u}L_{n-1}^{(1)}(u)\) tiene lóbulos alternantes, estos
coeficientes no tienen un signo fijo.  Por tanto A1 directa no se cierra
por positividad término a término; necesita compensación firmada global.
`298_LAGUERRE_LOBE_BLOCK_COMPENSATION_GATE.md` convierte esa compensación
en el criterio mínimo por bloques: al partir \([T_8,T_n]\) según el signo
de \(G_{n-1}(T_n)-G_{n-1}(u)\), el bloque alto queda como
\[
  H_n^+-H_n^-,
\]
y el certificado directo exige
\[
  H_n^+-H_n^-+B_n^{\rm base}\ge0.
\]
Las cotas de carga absoluta \(H_n^++H_n^-\) no bastan sin dominancia
orientada.
`299_LOBE_BLOCK_PARTIAL_SUMMATION_GATE.md` aplica sumación parcial exacta
en cada lóbulo directo: cada bloque se convierte en un término principal
explícito más una integral firmada del error de Chebyshev.  Por tanto el
input faltante es una desigualdad orientada de discrepancia sobre los
lóbulos de Laguerre, no una envolvente absoluta.
`329_DIRECT_A1_ORIENTED_CHEBYSHEV_MINIMAL_THEOREM.md` fija esa obligación
en su forma terminal:
\[
  \sum_jH_{n,j}^{\rm err}
  \ge
  -B_n^{\rm base}-\sum_jH_{n,j}^{\rm main}.
\]
También descarta el atajo por monotonicidad: \(\Lambda\ge0\) y \(\psi\)
creciente sólo dan masa positiva; no dicen en qué lóbulos de signo cae esa
masa.  Lo que falta es ubicación aritmética orientada respecto de los
lóbulos de Laguerre.
`320_TAIL_LOBE_ONE_SIDED_ENVELOPE_CRITERION.md` da la forma suficiente
análoga en el carril tail: cotas inferiores para
\(E(e^u)=\psi(e^u)-e^u\) sobre lóbulos positivos de
\(K_n=e^{-u}L_{n-1}^{(2)}\), y cotas superiores sobre lóbulos negativos,
cierran el índice \(n\) cuando su cota orientada \(\mathcal L_n\) cumple
\[
  \mathcal L_n\ge\left(d_n-\frac14\right)A_n.
\]
Las envolventes simétricas vuelven al no-go absoluto; las útiles tienen que
ser unilaterales y orientadas por signo de lóbulo.
`322_TAIL_LOBE_INTERVAL_CERTIFICATE_SCHEMA.md` convierte esa forma en un
certificado intervalar auditable: para cada \(n\) hay que aislar todos los
ceros de cola de \(L_{n-1}^{(2)}\), encerrar los pesos de lóbulo, probar
cotas unilaterales orientadas para \(E(e^u)\), y comparar con
\((d_n-1/4)A_n\).  Para cerrar todos los índices hace falta cubrir cada
\(n\ge8\), o dar un umbral efectivo más resto finito completo.
`326_TAIL_LOBE_STEP_ENVELOPE_EFFECTIVE_REDUCTION.md` vuelve finita la parte
de lóbulos acotados: \(\psi(e^u)-e^u\) decrece entre logaritmos de prime
powers y salta hacia arriba por \(\Lambda(m)\), de modo que las constantes
unilaterales exactas en un lóbulo acotado se obtienen revisando sólo esos
endpoints finitos.  Lo que queda como input infinito real es el teorema
unilateral ponderado en el rayo final, más cobertura de todos los índices o
umbral efectivo con resto finito.
`327_FINAL_RAY_ABSOLUTE_COST_GATE.md` permite usar una envolvente simétrica
PNT/VK sólo en ese rayo final como coste negativo explícito:
\[
  \mathcal R_{n,\infty}(W)=
  \int_{\xi_{n,*}}^\infty W(u)e^{-u}|L_{n-1}^{(2)}(u)|\,du.
\]
No revive el no-go de envolventes simétricas globales: los lóbulos
acotados siguen siendo aritmética orientada, y este coste final debe ser
absorbido punto a punto por el margen.
`321_DIRECT_TAIL_LOBE_TRANSFER_GATE.md` bloquea el atajo circular entre el
lenguaje directo compacto y el lenguaje tail: aunque
\[
  {d\over du}\bigl(G_{n-1}(T_n)-G_{n-1}(u)\bigr)
  =
  e^{-u}L_{n-1}^{(2)}(u),
\]
esa relación no preserva positividad y trae términos de borde.  La
dominancia de lóbulos directos y la dominancia tail son equivalentes sólo
después de usar \(C_n(T_n)=\lambda_n-A_n/4-R_n(T_n)\); usar esa equivalencia
para probar una desde la otra sería circular.
`171_LOCAL_COUNTERTERM_RIGIDITY_NO_GO.md` añade que el pareamiento cruzado indefinido no puede
repararse después de fijar la diagonal de Li mediante un contratérmino positivo: si el término añadido
se anula en todos los tests \(1-z^n\), se anula en todo \((z-1)\mathbb C[z]\).
