# Construcción 082 — Defecto equilibrado con regularización arquimediana

Estado: fórmulas (1)–(2), dominio y equivalencia de signo revisados independientemente. Es un balance de tipo Birman–Schwinger, no un mecanismo de signo nuevo.

## Cambio respecto de los anuladores de perfiles

BUILD079–081 no reprodujeron la cancelación de la forma sobre vectores casi nulos. Aquí se incluye esa cancelación completa en el operador, sin invertir la forma objetivo. Esto evita ajustar perfiles, pero puede trasladar íntegramente la obligación de signo; el residuo se calcula para comprobarlo.

Trabajar en el Hilbert primitivo P_T. Sean A el operador autoadjunto asociado a a_T, A_arch el asociado a la forma arquimediana comprimida a P_T y L=ΣΛ(n)/sqrt(n) U_log n. Poner s=ΣΛ(n)/sqrt(n), con n<exp(2T), y

    β_T=1−C0+2s,
    B=A_arch+β_T I,
    P=β_T I+Q(L+L*)Q.

B≥(1+2s)I y P≥(1−C0)I>0, pues ||L||≤s. Son operadores sobre P_T; B no es la forma objetivo. Se tiene A=B−P como identidad de formas y con perturbación acotada sobre Dom(B).

Definir

    C=B^(-1/2) P B^(-1/2)≥0,
    V F=(I−C) B^(1/2)F
       =B^(1/2)F−B^(-1/2)PF,

para F en el dominio de forma. La inversa sólo corresponde a la parte arquimediana desplazada B, cuya positividad está asegurada de antemano. En Dom(A), V=B^(-1/2)AF. No se emplea una raíz o inversa de A ni sus autovectores para definir V.

## Cuadrado y residuo exactos

Con x=B^(1/2)F,

    a_T(F)=<x,(I−C)x>,
    ||VF||²=<x,(I−C)²x>,
    ρ(F)=a_T(F)−||VF||²=<x,(C−C²)x>.                    (1)

En las variables originales,

    ρ(F)=<F,PF>−<PF,B^(-1)PF>.                           (2)

Todos los cruces entre contactos están presentes en PF y en el segundo término; no se sustituyen por una suma de normas independientes.

## Diagnóstico favorable y límite lógico

Si F es un autovector de A con AF=λF, se obtiene, sólo como diagnóstico,

    ||VF||²=λ²<F,B^(-1)F>≤λ²||F||²/(1+2s).

El candidato suprime automáticamente toda dirección casi nula con residuo operatorial pequeño, sin escogerla de antemano. Una pequeña razón de Rayleigh por sí sola NO basta para esta cota: se necesita controlar AF.

Pero C≥0 implica que C−C²≥0 si y sólo si C≤I. Además C≤I equivale a A≥0 por la primera igualdad de (1). Como B≥constante>0, x recorre todo P_T cuando F recorre Dom(B^(1/2)); no falta un subespacio en esa equivalencia.

Por tanto este diseño resuelve la incompatibilidad de extracción sobre autovectores casi nulos, pero NO reduce la obligación lógica de signo. Probar ρ≥0 es exactamente probar la contracción C≤I. No se supone esa contracción y no se presenta (1) como prueba de positividad.

## Qué sería una operación adicional

La fórmula (2) deja una diana concreta: una identidad aritmético-arquimediana que controle el apareamiento de PF con el Green positivo de B, conservando todos los cruces. Definir ese control como la norma óptima o volver a factorizar I−C sería circular. La regularización arquimediana ya está escrita; falta una razón independiente para la contracción.

Para falsificadores con pesos positivos, la misma construcción y las identidades existen al adaptar s y P. En una ventana negativa, C tiene una dirección espectral por encima de1 y el residuo también falla. Esa observación comprueba coherencia; no identifica todavía una ley aritmética que separe el peso verdadero.

## Desarrollo explícito de la compensación de los dos momentos

Cálculo añadido para revisión. Se distingue H0=L²(I) del subespacio primitivo. En H0 poner

    B0=A_arch,full+β_T I, G0=B0^(-1),
    E(z+,z−)=z+ e+ + z− e−,
    Hpol=E*G0E.

B0≥(1+2s)I; G0 es positivo e inyectivo. E es inyectivo y Hpol es una matriz2x2 estrictamente positiva. Definir

    Gprim=G0−G0 E Hpol^(-1) E*G0.                        (3)

Ésta es la extensión por cero sobre P_T^perp del inverso de la compresión primitiva B. En efecto, para fuente f, u=Gprim f cumple E*u=0 y B0u=f−E Hpol^(-1)E*G0f. Al probar contra cualquier h∈P_T, se obtiene b_B(h,u)=<h,f>; la coercividad da unicidad. Además Gprim E=0 y E*Gprim=0. No se confunde Gprim con QG0Q, que en general es distinto.

Con P0=β_T I+L+L*, para F∈P_T la fórmula(2) se convierte en

    ρ(F)=<F,P0F>−<P0F,G0P0F>+v(F)*Hpol^(-1)v(F),       (4)
    v(F)=E*G0P0F.

La última contribución es manifiestamente no negativa, pero de rango a lo sumo2. No se supone positivo el núcleo puntual de Gprim: positividad como operador y positividad del núcleo son propiedades distintas.

Se pueden escribir los dos funcionales sin aplicar el inverso a la fuente aritmética: kσ=G0eσ depende sólo de Arch, la ventana y β_T. Entonces

    vσ(F)=<kσ,P0F>=<rσ,F>,
    rσ=β_T kσ+Σ_n Λ(n)/sqrt(n)(U_log n+U_log n*)kσ.       (5)

Todos los contactos y las dos restricciones aparecen en(4)-(5), con sus cruces conservados. El problema pendiente es dominar el defecto <P0F,G0P0F>−<F,P0F> por estos dos funcionales para todo F∈P_T. No se afirma que el rango dos baste por una razón dimensional: precisamente esa dominación es lo que falta demostrar.

Para F tal que v(F)=0, la compensación desaparece. Cualquier prueba basada en(4) debe por tanto controlar el defecto completo también sobre ese subespacio; no puede usar la mera positividad de Hpol^(-1) como conclusión. Esto fija una condición verificable para un intento posterior de cancelación.


## Alcance de la revisión

La cota general es ||VF||≤||AF||/sqrt(1+2s); para AF=λF+r, es ≤(|λ|||F||+||r||)/sqrt(1+2s). No se deduce amortiguación de todos los tests de pequeña razón de Rayleigh sin controlar su residuo operatorial.

Antecedente conceptual verificado: P47 subsec:wh-det/thm:wh-pencil. No se importa su conclusión de clase traza: P≥(1−C0)I en dimensión infinita no es de clase traza. La equivalencia de orden operatorial aquí escrita no requiere esa propiedad.

La fórmula del Green restringido (3) también fue confirmada como eliminación exacta de las dos restricciones. Exhibir su término positivo de rango dos no prueba la dominación pendiente en(4).
