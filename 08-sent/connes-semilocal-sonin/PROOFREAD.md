# Line-by-line proofreading of main.tex (10 pp.)

Compiled with pdflatex ×2: no `??`, 10 pages; one overfull hbox of 9.9 pt (l. 152–156), two hyperref warnings (l. 194), one overfull vbox of 1.6 pt (p. 1, irrelevant). Bibliography: 14 keys defined, 14 used, none unused. Checked against the local text of CC (`cc_2006.13771_text.txt`): (83)–(90), Thm 1, Thm 3.6/Cor 3.8/Rem 3.9, Thm 6.11, Fact 6.5, (127) and the bound 0.772216; the figures of §4 against R186_021/022/102/103. Line numbers refer to `main.tex` at the time of this proofreading.

Severity: **A** = mathematical error or incorrect statement; **B** = undefined symbol / numerical inconsistency / citation; **C** = LaTeX; **D** = English and style.

## A. Mathematical errors

| Line | Problem | Exact replacement |
|---|---|---|
| 341–342 (proof of thm:84) | The identity `\Tr\vartheta(f)Q_1Q_2Q_1-\Tr\vartheta(f)\Pi_F=E_F(f)+\sum\lambda_n^2\langle\zeta_n\|\vartheta(f)\zeta_n\rangle` is **false**: by thm:gap(i), $Q_1Q_2Q_1=\Pi_F+\sum\lambda_n^2\lvert\zeta_n\rangle\langle\zeta_n\rvert$, so the difference of traces is $\sum\lambda_n^2\langle\zeta_n\lvert\vartheta(f)\zeta_n\rangle$ without the term $E_F(f)$ (exactly (90) of CC). $E_F$ enters in the step (85)→(89), not in (90). | `By Theorem~\ref{thm:gap}(ii) the four series (two diagonal, two cross) converge absolutely, so your passage (85)--(89) can be performed term by term: for each $n$, $\lambda_n^2\langle\xi_n|\vartheta(f)\xi_n\rangle=\lambda_n^2\langle\zeta_n|\vartheta(f)\zeta_n\rangle+\lambda_n^2\tau_n(c_n+c_n')$, and $\lambda_n^2\tau_n+\lambda_n(1-\lambda_n^2)^{1/2}=\tau_n$ collects the two cross coefficients into $E_F(f)$; your (90), $\Tr\vartheta(f)Q_1Q_2Q_1-\Tr\vartheta(f)\Pi_F=\sum_n\lambda_n^2\langle\zeta_n|\vartheta(f)\zeta_n\rangle$, is Theorem~\ref{thm:gap}(i).` |
| 339–340 | $c_n$, $c_n'$ are used without definition. | Replace `gives, for each $n$ and without summing, $\langle\zeta_n|\vartheta(f)\zeta_n\rangle=\langle\xi_n|\vartheta(f)\xi_n\rangle-\tau_n(c_n+c_n')$, your (87).` by `gives, for each $n$ and without summing, $\langle\zeta_n|\vartheta(f)\zeta_n\rangle=\langle\xi_n|\vartheta(f)\xi_n\rangle-\tau_n(c_n+c_n')$ with $c_n=\langle\xi_n|\vartheta(f)\zeta_n\rangle$, $c_n'=\langle\zeta_n|\vartheta(f)\xi_n\rangle$, your (87).` |
| 526–527 (thm:schur) | `$\min\{c,\lambda_S\}/(1+\|K\|)^2\le\lamA(T)\le\min\{c,\lambda_S\}$`: the upper bound $\lamA\le\lambda_S$ only follows with $F=e-Ke$, $\|F\|^2=1+\|Ke\|^2\ge1$, hence $\lamA\le\mathfrak s(e)/\|F\|^2$, which is $\le\lambda_S$ only if $\lambda_S\ge0$. If $\lambda_S<0$ the bound as written is false (one only gets $\lamA<0$). The "if and only if" remains correct. | `then $\min\{c,\lambda_S\}/(1+\|K\|)^2\le\lamA(T)\le\min\{c,\lambda_S\}$ when $\lambda_S\ge0$, and $\lamA(T)<0$ when $\lambda_S<0$. Hence` |
| 168–170 (thm:nogo) | The statement includes "also on $\PT\cap\{\int F=0\}$", but $\int\beta=-\frac14\int c_w\neq0$ in general; the proof does not treat it. It suffices to take $\int c_0=0$. | In the proof, l. 173: `Fix $c_0\in C_c^\infty(-1,1)$ real (with $\int c_0=0$ for the clause on $\int F=0$), $c_w=c_0(\cdot/w)$ and` |
| 92–93 (Notation) | "the two conditions ``vanishing at $i/2$ and $0$'' of your Theorem~1 are, up to the second moment, the conditions defining $\PT$": Thm 1 of CC imposes $\widehat g(i/2)=0$ and $\widehat g(0)=0$; $\PT$ imposes $\widehat g(\pm i/2)=0$ and **not** $\widehat g(0)=0$. The sentence is ambiguous. | `the condition $\widehat g(i/2)=0$ of your Theorem~1 is one of the two defining $\PT$; $\PT$ also imposes $\widehat g(-i/2)=0$ and does not impose $\widehat g(0)=0$.` |

## B. Undefined symbols, inconsistent numbers, citations

| Line | Problem | Exact replacement |
|---|---|---|
| 411–414 (obs:s0) | Mutually inconsistent figures: with $C_\infty(s_0)=-0.140$ and $C_S(s_0)=+0.010$ one gets $\Delta C=0.150$, not $0.135$; and $\mathfrak a_T^\infty(s_0)\approx0.140$ does not match $\mathrm{Son}_\infty(s_0)=0.014$, $C_\infty=-0.140$ (which would give $0.154$). Source (R186_021/102): at the semilocal $s_0$, $\Delta C=0.135$, $\mathfrak a^\infty=0.140$; at the archimedean minimiser $s_0^\infty$: $C_\infty=-0.140$, $\mathfrak a^\infty=0.153$. The text mixes the two vectors. | `The prime acts on $s_0$ only through $C$: in the semilocal $s_0$ the balance is $\Delta C=C_S(s_0)-C_\infty(s_0)\approx0.135$ against $\mathfrak a^\infty_T(s_0)\approx0.140$ (the archimedean form in $s_0$), with $C_S(s_0)=+0.010$; in the archimedean minimizer $s_0^\infty$ the same numbers are $C_\infty(s_0^\infty)=-0.140$ and $\mathfrak a^\infty_T(s_0^\infty)=0.153$; over all of $\PT$ the relative loss ...` and in l. 416–417 keep `almost all of the archimedean surplus $0.153$ in $s_0^\infty$ ($0.140$ in the semilocal one).` |
| 448–449 (§5, first paragraph) | $\tau$ is the frequency variable in the bound for $m$, and two lines later $\tau=T/k$ (Definition). Notation clash on the same page. | `$\log\frac s{2\pi}-\frac1s-\frac1{2s^2}\le m(s)$ and $m$ increasing on $[0,\infty)$ with $m(0)=C_0$` |
| 201 (§3.1) | $\widehat k(D)$ (l. 225, 228) and $\widehat{\tilde g}(D)$ (l. 288–289) are used without saying that $\vartheta(h)$ is a function of $D$; $k$, $K_g$ are undefined. | Add after `$D=-i\,d/dt$.`: `For $h$ on $\R_+^*$, $\vartheta(h)$ is then the convolution by $k(s)=h(e^s)$, which we write $\widehat k(D)$.` And in l. 288–289 replace `$\widehat{\tilde g}(D)$` by `$\widehat k(D)$`, `$\int|K_g|^2(-2a-x)_+dx$` by `$\int|K|^2(-2a-x)_+dx$, $K$ the kernel of $\widehat k(D)M(D)$,` y `$\widehat{\tilde g}\,m_\infty e^{i\varphi}$ is Schwartz` by `$\widehat k\,m_\infty e^{i\varphi}$ is Schwartz`. |
| 226 (proof of thm:phase) | $P_a$ undefined. | `then, with $P_a=\mathbf 1_{t<a}$ (the cut-off $P$ at level $\lambda=e^a$), $UP_aU^*-P_a=\dots$` |
| 215–216 (thm:phase) | $\Pih_\infty$ is not defined (only $\Pih^S$). | `$\vartheta(h)(\Pih^S-\Pih_\infty)$, $\Pih_\infty=F_\infty PF_\infty$, is trace class` |
| 294 (proof of thm:gap) | $X_{10}$ undefined. | `$\Theta_{01}X_{10}$, $X_{10}=(1-P)(\Pih^S-\Pih_\infty)P$,` |
| 319 (proof of thm:L2) | $K_S$ undefined. | `the dyadic quasi-covariance of the kernel $K_S$ of $F_S$, $K_S(2^jx,y)=K_S(x,y)-B_j(x,y)$,` |
| 306 (thm:L2) | The sum starts at $j=0$ but $\beta_0=0$. | `\sum_{1\le j\le\log_2R}\beta_j\,\log^+\frac1{|\rho-2^j|}+O_R(1)` |
| 556 (§6) | $P_\lambda^S$ undefined; it should be $\Pih^S$. | `does not commute with $\Pih^S$ for $S=\{\infty,2\}$` |
| 159–160 (§2) | "$\lambda_2\le0.7722$ for your operator $T$ (numerically $0.6865$)": $T$ clashes with the half-length $T$; in CC, $0.7722$ is the a priori bound of §6 and $0.686494$ is (127). | `$\lambda_{\max}(K_I)\approx1.05158$, $\lambda_2\approx0.6865$ (bounded a priori by $0.7722$ in your \S6), with the eigenvector $\zeta$ of the negative direction overlapping the constant by $\langle\zeta|\xi_0\rangle\approx0.94865$;` |
| 362–363 (cor:split) | "with $\varepsilon_S$ now carrying $\log^2$ singularities…": the exact form of the $\log^2$ term is ARGUED in the source (R186_015), not PROVED. | `with $\varepsilon_S$ now carrying $\log^2$ singularities at the $S$-units $q=a/b$ ($a,b\in\langle2,3\rangle$ coprime), cut off at scale $1/b$ (the lower-order terms are not made explicit).` |
| 97–101, 448 | `\cite[certificate at half-length 0.8047]{Paper47}`, `[the margin theorem]`, `[the L\'evy-kernel lemma]`, `[elementary bounds on the symbol]`: descriptions instead of numbers. Acceptable if the PDF is attached; better with section numbers. | `\cite[\S2]{Paper47}` etc. (use the actual section numbers of the attached PDF). |
| 578, 572 (bib) | `Kim2026`: "Kim et al." without names or title; `CCM2024`: no title. A bibitem without a title is not acceptable for the recipient. | Complete with authors and title of arXiv:2607.24830 and arXiv:2403.01247 (e.g. `A.~Connes, C.~Consani and H.~Moscovici, \emph{<exact title>}, arXiv:2403.01247.`). |
| 540–541 (remark §5) | Broken sentence: "for $k\ge9$ (92\% at $T=\frac12\log5$ with $k=5$) for $k\ge5$;". | `have $99\%$ of their mass in $E_k$ for $k\ge9$ ($92\%$ at $T=\frac12\log5$ with $k=5$); this is approximation theory` |

## C. LaTeX

| Line | Problem | Exact replacement |
|---|---|---|
| 152–156 | Overfull hbox 9.9 pt (runs into the margin on p. 2). | Replace `and $\int f(\rho^{-1})\varepsilon(\rho)d^*\rho=\int\cF(x)\varepsilon(e^{|x|})dx$; the prime comb` by `and` + `\[\int f(\rho^{-1})\varepsilon(\rho)\,d^*\rho=\int\cF(x)\,\varepsilon(e^{|x|})\,dx;\]` + `the prime comb` |
| 194 | hyperref warning: `$2$` in a section title. | `\section{The semilocal Sonin space at the prime \texorpdfstring{$2$}{2}}\label{sec:semilocal}` |
| 42 | `\thanks{...}` in amsart prints the affiliation as an unmarked footnote; `\address` is better. | `\address{Independent researcher, Buenos Aires}` and `\date{October 2026}` |

## D. English and style (phrases that sound mechanical or formulaic)

| Line | Problem | Exact replacement |
|---|---|---|
| 46–47 | "we record three things" | `we prove three things` (the first two are theorems; so is the third) |
| 58–59 | "None of this produces a sign; it localizes where positivity lives." (a slogan, repeated in l. 126) | Abstract: `No sign is obtained; the results say in which subspace the sign has to be decided.` |
| 126–129 | "None of this produces a sign. What it does is localize where positivity lives: in the semilocal picture, in … ; in the archimedean picture, in …" | `No sign is obtained. Both pictures point to the same small subspace: in the semilocal picture, a single almost Sonin-orthogonal direction where the window form is a $94\%$ cancellation between two positive quantities (\S\ref{sec:num}); in the archimedean picture, the span of the piecewise Tate exponentials $e^{\pm t/2}\mathbf 1_{B_j}$ (\S\ref{sec:coer}).` |
| 65–68 | "the one I came to love is yours … It has a shape; one can see where the primes enter" | `the one I kept returning to is yours: … It has a visible structure: one sees where the primes enter and what the archimedean place does on its own.` |
| 70–71 | "I want to be honest about where I stand. I think … needs a genuinely new mathematical idea, and I do not have it." | `Let me say where I stand. I think the positivity of the quadratic form on windows of growing length needs a new idea, and I do not have it.` |
| 76–78 | "with proofs sketched and every statement labelled by what it is: a theorem, a numerical observation, or an open question." (fine), but l. 131–133 "the full arguments, each of which was re-derived independently, are in the author's notes" reads as an internal process note. | `the proofs below are sketches; the full arguments are in the author's notes and are available on request.` |
| 108 | "In short:" | `Briefly:` (or delete) |
| 262 | "So the primes change the spectrum of the band operator genuinely:" | `So the primes do change the spectrum of the band operator:` |
| 266 | "so the gap of the next theorem is real but tiny at your level." | `so the gap in the next theorem is positive but tiny at the level $\lambda=1$.` |
| 251 | "Compactness is yours \cite[…]{CCquasi}; directly, …" | `Compactness is proved in \cite[Thms.~2.1, 4.4]{CCquasi}; directly, …` |
| 286–287 | "the semilocal case is literally the archimedean one with another symbol." | `the semilocal case is the archimedean one with another symbol.` |
| 349–352 | Debugging narrative: "turned out to be the difference between a consistent and an inconsistent chain: … and without it the semilocal Sonin trace came out negative…" | `The term $2\log\frac1\lambda\,f(1)=2\log\frac1\lambda\,\|F\|^2$ ($=1.386\|F\|^2$ at $\lambda=\frac12$) is not negligible: without it the semilocal Sonin trace is negative on the near-minimizer of the window form; with it every check we could make passes, including the monotonicity …` |
| 402–403 | "The rise of $\rho^*$ from $0$ to $0.94$ is not driven by the numerator: … It is driven by the collapse of …" | `The rise of $\rho^*$ from $0$ to $0.94$ comes from the denominator, not from the numerator: $C(u_T)$ stays in $[0.017,0.026]$ from $T=0.40$ on, while the Sonin mass of the maximizer collapses as $u_T$ aligns with …` |
| 416 | "The mechanism is visible:" | `Concretely:` |
| 486 | "The theorem deliberately does not separate" | `The theorem does not separate` |
| 490 | "Either way an operator-norm argument cannot close:" | `Either way an operator-norm argument cannot succeed:` |
| 544–545 | "We have not found this block structure in the literature." (l. 456) and "What seems new is…" (l. 470): fine; keep. | — |
| 547–548 | "In summary, the two halves of this note localize the same difficulty from two sides without touching it." | `The two halves of this note isolate the same difficulty from two sides without resolving it.` |
| 556 | "The questions we would most like to ask you. First, … Second, … Third, … Fourth, …" (mechanical list) | `These are the questions we would most like to ask you.` + `\begin{enumerate}\item[(1)] whether the semilocal Sonin space … \item[(2)] whether the moment structure … \item[(3)] whether a differential operator … \item[(4)] whether the direction $s_0$ … \end{enumerate}` (same text, without "First/Second/Third/Fourth") |
| 46–57 (abstract) | "First, … Second, … Third, …" | Optional: `(i) … (ii) … (iii) …`, or paragraphs without ordinals. Tolerable in an abstract. |
| global | Mixes "I" (introduction) / "we" (body) and "your Theorem 1", "your (87)", "your \S6", "your Lemma D.1" in the body. A coherent choice for a letter-article that the recipient will understand; the text does not circulate well to third parties without editing. | — |
| 96–97 | "It is known with a certificate for $T\le0.8$ \cite{Zhu2026} and …" | `A certificate exists for $T\le0.8$ \cite{Zhu2026}, and …` |

## Verified and correct (no change needed)
Constants: $C_0=-5.3722$; $C_0+\log2+\pi/2=-3.108$; $w(2)=2.1045$; cota de baja frecuencia $0.0975$; $-1.209$; $C_B\to1.6399$; $\beta_1=0.510$ ($\lambda=1$), $0.128/0.272/0.448$ ($\lambda=\frac12$); $\|\Pi_T\|$: $0.4901$, $1.6740$; $c(T,k)$: $0.486/0.094/0.281$, $\dim E_k=14/48/58$; $1-\|A_S\|^2=5\cdot10^{-6}$; $94\%$ / $6\%$ consistent; $0.0147$ unified. Proofs: thm:nogo (contacts, $O(w)$), thm:A, thm:B (closed form of $\Phi_\tau$ and $C_0\delta(\tau)$), prop:prime, thm:schur (complete the square), thm:phase ($\varphi'$ = comb), prop:AS, thm:gap(i)–(ii), thm:L2 ($\beta_j$), consistency of (Cprime) with $\mathrm{comb}_2$ and with $v_{2^k}$. Citations of CC: (83)–(90), Thm 1, Thm 6.11 ($c|\widehat g(0)|^2$), Thm 3.6/Cor 3.8/Rem 3.9 ($0.14043$), Fact 6.5, (127): all correct. No mention or suggestion of RH.

## Verdict
Correct first the five A rows (the identity in the proof of thm:84 is an error the recipient would see; the upper bound of thm:schur is false if $\lambda_S<0$) and the first two B rows (figures of obs:s0; double $\tau$ in §5), plus the undefined symbols and the two untitled bibitems.
With that done, the mathematical content is correct in everything that could be checked, and the labels are honest.
Ready to send after these corrections; not before.
