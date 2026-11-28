> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# Uniones individualizadas de theta, Hecke y covolumen

28-11-2026. Fuentes: los `main.tex` de46,49,50,53,54, los apéndices de49/50/53/54 y las reconstrucciones de THETA.md. Se excluyen47/48. «(a) unión» significa que se comprobó la instancia matemática descrita, no sólo una semejanza textual. «(c) por exchange» significa que la deducción recibe una premisa cuya prueba escrita falla: **no** que se haya demostrado falso el resultado descendiente. Las reconstrucciones con reparaciones expresas tampoco certifican todas las líneas literales del original.

## Entradas de la tabla de46:5072–5087 en esta especialidad

| Destino46 | Origen matemático | Hipótesis, normalización y rango efectivamente comprobados | Dictamen y exchange |
|---|---|---|---|
| `au:seesaw`,4314 | 49 `ps:onestep`,3984; `ps:double`,4062; ensamblaje4265–4364, `pk:chi0` | Dato Ψ puede depender del twist; c_ss no. No se exige que la función resultante sea no nula. Haar autodual y volumen de clases conservados; cancelación de los tres exponentes de upsilon en chi0; soporte y familias finitas tratados en AS01. | (a) reconstrucción de esta unión en SS01/AR01–03/AS01, con errata de orden de traslación FJ reparada según SPANNING. No depende de product53. No da no anulación que el enunciado no promete. |
| `au:divis`,4368 | 49 `pa:divis`,3184–3277; `pa:eldiv`,3156; 50 `ph:thm`,396 | Todos los primos, twist de conductor primo a ℓ, mismo retículo integral. Excepcionales: primero S₀=Y_Λ^m S_j+ℓ^j S_j y después S=S₀∩S^ram; no se afirma que cada Hecke preserve S^ram. NivelN usa U_N y retículoL₀, no el ciclo excepcional50. | (a) unión reconstruida CM01/KI01/LN01/EX01/BR01/AS01/HE01. Sin exchange. |
| `au:count`,3900 | 49 `pa:count`,2522, y `pa:schur`,2673 | Forma normal previa; columnas de altura<n′; B≥1; entradas Schur con fila estándar o menores anidados, no polinomios arbitrarios. Se conserva deducción adicional e=0 para p=d y v(π_d)=1/2. | (a), CM01 y lectura de la cota. Aplicación a norma normal revisada, no sólo enunciado copiado. Sin exchange. |
| `au:kernel`,4497 | 49 `ps:conj`,3845; `pk:conj`,5433; `ps:monomial`,3862 y empaquetamiento | Cada conjugado, vacío trasladado, mismos factoriales y Ω exacto; ver detalle CS abajo. La fórmula más fuerte sobre la fase δ_g no se certifica literalmente; las consecuencias usadas se reconstruyen separadamente. | (a) unión para la cota efectivamente usada, CJ01–08. No equivale a declarar probada la fórmula fuerte de fase. Sin exchange. |
| `au:restrict`,4516 | 49 `ps:branching`,3803; `pk:branching`,5080–5198 | Misma representación de Schur y métrica; factor hook elimina denominadores; la saturación se usa después de limpiar la variable principal. | (a), BR01, con constante y retículo. Sin exchange. |
| `au:expansion`,4532 | 49 §5.1.6,3922–3967 | Gluing da suma finita de raíces de unidad por datos originales. Denominadores N permitidos por K1_N; no declarar integralidad ordinaria fuera del rango. Invariancia se aplica al tensor completo. | (a), AS01. Sin exchange. |
| `au:equiv`,4584 | 49 §5.1.3,3627–3766, W1/W4/W5 | Niveles y caracteres de Y_j, transporte del vacío y retículos. El cierre de las propiedades locales usadas está en KI01/AS01; la afirmación fuerte de fase sigue separada. | (a) para el transporte usado en SF; no certificación universal de toda fórmula auxiliar W4. Sin exchange. |
| `au:shortbasis`,4427 | 49 `ps:transfer`,3589 y prueba3608–3624 | n≥1 y entero positivo c₀ en la diferente. Retículo L unimodular, producto real Tr/2; Λ=(2/c₀)L tiene dual⊂L. Dimensión real2fn produce exactamente6c₀(fn)². | (a), relectura directa en esta consolidación; no precisa transference más fuerte. Sin exchange. |
| `au:inj`,4794 | 53 `pc:tri-inj`,557; `pc:tri`,1248; `pc:first`,1270; 54 primeros lifts | Álgebra de triángulo(T1–T3) correcta; no se divide por el escalar para demostrar primero que no es cero. La realización automorfa exige las identidades de intercambio. | (c) conclusión global por exchange; (a) deducción algebraica bajo T1–T3. No trasladar el cierre algebraico a inyectividad automorfa. |
| `au:factor`,4850 | 53 `pc:tri-gram`,582; realización del triángulo y multiplicidades51 | Normalización de Z_j=det(u* u), exponentes d_T y twists θ^j; ratios ramificados y factor Nm(Q)^{e/2} conservados. | (c) por exchange y la realización del triángulo, aunque el traslado de la fórmula de Gram es correcto condicionalmente. Véase COVOLUMEN/MULTIPLICIDADES para los otros inputs. |
| `au:aux`,4878 | 53 `pc:auxcore`,1616 y desarrollo §5 | La unión exige integralidad y tamaño del segundo grid, no sólo que existan lifts. | (c) en esta revisión individual: no se rehízo toda la prueba de auxcore aquí. Consultar cierre del agente principal en COVOLUMEN; no asignar(a) por citar Theorem2.28. |
| `au:onelift`,4965 | 54 `po:ss-proof`,1134; `po:glue`,1061; `po:exchange`,995 | Determinante del operador **comprimido** a la imagen, no restricción presuponiendo invariancia. C_j independiente del twist, exponente d_j, condición ℓ∤NmQ y denominadoresβ. Primera identidad depende de tres exchanges. | (a) álgebra condicional y concordancia; (c) resultado completo por exchange53. No confundirlo con la norma de rango uno que sí tiene ruta SW independiente. |
| `au:hecke`,4992 | 54 §2.7,1224; `po:rallis`,1395; `psu:small`,9118; `psu:arch`,9217; CL53 | Pares principales m<z≤r; k/2 pares al cuadrado, otros5m ramificados; constante corregida3x³⁵ preservada. R2/R3 de regularidad se mantienen como hipótesis. | Deducción local de alturas y constantes reconstruida; su uso para una familia regular requiere además regularidad55. No elimina la rama z=1 de IM. CL/norma se distinguen abajo; no afirmar GRH por este cierre. |

`au:moment`, `au:mult` y `au:regular` están individualizados en SPANNING, MULTIPLICIDADES y MATRIZ-UNIONES/SELMER; esta división de trabajo no convierte su estado en(a) automáticamente.

## Constante exacta, ciclo de Hecke y partes tame

**49→46/53/54, CS y conjugados.** En `ps:conj`/`pk:conj` se necesita |t_σ|²=Ω⁻¹, con Ω=2πexp(c_CS)/rd_E, no equivalencia hasta un algebraico. CJ01 contrastó la página original de Chowla–Selberg; CJ02–04 reconstruyeron modelo, buena reducción en2, unidad de normalización y reciprocidad. La identidad de área es (2π²exp(c_CS)/sqrt(d))^h. Al combinar |σ(varpi_vac)|²=rd_E/sqrt(d), c_ψ²=2π/sqrt(d) y areaΛ_σ=|Ω_σ|²sqrt(d)/2, resulta exactamente Ω⁻¹. En53 CL y54 normL se usa esta misma normalización. Las fases Weil requieren la reconstrucción independiente CJ05b; la fórmula fuerte δ_g impresa no queda convertida por ello en teorema literalmente comprobado.

**49→50→49.** 50 `ph:thm` controla colongitud truncada: col(Λ,YΛ+p^jΛ)|p^l, l≤(3c_d+θj)dimΛ. No promete media finita uniforme en j ni invertibilidad. En la aplicación se tiene ciclo par N=o/o₀, P=p^{o₀}≥5, q=P^N, n=a, r=ceil(log_p m), θ=(m²f)⁻¹. La libertad de aristas se comprueba por representantes integrales y nivel libre, no se reemplaza por libertad de vértices. HE01 verifica n⁴≤q y (Nk log(q)/θ)^5 P^{3r}≤n desde los datos. Se deduce precisamente12A_l/(mp)+j₀/(m²f) en `pa:eldiv`, y al iterar m·#Λ veces queda el término j_p/m declarado. `ph:root`, `ph:count`, `ph:av` fueron demostrados en la lectura algebraica; no son axiomas adicionales ocultos. La flecha inversa del apéndice50 que reproduce `pa:eldiv` y `pa:divis` es también una presentación de resultados de aplicación: no autoriza usarlos como premisas de la prueba abstracta. No se identificó circularidad en esa deducción.

**54→49/46, tame.** Relectura completa54:7499–7615, `pfq:roots`, `pfq:mu`, `pfq:def-chars`, `pfq:tame`; destino49:8968–8997 y49 `pz:mu` (Lemma8.6). La compatibilidad sobre μ_E es necesaria y suficiente porque U(1)(E⁺)∩U=μ_E y el carácter de un subgrupo abierto se extiende. D4 hace q₁|κ(τ), y p_i≡1 mod q₂² garantiza que cada raíz de unidad residual es potencia q₂. Así se eligen ω_w de orden exactamenteq₂ y μ_j⁰=μ^flat(upsilon^{-Δ}χ_M)^j con tameω_w^j. q₂≥m²²>8m asegura no trivialidad para1≤|n|≤8m, no sólo paraj=1. Los twists son no ramificados enM, por eso no cambian esas partes tame. Para ν^flat se cancela χ_M^jθ, dando independencia deθ. **(a) esta unión, rango y existencia; independiente del exchange defectuoso.**

## Norma de un lift, forma test y retorno a Selmer

| Unión específica | Comprobación matemática | Dictamen |
|---|---|---|
| 53 `pc:SW/clean/sharp/rallis`,897–1108 →54 `pex:rallis`,Prop3.4 | SW01 coteja Weil1965: ε=1/2, rango doblado M′>2n, normalización Haar de masa1. En fuente/target definidos de54 ambos cocientes son compactos. Doubling usa tensor con conjugado y cancela caracteres; no usa product53. | (a) especialización de rango uno y z≥2; no se extrapola a fuentes no compactas. |
| 54 `pex:vac`, `pex:arch`, `pex:rallis` →53 CL y54 `psu:normL` | Serie split=(1−q^{-2z})/((1−aq^{-z})(1−a^{-1}q^{-z})); inert1. Índices deM, factoresq^{2z−1} deQ y factoriales Fock se conservan; no nulidad z≥2 precede a CL. | (a), TL05/SW01. Esta vuelta53↔54 no es un círculo: CL no se usa para demostrar la no nulidad que recibe. |
| 49 `pl:vac` Lemma6.8 →54 `ppe:transfer` | Cosets dan Gaussian binomials; pasar un Hecke a través de la integral invierte el double coset y el lugar conjugado. Constantesα=q^{m_X/2},β=q^{n/2} conservadas. | (a), TL05. |
| 49 forma normal/count →54 `psm:katz/coupling/twelve/attained` | Doce copias y sumas finitas producen un coeficiente de valoración mínima; no se presupone alcanzabilidad sólo a partir de una cota inferior. TL02 contiene la prueba. | (a) segmento local reconstruido, todos los primos descritos, incluida rama ramificada. |
| 54 `psm:attained` → `psu:small` → `po:small` →46 `au:hecke` | t=M^{12f}c_vac,y∏B(l_τ)² cancela factores y factoriales; mínimo de una suma integral da la desigualdad unilateral necesaria. La versión corregida es fmb/k+3x³⁵ y46 la cita expresamente. | (a) transferencia de valuación y constante. Las propiedades globales de test form usan periods/tower; TL04 y el cierre independiente de bounded descent comunicado por spanning completan esa obligación, sin usar el exchange defectuoso. |
| 53 mixed laws/momentos →54 `ppe:zero/bdd/rallis`,tower | Ley del Levi reconstruida sobre Schwartz, donde cancelan factores upsilon del target. El slice NO es un operador acotado en HilbertL²; su uso requiere normas de momentos. Rango de tower para r=1,p=20:45<2z, satisfecho por flat pairs. | (a) ley local y rango; bounded descent cerrado por spanning: R2 con A≥2s, R3 y pcx:mean con l=A cancelan ht^Aδ^A, uniformemente en compactos. No usar la falsa acotación Hilbert como atajo. |
| 53 `pcj` CL →54 `psu:arch` → `po:arch` | Se exige el mismo a_σ(z) para par principal y flat; así se cancela con B(z). NormL es exacto, no sólo proporcional a unL-valor. El agente principal reconstruyó CL por reciprocidad49 y no nulidad54. | (a) reconstruido con CL cerrado por responsable53, normL y psu:I(b); se releyó9217–9255. No usa auxcore53. Véase COVOLUMEN y THETA TL05/SW01. |
| 54 `pex:IM`/`pex:IM1` →55 II | Expansión finita, factores Euler y cociente deL conservados; n_p puede depender del par pero no del twist/conductor. | (a) traslado bajo IM; z≥2 reconstruido. (c) rama z=1 por exchange53, según SELMER§13. |

## C275 — Cotejo semántico completado de las275 reproducciones

Se extrajeron los cuerpos completos de los275 entornos quoteddef/quotedthm y los cuerpos de sus enunciados fuente, no sólo sus títulos.188 coinciden tras normalizar espacios, etiquetas y referencias; se inspeccionaron manualmente los87 diffs restantes. Sólo cambian referencias internas por citas externas, numeración de ecuaciones/align y espaciado. No se identificó supresión de hipótesis, ampliación de cuantificadores o rangos, cambio de constante, signo, exponente o condición de no anulación.

Para evitar que la normalización ocultara una referencia incorrecta se compilaron en modo draft, en directorios aislados de evidencia, los papers46,49,50,51,52,53,54,55. Las ocho compilaciones terminaron con código0. Sus archivos aux resolvieron las referencias de cada enunciado y su reproducción: **las275 listas de referencias coinciden después de resolver su destino**, descontando las etiquetas de ecuación añadidas para mostrar el número de origen. Se inspeccionaron además los subincisos: por ejemplo L3 se conserva entre cite[2.2(L3)] y ref(po:facts)(L3), y K1/K2/S3 se mantienen cuando pasan a formar parte del argumento opcional de cite. El compendio de diferencias de referencias contiene89 grupos, todos compatibles.

También se extrajeron las definiciones newcommand/renewcommand/providecommand de todos los macros usados por estos cuerpos y su cierre transitivo. **Cero diferencias de definición entre fuente y destino.** Las definiciones matemáticas reproducidas como quoteddef se cotejaron con el mismo procedimiento; las definiciones remitidas mediante referencias conservan el mismo destino. Esto controla la interpretación del enunciado copiado en la notación de su fuente; no sustituye comprobar que los objetos de una aplicación posterior satisfagan esas definiciones.

Por tanto, la columna «Copia semántica» es **(a) en las275 filas**. La columna «Prueba/aplicación» permanece separada: puede ser(c), o estar afectada por una prueba fuente(b), aunque la copia sea fiel. En particular, copiar correctamente exchange53 no repara su error de caracteres. Los códigosP del inventario se refieren sólo a la comprobación de aplicación no individualizada por este agente, **ya no al cotejo del enunciado reproducido**.

Evidencia reproducible: `../evidencia/cotejo_275_theta.json`, `cotejo_275_theta.tsv`, `cotejo_275_theta_diffs.txt`, `cotejo_275_theta_referencias.txt`, `cotejo_275_theta_macros.json` (lista vacía); scripts `compare_theta_quotes.py`, `compare_theta_macros.py`, `check_theta_refs.py`; auxiliares `aux-cotejo/<paper>/main.aux`. Los scripts se ejecutan desde la raíz del repositorio. Los87 diffs incluyen alguna diferencia técnica del normalizador al retirar tag de una línea align; la lectura del fuente confirma que no se pierde un separador matemático real.

## Cómo leer el inventario exhaustivo de apéndices que sigue

Se enumeran **todos** los entornos quoteddef/quotedthm de los cuatro apéndices. Se vincula la cita numerada a la etiqueta y línea de su fuente mediante el contador theorem compartido por sección. El mapeo se guarda en `../evidencia/mapa_numeros_theta.json`; se contrastaron anclas ph:thm=2.2, ps:conj=5.7 y pfq:tame=6.15. Este inventario descubre también imports secundarios que no figuran en la tabla46.

Los códigos de evidencia significan: **HE**=THETA HE01 y álgebra50; **CM**=CJ01–08/CM01/KI01/LN01/BR01/AS01; **AR**=AR01–03 y SPANNING/FJ con errata reparada; **SW**=SW01, sólo especialización compacta indicada; **EX**=dependencia de exchange con fallo demostrado en product; **TAME**=relectura anterior; **P**=pendiente individual de comprobar la aplicación íntegra de esa etiqueta en el destino. Una filaP no afirma que el resultado fuente sea falso ni desconocido en toda la auditoría: identifica el límite de esta consolidación por agente, a resolver contra el ledger de su responsable. No se declara(a) por una extracción automática. En las filas secundarias, «segmento reconstruido» califica la prueba fuente y su aplicación descrita en el ledger; no certifica una aplicación adicional distinta sólo porque aparezca en el apéndice. Tal aplicación adicional mantiene (c) hasta identificar la instancia. Los responsables pueden sustituir P con sus pruebas concretas: P no es un fallo demostrado ni un pendiente global permanente.

### Apéndice de P49: 49 importaciones

| Línea destino | Fuente numerada | Etiqueta y línea fuente | Copia semántica | Evidencia | Prueba/aplicación |
|---:|---|---|---|---|---|
| 8343 | 46 13.1 | `an:def-param` (2886) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8349 | 46 13.3 | `an:def-data` (2954) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8383 | 46 13.4 | `an:lem-sizes` (2989) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8421 | 46 13.9 | `an:thm-data` (3198) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8430 | 46 14.5 | `au:free` (3598) | (a), C275 | HE | (a) libertad aplicada a aristas en HE01 |
| 8435 | 46 14.8 | `def:au-hmain` (3804) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8456 | 46 14.9 | `au:gains` (3833) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8479 | 46 14.10 | `au:count` (3900) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 8497 | 46 14.13 | `thm:srcA` (3993) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8516 | 46 14.18 | `au:errsum` (4213) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8521 | 46 14.19 | `au:seesaw` (4314) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 8533 | 46 14.20 | `au:divis` (4368) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 8558 | 46 14.21 | `au:shortbasis` (4427) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 8564 | 46 14.22 | `au:short` (4438) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8570 | 46 14.23 | `au:kernel` (4497) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 8580 | 46 14.24 | `au:restrict` (4516) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 8587 | 46 14.25 | `au:expansion` (4532) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 8595 | 46 14.26 | `au:size` (4544) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8604 | 46 14.27 | `au:equiv` (4584) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 8611 | 46 14.28 | `au:good` (4597) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8621 | 46 14.29 | `au:ramcount` (4619) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8625 | 46 14.32 | `au:moment` (4692) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8639 | 50 2.2 | `ph:thm` (396) | (a), C275 | HE | (a) instancia HE01; teorema truncado y rango, no media sin truncar |
| 8653 | 50 2.3 | `ph:col` (429) | (a), C275 | HE | (a) instancia HE01; teorema truncado y rango, no media sin truncar |
| 8663 | 50 2.10 | `ph:root` (661) | (a), C275 | HE | (a) instancia HE01; teorema truncado y rango, no media sin truncar |
| 8672 | 50 2.12 | `ph:count` (687) | (a), C275 | HE | (a) instancia HE01; teorema truncado y rango, no media sin truncar |
| 8677 | 50 2.13 | `ph:av` (696) | (a), C275 | HE | (a) instancia HE01; teorema truncado y rango, no media sin truncar |
| 8686 | 51 2.14 | `pb:lattice` (1027) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8719 | 51 4.7 | `pm:kernel` (4346) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8733 | 51 4.8 | `pm:cusp` (4377) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8738 | 51 4.43 | `pbr:degree` (5823) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8743 | 51 5.2 | `pds:haar` (6029) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8749 | 51 5.4 | `pds:blockdet` (6056) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8754 | 51 5.5 | `pds:fischer` (6070) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8759 | 51 5.6 | `pds:decay` (6102) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8768 | 51 5.10 | `pds:kappa` (6219) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8776 | 53 2.14 | `pc:clean` (961) | (a), C275 | SW | Fuente: (a) especialización compacta54 en SW01. Instancia destino49: (c) salvo la vuelta explícita54Prop3.4→53CL descrita arriba; revisar uso local de esta etiqueta. |
| 8793 | 53 3.27 | `pcx:def-ht` (2272) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8801 | 53 3.28 | `pcx:reduce` (2320) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8809 | 53 3.30 | `pcx:superpos` (2408) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8835 | 53 4.10 | `ptr:conv` (6761) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8855 | 53 4.40 | `ptv:rev` (7908) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8871 | 53 5.37 | `pgu:line` (10296) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8890 | 53 6.9 | `pgv:alpha` (11015) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8901 | 53 6.30 | `pgx:vac` (12086) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8908 | 53 6.31 | `pgx:conv` (12106) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8919 | 53 6.32 | `pgx:dict` (12140) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 8968 | 54 6.14 | `pfq:def-chars` (7558) | (a), C275 | TAME | (a) peso, orden q₂, independencia del twist en las partes tame |
| 8981 | 54 6.15 | `pfq:tame` (7571) | (a), C275 | TAME | (a) peso, orden q₂, independencia del twist en las partes tame |

### Apéndice de P50: 8 importaciones

| Línea destino | Fuente numerada | Etiqueta y línea fuente | Copia semántica | Evidencia | Prueba/aplicación |
|---:|---|---|---|---|---|
| 1545 | 49 4.2 | `pa:elim` (2538) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 1551 | 49 4.11 | `pa:partner` (2927) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 1559 | 49 4.17 | `pa:mark` (3123) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 1563 | 49 4.18 | `pa:hecke` (3149) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 1569 | 49 4.19 | `pa:eldiv` (3156) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 1576 | 49 4.21 | `pa:divis` (3184) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 1602 | 49 6.3 | `pl:wa` (5932) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 1608 | 49 6.4 | `pl:wacor` (5953) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |

### Apéndice de P53: 120 importaciones

| Línea destino | Fuente numerada | Etiqueta y línea fuente | Copia semántica | Evidencia | Prueba/aplicación |
|---:|---|---|---|---|---|
| 16079 | 46 13.4 | `an:lem-sizes` (2989) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16117 | 46 14.1 | `def:au-height` (3394) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16124 | 46 14.3 | `def:au-lattice` (3425) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16154 | 46 14.4 | `au:twistprime` (3461) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16170 | 46 14.5 | `au:free` (3598) | (a), C275 | HE | (a) libertad aplicada a aristas en HE01 |
| 16175 | 46 14.8 | `def:au-hmain` (3804) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16196 | 46 14.15 | `thm:srcC` (4020) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16204 | 46 14.21 | `au:shortbasis` (4427) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 16210 | 46 14.22 | `au:short` (4438) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16216 | 46 14.23 | `au:kernel` (4497) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 16226 | 46 14.27 | `au:equiv` (4584) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 16233 | 46 14.28 | `au:good` (4597) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16243 | 46 14.35 | `au:inj` (4794) | (a), C275 | EX | (c) conclusión condicionada al exchange, véase fila individual |
| 16248 | 46 14.36 | `au:mult` (4812) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16260 | 46 14.37 | `au:factor` (4850) | (a), C275 | EX | (c) conclusión condicionada al exchange, véase fila individual |
| 16275 | 46 14.38 | `au:aux` (4878) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16284 | 46 14.39 | `def:au-regular` (4895) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16305 | 46 14.40 | `au:regular` (4921) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16309 | 46 14.41 | `au:onelift` (4965) | (a), C275 | EX | (c) conclusión condicionada al exchange, véase fila individual |
| 16325 | 46 14.42 | `au:hecke` (4992) | (a), C275 | CM+SW | (a) deducción con familia regular dada; existencia de familia es otro input |
| 16330 | 46 14.43 | `au:Zj` (5013) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16335 | 49 2.1 | `pwf:def` (589) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16364 | 49 2.3 | `pwf:dist` (650) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16374 | 49 2.4 | `pwf:siegel` (690) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16378 | 49 2.5 | `pwf:sum` (740) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16385 | 49 2.17 | `pwf:W5` (1101) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16398 | 49 3.2 | `par:A1` (1421) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16406 | 49 3.3 | `par:A2` (1444) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16413 | 49 3.4 | `par:D3` (1491) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16417 | 49 3.5 | `par:rigid` (1516) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16425 | 49 3.6 | `par:vac` (1564) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16440 | 49 3.7 | `par:match` (1613) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16444 | 49 3.9 | `par:def-harm` (1642) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16452 | 49 3.10 | `par:relw` (1654) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16458 | 49 3.11 | `par:exist` (1680) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16468 | 49 3.12 | `par:polar` (1711) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16476 | 49 3.13 | `par:unique` (1730) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16480 | 49 3.14 | `par:casimir` (1753) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16488 | 49 3.15 | `par:A3` (1776) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16498 | 49 3.17 | `pco:FJ` (1876) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16502 | 49 3.18 | `pco:minors` (1898) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16517 | 49 3.19 | `pco:equiv` (1938) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16531 | 49 3.20 | `pco:density` (1968) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16536 | 49 3.21 | `pco:indep` (2029) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16542 | 49 3.22 | `pco:local` (2084) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16549 | 49 3.23 | `pco:K` (2097) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16561 | 49 3.25 | `pco:decay` (2148) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16566 | 49 3.29 | `pco:V` (2337) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16573 | 49 5.2 | `ps:weil` (3428) | (a), C275 | CM | (a) propiedades usadas reconstruidas; (c) fórmula fuerte δ_g si se la exige literalmente |
| 16622 | 49 5.4 | `ps:transfer` (3589) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16628 | 49 5.5 | `ps:level` (3730) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16635 | 49 5.7 | `ps:conj` (3845) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16650 | 49 5.8 | `ps:monomial` (3862) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16656 | 49 5.14 | `pk:cauchy` (4557) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16665 | 49 5.22 | `pk:hook` (5085) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 16672 | 49 5.24 | `pk:branching` (5131) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16679 | 49 5.26 | `pk:dict` (5354) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 16691 | 49 5.27 | `pk:conj` (5433) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16697 | 49 5.30 | `pk:K12` (5606) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 16702 | 49 6.4 | `pl:wacor` (5953) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16713 | 49 7.9 | `pf:recip` (7111) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 16729 | 49 7.11 | `pf:frame` (7210) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 16733 | 49 7.13 | `pf:semi` (7284) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 16744 | 49 7.15 | `pf:std` (7362) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 16758 | 49 7.17 | `pf:flip` (7455) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16775 | 49 7.20 | `pf:classes` (7605) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16789 | 49 8.1 | `pz:def-type` (7759) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16803 | 49 8.2 | `pz:growth` (7791) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16816 | 49 8.3 | `pz:absgrowth` (7850) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16843 | 49 8.4 | `pz:types` (8021) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16865 | 49 8.5 | `pz:lastlevel` (8124) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16875 | 49 8.7 | `pz:C0` (8191) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16887 | 49 8.8 | `pz:sizes` (8235) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16899 | 51 4.6 | `pm:mult` (4331) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16912 | 51 4.7 | `pm:kernel` (4346) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16926 | 51 4.8 | `pm:cusp` (4377) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16931 | 51 4.9 | `pm:siegel` (4442) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16946 | 51 4.10 | `pm:decay` (4515) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16955 | 51 4.11 | `pm:bound` (4562) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16966 | 51 5.1 | `pds:chamber` (5983) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16977 | 51 5.2 | `pds:haar` (6029) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16983 | 51 5.4 | `pds:blockdet` (6056) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16988 | 51 5.5 | `pds:fischer` (6070) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 16993 | 51 5.6 | `pds:decay` (6102) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17002 | 51 5.7 | `pds:lip` (6138) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17006 | 51 5.9 | `pds:tail` (6185) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17015 | 51 7.10 | `pbp:residue` (7035) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17021 | 51 7.16 | `pbp:third` (7199) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17029 | 51 7.17 | `pbp:second` (7229) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17034 | 51 7.18 | `pbp:minorsize` (7254) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17039 | 51 7.19 | `pbp:minorconj` (7266) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17052 | 51 7.20 | `pbp:reduced` (7320) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17060 | 51 7.21 | `pbp:dLambda` (7349) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17064 | 51 7.22 | `pbp:gauss` (7367) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17069 | 51 7.25 | `pbp:rows` (7430) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17074 | 51 7.26 | `pbp:leftX` (7451) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17078 | 51 7.27 | `pbp:far` (7463) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17082 | 51 7.28 | `pbp:localise` (7472) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17087 | 51 7.29 | `pbp:cone` (7492) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17091 | 51 7.31 | `pbp:cover2` (7535) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17095 | 51 8.22 | `pbc:pack` (8356) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17102 | 51 8.32 | `pbc:tb-covol` (8695) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17108 | 51 8.34 | `pbc:siegel` (8727) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17116 | 54 2.1 | `po:naut` (478) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17123 | 54 2.2 | `po:facts` (544) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17136 | 54 2.15 | `po:exchange` (995) | (a), C275 | EX | (c) recibe exchange53 no demostrado por la ruta escrita |
| 17148 | 54 2.24 | `po:arch` (1411) | (a), C275 | CM+SW | (a) arch reconstruido con CL y normL; no depende de auxcore |
| 17153 | 54 3.2 | `pex:vac` (1639) | (a), C275 | SW | Fuente: (a) especialización compacta54 en SW01. Instancia destino53: (c) salvo la vuelta explícita54Prop3.4→53CL descrita arriba; revisar uso local de esta etiqueta. |
| 17166 | 54 3.3 | `pex:arch` (1688) | (a), C275 | SW | Fuente: (a) especialización compacta54 en SW01. Instancia destino53: (c) salvo la vuelta explícita54Prop3.4→53CL descrita arriba; revisar uso local de esta etiqueta. |
| 17173 | 54 3.4 | `pex:rallis` (1713) | (a), C275 | SW | Fuente: (a) especialización compacta54 en SW01. Instancia destino53: (c) salvo la vuelta explícita54Prop3.4→53CL descrita arriba; revisar uso local de esta etiqueta. |
| 17189 | 54 4.3 | `plf:A12` (3554) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17197 | 54 4.7 | `plf:harm` (3685) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17202 | 54 4.8 | `plf:L4` (3700) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17209 | 54 4.10 | `plf:KS` (3792) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17223 | 54 5.39 | `psr:series` (5943) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17233 | 54 5.40 | `psr:SW` (5987) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17239 | 54 5.41 | `psr:Egrowth` (6017) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17245 | 54 7.27 | `psu:flat` (8714) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 17259 | 54 7.43 | `psu:arch` (9217) | (a), C275 | CM+SW | (a) arch reconstruido con CL y normL; no depende de auxcore |
| 17264 | 55 6.7 | `pga:L` (4010) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |

### Apéndice de P54: 98 importaciones

| Línea destino | Fuente numerada | Etiqueta y línea fuente | Copia semántica | Evidencia | Prueba/aplicación |
|---:|---|---|---|---|---|
| 9261 | 46 13.1 | `an:def-param` (2886) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9267 | 46 13.2 | `an:def-sparse` (2930) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9278 | 46 13.3 | `an:def-data` (2954) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9312 | 46 13.4 | `an:lem-sizes` (2989) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9350 | 46 14.1 | `def:au-height` (3394) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9357 | 46 14.5 | `au:free` (3598) | (a), C275 | HE | (a) libertad aplicada a aristas en HE01 |
| 9362 | 46 14.6 | `def:au-target` (3674) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9367 | 46 14.8 | `def:au-hmain` (3804) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9388 | 46 14.9 | `au:gains` (3833) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9411 | 46 14.10 | `au:count` (3900) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 9429 | 46 14.15 | `thm:srcC` (4020) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9437 | 46 14.21 | `au:shortbasis` (4427) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 9443 | 46 14.23 | `au:kernel` (4497) | (a), C275 | CM | Véase fila individual arriba: resultado de destino, no premisa independiente circular |
| 9453 | 46 14.37 | `au:factor` (4850) | (a), C275 | EX | (c) conclusión condicionada al exchange, véase fila individual |
| 9468 | 46 14.39 | `def:au-regular` (4895) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9489 | 46 14.41 | `au:onelift` (4965) | (a), C275 | EX | (c) conclusión condicionada al exchange, véase fila individual |
| 9505 | 46 14.42 | `au:hecke` (4992) | (a), C275 | CM+SW | (a) deducción con familia regular dada; existencia de familia es otro input |
| 9510 | 46 14.43 | `au:Zj` (5013) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9515 | 49 2.14 | `pwf:W2` (1003) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9533 | 49 2.20 | `pwf:delta-red` (1206) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9540 | 49 2.21 | `pwf:eplus` (1229) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9547 | 49 3.2 | `par:A1` (1421) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9555 | 49 3.3 | `par:A2` (1444) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9562 | 49 3.5 | `par:rigid` (1516) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9570 | 49 3.6 | `par:vac` (1564) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9585 | 49 3.9 | `par:def-harm` (1642) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9593 | 49 3.10 | `par:relw` (1654) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9599 | 49 3.11 | `par:exist` (1680) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9609 | 49 3.14 | `par:casimir` (1753) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9617 | 49 3.15 | `par:A3` (1776) | (a), C275 | AR | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9627 | 49 3.17 | `pco:FJ` (1876) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9631 | 49 3.29 | `pco:V` (2337) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9638 | 49 4.5 | `pa:model` (2705) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9644 | 49 4.6 | `pa:param` (2743) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9657 | 49 4.7 | `pa:units` (2809) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9667 | 49 4.9 | `pa:onecurve` (2861) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9678 | 49 4.12 | `pa:product` (2953) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9689 | 49 4.13 | `pa:kernel` (3006) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9721 | 49 5.2 | `ps:weil` (3428) | (a), C275 | CM | (a) propiedades usadas reconstruidas; (c) fórmula fuerte δ_g si se la exige literalmente |
| 9770 | 49 5.7 | `ps:conj` (3845) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9785 | 49 5.22 | `pk:hook` (5085) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9792 | 49 5.25 | `pk:curve` (5215) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9820 | 49 5.26 | `pk:dict` (5354) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9832 | 49 5.27 | `pk:conj` (5433) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9838 | 49 5.30 | `pk:K12` (5606) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9843 | 49 6.4 | `pl:wacor` (5953) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9854 | 49 6.8 | `pl:vac` (6092) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9863 | 49 6.9 | `pl:onelift` (6123) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 9873 | 49 7.1 | `pf:chi` (6815) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9890 | 49 7.2 | `pf:two` (6848) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9897 | 49 7.3 | `pf:CS` (6911) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9903 | 49 7.4 | `pf:eps` (6941) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9910 | 49 7.5 | `pf:values` (6985) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9919 | 49 7.6 | `pf:pull` (7023) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9932 | 49 7.9 | `pf:recip` (7111) | (a), C275 | CM | (a) segmento reconstruido; conserva hipótesis del enunciado fuente |
| 9948 | 49 7.11 | `pf:frame` (7210) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9952 | 49 7.12 | `pf:scale` (7250) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9959 | 49 7.13 | `pf:semi` (7284) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9970 | 49 7.14 | `pf:fourier` (7314) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9978 | 49 7.15 | `pf:std` (7362) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 9992 | 49 7.16 | `pf:K1` (7404) | (a), C275 | CM | (a) consecuencias CM/integrales usadas; salvedad fase fuerte δ_g en texto principal |
| 10004 | 49 7.20 | `pf:classes` (7605) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10018 | 49 8.1 | `pz:def-type` (7759) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10032 | 49 8.2 | `pz:growth` (7791) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10045 | 49 8.4 | `pz:types` (8021) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10067 | 49 8.6 | `pz:mu` (8144) | (a), C275 | TAME | (a) compatibilidad de caracteres y rango explicitados arriba |
| 10080 | 49 8.7 | `pz:C0` (8191) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10092 | 51 4.7 | `pm:kernel` (4346) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10106 | 51 5.6 | `pds:decay` (6102) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10115 | 51 5.9 | `pds:tail` (6185) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10124 | 51 5.10 | `pds:kappa` (6219) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10132 | 53 2.9 | `pc:level` (705) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10142 | 53 2.10 | `pc:arch` (749) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10158 | 53 2.11 | `pc:series` (780) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10177 | 53 2.13 | `pc:SW` (897) | (a), C275 | SW | (a) especialización compacta de54; generalidad no compacta requiere COVOLUMEN |
| 10215 | 53 2.14 | `pc:clean` (961) | (a), C275 | SW | (a) especialización compacta de54; generalidad no compacta requiere COVOLUMEN |
| 10232 | 53 2.15 | `pc:sharp` (1007) | (a), C275 | SW | (a) especialización compacta de54; generalidad no compacta requiere COVOLUMEN |
| 10242 | 53 2.16 | `pc:rallis` (1017) | (a), C275 | SW | (a) especialización compacta de54; generalidad no compacta requiere COVOLUMEN |
| 10255 | 53 2.18 | `pc:algpet` (1128) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10263 | 53 3.1 | `pcx:def-matched` (1757) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10273 | 53 3.2 | `pcx:X` (1767) | (a), C275 | EX | (c) import no justificado por la prueba de exchange; fallo(b) en product3359 |
| 10297 | 53 3.4 | `pcx:cne0` (1843) | (a), C275 | EX | (c) import no justificado por la prueba de exchange; fallo(b) en product3359 |
| 10301 | 53 3.24 | `pcx:mod` (2098) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10310 | 53 3.26 | `pcx:decay` (2257) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10323 | 53 3.27 | `pcx:def-ht` (2272) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10331 | 53 3.28 | `pcx:reduce` (2320) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10339 | 53 3.29 | `pcx:thetagrowth` (2368) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10350 | 53 3.30 | `pcx:superpos` (2408) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10376 | 53 3.32 | `pcx:mean` (2521) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10392 | 53 3.34 | `pcx:conv` (2639) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10402 | 53 3.62 | `pcu:laws` (3766) | (a), C275 | CM | (a) ley sobre Schwartz con normas de momentos; no acotación Hilbert |
| 10413 | 53 4.24 | `ptq:vac` (7256) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10418 | 53 6.9 | `pgv:alpha` (11015) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10429 | 53 6.30 | `pgx:vac` (12086) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10436 | 53 6.31 | `pgx:conv` (12106) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10447 | 53 6.32 | `pgx:dict` (12140) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
| 10496 | 53 9.1 | `pcj:CL` (15463) | (a), C275 | CM+SW | (a) CL reconstruido por responsable53; misma constante por rango |
| 10505 | 55 2.2 | `pg:main` (440) | (a), C275 | P | (c) aquí: cotejar hipótesis y uso de esta etiqueta en el destino; responsable según fila principal |
