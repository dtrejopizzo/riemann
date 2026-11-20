# POWER GROUP AUDIT 037

Estado: ENERGY_GROUP037 completo, incluida adición Q creciente, APROBADO. Papers intactos.

## 1. Corpus y obligación mínima

Reconsultados índice ROUTES-TRIED-INDEX, grid maestro y crucigrama, entradas036 y antecedentes LOW_TABLE018, INTERIOR_SCALE030 y WEIGHTED_BLOCK031. La cancelación principal y su residuo E0, las representaciones conjuntas y primitivas ponderadas son conocidas. La nueva obligación requiere una desigualdad firmada con error explícito contra el perfil gamma real y control suficiente del complemento; no basta otra identidad ni coincidencia de fases exponenciales.

## 2. Centro crítico y agrupación finita — APROBADOS

Revisados `POWER_ENERGY_GROUP_037.md` y `tools/power_energy_group_037_verify.py`; ejecución independiente PASS. La Riccati en t_N=d/992 factoriza q′=(q−1/2)(q+1984+1/2); CURV implica1/2<q≤1/2+M_N/1985. El centro es propio de la energía real y no un punto elegido mediante un barrido.

En D_N(m)=mH_N(mx_N)/H_N(x_N), el factor de escala es m^−1/2 antes de la razón de rho. Integrar las cotas de q produce exactamente DILATE, incluido el resto M_N(logm/1985+(logm)²/2). La razón de1/2+q está entre1 y1+M_Nlogm. ERROR conserva así un bound explícito de orden(logm)²/m, no sumable hasta infinito.

Para R entero, el conteo por cuadrados da A(R)>R/4. Abel DISCRETO daΣ_(m=1)^R|μ(m)|/m≥H_R/4>logR/4; restar m1 justifica el lower usado. Los extremos R2^18,N≥2^16 hacen D_N(m)>1/(2m) y prueban ABS-FAIL. La precisión de usar R entero evita un error de piso en una hipotética cota real A(x)>x/4. El resultado sólo refuta contracción absoluta en este régimen, no la suma firmada ni W.

La suma principal de los divisores de Q es EXACTAMENTE U_Q/m. Para el error, los pesos positivos1/b normalizados por V_Q incluyen cada primo con probabilidad1/(p+1), dando los momentos logarítmicos y SIGNED. WINDOW preserva el signo de cada grupo finito bajo una condición comprobable, uniforme en toda la ventana. Es una desigualdad nueva respecto a la identidad Euler sola, pero no cambia el exponente crítico1/m.

FULL reagrupa correctamente todos los enteros libres de cuadrados y es absoluto para N fijo. La relación P−Pi=2Lminus−F concuerda con ERR018. No se suma el mayorante no sumable de SIGNED a infinito ni se convierte el signo de grupos en el del inverso. El complemento firmado y su integración siguen abiertos; la precisión necesaria frente a componentes exponenciales no se obtiene de un error relativo polinómico.


## 3. Elección Q creciente — APROBADA

Leída la adición§8 y ejecutado de nuevo el verificador ampliado: PASS. Los productos sobre todos los enteros2..K dan U≥1/K yV≤(K+1)/2; UV≤1,U≤1/2 yV/U≤N^(1/4). Los bounds de logQ y de los momentos logarítmicos implican el error relativo epsilon≤u²[4aN^−1/2+(17/2)N^−1/4]<.01 en TODA la ventana1≤m≤exp(3N^(1/4)), para todos N≥2^80. No se enumera la función Möbius ni se verifica una campaña de N.

M>Q asegura que el error de H_floor(z)−log z está entre0 y1 para cada divisor. La inclusión–exclusión conserva el término logarítmico favorable−Σμ(b)logb/b, así S(M)≥Uell−V. La pérdida por cuadrados sólo usa primos>K; dividir por p² mantiene coprimalidad y S(M/p²)≤S(M). La unión con pesos positivos deja T(M)≥(1−1/K)S(M).

Como U²ell≥3,UV≤1,U≤1/2 yK≥1024, el lower de la suma de módulos de TODOS los grupos exteriores, acotada por un subconjunto finito de la ventana, supera37/25. El grupo principal es<101/200. Esto refuta dominación diagonal/contracción ABSOLUTA para ESTA elección creciente de agrupación, aunque sus grupos locales sean positivos. No determina el signo de la suma firmada exterior, ni de h,F o W; no excluye otras agrupaciones o desigualdades firmadas.

## 4. Cierre de alcance

La ronda cumple una distinción matemática nueva: cota crítica1/m en un perfil real, resto explícito de agrupación finita y control cuantitativo de una elección creciente. Sigue sin satisfacer la obligación mínima de controlar el complemento aritmético firmado e integrarlo con precisión suficiente; no se etiqueta esa ausencia como signo, cierre por dificultad o imposibilidad global. No hay nueva cobertura W/T. Root coincide independientemente en núcleo, adición y verificador.
