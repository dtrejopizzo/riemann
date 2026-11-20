# AUDIT_007 — Módulo de contracciones del kernel canónico

2026-10-18. Revisor independiente. Leído CONSTRUCTOR_007 completo, incluido §8.
**Veredicto: PROVED en el dominio auxiliar declarado. No enlace con Q_T ni cierre D.**

## 1. Corpus y razón nueva

Consulta dirigida de índice/grid/crucigrama por contracciones, dilataciones, Frobenius, isometría y Hecke; lectura de P44 (grado/half-density y Gram Frobenius), INV_B_002 y entradas L2_016, INV_V_001/002, P1_BBSTAR y CELL_001. Ninguna de esas rutas se reabre como prueba de signo.

La razón nueva de CONSTRUCTOR007 es suficiente para examinar el auxiliar: norma −R fijada antes, acción exacta sobre ella y defecto gaussiano calculado sin cota de ángulo. No es el transporte de la forma de ventana por n↦n^k de L2_016 ni una nueva lectura del grado aritmético de P44. Tampoco la existencia de este semigrupo entrega el arquimediano que faltaba en las construcciones anteriores. La diferencia reside en el objeto concreto y su defecto Π, no en renombrar dilataciones como Frobenius.

## 2. Dominio Haarcentrado y completación

𝒜₀ permite X₁ para imponer E₁A=0. La fórmula de −R se reduce entonces exactamente a C_αE_s|A|²+Π_α(A). Un observable constante en 𝒜₀ es cero, por lo que la norma es definida positiva.

La realización en el producto de Hilbert y el cierre de la imagen son correctos. No se necesita demostrar de antemano que el mapa A↦E_yA sea clausurable como operador desde el primer factor por separado. Las leyes P_s compatibles sobre finitísimos primos admiten la realización usual por producto de probabilidades; no son una ley normalizada sobre enteros bajo s<1.

No se supone continuidad global de E₁ en la norma K sobre un espacio mayor: se completa únicamente el subespacio algebraico ya centrado. Esa elección evita una condición de dominio no demostrada.

## 3. Memoria geométrica y cambio de escala

D_nA=1_{n|N}A(N/n) implica D_nX_d=X_nd y composición D_mD_n=D_mn. Bajo P_t, condicionar las valuaciones en v_p≥v_p(n) deja las diferencias con la misma ley geométrica independiente, incluso cuando n comparte primos con los índices de A. Por ello las dos identidades del Lema1 son correctas y D_n preserva el centro Haar.

En la gaussiana, la sustitución entera N=nM da exactamente E_yD_nA=q_n(y)E_{n²y}A. No interviene una aproximación de medias ni un argumento de fase estacionaria.

Con u=n²y y s=2α,

    Π(V_nA)=∫u^(α−1)τ(u)q_n(u/n²)|E_uA|²du.

Los factores n^s y n^(−2α) cancelan correctamente. El componente aritmético es isométrico y la diferencia de normas es exactamente (1). Como q_n<1/n para n>1, la cota (2) tiene signo y constante correctos.

Los V_n son contracciones en el núcleo algebraico, por lo que se extienden a su completación. La igualdad de semigrupo pasa por continuidad. No se deduce automáticamente una acción unitaria invertible ni una relación de adjuntos.

## 4. Adjunto gaussiano

Para G_nf(y)=n^(s/2)q_n(y)f(n²y), el cambio u=n²y en el producto interno deja n^(−s/2). Así

    G_n*g(u)=n^(−s/2)g(u/n²),
    G_n*G_nf(u)=q_n(u/n²)f(u).

Ambas fórmulas son exactas en el L² con medida y^(α−1)τ(y)dy. El operador es acotado; la cota de norma ≤1/√n proviene del supremo del multiplicador q_n. La composición telescópica de cocientes de τ da G_mG_n=G_mn.

La cautela del memo es indispensable y correcta: el cierre de la imagen en el producto de Hilbert está demostrado invariante por las acciones, no reductor. No se puede restringir sin más el adjunto ambiental para obtener V_n* en 𝓗_α.

## 5. Borrado y monoides

Para p eliminado, D_pA=0 en la ley condicionada. Si A es NO NULO como observable de esa ley, p^(−s)E_s^P|A|²>0 y falla la identidad isométrica de ese mismo p. Esto no rompe contractividad: el operador cero también es una contracción. El enunciado sólo identifica una identidad de grado que desaparece.

La precisión de §8 es correcta: memoria geométrica y escalamiento multiplicativo son propiedades de monoides con norma, y q_n<1/n se extiende a escalas reales n>1 por concavidad. La prueba del módulo por sí sola no discrimina todos los sistemas de Beurling ni produce especificidad completa. La interpretación como divisibilidad efectiva de enteros, la identidad con R y la FE de perfil único son información adicional cuya acción sobre Q_T todavía debe demostrarse.

No usar el test de primo borrado como prueba de una batería completa de falsificadores ni convertir la genericidad parcial en un NO-GO absoluto para todo enlace.

## 6. Veredicto de alcance

La representación multiplicativa contractiva, sus dos factores, adjunto gaussiano y defecto positivo quedan PROVED. α=1/4 da normalización V_n=n^(1/4)D_n y ley de normas n^(−1/2) en el primer factor antes de normalizar; eso no identifica aún el coeficiente del peine de Q_T.

La inversión FE de Π no está demostrada como involución unitaria cerrada en 𝓗_α, ni como conjugación a V_n*. No hay traza o forma de caracteres sobre todos los tests del nodo construida aquí. Ninguna se obtiene sólo de que V_n sea contracción o de que una fórmula parezca Frobenius.

**Resultado auxiliar aprobado. Objetivo íntegro D activo.** Siguiente obligación concreta: definir la realización/inversión y el enlace de forma o traza con dominio y convergencia, en vez de sustituirlo por una existencia abstracta o una norma genérica.
