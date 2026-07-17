# III: la ruta correcta, fijada con cómputo de alta precisión ## Cómputo decisivo (mpmath dps=40, motor CCM validado) **Escala de ε₀ (N=8, λ creciente):** ε₀ minúsculo, positivo, DECAE:
λ=3.7→3.7e-20, λ=5→1.6e-20, λ=7→1.0e-20, λ=10→6.3e-21. Ajuste ε₀ ~ λ^{-2} (≈e^{-L}).
⟹ **REFUTA |ε₀|~2λ** del panel/Hankel. El 2λ es profundidad del símbolo / tope del espectro. **Espectro relativo (λ=3.7, N→∞), ε_k/ε₀:**
N=12: 4.58, 9.14, 19.3, 26.3 (γ=3.58)
N=14: 3.74, 9.14, 15.2, 26.3 (γ=2.74)
N=16: 4.05, 9.09, 16.4, 25.9 (γ=3.05)
Converge a (k+1)² = 4,9,16,25; γ→3.
⟹ **REFUTA el modelo de borde γ→1, {-C,0,C}.** Confirma escalera (k+1)², Dirichlet-Laplaciano. ## Reconciliación de los 8 matemáticos + panel - `ε₀~2λ` (panel/Hankel): REFUTADO. ε₀~λ^{-2}=e^{-L}.
- `γ→1` (modelo de borde, hankel.md): REFUTADO. γ→3.
- `γ→3`, escalera (k+1)² (IV.1 original, mat.1-6): CONFIRMADO numéricamente.
- constante c=-ψ''(1/4)/8 (IV.1, mat.1-6): REFUTADA por el panel (es la curvatura arquimediana, subdominante). PERO irrelevante: los cocientes ε_k/ε₀ son invariantes de escala.
- `(1/2λ)D_λ(s/logλ)→cos2s`, `W_I(1-cos2s)=I` (panel): CORRECTOS, pero describen la escala 2λ (símbolo/borde), no el fondo ε₀~e^{-L}. Refutan la constante absoluta, no la estructura relativa. ## Por qué el modelo de Hankel falló (diagnóstico) (1) Premisa de escala equivocada: modeló ε₀ a escala 2λ; el fondo real está a e^{-L}.
(2) Aproximación demasiado cruda: el núcleo de borde rank-uno (separable ½e^{-v/2}) da {-C,0,C}; el núcleo verdadero es Carleman de rango infinito (hankel.md riesgo #2), cuyo espectro ES la escalera (k+1)². El γ→1 fue artefacto del rank-uno.
(3) El muro de Kronecker (norm convergence falla) es real PERO para el objeto equivocado (Hankel de borde a escala 2λ). No bloquea la ruta (k+1)² a escala e^{-L}. ## La ruta correcta (lo que hay que probar para cerrar III) LEMA (tightness en escala WKB). A_λ/ε₀ → -c d²/dx² Dirichlet (resolvente fuerte), con ε₀≍e^{-L},
dando ε_k/ε₀→(k+1)² y γ→3. RH-neutral. - NO es el lema de Hankel del panel (γ→1, escala 2λ, muro de Kronecker — objeto equivocado).
- ES el problema de capa de borde SEMICLÁSICO (WKB): ε₀~e^{-SL}, S≈1, modos de borde, el programa ya tenía trabajo previo (2b_PROOF_DRAFT, softmodes, edge-localization).
- La estructura relativa (k+1)²/γ→3 está confirmada numéricamente y es RH-neutral; falta la cota cuantitativa de convergencia (Landau-Widom/WKB en la escala e^{-L}). ## Estado de III
- ε₀ escala e^{-L}, positivo: establecido numéricamente.
- ε_k/ε₀→(k+1)², γ→3: establecido numéricamente, RH-neutral, robusto en N.
- Prueba rigurosa de la convergencia: ABIERTA, vía WKB/Landau-Widom en escala e^{-L} (no Hankel 2λ).
- (P) (signo de ε₀): separado. Nota: aquí ε₀>0 para ζ — consistente con RH-true, pero es medición a λ finito, no prueba de ε₀>0 ∀λ.
