# QRH — revisión alta de la geometría candidata

2026-10-19. Revisor independiente. **PROVED: cálculos de parámetros y
fallo de aplicabilidad de hipótesis publicadas. CONDITIONAL: transporte
de la fórmula alta a otra geometría. No nueva región libre de ceros.**

## Corpus, objeto y fuente

Consultados las reglas del proyecto, índice ROUTES-TRIED-INDEX, grid maestro y crucigrama
actual. Diferencia escrita: verificar las hipótesis altas de una geometría
específica que hasta ahora sólo tenía una plantilla baja formal. No se
reabre una fuente de signo para D ni se considera probada una extensión
de los lemas externos.

Fuente primaria: OpenAI, manuscrito30Sept2026, §§18–20, leído en
`/tmp/qrh-review/september.txt`. Las referencias siguientes son al texto
del manuscrito; no se realizó auditoría integral de sus demostraciones.

La candidata es

    ell=1/5, b=1/10, lx=7/20, ly=9/20, h=17/20.

## 1. Suministro de primos: estas desigualdades sí pasan

La comprobación de§20.5 exige ell/d>7/37 para el rango con selección.
Para 1/2≤d≤h, el mínimo candidato es

    ell/h=4/17,     4/17−7/37=29/629>0.

Además 5ell−h=3/20>0. Por ello cualquier extensión fija
0<zeta<3/20 mantiene ell/(h+zeta)>1/5>7/37. Con K par fijo
suficientemente grande, los tamaños de slot ell_i/d≤2ell/K pueden
quedar bajo cualquier umbral positivo de malla ya disponible. Este
cálculo no demuestra que dicho umbral esté disponible para los nuevos
parámetros: ése es un requisito analítico separado.

La normalización de§20.1 tampoco introduce una potencia adicional:
Z^(-ell/6)∏P_i^(1/6)=1 cuando Σell_i=ell. Su argumento de signo y
subpotencia del normalizador conserva la misma aritmética formal con K
par. Esto no valida todos los contornos ni la identidad alta modificada.

## 2. El trasplante dinámico no es la única elección de kappa

Lemma18.1 empieza con **3/4≤kappa≤1**. Su uniformidad de malla también
se declara sólo en ese intervalo. En§19 se usa la relación dinámica

    kappa=2beta*−1,

incluida en§20 como kappa=3/4+2Delta para Delta=beta*−7/8.

Si se intenta un extremo sigma0=13/15 y beta*=sigma0+Delta, resulta

    kappa=11/15+2Delta.

Para 0<Delta<1/120, kappa<3/4: el Lemma18.1 publicado no se aplica
con ESA elección dinámica.
En el objetivo sigma0=4/5, kappa=3/5+2Delta y la misma insuficiencia
se presenta para 0<Delta<3/40. Esto impide copiar literalmente la
capacidad dinámica, pero NO obliga a extender el teorema de momentos.

La condición real de Lemma18.1 para slots positivos y kappa<1 es
beta*≤(1+kappa)/2. Si se toma el resultado publicado7/8 como insumo,
con el alcance declarado para toda la familia Hecke relevante, se puede
usar conservadoramente kappa=3/4 para beta*≤7/8. Más generalmente,
kappa=max{3/4,2beta*−1} respeta el rango del lema y su condición de
ceros cuando beta*≤1. La malla uniforme publicada sí cubre esa elección.
Esto no verifica independientemente el insumo externo7/8.

La capacidad pasa a ser z_P=(1−2m)/(6kappa); es menor que la capacidad
dinámica formal cuando 2beta*−1<3/4. Deben recalcularse los cruces de
testigos, cuentas de filas y márgenes altos para esa capacidad efectiva.
El hallazgo es sólo una insuficiencia del trasplante DINÁMICO literal,
no un obstáculo inevitable del dominio de Lemma18.1. El problema del
piso de filas de la sección siguiente no depende de esta elección.

## 3. El certificado del piso de filas tampoco se transporta intacto

Conservar formalmente la primera línea de(20.4), reemplazando la
geometría y la escala de referencia sigma0, da en d=h

    E(h)=C_geom+(1/2+ell)delta+ell q−h(1−R),
    C_geom=lx/2−sigma0+5h/6.

Prueba algebraica: sustituir a=(1+delta)/2 y usar
ly=lx+b, 2lx+b+ell=1, h=1+ell−lx. Esta identidad es un cálculo de
la plantilla, no un nuevo bound alto fuera de la geometría publicada.

Para la candidata,

    C_geom=53/60−sigma0.

El piso de§20.2 usa delta0=1/50, R=1, q≤delta0/2, sin testigo de cero.
Aplicar esa misma majoración da

    E(h)≤C_geom+(4/5)delta0.

En sigma0=13/15, el lado derecho es

    1/60+2/125=49/1500>0.

Al comparar con C(beta*) se resta Delta. Así, el certificado conservado
no da margen negativo para todos los Delta>0: para Delta≤49/1500 su
cota superior no es negativa. Esto NO afirma que la contribución real
sea positiva ni que la cota sea óptima. Identifica el paso publicado
que ya no certifica el signo del exponente.

En sigma0=4/5, la misma cota sería149/1500. Incluso llevar el piso
delta0 a cero dejaría C_geom=1/60>0 en sigma0=13/15; cambiar únicamente
ese piso tampoco recuperaría el certificado formal. Una estimación
distinta de filas, o una reorganización que mejore esta majoración,
requiere demostración adicional.

## 4. Certificado conjunto relajado: no basta mover los slots

Para una geometría formal variable, el mismo cálculo del piso exige que
la escala de referencia supere el umbral de su majoración

    sigma_floor=2/3+b/6+ell+(1/2+3ell/2)delta0.

Con delta0=1/50 publicado, esto es

    sigma_floor=203/300+(103/100)ell+b/6.

Combinarlo con la plantilla baja de QRH_FOUR_FIFTHS_ATTEMPT da el
problema puramente algebraico de minimizar, en ell,b≥0,

    max{11/12−ell/4+(5ell−1)_+/8,
        203/300+(103/100)ell+b/6}.

Relajar b a cero sólo puede reducir ese máximo. Antes de ell=1/5 la
primera función decrece y la segunda crece; se cruzan en ell=3/16, con
valor167/192. Después de ell=1/5 ambas crecen. Por tanto el ínfimo
relajado es exactamente

    167/192 > 13/15 > 4/5.

En particular, para 0<b≤1 el cruce es
ell=3/16−25b/192 y el mínimo aumenta a167/192+25b/768. El caso b=0
relaja la aplicabilidad de Pa≥1 y no se declara realizable por el probe.
Tampoco el ínfimo obtenido es una nueva región libre de ceros: sólo es
el piso de este par de certificados formales conservados. Para obtener
un margen estricto se requieren además las holguras y pérdidas analíticas.

Si se permitiera llevar delta0 a cero, el problema relajado tendría
ínfimo13/15 en ell=1/5,b=0. Así ni esa relajación puramente algebraica
autoriza4/5 conservando estas majoraciones. Mejorar alguna de ellas o
su compatibilidad es una tarea adicional; no se excluye que pueda hacerse.

## 5. Balance de la revisión

El suministro escalar de slots no bloquea esta candidata. En cambio,
hay dos cambios concretos para reutilizar la parte alta: reemplazar la
elección dinámica de kappa por una autorizada, recalculando sus capacidades,
y reparar la pérdida de holgura del piso de filas en(20.5). El primero
no exige por sí solo extender Lemma18.1 si se acepta el insumo externo7/8.
No se han recalculado aquí el certificado
adaptativo completo, las comparaciones de capacidades ni todos los
contornos: siguen pendientes, no se declaran aprobados.

La geometría candidata no constituye una prueba13/15 y mucho menos4/5.
Estos hallazgos delimitan tareas matemáticas necesarias para esta
extrapolación; no clasifican todos los probes o métodos externos y no
aportan signo de D.
