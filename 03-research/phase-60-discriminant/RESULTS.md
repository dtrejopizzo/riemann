# Phase 60 — Discriminante: RESULTADOS (cierre honesto) **Autor:** David Alejandro Pizzo · **Ejecutado:** 2026-06-16
**Veredicto:** NO-GO. La tesis central (multiplicatividad controla el signo de Weil, medible
vía el discriminante de la forma localizada) queda **refutada** por experimentos reales y
reproducibles. Todo el código corre en el venv y reproduce las gates validadas. --- ## Tesis testeada > El signo del residual de Weil no lo controla la ubicación de los ceros sino la
> **multiplicatividad** (producto de Euler). Aislarlo comparando ζ (Euler) vs controles
> no-multiplicativos en la forma de Weil localizada. ## Experimentos (todos reproducibles, engine P7 validado) ### E1 — `E1_zero_side_blindness.py` (corre, gates PASS)
El lado-cero validado `M_zeros` es función del **multiset de ceros únicamente**.
- Toda configuración ON-line (cualquier densidad/espaciado, = cualquier L-función RH-true) queda en el floor: λ_min/tr ∈ [+2.3e-5, +1.1e-1] ≥ 0.
- El único movedor del signo es desplazar ceros OFF-line (status-RH).
- **Conclusión:** el lado-cero mide status-RH, es **ciego a multiplicatividad**. Separar ζ de L_DH aquí = separar por ceros off-line = ubicación = **circular** (NO-GO pre-registrado §5).
- ⇒ la tesis vive enteramente en el lado-aritmético `M_arith` (P). ### E2 — `E2_multiplicativity_discriminant.py` (corre)
Aporte metodológico: fijar el bloque arquimediano A (ζ, a=1/4) y variar SOLO la
multiplicatividad de los coeficientes (normalización desconocida se cancela en la comparación
relativa). C(L) = λ_max(A^{-1/2} P A^{-1/2}).
- ζ (multiplicativo): C = 1.98.
- shuffle / random (mismo soporte, misma distribución de valores, sin correlación posicional): C ≈ 0.31 ± 0.05.
- ζ a **+31σ (shuffle), +41σ (random)**. *Aparente* GO. ### E2b — `E2b_kill_confound.py` (corre) — EL CONTROL DECISIVO
Sospecha: shuffle/random rompen la correlación posición(log n)↔valor, así que +30σ podría ser
"suma coherente (suave en log n) vs incoherente", NO multiplicatividad. Λ(n)=log p es
trivialmente suave en log n.
Control suave **no-multiplicativo**, magnitud-matched: | coeficiente | C | ¿multiplicativo? |
|---|---|---|
| ζ (Λ real) | 1.98 | sí |
| flat (Λ̄ constante) | **2.44** | no |
| loglin (ajuste lineal de Λ) | **2.11** | no |
| logn | **2.21** | no |
| shuffle / random | 0.31 | no | **Los controles suaves no-multiplicativos igualan o SUPERAN a ζ.** ζ ni siquiera es el más
coherente (C(ζ) < C(flat)). --- ## Veredicto La separación de E2 era **suavidad/coherencia en log n**, no multiplicatividad. La firma
"Euler" es **espuria**. Sumado a E1: > **Ambos lados de la forma de Weil localizada son ciegos a la multiplicatividad.**
> El lado-cero ve solo ubicación de ceros (status-RH). El lado-aritmético, vía la forma
> localizada con envolvente suave (Hermite/Slepian), ve solo la **envolvente suave de los
> coeficientes** (primer momento/densidad) y lava las correlaciones de Euler. Razón estructural (nueva, precisa): la multiplicatividad es una correlación aritmética fina
(entre Λ en p, p², q…) que vive a la escala de log p individuales. La envolvente suave de la
forma localizada la integra y la borra. Esto es coherente con T3.4 (la "banda" aritmética era
artefacto de base) — el mismo dedo apuntando: **no sobrevive estructura aritmética fina en la
forma localizada.** Es MW-2 (propagación aritmética) con disfraz nuevo. ## Consecuencia para RH La ruta del discriminante de multiplicatividad **no lleva a una condición para el signo de
Weil** con los observables disponibles. RH permanece detrás del muro cross-place (MW-3/MW-5),
intacto. Esta phase se **cierra**. Se registra como [NG-F1] en NO-GO-LIST. ## Lo que SÍ deja (honesto)
1. Un instrumento de discriminante relativo (A fija, varía multiplicatividad) que **cancela la normalización** — desbloquea el confound de baseline de Phase3-results, y es reutilizable.
2. La constatación dura: la forma de Weil localizada es ciega a multiplicatividad por ambos lados, con razón estructural. Cierra limpiamente la dirección δ del PLAN-RH-FRONTIER.
