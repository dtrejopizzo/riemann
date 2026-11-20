# POWER_EXACT_H_ORIGIN_AUDIT_098 — Auditoría independiente

Estado: **APROBADO**, constructor19778 exit0/FULL PASS128paneles y signoPOSITIVO. Reproducción independiente root57072 exit0/FULL PASS128, con H3/Th0 positivos y hash coincidente. Fuente `POWER_EXACT_H_ORIGIN_DESIGN_098.md` final leída íntegramente; diseño y código literal aprobados ANTES de la corrida. Hash comprobado localmente:

    bebcca70c5dd54ba53841e77542aa3e3e2ea059306061dc676e24f88ee5117c9

Papers intactos; un solo test de signo predeclarado, sin campañas.

## Dato exacto y regularización

La fórmula097 T_h0=12aH3/b⁴ fue reproducida independientemente por expansión formal. a>0 es varianza; b<0 procede de086R'0>0 yR=1/N, no de sóloM''<0 enelinterior. B0=(a−N)/x tienevalor−b>0 y da h=N/B0 analítica en0. Por tanto el signoH3 es exactamente el signoT_h0, no una condición de densidades más fuerte como093.

Los seis momentosparesI0..I10 dan la serieZ/Z0 concoeficientes m2k/(2k)!, pues la normalizaciónbilateral2cancela. m0=1exacto. La serie se declara conprec11 (sóloconocidosgrados0..10); logZprec11 yMderivativeprec10 conservan exactamente loscoeficientes1,3,5,7,9 deN=a+bx+cx²+dx³+ex4. No se rellenan coeficientes desconocidos, no se requiere el momento12 ni se confunden cumulantes normalizados con momentos positivos.

## Momentos, restos y literal

Se conserva093:128paneles[0,2],grado64/cap65/512bits,16modosconcolaCOMPLETAEPS. Para órdenespares hasta10, |t^rPhi|<3^10·2^22<1e12 enelrecintocomplejo. ElrestoTOTALdeintegración2e12·4^-65/(1−1/4)<1e−24 se añade simétricamente. Las colascoeficientesEPS32^k seincorporan aPhi0..64 ANTES de multiplicart^r.

La nueva colatemporal está adaptada alorden10: (2+s)^r<=1024exp5s, juntoPhi2+s<2^-140exp−300s, da(1024/295)2^-140<2^-138. Añadir[0,2^-138] aCADA momento esseguro; reutilizar2^-140de093habríasidoinsuficiente, yelcódigoNOlohace.

Elliteralnoimportacorridasanteriores. Verificaprecisión/finitud/positividad de momentos yseries, a>0,b<0. EvalúaH3=ace−ad²−b²e+2bcd−c³ y aceptaAMBOSsignos estrictos. Th0divide porb⁴ no nulo; no hayassertquefuercepositivo ni ajuste posterior de parámetros. La fuente conserva el diseño previo y documenta la ÚNICA corrida19778 conhashinmutable.

## Resultado y alcance

H3 está encerrado en unballestrictamentepositivo (centroaprox1.73824840842e−21) yTh0 en otropositivo (aprox3.15512974175e−5). Losdecimales son lectura; la prueba es elassertintervalar riguroso quepropaga todosloserrores. Elconstructor terminó exit0/FULL PASS128. Root57072 reprodujo independientemente exit0/FULL PASS128 con los mismos balls positivos y hash coincidente.

Se obtiene **T_h(0)>0 para la Phi real** y, poranaliticidad, positividad en una vecindad existente sinradio. Elorigenesauxiliar, no unexponenteWadmisible. Junto097 haypositividad enunentorno delorigen yentodalacola u>=512, no unempalmecompleto: elintervalointermedio sigueOPEN. NoT_hglobal,triplesGp,cinco/todoslosgeneradores,nuevaW/Tniobjetivoglobalresuelto. Consulta073/077/087–097yregistros distingueestejetEXACTOdelparticularmásfuerte093.
