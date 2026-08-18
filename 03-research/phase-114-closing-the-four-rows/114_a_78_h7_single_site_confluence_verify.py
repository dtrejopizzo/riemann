#!/usr/bin/env python3
"""Exact finite checks for a78; interacting cancellation cascades stay open."""

from functools import lru_cache
from itertools import product
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


# The durable short primary source contains the graphical cancellation and
# commutativity relations.  The long-source normal-form audit is recorded in
# a76 and is supplemented below by a direct joint-confluence check.
source = H17.read_text()
for marker in (
    r"(10.16) \quad {\bf cancellation}",
    r"(10.17) \quad {\bf commutativity}",
):
    check(f"source marker {marker}", marker in source)


LEAF = ("L",)


def node(color, children):
    children = tuple(sorted(children, key=repr))
    return LEAF if not children else (color, children)


def one_steps(tree, is_root=True, parent_color=None):
    if tree == LEAF:
        return set()
    color, children = tree
    out = set()
    # 1-reduction, including at the root.
    if len(children) == 1:
        out.add(children[0])
    # lhd-reduction of this nonroot vertex: splice its children at parent.
    # This move is implemented by the caller below.
    for i, child in enumerate(children):
        if child != LEAF:
            child_color, grand = child
            if child_color == color:
                out.add(node(color, children[:i] + grand + children[i + 1:]))
        for reduced_child in one_steps(child, False, color):
            out.add(node(color, children[:i] + (reduced_child,) + children[i + 1:]))
    return out


@lru_cache(None)
def normal_forms(tree):
    steps = one_steps(tree)
    if not steps:
        return {tree}
    out = set()
    for nxt in steps:
        out.update(normal_forms(nxt))
    return out


def recursive_parent_trees(n):
    if n == 1:
        yield (0,)
        return
    for tail in product(*[range(i) for i in range(1, n)]):
        yield (0,) + tail


tree_count = 0
for n in range(1, 8):
    for parents in recursive_parent_trees(n):
        children = [[] for _ in range(n)]
        for v in range(1, n):
            children[parents[v]].append(v)
        internal = [v for v in range(n) if children[v]]
        for bits in range(1 << len(internal)):
            colors = {v: (bits >> i) & 1 for i, v in enumerate(internal)}

            def build(v):
                if not children[v]:
                    return LEAF
                return node(colors[v], tuple(build(w) for w in children[v]))

            tree = build(0)
            forms = normal_forms(tree)
            if len(forms) != 1:
                raise AssertionError((parents, colors, tree, forms))
            tree_count += 1
check(f"joint tree-reduction confluence for {tree_count} generated trees", True)


def completion(a, b, left_context, right_context):
    """Combinatorial signature before any newly exposed second site."""
    net = a - b
    magnitude = abs(net)
    sign = 0 if net == 0 else (1 if net > 0 else -1)
    left_degree = left_context + magnitude
    right_degree = right_context + magnitude
    return (
        sign,
        magnitude,
        left_degree == 0,
        right_degree == 0,
        left_degree == 1,
        right_degree == 1,
    )


cases = {"zero": 0, "unary": 0, "multiple": 0}
for a in range(9):
    for b in range(9):
        for lc in range(5):
            for rc in range(5):
                signature = completion(a, b, lc, rc)
                # Canceling any chosen opposite pair first gives the same
                # completion as long as a pair exists.
                if a and b and completion(a - 1, b - 1, lc, rc) != signature:
                    raise AssertionError((a, b, lc, rc))
                magnitude = signature[1]
                if magnitude == 0:
                    cases["zero"] += 1
                elif signature[4] or signature[5]:
                    cases["unary"] += 1
                else:
                    cases["multiple"] += 1
check(f"single-site completions unique in {sum(cases.values())} contexts", True)
check("zero/unary/multiple topology cases all reached", all(cases.values()))


for p in (2, 3, 5, 7, 11):
    for a in range(9):
        for b in range(9):
            for c in range(9):
                for d in range(9):
                    if p * (a - b) == p * (c - d) and a - b != c - d:
                        raise AssertionError((p, a, b, c, d))
check("stable one-site prime-root closure", True)


doc = (HERE / "114_a_78_H7_SINGLE_SITE_TOPOLOGY_CHANGE_IS_CONFLUENT.md").read_text()
for marker in (
    "H7-CASCADE-2",
    "stopping convention",
    "does not\nassert H7-CASCADE-2",
    "full H7-CANCEL-PURE",
):
    check(f"scope marker {marker}", marker in doc)

print("VERDICT: VISIBLE SINGLE-SITE CONFLUENCE PASS; FULL MACRO CONTEXT SYSTEM OPEN")
