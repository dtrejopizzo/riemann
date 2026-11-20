# Alcance de la equivalencia de inercia del sector par

Estado: corrección documental verificada independientemente. No es una prueba nueva de signo.

## Cotejo

El antecedente es `../phase-211-sign-sandbox/DOSSIER_001.md` §6(c), resumido en las Partes VI, VII.A y VII.C del índice maestro. La fuente primaria es Paper 47, `prop:H`, junto con `cor:H1minus`. El resumen de resultados positivos en VII.C omitía que la cota superior de inercia era un lado de una equivalencia, no un teorema incondicional disponible.

No se reabre una vía de inercia ni se construye otro criterio. Se corrige una premisa que podría producir un razonamiento circular al intentar demostrar el signo global. La diferencia es de alcance lógico de la herramienta registrada, no de notación ni de método matemático.

## Lo que afirman las fuentes

Escribir I(T)=n_−(A_ev(T)) para el índice negativo de la forma par sin polo. La primera frase de `prop:H` afirma

    [I(T)≤1 para todo T]  ⇔  [W_T^ev es PSD para todo T].

La equivalencia está etiquetada PROVED. No se sigue de ello que alguno de sus dos lados esté probado por separado. No se reconstruye aquí su demostración.

`cor:H1minus` afirma la cota en la dirección contraria:

    I(T)≥1 para T≥0.12.

Por tanto, BAJO la hipótesis de positividad global del sector par, se obtiene I(T)=1 para T≥0.12. La corrección de DOSSIER §6(c) evita exigir I(T)=1 en ventanas arbitrariamente pequeñas; no descarga la cota superior global.

## Corrección del registro

El resumen «≤1 autovalor negativo ∀T; =1 para T≥0.12 [PROVED]» debe sustituirse por:

    PROVED: equivalencia entre I(T)≤1 para todo T y positividad global del sector par.
    PROVED: I(T)≥1 para T≥0.12.
    Bajo la primera condición, I(T)=1 para T≥0.12.
    OPEN: establecer incondicionalmente la cota superior I(T)≤1 para todo T.

La cota superior no ha sido refutada. Tampoco se identifica aquí el sector par con todos los sectores ni se ofrece una nueva condición suficiente para el objetivo completo.

## Resultado

Se corrigen los resúmenes operativos del índice y se conserva la fuente histórica con una aclaración. Ninguna prueba futura puede invocar esa cota superior global como insumo ya demostrado. No se modifican papers ni se añade un NO-GO matemático. La positividad global permanece OPEN.
