> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# Incompatibilidad de caracteres en `pcu:product` (paper 53)

## Dictamen local

**(b) Incorrecto tal como está escrito.** La fórmula de `pcu:product`, líneas 3351–3352, no respeta la definición de los dos caracteres de splitting de las líneas 671 y 1732. La primera inferencia inválida de la demostración está en 3359–3360: después de restringir αβ a cada bloque, se afirma que puede asignarse β al primero y α al segundo «por la convención» de twisting. Esa convención no permite eliminar caracteres.

Este defecto también está presente en el volumen 58, líneas 37993–37994. No es una discrepancia entre una versión vieja y el volumen unificado.

El cálculo fue comprobado independientemente por el agente de theta, que cotejó las definiciones, la ley de twist, el producto externo y la aplicación al período. El producto externo no contiene una dependencia oculta en α o β que elimine los factores.

## Cálculo directo

El manuscrito define

`ω_{α,β}(g,h)=α(det g)⁻¹ β(det h) ω_Hom(g,h)`.

Escribir A(g)=α(det g) y B(g)=β(det g). La traslación de Heisenberg y los datos no modifican estos factores escalares. Bajo la factorización ortogonal de la representación sin twists que invoca la propia prueba:

| Expresión | Factor de caracteres |
|---|---|
| Lado izquierdo de 3351 | A(g)⁻¹ A(y)B(y) A(l)B(l) |
| Lado derecho de 3352 | A(g)⁻² B(y) A(l) |

Por tanto falta el factor

`A(g) A(y) B(l)`.

La identidad compatible con las definiciones sería

`LHS = α(det g) α(det y) β(det l) · RHS`,

con las mismas normalizaciones de producto que pretende usar el texto. Una constante fija de identificación tensorial no puede eliminar un factor que varía con los caracteres y con g,y,l.

Una forma general de distribuir correctamente los twists es: al descomponer el grupo de destino en dos bloques, el mismo carácter de destino aparece en **ambos**; los caracteres de fuente asignados a los dos factores deben tener producto igual al carácter de fuente original. En la fórmula impresa no ocurre ninguna de esas dos cosas.

## Por qué no es una identidad sólo en un soporte donde el factor valga 1

El lema cuantifica sobre caracteres α,β, datos finitos y vectores reales arbitrarios, y sobre g,y,l. No impone α(det g)α(det y)β(det l)=1.

Ya con α=1 y g=y=1, variar β sólo introduce en el lado izquierdo el factor β(det l). En el derecho no aparece β(det l). Elegir un carácter automorfo con componente arquimediana no trivial, como los de peso positivo que el contexto contempla, y l infinito próximo a 1 con β(det l)≠1. Los datos pueden elegirse con ambos funcionales theta sin twist no nulos en 1; por continuidad permanecen no nulos en un entorno. Esto excluye que el factor omitido se vuelva inocuo por anulación universal del kernel.

También puede comprobarse la incompatibilidad directamente a nivel de representaciones, antes de aplicar theta: los factores de determinante son distintos para operadores invertibles y tensores no nulos.

## Dependencia en la prueba global

El uso explícito está en `pcu:period`, líneas 3407–3410, con α=γ y l=u, variable que se integra sobre [U(W₀)]. Al conservar los caracteres, el integral que el texto identifica con I₀(ν) lleva además **β(det u)**, y fuera aparecen γ(det g)γ(det y). El módulo uno de ese factor no permite retirarlo de una integral oscilante.

La cadena de usos escrita es:

`pcu:product → pcu:period → pcu:coeff → P-top → P-std → P-matches/P-equal → pcx:X`.

`pcu:coeff` usa el reemplazo por el período en 3622; `P-top` se apoya en ese lema en 3732–3740; `P-std` usa `P-top` en 4513. El intercambio se usa después en los cuadrados y en la factorización del determinante de la cadena.

**Impacto demostrado:** esta ruta no prueba el intercambio como está escrita. No se deduce que el enunciado del intercambio sea falso, ni que RH sea falsa. Tampoco basta corregir sólo una igualdad de caracteres para declarar reparado todo el argumento: hay que reconstruir el período correcto, su no anulación y su dependencia exacta en ν, y comprobar que las identidades posteriores conservan el factor L_* requerido.

## Trabajo necesario para una reparación

1. Fijar de manera consistente los caracteres de cada factor al descomponer Hom(W₀,U⊕W₀).
2. Recalcular `pcu:period` y el coeficiente interno de `pcu:coeff` con esos caracteres.
3. Demostrar que el período resultante es el que entra en la razón de rango igual, o demostrar una nueva identidad que lo compare con ella.
4. Rehacer las deducciones de `P-top`, la constancia de la razón y el valor absoluto de c. No se ha aportado todavía una reparación completa en esta auditoría.

## Límite de una reparación por simple cambio de nombres

La factorización general compatible con la definición es

`ω_{a,b}(g,y⊕l)=ω_{a₁,b}(g,y) ⊗ ω_{a₂,b}(g,l)`, con `a₁a₂=a`.

Aquí los caracteres se entienden restringidos a los grupos de determinantes pertinentes. En particular, el carácter de destino es el mismo en ambos bloques. Si se quiere conservar exactamente el factor pequeño `ω_{γ,β}` y el factor de rango igual `ω_{γ,γ}` empleados en `pcu:period`, la fuente del producto sería γ², y el destino restringido a los bloques sería β⊗γ. Un twist único por el determinante del grupo grande restringe como b⊗b, por lo que no produce β⊗γ para caracteres distintos. Esto muestra por qué cambiar solamente el nombre de un carácter de fuente no arregla la identidad conservando los dos períodos del argumento.

Esta observación no excluye una reparación mediante una construcción diferente del dato, un período torcido o una identidad adicional. Delimita la obligación: hay que explicar cómo la nueva construcción conserva el período y su factor L, y no sólo obtener una identidad tensorial formal distinta. Para los caracteres arbitrarios que cuantifica el lema, esas condiciones adicionales no están disponibles en su enunciado.
