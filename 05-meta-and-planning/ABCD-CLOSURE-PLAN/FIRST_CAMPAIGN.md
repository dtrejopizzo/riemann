# Primera campaña: viabilidad del portador y del contacto

Fecha: 2026-09-05. Estado: **ejecución iniciada tras aprobación del usuario**.

Avances y límites: [registro de la primera campaña](../../03-research/phase-123-weil-strength-abc/P123_024_FIRST_CAMPAIGN_LEDGER.md). Las secciones siguientes conservan los criterios originales; no todos están cerrados.

Objetivo: decidir si la candidata de fase 123 se puede reparar en una categoría que aloje el contacto aritmético. No intentar cerrar RR ni RH en este bloque.

## 1. Fijar el contrato local

Trabajar primero con `S={infinito,2,3}` y después con inclusiones de cartas. Explicitar si Gamma_S incluye signos o sólo unidades positivas y cómo se compara con las fuentes que usan todas las unidades.

Mantener distintos el ideal rápido K_S, su unitización, su álgebra de multiplicadores, la representación C* de control y el núcleo de tests suaves. Escribir dónde viven U_gamma, la diagonal y cada bimódulo.

Entregable propuesto: `P123_019_REPAIRED_LOCAL_BIMODULE_CONTRACT.md`.

Aceptación: cada fórmula tiene dominio/codominio; no usa `1 in K_S` ni `U_gamma in K_S+C1` para gamma distinto de 1.

## 2. Demostrar el cambio de levantamiento en la categoría elegida

Para cada automorfismo beta_a, construir el bimódulo esencial correspondiente. Probar que el multiplicador U_gamma induce un entrelazador válido entre los levantamientos a y gamma*a.

Demostrar composición y coherencia de tres cambios de levantamiento. En el modelo no unital, probar la identificación del tensor balanceado mediante la herramienta realmente disponible —unidad aproximada, esencialidad o teorema de correspondencias— y verificar sus hipótesis en el núcleo rápido.

Si sólo se obtiene el teorema C*, etiquetarlo así. La versión nuclear/rápida permanece abierta hasta demostrar la comparación.

**Primera oportunidad de éxito:** un teorema local de independencia de levantamiento que repare una fórmula actualmente mal tipada.

## 3. Construir una transición real de cartas

Usar como regresión exacta el par de representantes `(1,1)` y `(2,2)` en `S={infinito,2}`. La transición corregida debe reconocer su equivalencia al incorporar el lugar 3, sin enviar ingenuamente ambos a extensiones por uno.

Proponer un span/inducción compatible con la inclusión de coeficientes o definir el objeto global y derivar sus restricciones. Escribir la acción sobre objetos y flechas y comprobar `S -> S' -> S''`.

Entregable propuesto: `P123_020_TRUE_CHART_TRANSITIONS.md`.

Aceptación: diagrama de coherencia demostrado, conexión explícita con el haz de coeficientes y alcance topológico declarado. Una elección de representante canónico, si se usa, necesita su propia coherencia multiplicativa; no equivale a un mapa inducido por extensión por uno.

## 4. Probar que el núcleo de tests es estable

La acción sobre coeficientes C_0 es continua; determinar su subespacio de vectores suaves y los niveles localmente constantes adecuados. Comprobar el producto de dos secciones y dagger dentro de ese subespacio.

Probar las estimaciones locales que después sostendrán la continuidad LF. No declarar la completación total en esta etapa por analogía con las funciones escalares.

## 5. Controlar la categoría clásica y la efectividad

Rehacer P123.011 en un caso de dimensión cero y una curva sencilla:

- permutación de tres puntos: grafo efectivo frente a positividad matricial;
- diagonal y rulings;
- grafo de un endomorfismo finito y su transpuesto;
- Frobenius: convención y diferencia entre transposición e inverso;
- intersección de ciclos frente al carácter del kernel perfecto, con cualquier corrección RR necesaria.

Entregable propuesto: `P123_021_CLASSICAL_COMPARISON_AND_CONE_TEST.md`.

Aceptación: relación precisa entre las dos teorías, incluso si la conclusión es que debe ampliarse la categoría. No afirmar equivalencia de conos porque ambos admitan sumas.

## 6. Test decisivo B: 2, 4, 3 y 6

Construir los objetos, antes de asignarles un grado. Calcular sus composiciones y contactos derivados. Valores esperados sólo como test externo:

| n | Phi_n(1) | Contacto aritmético esperado |
|---|---:|---|
| 2 | 2 | `[Z --2--> Z]` |
| 4 | 2 | `[Z --2--> Z]` |
| 3 | 3 | `[Z --3--> Z]` |
| 6 | 1 | complejo acíclico |

Exigir `Gamma_2 star Gamma_2 ~= Gamma_4` y `Gamma_2 star Gamma_3 ~= Gamma_6`. El contacto no tiene por qué ser multiplicativo: justamente debe deducirse cómo un producto no trivial puede tener contacto acíclico.

Comparar la construcción con el contacto lineal `1-u^(-1)` y con la realización Witt de Deninger/Haran. Identificar el morfismo o exceso que produce Phi_n(1); si no aparece, el modelo de grafos simples todavía no pasa el test.

Entregable propuesto: `P123_022_MINIMAL_ARITHMETIC_CONTACT_TEST.md`.

Aceptación: complejos y mapas derivados, no etiquetas numéricas ni una categoría producto que transporte un complejo añadido.

## 7. Mantener una pregunta concreta de D durante la campaña

Leer P122.028 y P122.029 como cálculos existentes. Formular una relación global de borde candidata que pudiera demostrar flujo cero o transmisión en un espacio fuente definido antes de imponer el signo.

Anotar por separado:

1. la identidad fuente que se puede demostrar;
2. la comparación con los canales físicos;
3. la estimación o condición aún pendiente;
4. un contramodelo que decida si lo demostrado alcanza.

No es un requisito cerrar D para aceptar el bloque local. Sí es obligatorio comprobar que A conserva los datos que esa futura ley necesitaría: lugares, orientaciones, Gamma y Tate antes de scalarizar.

## 8. Decisión al terminar

| Resultado | Continuación |
|---|---|
| Bimódulos y transiciones pasan; contacto derivado pasa | Completar A: traza, topología numérica, efectividad y RR; generalizar B. |
| Sólo pasa el modelo C* | Mantenerlo como control analítico; construir el puente integral/suave antes de promoverlo. |
| Contacto lineal no produce el ciclotómico | Examinar ampliación a correspondencias finitas/Witt; no seguir completando los grafos solos. |
| Transiciones semilocales fallan para la candidata | Estudiar la variante global con un teorema explícito de recuperación de cartas. |
| Sólo aparecen identidades del defecto de D | Retenerlas como diagnóstico; el teorema de signo sigue abierto. |

Ningún resultado se acepta por el tamaño del archivo ni por un PASS matricial. Cada salida debe cambiar una obligación concreta y actualizar el plan maestro sin borrar el historial de los fallos.
