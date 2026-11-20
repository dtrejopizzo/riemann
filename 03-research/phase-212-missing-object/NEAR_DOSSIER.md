# Expediente del término de casi-coincidencias (Near_M)

Reúne en un solo lugar lo que el corpus sabe y lo que intentó sobre el término
`Near_M(m,k) = ½ Σ_{n≥2, kn≠m} v_n c_0(log(kn/m))` de `𝔸_M = Arch_M − Div_M − Near_M` (Paper 47, prop:AM).
Es una compilación de lectura: no contiene resultados nuevos y las etiquetas son las de cada fuente.

Límites: varios memos se leyeron sólo en los pasajes que nombran el término (fases 199, 200 y parte de la 211);
CA_K_002, INV_V_002, INV_G_001, la fase 190 y L2_BUILD_020/023 entran en la Parte C sólo por las filas del índice
maestro. Nada fue re-derivado.

Contenido: Parte A, hechos exactos. Parte B, intentos de las fases 191–204. Parte C, intentos de las fases 161,
162, 188, 211 y 212, con el diccionario de coordenadas.

---

# Parte A — Hechos

## Expediente: el término Near_M de 𝔸_M

P47 = `04-papers/47-row-d-dual-certificates/main.tex`. Rutas de memos relativas a `03-research/`.
Donde una fuente razona del lado de ceros se marca [H].

## 1. Definiciones exactas

- **Perfil** (P47 §subsec:oneprofile, l.7759–7771): a>0, |b|>½, g(t)=e^{bt}1_{[0,a]}(t), c_g=g*g̃, G₀:=c_g*c_g, T₀:=2a,
  F₀:=(¼−∂²)G₀ ∈ 𝒫_{T₀}; F̂₀(τ)=(τ²+¼)|ĝ(τ)|⁴>0; **c₀ := c_{F₀}** (autocorrelación), ĉ₀=F̂₀². Soporte de c₀: [−2T₀,2T₀].
  Doble cero de ĉ₀ en ±i/2 ⇒ ∫c₀e^{±u/2}=0 y ∫u c₀e^{u/2}=0 (lem:transl(iii); NT_004 Thm 4.2; EI_002 Thm 3(i)).
- **Función de desfase** 𝖡(d)=𝔞(F₀,V_dF₀)=(1/2π)∫m F̂₀² cos(τd)dτ − ½Σ_{n≥2}v_n[c₀(log n−d)+c₀(log n+d)] (l.7769).
- **𝔸_M** := [𝖡(log m − log k)]_{m,k≤M} (prop:AM, l.7813, hipótesis 2T₀<log 2).
- **prop:AM(iii)** (l.7818–7826): 𝔸_M = Arch_M − Div_M − Near_M,
  Arch_M(m,k)=(1/2π)∫mF̂₀²cos(τ log(m/k))dτ; Div_M=½(𝕍_M+𝕍_Mᵀ), (𝕍_M)_{mk}=v_{m/k} si k|m, k<m;
  **Near_M(m,k)=½ Σ_{n≥2, kn≠m} v_n c₀(log(kn/m))** (m>k), v_n=2Λ(n)n^{−½};
  «suma suavizada de Λ(n)n^{−½} sobre n≠m/k en el intervalo multiplicativo (m/k·e^{−2T₀}, m/k·e^{2T₀})». Diagonales de Div y Near nulas.
- **Relación con Ξ**: Ξ_{F₀}(D):=Σ_{n≥2}v_n c₀(log n − D)=2∫_{[1,∞)}y^{−½}c₀(log y−D)d(ψ(y)−y) (thm:band, l.7712; término principal
  anulado por Tate). **(Div_M+Near_M)_{mk}=½Ξ_{F₀}(log(m/k)) para m>k** (l.7826). Equivalente: Near_M(s)=Σ s_ms_k[Ξ_{F₀}(log(m/k)) − 1_{k|m}v_{m/k}c₀(0)]
  (N_BUILD_021 Prop 1, PROVED).
- **Forma espectral** prop:AM(ii) (l.7816): sᵀ𝔸_Ms=(1/2π)∫F̂₀²|P_s|²[m(τ) − Σ_{2≤n<Me^{2T₀}}v_n cos(τ log n)]dτ, P_s=Σs_m m^{iτ}.

## 2. Hechos sobre Near

**Estructura**
1. Descomposición y forma Toeplitz-en-log: Div+Near es la muestra en {log m − log k} de la función ½Ξ_{F₀} de una variable; Near = esa muestra menos las coincidencias exactas n=m/k. PROVED (P47 prop:AM(iii), l.7818–7826; (S) l.10712–10717).
2. Soporte: para m>k, contribuyen sólo n con |log(kn/m)|<2T₀, n≠m/k; el término c₀(log n + log(m/k)) se anula porque log n ≥ log 2 > 2T₀. PROVED (prop:AM, prueba (iii), l.7834–7836).
3. Inevitabilidad: con F₀ fijo, hay casi-coincidencias para todo M grande (gaps de log m ~1/m < 2T₀). PROVED/afirmado (P47 l.7842–7843; L2_BUILD_028 §2(b)).
4. Forma por desplazamiento aditivo h=m−kn: sᵀW₁Vs=Σ_hΣ_{m−kn=h}s_ms_kv_nc₀(−log(1−h/m)); h=0 ↔ Div, h≠0 ↔ Near; |h|≤(e^{2T₀}−1)m. PROVED (L2_BUILD_030 §1(c)). Nota: la frase «número acotado de h ∈[−c,c]» vale sólo en el régimen 2T₀=c/M, no con T₀ fijo (ver §4).
5. Near no tiene signo propio: es el resto de resolución finita del producto |P_s|²·V(τ); W₁=[c₀(log m/k)]⪰0, V triangular, W₁V sin signo. PROVED (L2_BUILD_030 §2).
6. Lado aritmético: para (m,k) fijo, Near es un conteo suavizado de primos en intervalo multiplicativo de ancho relativo fijo e^{±2T₀} (no corto aditivamente), menos n=m/k. PROVED (N_BUILD_021 Prop 1).
7. Dualidad: Poisson en ℤ² del suma de átomo n devuelve casi-coincidencias duales −ℓ₂≈ℓ₁n (precisión e^{±2T₀}); Poisson ℤ² mapea (S) en sí mismo, no diagonaliza Near ni lo separa de Arch. PROVED (phase-192 EI_002 Thm 3(ii), l.60–63).
8. Bohr: en el toro con fases independientes sólo Div es diagonal; Near y Arch viven en la diagonal θ_p=θ log p; la multiplicatividad no diagonaliza 𝔸_M. NO-GO PROVED (L2_BUILD_028 §2(c); N_BUILD_022 §4).
9. Métrica de altura: casi-coincidencia = r=m/k cerca de n con altura grande, defecto h−ℓ=2 log den; el «damping por denominador» vale 1 en Div y suprime Near. PROVED (phase-189 NT_001 Prop 2.1 y lectura, l.45–59). Conteo: #{a≠nb: |log(a/nb)|≤2T₀} ≤ 2nb(e^{2T₀}−1) (NT_001_004_REVIEW l.32, CONFIRMED; requiere T₀≤T_abs).

**Dónde es invisible y dónde se ve**
10. prop:nearfree (P47 l.7642–7669): sobre resonadores F_b de ancho ε_M=1/(8KM(2+log M)) y T≥½log M+ε_M, 𝔞_T(F_b) ≥ c₀‖F_b‖² (aquí c₀ es una constante, no la autocorrelación). PROVED. Ahí no hay casi-coincidencias: el peine es sólo 𝔻 (divisibilidad), cota de Schur ≤ (log M+E)‖F_b‖² vía Σ_{d|m}Λ(d)=log m; el arquimediano da log(1/ε). Nota: usa perfil de ancho ~1/M, no F₀ fijo.
11. rem:boxes (l.7660–7669): en cajas multiplicativas 𝔻 es suma de Kronecker de Toeplitz de un primo, símbolo 2log p·Re x/(1−x), rango [−2log p/(√p+1), 2log p/(√p−1)]. PROVED. «Los tests sin casi-coincidencias visibles no llevan información del signo más allá de eso»: barrera.
12. Conjuntos multiplicativos Near-free (2T₀<e^{−2L}/2): Near=0, 𝔸|_S = a₀I − ⊕D_i + E; ζ pasa trivialmente porque la separación compra energía ≈2L. PROVED (§1–2), a₀≈log(1/T₀) ARGUED (L2_BUILD_029 §§1–3). Veredicto: el signo debe involucrar Near.
13. Test m^{−½} con resolución sin solapes (ε=θ/M): Near=0, Q(M)=(γ+C_χ+log(1/θ))log M+o(log M). Mertens CITED, asintótica arquimediana ARGUED (L2_BUILD_028 §3).
14. Vectores que ven Near: la positividad debe decidirse en ellos (P47 l.7842–7844; rem:bar-arith l.8532–8536: no excluido «𝖡 PD en vectores que ven Near_M»). OPEN.
15. Vectores torcidos s_m=χ(m)u_m: Div → convolución por χ(n)v_n, Arch queda el de ζ, Near lleva fases χ(m)χ̄(k) con m≠kn (no χ(n)): híbrido, no la forma de L(s,χ). PROVED (N_BUILD_021 Prop 3; P47 l.8394–8398). Estadísticas de progresiones entran sólo vía Near correlacionado con clases de residuos.
16. Clases de progresión (SW, BV, BDH, Brun–Titchmarsh) como propiedades de clase: cerradas bajo borrado/amplificación finita ⇒ no prueban (N_BUILD_021 Thm 2, PROVED; P47 prop:prog).
17. Subespacios restringidos (R_Q rugoso, B_Q balance de residuos): equivalentes al objetivo completo, no más débiles (L2_BUILD_031 Thm E, PROVED). La supresión de componentes p^b≤Q de §3–§4 está CORREGIDA como inválida (aviso al inicio del memo: contraejemplo M=Q=2, s=(1,1)).

**Identidades exactas que lo tocan / que no lo alcanzan**
18. Identidad divisora Δ=Z⁻¹LZ−L (ZΔ=[L,Z], 1*Λ=log matricial); espectro de Δ+L = {log m}. PROVED (= R162_903 B2.1). Normalización: Div_M = 2D_sym (corrección registrada en el memo). (N_BUILD_022 §§1–2.)
19. **NO-GO**: X_M=[Ξ(log m−log k)] = Z⁻¹Ł_M + 𝒟_M, con 𝒟_M = contribución de no-divisores = Near; 𝒟_M=0 sse Near=0. Ninguna identidad matricial exacta derivada de 1*Λ=log relaciona X_M con L y Δ más allá de la parte divisora. NO-GO PROVED; índice exacto de 𝒟_M ARGUED (N_BUILD_022 §3 y self-review 4).
20. Colapso central (NT_004 Thm 4.1, PROVED/CONFIRMED): en tests de Euler s_a=χ(a)a^{−½}, la suma en b es completa (b≤j/2<N) y la forma es exacta con casi-coincidencias conservadas: comb = 2Re ΣΣ χ(a)χ̄(j)(aj)^{−½}g_χ(j)c₀(log a−log j), g_χ=(Λχ)*1. Casi-coincidencias multiplicativas → aditivas (j=bn≈a); Prop 4.4: correlaciones χ(a)χ̄(a+h)g_χ(a+h), |h|≤2.5T₀a (identidad PROVED, lectura ARGUED; requiere T₀≤T_abs).
21. χ=1: parte de peine (Div+Near) acotada O(1) uniformemente en N (doble cero de Tate + Euler–Maclaurin). PROVED (NT_004 Thm 4.2). 𝔞(G_N^1)=c_A N+O(√N), c_A>0 «PROVED up to routine bookkeeping» (Thm 4.3; Titchmarsh 4.11 CITED). NO-GO 4.5 como portador de signo.
22. Identidad de balance en red (C3): para s=m^{−½}, sᵀ(Div+Near)s = 2Σ_N N^{−½} log N·E_M(N), E_M(N)=Σ_{m≤M}m^{−½}c₀(log(N/m)). PROVED (elemental, clase W7: uso lineal de Λ*1=log, sin signo); comprobada a 12 dígitos (1.985815103517, M=800). Decaimiento de E_M(N): ARGUED (Euler–Maclaurin). (phase-190 EXP_003 §4, EXP_005 C3.)
23. Familia s_w=m^{−½}w(m/M) (P47 prop:shape-family, l.9008–9045, (i)–(iii) PROVED, crecimiento de ζ CITED): colapso sᵀ𝔸s = sᵀArch s − Σ_{N<Me^{2T₀}}N^{−½}D_w(N)E_w(N); el peine entra sólo vía Σ_{d|N}Λ(d)=log N y Λ(d), d<e^{2T₀}/η. (iv): Ψ_w es el análogo continuo del átomo n de Div+Near; se anula a segundo orden, ∫Ψ_w=0. EI_002 Thm 3(iii): «Div ≈ −Near» PROVED como identidad; quedan término de borde (escala M), defectos de divisores pequeños y términos duales.
24. Variante EI_003 Thm 2 «ninguna identidad hace el símbolo no lineal en Λ»: RECHAZADA por la revisión como tautología (σ_T es afín en Λ por definición) (PHASE_192_REVIEW_SUMMARY l.17, 33; EI_003_REVIEW l.6, 16).

**Controles** (phase-190, NUMÉRICO, doble precisión, T₀∈{0.05,0.15,0.3}, b=1)
25. Λ: 𝔸_M ⪰ 0 en todo M≤3000 calculado; λ_min = M^{−3+o(1)} (exponente local 2.89→2.98). (EXP_003 §1, Fact N1.)
26. Borrado a₃, a₅: indefinidos ya en M=50 (λ_min −1.5, −2.4) y creciendo ~ −M (−42, −54 en M=1500). (EXP_002 §1.)
27. Peso perturbado v₂(1±10⁻⁵): indefinido desde M≈200–400; ±10⁻²: desde M=50. Umbral de amplificación c*(M) ≍ λ_min/0.18 ≍ M^{−3}; ∂λ_min/∂v₂ = O(1). (EXP_002 §§1–2.)
28. Beurling (q=p e^{ε_p}, ε_p∈±0.02): indefinido en M=50 (−1.5) en la red entera y en la propia. Poisson: −3…−237. (EXP_002 §1.)
29. Fallo de controles: autovector = paquete suave de enteros consecutivos en la escala superior (pico ≈0.15–0.25M); Div≈0, Near ≈ Arch + |λ| («Near excede a Arch»). Ej. pert₂(+10⁻⁵), M=1500: Arch 120.12, Div 0.60, Near 119.52, λ=−7.9·10⁻⁴. Near_n en M=800: n=2 +41.9, 3 +27.9, 4 +10.5, 5 −14.1. (EXP_002 §§3–4.)
30. Banda 2×2 (necesaria): mata Poisson, Beurling (T₀=0.3), a₅; a₃, amp2(0.05), pert₂(1.01) la pasan hasta d=15 siendo indefinidos. Λ: sup|𝖡|/a₀ = 0.942 en d=12.69 (T₀=0.3). (EXP_002 §5.)

**Datos numéricos de Near para Λ** (NUMÉRICO)
31. En el minimizador (≈ m^{−½}·w(m/M), solapamiento 0.993, entradas positivas): Div(v)≈log M+0.4, Near(v)≈−Div(v)+Arch(v)−λ; p.ej. M=800: Arch 0.322, Div 6.032, Near −5.709. (EXP_003 §3; EXP_005 §5.)
32. Por átomo (M=800): todo n≥5 cancela su parte divisora a 3 decimales; defectos δ_n=Near_n+Div_n: n=2 +0.169, 3 +0.120, 4 +0.027; Σδ_n = Arch−λ. Mecanismo (suma de Riemann de integral anulada por Tate) PROVED-elemental, no específico de ζ. E_M(2,3,4)=0.778, 0.636, 0.287; |E_M(N)|≤2·10⁻⁶ para 50≤N≤400. (EXP_003 §4.)
33. Matriz: ‖Near‖_op ≈ 0.17M (T₀=0.3), 0.087M (0.15); indefinida, rango pleno; autovalores −517…+312 (M=3000); 56.5 % de entradas positivas; Σ entradas −2786 vs Σ|·| 4.5·10⁵ (M=2000); masa ∝ Λ(n)n^{−3/2}M², n=2,3,5 llevan 45 %; autovectores principales ortogonales (≤2.7·10⁻⁴) al espacio negativo de Arch. Todas estas estadísticas coinciden a 5 dígitos con las perturbaciones 10⁻⁵ ⇒ no específicas. (EXP_003 §5; EXP_005 R11.)
34. Masa por desplazamiento h plana (h=±1: 4.61, ±2: 3.90, ±3: 3.42) para Λ y controles: h no separa. (EXP_003 §4; EXP_002 §4.)
35. Mecanismo del minimizador: P_v se anula en las ordenadas [H] (EXP_003 Fact N2; EXP_005 C2) — clasificado por la fuente como observación del lado de ceros, no insumo del lado de primos.
36. Conclusión de la fuente: ningún hecho estructural del lado de primos sobre Near vale para Λ y falla en todos los controles (EXP_005 §0; README phase-190).

## 3. Preguntas abiertas explícitas
- (S): Arch_M − Div_M − Near_M ⪰ 0 ∀M (P47 l.10707–10717). OPEN.
- Control conjunto de Near con Arch en vectores que ven casi-coincidencias (rem:bar-arith l.8532–8536; EXP_005 §4 nota R9). OPEN.
- C1 ley de criticidad λ_min=M^{−3+o(1)}; C2 ley del minimizador (NUMÉRICO; ruta sólo [H]). (EXP_005 §2.)
- Término de borde de Q_M(w) en N≈M: ¿tamaño de error de PNT o del margen M^{−3}? Paso siguiente propuesto, no hecho (EXP_005 §6; EI_002 Thm 3(iii)(a) «not estimated here»).
- Fila 18 del mapa (conductor >1) como fuente de falsificador: UNKNOWN; otras rutas no excluidas (N_BUILD_021 §3).
- Índice exacto de 𝒟_M en N_BUILD_022 §3: ARGUED.
- «Balance mata exactamente las componentes q=p^b» más allá de primer orden: ARGUED, y luego corregido como inválido (L2_BUILD_031).

## 4. Tensiones / contradicciones entre fuentes
- L2_BUILD_030 §1(c) «Near es suma sobre un número acotado de h∈[−c,c]» supone 2T₀=c/M; con T₀ fijo (P47 prop:AM) |h|≲2T₀m, no acotado. No es error lógico, pero el régimen difiere del paper.
- prop:nearfree (P47) trata resonadores de ancho ~1/M, no el perfil F₀ fijo de prop:AM; P47 l.7842 lo cita como «tests en que Near es invisible».
- N_BUILD_022 §2 D_sym ≠ Div_M (factor 2) — corregido dentro del memo.
- L2_BUILD_031 §3–§4 (supresión de componentes p^b≤Q) invalidado por aviso posterior; Thm E intacto.
- EI_003 Thm 2 / README phase-192 («PROVED impossible») vs revisión (rechazado como tautología).
- NT_002/NT_004 cotas «≤5T₀», «≤2.5T₀» necesitan T₀≤T_abs, no sólo 2T₀<log 2 (NT_001_004_REVIEW l.70).
- Ninguna contradicción numérica detectada: 𝔞(G_N^1)=c_A N (NT_004) es compatible con el cociente de Rayleigh creciente de m^{−½} en EXP_003 §2 (0.06→0.50, M=100→1200).

---

# Parte B — Intentos, fases 191–204

## Inventario de intentos sobre Near_M (fases 191–204)

Objeto: 𝔸_M = Arch_M − Div_M − Near_M (P47 prop:AM), Near_M(m,k) = ½ Σ_{n≥2, kn≠m} v_n c₀(log(kn/m)).
Etiquetas copiadas de la fuente o de su auditoría. «[H]» indica que la fuente razona del lado de los ceros o usa una equivalencia; ese razonamiento no se usa aquí.
Alcance: se leyeron los pasajes de cada memo que contienen Near o casi-coincidencia (grep y contexto), además de las síntesis y auditorías. No se leyeron completos todos los memos de 199/proof-L-sharp ni de 200 que sólo citan Near de pasada. Índice: ROUTES-MASTER-INDEX.md l.102, 135, 207–213, 272–310, 4397, 5770–5775, 5833, 5875, 5916, 5922, 7027, 7086, 7162, 8825–8836, 9016–9019, 9093–9119, 9255, 9278.

## Familia 1. Reescrituras exactas (coordenadas)

| id / archivo | operación sobre Near | resultado / etiqueta | motivo exacto del fracaso | qué sobrevivió |
|---|---|---|---|---|
| CA_C_002 Prop 2(c),(d) (193) | Near_M = (μ_line∘ι⁻¹ − Haar)(Σ_p δ_p·\|P_s\|²) en cajas 𝕋^S | PROVED; revisión: «coordenada, no mecanismo» (CA_C_002 l.90) | Requiere que todo átomo de casi-coincidencia sea S-unidad (hipótesis de (c)); la identidad es lineal en Λ y no fija ningún signo | Identidad «defecto de Hasse» = Near; se anula en tests sin casi-coincidencias visibles |
| CA_H_002 Thm 3.1/3.2 (193) | Extensión a Ĝ: Div = ∫g_s dHaar, Div+Near = ∫g_s dν₀; sᵀ𝔸s = Σ_q[α(log q)N_s(q) − c₀(log q)M_s(q)] | PROVED, REF-D (Cor 3.5) | «anatomy is (additive weight) × (monoid coefficient), linear in Λ, (B″)»; el contenido de signo es (K) = la afirmación misma | H-K, H-T: la masa de la recta más allá de la frecuencia de Nyquist entera M es ≍ M⁻³ (PROVED) |
| CA_M_001 Prop 1.1 (193) | Forma en sitios primos: Q = Arch − Near, Near = Σ_h C_s(h) (correlaciones de Chen p ~ p′q^a, todos los desplazamientos \|h\| ≲ 2T₀p) | PROVED | No codifica pares de primos a desplazamiento fijo; sólo el primer momento en h; el signo no queda determinado | Forma exacta; Div ≡ 0 en sitios primos |
| CA_K_002 Thm 3.2/Cor 3.3 (193) | Independencia de sitios: meta ⟺ Arch(s) ≥ Near(s) ∀ s en sitios primos ∀M | PROVED como reformulación; REF-D. Índice l.5922 | Es la misma desigualdad; Cor 3.3(iii): bajo la premisa todo el déficit lo paga Near (p ≈ np′) | Reducción limpia «Arch ≥ Near» (TRACT_D l.296 la toma como forma canónica de G8) |
| fase 190, identidad C3 (índice l.5775) | sᵀ(Div+Near)s = 2Σ_N N^{−½}log N·E_M(N) sobre s = m^{−½} | PROVED (clase W7) | el balance se da sólo por defectos N = 2, 3, 4; los átomos n ≥ 5 cancelan su Div (suma de Riemann común a todo peine) | identidad |
| INV_V_002 Thm V2.1 (196) | Forma afín 𝔄ff_T (desplazamientos 0<\|a\|<e^T(1+1/n)): 𝔞_T = A_∞ + ½𝔄ff − ½Re⟨Vf,f⟩_Ш | PROVED, no diagonal; (G2) REF-D tautológico (AUDIT_196 l.53) | 𝔄ff = 2(𝔞_T − A_∞) + Re⟨Vf,f⟩_Ш idénticamente; lineal en el peine (Prop V2.2(d)) | Split exacto; V2.2(c) FALSO (vale para todo retículo αℤ) |
| CA_B_007 / CA_B_008 (193) | Gap de concavidad Γ = desalineación entre el minimizador arquimediano y el minimizador de las casi-coincidencias | EXCLUDED (REF-D + (B″) + (R)(5)) | Γ es un solapamiento ⟨h₁,h₂⟩ más dos gaps: observable de ventana (R)(5); la cota Γ ≥ m(1−\|c\|) es fina sólo con dos modos bajos, y la arena tiene ≥ 12 | Thm 1 (cota de ángulo entre dos minimizadores) PROVED como coordenada |
| PROOF_L_SHARP_GG_001 / II_001 (199) | Renormalización: conjunto de acoplamiento = casi-coincidencias nN ≈ N′ (exacto); pares cercanos N′/N ∈ (μ⁻¹, μ) | PROVED (identidades lineales); sin signo | el conjunto de pares no es finito; queda la autocorrelación local de g (identidad lineal W_T(g) = …) | descomposición radical de la recta completa |

## Familia 2. Aritmética de los sitios (paridad, residuos, criba, series singulares)

| id / archivo | operación | resultado / etiqueta | motivo exacto | sobrevive |
|---|---|---|---|---|
| CA_M_001 §1.2, Thm 3.1/Cor 3.2, Prop 3.3 (193) | Partir Near por paridad/residuos de p − np′; Chen, HL, criba | NO (PROVED: «integrality invisible») | Near^{h impar} = Near_{q=2}; cada Near_q tiene traza 0 y es indefinido; el enunciado ∀M equivale al mismo con sitios reales p+θ_p, θ_p ℚ-independientes (ninguna diferencia x − nx′ es entera); en las configuraciones decisivas h → ∞ y los desplazamientos acotados tienen peso 0 | M-S, M-I, M-P (PROVED) |
| CA_M_000 M4 (193) | Pesos de criba de Selberg / b_θ como cotas de Near | DISCARD (pre-screen) | W-sieve: b_θ ≥ 0, b_θ ≤ Λ refuta toda cadena de cotas superiores (R167_102); NG-A4: una criba no puede ponderar Λ por debajo | — |
| CA_M_000 M5 (193) | Promedios de series singulares (Gallagher, Montgomery–Soundararajan) para evaluar Near | DISCARD | input conjetural; desajuste de resolución: Near ve h a escala T₀p, los h acotados tienen densidad 0 | — |
| SPEC_SIGN_OBJECT_002 Q3 (200) + AUDIT_200_SPEC_002 | Serie singular exacta 𝔖_n(h) de N′ = nN + h vía sumas de Ramanujan; Bochner en ℤ | DOUBTFUL tendiendo a NO-GO | 𝔖_1 es PD trivialmente (autocorrelación media de cualquier sucesión, Herglotz); los pesos ∫w_{n,h} vienen de c_g∗ν con ν de signo indefinido (m < 0 para \|t\| < 6.29, átomos −v_n), así que no son de tipo positivo en h; todo el contenido queda en 𝔈_Poisson en el borde N ≈ μ (C6); falsificador cΛ, c > 1, deja 𝔖_n intacto | fórmula cerrada de 𝔖_n(h) (Lemma Q3.1, verdadera); 𝔖_1(1) = −0.040360 (NUMÉRICO) |

## Familia 3. Estadística y espectro de la matriz Near

| id / archivo | operación | resultado / etiqueta | motivo exacto | sobrevive |
|---|---|---|---|---|
| fase 190 (índice l.5774, 8825–8836) | Estadística y espectro de Near como huella | NUMÉRICO; NO-GO por [sens] | estadísticas idénticas a 5 dígitos bajo una perturbación de 1e−5 del peine; el minimizador es la suma parcial suavizada [H] | norma ≈ 0.17M, rango completo, 56 % de entradas positivas (NUMÉRICO); λ_min(A_M) ≍ M^{−3+o(1)} |
| SPEC_SIGN_OBJECT_007 C1 (200) | Espectro o componentes del grafo de casi-coincidencias 𝔐_T a resolución π/T | NO-GO (PROVED, dado Lemma E certificado) | el soporte del peine falsificador de Lemma E contiene el de ζ; todo invariante monótono del soporte que certifica ζ certifica también esa forma en T ≥ 1.59, donde vale [−0.0599398587, −0.0599398456]. Lema A.0: Baker es más débil que la separación \|log(m/n)\| ≥ ½e^{−2T} | registro «Do not retry: … near-coincidence matrices or spectra» |
| CA_C_006 E1 (193) | Pila–Wilkie / o-minimalidad: los pares peligrosos están en un conjunto de parte trascendente chica | NO-GO como mecanismo | el conjunto de casi-coincidencias es semialgebraico (ARGUED), Pila–Wilkie no actúa; las cotas superiores de conteo son B′; conteos ponderados por peine positivo son genéricos en signo (B″) | — |
| CA_C_006 E2 (193) | Libertad / probabilidad libre entre Arch y Div+Near | DISCARD | ambos son compresiones de operadores de convolución sobre ℚ^×_{>0} y conmutan (la libertad exige τ((a−τa)(b−τb)(a−τa)(b−τb)) = 0, pero con conmutación da τ((a−τa)²(b−τb)²) > 0); además, aunque hubiera libertad, λ_min ≍ M⁻³ tiene peso O(1/H(M)) en τ_M, y una perturbación de rango uno (O5) no cambia los momentos límite pero puede volver negativo el fondo | — |
| AUDIT_201_SPEC_001 B-V1 (201) | Bloque ε = ±1 = matriz de casi-coincidencias m = kn ± 1 (rango no negativo) | NO-GO CONDITIONAL (rama 2 + C-emb (a)) | el umbral κ_∞ compara v_n con una pieza arquimediana elegida a mano: lista finita de comparaciones; además repite el «do not retry» de SPEC_007 | — |

## Familia 4. Interpolación / deformación de Near

| id / archivo | operación | resultado / etiqueta | motivo exacto | sobrevive |
|---|---|---|---|---|
| CA_K_002 Prop 3.1 (193) (semilla K10) | Q_t = Arch − Div − Near∘E_t con multiplicador de Schur gaussiano e^{−tℓ(q)} (flujo de la recta a Haar) | NO-GO para la interpolación determinista; REF-D | ∂_tQ_t es peso aditivo × coeficiente del monoide, lineal en Λ (falla P2); el signo del camino es un enunciado sobre el minimizador (Thm 1.2); Cor 3.3(ii): NO-GO PROVED para el extremo Haar | Prop 2.1: λ_min(𝔸∘K_μ) ≥ λ_min(𝔸), es decir que promediar acota por arriba (dirección equivocada) |
| P211-3B (índice l.9776) | 𝔸_M = 𝕏∘𝕂_t + ℝ, multiplicador de Schur gcd | NO-GO | la existencia de la descomposición ⟺ 𝔸_M ⪰ 0 (reformulación) | — |

## Familia 5. Reescritura como h⁰ / pares / hipérbola (absorber Near en otro objeto)

| id / archivo | operación | resultado / etiqueta | motivo exacto | sobrevive |
|---|---|---|---|---|
| INV_C_001 (194) | h⁰ fuera de la diagonal multiplicativa (pares coprimos a/b) | Thm 4 PROVED; (Q3) REF-D | ninguna medida sobre log ℚ_{>0} iguala 𝔞_T en 𝒫_T, así que la identidad sólo vale en el límite, y ese límite es Arch − Near; «h⁰_off ≥ h⁰_diag en el límite» es W ≥ 0 reformulado; la tasa Farey es irrelevante porque hace falta el límite, no la tasa | Lemas 1–3, Thm 4, Identidad 5 |
| INV_B_002 (194) | Efectividad de h⁰ en el lugar de las casi-coincidencias | OPEN, mal planteado (AUDIT_194 l.43) | quitar los pares de razón potencia de primo destruye la estructura de Gram; la parte de intersección finita es ≤ 0 para F efectivo (PROVED) | — |
| INV_G_001 Thm G1 (194) | Término de balance Σ min(d,n/d); kernel PD e^{−\|u\|/2} | NO-GO en clase 𝓒_G, CONDITIONAL en el chequeo Beurling (AUDIT_194_2) | todo ingrediente es Beurling-genérico (B″); la parte positiva ∫F e^{−\|u\|/2} = Near; «Arch_T − Near-comb ≥ 0» es 𝔞_T ≥ 0 | D_M = Σ_k ζ_{≥k}(s)² (identidad PROVED) |
| INV_D_001 (194), TRACT_D l.391 | defecto renormalizado − peine ≥ 0 | TRANSFER | ‖ω_+‖²_HS ≥ 0 no ve el peine | — |
| INV_J_001 (194), Cor J4 | acoplamiento FE = Near | primera mitad PROVED; «= Near ⇒ REF-D» ARGUED | J2: Gram/Bochner da la dirección equivocada; MV/criba sólo dan cotas superiores | — |

## Familia 6. Transferencia / identidad desde Λ∗1 = log

| id / archivo | operación | resultado / etiqueta | motivo exacto | sobrevive |
|---|---|---|---|---|
| N_BUILD_022 (188), citado en INV_I_001 y SPEC_B | Identidad matricial exacta desde 1∗Λ = log más allá de los divisores | NO-GO (06_OPEN_RESIDUES) | ZΔ = [L,Z] exacto; Near aparece como **defecto de discretización** | identidad conmutador |
| INV_V_002 Thm V2.3/V2.4 (196) | Transferencia Hecke–Chebyshev V*Ш = 2log\|x\|·Ш para levantar a núcleo hermítico positivo | V2.4 PROVED (rigidez); NO-GO | Chebyshev es un enunciado sobre un solo vector (Ш); todo núcleo hermítico del retículo que admita la transferencia exacta es constante en la variable transferida; (G1) «eigen-núcleos aproximados» cae en N_018 ∪ I4 (ARGUED) | la relación específica de Λ vive sólo en la distribución de rango uno Ш |
| L2_BUILD_030 (188), fila muerta R9 | Near como operador firmado por separado | NO-GO (fila muerta R9) | — (citado en SPEC_B l.160 como entrada, no retomado aquí) | — |
| SPEC_B T*₃ / C*₃ (191) | Colapso por divisores D_w(N) = 2c log N − defectos; Poisson en ℤ: casi-coincidencias = frecuencias duales no nulas | C*₃ OPEN; REF-D para η ≤ η₀ ≈ 0.3–0.4 (NUMÉRICO); para η > η₀ es condición necesaria | el peine sólo sobrevive en n < e^{2T₀}/η; para η → 0, ψ − y reentra por los defectos de divisor a escala M y resulta inútil a precisión M⁻³; T*₃ es NUMÉRICO-falso para modificaciones finitas | «EXP_005 §6 names the bulk/edge split of Q_M(w) as the next step and it has not been done» |
| SPEC_A (191) | Inducción exacta por contactos | O6 ARGUED / (θ) FAIL | «no line of the specification uses that the lags are log ℕ»: las casi-coincidencias aparecen como datos, sin especificar | — |
| P211-A (índice l.7312) | Media de las casi-coincidencias a lo largo de s_w: Q_M = M·𝒜(w) + pequeño | NO-GO (transferencia red→continuo); descomposición PROVED | — | borde superpolinomialmente pequeño |

## Familia 7. Dominación Arch ≥ Near (cota directa)

| id / archivo | operación | resultado / etiqueta | motivo exacto | sobrevive |
|---|---|---|---|---|
| TRACT_D G8 (204), WEAKEN_001 l.78, FINAL_204 #40 | Schoenberg/Bochner sobre sitios; dominación término a término | TRANSFER; «OPEN with no sign (not weakened, just separated)» | «Missing hypothesis: the inequality itself»; la dominación término a término está excluida por thm:band/Thm T/Thm L: cada sección 2×2 es la banda \|Ξ(d)\| ≤ 2a₀ y Ξ oscila en torno a 0 (no hay signo término a término) | residuos l.391/415 «attackable without a sign» |
| CA_M_001 Prop 4.3 (193) | Lo que deben pagar las casi-coincidencias en sitios primos (Fejér) | ARGUED; necesario bajo la premisa; REF-D | condición de Cesàro sobre Ξ, en la clase Thm Z [H] | — |
| CA_M M-R (193) | Inversión antidiamagnética | PROVED (identidad FE-genérica) | m(τ) + 2Re(ζ′/ζ)(½+iτ) ≡ 0: los primos cancelan C₀ con holgura cero; lo que lleva la positividad no es una densidad a.c. [H] | — |

## (a) Motivos de fracaso agrupados

1. **Linealidad en Λ / genericidad de peine (B″, O7).** CA_C_002, CA_H_002, CA_M parity, CA_K_002, INV_G, INV_V_002 V2.2(d), CA_C_006 E1, fase 190 C3. Toda identidad exacta para Near es (peso aditivo en log q) × (coeficiente del monoide), lineal en Λ, y vale igual para Beurling, cΛ y a_P.
2. **Reformulación (REF-D).** Cualquier forma cerrada «Arch ≥ Near» (CA_K_002, INV_C Q3, INV_G, INV_V G2, P211-3B, TRACT_D G8) es la misma desigualdad.
3. **Integralidad invisible (independencia de sitios).** CA_M Thm 3.1/Cor 3.2 y Prop 3.3: paridad, residuos, criba y series singulares no existen en la clase decisiva (h → ∞).
4. **Dependencia sólo del soporte o de la estadística ([sens], falsificador de Lemma E, O5 rango uno).** Fase 190, SPEC_007 C1, CA_C_006 E2.
5. **Dirección equivocada (Gram/Bochner/promedios dan cotas superiores de λ_min).** CA_K_002 Prop 2.1, INV_J J2, Q3 (pesos no de tipo positivo).
6. **Rango uno de Chebyshev (no hay levantamiento hermítico).** INV_V_002 V2.4 y N_022 (Near = defecto de discretización).
7. **Observable de ventana (R)(5) / precisión M⁻³.** CA_B_008, CA_C_006 [crit], SPEC_B (ψ − y inútil a M⁻³).

Distintos de verdad: unos 4. Los motivos 1, 2 y 5 son la misma obstrucción: una identidad lineal o una cota de Bochner no fija el signo, y cerrar la desigualdad la reformula. El 3 (sitios reales) es independiente. El 4 se reduce a 1 vía falsificadores. El 6 es estructural y distinto. El 7 es la escala M⁻³ del fondo y también es distinto.

## (b) Operaciones que las fuentes señalan como no ejecutadas

- **Corte bulk/edge de Q_M(w)** (SPEC_B l.160–161: «EXP_005 §6 names the bulk/edge split … has not been done»). La contabilidad de Euler–Maclaurin/Poisson del término principal tampoco está escrita (SPEC_B tabla: «not written out; ARGUED»).
- **Prueba de 𝓕_T ≤ 𝔞^♯ con el vector y la forma arquimediana juntos sobre vectores que ven Near_M** (P47 rem:bar-arith; índice B.3 #38, «terreno declarado no excluido»).
- **Positividad de Hadamard/Schur que acople primos distintos con m ≈ kn; bloque positivo no Gram con fuente propia** (índice B.3 #30, sin objeto escrito).
- **Restricción conjunta entre primos (requiere identidad nueva)** y **álgebra tipo Hecke con multiplicadores arquimedianos** (índice B.2 #28, «sin candidato»).
- **Término de grado ≥ 2 en el peso que se anule en Λ; W soportado en m ≈ kn; cierre de {𝔸_M} bajo Schur con peso transformado** (índice B.2 #27).
- **Eigen-núcleos de Chebyshev aproximados con cota no Cauchy–Schwarz de 𝔄ff** (INV_V_002 §3 (G1); AUDIT_196: «not worth pursuing unless a concrete non-CS bound on 𝔄ff is named»).
- **Residuos l.391/415 de G8 «attackable without a sign»** (WEAKEN_001, TRACT_D): separados, no atacados.
- **Test de asimetría 𝔖_2(h) vs 𝔖_2(−h)** (AUDIT_200_SPEC_002: «cheap and worth running as data, not as a route»).
- **Reflexión tipo OS a través de log m ≈ log(kn)** (LEDGER_L1 l.99, l.144): propuesta como candidata, con la diferencia frente a INV_V_002 pendiente.

## (c) Resultados positivos parciales sobre Near

- **prop:nearfree / rem:boxes (P47, PROVED; índice l.135):** positividad con margen c₀ para todo b en el perfil resonador ε ≍ 1/M. Allí las casi-coincidencias son invisibles y Near no contribuye.
- **CA_C_002 (d):** en tests sin casi-coincidencias visibles el defecto de Hasse se anula y la positividad vale con margen.
- **Ventanas chicas:** con 2T₀ < log 2 y T₀ ≤ 0.3, D ya es Theorem A (TRACT_D: «l.55/135 … already Theorem A»). En sitios primos Div ≡ 0, pero el resultado no firma Near por sí solo.
- **Escala:** la masa de la recta de Kronecker más allá de la frecuencia M es ≍ M⁻³ (H-T, PROVED), igual al orden de λ_min (NUMÉRICO).
- **Identidad C3:** el balance contra Arch depende sólo de los defectos N = 2, 3, 4; los átomos n ≥ 5 cancelan su Div (PROVED, clase W7).
- **SPEC_B C*₃:** para η > η₀ es una condición necesaria (no cierra); para η ≤ η₀ es REF-D.
- **P211-A:** el borde de la media de casi-coincidencias es superpolinomialmente pequeño (PROVED).
- No se encontró ninguna familia de vectores que vea Near_M ≠ 0 y donde Near quede firmado o dominado por Arch con prueba.

---

# Parte C — Intentos, fases 161, 162, 188, 211, 212

## Inventario de intentos sobre Near_M (casi-coincidencias m≈kn, m≠kn) y sus equivalentes

Lectura, sin construcción. Convención: etiquetas copiadas de la fuente. «[H]» marca pasos de una fuente que
razonan vía ceros / ecuación funcional ξ / equivalencias prohibidas; se registran sólo como lo que dice la fuente.
«Leído» = memo abierto; «vía índice» = sólo la fila del índice maestro (no se abrió la primaria).

Objeto: 𝔸_M = Arch_M − Div_M − Near_M (P47 prop:AM), Near_M(m,k) = ½Σ_{n≥2, kn≠m} v_n c_0(log(kn/m)),
v_n = 2Λ(n)/√n; (Div+Near)_{mk} = ½Ξ_{F_0}(log(m/k)), Ξ_{F_0}(d) = Σ_n v_n c_0(log n − d) (211 DOSSIER_001 §1.4).
Problema (S) / R9 del índice: Arch_M − Div_M − Near_M ⪰ 0 ∀M, estado **OPEN** (índice l.12940–12960, l.4397).

---

## 1. Tabla por familia de método

### F1. Separar Near como operador propio / soportes sin Near (fase 188, citada por 211 y 212)

| id / archivo | coordenadas y nombre | operación | resultado y etiqueta | motivo exacto del fracaso | qué sobrevivió |
|---|---|---|---|---|---|
| L2_BUILD_029 (188; leído) | enteros; «Near-free sets» | restringir a S = {Πp_i^{k_i}} con 2T₀ < e^{−2L}/2 para que Near ≡ 0 | PROVED (estructura); test trivial | separar exige resolución: a₀ ≈ log(1/T₀) ≈ 2L domina Σ 2log p/(√p−1); se cumple «por razones locales», sin entrada global; la amplificación sólo falla con c ≳ a₀ | A|_S = a₀I − ⊕_i D_i + E (suma de Kronecker de Toeplitz locales); conclusión de la fuente: «el signo no puede vivir en conjuntos sin Near» |
| L2_BUILD_030 (188; leído) | enteros / Dirichlet: sᵀW_1Vs; corrimiento aditivo h = m − kn (h=0 Div, h≠0 Near) | escribir Near como suma de convoluciones desplazadas Σ_{m−kn=h}; expansión de Ramanujan 1_{n\|j} = n^{-1}Σ_{q\|n}c_q(j) | identidades PROVED; §2 «Near no es un operador con signo propio» PROVED; paso a S suave ARGUED | W_1V no tiene signo (parte simétrica = multiplicador Re V(τ), indefinido); Near es «el resto de resolución finita del mismo producto \|P_s\|²V» | Q = (forma m^♯) − ⟨fluctuación de Chebyshev q=1⟩ − Σ_{p^b}⟨componentes c_{p^b}(j)⟩, exacta en el emparejamiento analítico |
| L2_BUILD_031 (188; leído encabezado) | enteros; vectores equilibrados en residuos (R_Q),(B_Q) | anular componentes c_{p^b}, p^b ≤ Q | Teorema E PROVED: (B_Q) ⟺ D; §3–4 **corregidos** (CORRECTION_RESIDUE_BALANCE_031: M=Q=2, s=(1,1), componente q2 = v2/2 > 0) | la restricción no debilita el objetivo; la supresión de §3 era inválida | Teorema E intacto |
| N_BUILD_021 (188; leído §§1–3) | enteros; Near = Ξ-kernel menos exactas; en primos: correlaciones desplazadas | usar estadísticas de progresiones (SW, BV, BDH, Titchmarsh, Brun–Titchmarsh) como propiedades de clase; vectores torcidos por χ | Prop 1, Thm 2, Prop 3 PROVED; clase 𝒞_prog NO-GO | Thm 2: toda clase definida por errores o(x) es cerrada bajo borrado/amplificación finita ⇒ contiene falsificadores (finmod/void); Prop 3: con χ, Near lleva fases χ(m)χ̄(k) ≠ χ(n) (forma híbrida) | rutas de conductor >1 distintas de las dos excluidas: no excluidas |
| N_BUILD_022 (188; leído §§1–3) | matrices Z, Δ, L; X_M = [Ξ(log m − log k)] | identidad exacta ZΔ = [L,Z] (1∗Λ=log) e intento de alcanzar X_M | §1 PROVED (= R162_903 B2.1); §3 **NO-GO PROVED** | X_M = Z⁻¹Ł_M + 𝒟_M; 𝒟_M (no divisores, a ≈ m/(kb)) se anula sii Near = 0: «Near es un defecto de discretización»; la identidad sólo controla divisibilidad exacta | símbolo Bohr: con fases independientes θ_p sólo Div es diagonal; Near y Arch viven en la diagonal θ_p = θ log p |

### F2. Media de Near a lo largo de polinomios de Dirichlet suaves (211)

| id | coordenadas | operación | resultado | motivo exacto | sobrevivió |
|---|---|---|---|---|---|
| 211 ROUND_001_A (leído) / LEDGER C1 | espectral: Q_M(s) = (1/2π)∫F̂₀²\|P_s\|² s_N dτ, familia s_w = m^{−½}w(m/M) | sumación de Poisson en ℤ; resumar Div+Near | descomposición PROVED; Q_M = M·𝒜(w) + 𝒵_N + ℛ_M; ℛ_M = O(M^{−3+ε}) ARGUED; **NO-GO** (transferencia red→continuo). Pasos (0.2) y (c) usan ζ/ζ′ y la ecuación funcional [H] | en la familia suave, Q_M ≥ 0 ⟺ (hasta O(M^{−3})) 𝒜(w) ≥ 0, i.e. la forma continua de ventana en T′ = (L+2T₀)/2: reformulación, no signo. «Div y Near son contabilidad del retículo que Poisson resuma» | término de borde 𝒳_M = O(M^{−K}) ∀K (PROVED); conjetura ARGUED: el exponente −3 de λ_min es regularidad del perfil, no margen |
| fase 190 (vía índice l.8825–8840) | enteros, M ≤ 3000 | experimento numérico sobre Near | NUMÉRICO; NO-GO por [sens] | estadísticas de Near (norma ≈0.17M, rango completo, 56% positivas, plana en h) idénticas a 5 dígitos bajo perturbación 1e−5 de v₂: no específicas | Identidad C3 PROVED (clase W7): sᵀ(Div+Near)s = 2Σ_N N^{−½}log N·E_M(N); balance sólo por defectos N=2,3,4 |

### F3. Schur / multiplicadores / factorizaciones sobre 𝔸_M

| id | coordenadas | operación | resultado | motivo exacto | sobrevivió |
|---|---|---|---|---|---|
| 211 ROUND_003_B (leído) | enteros; métricas ρ = \|log m − log k\| y δ = log(lcm/gcd); Near = pares ρ<δ | 𝔸_M = 𝕏∘𝕂_t + ℝ, 𝕂_t = [(gcd²/mk)^t] | Prop 1 (restatement) PROVED; Thm 3, Thm 4 NO-GO PROVED (Thm 4 corregido en STATE_001: «Near^comb ≠ 0 para algún M») | Lema 2: \|𝔸−ℝ\|_{mk} ≤ βe^{−tδ}; en pares m≈kn (δ grande) ℝ debe reproducir 𝔸: «el multiplicador nunca ve las casi-coincidencias». Thm 4: con la prescripción Div/Near, ℝ = −Near^comb tiene diagonal cero ⇒ no PSD | t*_M = inf{t: 𝔸∘𝕂_t ⪰ 0}; 𝔸 ⪰ 0 ⟺ t*_M = 0 (reformulación) |
| 212 ROUND_003_7 (leído) | enteros; incidencia de divisores | 𝔸_M = WᵀDW, W soportada en d\|k | Lema 1 NO-GO de formato PROVED; Lema 2 PROVED; Cor 3 PROVED; selección: **repetición** | la incidencia de divisores no ve pares coprimos casi proporcionales; en primos WᵀDW = D₁wwᵀ + diag (rango uno + diagonal), y la restricción a primos ya equivale al objetivo (CA_K_002 Teor. 3.2): todo el signo queda en ρ | «falta una W no soportada en la divisibilidad que vea m≈kn, con fórmula propia y ρ con signo manifiesto. No sé escribirla» |
| 212 ROUND_004_D (leído §§2–3) | enteros; soporte de casi-divisibilidad | factorizar 𝔸_M con soporte en m≈kn; buscar clases cerradas bajo complemento de Schur | Lemas A, B PROVED; Lema C NO-GO de formato PROVED; selección no pasa | Lema B: la casi-divisibilidad no es orden parcial; su soporte es un semiorden de umbral independiente del peso. Lema C: 𝖡 < 0 en (θ₀, log2−θ₀), no es Laplace de medida ⇒ 𝔸_M no está en TP/signo-regular, Green de árbol, f(mcd) | «La información aritmética está en los VALORES de las entradas de Near, no en su patrón» |
| 212 ROUND_022_A (leído parte 2) | congruencia de Möbius 𝔹_M = ZᵀArch Z − [...] − ZᵀNear Z | congruencia unitriangular entera | repetición / NO-GO de clase registrado | cancela sólo la parte de divisibilidad; ZᵀNear_M Z queda sin identidad (N_BUILD_022 §3) | — |
| 212 ROUND_001_B (leído §6) | cadenas multiplicativas | pivotes de Schur a lo largo de anidamientos | sin mecanismo nuevo (repetición de C6) | Prop 5: en puntos αℕ+βℕ irracional Div=0 y todo el peine es Near; la estructura multiplicativa no cambia pivotes; en cajas sin Near suma de Kronecker, no producto | — |
| R162_903 (leído) | álgebra 𝒜_T = {M_T(α)}, Gram de imágenes de Möbius | Gram entero, BCH terminante, Sylvester/Moore, levantamiento tensorial | 8 enunciados PROVED; ruta **NO-GO** | Prop 2.1: los suelos ⌊y/u⌋ sólo existen puntualmente; en L² dan hipérbola/diente de sierra lineal (peine (PC)); Thm 4.1–4.2: invariantes continuos colapsan a (sig,det); Λχ₂ y Beurling pasan todas las líneas | residuo afinado: hace falta un funcional DISCONTINUO de F que distinga enteros de enteros generalizados y 1 de χ₂ |

### F4. Gram theta / gaussiano: parte resonante kn² = lm² vs. no resonante (211 POWER_GRAM_SLICES §§16–17, POWER_GLOBAL)

| id | coordenadas | operación | resultado | motivo exacto | sobrevivió |
|---|---|---|---|---|---|
| GRAM §16.1–16.4 (leído) | theta: A(z_k, z̄_l), z_k = ½log k + iy; modos n,m con fase kn² − lm²; casi resonancias = kn² ≠ lm² | equivalente asintótico ε = cos2y → 0 | (INT-ASYM) PROVED; (NEAR) S_δ ≤ C_{k,l}δ^{−4}log(2+1/δ) PROVED; (OFF) PROVED | uniformidad sólo para lista FIJA de enteros; constantes dependen de k,l | principal [105/(512√2)]ρ(k,l), ρ = gcd(a,b)/√(ab) en clase libre de cuadrados; bloques fijos complejos definidos positivos para ε pequeño |
| GRAM §16.5 (leído) | idem, k, l = k+1 | comparar con ρ tras normalizar la diagonal | PROVED (negativo) | \|C_y(k,k+1)\| → 1 mientras ρ(k,k+1) = 0: no hay C_y ≥ c_yρ ni aproximación uniforme | — |
| GRAM §17–17.5 (leído) | theta; R_res = pares kn² = lm²; Off = A − R_res (lo no resonante, incluye la cola theta) | SOS por cambio de escala u = λt y Λ∗1 = log (RES-SOS) | PROVED: R_res definida positiva en todos los órdenes; R_res ≥ c_*E_y (UNIF-D) | «NO se demuestra el signo de la contribución kn² ≠ lm²» | (RES-SOS), D_q > 0, c_* explícita |
| GRAM §17.6 (leído) | theta, y=0 incluido | acotar Off por E_y o por fracción de R_res | PROVED (negativo; RULES_AVOID D9) | pares k,k+1: Off_y[c^{(k)}] = −log k + o(1) con E_y = 1; A_y[c]/R_res[c] → 0: no hay Off ≥ −C E_y ni A ≥ δR_res | «en y=0 Off ≥ −R_res es exactamente A_0 ⪰ 0 sobre enteros: el objetivo completo, sin margen» |
| GLOBAL «presupuesto resonante» (leído) | theta, bloques k..k+N−1, k > N² | cota superior uniforme de Off por R_res | PROVED (en y=0) | R^{−½}Off R^{−½} → J_N − I_N: no hay \|Off\| ≤ C R | Off ≥ −R (crítica unilateral) OPEN; el límite I−J la satisface |
| GLOBAL «Extensión factorial antes de resonancia» + corolarios (leído) | theta, y=0; b_λ, cuadrados P_m b − R_m b | Q = Σ Λ(m)‖P_m b − R_m b‖²_K + b*Db + E(b) exacta | identidad PROVED; D ⪰ 0 y E ≥ 0 por separado refutados; E ≥ −C·S_sq refutado (c = δ₁); B+M ≥ 0 FALSO (test d=1,2, c=(1,−1/100)) | D tiene entradas > 0 pero D ≤ H y H tiene test compacto negativo (GRAM §19.11); E(δ₁) < 0 con S_sq = 0 | Q = L + M en el núcleo libre de cuadrados; 0 ≤ B ≤ L matricial |
| GLOBAL «Control de la sustitución ortogonal» (leído) | theta | P_m → proyección ortogonal Π_m | PROVED (invalida el reemplazo) | Π_m = I; Σ Λ(m)‖F − R_mF‖² = ∞ | — |
| GLOBAL «Covarianza divisorial agrupada» y «resto divisorial indefinido» (leído) | lift probabilista: R(F) = Σ n^{−½}C_{½}(n) Re c_F(log n) | firmar los coeficientes agrupados C_s(n) | PROVED (negativo) | C_s(p²) < 0, C_s(p²q²) > 0; tests pares primitivos F_± (bumps (1,−5/2,1)) dan R(F_+) = (7/4)κ‖g‖² > 0, R(F_−) = −(1/4)κ‖g‖² < 0 | no descarta compensación con ARCH |
| GLOBAL §2 (leído) | enteros | auditoría estratégica de «transferencia aritmética exacta y casi coincidencias» | revisión, sin teorema | «Near no tiene signo separado… estimar Near en valor absoluto no constituye el cambio» | **obligación viva**: desigualdad FIRMADA conjunta Arch vs términos m≈kn, uniforme en vectores y tamaños, conservando fases y bordes |

### F5. Gram hiperbólico / realización operatorial (211 POWER_HYPERBOLIC_MODEL_GRAM)

| id | coordenadas | operación | resultado | motivo exacto | sobrevivió |
|---|---|---|---|---|---|
| §§1–6 (leído) | modelo φ_a = exp(−a cosh 2t); kernel [(M_a(u_i)+M_a(u_j))/(u_i+u_j)] | Green positivo de ODE en escala | PROVED para el modelo; transferencia a Φ real **OPEN** | no hay ODE/Green con identidad REP para la Φ real; mezclas de densidades no conservan el signo (GRAM §7) | prueba de que fallo de capas no impide signo de todos los órdenes en un modelo |
| §12.6 (leído) | realización Q,B,C,D con observación theta exacta | construir operadores | PROVED como realización, no como signo | falta métrica y Green positivos | realización y ecuación fuerte Y_rr = (b²+ν²)Y + 2DY_r + (−C+2bB̄)Y |
| §12.7 (leído) | idem | métrica local positiva acotada | NO-GO PROVED en la clase declarada | exponentes 25/2, 21/2, 11/2, 8 distintos fuerzan m₁₁ = m₂₂ = 0 | no excluidas: métricas no locales/no acotadas, conexiones nuevas (las reglas del proyecto: reabrir sólo con kernel no local explícito + identidad Green) |

Nota: en este archivo Near no aparece con nombre; vive dentro del kernel A completo (parte no resonante). La fuente no da fórmula de paso a Near_M.

### F6. Descenso / recurrencia / compensación entre escalas (211 POWER_DESCENT_016, POWER_RECURRENCE_BOUNDARY_036)

| id | coordenadas | operación | resultado | motivo | sobrevivió |
|---|---|---|---|---|---|
| DESCENT_016 (leído §§1–4) | filtros Q = s/(s+u), L = u/(s+u) sobre la forma completa W (contactos incluidos) | (DEF) W[f] = W[Qf] + W[Lf], binomial (BIN), ley (LAW) | PROVED; descenso aritmético OPEN | cola positiva sólo en borde de masa nula; el prefijo finito no tiene signo | (FD) diferencias finitas eventualmente positivas |
| RECURRENCE_036 (leído §§1–5) | frontera diagonal A_{N,k} | (FRONT) con pesos beta-binomiales | PROVED: energía del cono O(log L/√L), R_L → A_{N,k} | el resto conserva todo el valor inicial | criterio de reapertura: R_L ≥ −ε_L, ε_L → 0 (RULES_AVOID D4) |

Near aparece aquí sólo dentro de «todos los contactos» (bounds de QUADRATIC_EXPLICIT017).

### F7. Krylov, mallas de Nyquist y conteos (211)

| id | coordenadas | operación | resultado | motivo | sobrevivió |
|---|---|---|---|---|---|
| ROUND_005_A Prop 3.4 (leído) | potencias del peine Π³; clases de razón r = mn/k, peso W₃(r) ≥ 0 | expansión cos³ | PROVED como signo de la contribución (REVIEW_004 lo baja a **ARGUED**); familia Krylov NO-GO | en grado 2 no hay casi-coincidencias; en grado 3 entran con peso ≥ 0 y Π entra con signo menos: «trabajan en contra del signo en K₂» | — |
| ROUND_007_B §3.2 (leído) | triples (m;n,k) | localizar cuándo entran | Cor 3.2 PROVED; tamaños NUMÉRICO | a T = ½log5 los triples cercanos pesan < 1e−4; domina la parte m = k | lista de umbrales de entrada |
| ROUND_002_A Prop M (vía índice l.9767) | malla de Nyquist s_k | forma de malla de la casi-coincidencia | Prop M PROVED (fila del índice) | muestras profundas ⇒ casi-coincidencias n′^{q_n} ≈ n^{q_{n′}}; ningún criterio sobre muestras solas decide (212 ROUND_003_1 fila 7) | — |
| ROUND_006_C §7 (leído) | productos k-fold | conteo de gran criba 𝒩_k(ν) | Thm A–B PROVED; §7 lema **OPEN** | cota exp(2e^T) no mejora sin contar casi-coincidencias de productos | objetivo 𝒩_k(ν) ≤ C^kΣb_m² (OPEN, energía multiplicativa) |
| ROUND_015_B §2.1 (leído) | bloque bajo, cola de Poisson | identificar qué parte de Λ actúa | PROVED estructura + ARGUED tamaños | las casi-coincidencias no aparecen en el bloque bajo; sólo divisibilidad exacta (Λ∗1)(N) = log N | — |
| NEAR_CASES_RESULTS (leído) | paquetes ψ_ε centrados en log m | mejora de nearfree; 2 paquetes; triángulo (k,2k+1,4k+3) | §1 PROVED (quita log log M); §2 contraejemplo a monotonía de Loewner; §4 falsificador del ciclo (p,p,p²) | §1: K grande sigue impidiendo near-coincidencias; §4: término cúbico −2x²z < 0; d → ∞, no es negatividad de la forma | batería 2×2/cadena/triángulo; «falta controlar la norma colectiva de la matriz de near-contactos frente a la energía arquimediana» |

### F8. Identidad (PC) de la fase 161 y su cola de hipérbola

| id | coordenadas | operación | resultado | motivo exacto | sobrevivió |
|---|---|---|---|---|---|
| R161_001 (leído) | operadores de traslación; H_{M,N} = L_M S_N − K_N (cola de hipérbola, coeficientes h(k) en k > N) | identidad conjunta (PC): S_N A_M 𝓕 = {X,E_N} − L_M*E_N − JH − H𝓕 | Thm 2.1, 3.1, 4.1 PROVED; sin signo | «coeficientes positivos no hacen positiva una suma de traslados» | (PC); defecto interior δ_a(k) de cada falsificador |
| R161_002 §1 | idem | cuadrado ‖R_{M,N}F‖² | Thm 1.1 PROVED (ciego al signo) | invariante bajo A_M → −A_M | emparejamiento orientado (OR) = ⟨A_MG, S_N*S_NG⟩ |
| R161_002 §§4–8 | idem | SP-161 / L161.1: pesos w_N ≥ 0 que telescopen | Thm 8.1 PROVED: NO-GO | [p](Σ w_N H_{M,N}) = log p Σ_{N<p} w_N > 0 en todo primo grande | Cor 8.2 (ver (d)) |
| R161_003 | Mellin; S_N^ren = S_N − C_N(D) (retículo − continuo) | renormalización polar | Prop 1.1, Thm 2.1–2.2 PROVED; L161.2 OPEN → retirado | sumas crudas oscilan ≍ N^{½} | defecto renormalizado → 0 en Schwartz |
| R161_004 | escalar D(u) = Σ_{log n≤u} Λ(n)/√n − 2(e^{u/2} − 1); fibra de divisores | escalarizar o promediar en fibras | Cor 2.1, 3.1 PROVED (por citas): L161.2 retirado | escalar → Paper 41 C4–C5 (cuadrado de signo equivocado, densidad negativa bajo log 2); fibra → ANOVA 104/106 (hueco espectral cero); Möbius → P121 CMO (la derivada logarítmica anula la diagonal). §4 identifica el objetivo con un certificado de rango [H] | L161.3 (ver (d)) |
| R161_005–006 | puerto exterior ℓ_T(F) = (1−P)AF; discrepancias unilaterales Δ^R, Δ^L | especialización de (PC) a estado de primer contacto | Thm 1.1, 2.1 PROVED; símbolo normal crítico OPEN [H] | — | contaminación cruzada sólo en las dos direcciones de Tate |
| 212 ROUND_003_6 (leído) | test de Möbius truncado M_N; resto R(F) | a_T = f₀ − f₁ − R₀ + R₁ | PROVED / CONDITIONAL (dominio); Lema 1 y Cor 2 NO-GO con clase | ceguera afín: a_T^{(c)} = f₀ − cf₁ − (c−1)g − R₀ + cR₁ | **R(F)** «ve exactamente las casi-coincidencias d ≈ k, k ∈ (N,N²], con pesos de Möbius c_N(k) sin signo» |
| 212 ROUND_004_C (leído) | R(F) | estudiar R(F) | repetición en lo esencial; Lemas 1–5 PROVED; R ≤ 0 falso (Lema 5) | en la clase invariante por traslaciones toda escritura manifiesta suma a un certificado sin inverso (Lema 4); agujas no distinguen c | — |
| 212 ROUND_004_A (leído) | pesos w_N reales y de criba λ_d | L161.1 con signo | Lema 1, Cor, Prop 2, Lema 3 PROVED; NO-GO con clase 𝒞_w | telescopado exacto fuerza w = δ_{N=1} (tautológico); cancelar la cola en primos exige Σw_N = 0 vs Σw_N = 1 | bloque interior I^λ (casi-coincidencias con coeficientes θ^λ de criba): «su signo no se examinó» |
| 212 ROUND_011_A (leído §§0–2) | Δ^R ℓ_T(F) | signo de discrepancia reticular (Euler–Maclaurin, Hermite–Hadamard) | NO-GO de selección; Lemas 1–2 PROVED | Δ^R lineal en F (signo uniforme ⇒ funcional nulo) y sin Λ (ciego a cΛ y borrado) | ver (d) |

### F9. Canales suma/diferencia (R162_1003, leído)

| coordenadas | operación | resultado | motivo | sobrevivió |
|---|---|---|---|---|
| línea completa T = ∞; canal suma Re(D²) (Λ∗Λ) y canal diferencia \|D\|² | cancelación de (Im D)² entre canales vía ecuación funcional [H]; test Λ²-Selberg; T finito | Thm S PROVED; Thm R PROVED [H]; Prop 4.1–4.2, Cor 4.3 PROVED; §5 NO-GO | Prop 4.2: el kernel es Toeplitz en log, no GCD; Cor 4.3: H = Z*DZ es congruencia (Sylvester); §5: a T finito P_TS_xP_TS_yP_T ≠ P_TS_xS_yP_T (Brown–Halmos), los canales difieren por productos de Hankel | — |

### F10. Sitios primos y forma afín (vía índice; primarias no abiertas)

| id | resultado (índice) |
|---|---|
| CA_K_002 (193, l.9002, l.9016–9019) | en sitios primos Div ≡ 0 y el objetivo es Arch ≥ Near; Near = Σ_h C_s(h) (correlaciones de Chen p − h = p′q^a); paridad y residuos son reindexaciones (cada Near_q de traza 0, indefinido); sitios p+θ_p irracionales tienen el mismo valor de verdad. PROVED reformulación; «candidato a re-examinar» |
| INV_V_002 (196, l.9119) | 𝔞_T = A_∞ + ½𝔄ff_T − ½Re⟨Vf,f⟩_Ш; 𝔄ff no diagonal en Mellin, lineal en el peine; Thm V2.4 PROVED, V2.2(c) FALSO |
| INV_G_001 (194, l.5833) | NO-GO clase 𝒞_G; «parte positiva = Near (REF)» |
| L2_BUILD_020 (índice R9) | resonador de casi-ternas: exacto a Ω ≥ N³; resonancia natural O(1) |
| L2_BUILD_023 Thm T (índice R9) | cada sección 2×2 es la banda \|X(d)\| ≤ 2a₀; sólo necesaria |
| 212 ronda 15 Y1 (RULES_AVOID) | reindexación m − kn = h, Farey, Ramanujan, gran criba, Selberg: repetición; clase Σx_nQ_n ciega (PROVED) |

---

## (a) Diccionario del mismo término

| sistema | nombre en la fuente | fórmula / paso (cuando la fuente lo da) |
|---|---|---|
| enteros (P47 prop:AM) | Near_M | Near_M(m,k) = ½Σ_{n≥2, kn≠m} v_n c₀(log(kn/m)); Div_M + Near_M = ½[Ξ_{F₀}(log(m/k))] (DOSSIER §1.4; N_021 Prop 1: Near = sᵀ[Ξ − 1_{k\|m}v_{m/k}c₀(0)]s) |
| enteros, corrimiento aditivo | rebanadas h ≠ 0 | sᵀW₁Vs = Σ_h Σ_{m−kn=h} s_ms_kv_nc₀(−log(1 − h/m)); h = 0 ↔ Div, h ≠ 0 ↔ Near; \|h\| ≲ 2T₀m (L2_030 §1(c)) |
| espectral / Dirichlet | resto de resolución finita de \|P_s\|²V | sᵀ𝔸s = (1/2π)∫F̂₀²\|P_s\|²[m(τ) − Re V(τ)]dτ; Div = parte Bohr-diagonal, Near = casi-diagonal (L2_030 §§1(b), 2) |
| Ramanujan | fluctuación q=1 + componentes c_{p^b}(j) | Q = m^♯ − ⟨Chebyshev q=1⟩ − Σ_{p^b}⟨c_{p^b}⟩ (L2_030 §3; supresión de 031 §3 corregida) |
| matrices Z, Δ | 𝒟_M | X_M = Z⁻¹Ł_M + 𝒟_M, 𝒟_M = Near (N_022 §3, ARGUED índice preciso) |
| Bohr (fases θ_p) | parte fuera del toro diagonal | sólo Div es diagonal con θ_p independientes (N_022 §4; L2_028 §2(c)) |
| sitios primos | Near = Σ_h C_s(h) | vía índice (CA_K_002) |
| métricas de ℕ | pares ρ < δ | ρ = \|log m − log k\|, δ = log(lcm/gcd); Div: ρ = δ = log p^j (ROUND_002_D, ROUND_003_B) |
| theta / gaussiano | Off = A − R_res (pares kn² ≠ lm²) | A(z_k, z̄_l) = ∫_1^∞ w_{kl}Φ_kΦ̄_l; resonancias kn² = lm²; no resonante acotado por (NEAR)/(OFF) (GRAM §§16.2, 17). La fuente no da paso explícito Off ↔ Near_M; en y=0, «Off ≥ −R_res ⟺ A₀ ⪰ 0 sobre enteros» (§17.6) |
| theta, factorial | D y E en Q = ΣΛ‖P_mb − R_mb‖²_K + b*Db + E | GLOBAL «Extensión factorial» |
| ventana (operadores de traslación) | resto R(F) del Möbius truncado; bloque I^λ | R(F) = Σ_{N<k≤N²} c_N(k)k^{−½}Re[⟨𝓜V_{−log k}F,F⟩ − Σ_{\|log(k/d)\|<2T} Λ(d)d^{−½}⟨V_{log d−log k}F,F⟩] (212 ROUND_003_6 (4.2)); I^λ (ROUND_004_A (4.3)) |
| ventana, Krylov | clases de razón W₃(r), r = mn/k ≈ 1 | ROUND_005_A Prop 3.4 |
| malla de Nyquist | muestras profundas s_k | s_k = m + r − A_T + c(−1)^k + 2Σv_n sin²(πk log n/4T) (Prop M, vía índice) |
| hipérbola de divisores (161) | cola H_{M,N}, coeficientes h_N(k), k > N | H = L_MS_N − K_N; h_N(p) = log p (N < p), 0 (N ≥ p). Es la contraparte de divisibilidad exacta, no Near; Near aparece sólo al comprimir a ventana (R(F), I^λ, Δ^R) |
| Gram hiperbólico | (no nombrado) | dentro del kernel completo; sin fórmula de paso |
| paquetes | near-contactos | entrada −v_n c/2 en matriz de paquetes (NEAR_CASES_RESULTS §2) |

## (b) Motivos de fracaso agrupados

1. **Near no tiene signo propio**: es el resto de resolución del mismo producto (L2_030 §2; GLOBAL §2); tratarlo aparte deja una matriz de diagonal cero o un resto indefinido (ROUND_003_B Thm 4; resto divisorial con F_±).
2. **Formato / patrón**: incidencia de divisores, Schur, semiórdenes y Kronecker no ven pares coprimos casi proporcionales; la información está en los valores, no en el patrón (ROUND_003_B Lema 2; 212 ROUND_003_7 Lema 1; ROUND_004_D Lemas B–C; N_022 §3).
3. **Separar cuesta resolución**: eliminar Near (Near-free, nearfree, K grande) compra energía arquimediana que gana por razones locales (L2_029; RESULTADOS §1).
4. **Ceguera al peso / linealidad**: identidades con Λ∗1 = log, Möbius o criba son afines en c o lineales en F (Lema 1 de 003_6; ROUND_011_A Lemas 1–2; Y1 de RULES_AVOID; R162_903 Thm 4.1–4.2).
5. **Clase cerrada bajo modificación finita**: estadísticas de progresiones/criba (N_021 Thm 2; fase 190 [sens]).
6. **Reformulación**: Poisson en familia suave regresa a la forma continua (ROUND_001_A); restricciones equilibradas ⟺ D (L2_031 Thm E); Off ≥ −R_res en y=0 es el objetivo (GRAM §17.6).
7. **Falta de uniformidad**: equivalentes theta sólo para listas fijas (GRAM §16); ni cota inferior (Off ≥ −CE_y) ni superior (\|Off\| ≤ CR) uniformes (§17.6, presupuesto resonante).
8. **Pares no implican colectivo**: secciones 2×2 sólo necesarias (L2_023 Thm T); triángulo y ciclo (p,p,p²) con cúbico negativo (RESULTADOS §§3–4).
9. **Signo perdido por cuadrar / orientación**: (SQ) ciego; pesos positivos no telescopan la cola (R161_002 Thm 1.1, 8.1).
10. **Contribución en contra en grado 3**: W₃(r) ≥ 0 con Π restando (ROUND_005_A; ARGUED tras REVIEW_004).

## (c) Señalado explícitamente como no ejecutado / abierto

- Desigualdad FIRMADA conjunta Arch vs términos m≈kn, uniforme, con fases y bordes (GLOBAL §2; índice R9 «direcciones admisibles»: fluctuación q=1 + c_{p^b}(j) a resolución ≈ e^{2T}). OPEN.
- Comparación crítica unilateral Off ≥ −R_res (GLOBAL «presupuesto resonante»). OPEN.
- Compensación conjunta D+E con los cuadrados; L+M en todos los órdenes (GLOBAL factorial). No obtenida.
- W no soportada en la divisibilidad que vea m≈kn, con fórmula propia y ρ firmado (212 ROUND_003_7, ROUND_004_D: «no sé escribirla»).
- Bloque interior I^λ con coeficientes de criba: «su signo no se examinó» (212 ROUND_004_A).
- Telescopado tras comprimir a la ventana con los cuadrados de fuga de C_T; contabilidad R161_032 (4.2) «sigue sin derivar»; tests distintos de S_N𝓕F; pesos dependientes de F (ROUND_004_A).
- SP-161/L161.1 con pesos con signo/derivadas discretas y fugas comprimidas: «nunca se escribió» (ANNEX_161_FILES_1 §(c)); la rama 𝒞_w luego NO-GO (ROUND_004_A).
- Lema de gran criba 𝒩_k(ν) para productos k-fold (ROUND_006_C §7). OPEN.
- Rutas de conductor >1 distintas de las dos excluidas (N_021 §3). No excluidas.
- Métricas no locales / no acotadas y conexiones nuevas para la realización theta (HYPERBOLIC §12.7). No excluidas.
- Positividad de Hadamard que acople primos con m≈kn; transporte de retardos no afín; emparejamiento impar no lineal en A_M (RULES_AVOID X, sin objeto escrito).
- Sitios primos Arch ≥ Near: «candidato a re-examinar» (índice l.5922, vía índice).
- Fase 190: decidir si el borde de Q_M(w) es tamaño error-PNT o margen M^{−3} (vía índice); ROUND_001_A lo resolvió como superpolinomial en su familia y el resto ℛ_M quedó ARGUED.

## (d) Estado exacto de L161.3 y de la derivada terminal de R161_002 Cor 8.2

**Cor 8.2 (R161_002).** Enunciado: en un primo p, h_p(p) − h_{p−1}(p) = −log p; «el signo de von Mangoldt aparece como derivada discreta terminal de la cola positiva, no como promedio positivo; el siguiente mecanismo debe orientar esta derivada». Es un corolario PROVED del Thm 8.1 (que es NO-GO PROVED para pesos ≥ 0). Seguimiento:
- R161_003 §5 convirtió esa exigencia en L161.2 («la derivada con signo debe recuperar el salto −log p»); L161.2 RETIRADO (R161_004) en sus formas escalar-positiva y de fibra positiva.
- 212 ROUND_004_A: con pesos reales w_N, telescopado exacto fuerza w = δ_{N=1} y cancelar la cola en primos exige Σw_N = 0, incompatible (Corolario PROVED). La derivada pura w = δ_{N+1} − δ_N da la identidad PC de un solo traslado con coeficiente 0 en r = 1: «a_T no aparece» (PROVED). NO-GO con clase 𝒞_w.
- Índice: fila «Cola de hipérbola… pesos no negativos — DEAD [signo sólo en el salto terminal]» (l.5166, l.12346).
- No encontré memo que construya una orientación de la derivada terminal fuera de la clase 𝒞_w; quedan sólo los «no excluidos» de ROUND_004_A (tests no S_N𝓕F, pesos dependientes de F, telescopado tras compresión con fugas de C_T).

**L161.3 (oriented first-contact Poisson port).** Definido en R161_004 §6: aplicar (PC)/(PC-ren) a un estado primitivo de primer contacto antes de cualquier norma o traza y probar que su puerto exterior aditivo anula una clase conormal crítica [H] (la formulación de la fuente usa ceros). Estado en la fuente: **OPEN** (R161_003 §6, R161_004 §6, R161_099). Piezas PROVED alrededor: R161_005 Thm 1.1 (PR𝓕F = PS_Nr + B_{N,T}(F)); R161_006 Thm 2.1 (B^ren = Δ^R_{N,T}ℓ_T(F) − e^{−t/2}a_−(ℓ_T(F))); contaminación cruzada en el span de Tate PROVED; «cancelación con el forzamiento de Tate: no calculada»; «extracción y anulación del coeficiente normal crítico: OPEN» [H]. R161_099 y R161_007–008 avanzan la identificación del jet [H].
Estado posterior (212): ROUND_011_A / RULES_AVOID U1–U2: «L161.3 cuadrático cerrado por R161_029 (monotonía falsa), **orientado OPEN**»; signo de discrepancia reticular sobre Δ^R: NO-GO de selección (lineal en F; sin Λ). Falta «un apareamiento orientado de dos orientaciones cuyo término cruzado tenga el signo de D^Poisson ≥ 0 (R161_029 (6.1))». Además «los cuatro residuos viven sobre el radical de un primer contacto supuesto, no sobre todo P_T». ROUND_013_B: (OR) de R161_002 no lo cierra; L161.3 orientado sigue OPEN.

## Fuentes leídas

211: README, STATEMENT_001, DOSSIER_001 §1.4, STATE_001 (filas), LEDGER (filas), NEAR_CASES_RESULTS_2026_11_04, ROUND_001_A, ROUND_003_B, ROUND_005_A §3, ROUND_006_C §7, ROUND_007_B §3.2, ROUND_015_B §2.1, POWER_GLOBAL_ROUTE_REVIEW §§1–5 y secciones citadas, POWER_GRAM_SLICES_OBSTRUCTION §§1–2, 16–17.7, POWER_HYPERBOLIC_MODEL_GRAM §§1, 6, 12.6–12.7, POWER_DESCENT_016 §§1–4, POWER_RECURRENCE_BOUNDARY_036 §§1–5 (resto de memos 211 de la lista grep: sólo líneas de contexto).
212: RULES_AVOID (C, D, E, F, U, V, X, Y), OBJECT_SPEC O6, ROUND_001_B, ROUND_003_6, ROUND_003_7, ROUND_004_A, ROUND_004_C, ROUND_004_D, ROUND_011_A, ROUND_022_A (verdicto), ANNEX_161_FILES_1 (líneas).
161: R161_001–006 completos o por secciones de veredicto/estado; R161_099 §4.
162: R162_903, R162_1003.
188 (antecedentes citados por 211/212): L2_BUILD_029, 030, 031 (encabezado), N_BUILD_021 §§1–3, N_BUILD_022 §§1–4.
Índice maestro: grep de Near / casi-coincidencias / L161 (filas citadas por número de línea).
