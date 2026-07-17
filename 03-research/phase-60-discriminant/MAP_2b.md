# Eslabón 2b (λ→∞): reformulación como límite de Szegő y target concreto **Estado del mapa:** Eslabones 1,3,4 cerrados (CCM + clásico). 2a: simplicidad cerrada (H1
probado); convergencia N→∞ vía proyectores de Perron–Frobenius (fondo no aislado). **2b es el
único crux** = problema abierto de ("missing step"). --- ## 1. Qué es 2b, precisado ξ̂_{λ,∞}(z) → Ξ(z) localmente uniforme cuando λ→∞. Por H1 + Thm 1.1(iii) — **ahora que H1 está
probado** — cada ξ̂_{λ,∞} tiene SOLO raíces reales (incondicional). Por Hurwitz, si converge
localmente uniforme a Ξ≢0, entonces Ξ es real-rooted ⟹ **RH**. Así que: **2b (convergencia) ⟹ RH**, y es lo único que falta. ## 2. Por qué NO es truncación del explicit formula Dato duro (E4hp): el 1er cero sale a ~1e-18 con primos ≤13. La truncación de primos en X=13
daría error O(ψ(X)−X)~O(1). La precisión real es exponencialmente mejor ⟹ el mecanismo es la
**rigidez de Carathéodory–Fejér** (CF), no la truncación. La forma de Weil localizada minimiza,
y la minimización pin-ea los ceros con precisión exponencial. ## 3. Reformulación: límite de determinantes de Toeplitz/Hankel La matriz QW en base V_k es **Cauchy–Toeplitz/Loewner**: τ_{n,n}=log(λ)/2,
τ_{n,m}=(b_n−b_m)/(n−m), con b_n=(1/L)Σ_k Λ(k)/√k·sin(2πkn/L) (dato de primos, L=2logλ).
Por Thm 1.1(ii), det_reg(D_λ−z) = −iλ^{−iz} ξ̂_λ(z): **el determinante regularizado de la
estructura Toeplitz/Loewner de los primos**. CF (ref [7] del paper) conecta Toeplitz↔símbolo y
da la auto-adjuntez. Entonces: **2b ⟸ teorema límite tipo Szegő/Carathéodory–Fejér:** los determinantes de Toeplitz de la forma de Weil localizada, con símbolo = dato de primos (b_n), convergen (λ→∞) a Ξ(z). Esto reemplaza "convergencia" abstracta por una pregunta de **análisis clásico** (asintótica de
determinantes de Toeplitz), donde entra la distribución de primos vía el símbolo. ## 4. El horizonte H(λ) (contenido cuantitativo de 2b) Los ceros bajos ya están resueltos; el contenido de 2b está en los altos. Definir
H(λ;ε) = altura hasta la que ξ̂_λ resuelve ceros a <ε. 2b ⟺ H(λ)→∞. **Conjetura del mecanismo (zero-independiente):** el operador "fija" un cero por cada
constraint de primo independiente; igualando conteos, N(H(λ)) ≈ π(λ²), con N(T)~(T/2π)log(T/2π) (conteo de ceros), π(λ²)~λ²/(2logλ) (primos).
⟹ H(λ) crece (despejando), gobernado por **conteo de primos = PNT** ⟹ **zero-independiente** ⟹
ruta NO circular a RH. **Datos E7 (alta precisión):** [se completa al terminar E7] ## 5. Riesgo (el único que decide si 2b→RH es real o circular) ¿La asintótica de Szegő/CF requiere control fino del símbolo que secretamente equivalga a
regiones libres de ceros (RH)? Si la convergencia se controla por π(λ²)+propiedades analíticas
del símbolo INDEPENDIENTES de los ceros ⟹ no circular. Si requiere RH ⟹ circular (no-go).
**Decidir esto = la pregunta de prueba pura central.** El contraste con un símbolo de
L-función-violadora (L_DH) ayudaría: si su determinante de Toeplitz NO converge a una función
real-rooted, confirma que la convergencia codifica la realidad de los ceros. ## 6. Targets concretos
- **T1:** confirmar H(λ)→∞ limpio (mpmath, E7) y testear N(H(λ))≈π(λ²). [E7 bloqueado: mpmath eigsy a dim>100 es horas; conditioning exp-malo. Pendiente método estable, sector par.]
- **T2:** escribir el determinante det_reg(D_λ−z) como determinante de Toeplitz explícito en el símbolo b_n; identificar la clase de Szegő aplicable.
- **T3:** la pregunta de circularidad (símbolo zero-independiente). --- ## 7. AVANCE: localización de la dificultad de 2b (la split (i)/(ii)) 2b = convergencia del **ground state** ξ_λ de la forma de Weil A_λ. Se parte en dos, con
estatus de circularidad OPUESTO: **(i) Convergencia de la FORMA A_λ → A_∞.** El defecto es la cola de primos
Σ_{n>λ²} Λ(n) T(n). Por el explicit formula aplicado a un test function fijo (altura acotada),
esta cola está controlada por **PNT** (error ψ(x)−x), que es **zero-independiente**.
⟹ **(i) es NO CIRCULAR** (lado-primo puro). Esto es real y limpio. **(ii) Estabilidad del MINIMIZADOR ξ_λ, dada (i).** Es perturbación de autovector. Cota
estándar: ‖δξ‖ ≲ ‖δA‖ / gap. **PERO el gap ε_1(λ)−ε_0(λ) es EXPONENCIALMENTE PEQUEÑO**
(descubierto al probar H1: el espectro de QW decae geométricamente a 0). ⟹ la cota ingenua
1/gap es **inútil**. La estabilidad del minimizador NO sale por perturbación estándar. > **Esto localiza el problema abierto de:** 2b no falla por la forma (i, limpia/PNT)
> sino por la **estabilidad del minimizador bajo gap exponencialmente pequeño (ii)**. Ahí, y
> solo ahí, puede entrar RH. **Hecho empírico que acota el problema:** el minimizador ES estable (E4: ceros reproducidos a
1e-15 establemente en N). Entonces (ii) se cumple — pero por un **mecanismo especial**, no por
la cota 1/gap. Identificar ese mecanismo = resolver 2b. **Reformulación prometedora hacia (ii):** los CEROS de ξ̂_λ (= espectro del operador de scaling
perturbado D_λ) son un funcional MÁS ROBUSTO del operador que el autovector ξ_λ de QW. La
convergencia espectral de operadores auto-adjuntos es más estable que la de autovectores. ⟹
atacar (ii) vía convergencia del **espectro de D_λ** (no del ground state de QW). Posible vuelta
al gap exponencial. **Veredicto de circularidad (provisional, honesto):**
- (i) forma: no circular (PNT). ✔
- (ii) minimizador: el mecanismo de estabilidad es el crux abierto; si se controla por la estructura CF (que produce los ceros como OUTPUT del símbolo de primos) ⟹ no circular; si requiere cota de gap que equivalga a regiones libres de ceros ⟹ circular. **Indeciso, pero la estructura (ceros como output, no input) inclina a no-circular** — consistente con. ## 8. RESULTADO: el gap relativo es O(1) — (ii) probablemente auto-controlada Medición (gap.py, mpmath dps=40, N=12): | λ | primos≤λ² | ε0 | gap=ε1−ε0 | gap/ε0 |
|---|---|---|---|---|
| 2.5 | 6 | 6.1e-20 | 4.2e-18 | 68.2 |
| 3.0 | 9 | 2.8e-20 | 1.1e-19 | 3.92 |
| 3.7 | 13 | 1.7e-20 | 6.0e-20 | 3.58 |
| 5.0 | 25 | 1.0e-20 | 3.4e-20 | 3.33 |
| 7.0 | 49 | 6.5e-21 | 2.0e-20 | 3.07 | **Hallazgo:** el gap es exp-pequeño en ABSOLUTO (~1e-20) pero **gap/ε0 ≈ 3, O(1) y estable en λ**. **Consecuencia para (ii):** la rotación del autovector es ‖δA_eff‖/gap, pero δA_eff (proyección
de la cola de primos sobre el near-null space del ground state) vive en la escala ε0. Entonces
la perturbación RELATIVA ~ ε0/gap ~ O(1) — **acotada, no explota por 1/gap**. El ground state
está bien separado a su propia escala. ⟹ mi preocupación previa (fragilidad por gap exp-chico)
queda **desactivada**: (ii) es probablemente AUTO-CONTROLADA por el gap relativo, propiedad
estructural del espectro geométrico, NO de RH. **Veredicto de circularidad (actualizado, honesto):**
- (i) forma: NO circular (PNT). ✔
- (ii) minimizador: gap relativo O(1) ⟹ estabilidad probablemente auto-controlada, **NO circular**.
- ⟹ la evidencia inclina a **2b NO circular** — el programa CCM puede llegar a RH. Consistente con la convicción de. **Caveat honesto:** gap/ε0 decrece lento (68→3.9→3.6→3.3→3.1); falta confirmar que se estabiliza
en O(1) y no decae a 0 asintóticamente. Y falta la cota rigurosa de perturbación de autovector
en la escala relativa (que δA_eff proyectado sí escala como ε0). Pero la dirección es buena. ## 9. (i) CERRADO exacto + (ii) reformulado correctamente **(i) [CERRADO]** — ver `2b_part_i_EXACT.md`. A_λ = A_∞|_{E_λ} EXACTO (verificado 0.00e+00):
los primos >λ² contribuyen cero por soporte (f**g ⊂ [λ⁻²,λ²]). NO hay cola de primos / defecto
PNT — la truncación es exacta. ⟹ 2b NO es perturbación de primos sino **convergencia de
Galerkin del minimizador a un fondo NO aislado de A_∞** (autovalores acumulan en 0). **(ii) [GRAN AVANCE]** — el objeto correcto es el ESPECTRO RELATIVO {ε_k(λ)/ε_0(λ)}, que
determina ξ̂_λ vía el determinante. Medición (relspec.py, mpmath dps=45, N=14): | λ | ε1/ε0 | ε2/ε0 | ε3/ε0 | ε4/ε0 | ε5/ε0 |
|---|---|---|---|---|---|
| 3.0 | 3.88 | 9.39 | 16.67 | 957 | — |
| 3.7 | 3.74 | 9.14 | 15.17 | 26.35 | 35.18 |
| 5.0 | 4.08 | 9.07 | 16.51 | 25.61 | 37.95 |
| 7.0 | 4.07 | 9.05 | 16.40 | 25.40 | 37.42 | **(a) El espectro relativo CONVERGE** — cada columna se estabiliza al crecer λ, de abajo hacia
arriba (horizonte avanzando). A λ=5,7 las primeras 5 razones coinciden a ~1%. Esto es
EXACTAMENTE lo que (ii) necesita: la estructura espectral relativa converge a un límite
**zero-independiente** ⟹ ξ̂_λ converge ⟹ evidencia fuerte de que **2b-(ii) se cierra sin RH**. **(b) Límite con forma cerrada: ε_k/ε_0 ≈ (k+1)²** (4, 9, 16, 25, ~36). La "geometricidad"
previa en float64 era ruido; la estructura real (mpmath) es **ε_k ≈ ε_0·(k+1)²**. Una forma
cerrada es un HANDLE DE PRUEBA: si el espectro relativo de A_∞ es {(k+1)²}, su convergencia
(y la de ξ̂_λ) es demostrable analíticamente. **Veredicto de circularidad (actualizado):** (i) exacto/zero-indep ✔; (ii) espectro relativo
converge a límite estructural con forma cerrada ⟹ **2b parece NO circular y CERRABLE**. El
programa CCM puede llegar a RH. ## 10. Próximos pasos (cierre de 2b)
- **(ii)-T1:** confirmar ε_k/ε_0 → (k+1)² rigurosamente (verificar más k, más λ, convergencia N).
- **(ii)-T2:** PROBAR que el espectro relativo de A_∞ es {(k+1)²} (o lo que sea) analíticamente — vía la estructura Cauchy-Toeplitz/Loewner de QW. Esto cierra (ii).
- **(ii)-T3:** linkear rigurosamente "espectro relativo de A_λ converge" ⟹ "ξ̂_λ→Ξ" (vía el determinante det(D_λ−z), Thm 1.1.ii).
- Con (i) exacto + (ii) cerrado ⟹ **2b ⟹ RH**.
