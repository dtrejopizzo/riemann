# Auditoría — completitud parcial en potencias perfectas

Estado: **Fuente completa §§1–11 aprobada matemática y literalmente.** Fuente:`SQUARE_COMPLETENESS_OBSTRUCTION.md`. Sin ejecución nueva. No se toca ningún paper ni se refuta el miembro Lambda.

## Familia y reutilización exacta de007_C

Para Fp=(1+cpz)/(1−z²),0<=cp<=1, expansiónlogarítmica yregla multiplicativa dan N(p2j)=1,N(p2j+1)=cp,N(n²)=1; ell(p^k)/logp=cp^k si k impar y2−cp^k si kpar. TodosloscoeficientesdeNestán en[0,1] yla combes no negativa. No se presuponeecuación funcionaldeladeformación.

Leído ROUND_007_C §§1–2: eltestigoexactodeTheorem1espar,H¹0,yprimitivo porque x eselcoeficientereal queanulaA exactamente;B=A. x>1 y elvalorcertificadoWa3/||F||²<=−.50528 soninputsexistentes, no calculados otra vez. a3 aquí borra TODOSlos poderesdelprimo2; no confundir la notaciónconotro borradodeprimosdephase198.

Con L=log5+1/5000,delta=L−log4,delta<L/7equivalea log(128/125)>3/5000 ysepagaporintegral1/u>3/128. Enelcollar sin3theta>2sintheta,sin5theta>0,sin7theta<=7sintheta; asímismoscoeficientesdanf(s)>1.384465sintheta>0. Modosimpares danf(L−s)=f(s),yC_F(log4)=integral0delta f(s)f(delta−s)ds>0.

Para c2=0,cp1restantes,ell4=2log2 ypesov4=2ell4/sqrt4=2log2. Loscontactos3,5igualana3,y2es0; Wnuevo=Wa3−2log2C_F(log4)<0. El polar siguecero sobreelMISMOtestigo. CompletitudenTODOSloscuadradosmáslosrequisitosdeclaradosNOgarantizasignouniforme deforma conese fondo fijo. Noexclusiónglobaldetodousodecuadrados.

## Residuo exacto, alcance del ansatz

Elmiembro c20esζ/(1+2^-s),residuo2/3,noFEasumida. Enelansatz0<=cp<=1,paraσ>1,Fc/ζ=producto(1+cp p^-σ)/(1+p^-σ),convergenteabsoluto. Siun cp0<1,elproducto<=esefactoryalσ↓1su límite superior<1. SiexisteresiduoR,entoncesR=limFc/ζ<1. ResiduoEXACTO1fuerzatodoscp1,inclusoconinfinitosparámetros. Sólo identificaelmiembroenESTEansatz; no aportasignodeWni excluyefamiliasmásgeneralesconresiduo1.

## Exponente fijo m>=2

Fm=ζ(1−2^-s)/(1−2^-ms) conservaEulerlocal2=1/(1−z^m). AsíN(2^k)=1_{m|k},otrosprimoscompletos,yluegoN(n^m)=1TODOn;ell(2^k)=m log2·1_{m|k}. Para m2eselcasoprevio;paraTODOm>=3,primercontacto2^m>=8estáfueradelaventana007C,de modoqueWm(F)=Wa3(F)<0exactamente. No nuevos testsni recorrido deparámetros. Residuo1/[2(1−2^-m)]<1. LacondiciónescompletitudparacadaexponenteFIJOseparado,no completitudsimultáneaparatodosm.

Dedup: endpoint2→4yafigurabaenR163_102CorFyejemploT{2},Q{4},confirmadoR163_191. Elcaso2→2^mesel mismo tipo de reemplazo finito. No se atribuye novedadalEulerendpoint; se usa el certificado primitivo previo para el argumento acotado actual.

## Lectura final de§§7–10 ypotencias simultáneas

Aprobadosliteralmenteelresiduo1dentrodelansatz yelargumentouniformeparamfijo. La extensiónsimultánea usaOTROmiembro: local2=(1−z/2+z²/2)/(1−z), N(2)=1/2 yN(2^k)=1 parak>=2, luegoN(n^m)=1TODOn,m>=2simultáneamente. Factorizarformalmentelcuadrático conr±=(1±i sqrt7)/4 daell(2^k)/log2=1−r+^k−r-^k>=0: k1=1/2,k>=2por2|r|^k<=1.

Pesosv2=sqrt2log2/2 yv4=7log2/4correctos. Reutilizar007C yC_F(log4)>0 más|C_F(log2)|<=norm² pagaWnuevo<−(.50528−.5)norm²=−.00528norm². Taylor positivoexp(.7)hasta3=12013/6000>2 ysqrt2<10/7 justificanv2<.5. No se calculó otrocontacto. Residuo7/8,noFEasumida,coefN2NOentero: elcontraejemploNOafecta clasesqueexijan esascondicionesadicionales.

La identificaciónentera§10 es independiente ycorrecta: N(p^k)=1k>=2, c=N(p)entero>=0 ylogcoefenp²=2−c²>=0 fuerzanc0/1. Sic0,localFp=(1+z³)/(1−z²)da coeflogderz6=2−3=−1. Luegoallc1⇒N≡1,ellLambda. No esunapruebadesignoparaLambda niNO-GOdetodacompletitudparcial. Estado111/112/WMnodisminuye. No nuevas ejecuciones; antecedentefiniteEuler endpointatribuidoR163102/R163191. Noquedanauditoríaspendientesdeestafuente.

## Última lectura literal§11 — reparación del residuo

APROBADA sin nuevo cálculo. Los factoresaltos Pdelta=1+delta z−delta z² mantienenNk1para k>=2 ydanNp1+delta. Factorización(1−rz)(1+sz), s−r=delta,rs=delta,0<r<s<1; el logcoefpar>=1−delta²−2delta>=1/25 eimparpositivo paganTODOSniveles. La elecciónfinita/racionaldeldelta finalporprimerproducto quealcanza8/7esexacta yexiste pordivergenciaelementalΣ1/p. No se ejecutó una búsqueda deprimos.

R(s)Dirichletpolynomialfinito conR1=1daresiduoEXACTO1 ysumN=x+O1porpisos; fuenteatribuyeesaidentidadalLemaSR163102. Nmultiplicativa≥0acotadaporCfinito,yALL-POWERSsimultáneo. PeroNp>1enprimoscompensadores yN2=.5noentero: no sedebeañadirN<=1/integralidad/FE asusrequisitos. Primos>=7invisiblesal007C⇒MISMOWnegativo<−.00528norm², sinactualizarcontactosnimargenporcálculo.

Se revisó ladistinción197: reparar residuono escontrolar ocompensarel defectoBohrDelta, yestosPdelta no sonlosfactoresgeométricosdeesaotrahipótesis. No haycontradiccióncon§7,que identificasóloelansatzcp<=1. Elresultadoañadido sigue siendo unfalsificadorde laclaseDECLARADA, no deLambda, cualquiercompletitudparcial ocompatibilidadFE. Noampliacionesnicampañas pendientesdeestaauditoría.
