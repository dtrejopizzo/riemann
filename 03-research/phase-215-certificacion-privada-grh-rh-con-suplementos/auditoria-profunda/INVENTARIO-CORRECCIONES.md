> **V1: registro histórico, revisado en V2.** No aplicar sus objeciones de caracteres ni sus estados de propagación a los manuscritos corregidos sin consultar el [estado V2](../revision-v2/ESTADO.md). La cancelación especializada de caracteres corrige el impacto global atribuido en V1; se están consolidando los demás resultados.

# Inventario de correcciones para el autor

Consolidación del 28-11-2026. Se refiere a las fuentes `04-papers/NN-*/main.tex` examinadas; los números siguientes son líneas de esas fuentes. No se modificaron los papers. Los dictámenes **(b)** se aplican a la afirmación o inferencia expresamente identificada, y no por extensión automática a todos los teoremas del paper. Una reparación reconstruida por la auditoría debe incorporarse al texto antes de calificarlo como correcto tal como está escrito.

## 1. Prioridad crítica para la conclusión global

### P53 — caracteres de `pcu:product` y el período posterior

**(b), igualdad3351–3352; primera inferencia inválida3359–3360.** Con la definición `ω_{α,β}(g,h)=α(det g)⁻¹β(det h)ω_Hom(g,h)`, el cociente entre ambos lados es

`α(det g) α(det y) β(det l)`.

No es una constante de normalización. En `pcu:period`3407–3410, l=u es una variable integrada: queda el factor β(det u) dentro del período y no puede retirarse por tener módulo uno. El defecto aparece también en P58:37993–37994. Fue comprobado independientemente por dos frentes de revisión.

**Qué corregir:** fijar los caracteres de fuente/destino en cada bloque; recalcular `pcu:period` y `pcu:coeff`; identificar el período resultante con el que necesita la razón de rango igual; demostrar no anulación y módulo exacto de la constante. Rehacer luego `P-top`, `P-std`, `P-equal` y `pcx:X`. Cambiar sólo un nombre de carácter no conserva los dos períodos usados: un carácter único de destino se restringe igual a ambos bloques.

**Estado:** no hay reparación global demostrada. La ruta escrita al intercambio, y por ella al Covolume Theorem y a la conclusión global, no queda certificada. Esto no prueba que exchange sea falso ni que RH sea falsa. [Cálculo y cadena de dependencias](ERROR-53-CARACTERES.md); [uso adicional en `pct:vantop`,5632–5634](PLANO-53.md).

## 2. Reparaciones locales demostradas

| Paper / punto | Dictamen y primera línea | Cambio que debe incorporarse | Efecto comprobado |
|---|---|---|---|
| 46, pairing polar complejo | **b**,277: `2Re(a conjugate(b′))` se llama hermitiana | Escribir `a conjugate(b′)+b conjugate(a′)`. La expresión anterior da2 en un orden y0 en el inverso para(1,0),(0,1). | La diagonal2Re(a conjugate(b)) ya es correcta; no cambia W_T. |
| 46, `thm:coer-A` | **b** local2094: máximo en(2R²−a)/3 para todo R | Si R²<a/2 el punto está fuera del intervalo. Acotar con y=x+a y `y²(R²+a−y)≤4(R²+a)^3/27` en el intervalo mayor[0,R²+a]. | Misma cota M_R para todo R; mismas constantes; R=2 ya estaba en el rango interior. |
| 49, Flensted–Jensen | **b**,2250–2251: cambiar F(xh) por traslación derecha declarada R(x)F(h)=F(hx) | Partir directamente de `F(g)=∫e(h)F(gh)dh`; sustituir x=gh y usar `e(h)=d c(h⁻¹)`. Resulta `F(g)=d∫F(x)c(x⁻¹g)dx`. | Evita la doble integral incorrecta; preserva constante y Steps2–4, sin centralidad de F. |
| 51, `pm:siegel(c)` | **b**,4453, repetido4511–4512: convergencia uniforme en todo g | Exigir g y x en compactos para convergencia uniforme de la serie. Conservar por separado la cota global de la suma total. | Continuidad local y convolución por e∈L1 permanecen justificadas. No confundir cota uniforme de sumas con colas uniformemente pequeñas. |
| 51, `pbo:tube` | **b**,10499–10500: dimensión homogénea incorrecta | Sustituir `Q=2ρk+ρ²` por `Q=2ρk+2ρ²`, pues σ escala por t². | Sigue Q≤r²/2, `(1+1/Q)^Q<3`, norma≤T⁹≤T¹⁰; conserva factor3 y exponente10⁵n⁴ de O1. |
| 52, `pff:offT` | **b**,4364–4365: u→0 hace contraerse el corte frecuencial | Tomar u=varpi₁^(−j), j→∞, o usar directamente el agotamiento B_l de `pfg:orth/fibres`,4970–5080. | Frecuencias agotan el espacio y duales se contraen. La dominación uniforme ya demostrada conserva constante de Siegel→fibras→cuadrados orbitales. |
| 52, acción de `U_(<l)` | **b**,1810: dice que fija cada e_b,b<l | Sustituir por preservación de la bandera y acción unitriangular; puede enviar e₁ a e₁+a e₀. | Los usos efectivos requieren congruencia módulo la bandera inferior y trivialidad sobre Y^(l), que siguen válidas. |
| 53, `pcx:decay` | **b** en alcance2257–2269; inferencia2622–2627 requiere lugar inexistente si P=∅ | Añadir P≠∅ en la hipótesis de convergencia y propagarla a `pcx:conv` cuando se cite fuera del contexto de exchange. | En `pcx:X` el módulo no trivial ya aporta un lugar. El enunciado literal vacío sí tiene contraejemplo: fuente0, destino hiperbólico, theta=1 y altura no acotada. |
| 53, `pcu:mixedmodel/slicedecay` | **b**,4409–4410: evaluación puntual Hilbert-acotada | Definir sl(x) sobre trasladados coherentes y extender en normas de momentos. Probar `(1+|x|)^M||sl(x)v||_N≤C||v||_(N+M)` antes de intercambiar integrales. | En modelo L2, φ(x/ε)v₀ tiene norma→0 y valor fijo en0, refutando la frase Hilbert. La reconstrucción en normas de momentos conserva M1, `P-slice` y su constante κ. |
| 55, M3 | **b**,883: todos los roots tienen orden divisor de p_i^r−1 | Para factor de grado d_k usar p_i^(d_k)−1; no se supone d_k|r. El primo que divide ese orden divide #GL_rt y N_ch. | Conserva `v_l(det(R(γ)−1))≤r v_l(N_ch)`; M4/M5 usan lugar primitivo y no requieren cambio. |
| 55, G4 | **b** en justificación3946–3949: norma F_(q^n)→F_(q^d), d=lcm(d_k), inexistente si d no divide n | Elegir generador topológico tame y raíces compatibles; usar directamente θ_d(s) y sus proyecciones a d_k|d. | Grados2,3 dan n=5,d=6. La reparación conserva G4; elegir sólo θ_n(s) generador no basta. |
| 55, `pri:BL(c)` | **b**,2271 y6556–6560: un polinomio fijo mata todos los s∈I_w | Restringir al generador tame normalizado necesario en `pri:columns`,2855–2865, o definir o_(w,s) con raíces evaluadas en s. | Para s=γ² las raíces se elevan al cuadrado. La aplicación usa un generador y conserva sus cotas. P56 ya distingue M_s,q_s y no contiene este mismo error. |

Evidencia y demostraciones: [46](CHECKLIST-46-PURO.md), [49/51/52](SPANNING.md), [uniformidad51](MULTIPLICIDADES.md), [convergencia y topología53](COVOLUMEN.md), [55](SELMER.md). Estas reparaciones no solucionan la incompatibilidad crítica de caracteres de53.

### P55 — uniformar «base level» y preservar el tipo e_c

**Discrepancia de formulación y construcción omitida, reparada en la auditoría; no contraejemplo al teorema pg:III.** `prm:def-level`7527–7543 define F(O) sin condición e_c. `prm:label`7606 sí exige e_cy=y. `pri:BL(c)`2265–2273 y la elección de Y en3094–3098 hablan de todos los sistemas de base level; la prueba6467–6471 necesita el tipo e_c. La subsección6430–6437 declara una convención restringida, pero debe propagarse a los enunciados y a Y.

No basta proyectar el operador de Higman por e_c, porque introduciría denominadores no controlados. La reparación reconstruida es trabajar en nivel libre J₁ y promediar el indicador Ψ₁ por `D=Π_(w chosen)GL_n(F_w)`:

`Ψ_D=Σ_(d∈D)d⁻¹Ψ₁d`.

Las acciones de D y del grupo auxiliar Γ conmutan, por tener soportes disjuntos. Ψ_D es integral y D-invariante; preserva las invariantes del nivel y el tipo e_c. Su suma de conjugados auxiliares vale #D. Se toma c₀=#D, y #D divide N_ch; las estimaciones sólo necesitaban esa divisibilidad. Así se conserva β_l y no se paga por un proyector fraccionario.

**Acción del autor:** restringir explícitamente BL y Y al tipo e_c y reemplazar la construcción del operador por ésta, demostrando las conmutaciones y divisibilidades. No describir el operador original como si ya tuviera esa invariancia. [SELMER§11.2](SELMER.md).

### Dos reparaciones adicionales de las estimaciones auxiliares de P53

- **(b) `pgq:slice`, 13740–13742:** el producto `(g(r₀⊕1))⁻¹g(r⊕1)` es `(r₀⁻¹r)⊕1`, no `(rr₀⁻¹)⊕1`. Reemplazar en toda la demostración `rr₀⁻¹` por `r₀⁻¹r` e integrar por invariancia **izquierda**. Como `||g(r₀⊕1)||=t₀`, la norma de su inversa es también t₀ y t₀≤||g(r⊕1)||. Resulta la misma dominación y exactamente `2·16^(n²)Vτ`, por `pgq:balls` con s/2. El lema se conserva; la igualdad escrita es incorrecta.
- **(b) `pgk:lat(c)`, 14549–14551:** preservar la forma unimodular no implica que `det x_f` sea una unidad en cada lugar de E. En un lugar escindido, U(1)(F_v) contiene `(π,π⁻¹)`. Sustituir esa frase por el cálculo del módulo total: los valores absolutos de los determinantes en dos lugares conjugados se cancelan, y en un lugar no escindido el determinante tiene norma uno y valoración cero. Por tanto el jacobiano finito total es uno; el covolumen declarado y su constante se conservan. Véase [AUXCORE-53-54](AUXCORE-53-54.md).

## 3. Lagunas (c) y obligaciones no sustituidas por una errata

- **P53, consecuencias del período torcido:** además del fallo(b) ya demostrado, permanece sin verificación una nueva prueba que conserve no anulación y factor L de exchange después de corregir los caracteres. No hay aquí autorización matemática para dar el Covolume Theorem como reparado.
- **P46:2405–2409, comparaciones finitas:** el texto las declara sin prueba. No se verificaron la positividad para hasta cuatro exponentes arbitrarios ni la cota para trece polos con multiplicidades. No se usan en la proposición ladder. La identidad de todos los grados2411–2428 sí fue reconstruida, pero está explícitamente condicionada al input aritmético; no elimina la obligación global de53.
- **P49, fórmula más fuerte W4 para δ_g:** no se cotejó literalmente la descomposición del coeficiente en una raíz de unidad, una potencia de índice y un valor de υ. THETA reconstruye por separado las consecuencias efectivamente usadas: módulo en cada conjugado e integralidad local. Conviene demostrar la fórmula completa o enunciar sólo las consecuencias justificadas; no confundir ese alcance limitado con un fallo de dichas consecuencias.
- **Novedad y prioridad:** una conexión reconstruida no demuestra prioridad histórica. Las afirmaciones de novedad integral requieren comparación especializada con fuentes primarias; el informe de conexiones distingue antecedentes, mecanismos verificados y propuestas pendientes.

Este apartado no rescata pendientes históricos que las tandas posteriores ya cerraron. Para el dictamen por cada pregunta y el certificado de T=2.8022 debe consultarse la matriz final del frente principal y VENTANA-28022, no una lista antigua de tareas.

## 4. Datos editoriales y presentación de certificados

1. **P46:1896–1899.** ε9≤0.01567 es cierto con el valor preciso de γ1, certificado en `evidencia/Z1_margin_46_arb.json`. Pero no se deduce sólo de γ1≥14.13: éste da0.0157505828. Usar ε≤0.016 conserva exactamente el denominador0.484 y la cota final; alternativamente declarar el intervalo preciso usado. Es una precisión de dependencia, no una refutación del decimal verdadero.
2. **P46, certificados de log5/2.** Incorporar o enlazar los programas y salidas con versión, precisión, restos y método efectivo. Las cuatro inercias pasaron con congruencia precondicionada y Gershgorin; la factorización intervalar ingenua falló por acumulación de dependencia. No presentar ese fallo computacional como signo negativo ni afirmar que aquel algoritmo pasó. NUMERICA-46 documenta el certificado positivo que sí pasó.
3. **Redondeos ilustrativos.** Separar números decimales descriptivos de cotas racionales/intervalares usadas. No sustituir automáticamente una constante exacta por su redondeo hacia abajo en un certificado.
4. **P58 y apéndices.** Propagar las correcciones a las reproducciones de enunciados y pruebas; en particular, el fallo de caracteres está también en58. Volver a comprobar hipótesis P≠∅, tipo e_c, generador tame y topología de momentos en las uniones, además de igualdad textual.
5. **Atribución de revisión.** Los especialistas mencionados por el autor no han avalado este informe. No se enviaron mensajes a ellos. La auditoría de agentes y los certificados reproducidos deben identificarse como tales.

## Orden práctico de revisión del manuscrito

Primero resolver la identidad de caracteres y su período: es la obligación que impide certificar la cadena global. En paralelo pueden incorporarse las reparaciones locales demostradas, cada una con su prueba breve. Después actualizar apéndices/58 y volver a verificar las uniones afectadas. Finalmente incorporar los certificados reproducibles y decidir si se mantienen las afirmaciones auxiliares sin prueba. Ninguno de estos pasos requiere modificar los valores de corte T fijados por el autor.
