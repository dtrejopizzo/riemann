# QRH — ensayo 4/5 y límite de la extrapolación geométrica conservada

2026-10-19. **PROVED: cálculo local y obstrucción algebraica en una clase
explícita de extrapolaciones. OPEN: nuevas estimaciones o nuevo probe.
No signo de D; no imposibilidad general de alcanzar4/5.**

## Corpus y objeto nuevo

Consultados las reglas del proyecto, ROUTES-TRIED-INDEX (L74 y revisiónQRH), grid maestro
y CROSSWORD-TO-D.md. Fuente: manuscrito OpenAI30Sept2026, texto local
/tmp/qrh-review/september.txt, §§7,15,16,20. No se reabre una rutaD.
Diferencia escrita: ensayar el umbral4/5 en las hipótesis concretas de esta
fuente, calculando qué sobrevive localmente y qué falla al conservar su
geometría de estimación de TODOS los subconjuntos reescalados. No se supone
que Prop15.3 ya esté probada para parámetros distintos de los publicados.

## 1. El numerador principal no es el bloqueo local

**PROVED condicional a las identidades locales de la fuente; aritmética de
exponentes verificada. No auditoría completa del manuscrito.**

En Lem7.1, ec7.17, ampliemos únicamente la segunda caja a

    xr≥4/5, zr≥33/200, wr≥19/20.

La misma estimación de Ep en la prueba da los exponentes de buenos primos

    4−6xr−6zr ≤ −179/100,
    1−xr−wr−6zr ≤ −87/50.

Como wr>0 no hay coste adicional de W. Los otros términos de7.17 cumplen
DW=O(Q^(-7/4)) y VW=O(Q^(-97/50)); los denominadores locales permanecen
uniformemente separados de cero, por los mismos exponentes positivos.
Así Hp−1=O(Q^(-87/50)) para p∤u. Para p|u, el peor exponente de la tabla
local es1−xr−wr≤−3/4; los restantes son menores. Esto da producto normal
y control divisor O_ε((Nu)^ε) como en la prueba original. Para u=1, la cola
sobre primos NP>P0 es O(P0^(-37/50)) por conteo de ideales; en particular
puede usarse O(P0^(-7/10)). Aumentar el corte fijo vuelve Hη cercano a1.
No se ha extendido con esto toda la prueba global ni sus contornos.

En el cálculo principal de§16, los cuatro exponentes son

    −xr, −6zr, 4−5xr−6zr, 1−wr−6zr.

En la caja ampliada son≤−4/5. Por ello el mismo cálculo local produce
Bp=−1+O(Q^(-4/5)). La contracción del numerador NO impide por sí sola4/5.

## 2. Geometría publicada: falta3/40 en la cota baja

La fuente tiene lx=17/48, ly=23/48, ell=1/6, b=ly−lx=1/8 y h=13/16.
Prop15.3 prueba el exponente bajo L=lx/2+b/12=3/16. La normalización es
CII(s)=s−11/16, por lo que CII(4/5)=9/80 y

    L−CII(4/5)=3/40.

Con esa cota solamente, no se verifica el criterioProp2.1 para un supuesto
β*∈(4/5,7/8]: se necesitaría un ω al menos3/40 para cubrir el exponente
bajo, pero también ω<β*−4/5≤3/40. Es insuficiencia de la cota, no una
cota inferior sobre el probe verdadero. Mejorar cancelación puede cambiarla.

## 3. Plantilla de extrapolación y pérdida de la norma completada

La geometría satisface ly=lx+b, 2lx+b+ell=1, h=1+ell−lx y
M=lx+ly=1−ell. Consideremos su extrapolación conservando la MISMA cadena
de cotas de§15, con b≥0, ell≥0, y sus condiciones de aplicabilidad.
Esto es una plantilla condicional de estimaciones; no se afirma que los
lemas analíticos ya estén probados para geometrías no publicadas.

No es correcto conservar sin más la norma completada Z^(M'+ε) de15.1:
ese cierre usa ell=1/6. En su prueba, para el subconjunto reescalado de
longitud d∈[0,ell], M'=M−2d y ell'=ell−d. Antes de sustituir los valores
publicados, la segunda rama de la ecuación(15.3), en la prueba deLemma15.1,
contiene la pérdida

    (1+3ell'−2M')/4 = (5ell−1+d)/4.

La primera rama da M' sin esa pérdida. Repitiendo ESTA majoración de las
dos ramas resulta la plantilla de exponente para la norma CUADRADA

    M' + ((5ell−1+d)/4)_+.

Esto conserva el paso M'+ell'−1=−3d usado en la prueba. No es una
estimación inferior ni una afirmación de que el extremo de cada rama se
alcance; es el coste del bound que se está extrapolando.

## 4. Umbral de la plantilla conservada (PROVED algebraicamente)

En Cauchy–Schwarz, la pérdida anterior se divide por dos. El cómputo de
tuplas, coeficientes y longitud X' de15.8 sigue aportando −d. El exponente
adicional para el subconjunto d es por tanto

    f(d)=−d+(5ell−1+d)_+/8.

Es decreciente en d, con pendientes −1 o−7/8. Su máximo sobre[0,ell]
es f(0)=(5ell−1)_+/8. Si se conserva la absorción aditiva de15.7, la
plantilla total de cota baja es así

    L=lx/2+b/12+(5ell−1)_+/8.

La normalización principal es C(s)=lx/2+s−1+h/6. El umbral formal que
resuelve C(σ_low)=L es

    σ_low=11/12−ell/4+(5ell−1)_+/8
          =11/12−ell/4                 si0≤ell≤1/5,
          =19/24+3ell/8                siell≥1/5.

La primera rama decrece y la segunda crece. Su mínimo en TODO ell≥0,
incluso relajando restricciones de longitudes, es

    σ_low(1/5)=13/15 > 4/5.

Por tanto la plantilla conservada de cotas no certifica4/5 cambiando sólo
la geometría. El cálculo ingenuo que omite la pérdida de norma completada
da11/12−ell/4 y pediríaell≥7/15; pero paraell=7/15 la plantilla correcta
da29/30, no4/5.

Esta es una obstrucción algebraica a la extrapolación de estas
MAJORACIONES, no una barrera universal13/15 del método o del probe.
Incluso en esta plantilla relajada falta un ahorro adicional de al menos
13/15−4/5=1/15 en el exponente para llegar a4/5 (sin contar pérdidas
positivas). Ese ahorro debe venir de una estimación nueva; no es un
parámetro libre.

El mínimo no es un nuevo resultado externo13/15: no se ha verificado
que sus otras hipótesis puedan satisfacerse enell=1/5.

Un candidato concreto para ensayar ese mínimo formal es

    ell=1/5, b=1/10, lx=7/20, ly=9/20, h=17/20.

Cumple las relaciones geométricas anteriores. El exponente bajo de la
plantilla es L=11/60 y C(s)=s−41/60, con C(13/15)=11/60.
Incluso en el subconjunto totalmente reescalado, M'=2/5>0 y
ly−ell−11b/6=1/15>0. Esto verifica esas condiciones ESCALARES;
no verifica todas las hipótesis analíticas ni los detectores y la
comparación alta. Es un candidato para un siguiente ensayo, no un
teorema13/15 ni una mejora demostrada de la región libre.

## 5. Condiciones adicionales y límites

Para conservar la absorción Pa²/Y'≲Pa^(1/6), con Pa≈Z^b y
Y'≈Z^(ly−d), se necesita ly−ell−11b/6≥0. Sustituyendo
ly=(1+b−ell)/2, resultaell≤1/3−8b/9. Es una condición adicional de la
cadena de cotas, no una mejora de su mínimo formal anterior. b>0 asegura
Pa≥1 eventualmente cuando el factor fijo Nb*>1; permitirb=0 sólo relaja
las condiciones necesarias. Con exponentes iguales a cero hay que
comprobar además factores constantes y márgenes de las aplicaciones.

Para bajar del límite de la plantilla debe mejorarse al menos un bound:
la segunda rama de la norma completada, la estimación aditiva, o la
sumación de subconjuntos/estructura del probe. No se ha obtenido aquí
esa mejora. Un bound más fino que demuestre que las ramas extremas son
incompatibles también escaparía del cálculo, pues éste conserva su
majoración separada, no prueba que se alcance.

El certificado de§20.4 tampoco se traslada sin recalcular. Congelar todos
los demás parámetros y cambiar la escala de referencia suma3/40 al
exponente bruto; eso NO prueba fracaso de una optimización distinta.
La comparación alta, las cuentas de detectores y sus márgenes tampoco
quedan probados por la minimización de la plantilla baja.
La cantidad dinámica κ=2β*−1, las capacidades y las cuentas cambian también
al tomar Δ=β*−4/5, y sus hipótesis deben comprobarse de nuevo.

No se construyó una prueba4/5 ni una fuente de signo paraD. El resultado
es más preciso: H no es la dificultad local, y cambiar sólo la geometría
conservando esta cadena de cotas bajas no llega a4/5.
