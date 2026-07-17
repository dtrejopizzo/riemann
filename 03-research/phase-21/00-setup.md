# Phase 21 — Geometry of Negative Directions

**Date:** June 2026  
**Predecessor:** Phase 20 (ω-information barrier, T4/T4.1/T5)  
**Status:** Active

---

## Reglas absolutas de la fase

Esta fase NO usa:
- experimentos numéricos
- Python o cómputos externos
- par-correlación como axioma
- sistemas de de Branges como input
- SURF, Hilbert–Pólya, GUE como hipótesis
- ningún criterio equivalente a RH como punto de partida

Todo resultado debe salir de razonamiento matemático puro.

---

## Objeto central

Sea $Q$ la forma de Weil localizada (forma de Kreĭn cuadrática sobre funciones de prueba).

Definición: $\mathcal{N}$ = subespacio negativo máximo de $Q$.

Definición: $\kappa = \dim\mathcal{N}$.

RH $\iff \kappa = 0$.

El objeto de estudio de esta fase es $\mathcal{N}$ en sí mismo, no $\kappa=0$.

---

## Principio estratégico

En lugar de preguntar: "¿Por qué $\kappa = 0$?"

Preguntar: "¿Qué propiedades debe tener necesariamente todo subespacio negativo no-nulo?"

Si toda geometría posible de $\mathcal{N}$ es eventualmente imposible → RH sigue.

Pero el objetivo inmediato NO es probar RH. Es construir una teoría matemática de $\mathcal{N}$.

---

## Objetivos

### 21-A: Teorema de Paridad (Clase B, incondicional)

Estudiar si $\kappa \equiv 0 \pmod{2}$ para $\zeta$ y L-funciones reales.

Hipótesis: los ceros fuera de línea vienen en órbitas completas bajo el grupo de Klein $V = \{id, \sigma, \iota, j\}$. Cada órbita completa contribuye exactamente 2 direcciones negativas independientes.

### 21-B: Separación Angular (Clase B/A)

Desarrollar una teoría geométrica de la interacción entre direcciones negativas.

Hipótesis: paquetes de frecuencia distintos (órbitas a distintas alturas) son casi-ortogonales exponencialmente.

### 21-C: Medida de Defecto (Exploratoria)

Definir la medida $\mu_\kappa$ asociada a las direcciones negativas y estudiar su soporte y rigidez.

### 21-D: Principio de Exclusión (Clase A si tiene éxito)

Buscar un teorema de rigidez: si $\kappa > 0$, ¿qué estructura global necesariamente existe en $\mathcal{N}$?

---

## Documentos de la fase

- `00-setup.md` — este documento
- `01-parity-and-geometry.md` — Teorema de Paridad + Separación Angular

## Paper

P32 — `06-papers/P32-negative-packet-theory/main.tex`
