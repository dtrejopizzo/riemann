# AUDIT_006 — FE de Π y defecto de autodualidad

2026-10-18. Revisión inicial y final de CONSTRUCTOR_006. No se construyeron candidatos paralelos. Objetivo D íntegro activo.

**Veredicto: PROVED las identidades FE y el defecto de autodualidad borrado, con precisión de alcance sobre no-Hankel indicada al final. Enlace Q_T OPEN.**

## 1. Corpus y alcance de la ronda

Consultados índice (Tate/Poisson, SPEC005, R11_2_ORIGIN, INV_C/V, auditorías de transporte Mellin) y las construcciones209. Se conserva la razón nueva: calcular la transformación EXACTA del kernel Π ya construido y preguntar por su enlace al nodo, sin cambiarlo por un Gram favorable. La masa m=c−τ autodual es clásica; no presentarla como segundo puente nuevo.

No se reabre el envío de coeficientes por inversión de Möbius como ruta de signo: demostrar PSD de un empuje finito de una forma PSD es una norma genérica. Para habilitar un enlace nuevo hay que explicar la diferencia frente a P1 y a los intentos indexados, además de demostrar la igualdad con términos de Q_T.

## 2. Fórmula FE de W_d

Sea W_d(y)=τ(d²y)−τ(y)/d. Entonces

    Π_α(d,e)=∫_0^∞ y^(α−1)W_d(y)W_e(y)/τ(y)dy.

Poisson da exactamente

    W_d(1/y)=√y/d [θ(y/d²)−θ(y)]−(1−1/d).

**PROVED:** τ(d²/y)=√y θ(y/d²)/d−1 y τ(1/y)/d=√y θ(y)/d−1/d. Restar. El término constante es negativo con el signo indicado. No se pierde al excluir el origen; es precisamente la corrección de origen.

La FE transforma escalas enteras d² en escalas fraccionarias d^(−2). Para convertir esta identidad en una transformación cerrada de Π hace falta conservar esas escalas, sus denominadores y todos los términos cruzados; no sólo la parte homogénea. Ningún signo de Π resulta de ignorar los términos constantes.

## 3. Masa faltante clásica y test de borrado

Para m(y)=c(y)−τ(y), la comparación integral de la gaussiana da m>0 y Poisson implica

    m(1/y)=√y m(y).

Es un objeto positivo autodual preciso, pero anterior a esta ronda. Su Mellin es −Z_α en 0<α<1/2. Esto prueba la normalización del auxiliar; no produce por sí solo el arquimediano de Q_T.

Para P>1 squarefree, τ_P=Σ_{a|P}μ(a)τ(a²y), δ_P=Π_{p|P}(1−1/p), m_P=δ_P c−τ_P. Como Σμ(a)=0,

    τ_P(1/y)=√y Σ_{a|P}μ(a)/a ·θ(y/a²).

Éste es el defecto específico de la FE: aparecen simultáneamente coeficientes 1/a y escalas fraccionarias. No se puede reemplazar esa suma dual por τ_P(y) ni por θ(y) sin una identidad adicional.

En particular,

    m_P(y)=O_P(c(y)exp(−c_P/y)) cuando y↓0,
    m_P(y)~δ_P c(y) cuando y→∞,

porque la constante de τ_P se cancela en cero y τ_P decae exponencialmente en infinito. Así

    m_P(1/y)−√y m_P(y)→−δ_P≠0 cuando y→∞.

La autodualidad de m se rompe de modo exacto bajo este borrado. Esto es compatible con que el kernel −R^P conserve PSD después de integrar: positividad y autodualidad son propiedades distintas y no debe confundirse una con la otra.

## 4. Qué se puede y no se puede concluir

El defecto anterior localiza una identidad que falla para un falsificador. Aún no prueba que esa identidad aporte el signo de Q_T; separación no es dominación del déficit gamma. El rango uno de (5)/(7) tampoco se identifica con el polar cosh por analogía.

La siguiente revisión debe exigir un mapa explícito y dominio, grado cuadrático, intercambio/límites justificados, y correspondencia término por término. Si sólo se obtiene FE para el auxiliar, registrarlo como identidad estructural. Si no hay enlace todavía, no cerrar el objetivo ni convertir una equivalencia interna en razón para abandonar.

Revisión final pendiente de CONSTRUCTOR_006.

## 5. Revisión final de CONSTRUCTOR_006

Aprobados §§1–4 en sus identidades y signos:

- 0<m<1, m(y)=y^(−1/2)m(1/y), τ(1/y)=√y(1−m(y)): correctos. El primer límite viene de comparación integral estricta y el segundo de Poisson.
- W_d=m/d−m(d²y): cancelación exacta del perfil c. La inversión produce W_d(1/u)=√u[d^(−1)](m(u)−m(u/d²)). Al dividir por τ(1/u), el jacobiano deja u^((1/2−α)−1)/(de). α=1/4 es punto fijo del parámetro de ESTA identidad.
- La fórmula directa con τ lleva −(1−1/d); coincide con la fórmula θ porque las constantes dentro de la diferencia se cancelan. No hay omisión del origen.
- Para P>1, m_P^∨=−Σ_{a|P}μ(a)τ(y/a²)/a. El término δ_P se cancela con Σμ(a)/a=δ_P. Las fórmulas Δ_P y sus límites δ_P en cero y −δ_Pc en infinito son correctas. La representación dual de Π_P conserva δ_P−m_P^∨>0 y es un Gram; no requiere signo de m_P ni de m_P^∨.
- La discrepancia de perfiles es real y no idénticamente nula. La igualdad de un perfil forward/backward se pierde; esto no prueba que alguna parte del defecto tenga el signo requerido para Q_T.

**Precisión de alcance §3:** la fórmula de Π mantiene dos escalas por separado. Eso no demuestra por sí solo que el kernel INTEGRADO Π_α sea diferente de toda función w(de) para un α fijo; una integral puede colapsar dependencias. El Teorema 3 de CONSTRUCTOR004 es sobre A_α, no sobre Π_α aislado. Se comunicó al coordinador para ajustar esa frase. No afecta ninguna identidad FE.

El rechazo del empuje Möbius finito se entiende como filtro de la clase concreta de símbolos convolutivos de P1, no como un nuevo NO-GO para todo mapa lineal hacia el auxiliar. Tal mapa podría tener contenido si se construye su enlace específico; no basta su existencia abstracta ni su PSD.

Los §§5–6 conservan correctamente como pendientes mapa de dominio continuo, grados, lcm/cocientes, gamma, polo, colas y todos los modos. La autodualidad de m es un objeto clásico explícito; su acción sobre Π está calculada, pero no constituye por sí sola el segundo puente buscado. **FE y defecto probados; objetivo D activo y sin cerrar.**
