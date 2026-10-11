"""Gera uma página HTML interativa com a árvore de elementos de um XSD.

Uso:
    python scripts/xsd_to_html.py [caminho_do_xsd] [ficheiro_html] [elemento_inicial]

Exemplo:
    python scripts/xsd_to_html.py schemas/SAFTPT1.04_01.xsd docs/saft_structure.html

A página tem:
    - árvore recolhível (clique num bloco para abrir/fechar)
    - botões para abrir até um nível ou abrir/fechar tudo
    - pesquisa por nome de campo (abre o caminho até cada resultado)
    - indicação de obrigatório / opcional / repetível
    - tipo de cada campo e as suas regras (tamanho máximo, valores possíveis...)
"""

import html
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

XS = "{http://www.w3.org/2001/XMLSchema}"


def local(name: str | None) -> str:
    """Remove o prefixo de namespace (ex.: 'xs:string' -> 'string')."""
    return (name or "").split(":")[-1]


class Schema:
    def __init__(self, path: str):
        root = ET.parse(path).getroot()
        self.elements = {e.get("name"): e for e in root.findall(f"{XS}element")}
        self.ctypes = {t.get("name"): t for t in root.findall(f"{XS}complexType")}
        self.stypes = {t.get("name"): t for t in root.findall(f"{XS}simpleType")}
        self.count = 0

    # ---------- leitura do esquema ----------

    def children(self, node):
        """Elementos filhos diretos, atravessando sequence/choice/extension."""
        for child in node:
            tag = child.tag.replace(XS, "")
            if tag == "element":
                yield child
            elif tag in ("sequence", "choice", "all", "complexContent", "simpleContent"):
                yield from self.children(child)
            elif tag == "extension":
                base = self.ctypes.get(local(child.get("base")))
                if base is not None:
                    yield from self.children(base)
                yield from self.children(child)

    def rules(self, simple_type, depth=0) -> list[str]:
        """Regras de um tipo simples: base, tamanho, valores possíveis..."""
        if simple_type is None or depth > 5:
            return []
        restriction = simple_type.find(f"{XS}restriction")
        if restriction is None:
            return []
        base = local(restriction.get("base"))
        out = self.rules(self.stypes.get(base), depth + 1) if base in self.stypes else [base]
        enums = []
        for facet in restriction:
            tag = facet.tag.replace(XS, "")
            value = facet.get("value")
            if tag == "enumeration":
                enums.append(value)
            elif tag != "annotation" and value is not None:
                out.append(f"{tag}={value}")
        if enums:
            shown = ", ".join(enums[:12]) + (" …" if len(enums) > 12 else "")
            out.append(f"valores: {shown}")
        return out

    def documentation(self, node) -> str:
        doc = node.find(f"{XS}annotation/{XS}documentation")
        return " ".join(doc.text.split()) if doc is not None and doc.text else ""

    def find(self, target: str):
        if target in self.elements:
            return self.elements[target]
        for definition in list(self.elements.values()) + list(self.ctypes.values()):
            for el in definition.iter(f"{XS}element"):
                if el.get("name") == target or local(el.get("ref")) == target:
                    return el
        return None

    # ---------- geração do HTML ----------

    def render(self, el, depth=0, path=frozenset()) -> str:
        node = self.elements.get(local(el.get("ref")), el) if el.get("ref") else el
        name = node.get("name") or "?"
        self.count += 1

        lo = el.get("minOccurs", "1")
        hi = el.get("maxOccurs", "1")
        badges = []
        badges.append(
            '<span class="b req">obrigatório</span>'
            if lo != "0"
            else '<span class="b opt">opcional</span>'
        )
        if hi == "unbounded" or (hi.isdigit() and int(hi) > 1):
            badges.append('<span class="b rep">repete</span>')

        type_name = local(node.get("type"))
        inline_ct = node.find(f"{XS}complexType")
        definition = inline_ct if inline_ct is not None else self.ctypes.get(type_name)

        kids = []
        if definition is not None and name not in path:
            kids = [self.render(c, depth + 1, path | {name}) for c in self.children(definition)]

        info = []
        if not kids:
            simple = node.find(f"{XS}simpleType")
            if simple is None:
                simple = self.stypes.get(type_name)
            if type_name:
                info.append(f'<span class="type">{html.escape(type_name)}</span>')
            rules = self.rules(simple)
            if rules:
                info.append(f'<span class="rules">{html.escape(" · ".join(rules))}</span>')
        doc = self.documentation(node)
        if doc:
            info.append(f'<span class="doc">{html.escape(doc)}</span>')

        head = (
            f'<span class="name">{html.escape(name)}</span> {"".join(badges)}'
            f"{'<div class=info>' + ''.join(info) + '</div>' if info else ''}"
        )
        data = f'class="node" data-name="{html.escape(name.lower())}" data-depth="{depth}"'

        if kids:
            return (
                f"<details {data}><summary>{head}</summary>"
                f'<div class="kids">{"".join(kids)}</div></details>'
            )
        return f'<div {data}><div class="leaf">{head}</div></div>'


PAGE = """<!DOCTYPE html>
<html lang="pt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root {{
  --bg: #ffffff; --fg: #1f2328; --muted: #656d76; --line: #d0d7de; --hover: #f6f8fa;
  --req: #1a7f37; --req-bg: #dafbe1; --opt: #656d76; --opt-bg: #eaeef2;
  --rep: #8250df; --rep-bg: #fbefff; --hit: #fff8c5; --accent: #0969da;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #0d1117; --fg: #e6edf3; --muted: #8d96a0; --line: #30363d; --hover: #161b22;
    --req: #3fb950; --req-bg: #12261e; --opt: #8d96a0; --opt-bg: #21262d;
    --rep: #bc8cff; --rep-bg: #271d3a; --hit: #3a3000; --accent: #4493f8;
  }}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--fg);
  font: 14px/1.45 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
header {{ position: sticky; top: 0; background: var(--bg); border-bottom: 1px solid var(--line);
  padding: 12px 20px; z-index: 1; }}
h1 {{ font-size: 18px; margin: 0 0 4px; }}
.sub {{ color: var(--muted); font-size: 12px; margin-bottom: 10px; }}
.bar {{ display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }}
input {{ flex: 1 1 220px; padding: 6px 10px; border: 1px solid var(--line); border-radius: 6px;
  background: var(--bg); color: var(--fg); font: inherit; }}
button {{ padding: 6px 10px; border: 1px solid var(--line); border-radius: 6px; background: var(--hover);
  color: var(--fg); font: inherit; cursor: pointer; }}
button:hover {{ border-color: var(--accent); }}
#status {{ color: var(--muted); font-size: 12px; }}
main {{ padding: 12px 20px 40px; overflow-x: auto; }}
details > summary {{ list-style: none; cursor: pointer; }}
details > summary::-webkit-details-marker {{ display: none; }}
details > summary::before {{ content: "▸"; display: inline-block; width: 14px; color: var(--muted); }}
details[open] > summary::before {{ content: "▾"; }}
summary, .leaf {{ padding: 3px 6px; border-radius: 4px; }}
summary:hover, .leaf:hover {{ background: var(--hover); }}
.leaf {{ padding-left: 20px; }}
.kids {{ margin-left: 10px; padding-left: 10px; border-left: 1px solid var(--line); }}
.name {{ font-weight: 600; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
.b {{ font-size: 11px; padding: 1px 6px; border-radius: 10px; margin-left: 4px; }}
.req {{ color: var(--req); background: var(--req-bg); }}
.opt {{ color: var(--opt); background: var(--opt-bg); }}
.rep {{ color: var(--rep); background: var(--rep-bg); }}
.info {{ margin: 2px 0 2px 2px; font-size: 12px; color: var(--muted); }}
.info span + span::before {{ content: " — "; }}
.type {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
.hit > summary, .hit > .leaf {{ background: var(--hit); }}
[hidden] {{ display: none !important; }}
</style>
</head>
<body>
<header>
  <h1>{title}</h1>
  <div class="sub">{count} elementos · ficheiro: {source}</div>
  <div class="bar">
    <input id="q" type="search" placeholder="Pesquisar campo (ex.: InvoiceNo, CustomerTaxID)…">
    <button data-level="1">Nível 1</button>
    <button data-level="2">Nível 2</button>
    <button data-level="3">Nível 3</button>
    <button id="all">Abrir tudo</button>
    <button id="none">Fechar tudo</button>
    <span id="status"></span>
  </div>
</header>
<main>{tree}</main>
<script>
const nodes = [...document.querySelectorAll('.node')];
const details = [...document.querySelectorAll('details')];
const q = document.getElementById('q');
const status = document.getElementById('status');

function openTo(level) {{
  details.forEach(d => d.open = Number(d.dataset.depth) < level);
}}
document.querySelectorAll('[data-level]').forEach(b =>
  b.addEventListener('click', () => openTo(Number(b.dataset.level))));
document.getElementById('all').onclick = () => details.forEach(d => d.open = true);
document.getElementById('none').onclick = () => details.forEach(d => d.open = false);

q.addEventListener('input', () => {{
  const term = q.value.trim().toLowerCase();
  nodes.forEach(n => {{ n.classList.remove('hit'); n.hidden = term !== ''; }});
  if (!term) {{ status.textContent = ''; return; }}
  let count = 0;
  nodes.forEach(n => {{
    if (!n.dataset.name.includes(term)) return;
    count++;
    n.classList.add('hit');
    n.hidden = false;
    n.querySelectorAll('.node').forEach(d => d.hidden = false);
    let p = n.parentElement.closest('.node');
    while (p) {{
      p.hidden = false;
      if (p.tagName === 'DETAILS') p.open = true;
      p = p.parentElement.closest('.node');
    }}
  }});
  status.textContent = count + ' resultado(s)';
}});

openTo(2);
</script>
</body>
</html>
"""


def main():
    xsd_path = sys.argv[1] if len(sys.argv) > 1 else "schemas/SAFTPT1.04_01.xsd"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "docs/saft_structure.html"
    start = sys.argv[3] if len(sys.argv) > 3 else "AuditFile"

    schema = Schema(xsd_path)
    start_el = schema.find(start)
    if start_el is None:
        sys.exit(f"Elemento '{start}' não encontrado no XSD.")

    tree = schema.render(start_el)
    page = PAGE.format(
        title=html.escape(f"Estrutura {start} — {Path(xsd_path).name}"),
        source=html.escape(xsd_path),
        count=schema.count,
        tree=tree,
    )
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text(page, encoding="utf-8")
    print(f"Página gerada: {out_path} ({schema.count} elementos)")


if __name__ == "__main__":
    main()
