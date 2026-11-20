# Auditoría108 — determinante polinómico correlacionado

Estado: **DISEÑO Y LITERAL APROBADOS; ejecución fija INCONCLUSA reproducida independientemente.** Fuente:`POWER_MIXED_FOUR_POLYNOMIAL_DESIGN_108.md`. La diferencia respecto107 es el orden algebraico de evaluación, no aumentar parámetros tras un resultado.107 sigue INCONCLUSO sin falsificador. Papers intactos.

Los módulos107 permanecen intactos y deben verificarse porhash antes de importar. El builder mantiene errores de momentos, a ymodos en coeficientes intervalares. Formar todos los24productos como polinomios y no truncarlos encierra el determinante polinómico de coeficientes verdaderos truncados, preservando la variable común lambda. No se supone correlación favorable entre errores de coeficientes.

El bound de entradasB=2^62 yresto porentrada epsilon=2^-400 son los auditados107. Para los polinomios de coeficientes verdaderos, sus valores difieren de las funciones exactas por epsilon, por lo que tienen módulo<B+1. Telescopar los24productos paga96epsilon(B+1)^3<2^-200. No hace falta afirmar que cualquier ancho de una evaluación intervalar del polinomio sea menor queB+1; sólo que el polinomio verdadero contenido en el encierro cumple ese bound. La aritmética intervalar paga aparte redondeo ycoeficientes.

TrasladoTaylor en centrodyádico: cada coeficiente esoutward y se conservan TODOSlos grados. Lower=b0.lower−sumabs(bj).upper*h^j−2^-200 yupper análogo danencierro para toda la celda. No son muestras. El grado2048 es un máximo seguro; el código no debe recortar coeficientes inciertos ni tratar bolas quecontienen0 como coeficientes exactamente nulos.

El algoritmo mantiene los límites107 y cobertura completa antesPASS; origen noPASS impideREST. El presupuesto puede resultar INCONCLUSO o costoso; no promete signo ni viabilidad. Antes de correr se requiere lectura literal y verificación local de la API de traslado polinómico, junto con hashes. Ninguna evaluación theta se ejecutó en esta auditoría.

## Literal108 y API

Leído completo `tools/power_mixed_four_polynomial_108_verify.py`. Hashes107 se comprueban antes de importar, losmódulos sonintactos ylaimportaciónnoevalúatheta. Qpoly=−phi−2lambda phi' y susderivadas soncorrectas.24permutacionesseformanconproductos completos; no se truncagradoniseeliminancoeficientesinciertos.

Verificada laAPIlocal de composición en untoy racional 1+2x+3x², trasladado porx+.5:lasbolascoeficientescontienen(2.75,5,3). Igualdadestructuraldearb_poly no se usócomo prueba; contenciónporcoeficientes sí. No seevaluó theta. El literal traslada concentro exacto dyádico ysumatodoslosgrados;radiooutwardincluye2^-200antesdecidirsigno. DFSleftfirst/presupuestos/coberturaexacta1/4conservados; REST107sólocorretrasPASSorigen108. Revisiónliteralaprobadaantesdatos; root coordinaunúnicoproceso, sinpromesaPASS.

## Resultado y diagnóstico sin nuevas evaluaciones

Root82660 y mapa28564 terminaronexit2/INCONCLUSIVE: grado2042,15evaluaciones,4aceptadas,cobertura141/8192,depth10en[141/8192,1129/65536],det[+/−2.04e−4]. RESTnoejecutado. Hashdriver eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a y107intactos,conlogsseparados.

La réplica usó sys.setprofile para registrar SÓLO locales existentes alretorno evaluate: left,right,coefficients[0],radius yvalor devuelto enlas15celdas. No hubo nuevas evaluaciones de theta o de polinomios. Enelúltimoencierro coefficient0=[+/−1.79e−4],mientraselradioadicional≈2.4560e−5. El propiocoeficiente central ya contiene0; no se puedeatribuir todoel ancho ala variación dentrodelacelda. Tampoco esto decide sihaycero realni cuálfuente de incertidumbre dominaenla construcción. Enlos intervalosmásanchos aparecenballs muygrandes; sólo describenencierros, no magnitudrealcertificada.

El literal paró correctamente sinpromover cobertura parcial. Noesunfalsificador niunaobstrucciónmatemática; ninguna nuevaW/T/allorders. No se editaronparámetros trasdatos.
