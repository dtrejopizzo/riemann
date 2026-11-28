# P54: tres exchanges, primeros factores y corrección de ν^flat

Fecha: 2026-11-28. Revisión de `main.tex`: 2111–3448, 3496–3550, 3780–3940, 7137–7608. Auditoría independiente de los caracteres, escalares, congruencias, integralidad y tamaños. No se modificó el manuscrito.

## 1. Fallo literal localizado y reparación concreta

**(b) para la igualdad de caracteres de `pte:third`, línea 2730, con las definiciones impresas.** La línea 2695 define

`ν^flat = ν″_ϑ υ^m / χ′`.

Por ello `χ′ν^flat υ^m=ν″_ϑ υ^{2m}`, mientras que 2730 lo identifica con `ν″_ϑ υ^m`. Como υ tiene peso infinito uno y m>0, los caracteres difieren realmente. La misma definición reaparece en `pfq:tame(T4)`, 7584, incluido el exponente final `+m`; y la igualdad incorrecta reaparece en `ptf:leftside`, 3366. No es una fase constante: es una diferencia de peso de un carácter de una variable integrada.

La reparación que preserva las fórmulas utilizadas es definir, en 2695 y 7584,

`ν^flat := ν″_ϑ / χ′ = μ^flat υ^{-jΔ+j+(t+k−1)/2}`,

es decir, quitar el factor υ^m y el sumando final +m **en esas dos definiciones**, manteniendo el carácter `ν^flat υ^m` en F_i y en las fórmulas operativas. ν^flat sigue independiente del twist y no ramificado en todos los lugares finitos. Su peso pasa a ser `−#ι(τ)`, como requieren los cálculos posteriores.

Con esta definición corregida:

- `α=χ′ν^flat υ^m=ν″_ϑ υ^m`, con peso `m−#ι(τ)`;
- `β=ν″_ϑ`, y `αβ^{-1}=υ^m`, exactamente el carácter objetivo en el lado invertido;
- `n=3m+N″`, `b=3m`, `a=N″`, `a−b=7m+k=2z_*`;
- `α^{-1}υ^{3m+z_*}=(ν_*ϑ)^{-1}`, porque `j+(t+k−1)/2−2m−z_*=j+(t−11m−1)/2=n′`;
- el carácter fuente del kernel F_i es `ν^flat υ^m`, de peso `m−#ι(τ)`, no `2m−#ι(τ)`.

No cambia z_*, el número de pares críticos ni H_j. Esta corrección debe propagarse a la interpretación de F_i en psp/psv; se notificó expresamente a la rama encargada de dicha prueba. La verificación siguiente es para esta reconstrucción corregida, no una certificación literal de la versión actual.

## 2. Explicit exchange: constantes independientes y proyección archimedea

La aplicación de P53 tiene `μτ=#ι(τ)+n/2−l≥1`, `γ=α`, `a=b+2d`, `q_W=l=q_{I_a}+q_{V′}` y `2l+2≤n`. El vector de entrada Q₀ es fijo antes del módulo/character. P53 da x₀ y C independientes de ellos; `|c₀|²=C L_*` y c₀≠0.

El promedio circular de `pte:explicit` elimina todas las variables salvo el bloque cuadrado x^flat. El promedio compacto objetivo selecciona su potencia de determinante. La extensión de polinomios a x₀ debe hacerse en las normas de momentos/Schwartz donde las funcionales theta integradas son continuas; densidad meramente Hilbert no basta. Con la suavización y densidad de P53 `pcn:smooth`, esta precisión permite el paso sin cambiar κ ni introducir una dependencia en el módulo.

Recalculé `ptf:fock` y `ptf:SDlaw`: sobre las variables de signo producto positivo la sustitución es `h^t X g^{-t}`; sobre las negativas, `h^{-1}Xg`. El carácter del vacío es la inversa del determinante del bloque negativo. Los factores de det(u) de los menores cancelan exactamente el carácter objetivo `l−#ι`; en el círculo, la potencia `z^{aNι}` cancela la prefijada, y la homogeneidad MP produce `z^{-2pNι}` frente a `z^{(2p+a)Nι}`. No queda fase dependiente de z.

La polarización usa el módulo irreducible de productos de menores máximos (Cartan/Grassmanniana). La identidad de stackeval transporta los mismos coeficientes a SD, incluso si la matriz inferior pierde rango, pues entonces su determinante complementario d puede ser cero. El caso p=0 es el espacio constante y no exige una Grassmanniana no trivial.

La normalización final es `c=κ/c₀`; por tanto `|c|² L_*=|κ|²/C`. No se divide por κ. Es lícito que este escalar sea inicialmente cero; su no nulidad se obtiene posteriormente con generación global. El paso de integral a suma de clases usa masas uno y los estabilizadores, sin índice omitido.

## 3. Negación y primeros dos exchanges

`ptf:conj` se reconstruye usando el intertwiner antilineal que conserva los vacíos y la normalización de media cuadrática de theta. Su constante ε tiene módulo uno y no depende del carácter ni del módulo. La corrección de splitting es `Aω_W(g)A^{-1}=υ(det g)ω_{W^-}(g)`. Aplicada a Hom(S,T), `det(g,h)=det(h)^{rank S}det(g)^{-rank T}`, da los desplazamientos de caracteres `(α^{-1}υ^{rank T},β^{-1}υ^{rank S})`. El contenido clásico necesario sobre cambio del carácter de splitting se coteja en paralelo con P3; no se infiere este carácter únicamente de la unicidad de Heisenberg.

En el primer exchange, d=m/2 y α=c^{-1}; su conjugado tiene ambos caracteres `cυ^m`. El segundo usa `(W,V′,I_a)=(I_m⊕S,I_m^-,I_{3m})`, d=m, α=cυ^m. En el producto sobre el objetivo, los caracteres fuente se distribuyen `(cυ^m)·1` y el objetivo común permanece cυ^m. En el producto sobre la fuente, el objetivo se distribuye `c·υ^m` y la fuente común permanece 1. El factor exterior c(det x) aparece en ambos lados y se cancela. Así

`|γ|² L_*(c^{-1}υ^m,m)L_*(cυ^{m/2},m/2)=C₁C₂`.

La no nulidad del carrier no usa esos c ni una identidad circular. Su coeficiente de Fourier de Gram identidad reduce, por soporte finito, a una sola clase compacta; el slice archimedeo es no nulo en algún punto invertible. Las traslaciones de Heisenberg separan un vector no nulo por la identidad de Parseval de theta. Esta última es la justificación precisa para la conclusión; no basta afirmar que el kernel de una funcional theta es cerrado en la norma Hilbert. La revisión concurrente de carrier verificó esta sustitución.

## 4. Tercer exchange y primeras formas

Con ν^flat corregido, `pte:one` se aplica con `(a₁,a₂,β₀)=(χ′,ν^flat υ^m,υ^m)`. La suma de traslaciones elimina el promedio finito con el factor exacto `N=#GL_{3m}(O_E/π_M²)`, porque el carrier es K_S-invariante y a₂ no tiene tame part. De ahí `c′_ϑ=c₃γ/N` y `|c′_ϑ|²H_j(ϑ)=C₃C₁C₂/N²`. Todos los módulos de π_M² se usan con sus primos una sola vez en L_*; no se duplica el factor de conductor.

`pte:matched` es una identidad de complementos de Schur sobre el anillo finito, y los soportes no invertibles anulan ambos lados. `pte:column` recupera simultáneamente σ≡ι₀ modπ_M y Λ(σ−ι₀)≡0 modπ_M². `pte:rowstab` divide el soporte invertible en cosets AH. El recuento órbita–estabilizador convierte la suma original en la suma de clases al nivel menor; no debe insertarse además el índice de Haar, pues la expansión del dato ya suministra la suma de cosets.

En `ptf:laplace`, las filas constantes eliminan las columnas de X posteriores a h y cada coeficiente depende sólo de Z. El mapa conjugado-lineal ξ↦p″_ξ tiene kernel W″⊥; escoger una base de W″ hace única la expansión. `ptf:sum` conserva el mismo carácter fuente y multiplica los objetivos. Se distribuyen `υ^{m−j}` y `ν″υ^j`, cuyo producto es `ν″υ^m`, como requiere el tercer exchange corregido.

Las transformaciones de las primeras formas son exactas: los coeficientes c_λ reciben χ′(det k), y sus conjugados reciben χ′(det k)^{-1}; el kernel W recibe también χ′^{-1}, que se cancela al insertar la forma por conjugado-linealidad. La acción racional se obtiene comparando coeficientes en SD, invariante bajo U(V″)∞. La identidad `ν″υ^{m/2−j}=μυ^{n/2}` usa `r=k+m−1`, `t=5r`; sus exponentes son `(5r+k−1+m)/2=3r`. Por ello se obtiene exactamente el kernel θ″ usado en glue, no otro isomorphic kernel sin normalización fijada.

## 5. Escala integral, hook complementario y cotas

`pfq:hook` usa la aplicación estrella integral y unitaria en cada potencia exterior: transporta el retículo y la proyección al diagrama complementario. El factor H^c hace integral la proyección. La notación `e^{3e}` en ese lema tiene base **el entero e=|μ^c|**; la prueba usa correctamente `log H^c≤3e log e`, no la exponencial de base natural.

En `pfq:Q`, cada coeficiente es un determinante complementario de tamaño ≤12m+1, homogéneo de grado N″−h. Cauchy–Binet suma cuadrados de sus menores y Hadamard da la cota conjunta, evitando multiplicar otra vez por el número de fillings. La sustitución racional en el bloque W^flat cambia Y a γY y aporta el carácter de determinante que cancela el carácter fuente de peso −#ι. Estos cálculos dependen de ν″, no de la definición incorrecta de ν^flat, y no requieren modificarse.

`plf:KS` se reconstruye con los inputs49 ya auditados. La expansión por vacíos tiene Nm(m)^{2ln_N} términos y denominador Nm(m)^{ln_N}. Si qM²∈m y ℓ∤q, M^{4fln_N}/Nm(m)^{ln_N} es integral sobre ℓ; las traslaciones son de nivel M². En lugares donde a_w no es unidad, éstos sólo pueden entrar vía Q y están excluidos de ℓ∤NmQ, de modo que no se invoca falsamente el vacío del retículo no escalado. La escala `(dM²s₀/κ_F)^e` convierte los jets en derivadas integrales; en ℓ=d se utiliza explícitamente `v(g″(0))>−2`, y las derivadas de g(dz) son integrales. Las exponenciales conservan derivadas integrales por los polinomios de Bell con coeficientes enteros.

Para KS2 se usan las DOS consecuencias de δ_g reconstruidas en REVISION-FASE49-V2, no su clasificación fuerte. La integral Gaussiana, con ρ=dΩ^{-1/2}M^{-2}≪b^{-37}, da factor ≤2^{D+1}; se mantienen el número de términos y M^{4f ln_N}. El logaritmo total queda ≤x^{200}≤x₁ en el rango declarado. La constante de kernel no depende del carácter, del dato finito ni de la elección i.

En `pfq:ff`, la normalización es `κ₁=n′_Aut² c_{m,3m,0} conj(c_{j,N″,0}) ε_j c_{12m+1−j,N″,e}`, `κ=H^c conj(κ₁)`. El ε_j cancela el de negación; n′_Aut elimina ambos denominadores de estabilizadores. Las formas se proyectan como `H^c π(conj(κ₁a))`; por ello la integralidad se prueba en la inmersión conjugada, como está escrito. Para tamaños, σ′=σ∘c actúa sobre los coeficientes y la proyección racional tiene norma uno. La dualidad para el vector de todos los C_U evita un factor por su dimensión. Las cotas finales son `2logH^c≤6072 fmb logb` y el término de menores ≤10764 fmb logb`, ambos por debajo de `1.7·10⁴ fmb logb`; las otras pérdidas caben en 8x₁. No se usa una falsa conmutación universal σc=cσ.

La sustitución de primeros factores por κ veces los originales cambia Ξ por conj(κ), c′ por c′/conj(κ) y C_x por C_x/|κ|². Sólo cambia la constante fija C_j en Gram. Los caracteres tame se construyen por extensión de un carácter del subgrupo abierto, con compatibilidad sobre μ_E; ésta se comprueba con q₁|q₂ y los primos ≡1 modq₂². La corrección de ν^flat en T4 deja todas esas condiciones intactas.

## 6. Dictamen de alcance

- **(b), literal:** definición de ν^flat2695/7584 incompatible con igualdad2730 y usos3366/6448.
- **(a), reconstrucción corregida:** tres exchanges y sus primeros factores, con ν^flat=ν″/χ′, corrección topológica del promedio de explicit y justificación Parseval del carrier; las constantes y H_j permanecen exactas.
- **Entrada clásica individualizada:** la compatibilidad de splitting bajo negación/cambio de carácter debe recibirse de la normalización P3 cotejada por la rama correspondiente; se ha comprobado toda la cuenta de signos a partir de ella.
- **Gram general:** el álgebra de glue y del determinante comprimido está verificada; períodos generales ya cerrados en REVISION-54-PERIODOS-GENERALES-V2. La generación global `po:span` sigue la auditoría separada de psp/psr/psv, con la misma definición corregida de ν^flat. No se declara Gram completo antes de recibir ese resultado.

## 7. Cierres cruzados y sincronización con P58

La revisión primaria de splitting quedó cerrada en `SPLITTING-V2`, §§6–7: en la normalización izquierda de Murase el carácter es υ^{-1}; la forma R_g=Q(g−1) sobre el cociente por el núcleo satisface `R_g*=R_g g^{-1}`, de donde `Δ/conj(Δ)=det g`. Sustituir υ por `υ·(μ∘bc)` multiplica el splitting por `μ(det g)^{-1}`. Éste es exactamente K3 con s=−1, también bajo doblamiento D2; la factorización ortogonal de M y Δ conserva la compatibilidad de productos. Así se descarga la entrada clásica que §6 dejaba individualizada, sin una fase residual arbitraria.

La rama spanning confirmó el efecto preciso de la definición impresa sobre H5, 6448: el peso sería `2m−μ₁`, y el coeficiente calculado tendría un factor adicional `det(h)^{-m}`. En el promedio que debe dar el valor positivo inicial, ese peso central obliga a cero. Por tanto no cabe afirmar que la definición impresa es inocua. Con la definición corregida el peso vuelve a `m−μ₁` y se restablece la identidad H5; la fórmula `psv:char` usa ν″ directamente y no cambia. El cierre completo de span se registra en su ledger propio.

En el volumen P58 la misma definición defectuosa aparece en **51272** y **56151** de `main.tex`. La segunda incluye también el exponente final `+m`. Son las dos ubicaciones que requieren la misma corrección; los usos de `ν^flat υ^m` se conservan. Se trata de una reconstrucción suplementaria, no de un cambio ya incorporado en el manuscrito.
