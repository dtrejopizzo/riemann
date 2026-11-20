# Síntesis de las rondas O1

**Estado actual:** objetivo completo D active. La sección final «Rondas 005–007»
recoge los resultados más recientes; las rondas previas quedan como historia.

2026-10-18. Fila D independiente. Documento de integración, sin modificación
de Paper 47. Revisión final favorable: AUDIT_001 §8.

## Qué cambió en el encargo

La pregunta original «K de dos variables positivo y que falle al borrar un
primo» se sustituyó por una prueba en puertas: dominio efectivo; salida
precisa de SOS/PD; traducción real a BR, si existe; signo independiente;
fallo de una premisa o del enlace ante falsificadores pertinentes; enlace
con Q_T sólo al final. El signo del candidato no tiene por qué fallar él
mismo ante toda eliminación. Una identidad específica puede ser el paso
que evite la transferencia, pero su demostración debe aportar contenido.

## Resultados y límites

- CONTROL_001: la proyección P_T M_a P_T crea un kernel de dos variables
  sin cambiar la forma en la imagen de P_T. PROVED y revisión hostil favorable.
- AUDIT_001: thm:sos no es una prohibición de toda identidad de normas.
  Se distingue su clase de def:PD y del colapso abstracto B*B.
- AUDIT_001: núcleo de P36-4, operador K(t,t′) y conjunto relajado W₂ de
  BR son objetos diferentes. No se transfiere una pared por la notación.
- El examen del ansatz J+corrección compacta se registra en CONSTRUCTOR_001
  y fue aceptado por la revisión final (AUDIT_001 §8). Se refiere a positividad en un intervalo
  completo de alturas o en un ideal lineal denso explícito; no al dominio
  aritmético Euler+FE ni al nodo global con sus colas.

No se ha construido un núcleo con signo propio y enlace aritmético útil.
La ronda NO demuestra inexistencia del objeto de O1.

## Qué significaría continuar después del control compacto

Dentro del ansatz J+K y con positividad sobre el espacio completo de alturas,
una corrección tendría que escapar la clase compacta. Esto no impone no
compacidad a todo posible mecanismo O1: otro dominio u otra forma de
positividad requieren otro análisis.

Por ejemplo, I+J es ya positivo y no compacto en ese espacio. Eso sólo
ilustra que salir de la clase compacta no basta: es una positividad genérica,
sin especificidad aritmética. La siguiente ronda necesita un candidato
explícito antes de añadir otra condición necesaria al catálogo.

**Balance:** encargo mejorado y primera tentativa ejecutada; sin fuente de
signo, sin cierre del nodo ni cambio de estado de O1 o de la fila D.

## Segunda ronda — resultado positivo auxiliar con signo estricto

El plan posterior fue continuar hasta un resultado positivo.
Se construyó C_y como covarianza de divisibilidad bajo la gaussiana discreta
sin origen, con τ=θ−1. Su PSD genérica no se contó como avance. El cálculo
posterior produjo estos signos adicionales, aceptados en AUDIT_003:

1. **Concavidad geométrica puncturada:** (d/dx)²logτ(e^x)<0 para todo x.
   Prueba elemental con Poisson y cotas racionales uniformes; no depende de
   ceros. No se afirma prioridad bibliográfica.
2. **Anticorrelación estricta:** para d,e>1 coprimos,
   Cov_y(1_{d|N},1_{e|N})<0 para TODO y>0. No es la PSD automática de una
   covarianza; determina el signo de su interacción cruzada.
3. **Factores primos:** Cov_y(v_p,v_q)<0 para p≠q, y
   Var_y(log|N|)<Σ_p(log p)²Var_y(v_p), con convergencia absoluta probada.
4. Para familias FINITAS coprimas dos a dos, la matriz C_y es definida
   positiva, tiene entradas cruzadas negativas y su inversa es positiva
   entrada a entrada. Esa estructura no se atribuye al nodo.

### Paso crítico coprimo

Si B_y(d,e)=τ(y)C_y(d,e), el término divergente de B_y en cero es
G₀(d,e)y^(-1/2), G₀=(gcd(d,e)−1)/(de). Para coprimos G₀=0 exactamente.
Se obtiene directamente, para α>0,

    A_α(d,e)=−∫₀∞y^(α−1)B_y(d,e)dy >0.

En α=1/4 no hace falta contratermino COPRIMO. B conserva el cociente
τ(d²y)τ(e²y)/τ(y); desnormalizar el factor exterior no lo elimina.
La diferencia conjunta converge; no separar sus dos integrales divergentes
sin la continuación correspondiente.

CONSTRUCTOR_004 y AUDIT_004 desarrollan además la no dependencia exclusiva
del producto de los índices y la extensión Mellin a todas las potencias de
DOS primos distintos. Ésta no autoriza sumar todos los primos en el peso
crítico sin una estimación uniforme.

### Lo que se alcanzó y lo que no

Se alcanzó un **resultado positivo parcial real**: una interacción cruzada
firmada, válida en todas las escalas y cuyo Mellin coprimo conserva el signo
en α=1/4 sin resta. No se construyó la forma PSD global que cierre O1.
Positividad de entradas no es positividad de forma; falta diagonal y mismo
primo, enlace exacto con Q_T, identificación del polar y control de todos
los tests/modos. α=1/4 por sí solo no verifica la ley de peso del nodo.
La anticorrelación podría heredarse por un Euler incompleto: no se demostró
la especificidad completa exigida al mecanismo final.

La primera ronda dejó controles negativos; la segunda deja este lema de
signo y un objeto explícito. El nodo y D siguen OPEN. No se escribió ningún
cierre en Paper 47 ni se repintaron celdas del grid.

Revisión final de segunda ronda: AUDIT_003 y AUDIT_004 favorables; sin
objeciones pendientes. El hito positivo alcanzado es auxiliar y firmado,
no el hito mayor del núcleo O1 con enlace completo.

## Rondas 005–007 — completación auxiliar y enlace funcional

**CONSTRUCTOR_005 / AUDIT_005: PROVED.** Todo el kernel canónico −Rα
queda SPD sobre coeficientes finitos de divisores distintos≥2:

    −Rα(A)=κ E_s|A−μ₁(A)|²+∫y^{α−1}τ|E_yA−μ₁(A)|²dy,
    s=2α∈(0,1), κ=−2π^{−α}Γ(α)ζ(2α)>0.

La diagonal de R y los bloques del mismo primo YA están pagados para ese
objeto. No se asignó una diagonal favorable ni se supuso positividad deQ.
No se usó una leyζnormalizable a s<1: P_s vive en finitísimas valuaciones.
La positividad se hereda bajo borrado finito; no es específica por sí sola.

**CONSTRUCTOR_006 / AUDIT_006: PROVED.** Con m=y^{−1/2}−τ,
0<m<1 y m(y)=y^{−1/2}m(1/y), la FE de Π transforma α en1/2−α,
con dilataciones fraccionarias explícitas y mismo parámetro en1/4.
Para una ley borrada, el perfil dual m_P^∨ difiere de m_P porΔ_P
explícito y no nulo. Esa identidad de un único perfil sí falla al borrar;
aún no se ha demostrado que aporte el signo deQ. No se atribuye aΠ
noHankel aαfijo sólo por escribir dos escalas.

**CONSTRUCTOR_007:** en el núcleo Haarcentrado de la completación de−R,
D_nA=1_{n|N}A(N/n) preserva el centro. V_n=n^{s/2}D_n es un semigrupo
de contracciones. El factor geométrico es isométrico y el defecto de norma
es exactamente

    ∫u^{α−1}τ(u)[1−q_n(u/n²)]|E_uA|²du ≥(1−1/n)Π(A).

El cálculo de adjuntos en el factor gaussiano no se transfiere automáticamente
al subespacio grafo. Las propiedades del monoide solas pueden ser genéricas;
la FE y la interpretación entera deben intervenir en el enlace concreto.

**Objetivo D activo.** Próximo paso: realizar la inversión de006 en el
espacio de007 y verificar la forma/traza que produzca, con dominio y
convergencia. No se da por existente una traza ni se identifica su signo
conQ por semejanza. Faltan ese enlace, todos los modos/ventanas, colas y
los sectores/polar requeridos por el portador declarado.

## Ronda008 — defecto de inversión verificado

CONSTRUCTOR008/AUDIT008: en el factorGaussian la inversiónU satisface
UGnU=M_bGn*, b²=r(y/n²)/r(y), r=τyτ1/y. b cruza1 en y=n.
No se puede importar una conjugación simple conadjunto al módulo.
La sucesión primorial que parecía producir una componente vertical
converge sólo puntualmente: su normaGaussian diverge. Prueba aritmética
elemental; no Mertens ni nueva hipótesis de ceros.

Sigue pendiente determinar el cierre y su invariancia; el cálculo de008
no decide ni clausurabilidad ni componentes verticales. El mapa conQ_T
no fue construido. Objetivo íntegroD active.

## Ronda009 — resultado de la prueba directa del enlace

LINK009/AUDIT009 descartan un semigrupoC0 que interpole n^betaV_n enlogn
para cualquierbeta, tambiénD_n. La prueba usa un vector concreto de007,
no un argumento de soporte ni información de ceros. Compresiónunitaria
fijaV_n excluida; paraD_n no se afirma esa segunda conclusión.

Por tanto no se puede pasar del módulo a un generadorMellin continuo por
simple interpolación de sus acciones. Falta otra realización/mapa y la
identidad conQ_T. SCOPE_P44_009 separa este resultado del sobrealcance
de rem:nointerp sobre interpolaciónweak* arbitraria. ObjetivoD active.


### Fase209 — LINK010: regularidad de una compresión de D_n (2026-10-19)

LINK_010_SPECTRAL_REGULARITY calcula, para cada observable finito centrado
no nulo A, incrementos con liminf ||D_mA−D_nA||²/log(m/n)^s>0,
s=2alpha, mediante n=1+kL,m=n+L fuera del soporte primo de A.
Toda realización D_n=P U(log n)J con mapas fijos acotados y U unitario C0
requiere momento espectral s INFINITO para JA: no Dom(|B|^(s/2)).
En alpha1/4, momento1/2 y potencia de dominio1/4. PROVED, revisión
independiente favorable en AUDIT_010. Sólo excluye compresiones con esa
regularidad; la compresión general permanece OPEN, igual que el enlace Q_T.
No se reabre la compresión normalizada009 ni se modifica el estado de D.


### Fase209 — LINK011: primer mapa continuo calculado y cotejado (2026-10-19)

LINK_011_MELLIN_GAUSS_MAP construye UF=Σ a_d(F)(X_d−1/d), con
 a_d=2∫ e^(x/2)F(x)W_d(e^(2x))dx en alpha1/4.
Convergencia enH por a_d=O_T(||F||/d), Sdd=O(d^-s); operador compacto,
featureC∞ y kernel efectivo suave. FEcoef paraFpar recupera exactamente
C(F)=∫Fcosh(x/2). No sumar el vector polar separado: diverge; cancelar
coeficientes primero. La igualdad Q_T=||UF||² en el portador continuo es
FALSA para ESTE mapa: tests polarcorregidos de alta frecuencia tienen
Q_T~logλ y||UF||→0. La dominación Q_T≥||UF||² sigue OPEN, igual que otros
mapas no suavizantes. No NO-GO generalO1, ni prueba deD. Revisión favorable en AUDIT_011.
Precisión006: no se exigen correspondenciasG/Π/v pieza a pieza; basta
identidad o dominación TOTAL sobre un core denso para norma de forma.


### Fase209 — LINK012: dominación011 refutada por test certificado (2026-10-19)

LINK_012_DOMINATION_FALSIFIER conserva exactamente el mapaU de011 y
prueba la desigualdad que había quedadoOPEN, sin reintentar la igualdad.
Test explícitoT=4/5, ω=5π/8, r=3(ω²+1/4)/(9ω²+1/4),
F=(cos3ωx+r cosωx)/sqrt(T(1+r²)), par, H0¹ y polar libre EXACTO.
CertificaciónArb128 y colasanalíticas: Q(F)<.002351, mientras el rango uno
positivo de005 da ||UF||²≥κ|Σa_dv_d|²>.26134304. Resto<−.25899.
Laplaceexacta de autocorrelación y expansiónK=2Σexp(−(2j+.5)u)
proporcionan comprobaciónindependiente sincuadraturagamma/peine:
Qupper<.001647953. Datos/códigoenLINK012_data. AproximaciónH1polarcorregida
extiende el falsificador a coreC_c∞. AUDIT_012 favorable, ambos scripts reproducidos.
Sólo escala EXACTA deU011: ninguna exclusión de reescalares pequeñas,
otros mapas/O1 niD. Esta dominación concreta ya no es un residuoOPEN.
No integraciónP47 ni cambio de celdas/conteos. ObjetivoD íntegro active.


### Fase209 — LINK013: toda escala fija deU011 falla para ventanas grandes (2026-10-19)

Diferencia nueva escrita respecto012: no cambiaU ni reintenta escala1;
calcula la respuesta del mismo mapa sobre la familia EXPLÍCITA de P47
lem:testfam aT→∞, y prueba la clase antesabierta de constantes arbitrarias.
El perfilM(F)=∫Fh cumple h(−∞)=−κ,h(+∞)=0, por sumaRiemann y Mellin
positiva de m=y^−1/2−τ. Para G_T=ω_k(x/T),k=ceil21T/e,F_T=P(D)G_T,
masaG_T/Tescapa compactos, derivadasL1 son o(T), y
M(F_T)/T→γ1²κ/8. AsíE_T≥κM²≥c0T². La prueba deP47thm:margin/cor:margin1
(CITED, inputsZ1/Z2 y fórmulaexplícita sólo para este falsificador) da
|Q_T(F_T)|/||F_T||²≤4e9Texp(−15.449T) paraESTAFAMILIA, no porinferir
un test de un ínfimo. NormF²O(T^1.5) => |Q|/E=O(√Texp(−15.449T))→0.
No existec>0 fijo conQ_T≥cE_Ten todasventanas. Cualquierc(T) eventual
requiere c(T)≤C√Texp(−15.449T); su existencia no se demuestra.
Pruebaanalítica sin nuevo cálculo numérico; AUDIT_013 favorable, inputCITED explícito.
No exclusión de otrosmapas, ni signoD nuevo. No integraciónP47/celdas/conteos.


### Fase209 — LINK014: quitar piezas positivas tampoco reparaU011 (2026-10-19)

Diferencia escrita:013 descartó una forma MAYOR porκvv*; no implicaba
falla de subformas. Aquíse prueba directamente cada pieza conMISMOa_d011.
ParaΠ, el perfil K_y(x)=2e^.5xΣWd(e2x)(qd(y)−1/d) es positivo,L1 y
∫K_y=C(y)=κΣvd(1/d−qd)>0. LocalCLTporFourier paraG_T ycotassupderivadas
=>B_FT(y)/√T→−γ1²g0 C(y)/4. Fatouen[1,2] daEΠ(F_T)≳T.
ParaG_s, G(d,2)=(1−1/√2)d^−.5 1_even; perfilh2boundedconlímites
−κ(1−1/√2)/2 y0. Riemannpares+masaescape danL2(F_T)≍T; Cauchycovarianza
=>E_G(F_T)≳T². κvv*ya daba≳T² en013. ConQ(F_T)CITEDdelpaper decreciendo
exponencialmente, TODA combinaciónfija nonegativanonula AκG+Bκvv*+CΠ
con MISMOa_d011 tiene |Q|/E→0. No constantepositivauniforme de dominación.
No inferencias de mayor a menor; nueva prueba para ambas subformas.
Sin numerics nuevos. AUDIT_014 y addendum favorables para toda la clase.
No se excluyen otros mapas, cancelacionesfirmadas ni factoresTdependientes.
ObjetivoD íntegro active/OPEN; no integraciónP47/celdas/conteos.


### Fase209 — CONSTRUCTOR015: dominio separado y cono PSD exacto (2026-10-19)

Diferencia nueva frente008: pequeños tilts positivos sobre muchos primosaltos,
no el primorial cuya normaGaussian divergía. ParaH=Σp^-s→∞,t=H^-2/3,
Z_u=∏(1+tp^-u), A=∏(1+tXp)/Z_s−Z_1/Z_s es Haarcentrado y satisface
Es|A−1|²→0, ||TA||≤C(Z_r−1)/Z_s→0,r=(s+1)/2>s, porΠdd de011.
Esto produce(√κ1,0)∈H. AccionesDnacotadas007 generan purosXd y dan
H=L²(P_s)⊕V,V=closureTA0. Tdensamente definido NOclausurable, con
sucesiónexplícita f2−(D2A_j−A_j/2)→0arith, imagen→q2−1/2≠0.
Las3formasκG,κvv*,Π son energías de3proyeccionesortogonales genuinas.
El conoPSD en su spanREAL sobreTODOA0 es exactamentea,b,c≥0.
Con014cierratambiéncombinacionesfirmadasPSDglobales deese span con
MISMOmapa011. No clasifica formas positivas sóloensuimagen niotrosmapas.
Psproducto devaluaciones, NOleyzetasobreN. NoV=todoGaussian niFEinvariancia.
Sin numerics nuevos ni inputnuevo de ceros. AUDIT_015 favorable a los tres teoremas.
No signoQ/D; objetivo íntegroactive, sin integraciónP47/celdas/conteos.


### Fase209 — LINK016: imagen par polar libre densa (2026-10-19)

Nueva diferencia frente015: ya no se suponePSDglobal; se calcula el
anulador de U_T011 sobre TODOS los tests pares polar libres. Enα1/4,
para cadaT>0, closureU_T(P_Tev)=H, tambiénparaelcoreC_c∞polarcorregido.
Prueba: ηd=<fd,h>=O(d^-1/4), c=Σηd/d converge; el perfilanalítico b_h
anuladorsatisface b_even=λcosh. Combμatómicaentera, a_n=Σd|nηd−c,a0=0;
μ'=μ−λδ0/2 es antiFourier porinyectividadGaussianenS'par (lemaentero
incluido). Fourierdecombenteraesperiódica=>μ'periodic=>constantcoeff;
Thetaμ'(1)=0 obliga0; divisorinductionηd0=>h0. No nuevo input de ceros.
Así cualquierformaHermítica Hcontinua PSDenU_T(core) esPSDglobal.
Con015+014cierratambiéncombinacionesfirmadascontinuas del span3piezas
positivas sóloenesa imagen, conMISMOmapa011. No finiteblockE_N, no formas
Hdiscontinuas, no otrosmapas/coefTdependientes ni signoQ. Auditoría favorable
independiente enAUDIT_016.md. D íntegroactive/OPEN.
