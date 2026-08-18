# Phase 104 — cerrar A1

**Fase cerrada.** El objetivo no fue demostrado. El balance vinculante,
las piezas permanentes y el handoff a Phase 105 están en
[`PHASE_104_CLOSURE.md`](PHASE_104_CLOSURE.md). Ningún documento de esta
carpeta puede citarse como prueba de RH.

Objetivo único: probar, incondicionalmente y para todo \(n\ge150\),

\[
\text{(A1)}\qquad
\int_{\log 2}^{T_n}\bigl(\psi(e^u)-e^u\bigr)e^{-u}L^{(2)}_{n-1}(u)\,du
\ \le\ q_n=\tfrac34A_n+1-L_n^{(1)}(\log 2).
\]

Con A0, los certificados finitos \(1\le n\le149\) y la identidad
\(C_n(T)=\lambda_n-\frac14A_n-R_n(T)\) —los tres ya probados— esto cierra \(\Omega_7\)
y por tanto RH. La cadena estable está en la subsección
`The Phase 102--103 direct route`, etiquetas `prop:li-compact-tail`,
`thm:a1-direct-collapse` y `cor:a1-to-omega7` del obstruction ledger.

**Restricción de cierre.** Un cierre condicional para \(n\ge n_{\rm eff}\) más un rango finito
nunca completa RH. A1 debe quedar probada incondicionalmente para todos los índices restantes.

## Corrección vinculante 104_56A: el cutoff es cofinal

La condición de A0 se impone sobre todo el rayo \(u\ge T\). Por tanto, si un cutoff es
admisible, todo cutoff mayor también lo es, y para todo \(T\ge T_n^0\)
\[
 |R_n(T)|\le \frac{A_n}{4(1+T)}.
\]
En consecuencia, si \(\delta_n:=\lambda_n-A_n/4>0\), se puede elegir
\[
 T>\max\left\{T_n^0,\frac{A_n}{4\delta_n}-1\right\}
\]
y entonces \(C_n(T)>0\). El frente cofinal suficiente es, pues,
\[
 \boxed{\;4\lambda_n>A_n\;},
\]
no el margen fijo \(4\lambda_n-A_n\ge A_n/1001\). La constante
\(2002/501\) sigue siendo correcta como suficiente uniforme obtenido del piso bruto
\(T\ge1000\), pero no es intrínseca. La elección adaptada usa la misma holgura que queda por
probar y no constituye un mecanismo para obtenerla.

Hay además una distinción lógica que el registro anterior no hacía: demostrar
\(4\lambda_n-A_n\ge0\) para todo \(n\ge150\) ya da \(\lambda_n>0\) y prueba RH directamente,
aunque la igualdad no baste para deducir A1 en un cutoff finito usando solamente el techo
bilateral de A0. Por tanto se retira la afirmación general de que una conclusión
semidefinida nunca puede cerrar el objetivo maestro; solo era insuficiente para la
transferencia A1 con cutoff prefijado.

## Corrección de cuantificador 104_56: densidad y bloques

Si RH es falsa, los modos transformados de módulo máximo producen excursiones
\(4\lambda_n-A_n<0\) sobre un conjunto sindético de densidad natural positiva. De aquí se
deducen dos criterios equivalentes a RH:

1. \(4\lambda_n>A_n\) fuera de una excepción de densidad logarítmica superior cero;
2. \(4\lambda_n>A_n\) en bloques consecutivos de longitudes no acotadas.

No existe una constante universal positiva para la densidad mala deducible de los axiomas
abstractos de Bombieri--Lagarias; una familia explícita de fases de Fejér hace esa densidad
arbitrariamente pequeña. Esta relajación reduce el objetivo maestro, pero no prueba todavía
ningún bloque bueno nuevo para la zeta. El objetivo literal de Phase 104 —A1 para cada
\(n\ge150\)— permanece abierto.

## Erratum vinculante: signo del coeficiente incompleto

La importación anterior de Lagarias, ec. (1.15)--(1.17), tenía el signo del bloque incompleto
invertido. Con
\[
 k_n(s)=\left(1+\frac1s\right)^n-1,
\]
el residuo de \(k_n(s)(-L'/L)(s+1,\pi)\) en \(s=\rho-1\) es
\(-m_\rho k_n(\rho-1)\). Al conservar también la orientación del contorno, la traducción
corregida en el caso de \(\zeta\) es
\[
 \lambda_n=A_n+\lambda_n(\sqrt n)+O(\sqrt n\log n),
\]
no \(A_n-\lambda_n(\sqrt n)+O(\sqrt n\log n)\). Por tanto el resto pequeño correcto es
\[
 \widetilde\varepsilon_n:=A_n-\lambda_n+\lambda_n(\sqrt n)
 =O(\sqrt n\log n).
\]
La cantidad usada antes,
\[
 \varepsilon_n^-:=A_n-\lambda_n-\lambda_n(\sqrt n),
\]
sigue siendo una identidad exacta, pero
\(\varepsilon_n^-=\widetilde\varepsilon_n-2\lambda_n(\sqrt n)\) y **no** tiene una cota
incondicional \(O(\sqrt n\log n)\). Todo corolario que usaba tal cota, incluido el rango finito
derivado de \(C_*\), queda retirado. Este erratum no toca la identidad prima--Laguerre ni A0--A1.
La prueba de contorno requiere además reparar el tramo horizontal impreso:
se toma primero \(T=2\sqrt n+\varepsilon_n\), donde la razón geométrica es
\(e^{1/4}/2<1\), y se vuelve a \(\sqrt n\) acotando la banda intermedia por
\(O(\sqrt n\log n)\).

## Dónde está el contenido nuevo

`104_00`–`104_03` son gate, normalización y auditoría: consolidan el terreno y traducen con
rigor lo que ya existe en la literatura, sin reclamarlo como frente.
**El trabajo matemático nuevo empezó en `104_10` (M1).** `104_11` cerró ese
mecanismo con un stop-gate exacto. `104_12` auditó el sucesor M5: conserva la
convolución Möbius--divisor firmada, pero no produce una métrica positiva ni una
cota nueva. `104_13` descarta específicamente **positividad de Selberg + fórmula
sumatoria \(O(x)\) + Riccati** como fuente autónoma; no descarta todo posible
teorema acoplado especial para los pesos reales. `104_14` cierra también M3 en su especificación actual: el mapa
estacionario organiza alturas, pero pierde el parámetro radial que determina el
signo. `104_15` prueba que el complejo de Koszul positivo del cubo divisor
cancela los cocientes \(p/q\), pero simultáneamente vuelve nulo-homotópica la
conexión \(M\delta Z\); tampoco es el mecanismo faltante. El siguiente frente deberá aportar una identidad aritmética concreta para
los pesos reales \(\Lambda\), no otra polarización de las mismas formas.
`104_16` ensaya precisamente la jerarquía completa del cociclo de Jordan:
prueba \(\mu*\log^k\ge0\) para todo \(k\), pero su primer jet polar--Euler es
el mismo costo \(C_{n,\varepsilon}\) y pierde el signo ya en grados \(1,6\).
La completación Gamma produce una familia Schur equivalente a RH y la mitad
de completación tiene coeficiente exactamente \(-\Delta D_n/2\); no aparece
una cota intermedia. Tras corregir el signo del bloque incompleto, `104_17`
ataca directamente su cota inferior mediante promedios Abel--Fejér. Prueba
que el germen Abel radial de cada cuarteto es estrictamente positivo incluso
fuera de la línea, mientras sus coeficientes y promedios triangulares pueden
ser exponencialmente negativos. Por tanto la positividad radial no transfiere
el signo que A1 necesita. `104_18` conserva finitos y correlacionados
\(u=c\varepsilon\) en el cociclo Jordan: obtiene una recurrencia y una
renovación exactas, pero el límite es otra vez
\(C_n=\lambda_n^{\rm prime}-\lambda_{n+1}^{\rm prime}\). El orden real, la
monotonía en \(c\) y la anulación idéntica del canal explícito mediante
pesos constantes fallan con testigos exactos. `104_19` incorpora el factor Gamma y elimina la raíz del
medio-cociclo: deriva tres canales finitos exactos, pero su medida polar es
firmada para todo \(c>0\), los canales aislados divergen y el límite vuelve a
ser \(-\Delta D_n\).
`104_20` combina cada torre prima y los tres canales antes de estimar. La
fórmula se factoriza como un cuadrado algebraico exacto \(\mathsf C_p^2\),
pero no como \(\mathsf C_p^*\mathsf C_p\): los bloques aritméticos reales
tienen ambos signos. Muere el signo torre a torre; permanece viva la
desigualdad de la suma multiplicativa global.
`104_21` ejecuta ese gate global: la ley multiplicativa normalizada es
compound-Poisson y ordenada por convolución, pero falla PF2 con un menor
racional de los primos 2 y 3. Más decisivamente, el cociclo completado real
no es completamente monótono: su densidad inversa de Laplace es negativa en
\(x=\frac12\log2\), antes del primer átomo aritmético. Mueren las rutas
PF/TP, variación disminuyente y medida positiva global; queda como sucesor
la identidad global firmada de Stein--Mecke.
`104_22` retiene el factor \((1+T_n)^{-1}\) que la última línea de A0
descartaba. Con él, la A1 original ya no requiere
\(2\lambda_n-A_n\ge0\): basta el margen estrictamente más débil
\(3\lambda_n-A_n\ge0\). El cociclo exacto correspondiente es
\(H_u^3K_u^2\); tres canales Euler y dos Gamma son positivos, y el único
frente restante es controlar globalmente el polo cúbico acoplado.
`104_23` usa además \(T_n\ge1000\): el margen suficiente baja al valor fijo
\(r_*\lambda_n-A_n\ge0\), \(r_*=2002/501\), casi cuártico. Euler y Gamma
siguen siendo positivos para este exponente real por divisibilidad infinita;
el polo se suma como una densidad hipergeométrica firmada. `104_56A` corrige su
interpretación: es el suficiente uniforme asociado al piso bruto, no el frente
intrínseco cuando el cutoff puede aumentarse índice por índice.
`104_24` ejecuta Stein--Mecke sobre el cociclo cúbico. Obtiene cuatro canales
directos con \(L_k^{(1)}\) y una recurrencia global que conserva todos los
otros primos, pero el generador completado es negativo ya en
\(\frac12\log2\), antes del primer átomo primo. Muere el orden positivo del
generador, no la desigualdad firmada especial.
`104_25` aplica Fejér--Carathéodory al mismo cociclo. La identidad produce
exactamente \(3\lambda_n-A_n\), pero la holomorfía necesaria en una sucesión
de discos completos ya equivale a RH. El disco seguro de la serie Euler se
contrae como \((1-c)\varepsilon\) y solo controla medias amortiguadas.
`104_26` prueba que pasar al exponente entero cuatro tampoco crea una suma
de cuadrados: la cuarta potencia local sigue siendo algebraica, falla PF2 y
su parte cuadrática se anula en el límite directo. Su slack
\(4\lambda_n-A_n\ge A_n/1001\) sigue siendo el costo exacto de la
transferencia que fija únicamente \(T\ge1000\), pero `104_56A` retira la
afirmación de que ese slack sea necesario para RH o para un cutoff cofinal
adaptado: basta el signo no negativo para RH y el signo estricto para la
transferencia cofinal a A1.
`104_27` descarta recuperar ese slack declarando favorable el signo de la
cola: bajo el mismo envelope VK hay discrepancias suaves y monótonas con
\(R_n(T)\) de ambos signos. Cualquier signo real debe usar los pesos
\(\Lambda(m)\).
`104_56`--`104_61` cambian por primera vez el cuantificador, en vez de
volver a reformular la misma desigualdad puntual. Bajo \(\neg\mathrm{RH}\),
los modos exteriores dominantes fuerzan excursiones exponenciales sobre un
conjunto sindético. Por ello basta excluir en algunos intervalos largos una
densidad positiva de excursiones más profundas que cualquier barrera
subexponencial. `104_60` lo expresa mediante una barrera unilateral saturada;
`104_61` obtiene el criterio todavía más débil \(\lambda_n\ge-1\) en bloques
de longitud no acotada y una partición acotada de Fermi--Dirac que mide la
densidad logarítmica de las excursiones. Su representación prima--Laguerre
conserva polo, Gamma y todos los pesos \(\Lambda(m)\) dentro de la no
linealidad. La partición exponencial
\(\sum_{n\le X}e^{-t\lambda_n}/n\) queda como auxiliar algebraico más fuerte:
su cota \(O(\log X)\) ya fuerza una cota inferior en cada grado y no explota
la relajación de densidad. Ninguno de los dos límites está probado.
`104_62` lleva Fermi a un producto prima--Laguerre unitario y localiza
exactamente su señal en microfrecuencias \(s\asymp e^{-an}\). La coordenada
diagonal \(s=e^{-nv}\) vuelve fija esa tasa, pero la generatriz solo controla
el producto geométrico de fases: en la frontera todos los poderes de Hadamard
sobreviven y la media aritmética de Fermi queda abierta. `104_63` cierra
también el rescate por energía entre grados: Parseval y
Christoffel--Darboux existen, pero sus piezas reguladas divergen como
\(\varepsilon^{-4N}\) y solo el funcional completo cancela.
`104_64` reemplaza la media logarítmica de Cesàro por una media Abel exacta:
basta una subsucesión radial prefijada, aunque el falsificador muestra que la
capa de Fourier debe alcanzar \(s=\exp(-c/h)\). `104_65` prueba que ninguna
diferencia, promedio móvil o filtro local fijo elimina las excursiones
dominantes salvo que aniquile también el contraejemplo. `104_66` diagonaliza
el regulador con \(\varepsilon(h)=e^{-1/(100h)}\), de modo que cada escala
usa una serie de Euler absolutamente convergente; separar polo y primos sigue
costando una precisión \(\exp(-C/h^2+O(1/h))\). `104_67` refuerza la
obstrucción: bajo no-RH hay excursiones exponenciales de ambos signos, cada
una sindética y de densidad positiva. Finalmente, `104_68` elimina el
selector existencial de bloques: las ventanas fijas
\(I_L=[L^2,L^2+L-1]\) distinguen RH mediante una suma Fermi o un producto
finito que tiende a \(1\) bajo RH y a \(0\) bajo no-RH. `104_69` da la
versión global finita en \(\log X\), también sobre una diagonal Euler única.
La auditoría `104_69B` separa estos repackagings de los antecedentes
Bombieri--Lagarias y de la sumabilidad clásica. `104_70` prueba que bajar la
temperatura de Fermi subexponencialmente conserva el detector, pero no puede
amortiguar el polo con un regulador que tienda al borde: ambas obligaciones
son cuantitativamente incompatibles. `104_71` da la dualidad entrópica exacta
de las ventanas: las correlaciones pagan su multiinformación y el optimizador
refactoriza, pero basta una cota variacional con slack
\(\exp(o(L^2))\) en una sola subsucesión para probar RH. `104_72` vuelve
al detector acotado mediante una razón de presiones: cada excursión profunda
aporta solo un factor \(e^\tau\), de modo que se conserva la densidad y no la
profundidad. La ganancia es real, pero la transición sigue dependiendo de la
diferencia prima--polo completa con precisión aditiva \(O(1)\).
`104_73` prueba que ni la representación positiva de Bernstein ni un ancho
variable eliminan esa pared: toda anchura que detecta cada modo exterior deja
un costo relativo \(\exp\{-X^2/100+o(X)\}\). `104_74` reformula la misma
presión mediante un semigrupo de Hadamard y potenciales de Jensen; el contorno
exterior queda polinómico, pero toda tasa exponencial reside exactamente en la
suma finita de residuos interiores. Finalmente, `104_75` sustituye la
transición \(O(1)\) por el blanco unilateral más débil obtenido hasta ahora:
basta que los sobrepasos prima--polo de tamaño \(e^{\sqrt X}\) tengan densidad
logarítmica nula. La transformada poissonizada de primer orden se cierra en
forma de Bessel, pero el cuarteto demuestra que no controla ese evento raro.
`104_76` muestra que la cola de ceros con
\(\gamma>X^{1/4}\) es \(O(X\log X\,e^{\sqrt X/2})\), uniformemente en
\(n\le X\): toda posible violación profunda queda localizada en el bloque
\(\gamma\le X^{1/4}\). `104_77` obtiene la localización complementaria por
contorno: la parte exterior es polinómica y la dificultad completa es una
suma finita de residuos interiores; Jensen, Cartan y Turán detectan esos
residuos, pero no los eliminan.
`104_78` construye un falsificador Euler reticular con renovación unitaria,
torres completas, pesos positivos, ecuación funcional y ley prima de grado:
su cola profunda tiene densidad \(1/4\). No conserva el PNT continuo ni el
factor Gamma, y por eso delimita —sin reemplazar— el problema real.
`104_79` vuelve a los \(\Lambda(m)\) ordinarios: la representación exacta
por la ley zeta tiene colas prima y semiprima de ambos signos con primeros
excesos \(\ge e^{X^2/500}\). Así, truncar o concentrar cada cola por
separado pierde la cancelación que determina la media.

## Documentos

| file | rol | contenido |
|---|---|---|
| `104_00_BIBLIOGRAPHY_GATE.md` | gate (bloqueante) | veredicto duplica / no-duplica por mecanismo, con etiqueta condicional/incondicional explícita |
| `104_01_THETA_FAMILY.md` | normalización | familia \(C_n^\theta\), reserva \(q_{n,\theta}\), \(T_n(\theta)\) efectivo, transporte firmado \(\Delta_{n,\theta}\) |
| `104_02_LAGARIAS_TRANSLATION.md` | **erratum de signo vinculante** | coordenada corregida \(-\lambda_n(\sqrt n)+\widetilde\varepsilon_n\); retirados el antiguo Teorema A y el corolario finito basado en \(C_*\) |
| `104_03_CONTOUR_RESIDUE_AUDIT.md` | auditoría | contorno de \(R(t)\), polos triviales, identidad de Cayley, mapa estacionario |
| `104_10_M1_COLLECTIVE_KERNEL.md` | mecanismo auditado | identidad colectiva y no-go local-PSD |
| `104_11_M1_GLOBAL_MAX_STOP_GATE.md` | **stop-gate exacto** | el compensador es la energía `max`; cancelación de Hessianas y colapso al funcional lineal original |
| `104_12_M5_MOBIUS_DIVISOR_AUDIT.md` | **identidad exacta + stop-gate de Gram** | convolución Möbius--divisor en grado; comparación con E70.11--12 y 103_71; el inverso de Möbius no puede ser un adjunto positivo |
| `104_13_M5_SELBERG_RICCATI_GATE.md` | **recurrencia exacta + stop-gate de escala** | recurrencia Selberg--Riccati en grado; la colisión regulada cuesta \(\varepsilon^{-n-1}\) y la sumatoria \(O(x)\) pierde \(\exp((1+o(1))n\log n)\) |
| `104_14_M3_NONLOCAL_STOP_GATE.md` | **forma completada + stop-gate bulk** | A1 como autocorrelación de Weil menos reserva y cola; un cuarteto off-line y un divisor crítico con las mismas alturas dan signos opuestos |
| `104_15_EULER_GAMMA_COMPLEX_GATE.md` | **construcción mínima + stop-gate cohomológico** | complejo de Koszul positivo en los posets \(\{1,p\}\), \(\{1,p,q,pq\}\); cancela cocientes mixtos, pero hace exacto \(M\delta Z\) |
| `104_16_JORDAN_COCYCLE_ATTACK.md` | **jerarquía positiva + stop-gate Cayley/Schur** | cociclo \(\zeta(s-u)/\zeta(s)\), \(\mu*\log^k\ge0\); el emparejamiento polar pierde signo, el presupuesto es \(-\Delta D_n/2\) y la contractividad completada equivale a RH |
| `104_17_INCOMPLETE_LI_ABEL_STOP_GATE.md` | **teorema Abel + stop-gate Tauberiano** | fórmulas exactas para el cuarteto incompleto y sus promedios; positividad Abel radial compatible con coeficientes exponencialmente negativos |
| `104_18_CORRELATED_SHIFT_STOP_GATE.md` | **identidad finita + stop-gate de orden** | recurrencia exacta para \(u=c\varepsilon\), forma de renovación firmada; el límite vuelve a \(C_n\), el orden real no controla coeficientes y pesos constantes finitos no anulan idénticamente el canal explícito |
| `104_19_THREE_CHANNEL_BRANCH_FREE_GATE.md` | **expansión exacta + stop-gate polar** | cociclo \(Y(s-u)/Y(s)\) en tres canales Jordan--Beta; medida polar firmada, divergencia al separar y límite exacto \(-\Delta D_n\) |
| `104_20_LOCAL_TOWER_SQUARE_AND_GLOBAL_GATE.md` | **factorización local + gate global vivo** | segunda diferencia exacta de \(b_u(p^k)\), cuadrado operacional \(\mathsf C_p^2\), testigo de ambos signos por fondos; la cancelación entre todas las torres queda como frente |
| `104_21_GLOBAL_COMPOUND_POISSON_TP_GATE.md` | **producto global + stop-gate PF/CM** | ley compound-Poisson exacta sobre todos los primos; menor PF2 racional \(-1/2916\); densidad inversa completada negativa antes de \(\log2\); sucesor Stein--Mecke identificado |
| `104_22_CUBIC_MARGIN_REDUCTION.md` | **reducción nueva + gate cúbico vivo** | A0 retenido da \(|R_n|\le A_n/[4(1+T_n)]\); \(3\lambda_n-A_n\ge0\) implica la A1 original; cociclo \(H_u^3K_u^2\) y normalización directa con límite \(-(3\lambda-A)\) |
| `104_23_NEAR_QUARTIC_REAL_MARGIN.md` | **reducción uniforme desde el piso de A0 + gate real vivo** | \(r_*=2002/501\) es suficiente usando solo \(T_n\ge1000\); potencias reales Euler--Gamma positivas; polo exacto \(-rce^{-q}{}_1F_1(1-r;2;cq)\) |
| `104_24_DIRECT_CHANNELS_AND_STEIN_GATE.md` | **identidad global + stop-gate Stein positivo** | cuatro canales \(L_k^{(1)}\), base \(k+1\), recurrencia Stein--Mecke; densidad completada negativa antes de \(\log2\), sin refutar el signo global especial |
| `104_25_FEJER_CARATHEODORY_GATE.md` | **positividad analítica + stop-gate de holomorfía** | Fejér convierte \(\Re\Phi\le1\) en el margen cúbico; holomorfía de los discos regulados \(\Longleftrightarrow\) RH; testigo exacto contra transferencia desde discos menores |
| `104_26_QUARTIC_SQUARE_STOP_GATE.md` | **cuarta potencia + stop-gate de cuadrados** | cuarta diferencia local, menor PF2 exacto, bloque real de ambos signos y falsificador off-line; \(D_n^{[4]}\ge A_n/1001\) es solo el costo suficiente del cutoff fijado por el piso \(T\ge1000\), no una coercividad intrínsecamente necesaria |
| `104_27_TAIL_SIGN_NO_GO.md` | **auditoría A0+ + stop-gate de signo** | dos discrepancias bajo el mismo envelope VK producen colas opuestas; versión suave compatible con monotonicidad final |
| `104_28_FIXED_VECTOR_BRIDGE_AND_WHITENING_STOP_GATE.md` | **puente hard-edge exacto + stop-gate de whitening** | \(g_n=e^{-x/2}L_{n-1}^{(1)}=\sum_{k<n}e^{-x/2}L_k\); forma prima--polo sobre un solo rayo; el archimedeano Toeplitz tiene \(A_1<0\), por lo que no existe el cociente espectral propuesto |
| `104_29_LOG2_COMPENSATED_SPLIT_GATE.md` | **corte exacto en el primer primo + stop-gate de masas** | generador compensado, bloques \(J_n^<+J_n^\ge\); la comparación de masas da un falso positivo y la desigualdad ponderada exterior recompone exactamente \(D_n^{[r]}\ge0\) |
| `104_30_FLAG_HARD_EDGE_REFERENCE_AND_SCHUR_GATE.md` | **referencia positiva exacta + gate espectral** | la bandera diagonal satisface \(A_{\rm flag}[g_n]=A_n\); polarización prima--polo y blanqueo finito exactos; el diagnóstico espectral es favorable pero Schur/Gershgorin exige controlar \(\Delta^2(A-\lambda)\) |
| `104_31_EPSILON_FLOW_OBSERVABILITY_STOP_GATE.md` | **flujo birth--death exacto + stop-gate de dominio** | \(c'=Qc\), \(Q=-M_x\); el test backward exige \(\varepsilon<1/2\) y el operador Euler separado exige \(\varepsilon>1/2\); \(A_{\rm flag}\) no es invariante ni mueve el umbral |
| `104_32_HIGHER_PRIME_POWER_BUDGET.md` | **separación exacta + presupuesto explícito** | \(H_{\ge2}=-\sum_{j\ge2}\mu(j)(-\zeta'/\zeta)(js)\); polo \(j=2\) en \(z=-1\), cota \(\lvert P_{n-1}^{(\ge2)}(1)\rvert<14n+1\) y reducción cuártica exacta al canal primos--polo |
| `104_33_FLAG_SYMBOL_BOUNDARY_RESIDUE_GATE.md` | **símbolo exacto + stop-gate frontera--residuos** | \(h(z)=-\zeta'/\zeta((1-z)^{-1})-1/(s-1)\); el momento de bandera es frontera más residuos off-line; un cuarteto conserva la frontera real y cambia el momento exponencialmente |
| `104_34_FLAG_PREFIX_CURVATURE_AND_ADJACENT_SCHUR_GATE.md` | **curvatura refutada + gate de Schur adyacente** | el certificado outward prueba \(\nabla_c^2(\lambda-501A/2002)_{220}<0\); la compresión \(\mathrm{span}\,\{g_n,\phi_n\}\) da el criterio coercivo suficiente \(4H_nd_n\ge(H_n+d_n-H_{n+1})^2\), todavía abierto uniformemente |
| `104_35_SIMPLE_PRIME_POLE_SELBERG_GATE.md` | **correlación \(\theta\) exacta + stop-gate Selberg simple** | \(B_n^{(p+\mathrm{pole})}=-n-\int(\theta(e^u)-e^u)e^{-u}L_{n-1}^{(2)}\); identidad colectiva solo primos/semiprimos; núcleo inverso no coercivo y testigo sobre soporte primo real |
| `104_36_SIMPLE_PRIME_CHOLESKY_DOMAIN_GATE.md` | **Cholesky colectivo exacto + stop-gate de dominio** | \(B_{n,a}^{(p+\mathrm{pole})}=\langle V_{n,a},g_n\rangle\) y norma large-sieve exacta para \(a>2\); residuos de ceros impiden continuar la norma a \(a=1\), con divergencia \(\gg(a-1)^{-1}\) incluso por ceros críticos |
| `104_37_TAPERED_SELBERG_HANKEL_GATE.md` | **taper Schur exacto + stop-gate Hankel de dos puntos** | el test óptimo es \(ae^{-au}[L_{n-1}^{(1)}+tL_n+t(t-1)]\); después de invertir Selberg, todo \(t\) tiene un menor de cola con término principal \(8^d-9^d<0\), también sobre logaritmos de primos reales |
| `104_38_CANONICAL_SELBERG_SQUARE_CANCELLATION_GATE.md` | **completación Schur exacta + stop-gate del cuadrado canónico** | el término \(\mu*\mu\) de Selberg cancela idénticamente el cuadrado de la inversión; si se lo reserva para pagar el Schur, el kernel residual tiene diagonal \(-a^{2n+2}e^{-2aR}R^{2n}/[4d(n!)^2](1+o(1))<0\), incluso en un átomo \((\log p)\delta_{\log p}\) |
| `104_39_ADJACENT_RICCATI_TRIANGLE_STOP_GATE.md` | **factorización triangular exacta + stop-gate de suficiencia** | el determinante adyacente equivale a desigualdades triangulares entre \(\sqrt{H_n},\sqrt{d_n},\sqrt{H_{n+1}}\); un cuarteto crítico mantiene el margen escalar y rompe el gate, por lo que éste es estrictamente más fuerte que el objetivo |
| `104_40_CANONICAL_EULER_RESOLVENT_STOP_GATE.md` | **resolvente del rayo fijo + stop-gate de módulo** | la optimización sobre todo multiplicador positivo conserva primos--polo hasta el último paso, pero su costo óptimo es \(\int|\widehat g_n|^2|M|\), que diverge logarítmicamente por los ceros críticos; los ceros off-line aparecen antes como residuos de cruce |
| `104_41_FULL_MANGOLDT_PHASE_HOMOTOPY_GATE.md` | **fase Mangoldt completa + stop-gate de homotopía** | para \(M_\Lambda=(s-1)^{-1}+\zeta'/\zeta\), polo y todos los \(p^k\) acoplados, la fase exacta prueba \(|\mathcal B_{n,a}|\le3n\) en \(a\ge4\); al bajar a \(a=1\), cada cero derecho cruza en \(a=2\Re\rho\) y aporta el residuo de `104_33`; un cuarteto racional conserva toda la fase crítica y cambia el momento exponencialmente |
| `104_42_DEGREE_ADAPTED_NONCOMMUTATIVE_PRECONDITIONER_GATE.md` | **óptimo cuadrático no conmutativo + stop-gate de grado** | el ínfimo algebraico sobre todo \(R>0\) es \(|\langle v,g\rangle|\); la proyección a los primeros \(n\) Laguerre conserva la fase, pero el dato nuevo reaparece con factor \(\sqrt{n/2}>1\) |
| `104_43_ZETA_SIZE_BIAS_DIVISOR_MARTINGALE_GATE.md` | **factorización size-biased exacta + stop-gate probabilístico** | \(N^*=DN'\), con \(D\) de ley \(\Lambda(d)d^{-s}\) y selector \(\Lambda(d)/\log N\); el comparador polar es un split Gamma uniforme, pero el orden cambia de signo, la comparación marginal es exactamente \(R\) y Efron--Stein separado pierde \(\varepsilon^{-2n+2}\) |
| `104_44_DIVISOR_MARKOV_LAGUERRE_TRANSPORT_GATE.md` | **transporte \(\Lambda*1=\log\) + stop-gate de escala** | el operador divisor es Markov pero tiene brecha cero aun en media cero; la adición de Laguerre conserva la convolución completa y su continuo Gamma contrae por grado, pero cambiar al test no escalado cuesta exactamente \((2/\varepsilon-1)^{n-1}\) |
| `104_45_CROSSED_DIVISOR_GAMMA_STEIN_GATE.md` | **Stein cruzado exacto + kernel firmado canónico** | cualquier coupling recompone el mismo kernel de colas \(K_s\), que cambia de signo alrededor de \(\log2\); sobre exponenciales sí vale \(R(q)<0\), pero no hay completa monotonía y sobre Laguerre la identidad vuelve exactamente a \(B_n\) |
| `104_46_FIXED_LAGUERRE_MARKOV_EXTREMAL_GATE.md` | **stop-gate específico del vector fijo** | para \(s>1\) próximo a uno, el propio Laguerre centrado satisface \(Q_r(s)\to1\) en el selector divisor, mientras el comparador Gamma satisface \(Q_r^\Gamma(s)\to0\); una brecha de Markov no puede dar la coercividad buscada |
| `104_47_SIZE_BIASED_HOMOTOPY_FLUX_GATE.md` | **flujo exacto de la homotopía** | \(a\partial_a\mathcal B_{n,a}=n(\mathcal B_{n+1,a}-\mathcal B_{n,a})\); su flujo integrado es equivalente sin resto al margen, y el cuarteto off-line aparece como un pulso exponencial |
| `104_48_PRIME_TOWER_SIGNED_COERCIVITY_GATE.md` | **cierre por torre + gate de multiplicidad unitaria** | \(\Phi_n\) tiene una fórmula de Poisson y una cota unilateral en dirección inútil; constancia por torre + PNT admite un testigo en \(n=151\), por lo que solo sobrevive la renovación unitaria global \(\Lambda*{\bf1}=\log\) |
| `104_49_UNIT_DIVISOR_RENEWAL_SIGNED_GATE.md` | **Palm unitario + stop-gate momento--cumulante** | el exponente marcado es uniforme dentro de cada torre y distingue a \(\omega_c\), pero selector y transporte cancelan exactamente el momento total grado por grado; su combinación Laguerre vuelve a \(B_n\) |
| `104_50_SECOND_ORDER_UNIT_PALM_COVARIANCE_GATE.md` | **Palm unitario de segundo orden + gate de orientación** | la covarianza centrada cancela todas las torres distintas; el defecto no centrado las retiene, pero su cuadrado completado es varianza más el cuadrado del margen y pierde exactamente la orientación |
| `104_51_MOBIUS_INVERTED_LCM_RESERVE_GATE.md` | **inversión doble del Gram `lcm` + gate de reserva** | \(K=Z^TWZ\) y \(M^TKM=W\) diagonalizan exactamente el kernel; la reserva infinita es indefinida en un vector de dos niveles, y su cutoff local tiene signos opuestos para el Laguerre real \(P_{150}\) en \(p=2,7\) |
| `104_52_CONNECTED_TWO_TOWER_FLUX_GATE.md` | **Hessiano completado + cancelación conectada** | el margen exacto tiene Hessiano torre--polo--Gamma, pero todos los pares entre primos distintos y los cruces primo--polo se cancelan; el Hessiano y el cociclo Laguerre tienen ambos signos |
| `104_53_CONNECTED_CUMULANT_CANCELLATION_THEOREM.md` | **clasificación Hopf de identidades aditivas** | todo observable polinómico aditivo en los momentos es combinación lineal de cumulantes; para la ley zeta cada cumulante queda dentro de una sola torre, de modo que una identidad multi-torre exacta no puede dejar una reserva desconectada |
| `104_54_GIBBS_CHERNOFF_UNIT_PALM_GATE.md` | **gate no aditivo Gibbs--Chernoff** | para todo \(n\ge4\), \(s>1\) y \(t\ne0\), \(\mathbb E_s e^{tD_{n,s}}=\infty\); fibras primas y semiprimas producen colas opuestas de orden \((\log N)^n\), y el bound variacional es infinito |
| `104_55_THREE_MARK_UNIT_PALM_ORIENTATION_GATE.md` | **Palm de tres marcas + gate cúbico** | tercer momento, determinante y tercera diferencia carecen de signo; la polarización orientada es exactamente varianza positiva por el margen desconocido, y la asimetría unitaria real ya cambia de signo entre \(N=6\) y \(N=18\) |
| `104_56_DENSITY_RELAXED_LI_CRITERION.md` | **teorema de cuantificador relajado** | si RH falla, el margen cuártico falla sobre un conjunto sindético de densidad positiva; RH equivale al margen fuera de densidad logarítmica cero o en bloques buenos no acotados; no hay densidad universal desde los axiomas BL |
| `104_56A_CUTOFF_FREEDOM_AUDIT.md` | **erratum de frente intrínseco** | A0 es cofinal en el cutoff; \(4\lambda_n>A_n\) permite un cutoff adaptado que cierra A1, mientras \(2002/501\) solo codifica el piso \(T\ge1000\) |
| `104_56B_DENSITY_NOVELTY_AUDIT.md` | **gate bibliográfico específico** | modos dominantes y negatividad exponencial i.o. son conocidos; no se localizaron en las fuentes primarias revisadas los refuerzos de densidad positiva, sindeticidad, bloques ni el lift Fermi prima--Laguerre, sin reclamar prioridad exhaustiva |
| `104_57_LOW_ZERO_BLOCK_BUDGET.md` | **mapa cuantitativo del bloque bajo** | la cola regularizada \(|\gamma|\ge\sqrt n\) reproduce \(A_n\) con error \(O(\sqrt n\log n)\); el bloque restante tiene \(\asymp\sqrt n\log n\) etiquetas y se fija el presupuesto exacto de todo sucesor |
| `104_58_TRANSLATIONAL_DENSITY_ATTACK.md` | **ventanas de grado + no-go de homotopía** | toda ventana traslacional fija conserva una clase de fallos off-line de densidad positiva; la cota de fase en \(a\ge4\) no se transporta a \(a=1\) sin los residuos cruzados |
| `104_59_PRELOG_MAJORISATION_GATE.md` | **auditoría Schur/Karamata** | la mayorización pre-log clásica ya estaba contenida en 104_21/43/44; el test Laguerre tiene curvatura de ambos signos y el selector divisor real invierte orientación |
| `104_60_NONLINEAR_DEGREE_BARRIER_CRITERION.md` | **criterio de gran desviación en el grado** | RH equivale a que una barrera saturada de las excursiones \(4\lambda_n-A_n\le-b_n\), \(b_n=e^{o(n)}\), tenga media tendiendo a cero en algunos intervalos largos |
| `104_61_SUBEXPONENTIAL_DENSITY_AND_NONLINEAR_PARTITION.md` | **criterio débil + particiones emparejadas** | basta \(\lambda_n\ge-1\) en bloques no acotados; la partición Fermi acotada detecta exactamente densidad logarítmica positiva y tiene representación prima--Laguerre completa; la partición exponencial es un criterio auxiliar coeficiente a coeficiente |
| `104_62_UNITARY_FERMI_MICROFREQUENCY_GATE.md` | **lift unitario + stop-gate de microfrecuencia** | Fourier conserva todos los canales como fases de módulo uno, pero una excursión de profundidad \(Y\) vive en \(s=O(Y^{-1})\); el escalado diagonal solo controla el producto geométrico, no la media Fermi |
| `104_63_CROSS_DEGREE_H2_ENERGY_GATE.md` | **Parseval/CD entre grados + no-go cuantitativo** | la energía diádica detecta exactamente el primer polo interior; el kernel CD es positivo, pero polo², primos² y cruce son de orden \(\varepsilon^{-4N}\) y no pueden separarse |
| `104_64_LOG_ABEL_FERMI_BOUNDARY_GATE.md` | **criterio Abel logarítmico + gate de capa** | la media Fermi de Cesàro y la de Abel son equivalentes y basta una subsucesión fija; el falsificador exige microfrecuencias hasta \(s=\exp(-c/h)\) |
| `104_65_LOCAL_FILTER_LONG_BLOCK_GATE.md` | **clasificación de filtros locales** | toda diferencia, promedio móvil o filtro finito conserva excursiones negativas sindéticas salvo aniquilación exacta de los modos dominantes; el cuarteto exhibe esa pérdida de información |
| `104_66_DIAGONAL_ABEL_REGULATOR_GATE.md` | **diagonal Euler exacta + stop-gate de separación** | \(\varepsilon(h)=e^{-1/(100h)}\) aproxima uniformemente los grados \(n\le1/h\) dentro de una serie Euler convergente; polo y primos requieren cancelación relativa superexponencial |
| `104_67_TWO_SIDED_EXCURSION_GATE.md` | **excursiones bilaterales** | bajo no-RH existen conjuntos sindéticos de densidad positiva con \(\lambda_n\ge cR^n\) y con \(\lambda_n\le-cR^n\); barreras subexponenciales superiores, inferiores o bilaterales en bloques no acotados equivalen a RH |
| `104_68_DETERMINISTIC_BLOCK_POLYMER_CRITERION.md` | **ventanas deterministas + partición finita** | RH equivale a que la suma Fermi sobre \([L^2,L^2+L-1]\) tienda a cero, o a que su producto tienda a uno; \(\varepsilon_L=e^{-(L^2+L-1)/100}\) da una única sucesión Euler convergente, pero el gas refactoriza y no crea cancelación nueva |
| `104_69_FINITE_LOGX_DIAGONAL_FERMI_CRITERION.md` | **criterio finito en \(\log X\) + diagonal Euler** | RH equivale a una sola media logarítmica Fermi; \(\varepsilon_X=e^{-X/100}\) sustituye simultáneamente los primeros \(X\) grados por una fórmula prima--Laguerre absolutamente convergente, con error exponencial |
| `104_69B_COUNTEREXAMPLE_ROUTE_NOVELTY_AUDIT.md` | **gate bibliográfico Fermi/bloques** | separa el modo exterior conocido y la sumabilidad log-Cesàro/Abel clásica de la sindeticidad/densidad potencialmente sustantiva; Fermi, producto, ventanas cuadráticas y diagonal Euler se registran como corolarios o repackagings no localizados exactamente, sin reclamar prioridad |
| `104_70_VARIABLE_TEMPERATURE_FERMI_GATE.md` | **temperatura variable + no-go polar** | temperaturas subexponenciales conservan el detector de todos los modos exteriores, pero toda escala que amortigua el polo con \(\varepsilon_n\to0\) pierde necesariamente esa sensibilidad; el condicionamiento relativo no mejora |
| `104_71_ENTROPIC_BLOCK_VARIATIONAL_ATTACK.md` | **dualidad Bernoulli--entropía + gate de interacción** | la partición de bloques es una esperanza Bernoulli con factor telescópico; Gibbs la convierte en una cota uniforme sobre \(G_{L,q}\), admisible con slack \(\exp(o(L^2))\), pero la multiinformación elimina toda correlación y el optimizador refactoriza |
| `104_72_BOUNDED_PRESSURE_RATIO_ATTACK.md` | **razón de presiones saturada + gate de transición** | una razón de dos particiones limita cada sitio a \([1,e^\tau]\) y conserva solo la densidad de excursiones; el lift diagonal es exacto, pero decidir la transición \(z\asymp1\) exige la diferencia prima--polo con error aditivo \(O(1)\) |
| `104_73_BERNSTEIN_PRESSURE_WIDTH_GATE.md` | **Bernstein exacto + gate de ancho variable** | la presión es una mezcla positiva de probabilidades Poisson; no admite mayorante afín global no trivial y toda anchura que conserva todos los modos exteriores mantiene el condicionamiento cuadrático prima--polo |
| `104_74_HADAMARD_JENSEN_PRESSURE_GATE.md` | **semigrupo Hadamard + Jensen + residuos interiores** | el exponencial de Hadamard tiene radio positivo exactamente bajo RH; Jensen representa la presión por cruces de anillos, mientras un contorno seguro deja toda tasa exponencial en una suma finita de polos interiores |
| `104_75_POISSON_LOGX_HARD_TRANSITION_GATE.md` | **transición dura + gate profundo de densidad** | RH equivale a densidad logarítmica nula de sobrepasos prima--polo \(\ge e^{\sqrt X}\); poissonización localiza los grados y da una identidad de Bessel para el primer momento, pero el cuarteto prueba que ese momento no controla la cola no lineal |
| `104_76_DEEP_TAIL_HEIGHT_LOCALIZATION.md` | **localización de altura + gate de momentos** | los ceros con \(\gamma>X^{1/4}\) aportan \(O(X\log X\,e^{\sqrt X/2})\); bajo RH parcial hasta \(X^{1/4}\) el observable profundo es idénticamente cero, y todo obstáculo queda en el bloque bajo |
| `104_77_CARTAN_TURAN_DEEP_TAIL_GATE.md` | **contorno seguro + gate Cartan--Turán** | el error exterior es \(O(n^5\log^2n)\) y toda cola profunda reside en una suma finita de polos interiores; Jensen, Cartan y Turán no la anulan, y un cuarteto con continuación positiva en el rayo real conserva densidad profunda \(1/8\) |
| `104_78_UNIT_RENEWAL_EULER_DEEP_TAIL_FALSIFIER.md` | **falsificador Euler unitario reticular** | renovación, torres unitarias, positividad, ecuación funcional y una ley prima de grado exponencialmente precisa aún permiten ceros off-line y densidad profunda \(1/4\); el modelo no satisface el PNT continuo ni contiene el Gamma de Riemann |
| `104_79_ZETA_LAW_DEEP_TRUNCATION_GATE.md` | **ley zeta exacta + gate de truncación** | \(Q-p\) es la esperanza de un defecto prima--polo con \(\Lambda\) real; sus excesos positivo y negativo sobre \(e^{\sqrt X}\) son al menos \(e^{X^2/500}\) en la diagonal, por lo que concentración o truncación separada no transporta la media |
| `104_80_MAXIMAL_SIGNED_LAMBDA_IDENTITY_GATE.md` | **identidad firmada máxima + polo no removible** | Möbius--Laguerre recompone exactamente \(-\partial_z\log\{(s-1)\zeta(s)\}\); cada cero \(\Re\rho>1/2+\varepsilon\) deja un polo interior de residuo \(-m_\rho\) y coeficientes \(m_\rho z_\rho^{-n}\), de modo que ningún reagrupamiento exacto elimina la obstrucción |

| 104_81_ON_OFF_LINE_DEEP_OBSERVABLE_CONTROLS.md | **controles on/off-line del observable profundo** | un cuarteto crítico da densidad \(0\) exactamente y uno exterior da \(1/8\), incluso con el regulador diagonal; dos modelos Euler positivos dan respectivamente \(0\) y \(1/4\), validando el detector pero sin probar el límite para los \(\Lambda(m)\) ordinarios |

## Reglas de proceso

1. Pre-registro: enunciado + **enumeración explícita de axiomas e inputs** + falsificador
   off-line construido para satisfacer exactamente esos axiomas.
2. Nunca valores absolutos sobre el kernel. Polo + Γ + primos + conjugación + borde acoplados
   hasta después de estimar.
3. \(q_n\) exacto, nunca la forma asintótica \(\frac38 n\log n\).
4. Erratum vinculante: \(\lambda_n^{\rm prime}=-n+\int(\psi-y)f'=\int(\psi-y+1)f'\).
   El borde \(-n\) no se descarta.
5. Etiquetado condicional/incondicional explícito en todo enunciado importado.
6. Aritmética racional con intervalos outward en todo certificado.
7. Ledger adversarial al cierre, estilo `103_13`.

## Tools

`cd tools && python3 <file>` — Python puro + numpy, sin dependencias externas, igual que
phase-103. `m1_global_hessian_check.py` y `jordan_cocycle_sign_gate.py` usan
solamente aritmética racional `Fraction` para sus decisiones de signo;
`incomplete_abel_stop_gate_check.py` hace lo mismo para el testigo de `104_17`.
`three_channel_cocycle_check.py` verifica con `Fraction` la convolución en
potencias primas y las identidades polares de `104_19`.
`local_tower_square_check.py` verifica exactamente los operadores y el
umbral de signo local de `104_20`.
`global_cocycle_probe.py` reproduce el diagnóstico Cauchy/Borwein de la suma
global; es `float64`, no un certificado.
`global_compound_poisson_tp_check.py` usa `Fraction` para el menor PF2 de dos
primos y registra el certificado integral exacto de la desigualdad `atanh`
de `104_21`; no toma decisiones de signo en coma flotante.
`cubic_cocycle_probe.py` compara dos radios de Cauchy para el cociclo
\(Y_r(s-u)/Y_r(s)\); es un diagnóstico `float64`, nunca un certificado. Para
\(r\notin\mathbb Z\) usa logaritmos principales punto a punto, no una rama
analítica desenrollada; por eso sus filas no enteras son solo exploratorias y
no se citan como evidencia.
`near_quartic_margin_check.py` verifica con `Fraction` el valor
\(r_*=2002/501\), la igualdad límite de A0, los signos binomiales del polo y
doce coeficientes de su suma hipergeométrica; no prueba el signo global.
`fejer_caratheodory_gate_check.py` verifica con `Fraction` la identidad de
coeficientes de `104_25` y el testigo \(R=1/2\), \(\Phi(z)=6z^4\), para el que
la norma local es \(3/8\) pero \(q_4=-1\).
`quartic_square_stop_gate_check.py` verifica con `Fraction` el testigo
cuártico de grado dos, la relación exacta entre \(D^{[r_*]}\) y \(D^{[4]}\),
y la fase off-line del índice \(150\).
`fixed_vector_bridge_check.py` verifica con `Fraction` la identidad
Laguerre--prefijo y la telescopía Toeplitz--Fejér.
`log2_compensated_split_check.py` verifica la compensación en cero, el
orden exacto \(\varepsilon^{-n}\) de los momentos separados y el signo
estricto de la densidad antes del primer primo.
`flag_hard_edge_spectrum.py` construye y diagonaliza las secciones blanqueadas
de `104_30`; usa dos extracciones Cauchy/FFT en `float64` y es solamente un
diagnóstico, nunca un certificado.
`epsilon_flow_observability_gate_check.py` usa exclusivamente `Fraction` para
verificar la recurrencia de Laguerre, el flujo polar, la generatriz racional
del test transportado y la fuga exacta \(M(M-1)=22350\) de la bandera en
\(M=150\).
`higher_prime_power_budget_check.py` verifica con `Fraction` la
descomposición del polo \(j=2\), sus coeficientes paritarios y el slack
racional de los umbrales \(e^{28032}\) y \(e^{112116}\).
`flag_symbol_residue_check.py` verifica con racionales gaussianos la
identidad exacta frontera--residuos para el cuarteto \(w=i/2\), incluido
que su par derecho aporta \(-Q_n\) y que el logaritmo derivado del cuarteto
es puramente imaginario sobre la línea crítica.
`flag_prefix_curvature_gate.py` usa el generador Hasse--eta outward de
`103_51` para certificar \(\nabla_c^2H_{220}<0\) y, en el mismo rango,
\(\mathcal T_{219}>2220\), sin `float` en los signos.
`flag_prefix_adjacent_schur_diagnostic.py` compara dos radios Cauchy/FFT,
localiza los bloques de curvatura negativa y mide el determinante de Schur
adyacente; es solo diagnóstico `float64`.
`simple_prime_pole_selberg_check.py` verifica con `Fraction` la identidad
de borde Laguerre, su masa exacta \(n\), y la expansión centrada de Selberg
para el canal de primos simples.
`simple_prime_cholesky_gate.py` verifica con racionales gaussianos y
`Fraction` las transformadas de Laplace de Laguerre, el polo continuo y
el cuarteto \(w=i/2\), \(\rho=(4+2i)/5\): en \(n=152\) el residuo tiene
amplitud \(1-2^{-152}\), crecimiento \(e^{3x/10}\) y contribución de Li
negativa.
`tapered_selberg_hankel_gate_check.py` verifica con `Fraction` la
polarización tapered, el término obligatorio \(t(t-1)\), la identidad de
Schur en ambos gauges y el menor principal \(8^d-9^d<0\); no usa signos
en coma flotante.
`canonical_selberg_square_gate_check.py` verifica con `Fraction` la
cancelación exacta del cuadrado Selberg, la respuesta Laguerre de la entrada
cruzada, el grado dominante negativo del kernel Schur residual y el defecto
de colisión \(-2n^2a^4\); no aproxima primos ni \(\zeta\).
`adjacent_riccati_gate_check.py` verifica con `Fraction` la factorización
triangular del determinante adyacente, un cuarteto crítico que conserva
todos los márgenes positivos pero rompe ese determinante, y el cruce exacto
del cuarteto racional off-line
\(\rho=16/41+(20/41)i\).
`canonical_euler_resolvent_gate_check.py` verifica con racionales
gaussianos el cruce off-line, el multiplicador residual y la optimización
de Young para resolventes positivos; su tabla `asinh` solo ilustra la
divergencia logarítmica probada en `104_40`.
`full_mangoldt_phase_homotopy_gate_check.py` verifica con `Fraction` la
cota racional de fase, el conteo \(\mathrm{TV}(W_n)=8n\), la ley de
cruce \(a=2\Re\rho\), la fase crítica invariante del cuarteto \(w=i/2\) y
su defecto exponencial en \(n=152\).
`degree_adapted_noncommutative_gate_check.py` verifica con `Fraction` el
óptimo cuadrático no conmutativo para productos internos de ambos signos,
la compresión Toeplitz por grado, el coeficiente defectuoso \(n/2\) y el
cuarteto racional off-line de `104_42`.
`zeta_size_bias_martingale_gate_check.py` verifica con enteros y `Fraction`
la desintegración size-biased, los signos opuestos del selector divisor en
\(2\) y \(30\), y las constantes líderes de la pérdida Efron--Stein.
`divisor_markov_laguerre_check.py` verifica con `Fraction` la identidad
divisor, la adición y dilatación de Laguerre, y la contracción exacta del
comparador Gamma; no evalúa ceros ni toma decisiones en punto flotante.
`crossed_divisor_gamma_stein_gate_check.py` verifica la identidad de segmento
orientado, la derivada Laguerre, la cancelación de símbolos y el fallo exacto
de completa monotonía registrado en `104_45`.
`fixed_laguerre_markov_extremal_check.py` verifica las identidades de
dilatación y el cociente Gamma exacto de `104_46`; la transferencia PNT del
saddle se prueba analíticamente en el documento.
`size_bias_homotopy_flux_gate_check.py` verifica la ley diferencial, el
canal polar y el pulso gaussiano racional del cuarteto de `104_47`.
`prime_tower_signed_coercivity_gate_check.py` verifica las identidades de
torre, los átomos de fase desplazados y el testigo alternante \(n=151\).
`unit_divisor_renewal_signed_gate_check.py` verifica la marca Palm uniforme,
la cancelación momento--cumulante, los dos signos del defecto unitario en
grado 151 y la pérdida de uniformidad del selector desplazado.
`second_order_unit_palm_covariance_check.py` verifica el Palm cuadrático, el
kernel `lcm`, la descomposición bilineal completada y el falsificador racional.
`mobius_inverted_lcm_reserve_gate_check.py` verifica \(K=Z^TWZ\), su inversión
doble, la indefinitud del kernel infinito y los dos signos locales certificados
del vector \(P_{150}\) en torres primas reales.
`connected_two_tower_flux_gate_check.py` verifica la cancelación conectada,
el Hessiano torre--polo--Gamma, su cambio de signo y el cociclo Laguerre.
`connected_cumulant_cancellation_check.py` verifica con `Fraction` la
aditividad de cumulantes hasta orden doce y las cancelaciones desconectadas
en órdenes bajos; la clasificación general se prueba en `104_53`.
`gibbs_chernoff_unit_palm_gate_check.py` verifica los coeficientes líderes de
las fibras prima y semiprima que fuerzan la divergencia bilateral de Gibbs.
`three_mark_unit_palm_orientation_check.py` verifica el Palm cúbico, el factor
polar seis, la polarización orientada, los dos sesgos aritméticos y los signos
de la tercera diferencia Laguerre.
`cutoff_freedom_audit_check.py` verifica con `Fraction` la monotonía de
\(r_{\max}(T)\), la identidad \(r_{\max}(1000)=2002/501\) y el cutoff adaptado.
`density_relaxed_li_criterion_check.py` verifica la orientación de Cayley, el
cuarteto racional y la familia periódica de Fejér que impide una densidad mala
universal. `low_zero_block_budget_check.py` verifica las equivalencias del
bloque \(|\gamma|<\sqrt n\) y las cotas de activación por cuarteto.
`translational_density_attack_check.py` verifica exactamente que toda ventana
fija conserva el falsificador \(w=2i\). `prelog_majorisation_gate_check.py`
certifica los dos signos de curvatura y la inversión de orientación aritmética.
`nonlinear_degree_barrier_check.py` verifica con racionales gaussianos que la
barrera saturada detecta exactamente la clase \(n\equiv0\pmod4\) del cuarteto y
que su media tiende a \(1/4\). `subexponential_density_partition_check.py`
certifica la barrera polinómica, la ausencia de bloques buenos de longitud
cuatro y la incompatibilidad con el germen Abel positivo del mismo cuarteto.
`unitary_fermi_microfrequency_check.py` verifica las generatrices armónica y
no armónica de Laguerre, el polo regulado y la escala exponencial del cuarteto;
su cuadratura de Fourier es diagnóstica. `cross_degree_h2_energy_check.py`
certifica exactamente Christoffel--Darboux y el polo de Laplace, y comprueba
diagnósticamente la normalización de cuarta raíz para un polo interior.
`log_abel_fermi_boundary_check.py` verifica el límite Fermi \(1/4\) del
cuarteto, la masa armónica por progresiones y la transición
doblemente logarítmica de la nueva coordenada Abel; sus límites se prueban
en `104_64`.
`diagonal_abel_regulator_gate_check.py` verifica la fórmula polar cerrada,
la constante diagonal \(C=1/100\), la escala \(C/h^2\) y la estabilidad de
un modo exterior desplazado de `104_66`.
`local_filter_long_block_check.py`, `two_sided_excursion_check.py` y
`deterministic_block_polymer_check.py` verifican respectivamente la
clasificación de filtros finitos, los dos signos del cuarteto y las
identidades exactas suma--producto--polímero de las ventanas cuadráticas.
`finite_logx_diagonal_fermi_check.py` verifica la versión finita de la
diagonal, el umbral \(X=70\), el valor \(1/4\) del cuarteto y el costo
polar \(e^{X^2/100}\) de `104_69`.
`variable_temperature_fermi_gate_check.py` verifica la caracterización
exacta del regulador polar, la incompatibilidad temperatura--detección, el
cuarteto y la escala diagonal de `104_70`.
`entropic_block_variational_check.py` verifica con racionales la identidad
Bernoulli telescópica de `104_71`, y numéricamente la dualidad de Gibbs, la
regla de cadena entrópica, el polinomio Laguerre combinado y el falsificador.
`bounded_pressure_ratio_check.py` verifica las identidades finitas de la
razón acotada de `104_72`, la constante aguda de sensibilidad
\(\tanh(\tau/4)\), la densidad \(1/4\) del cuarteto y el costo diagonal
\(e^{-X^2/100+O(1)}\) de resolver la transición al separar canales.
`bernstein_pressure_width_check.py` verifica la identidad de Bernstein, sus
signos, el mayorante de Mellin, el cambio de curvatura y la incompatibilidad
anchura--polo de `104_73`. `hadamard_jensen_pressure_check.py` comprueba las
identidades Hadamard--Jensen y el costo exponencial de truncación de `104_74`.
`poisson_logx_hard_transition_check.py` verifica los sandwiches de nivel, la
transformada de Bessel, el promedio Poisson del polo y los límites
\(4,1/4,1/8\) del cuarteto en `104_75`.
`deep_tail_height_localization_check.py` verifica la geometría de cuartetos,
la escala \(X^{1/4}\), la cola muy alta y la separación exponencial de
`104_76`. `cartan_turan_deep_tail_check.py` verifica la continuación
racional positiva, los signos por clases residuales y la densidad profunda
\(1/8\) de `104_77`.
`unit_renewal_euler_deep_tail_falsifier.py` verifica las multiplicidades
de collares, renovación, ecuación funcional, modo Li dominante, densidad
\(1/4\) y la falla del PNT continuo del modelo `104_78`.
`zeta_law_deep_truncation_check.py` certifica con racionales las fibras
prima/semiprima, sus signos opuestos y las escalas cuadráticas de `104_79`;
la masa de las fibras usa PNT en la prueba, no primos flotantes.

## Status

| doc | estado |
|---|---|
| `104_00` | **cerrado.** Dos rutas eliminadas por duplicación (lcm/Stieltjes ← Coffey; espacio modelo ← Suzuki). El rango finito con altura verificada es terreno mayormente bibliográfico: no es el frente |
| `104_01` | **cerrado** (álgebra + cota PNT explícita de Johnston--Yang + diagnóstico). Bajar \(\theta\) **no regala nada**: \(-2\theta A_n\le\mathcal N_n\le\frac12A_n\), signo indeterminado. **Se fija \(\theta=\frac14\)** |
| `104_02` | **corregido por erratum.** La cota para \(\varepsilon_n^-=A_n-\lambda_n-\lambda_n(\sqrt n)\) y sus antiguos corolarios quedan retirados. La coordenada pequeña correcta es \(\widetilde\varepsilon_n=A_n-\lambda_n+\lambda_n(\sqrt n)\); por sí sola no produce una cota incondicional uniforme de A1, porque ahora hace falta controlar por abajo el bloque incompleto |
| `104_03` | **cerrado.** Contorno local y signos auditados; la suma desnuda de residuos triviales diverge y la suma canónica exacta es \(\Delta A_n+(\gamma+\log4\pi)/2-1\) |
| `104_10` | **cerrado como no-go local.** Identidad finita y bloques exactos; la versión local-PSD murió porque cruces/bordes no tienen signo y el \(H_j\) real cambia de signo |
| `104_11` | **cerrado como stop-gate global.** El correlador sobreviviente tiene Hessiana nula: las dos energías `max` se cancelan con el borde exacto y queda \(-\int E\tau'\). M1 no aporta la desigualdad |
| `104_12` | **cerrado como auditoría M5.** La convolución de grado es el pullback Laguerre de \(Z^{-1}\delta Z\); Riccati no añade signo y separar normas reproduce 103_71. No existe métrica positiva que realice \(Z^{-1}=Z^\dagger\) en un poset divisor no trivial. M5 no aporta hoy una cota nueva |
| `104_13` | **cerrado como stop-gate Selberg--Riccati.** La recurrencia exacta conserva la colisión polo--primos, pero su coeficiente centrado cancela otra pieza de orden \(\varepsilon^{-n-1}\). La positividad de \(\Lambda\log+\Lambda*\Lambda\) no sobrevive al pullback y su sumatoria \(O(x)\) tiene norma dual al menos \(n(n-1)^n-1\) para \(\varepsilon=1/n\) |
| `104_14` | **cerrado como stop-gate M3.** Directamente para A1, \(C_n^\theta=\frac12\mathcal W_\zeta(f_n*f_n^\#)-\theta A_n-R_n\). El falsificador queda dentro del bulk y prueba que el mapa cero--lóbulo no aporta signo; sigue faltando un teorema especial para la sucesión real \(\Lambda\) |
| `104_15` | **cerrado como stop-gate del complejo mínimo.** El Koszul divisor tiene métrica positiva y \(d_E^2=0\); la anticomutación cancela \(p/q\), pero \(N_p=d_E\iota_p+\iota_pd_E\), de modo que \(M\delta Z\) induce cero en cohomología. El alcance no incluye complejos no locales que no hagan exactos los \(N_p\) |
| `104_16` | **cerrado como stop-gate del cociclo Jordan.** La jerarquía \(\mu*\log^k\) es no negativa, pero el polo la convierte en \(D_k-kD_{k-1}/(s-1)\). El primer jet Cayley satisface \(C_1<0<C_6\) con intervalos racionales; el falsificador \(\xi(s+a)\xi(s-a)\) conserva jerarquía Euler positiva y ecuación funcional con ceros off-line. La familia completada \(\xi(s-u)/\xi(s)\) es Schur para todo \(u\downarrow0\) si y solo si RH, y su medio presupuesto vuelve exactamente a \(\Delta D_n\ge0\) |
| `104_17` | **cerrado como stop-gate Abel--Fejér del bloque incompleto.** Para cada cuarteto, el germen Abel radial es positivo aun off-line. El testigo exacto \(w=2i\) tiene \(Q_4=-225/8\), \(F_8=-10885/128\) y, sin embargo, germen Abel positivo. Ningún promedio radial de orden fijo aporta la cota inferior coeficiente a coeficiente |
| `104_18` | **cerrado como stop-gate del shift correlacionado.** Mantener \(u=c\varepsilon\) produce una identidad finita no divergente, pero al retirar el regulador reaparece exactamente \(C_n\). La monotonía real de \((s-1)\zeta(s)\) es compatible con \(C_6>0\); la tercera diferencia en \(c\) tiene el signo contrario al de Hausdorff, y la unicidad de series de Dirichlet impide anular idénticamente el canal explícito con un sistema finito no trivial de pesos constantes |
| `104_19` | **cerrado como stop-gate de positividad inmediata; cociclo global no descartado.** \(A_u^2\) tiene coeficientes \(J_u*J_u\ge0\) y Gamma una medida Beta positiva, pero el factor polar al cuadrado tiene medida \(\delta_0+c(cr-2)e^{-r}dr\), negativa cerca de cero para todo \(c>0\). Los tres canales solo convergen acoplados y su límite es el gate fuerte \(-\Delta D_n\). El falsificador desplazado muestra que Jordan + Beta + ecuación funcional no determinan por sí solos el signo Cayley |
| `104_20` | **cerrado localmente; gate global activo.** La identidad \(b_u(p^k)=\nabla^2((k+1)p^{ku})\) absorbe torre y canales en \(\mathsf C_p^2\), pero el cuadrado no es de norma. El bloque de grado uno cambia de signo al variar el fondo \(m\), y todo grado par tiene infinitos bloques positivos. Un diagnóstico no certificado mantiene \(g_n<0\) hasta 1200; probar el signo de la suma global, conservando interacciones entre primos, es el frente vivo |
| `104_21` | **cerrado como stop-gate PF/TP/CM global.** \(\log N\) tiene una medida compound-Poisson exacta y creciente en \(u\), pero la retícula de exponentes falla PF2 con menor \(-1/2916\). Para \(u=1,\varepsilon=2\), la inversa de Laplace del cociclo aritmético--Gamma--polar completo tiene densidad negativa en \(\frac12\log2\); no existe representación probabilística positiva que transfiera el orden al gate. El signo global de \(g_n\) no queda refutado ni probado; el sucesor concreto es una desigualdad firmada Stein--Mecke para el test Laguerre completado |
| `104_22` | **reducción cerrada; gate cúbico activo.** La estimación A0 exacta conserva \((1+T_n)^{-1}\), de modo que \(D_n^{[3]}=3\lambda_n-A_n\ge0\) implica \(C_n(T_n)\ge0\) para \(T_n\ge2\). Es estrictamente más débil que el margen cuadrático. El cociclo \(Y_3(s-u)/Y_3(s)=H_u^3K_u^2\), normalizado por \(u(1-z)^2\), converge directamente a \(-D_n^{[3]}\); el diagnóstico permanece negativo hasta el índice 1201, pero falta probar su signo global |
| `104_23` | **reducción cerrada; gate casi cuártico activo.** Como \(T_n\ge1000\), basta \(D_n^{[r_*]}=r_*\lambda_n-A_n\ge0\), \(r_*=2002/501\), equivalente a pedir solo \(\lambda_n/A_n\ge501/2002\). Las potencias reales de Euler y Gamma conservan medidas positivas; el polo real es firmado. Es el margen uniforme más débil obtenido hasta ahora usando solo el piso declarado del cutoff; no se reclama optimalidad absoluta |
| `104_24` | **cuatro canales cerrados; Stein positivo descartado.** La normalización directa tiene base \(k+1\) y límite exacto \(-(3\lambda_{k+1}-A_{k+1})\). La medida de Lévy \(\nu_A^{[3]}+2\nu_K-3\nu_P\) entra en una recurrencia Stein--Laguerre global, pero es negativa en un intervalo anterior a \(\log2\), incluso en el límite regulado. Queda abierta solo una cancelación firmada no local específica |
| `104_25` | **Fejér cerrado; gate global circular descartado.** Si \(\Re\Phi\le1\) en el disco, Herglotz--Fejér da todos los signos del margen cúbico. Pero la holomorfía de \(Y_3(s-u)/Y_3(s)\) en esos discos para \(\varepsilon\downarrow0\) ya equivale a RH. El radio Euler seguro tiende a cero y un testigo polinómico exacto impide transferir su signo al coeficiente sin amortiguar |
| `104_26` | **ataque cuártico cerrado como no-go SOS.** \(J_u^{*4}\) da una cuarta diferencia exacta, pero falla PF2 y los bloques completos cambian de signo. El cuadrado formal \(H_u^4K_u^3=(H_u^2K_u^{3/2})^2\) se linealiza al retirar \(u\). El margen \(4\lambda_n-A_n\ge A_n/1001\) corresponde al cutoff fijo basado solo en \(T\ge1000\); `104_56A` retiró su pretendida necesidad intrínseca |
| `104_27` | **signo de cola descartado desde A0/VK.** Más allá del último cero de Laguerre, dos funciones que saturan el mismo envelope dan \(R_n(T)\) estrictamente positivo y negativo. El testigo puede suavizarse y conservar monotonicidad eventual; no conserva soporte primo, que es precisamente el input nuevo que haría falta |
| `104_28` | **puente de vector fijo cerrado; diagnóstico \(v_{\max}\) descartado.** El test Li es exactamente el estado de kernel reproductor hard-edge \(g_n/\sqrt n\) y la suma prima es una forma Abel-renormalizada sobre ese rayo. El operador blanqueado antiguo vive en otro gauge; la polarización natural de \(A_n\) es indefinida y el Gram de referencia normaliza por \(n\), no por \(A_n\). No hay proyector casi-extremal fiel sin construir primero una nueva forma renormalizada cerrada |
| `104_29` | **corte \(\log2\) cerrado como identidad, balance de masas descartado.** La versión válida usa \(\varphi_n=L_{n-1}^{(1)}-n\) contra el generador compensado. El bloque exterior conserva todos los primos, pero la cota que se necesita sobre él es algebraicamente \(D_n^{[r]}\ge0\). Separar polo y primos cuesta \(\varepsilon^{-n}\) y repite 103_53--103_57 |
| `104_30` | **referencia de bandera cerrada; desigualdad espectral abierta.** La forma positiva diagonal evalúa exactamente \(A_n\) sobre cada prefijo y permite el cociente fiel de sección finita. El diagnóstico de masa es favorable, pero no certificado; las cotas de Schur/Gershgorin pierden la cancelación y requieren el control firmado de \(\Delta^2(A_n-\lambda_n)\) que no está probado |
| `104_31` | **flujo en \(\varepsilon\) cerrado como stop-gate Hilbert.** La realización unitaria es \(Q=-M_x\). No existe regulador que sea simultáneamente seguro para el operador Euler separado y para el transporte inverso del prefijo. La referencia \(A_{\rm flag}\) fuga fuera de su bandera, no simetriza \(Q\) y conserva exactamente el borde \(1/2\). La forma acoplada y renormalizada de `104_30` no queda descartada |
| `104_32` | **potencias superiores retiradas de la regularización; gate primos--polo abierto.** El bloque \(k\ge2\) converge ordinariamente y satisface \(\lvert P_{n-1}^{(\ge2)}(1)\rvert<14n+1=o(A_n)\). En el margen cuártico entra con factor \(-4\), y su absorción por valor absoluto en \(A_n/1001\) solo queda probada desde \(n\ge e^{112116}\), no desde \(150\). La obligación exacta restante es la desigualdad primos--polo (26) de `104_32` |
| `104_33` | **símbolo cerrado; prueba solo por frontera descartada.** Cada cero con \(\Re\rho>1/2\) aporta exactamente \(m_\rho\mathcal F_n(w_\rho)/[\rho(\rho-1)]\) al momento. Un cuarteto recíproco deja idéntica la frontera real y cambia \(B_n/A_n\) exponencialmente; una prueba debe controlar la suma firmada de residuos con aritmética específica, no suponer holomorfía Hardy |
| `104_34` | **dominación por curvatura descartada; compresión adyacente abierta.** El ansatz \(q_d(B)\le(1501/2002)q_d(A)\) falla rigurosamente en \(d=220\), ya dentro del rango infinito. La compresión exacta de bandera produce \(\mathcal T_n=4H_nd_n-(H_n+d_n-H_{n+1})^2\); probar \(\mathcal T_n\ge0\) para todo \(n\ge149\) propaga el certificado finito y cierra el margen, pero ese teorema firmado no está probado |
| `104_35` | **canal \(\theta\) cerrado como identidad; Selberg simple descartado como coercividad.** El borde correcto es \(-n\), y la obligación (26) de `104_32` se vuelve una correlación exacta de \(\theta-x\). La medida Selberg de primos/semiprimos es positiva, pero su inversa Hankel tiene ambos signos. Incluso con soporte en los primos verdaderos, PNT y escala Selberg no fijan el funcional si se altera un peso; queda abierto únicamente un teorema global para los pesos canónicos \(\log p\) |
| `104_36` | **Cholesky primos--polo construido y descartado como cierre por norma.** Para \(a>2\) la norma conserva todas las interacciones dentro de \(\lvert(s-1)^{-1}-Q(s)\rvert^2\). Su Laplace tiene en \(z=\rho/a-1/2\) residuo \(m_\rho[1-(1-a/\rho)^n]\): dos prefijos \(L^2\) consecutivos ya excluyen \(\Re\rho>a/2\), y los ceros críticos fuerzan \(\|V_{n,a}\|_2^2\gg(a-1)^{-1}\). Sobrevive solo una cota unilateral de la proyección firmada, no de la norma |
| `104_37` | **el taper adyacente queda cerrado como identidad y descartado como energía Hankel.** La forma en \(g_n+t\phi_n\) conserva exactamente bloque arquimediano, potencias superiores y primos--polo. La inversión colectiva da un kernel cuyo menor sobre \(\{R,2R\}\) es \(C^2e^{-6aR}R^{2d}(8^d-9^d+O(R^{-1}))<0\) para todo \(t\), incluido \(t_n^*\). Sigue abierto \(\mathcal T_n\ge0\) mediante una cancelación especial de los pesos canónicos, no mediante PSD Hankel |
| `104_38` | **la completación Selberg del cuadrado de Schur queda descartada.** Al mantener la identidad centrada completa, \(-\langle G,\mu*\mu\rangle+\mathcal Q_G(\mu)=0\) exactamente. Si se intenta reservar \(\mathcal Q_G\) para dominar la entrada cruzada, el kernel diferencia ya es negativo sobre un solo átomo primo canónico en la cola; además el cuadrado de la respuesta cruzada no es Hankel, con defecto de colisión \(-2n^2a^4x^2+O(x^3)\). Queda abierto únicamente el valor conjunto firmado para toda la medida canónica |
| `104_39` | **Riccati adyacente cerrado como stop-gate de necesidad.** El determinante equivale a las desigualdades triangulares para \(\sqrt{H_n},\sqrt{d_n},\sqrt{H_{n+1}}\). Un cuarteto sobre la línea mantiene \(H_n>0\) y rompe el gate exactamente, de modo que éste es más fuerte que el margen; bajo RH sí es positivo para todo \(n\) suficientemente grande. Optimizar la referencia da el óptimo circular \(D=H_n+H_{n+1}\), y la referencia de prefijos ortogonales solo cambia \(\Delta B_n\) por \(B_n+B_{n+1}\). No se descarta el gate para la zeta, pero deja de ser el único frente |
| `104_40` | **resolvente Euler canónico descartado como cota cuadrática conmutativa.** En el rayo fijo, el precondicionador positivo óptimo reemplaza \(\Re M\) por \(-|M|\). Su costo diverge como \(\log(1/(a-1))\) por un cero crítico no resonante, mientras un cero off-line obliga a sumar el residuo al cruzar \(a=2\Re\rho\). Sobrevive únicamente una estimación firmada/no conmutativa o el criterio \(\mathcal T_n\ge0\) |
| `104_41` | **cota de fase completa probada en el semiplano Euler; transporte descartado sin residuos.** Con \(F=(s-1)\zeta(s)\), \(\mathcal B_{n,a}=-(2\pi)^{-1}\int W_n\,d\arg F\), \(\mathrm{TV}(W_n)=8n\) y \(|\arg F|<3\pi/4\) dan \(|\mathcal B_{n,a}|\le3n\) para \(a\ge4\). El transporte a \(a=1\) cruza exactamente los ceros con \(\Re\rho>1/2\); el defecto es la suma firmada de residuos. El cuarteto \(w=i/2\) deja idéntica la fase completa sobre la línea y aporta \(2(2^{152}+2^{-152})-4>0\) al defecto. Sigue faltando un teorema específico para los pesos exactos \(\Lambda(m)\) que controle esos residuos |
| `104_42` | **optimización cuadrática no conmutativa descartada; compresión de grado cerrada como stop-gate.** Para el operador Euler--polo completo, con todas las \(\Lambda(p^k)\), el ínfimo algebraico sobre todo precondicionador positivo es exactamente \(|B_n|\); en el régimen peligroso devuelve el objetivo mismo. Si la continuación vectorial está en \(L^2\), todo costo acotado exige \(\mathrm{cond}\,R\gg(a-1)^{-1}\). La proyección de los primeros \(n\) estados conserva fase y da una fórmula exacta en \(\Delta B_j\), pero el dato nuevo entra con ganancia \(\sqrt{n/2}>1\). No se descarta una cota aritmética nueva para un \(R\) explícito; la optimización por sí sola no la suministra |
| `104_43` | **factorización size-biased cerrada; orden y energía separada descartados.** El selector divisor canónico conserva exactamente todas las \(\Lambda(p^k)\), pero está por encima del selector uniforme en \(n=2\) y por debajo en \(n=30\). Su error marginal es exactamente \(R\), y la energía Efron--Stein del Laguerre no escalado diverge como \(\{\binom{2n-2}{n-1}-1\}\varepsilon^{-2n+2}\). Queda abierta solo una comparación cruzada, firmada y no monótona |
| `104_44` | **transporte divisor--Markov cerrado como stop-gate operatorial y de escala.** La desintegración de `104_43` tiene norma uno incluso en media cero, de modo que no existe brecha global. El continuo Gamma sí contrae \(L_r(\varepsilon x)\), pero recomponer \(L_r(x)\) tiene carga \((2/\varepsilon-1)^r\); para \(\varepsilon=1/n\) reproduce la pared \(\exp(n\log n)\). No se descarta una estimación especial que conserve toda la suma alternada |
| `104_45` | **coupling cruzado cerrado como identidad y stop-gate local.** El kernel Stein es único e independiente del coupling. Tiene patrón \(-,+,-\) alrededor de \(\log2\). El orden \(R(q)<0\) vale para exponenciales y sus mezclas positivas, pero \(-R\) no es completamente monótona; el test Laguerre recompone exactamente \(B_n\) |
| `104_46` | **no-alineación del vector fijo descartada.** Para todo \(s\in(1,s_0)\), el cociente centrado del Laguerre aritmético converge a uno; el del split Gamma converge a cero. Los cocientes centrados son además invariantes por traslación y no observan la diferencia firmada de medias |
| `104_47` | **flujo size-biased cerrado como stop-gate.** La homotopía satisface una ecuación exacta entre grados, pero integrar el flujo da \(\mathcal B_{n,a_0}-B_n\); exigir el signo necesario es exactamente el margen original. Positividad/Markov genérica también vale para \(\zeta(s+c)\zeta(s-c)\) con ceros off-line |
| `104_48` | **fase por torre cerrada; multiplicidad local descartada.** La fórmula de Poisson da solo un minorante no sumable y también acepta los pesos desplazados. Una torre completa de multiplicidad \(1+t\) conserva soporte, constancia y PNT, pero viola cualquier techo proporcional en \(n=151\). El único input no falsado es la renovación unitaria completa \(\Lambda*{\bf1}=\log\) |
| `104_49` | **renovación unitaria cerrada como identidad lineal; coercividad aún abierta.** El Palm geométrico selecciona uniformemente una altura de la torre, propiedad que \(\omega_c\) pierde. Sin embargo, en cada grado el defecto selector \(\kappa_r-m_r/r\) y el transporte \(m_r/r-(r-1)!\varepsilon^{-r}\) cancelan exactamente \(m_r\), y el Laguerre recompone \(B_n\). El defecto condicionado ya tiene ambos signos en \(n=151\). Solo sobrevive una correlación no lineal entre varias torres que no desaparezca al promediar |
| `104_50` | **covarianza Palm cerrada como stop-gate.** El kernel centrado se diagonaliza por torre. Mantener el defecto total da \(\mathrm{Cov}(D_f,D_g)+M_s(f)M_s(g)\); para el test real, completar el cuadrado produce varianza más \((\mathcal B_{n,s}-\kappa A_n)^2\). Derivada, primitiva y score vuelven a coeficientes desconocidos o al flujo ya abierto |
| `104_51` | **inversión Möbius cuadrática cerrada como stop-gate.** La congruencia \(M^TKM=W\) elimina toda correlación `lcm`. Para el kernel infinito, la diferencia entre las energías es indefinida sobre un vector de dos niveles; para \(P_{150}\), el cutoff divisor local tiene signos opuestos en \(p=2,7\). No se afirma ese signo para la forma infinita sobre el Laguerre fijo. Polarizar la diagonal vuelve a una diferencia de cuadrados sin orientación |
| `104_52` | **flujo conectado de dos torres descartado.** El Hessiano exacto del margen conserva torre, polo y Gamma, pero la proyección logarítmica cancela con coeficiente cero todos los pares de torres distintas. Cambia de signo entre \(s=1\) y \(s=10\), y su cociclo Laguerre también tiene ambos signos |
| `104_53` | **jerarquía polinómica aditiva clasificada.** En el álgebra universal de momentos, los primitivos son exactamente las combinaciones lineales de cumulantes. Como los cumulantes zeta son sumas de una sola torre, ninguna identidad polinómica aditiva de orden finito puede conservar una reserva multi-torre. El teorema no cubre desigualdades no aditivas arbitrarias |
| `104_54` | **Gibbs/Chernoff descartado rigurosamente.** El defecto unitario Laguerre tiene colas aritméticas de ambos signos y orden \((\log N)^n\), mientras la ley zeta solo decae como \(e^{-s\log N}\). Todos sus momentos exponenciales no triviales divergen; añadir polo o presupuesto solo traslada por una constante |
| `104_55` | **formas cúbicas canónicas descartadas.** El Palm de tres marcas conserva el momento desconectado, pero el tercer central no tiene signo, el determinante alternante promedia cero y su cuadrado es genérico. Toda orientación obtenida multiplicando una copia independiente por una energía positiva factoriza exactamente como energía por el margen. Queda fuera del no-go únicamente una desigualdad no aditiva no canónica que correlacione la reflexión unitaria local con el entero total antes de la proyección conectada |
| `104_56` | **cuantificador reducido rigurosamente.** Bajo \(\neg\mathrm{RH}\), los fallos del margen contienen un conjunto sindético de densidad positiva. Basta probar bloques buenos de longitud no acotada o una excepción de densidad logarítmica cero. Esto reduce el objetivo, pero no suministra todavía esos bloques para zeta |
| `104_56A` | **corrección cofinal cerrada.** El cutoff puede crecer con \(n\) y con la holgura; \(4\lambda_n>A_n\) cierra A1 en un cutoff adaptado. \(A_n/1001\) no es un slack intrínseco. La adaptación no prueba la holgura que usa |
| `104_56B` | **auditoría de antecedente cerrada.** La parte de modos dominantes/excursiones infinitas ya está en Bombieri--Lagarias y en trabajos posteriores. El refuerzo topológico a densidad positiva/sindeticidad y el lift Fermi prima--Laguerre no aparecieron explícitos en la búsqueda primaria dirigida; se registran como no localizados, no como prioridad establecida |
| `104_57` | **bloque bajo aislado.** La obligación RH-strength queda en \(\asymp\sqrt n\log n\) etiquetas bajo \(\sqrt n\), con error de transporte de la misma escala y un criterio de presupuesto explícito. No se obtuvo una cota inferior nueva |
| `104_58` | **promedio traslacional fijo descartado.** Toda ventana fija conserva los modos exteriores y falla sobre densidad positiva bajo \(\neg\mathrm{RH}\). La fase Euler en \(a\ge4\) tampoco controla esos fallos al cruzar a \(a=1\) |
| `104_59` | **mayorización clásica descartada.** Las masas sin etiquetas pierden \(m\mapsto\log m\), los Laguerre no tienen curvatura global y el selector divisor cambia de orientación. Solo sobrevive la misma comparación global firmada específica de \(\Lambda\) |
| `104_60` | **barrera no lineal construida; estimación abierta.** Para cualquier \(b_n=e^{o(n)}\), RH equivale a que la profundidad negativa saturada tenga media cero en una sucesión de intervalos largos. El criterio pasa el cuarteto y queda fuera de 104_17/104_53, pero falta probar su media para zeta |
| `104_61` | **particiones exactas construidas; cotas abiertas.** RH equivale ya a \(\lambda_n\ge-1\) en bloques no acotados y a que la partición Fermi acotada \(\mathfrak F_{t,b}(X)\) tienda a cero. Su forma prima--Laguerre emparejada es exacta y conserva la relajación de densidad. \(\mathcal Z_t(X)=O_t(\log X)\) queda como criterio auxiliar más fuerte que sí implica una cota grado a grado |
| `104_62` | **lift Fermi unitario construido; rama diagonal cerrada.** La señal de una excursión \(-Y\) está en \(s=O(Y^{-1})\), por lo que toda resolución polinómica falla en el cuarteto. El cambio \(s=e^{-nv}\) fija la tasa, pero la generatriz radial ve un producto geométrico y no la media aritmética; en la frontera no existe truncación a orden finito |
| `104_63` | **energía cross-degree cerrada como no-go.** \(\limsup \mathcal E_N^{1/(4N)}=1/r_0\) localiza exactamente el primer polo transformado. Parseval/CD conserva el cuadrado completo, pero toda estimación separada pierde una cancelación de orden \(\varepsilon^{-4N}\) |
| `104_64` | **Abel logarítmico exacto; truncación de microfrecuencia cerrada.** La media Fermi de Cesàro tiende a cero si y solo si su media Abel lo hace; basta incluso una subsucesión radial. El lift prima--Laguerre exterior infinito es exacto. En el cuarteto, la corrección mala obedece una ley uniforme en \(\alpha=\log\log(1/s)/\log(1/h)\), y capturarla completa exige llegar a \(s=\exp(-c/h)\). Una cancelación previa entre todos los canales no queda descartada |
| `104_65` | **filtros locales clasificados y cerrados.** Todo filtro finito que no aniquile los modos exteriores conserva excursiones exponenciales negativas sobre un conjunto sindético; diferencias y promedios móviles fijos no fabrican bloques buenos. Un aniquilador exacto puede ocultar el cuarteto, por lo que tampoco es un detector fiel |
| `104_66` | **diagonal regulador--Abel probada; separación cerrada.** Con \(\varepsilon(h)=e^{-1/(100h)}\), \(\lambda_{n,\varepsilon(h)}\to\lambda_n\) uniformemente para \(n\le1/h\), y el criterio Fermi puede formularse con una única serie de Euler absolutamente convergente. Separar polo y primos exige precisión relativa \(\exp(-C/h^2+O(1/h))\); el producto completo vuelve a la fase Fermi desconocida |
| `104_67` | **dicotomía bilateral probada.** Si RH es falsa, hay excursiones positivas y negativas de la misma tasa exponencial máxima sobre sendos conjuntos sindéticos de densidad positiva. En consecuencia basta una barrera superior, inferior o bilateral subexponencial sobre bloques de longitud no acotada; transportar la cota Euler superior desde \(a\ge4\) a \(a=1\) cruza los mismos residuos off-line |
| `104_68` | **selector de bloques y doble límite eliminados.** Las ventanas deterministas \(I_L=[L^2,L^2+L-1]\) bastan: la suma Fermi tiende a cero y el producto asociado a uno bajo RH, mientras bajo no-RH la suma tiene \(\liminf\ge1\) y el producto tiende a cero. Con \(\varepsilon_L=e^{-(L^2+L-1)/100}\) queda una sola familia Euler convergente. El gas prima--Laguerre sigue siendo no interactuante; probar su cota queda abierto |
| `104_69` | **criterio \(\log X\) finito y diagonal Euler probados.** RH equivale a \(H_X^{-1}\sum_{n\le X}[n\{1+(n+1)e^{\lambda_n}\}]^{-1}\to0\). Con \(\varepsilon_X=e^{-X/100}\), los primeros \(X\) coeficientes se aproximan uniformemente y queda una única fórmula prima--Laguerre absolutamente convergente. El cuarteto da \(1/4\); separar polo y primos cuesta precisión \(e^{-X^2/100+O(X)}\) |
| `104_69B` | **auditoría de novedad cerrada.** Li/Bombieri--Lagarias/Bucur et al. ya contienen el mecanismo de excursión exponencial, Palojärvi es adyacente por intervalos finitos y Bingham--Gashi contiene la capa log-Cesàro/Abel. No se localizó la forma exacta Fermi--bloque--producto--diagonal; se registra como repackaging/corolario, no como prioridad. La pieza potencialmente sustantiva es el refuerzo densidad/sindeticidad de `104_56`, si su prueba permanece íntegra |
| `104_70` | **temperatura variable construida; ahorro polar descartado.** \(t_n=e^{-\sqrt n}\), \(b_n=e^{2\sqrt n}\) conserva un criterio Fermi equivalente a RH. En general, si \(\varepsilon_n\to0\) y \(t_n|p_n(\varepsilon_n)-1|\) queda acotado, entonces \(t_nR^n\to0\) para todo \(R>1\); esto contradice la sensibilidad necesaria a todo modo off-line. El lift acoplado existe, pero el costo relativo sigue siendo \(e^{-X^2/100+O(X)}\) |
| `104_71` | **dualidad entrópica exacta; interacción refactorizada.** \(P_L^{-1}=C_L\mathbb E_{\nu_L}e^{-\sum B_n\lambda_n}\) y Gibbs reduce el supremo completo a perfiles Bernoulli \(q_n\). La entropía no crea interacción: toda correlación paga multiinformación. Bajo no-RH el logaritmo crece al menos como \(cR^{L^2}\); por ello basta una cota uniforme con slack \(\exp(o(L^2))\) en una subsucesión. La cota para los pesos reales queda abierta |
| `104_72` | **razón de presiones acotada construida; transición emparejada abierta.** Para \(g_\tau(x)=\tau^{-1}\log\{(1+e^{-x})/(1+e^{-x-\tau})\}\), RH equivale a \(\sum_{n\in I_L}g_\tau(\lambda_n+\log(n+1))\to0\). Cada sitio aporta un factor entre \(1\) y \(e^\tau\), de modo que, a diferencia de `104_71`, la profundidad exponencial se satura y sobrevive solo la densidad de excursiones. El lift prima--Laguerre diagonal es exacto, pero la franja \(z\asymp1\) exige la diferencia prima--polo con error aditivo \(O(1)\), es decir precisión relativa \(e^{-X^2/100+O(1)}\) si se separan canales. El cuarteto da densidad \(1/4\); la cota para los pesos reales sigue abierta |
| `104_73` | **representación Bernstein cerrada; rescates afín, Jensen y ancho variable descartados.** La medida positiva tiene masa \(\tau\), pero sus momentos vuelven a las particiones exponenciales. La anchura efectiva es \(w(\tau)=\tau/\tanh(\tau/4)\); transportar un bloque de \(L\) sitios requiere error uniforme \(o(w/L)\). Toda anchura sensible a cada \(R^X\) conserva el costo \(e^{-X^2/100+o(X)}\); una anchura que absorbe el polo destruye esa sensibilidad |
| `104_74` | **Hadamard--Jensen construido; residuo interior aislado.** \(\sum e^{-t\lambda_n}z^n\) es entera de orden \(2/t\) bajo RH y tiene radio cero bajo no-RH. La presión es una mezcla exacta de incrementos de Jensen. Un contorno común a \(N\le n\le2N\) deja un término \(O(N^5\log^2N)\) y la suma finita de polos \(|w_\rho|<r_N\); ninguna estimación obtenida elimina esa suma. El truncamiento Hadamard necesita orden \(\Theta(2^n)\) en el cuarteto |
| `104_75` | **criterio duro y profundo probado; cota aritmética abierta.** Para cualquier \(0<\alpha<1\), RH equivale a que los índices con \(\lambda_n+\log(n+1)\le-e^{X^\alpha}\) tengan densidad logarítmica tendiendo a cero. Con \(\alpha=1/2\) y \(\varepsilon_X=e^{-X/100}\), esto es exactamente el evento \(Q_{n,\varepsilon_X}\ge A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}\). Poisson y Bessel cierran el primer momento, pero el cuarteto da primer momento \(4\) y colas no lineales \(1/4\) y \(1/8\); la estimación de densidad para los pesos reales no está probada |
| `104_76` | **cola alta cerrada en valor absoluto; bloque bajo abierto.** Por cuartetos funcionales, \(\sup_{n\le X}|\lambda_n^{(\gamma>X^{1/4})}|\ll X\log X\,e^{\sqrt X/2}\). Si RH está verificada hasta \(X^{1/4}\), el indicador profundo vale cero en todos los grados \(n\le X\). Markov y segundo momento ya tienen margen después de retirar ese bloque; sin retirarlo, un solo cuarteto exterior fijo produce densidad positiva |
| `104_77` | **reducción compleja cerrada; suma de residuos abierta.** Un radio seguro da \(\lambda_n=C_{n,n}-Z_n\) con \(C_{n,n}=O(n^5\log^2n)\), de modo que el criterio profundo equivale a una cola unilateral de la suma finita \(Z_n\). Jensen mide la masa interior, Cartan puede retirarla y Turán fuerza sus excursiones; ninguno prueba que sea nula. El cuarteto \(w=2i\) tiene continuación positiva en \(0<r<1\) y densidad profunda \(1/8\) |
| `104_78` | **falsificador Euler reticular validado; alcance delimitado.** El monoide formal tiene primos con multiplicidad entera, torres unitarias, renovación exacta, FE y ley de grado \(6^k+1-3^k-2^k\), pero ceros off-line y densidad profunda \(1/4\). No satisface \(\psi(x)\sim x\) continuo: es reticular y tiene polos periódicos en \(\Re s=1\). Por tanto descarta solo teoremas universales basados en los axiomas discretos conservados |
| `104_79` | **representación por ley zeta exacta; truncación separada descartada.** \(Q_{n,\varepsilon}-p_n(\varepsilon)=\mathbb E[J_n(N)-U_n(Y)]\). En la diagonal y para \(X/2\le n\le X\), los excesos positivo y negativo por encima de \(e^{\sqrt X}\) son \(\ge e^{X^2/500}\), ya sobre fibras prima y semiprima reales. Esto impide concentración más error de truncación por colas separadas; no excluye una identidad firmada que las cancele conjuntamente |
| `104_80` | **identidad conjunta encontrada; cierre negativo.** \(\sum_{n\ge1}(Q_{n,\varepsilon}-p_n(\varepsilon))z^{n-1}=-\partial_z\log\{(s_\varepsilon(z)-1)\zeta(s_\varepsilon(z))\}\). La involución Möbius cancela las fibras multiprimo, pero un cero \(\rho\) produce el polo \(z_{\rho,\varepsilon}=(\rho-1-\varepsilon)/(\rho-\varepsilon)\) con coeficientes \(m_\rho z_{\rho,\varepsilon}^{-n}\). Un reagrupamiento exacto no puede borrarlo por unicidad meromorfa; el límite profundo sigue sin probarse |

| 104_81 | **detector adversarial validado.** Para el cuarteto \(\{i,-i,i,-i\}\), \(\ell_n=4-4\cos(\pi n/2)\ge0\) y la densidad profunda es \(0\). Para \(\{Ri,-Ri,i/R,-i/R\}\), \(R=201/200\), solo \(4\mid n\) produce \(-\Theta(R^n)\) y la densidad es \(1/8\); \(R<e^{1/100}\) conserva el resultado bajo \(\varepsilon_X=e^{-X/100}\). Un par adicional de productos Euler con multiplicidades primas no negativas separa \(0\) (todos los ceros on-line) de \(1/4\) (ceros off-line). Esto descarta tautología y error de signo, pero no establece el límite para la zeta real |

**Objetivo, en su forma exacta** (independiente de Lagarias, \(\theta=\frac14\)):
\[
\int_{\log2}^{T_n}\bigl(\psi(e^u)-e^u\bigr)e^{-u}L_{n-1}^{(2)}(u)\,du
\ \le\ \tfrac34A_n+1-L_n^{(1)}(\log2)
\qquad(n\ge150),\ \text{incondicionalmente},
\]
equivalentemente
\[
 A_n-\lambda_n+R_n(T_n)\le\tfrac34A_n
 \iff
 \lambda_n\ge\tfrac14A_n+R_n(T_n).
\]
En la coordenada incompleta corregida, la misma desigualdad es
\[
 -\lambda_n(\sqrt n)+\widetilde\varepsilon_n+R_n(T_n)
 \le\tfrac34A_n.
\]

**Dos trampas registradas, que no deben repetirse:**
1. No existe una cota incondicional
   \(|A_n-\lambda_n-\lambda_n(\sqrt n)|\ll\sqrt n\log n\). El resto pequeño tiene el signo
   opuesto, \(A_n-\lambda_n+\lambda_n(\sqrt n)\), y usar el resto antiguo como pequeño introduce
   exactamente contenido RH-strength.
2. Para A1 no basta \(\lambda_n>0\): la condición exacta es
   \(\lambda_n\ge A_n/4+R_n(T_n)\). La antigua cota grosera de A0 hacía
   suficiente el **strong margin** \(2\lambda_n-A_n\ge0\), pero no necesario.
   Para un cutoff prescrito, reteniendo el factor de A0 basta el margen
   dependiente de \(T_n\); el valor \(r_*=2002/501\) es solo la versión uniforme
   obtenida del piso \(T\ge1000\). Si se permite aumentar el cutoff después de
   conocer una holgura positiva, \(4\lambda_n>A_n\) es suficiente. Separadamente,
   \(4\lambda_n-A_n\ge0\) para todos los índices ya prueba RH directamente y no
   necesita pasar por A1.

**Nuevo frente maestro.** Para cerrar la afirmación literal de esta fase sigue
haciendo falta A1 en cada \(n\ge150\). Para probar RH basta ahora un objetivo
mucho más débil: por ejemplo \(\lambda_n\ge-1\) en bloques consecutivos de
longitudes no acotadas, o, para \(b_n=\log(n+1)\) y algún \(t>0\), el límite
\[
 \mathfrak F_{t,b}(X)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 {1\over1+e^{t(\lambda_n+b_n)}}\longrightarrow0.
\]
`104_61` da una representación aritmética exacta de esa partición que mantiene
acoplados polo, Gamma, primos y potencias primas. Ningún documento actual
prueba todavía el límite para la zeta real. La cota
\(\mathcal Z_t(X)\ll_t\log X\) sigue disponible como blanco auxiliar, pero es
coeficiente a coeficiente y no es el frente de densidad. `104_62` y
`104_63` registran que Fourier unitario, escalado diagonal, Parseval y
Christoffel--Darboux tampoco aportan esa estimación. `104_64` permite buscar
el límite sobre una sola subsucesión Abel, pero prueba que truncar la capa
antes de \(s=\exp(-c/h)\) pierde una contribución de orden uno en el
falsificador. `104_68` elimina incluso la elección de los intervalos: basta
probar
\[
 \sum_{n=L^2}^{L^2+L-1}{1\over1+(n+1)e^{\lambda_n}}\longrightarrow0,
\]
equivalentemente que el producto complementario tienda a uno. `104_69`
elimina el doble límite del frente global: con \(\varepsilon_X=e^{-X/100}\),
RH equivale a que tienda a cero una única media finita en \(n\le X\), cuya
entrada prima--Laguerre es absolutamente convergente para cada \(X\). La
cota de cualquiera de estas dos expresiones para los pesos reales
\(\Lambda(m)\) sigue abierta y es exactamente el contenido RH-strength.
`104_71` debilita todavía más el blanco de ventanas: no hace falta probar el
límite cero. Basta acotar, en una subsucesión, el supremo entrópico combinado
contra \(G_{L,q}=\sum q_nL_{n-1}^{(1)}\) por cualquier
\(B_L=\exp(o(L^2))\). La dualidad prueba que esta formulación es exacta, pero
también que la entropía por sí sola no suministra la cota.
`104_72` conserva mejor la relajación original: basta demostrar
\[
 \sum_{n\in I_L}{1\over\tau}\log
 {1+e^{-(\lambda_n+\log(n+1))}
  \over1+e^{-(\lambda_n+\log(n+1)+\tau)}}\longrightarrow0.
\]
El observable es una razón de presiones con factores uniformemente acotados;
bajo no-RH crece linealmente en la cantidad de sitios malos. Su forma Euler
diagonal está cerrada, pero la cota para \(\Lambda(m)\) sigue siendo el único
input RH-strength.
`104_73` y `104_74` auditan directamente esa última frase: Bernstein,
Jensen, ancho variable y exponenciación Hadamard dan representaciones exactas,
pero no una cota superior de la diferencia ya cancelada. `104_75` reduce el
blanco todavía más. Con
\[
 \varepsilon_X=e^{-X/100},\qquad
 Q_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),
\]
basta demostrar
\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}
 \right\}}\longrightarrow0.                              \tag{Deep-\Lambda}
\]
Este enunciado solo excluye sobrepasos de tamaño \(e^{\sqrt X}\) en densidad
logarítmica positiva; no pide signo, transición \(O(1)\), ni control grado a
grado. Es el blanco aritmético más débil del ledger y es equivalente a RH.
La identidad poissonizada de Bessel controla únicamente el primer momento;
el cuarteto da primer momento inocuo y, simultáneamente, una cola profunda de
densidad positiva. Ningún documento actual prueba (Deep-\(\Lambda\)) para los
pesos reales.
`104_76` sí elimina incondicionalmente la cola
\(\gamma>X^{1/4}\) con margen \(e^{\sqrt X/2}\): si los ceros del bloque
\(\gamma\le X^{1/4}\) están en la recta, el indicador es cero en todos los
grados \(n\le X\). `104_77` confirma desde el contorno que ese bloque bajo
es exactamente la suma finita de residuos interiores; Jensen, Cartan y Turán
la detectan pero no aportan la cota unilateral. Por tanto el frente ya no
contiene ceros altos, una cola condicional ni un problema de primer momento:
contiene solamente la exclusión aritmética de un polo interior bajo.
`104_78` muestra que renovación unitaria, torres, positividad, FE y una
ley prima fuerte **de grado** todavía admiten ese polo; el modelo deja de ser
comparable justo en el PNT continuo, el soporte ordinario y Gamma. `104_79`
usa ya la ley zeta y los \(\Lambda(m)\) reales, pero prueba que sus colas
prima y semiprima antes de promediar tienen excesos bilaterales
\(e^{\Theta(X^2)}\). Por tanto tampoco sirve truncarlas o concentrarlas por
separado. Sobrevive únicamente una cancelación firmada conjunta, específica
de la ubicación ordinaria \(\{\log p\}\), el polo y Gamma.
`104_80` ejecuta esa cancelación conjunta a nivel de identidad:
\[
 \sum_{n\ge1}(Q_{n,\varepsilon}-p_n(\varepsilon))z^{n-1}
 =-\partial_z\log\{(s_\varepsilon(z)-1)
                     \zeta(s_\varepsilon(z))\}.
\]
La involución Möbius elimina exactamente las fibras multiprimo, pero deja
las torres \(p^k\), y cada cero exterior reaparece como un polo interior de
residuo positivo. Por unicidad meromorfa, ninguna reescritura exacta de esa
convolución puede suministrar la cota: el sucesor tendría que ser una
desigualdad nueva sobre la ubicación de los primos ordinarios, no otra
identidad algebraica.

**Política de fuentes** (`104_00` §7): arXiv, Zenodo, repositorios institucionales y revistas
con revisión por pares son admisibles para importar resultados. ResearchGate, Academia.edu y
viXra no justifican ningún lema, pero se registran y comparan como posibles antecedentes de
prioridad.

104_81 somete ese observable a dos controles adversariales. El cuarteto
crítico lo anula exactamente, mientras el cuarteto exterior de radio
\(201/200\) produce densidad \(1/8\) y permanece estable bajo la diagonal
\(\varepsilon_X=e^{-X/100}\). Un segundo par con productos Euler y
multiplicidades primas no negativas separa igualmente densidad \(0\)
(todos los ceros sobre la línea) de \(1/4\) (ceros fuera). Así queda
verificado que el gate detecta el fenómeno correcto y no es una tautología
de la normalización. Estos controles no prueban su anulación para los
pesos ordinarios \(\Lambda(m)\).

`104_82` elimina la independencia racional de las longitudes como posible
input faltante. El lift toral da Haar y Parseval, pero la evaluación
*untwisted* es no acotada; además, el modelo Euler exterior puede deformarse
a longitudes totalmente \(\mathbb Q\)-independientes sin perder su densidad
profunda positiva. `104_83` hace la auditoría theta complementaria: todos
los cumulantes entran en Deep-\(\Lambda\), la cola theta puntualmente menor
que \(1/300\) cancela el cien por ciento de los jets de borde del primer
modo, y ni dominancia modal, PF finito ni una parte imaginaria unilateral
controlan la transformada completa.

`104_84` identifica canónicamente la obstrucción restante. Para
\(E(z)=(s(z)-1)\zeta(s(z))\), \(s(z)=(1-z)^{-1}\), Deep-\(\Lambda\) equivale
a la ausencia de su factor de Blaschke interior. Jensen da exactamente
\[
 {1\over2\pi}\int_{-\infty}^{\infty}
 {\log|\zeta(1/2+it)|\over t^2+1/4}\,dt
 =-\log B(0)\ge0,
\]
y RH equivale a la igualdad. El mismo documento prueba que toda identidad
Euler local analítica —Möbius, *squarefree*, \(\zeta(2s)\), o una
combinación finita— conserva ese factor interior o borra también el
observable. Por tanto el único sucesor no descartado es una desigualdad
genuinamente no local para los primos ordinarios que pruebe \(B(0)=1\).

`104_85` prueba que las dos realizaciones no locales inmediatas conservan
exactamente la misma obstrucción. Un producto *all-primes* renormalizado es
entero, cero-libre y converge a \((s-1)\zeta(s)\) hasta \(\Re s=1\); su
convergencia local uniforme en \(\Re s>1/2\) equivale a RH por Hurwitz. La
forma Nyman--Báez-Duarte mantiene todas las interacciones mediante el kernel
PSD \(1/\max(m,n)\), pero cada cero derecho fuerza una distancia
\((2\beta-1)/|\rho|^2\). Probar que esa distancia se anula vuelve a ser
exactamente \(B\equiv1\).

`104_86` ensaya una coordenada de signo único distinta. El kernel Bose
\(q(x)=x^{-1}-(e^x-1)^{-1}>0\) satisface
\(-\Gamma(s)\zeta(s)=\int x^{s-1}q(x)dx\) y la autorreflexión exacta
\[
 q(x)={1\over\pi}\int_0^\infty q(t)
       \sin\!\left({xt\over2\pi}\right)dt.
\]
El operador seno es necesariamente firmado. El kernel es PF2/log-cóncavo
en escala logarítmica, pero falla complete monotonicity con el menor exacto
\(-1/144\), y no es PF infinito. Una mezcla positiva explícita conserva
signo, monotonía, asintóticos y la misma autorreflexión, pero introduce
cuartetos off-line. Por tanto tampoco esas propiedades fuerzan el caso
Deep-\(\Lambda\)=0.

`104_87` cierra la auditoría de la sección finita de Nyman sin reabrir
Hurwitz como frente. La inversión de \(1/\max(m,n)\) es tridiagonal y la
identidad \(\mu*1=\delta\) anula exactamente el residual en
\((1/N,1]\). Toda la energía queda en una cola positiva de pisos. En su
primer bloque aparece exactamente
\(M(m)-M(N)+N\sum_{k\le N}\mu(k)/k\); PNT no controla la escala cuadrática
necesaria. El inverso resuelve el prefijo, no la cola.

`104_88` vuelve al observable directo y genera una visualización
reproducible. La zeta ordinaria tiene indicador profundo cero en el rango
diagnóstico estable \(n\le2000\); el cuarteto exterior crece hacia su límite
exacto \(1/8\). También prueba la unicidad pertinente: cualquier función
meromorfa con la derivada logarítmica de los \(\Lambda(m)\) ordinarios y la
misma normalización es la propia \(\zeta\). Por ello no existe un
contra-modelo distinto con **todos** los pesos exactos; excluir que la zeta
misma tenga un cero exterior sigue siendo precisamente Deep-\(\Lambda\).

`104_89` normaliza las truncaciones Euler globales de `104_85` y prueba
que su log-módulo tiene media de Poisson exactamente cero para cada corte.
La media del límite \((s-1)\zeta(s)\) es el defecto BSY
\(D_B=-\log|B(0)|\). De aquí sale el blanco unilateral exacto
\[
 D_B\le\int
 \bigl(\log|(s-1)\zeta(s)|-\log|\widehat F_X(s)|\bigr)_+\,d\nu.
\]
Probar que el miembro derecho tiende a cero para alguna sucesión de cortes
probaría RH. Un pozo de Poisson explícito muestra que convergencia interior,
convergencia fronteriza casi en todas partes y media cero no bastan; una
familia \(\xi(s-a)\xi(s+a)\) muestra lo mismo aun con canal Euler positivo
sobre las potencias de los primos ordinarios. La pieza no probada sigue
siendo impedir ese escape usando las alturas **exactas** \(\Lambda(m)\).
El mismo documento prueba ahora la dirección recíproca condicional:
bajo RH, la energía de Cramér permite escoger una subsucesión de cortes con
convergencia \(L^1(\nu)\). Así el gate con subsucesión es equivalente a RH,
no una condición accidentalmente más fuerte.

104_90 efectiviza el ataque directo a la escala profunda. Una altura
verificada \(H\), VK y el conteo \(\mathcal N(T)\le25T\log T\) dan
\[
 \lambda_n\ge-500n(\log(2n)+1)(1+e^{a_Hn}),
 \qquad a_H<{1\over2H^2},
\]
y por ello solamente
\(\limsup\mathcal D_X\le1/2\), no el límite cero. Para
\(H=3\cdot10^{12}\), el cambio de régimen aparece cerca de
\(3.24\cdot10^{50}\). El mismo documento subordina el modelo reticular
exterior a la torre \(7^k\): conserva pesos Euler no negativos, PNT de
tipo VK y un completamiento entero simétrico, pero tiene ceros exteriores.
Sus polos Euler adicionales y sus pesos modificados impiden llamarlo
contraejemplo a RH; prueba exactamente que ese paquete amplio no sustituye
los valores ordinarios literales.

`104_91` audita la forma dual de `104_89`. Por Bochner, exigir que
\(K\) y \(e^{-|y|/2}-K\) sean definidas positivas es exactamente
equivalente a \(K=\widehat{\varphi\nu}\) con
\(0\leq\varphi\leq1\): el minimax PD no relaja el selector unilateral. La
parte Euler--comparador se escribe en una sola integral contra
\(d(J-\mathrm{Li})\). Además, para cada prefijo \(M\) se construye
un contramodelo que conserva todos los pesos ordinarios hasta \(M\) y
todas salvo una torre prima remota, junto con
positividad, PNT/VK y simetría funcional, pero tiene un cero derecho y
defecto Jensen explícito. Esto descarta cierres por compactación de
prefijos o por las restricciones PD solas; no descarta una desigualdad que
use literalmente todas las torres y el completamiento exacto de Riemann.

`104_92` suaviza directamente el cutoff Euler, sin volver a Hurwitz o
Nyman. Las medias Riesz--Cesàro y el Abel aritmético
\(e^{-\varepsilon m}\) conservan los pesos ordinarios literales, son
cero-libres y tienen media Poisson cero. El Abel en \(\log X\) se calcula
exactamente como \(H(s+\eta)/H(1+\eta)\), de modo que su barrera
\(\eta=1/2\) es otra forma de la frontera RH. Un spike alineado demuestra
que toda matriz positiva regular puede conservar íntegra la fuga unilateral.
Un modelo continuo con medida de Mangoldt positiva, PNT
\(x+O(x^\beta)\), polo simple y ceros simétricos \(\beta,1-\beta\)
cuantifica la falla: los defectos Cesàro y Abel crecen respectivamente como
\(X^{\beta-1/2}/\log^2X\) y
\(\varepsilon^{1/2-\beta}/\log^2(1/\varepsilon)\). El modelo no conserva
el soporte ni los valores ordinarios; por tanto cierra el principio general
de tightness, no el target exacto para \(\Lambda(m)\).

`104_93` registra la energía discreta exacta
\[
 \mathcal E(N)=\sum_{m\le N}{1\over m(m+1)}
 \left\{\sum_{2\le n\le m}{\Lambda(n)-1\over\log n}\right\}^{\!2}
\]
y prueba
\(\mathrm{RH}\Longleftrightarrow\sup_N\mathcal E(N)<\infty
\Longleftrightarrow\mathcal E(N)=N^{o(1)}\). Un cero de parte real
\(\beta>1/2\) fuerza exponente energético al menos \(2\beta-1\). La
identidad finita del kernel es
\(1/\max(r,s)-(N+1)^{-1}\): el término faltante vive en el cociente
\(r/s\), mientras toda la jerarquía Selberg empuja las marcas al producto
\(rs\). Al centrar, el segundo coeficiente ya satisface
\(r(2)<0<r(3)\); sin centrar, la positividad pierde la cancelación con el
comparador. Por tanto variar el orden de Selberg o aplicar Vaughan con
normas diagonales no prueba la cota: conservar la correlación firmada deja
exactamente una condición equivalente a RH. El documento no establece esa
cota incondicionalmente. La equivalencia (L^2) continua subyacente es
clásica (marco Cramér--Ingham--Titchmarsh); queda pendiente el gate externo
con referencias exactas y no se reclama novedad para esa equivalencia ni
para su discretización estándar. Esta coordenada queda fuera del frente
activo porque pierde el andamiaje compacto--cola de Li--Laguerre.

`104_94` separa por primera vez esa energía en el canal de primos
ordinarios y el de potencias propias. La identidad exacta
\(\Lambda(p^k)/\log(p^k)=1/k\) da
\[
 B_m=\pi(m)-\sum_{n=2}^m{1\over\log n}
     +\sum_{k\ge2}{1\over k}\pi(m^{1/k}).
\]
Usando solo Chebyshev, el último sumando es
\(O(\sqrt m/\log m+m^{1/3})\), y por tanto tiene energía discreta
finita. Se sigue que \(\mathcal E(N)=N^{o(1)}\) equivale exactamente a
la misma cota para \(\pi(m)-\mathrm{Li}_2(m)\). La inversión de
Möbius muestra además que \(J\leftrightarrow\pi\) es un cambio de
coordenadas finito e invertible; lcm frente a radical del factorial añade
precisamente el bloque de potencias de energía finita. Esto descarta que la
contabilidad exacta de potencias primas sea la desigualdad ausente: el
obstáculo vive ya en la colocación de los primos ordinarios. No prueba la
cota subpolinomial ni RH.

`104_95` cierra la variante Landau basada en polinomios diferenciales de
\(\ell=-\zeta'/\zeta\). En orden cuadrático, la única combinación no
constante que cancela ambos términos polares en \(s=1\) es
\(A(\ell'+\ell^2+2\gamma\ell)\); su coeficiente primo
\(A\log p(2\gamma-\log p)\) cambia de signo ya entre \(p=2\) y
\(p=11\). Más generalmente, si
\(P(\ell,\delta\ell,\ldots,\delta^r\ell)\) tiene coeficientes de Dirichlet
no negativos y es holomorfo en \(1\), entonces \(P\) es constante. La
prueba aísla cada grado sobre productos *squarefree* de exactamente ese
número de primos y usa la divergencia de \(\sum_p1/p\). Por tanto ningún
polinomio diferencial de coeficientes constantes puede cancelar el polo,
conservar positividad y retener polos en los ceros. El teorema extiende el
gate Riccati particular de `104_13`; no cubre operadores no polinómicos o
no locales y no prueba RH.

`104_102` cierra la ampliación analítica/racional de ese gate. Para un
germen holomorfo arbitrario
\(\Phi(\ell_0,\ldots,\ell_r)\), el soporte *squarefree* de exactamente
\(k\) primos sigue aislando el grado \(k\) del Taylor infinito. Si la
serie de Dirichlet ensamblada tiene coeficientes no negativos, llega a
\(\Re s>1\) y la misma rama es holomorfa en \(1\), la divergencia de
\(\sum_p1/p\) fuerza que todos los grados positivos desaparezcan. Para
cocientes racionales se prueba además que poseer una serie de Dirichlet
ordinaria ya fuerza regularidad en el origen: al proyectar sobre
\(r+1\) primos, el jacobiano
\((\log p_i)^{j+1}\) es Vandermonde e invertible. La salvedad exacta es
que holomorfía solo local en \(1\) no basta:
\(1/(c-\ell_0)\) tiene coeficientes positivos y un cero en \(1\), pero
fabrica un polo real \(\sigma_c>1\). En general, todo transformado no
constante de esta clase tiene abscisa \(\sigma_c>1\), que Landau convierte
en una singularidad real situada antes que los ceros no triviales. No
surge una prueba de la cota energética ni de RH.

`104_96` calcula la energía discreta literal hasta \(N=10^7\) y la separa
en bloques diádicos. En el rango \(9\le j\le23\) se observa
\(0.0519<j^2\Delta_j<0.0982\), lo que propone el blanco falsable y
sumable \(\Delta_j\le1/(8j^2)\). Probarlo para todos los bloques implicaría
RH por `104_93`; el cálculo finito no lo prueba. Controles prescritos con
primitivo \(m^\beta\cos(7\log m)/\log m\) verifican escala constante en
\(\beta=1/2\) y crecimiento \(2^{(2\beta-1)j}\) en \(\beta=0.65\). El
mismo diagnóstico refuta monotonía de \(j^2\Delta_j\) y la cota más fuerte
\(1/(20j^2)\). Se auditan la tabla de potencias primas, `float64` frente a
`longdouble` y la independencia del *chunk*; sigue faltando demostrar una
cota sumable para todos los bloques.

`104_97` audita adversarialmente la constante candidata \(1/8\). Para el
primitivo crítico exacto
\(B_m=c\sqrt m\cos(\gamma\log m+\phi)/\log m\) prueba
\[
 j^2\Delta_j={c^2\over\log^22}
 \int_{(j-1)\log2}^{j\log2}\cos^2(\gamma t+\phi)\,dt+o(1).
\]
Con \(c=1,\gamma=7\), el liminf es mayor que \(0.574>1/8\); con la
normalización de residuo de un par crítico de multiplicidad cuatro en la
primera ordenada, es mayor que \(0.222>1/8\). Por tanto \(1/8\) no es una
constante impuesta por la escala o por la mera localización espectral en
la línea. Estos son controles críticos, no la zeta ordinaria: no refutan
la cota para sus pesos. El blanco de `104_96` queda como conjetura
aritmética adicional de fuerza al menos RH, no como consecuencia
automática de RH; el control general válido bajo RH es solamente la
sumabilidad de los bloques.

`104_98` factoriza exactamente la energía literal de
\(P_m=\pi(m)-\mathrm{Li}_2(m)\) sobre la recta Mellin:
\[
 \sum_{m\le N}{P_m^2\over m(m+1)}
 ={1\over2\pi}\int_{\mathbb R}
 \left|{\Phi_N(1/2+it)\over1/2+it}\right|^2dt,
\]
con el borde móvil
\(\Phi_N(s)=\sum_{m\le N}(P_m-P_{m-1})m^{-s}
-P_N(N+1)^{-s}\). Su símbolo infinito es prime-zeta menos el comparador
discretizado; la diferencia con
\(E_1((s-1)\log2)\) es holomorfa en \(\Re s>0\). En
\(\Re s>1/2\), un cero exterior de multiplicidad \(m\) produce
exactamente la rama \(m\log(s-\rho)\). La monodromía tiene un piso Hardy
positivo \(m^2\pi^2/6\), pero ese piso pertenece al promedio de las dos
hojas. En una sola hoja queda el término firmado
\(\pm2\pi m\,\Im\Phi_0\). La fórmula explícita reproduce la misma pérdida:
diagonal cero--cero positiva más interferencias de ambos signos. Así se
localiza exactamente el signo ausente, pero no se demuestra la cota
energética subpolinomial ni RH.

`104_99` ejecuta el ataque exacto de Eratóstenes sobre el núcleo de
`104_94`. Con \(P(z)=\prod_{p\le z}p\), prueba
\[
 \pi(x)=\pi(\sqrt x)-1+
 \sum_{d\mid P(\sqrt x)}\mu(d)\lfloor x/d\rfloor
\]
y mantiene, sin módulos, el residuo firmado completo. La pareja de
paridad \(a_n^\pm=1\pm(-1)^{\Omega(n)}\) produce además la identidad
exacta
\[
 \sum_{d\mid P(\sqrt x)}L(\lfloor x/d\rfloor)
 =1+\pi(\sqrt x)-\pi(x),
 \qquad L(y)=\sum_{n\le y}(-1)^{\Omega(n)}.
\]
Como \(1+\pi(\sqrt m)\) tiene energía finita, RH equivale a energía
subpolinomial de
\(\mathrm{Li}_2(m)+\sum_{d\mid P(\sqrt m)}L(\lfloor m/d\rfloor)\).
Esto no prueba esa cota, pero localiza la cancelación completa. Para todo
nivel \(D\le x^{1-\eta}\), los datos de divisibilidad de \(a^+\) y
\(a^-\) difieren en \(O_A(x/\log^A x)\) para todo \(A\), mientras sus
masas cribadas difieren en \(\sim2x/\log x\). Por ello ninguna
inclusión--exclusión/criba estable de nivel subcompleto puede cerrar la
energía; el nivel completo escapa al falsificador, pero allí la identidad
recompone exactamente el error primo original.

`104_100` ejecuta el promedio de las dos hojas de `104_98` con el
completamiento exacto. Escribiendo
\(\Phi=\log\xi+G\), ecuación funcional y conjugación centran las hojas de
\(\log\xi\), pero en el símbolo primo queda exactamente
\[
 |\Phi_+|^2-|\Phi_-|^2=4\pi m\,\Im G(1/2+i\gamma).
\]
Las simetrías preservan, en vez de invertir, el carácter de monodromía.
En los prefijos reales, el promedio se reduce exactamente a la
descomposición pitagórica entre \(\Re\Phi_N\) e \(\Im\Phi_N\); ambos
polinomios siguen siendo monovaluados y no contienen la diagonal.
Un cuarteto polinomial funcionalmente simétrico con corrector entero
\(c(s-1/2)\) cancela exactamente una hoja y duplica la otra, de modo que
el promedio no selecciona la hoja aritmética. Para la zeta real, el
corrector tampoco es una perturbación finita:
\(\Re G(1/2+it)=\pi|t|/4+O(\sqrt{|t|}+\log|t|)\), y su energía en
\([T,2T]\) es \((\pi^2/16+o(1))T\). BSY conserva el factor de Blaschke
interior y Weil conserva el defecto radial firmado del cuarteto. Por tanto
el completamiento no entrega la cota subpolinomial ni prueba RH.

`104_101` pasa la energía de `104_94` a gaps consecutivos sin pérdida. En
cada celda \([p_k,p_{k+1})\) obtiene
\[
 \mathcal E_k=W_k(c_k-\bar\ell_k)^2+V_k,
 \qquad W_k=p_k^{-1}-p_{k+1}^{-1},
 \qquad c_{k+1}=c_k+1-\ell_{k,g_k}.
\]
La completación cuadrática decide el signo del intento variacional: la
convexidad da un mínimo celular, mientras la cota superior requiere
controlar el paseo acumulado de los gaps normalizados. Para cualquier
rueda fija \(W\), \(1/2<\beta<1\) y \(c>0\), construye una sucesión
\(0\)-\(1\), apoyada en \((n,W)=1\), con PNT/VK, gaps
\(O(\log x)\) y
\[
 A(x)-\sum_{n\le x}{1\over\log n}=cx^\beta+O(1),\qquad
 \mathcal E_A(N)\sim{c^2\over2\beta-1}N^{2\beta-1}.
\]
Así las restricciones relajadas de composición, densidad y gap no
fuerzan energía subpolinomial. Imponer a la vez «seleccionado implica
primo» y «omitido implica compuesto» deja el singleton de los primos
literales; no queda una comparación convexa independiente y estimarlo es
el problema original.

`104_103` refuerza adversarialmente ese diagnóstico hasta la composición
de Euler abstracta. Para cualquier cero prescrito
\(\rho=\beta+i\gamma\), \(1/2<\beta<1\), y cualquier rueda fija,
redondea la densidad
\[
 {1-2x^{\beta-1}\cos(\gamma\log x)\over\log x}
\]
a una escalera literal \(0\)-\(1\), de normas enteras y gaps
\(O(\log x)\). Al declarar sus puntos generadores de un monoide
conmutativo libre, obtiene pesos \(\Lambda_{\mathcal P}\ge0\), Euler
producto exacto y la identidad coeficiente a coeficiente
\[
 g(m)\log m=\sum_{d\mid m}g(m/d)\Lambda_{\mathcal P}(d),
\]
pero la zeta resultante tiene ceros simples en \(\rho,\bar\rho\) y su
energía crece como \(N^{2\beta-1}/\log^2N\). Por tanto integridad,
escalonamiento, gaps, PNT/VK y factorización de Euler abstracta no
excluyen una excursión exterior. La propiedad no conservada queda
identificada exactamente: que las normas generadoras sean los
irreducibles ordinarios de \((\mathbb N,\cdot)\), sin colisiones de
norma. Un teorema de rigidez interno prueba que una norma inyectiva
fuerza \(P_{\mathcal Q}(x)\le\pi(x)\), y que una norma biyectiva fuerza
exactamente el sistema primo ordinario. Imponerla devuelve el singleton
de los primos literales y, con
él, el blanco energético original. Este falsificador no prueba la cota
para los primos ordinarios ni RH.

`104_104` ataca directamente el criterio de bloques desde los valores y
derivadas reales de
\(\mathcal F(z)=\log(2\xi((1-z)^{-1}))\). Prueba el criterio exacto
\[
 \mathrm {RH}\iff
 \limsup_{k\to\infty}
 \left({|\mathcal F^{(k)}(r)|\over k!}\right)^{1/k}
 \le {1\over1-r}\qquad(0<r<1),
\]
incluso bastando los \(r\in\mathbb Q\cap(0,1/2)\). La identidad de Euler
con los \(\Lambda(m)\) ordinarios da fórmulas absolutamente convergentes
para cada jet, pero certifica los discos requeridos directamente solo en
el horodisco \(|z-1/2|<1/2\), equivalente a \(\Re s>1\). Para
\(r<1/2\), pasar del radio seguro \(r\) al radio \(1-r\) es exactamente la
continuación que excluye ceros interiores. Un factor polinómico explícito
\(P_{\beta,\gamma}\), positivo en el eje real y compatible con ecuación
funcional, realidad y orden uno, se vuelve \(C^J\)-arbitrariamente invisible
en cualquier compacto real mientras añade un cuarteto off-line y excursiones
negativas sindéticas. Es el falsificador cualitativo de `104_84` refinado
cuantitativamente, no una nueva familia de completaciones. Esto descarta
inferencias estables desde una cantidad
finita de jets. Un segundo factor
\(1+c[s(s-1)]^{2M_0}\prod_j((s-1/2)^2-a_j^2)^{2M_j}\)
iguala además **exactamente** cualquier familia finita prescrita de jets
reales y aún introduce un cero con \(1/2<\Re\rho<1\); la salvedad explícita
es que puede introducir otros ceros en \(\Re s>1\). Ninguno de los dos es
un contramodelo con los mismos primos. Tener exactamente
los mismos \(\Lambda(m)\) fuerza la misma \(\zeta\) por unicidad del
logaritmo derivado. El gate no prueba los bloques, Deep, A1 ni RH.

`104_106` calcula el filtro de bloque general sobre el defecto de
residuos:
\[
 \sum_ja_j\mathscr R_{N+j}
 =\sum_{\Re\rho>1/2}m_\rho
 \{w_\rho^NA(w_\rho)+w_\rho^{-N}A(w_\rho^{-1})-2A(1)\}.
\]
Caja, Cesàro y Fejér son solo elecciones de \(A\) y no orientan el modo
exterior. El cuarteto racional \(w=i/2\) tiene, en todo bloque que empieza
en \(N\equiv2\pmod4\),
\[
 q_N>2^{N+1},\qquad
 \sum_{j=0}^3q_{N+j}
 =16-6\,2^N+\tfrac32\,2^{-N}<0.
\]
Así una media firmada favorable no fabrica un bloque bueno. La operación
correcta es
\(\sum(-\mathscr R_n)_+=\sup_{0\le a_j\le1}-\sum a_j\mathscr R_{N+j}\).
Se obtiene un criterio determinista exacto sobre
\([L^2,L^2+L-1]\), pero la cota para ese supremo con los
\(\Lambda(m)\) ordinarios no está probada.

`104_107` vuelve a la coordenada Li--Laguerre y combina por primera vez la
cota de fase de `104_41` con la relajación por bloques de `104_67`. Para
los pesos triangulares
\(\alpha_{L,k}=(L-|k|)/L^2\), \(|k|<L\), prueba
\[
 |\mathcal B^\triangle_{N,L,a}|
 \le {3\pi\over2}{N\over L}+2(1-L^{-2}),\qquad a\ge4.
\]
Así un bloque de \(2L-1\) grados con \(N\asymp L\) tiene costo de fase
absoluto, en vez de \(O(N)\). El transporte de residuos también queda
cerrado exactamente:
\[
 {1\over\rho(\rho-1)}
 \sum_{|k|<L}\alpha_{L,k}\mathcal F_{N+k}(w_\rho)
 =T_{N,L}(w_\rho)+T_{N,L}(w_\rho^{-1})-2,
\quad
 T_{N,L}(w)=w^{N-L+1}
 \left({1-w^L\over L(1-w)}\right)^2.
\]
El multiplicador no tiene ceros en \(|w|<1\), y el término recíproco
conserva tamaño \(\asymp |w|^{-N-L}/L^2\). El cuarteto \(w=i/2\)
produce ambos signos exponenciales mientras preserva la fase crítica.
Por ello el promedio elimina el costo de frontera pero no el defecto
off-line. Además, una media firmada acotada no da un bloque bueno
coeficiente a coeficiente: para aplicar `104_67` aún haría falta controlar
la parte positiva, el máximo o cada grado. La cota unilateral acoplada
para los \(\Lambda(m)\) ordinarios permanece sin probar.

`104_108` reduce ese cubo de tests a una familia uniparamétrica
de Fejér modulada. Para \(a\ge4\), uniformemente en \(\phi\),
\[
 |\mathcal B^\triangle_{N,L,a}(\phi)|
 \le3\pi N/L+4.
\]
Parseval identifica su promedio \(L^2\) con
\(\sum\alpha_{L,k}^2B_{N+k}^2\), por lo que una cota uniforme
subexponencial en \(\phi\) detectaría cualquier excursión exterior y es
equivalente a RH. Al transportar a \(a=1\), el residuo es
\[
 w_\rho^NK_L(w_\rho e^{-i\phi})
 +w_\rho^{-N}K_L(w_\rho^{-1}e^{-i\phi})-2H_L(\phi).
\]
La frecuencia emparejada conserva tamaño
\(|w_\rho|^{-N-L+1}/L^2\). Para el cuarteto completo \(w=i/2\),
\(N=2L\) y \(L\) par, el filtro vale al menos
\(2^{3L}/L^2-4\), sin cancelación del conjugado. Esta es una reducción
estructurada de coordenadas, no un debilitamiento de la fuerza RH ni una
prueba: la cota aritmética uniforme en la frontera sigue abierta.

`104_109` combina el residuo de `104_33`--`104_41`
con la localización alta de `104_76`. Para
\[
 D_n(Y)=2\Re\sum_{\substack{\Re\rho>1/2\\0<\Im\rho\le Y}}
 {m_\rho\mathcal F_n(w_\rho)\over\rho(\rho-1)}
\]
prueba uniformemente
\[
 |\lambda_n+D_n(Y)|
 \ll Y\log Y+X\log X\{1+e^{X/(2Y^2)}\}\qquad(n\le X).
\]
Así RH equivale a la existencia de bloques
\(I\subset[N,2N]\), de longitudes no acotadas, en los que
\(D_n((2N)^{1/4})\ge-\tfrac12e^{\sqrt N}\) grado a grado. La escala
correcta del gate profundo es \(N^{1/4}\), no \(\sqrt N\). El cuarteto
\(w=4i/5\) prueba que una media firmada puede ser favorable sobre bloques
arbitrariamente largos mientras persisten excursiones positivas
exponenciales, y que el promedio binomial de \(a=4\) vuelve contractivos
ambos modos. Por tanto la cota de fase y un promedio lineal no entregan la
barrera; falta una cota para el máximo o la parte positiva de la forma
prima--Laguerre exacta.

`104_110` vuelve a la forma prima literal del filtro modulado de
`104_108`. Si
\[
 P_{L,\phi}=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}
 L_{2L+k-1}^{(1)},\qquad
 Q_{L,\phi}=\sum_{|k|<L}\alpha_{L,k}e^{-ik\phi}
 L_{2L+k-1}^{(2)},
\]
prueba la identidad completa
\[
 \mathcal B^\triangle_{2L,L,1}(\phi)
 =P_{L,\phi}(0)+\int_0^\infty
 E(e^u)e^{-u}Q_{L,\phi}(u)\,du,
\]
además de un contorno cerrado con
\(M_\Lambda((1-z)^{-1})K_L(e^{-i\phi}/z)\). Para
\(\phi=\pi\), todos los grados tienen exactamente el mismo signo en el
rayo exterior. En la escala
\(U_L=L^{5/3}(\log L)^{1/3}\), el majorante VK es al menos
\[
 \exp\{(4/3)L\log L+(2/3)L\log\log L-O(L)\}.
\]
Así PNT/VK, incluso conservando polo y potencias primas hasta después de
integrar por partes e incluso añadiendo monotonía, no entrega la barrera
subexponencial uniforme. Esto descarta ese método de estimación, no la cota
para los pesos literales \(\Lambda(m)\), cuya cancelación firmada sigue
abierta.

Ningún documento de esta fase puede citarse como prueba de RH.

104_111 audita directamente el límite Deep de 104_75 mediante la
factorización canónica de
\(E(z)=((1-z)^{-1}-1)\zeta((1-z)^{-1})\). Prueba
\[
 \lambda_n=C_n-Z_n,\qquad C_n=O(n^2\log(n+1)),
\]
donde \(Z_n\) contiene exactamente los coeficientes del producto de
Blaschke de los ceros con \(\Re\rho>1/2\). En consecuencia, \(\Omega_X\)
queda atrapado entre los eventos
\(Z_n\ge(1\pm o(1))e^{\sqrt X}\), y
\(\Omega_X\to0\iff B\equiv1\iff\mathrm{RH}\). También corrige una laguna
expositiva de 104_75: el lift diagonal del indicador duro se prueba por
inclusiones con umbrales \(e^{\sqrt X}\pm1\), no solo comparando escalas.
El resultado localiza exactamente el factor interior pendiente; no lo
anula y no prueba RH.

`104_112` cierra la interpretación de Markov del límite Deep. Para un
cuarteto exterior
\[
 q_n(\rho)=4-4\cosh(na_\rho)\cos(n\theta_\rho),
 \qquad
 a_\rho={1\over2}\log {|\rho|^2\over|\rho-1|^2},
\]
el umbral \(e^{\sqrt X}\) se dispara en retornos con
\(\cos(n\theta_\rho)\ge1/2\) exactamente cuando
\[
 a_\rho>2X^{-1/2}+o(X^{-1/2}).
\]
Como \(a_\rho\asymp(\beta-\tfrac12)/\gamma^2\), el observable profundo
equivale operacionalmente a excluir ceros en la caja
\[
 0<\gamma\lesssim X^{1/4},\qquad
 \beta-\tfrac12\gtrsim \gamma^2X^{-1/2}.
\]
La frontera de esa caja toca \(\Re s=1/2\) cuando \(X\to\infty\). Además,
si se orienta \(D_n(Y)\) para que los cuartetos exteriores aporten parte
positiva, entonces bajo RH \(D_n(Y)_+\equiv0\), mientras que un solo cero
en la caja fuerza
\[
 \sum_{n\le X}{D_n(X^{1/4})_+\over n}
 \gg e^{Xa_\rho/2}-O(X^{1/4}\log X).
\]
Por tanto Markov no tiene slack: vale cero o falla por encima del umbral.
También queda registrado que una cota
\(\limsup\Omega_X\le c\) con cualquier \(c>0\) no descarta los modelos de
fase dominante de `104_56`. El límite Deep sigue siendo un criterio exacto,
no una prueba; el mecanismo faltante tendría que excluir la caja usando los
primos ordinarios literales y fallar para los modelos Euler exteriores.

`104_113` reescala esa caja con \(T=X^{1/4}\):
\[
 0<\gamma\lesssim T,\qquad
 \beta-\tfrac12\gtrsim\gamma^2/T^2.
\]
Esto muestra por qué los inputs clásicos no cierran el límite Deep. Las
regiones libres de ceros viven cerca de \(\Re s=1\), mientras la caja toca
\(\Re s=1/2\) para \(\gamma=o(T)\). Los teoremas de densidad dan conteos
positivos en \(\sigma=1/2+o(1)\), no ausencia de un solo cero. La
verificación hasta altura \(H\) solo cubre \(X\le H^4\), nunca el límite
asintótico. El frente queda reducido a una exclusión aritmética literal de
la caja, no a conteo, altura finita o mejora de constantes.

`104_114` construye el detector local exacto de esa caja en el disco de
Cayley. Con
\[
 E(z)=((1-z)^{-1}-1)\zeta((1-z)^{-1})=B(z)O(z),
\]
la cantidad
\[
 \mathcal J(z)=P_z(\log|E^*|)-\log|E(z)|
 =\sum_{\Re\rho>1/2}m_\rho
 \log\left|{1-\overline{a_\rho}z\over z-a_\rho}\right|
\]
es precisamente el potencial de Green del factor de Blaschke interior. Un
cero en la caja produce un pico local \(\gg1\), y
\(\mathcal J\equiv0\iff B\equiv1\iff\mathrm{RH}\). Esto prueba que la ruta
Poisson--Jensen detecta la caja sin pérdida, pero no aporta signo nuevo:
la desigualdad que anula \(\mathcal J\) es exactamente la eliminación del
factor interior, es decir Weil/RH en esa familia de tests.

`104_115` audita el certificado resolvente escalar sobre el retículo de
factorizaciones. El generador que intercambia todas las torres tiene tasa
de salida infinita para (0<\varepsilon\le1), el cruzado
\(\langle i[X,S]g_n,g_n\rangle\) es exactamente cero para el vector
Laguerre real y (C g_n) no satisface en general la compatibilidad de
Poisson con las constantes de cada capa (\Omega\). El pivote a primos
consecutivos, con tasa difusiva
\(\log(p_{j+1}/p_j)^{-2}\), repara el dominio y hace positivo el
resolvente después de proyectar el núcleo. Un twist complejo recupera la
fase pero cambia de signo con (n). El sucesor mínimo queda fijado como un
lift de dos grados Laguerre y una corriente conservativa sobre ciclos de
tres torres cercanas; el certificado escalar original queda retirado.
La corriente finita satisface un Schur exacto con constante computable;
el único puente aún no obtenido es una identidad Mecke de segundo orden
que convierta ese cruzado de dos grados en el funcional lineal real
(B_{n,\varepsilon}).

`104_116` demuestra la identidad Mecke de intercambio solicitada. Para
una corriente antisimétrica (\omega), su forma es
\[
 \langle F,J_\omega G\rangle_s
 =\sum_{p,q}{\omega_{pq}\over(pq)^{s/2}}
   \mathbb E_s\{\overline{F(qN)}G(pN)\}.
\]
La condición conservativa (J\mathbf1=0) es
\(\omega(p^{-s/2})_p=0\); sobre tres primos fija una circulación única y
la forma se vuelve un determinante cíclico de los tres desplazamientos.
La comparación exacta cierra negativamente el puente de `104_115`: la
corriente es alternante y bilineal, mientras (B_{n,s}) es la fuente
lineal prima--polo. Abrir la corriente hacia el comparador continuo
reproduce exactamente (M_s(f)), y cerrarla para obtener positividad lo
elimina. Por tanto Mecke queda demostrado, pero no aporta el resto positivo
requerido para A1.
