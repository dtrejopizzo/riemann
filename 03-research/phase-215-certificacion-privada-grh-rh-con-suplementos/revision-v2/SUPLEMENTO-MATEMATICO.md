# Suplementos a las fuentes corregidas

Esta nota propone formulaciones exactas verificables para completar la versión identificada en fuentes-v2.json. No se editaron los manuscritos. Su inclusión en un dictamen debe ser explícita: no se atribuyen al texto actual pruebas que todavía no contiene.

## Nivel auxiliar de pri:forms55

Sustituir J_O^(1)=J_O∩J_1 por

`J_O^(1) = {k∈J_O : k_(w_j) ≡ 1 mod w_j para todo j}`.

Los lugares w_j son disjuntos de los lugares elegidos. Entonces J_1 es normal en J_O^(1), el cociente es H=J_O/J_0 y las formas de nivel J_O^(1) son exactamente las invariantes H en el espacio de nivel J_1. Con esta definición, el promedio integral Ψ=Σ_(d∈D)R(d)^−1Ψ_1R(d) preserva ese nivel y conmuta con e_c. La identidad Σ_(k∈Γ′)k^−1Ψk=#D sigue válida porque D y Γ tienen soportes disjuntos. No se divide por |D|. Como #D|N_ch, se conservan todas las pérdidas. Prueba y aplicaciones: [revisión55/56](../auditoria-profunda/REVISION-55-56-V2.md).

## Coeficiente fijo de pcu:coeff53

Con la notación de U2, d_0=det(s_0x_U), B=y^−1Y, q=s_0x_UY. La razón de caracteres Levi es ν_bc(det q), la razón de datos finitos es ν_bc(det x_f)^−1, el período aporta ν_bc(ζ_B)^−1 y la diferencia de caracteres de destino es ν(det y)^−2. Como det B=ζ_B det x_f y ν_bc(det y)=ν(det y)^2, su producto es exactamente ν_bc(d_0).

El cociente positivo de módulos se debe conservar en forma adélica:

`|det q|_(A_E)^j / N(ζ_B)^j = |d_0|_(A_E)^j`,

pues det x_f es unidad y det y tiene módulo adélico1. Por tanto la expresión completa del factor fijo es

`κ_0 = (ε_T/ε_U) |d_0|_(A_E)^j`.

La fórmula impresa conserva sólo la parte infinita. Los marcos y s_0 se fijan antes de elegir ν y su módulo, así que el factor finito adicional es fijo, positivo y no nulo. Puede incorporarse a K, cuya afirmación en pcu:coeff es existencial; no se modifica la dependencia en ν, el período I_0, la no anulación ni las razones normalizadas. Esta precisión es distinta del supuesto carácter residual de V1: aquel carácter residual no subsiste en la aplicación corregida.

## Fase49: lema suficiente

En lugar de la clasificación fuerte de δ_g atribuida a W4, usar el lema y prueba de [REVISION-FASE49-V2](../auditoria-profunda/REVISION-FASE49-V2.md): todos sus conjugados tienen módulo I_g^−1/2; si g es integral sobre l, δ_g es una unidad l-ádica y las traslaciones se eligen integrales sobre l. La demostración aritmética mediante modelos finitos de Schrödinger debe acompañar el enunciado; unitariedad compleja por sí sola no lo demuestra. La normalización exacta quedó reconstruida en [REVISION-SPLITTING-V2](REVISION-SPLITTING-V2.md), §§6–9: el índice de Weil coincide con la constante gaussiana de la norma, con ψ_K=2ψ_k; doubling, cambio de carácter y negación conservan esta normalización. La imposibilidad de consultar el original de Kudla no queda como obligación matemática: se aporta una reconstrucción explícita con Murase y las convenciones reproducidas por Chan.

## Sincronización documental

En el apéndice56, actualizar el dominio de BL a e_cF(O) y sustituir la explicación antigua de G4 mediante una norma inexistente por la del generador tame compatible de55. En58, replicar la definición corregida de nivel anterior y cualquier precisión de κ_0. Las comparaciones finitas sin prueba de46 y los enlaces a certificados no son premisas de la deducción automórfica de GRH/RH; se conservan fuera de la certificación de esa cadena hasta tratarlos por separado.

## Carácter νflat de54 y su propagación

En54:2695 y7584, sustituir la definición por

`νflat = ν″_ϑ / χ′ = μflat υ^(−jΔ+j+(t+k−1)/2)`.

Quitar el factor υ^m y el sumando final +m únicamente en esas definiciones. Mantener νflat υ^m en los kernels, F_i y las aplicaciones. Replicar en58:51272 y56151.

La prueba de suficiencia consta en [tres intercambios](../auditoria-profunda/REVISION-54-TRES-EXCHANGES-V2.md): α=χ′νflat υ^m=ν″υ^m, β=ν″, αβ⁻¹=υ^m, y α⁻¹υ^(3m+z*)=(ν*ϑ)⁻¹. La identidad de exponentes es j+(t+k−1)/2−2m−z*=j+(t−11m−1)/2. El peso fuente vuelve a m−μ1. Por [generación general](../auditoria-profunda/REVISION-54-SPAN-GENERAL-V2.md), se recupera H5 y F⁰(1)=I_(u3)φ°(g1)||v||²≠0. No cambia H_j, z*, los niveles, ni las cotas de los primeros factores. En el texto sin corregir, el carácter central adicional fuerza F⁰(1)=0; por eso la corrección es indispensable para la prueba escrita.

## Generación y funcionales de54

Estas precisiones también forman parte del suplemento; no se atribuyen silenciosamente al manuscrito:

1. En ppe:harm, usar la generación del componente polinomial por U(g_W,C) y U(V) a partir de los p_ξ. El miembro U(V) es compacto y la irreducibilidad conjunta pertinente está cotejada con Howe(3.9a). La demostración está en [períodos generales, §3](../auditoria-profunda/REVISION-54-PERIODOS-GENERALES-V2.md).
2. En ppe:bottom, la acción Ψ(T)↦Ψ(TA) corresponde al operador por A, no A⁻¹; trasladar también el argumento. La anulación para todos los argumentos se conserva. En la suma ponderada, respetar la conjugado-linealidad respecto de Ξ; misma ficha §4.
3. En pte:explicit, extender desde polinomios en la topología de momentos/Schwartz, con pcn:smooth de53; no usar únicamente densidad Hilbert. Las funcionales integradas son continuas en esa topología y el promedio compacto conserva las seminormas requeridas.
4. En pte:carriernz, sustituir la afirmación sobre un núcleo cerrado Hilbert por Parseval: la integral de |θ(ρ(w)Λ)|² es ||Λ||²>0 para la rebanada Schwartz no nula. Por tanto algún traslado tiene valor no nulo.
5. En psv:c y psv:F, aplicar pss:coefs con E=Schwartz y la órbita C∞ demostrada en pss:carrier; no identificar sin más los vectores suaves de cualquier subgrupo con Schwartz.

Las pruebas de los puntos3–5 están en las fichas de [intercambios](../auditoria-profunda/REVISION-54-TRES-EXCHANGES-V2.md) y [generación general, §7](../auditoria-profunda/REVISION-54-SPAN-GENERAL-V2.md). Ninguno añade una pérdida a las constantes. El suplemento incluye estas pruebas por referencia, no sólo la instrucción de corregir palabras.
