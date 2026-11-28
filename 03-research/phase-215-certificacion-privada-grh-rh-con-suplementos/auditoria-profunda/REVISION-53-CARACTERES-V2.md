# Revisión independiente de los caracteres de P53, versión corregida

Fecha: 2026-11-28. Fuente: `04-papers/53-covolume-theorem-exchange-identities-chain-determinant/main.tex`, SHA256 `ef430fe477fe53621578202a8f735b31933cba5f6299e35b6ec5c429df2d1d5a`. Se leyó el diff y se reconstruyeron los pasajes indicados; no se modificaron papers. Los dictámenes aquí se limitan a la identidad tensorial, sus tres aplicaciones, el cálculo de escalares y la propagación de esta cuestión. No constituyen por sí solos una nueva certificación de todos los lemas analíticos de P53.

## Resultado y rectificación del informe anterior

La modificación de `pcu:product` **corrige el problema de caracteres**, también en la aplicación real de `pcu:period` y `pcu:coeff`. No queda un período igual-rango ponderado por un carácter adicional. Las aplicaciones en integrabilidad (línea 4119) y `pct:vantop` (5655) también son compatibles con la nueva fórmula. Se retira, para esta versión, la propagación del antiguo error de caracteres a PLANO, no anulación y exchange.

Existe una precisión independiente: el escalar explícito `κ₀` de la línea 3631 omite, con la fórmula (U2) impresa, el factor fijo positivo `|det(s₀x_U)|_f^j`. La reconstrucción da el módulo adélico completo. Esto requiere corregir esa fórmula intermedia; **no invalida el enunciado existencial de `pcu:coeff`, ni introduce dependencia del módulo/twist, ni cambia los cocientes calibrados de exchange**. Se detallan abajo tanto la cuenta como el alcance de esta corrección.

| Obligación | Dictamen localizado |
|---|---|
| `pcu:product`, 3347–3370 | (a) identidad corregida, reconstruida directamente |
| `pcu:period`, 3387–3435 | (a) caracteres y constante archimedea exactos, bajo las propiedades de slice/vacío allí citadas |
| `pcu:coeff`, cancelación de caracteres, 3622–3648 | (a) reconstruida, incluidos los dos componentes de cada lugar descompuesto |
| Fórmula explícita de `κ₀`, 3631 | (b) falta el módulo finito salvo normalización adicional `|d₀|_f=1`, no impuesta; corrección explícita abajo |
| Enunciado de `pcu:coeff` | (a) reconstruido tras esa corrección fija; no afirmar que la fórmula intermedia es correcta tal como está |
| Aplicación de `product` en integrabilidad, 4119 | (a) caracteres compatibles; su uso en valores absolutos no deja factor de crecimiento |
| Aplicación de `product` en `pct:vantop`, 5655 | (a) el factor igual-rango es exactamente el que anula la hipótesis |
| Propagación a `P-top` y calibración `twice` | (a) inferencia reconstruida, condicionada a los demás inputs de esas proposiciones, auditados por separado |

## 1. Convenciones y producto

Por 1732, `ω_{α,β}(g,h)=α(det g)^{-1}β(det h)ω_Hom(g,h)`. La fórmula corregida es

`vartheta^{αα′,β}_{f⊠F}(g,y⊕l)=vartheta^{α′,β}_{f}(g,y) θ^{W₀,W₀}_{α,β}(g,l)`.

El carácter fuente de la derecha es `(αα′)(det g)^{-1}`; el carácter objetivo es `β(det y)β(det l)=β(det(y⊕l))`. La representación no torcida y la funcional theta se factorizan por suma ortogonal. La traslación de Heisenberg es `(x;0)` y por tanto actúa sólo sobre el primer factor. No aparece constante adicional en esta factorización.

Póngase `rank W₀=2j`, `rank U=b`, `X=H^b⊕W₀`, `γ=ν^{-1}υ^j`, `γ_X=γυ^b`. La instancia empleada es **`(α,α′,β)=(γ,υ^b,γ)`**. Produce los caracteres `(υ^b,γ)` en `(W₀,U)` y `(γ,γ)` en `(W₀,W₀)`. La asignación de índices de la versión anterior no debe reutilizarse.

## 2. La constante archimedea de period

La integral del factor igual-rango es exactamente `I₀(ν)`, constante en `g` por `pcx:const`; su dato finito es `F₁=χ_S^{-1}∘det` en `GL_{2j}(O_S)`, y vacío fuera de ese conjunto. No se reemplaza por un período con otro carácter.

Para `ζ=det B_∞`, escribamos `P=∏τ ζτ`, `Q=∏τ ζτ^{μτ}`. Las fórmulas de los vectores Φ y Λ, 3306–3337, dan

`ν_bc(ζ)=Q²/|Q|²`, `N(ζ)^j=|P|^{2j}`,

`|P^j Q|² / (ν_bc(ζ)N(ζ)^j)=conj(Q)²`.

Esta es exactamente la potencia de determinante que queda al mover `ph` a la sección real y aplicar el vacío de Fock. Las potencias de `υ` corresponden al carácter objetivo `γ`; no se ha estimado una constante que se necesitaba exacta. El escalar de period es, por tanto,

`ρ(h) I₀(ν) / (ν_bc(ζ_B) N(ζ_B)^j)`.

Los casos fuera del soporte son identidades cero por los lemas de frame/soporte; no se divide por una función de corte que pudiera anularse.

## 3. (U2) y cancelación finita, signo por signo

La reducción (U2), 3458–3470, conserva el carácter fuente y divide el objetivo por `υ^b`. Su factor de Levi es `χ_V(det q)^{-1}|det q|^{a/2}`, con

`χ_V(t)=α_V(t/bar t)υ(t)^{-a}`.

Usando `υ(t/bar t)=υ(t)^2`:

| Lado | `a` | fuente antes/después | objetivo después | `χ_V(t)` |
|---|---:|---|---|---|
| grande | `b+2j` | `γ_X=ν^{-1}υ^{b+j}` | `γ=ν^{-1}υ^j` | `ν_bc(t)^{-1}υ(t)^b` |
| pequeño | `b` | `υ^b` | `νυ^j` | `υ(t)^b` |

El cociente de Levi grande/pequeño es `ν_bc(det q)|det q|^j`. Después de product, el cociente entre los caracteres objetivos sobre `y∈U(U)` es `ν(det y)^{-2}`.

Sea `B=y^{-1}Y`, `x_f=B_f`. El slice grande tiene factor `εχ_S^{-1}(det x_f)`; el pequeño, `χ_S^{-1}(det bar x_f)`. Para cada par `w,bar w`, escribamos `t=(det x_f)_w`, `u=(det bar x_f)_w`. Son unidades donde el slice es no nulo. **No se supone `u=t^{-1}`**: `x_f` no es un elemento unitario. Los factores son respectivamente `χ(t)^{-1}` y `χ(u)^{-1}`; su cociente es

`χ(u)/χ(t)=ν_bc(det x_f)^{-1}`.

Fuera de `S∪bar S` el carácter es no ramificado y `det x_f` es unidad. De ahí la identidad global. Con `det B=ζ_B det x_f`, el producto de la fase finita y la fase de period es `ν_bc(det B)^{-1}`.

Finalmente `q=s₀x_UY`, `d₀=det(s₀x_U)`, `det B=(det y)^{-1}det Y`, y `ν_bc(det y)=ν(det y)^2`. Por tanto, exactamente:

`ν_bc(det q) · ν_bc(det B)^{-1} · ν(det y)^{-2} = ν_bc(d₀)`.

No queda dependencia en `y`, `g`, ni un carácter en el período igual-rango. `|ν_bc(d₀)|=1`.

## 4. Módulo fijo: la corrección de κ₀

La misma cuenta, conservando los módulos y los factores ya definidos en (U2), da

`κ̂₀ = ε_T ε_U^{-1} |d₀|_{A_E}^j`,

no sólo `ε_T ε_U^{-1} N((d₀)_∞)^j` como en 3631. En efecto, el factor no característico después de period es

`|det q|_{A_E}^j / N(ζ_B)^j`.

Se tiene `|det y|_{A_f}=1` por unitariedad (producto de los dos componentes en lugares descompuestos), `|det x_f|=1` por integridad y Gram unimodular, y así `|det Y_f|=1`; además `N(ζ_B)=N(det Y_∞)`. Sustituyendo `det q=d₀det Y` queda `|d₀|_{A_E}^j`.

La igualdad impresa exigiría adicionalmente `|d₀|_f=1`. No se sigue de que `x_f` sea unidad: `d₀` contiene `s₀`, no `x_f`. P49, 3316–3325, fija `s₀O_hat=αO_hat`, donde `α=1/P′(ζ_q1)` en los lugares indicados de la diferente, y no supone que sea unidad. Para un espacio estándar con frame identidad, `d₀=s₀^b`; el factor omitido es entonces `|s₀|_f^{bj}`. Los factores `ε_T,ε_U` son los que ya figuran en (U2), por lo que no pueden absorberse de nuevo dentro de la igualdad que los mantiene con esa definición.

**Uniformidad:** los espacios, sus frames y sus retículos se fijan en 656–664; `s₀` se fija por los datos de Weil de P49. Ninguno depende de `S`, de su módulo ni de `ν`. Un cambio de frame integral tiene módulo finito uno; cambiar `s₀` por una unidad tampoco modifica este factor. En consecuencia, sustituir `κ₀` por `κ̂₀` conserva la uniformidad requerida para todos los módulos admisibles, no sólo para un módulo fijo.

Con `R=∫_{H\G}ρ′`, la prueba da `Cν=R κ̂₀ ε ν_bc(d₀)I₀(ν)` cuando `R<∞`, y `K=R|κ̂₀|`. Si `R=∞`, (U3) fuerza `I₀(ν)·coef_pequeño=0` y ambos coeficientes son cero; se puede tomar `Cν=κ̂₀ ε ν_bc(d₀)I₀(ν)`, `K=|κ̂₀|`. No se necesita dividir por `I₀` ni asumir aquí que es no nulo.

## 5. Otras dos aplicaciones y no anulación

En 4119 la expansión coherente se factoriza con la misma instancia `(γ,υ^b,γ)`. El segundo factor tiene caracteres `(γ,γ)` y el dato `F₁` soportado en matrices invertibles. Los caracteres son unitarios; la estimación absoluta de decaimiento no adquiere ninguna potencia de altura adicional. Esto verifica el uso de product; las estimaciones analíticas de momentos y convergencia son obligaciones separadas.

En `pct:vantop`, 5634–5664, la integral interior sobre `l∈[U(W₀)]` contiene exactamente

`θ^{W₀,W₀}_{γ,γ}(g,l;ρ(y₂)e⊗F₁)`.

Su integral es el lift igual-rango que se supone cero para todos los vectores de momentos finitos. Los coherentes satisfacen esa condición. No se requiere un nuevo teorema de no anulación de un período torcido. El paso Fubini usa la cota de decaimiento con peso polinómico en `y₂` y los momentos de φ, tal como está expuesto.

Así la contradicción de `pcx:P-nonvan`, 5666–5678, vuelve a tener su premisa correcta: Van desciende hasta `(J,0)` y allí el dato es `χ^{-1}(det 1)=1`, con integral no nula. Esta revisión valida el paso de caracteres en esa cadena; los lemas de descenso y de coeficientes negativos siguen siendo los lemas propios de la prueba, no consecuencias de una cancelación formal.

## 6. Consecuencias para las constantes finales

En `pcx:P-top`, 3753–3773, se usa exclusivamente `|Cν|=K|I₀(ν)|`; con el K corregido,

`|Cν|²=K² L_*(m,ν,j) r_{W₀}(ν;z)`.

La constante RC se toma `K^{-2}`. No hay constante numérica prescrita que sea contradicha por el factor finito fijo.

En `pcx:twice`, 2191–2230, las dos aplicaciones dan `B|c₁|²=L_*(k)r`, `C|c₂|²=L_*(-k)r`. Fubini da exactamente `ξ=c₁c₂`, y `L_*(k)L_*(-k)=1`; por tanto `r²=BC|ξ|²`, independiente de ν. Una modificación fija de los coeficientes auxiliares se refleja en B y C; no queda un factor dependiente de ν sin cancelar. `P-nonvan` y la no negatividad fijan el valor positivo común. Ésta es la calibración que se emplea para exchange.

Conclusión localizada: la corrección actual resuelve la objeción sustancial de caracteres de la versión anterior, también en las aplicaciones necesarias para no anulación. Queda una fórmula intermedia de normalización positiva que debe escribirse con el módulo adélico completo; reparada ésta, no constituye una obstrucción a exchange ni a los resultados que lo importan. Este archivo no sustituye las auditorías separadas de los demás inputs de P53.
