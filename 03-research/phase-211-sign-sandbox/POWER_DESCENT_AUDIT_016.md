# POWER_DESCENT_AUDIT_016 — Qué falta para descender de las colas high-pass

Estado: PROVED y revisado: obstrucciones de densidad, no-implicación lógica y construcciones específicas de016; véanse §§6–8. Papers intactos.

## 1. Corpus y diferencia de alcance

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX entradas POWER014–015, grid/crucigrama y búsquedas de highpass, dense, vanishing moments, all moments vanish y continuous moment functional. Los puentes BRIDGE002/CONFLUENT_BRIDGE014 y su revisión prueban densidad fuerte de la envolvente confluente COMPLETA. Las obstrucciones de umbrales crecientes de THREE002 trataban otra concentración temporal. No se encontró registrada la siguiente aplicación exacta de ceros crecientes de Laplace a las colas actuales. La continuidad de momentos y la unicidad analítica de Laplace son herramientas estándar, no se atribuye novedad a esos principios generales.

## 2. Un cero high-pass impide densidad en la norma de015

Sea eta>0 fijo y use L²_eta={f causal: e^(eta y)f∈L²(0,infinito)}. Para cada entero r>=0, el momento

    ell_r(f)=integral_0^infinito y^r f(y)dy

es un funcional continuo, con cota exacta

    |ell_r(f)|<=sqrt((2r)!/(2eta)^(2r+1)) ||e^(eta y)f||_2.

Toda función de Q^k V_N, Q=s/(s+u), con k>=1, tiene Laplace con numerador divisible por s^k y denominador no nulo en0. Por tanto ell_r(f)=0 para0<=r<k. En particular la unión de TODOS esos espacios con k>=1 permanece en el hiperplano cerrado ell_0=0 y no es densa en L²_eta ni en las normas más fuertes de015 que incluyen ese peso.

La obstrucción subsiste en el portador primitivo relevante: elija g≥0 suave compacto dentro de la semirrecta, con integral positiva, y F=(1/4-D²)g. Sus dos momentos Tate se anulan por integración por partes, pero ell_0(F)=(1/4)integral g>0. Para cualquier h de aquella unión,

    ||e^(eta y)(F-h)||_2>=sqrt(2eta)|ell_0(F)|>0.

No basta alegar que las restricciones Tate ya seleccionan los tests pertinentes: el momento ordinario adicional no es una consecuencia de ellas. Trasladar funciones tampoco elimina un cero de orden k en Laplace0, pues la transformada se multiplica por una exponencial no nula.

## 3. Ceros de orden creciente: todo límite fuerte es cero

Suponga k_j→infinito y f_j∈Q^(k_j)V_(N_j), con N_j arbitrario. Si f_j converge a f en L²_eta para un MISMO eta>0, la continuidad de cada ell_r y su anulación eventual implican ell_r(f)=0 para TODO r.

Laplace H_f(z)=integral e^(-zy)f(y)dy es analítica en Re z>-eta, por Cauchy--Schwarz en compactos. El punto0 está en ese dominio y H_f^(r)(0)=(-1)^r ell_r(f)=0 para todo r. Por el teorema de identidad H_f es cero en el semiplano conexo. Unicidad de Fourier en una recta vertical implica f=0.

Así una sucesión de vectores normalizados con k_j→infinito no puede tener un límite fuerte no nulo en ninguna norma común de015. Este resultado no depende de cómo crezca N_j ni de una tasa entre N_j y k_j. En particular no autoriza un puente por densidad de la unión de colas individuales en ESA topología.

Si una asignación k(N) es>=1 para todos N grandes y sólo tiene finitos bloques con k0, su unión también queda lejos de tests genéricos: el cierre está contenido en el hiperplano ell0=0 más la unión finita de esos bloques excepcionales. Si k0 aparece en grados N arbitrariamente grandes, la densidad puede recuperarse por el puente confluente, pero precisamente se han reintroducido los bloques iniciales sin signo que015 no decide.

La afirmación no excluye aproximaciones en una topología distinta donde esos momentos no sean continuos, ni una corrección adicional de momentos. Tal argumento tendría que verificar otra vez la continuidad de la forma COMPLETA, incluidos todos los contactos y la polar; densidadL² por sí sola no lo prueba.

## 4. Falsificador lógico de un descenso basado sólo en estructura y positividad eventual

Considere la forma modificada W_C[f]=W[f]-C||f||². Las identidades finitas e infinitas de mezcla de015 se conservan, porque la norma² satisface las MISMAS identidades con los mismos pesos. También se conservan las particiones lineales de formas que se deducen de esas identidades. El teorema EVENTUAL se conserva para cada N fijo: su Rayleigh crece como .5logk más un bloque acotado, y restar C sólo cambia la constante, dejando positivo todo k suficientemente grande con otro umbral.

Sin embargo se puede tomar C4 y obtener un vector inicial negativo explícito. Para f(y)=e^(-31.5y), su cociente completo es

    W[f]/||f||²=psi16-logpi+2zeta'(32)/zeta(32)+126/992.

Como psi16=H15-gamma<H15<7/2, logpi>0, zeta'(32)/zeta(32)<0 y126/992<1/2, este cociente es estrictamente menor que4. Por tanto W_4[f]<0.

Esto refuta sólo la inferencia lógica 'mezcla positiva + particiones + positividad eventual en cada dimensión ⇒ signo de todos los miembros iniciales'. Es una forma DIFERENTE, con símbolo arquimediano m-4, no un contraejemplo a W real ni un argumento contra usar sus coeficientes y certificados específicos. Los certificados iniciales de W no se trasladan a W_4 y no se pretende que lo hagan.

## 5. Obligación que sigue siendo legítima

Para descender hace falta una desigualdad que controle el defecto de los bloques iniciales por información adicional, o una uniformidad conjunta que alcance la masa pertinente de una partición y permita pasar la forma al límite. El puente confluente completo sigue válido. Los resultados anteriores sólo impiden sustituirlo sin prueba por la unión de colas que tienen ceros prescritos; no clasifican ni cierran las nuevas desigualdades que se intentan construir.

## 6. Revisión de POWER_DESCENT_016 y su verificador

APROBADO íntegramente. La identidad complementaria incluye la polar porque los productos de evaluaciones de Q y L en±1/2 suman1. Los filtros conmutan y la iteración binomial es exacta para cada contacto y la suma completa. La fórmula (-1)^r Delta^r a_k=W[L^rQ^k f] se obtiene por inducción sin normalizar los vectores. Aplicar015 al espacio V_(N+r) es legítimo para N,r fijos y proporciona uniformidad en el numerador, no un umbral común en r.

La serie telescópica de energías converge absolutamente: las sumas parciales convergen por Q^k f->0 en norma fuerte, y la cola de sus términos es positiva por EVENTUAL aplicado a Lf. Una cola positiva de suma convergente es absolutamente sumable; el prefijo es finito. No se supuso positividad de todos los términos para probarla.

La ley binomial condicional y el bound Lipschitz1/(2sqrt(m)) son correctos. Para un borde fijo r<=R, la probabilidad condicional de tener pocos fracasos tiende a0 para cada frecuencia finita, y la dominación por1 justifica EDGE. Su versión uniforme en la esfera de V_N usa una compresión positiva finita de multiplicadores acotados, cuya traza tiende a0; operatornorm<=trace es el paso correcto.

La contribución ENERGÉTICA del borde fijo también se verificó: L^r f tiene orden inicial N+r y el mismo grado de numeradorD, así su déficit de grado es r0+r. Las asintóticas015 dan norma²O(m^(.5-r0-r)) y RayleighO(logm). Multiplicar por binom(m,r)=O(m^r) deja O(m^(.5-r0)logm), que tiende a0 porque r0>=1. La suma sobre r=0,...,R es finita. No se infirió la desaparición de energía sólo desde la desaparición de masa; aquí se aportó su estimación propia.

El verificador actual tools/power_descent_016_verify.py se ejecutó con PASS. Su cota elemental2L32<H15-1+1/16+2/31<3 es correcta: psi16<H15,logpi>1 y zeta'/zeta32<0. Por tanto el falsificador modificado W4 tiene el margen más fuerte<-1 sobre el vector inicial. Esto refuerza la cota más débil de§4 de esta auditoría sin cambiar su alcance.

## 7. Revisión de POWER_JOINT_SCALE_016

APROBADO. La transformación Z=tau²/(u²+tau²) produce Beta(k+.5,N-.5), y el factor de norma es u^(1-2N)B/(2pi), con la contribución de ambas semirrectas correctamente incorporada. La concentración para k/N->c y la convergencia de correlaciones a cos(u sqrt(c)t) son consecuencias de media/varianza beta. Para el promedio de m, la cota uniforme de E tau² y el crecimiento logarítmico proporcionan la uniformidad integrable requerida. El contraejemplo a desaparición uniforme del contacto2 en un cono lineal usa c fijo resonante y k=ceil(cN); no hace ninguna afirmación de signo completo.

La identidad del extremo P=s^(N-1) con la órbita inicial de dimensión1 es exacta. Las entradas de Gram completas tienen signo(-1)^(r+i) cuando i+j=2r, y los parámetros beta declarados son correctos. La coordenada Jacobi con exponente final±.5 se interpreta tomando el grado máximo PERMITIDO del sector por N (se pueden rellenar coeficientes nulos), no necesariamente el grado efectivo de un P particular. Así la afirmación cubre todo el sector sin cambiar su peso.

La media temporal(N-.5)/u sigue de la derivada de fase con signo correcto. Para k>=1, el salto en fase de(i tau)^k no aporta porque la transformada se anula en0. La segunda derivada de Parseval usa exactamente k²/tau²+(N²-k²)/(u²+tau²); los momentos beta producen E y² y Var y del memo. La extensión algebraica k0 coincide con la ley gamma temporal conocida. Jensen demuestra el crecimiento exponencial en N del peso NO centrado para todo k, y cosh/Jensen demuestran que centrar no uniformiza simultáneamente los dos pesos: el producto de sus esperanzas es al menos1+2eta²Var, como se afirma (de hecho las mismas hipótesis permiten una cota mayor).

Estos resultados refutan herramientas de uniformización precisas, no el signo de W en conos lineales o cuadráticos. El cono cuadrático conserva el estado OPEN del memo y no se convierte por esta auditoría en un teorema de dispersión espectral uniforme.

## 8. Estado final de esta ronda

Los lemas de momentos de§§2–4 fueron revisados independientemente por el coordinador y aprobados. Las dos construcciones específicas de016 quedan revisadas y aprobadas en§§6–7. Descenso aritmético global, signo de los bloques iniciales y uniformidad conjunta de signo siguen abiertos. No se editó ningún paper.


## 9. Complemento: filtro desplazado, span denso y diagonales positivas insuficientes

**PROVED; revisión matemática y literal root/casos/mapa aprobada.** Es un complemento del falsificador W4 de§4/§6, no un nuevo principio de signo. Dedup: búsquedas dirigidas en índices01–06, grid/crucigrama y corpus; antecedentes015 (órbitas ponderadas),014 (densidad confluente),016 (partición y momentos) y010 (multiplicadores ponderados). No se halló la fórmula literal siguiente; no se afirma novedad absoluta del filtro exterior.

Fijar u=63/2, delta=1, eta=3/4, f0(s)=1/(s+u) y Qdelta(s)=(s+delta)/(s+u). Usar H_eta={h:e^(eta t)h pertenece a H¹(0,infinito)}, norma de014. El filtro y su inversa son operadores causales acotados en ese espacio:

 Qdelta=1-(u-delta)/(s+u),
 Qdelta^(-1)=1+(u-delta)/(s+delta).

Sus núcleos exponenciales, ponderados, son integrables porque u,delta>eta; las derivadas se controlan también por la ecuación de convolución exponencial. Así cada potencia fija es un isomorfismo acotado. En particular Qdelta(0)=delta/u no anula el momento ordinario; el cero -delta queda fuera del semiplano Re s>-eta donde los momentos de§2 se leen continuamente.

Para r>=0 poner fr=Qdelta^r f0. Para cada m, span{fr:0<=r<=m}=V_(m+1)(u): expandir Qdelta=1-(u-delta)/(s+u) da una matriz triangular con diagonal no nula sobre las potencias (s+u)^(-j-1). Por014 la unión de esos espacios es densa en H_eta. Para TODO R fijo, span{fr:r>=R}=Qdelta^R span{fr:r>=0} también es denso. Esto evita de verdad la obstrucción de momento cero, incluso para una cola de la familia.

Ahora sea W4=W-4||.||², el mismo falsificador completo de016. Es continuo en H_eta por014/002. Poner Q0=s/(s+u), gk=Q0^k f0 y d=delta²/u², p=1-d. La identidad escalar EXACTA es

 |Qdelta(i tau)|²=d+p|Q0(i tau)|²,
 Qdelta(-1/2)Qdelta(1/2)=d+p Q0(-1/2)Q0(1/2).

Por ello, incluidos el polar, todos los contactos y la norma,

 W4[fr]=sum_(k=0)^r binom(r,k)d^(r-k)p^k W4[gk].

No se ha expandido cuadráticamente la suma de funciones suprimiendo cruces; se usa una identidad de multiplicadores de las formas completas.015 en dimensión1 da W4[gk]~C k^(-1/2)log k, C>0, y lo mismo para W. Existe K con todas esas diagonales positivas para k>=K. Los términos k<K de la suma binomial tienen pérdida absoluta O(r^K d^(r-K)), exponencialmente pequeña. En el bulk k>=pr/2 la probabilidad binomial tiende a1; allí W4[gk]>=c log(r)/sqrt(r) para r grande, uniformemente en pr/2<=k<=r. Por tanto W4[fr]>0 para TODO r suficientemente grande. También W[fr]>0 eventualmente. Son afirmaciones escalares a dimensión inicial1 fija; no uniformidad en todos los numeradores ni positividad de los pares cruzados.

Sin embargo,016§6 prueba W4[f0]/||f0||²<-1. El span de cualquier cola r>=R es denso y W4 es continuo; existe por tanto una combinación FINITA v=sum_(r=R)^L c_r fr con W4[v]<0. Elegir R después del umbral anterior garantiza que cada generador usado tiene individualmente W4[fr]>0. Todos los términos son racionales causales en H_eta; no se usa una topología débil que pierda el polar o la aritmética.

Queda refutada la inferencia «span denso en norma de forma + signo individual eventual de sus generadores implica signo sobre ese span», incluso después de reparar el momento cero mediante un filtro invertible. No se afirma W real negativa, ni pares PSD, ni imposibilidad de un control de cruces específico del dato real. No hay nuevo certificado, nueva ventana temporal, torre de grados ni modificación de papers.
