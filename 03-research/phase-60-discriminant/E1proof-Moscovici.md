# E1 — Real-rootedness de ξ̂_{λ,N}: ¿prueba propia o cita obligada?
## Re-examen (lente de Branges / Hermite–Biehler) **Autor del análisis:** H. (referee), en colaboración con ·.
**Regla:** frío. Una prueba forzada es peor que un gap admitido. NO se reclama RH.
**Objeto:** E1 = «para todo λ,N, ξ̂_{λ,N}(s)=sin(Ls/2)·Σ_{|k|≤N} ξ_k/(s−d_k) tiene sólo
ceros reales», donde ξ es el ground state de la forma de Weil QW. Vale empíricamente incluso
para Davenport–Heilbronn (RH-falsa). **Veredicto:** **CITA OBLIGADA** (CCM Thm 1.1(iii)). El intento de rescate por «resolvente
cuadrático» **no aplica al objeto correcto**, y la construcción de Branges, aunque existe en
abstracto, **es equivalente a la realización autoadjunta misma** — no un atajo. Detalle abajo. --- ## 1. La pregunta decisiva: ¿lineal o cuadrático? (tarea §1) La hipótesis de rescate era: quizá el objeto CCM correcto sea el **resolvente diagonal**
``` m(s) = ⟨ξ,(s−D)^{-1}ξ⟩ = Σ_k ξ_k²/(s−d_k) (residuos al CUADRADO),
```
que es **automáticamente Herglotz** (residuos ξ_k²≥0 ⟹ Im m<0 en el semiplano superior
⟹ sólo ceros reales, Nevanlinna). Si ξ̂ proviniera de m, E1 cerraría en una línea. **Esto es FALSO, y de forma terminal. Hay que separar dos cosas:** ### 1.1 La ecuación de autovalor SÍ tiene cuadrados — pero no es ξ̂
La verdadera ecuación secular de la **perturbación rango-1** (H1_PROOF.md §7, term de polo
P=|φ⟩⟨φ|) es
``` 1 + Σ_k |⟨φ,ψ_k⟩|²/(λ_k − μ) = 0,
```
sí, con residuos **cuadrados** |⟨φ,ψ_k⟩|²>0 — y por eso da interlacing μ₀∈(λ₀,λ₁) limpio.
Pero esa es la ecuación que localiza **el autovalor μ₀ del operador**, NO la función band-limited
ξ̂ cuyos ceros son los γ_ρ (los ceros de ζ). Son dos resolventes distintos: | objeto | residuos | papel | real-rooted |
|---|---|---|---|
| `1+Σ|⟨φ,ψ_k⟩|²/(λ_k−μ)` | cuadrados | localiza μ₀ (autovalor) | sí, trivial (Herglotz) |
| `f(s)=Σ ξ_k/(s−d_k)` | **lineales** | secular: sus ceros = γ_ρ | **es E1, lo no trivial** | ### 1.2 ξ̂ es inequívocamente el resolvente LINEAL (no hay typo/gauge)
La Prop. \ref{prop:bandlimited} de `rh-proof.tex` lo fija sin ambigüedad:
``` ξ̂_{λ,N} = Σ_k ξ_k · sinc_k (interpolación cardinal de las MUESTRAS ξ_k en la red d_k).
```
Esto es lineal en ξ_k por construcción: ξ̂ interpola los **valores** ξ_k, no sus cuadrados.
Es la imagen del autovector bajo el isomorfismo de Paley–Wiener (ℓ²(red Nyquist)→PW_Ω),
una **isometría lineal**. Sustituir ξ_k↦ξ_k² destruiría esa estructura: la función resultante
ya no sería la transformada del ground state, no satisfaría la identidad de Weil
⟨ξ,QWξ⟩=Σ_ρ ξ̂(γ_ρ)conj(ξ̂(conj γ_ρ)) (§1 del documento maestro), y sus ceros **no** serían
los ceros de ζ. No es gauge: es otro objeto, con otra función-cero. ### 1.3 Demostración elemental de que m y f son funciones-cero DISTINTAS
Contraejemplo del programa, ξ=(−1,2,−1), d=(−1,0,1) (cálculo a mano, Python bloqueado): - **Lineal** f = −1/(s+1)+2/s−1/(s−1). Numerador = −s(s−1) + 2(s²−1) − s(s+1) = (−s²+s) + (2s²−2) + (−s²−s) = **−2** (constante). ⟹ **CERO ceros reales** (de hecho cero ceros). [coincide con `−2/(s³−s)` del programa]
- **Cuadrático** m = 1/(s+1)+4/s+1/(s−1). Numerador = s(s−1) + 4(s²−1) + s(s+1) = (s²−s)+(4s²−4)+(s²+s) = **6s²−4**. ⟹ ceros en s=±√(2/3)=±0.816, **reales** (como obliga Herglotz). **Conclusión §1.** El resolvente cuadrático m es trivialmente real-rooted, **pero sus ceros
(±0.816) no son los de ξ̂ (ninguno)**. Reemplazar f por m no es corregir un typo: cambia la
función-cero y rompe la identidad de Weil. ξ̂ es genuinamente el resolvente **lineal**.
La vía Herglotz-de-cuadrados **no cierra E1**. ∎(§1) > Corolario severo: la tentación «residuos²⟹Herglotz⟹RH» es exactamente el tipo de atajo que
> hay que rechazar. El cuadrado correcto (la forma cuadrática ⟨ξ,QWξ⟩=Σ_ρ|ξ̂(γ_ρ)|²) **sí**
> existe y **sí** es ≥0 — pero **solo bajo RH** (γ_ρ reales). Ahí vive el núcleo RH (IV.2),
> no una prueba de E1. El cuadrado que ayudaría está horneado con RH; el cuadrado gratis (m)
> es el objeto equivocado. --- ## 2. El intento de Branges explícito (tarea §2) Como f es genuinamente lineal, hay que ver si ξ̂ es la parte B (o A) de una E=A−iB de
Hermite–Biehler, lo cual daría ceros reales por interlacing de de Branges. ### 2.1 Lo que ξ̂ SÍ satisface (constraints favorables)
ξ̂ es: entera, **de tipo exponencial exacto Ω=logλ** (Paley–Wiener), **real en ℝ**, **par**
(ι-simetría del ground state), y en L²(ℝ) (Plancherel–Pólya, ‖ξ̂‖²=π logλ). Estas son
precisamente las condiciones para *aspirar* a membresía en un espacio de Branges H(E) con E
de estructura real y par. Hasta aquí, prometedor. ### 2.2 La construcción canónica y por qué es circular
Para una función entera real g de tipo exponencial τ en L²(ℝ), la candidata canónica es
``` E(s) = g(s) − i·g̃(s), g̃ = transformada de Hilbert (conjugada armónica) de g,
```
y g=B=−Im E|_ℝ. La **desigualdad de Hermite–Biehler** |E(s̄)|<|E(s)| para Im s>0
**equivale** (de Branges, Teoremas 12–13; Hermite–Biehler clásico) a: > los ceros de A=Re E y de B=g son **todos reales y se entrelazan**, con Wronskiano
> A'B−AB' de **signo constante** en ℝ. Es decir: **construir E HB ⟺ ya saber que los ceros de ξ̂ son reales y simples**. La
desigualdad HB no es una hipótesis verificable por separado a partir de la información que el
programa tiene aislada (envolvente PF positiva); **es lógicamente equivalente a la conclusión
E1**. No hay ganancia: exhibir E con HB *es* probar E1. ### 2.3 El obstáculo concreto que impide verificar HB a mano: desajuste de fase
¿Por qué no se puede certificar |E(s̄)|<|E(s)| directamente? Porque el único insumo de signo
disponible es **PF en el espacio-función**: ψ₀ es nodeless en L²([λ⁻¹,λ]) (H1, §6). Pero los
**coeficientes ξ_k** son las coordenadas de ψ₀ en la **base sinc/Nyquist**, ligadas a ψ₀ por
la isometría PW — que **no preserva positividad coordenada**. El ground state real tiene
``` ξ_k ≈ u_k·cos(ω* k + φ), u_k>0 (envolvente PF positiva), ω*≈0.966π (carrier de borde).
```
- Demodular por el portador Nyquist exacto, ξ_k=(−1)^k η_k, haría η_k de signo casi-constante, pero **reintroduce (−1)^k en los residuos** de f ⟹ no es Herglotz.
- Como ω*≈0.966π **≠** π, no hay demodulación que vuelva los residuos *crudos* de signo constante: **ni ξ_k>0 ni (−1)^k ξ_k>0**. Para E=A−iB, esto significa: A y B son ξ̂ y su conjugada de Hilbert, y el control del
**Wronskiano A'B−AB' de signo constante** (la condición HB operativa) requiere precisamente
el interlacing de los ceros de A y B — que es la propiedad espectral autoadjunta. PF entrega
positividad en la coordenada equivocada (envolvente, no residuos), de modo que **el signo del
Wronskiano no se deduce de la información PF aislada**. Ese es el muro técnico exacto. ### 2.4 Por qué la realización autoadjunta SÍ da HB — pero eso ES CCM 1.1(iii)
Si f(s)=Σ ξ_k/(s−d_k) es la **función-m de Weyl–Titchmarsh de un operador de
Jacobi/Sturm–Liouville autoadjunto** (no necesariamente con pesos positivos), entonces f es
Nevanlinna/Herglotz por construcción espectral, sus ceros y polos se entrelazan, y la E
asociada es HB **automáticamente** — incluso con coeficientes de signo variable (esto es por
qué funciona para Davenport–Heilbronn, donde Λ≥0 falla: la autoadjunción no usa positividad).
**Pero «las raíces seculares = espectro real de la realización autoadjunta de CCM» es
literalmente el enunciado de CCM Thm 1.1(iii).** Reconstruir esa realización (exhibir el Jacobi
del que f es la m-función, o el H(E) del que ξ̂ es elemento) **es re-probar 1.1(iii)**, no un
lema de funciones enteras pendiente de azúcar. **Conclusión §2.** E existe en abstracto (cualquier g∈LP de tipo finito vive en algún H(E)),
pero exhibirla con HB **verificada** es equivalente a E1, y el insumo PF disponible no la
certifica por el desajuste de fase ω*≠π. La construcción de Branges **no es self-contained**;
colapsa a la realización autoadjunta = CCM 1.1(iii). ∎(§2) --- ## 3. Veredicto brutalmente honesto (tarea §3) **E1 es CITA OBLIGADA de CCM Thm 1.1(iii).** Precisamente: 1. **Sub-caso cerrado (Lema M1, propio, sin citar CCM):** si todos los residuos ξ_k>0, f es Herglotz ⟹ sólo ceros reales con interlacing estricto. Elemental, sólido. **NO cubre el ground state real** (carrier ω*≈0.966π). 2. **Rescate por resolvente cuadrático: REFUTADO.** Σξ_k²/(s−d_k) es Herglotz y real-rooted, pero es un **objeto distinto** cuyos ceros no son los de ξ̂ (demostrado elementalmente en §1.3); ξ̂ es genuinamente el resolvente **lineal** Σξ_k sinc_k fijado por Paley–Wiener y por la identidad de Weil. No hay typo ni gauge. 3. **Rescate por de Branges explícita: NO es atajo.** La E=A−iB canónica existe, pero la desigualdad HB |E(s̄)|<|E(s)| es **lógicamente equivalente** a E1, y su verificación pide el signo del Wronskiano A'B−AB', que la positividad PF (envolvente, base función) **no** entrega en la base de residuos por el desajuste de fase ω*≠π. La única vía es la m-función de un operador autoadjunto = **CCM Thm 1.1(iii)**. **Obstrucción precisa (one-liner):** *La real-rootedness de ξ̂ es la afirmación de que la
secular lineal f(s)=Σξ_k/(s−d_k) es una m-función de Nevanlinna autoadjunta; la única
positividad probada (PF, envolvente positiva u_k>0) vive en la base función y, vía el carrier
de borde ω*≈0.966π≠π, NO se traduce a positividad de los residuos crudos ξ_k ni a un
Wronskiano de signo constante. Por tanto E1 no admite prueba al nivel Herglotz/HB elemental;
es cita obligada de la realización autoadjunta CCM 1.1(iii).* **Estatus heredado:** E3 (Hurwitz) y N5c siguen «módulo E1». Etiqueta del documento maestro
(🔧, cita obligada) **confirmada y reforzada**: no es «reparación cerrable con más trabajo de
funciones enteras». **Honestidad:** E1 es **RH-neutral** (vale para DH). Usar E1 como caja negra de CCM para
concluir RH **no es circular** — la carga RH no está en E1 sino en la convergencia (IV.2).
Citar CCM 1.1(iii) aquí es legítimo; presentarlo como gap cerrable sería auto-engaño. *— H..*
