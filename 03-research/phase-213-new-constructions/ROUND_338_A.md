# Dos copias del mismo bloque de Möbius en la media local

Para X grande, δ=1/j con j≥3, h=X^(−δ), fijar 0<ε<1/2−δ. Poner D=⌈2√X⌉, L=X^(1−δ−ε)/D y M(d)=μ(d)1_{L<d≤D}. Definir W_x(v)=η(log(x/v)/h). Uniformemente en X≤x≤2X,

    S_h(x)−2S_h(x/2)
      = −Σ_{k≤2X/L²} Σ_{d,e} M(d)M(e)[W_x(kde)−2W_x(2kde)] + O_B(X^(−B))

para cualquier B fijo. También se puede cortar k en O(X^(δ+ε)) si se impone de>X^(1−δ−ε). La fórmula con el corte más largo conserva un cuadrado de convolución exacto M*M, sin corte dependiente del par.

**Identidad y error.** Para U(d)=μ(d)1_{d≤D}, la convolución μ−2U+U*U*1 es (1*U−e₁)^( *2 )*μ. El defecto entre paréntesis se anula hasta D, luego todo el residuo se anula hasta D². Los términos 2U desaparecen en ambas muestras porque n está en (xe^(−h)/2,x] y supera D. Para cada l=de≤X^(1−δ−ε), los dos peines de múltiplos de l y 2l tienen la misma contribución integral tras el factor dos. En la variable real k, el pulso W_x(lk) tiene longitud comparable a J=hx/l y norma L¹ de la derivada de orden N acotada por C_N J^(1−N), por la regla de la cadena en su soporte. La sumación de Poisson y N>1 dan error O_N(J^(1−N)) para el peine; el mismo argumento vale a paso 2l. Aquí J≥X^ε. Hay O(D²)=O(X) pares. Elegir N según ε,B permite borrar cualquier subconjunto de esos pares completos, incluyendo todos los que tienen min(d,e)≤L. Por soporte k≤2X/L² en el rectángulo restante. Si se borran todos los pares pequeños, el corte para k mejora al indicado.

**Equivalencia.** La media cuadrática de este bloque en dx/x satisface el criterio de 337 con techo X^(1+ε')h para cada ε'>0 y j≥3 si y sólo si vale RH. En efecto el transformado de Dirichlet para S_h(x)−2S_h(x/2) es F(s)(1−2^(1−s)); sus coeficientes están acotados por 3. El factor extra conserva cada polo con 1/2<Re s<1 pues sus ceros tienen parte real uno; ζ no tiene ceros en Re s=1. Bajo RH el factor está acotado en cada franja considerada. El argumento dual con el peso φ y el error O(Xh^K) de 337 se aplica por tanto sin cambios, y el error uniforme O_B(X^(−B)) pasa a la norma local.

**Comparación con el antecedente.** 049 ya obtuvo factores cerca de √X mediante correcciones en progresiones para un déficit puntual. Su peso exterior a(k)+c(k) es distinto del interior μ(m). Aquí la misma sucesión real M interviene dos veces y la norma es la media de 337. La convolución simétrica permite escribir un cuadrado ordinario de polinomios de Dirichlet, que puede tener fase compleja. Eliminar factores cortos es una aplicación de inversión truncada y Poisson; la cota de la media del bloque simétrico sigue abierta.
