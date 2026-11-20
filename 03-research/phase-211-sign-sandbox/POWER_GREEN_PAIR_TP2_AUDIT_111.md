# Auditoría111 — monotonías individuales y signo paramétrico TP2

Estado: **Fuente base y extensiones aprobadas matemática y literalmente.** Fuente:`POWER_GREEN_PAIR_TP2_SCOPE_111.md`. Sin cálculos ni datos nuevos. Papers intactos.

La diferencia respecto074/101y091/105 es la implicación genérica desdeTODASlasmonotoníasindividuales Vp/K al signofijodelosmenoresparamétricos. No seusa la compatibilidadthetaREALni seafirmaqueelobjetoabstractolasatisfaga.

## Solución exacta y menores

Verificadoslambda_p=2−1/(2coshp), lasdosfórmulasVp, susvaloresyderivadasen1 ylosbordesVp'(0)=Vp(2)=Vp'(2)=0. La extensiónparcompacta esC1, sinδ eneloperadorsegundo. La fuerza interior es−A,exteriorB. Vp>0yVp'<0 paraTODOp>0en0<t<2; elcocienteno seusa fuera delsoporte.

Para q>p, elratiodecreceen1<t<2 porla derivadalogarítmicaq coth(qδ/2)−p coth(pδ/2)>0 conδ=2−t. Para p1,q2en0<t<=.5, fórmula exactadelratio yF(z,c) correctas. Elpasoc>1.5 exige∂cF=4(c−z)>0, válidoz<=8/7<c; luegoF>=23/98>0. Losmismosparams1,2dandosmenoresde signosopuestos enloscuatronodosfijos, no untestnumérico. No esTP2ni signoregular2 invertiendoun eje.

La regularizaciónsuave sólo preservasignosdeminorestodosfijos ymonotoníaslocalespara1,2. La fuenteNOsuponeglobalallpdespuésmollificar. Suencierrodeclaseesacotado yhonesto.

## Extensión con r estrictamente creciente

Para r_epsilon=1+step_(t>1)+epsilon t², K=1_(|t|<2), epsilon>0, λ sigue siendoelpromediocosh. En(0,2), W=Vepsilon' satisface(D²−p²)W=δ1+2epsilon t yW(0)=W(2)=0. GreenDirichlet es

`−sinh(p min(t,s)) sinh(p(2−max(t,s)))/(p sinh(2p))<0`.

AsíW<0paraTODOp>0 yVepsilon(t)=−integral_t^2W>0. LaextensiónparporceroesC1,mientrasr_epsilonesestrictamentecrecienteenelinteriorcomún. Losdosmenoresdependencontinuamenteenepsilon ysons estrictosenepsilon0; porlotantopersistensignosopuestosparaepsilon>0suficientementepequeño. Es afirmacióndeexistencia, no uncorte numéricoepsilonexplícito. No seafirmadensidadcompactasuaveconpropiedadesglobalesallp. ElcontraejemplosiguenoREALPhi/W.

Lectura final completa de§5.1/5.2 aprobada. La extensión estricta ylaopciónsuavizarsóloel escalóninterior conservanallp mientrasKsiguesiendoindicador; lafuente no promueve el suavizadodeambasdensidades a unahipótesisglobalallp. Laexistenciadelta>0porcontinuidadesexpresamentenonumérica. Noquedanpendientesdeauditoría111.

## Ampliación propuesta — monotonía completa del parámetro

Prueba matemática y lectura literal final de §5.3 APROBADAS. Para x=p², q_x=−derivative_tV_x resuelve A_xq_x=mu, A_x=−D²+x, Dirichlet0en0,2 ymu=Dirac1 (más2delta tdt enla varianteestricta). El kernelGreenpositivo escontinuo, condependenciaanalíticaenx>0yconderivadasuniformesparaxencompactos. Asíel intercambio conmedidafinitamu eslegítimo,incluidoDirac; no se presupone regularidad inexistente de la fuente.

Poner q_n=(−1)^n derivative_x^nq_x. Diferenciar A_xq_x=mu da A_xq_n=nq_(n−1), conbordesDirichlet0. PositividaddelGreenyfuenteinicialnonulaimplican q_n>0entodointeriorparaTODO n. V_x(t)=integral_t^2q_x(s)ds permite intercambiarlasderivadasenelintervalofinito. Entonces V_x(t)escompletamentemonótonaestrictaenx>0paratinterior. LosmenoresTP2opuestos111siguenigual: CMdelparámetro,másmonotoníasindividualesallp, no implicaTP2. No seafirmaCMdelafamiliaREALni seexcluyemétodoqueusemásestructura.

Se leyó la versión final de §5.3 con la convención q_n=partial_x^n q_x: la recurrencia A_xq_n=−nq_(n−1) y los signos alternados están correctos. La medida Dirac fija no obstruye diferenciar el Green; los argumentos de compactos y bordes son explícitos. No quedan pendientes de auditoría de la ampliación.
