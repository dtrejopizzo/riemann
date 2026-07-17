# Documento 103 — Positividad estricta de $W_\lambda$ y afilado de P39

**Programa:** Hipótesis de Riemann — Fase 35 (verificación micro)
**Fecha:** 2026-06-09
**Autor:** David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com
**Prerrequisitos:** Docs 63 (kernel de Abel y su positividad), 64/P39 (criterio de traza), 83 ($d\nu\geq 0$).

---

## Resumen

Probamos que el kernel de Abel $W_\lambda$ del programa CCM es **estrictamente positivo en todo punto** de $\mathbb{R}$ (no solo en casi todo punto), para todo $\lambda$ con $N(\lambda)\geq 1$. Esto **afila el Corolario 7.5 del Doc 63**, que dejaba un conjunto excepcional finito (los nodos de $\mathcal{P}_{N(\lambda)+1}$) y lo neutralizaba apelando a la absoluta continuidad de $d\nu$. Demostramos aquí que ese conjunto excepcional es **vacío**. Como consecuencia inmediata, el cuantificador universal "$\forall\lambda>0$" del criterio de traza P39 (Doc 64) es **redundante**: la anulación $T_\lambda=0$ para **un solo** $\lambda$ (con $N(\lambda)\geq 1$) ya equivale a RH. La familia uniparamétrica $\{T_\lambda\}_{\lambda>0}$ deja de ser una familia: un único miembro la determina.

---

## §1. Definición y la recurrencia de tres términos

Por Doc 63 (§7.1), con la convención de truncación $N(\lambda)=\#\{n:\gamma_n\leq\lambda\}$, el kernel de Abel admite la forma sumada por partes
$$
W_\lambda(s) \;=\; \sum_{n=1}^{N(\lambda)} \bigl[(a_n^\infty)^2-(a_{n-1}^\infty)^2\bigr]\,|\mathcal{P}_n(s)|^2 \;+\; (a_{N(\lambda)}^\infty)^2\,|\mathcal{P}_{N(\lambda)+1}(s)|^2,
$$
donde $(a_n^\infty)^2-(a_{n-1}^\infty)^2 = n$ (cálculo directo con $a_k^\infty=\tfrac12\sqrt{(2k+1)(2k+2)}$, ver Doc 63 Cor. 7.2). Escribimos $N:=N(\lambda)$. Así
$$
W_\lambda(s) \;=\; \sum_{n=1}^{N} n\,|\mathcal{P}_n(s)|^2 \;+\; (a_N^\infty)^2\,|\mathcal{P}_{N+1}(s)|^2. \tag{1}
$$
Todos los coeficientes son estrictamente positivos.

Los polinomios ortonormales CCM $\{\mathcal{P}_n\}$ respecto de $dm_\infty$ satisfacen, por la paridad de la medida ($b_n=0$, ver Doc 92/P39), la recurrencia de tres términos
$$
s\,\mathcal{P}_n(s) \;=\; a_n^\infty\,\mathcal{P}_{n+1}(s) + a_{n-1}^\infty\,\mathcal{P}_{n-1}(s), \qquad a_k^\infty>0,\quad \mathcal{P}_0\equiv 1. \tag{2}
$$

---

## §2. El conjunto de ceros de $W_\lambda$ es vacío

**Lema 2.1 (No-anulación simultánea de polinomios consecutivos).**
Para todo $n\geq 0$, los polinomios $\mathcal{P}_n$ y $\mathcal{P}_{n+1}$ no tienen ningún cero común en $\mathbb{C}$.

*Demostración.* Supongamos $\mathcal{P}_{n+1}(s_0)=0$ y $\mathcal{P}_n(s_0)=0$ para algún $s_0\in\mathbb{C}$. Sustituyendo en (2) con índice $n$:
$$
s_0\,\mathcal{P}_n(s_0) = a_n^\infty\,\mathcal{P}_{n+1}(s_0) + a_{n-1}^\infty\,\mathcal{P}_{n-1}(s_0)
\;\Longrightarrow\; 0 = 0 + a_{n-1}^\infty\,\mathcal{P}_{n-1}(s_0).
$$
Como $a_{n-1}^\infty>0$, se sigue $\mathcal{P}_{n-1}(s_0)=0$. Iterando la recurrencia hacia abajo (índices $n-1,n-2,\dots,1$) se obtiene $\mathcal{P}_{n-1}(s_0)=\mathcal{P}_{n-2}(s_0)=\cdots=\mathcal{P}_0(s_0)=0$. Pero $\mathcal{P}_0\equiv 1\neq 0$, contradicción. $\square$

**Teorema 2.2 (Positividad estricta puntual de $W_\lambda$).**
Para todo $\lambda$ con $N(\lambda)\geq 1$,
$$
W_\lambda(s) \;>\; 0 \qquad \text{para todo } s\in\mathbb{R}.
$$

*Demostración.* Por (1), $W_\lambda$ es una suma de términos no-negativos con coeficientes $>0$. Si fuese $W_\lambda(s_0)=0$ para algún $s_0\in\mathbb{R}$, cada término se anularía; en particular el término $n=N$, $N\,|\mathcal{P}_N(s_0)|^2$ (presente porque $N\geq 1$), forzaría $\mathcal{P}_N(s_0)=0$, y el término final forzaría $\mathcal{P}_{N+1}(s_0)=0$. Esto contradice el Lema 2.1 (caso $n=N$). Luego $W_\lambda(s)>0$ en todo $\mathbb{R}$. $\square$

**Observación 2.3 (Comparación con Doc 63).** El Cor. 7.5 del Doc 63 afirmaba $W_\lambda>0$ *salvo en un conjunto finito* (los nodos de $\mathcal{P}_{N+1}$), y cerraba el argumento de la CTP invocando que $d\nu$ es absolutamente continua (Doc 83), de modo que el conjunto finito tiene $d\nu$-medida nula. El Teorema 2.2 muestra que **ese conjunto es vacío**: la positividad es genuinamente puntual y no requiere ninguna hipótesis sobre $d\nu$. El argumento es puramente estructural (recurrencia de tres términos con $a_k>0$).

**Observación 2.4 (Caso $N(\lambda)=0$).** Para $\lambda$ por debajo del primer nodo, $N(\lambda)=0$ y la suma de (1) es vacía: $W_\lambda(s)=(a_0^\infty)^2|\mathcal{P}_1(s)|^2$, que se anula en el único cero de $\mathcal{P}_1$ (esto es $s=0$, pues $\mathcal{P}_1(s)=\sqrt2\,s$). En este régimen degenerado se recupera exactamente la situación del Doc 63 (un cero aislado, neutralizado por la a.c. de $d\nu$). El Teorema 2.2 cubre todos los demás $\lambda$.

---

## §3. Consecuencia: un solo $\lambda$ determina RH

**Teorema 3.1 (Afilado de P39).**
Fijemos cualquier $\lambda_0>0$ con $N(\lambda_0)\geq 1$. Entonces
$$
\mathrm{RH} \;\Longleftrightarrow\; T_{\lambda_0}=0.
$$
Es decir, el criterio de traza del Doc 64 / P39 vale con un **único** valor del parámetro; el cuantificador "$\forall\lambda>0$" es redundante.

*Demostración.* ($\Rightarrow$) Bajo RH, $dm_{\mathrm{full}}=dm_{\mathrm{full,on}}$, luego $d\nu=0$ y $T_{\lambda_0}=\int W_{\lambda_0}\,d\nu=0$ (Doc 64).

($\Leftarrow$) Por Doc 83, $d\nu = dm_{\mathrm{full}}-dm_{\mathrm{full,on}}\geq 0$ es una medida no-negativa (de hecho $d\nu=(R-1)\,|\zeta_{\mathrm{on}}|^2\,dm_\infty$ con $R=|\zeta/\zeta_{\mathrm{on}}|^2\geq 1$). Por el Teorema 2.2, $W_{\lambda_0}(s)>0$ para todo $s\in\mathbb{R}$. Entonces el integrando $W_{\lambda_0}\,\dfrac{d\nu}{dm_\infty}$ es no-negativo y, si
$$
T_{\lambda_0}=\int_{\mathbb{R}} W_{\lambda_0}(s)\,\bigl(R(s)-1\bigr)\,|\zeta_{\mathrm{on}}(1/2+is)|^2\,dm_\infty(s)=0,
$$
la no-negatividad del integrando obliga a $W_{\lambda_0}\,(R-1)\,|\zeta_{\mathrm{on}}|^2=0$ en $dm_\infty$-casi todo punto. Como $W_{\lambda_0}>0$ en todo punto y $|\zeta_{\mathrm{on}}|^2>0$ salvo en los ceros aislados de $\zeta_{\mathrm{on}}$ (conjunto de medida nula), se concluye $R-1=0$ c.t.p., es decir $d\nu=0$. Por la equivalencia $d\nu=0\iff$ RH (Doc 89, condición 2), se obtiene RH. $\square$

**Corolario 3.2.** La condición 4 de la lista de equivalencias del Doc 89 ("$T_\lambda=0$ para todo $\lambda>0$") puede reemplazarse por "$T_{\lambda_0}=0$ para algún (equivalentemente, cualquier) $\lambda_0$ con $N(\lambda_0)\geq 1$".

---

## §4. Lectura estructural

Este resultado es deliberadamente modesto en dificultad pero significativo en estructura. En el "meta-patrón" del programa (ver P41, §2), RH aparece reiteradamente como el **punto frontera** de una familia uniparamétrica cuyos demás miembros son teoremas incondicionales: el tiempo de De Bruijn–Newman $t$, el parámetro de aproximación $x$ de los triples espectrales, la escala $\lambda$ del kernel de Abel. El Teorema 3.1 muestra que **al menos una de esas familias colapsa a un punto**: $\{T_\lambda\}$ no es una familia uniparamétrica de obstrucciones independientes, sino una sola obstrucción presentada redundantemente. Esto no acerca la prueba de RH —la dificultad sigue concentrada en mostrar $d\nu=0$ sin conocer las posiciones de los ceros (barrera de Hadamard, MW-7)— pero limpia el enunciado y elimina un grado de libertad espurio del mapa.

---

## §5. Tabla de resultados

| Objeto | Resultado | Calidad |
|---|---|---|
| $\mathcal{P}_n,\mathcal{P}_{n+1}$ sin cero común | Sí (Lema 2.1) | Riguroso |
| $W_\lambda(s)>0\ \forall s\in\mathbb{R}$, $N(\lambda)\geq 1$ | Sí (Teorema 2.2) | Riguroso |
| Conjunto excepcional de Doc 63 Cor. 7.5 es vacío | Sí (Obs. 2.3) | Riguroso |
| RH $\iff T_{\lambda_0}=0$ para un solo $\lambda_0$ | Sí (Teorema 3.1) | Riguroso |

---

*Fin del Documento 103.*
