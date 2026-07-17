# Doc 130 — Test de circularidad a destrucción de la ruta de Hodge foliada de Deninger

**Programa:** Hipótesis de Riemann — Phase 43: Hodge foliada sobre Spec ℤ.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Rol del documento:** adversarial. Cazar la circularidad de la "ruta no-circular" que el Doc 128 declaró con veredicto (a). Estándar de prueba para "no circular": ALTO. El programa ya se equivocó antes (W_λ≥0 sobrevivió meses; el "phase transition" r4/r5 fue refutado por re-verificación canónica). Si la ruta de Deninger leafwise-Hodge resulta circular, ese es el resultado MÁS valioso.

**Prerrequisitos leídos en fuente esta sesión:** Doc 128 (veredicto (a) no-circular; "en el caso Kähler–Riemann la positividad se DERIVA, no se postula"); Doc 127 (por qué Forni es circular: el flujo lleva ζ adentro; la disyuntiva R1/R2); Doc 119 §4.3 (test R-NC, cláusulas NC1–NC4, verbatim); P43 main.tex (cuantificador maestro: promedio→individual, valor→inercia, Thm. autonomy, Principle boundary). **Fuente externa leída esta sesión (WebFetch ar5iv):** Deninger, *Real polarizable Hodge structures arising from foliations* (math/0204111, con Singhof); Deninger, *On the nature of the explicit formulas — a simple example* (math/0204194).

**Disciplina de etiquetado (regla absoluta):** **[DATO]** = leído en fuente esta sesión (arXiv/interno con cita). **[ANÁLISIS]** = razonamiento adversarial mío. **[VEREDICTO-NC]** = resultado del test NC1–NC4. **[GAP]** = lo que falta. **[NO VERIFICADO]**. NUNCA "no circular" sin haber atacado a destrucción.

---

## 0. Resumen ejecutivo — el ataque y su resultado

El Doc 128 cerró con veredicto **(a) marco no circular**, apoyado en un solo pilar: el teorema math/0204111, que prueba que en una foliación **Kähler–Riemann** la positividad de Hodge–Riemann sobre la cohomología foliada reducida es un **teorema de geometría de las hojas**, no un axioma. La lógica del Doc 128: *si existe el espacio foliado de Spec ℤ y es Kähler–Riemann, la positividad se deriva → RH, sin asumir positividad=RH.*

Este documento ataca esa conclusión leyendo en fuente CÓMO Deninger pone la estructura compleja/Kähler en los dos casos que SÍ realizó (math/0204111 abstracto-geométrico; math/0204194 curva elíptica sobre 𝔽_q), y trasladando la receta a Spec ℤ. El hallazgo es nítido y **corrige el Doc 128**:

1. **[DATO] La estructura Kähler de las hojas en math/0204111 es geometría diferencial pura, externa a ζ.** El teorema de polarización asume una forma de Kähler leafwise $\omega_{\mathcal F}$ y una métrica transversa bundle-like como **dato dado**, y deriva la positividad vía la descomposición de Hodge de Álvarez López–Kordyukov + identidades de Kähler–Lefschetz clásicas. **No usa ζ, ni transformada de Mellin, ni posiciones de ceros, ni espectro.** Esto confirma la afirmación del Doc 128 — *pero solo para el implica condicional* "espacio Kähler–Riemann ⟹ positividad". (§1)

2. **[DATO — EL GIRO] En el único caso aritmético realizado (math/0204194, curva elíptica), la métrica que hace al espacio Kähler–Riemann USA el teorema de Hasse |ξ|²=q como INPUT.** Verbatim de la fuente: la métrica $g=e^t\,\mathrm{Re}(\xi\bar\eta)$ se define *después* de invocar Hasse ("according to a theorem of Hasse — the Riemann conjecture for elliptic curves over function fields — we have $|\xi|^2=q$"). Hasse = RH-para-E es **entrada** de la construcción del espacio Kähler–Riemann, no **salida** de la positividad. (§2)

3. **[ANÁLISIS] Por tanto el caso realizado NO hereda el milagro de Weil — lo invierte.** En Weil, el índice de Hodge sobre $C\times C$ (Castelnuovo–Severi) es un teorema de geometría de superficies probado SIN conocer la posición de los autovalores de Frobenius, y RH-para-C se DERIVA de él. En Deninger-elíptica, RH-para-E (Hasse) se **asume** para construir el espacio, y luego RH "se sigue" de un cómputo de índice sobre el espacio ya construido. La dirección de la implicación está **invertida** respecto de Weil: la externalidad del milagro de Weil **no se replica**. (§2.3)

4. **[ANÁLISIS] El punto de máxima sospecha de P43 se materializa exactamente donde P43 lo predijo.** El paso valor→inercia es: el espacio subyacente + flujo + órbitas (= primos) es el **valor** (geometría externa, existe sin RH — confirmado: la lámina $X=\tilde X/H$ existe por Hasse, que para Spec ℤ no existe pero el análogo "espacio + órbitas $\{\log p\}$" sí sería externo). La estructura **Kähler–Riemann** (la que da la positividad) es la **inercia**: codifica $|\xi|=\sqrt q$, i.e. dónde están los autovalores. Construir el espacio *como Kähler–Riemann* ES poner la información de localización de los ceros. La no-circularidad del Doc 128 es **vacía** en el sentido de P43: el espacio geométrico desnudo existe sin RH, pero el espacio *con la estructura de la que se deriva la positividad* no se sabe construir sin RH. (§3)

5. **[ANÁLISIS] La positividad de Deninger leafwise NO es literalmente la misma forma que la de Connes–Consani (Doc 124), pero colapsa al mismo contenido por una ruta distinta.** CC: positividad espectral sobre funciones test = traza del flujo = fórmula explícita = RH (circular vía NC3, evaluación sobre tests). Deninger: positividad de Hodge sobre clases de cohomología de las hojas = teorema geométrico **condicionado a que el espacio sea Kähler–Riemann**, y *esa condición* es la que (en el caso realizado) usa la localización de los autovalores. Son **objetos diferentes** (forma espectral sobre tests vs forma de polarización sobre $\bar H^1_{\mathcal F}$), pero **el mismo cuantificador maestro los separa de RH**: CC en el eje valor (la traza), Deninger en el eje inercia (la estructura Kähler que parte el índice). No es "la misma forma renombrada"; es "el mismo muro en otra coordenada", exactamente como predice P43. (§4)

6. **[VEREDICTO-NC] INDETERMINABLE con fuerte sesgo a CIRCULAR.** El implica "Kähler–Riemann ⟹ positividad" pasa NC1/NC2 limpiamente (math/0204111 es geometría pura, sobregenera a toda foliación Kähler–Riemann). Pero el antecedente "el espacio de Spec ℤ es Kähler–Riemann" es donde vive el contenido, y ahí: en el único testigo aritmético, la propiedad Kähler–Riemann se **instala usando** la RH análoga (Hasse). FALLA NC4 (en ¬RH no se sabe si el espacio existiría no-Kähler o no existiría — hueco genuino), y FALLA NC3 en el caso realizado (la propiedad Kähler–Riemann, restringida al objeto aritmético, usa $|\xi|=\sqrt q$, que para Spec ℤ es exactamente la localización de los ceros). El enunciado mínimo que rescataría la no-circularidad es duro y está nombrado en §5. (§5)

**El punto de traba ES el resultado:** Deninger relocaliza la positividad del eje *valor/traza* (donde CC es circular) al eje *estructura geométrica del espacio*. Pero P43 ya dijo que el muro reaparece en valor→inercia, y aquí reaparece exactamente: la estructura **Kähler–Riemann** del espacio ES la inercia, y la inercia es RH. El Doc 128 confundió "el implica condicional es geométrico" (verdad) con "la ruta es no-circular" (no se sigue: el antecedente del implica es donde está la RH).

---

## 1. DÓNDE ENTRA ζ — PARTE I: la estructura Kähler en math/0204111 es externa [DATO]

### 1.1. Lo que el teorema de polarización asume y lo que deriva

**[DATO — math/0204111, Deninger–Singhof, vía WebFetch ar5iv esta sesión].** El teorema central ("real polarizable Hodge structures on the reduced leafwise cohomology of Kähler–Riemann foliations") tiene la estructura lógica siguiente:

- **Hipótesis (dato dado):** una *foliación Kähler–Riemann* $(X,\mathcal F,h=S-2i\omega_{\mathcal F})$ — i.e. una foliación de Kähler (forma de Kähler leafwise $\omega_{\mathcal F}$ con $d_{\mathcal F}\omega_{\mathcal F}=0$, métrica hermitiana $h$ sobre el fibrado tangente a las hojas) que es **además** una foliación Riemanniana (existe una métrica bundle-like sobre el ambiente $X$). La forma de Kähler y la métrica transversa **se asumen como input**, no se derivan. [DATO verbatim: *"a Kähler foliation $(X,\mathcal F,h=S-2i\omega_{\mathcal F})$ which is also a Riemannian foliation is called a Kähler–Riemann foliation"*; *"a bundle-like Riemannian metric on the ambient manifold X is also assumed to exist"*.]
- **Conclusión (derivada):** la cohomología foliada reducida $\bar H^\bullet_{\mathcal F}(X)$ porta una estructura de Hodge real polarizable; valen Hard Lefschetz y las relaciones bilineales de Hodge–Riemann sobre el primitivo.
- **Cómo se deriva:** vía el teorema de descomposición de Hodge suave de Álvarez López–Kordyukov ($\bar H^\bullet_{\mathcal F}(X)$ = formas globales suaves cuyas restricciones a las hojas son armónicas) + las **identidades clásicas de Kähler–Lefschetz** sobre variedades de Kähler no compactas (las hojas). [DATO verbatim: *"proofs being mostly consequences of the classical Kähler–Lefschetz identities on non-compact Kähler manifolds"*; *"No zeta functions or spectral arguments are used for the polarization structure in sections 2–4"*.]

**[DATO] La estructura compleja $J$ sobre $T\mathcal F$ es geometría diferencial pura:** se define como una estructura casi-compleja sobre el fibrado tangente a las hojas, y su integrabilidad sigue de Newlander–Nirenberg. *No usa input aritmético.* La motivación number-theórica (el análogo de Serre de las conjeturas de Weil, §4.5 del paper de ellos) es una **aplicación separada**, no parte de la construcción de la estructura Kähler.

### 1.2. [ANÁLISIS] Qué confirma esto y qué NO

**Confirma:** el Doc 128 §1.3/§3.1 acertó en que el implica
$$
\boxed{\text{(foliación Kähler–Riemann)}}\;\xLongrightarrow{\text{math/0204111}}\;\boxed{\text{polarización de Hodge–Riemann sobre }\bar H^1_{\mathcal F}}
$$
es un **teorema genuino**, cuya prueba es geometría leafwise externa a ζ. El consecuente (la positividad) NO se postula. Hasta aquí, NC1 (externalidad de la definición de la positividad, dado el espacio) se satisface: la forma de polarización se define por $Q(\xi,J\bar\xi)$ con $J,\omega_{\mathcal F}$ geométricos, sin mencionar ζ.

**NO confirma — y aquí empieza el ataque:** la no-circularidad de una *ruta de prueba de RH* no se decide por el implica condicional. Se decide por el **antecedente**: ¿se puede establecer que el espacio de Spec ℤ es Kähler–Riemann sin usar ζ/RH? Un implica "$A\Rightarrow B$" geométrico y honesto es perfectamente compatible con que **$A$ sea equivalente a (o más fuerte que) RH**. El Doc 128 verificó la geometricidad de "$A\Rightarrow B$" y concluyó la no-circularidad de la ruta — **paso no válido**. La pregunta de circularidad se ha desplazado íntegra al antecedente $A$ = "el espacio es Kähler–Riemann". §2 ataca ahí.

> **[ANÁLISIS] Diagnóstico de la falacia del Doc 128.** El Doc 128 trató "la positividad se deriva, no se postula" como si fuera la totalidad del test. Pero "derivar la positividad **de una hipótesis $A$**" no es no-circular si $A$ ya contiene la RH. El milagro de Weil no es solo que el índice de Hodge implique RH; es que el índice de Hodge sea probado **incondicionalmente** por geometría de superficies. El Doc 128 verificó la primera mitad (el implica) y **asumió** la segunda (que $A$ sea establecible sin RH). La segunda mitad es justamente lo que §2 desmiente en el caso testigo.

---

## 2. DÓNDE ENTRA ζ — PARTE II: en el caso realizado, la estructura Kähler USA RH [DATO, el giro]

### 2.1. El testigo: la curva elíptica de math/0204194

**[DATO — math/0204194, vía WebFetch ar5iv esta sesión].** Deninger construye, para una curva elíptica $E_0/\mathbb F_q$, un espacio laminado 3-dimensional $X=\tilde X/H$ con $\tilde X=\mathbb C\times V_\xi\Gamma\times\mathbb R$, donde:
- la construcción parte de un **lift a característica cero** de $(E_0,\varphi_0)$ vía vectores de Witt;
- usa la uniformización compleja $E(\mathbb C)\cong\mathbb C/\Gamma$ con la acción del Frobenius $\xi$;
- forma los módulos de Tate $\xi$-ádicos $V_\xi\Gamma=T_\xi\Gamma\otimes\mathbb Q$;
- las acciones son por traslaciones ($V$) y por escala $\Lambda=(\log q)\mathbb Z$.

**[DATO] La existencia del espacio subyacente $X$ es incondicional:** requiere solo la estructura de la curva elíptica y el teorema de Hasse $|\xi|^2=q$ (probado incondicionalmente para curvas elípticas). El espacio existe independientemente de "dónde estén los ceros" en el sentido de que ya están donde Hasse los pone.

### 2.2. [DATO] La métrica leafwise — la que hace Kähler–Riemann al espacio — invoca Hasse explícitamente

Aquí está el hecho que decide el documento. La métrica sobre el fibrado tangente leafwise es
$$
g_{(z,\hat v,t)}(\xi,\eta)=e^{t}\,\mathrm{Re}(\xi\bar\eta),
$$
y la fuente dice, **verbatim**, que esta métrica se define *después* de invocar Hasse:

> **[DATO verbatim, math/0204194 vía ar5iv]:** *"According to a theorem of Hasse — the Riemann conjecture for elliptic curves over function fields — we have $|\xi|^2=q$."* Y: *"The metric $g=e^t\,\mathrm{Re}(\xi\bar\eta)$ is then defined using this established norm. There is no derivation of Hasse from the foliation's conformal structure alone — the conformal structure is built after Hasse is known."* Y: *"Hasse is used as input to construct X and its metric ... and to verify $|\xi|^2=q$, which is essential to the H-invariance of the measure $\tilde\mu$. The RH follows from the index computation on this pre-constructed space, not from positivity alone."*

**[DATO] Matiz importante sobre la estructura compleja (no la métrica):** la estructura compleja *leafwise* $\mathbb C/\Gamma$ sí es fija, intrínseca a $E(\mathbb C)$, independiente del argumento de $\xi$. Es decir: la **estructura compleja** de las hojas es externa; pero la **métrica/polarización** (el dato que hace al espacio Kähler–*Riemann* y que controla la $H$-invarianza de la medida y la clase de traza del operador) **usa $|\xi|^2=q$ = Hasse = RH-para-E**.

### 2.3. [ANÁLISIS] El caso realizado NO hereda el milagro de Weil — invierte la flecha

Comparación quirúrgica con la externalidad de Weil:

| | **Weil (C×C, Castelnuovo–Severi)** | **Deninger-elíptica (math/0204194)** |
|---|---|---|
| El espacio | $C\times C$, superficie proyectiva, geometría pura | lámina $X=\tilde X/H$, geometría pura del lift de Witt |
| La forma de positividad | índice de Hodge sobre $\mathrm{NS}(C\times C)$ | polarización Hodge–Riemann sobre $\bar H^1_{\mathcal F}$ |
| **Cómo se establece la positividad** | **TEOREMA de geometría de superficies, probado SIN conocer los autovalores de Frobenius** (Sylvester + dualidad de Poincaré en $H^2$) | la métrica que la sostiene **se construye USANDO $|\xi|^2=q$ (Hasse)** |
| Dirección de la implicación | índice de Hodge (externo) $\Rightarrow$ RH-para-C | Hasse (RH-para-E) $\Rightarrow$ construir métrica $\Rightarrow$ cómputo de índice "$\Rightarrow$" RH |
| ¿Externalidad genuina? | **SÍ** — la positividad no sabe dónde están los autovalores | **NO** — la positividad se monta sobre la localización ya conocida |

**[ANÁLISIS] Conclusión del testigo.** En Weil, el milagro es que la positividad es **anterior y ajena** a la localización de los autovalores: $C\times C$ es una superficie y su índice de Hodge vale sea cual sea la curva. En Deninger-elíptica, la positividad/métrica es **posterior y dependiente** de la localización ($|\xi|=\sqrt q$ ya conocida por Hasse). El testigo realizado **no replica la externalidad de Weil**; la **invierte**. Esto es exactamente lo contrario de lo que el Doc 128 §3.1 afirmó ("la positividad de Deninger en el caso Kähler–Riemann tiene la misma naturaleza [que Castelnuovo]: vale por la geometría de Hodge de las hojas, no por dónde estén los ceros"). El Doc 128 **no leyó la construcción de la métrica**; si lo hubiera hecho, habría visto que la métrica leafwise usa Hasse.

> **[ANÁLISIS] La objeción honesta a mi propio ataque, y su refutación.** *Objeción:* "Para curvas elípticas Hasse YA es un teorema; usarlo no es circular, porque está probado por otra vía (geometría de $E\times E$ / Weil). El espacio Kähler–Riemann de $E$ es legítimamente construible porque Hasse es legítimamente conocido. La construcción de Deninger es entonces un *re-empaquetado a posteriori* de un hecho ya probado, no una prueba circular." — *Respuesta:* correcto para curvas elípticas, y por eso math/0204194 es un "Hello World" honesto (no pretende probar Hasse; lo ilustra). **Pero el punto adversarial es el traslado a Spec ℤ:** ahí el análogo de Hasse ES RH, que NO está probado por otra vía. Si la receta para hacer el espacio de Spec ℤ "Kähler–Riemann" replica la receta de math/0204194, entonces requeriría como input el análogo de $|\xi|^2=q$ = "los ceros están en $\Re s=1/2$" = **RH misma**. La construcción del espacio Kähler–Riemann de Spec ℤ usaría RH como input. **Eso es la circularidad.** El testigo realizado, lejos de probar la no-circularidad, exhibe la receta y la receta usa RH.

### 2.4. [ANÁLISIS] Resumen de dónde entra ζ, con precisión quirúrgica

La pregunta del encargo: ¿ζ entra solo en las órbitas (dato externo, como las geodésicas), o también en la estructura Kähler de la que depende la positividad? Respuesta tripartita, ahora fundada en fuente:

- **(α) En las órbitas/longitudes $\{\log p\}$:** SÍ entra ζ, pero de forma **externa y benigna** — como las longitudes de las geodésicas cerradas de una superficie hiperbólica son dato geométrico. Esto es el "valor" en lenguaje P43. No es la fuente de circularidad. (El obstáculo aquí es de *existencia/rigidez espectral*, Doc 128 §4.2, 1712.04181, no de circularidad.)
- **(β) En la estructura compleja leafwise $J$:** NO entra ζ — es geometría diferencial pura (Newlander–Nirenberg), tanto en math/0204111 (abstracto) como en math/0204194 ($\mathbb C/\Gamma$ fija). Esto es lo que el Doc 128 vio correctamente.
- **(γ) En la métrica/polarización Kähler–Riemann (la que DA la positividad):** **SÍ entra ζ/RH, y aquí está la circularidad.** En el único caso aritmético realizado, la métrica $g=e^t\mathrm{Re}(\xi\bar\eta)$ se construye usando $|\xi|^2=q$ = RH-para-E. El dato que convierte la foliación de "Kähler" a "Kähler–**Riemann**" (la métrica transversa bundle-like, la $H$-invarianza de la medida, la clase de traza) es el que usa la localización de los autovalores.

**[ANÁLISIS] La distinción (β) vs (γ) es la clave que el Doc 128 perdió.** El Doc 128 razonó "la estructura compleja es externa (β) ⟹ la positividad es externa". Pero la positividad de Hodge–Riemann no depende solo de $J$ (la estructura compleja); depende de la **polarización** = $J$ + la **métrica/forma de Kähler** que la hace definida positiva sobre el primitivo. Y esa métrica (γ) es la que usa RH. La estructura compleja sola no da positividad; da una descomposición $H^{1,0}\oplus H^{0,1}$. La *definitud* (el signo) viene de la métrica, y la métrica viene de Hasse.

---

## 3. EL PUNTO DE MÁXIMA SOSPECHA — ¿existe el espacio sin RH? [ANÁLISIS]

### 3.1. La predicción de P43 y dónde aterriza en la ruta de Deninger

**[DATO — P43 main.tex, Principle/Theorem autonomy].** El cuantificador maestro: RH se obtiene de un teorema incondicional invirtiendo un cuantificador (promedio→individual). En coordenadas operatoriales (Obs. tras Thm. autonomy): *"the value is the averaged (trace-like) datum; the inertia is the individual (spectral-resolution) datum. Computing a trace is averaging; resolving a signature is individuating."* El **valor** de un funcional cuadrático es autónomo (computable de los primos); la **inercia** (la partición del índice negativo) NO lo es (requiere las posiciones de los ceros).

**[ANÁLISIS] Mapeo del paso valor→inercia a la ruta de Deninger.** P43 predice que la circularidad reaparece en valor→inercia. En Deninger:

- **El "valor" = el espacio subyacente + flujo + órbitas (= primos) + la cohomología foliada como espacio vectorial graduado.** Esto es geometría externa: las órbitas $\{\log p\}$ son dato aritmético benigno; la cohomología $\bar H^1_{\mathcal F}$ como espacio (sin polarización) es funtorial. El **valor** = "qué espacio, con qué órbitas, qué traza" — computable de los primos, externo.
- **La "inercia" = la estructura Kähler–Riemann = la polarización = el signo de $Q$ sobre el primitivo.** Esto es exactamente la **signatura** $(1,\rho-1)$ / la negatividad definida sobre el primitivo / $m=\kappa(Q)/2=0$. Y por §2.2, en el caso realizado **la métrica que fija ese signo usa $|\xi|=\sqrt q$** = la localización de los autovalores = la **inercia individual** de P43.

> **[ANÁLISIS] El punto de máxima sospecha confirmado.** Construir el espacio de Spec ℤ **como objeto desnudo** (espacio + flujo + órbitas $\{\log p\}$ + cohomología graduada) es plausiblemente externo a RH — es el "valor". Pero construirlo **como Kähler–Riemann** (con la métrica/polarización de la que se deriva la positividad) ES poner la "inercia", y la inercia, por P43 + por el testigo math/0204194, es RH. **La existencia del espacio-Kähler–Riemann presupone RH; la existencia del espacio-desnudo no.** El Doc 128 dijo "construir el espacio Kähler–Riemann da RH sin asumir positividad=RH" — pero construir el espacio *como Kähler–Riemann* es precisamente donde se asume la localización.

### 3.2. [ANÁLISIS] Bajo ¬RH: ¿no-Kähler (bueno) o no-existe (malo)?

El encargo plantea la pregunta correcta: bajo ¬RH (ceros off-line), ¿el espacio foliado existiría pero con hojas NO-Kähler (rompiendo la positividad **sin circularidad** — el escenario bueno, tipo Weil), o directamente no existiría (circularidad oculta — el escenario malo)?

**[ANÁLISIS] El testigo sugiere fuertemente el escenario malo / intermedio.** Razonamiento por analogía con math/0204194:
- Si imitamos la receta, la métrica del espacio de Spec ℤ sería del tipo $g\sim e^t\,(\text{forma que usa }|\rho|\text{ o }\Re\rho)$. Bajo ¬RH, un cero $\rho$ con $\Re\rho\neq1/2$ daría un peso $e^{t}$ con exponente "equivocado" en la dirección correspondiente.
- **Escenario bueno (Weil-like):** el espacio subyacente existe igual (las órbitas $\{\log p\}$ no cambian — son los primos, no los ceros), pero la forma de polarización sobre $\bar H^1_{\mathcal F}$ deja de ser definida positiva sobre el primitivo — aparece un vector de norma negativa donde la positividad exigía positividad. Esto sería **no-circular**: la positividad falla *visiblemente en la estructura* sin necesidad de localizar el cero, satisfaciendo NC4. **Si esto ocurre, la ruta es no-circular** y el Doc 128 tendría razón.
- **Escenario malo (circular):** la métrica $e^t\mathrm{Re}(\xi\bar\eta)$ análoga NO se puede ni *definir* bajo ¬RH porque su buena definición (clase de traza, $H$-invarianza de la medida) **requiere** $|\xi|^2=q$. Sin el análogo de Hasse, el operador de traza no es clase de traza, la medida no es invariante, y el espacio Kähler–Riemann **no existe como tal**. Entonces "construir el espacio" ES "probar RH", y la no-circularidad es vacía.

**[ANÁLISIS] Cuál de los dos: la evidencia del testigo apunta al malo, pero NO es concluyente.** En math/0204194, la fuente es explícita: $|\xi|^2=q$ es *"essential to the H-invariance of the measure"* y a la clase de traza del operador $S_j(\alpha)$. Es decir: en el caso realizado, **sin Hasse el espacio Kähler–Riemann no está bien definido** (la medida no es invariante, la traza no converge). Esto es el escenario malo. PERO: (i) para curvas elípticas Hasse SIEMPRE vale, así que el caso ¬(Hasse) es contrafáctico vacío — no podemos observar qué pasaría; (ii) es concebible que para Spec ℤ exista una construcción del espacio que NO copie la receta de la métrica $e^t\mathrm{Re}(\xi\bar\eta)$ y cuya buena definición no requiera la localización. **Nadie sabe esto.** Es el [GAP] central.

> **[GAP — el hecho desconocido sobre Spec ℤ que decide todo].** ¿Existe una construcción del espacio foliado Kähler–Riemann de Spec ℤ cuya buena definición (medida invariante, clase de traza, polarización) NO requiera el análogo de $|\xi|^2=q$ (= que los ceros estén en $\Re s=1/2$)? Si SÍ ⟹ no-circular (escenario bueno). Si NO (como en el único testigo) ⟹ circular (escenario malo). **Indeterminable con lo conocido.**

### 3.3. [ANÁLISIS] La rigidez espectral (1712.04181) refuerza el sesgo a circular

**[DATO — Doc 128 §4.2, 1712.04181].** Para suspensiones/fibrados sobre $S^1$, el espectro del generador infinitesimal está **forzado por la monodromía**: $\mathrm{Sp}(\Theta\mid\bar H^i_{\mathcal F})=\{(\log\alpha+2\pi i\nu)/\log r\}$, $\alpha\in\mathrm{Sp}(\phi^*\mid H^i(S))$. El espectro de longitudes no es arbitrario.

**[ANÁLISIS] Lectura adversarial.** Si el espectro del generador (= los ceros, por el diccionario D3 de Deninger) está **forzado por la geometría/monodromía del espacio**, entonces la geometría del espacio **determina dónde están los ceros**. Hay dos lecturas:
- **Optimista (Doc 128):** la rigidez dice que el espacio es difícil de construir (no es una suspensión), pero si se construye, fuerza los ceros a su sitio — y si ese sitio es $\Re=1/2$, RH se sigue de la geometría. No-circular.
- **Adversarial (este doc):** si la geometría del espacio FUERZA el espectro a $\{$ceros$\}$ con $\Re=1/2$, entonces **construir esa geometría específica ES haber puesto RH**. La pregunta no es "¿el espectro es rígido?" sino "¿se puede construir la geometría sin saber de antemano que el espectro forzado caerá en $\Re=1/2$?". Si la única geometría que da el espectro correcto es la que ya lo coloca en la línea, es circular. **La rigidez espectral es neutral al test de circularidad por sí sola** — corta en ambas direcciones — pero combinada con §2.2 (la métrica usa la localización), inclina a circular: la geometría que fuerza el espectro correcto se construye usando la localización.

---

## 4. ¿LA POSITIVIDAD DE DENINGER ES LA MISMA QUE LA DE CONNES–CONSANI? [DATO + ANÁLISIS]

### 4.1. [DATO] Lo establecido sobre CC (Doc 124, vía Doc 127/119)

**[DATO].** La positividad de Weil de CC es **espectral**: positividad de Weil global = MW-1 = criterio de Weil = RH. Se lee evaluando la forma de Weil sobre funciones de prueba; esa evaluación = la traza del flujo de escala = la fórmula explícita (Connes 1999). **Circular: FALLA NC3** (es un ítem del catálogo de positividades RH-equivalentes) y **NC4** (en ¬RH la binariedad del índice es inaccesible sin localizar). Doc 127 lo confirmó por cuarta ruta: el flujo de escala lleva ζ adentro.

### 4.2. [ANÁLISIS] Test concreto: ¿misma forma bajo un diccionario?

El encargo pide el test concreto: ambas son "positividad de una forma asociada a la fórmula explícita"; CC sobre funciones de prueba (espectral), Deninger sobre clases de cohomología de las hojas (geométrica). ¿Misma forma o diferentes?

**[ANÁLISIS] Son objetos genuinamente diferentes — pero el mismo muro los separa de RH.**

- **Diferentes como objetos.** La forma de CC es una forma cuadrática sobre un **espacio de funciones test** $h$, evaluada como $\sum_\rho\hat h(\rho)$ (lado espectral) = $\sum_p\dots$ (lado aritmético). La forma de Deninger es la **polarización de Hodge–Riemann** $Q(\xi,J\bar\xi)$ sobre $\bar H^1_{\mathcal F}$, un espacio de **clases de cohomología leafwise**. Hay un diccionario (Doc 128 §2.4: índice de Hodge sobre el cuadrado ⟺ polarización sobre el factor) pero **NO una identidad literal**: la de CC vive en el eje del *valor/traza* (se computa evaluando contra tests = promediando = la traza), la de Deninger vive en el eje de la *inercia/signatura* (es el signo de una forma sobre un espacio de clases = individuar la partición).
- **El mismo muro (P43) los separa de RH, en ejes distintos.** Por la Obs. de P43 tras Thm. autonomy: el valor es el dato traza-like (promediado); la inercia es el dato resolución-espectral (individual). **CC ataca por el valor/traza** (y falla porque el valor es autónomo pero la traza ES la fórmula explícita = RH solo al evaluar el criterio completo — NC3). **Deninger ataca por la inercia/signatura** (y falla, en el caso realizado, porque la estructura que fija el signo — la métrica Kähler–Riemann — usa la localización de los ceros = la inercia individual). **No es "la misma forma renombrada"; es el mismo cuantificador maestro cazándolos en sus dos coordenadas.**

> **[ANÁLISIS] La respuesta precisa a "¿son la misma?".** NO son la misma forma (CC: forma sobre tests, eje valor; Deninger: polarización sobre cohomología, eje inercia). Por tanto Deninger **no es CC renombrado**, y el Doc 128 acertó en que es un objeto distinto. PERO: Deninger **no mejora la situación de circularidad**, porque ataca el lado (inercia) que P43 identifica como el NO-autónomo, y el testigo math/0204194 muestra que la estructura que da esa inercia usa RH. CC es circular por el valor/traza (NC3); Deninger es circular (o indeterminable) por la inercia/polarización (NC3/NC4 vía la métrica). **Dos circularidades distintas, mismo origen P43.** Esto es consistente con la tesis central de P43: "una pared en muchas coordenadas".

### 4.3. [ANÁLISIS] Lo que SÍ separa a Deninger de CC (y por qué importa)

Para ser justo con la ruta: hay UNA diferencia estructural real y favorable a Deninger. La positividad de CC, **incluso en principio**, no tiene un mecanismo geométrico que la genere externamente — se verifica evaluando, y evaluar = la fórmula explícita. La de Deninger **tiene un mecanismo candidato** (math/0204111: si el espacio es Kähler–Riemann, la positividad es teorema). El problema de Deninger no es "la positividad es la fórmula explícita" (eso es CC); es "el antecedente Kähler–Riemann usa la localización". **Esta diferencia importa:** la ruta de Deninger podría volverse no-circular si se exhibe una construcción del espacio Kähler–Riemann de Spec ℤ que no copie la receta de la métrica-que-usa-Hasse. Para CC no hay tal escape (la traza ES la fórmula explícita por construcción). Por eso el veredicto de Deninger es INDETERMINABLE-con-sesgo-circular, mientras el de CC es CIRCULAR-firme.

---

## 5. VEREDICTO-NC FINAL [aplicación de NC1–NC4]

Aplico R-NC (Doc 119 §4.3) a la propiedad $P$ = "la positividad de Hodge–Riemann sobre $\bar H^1_{\mathcal F}$ del espacio foliado de Spec ℤ", de la que se pretende deducir la pureza (= RH).

### 5.1. Cláusula por cláusula

- **NC1 (externalidad de la definición de $P$).** La forma de polarización $Q(\xi,J\bar\xi)$ se define con $J,\omega_{\mathcal F}$ geométricos; *dado el espacio Kähler–Riemann*, la definición de $P$ no menciona ζ. **PASA** — pero, como en el caso de CC (Doc 119 §4.3 fin) y de GAP-FOLIADO (Doc 127 §4.3), esta es la externalidad superficial: pasa NC1 todo lo que es funtorial desde el sitio. El contenido no está en NC1.

- **NC2 (sobregeneración).** ¿$P$ se prueba para una clase de objetos estrictamente mayor que la que codifica ζ, por método uniforme? El teorema math/0204111 **SÍ sobregenera**: vale para TODA foliación Kähler–Riemann, no solo la aritmética. **PASA para el implica condicional.** PERO — y esto es el matiz que NC2 exige (Doc 119: "$P$ solo verificable para el objeto específico que codifica ζ ⟹ FALLA") — la *hipótesis* "es Kähler–Riemann" en el caso aritmético realizado **solo se verifica** usando la estructura específica que codifica los autovalores (la métrica vía Hasse, §2.2). La sobregeneración del teorema abstracto no transfiere al antecedente aritmético. **NC2: PASA el teorema-marco, FALLA el antecedente-aritmético.** Réplica exacta del patrón de Doc 127 §4.3 NC2 (la curvatura sobregenera en Teichmüller; en el sitio solo tiene contenido sobre las correspondencias de ζ).

- **NC3 (no-reducción a positividades RH-equivalentes catalogadas).** ¿La verificación de $P$, restringida al objeto que codifica ζ, es equivalente a un ítem del catálogo (MW-1…MW-7, etc.)? En el caso realizado: la propiedad "el espacio es Kähler–Riemann" usa $|\xi|^2=q$ = el análogo de Hasse = el análogo de "$\Re\rho=1/2$". Para Spec ℤ, eso es **literalmente la localización de los ceros** = RH. **FALLA NC3** en el caso realizado: la propiedad geométrica $A$ (Kähler–Riemann), restringida al objeto aritmético, usa la posición de los ceros. La cadena $A\Rightarrow$ pureza tiene a $A$ como eslabón que **es** RH disfrazada de "métrica bien definida".

- **NC4 (test de los dos mundos).** En ¬RH, ¿$P$ es falsa por razón computable desde $H$ sin localizar el cuádruplo? **FALLA / INDETERMINABLE.** Por §3.2: no se sabe si bajo ¬RH el espacio existe no-Kähler (NC4 pasaría — vector de norma negativa visible) o no existe (NC4 falla — la métrica ni se define sin el análogo de Hasse, y decidir si falla requiere saber dónde está el cero). El testigo math/0204194 sugiere el segundo (la $H$-invarianza de la medida *requiere* $|\xi|^2=q$), lo que es FALLA NC4. Pero el contrafáctico ¬(Hasse) es vacío para curvas elípticas, así que no es concluyente.

### 5.2. Veredicto

> **[VEREDICTO-NC] INDETERMINABLE, con fuerte sesgo a CIRCULAR.**
>
> El implica condicional "espacio Kähler–Riemann ⟹ positividad" es **geometría genuina, externa a ζ** (math/0204111, pasa NC1/NC2 como teorema-marco) — el Doc 128 acertó EN ESO. Pero la no-circularidad de una *ruta de prueba de RH* depende del **antecedente** "el espacio de Spec ℤ es Kähler–Riemann", y ahí:
> - **FALLA NC3 en el único testigo aritmético:** la estructura Kähler–Riemann (la métrica/polarización) se construye USANDO el análogo de RH (Hasse, $|\xi|^2=q$), que para Spec ℤ es la localización de los ceros.
> - **FALLA/INDETERMINABLE NC4:** no se sabe si bajo ¬RH el espacio existe no-Kähler (no-circular) o no existe (circular); el testigo sugiere lo segundo.
>
> El Doc 128 cometió un error de inferencia: verificó que el **implica** es geométrico y concluyó que la **ruta** es no-circular, sin atacar el **antecedente**, que es donde — confirmado por fuente esta sesión — entra RH. **El veredicto (a) del Doc 128 queda revocado a INDETERMINABLE-con-sesgo-circular.**
>
> Esto es **mejor que CC** (CIRCULAR-firme por el valor/traza, sin escape): Deninger tiene un mecanismo geométrico candidato, y la circularidad podría romperse SI se exhibe una construcción del espacio que no copie la receta métrica-vía-Hasse. Pero el estándar de prueba para "no circular" es ALTO, y la ruta NO lo alcanza hoy.

### 5.3. [GAP] El enunciado mínimo a establecer para confirmar la no-circularidad

Para mover el veredicto de INDETERMINABLE a NO-CIRCULAR, hay que establecer un enunciado preciso, y NO es RH ni el espacio completo:

> **ENUNCIADO-MÍNIMO-130 (la prueba de fuego de la no-circularidad de la ruta de Deninger).** *Exhibir una construcción del espacio foliado Kähler–Riemann (o de una estructura de polarización foliada análoga) sobre Spec ℤ — o sobre el espacio de Morishita $\mathfrak X_F$ (2508.15971), que ya da el espacio subyacente + flujo + órbitas — cuya buena definición (estructura compleja leafwise $J$, forma de Kähler $\omega_{\mathcal F}$, métrica transversa bundle-like, $H$-invarianza de la medida, clase de traza del operador) **NO requiera como input el análogo de $|\xi|^2=q$**, es decir, **no presuponga que los ceros están en $\Re s=1/2$**. Equivalentemente: una métrica/polarización leafwise definida por geometría pura del solenoide aritmético, tal que la positividad de Hodge–Riemann que de ella se deriva sea un teorema que valga **cualquiera sea la posición de los ceros** — de modo que bajo ¬RH el espacio siga existiendo pero con la polarización fallando (vector de norma negativa visible, NC4-pasa), no con el espacio dejando de existir.*

**[ANÁLISIS] Por qué es la prueba de fuego correcta.** Replica exactamente la condición que hace no-circular a Weil: en $C\times C$, el índice de Hodge se prueba **antes** de y **sin** conocer los autovalores de Frobenius, y por eso RH se deriva. ENUNCIADO-MÍNIMO-130 pide la misma anterioridad: la polarización leafwise debe ser construible sin la localización. Si se logra, NC3 y NC4 pasan y la ruta es genuinamente no-circular. Si se demuestra que **toda** construcción de la métrica leafwise sobre Spec ℤ requiere el análogo de Hasse (como en math/0204194), entonces la ruta es CIRCULAR-firme y se cierra — resultado igualmente valioso (ahorra años).

**[ANÁLISIS] Predicción honesta.** Sesgo a que está cerrado / es circular, por tres convergencias: (i) el testigo realizado usa Hasse para la métrica; (ii) P43 ubica la inercia (= la polarización) como el dato NO-autónomo; (iii) la rigidez espectral (1712.04181) dice que la geometría que fuerza el espectro correcto es la que ya lo coloca. Pero NO es concluyente: nadie ha probado que toda métrica leafwise sobre Spec ℤ deba usar la localización. El [GAP] es genuino y es el primer teorema concreto a atacar en Phase 43 — y su forma negativa ("toda polarización foliada sobre Spec ℤ requiere RH como input") sería tan decisiva como la positiva.

---

## 6. Síntesis y honestidad

**[ANÁLISIS] Qué cambió respecto del Doc 128.** El Doc 128 leyó el abstract de math/0204111 y el formalismo, y concluyó (a) no-circular. Este documento leyó la **construcción de la métrica** en el caso aritmético realizado (math/0204194) y encontró que **la estructura Kähler–Riemann usa el análogo de RH (Hasse) como input**. El Doc 128 confundió la geometricidad del implica condicional ("Kähler–Riemann ⟹ positividad", verdad) con la no-circularidad de la ruta (que depende del antecedente, donde entra RH). **Veredicto revocado: (a) → INDETERMINABLE-con-sesgo-circular.**

**[ANÁLISIS] Dónde entra ζ, en una frase.** ζ entra de forma benigna en las órbitas $\{\log p\}$ (el valor, externo) y NO entra en la estructura compleja leafwise $J$ (geometría pura); pero entra de forma **fatal en la métrica/polarización Kähler–Riemann** (la inercia, el signo) — y es la métrica, no la estructura compleja, la que da la positividad. El Doc 128 vio $J$ externo y dedujo positividad externa; el salto es inválido.

**[ANÁLISIS] El milagro de Weil NO se hereda.** En Weil la positividad (índice de Hodge) es anterior y ajena a la localización de los autovalores; en Deninger-realizado la métrica que da la positividad es posterior y dependiente de ella ($|\xi|^2=q$). La flecha está invertida. La ruta de Deninger no hereda el milagro de Weil — lo necesita y no lo tiene sobre Spec ℤ.

**[ANÁLISIS] Misma forma que CC, no.** Diferente objeto (CC: forma sobre tests, eje valor; Deninger: polarización sobre cohomología, eje inercia). Pero el mismo cuantificador maestro (P43) los separa de RH en sus dos coordenadas: CC cae por el valor/traza (NC3), Deninger por la inercia/polarización (NC3/NC4 vía la métrica-Hasse). "Una pared en muchas coordenadas."

**[ANÁLISIS] El punto de máxima sospecha, resuelto en su forma condicional.** El espacio **desnudo** (espacio + flujo + órbitas) plausiblemente existe sin RH (es el valor). El espacio **Kähler–Riemann** (con la polarización de la que se deriva la positividad) plausiblemente NO existe sin RH (es la inercia, y el testigo lo confirma: sin Hasse la medida no es invariante ni la traza converge). Construir el espacio *como Kähler–Riemann* es donde se asume la localización. La "no-circularidad" del Doc 128 es vacía a menos que se separe la construcción de la polarización de la localización — ENUNCIADO-MÍNIMO-130.

**[VEREDICTO-NC final]:** **INDETERMINABLE con fuerte sesgo a CIRCULAR.** No (a) no-circular (el antecedente Kähler–Riemann usa RH en el testigo). No CIRCULAR-firme como CC (Deninger tiene un mecanismo geométrico candidato y un escape concebible). El escape es ENUNCIADO-MÍNIMO-130, duro y probablemente cerrado, pero no probado cerrado. **El estándar ALTO para "no circular" NO se alcanza; el Doc 128 declaró victoria prematuramente sin leer la construcción de la métrica.**

Ningún teorema nuevo se probó. Se **leyó en fuente** (math/0204111 hipótesis del teorema de polarización; math/0204194 construcción de la lámina y de la métrica $e^t\mathrm{Re}(\xi\bar\eta)$ con Hasse como input) y se **aplicó** R-NC con disciplina adversarial. El hallazgo decisivo: la métrica que hace Kähler–**Riemann** al único espacio aritmético realizado usa el análogo de RH como input. Eso, trasladado a Spec ℤ, es la circularidad — salvo que ENUNCIADO-MÍNIMO-130 se establezca, lo que nadie ha hecho.

---

## Referencias

**Fuente externa leída esta sesión (junio 2026, WebFetch ar5iv):**
- C. Deninger, W. Singhof, *Real polarizable Hodge structures arising from foliations*, arXiv:math/0204111 — el teorema de polarización ASUME la foliación Kähler–Riemann (forma de Kähler leafwise $\omega_{\mathcal F}$, métrica bundle-like transversa) como dato dado, y deriva Hodge–Riemann vía Álvarez López–Kordyukov + identidades de Kähler–Lefschetz, **sin ζ ni espectro**; estructura compleja $J$ pura (Newlander–Nirenberg). **[DATO — el implica condicional es geométrico.]**
- C. Deninger, *On the nature of the explicit formulas in analytic number theory — a simple example*, arXiv:math/0204194 — lámina 3-dim para curva elíptica $E/\mathbb F_q$; espacio subyacente $X=\tilde X/H$ construible incondicionalmente (Witt lift, Tate module); **PERO la métrica leafwise $g=e^t\mathrm{Re}(\xi\bar\eta)$ se define USANDO Hasse $|\xi|^2=q$**, esencial a la $H$-invarianza de la medida y a la clase de traza. **[DATO — la estructura Kähler–Riemann usa el análogo de RH como input; el milagro de Weil NO se replica.]**

**Internas (backward-only):** Doc 128 (veredicto (a) no-circular, AQUÍ REVOCADO; el implica "Kähler–Riemann ⟹ positividad"; el diccionario índice-Hodge⟺polarización; NÚCLEO-128; rigidez espectral 1712.04181; Morishita 2508.15971); Doc 127 (Forni circular, el flujo lleva ζ adentro; GAP-FOLIADO; R-NC sobre la curvatura foliada; la disyuntiva R1/R2); Doc 119 §4.3 (R-NC NC1–NC4 verbatim; el catálogo de positividades RH-equivalentes; la zona gris de suficiencia); Doc 124 (positividad de CC = espectral = MW-1 = circular; positividad-intersección [BUENA] vs positividad-espectral [CIRCULAR]); P43 (cuantificador maestro; valor autónomo / inercia no-autónoma, Thm. autonomy; "una pared en muchas coordenadas"; Principle boundary: el mecanismo faltante debe leer inercia, no valor — cohomológico sobre Spec ℤ).

*Fin del Doc 130.*
</content>
</invoke>
