# Revisión de la ronda 9 (`ROUND_009_G1.md`, `ROUND_009_G2.md`, `ROUND_009_G3.md`)

Ninguna candidata pasa la puerta. Signo global: OPEN. Los antecedentes citados por los memos conservan la
etiqueta CITED; aquí se rederivó sólo lo indicado.

## R9-a. Contactos como fuente (G1)

- La inversión de papeles ya está en la fase 188: N_BUILD_001 (la densidad media `ρ₁ = 2e^{u/2}du` aporta un
  término `≥ 0` sobre `P_T`; símbolo `m^♯ = m + 1/(¼+τ²)`) y N_BUILD_011 Teor. 1 (`ρ_κ` positiva sólo para
  `κ ≥ κ* ≥ |C₀|/4 ≈ 1.343 > 1`). La media no alcanza; la fluctuación debe aportar. CITED.
- Polarización de `Λ = μ∗log`: caso `W = 1` de L2_BUILD_017; traslada el signo al cuadrado. Repetición.
- Anti-alineación de `U_μF` y `U_{log}F` sobre las direcciones negativas de `Arch`: residuo abierto (a) de
  `06_OPEN_RESIDUES_DEAD_SUBROUTES.md`; sin identidad nueva es un acoplamiento 2×2 a precisión del margen.

## R9-b. Recursiones con historia (G2)

- Las recursiones clásicas (Schur/Verblunsky, sistemas canónicos, matriz de transferencia por primos, inducción
  en la ventana, Jacobi inverso, Sturm, Darboux, cadena de Sonin) están en el corpus y terminan en una de dos
  formas: parámetros que exigen invertir la matriz (J3), o factores que no ven el peso. CITED.
- Lema A, rederivado: en todo sistema de Beurling `Λ_𝒩` se define por `Λ_𝒩 ∗ 1 = log`, luego
  `Σ_{d|ν}Λ_𝒩(d) = log ν`. Un paso que use sólo divisores y el monoide libre no puede fallar bajo un peso de
  ese tipo; debe usar estructura aditiva. PROVED.
- Lema B (el contacto aporta cero en el instante de entrada; el dato de etapa debe ser una ley de transporte
  en `T`): CITED + ARGUED.
- Candidata sin objeto: parámetro `ρ_n = Φ_T(ρ_d, d|n; ρ_{n−1}; log n)`. Falta `Φ` y la región.

## R9-c. Complemento del mapa (G3)

- Taxonomía de 25 clases de método y lista P1–P12 de propiedades simultáneas del objeto: documento de trabajo;
  la clasificación es ARGUED.
- Operaciones fuera de la taxonomía examinadas: varianza con ley no lineal (R5-e), mayorización (N_BUILD_007),
  reflexión con contactos que cruzan (R3-a), conteo puro (no se rompe en `c = 2`): todas con antecedente.
- Sin marca textual en el corpus y sin objeto: (A) contracción de Birkhoff–Hopf con paso de ventana a ventana
  dependiente de la historia; falta una aplicación no lineal `T → T′` que preserve positividad (la inclusión
  `P_T ⊂ P_{T′}` transfiere el signo en sentido contrario). (B) funcional convexo con hessiano `a_T` y
  certificado propio de convexidad (hueco de R5-a); falta una tercera fuente de convexidad.
