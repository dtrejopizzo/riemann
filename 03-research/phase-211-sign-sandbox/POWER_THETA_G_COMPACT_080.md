# POWER_THETA_G_COMPACT_080 — Curvatura restante y tres generadores en TODO el rango admisible

Estado: **PROVED, certificado constructor completo exit0/PASS y reproducción root92790 exit0/FULL PASS, auditoría independiente aprobada.** Véase `POWER_THETA_G_COMPACT_AUDIT_080.md`. No se prueban cuatro generadores, todos los órdenes ni una nueva ventana temporal. Papers intactos.

## 1. Obligación exacta y antecedentes

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID y CROSSWORD-TO-D; leídos073–079 y las auditorías correspondientes.073 prueba M creciente, estrictamente cóncava y M(0)=0 para la media del tilt theta real.079 demuestra, bajo esas propiedades, que todos los bloques de tres nodos de un intervalo son semidefinidos positivos SI Y SÓLO SI

    g(x)=a sqrt(x)/M(sqrt(x))−1

es cóncava en sus cuadrados, con a=M'(0)>0. No exige concavidad de1/b ni el resultado adicional077 para su prueba mínima.078 ya prueba g''<0 para u=sqrt(x)>=63/2. Para exponentes admisibles A=u+1/2>1, sólo falta1/2<u<63/2, no el origen u=0.

Aquí se prueba esa ÚNICA obligación compacta, con todas las constantes y la función aritmética completas. No se seleccionan triples ni autovalores, no se certifica una sucesión de nuevas dimensiones y no se infiere el signo por muestras. El cambio frente a los encierros anteriores es usar jets sólo en centros EXACTOS y un resto analítico uniforme de Cauchy, derivado de la densidad theta positiva; no evaluar jets de la función deflatada sobre bolas anchas cerca de su cancelación polar.

## 2. Curvatura escalar y regularización completa en A=1

Sea Z(u)=∫_R Phi(t)e^(ut)dt y M=Z'/Z, como073. Con c=M(u),d=M'(u),e=M''(u), definir

    Delta(u)=c²+ucd+u²ce−2u²d².

La derivación exacta da

    g''(u²)=−a Delta(u)/(4u³c³).                     (CURVATURE)

Para u>=1/2, c>0. Por tanto basta probar Delta>0. La fórmula aritmética de CONE001 identifica Z, salvo constante positiva irrelevante para M, con la función entera real

    E(A)=A[1+(A−1)zeta_deflate(A)]Gamma(A/2)exp(−A logpi/2),
    A=u+1/2,
    zeta_deflate(A)=zeta(A)−1/(A−1).

La deflación NO significa (A−1)zeta(A). El producto entero Q=1+(A−1)zeta_deflate(A) es el que evita evaluar el polo en A=1. Allí Q=1 y E(1)=1. El uso de A=1 como extremo regular no afirma convergencia separada del polar y el peine del test de borde: los exponentes originales de la conclusión son estrictamente mayores que1.

El significado de deflate y las series se cotejaron con la API instalada python-flint0.9.0, las cabeceras locales de FLINT y la documentación oficial:

- https://arblib.org/arb_poly.html
- https://flintlib.org/doc/arb_poly/_arb_poly_zeta_series.html

La documentación especifica la función ζ(s,a)+1/(1−s) cuando deflate es no nulo. Los autotests E(1) y la coincidencia de jets regularizados con la fórmula ordinaria en A=2 sólo validan implementación; la identidad matemática proviene de la deflación explícita, no de esos dos tests.

## 3. Un bound real uniforme para los discos de Cauchy

Fijar r=1/16. Para todos los centros c0 en[1/2,63/2], c0+r+1<=32+9/16<33+1/2. La monotonía M de073 y la fórmula aritmética en A=34 dan

    M(t)<=M(33+1/2)
      <1/34+1/33+(1/2)log[34/(2pi)]
      <2/32+(1/2)log6 <1,

para1/2<=t<=c0+r+1. Se descartó sólo el término aritmético negativo de M para este UPPER. Se usaron pi>3, psi(y)<=log y y log6<9/5; esta última se verifica con una suma Taylor positiva de exp(9/5)>6. No se acota el término racional por2/32 punto a punto a tasas pequeñas: primero se usa la monotonía hasta el ancla33+1/2.

Por ello

    Z(c0+r+1)/Z(c0)
      =exp[int_(c0)^(c0+r+1)M(t)dt]
      <exp(17/16)<3.                               (RATIO)

Para la última constante basta e<11/4 y exp(1/16)<16/15, que dan exp(17/16)<44/15<3. El bound e<11/4 se demuestra sumando hasta grado3 y pagando desde grado4 la geométrica de razón1/5: e<=8/3+5/96<11/4.

## 4. Bound complejo completo de Delta, sin jets intervalares

Para |z−c0|<=r y k>=0, positividad de Phi y |t|^k<=k!exp(|t|) dan

    |Z^(k)(z)|
      <=k![Z(Re z+1)+Z(Re z−1)]
      <=2k! Z(c0+r+1)<6k! Z(c0).

La última comparación usa la paridad de Phi y la monotonía de Z respecto del módulo de su argumento real. El segmento entre c0 y z permanece en el disco, por lo que

    |Z(z)−Z(c0)|<=2rZ(c0+r+1)<(3/8)Z(c0),
    |Z(z)|>(5/8)Z(c0).

Así M=Z'/Z y sus derivadas son analíticas allí y satisfacen

    |Z^(k)(z)/Z(z)|<(48/5)k!, k=1,2,3,
    |M|<10,
    |M'|<120,
    |M''|<2700.

En efecto se usan M'=Z''/Z−(Z'/Z)² y M''=Z'''/Z−3Z'Z''/Z²+2(Z'/Z)³. Los bounds intermedios exactos son48/5,96/5,288/5. Como |z|<32 en todos estos discos,

    |Delta(z)|
      <10²+32·10·120+32²·10·2700+2·32²·120²
      <60000000=:B.                                (CAUCHY-BOUND)

No se invoca un signo de la forma sobre datos complejos. Sólo se deriva un error analítico absoluto para la MISMA función aritmética entera que se evalúa sobre el eje real.

## 5. Partición fija y resto exacto

Los4096intervalos iguales cubren[1/2,63/2]. Tienen radio h=31/8192 y centros exactos

    c_j=[4096+(2j+1)31]/8192, j=0,...,4095.

Para Delta(c_j+t)=ΣD_k(c_j)t^k, los coeficientes D_k están normalizados por k!. Cauchy y CAUCHY-BOUND dan, uniformemente en |t|<=h,

    |Σ_(k>=17)D_k t^k|
      <= B(h/r)^17/(1−h/r)=epsilon,
    h/r=31/512,
    epsilon=5285183618944392932503807265625/
            41901009533176678637026095660718210485846016
      <10^(−12).                                   (TAIL)

Es un error de TODA la cola de Taylor, no sólo el siguiente coeficiente. El verificador utiliza la fracción exacta TAIL, no el upper decimal10^(−12), al comprobar el signo.

En cada centro, ball arithmetic a256bits encierra D0,...,D16 de la función completa. El assert suficiente es

    D0.lower−Σ_(k=1)^16 |D_k|.upper h^k−epsilon>0.     (PANEL)

No se evalúa la función en una malla y se interpola sin resto. PANEL demuestra el signo en cada intervalo entero, incluidos sus extremos.

## 6. Implementación, fallos de encierro y reproducción

El código es tools/power_theta_g_compact_080_verify.py. Usa arb_series REAL, precisión256bits y cap20: logE tiene coeficientes hasta grado19; M hasta18; M'' hasta16; Delta conserva los17coeficientes necesarios. Se exige Delta.prec>=17 y finitud de TODOS D0,...,D16. Antes de logE se exige E0>0. La función real entera se evalúa únicamente en centros exactos, con jets de funciones especiales y errores completos de FLINT; no se trunca una suma de primos sin cola.

La partición4096, el dominio, la precisión256 y el margen estricto>0 se fijaron antes de ejecutar y no se ajustaron a resultados. Los primeros encierros intentaron usar el coeficiente6 sobre una bola de parámetro. El encierro directo y sus correcciones Taylor2/Taylor4 fallaron por pérdida de dependencia cerca de la cancelación del polo de ζ. Los valores centrales eran positivos, pero esos FAIL NO probaron el signo en los paneles ni constituyeron un contraejemplo de curvatura. Se conservaron historia y alcance. Aumentar sólo el orden de jets no resolvía esa causa: el último fallo intervalar fue en el panel1, con un resto excesivo.

La representación final elimina TODAS las evaluaciones de ζ sobre bolas de parámetro y las sustituye por el resto externo TAIL demostrado arriba. Se fijaron r=1/16,B=60000000,grado16/cap20 y se auditaron sus fórmulas ANTES de la corrida de esa representación. Fue una corrección matemática del encierro del mismo objetivo, no un barrido de hipótesis o parámetros de signo.

Ejecutar

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_g_compact_080_verify.py

La corrida43260 terminó exit0, PASS de regularización y PASS de TODOS los4096paneles. El SHA256 del script que terminó es

    640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc.

Root92790 reprodujo independientemente el certificado completo: exit0/FULL PASS4096 y el mismo hash. No se modificó ese script mientras se ejecutaba. Los asserts son pruebas con intervalos rigurosos y constantes racionales; no se empleó un autovalor ni un número flotante como premisa de signo.

## 7. Empalme y conclusión sobre tres generadores

PANEL prueba Delta>0 en[1/2,63/2] y CURVATURE da g''<0 allí.078 prueba la misma curvatura para u>=63/2 mediante bounds aritméticos uniformes. Por tanto

    g''(x)<0 para TODO x>=1/4.                        (GLOBAL-ADMISSIBLE)

073 aporta todas las propiedades BASE de079. Para cualesquiera tres exponentes distintos A1,A2,A3>1, sus nodos ui=Ai−1/2 son>1/2 y g es estrictamente cóncava en todo su intervalo de cuadrados. El teorema de secantes079 demuestra que

    K_ij=[L(Ai)+L(Aj)]/(Ai+Aj−1), i,j=1,2,3,

es DEFINIDA POSITIVA. Es la forma real COMPLETA de los tres exponenciales, con ARCH, polar y TODOS los contactos. La congruencia diagonal del mapa exterior conserva el signo sobre cualquier combinación real de tres potencias con exponentes>1.

Si algunos exponentes coinciden, se combinan coeficientes y queda el caso de uno o dos generadores probado073: la matriz redundante es semidefinida positiva y la energía es positiva para toda FUNCIÓN representada no nula. No se atribuye energía positiva a un vector no nulo que represente la función cero.

## 8. Límite exacto del avance

El resultado amplía de TODOS los pares073 a TODOS los triples admisibles, no sólo a tasas grandes ya cubiertas por053. No requiere concavidad de1/b. No demuestra cuatro generadores, todos los órdenes ni la envolvente lineal completa; tampoco modifica una ventana T del paper o cierra su signo global. Los papers permanecen intactos.
