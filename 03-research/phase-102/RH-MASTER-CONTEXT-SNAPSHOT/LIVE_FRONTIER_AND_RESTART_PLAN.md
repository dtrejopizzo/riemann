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

5. **Probar la desigualdad firmada global. — ABIERTO / FUERZA-RH.**
   
   Para todo \(n\ge8\), demostrar
   \[
      \boxed{
      \lim_{\varepsilon\downarrow0}
      \int_1^\infty(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy
      \ge-\lambda_n^{\rm arch}}
   \]
   desde datos aritméticos. Éste es el núcleo central. Su fuerza-RH no autoriza suspenderlo: obliga a
   encontrar una identidad, desigualdad unilateral, principio variacional o estructura geométrica que
   lo demuestre.

6. **Justificar uniformemente el límite de borde. — ABIERTO.**
   
   La estimación que pruebe el punto 5 debe ser uniforme en \(\varepsilon\downarrow0\). Hay que exhibir
   una cantidad integrable o una cancelación exacta que permita pasar al límite sin reemplazar el
   integrando por su valor absoluto y sin perder el término \(-n\).

7. **Controlar todas las escalas de \(n\). — ABIERTO.**
   
   La prueba debe cubrir simultáneamente:
   
   - el rango finito posterior a \(I_-\);
   - la zona de transición del kernel Laguerre;
   - el régimen oscilatorio \(\log m\lesssim4n\);
   - la cola \(\log m\gtrsim4n\);
   - el límite \(n\to\infty\).
   
   Puede hacerlo mediante un teorema global que evite esta partición, pero no puede dejar constantes
   dependientes de \(n\) que destruyan la desigualdad final.

8. **Conservar el signo antes de estimar. — ABIERTO.**
   
   Debe construirse un pareamiento o una descomposición para la cual la excursión negativa sea visible
   sin aplicar
   \[
      \left|\int gh\right|\le\int|g||h|.
   \]
   El objeto buscado debe retener conjuntamente polo, Gamma, primos, conjugación y borde. La pérdida de
   signo por shells o por primos individuales no puede recuperarse después.

9. **Probar el mecanismo discriminante desde datos aritméticos. — ABIERTO / FUERZA-RH.**
   
   Sea cual sea la forma elegida en los puntos 5--8, sus hipótesis deben demostrarse para \(\zeta\)
   desde una construcción independiente. No basta definir una métrica, medida, corriente o
   factorización que exista exactamente cuando \(\lambda_n\ge0\). Si el mecanismo mismo equivale a RH,
   debe ser demostrado: no será descartado por esa equivalencia.

10. **Demostrar sensibilidad fuera de línea dentro de una clase tipada. — CONTROL DE VALIDEZ ABIERTO.**
    
    Construir una clase \(\mathcal C_{\rm Euler}\) con datos de Dirichlet, factor Gamma, ecuación
    funcional y continuación comunes. El nuevo mecanismo debe:
    
    - funcionar para los datos de \(\zeta\);
    - ser compatible con un control sobre la línea;
    - fallar estructuralmente para un miembro aritmético fuera de línea.
    
    Este punto no es una premisa lógica del criterio de Li y no debe insertarse artificialmente en la
    demostración. Es un control de validez del mecanismo: impide invertir el programa en una identidad
    incapaz de distinguir el fenómeno buscado.

11. **Cerrar el ensamblaje Li. — ABIERTO, dependiente de 4--9.**
    
    Combinar los certificados de \(1\le n\le7\) con el teorema uniforme para \(n\ge8\), concluir
    \(\lambda_n\ge0\) para todo \(n\), verificar las hipótesis de la versión utilizada del criterio de
    Li y deducir RH. Este último paso es corto, pero sólo queda cerrado cuando no arrastra ninguna
    hipótesis pendiente.

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

14. **Cerrar el error de truncación firmado. — ABIERTO.**
    
    Para toda truncación utilizada, demostrar que la contribución omitida conserva la desigualdad
    unilateral o converge con un resto firmado controlable. Una cota de norma de la cola no basta si es
    mayor que el margen arquimediano.

15. **Cerrar la uniformidad \((n,\varepsilon,X)\). — ABIERTO.**
    
    Declarar el orden de límites y demostrar las estimaciones uniformes necesarias para
    \(X\to\infty\), \(\varepsilon\downarrow0\) y \(n\to\infty\). No se acepta intercambiar estos límites
    por convergencia puntual.

16. **Convertir el mecanismo en el teorema global del punto 5. — ABIERTO.**
    
    El resultado final del carril no debe ser una nueva coordenada: debe entregar literalmente
    \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\) para todo \(n\ge8\).

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
