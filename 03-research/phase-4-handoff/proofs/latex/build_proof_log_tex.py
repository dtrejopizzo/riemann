#!/usr/bin/env python3
"""
Convert the running proof-log bitacora (00-PROOF-LOG.md) into a typeset LaTeX
document (PROOF-LOG.tex).  No pandoc dependency: a self-contained converter that
handles headers, bold, inline code, blockquotes, lists, fenced code blocks,
inline $...$ math, and a comprehensive unicode -> LaTeX map.  Unknown non-ASCII
is replaced by '?' so the output always compiles.
"""
import re, sys

SRC = "../00-PROOF-LOG.md"
OUT = "PROOF-LOG.tex"

# ---- unicode -> LaTeX (works in text via \ensuremath) ----
U = {
 'λ':r'\ensuremath{\lambda}', 'Λ':r'\ensuremath{\Lambda}', 'ζ':r'\ensuremath{\zeta}',
 'ω':r'\ensuremath{\omega}', 'Ω':r'\ensuremath{\Omega}', 'β':r'\ensuremath{\beta}',
 'γ':r'\ensuremath{\gamma}', 'Γ':r'\ensuremath{\Gamma}', 'σ':r'\ensuremath{\sigma}',
 'Σ':r'\ensuremath{\Sigma}', 'π':r'\ensuremath{\pi}', 'Π':r'\ensuremath{\Pi}',
 'μ':r'\ensuremath{\mu}', 'δ':r'\ensuremath{\delta}', 'Δ':r'\ensuremath{\Delta}',
 'ε':r'\ensuremath{\varepsilon}', 'φ':r'\ensuremath{\varphi}', 'Φ':r'\ensuremath{\Phi}',
 'ψ':r'\ensuremath{\psi}', 'Ψ':r'\ensuremath{\Psi}', 'τ':r'\ensuremath{\tau}',
 'θ':r'\ensuremath{\theta}', 'Θ':r'\ensuremath{\Theta}', 'κ':r'\ensuremath{\kappa}',
 'ρ':r'\ensuremath{\rho}', 'α':r'\ensuremath{\alpha}', 'χ':r'\ensuremath{\chi}',
 'ξ':r'\ensuremath{\xi}', 'Ξ':r'\ensuremath{\Xi}', 'ν':r'\ensuremath{\nu}',
 'η':r'\ensuremath{\eta}', 'ℓ':r'\ensuremath{\ell}',
 '→':r'\ensuremath{\to}', '⟹':r'\ensuremath{\Rightarrow}', '⟸':r'\ensuremath{\Leftarrow}',
 '⟺':r'\ensuremath{\iff}', '↔':r'\ensuremath{\leftrightarrow}', '⤳':r'\ensuremath{\rightsquigarrow}',
 '≤':r'\ensuremath{\le}', '≥':r'\ensuremath{\ge}', '≈':r'\ensuremath{\approx}',
 '≠':r'\ensuremath{\ne}', '≡':r'\ensuremath{\equiv}', '×':r'\ensuremath{\times}',
 '÷':r'\ensuremath{\div}', '±':r'\ensuremath{\pm}', '∓':r'\ensuremath{\mp}',
 '²':r'\ensuremath{^2}', '³':r'\ensuremath{^3}', '⁴':r'\ensuremath{^4}', '⁵':r'\ensuremath{^5}',
 '∞':r'\ensuremath{\infty}', '∑':r'\ensuremath{\sum}', '∫':r'\ensuremath{\int}',
 '√':r'\ensuremath{\surd}', '∈':r'\ensuremath{\in}', '∉':r'\ensuremath{\notin}',
 '⊂':r'\ensuremath{\subset}', '⊆':r'\ensuremath{\subseteq}', '⊊':r'\ensuremath{\subsetneq}',
 '⊥':r'\ensuremath{\perp}', '·':r'\ensuremath{\cdot}', '∘':r'\ensuremath{\circ}',
 '∧':r'\ensuremath{\wedge}', '∨':r'\ensuremath{\vee}', '¬':r'\ensuremath{\neg}',
 '∀':r'\ensuremath{\forall}', '∃':r'\ensuremath{\exists}', '⪰':r'\ensuremath{\succeq}',
 '⪯':r'\ensuremath{\preceq}', '≍':r'\ensuremath{\asymp}', '≪':r'\ensuremath{\ll}',
 '≫':r'\ensuremath{\gg}', '∼':r'\ensuremath{\sim}', '∝':r'\ensuremath{\propto}',
 '½':r'\ensuremath{\tfrac12}', '¼':r'\ensuremath{\tfrac14}', '¾':r'\ensuremath{\tfrac34}',
 'ℤ':r'\ensuremath{\mathbb{Z}}', 'ℚ':r'\ensuremath{\mathbb{Q}}', 'ℝ':r'\ensuremath{\mathbb{R}}',
 'ℂ':r'\ensuremath{\mathbb{C}}', '𝔽':r'\ensuremath{\mathbb{F}}', '𝒯':r'\ensuremath{\mathcal{T}}',
 '𝒮':r'\ensuremath{\mathcal{S}}', '𝓛':r'\ensuremath{\mathcal{L}}', '𝔱':r'\ensuremath{\mathfrak{t}}',
 '𝔞':r'\ensuremath{\mathfrak{a}}', '𝔭':r'\ensuremath{\mathfrak{p}}', '𝔮':r'\ensuremath{\mathfrak{q}}',
 '⟨':r'\ensuremath{\langle}', '⟩':r'\ensuremath{\rangle}', '〈':r'\ensuremath{\langle}',
 '〉':r'\ensuremath{\rangle}', '◆':r'$\blacklozenge$', '✅':r'[OK]', '❌':r'[X]',
 '⚑':r'[flag]', '⚑⚑':r'[flag]', '⭐':r'$\star$', '—':'---', '–':'--',
 '’':"'", '‘':"'", '“':'``', '”':"''", '…':r'\ldots', '°':r'\ensuremath{^\circ}',
 '∂':r'\ensuremath{\partial}', '∅':r'\ensuremath{\emptyset}', '⊕':r'\ensuremath{\oplus}',
 '⊗':r'\ensuremath{\otimes}', '∩':r'\ensuremath{\cap}', '∪':r'\ensuremath{\cup}',
 '⌊':r'\ensuremath{\lfloor}', '⌋':r'\ensuremath{\rfloor}', '√':r'\ensuremath{\sqrt{}}',
 '⊥':r'\ensuremath{\perp}', '∆':r'\ensuremath{\Delta}', '′':r"\ensuremath{'}",
 'ç':r'\c{c}', 'é':r'\\\'e', 'í':r'\\\'i', 'ó':r'\\\'o', 'á':r'\\\'a', 'ú':r'\\\'u',
 'ñ':r'\~n', 'ü':r'\"u', ' ':' ',
}

SPECIAL = {'&':r'\&','%':r'\%','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}','$':r'\$'}

# ASCII transliteration for fenced code blocks (box-drawing, arrows, etc.)
CODEMAP = {'─':'-','│':'|','┌':'+','┐':'+','└':'+','┘':'+','├':'+','┤':'+','┬':'+',
 '┴':'+','┼':'+','►':'>','◄':'<','▼':'v','▲':'^','→':'->','⟹':'=>','⟸':'<=','⟺':'<=>',
 '≤':'<=','≥':'>=','≈':'~=','≠':'!=','×':'x','·':'.','∞':'inf','√':'sqrt','²':'^2','³':'^3',
 '—':'-','–':'-','’':"'",'‘':"'",'“':'"','”':'"','…':'...','⊥':'_|_','∈':'in','⪰':'>=',
 'λ':'lambda','Λ':'Lambda','ζ':'zeta','ω':'omega','β':'beta','γ':'gamma','σ':'sigma',
 'π':'pi','μ':'mu','δ':'delta','ε':'eps','Φ':'Phi','τ':'tau','κ':'kappa','ρ':'rho',
 'α':'alpha','ξ':'xi','Ξ':'Xi','Δ':'Delta','ℤ':'Z','𝔽':'F','𝒯':'T','½':'1/2','∑':'sum'}
def codetrans(s):
    return ''.join(CODEMAP.get(ch, ch if ord(ch)<128 else '?') for ch in s)

def esc_text(s):
    # escape LaTeX specials in plain text (NOT $, handled separately; NOT backslash from our subs)
    out=[]
    for ch in s:
        if ch in SPECIAL: out.append(SPECIAL[ch])
        elif ch=='\\': out.append(r'\textbackslash{}')
        else: out.append(ch)
    return ''.join(out)

def uni(s):
    out=[]
    for ch in s:
        if ord(ch)<128: out.append(ch)
        elif ch in U: out.append(U[ch])
        else: out.append('?')
    return ''.join(out)

def inline(s):
    # protect $...$ math, **bold**, `code`; escape the rest; restore.
    toks=[]
    def stash(m, kind):
        toks.append((kind,m.group(1))); return f"\x00{len(toks)-1}\x00"
    s=re.sub(r'\$([^$]+)\$', lambda m: stash(m,'math'), s)
    s=re.sub(r'`([^`]+)`', lambda m: stash(m,'code'), s)
    s=re.sub(r'\*\*([^*]+)\*\*', lambda m: stash(m,'bold'), s)
    s=re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', s)   # links -> text
    s=esc_text(s)
    # restore tokens
    def rep(m):
        kind,val=toks[int(m.group(1))]
        if kind=='math': return '$'+uni(val)+'$'
        if kind=='code': return r'\texttt{'+esc_text(uni(val))+'}'
        if kind=='bold': return r'\textbf{'+esc_text(uni(val))+'}'
        return val
    # iterative restore: nested tokens (e.g. code/math inside bold) need multiple passes
    for _ in range(6):
        if '\x00' not in s: break
        s=re.sub('\x00(\d+)\x00', rep, s)
    s=s.replace('\x00','')   # safety: drop any unresolved placeholder
    return uni(s)

def convert(md):
    lines=md.split('\n'); out=[]; i=0
    inlist=False; inquote=False
    def close_list():
        nonlocal inlist
        if inlist: out.append(r'\end{itemize}'); inlist=False
    def close_quote():
        nonlocal inquote
        if inquote: out.append(r'\end{quote}'); inquote=False
    while i<len(lines):
        ln=lines[i].rstrip()
        # fenced code block
        if ln.strip().startswith('```'):
            close_list(); close_quote()
            out.append(r'\begin{lstlisting}')
            i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'):
                out.append(codetrans(lines[i])); i+=1
            out.append(r'\end{lstlisting}'); i+=1; continue
        if not ln.strip():
            close_list(); close_quote(); out.append(''); i+=1; continue
        # headers
        m=re.match(r'^(#{1,4})\s+(.*)$', ln)
        if m:
            close_list(); close_quote()
            lvl=len(m.group(1)); txt=inline(m.group(2))
            cmd={1:r'\section*',2:r'\subsection*',3:r'\subsubsection*',4:r'\paragraph*'}[lvl]
            out.append(f'{cmd}{{{txt}}}'); i+=1; continue
        # blockquote
        if ln.lstrip().startswith('>'):
            close_list()
            if not inquote: out.append(r'\begin{quote}\itshape'); inquote=True
            out.append(inline(re.sub(r'^\s*>\s?','',ln))+r'\par'); i+=1; continue
        else:
            close_quote()
        # list item
        m=re.match(r'^(\s*)[-*]\s+(.*)$', ln)
        if m:
            if not inlist: out.append(r'\begin{itemize}'); inlist=True
            out.append(r'\item '+inline(m.group(2))); i+=1; continue
        else:
            close_list()
        # horizontal rule
        if re.match(r'^---+$', ln):
            out.append(r'\medskip\hrule\medskip'); i+=1; continue
        # day-entry bold header line: **2026... Day N ...** -> subsection
        m=re.match(r'^\*\*(20\d\d.*?Day[^*]*)\*\*\s*(.*)$', ln)
        if m:
            out.append(r'\subsection*{'+inline(m.group(1))+'}')
            rest=m.group(2).strip()
            if rest: out.append(inline(rest)+r'\par')
            i+=1; continue
        # normal paragraph line
        out.append(inline(ln)+r'\par'); i+=1
    close_list(); close_quote()
    return '\n'.join(out)

if __name__=='__main__':
    md=open(SRC,encoding='utf-8').read()
    body=convert(md)
    doc=r'''\documentclass[10pt]{article}
\usepackage[a4paper,margin=0.9in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{listings}
\usepackage{microtype}
\usepackage[hidelinks]{hyperref}
\lstset{basicstyle=\ttfamily\scriptsize,breaklines=true,frame=single,
  showstringspaces=false,columns=fullflexible,keepspaces=true,
  extendedchars=true,literate={-}{-}1}
\setlength{\parindent}{0pt}\setlength{\parskip}{4pt}
\title{\textbf{The Riemann Program --- Proof Log (Bit\'acora)}\\[4pt]
\large A continuous research diary, Days 0--46}
\author{David Alejandro Trejo Pizzo}
\date{June 2026}
\begin{document}
\maketitle
\noindent\emph{Faithful LaTeX rendering of the running \texttt{00-PROOF-LOG.md}.
Auto-generated by \texttt{build\_proof\_log\_tex.py}; informal inline notation is
preserved as written.}\par\medskip
\hrule\medskip
'''+body+r'''
\end{document}
'''
    open(OUT,'w',encoding='utf-8').write(doc)
    print(f"wrote {OUT}: {len(doc)} chars, {doc.count(chr(10))} lines")
