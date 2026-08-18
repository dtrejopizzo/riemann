# Registro consolidado de no-go, circularidades y retiros

## Regla de uso

Un no-go tiene la forma

\[
\mathcal H+\mathcal M\Longrightarrow
\text{el mecanismo no puede entregar }\mathcal C,
\]

donde \(\mathcal H\) son hipótesis y \(\mathcal M\) es una clase de métodos formalizada. Sólo cierra \(\mathcal M\) bajo \(\mathcal H\). No autoriza la frase “ningún método de este lenguaje puede funcionar” si el teorema sólo analiza un kernel, una normalización o una familia finita.

El registro separa:

- **REFUTACIÓN:** hay contraejemplo o inferencia inválida;
- **INSUFICIENCIA:** el input admite todavía un cero fuera de línea o pierde información decisiva;
- **CIRCULARIDAD:** la hipótesis ya contiene una condición de fuerza-RH;
- **DUPLICACIÓN:** cambia la coordenada del mismo residuo sin crear una estimación nueva;
- **CONDICIONALIDAD:** el mecanismo sería válido si se construyera un objeto aún inexistente.

## Matriz de rutas ya recorridas

| Familia | Veredicto | Alcance exacto |
|---|---|---|
| Multiplicatividad y clases \(\omega\) | **REFUTADA como criterio de ceros** | Liouville y funciones multiplicativas aleatorias rompen la inferencia. Las identidades de energía siguen válidas. |
| Coherencia, colas, GEV y clasificación | **REFUTADA como cadena de prueba** | Los parámetros dependen de generador, selección y escala; un clasificador finito no cuantifica sobre ceros desconocidos. |
| Matrices de picos como inversión espectral | **REFUTADA** | Responden principalmente a coeficientes, conductor, soporte y ablaciones; la inyección de ceros no reproduce el efecto. |
| Gram construida sólo con ceros | **REFUTADA como detector de horizontalidad** | Es PSD por construcción y puede haber descartado la coordenada que debía distinguir. |
| TDA y geometría de nubes | **INSUFICIENTE** | Una distancia finita o una nube truncada no excluye un cero futuro ni controla el divisor completo. |
| Positividad finita de Li, Mercer o Weil | **INSUFICIENTE** | Un tramo finito no controla todos los índices o tests. La cuantificación completa es fuerza-RH. |
| Forma de Weil frente a residuo truncado | **CONFUSIÓN REFUTADA** | El residuo entre dos cortes no hereda la positividad de la forma completa. |
| Cotas puntuales de \(\psi(x)-x\) tomadas en valor absoluto | **INSUFICIENTE en la ruta ensayada** | Se pierde la fase contra el kernel Laguerre y aparece un déficit de orden medido; no descarta toda desigualdad firmada. |
| Positividad de \(\Lambda(n)\) término a término | **INSUFICIENTE** | El whitening amplifica las normas individuales y destruye la interferencia entre primos que sostiene el signo. |
| Truncación prima positiva | **REFUTADA** | Las secciones finitas pueden ser negativas mientras la forma completa observada es positiva; no hay “parte positiva menos cola pequeña”. |
| Regiones libres y densidad de ceros | **INSUFICIENTE para todos los \(n\)** | Admiten un cero fuera de línea; ese solo cero puede forzar coeficientes de Li negativos en índices grandes. |
| Recurrencia casi periódica de todas las fases | **INSUFICIENTE para el esquema cuantificado** | El costo de emparejar el vector completo supera la ganancia de detección disponible. No es no-go universal para toda función escalar. |
| Fejér–Riesz | **CIRCULAR en la aplicación propuesta** | Requiere no negatividad del símbolo de borde, que es precisamente la positividad buscada. |
| Kreĭn y extensiones positivas | **INSUFICIENTE** | Existencia de alguna extensión positiva no identifica que el kernel aritmético sea esa extensión. |
| Calor y de Bruijn–Newman | **INSUFICIENTE sin input aritmético** | La dinámica caracteriza el régimen real, pero no determina el parámetro terminal; la cascada adicional tiene cotas uniformes abiertas. |
| de Branges y Hermite–Biehler | **CIRCULAR o incompatible en las condiciones ensayadas** | Las condiciones útiles implican real-rootedness; formulaciones clásicas concretas ya fallan para el objeto propuesto. |
| Aproximantes con ceros reales | **FUERZA-RH en la convergencia** | Si convergen localmente a \(\Xi\), Hurwitz transmite la realidad. Construir esa convergencia es el trabajo decisivo. |
| Índice finito de Pontryagin | **CONDICIONAL / INSUFICIENTE** | Depende de finitud del defecto y no excluye infinitas órbitas fuera de línea. |
| Símbolo GLT, índice y pasividad | **DUPLICACIÓN** | En el límite completo vuelven a positividad global o a una condición Herglotz equivalente. |
| Hodge, Lefschetz y superficie absoluta | **CONDICIONAL** | Una geometría real podría ser decisiva; el corpus no construye objeto, diagonal, cohomología, Frobenius y polarización compatibles. |
| Trasplante Castelnuovo/Minkowski | **REFUTADO tal como está escrito** | La condición X3 para norma positiva se aplica a una clase de norma negativa. |
| Prolate, gap y cuasimodo | **INSUFICIENTE** | Un gap no identifica el estado base ni excluye índice negativo sin una cota adicional; esa cota vuelve a Weil. |
| Pseudoinversa sobre curva singular | **REFUTADA** | Deben usarse adjugados/cofactores polinómicos; dividir en el punto singular pierde el objeto. |
| Matching célula por célula | **REFUTADO** | La cancelación es acoplada; separar sumandos destruye la identidad firmada. |
| Momentos holomorfos de un nivel | **REFUTADA como recuperación de divisor** | Representaciones firmadas distintas tienen los mismos momentos finitos; falta soporte transversal y multiplicidad lineal. |
| Productos de trazas para recuperar conjugación | **REFUTADA** | Crean todos los pares y peso cuadrático en multiplicidades; restringir después no reconstruye el grafo conjugado. |
| Convergencia de divisor real sensible a soporte | **FUERZA-RH** | Si preserva soporte real hasta \(\Xi\), ya excluye ceros fuera de línea. No es infraestructura topológica neutral. |

## Equivalencias disfrazadas bajo nombres distintos

Las siguientes familias deben contarse una sola vez.

### Positividad y real-rootedness

\[
\begin{aligned}
\mathrm{RH}
&\Longleftrightarrow \text{positividad de Weil completa}\\
&\Longleftrightarrow \lambda_n\ge0\quad\forall n\\
&\Longleftrightarrow \Xi\text{ tiene todos sus ceros reales}\\
&\Longleftrightarrow -\Xi'/\Xi\text{ tiene la propiedad Pick apropiada}.
\end{aligned}
\]

Herglotz, Laguerre–Pólya, Hilbert–Pólya útil, índice negativo nulo y una estrella de Hodge ya identificada con Weil son coordenadas de esta familia. Ninguna suma evidencia independiente.

### Cadena Cauchy–Feshbach

Los nombres

\[
\texttt{PW-Cauchy},\ 
\texttt{HPR-DIV},\ 
\texttt{K-DIAGOFF},\ 
\texttt{EG\_LOCK},\ 
\texttt{ADJ-ARITH-LOCK}
\]

representan versiones sucesivas de una cancelación o divisibilidad aritmética firmada. Las identidades de Cauchy, Feshbach y adjugado son demostradas en secciones finitas; el lock aritmético no.

### Ancla bordeada

\[
\begin{aligned}
&\texttt{RDI-ANCHOR}
=\texttt{DIRECT-BORDERED-ANCHOR}
=\texttt{CLUSTER-RDI-ANCHOR}\\
&=\texttt{COFACTOR-CELL-ANCHOR}
=\texttt{CHARACTERISTIC-JACOBIAN-ANCHOR}
=\texttt{BASE+SUMDEF}\to0.
\end{aligned}
\]

Kato, cociclo Euler, determinante bordeado, cofactores, Jacobiano característico, respuesta von Mangoldt, conmutador y cáscara Fourier cambian la representación del mismo ancla Gamma–Euler.

### Atlas de identificación

\[
\texttt{LOCAL-COVARIANT-IDENT}
=
\texttt{STIELTJES-IDENT}
=
\texttt{SR-LOG}
=
\bigl[C_{\mathrm{core}}\to0\text{ en intervalo seguro}\bigr].
\]

Por propagación Pick–Nevanlinna, la identificación en un intervalo seguro ya tiene fuerza-RH. `XI-PARITY-CURRENT-NULL` es el mismo contenido expresado como anulación de corrientes separadoras. `TRUE-DIVISOR-IDENT` es una condición suficiente aún más fuerte, sensible a soporte y multiplicidad.

## Retiros y correcciones vinculantes

| Afirmación anterior | Estado vinculante |
|---|---|
| Multiplicatividad suprime la resonancia peligrosa | **RETIRADA** por Liouville y controles multiplicativos aleatorios. |
| Covarianzas interclase son predominantemente negativas | **RETIRADA**; el remuestreo no sostiene la cifra y los picos son constructivos. |
| \(\omega=2\) es causa singular | **RETIRADA**; clases vecinas tienen masa y respuesta comparables. |
| Un cero fuera de línea produce automáticamente una ley de crecimiento en el truncado | **RETIRADA como lema**; falta la derivación y el control operativo no la muestra. |
| Una Gram cero-sólo puede detectar horizontalidad por negatividad | **REFUTADA** por PSD tautológica. |
| H0 tiene una ley universal lineal o cuadrática | **RETIRADA**; depende del montaje, paridad y definición del operador. |
| `det Y≡1` cierra convergencia Hermite–Biehler | **RETIRADA** por non sequitur. |
| El rótulo QED de la fase 65 cierra continuidad de signatura | **SUPERADO** por correcciones posteriores que dejan `D8.5` abierto. |
| H2 cubre alturas acotadas por compactitud y diagonales positivas | **REFUTADA**; ese razonamiento no prueba PSD. |
| H6 da un testigo negativo cuantitativo para cada cúmulo | **REBAJADA** a una cota con dominación de cola pendiente y factor \(|\kappa|\) inconsistente. |
| \(\Omega_4\) usa un único whitening global | **CORREGIDA**; la referencia positiva y \(J_N^\infty\) tienen dominios distintos. |
| \(\Omega_5\) prueba positividad de borde por \(N\) | **CORREGIDA**; sólo prueba continuidad, y transmite signo únicamente bajo positividad interior. |
| \(\Omega_7\) equivale a \(|\lambda_n^{\mathrm{prime}}|<\lambda_n^{\mathrm{arch}}\) para todo \(n\) | **REFUTADA**; el blanco exacto es \(\lambda_n^{\mathrm{prime}}\ge-\lambda_n^{\mathrm{arch}}\). La cota absoluta es sólo una estrategia suficiente cuando la parte arquimediana es positiva y ya falla como equivalencia en \(n=1\). |
| La integración por partes prima es \(-\int(\psi-y)f'_{n,\varepsilon}\) | **REFUTADA**; el signo correcto es \(-n+\int(\psi-y)f'_{n,\varepsilon}=\int(\psi-y+1)f'_{n,\varepsilon}\). La fórmula anterior invierte el signo y omite el borde inferior. |
| La asintótica de envolvente puede omitir el término lineal | **REFUTADA**; este split contiene \(\frac{\gamma-1}{2}n\), que no es \(O(\sqrt n\log n)\). La cota \(c\sqrt n\log n\) para la parte prima debe empezar en \(n\ge2\). |
| La suma \(\sum_\rho(1-1/\rho)^n\) puede aislarse | **REFUTADA**; diverge aun bajo RH. |
| El término característico del adjugado desaparece | **REFUTADA**; es regla de la cadena y debe recombinarse. |
| Masa raw, borde antisimetrizado y masa core son intercambiables | **REFUTADA**; difieren por factor exterior y defecto de fase explícitos. |
| Un nivel holomorfo recupera el divisor | **REFUTADA** por representaciones firmadas y pérdida de multiplicidad lineal. |

## Precedencia y cuarentena

Un documento con `QED`, `closure` o `theorem` queda en cuarentena si una corrección posterior exhibe el hueco. No se elimina: se conserva como registro, pero no entra como premisa. Para reutilizarlo se requiere un archivo de reparación que contenga:

1. enunciado corregido con todos los cuantificadores;
2. definición única de cada objeto;
3. prueba que no cite el resultado que pretende reparar;
4. control fuera de línea;
5. lista explícita de documentos supersedidos.

## Consecuencia para el reinicio

No se abre una nueva línea por cambiar Li a Weil, Weil a Pick, Pick a Herglotz, Herglotz a índice, índice a Hodge, o Cauchy a adjugado. Una línea entra sólo si aporta una desigualdad o identidad aritmética nueva que no esté en el atlas anterior y que falle en el modelo fuera de línea antes de invocar el divisor.

En particular, los no-go obtenidos al reemplazar la oscilación por valores absolutos no clausuran una desigualdad unilateral que conserve el kernel Laguerre. Cuando \(\lambda_n^{\rm arch}\ge0\), esa desigualdad controla sólo la excursión negativa; en los índices con parte arquimediana negativa debe conservar el lower bound completo. Esta clase vuelve a ser admisible, aunque por H0 su cierre seguirá teniendo fuerza-RH.

La síntesis transversal completa está en [`fragments/CROSS_PROGRAM_SYNTHESIS.md`](fragments/CROSS_PROGRAM_SYNTHESIS.md).
