# Auditoría matemática de paper 36

## Veredicto

El resultado central defendible del manuscrito es la equivalencia estructural

\[
\mathrm{ARP\!\!-P}\Longleftrightarrow\mathrm{RH}.
\]

El sentido directo usa Pick–Nevanlinna: ARP-P produce interpolantes normales, la identidad analítica extiende la función y los canales detectan todo residuo no real. El sentido inverso usa que, bajo RH, cada canal es una transformada de Cauchy de una medida positiva. Esta equivalencia localiza correctamente la dificultad en ARP-P, pero no prueba ARP-P.

La afirmación más fuerte “todo salvo \(\Omega_7\) está probado” necesita corrección. Hay un solo residuo central equivalente a RH, pero varias piezas auxiliares anunciadas como cerradas son parciales, condicionales o contienen un paso inválido. No deben utilizarse como lemas en una continuación.

## Columna Step 1–15

| Bloque | Estado auditado | Contenido exacto |
|---|---|---|
| Step 1 | **DEMOSTRADO** | El cambio \(s=\tfrac12+iz\) traduce RH en realidad de los ceros de \(\Xi\). |
| Steps 2–3 | **DEMOSTRADO** | Los canales definidos por el lado de ceros convergen normalmente y tienen los residuos declarados. Esto define el objetivo; no lo realiza aritméticamente. |
| Step 4 | **DEMOSTRADO** con interfaz clásica | La fórmula explícita actúa sobre la clase de tests indicada. |
| Step 5 | **ABIERTO / FUERZA-RH** | ARP-P exige positividad para todo plano fuente finito y todo conjunto finito de nodos. |
| Steps 6–7 | **DEMOSTRADO bajo hipótesis de torre** | Una medida positiva da kernel Pick positivo y el cono PSD es cerrado. No se construye tower-ARP. |
| Steps 8–13 | **DEMOSTRADO como consecuencia de ARP-P** | NP matricial, normalidad fijada por pinning, identidad analítica, detección de residuos y simetrías eliminan polos fuera del eje. |
| Step 14 | **DEMOSTRADO bajo RH** | Los pesos de canal forman medidas positivas y dan ARP-P. |
| Step 15 | **DEMOSTRADO** | Ensambla las dos implicaciones. |

Por tanto, “catorce pasos cerrados” sólo es correcto si se conserva que varios son implicaciones condicionales a Step 5 o a una torre no construida. No son catorce fuentes independientes de evidencia.

## Estado corregido de H0–H8

| Nivel | Estado | Auditoría |
|---|---|---|
| H0 | **DEMOSTRADO** | Es conservación lógica de dificultad. Sirve como control de circularidad, no localiza por sí solo un teorema nuevo. |
| H1 | **DEMOSTRADO, escalar** | Un nodo para \(M_\Xi\) en \(\Re s>1\). No cubre canales matriciales con pesos complejos. |
| H2 | **PARCIAL** | El criterio Gershgorin para nodos suficientemente separados y altos es válido. La extensión a alturas acotadas no está probada. |
| H3 | **PARCIAL** | Cierra una región logarítmica y un enunciado casi en todo punto; no la desigualdad global de dos nodos. |
| H4 | **DEMOSTRADO como serialización** | Los determinantes de una secuencia acumulante caracterizan RH. No se demuestra su signo. |
| H5 | **DEMOSTRADO como equivalencia** | Positividad de ventanas y ARP-P son dos coordenadas de la misma condición. |
| H6 | **CUALITATIVO DEMOSTRADO; CUANTITATIVO NO CONFIRMADO** | Si RH falla existe algún testigo finito por contraposición. La construcción racional concreta no demuestra que su cola sea menor que el bloque negativo. |
| H7 | **PARCIAL** | SOS bajo RH y cierre de dos nodos en banda interior, caja fija y altura grande. No hay SOS aritmético global. |
| H8 | **PARCIAL** | Para \(N\) fijo, banda interior y traslación alta hay positividad. Falta uniformidad en \(N\) a una altura fija, que es justamente la carga terminal. |

### Fallo concreto de H2

Para una matriz hermítica \(K\),

\[
K_{ii}>0\quad\forall i
\]

no implica \(K\succeq0\). Compactitud sólo garantiza que \(\lambda_{\min}(K)\) alcanza un mínimo sobre un compacto; no determina el signo de ese mínimo. La prueba de paper 36 sí establece PSD cuando la suma de entradas fuera de diagonal queda dominada por la diagonal mediante Gershgorin. No establece el añadido para alturas acotadas. Ese añadido debe eliminarse o convertirse en una hipótesis verificable mediante menores principales o una dominación uniforme.

### Fallo concreto de H6

La proposición obtiene una cota de Rayleigh de la forma

\[
\lambda_{\min}P
\le
\frac{
-2|\kappa|\,|r(w_0)|\,|r(\overline w_0)|
+B_{\mathrm{far}}\|r\|_{\mathrm{far}}^2
}{\|c\|^2}.
\]

El teorema posterior borra \(|\kappa|\) aunque el canal no fue normalizado. Además, ajustar la fase sólo hace negativo el primer término; no prueba

\[
2|\kappa|\,|r(w_0)|\,|r(\overline w_0)|
>
B_{\mathrm{far}}\|r\|_{\mathrm{far}}^2.
\]

Lo demostrado es una reducción computable a dominación de cola. No es todavía un testigo negativo cuantitativo para toda configuración.

## Cadena \(\Omega\) auditada

| Enlace | Estado corregido | Observación |
|---|---|---|
| \(\Omega_1\) | **DEMOSTRADO** | RH equivale a que todos los ceros de \(\Xi\) sean reales. |
| \(\Omega_2\) | **DEMOSTRADO como equivalencia** | Realidad de ceros equivale a ARP-P mediante Steps 1–15. |
| \(\Omega_3\) | **DEMOSTRADO como equivalencia vía RH** | La positividad de todos los jets escalares en un punto regular y ARP-P caracterizan ambas RH. No hay una transferencia nivel a nivel desde todos los canales a un jet. |
| \(\Omega_4\) | **PARCIAL / REQUIERE REESCRITURA** | El defecto reference-whitened existe para todo \(N\); el whitening por \(J_N^\infty\) sólo mientras \(J_N^\infty\succ0\), hasta \(N_*(t_0)\). |
| \(\Omega_5\) | **CONTINUIDAD DEMOSTRADA; POSITIVIDAD CONDICIONAL** | Para cada \(N\), los jets son continuos cuando \(y\downarrow\tfrac12\). No se demuestra positividad interior incondicional ni uniformidad al tomar \(N\to\infty\). |
| \(\Omega_6\) | **DEMOSTRADO para familias completas vía RH** | Positividad de todos los jets de borde y \(\lambda_n\ge0\) para todo \(n\) son equivalentes porque ambas caracterizan RH. No existe una transformación positiva truncada nivel a nivel. |
| \(\Omega_7\) | **ABIERTO / FUERZA-RH** | Positividad de Li para todo índice. |

La cadena central sigue terminando en \(\Omega_7\), pero \(\Omega_4\to\Omega_5\to\Omega_6\) no puede citarse como un transporte incondicional ya cerrado. Debe distinguirse la caracterización global vía RH del pasaje constructivo interior–borde.

## Dos defectos que no deben mezclarse

El defecto global de signo usa una referencia positiva:

\[
\delta_N^{\mathrm{ref}}(z_0)
=
\min_{c\ne0}\frac{c^*J_N(z_0)c}{c^*G_N(z_0)c},
\qquad G_N(z_0)\succ0.
\]

Está definido para todo \(N\) en el dominio declarado y

\[
\delta_N^{\mathrm{ref}}\ge0
\Longleftrightarrow
J_N\succeq0.
\]

El defecto de dominación arquimediana usa

\[
T_N=(J_N^\infty)^{-1/2}J_N^{\mathrm{prime}}(J_N^\infty)^{-1/2},
\qquad
\delta_N^{\mathrm{arch}}=1-\lambda_{\max}(T_N).
\]

Sólo está tipado si \(J_N^\infty\succ0\). El propio lema del par de polos muestra que esa positividad falla después de una escala \(N_*(t_0)\). Toda afirmación asintótica \(N\to\infty\) escrita con \(T_N\) a \(t_0\) fijo queda sin objeto. El reinicio debe reservar símbolos distintos y declarar el dominio en cada teorema.

## Realización, muestreo y cascada

La capa operatorial es válida bajo auto-adjuntez, cota uniforme de fuentes y convergencia de resolventes, pero la construcción canónica de los operadores se remite fuera del manuscrito. La convergencia

\[
(\Phi_P^F)^*(A_P^\circ-z)^{-1}\Phi_P^F
\longrightarrow G_\Xi^F
\]

es precisamente una identificación fuerte; no se deduce de \(\Lambda(n)\ge0\).

Las leyes de muestreo, saturación factorial, recuperación de raíces y la cascada de de Bruijn–Newman contienen bosquejos o estimaciones uniformes pendientes. Pueden conservarse como programas condicionales, pero no deben sostener un cierre. En particular, la cascada \(t_N^*\to\Lambda_{\mathrm{dBN}}\) depende de cotas de detección y cola que no están demostradas con uniformidad suficiente.

## Ruta de envolvente: error de convergencia

La separación

\[
O(n)=\sum_\rho\left(1-\frac1\rho\right)^n
\]

no define una suma convergente. Bajo RH cada término tiene módulo uno y los pares no tienden a cero. La combinación de Li

\[
\lambda_n
=
\sum_\rho
\left[1-\left(1-\frac1\rho\right)^n\right]
\]

sí se interpreta con la convención simétrica apropiada. Por eso las reducciones estacionarias que aíslan \(O(n)\) deben retirarse tal como están escritas; el primer fallo ocurre antes de cualquier estimación de fase.

La identidad Laguerre en \(\Re s_0>1\) sí es reutilizable porque allí la suma prima converge absolutamente. El límite \(s_0\downarrow1\) debe mantener junta la cancelación entre polo y primos.

## Corrección del blanco primo: la cota absoluta no es \(\Omega_7\)

Del split declarado

\[
\lambda_n=\lambda_n^{\rm arch}+\lambda_n^{\rm prime}
\]

se sigue exactamente

\[
\lambda_n\ge0
\quad\Longleftrightarrow\quad
\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}.
\]

No se sigue la equivalencia con

\[
|\lambda_n^{\rm prime}|<\lambda_n^{\rm arch}.
\]

Cuando \(\lambda_n^{\rm arch}>0\), esta última cota es suficiente y más fuerte, porque también controla oscilaciones primas positivas que no amenazan Li. Con el propio split del manuscrito, el fallo ya aparece en \(n=1\):

\[
\lambda_1^{\rm arch}
=1-\frac{\gamma}{2}-\log2-\frac12\log\pi
\approx-0.55412,
\qquad
\lambda_1^{\rm prime}=\gamma\approx0.57722,
\]

mientras

\[
\lambda_1\approx0.02310>0.
\]

El rango excepcional puede determinarse exactamente. La representación

\[
\lambda_n^{\rm arch}
=1-\frac n2(\gamma+\log(4\pi))
+\sum_{r\ {\rm impar}}
\left[\left(1-\frac1r\right)^n-1+\frac nr\right]
\]

tiene diferencias segundas positivas:

\[
(\lambda_{n+2}^{\rm arch}-\lambda_{n+1}^{\rm arch})
-(\lambda_{n+1}^{\rm arch}-\lambda_n^{\rm arch})
=\sum_{r\ {\rm impar}}\frac{(1-1/r)^n}{r^2}>0.
\]

Con \(d_3\in(0.0062,0.0063)\), \(\lambda_7^{\rm arch}\in(-0.356,-0.355)\) y \(\lambda_8^{\rm arch}\in(0.020,0.022)\), más los valores directos de \(n=1,2\), resulta

\[
\lambda_n^{\rm arch}<0
\quad\Longleftrightarrow\quad
1\le n\le7.
\]

Por tanto la cota absoluta escrita en las secciones de anatomía y kernel primo no puede ser “la desigualdad exacta” para todo \(n\). Debe reescribirse como una estrategia suficiente para un rango donde la parte arquimediana sea positiva, con los índices restantes tratados aparte. El blanco mínimo de \(\Omega_7\) es el **lower bound unilateral** de la parte prima.

Esta corrección cambia el alcance de los no-go: los cálculos que toman \(|\psi(x)-x|\), suman normas o intentan controlar \(|\lambda_n^{\rm prime}|\) descartan rutas absolutas, pero no descartan el lower bound firmado. Cuando \(\lambda_n^{\rm arch}\ge0\), ese lower bound controla únicamente la excursión negativa; los índices con parte arquimediana negativa requieren tratamiento directo.

## Corrección de la integración por partes Laguerre

La representación regularizada de la parte prima mantiene la cancelación polo–primos. Defina

\[
f_{n,\varepsilon}(y)
=y^{-1-\varepsilon}L_{n-1}^{(1)}(\log y),
\qquad
f_{n,\varepsilon}(1)=L_{n-1}^{(1)}(0)=n.
\]

El polinomio polar del límite pareado es exactamente

\[
\sum_{k=1}^n\binom nk\frac{(-1)^{k-1}}{\varepsilon^k}
=
\int_0^\infty L_{n-1}^{(1)}(x)e^{-\varepsilon x}\,dx
=
\int_1^\infty f_{n,\varepsilon}(y)\,dy.
\]

Entonces

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[
\int_1^\infty f_{n,\varepsilon}(y)\,dy
-
\int_{1^-}^\infty f_{n,\varepsilon}(y)\,d\psi(y)
\right]
=-
\lim_{\varepsilon\downarrow0}
\int_{1^-}^\infty f_{n,\varepsilon}\,d(\psi-y).
\]

Como \(\psi(1)=0\), el extremo inferior aporta \(-n\). La integración por partes correcta es

\[
\boxed{
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\left[
-n+
\int_1^\infty
(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy
\right]
}
\]

o, equivalentemente,

\[
\lambda_n^{\rm prime}
=
\lim_{\varepsilon\downarrow0}
\int_1^\infty
(\psi(y)-y+1)f'_{n,\varepsilon}(y)\,dy.
\]

La fórmula impresa en paper 36 usa

\[
-\lim_{\varepsilon\downarrow0}
\int_1^\infty(\psi(y)-y)f'_{n,\varepsilon}(y)\,dy,
\]

que invierte el signo y omite el borde. Ya en \(n=1\) no reproduce \(\lambda_1^{\rm prime}=\gamma\). Si se conserva la definición del manuscrito

\[
A_n=\int_1^\infty|\psi(y)-y|\,|f'_{n,0}(y)|\,dy,
\]

la fórmula correcta sólo da \(\lambda_n^{\rm prime}\ge-n-A_n\); la triangulación necesitaría \(A_n+n\le\lambda_n^{\rm arch}\). Como el propio cálculo obtiene \(A_n\asymp0.27n^2\log n\), frente a un presupuesto arquimediano de orden \(n\log n\), el déficit cualitativo \(\Theta(n)\) sobrevive. Sus fórmulas y constantes, sin embargo, deben recalcularse. Toda nueva ruta firmada debe comenzar desde la identidad enmarcada, no desde la versión impresa.

La normalización asintótica de la envolvente requiere otra corrección. Para este split,

\[
\lambda_n^{\rm arch}
=
\frac n2\log\frac n{2\pi}
+\frac{\gamma-1}{2}n
+\frac34+O(n^{-1}).
\]

Por tanto, una afirmación con error \(O(\sqrt n\log n)\) debe conservar el término lineal \(\frac{\gamma-1}{2}n\); no puede absorberlo en ese error. Además, \(|\lambda_n^{\rm prime}|\le c\sqrt n\log n\) sólo puede enunciarse desde \(n\ge2\), porque en \(n=1\) el lado derecho es cero y \(\lambda_1^{\rm prime}=\gamma\). Estas correcciones no rehabilitan la ruta absoluta; fijan el enunciado que habría que comparar con la literatura.

## Alcance de los no-go de paper 36

Las paredes son filtros de clases concretas, no teoremas universales de imposibilidad. Sobreviven con este alcance:

- una positividad construida sólo después de asumir símbolo no negativo es circular;
- una extensión positiva abstracta no identifica el kernel aritmético requerido;
- las cotas de magnitud que toleran un cero fuera de línea no pueden probar Li positivo para todo índice;
- una suma por primos tomada término a término pierde la interferencia que sostiene el signo;
- la recurrencia de todas las fases examinada tiene un costo demasiado grande para la tasa de detección disponible;
- una geometría o polarización no construida es una condición suficiente, no un objeto existente.

No sobreviven como afirmaciones universales: “ninguna recurrencia puede funcionar”, “ninguna geometría puede existir” o “todo método clásico está excluido”. Esos cuantificadores no fueron formalizados.

La clausura Castelnuovo/Minkowski contiene además un fallo de signo: X3 se enuncia para clases de norma positiva y luego se aplica a una clase obtenida con norma negativa. M2 y sus consecuencias no quedan demostrados por ese argumento.

## Núcleo reutilizable

Puede conservarse:

1. la equivalencia formal ARP-P–RH;
2. la serialización escalar por jets en un punto regular;
3. el diccionario de Cayley \(w=1-1/\rho\);
4. la equivalencia completa con el criterio de Li;
5. las identidades finitas de Cauchy, Pick y Laguerre en sus dominios convergentes;
6. los cierres de banda con todos sus parámetros fijos;
7. el blanco primo unilateral
   \(\lambda_n^{\rm prime}\ge-\lambda_n^{\rm arch}\);
8. los no-go restringidos a la clase efectivamente demostrada.

Debe repararse o rebajarse antes de citarse:

1. el añadido compacto de H2;
2. el cierre cuantitativo H6;
3. la identificación global de los dos defectos;
4. la positividad atribuida a \(\Omega_5\);
5. muestreo, saturación y cascada;
6. la realización operatorial remitida fuera;
7. la envolvente que separa una suma divergente;
8. la identificación incorrecta de \(\Omega_7\) con una cota absoluta;
9. el signo y el término de borde de la integración por partes Laguerre;
10. la normalización asintótica de la envolvente y su dominio \(n\ge2\);
11. la clausura Castelnuovo/Minkowski.

La auditoría lógica completa que respalda este documento está en [`fragments/PAPER36_LOGIC_AUDIT.md`](fragments/PAPER36_LOGIC_AUDIT.md).
