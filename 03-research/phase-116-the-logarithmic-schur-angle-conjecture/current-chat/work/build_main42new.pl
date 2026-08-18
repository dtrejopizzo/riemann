use strict;
use warnings;
use utf8;
use open qw(:std :encoding(UTF-8));

my $base = '/Users/davidalejandrotrejopizzo/Library/Containers/net.whatsapp.WhatsApp/Data/tmp/documents';
my $project = '/Users/davidalejandrotrejopizzo/Documents/riemann/04-papers/42-arithmetic-lefschetz-programme';
my $workspace = '/Users/davidalejandrotrejopizzo/Documents/Codex/2026-08-12/referenced-chatgpt-conversation-this-is-an';

my %source = (
  main => "$base/504EDEB1-C752-4E5B-9C2B-31423916163F/main.tex",
  'row-a-deligne-nuclear' => "$base/D99D77F1-D421-4499-BAA8-F4A4533690E2/row-a-deligne-nuclear.tex",
  'row-a-intrinsic-periodic' => "$project/row-a-intrinsic-periodic.tex",
  'row-b-witt-lefschetz' => "$base/678772C1-4EEA-4880-8E12-2BF1B6672AFD/row-b-witt-lefschetz.tex",
  'row-c-nuclear-lefschetz' => "$base/0317F2FA-47ED-4FC0-AEDC-6CD7BE40149C/row-c-nuclear-lefschetz.tex",
  'row-d-local-analysis' => "$base/5180E7EF-B76E-42E6-BC98-E3514D2C5B2D/row-d-local-analysis.tex",
  supplement => "$workspace/work/row-d-gamma-tate-paper.tex",
);

sub slurp {
  my ($path) = @_;
  open my $fh, '<', $path or die "Cannot read $path: $!";
  local $/;
  my $text = <$fh>;
  close $fh;
  return $text;
}

sub expand_inputs {
  my ($text) = @_;
  while ($text =~ /\\input\{([^}]+)\}/) {
    my $name = $1;
    die "Unknown input source: $name" unless exists $source{$name};
    my $replacement = "\n% BEGIN INLINED SOURCE: $name\n"
      . slurp($source{$name})
      . "\n% END INLINED SOURCE: $name\n";
    substr($text, $-[0], $+[0] - $-[0], $replacement);
  }
  return $text;
}

my $main = slurp($source{main});

my $abstract = <<'LATEX';
\begin{abstract}
We construct the first three ingredients of Weil's argument over $\Z$ in an
explicit periodic--cohomological--nuclear setting.  The noncollapsed
spherical square carries intrinsic periodic section cohomology, a
coefficient-one determinant and derived prime contact.  Witt Frobenius gives
a faithful multiplicative correspondence family whose dynamic contact is
$[\Z\xrightarrow{\Phi_n(1)}\Z]$ and has degree $\Lambda(n)$.  Its monoidal
realization in Meyer's Poisson quotient yields the complete nuclear
Lefschetz character, including the finite, polar and archimedean terms.

For the fourth ingredient we identify the primitive operator and prove
full-space positivity for every $0<T\leq\log2$.  We then construct the
finite logarithmic Gamma--Tate amplitude, the conservative moving-Tate
terminal, a positive unreset Gamma storage form and the exact correlated
rational leakage at every arithmetic threshold.  These identities reduce
global propagation to one explicit generalized Schur inequality.  We also
give a source-defined, unit-constant Gamma--Tate domination estimate which
would suffice for that inequality.  Its uniform validity is not proved here.
Thus rows (a)--(c), the certified initial range of row (d), and the stated
boundary identities are established; the global Hodge inequality and the
Riemann Hypothesis remain open.
\end{abstract}
LATEX

$main =~ s{\\begin\{abstract\}.*?\\end\{abstract\}}{$abstract}s
  or die "Could not replace abstract";

my $rowd_start = index($main, '\\section{Row (d): the exact geometric gate}');
my $proposal_start = index($main, '\\subsection{A new proposal for row (d)}');
my $exec_start = index($main, '\\section*{Executable companion}');
die "Could not locate row-(d) splice points"
  if $rowd_start < 0 || $proposal_start < 0 || $exec_start < 0;

my $prefix = substr($main, 0, $proposal_start);
my $suffix = substr($main, $exec_start);
my $supplement = slurp($source{supplement});

my $assembled = $prefix
  . "\n% BEGIN CLEAN GAMMA--FOURIER--TATE ROW (d)\n"
  . $supplement
  . "\n% END CLEAN GAMMA--FOURIER--TATE ROW (d)\n\n"
  . $suffix;

$assembled = expand_inputs($assembled);

my $old_geometric_claim = <<'OLD';
Row (d) must come from a Riemann--Roch theorem on the square, or not at all.
OLD
my $new_geometric_claim = <<'NEW';
It cannot be obtained by reading the desired sign back from the explicit
formula.  A proof must instead come either from an independent geometric
index theorem or from a source-defined positive factorization whose
construction does not use that sign.
NEW
$assembled =~ s/\Q$old_geometric_claim\E/$new_geometric_claim/
  or die "Could not update the row-(d) methodological claim";

$assembled =~ s/\QThe remaining task is listed in
\S\ref{sec:remaining}.\E/The fourth-row construction and its final open inequality are stated in
Section~\\ref{ss:gammafouriertate}./
  or die "Could not update the introductory row-(d) reference";

$assembled =~ s/\Q[Exact row-(d) trilemma]\E/[Exact geometric row-(d) trilemma]/
  or die "Could not update the trilemma title";
$assembled =~ s/\QA non-circular proof of row~(d) must either:\E/A non-circular geometric proof of row~(d) must either:/
  or die "Could not update the trilemma scope";

my $new_status = <<'NEW';
Uniform arithmetic return summability, the finite logarithmic boundary
amplitude, the conservative moving-Tate terminal, the positive unreset
Gamma storage and the exact rational-leakage Gram are proved.  The uniform
joint Schur estimate and threshold propagation remain open; the spectral
sign is not assumed.
NEW
$assembled =~ s{Uniform arithmetic return summability is proved,\s*
but the corrected joint Schur estimate and threshold propagation remain\s*
open; the spectral sign is not assumed\.}{$new_status}s
  or die "Could not update the row-(d) status table";

my $old_open_paragraph = <<'OLD';
Such a
theorem would close row~(d).  The present results isolate it but do not prove
it.
OLD
my $new_open_paragraph = <<'NEW';
Such a theorem would close row~(d).  The source construction below gives a
second non-circular route to the same primitive inequality: an independently
positive Gamma--Euler--Tate factorization.  Neither route is completed here.
NEW
$assembled =~ s/\Q$old_open_paragraph\E/$new_open_paragraph/
  or die "Could not update the transition to the analytic construction";

$assembled =~ s{This is the precise point at which\s+the present argument stops\.}{This is the precise point at which the local-analysis argument stops; the
Gamma--Fourier--Tate source construction below begins from this capacity
defect.}s
  or die "Could not distinguish the local row-(d) stopping point";

$assembled =~ s/\r\n?/\n/g;
$assembled =~ s/[ \t]+\n/\n/g;
$assembled =~ s/\n{4,}/\n\n\n/g;

my $output = "$workspace/outputs/main42new.tex";
open my $out, '>', $output or die "Cannot write $output: $!";
print {$out} $assembled;
close $out;

print "$output\n";
